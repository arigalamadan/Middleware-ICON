import socket
def get_Host_name_IP():
	try:
		host_name = socket.gethostname()
		host_ip = socket.gethostbyname(host_name)
		print host_name + '\033[1;32m';
		print host_ip + '\033[1;33m';
	except: 
		print("unable to get Hostname and IP")
#Driver code
get_Host_name_IP()

