from time import sleep
import RPi.GPIO as GPIO

DIR4 = 5
STEP4 = 6
SPR = 200
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR4, GPIO.OUT)
GPIO.setup(STEP4, GPIO.OUT)
step_count = 53
step_count = int(step_count)
delay = .005/32

GPIO.output(DIR4, GPIO.LOW)
for x in range(step_count):
    GPIO.output(STEP4, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP4, GPIO.LOW)
    sleep(0.01)
