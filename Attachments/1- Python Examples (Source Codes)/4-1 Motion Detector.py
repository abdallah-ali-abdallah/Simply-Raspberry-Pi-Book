import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(23, GPIO.IN)


while True:
        if (GPIO.input(23) == True):
                pritn " Motion Detected "
        else:
                pritn " There is No Motion "
        time.sleep(1)
