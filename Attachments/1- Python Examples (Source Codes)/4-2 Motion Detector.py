import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(23, GPIO.IN)
GPIO.setup(11, GPIO.OUT)

while True:
        if (GPIO.input(23) == True):
                GPIO.output(11,1)
                print " Motion Detected, Now Turning On Led "
                time.sleep(3)
 
        else:
                GPIO.output(11,0)
                print " There is No motion "

time.sleep(1) 
