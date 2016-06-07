import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

p = GPIO.PWM(11, 50)
p.start(5)

p.ChangeDutyCycle(10)
time.sleep(3)
p.ChangeDutyCycle(40)
time.sleep(3)
p.ChangeDutyCycle(80)
time.sleep(3)
p.ChangeDutyCycle(100)
time.sleep(3)

p.stop()
GPIO.cleanup()
