#!/usr/bin/env python
# submits alls *.sh files to cluster
# usage: ./sup.py path/to/scripts [script_pattern]
import os
import sys
import datetime
pattern=''
path=''
if len(sys.argv) > 1:
    path= sys.argv[1]+'/'
if len(sys.argv) > 2:
    pattern= sys.argv[2]
from subprocess import call

if not os.path.exists('logs'):
    os.makedirs('logs')
logfile='logfile.txt'
if os.path.exists(logfile):
    logfile+=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
#f_list=open(logfile,'w')

files = [os.path.join(root, name)
                     for root, dirs, files in os.walk('./'+path)
                     for name in files
                     if pattern in name and name.endswith((".sh"))]
for f in files:
    call(['qsub', '-cwd', '-S', '/bin/bash','-l', 'h=bird*', '-hard','-l', 'os=sld6', '-l' ,'h_vmem=2000M', '-l', 's_vmem=2000M' ,'-o', 'logs/$JOB_NAME.o$JOB_ID', '-e', 'logs/$JOB_NAME.e$JOB_ID', f])
#    f_list.write(f+'\n')
#f_list.close()
