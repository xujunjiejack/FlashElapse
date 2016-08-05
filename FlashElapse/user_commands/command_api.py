import __init__
import copy

class CommandLineInputNotSupport(Exception):
	"""This exception will be raised when the command line input is not supported"""
	def __init__(self,*args,**kwargs):
		Exception.__init__(self,*args,**kwargs)
	
class CommandRuntimeError(Exception):
	'''This error indicates there is an error when command is executing. It fails to run'''
	def __init__(self,*args,**kwargs):
		Exception.__init__(self,*args,**kwargs)

class ExecutableCommand(object):
	'''This executable Command has the actual implementation of controlling the camera or other
	hardware. It will require some hardware dependency. The data inside should be populated by the 
	decode method in the corresponding command object'''

	def __init__(self, data_dict = None):
		self.data_dict = data_dict

	def execute(self):
		''' The only api for rpb_controller to use'''
		try:
			self._exe_()
		except Exception as e:
			print (e)
			raise CommandRuntimeError()
	
	def _exe_(self):
		pass

class CommandCMDLInput(object):

	# Probably I need to make the empty data_dict a class variable
	def _set_cmd_name_(self, CMD_NAME_KEY, cmd_name):

		data_dict = {}
		data_dict["CMD_NAME"] = cmd_name
		setattr(self.__class__, "data_dict", data_dict)
	# Overrideable
	# Implement for the use of CMDLInput
	def get_prompt_line(self):
		'''Overrideable
		return the prompt for the user option appearing on the 
		screen'''
		raise CommandLineInputNotSupport("There is no prompt line for this option")

	# Don't override
	def get_react_func(self):
		"""Don't override"""
		return self.react

	# This is a bug. I need to figure out a way that react actually can do something
	# Not recommend to be overriden. 
	def react(self):	
		'''Don't override
		This will ask user for data in the form of dictionary. Those data will then
		be updated with the original dict which has the command's name.(This original dict will get
		 deep copy before assigned with the data) The name of command has already 
		hard coded in to the class when the first instance get instantiated.'''
	
		try:
			extra_dict = {}
			if  self._require_extra_argument_():
				extra_dict = self._react_for_data_()

			data_dict = getattr(self.__class__,"data_dict")
			new_data_dict = copy.deepcopy(data_dict)
			new_data_dict.update(extra_dict)
			print("the new_data_dict is ", new_data_dict)
			return new_data_dict
		
		except CommandLineInputNotSupport as e:
			print("Sorry, currently we don't support this command")
			raise CommandLineInputNotSupport()

	# Overridable: not override will result in no return data
	def _react_for_data_(self):
		'''Overrideable
		This is the extra reaction that might be taken for encoding more data
		If this command does not require any other information, 
		then return empty dictionary!!'''
		raise CommandLineInputNotSupport()

	# Overridable: Default is false. Please override it to be false if you want nothing to do 
	# extra
	def _require_extra_argument_(self):
		return True


class Command(object):
	"""The command is responsible for encode and decode the command into or from json 
		Based on the data, it should return the appropriate executable object.
		It's actually a place to store data. What parameter the command want.
		It's a data structure, and most of what it does is to set and get data.
		Encode should be delegated to other object. and decode should only 
		do populate data for executable command

	"""
	CMDLInput = CommandCMDLInput

	def __init__(self):
		"""It initialize the instance variable. The data field needs to be hard coded.
		 The subclass of the command needs to be created with its own instance variable.
		 We will use a.__dict__ to make the json string, so please set anything you need to
		 send as instance variable.
		 """
		super(Command, self).__init__()
		self.CMD_NAME_KEY = "CMD_NAME"
		setattr(self,self.CMD_NAME_KEY,self._set_cmd_name_())

	# Overridable: must be overriden
	def _set_cmd_name_(self):
		'''Overrideable
		This will be called to set the command name, or the 
		class can't be instantiated'''
		raise CommandRuntimeError("CMD name has to be set in the command object")

	# Overridable: must be overriden
	def decode(self, data_dict):
		'''Overrideable
		This code will actually return the exectuable_command, and is only used 
		for the rbp end'''
		executable_command = ExecutableCommand()
		return executable_command;

	# Overridable
	# need to be overrided, or you can't use cmdl to get user input
	def _set_cmdl_channel_class_(self):
		"""Overridable
		This shall return a class object, instead of an instance"""
		return CommandCMDLInput

	# Not recommand to be overriden
	def get_cmdl_channel_instance(self):
		'''Not recommand to be overriden'''

		self.cmdl_channel = self._set_cmdl_channel_class_();
		cmdl_channel = self.cmdl_channel()
		# set the header to the dict 
		cmdl_channel._set_cmd_name_(self.CMD_NAME_KEY,
									getattr(self, self.CMD_NAME_KEY))
		return self.cmdl_channel()

	# Not recommand to be overriden
	def get_command_name_key(self):
		"""	Not recommand to be overriden
			It return the key string for getting command name
			from the origin command api"""
		return self.CMD_NAME_KEY

	# Not recommand to be overriden
	def get_command_name(self):
		'''Not recommand to be overriden'''
		return getattr(self, self.CMD_NAME_KEY)

	# don't use this now	
	def get_user_command_input(self, channel_source):
		
		if channel_source == "cmd":
			if getattr(self.__class__.__name__, "CMDLInput") == None:
				raise CommandLineInputNotSupport("The CMDLInput has not been specified")
		return 

	# Overridable:
	# need to be overriden if you want to use cmdl for this command
