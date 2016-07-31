''' This file contains the method for creating the channel and the Channel interface itself.

'''
from command_line_channel import CommandLineChannel

def create_channel(source):

	print ("source is %s "%(source))
	if source == 'cmd':
		return CommandLineChannel()
	pass