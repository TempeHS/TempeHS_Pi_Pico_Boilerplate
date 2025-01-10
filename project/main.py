import time
from servo import Servo

# Create our Servo object, assigning the
# GPIO pin connected the PWM wire of the servo
my_servo = Servo(pin_id=16)

while True:
    # Set the Servo to the mid-point (90 is half way between zero and 180 degrees)
    my_servo.write(90)
    time.sleep(1)  # Wait for 1 second
    print("Servo at 90 degrees")

    # Set the Servo to the left most position
    my_servo.write(0)  
    time.sleep(1)  # Wait for 1 second
    print("Servo at 0 degrees")

    # Set the Servo to the right most position
    my_servo.write(180)  
    time.sleep(1)  # Wait for 1 second
    print("Servo at 180 degrees")
