import machine, sys

sys.path.append("/py_scripts")

try:
    import v05
except KeyboardInterrupt:
    print("Exiting main.py")
except Exception as e:
    print("Fatal error in main:")
    sys.print_exception(e)

# block to always reset, instead.
machine.reset()
