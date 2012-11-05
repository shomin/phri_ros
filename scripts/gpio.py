#!/usr/bin/python
import roslib; roslib.load_manifest("phri_ros")
import rospy

import wiringpi as wp

from std_msgs.msg import ColorRGBA
from std_msgs.msg import Empty
import os

class Gpio:
	def __init__(self):
		rospy.init_node('gpio')
		rospy.loginfo("Starting GPIO ROS Driver")

                os.system('/home/pi/phri_ros/scripts/setup_gpio')
                self.io = wp.GPIO(wp.GPIO.WPI_MODE_SYS)

                self.pwm_range = 50

                self.button_Hz = 20.0
                self.button_offtime = rospy.Duration(1.0)

                rospy.loginfo("Starting Soft PWM Timers")
                wp.softPwmCreate(17, 0, self.pwm_range)
                wp.softPwmCreate(18, 0, self.pwm_range)
                wp.softPwmCreate(21, 0, self.pwm_range)
                wp.softPwmCreate(12, 0, self.pwm_range)
                wp.softPwmCreate(23, 0, self.pwm_range)
                wp.softPwmCreate(24, 0, self.pwm_range)

		self.leye_sub = rospy.Subscriber("left_eye", ColorRGBA, self.leye)
		self.reye_sub = rospy.Subscriber("right_eye", ColorRGBA, self.reye)

		self.ybut_pub = rospy.Publisher("yes", Empty)
		self.nbut_pub = rospy.Publisher("no", Empty)

                rospy.loginfo("Starting Button Query Timers")		
		rospy.Timer(rospy.Duration(1.0/self.button_Hz), self.check_buttons)
		
		self.yes_time = rospy.Time()
		self.no_time = rospy.Time()

	def leye(self, msg):
		wp.softPwmWrite(17, int(msg.r*self.pwm_range))
		wp.softPwmWrite(18, int(msg.g*self.pwm_range))
		wp.softPwmWrite(21, int(msg.b*self.pwm_range))

	def reye(self, msg):
		wp.softPwmWrite(22, int(msg.r*self.pwm_range))
		wp.softPwmWrite(23, int(msg.g*self.pwm_range))
		wp.softPwmWrite(24, int(msg.b*self.pwm_range))

	def check_buttons(self, event):
		if self.io.digitalRead(15)==0:
			if(event.current_real - self.yes_time) > self.button_offtime:
				self.ybut_pub.publish(Empty())
				self.yes_time = event.current_real
		if self.io.digitalRead(14)==0:
			if(event.current_real - self.no_time) > self.button_offtime:
				self.nbut_pub.publish(Empty())
				self.no_time = event.current_real


if __name__ == '__main__':
	ros_gpio = Gpio()
	rospy.spin()


#io.pinMode(17,io.OUTPUT)
#io.digitalWrite(17,io.HIGH)
#io.digitalWrite(17,io.LOW)

