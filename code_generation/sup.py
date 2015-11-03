#!/usr/bin/env python
# submits alls *.sh files to cluster
# usage: ./sup.py path/to/scripts [script_pattern]
import os
import sys
import datetime
from subprocess import call
pattern=''
path=''
files=[]
if len(sys.argv) > 1 and sys.argv[1]=='-f':
    files = [os.path.join(root, name)
             for root, dirs, files in os.walk('./'+path)
             for name in files
             if pattern in name and name.endswith((".sh"))]
    if len(sys.argv) > 2:
        path= sys.argv[2]+'/'
    if len(sys.argv) > 3:
        pattern= sys.argv[3]

else:
    files=sys.argv[1:]

if not os.path.exists('logs'):
    os.makedirs('logs')

for f in files:
    call(['qsub', '-cwd', '-S', '/bin/bash','-l', 'h=bird*', '-hard','-l', 'os=sld6', '-l' ,'h_vmem=2000M', '-l', 's_vmem=2000M' ,'-o', 'logs/$JOB_NAME.o$JOB_ID', '-e', 'logs/$JOB_NAME.e$JOB_ID', f])
