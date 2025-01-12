import machine, sys

sys.path.append("/libs")
sys.path.append("/py_scripts")

import v01 as pi_pico_project  # Change this as you create more versions

try:
    pi_pico_project.setup()
    pi_pico_project.loop()
except KeyboardInterrupt:
    print("Exiting main.py")
except Exception as e:
    print("Fatal error in main:")
    sys.print_exception(e)

# Following a normal Exception or main() exiting, reset the board.
# Following a non-Exception error such as KeyboardInterrupt (Ctrl-C),
# this code will drop to a REPL. Place machine.reset() in a finally
# block to always reset, instead.
machine.reset()
