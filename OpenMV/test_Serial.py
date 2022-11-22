
import time
from utime import time,  gmtime, sleep
import pyb

num_20lb = 0
num_30lb = 0
num_minutes = 0
num_seconds = 0
is_working_out = False
button = pyb.Pin(pyb.Pin.board.PC4, pyb.Pin.IN)
t_init = time()
greenLED = pyb.LED(2) # built-in blue LED
redLED = pyb.LED(1) # built-in red LED
redLED.on()
while True:

    if (is_working_out):
        delta = gmtime(time() - t_init)
        num_seconds = delta[5]
        num_minutes = delta[4]
        num_20lb += 1
        num_30lb += 3
    print(f"{num_20lb}, {num_30lb}, {num_minutes}, {num_seconds}")
    sleep(1)
    ##Start/Stop Workout
    if (button.value() == 1):
        is_working_out = not is_working_out
        if (is_working_out):
            num_20lb = 0
            num_30lb = 0
            greenLED.on()
            redLED.off()
            t_init = time()
        else:
            greenLED.off()
            redLED.on()



