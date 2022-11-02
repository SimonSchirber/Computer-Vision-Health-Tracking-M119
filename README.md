# Computer Vision Health Tracking M119

Using Nicla Sense microcontroller and computer vision with edge impulse to monitor workouts and publish tracking online.

# Resources
- Docs for Edge with Nicla Sense: https://docs.edgeimpulse.com/docs/development-platforms/officially-supported-mcu-targets/arduino-nicla-vision

# Notes
- When switching between camera recognition on edge impulse (arduino) and OpenMV (micropython), you have to reflash the firmware
- The "save images" script in Open MV folder allows a user to continously take pictures on NICLA device and save them in a folder. For some reason I can only find the folder to copy to a desktop if i unplug and then replug in the Nicla Sense


## Tasks Left:

* Connect Nicla Sense to Wifi
* Build Website to publish data
* build backened to store data for website
* train neural network on NICLA board
* control smart device on NICLA/run python script
