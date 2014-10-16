import Adafruit_BBIO.GPIO as GPIO
import time
import subprocess
import sys

GPIO.setup("P8_10", GPIO.OUT)
GPIO.setup("P8_14", GPIO.OUT)
GPIO.setup("P8_18", GPIO.OUT)

while 1:
	cmdstr = 'wget -O /dev/null http://speedtest.wdc01.softlayer.com/downloads/test10.zip 2>&1 | grep -o \'\([0-9.]\+ [KM]B/s\)\' | grep -o \'\([0-9.]\+\)\''
	#print cmdstr
	cmd = subprocess.Popen(cmdstr, shell=True, stdout=subprocess.PIPE)
	lines = [line.strip() for line in open('speed.txt')]
	#print lines
	#f = open('out.txt'), 'w')
	speed = [line.strip() for line in cmd.stdout]
	print lines[0] #need a file with a number in it for this to work
	print speed[0]
	percentChange = ( ( float(speed[0]) - float(lines[0])) / float(lines[0])) * 100 ##Calculate the new percent changed

	print percentChange
	#Now we've compared. Let's write the most recent speed to our file.
	f = open('speed.txt', 'w')
	f.write (speed[0])
	f.close()
	
	if percentChange < -5:
		GPIO.output("P8_10", GPIO.HIGH)
		GPIO.output("P8_14", GPIO.LOW)
		GPIO.output("P8_18",GPIO.LOW)
	else: 
		if percentChange in range(0,-6,-1):
			GPIO.output("P8_10", GPIO.LOW)
			GPIO.output("P8_14", GPIO.HIGH)
			GPIO.output("P8_18",GPIO.LOW)
		else:
			GPIO.output("P8_10", GPIO.LOw)
			GPIO.output("P8_14", GPIO.LOW)
			GPIO.output("P8_18",GPIO.HIGH)
