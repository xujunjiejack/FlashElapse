from command_api import CommandCMDLInput, Command, ExecutableCommand
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
		sys.exit(0)
		return {}

class ShutDownExeCmd(ExecutableCommand):
		pass

