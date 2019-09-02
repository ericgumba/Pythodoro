import platform
import numpy as np
import os

frequency = 1000 # Hertz
duration  = 2000 # milliseconds
 

if os.name == "nt":
    import winsound
    winsound.Beep(frequency, duration)
else:
    os.system('say "Break Time"')
    os.system('say "back to work"')