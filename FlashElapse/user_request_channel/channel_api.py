import __init__
class Channel(object):
	"""Channel is responsible for collecting the input information, and use call back
		to return the data to the adapter. It's just a interface"""
	def __init__(self):
		super(Channel, self).__init__()
		pass;


	def start_listening(self, callback):
		'''this method to invoke the Channel to start to allow user input For example:
		For command line, way of input, the program will stop running waiting for user input.
		For network, it will create a listener for listening
		 '''
		pass;
