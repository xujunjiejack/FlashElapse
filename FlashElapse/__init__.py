#import picamera
import os
import sys

print ("***The FlashElapse is initializing!***")

# check whether the camera is connected, if no, quit the program

def set_up_camera_or_exit():
	try:
		#camera = picamera.PiCamera()
		return camera
	except Exception as e:
		print ("Camera Initialization fails.\n"
			"Please check your connection with camera\n"
			"Program quitting")
	sys.exit(1)
#camera = set_up_camera_or_exit()


# it has connection with the camera, then start the main. In the main, it will create the control object, MainController




