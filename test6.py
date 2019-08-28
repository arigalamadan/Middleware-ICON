import socket

 

#Service list has a list of application protocols

serviceList = [

              "daytime",

              "ftp",

              "gopher",

              "http",

              "https",

              "imap",

              "kerberos-adm",

              "mysql-im",

              "pop3",

              "qotd",   #quote of the day

              "ssh",    #ssh remote login protocol

              "snmp",

              "smtp"

	      "weblogic"]

 

underlyingProtocol = "tcp"

 

print("======>Services and their port numbers<======")

for service in serviceList:               

    #get the port number for each application protocol which uses TCP as underlying

    portNum = socket.getservbyname(service, underlyingProtocol)

    print("The service {} uses port number {} ".format(service, portNum))

