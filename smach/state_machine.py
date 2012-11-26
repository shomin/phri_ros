#!/usr/bin/env python

import roslib; roslib.load_manifest('phri_ros')
import rospy
import smach
import smach_ros

class Exit(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['stop'])

    def execute(self, userdata):
        rospy.loginfo('Executing state EXIT')
        # thank the participant -- script dependent
        return 'stop'

class AttentionGet(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['yes', 'no'])
        self.ysub = rospy.Subscriber("yes", Empty, self.yesCB)
        self.nsub = rospy.Subscriber("yes", Empty, self.noCB)

    def yesCB(self, msg):
        return 'yes'

    def noCB(self, msg):
        return 'no'

    def execute(self, userdata):
        rospy.loginfo('Executing state ATTENTIONGET')
        while True:
            # wander and cry for help

class Introduction(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['yes', 'no'])
        self.ysub = rospy.Subscriber("yes", Empty, self.yesCB)
        self.nsub = rospy.Subscriber("yes", Empty, self.noCB)

    def yesCB(self, msg):
        return 'yes'

    def noCB(self, msg):
        return 'no'

    def execute(self, userdata):
        rospy.loginfo('Executing state INTRODUCTION')
        # introduce self/purpose

class TaskOne(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['yes', 'no'])
        self.ysub = rospy.Subscriber("yes", Empty, self.yesCB)
        self.nsub = rospy.Subscriber("yes", Empty, self.noCB)

    def yesCB(self, msg):
        return 'yes'

    def noCB(self, msg):
        return 'no'

    def execute(self, userdata):
        rospy.loginfo('Executing state TASKONE')
        # request first destination

class TaskTwo(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['yes', 'no'])
        self.ysub = rospy.Subscriber("yes", Empty, self.yesCB)
        self.nsub = rospy.Subscriber("yes", Empty, self.noCB)

    def yesCB(self, msg):
        return 'yes'

    def noCB(self, msg):
        return 'no'

    def execute(self, userdata):
        rospy.loginfo('Executing state TASKTWO')
        # request second destination

class TaskThree(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['yes', 'no'])
        self.ysub = rospy.Subscriber("yes", Empty, self.yesCB)
        self.nsub = rospy.Subscriber("yes", Empty, self.noCB)

    def yesCB(self, msg):
        return 'yes'

    def noCB(self, msg):
        return 'no'

    def execute(self, userdata):
        rospy.loginfo('Executing state TASKTHREE')
        # request third destination

class TaskLift(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['yes', 'no'])
        self.ysub = rospy.Subscriber("yes", Empty, self.yesCB)
        self.nsub = rospy.Subscriber("yes", Empty, self.noCB)

    def yesCB(self, msg):
        return 'yes'

    def noCB(self, msg):
        return 'no'

    def execute(self, userdata):
        rospy.loginfo('Executing state TASKLIFT')
        # ask to be lifted

class Conclude(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['finished'])

    def execute(self, userdata):
        rospy.loginfo('Executing state CONCLUDE')
        # final thanks
        return 'finished'

def main():
    rospy.init_node('smach_state_machine')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['done'])

    # Open the container
    with sm:
        # Add states to the container
        smach.StateMachine.add('EXIT', Exit(), 
                               transitions={'stopped':'done'})
        smach.StateMachine.add('ATTENTIONGET', AttentionGet(), transitions={'yes':'INTRODUCTION', 'no':'EXIT'})
        smach.StateMachine.add('INTRODUCTION', Introduction(), transitions={'yes':'TASKONE', 'no':'EXIT'})
        smach.StateMachine.add('TASKONE', TaskOne(), transitions={'yes':'TASKTWO', 'no':'EXIT'})
        smach.StateMachine.add('TASKTWO', TaskTwo(), transitions={'yes':'TASKTHREE', 'no':'EXIT'})
        smach.StateMachine.add('TASKTHREE', TaskThree(), transitions={'yes':'TASKLIFT', 'no':'EXIT'})
        smach.StateMachine.add('TASKLIFT', TaskLift(), transitions={'yes':'CONCLUDE', 'no':'EXIT'})
        smach.StateMachine.add('CONCLUDE', Conclude(), transitions={'finished':'done'})

    # Execute SMACH plan
    outcome = sm.execute()


if __name__ == '__main__':
    main()
