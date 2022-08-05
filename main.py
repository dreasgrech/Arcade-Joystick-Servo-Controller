import time
from imports import constants
from imports import joystickmanager

p1ServoGPIOPin = 12
p2ServoGPIOPin = 13

def testLoop(j):
    print("Starting loop")
    duty = constants.MIN_CYCLE_VALUE
    while duty <= constants.MAX_CYCLE_VALUE:
        print("iteration: " + str(duty-2) + ", duty: " + str(duty))
        
        j.move(duty)
        
        duty = duty + 1
    
    time.sleep(1)

    print("Turning to 90deg")
    j.move(7)

    #time.sleep(1)

    print("Turning to 0deg")
    j.move(constants.MIN_CYCLE_VALUE)
    
def angleLoop(j):
    while True:
        angle = float(input('Enter angle between 0 and 180: '))
        j.moveAngle(angle)

def positionsLoop(j):
    j.setToFourWay()
    isFourWayEnabled = True
    while True:
        if isFourWayEnabled == True:
            j.setToEightWay()
        else:
            j.setToFourWay()
        
        time.sleep(1)
        isFourWayEnabled = not isFourWayEnabled        

try:
    jm = joystickmanager.JoystickManager(p1ServoGPIOPin, p2ServoGPIOPin)
    jm.start()

    #testLoop(jm)
    #jm.moveAngle(81)
    #angleLoop(jm)
    positionsLoop(jm)

    jm.stop()
except KeyboardInterrupt:
    jm.stop()