import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(23, GPIO.IN)
GPIO.setup(11, GPIO.OUT)

while True:
        if (GPIO.input(23) == False):
                GPIO.output(11,0)
                print " Led on pin 11 is now OFF "
        else:
                GPIO.output(11,1)
                print " Led on pin 11 is now ON "

time.sleep(1) 
