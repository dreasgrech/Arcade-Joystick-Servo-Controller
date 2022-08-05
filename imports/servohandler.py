# IMPORTANT: make sure pigpio deamon is running: 'sudo pigpiod'
from gpiozero.pins.pigpio import PiGPIOFactory

#from gpiozero import AngularServo
from gpiozero import Servo
import time
from imports import constants

class ServoHandler:
    def __init__(self, pin):
        self.pin = pin
        
        # create a custom pin-factory to fix servo jitter
        # more info here: https://gpiozero.readthedocs.io/en/stable/api_output.html#servo
        # and here: https://gpiozero.readthedocs.io/en/stable/api_pins.html
        pigpio_factory = PiGPIOFactory()
        
        #self.servo = AngularServo(pin, pin_factory=pigpio_factory)
        #self.servo = AngularServo(pin, min_angle=-35, max_angle=55, pin_factory=pigpio_factory)
        self.servo = Servo(pin, pin_factory=pigpio_factory)

    def move(self, value):
        # value must be -1 and 1
        self.servo.value = value
        
    def moveAngle(self, angle):
        self.servo.angle = angle
        
    def moveMin(self):
        self.servo.min()
        
    def moveMax(self):
        self.servo.max()