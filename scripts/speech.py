#!/usr/bin/python
import roslib; roslib.load_manifest("phri_ros")
import rospy
import os
from std_msgs.msg import String

BIN="/usr/bin/festival"
class Festival(object):
	def __init__(self):
		self.p = os.popen("%s --pipe" %BIN, "w")
	def eval(self,scm):
		self.p.write(scm + "\n")
		self.p.flush()
	def say(self,text):
		text = text.replace('"','')
		self.eval('(SayText "%s")' %str(text))

class Speech:
	def __init__(self):
		rospy.init_node('pyspeech')
		rospy.loginfo("Starting Speech")
		self.sub = rospy.Subscriber("speech", String, self.cb)
		self.tts = Festival()
	def cb(self, msg):
		if(msg.data == "clear"):
			os.system("clear")
		else:
			os.system("clear")
			print(msg.data)
			self.tts.say(msg.data)


if __name__ == '__main__':
	os.system("clear")
	lt = Speech()
	rospy.spin()
