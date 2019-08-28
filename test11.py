#import socket, subprocess, os 


socket.gethostbyaddr(socket.gethostname())[0]
host_ip = socket.gethostbyname(socket.gethostname())
print ("Hostname: ", socket.gethostname()) 
print("IP: ", socket.gethostname())

if result == 0:
    print "server is running"
else:
    print "server is shutdown"
