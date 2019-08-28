#!/bin/python 

import socket 
 
def findservicename(): 
    protocolname = 'tcp'
    protocolName = socket.getservbyport(protocolname)  
for port in range (7004): 
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex(('eu-middleware-sb1',port))  
	if result == 0: 
	    print "Port {}:     Open".format(port), 'server is runing'
	    print ("Port: %s => service name: %s" %(port, socket.getservbyport(protocolName)))
#except socket.gaierror:
#    print 'Hostname could not be resolved. Exiting'
#    sys.exit() 

findservicename() 

