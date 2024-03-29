#!/bin/bash 

export JAVA_HOME=/usr/bin/java
export CATALINA_HOME=/home/arigalam/apache-tomcat-9.0.21
startScript=$CATALINA_HOME/bin/startup.sh

echo "Attempting to find process id for Tomcat . . ."
tomcatPID=$(ps -ef | grep tomcat | grep -v restart | awk '{print $2}')

if ["$tomcatPID" == ""]
then
    echo "Tomcat does not appear to be running . . ."
else
#    echo "Killing Tomcat using process id of $tomcatPID . . ."
#    kill -9 $tomcatPID
#    echo "Waiting for process $tomcatPID to end . . ."
    while ps -ef | grep $tomcatPID > /dev/null; do sleep 1; done
    echo "Process $tomcatPID has ended . . ."
fi

#echo "Deleting old log files . . ."
#find $CATALINA_HOME/logs/ -ctime +180 -daystart -exec ls "{}" \;

echo "Attempting to start Tomcat via $startScript . . ."
#nohup $startScript &
$startScript

echo "Process complete . . ." 

