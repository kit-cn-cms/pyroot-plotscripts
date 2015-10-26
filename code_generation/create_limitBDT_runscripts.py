ttbarfiles=['/nfs/dust/cms/user/hmildner/trees1019/ttbar_nominal.root']
samples=[]
samples+=('ttbarPlusBBbar',ttbarfiles)
samples+=('ttbarPlusB',ttbarfiles)
samples+=('ttbarPlus2B',ttbarfiles)
samples+=('ttbarPlusCCbar',ttbarfiles)
tthfiles+=['/nfs/dust/cms/user/hmildner/trees1019/ttHbb_nominal.root','/nfs/dust/cms/user/hmildner/trees1019/ttHnonbb_nominal.root']
samples+=('ttH125',tthfiles)

outpath='/nfs/dust/cms/user/hmildner/fastsim/tthbb72/'
scriptpath='/nfs/dust/cms/user/hmildner/BoostedAnalyzer_runscripts_NAF/alternative_runscripts_python/scripts_fastsim/'
cmsswcfgpath='/nfs/dust/cms/user/hmildner/fastsim/run2fastsim/CMSSW_7_2_3/src/fastsimtest.py'
cmsswpath='/nfs/dust/cms/user/hmildner/fastsim/run2fastsim/CMSSW_7_2_3/'

events_per_job=1000000

import os
import sys
import stat


if not os.path.exists(scriptpath):
    os.makedirs(scriptpath)

if not os.path.exists(outpath):
    os.makedirs(outpath)

if not os.path.exists(cmsswpath):
    print 'WRONG CMSSW PATH!'
    print cmsswpath
    sys.exit()

if not os.path.exists(cmsswcfgpath):
    print 'WRONG CMSSW CONFIG PATH!'
    print cmsswcfgpath
    sys.exit()

for s in samples:
    for f in s[1]:
        if not os.path.exists(f):
            print 'FILE DOES NOT EXIST!'
            print f
            sys.exit()
        
for s in samples:
    getEventsInFiles(s[1])

script="""#!/bin/bash                                                                                                                                                  
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch                                                                                                                                
source $VO_CMS_SW_DIR/cmsset_default.sh                                                                                                                                
"""
script+='cd '+cmsswpath+'/src\neval `scram runtime -sh`\n'


maxevents=nevents/njobs
for ijob in range(njobs):
    skip=maxevents*ijob
    jobstr=str(ijob)
    if ijob<1000:
        jobstr='0'+jobstr
    if ijob<100:
        jobstr='0'+jobstr
    if ijob<10:
        jobstr='0'+jobstr
    filename=scriptpath+'/'+samplename+'_'+jobstr+'.sh'
    f=open(filename,'w')
    f.write(script)
    f.write('export PROCESSNAME="'+samplename+'"\n')
    f.write('export OUTFILENAME="'+outpath+'/'+samplename+'_'+str(ijob)+'"\n')
    f.write('export SKIPEVENTS="'+str(skip)+'"\n')
    f.write('export MAXEVENTS="'+str(maxevents)+'"\n')
    f.write('cmsRun '+cmsswcfgpath+'\n')
    st = os.stat(filename)
    os.chmod(filename, st.st_mode | stat.S_IEXEC)
