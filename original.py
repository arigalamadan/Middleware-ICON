import subprocess, sys
import socket, os
import connect
import urllib2 

socket = socket.gethostbyaddr(socket.gethostname())[0]
os.system("ps -ef | grep oracle")
os.system("nohup $DOMAIN_HOME/bin/startNodeManager.sh")

# by using connect module the weblogic hosts  

#client = connect.Client()

#response = urllib2.urlopen("t3://eu-middleware-sb1:7004") 

url = "response"

# connect('username' 'password' 'url') 
connect('weblogic' 'weblogic1' 't3://eu-middleware-sb1:7004') 
