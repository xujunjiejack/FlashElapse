from channel_api import Channel
from user_commands.start_preview_cmd import StartPreviewCmd
from user_commands.test_cmd import TestCmd
from collections import OrderedDict
import json
import sys
from user_commands.cmd_manager import CommandManager

class UserInputError(Exception): pass;

class CommandLineChannel(Channel):

	def __init__(self, cmd_manager):
		super(CommandLineChannel,self).__init__(cmd_manager)

	def start_listening(self, callback_with_data):
		
		def ask_user_input(prompts):
					print (prompts)
					x = input("Please enter the command you want to use"
						" in interger: ")
					return x
		def process_before_user_input(cmd_manager, reactor):

			option_num = 0
			prompts = ""
			for cmd in cmd_manager:
				try:
					option_num += 1
					cmdl_channel = cmd().get_cmdl_channel_instance()
					cmd_prompt = cmdl_channel.get_prompt_line()
					react_func = cmdl_channel.get_react_func()
					
					# log reactor
					reactor.log_react_func_to_reactor(option_num, react_func)
					prompts += "\n%s: %s " %(option_num, cmd_prompt)
				except Exception as e:
					print(e)
			return prompts, option_num
		def validate_user_input(user_input,option_num):
			option = int(user_input)
			if option not in range(1,option_num+1):
				raise ValueError("Please enter the number for one of the function")
			return option
		def encode_data(data_dict):
			return json.dumps(data_dict)

		reactor = CommandLineReactor()
		cmd_manager = self.cmd_manager
		while True:
			try:

				# This includes add the prompt and log every commands reactor
				prompts, option_total = process_before_user_input(cmd_manager, reactor)
				user_input = ask_user_input(prompts)
				user_input = validate_user_input(user_input, option_total)
				
				# call the command to react to encode the string
				data_dict = reactor.get_react_func(user_input)()
				encoded_data = encode_data(data_dict)

				callback_with_data(encoded_data)
			
			except ValueError as e:
				print (e)
				print ("Input invalid, please try again")
		pass

	def end_listening(self):
		print ("The user console is quitting. Thank you for using")

def unitTest():
	c = CommandLineChannel()
	c.start_listening()

class CommandLineReactor():

	def __init__(self):
		self.logger = {}

	def log_react_func_to_reactor(self,option_num, react_func):
		"""option_num is an integer"""
		self.logger[option_num] = react_func

	def get_react_func(self, option_num):
		"""The option num should be validated before"""
		try:
			react_func = self.logger[option_num]
			return react_func
		except Exception as e:
			raise e

class CommandLineOptions():

	def __init__(self):
		self.options = OrderedDict()
		self.options["1"] = "Start Previewing"
		self.options["2"] = "Making videos"
		self.options["3"] = "Test"
		self.options["4"] = "Quit"
		

	def displayOptions(self):
		for optionNum in self.options:
			print ("%s : %s" %(optionNum, self.options[optionNum]))

	def encodeCommandBasedOnOption(self,optionNum):
		''''''
		def encode_cmd_with_json(cmd):
			return json.dumps(cmd.__dict__)

		cmd = ""
		if optionNum == "1":		
			cmd = StartPreviewCmd()
			#no setting

		elif optionNum == "2":
			print ("Sorry, it's not useable")

		elif optionNum == "3":
			print("Preparing %s" %cmd)
			cmd = TestCmd()

		elif optionNum == "4":
			print("system exiting")
			sys.exit(0)

		else: 
			raise ValueError("Input is not valid")

		return encode_cmd_with_json(cmd)


		option = CommandLineOptions()
		while True:
			option.displayOptions()
			user_opt = input("Please enter the option number: ")
			try:
				encode_data = option.encodeCommandBasedOnOption(user_opt)
				print("****encoding data is %s******"%encode_data)
				callback_with_data(encode_data)
			except Exception as e:
				print (e,  "Please try again")

		'''def lateruse():	
			def check_string_as_integer(string):
				try:
					num = int(string)
					return num
				except ValueError as e:
					raise UserInputError("Please enter an integer")

			def check_int_positive(num):
				if num <= 0:
					raise UserInputError("Frames per minute can't be negative or zero. ")

			def read_frame_per_minute_console():
				
				while True:
					try: 
						fpm = input("Please enter the number of frames per minue: ")
						fpm = check_string_as_integer(fpm)
						check_int_positive(fpm)
						return fpm

					except UserInputError as e:
						print(e,"\nPlease try again.")

			def read_time_of_experiment():
				while True:
					try:
						time_exp = input("Please enter the time length of actual" 
											"experiment in minutes: ")
						time_exp = check_string_as_integer(time_exp)
						check_int_positive(time_exp)
						return time_exp
					except UserInputError as e:
						print(e , "\nPlease try again.")

			fpm = read_frame_per_minute_console() #fpm is interger
			time_exp = read_time_of_experiment() #time_exp is interger
			data = [fpm, time_exp]
			callback_with_data(data)
			print ("fpm: %s, time_exp: %s" %(fpm, time_exp))'''
