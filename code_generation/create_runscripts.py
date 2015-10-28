import glob
import os
import sys
import stat
import ROOT

mode='_test'

non_weight_systematics=['nominal','jesup','jesdown','jerup','jerdown']
suffixes=['','_CMS_scale_jUp','_CMS_scale_jDown','_CMS_res_jUp','_CMS_res_jDown']
pwd='/afs/desy.de/user/h/hmildner/pyroot-plotscripts/code_generation/'
programs=[pwd+'plot_syst'+mode,
          pwd+'plot_nominal'+mode,
          pwd+'plot_nominal'+mode,
          pwd+'plot_nominal'+mode,
          pwd+'plot_nominal'+mode]

outpath='/nfs/dust/cms/user/hmildner/limitplots'+mode+'/'
scriptpath='/afs/desy.de/user/h/hmildner/pyroot-plotscripts/code_generation/runscripts'+mode+'/'
cmsswpath='/afs/desy.de/user/h/hmildner/CMSSW_7_4_14'


ttbarfiles={}
ttbarfiles['nominal']=['/nfs/dust/cms/user/hmildner/trees1027/ttbar/ttbar*nominal*.root']
ttbarfiles['jesup']=['/nfs/dust/cms/user/hmildner/trees1027/ttbar/ttbar*JESUP*.root']
ttbarfiles['jesdown']=['/nfs/dust/cms/user/hmildner/trees1027/ttbar/ttbar*JESDOWN*.root']
ttbarfiles['jerup']=['/nfs/dust/cms/user/hmildner/trees1027/ttbar/ttbar*JERUP*.root']
ttbarfiles['jerdown']=['/nfs/dust/cms/user/hmildner/trees1027/ttbar/ttbar*JERDOWN*.root']

tthfiles={}
tthfiles['nominal']=['/nfs/dust/cms/user/hmildner/trees1027/ttHbb/ttHbb*nominal*.root','/nfs/dust/cms/user/hmildner/trees1027/ttHnonbb/ttHnonbb*nominal*.root']
tthfiles['jesup']=['/nfs/dust/cms/user/hmildner/trees1027/ttHbb/ttHbb*JESUP*.root','/nfs/dust/cms/user/hmildner/trees1027/ttHnonbb/ttHnonbb*JESUP*.root']
tthfiles['jesdown']=['/nfs/dust/cms/user/hmildner/trees1027/ttHbb/ttHbb*JESDOWN*.root','/nfs/dust/cms/user/hmildner/trees1027/ttHnonbb/ttHnonbb*JESDOWN*.root']
tthfiles['jerup']=['/nfs/dust/cms/user/hmildner/trees1027/ttHbb/ttHbb*JERUP*.root','/nfs/dust/cms/user/hmildner/trees1027/ttHnonbb/ttHnonbb*JERUP*.root']
tthfiles['jerdown']=['/nfs/dust/cms/user/hmildner/trees1027/ttHbb/ttHbb*JERDOWN*.root','/nfs/dust/cms/user/hmildner/trees1027/ttHnonbb/ttHnonbb*JERDOWN*.root']

ttbar_subsamples=['ttbarPlusBBbar','ttbarPlusB','ttbarPlus2B','ttbarPlusCCbar','ttbarOther']

samplelists=[]
for s in non_weight_systematics:
    samples=[]
    samples+=[('ttH125',tthfiles[s])]
    for p in ttbar_subsamples:
        samples+=[(p,ttbarfiles[s])]
#    samples+=[('data_obs',ttbarfiles['nominal'])]
    samplelists.append(samples)

#events_per_job=1000000
files_per_job=20

if not os.path.exists(scriptpath):
    os.makedirs(scriptpath)

if not os.path.exists(outpath):
    os.makedirs(outpath)

if not os.path.exists(cmsswpath):
    print 'WRONG CMSSW PATH!'
    print cmsswpath
    sys.exit()

def getEventsInFiles(files):
    l=[]
    for f in files:
        tf=ROOT.TFile(f, 'readonly')
        tree=tf.Get('MVATree')
        l.append(tree.GetEntries())
        tf.Close()
    return l

       
def createScript(scriptname,programpath,processname,filenames,outfilename,maxevents,skipevents,suffix):
    script="#!/bin/bash \n"
    script+="export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch \n"
    script+="source $VO_CMS_SW_DIR/cmsset_default.sh \n"
    script+='cd '+cmsswpath+'/src\neval `scram runtime -sh`\n'
    script+='cd - \n'
    script+='export PROCESSNAME="'+processname+'"\n'
    script+='export FILENAMES="'+filenames+'"\n'
    script+='export OUTFILENAME="'+outfilename+'"\n'
    script+='export MAXEVENTS="'+str(maxevents)+'"\n'
    script+='export SKIPEVENTS="'+str(skipevents)+'"\n'
    script+='export SUFFIX="'+suffix+'"\n'
    script+=programpath+'\n'
    f=open(scriptname,'w')
    f.write(script)
    f.close()
    st = os.stat(scriptname)
    os.chmod(scriptname, st.st_mode | stat.S_IEXEC)

    
def createScriptsForSamples(samples,suffix,programpath):
    samples_=[]
    for s in samples:
        allfiles=[]
        neventsperfile=[]
        for f in s[1]:
            allfiles+=glob.glob(f)
#            neventsperfile+=getEventsInFiles(allfiles)
#            samples_.append((s[0],allfiles,neventsperfile,neventsperfile))
            samples_.append((s[0],allfiles,neventsperfile))
    samples=samples_

    for sample in samples:
        process=sample[0]
        files=sample[1]
#        nevents=sample[2]
        ijob=1
#        events_in_job=0
        nfiles=0
        files_in_job=[]
#        for f,n in zip(files,nevents):
        for f in files:
            files_in_job.append(f)
            nfiles+=1
#            events_in_job+=n
#            if events_in_job>=events_per_job or f == files[-1]:
            if nfiles>=files_per_job or f == files[-1]:
                scriptname=scriptpath+'/'+process+suffix+'_'+str(ijob)+'.sh'
                filenames=' '.join(files_in_job)
                outfilename=outpath+'/'+process+suffix+'_'+str(ijob)+'.root'
                maxevents=9999999999
                skipevents=0
                createScript(scriptname,programpath,process,filenames,outfilename,maxevents,skipevents,suffix)
                ijob+=1
                nfiles=0
                files_in_job=[]

for sa,su,pr in zip(samplelists,suffixes,programs):
    createScriptsForSamples(sa,su,pr)
