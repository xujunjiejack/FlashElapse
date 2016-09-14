from command_api import Command, ExecutableCommand, CommandCMDLInput

class StopPreviewCmd(Command):

	def __init__(self):
		super(StopPreviewCmd,self).__init__()
		
	def _set_cmd_name_(self):
		return "Stop preview";

	def decode(self,data_dict,delegate = None):
		return StopPreviewExeCmd()

	def _set_cmdl_channel_class_ (self):
		
		return StopPreviewCMDLChannel 


class StopPreviewExeCmd(ExecutableCommand):

	def __init__(self, data_dict = None, delegate = None):
		super(StopPreviewExeCmd, self).__init__(data_dict, delegate)
		from user_setting import get_camera
		self.camera = get_camera() 

	def _exe_(self):
		'''The actual execute code for doing command. Every exception it throws will
		be thrown to execute to be a command runtime error. This error handling has 
		been delegated to the execute(). Outsider should not use this method for run
		Developer needs to inheritance this method for the command to run
		'''
		self.camera.stop_preview()
		print ("Stop Preview")
			
class StopPreviewCMDLChannel(CommandCMDLInput):
	"""docstring for StopPreviewCMDLChannel"""
	def __init__(self):
		super(StopPreviewCMDLChannel, self).__init__()
		
	def get_prompt_line(self):
		return "Stop the preview"

	def _require_extra_argument_(self):
		return False
