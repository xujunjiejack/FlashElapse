import socket
import csv

client = socket.socket()

server_address = ('localhost', 10000)

client.bind(server_address)

client.listen(1)

while True:
	# Wait for a connection
	print >> sys.stderr, 'waiting for a connection'
	conne, client_address = 

