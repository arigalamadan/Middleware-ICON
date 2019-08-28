import socket
import subprocess 
import os 


#Ask for input

socket = socket.gethostbyaddr(socket.gethostname())[0] 
os.system('ps aux | grep oracle | grep -v grep | wc -l')
if ("Active: active(running)" in status): 

from subprocess import call 

command = raw_input('Please  enter service name : ')

call (["/etc/init.d/"+command, "status"]


