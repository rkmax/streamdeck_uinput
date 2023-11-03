from evdev import ecodes
from streamdeck_uinput import UInput
import time


keyboard = UInput()

time.sleep(2)
print("Simulating key press and release...")
# Simulate pressing a key
keyboard.write(ecodes.EV_KEY, ecodes.KEY_A, 1)
keyboard.syn()
keyboard.write(ecodes.EV_KEY, ecodes.KEY_A, 0)
keyboard.syn()
time.sleep(2)

# Close the virtual keyboard when done
keyboard.close()
