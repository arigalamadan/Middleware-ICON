import socket
import subprocess
import sys

# Get host information 

socket.gethostbyaddr(socket.gethostname())[0]

# We also put in some error handling for catching errors

try:
    for port in range(1,9000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(((socket.gethostname()),port))
        if result == 0:
            print "Port {}:     Open".format(port),	'', 	'server running'
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
