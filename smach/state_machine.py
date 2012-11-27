#!/usr/bin/env python

import roslib; roslib.load_manifest('phri_ros')
import rospy
import smach
import smach_ros

from std_msgs.msg import Int8
from std_msgs.msg import Empty
from std_msgs.msg import Bool
from phri_ros.msg import *

import scriptsPy

script = scriptsPy.base

"""Eye behavior:  put button flash at start of each state.  Driving in AttnGet:  publish an Int8 on /drive, 0=stop, 1=go.  Web form can send yes, no, teleop.  DoNothing/Teleop state:  go there if get Empty msg on /teleop while in AttnGet or from successful finish or from stop in any state other than AttnGet and Intro (after Goodbye).  Get out of Teleop state with a yes msg (button or teleop).  /leds takes special message I'll define (see, eg, visualization_msgs/Marker examples) -- actually an Int8, but enumerated -- RedFlash, GreenFlash, WifiReadingWeak, etc.  Email Mike S when have led message defined.
"""

class Teleop(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['yes', ''])
        self.sub = rospy.Subscriber("/buttons", Bool, self.buttonsCB)
        self.script_sub = rospy.Subscriber("/script", Int8, self.scriptCB)
        self.pub = rospy.Publisher("/speech", SpeechMsg)		
        self.button = ''

    def buttonsCB(self, msg):
        if msg.data:
            self.button = 'yes'

    def scriptCB(self, msg):
        global script
        if msg.data == 0:
            script = scriptsPy.base
            self.pub.publish(SpeechMsg('', 'Base Case'))
        elif msg.data == 1:
            script = scriptsPy.auth_deep
            self.pub.publish(SpeechMsg('', 'Authoritative Deep'))
        elif msg.data == 2:
            script = scriptsPy.auth_shal
            self.pub.publish(SpeechMsg('', 'Authoritative Shallow'))
        elif msg.data == 3:
            script = scriptsPy.like_deep
            self.pub.publish(SpeechMsg('', 'Likeable Deep'))
        elif msg.data == 4:
            script = scriptsPy.like_shal
            self.pub.publish(SpeechMsg('', 'Likeable Shallow'))
    
    def execute(self, userdata):
        self.button = ''
        while not self.button and not rospy.is_shutdown():
            rospy.sleep(1.0)
        return self.button

class AttentionGet(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['yes', 'no', 'teleop', ''], output_keys=['byeType'])
        self.sub = rospy.Subscriber("/buttons", Bool, self.buttonsCB)
        self.tsub = rospy.Subscriber("/teleop", Empty, self.teleopCB)
        self.button = ''
        self.teleop = False

        #self.dpub = rospy.Publisher("/drive", Int8)
        self.pub = rospy.Publisher("/speech", SpeechMsg)
    
    def buttonsCB(self, msg):
        if msg.data:
            self.button = 'yes'
        else:
            self.button = 'no'
    
    def teleopCB(self, msg):
        self.teleop = True

    def execute(self, userdata):
        rospy.loginfo('Executing state ATTENTIONGET')
        userdata.byeType = 'AGLoop'
        self.teleop = False
        self.button = ''
        #self.dpub.publish(Int8(1))
        # do something with the lights?
        ctr = 1
        while (not self.button) and (not self.teleop) and (not rospy.is_shutdown()):
            if ctr % 10 == 0:
                self.pub.publish(SpeechMsg(script['attention'][0], script['attention'][1]))
            rospy.sleep(1.0)
            ctr = ctr + 1
        #self.dpub.publish(Int8(0))
        if self.teleop:
            return 'teleop'
        else:
            return self.button

class Introduction(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['yes', 'no', ''], output_keys=['byeType', 'number'])
        self.sub = rospy.Subscriber("/buttons", Bool, self.buttonsCB)
        self.button = ''
        self.spub = rospy.Publisher("/speech", SpeechMsg)
        self.lpub = rospy.Publisher("/leds", LEDMsg)

    def buttonsCB(self, msg):
        if msg.data:
            self.button = 'yes'
        else:
            self.button = 'no'

    def execute(self, userdata):
        rospy.loginfo('Executing state INTRODUCTION')
        userdata.byeType = 'AGLoop'
        userdata.number = 1
        self.button = ''
        self.lpub.publish(LEDMsg(LEDMsg.GREENFLASH))
        self.spub.publish(SpeechMsg(script['introduction'][0], script['introduction'][1]))
        while not self.button and not rospy.is_shutdown():
            rospy.sleep(1.0)
        return self.button

