from user_request_channel.rpb_server import RpbServer
from user_request_channel.channel_api import Channel

class SocketNetworkChannel(Channel):

	def __init__(self, cmd_manager):
		super(SocketNetworkChannel, self).__init__(cmd_manager)
		pass

	def start_listening(self, data_handle_func):
		self.rpb_server = RpbServer()
		self.rpb_server.listen(data_handle_func)
		'''Create the server on the raspberry side, I'm using the local host now'''

	def end_listening (self):
		self.rpb_server.close()