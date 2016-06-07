import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
while True:
	GPIO.output(11,False)
	print "Led on Pin 11 is now OFF (output = zero volt)"
	time.sleep(1)

	GPIO.output(11,True)
	print "Led on Pin 11 is now ON (output = 3.3 volt)"
	time.sleep(1)
