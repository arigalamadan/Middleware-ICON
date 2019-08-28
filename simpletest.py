#!/usr/bin/python

import socket
import subprocess
import sys


# Get teh host information 

socket = socket.gethostbyaddr(socket.gethostname())[0] 
def findservicename():
    servicename = 'tcp'
remoteservicename = socket.getservbyport(socket.gethostname)

# We also put in some error handling for catching errors

try:
    for port in range(1,9000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('socket.gethostname()', port))
        if result == 0:
            print "Port {}:     Open".format(port) 
	    print("Port {}: %s => servicename: %s" %(port, socket.getservbyport(port, servicename))) 
     print ("Port: %s => servicename: %s" %(7004, socket.getservbyport(7004, 'udp')))

            print "server running"
#       else:
#           print"server is shutdown"
        sock.close()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit() 

findservicename()

# Printing the information to screen
print 'Scanning Completed: ', 
