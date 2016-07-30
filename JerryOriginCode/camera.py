from picamera import PiCamera
from time import sleep
import os


camera = PiCamera()

camera.resolution = (3240,2464)
for i in range(10):
    sleep(4)
    camera.capture('/home/pi/Desktop/GFP/GFP4%d.jpg' % i)
 
