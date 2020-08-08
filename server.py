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
#binding the socket and listening for connections 
def bind_socket():
	try:
		global host
		global s
		global port		
		print("binding the port "+str(port))
		s.bind((host,port))#tuple to bind the host and the socket 
		s.listen(5)
		#here 5 is the no of bad connections it will tolorate

	except socket.error as msg:
		print("socket binding error "+str(msg)+"\n retrying")
		bind_socket()
