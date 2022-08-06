import time
from imports import constants
from imports import enums
from imports import joystickmanager
from imports import ledmanager
from imports import buttonmanager

# PINS
p1ServoGPIOPin = 12
p2ServoGPIOPin = 13

fourWayButtonPin = 20
eightWayButtonPin = 21

ledPin = 18

# COLORS
fourWayButtonColor = (255, 0, 0)
eightWayButtonColor = (0, 0, 255)

# GLOBALS
currentState = None

def changeState(newState, stateFunction, stateColor):
    global currentState
    if currentState == newState:
        return
    stateFunction()
    ledManager.rainbow_cycle(0.001)
    ledManager.setRGBColor(stateColor)
    currentState = newState
    
def onFourWayButtonPressed():
    changeState(enums.JoysticksState.FourWay, joystickManager.setToFourWay, fourWayButtonColor)
    
def onEightWayButtonPressed():
    changeState(enums.JoysticksState.EightWay, joystickManager.setToEightWay, eightWayButtonColor)
 
try:
    joystickManager = joystickmanager.JoystickManager(p1ServoGPIOPin, p2ServoGPIOPin)
    ledManager = ledmanager.LEDManager(1, 1)
    buttonManager = buttonmanager.ButtonManager(fourWayButtonPin, onFourWayButtonPressed, eightWayButtonPin, onEightWayButtonPressed)
    
    onFourWayButtonPressed()

except KeyboardInterrupt:
    buttonManager.dispose()
    pass # swallow the keyboard interrupt exception