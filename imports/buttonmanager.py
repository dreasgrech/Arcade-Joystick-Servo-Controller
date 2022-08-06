from gpiozero import Button

class ButtonManager:
    def __init__(self, fourWayButtonPin, fourWayButtonPressedCallback, eightWayButtonPin, eightWayButtonPressedCallback):
        self.fourWayButton = Button(fourWayButtonPin)
        self.fourWayButton.when_pressed = fourWayButtonPressedCallback
        
        self.eightWayButton = Button(eightWayButtonPin)
        self.eightWayButton.when_pressed = eightWayButtonPressedCallback
        
        self.buttons = [self.fourWayButton, self.eightWayButton]

    def dispose(self):
        self.fourWayButton.when_pressed = None
        self.eightWayButton.when_pressed = None
        print("disposed")