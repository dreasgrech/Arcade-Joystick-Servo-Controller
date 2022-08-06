import time
from imports import constants
from imports import joystickmanager

from gpiozero import Button

p1ServoGPIOPin = 12
p2ServoGPIOPin = 13

fourWayButtonPin = 20
eightWayButtonPin = 21

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
        angle = float(input('Enter angle between -35 and 55: '))
        j.moveAngle(angle)
        
def valueLoop(j):
    while True:
        value = float(input('Enter value between -1 and 1: '))
        j.move(value)

def positionsLoop(j):
    j.setToFourWay()
    isFourWayEnabled = True
    while True:
        if isFourWayEnabled == True:
            j.setToEightWay()
            #j.moveMin()
        else:
            j.setToFourWay()
            #j.moveMax()
        
        time.sleep(1)
        isFourWayEnabled = not isFourWayEnabled        

try:
    jm = joystickmanager.JoystickManager(p1ServoGPIOPin, p2ServoGPIOPin)
    
    leftButton = Button(fourWayButtonPin)
    #leftButton.wait_for_press()
    leftButton.when_pressed = jm.setToFourWay
    #print("left pressed")
    
    rightButton = Button(eightWayButtonPin)
    #rightButton.wait_for_press()
    rightButton.when_pressed = jm.setToEightWay
    #print("right pressed")
    
    

    #testLoop(jm)
    #jm.moveAngle(81)
    #angleLoop(jm)
    #valueLoop(jm)
    #positionsLoop(jm)
    #jm.moveMin()
    #jm.moveMax()
except KeyboardInterrupt:
    leftButton.when_pressed = None
    rightButton.when_pressed = None
    pass # swallow the keyboard interrupt exception