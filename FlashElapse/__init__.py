import picamera
import os
import sys

print ("***The FlashElapse is initializing!***")

# check whether the camera is connected, if no, quit the program
camera = ''
try:
	camera = picamera.PiCamera();
except Exception, e:
	print ("Camera Initialization fails.\n"
			"Please check your connection with camera\n"
			"Program quitting")
	sys.exit(1)




# it has connection with the camera, then start the main. In the main, it will create the control object, MainController




