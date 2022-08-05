from imports import servohandler

EIGHT_WAY_VALUE = -0.35
FOUR_WAY_VALUE = 0.6

class JoystickManager:
    def __init__(self, p1ServoPin, p2ServoPin):
        #self.servoHandlers = [servohandler.ServoHandler(p1ServoPin)]
        self.servoHandlers = [servohandler.ServoHandler(p1ServoPin), servohandler.ServoHandler(p2ServoPin)]

    def move(self, value):
        for sh in self.servoHandlers:
            sh.move(value)
            
    def moveAngle(self, angle):
        for sh in self.servoHandlers:
            sh.moveAngle(angle)
    
    def moveMin(self):
        for sh in self.servoHandlers:
            sh.moveMin()
    
    def moveMax(self):
        for sh in self.servoHandlers:
            sh.moveMax()
            
    def setToEightWay(self):
        self.move(EIGHT_WAY_VALUE)
        
    def setToFourWay(self):
        self.move(FOUR_WAY_VALUE)