import time
from servo import Servo

# Create our Servo object, assigning the
# GPIO pin connected the PWM wire of the servo
my_servo = Servo(16)

while True:
    # Set the Servo to the mid-point (90 is half way between zero and 180 degrees)
    my_servo.move(0)
    time.sleep(5)  # Wait for 1 second
    print("Servo at 0 degrees")

    # Set the Servo to the left most position
    my_servo.move(90)
    time.sleep(2)  # Wait for 1 second
    print("Servo Stop")

    # Set the Servo to the right most position
    my_servo.move(180)
    time.sleep(5)  # Wait for 1 second
    print("Servo at 180 degrees")

    # Set the Servo to the left most position
    my_servo.move(90)
    time.sleep(2)  # Wait for 1 second
    print("Servo Stop")
