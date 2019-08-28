import os
import subprocess


#name = sshd
#def is_service_running(name):
#    with open(os.devnull, 'wb') as hide_output:
#        exit_code = subprocess.Popen(['service', name, 'status'], stdout=hide_output, stderr=hide_output).wait()
#        return exit_code == 0


#if not is_service_running('sshd'):
#    print 'ssh is not running' 





service = "AdminServer"

p =  subprocess.Popen(["systemctl", "is-active",  service], stdout=subprocess.PIPE)
(output, err) = p.communicate()
output = output.decode('utf-8')

print(output)


