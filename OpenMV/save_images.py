import pyb # Import module for board related functions
import sensor # Import the module for sensor related functions
import image # Import module containing machine vision algorithms
import time
import uos

redLED = pyb.LED(1) # built-in red LED
blueLED = pyb.LED(3) # built-in blue LED

sensor.reset() # Initialize the camera sensor.
sensor.set_pixformat(sensor.RGB565) # Sets the sensor to RGB
#sensor.set_framesize(sensor.QVGA) # Sets the resolution to 320x240 px
sensor.set_framesize(sensor.QVGA) # Sets the resolution to 320x240 px
#sensor.set_vflip(True) # Flips the image vertically
sensor.set_hmirror(True) # Mirrors the image horizontally

num = 0

#Delete all png files
files = uos.listdir()
for file in files:
    print(file)
    if "jpg" in file:
        print(f"removing {file}")
        uos.remove(file)
object = "two_finger_rotation_test2"

##uos.rmdir("stophand")
uos.mkdir(object)
uos.chdir(f"/{object}")



for i in range(15):
    redLED.on()
    sensor.skip_frames(time = 1000) # Skip some frames to let the image stabilize
    sensor.snapshot().save(f'{object}_{num}.jpg')
    redLED.off()
    time.sleep(2)
    num += 1
    print(f"picture {num}")



