from imports import enums
from imports import joystickmanager
from imports import ledmanager
from imports import buttonmanager

# PINS
p1_servo_GPIO_pin = 12
p2_servo_GPIO_pin = 13

four_way_button_pin = 20
eight_way_button_pin = 21

# COLORS
four_way_button_color = (255, 0, 0)
eight_way_button_color = (255, 255, 0)

current_state = enums.JoysticksState.NOTHING

def change_state(new_state, state_function, state_color):
    global current_state
    if current_state == new_state:
        return
    state_function()
    #ledManager.rainbow_cycle(0.001)
    led_manager.fade_to(state_color)
    current_state = new_state
    
def on_four_way_button_pressed():
    change_state(enums.JoysticksState.FOUR_WAY, joystick_manager.set_to_four_way, four_way_button_color)
    
def on_eight_way_button_pressed():
    change_state(enums.JoysticksState.EIGHT_WAY, joystick_manager.set_to_eight_way, eight_way_button_color)
 
try:
    joystick_manager = joystickmanager.JoystickManager(p1_servo_GPIO_pin, p2_servo_GPIO_pin)
    led_manager = ledmanager.LEDManager(1, 1, start_color = four_way_button_color)
    button_manager = buttonmanager.ButtonManager(four_way_button_pin, on_four_way_button_pressed, eight_way_button_pin, on_eight_way_button_pressed)
    
    on_four_way_button_pressed()
    
    #ledManager.lerp(fourWayButtonColor, (0, 255, 0))
    #ledManager.fadeTo((0, 255, 0))

except KeyboardInterrupt:
    button_manager.dispose()
    pass # swallow the keyboard interrupt exception
