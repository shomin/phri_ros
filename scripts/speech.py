#!/usr/bin/python
import roslib; roslib.load_manifest("phri_ros")
import rospy
import os
import string
import sys
from std_msgs.msg import Empty
from phri_ros.msg import SpeechMsg

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
		self.sub = rospy.Subscriber("speech", SpeechMsg, self.cb)
		self.pub = rospy.Publisher("done_speaking", Empty)
		self.tts = Festival()
	def cb(self, msg):
		if(msg.voice == "clear"):
			os.system("clear")
		else:
			os.system("clear")
			self.screenprint(msg.screen)
			self.tts.say(msg.voice)
			self.pub.publish(Empty())
	def screenprint(self, data):
		# We want the text to look like "Press the {red, fg=white, bg=red} button."  Assumes that any whitespace is a single space.  The string to be colored cannot contain any commas.  There must be a spaces before and after the {} section unless it is at one end of the string.  There must be spaces after the commas in the coloring arguments.

		# Step through and insert linebreaks, ignoring parameters
		data = self.addLinebreaks(data, 18)
		# Break apart based on curly braces and print with colors
		while data:
			a = data.partition("{")
			sys.stdout.write(a[0])
			sys.stdout.flush()
			if a[1]:
				b = a[2]
				c = b.partition("}")
				self.cprintParse(c[0])
				sys.stdout.flush()
				data = c[2]
			else:
				data = a[2]
	def addLinebreaks(self, data, lineLength):
		newData = ''
		ctr = 0
		inMacro = False
		inMacroString = False
		for word in data.split():
			n = len(word)
			if inMacro and not inMacroString:
				if word[-1] == "}":
					inMacro = False			
				newData = newData + word
				continue
			if word[0] == "{":
				inMacro = True
				inMacroString = True
				n = n - 1
			if inMacroString and word[-1] == ",":
				inMacroString = False
				n = n - 1
			if ctr + n > lineLength:
				newData = newData + "\n"
				ctr = 0
			newData = newData + " " + word
			ctr = ctr + n + 1
		return newData
	def cprintParse(self, s):
		lst = s.split(",")
		val = lst[0]
		fg = 'white'
		bg = 'black'
		mod = 'none'
		for item in lst[1:]:
			if item[:3] == 'fg=':
				fg = item[3:]
			if item[:3] == 'bg=':
				bg = item[3:]
			if item[:4] == 'mod=':
				mod = item[4:]
		self.cprint(val, fg, bg, mod)
	def cprint(self, s, fg='white', bg='black',mod='none'):
		bgc = {'red':41,'green':42,'yellow':43,'blue':44,'magenta':45,'cyan':46,'grey':47,'black':40}
		fgc = {'red':91,'green':92,'yellow':93,'blue':94,'magenta':95,'cyan':96,'grey':90,'black':30,'white':97}
		modc = {'bold':1,'grey':2,'und':4,'flip':7,'strike':9,'none':3}
		sys.stdout.write('\033['+str(fgc[fg])+'m'+'\033['+str(bgc[bg])+'m'+'\033['+str(modc[mod])+'m'+s+'\033[0m')


if __name__ == '__main__':
	os.system("clear")
	lt = Speech()
	rospy.spin()
