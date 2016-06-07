import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(23, GPIO.IN)

while True:
        if (GPIO.input(23)):
                print ('Input is HIGH (1)')
        else:
                print ('Input is LOW (0)')
        time.sleep(.5)