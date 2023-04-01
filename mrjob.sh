#!/bin/bash
/usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -files mapper.py,reducer.py -mapper 'python mapper.py' -reducer 'python reducer.py' -input /user/cloudera/Sample_Data.txt -output /user/cloudera/assignment
