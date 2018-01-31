import time

while 1:

	tempfile = open("/sys/bus/w1/devices/28-0000053091f4/w1_slave")
	thetext = tempfile.read()
	tempfile.close()
	tempdata = thetext.split ("\n")[1].split(" ") [9]
	temperatura = float(tempdata[2:])
	temperatura = temperatura / 1000
	print temperatura

	time.sleep(2)
