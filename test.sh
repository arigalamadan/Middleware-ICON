#!/bin/bash

#Mentioned valid service name
service=test3.py

#Checking for service pid value
process='ps -ef | grep -v grep | grep -i $service | wc -l'

case $process in
[2]*)

echo "OK -$service is running"
exit 0
;;

[0]*)

echo "CRITICAL -$service is not running"
exit 2
;;

[1]*)

echo "WARNING -$service please check the service"
exit 1
;;

esac

