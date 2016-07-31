from command_api import Command, ExecutableCommand
from cmd_header_const import START_PREVIEW

class StartPreviewCmd(Command):

	def __init__(self):
		super(StartPreviewCmd,self).__init__()
		
	def _set_cmd_name_(self):
		return START_PREVIEW;

	def decode(self,data_dict):
		pass;

class StartPreviewExeCmd(ExecutableCommand):

	def __init__(self):
		super(StartPreviewExeCmd, self).__init__()
		from FlashElapse.__init__ import camera, picamera
		self.camera = camera 

	def _exe_(self):
		'''The actual execute code for doing command. Every exception it throws will
		be thrown to execute to be a command runtime error. This error handling has 
		been delegated to the execute(). Outsider should not use this method for run
		Developer needs to inheritance this method for the command to run
		'''
		print("This function has not been implemented")
			







