
import sys
import os
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
port = 50000

try:
    s.bind((socket.gethostname() , port))
except socket.error as msg:
    print(str(msg))
s.listen(10)
conn, addr = s.accept()  
print 'Got connection from'+addr[0]+':'+str(addr[1]))
while 1:
        msg = s.recv(1024)
        print +addr[0]+, ' >> ', msg
        msg = raw_input('SERVER >>'),host
        s.send(msg)
s.close()
