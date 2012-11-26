#!/usr/bin/python
import roslib; roslib.load_manifest("phri_ros")
import rospy

import wiringpi as wp

from std_msgs.msg import ColorRGBA
from std_msgs.msg import Empty
from std_msgs.msg import Float32
from std_msgs.msg import Bool
from geometry_msgs.msg import Twist
import os

os_setup = '''#! /bin/sh 
gpio export 17 out
gpio export 18 out
gpio export 21 out

gpio export 22 out
gpio export 23 out
gpio export 24 out
gpio export 10 out
gpio export 9 out
gpio export 25 out

gpio export 11 out
gpio export 8 out
gpio export 7 out

gpio export 14 in
gpio -g mode 14 up

gpio export 15 in
gpio -g mode 15 up'''


class Gpio:
	def __init__(self):
		rospy.init_node('gpio')
		rospy.loginfo("Starting GPIO ROS Driver")
                #os.system('/home/pi/phri_ros/scripts/setup_gpio')
		os.system(os_setup)

                self.io = wp.GPIO(wp.GPIO.WPI_MODE_SYS)

                self.pwm_range = 50
                self.button_Hz = 20.0
                self.button_offtime = rospy.Duration(1.0)

                rospy.loginfo("Starting Soft PWM Timers")
                wp.softPwmCreate(17, 0, self.pwm_range)
                wp.softPwmCreate(18, 0, self.pwm_range)
                wp.softPwmCreate(21, 0, self.pwm_range)

                wp.softPwmCreate(22, 0, self.pwm_range)
		self.io.digitalWrite(23,1)
		self.io.digitalWrite(24,0)

                wp.softPwmCreate(25, 0, self.pwm_range)
		self.io.digitalWrite(10,0)
		self.io.digitalWrite(9,0)

                wp.softPwmCreate(11, 0, self.pwm_range)
                wp.softPwmCreate(8, 0, self.pwm_range)
                wp.softPwmCreate(7, 0, self.pwm_range)

		self.leye_sub = rospy.Subscriber("left_eye", ColorRGBA, self.leye)
		self.reye_sub = rospy.Subscriber("right_eye", ColorRGBA, self.reye)

		self.l_motor_sub = rospy.Subscriber("left_motor", Float32, self.lmotor)
		self.r_motor_sub = rospy.Subscriber("right_motor", Float32, self.rmotor)

		self.twistsub = rospy.Subscriber("cmd_vel", Twist, self.twistCallback)

		self.button_pub = rospy.Publisher("buttons", Bool)


                rospy.loginfo("Starting Button Query Timers")		
		rospy.Timer(rospy.Duration(1.0/self.button_Hz), self.check_buttons)
		
		self.yes_time = rospy.Time()
		self.no_time = rospy.Time()

	def leye(self, msg):
		wp.softPwmWrite(11, int(msg.r*self.pwm_range))
		wp.softPwmWrite(7, int(msg.g*self.pwm_range))
		wp.softPwmWrite(8, int(msg.b*self.pwm_range))

	def reye(self, msg):
		wp.softPwmWrite(17, int(msg.r*self.pwm_range))
		wp.softPwmWrite(21, int(msg.g*self.pwm_range))
		wp.softPwmWrite(18, int(msg.b*self.pwm_range))

	def lmotor(self, msg):
		if msg.data>=0.0:
			self.io.digitalWrite(23,0)
			self.io.digitalWrite(24,1)
			wp.softPwmWrite(22, int(msg.data*self.pwm_range))
		else:
			self.io.digitalWrite(23,1)
			self.io.digitalWrite(24,0)
			wp.softPwmWrite(22, int(-msg.data*self.pwm_range))

	def rmotor(self, msg):
		if msg.data>=0.0:
			self.io.digitalWrite(10,0)
			self.io.digitalWrite(9,1)
			wp.softPwmWrite(25, int(msg.data*self.pwm_range))
		else:
			self.io.digitalWrite(10,1)
			self.io.digitalWrite(9,0)
			wp.softPwmWrite(25, int(-msg.data*self.pwm_range))

	def check_buttons(self, event):
		if self.io.digitalRead(15)==0:
			if(event.current_real - self.yes_time) > self.button_offtime:
				self.ybut_pub.publish(Empty())
				self.button_pub.publish(Bool(True))
				self.yes_time = event.current_real
		if self.io.digitalRead(14)==0:
			if(event.current_real - self.no_time) > self.button_offtime:
				self.button_pub.publish(Bool(False))
				self.no_time = event.current_real

	def twistCallback(self,msg):
		l = msg.linear.x - msg.angular.z
		r = msg.linear.x + msg.angular.z
		self.lmotor(Float32(l))
		self.rmotor(Float32(r))




if __name__ == '__main__':
	ros_gpio = Gpio()
	rospy.spin()


#io.pinMode(17,io.OUTPUT)
#io.digitalWrite(17,io.HIGH)
#io.digitalWrite(17,io.LOW)

