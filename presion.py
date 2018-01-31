#!/usr/bin/python

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def presion (PiPin):

	measurement = 0

#	GPIO.setup(21,GPIO.OUT)
	GPIO.setup(PiPin, GPIO.OUT)
	GPIO.output(PiPin, GPIO.LOW)
	time.sleep(1)

	GPIO.setup(PiPin, GPIO.IN)

	while (GPIO.input(PiPin) == GPIO.LOW):
		measurement += 1

	return measurement

while(1):
	print presion(18)
