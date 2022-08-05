import RPi.GPIO as GPIO
from imports import servohandler

EIGHT_WAY_ANGLE = 80.5
FOUR_WAY_ANGLE = 35

class JoystickManager:
    def __init__(self, p1ServoPin, p2ServoPin):
        GPIO.setmode(GPIO.BCM)

        self.servoHandlers = [servohandler.ServoHandler(p1ServoPin), servohandler.ServoHandler(p2ServoPin)]
        #self.servoHandlers = [servohandler.ServoHandler(p1ServoPin)]

    def start(self):
        for sh in self.servoHandlers:
            sh.start()

    def move(self, duty):
        for sh in self.servoHandlers:
            sh.move(duty)
            
    def moveAngle(self, angle):
        for sh in self.servoHandlers:
            sh.moveAngle(angle)
            
    def setToEightWay(self):
        self.moveAngle(EIGHT_WAY_ANGLE)
        
    def setToFourWay(self):
        self.moveAngle(FOUR_WAY_ANGLE)

    def stop(self):
        for sh in self.servoHandlers:
            sh.stop()

        GPIO.cleanup()
