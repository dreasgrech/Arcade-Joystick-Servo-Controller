from gpiozero import Button

class ButtonManager:
    def __init__(self,
                 four_way_button_pin,
                 four_way_button_pressed_callback,
                 four_way_button_held_callback,
                 four_way_button_held_time,
                 eight_way_button_pin,
                 eight_way_button_pressed_callback,
                 eight_way_button_held_callback,
                 eight_way_button_held_time):
        
        self.four_way_button = Button(four_way_button_pin, hold_time = four_way_button_held_time)
        self.four_way_button.when_pressed = four_way_button_pressed_callback
        self.four_way_button.when_held = four_way_button_held_callback
        
        self.eight_way_button = Button(eight_way_button_pin, hold_time = eight_way_button_held_time)
        self.eight_way_button.when_pressed = eight_way_button_pressed_callback
        self.eight_way_button.when_held = eight_way_button_held_callback
        
        self.buttons = [self.four_way_button, self.eight_way_button]

    def dispose(self):
        self.four_way_button.when_pressed = None
        self.four_way_button.when_held = None
        self.four_way_button.close()
        self.eight_way_button.when_pressed = None
        self.eight_way_button.when_held = None
        self.eight_way_button.close()