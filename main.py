# IMPORTANT: make sure pigpio deamon is running (PiGPIOFactory for servo motors requires it): 'sudo pigpiod'
import time
from signal import pause
from imports import enums
from imports import joystickmanager
from imports import ledmanager
from imports import buttonmanager
from imports import logmanager
from imports import osmanager
from threading import Thread

# PINS
P1_SERVO_GPIO_PIN = 12
P2_SERVO_GPIO_PIN = 13

FOUR_WAY_BUTTON_PIN = 20
#EIGHT_WAY_BUTTON_PIN = 21
EIGHT_WAY_BUTTON_PIN = 3

# COLORS
FOUR_WAY_BUTTON_COLOR = (0, 0, 255)
EIGHT_WAY_BUTTON_COLOR = (255, 0, 0)

LEDS_TOTAL = 1 # the number of LEDs
LED_BRIGHTNESS = 1

SHUTDOWN_BUTTON_HOLD_TIME = 2

current_state = enums.JoysticksState.NOTHING
has_cleaned_up = False

def change_state(new_state, state_function, state_color):
    global current_state
    if current_state == new_state:
        return False
    state_function()
    led_manager.fade_to(state_color)
    current_state = new_state
    return True
    
def on_four_way_button_pressed():
    state_changed = change_state(enums.JoysticksState.FOUR_WAY, joystick_manager.set_to_four_way, FOUR_WAY_BUTTON_COLOR)
    if state_changed == True:
        log_manager.log("Switched to 4-way joystick")    
    
def on_eight_way_button_pressed():
    state_changed = change_state(enums.JoysticksState.EIGHT_WAY, joystick_manager.set_to_eight_way, EIGHT_WAY_BUTTON_COLOR)
    if state_changed == True:
        log_manager.log("Switched to 8-way joystick")

def on_shutdown_button_held():
    # Andreas: here I call the function in a new thread because I can't cleanup the button code in here since this function is a button callback
    t = Thread(target = shutdown_system)
    t.start()

def shutdown_system():
    time.sleep(1) #wait a bit to make sure all the callback thread has finished
    led_manager.fade_to_off()
    cleanup()
    log_manager.log("Shutting down Operating System...")
    os_manager.shutdown()
    
def cleanup():
    global has_cleaned_up
    if has_cleaned_up == True:
        return
    log_manager.log("Deinitializing managers...")
    joystick_manager.dispose()
    led_manager.dispose()
    button_manager.dispose()
    has_cleaned_up = True
    log_manager.log("Arcade Joystick Servo Controller exited.")
 
try:
    log_manager = logmanager.LogManager()
    log_manager.log("Initializing the Arcade Joystick Servo Controller...")
    
    joystick_manager = joystickmanager.JoystickManager(P1_SERVO_GPIO_PIN, P2_SERVO_GPIO_PIN)
    led_manager = ledmanager.LEDManager(num_pixels = LEDS_TOTAL, brightness = LED_BRIGHTNESS, start_color = FOUR_WAY_BUTTON_COLOR)
    os_manager = osmanager.OSManager()
    button_manager = buttonmanager.ButtonManager(
        FOUR_WAY_BUTTON_PIN,
        on_four_way_button_pressed,
        on_shutdown_button_held,
        SHUTDOWN_BUTTON_HOLD_TIME,
        EIGHT_WAY_BUTTON_PIN,
        on_eight_way_button_pressed,
        on_shutdown_button_held,
        SHUTDOWN_BUTTON_HOLD_TIME)
    
    # Do the booting animation stuff
    log_manager.log("Booting up the Arcade Joystick Servo Controller...")
    led_manager.rainbow_cycle(0.001)
    led_manager.rainbow_cycle(0.001)
    time.sleep(0.25)
    on_four_way_button_pressed()
    time.sleep(0.25)
    
    # Start on one of the states
    on_eight_way_button_pressed()
    
    log_manager.log("Listening for button presses...")
    
    pause()
    
except KeyboardInterrupt:
    #print("KEYBOARD INTERRUPT")
    pass # swallow the keyboard interrupt exception
finally:
    #print("FINALLY")
    cleanup()
    
    