import socket, os
import subprocess
import sys
import connect
import urllib2 

# Getting remote host information

socket.gethostbyaddr(socket.gethostname())[0]


# Modify the server information accordingly 

username = 'weblogic'
password = 'weblogic1' 
URL = 'http://eu-middleware-sb1:7004'

#connect(username, password, URL)
#domainconfig()
#serverList = cmo.getServers();

#domainRuntime()
#cd ('/ServerLifeCycleRuntimes/')

#for server in serverList:
#    name = server.getname()
#    cd(name)
#    serverState=cmo.getState()
#    print " Server: " + name + ' [ ' + serverState + '] ' 
#    cd ('..')   

# We also put in some error handling for catching errors

try:
    for port in range(1, 9000):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(((socket.gethostname()), port))
        if result == 0:
            print "Port {}:	Open".format(port), 'server is running' 
#	else:
#	    print "Port {}:      Open".format(port), 'server is shutdown' 
        sock.close()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit()

# Printing the information to screen
print 'Scanning Completed: ', 
