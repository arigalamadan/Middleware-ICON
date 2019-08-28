import os
import commands

service_name = "oracle"

def check_service_status(service_name):

        status = os.system('systemctl status '+service_name+ '')
        return status

def main():

        if (check_service_status(service_name) == 0):
                print "Server Running"
        else:
                print "Server Shutdown"
main()


