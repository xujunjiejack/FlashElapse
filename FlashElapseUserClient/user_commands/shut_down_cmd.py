from command_api import CommandCMDLInput, Command, ExecutableCommand

from rpb_controller import ShutDownException
import sys

class ShutDownCommand(Command):
	def _set_cmd_name_(self):
		return "Shut down"

	def _set_cmdl_channel_class_(self):
		return ShutDownCMDLInput

	def decode(self, data_dict):

		return ShutDownExeCmd()

class ShutDownCMDLInput(CommandCMDLInput):

	def get_prompt_line(self):
		return "Shut down the program"

	def _react_for_data_(self):
		print ("The program is quitting")
		return {}

class ShutDownExeCmd(ExecutableCommand):
		
	def execute(self):
		raise ShutDownException("Shut down command has been called")



