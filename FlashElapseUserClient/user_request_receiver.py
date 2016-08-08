''' This module contains the class for regulating different ways of user input '''
from user_request_channel import channel_creator

class UserRequestAdapter():
	''' This one will be responsible of making different ways of user input into one 
		behavior. '''


	def __init__(self, source, cmd_manager):
		''' call the user request channel module, which will in the close have two way. Command line (local from
			the raspberry pi) or LAN (from a local network). In the future, possible the network
			(HTTP protocal). 
			The user input class should conform the interface "Channel", which this class will be used to
			 regulate the behavior.
		 ''' 
		self.channel = channel_creator.create_channel(source, cmd_manager)
		pass;

	def start_listening(self, parsedata_callback):
		'''this will call the Channel to start running'''
		self.channel.start_listening(parsedata_callback);

	def end_listening (self):
		self.channel.end_listening()

class UserRequestError(Exception):
	"""docstring for UserRequestError"""
	def __init__(self, arg):
		super(UserRequestError, self).__init__()
		self.arg = arg
		




