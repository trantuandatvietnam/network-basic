# modules
import socket
import sys

# Thực hiện tạo instance socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")
except socket.error as err:
    print ("socket creation failed with error %s" %(err))

# default port for socket
port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    print ("there was an error resolving the host")
    sys.exit()

# connecting to the server
s.connect((host_ip, port))
print ("the socket has successfully connected to google on PORT: " + host_ip)