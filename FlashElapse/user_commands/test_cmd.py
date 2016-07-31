from command_api import Command,ExecutableCommand
from cmd_header_const import TEST

class TestCmd(Command):
	"""docstring for TestCmd"""
	def __init__(self):
		super(TestCmd, self).__init__()

	def _set_cmd_name_(self):
		return TEST

	def decode(self,data_dict):

		return TestExeCmd()

class TestExeCmd(ExecutableCommand):
	"""docstring for TestExeCmd"""
	def __init__(self):
		super(TestExeCmd, self).__init__()
		
	def _exe_(self):
		print ("Here is the test")
		

