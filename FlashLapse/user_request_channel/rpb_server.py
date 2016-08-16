import socket
import sys
import io

class RpbServer(object):
	"""This is the server for rpb to receive the command, it return the string."""
	def __init__(self):
		super(RpbServer, self).__init__()
		self.server_address = ('localhost',12011)
		self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.server.bind(self.server_address)

	def check_message_length(self,num_string):
		try:
			if len(num_string) == 0:
				raise NoIncomingMessage("There is no incoming message")

			num = int(num_string)
			print("The length of the incoming message is %s"%num)
			return num
		except ValueError as e:
			raise Exception("The string is not in the right format")


	def read_message(self,message_length, connection):
		data = bytes()

		while len(data) < message_length:
			package = connection.recv(message_length - len(data))
			if (len(package) == 0):
				raise MessageCorruptd("There is no more available data. Data might be corrupted")
			data += package
		return data

	def listen(self, output_func):
		self.server.listen(1)
	#should I put every thing there?

		while True:
			connection, sender_address = self.server.accept()
			string = ''
			try:
				while True:
					message_length = self.check_message_length(connection.recv(8))
					data = self.read_message(message_length, connection)
					string += data.decode(encoding = "UTF-8")

					print("received '%s'"%string)
					output_func(string)

			except NoIncomingMessage as e:
				print (e)

			except MessageCorruptd as e:
				print (e)

			finally:
				print("connection is closing")
				connection.close()

	def close(self):
		self.server.close()

class NoIncomingMessage(Exception):
	"""docstring for NoIncomingMessage"""
	pass

class MessageCorruptd(Exception): pass
