''' This is the main controller for the raspberry pi side 
	of work. The highest level in the back end
'''

from user_request_receiver import UserRequestAdapter
from user_request_receiver import UserRequestError

import sys
import json

class RpbController(object):
	''' This is the main controller for the raspberry pi side 
		of work. The highest level in the back end. 
		Its work involves receiving input from the user or the web.
		It also issue commands for camera to run.
		It supervises a lot of things
	'''


	def __init__(self, input_source):
		try:
			self.user_request_receiver = UserRequestAdapter(input_source)
		
		except UserRequestError as e:
			print (e.msg);
			sys.exit(2)

		pass;

	def run(self):

		self.user_request_receiver.start_listening(self.parse_data)
		pass;
		
	def parse_data(self, data):
		translator = CommandTranslator(data)
		cmd = translator.translate()
		cmd.execute()


class CommandTranslator(object):

	def __init__(self,data):
		'''Data passed in will become a json object '''
		try:
			self.data = json.loads(data)
		except Exception as e:
			print (e)
			raise TranslationError("Bad thing happened during translator")

	def translate(self):
		'''This needs to be able to be autogenerated'''

		from user_commands import cmd_header_const as headers

		cmd_name = self.data[headers.COMMAND_NAME_KEY]
		if cmd_name == headers.START_PREVIEW:
			from user_commands.start_preview_cmd import StartPreviewCmd
			return StartPreviewCmd().decode(data_dict = self.data)

		elif cmd_name == headers.TEST:
			from user_commands.test_cmd import TestCmd
			return TestCmd().decode(data_dict = self.data)

		raise TranslationError("Invalid Command")


class TranslationError(Exception):
	'''This exception indicates it has problem with the translation'''
	def __init__(self,*args,**kwargs):
		Exception.__init__(self,*args,**kwargs)




