import RPi.GPIO as GPIO
import time
from imports import constants

class ServoHandler:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin, GPIO.OUT)
        frequency = 50
        self.servo = GPIO.PWM(pin, frequency)

    def start(self):
        self.servo.start(0)

    def move(self, duty):
        self.servo.ChangeDutyCycle(duty)
        time.sleep(0.5)
        self.servo.ChangeDutyCycle(constants.STOP_CYCLE_VALUE)
        #time.sleep(0.7)
        
    def moveAngle(self, angle):
        # angle must be between 0 and 180
        duty = constants.MIN_CYCLE_VALUE + (angle/18)
        self.move(duty)
        
    def moveMin(self):
        self.move(constants.MIN_CYCLE_VALUE)
        
    def moveMax(self):
        self.move(constants.MAX_CYCLE_VALUE)

    def stop(self):
        self.servo.stop()