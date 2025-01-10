"""
A simple example that sweeps a Servo back-and-forth
Requires the micropython-servo library - https://pypi.org/project/micropython-servo/
pip install micropython-servo
Servo Easing(smoothing): https://www.youtube.com/watch?v=TFsr_gK8NrA
"""

import time
from servo import Servo
from smooth_servo import SmoothEaseInOut

# Create our Servo object, assigning the
# GPIO pin connected the PWM wire of the servo
my_servo = Servo(pin_id=20)

# Set easing parameters
value = 180  # End value the iterator should reach
time_ms = 3000  # Time in milliseconds to reach end value
start_value = 0  # Start value
tick_time_ms = 5  # Time between iterations (used to calculate the number of steps)

# Create an instance of the iterator class
linear = SmoothEaseInOut(value, time_ms, start_value)

# create an iterator with a given time between iterations
iterator = linear.generate(tick_time_ms)

while True:
    try:
        for i in iterator:  # Step the position forward from 0deg to 180deg
            print(180 - i)  # Show the current position in the Shell/Plotter
            my_servo.write(180 - i)  # Set the Servo to the current position
            time.sleep(tick_time_ms / 1000)  # Wait for the servo to make the movement
        for i in iterator:  # Step the position forward from 0deg to 180deg
            print(i)  # Show the current position in the Shell/Plotter
            my_servo.write(i)  # Set the Servo to the current position
            time.sleep(tick_time_ms / 1000)  # Wait for the servo to make the movement
    except KeyboardInterrupt:
        break
print("Finished.")
