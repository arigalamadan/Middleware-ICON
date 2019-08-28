#!/bin/bash

ports="7004 7004 8443"
service="JAVA  weblogic  tomcat"
c=1

echo "Running services status:"

/bin/netstat -tulpn | grep -vE '^Active|Proto' | while read LINE
do
 # get active port name and use : as delimiter
 t=$(echo $LINE | awk '{ print $4}' | cut -d: -f2)
 [ "$t" == "" ] && t=-1 || :
 # get service name from $services and : as delimiter
 sname=$(echo $service | cut -d' ' -f$c)
 status="$sname: No"
 # now compare port
 for i in $ports
 do
  if [ $i -eq $t ]; then
   status="$sname: Ok"
  fi
 done
 # display service status as OK or NO
 echo "$status"
 #next service please
 c=$( expr $c + 1 )
 # break afer 3 services
 [ $c -ge 4 ] && break || :
done

