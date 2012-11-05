#!/usr/bin/python
import RPi.GPIO as GPIO
import time

'''
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
print "Setting pin 12 high"
GPIO.output(12, GPIO.HIGH)
print "Waiting 2 seconds"
time.sleep(2)
print "Setting pin 12 low"
GPIO.output(12, GPIO.LOW)
print "Waiting 2 seconds"
time.sleep(2)
print "Setting pin 12 high"
GPIO.output(12, GPIO.HIGH)
'''

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
#GPIO.setup(24, GPIO.OUT)

GPIO.output(14, GPIO.LOW)
GPIO.output(15, GPIO.LOW)
GPIO.output(18, GPIO.LOW)
GPIO.output(23, GPIO.LOW)
#GPIO.output(24, GPIO.LOW)
time.sleep(0.5)

dt = 0.05

for i in xrange(1,10):
    GPIO.output(14, GPIO.HIGH)
    time.sleep(dt)
    GPIO.output(15, GPIO.HIGH)
    time.sleep(dt)
    GPIO.output(18, GPIO.HIGH)
    time.sleep(dt)
    GPIO.output(23, GPIO.HIGH)
    time.sleep(dt)
    #GPIO.output(24, GPIO.HIGH)
    #time.sleep(dt)

    GPIO.output(14, GPIO.LOW)
    time.sleep(dt)
    GPIO.output(15, GPIO.LOW)
    time.sleep(dt)
    GPIO.output(18, GPIO.LOW)
    time.sleep(dt)
    GPIO.output(23, GPIO.LOW)
    time.sleep(dt)
    #GPIO.output(24, GPIO.LOW)
    #time.sleep(dt)


