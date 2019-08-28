import os
import socket
import subprocess 
import sys 

#Get the hostname information 

socket.gethostbyaddr(socket.gethostname())[0] 

try:
   for port in range(1, 9000):  
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
      result = sock.connect_ex(((socket.gethostname()), port))
      if result == 0: 
	print "Port{}:		Open".format(port), 	'server is running' 
      sock.close()
except socket.error:
	print "couldn't connect to server"
	sys.exit()
# printing the information to screen
print 'scanning completed: ',

 

