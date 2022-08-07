import time
import board
import neopixel

import numpy as np

# NeoPixels must be connected to D10, D12, D18 or D21 to work.
# This class assumes that the LED is connected to pin BCM 18
class LEDManager:
    # The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
    # For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
    ORDER = neopixel.GRB
    
    current_color = None
    num_pixels = 0
    
    def __init__(self, num_pixels, brightness, start_color):
        self.num_pixels = num_pixels
        self.pixels = neopixel.NeoPixel(board.D18, num_pixels, brightness=brightness, auto_write=False, pixel_order=self.ORDER)
        self.set_color(start_color) # Set the starting default color
         
    def fade_to(self, new_color):
        start_color = self.current_color
        for t in np.arange(0, 1, 0.05):
            color = self.__lerp_RGB(start_color, new_color, t)
            self.set_color(color)
            time.sleep(0.05)
        self.set_color(new_color) #set the final color after the loop
        
    def set_color(self, rgb):
        self.pixels.fill(rgb)
        self.pixels.show()
        self.current_color = rgb #Save a reference to the color we just set
        #print(rgb)
        
    def rainbow_cycle(self, wait):
        for j in range(255):
            for i in range(self.num_pixels):
                pixel_index = (i * 256 // self.num_pixels) + j
                self.pixels[i] = self.__wheel(pixel_index & 255)
            self.pixels.show()
            time.sleep(wait)
            
    def __lerp_RGB(self, c1, c2, t):
        r = c1[0] + ((c2[0] - c1[0]) * t)
        g = c1[1] + ((c2[1] - c1[1]) * t)
        b = c1[2] + ((c2[2] - c1[2]) * t)
        return (r,g,b)

    def __wheel(self, pos):
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 85:
            r = int(pos * 3)
            g = int(255 - pos * 3)
            b = 0
        elif pos < 170:
            pos -= 85
            r = int(255 - pos * 3)
            g = 0
            b = int(pos * 3)
        else:
            pos -= 170
            r = 0
            g = int(pos * 3)
            b = int(255 - pos * 3)
        return (r, g, b) if self.ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)