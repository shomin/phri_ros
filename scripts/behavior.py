#!/usr/bin/python
import roslib; roslib.load_manifest("phri_ros")
import rospy
from std_msgs.msg import Int8
from std_msgs.msg import ColorRGBA
from phri_ros.msg import LEDMsg
from geometry_msgs.msg import Twist
from math import cos
from math import pi


class Drive:
	def __init__(self):
		self.sub = rospy.Subscriber("drive", Int8, self.drive_cb)
		self.pub = rospy.Publisher("cmd_vel", Twist)
		self.driving = False
		self.drive_Hz = 1.0
		self.cmds = self.get_cmd()
		rospy.Timer(rospy.Duration(1.0/self.drive_Hz), self.drive_loop)

	def drive_cb(self, msg):
		if msg.data == 1:
			self.driving = True
		else:
			self.driving = False
			
	def drive_loop(self,event):
		if self.driving:
			vel = Twist()
			cmd = self.cmds.next()
			vel.linear.x = cmd[0]
			vel.angular.z = cmd[1]
			self.pub.publish(vel)

	def get_cmd(self):
		while True:
			yield [0.9, 0.0]
			yield [0.7, 0.4]
			yield [0.9, 0.0]
			yield [0.7,- 0.4]

class Leds:
	def __init__(self):
		self.sub = rospy.Subscriber("leds", LEDMsg, self.led_cb)
		self.lpub = rospy.Publisher("left_eye", ColorRGBA)
		self.rpub = rospy.Publisher("right_eye", ColorRGBA)
		self.default = ColorRGBA(0.0, 1.0, 1.0, 0.0)
		self.flash_delay = 2.0

	def led_cb(self, msg):
		if msg.code == LEDMsg.REDFLASH:
			self.flash(ColorRGBA(1.0, 0.0, 0.0, 0.0))
		elif msg.code == LEDMsg.GREENFLASH:
			self.flash(ColorRGBA(0.0, 1.0, 0.0, 0.0))
		elif msg.code == LEDMsg.WIFILOW:
			self.chirp()
		elif msg.code == LEDMsg.WIFINORMAL:
			self.chirp(t_f = 5.0, freq=[1.0, 0.1], amp=[0.5, 0.5, 1.0])			
		elif msg.code == LEDMsg.WIFIHIGH:
			self.chirp(t_f = 3.0, freq=[0.5, 0.1], amp=[0.0, 1.0, 1.0])			
			
	def flash(self, color):
		self.pub(color)
		rospy.sleep(self.flash_delay)
		self.pub(self.default)

	def chirp(self, t_f = 8.0, freq = [2.0,0.1],	amp = [1.0, 0.0, 1.0], phase = [0.0, 0.0, pi]):
		loop_hz = 20
		t0 = rospy.get_rostime()
		t = rospy.get_rostime() - t0
		while t.to_sec() < t_f:
			t = rospy.get_rostime() - t0
			n = t.to_sec() / t_f;
			f = (freq[1]*n) + (freq[0]*(1-n))
			r = amp[0]*(0.5*(1.0 + cos( ((2*pi*t.to_sec())*f) + phase[0])))
			g = amp[1]*(0.5*(1.0 + cos( ((2*pi*t.to_sec())*f) + phase[1])))
			b = amp[2]*(0.5*(1.0 + cos( ((2*pi*t.to_sec())*f) + phase[2])))			

			self.pub(ColorRGBA(r,g,b,0.0))
			rospy.sleep(1.0/loop_hz)
			
			
		self.pub(self.default)
			
		

	def pub(self, color):
		self.lpub.publish(color)
		self.rpub.publish(color)


if __name__ == '__main__':
	rospy.init_node('behavior')
	rospy.loginfo("Starting Behavior Node")
	driver = Drive()
	leds = Leds()

	rospy.spin()
