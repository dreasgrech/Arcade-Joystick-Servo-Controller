import time
from imports import servohandler

EIGHT_WAY_VALUE = -0.35
FOUR_WAY_VALUE = 0.6

class JoystickManager:
    def __init__(self, p1_servo_pin, p2_servo_pin):
        #self.servo_handlers = [servohandler.ServoHandler(p1_servo_pin)]
        self.servo_handlers = [servohandler.ServoHandler(p1_servo_pin), servohandler.ServoHandler(p2_servo_pin)]

    def move(self, value):
        for sh in self.servo_handlers:
            sh.move(value)
            
    def move_min(self):
        for sh in self.servo_handlers:
            sh.move_min()
    
    def move_max(self):
        for sh in self.servo_handlers:
            sh.move_max()
            
    def set_to_eight_way(self):
        self.move(EIGHT_WAY_VALUE)
        
    def set_to_four_way(self):
        self.move(FOUR_WAY_VALUE)
        
    def positions_loop(self):
        self.set_to_four_way()
        is_four_way_enabled = True
        while True:
            if is_four_way_enabled == True:
                self.set_to_eight_way()
            else:
                self.set_to_four_way()
            
            time.sleep(1)
            is_four_way_enabled = not is_four_way_enabled     
            
    def value_loop(self):
        while True:
            value = float(input('Enter value between -1 and 1: '))
            self.move(value)
            
    def dispose(self):
        for sh in self.servo_handlers:
            sh.dispose()