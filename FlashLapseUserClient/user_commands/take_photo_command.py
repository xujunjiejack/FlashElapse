from command_api import Command, ExecutableCommand, CommandCMDLInput
from time import sleep
from _thread import start_new_thread
from __init__ import project_name

class TakePhotoCmd(Command):

	def __init__(self):
		super(TakePhotoCmd,self).__init__()
		
	def _set_cmd_name_(self):
		return "Take photo";

	def _set_cmdl_channel_class_(self):
		return TakePhotoCMDLChannel

	def decode(self,data_dict):
		return TakePhotoExeCmd(data_dict)


class TakePhotoExeCmd(ExecutableCommand):

		def __init__(self, data_dict = None):
				super(TakePhotoExeCmd, self).__init__()
				self.data_dict = data_dict
				#from __init__ import picamera,camera
				#self.camera = camera

		def _exe_(self):
				'''The actual execute code for doing command. Every exception it throws will
				be thrown to execute to be a command runtime error. This error handling has 
				been delegated to the execute(). Outsider should not use this method for run
				Developer needs to inheritance this method for the command to run
				'''
				time_interval = self.data_dict['time_interval']
				time_exp = self.data_dict['time_exp']
				total_frame_num = (time_exp * 60 / time_interval)
				
				def take_photo(total_frame_num, time_interval, project_name):
					i = 0
					while i < total_frame_num:
						sleep(time_interval)
						print("Taking photo %s"%i)
						i += 1

				start_new_thread(take_photo,(total_frame_num,time_interval, project_name))
				#self.camera.capture('/media/pi/%s/Mg-Fe/MG%s.jpg' % (project_name,i)) 

				


class TakePhotoCMDLChannel(CommandCMDLInput):
	def __init__(self):
		super(TakePhotoCMDLChannel, self).__init__()

	def get_prompt_line(self):
		return "Take photo"

	def _react_for_data_(self):
		data_dict = {}
		def check_string_as_integer(string):
				try:
					num = int(string)
					return num
				except ValueError as e:
					raise UserInputError("Please enter an integer")

		def check_int_positive(num):
				if num <= 0:
					raise UserInputError("Frames per minute can't be negative or zero. ")

		def read_time_interval_console():
				
				while True:
					try: 
						time_interval = input(" How many seconds do you want between"
							"each photo: ")
						time_interval = check_string_as_integer(time_interval)
						check_int_positive(time_interval)
						return time_interval

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

		time_interval = read_time_interval_console() #time_interval is interger
		time_exp = read_time_of_experiment() #time_exp is interger
		print ("time_interval: %s, time_exp: %s" %(time_interval, time_exp))
		data_dict['time_interval'] = time_interval
		data_dict['time_exp'] = time_exp
		return data_dict


class UserInputError (Exception):
	pass
