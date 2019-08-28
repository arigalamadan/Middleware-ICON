#!/usr/bin/python

import socket
import subprocess
import sys
import os

# Ask for input
remoteServer    = raw_input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer) 

# We also put in some error handling for catching errors

try:
    for port in range(1,9000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(((remoteServerIP), port))
        if result == 0:
            print "Port {}:     Open".format(port)
            print "server running"
#        else:
#            print"server is shutdown"
        sock.close()

except socket.gaierror: 
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

#except socket.error:
#    print "Couldn't connect to server"
#    sys.exit()

def printFormat(serverName, serverState):
serverHealth=''
    serverName=serverName.ljust(20)

underlyingProtocol = "tcp" 

print("============>Service and their port number<========") 

for service in remoteServerIP:

    #get the port numberfor each application protocol which use TCP as underlying
    
    port = socket.getservbyname(service, underlyingProtocol) 

	    print("The service {} uses port number {} ".format(service, port))


# Printing the information to screen
print 'Scanning Completed: ',
