import subprocess
import os
import sys


def reportDomainHealth('weblogic', 'weblogic1', 't3://eu-middleware-sb1:7004/'):
    connect('weblogic', 'weblogic1', 't3://eu-middleware-sb1:7004')
    domainRuntime()
    print "Found Servers: "
    serverList=ls('ServerRuntimes');
    serverList=serverList.split()
    print ("Server", "Threads", "HoggingThreads", "QueueLength", "Heap_Free", "HealthState")
    print "----------------------------------------------------------------------------------------------------------------"
    for i in range(len(serverList)):
        if serverList[i] != 'dr--':
            server_st=get('ServerRuntimes/' + serverList[i] + '/HealthState')
            server_tc=get('ServerRuntimes/' + serverList[i] + '/ThreadPoolRuntime/ThreadPoolRuntime/ExecuteThreadTotalCount')
            server_hog=get('ServerRuntimes/' + serverList[i] + '/ThreadPoolRuntime/ThreadPoolRuntime/HoggingThreadCount')
            server_ql=get('ServerRuntimes/' + serverList[i] + '/ThreadPoolRuntime/ThreadPoolRuntime/QueueLength')
            server_hpfp=get('ServerRuntimes/' + serverList[i] + '/JVMRuntime/' + serverList[i] + '/HeapFreePercent')
            print "%15s %15s %20s %15s %15s %40s" % (serverList[i],str(server_tc),str(server_hog),str(server_ql),str(server_hpfp)+"%",str(server_st))
    print "================================================================="

reportDomainHealth('weblogic', 'weblogic1','http://eu-middleware-sb1:7004') 


