#!/usr/bin/env python
import roslib; roslib.load_manifest('phri_ros')
import rospy
from math import sin

from std_msgs.msg import ColorRGBA

def talker():
    lpub = rospy.Publisher('left_eye', ColorRGBA)
    rpub = rospy.Publisher('right_eye', ColorRGBA)
    rospy.init_node('led_tester')

    while not rospy.is_shutdown():
        t = rospy.get_rostime().to_sec()

        k = 4.0
        msg = ColorRGBA()
        msg.r = ( 1.0 + sin(0.0 + (k*t)) ) / 2.0
        msg.g = ( 1.0 + sin(2.1 + (k*t)) ) / 2.0
        msg.b = ( 1.0 + sin(4.2 + (k*t)) ) / 2.0

        pub.publish(msg)
        rospy.sleep(.1)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
