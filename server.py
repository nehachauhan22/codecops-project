import socket
import sys
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
#Establish connection with the client (the socket must be listening )
def socket_accept():
	conn,address = s.accept()
	#accepts the connection and returns the obj of the connection adn 2nd is the ip add and the port 
	print("Connection has been Established with IP :"+address[0]+" and Port "+str(address[1]))
	send_commands(conn)


	#closing the connection
	conn.close()
	
#sending commands to the client
def send_commands(conn):  
	while True:
		cmd = input()
		if cmd=="quit":
			conn.close()
			s.close()
			sys.exit()
		
