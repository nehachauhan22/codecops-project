import socket
def create_socket():
	try:
		global host
		global s
		global port
		host = ""
		port = 9999
		#a desired 4 digit number
		s = socket.socket()
	except socket.error as msg:
		print("socket creation error "+str(msg))