class Goodbye(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['AGLoop', 'exit', 'complete'], input_keys=['byeType'])
        self.spub = rospy.Publisher("/speech", SpeechMsg)
        self.lpub = rospy.Publisher("/leds", LEDMsg)

    def execute(self, userdata):
        rospy.loginfo('Executing state GOODBYE')
        if userdata.byeType == 'complete':
            self.spub.publish(SpeechMsg(script['conclusion'][0], script['conclusion'][1]))
        else:
            self.lpub.publish(LEDMsg(LEDMsg.REDFLASH))
            self.spub.publish(SpeechMsg(script['redButton'][0], script['redButton'][1]))
        rospy.sleep(2.0)  # really should wait for done_speaking??
        return userdata.byeType

class Acknowledge(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['yes', 'no', 'done', ''], input_keys=['number'], output_keys=['number', 'byeType'])
        self.sub = rospy.Subscriber("/buttons", Bool, self.buttonsCB)
        self.button = ''
        self.spub = rospy.Publisher("/speech", SpeechMsg)
        self.lpub = rospy.Publisher("/leds", LEDMsg)
        self.wifiVals = [LEDMsg.WIFIHIGH, LEDMsg.WIFINORMAL, LEDMsg.WIFIWEAK, LEDMsg.WIFINORMAL]

    def buttonsCB(self, msg):
        if msg.data:
            self.button = 'yes'
        else:
            self.button = 'no'

    def execute(self, userdata):
        nstr = str(userdata.number)
        rospy.loginfo('Executing state ACKNOWLEDGE ' + nstr)
        userdata.byeType = 'exit'
        self.button = ''
        self.lpub.publish(LEDMsg(LEDMsg.GREENFLASH))
        self.lpub.publish(LEDMsg(self.wifiVals[userdata.number - 1]))
        self.spub.publish(SpeechMsg(script['acknowledge'+nstr][0], script['acknowledge'+nstr][1]))
        while not self.button and not rospy.is_shutdown():
            rospy.sleep(1.0)
        if userdata.number == 4 and not rospy.is_shutdown():
            userdata.byeType = 'complete'
            return 'done'
        else:
            return self.button

class Transit(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['yes', 'no', ''], input_keys=['number'], output_keys=['number', 'byeType'])
        self.sub = rospy.Subscriber("/buttons", Bool, self.buttonsCB)
        self.button = ''
        self.spub = rospy.Publisher("/speech", SpeechMsg)
        self.lpub = rospy.Publisher("/leds", LEDMsg)

    def buttonsCB(self, msg):
        if msg.data:
            self.button = 'yes'
        else:
            self.button = 'no'

    def execute(self, userdata):
        nstr = str(userdata.number)
        rospy.loginfo('Executing state TRANSIT ' + nstr)
        userdata.byeType = 'exit'

        self.button = ''
        self.lpub.publish(LEDMsg(LEDMsg.GREENFLASH))
        self.spub.publish(SpeechMsg(script['transit'+nstr][0], script['transit'+nstr][1]))
        while not self.button and not rospy.is_shutdown():
            rospy.sleep(1.0)
        userdata.number = userdata.number + 1
        return self.button 


def main():
    rospy.init_node('smach_state_machine')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['done'])

    # Open the container
    with sm:
        # Add states to the container
        smach.StateMachine.add('TELEOP', Teleop(), transitions={'yes':'ATTENTIONGET', '':'done'})
        smach.StateMachine.add('ATTENTIONGET', AttentionGet(), transitions={'yes':'INTRODUCTION', 'no':'GOODBYE', 'teleop':'TELEOP', '':'done'})
        smach.StateMachine.add('INTRODUCTION', Introduction(), transitions={'yes':'ACKNOWLEDGE', 'no':'GOODBYE', '':'done'})
        smach.StateMachine.add('GOODBYE', Goodbye(), transitions={'AGLoop':'ATTENTIONGET', 'exit':'TELEOP', 'complete':'TELEOP'})
        smach.StateMachine.add('ACKNOWLEDGE', Acknowledge(), transitions={'yes':'TRANSIT', 'no':'GOODBYE', 'done':'GOODBYE', '':'done'})
        smach.StateMachine.add('TRANSIT', Transit(), transitions={'yes':'ACKNOWLEDGE', 'no':'GOODBYE', '':'done'})

    # Create and start the introspection server
    sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
    sis.start()

    # Execute SMACH plan
    while not rospy.is_shutdown():
        outcome = sm.execute()
    sis.stop()


if __name__ == '__main__':
    main()
