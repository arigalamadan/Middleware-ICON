import socket
import subprocess
import sys

# Get host information

# socket.gethostbyaddr(socket.gethostname())[0]

host_name = socket.gethostname()
#sock_name = socket.gethostname()


#Get the server status 

domainRuntime()
for server in cmo.getServerLifeCycleRuntimes():
servers=cmo.getServers()
    print servers
    print "-------------------------------------"
    print "\t" + cmo.getName() + "domain status"
    print "--------------------------------------"
    for server in servers:
     state(server.getName(), server.getType())
    print "--------------------------------------" 

# We also put in some error handling for catching errors

try:
    for port in range(1,9000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(((socket.gethostname()),port))
        if result == 0:
            print "Port {}:     Open".format(port), (socket.gethostbyname(host_name)), 'server running', '\n'
	"state(server.getName(), server.getType(), server.getState())"
#        else:
#            print"server is shutdown"
        sock.close()


except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
except socket.error:
    print "Couldn't connect to server"
    sys.exit()

# Printing the information to screen
print 'Scanning Completed: ',
