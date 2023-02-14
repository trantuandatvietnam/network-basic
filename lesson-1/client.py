import socket            

s = socket.socket()        
 
# Define the port on which you want to connect
port = 12345               
 
# connect to the server on local computer
localhost_ip = "127.0.0.1"
s.connect((localhost_ip, port))
 
# receive data from the server and decoding to get the string.
print(s.recv(1024).decode())
# close the connection
s.close()    