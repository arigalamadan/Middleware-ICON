import os
import subprocess
import commands


output = commands.getoutput('ps -ef')
if 'httpd' in output:
    print("httpd is up an running!")


#def is_service_running(name):
#    with open(os.devnull, 'wb') as show_output:
#        exit_code = subprocess.Popen(['service', 'name', 'status'], stdout=show_output, stderr=show_output).wait()
#        return exit_code == 0


#if not is_service_running('tomcat'):
#    print 'tomcat is not running'




#    service = "tomcat"
#
#    p =  subprocess.Popen(["systemctl", "is-active",  service], stdout=subprocess.PIPE)
#    (output, err) = p.communicate()
#    output = output.decode('utf-8')
#
#    print(output)
