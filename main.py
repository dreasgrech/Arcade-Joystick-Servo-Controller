# IMPORTANT: make sure pigpio deamon is running (PiGPIOFactory for servo motors requires it): 'sudo pigpiod'
import time
from signal import pause
from imports import enums
from imports import joystickmanager
from imports import ledmanager
from imports import buttonmanager

# PINS
P1_SERVO_GPIO_PIN = 12
P2_SERVO_GPIO_PIN = 13

FOUR_WAY_BUTTON_PIN = 20
EIGHT_WAY_BUTTON_PIN = 21

# COLORS
FOUR_WAY_BUTTON_COLOR = (255, 0, 0)
EIGHT_WAY_BUTTON_COLOR = (0, 0, 255)

LEDS_TOTAL = 1 # the number of LEDs
LED_BRIGHTNESS = 1

current_state = enums.JoysticksState.NOTHING

def change_state(new_state, state_function, state_color):
    global current_state
    if current_state == new_state:
        return
    state_function()
    led_manager.fade_to(state_color)
    current_state = new_state
    
def on_four_way_button_pressed():
    change_state(enums.JoysticksState.FOUR_WAY, joystick_manager.set_to_four_way, FOUR_WAY_BUTTON_COLOR)
    
def on_eight_way_button_pressed():
    change_state(enums.JoysticksState.EIGHT_WAY, joystick_manager.set_to_eight_way, EIGHT_WAY_BUTTON_COLOR)
 
try:
    joystick_manager = joystickmanager.JoystickManager(P1_SERVO_GPIO_PIN, P2_SERVO_GPIO_PIN)
    led_manager = ledmanager.LEDManager(num_pixels = LEDS_TOTAL, brightness = LED_BRIGHTNESS, start_color = FOUR_WAY_BUTTON_COLOR)
    button_manager = buttonmanager.ButtonManager(FOUR_WAY_BUTTON_PIN, on_four_way_button_pressed, EIGHT_WAY_BUTTON_PIN, on_eight_way_button_pressed)
    
    # Do the booting animation stuff
    led_manager.rainbow_cycle(0.001)
    led_manager.rainbow_cycle(0.001)
    time.sleep(0.25)
    on_eight_way_button_pressed()
    time.sleep(0.25)
    
    # Start on one of the states
    on_four_way_button_pressed()
    
    pause()
    
except KeyboardInterrupt:
    #print("KEYBOARD INTERRUPT")
    pass # swallow the keyboard interrupt exception
finally:
    #print("FINALLY")
    joystick_manager.dispose()
    led_manager.dispose()
    button_manager.dispose()
    print("Arcade Joystick Servo Controller exited.")