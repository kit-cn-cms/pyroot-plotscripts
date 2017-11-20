import os
import sys
import subprocess
import stat

cmsswpath=os.getenv("CMSSW_BASE")

def create_script(cmsswpath,outputDir,workdir,card):
    script='#!/bin/bash\n'
    script+='export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch\n'
    script+='source $VO_CMS_SW_DIR/cmsset_default.sh\n'
    script+='cd '+cmsswpath+'/src\neval `scram runtime -sh`\n'
    script+='cd '+workdir+'\n'
    script+='ulimit -s unlimited \n'
    script+='text2workspace.py '+card+'\n'
    filename='scripts/'+'t2w'+'_'+card.replace('.txt','')+'.sh'
    f=open(filename,'w')
    f.write(script)
    f.close()
    st = os.stat(filename)
    os.chmod(filename, st.st_mode | stat.S_IEXEC)



if not os.path.exists("scripts"):
    os.makedirs("scripts")

if not os.path.exists("logs"):
    os.makedirs("logs")

incards=sys.argv[1:]
pwd=os.getcwd()
for card in incards:
  create_script(cmsswpath,"scripts",pwd,card)

