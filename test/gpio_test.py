#!/usr/bin/python

import wiringpi as wp
import time
import os

os.system('/home/pi/phri_ros/scripts/setup_gpio')

io = wp.GPIO(wp.GPIO.WPI_MODE_SYS)


io.pinMode(17,io.OUTPUT)


io.digitalWrite(17,io.HIGH)
time.sleep(2)
io.digitalWrite(17,io.LOW)

import pdb; pdb.set_trace()


