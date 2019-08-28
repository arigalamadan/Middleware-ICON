#import sys
#import subprocess


#class ServiceMonitor(object):

#    def __init__(self, service):
#        self.service = service

#    def is_active(self):
#        """Return True if service is running"""
#        cmd = '/bin/systemctl status %s.service' % self.service
#        proc = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)
#        stdout_list = proc.communicate()[0].split('\n')
#        for line in stdout_list:
#            if 'Active:' in line:
#                if '(running)' in line:
#                    return True
#        return False

#    def start(self):
#        cmd = '/bin/systemctl start %s.service' % self.service
#        proc = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)
#        proc.communicate()

#if __name__ == '__main__':
    # TODO: Show usage                                                 
#    monitor = ServiceMonitor(sys.argv[1])
#    if not monitor.is_active():
#        monitor.start() 


import sys
import subprocess
import socket
remoteServer = 'eu-middleware-sb1.iconcr.com'
remoteserver_IP = socket.gethostbyname
p = subprocess.Popen(["ps", "-a"], stdout=subprocess.PIPE)
out, err = p.communicate()
if ('Httpd' in str(out)):
    print('Httpd running')
if ('mysql' in str(out)):
    print('mysql running')

