from command_api import Command, ExecutableCommand, CommandCMDLInput

class StartPreviewCmd(Command):

	def __init__(self):
		super(StartPreviewCmd,self).__init__()
		
	def _set_cmd_name_(self):
		return "Start preview";

	def _set_cmdl_channel_class_(self):
		return StartPreviewCMDLChannel

	def decode(self,data_dict):
		return StartPreviewExeCmd()


class StartPreviewExeCmd(ExecutableCommand):

        def __init__(self):
                super(StartPreviewExeCmd, self).__init__()
                from __init__ import picamera,camera
                self.camera = camera

        def _exe_(self):
                '''The actual execute code for doing command. Every exception it throws will
                be thrown to execute to be a command runtime error. This error handling has 
                been delegated to the execute(). Outsider should not use this method for run
                Developer needs to inheritance this method for the command to run
                '''
                self.camera.start_preview()


class StartPreviewCMDLChannel(CommandCMDLInput):
	def __init__(self):
		super(StartPreviewCMDLChannel, self).__init__()

	def get_prompt_line(self):
		return "Start the preview"

	def _require_extra_argument_(self):
		return False



