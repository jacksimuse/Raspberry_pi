import RPi.GPIO as GPIO
import time

ledPin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT) # 

if __name__ == '__main__':
    while True:
        GPIO.output(ledPin, True)
        time.sleep(1)
        GPIO.output(ledPin, False)
        time.sleep(1)