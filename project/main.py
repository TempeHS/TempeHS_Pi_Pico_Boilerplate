import sys
from machine import Pin


sys.path.append("/py_scripts")


stop_pin = Pin(4, Pin.IN, Pin.PULL_UP)


def callback(stop_pin):
    raise KeyboardInterrupt("Stop button pressed")


stop_pin.irq(trigger=Pin.IRQ_FALLING, handler=callback)

try:
    import v01
except KeyboardInterrupt:
    print("Exiting main loop")
except ImportError as e:
    print("Import error in main:")
    sys.print_exception(e)
except RuntimeError as e:
    print("Runtime error in main:")
    sys.print_exception(e)
except OSError as e:
    print("OS error in main:")
    sys.print_exception(e)
except Exception as e:
    print("Unknown exception:")
    sys.print_exception(e)
