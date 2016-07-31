import __init__
from cmd_header_const import COMMAND_NAME_KEY
class Command(object):
	"""The command is responsible for encode and decode the command into or from json 
		Based on the data, it should return the appropriate executable object.
		It's actually a place to store data. What parameter the command want.
		It's a data structure, and most of what it does is to set and get data.
		Encode should be delegated to other object. and decode should only 
		do populate data for executable command

	"""

	def __init__(self):
		"""It initialize the instance variable. The data field needs to be hard coded.
		 The subclass of the command needs to be created with its own instance variable.
		 We will use a.__dict__ to make the json string, so please set anything you need to
		 send as instance variable.
		 """
		super(Command, self).__init__()
		setattr(self,COMMAND_NAME_KEY,self._set_cmd_name_())

	def _set_cmd_name_(self):
		raise CommandRuntimeError("CMD name has to be set in the command object")

	def decode(self, data_dict):
		'''This code will actually return the exectuable_command, and is only used 
		for the rbp end'''
		executable_command = ExecutableCommand()
		return executable_command;

class CommandRuntimeError(Exception):
	'''This error indicates there is an error when command is executing. It fails to run'''
	def __init__(self,*args,**kwargs):
		Exception.__init__(self,*args,**kwargs)
	

class ExecutableCommand(object):
	'''This executable Command has the actual implementation of controlling the camera or other
	hardware. It will require some hardware dependency. The data inside should be populated by the 
	decode method in the corresponding command object'''

	def execute(self):
		''' The only api for rpb_controller to use'''
		try:
			self._exe_()
		except Exception as e:
			print (e)
			raise CommandRuntimeError()
	
	def _exe_(self):
		pass

