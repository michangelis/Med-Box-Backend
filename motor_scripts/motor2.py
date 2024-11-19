from time import sleep
import RPi.GPIO as GPIO

DIR2 = 17     # Direction GPIO Pin
STEP2 = 27     # Step GPIO Pin
SPR = 200
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(STEP2, GPIO.OUT)
step_count = 53
step_count = int(step_count)
delay = .005/32

GPIO.output(DIR2, GPIO.HIGH)
for x in range(step_count):
    GPIO.output(STEP2, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP2, GPIO.LOW)
    sleep(0.01)
