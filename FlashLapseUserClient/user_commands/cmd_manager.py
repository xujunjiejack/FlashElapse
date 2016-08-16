import json
import os
import sys
from importlib import import_module

# I need to find a way that's not hard code. One way is to instantiate the command manager
# after the whole program starts
#config_file_path ="/home/pi/Desktop/FlashLapse/FlashLapse/user_commands/command_config.json"
config_file_path = "/Users/xu/Desktop/Projects/FlashLapse/FlashLapse/user_commands/command_config.json"
class  CommandManager(object):
	"""docstring for  CommandManager"""
	def __init__(self):
		super(CommandManager, self).__init__()
		file = open(config_file_path,"r")
		self.config = json.load(file)
		self.cmd_list = self.get_cmd_class_list()
		self.index = 0

	def get_cmd_class_list(self):
		
		cmd_list = [None] * len(self.config)
		if cmd_list == 0:
			print("No command available")
			sys.exit(2)

		for cmd_class_name in self.config:
			cmd_class_info = self.config[cmd_class_name]
			CmdClass = self._create_class_(cmd_class_name, cmd_class_info)
			#self._parse_rest_(CmdClass,cmd_class_info)
			cmd_position = self._get_position_(cmd_class_info)
			cmd_list[cmd_position] = CmdClass
		return cmd_list

	# this is a common pattern for class in json in our configuration file
	def _create_class_(self, class_name,class_info):
		module_name = class_info['Module']
		module =  import_module(module_name)
		Class = getattr(module, class_name)
		return Class
	
	def _get_position_(self, cmd_class_info):
		position = cmd_class_info["Position"]
		return position

	def _parse_rest_(self,CmdClass, cmd_class_info):
		'''This method parse the affliate class for command for further use'''
		for affliate_class_purpose in cmd_class_info:
			#"Module has already been parsed"
			if affliate_class_purpose == 'Module':
				continue
			else:
				affliate_class_def = cmd_class_info[affliate_class_purpose]
				for affliate_class_name in affliate_class_def:
					affliate_class_info = affliate_class_def[affliate_class_name]
					affliate_class = self._create_class_(affliate_class_name,affliate_class_info)
					setattr(CmdClass,affliate_class_purpose,affliate_class)

	def get_cmd_instance_list(self):
		cmd_instances = []
		for cmd_class in self.cmd_list:
			instance = cmd_class()
			cmd_instances.append(instance)
		return cmd_instances

	def __next__(self):
		if self.index >= len(self.cmd_list):
			self.index = 0
			raise StopIteration

		item = self.cmd_list[self.index]
		self.index += 1
		return item

	def __iter__(self):
		return iter(self.cmd_list)

	def __len__(self):
		return len(self.cmd_list)

def test_for_user_input():
	cmd_manager = CommandManager()

	option_num = len(cmd_manager)

	def user_input():
		x = input("Please enter the command you want to use"
			" in interger")
	user_input_after_prompt = user_input
		
	for cmd in cmd_manager:
		cmd_cmdl_channel = cmd().get_cmdl_channel_instance()
		user_input_after_prompt = cmd_cmdl_channel.get_line_prompt(user_input_after_prompt,option_num)
		option_num -=1

	user_input_after_prompt()

def test_all_class():
	cmd_manager = CommandManager()
	for cmd in cmd_manager:
		print (cmd)
