from user_commands.command_api import Command,ExecutableCommand, CommandCMDLInput

class TestCmd(Command):
	"""docstring for TestCmd"""
	def __init__(self):
		super(TestCmd, self).__init__()

	def _set_cmd_name_(self):
		return "Test"

	def decode(self,data_dict):
		return TestExeCmd()

	def _set_cmdl_channel_class_(self):
		return TestCMDLChannel

class TestExeCmd(ExecutableCommand):
	"""docstring for TestExeCmd"""
	def __init__(self):
		super(TestExeCmd, self).__init__()
		
	def _exe_(self):
		print ("Here is the test")
	
class TestCMDLChannel(CommandCMDLInput):
	
	def __init__(self):
		super(TestCMDLChannel,self).__init__()	

	def get_prompt_line(self):
		return "Test the system"

	def _require_extra_argument_(self):
		return False
