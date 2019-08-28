import socket
import sys
import os
import subprocess 



socket = socket.gethostbyaddr(socket.gethostname())[0]

def getserverStates()

result = sock.connect_ex(('socket.gethostname()', 7004))
cd('/apps/oracle/admin/domain/base_domain/servers' +ServerName); 
		print 'cd successful'; 
    ls(); 
    serverstate = cmo.getState() 
		print 'Serverstate'+serverstate; 
    if serverstate == "RUNNING":  
		print 'Server ' + servername + ' is :\033[1;32m' + serverstate + '\033[0m'; 
    elif serverstate == "STARTING": 
		print 'Server ' + servername + ' is :\033[1;33m' + serverstate + '\033[0m'; 
    elif serverState == "UNKNOWN": 
		print 'Server ' + servername + ' is :\033[1;34m' + serverstate + '\033[0m'; 
    else: 
		print 'Server ' + servername + ' is :\033[1;31m' + serverState + '\033[0m';  
    return serverstate 
#except:
        print 'Not able to get the' + serverState +'server status. Please try again\n';
        print 'Please check logged in user has full access to complete the requested operation on ' +servername+ '\n';
        exit()

gethostname()
getserverStates()
