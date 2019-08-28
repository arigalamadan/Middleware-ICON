import socket
import subprocess
import sys

def find_service_name(port):
    if port == 7004:
       portname = 'udp'
    else:
        protocolname = 'tcp'
    print ("Port: %s => service name: %s" %(port, socket.getservbyport(port, protocolname)))

# Ask for input
remoteServer    ="eu-middleware-sb1.iconcr.com"
remoteServerIP  = socket.gethostbyname(remoteServer)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    for port in range(1,8443):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(((remoteServer),port))
        protocolname = "tcp"
        if result == 0:
            print (port)
            find_service_name(port), "server running"
#       else:
#           print"server is shutdown"
        sock.close()
except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
except socket.error:
    print "Couldn't connect to server"
    sys.exit()
#Printing the information to screen
print 'Scanning Completed: ', 
