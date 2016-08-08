''' This file contains the method for creating the channel and the Channel interface itself.

'''
from command_line_channel import CommandLineChannel
from network_channel import SocketNetworkChannel

def create_channel(source, cmd_manager):

	print ("source is %s "%(source))
	if source == 'cmd':
		return CommandLineChannel(cmd_manager)
	elif source == 'lan':
		return SocketNetworkChannel(cmd_manager)

