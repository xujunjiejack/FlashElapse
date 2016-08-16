import socket
import sys

# it can also be called client. There may be many client that a server needs to deal with.
# They log on the port and start the conversation

class CommandSender(object):

	def __init__(self):
		self.connection_address = ('172.16.0.185', 12011)

	def format_message(self,text):
		return self.make_length_num_8_long_string(len(text)) + text

	def make_length_num_8_long_string(self,length):
		if length >= 10000000:
			raise ValueError("The string length is too big")

		return ("%08d"%length)

	def send(self, text):
		sender = socket.socket()
		sender.connect(self.connection_address)
		try:
			message = self.format_message(text)
			message_encoded =message.encode(encoding = "UTF-8")	
			sender.send(message_encoded)
			print ("message has been sent")
		except Exception as e:
			print (e)
		finally:
			print ("The sendering is closing")
			sender.close()

'''	def format_message(text):
		return make_length_num_8_long_string(len(text)) + text

	def make_length_num_8_long_string(length):
		if length >= 10000000:
			raise ValueError("The string length is too big")

		return ("%08d"%length)

	sender = socket.socket()
	connection_address = ('localhost', 12011)
	sender.connect(connection_address)
	try:
		message = format_message(text)
		message_encoded = message.encode(encoding = "UTF-8")	
		sender.send(message_encoded)
		print ("message has been sent")
	except Exception as e:
		print (e)
	finally:
		print ("The sendering is closing")
		sender.close()
'''