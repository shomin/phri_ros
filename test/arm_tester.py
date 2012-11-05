#!/usr/bin/env python
import roslib; roslib.load_manifest('phri')
import rospy
import math

from std_msgs.msg import UInt8

if __name__ == '__main__':
	rospy.init_node('arm_tester')
	i8 = UInt8()

	ros_timer = rospy.Rate(50)
	pub = rospy.Publisher('head', UInt8)

	try:	
		while not rospy.is_shutdown():
			i8 = round(50*(1+math.sin( rospy.get_time() / .3)))
			pub.publish(i8)
			ros_timer.sleep()

	except rospy.ROSInterruptException:
		rospy.logerr( 'Ros Interrupted, JS Tester Shutting Down')
