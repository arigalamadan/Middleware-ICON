import socket
import subprocess
import sys
import os
#import current

# Ask for input  
#remoteServer = raw_input("Enter a remote host to scan: ")
#remoteServerIP = socket.gethostbyname(remoteServer)

#try: 
#    for port in range(1,9000):
#	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#	result = sock.connect_ex('eu-middleware-sb1', port)
#	protocolname = "tcp"
#	port = getservbyname(service, 'tcp');
#	print("port: %s => servicename: %s " %(port, socket.getservbyport(port, protocolname))) 
#	if result == 0:
#	     print "Port {}: Open".format(port), 'server running' 
#	sock.close() 
#
#except socket.gaierror:
#    print 'Hostname could not be resolved. Exiting'
#    sys.exit()

#except socket.error:
#    print "Couldn't connect to server"
#    sys.exit()

#Printing the information to screen
#print 'Scanning Completed: ',







# Ask for input
#remoteServer    = raw_input("Enter a remote host to scan: ")
#remoteServerIP  = socket.gethostbyname(remoteServer)


hostname = socket.gethostname()

#TCP protocol

currentProtocol = "TCP"
protoConstant = socket.getprotobyname(currentProtocol)
print("Socket module constant associated with protocol {}")
print (currentProtocol) 

# We also put in some error handling for catching errors

try:
    for port in range(1,9000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((socket.gethostbyname(hostname), port))
#	servers=cmo.getServers()
#	print "\t"+cmo.getName()+"domain current status"
#	for server in server:
#		status=state(server.getName(),server.getType())
        if result == 0:
            print "Port {}:     Open".format(port),	socket.gethostbyname(hostname),		'server running'
        sock.close()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

#except socket.error:
#    print "Couldn't connect to server"
#    sys.exit()

# Printing the information to screen
print 'Scanning Completed: ',
