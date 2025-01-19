from machine import Pin
from utime import sleep

stop_pin = Pin(4, Pin.IN, Pin.PULL_UP)

pin = Pin("LED", Pin.OUT)


while stop_pin.value():
    pin.toggle()
    sleep(1)  # sleep 1sec
    print("LED is ON" if pin.value() else "LED is OFF")
