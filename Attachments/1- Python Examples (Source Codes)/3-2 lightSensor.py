import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(23, GPIO.IN)
GPIO.setup(11, GPIO.OUT)

while True:
        if (GPIO.input(23) == False):
                GPIO.output(11,0)
        else:
                GPIO.output(11,1)
