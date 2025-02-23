"""
Example code for teh RGB LED
More examples: https://github.com/CoreElectronics/CE-PiicoDev-RGB-LED-MicroPython-Module
"""

from PiicoDev_RGB import PiicoDev_RGB, wheel
from PiicoDev_Unified import sleep_ms # Cross-platform compatible sleep function

leds = PiicoDev_RGB() # initialise the LED module with conservative default brightness
# leds.setBrightness(127) # 0-255 set the global brightness to half

# pre-define some colours
red = [255,0,0] 
green = [0,255,0]
blue = [0,0,255]
yellow = [255,255,0]
magenta = [255,0,255]
cyan = [0,255,255]
white = [255,255,255]
black = [0,0,0]

# Example 1: Set LEDs to pure Red, Green, Blue for 3 seconds
leds.setPixel(0, red)
leds.setPixel(1, green)
leds.setPixel(2, blue)
leds.show() # call show() to update the LEDs with new colours
sleep_ms(3000)
leds.clear() # clear the LEDs