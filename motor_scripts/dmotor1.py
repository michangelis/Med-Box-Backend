from time import sleep
import RPi.GPIO as GPIO

DIR1 = 2       # Direction GPIO Pin
STEP1 = 3      # Step GPIO Pin
SPR = 200
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR1, GPIO.OUT)
GPIO.setup(STEP1, GPIO.OUT)
step_count = 53
step_count = int(step_count)
delay = .005/32

GPIO.output(DIR1, GPIO.LOW)
for x in range(step_count):
    GPIO.output(STEP1, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP1, GPIO.LOW)
    sleep(0.01)
