#!/usr/bin/python
import roslib; roslib.load_manifest("phri_ros")
import rospy
from serial import *
from geometry_msgs.msg import Twist
from std_msgs.msg import UInt8

class HriBot:
	def __init__(self):
		rospy.init_node('phri_tester')
		rospy.loginfo("PHRI Tester Node")
		
		port_name = rospy.get_param('~port','/dev/ttyACM0')
		baud = int(rospy.get_param('~baud','9600'))
		self.port = Serial(port_name, baud, timeout=2.5)

		self.port.timeout = 0.01
		rospy.sleep(0.1)
		rospy.loginfo("Connected on %s at %d baud" % (port_name,baud) )

		rospy.on_shutdown(self.close_ser)
		
		self.twistsub = rospy.Subscriber("cmd_vel", Twist, self.twistCallback)
		self.larmsub = rospy.Subscriber("larm", UInt8, self.larmCallback)
		self.rarmsub = rospy.Subscriber("rarm", UInt8, self.rarmCallback)
		self.headsub = rospy.Subscriber("head", UInt8, self.headCallback)
		

	def larmCallback(self,msg):
		s = bytearray('xH')
		s.append(msg.data)
		self.port.flush()
		self.port.write(s)
				
	def rarmCallback(self,msg):
		s = bytearray('xI')
		s.append(msg.data)
		self.port.flush()
		self.port.write(s)

	def headCallback(self,msg):
		s = bytearray('xJ')
		s.append(msg.data)
		self.port.flush()
		self.port.write(s)

		
	def twistCallback(self,msg):
		a = int(round( (100*msg.linear.x) + (100*msg.angular.z) ))
		b = int(round( (100*msg.linear.x) - (100*msg.angular.z) ))
		if(a>=0):
			sa = bytearray('xA')
		else:
			sa = bytearray('xa')
			a = -a
		if(b>=0):
			sb = bytearray('xB')
		else:
			sb = bytearray('xb')
			b = -b
			
		sa.append(a)
		sb.append(b)			
		self.port.flush()
		self.port.write(sa)
		self.port.write(sb)
		'''el = port.readline()
		print el'''
		
	def close_ser(self):
		rospy.loginfo('Closing Port')
		self.port.close();


if __name__ == '__main__':
    try:
        hribot = HriBot()
        rospy.spin()

    except rospy.ROSInterruptException: 
        pass
