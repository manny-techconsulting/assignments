#!/bin/bash 
if [ ! -d "/tmp/catbd125/emanuel/task" ]; then
    hdfs dfs -mkdir  /tmp/catbd125/emanuel/task
    hdfs dfs -chmod 777  /tmp/catbd125/emanuel/task
fi
