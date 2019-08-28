#!/bin/usr/python

import socket
import sys
import subprocess 

# Ask for input
#remoteServer    = raw_input("Enter a remote host to scan: ")
#remoteServerIP  = socket.gethostbyname(remoteServer)

# We also put in some error handling for catching errors

try:
#    for port in range(1,9000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('eu-middleware-sb1.iconcr.com', 7004))
        if result == 0:
            print "Port {}:     Open".format(port), 'server running'
s.bind((eu-middleware-sb1.iconcr.com, port)) 
s.listen() 
conn, addr = s.accept() 
with conn:  
    print('Connected by', addr)  
while True: 
#  data = conn.recv(1,9000) 
  if not data: 
break 
conn.sendall(data)
