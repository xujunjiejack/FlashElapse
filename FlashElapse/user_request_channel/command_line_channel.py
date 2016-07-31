from channel_api import Channel
from user_commands.start_preview_cmd import StartPreviewCmd
from user_commands.test_cmd import TestCmd
from collections import OrderedDict
import json
import sys

class UserInputError(Exception): pass;

class CommandLineChannel(Channel):

	def __init__(self):
		super(CommandLineChannel,self).__init__()

	def start_listening(self, callback_with_data):

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

		def lateruse():	
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
			print ("fpm: %s, time_exp: %s" %(fpm, time_exp))

def unitTest():
	c = CommandLineChannel()
	c.start_listening()

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
