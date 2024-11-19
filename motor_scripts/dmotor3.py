from time import sleep
import RPi.GPIO as GPIO

DIR3 = 10     # Direction GPIO Pin
STEP3 = 9     # Step GPIO Pin
SPR = 200
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR3, GPIO.OUT)
GPIO.setup(STEP3, GPIO.OUT)
step_count = 53
step_count = int(step_count)
delay = .005/32

GPIO.output(DIR3, GPIO.LOW)
for x in range(step_count):
    GPIO.output(STEP3, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP3, GPIO.LOW)
    sleep(0.01)
