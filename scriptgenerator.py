import xml.etree.ElementTree as ET
import re
import subprocess
import ROOT
import datetime
import os
import sys
import stat
import time
import plotutils

ROOT.gROOT.SetBatch(True)

def getHead():
    return """#include "TChain.h"
#include "TBranch.h"
#include "TLorentzVector.h"
#include "TFile.h"
#include "TH1F.h"
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include "TMVA/Reader.h"

using namespace std;

void plot(){
  TH1F::SetDefaultSumw2();
  
  // open files
  TChain* chain = new TChain("MVATree");
  char* filenames = getenv ("FILENAMES");
  char* outfilename = getenv ("OUTFILENAME");
  string processname = string(getenv ("PROCESSNAME"));
  string suffix = string(getenv ("SUFFIX"));
  int maxevents = atoi(getenv ("MAXEVENTS"));
  int skipevents = atoi(getenv ("SKIPEVENTS"));
  int eventsAnalyzed=0;
  float sumOfWeights=0;

  string buf;
  stringstream ss(filenames); 
  while (ss >> buf){
    chain->Add(buf.c_str());
  }
  chain->SetBranchStatus("*",0);

  TFile* outfile=new TFile(outfilename,"RECREATE");    

  // initialize variables from tree
"""

class Variable():
    def __init__(self,name,vartype='F',arraylength=None):
        self.name=name
        self.vartype=vartype
        self.arraylength=arraylength

def initVar(v):
    var=v.name
    t=v.vartype
    isarray=v.arraylength!=None
    if isarray:
        if t=='F':
            text='  float* '+var+' = new float[100];\n'
        elif t=='I':
            text='  int* '+var+' = new int[100];\n'
        else: "UNKNOWN TYPE",t
    else:
        if t=='F':
            text='  float '+var+' = -999;\n'
        elif t=='I':
            text='  int '+var+' = -999;\n'
        else: "UNKNOWN TYPE",t
    return text

def initVarFromTree(v):
    isarray=v.arraylength!=None
    if isarray:
        text= initVar(v)
        text+='  chain->SetBranchAddress("'+v.name+'",'+v.name+');\n'
    else:
        text= initVar(v)
        text+='  chain->SetBranchAddress("'+v.name+'",&'+v.name+');\n'
    return text

def initHisto(name,nbins,xmin=0,xmax=0,title_=''):
    if title_=='':
        title=name
    else:
        title=title_
    return '  TH1F* h_'+name+'=new TH1F("'+name+'","'+title+'",'+str(nbins)+','+str(xmin)+','+str(xmax)+');\n'


def initHistoWithProcessNameAndSuffix(name,nbins,xmin=0,xmax=0,title_=''):
    if title_=='':
        title=name
    else:
        title=title_

    return '  TH1F* h_'+name+'=new TH1F((processname+"_'+name+'"+suffix).c_str(),"'+title+'",'+str(nbins)+','+str(xmin)+','+str(xmax)+');\n'

def initReader(name):
    text=''
    text+='  TMVA::Reader *r_'+name+' = new TMVA::Reader("Silent");\n'
    return text

def calculateDerived(names,expressions):
    text=''
    for n,e in zip(names,expressions):
        if n!=e:
            text+='    '+n+' = '+e+';\n'
    return text

def addVariablesToReader(readername,expressions,variablenames):
    text=''
    for e,n in zip(expressions,variablenames):
        text+='  r_'+readername+'->AddVariable("'+e+'", &'+n+');\n'
    return text


def bookMVA(name,weightfile):
    return '  r_'+name+'->BookMVA("BDT","'+weightfile+'");\n'

def fillHistoSyst(name,varname,weight,systnames,systweights):
    text='      float weight_'+name+'='+weight+';\n'
    for sn,sw in zip(systnames,systweights):
        text+=fillHisto(name+sn,varname,'('+sw+')*(weight_'+name+')')
#        text+= '      if(('+sw+')*(weight_'+name+')>0)'
#        text+= '        h_'+name+sn+'->Fill('+varname+',('+sw+')*(weight_'+name+'));\n'
    return text

def evaluateMVA(plot):
    name=plot.name
    text='      float bdtoutput_'+name+' = r_'+name+'->EvaluateMVA("BDT");\n'
    return text

# returns all variables of an expression
def varsIn(expr):
    # find all words not followed by ( (these are functions)
    variablescandidates = re.findall(r"\w+\b(?!\()", expr)
    variables=[]
    for v in variablescandidates:
        if v[0].isalpha() or v[0]=='_':
            variables.append(v)
    return variables

# returns all variables of an expression that are not followed by [ (e.g. variable[0])
def varsNoIndex(expr):
    # find all words not followed by [
    variablescandidates = re.findall(r"\w+\b(?!\[)", expr)
    variables=[]
    for v in variablescandidates:
        if v[0].isalpha() or v[0]=='_':
            variables.append(v)
    return variables

def varsWithMaxIndex(expr,allvars):
    # find all words followed by [
    variablescandidates = re.findall(r"\w+\b(?=\[)", expr)    
    variables=[]
    maxidxs=[]
    for v in variablescandidates:
        if v[0].isalpha() or v[0]=='_':
            variables.append(v)
    variables=list(set(variables))
    arraylength={}
    for v in allvars:
        if v.arraylength == None: continue
        arraylength[v.name]=v.arraylength
    maxmap={}
    for v in variables:
        maxidx=-1
        lower=0
        while True:
            varstart=expr.find(v+'[',lower)
            if varstart>-1:
                lower=varstart+len(v)+1
            else:
                break
            upper=expr.find(']',lower)
            if lower > 0 and upper>0 and (varstart==0  or ( not expr[varstart-1].isalpha() and not expr[varstart-1] == '_' ) ):
                idx=int(expr[lower:upper])
                if idx>maxidx: maxidx=idx
        if arraylength[v] not in maxmap.keys() or maxmap[arraylength[v]]<maxidx:
            maxmap[arraylength[v]]=maxidx
    return maxmap

def checkArrayLengths(ex,allvars):
    maxidxs=varsWithMaxIndex(ex,allvars)
    arrayselection="1"
    for v in maxidxs.keys():
        arrayselection+='&&'+v+'>'+str(maxidxs[v])
    return arrayselection

def getArrayEntries(expr,variablesmap,i):
    newexpr=expr
    variables=varsNoIndex(expr)
    for v in variables:
        if v in variablesmap.keys():
            if variablesmap[v].arraylength==None: continue
            # substitute v by v[i]
            newexpr=re.sub(v+"(?!\[)",v+'['+str(i)+']',newexpr)
    return newexpr

def getVartypesAndLength(varnames,tree):
    vartypes={}
    arraylength={}
    for v in varnames:
        br=tree.GetBranch(v)
        if not hasattr(tree, v):
            print v,'does not exist in tree!'
            vartypes[v]='F'
            continue
        b=br.GetTitle()
        vartypes[v]=b.split('/')[1]
        varisarray=b.split('/')[0][-1]==']'
        if varisarray:
            arraylength[v]= re.findall(r"\[(.*?)\]",b.split('/')[0])[0]
            varnames.append(arraylength[v])
            vartypes[arraylength[v]]='I'
    varnames=list(set(varnames))
    variables=[]
    for v in varnames:
        if v in arraylength:
            variables.append(Variable(v,vartypes[v],arraylength[v]))
        else:
            variables.append(Variable(v,vartypes[v]))
    return variables

def startLoop():
    return """  
  // loop over all events
  long nentries = chain->GetEntries(); 
  cout << "total number of events: " << nentries << endl;
  for (long iEntry=skipevents;iEntry<nentries;iEntry++) {
    if(iEntry==maxevents) break;
    if(iEntry%10000==0) cout << "analyzing event " << iEntry << endl;
    chain->GetEntry(iEntry); 
    eventsAnalyzed++;
    sumOfWeights+=Weight;

"""


def encodeSampleSelection(samples,allvars):
    text=''
    for sample in samples:
        arrayselection=checkArrayLengths(sample.selection,allvars)
        if arrayselection=='': arrayselection ='1' 
        sselection=sample.selection
        if sselection=='': sselection='1'
        text+= '    if(processname=="'+sample.nick+'" && (!('+arrayselection+') || ('+sselection+')==0) ) continue;\n'
        text+= '    else if(processname=="'+sample.nick+'") sampleweight='+sselection+';\n'
    return text

def startCat(catweight,allvars):
    text='\n    // staring category\n'
    arrayselection=checkArrayLengths(catweight,allvars)
    if catweight=='': catweight='1'
    if arrayselection=='': arrayselection ='1' 
    text+='    if((('+arrayselection+')*('+catweight+'))!=0) {\n'
    text+='      float categoryweight='+catweight+';\n'
    return text

def endCat():
    return '    }\n    // end of category\n\n'


def fillHisto(histo,var,weight):
    text= '        if(('+weight+')!=0)\n'
    text+='          h_'+histo+'->Fill(fmin(h_'+histo+'->GetXaxis()->GetXmax()-1e-6,fmax(h_'+histo+'->GetXaxis()->GetXmin()+1e-6,'+var+')),'+weight+');\n'
    return text

def endLoop():
    return """  }\n // end of event loop

"""
def varLoop(i,n):
    return '      for(uint '+str(i)+'=0; '+str(i)+'<'+str(n)+'; '+str(i)+'++)'


def getFoot():
    return """  outfile->Write();
  outfile->Close();
  std::ofstream f_nevents((string(outfilename)+".cutflow.txt").c_str());
  f_nevents << "0" << " : " << "all" << " : " << eventsAnalyzed << " : " << sumOfWeights <<endl;
  f_nevents.close();
}

int main(){
  plot();
}
"""
                         
def initVarsFromTree(variables):
    r=""
    for v in variables:
        r+=initVarFromTree(v)
    r+='\n'
    return r

def compileProgram(scriptname):
    p = subprocess.Popen(['root-config', '--cflags', '--libs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    cmd= ['g++']+out[:-1].split(' ')+['-lTMVA']+[scriptname+'.cc','-o',scriptname]
    subprocess.call(cmd)


def createProgram(scriptname,plots,samples,catnames=[""],catselections=["1"],systnames=[""],systweights=["1"]):
    f=ROOT.TFile(samples[0].files[0])
    print 'using',samples[0].files[0],'to determining variable types'
    tree=f.Get('MVATree')
    
    
    # variables is the list of variables to be read from tree
    variablesnames=['Weight']
    variablesnames+=varsIn(','.join(catselections))#extract all words
    variablesnames+=varsIn(','.join(systweights))   
    
    # extract variablesnames of all plots
    for plot in plots:
        if isinstance(plot,plotutils.Plot):
            variablesnames+=varsIn(plot.variable)
        variablesnames+=varsIn(plot.selection)
    for s in samples:
        variablesnames+=varsIn(s.selection)

    for plot in plots:
        if isinstance(plot,plotutils.MVAPlot):
            variablesnames+=varsIn(','.join(plot.input_exprs))

    # remove duplicates
    variablesnames=list(set(variablesnames))

    # find out types of variables, length of arrays, and add length variables to variable list
    variables=getVartypesAndLength(variablesnames,tree)
    variablesmap={}
    for v in variables:
        variablesmap[v.name]=v
    # start writing script
    script=""
    script+=getHead()
    script+=initVarsFromTree(variables)
    
    # for
    for plot in plots:
        if isinstance(plot,plotutils.MVAPlot):
            for v,t in zip(plot.input_names,plot.input_types):
                initVar(Variable(v,t))
            script+=initReader(plot.name)
            script+=addVariablesToReader(plot.name,plot.input_exprs,plot.input_names)
            script+=bookMVA(plot.name,plot.weightfile)


    # initialize histograms in all categories and for all systematics
    for c in catnames:
        for plot in plots:
            t=plot.histo.GetTitle()
            n=plot.histo.GetName()
            mx=plot.histo.GetXaxis().GetXmax()
            mn=plot.histo.GetXaxis().GetXmin()
            nb=plot.histo.GetNbinsX()
            for s in systnames:
                script+=initHistoWithProcessNameAndSuffix(c+n+s,nb,mn,mx,t)

    # start event loop
    script+=startLoop()
    script+='    float sampleweight=1;\n'
    script+=encodeSampleSelection(samples,variables)
    # calculate derived variables used in BDT
    input_names=[]
    input_exprs=[]
    for plot in plots:
        if isinstance(plot,plotutils.MVAPlot):
            input_names.append(plot)
            input_exprs.append(plot)
    script+=calculateDerived(input_names,input_exprs)
    for cn,cs in zip(catnames,catselections):
        # for every category
        script+=startCat(cs,variables)
        # plot everything
        for plot in plots:
            if isinstance(plot,plotutils.MVAPlot): continue
            n=plot.histo.GetName()
            ex=plot.variable
            pw=plot.selection
            if pw=='': pw='1'
            variablenames_without_index=varsNoIndex(ex) 
            variablenames_without_index+=varsNoIndex(pw)
            size_of_loop=None
            for v in variablenames_without_index:
                if not v in variablesmap.keys(): continue
                if variablesmap[v].arraylength != None:
                    assert size_of_loop == None or size_of_loop == variablesmap[v].arraylength
                    size_of_loop=variablesmap[v].arraylength
            histoname=cn+n
            script+="\n"
            if size_of_loop!=None:
                exi=getArrayEntries(ex,variablesmap,"i")
                pwi=getArrayEntries(pw,variablesmap,"i")
                script+=varLoop("i",size_of_loop)                    
                script+="{\n"
                arrayselection=checkArrayLengths(','.join([ex,pw]),variables)
                weight='('+arrayselection+')*('+pwi+')*Weight*categoryweight*sampleweight'
                script+=fillHistoSyst(histoname,exi,weight,systnames,systweights)
                script+="      }\n"
            else:
                arrayselection=checkArrayLengths(','.join([ex,pw]),variables)
                weight='('+arrayselection+')*('+pw+')*Weight*categoryweight*sampleweight'
                script+=fillHistoSyst(histoname,ex,weight,systnames,systweights)
        for plot in plots:
            histoname=cn+plot.name
            if isinstance(plot,plotutils.MVAPlot):
                script+=evaluateMVA(plot)
                weight='('+plot.selection+')*Weight*categoryweight*sampleweight'
                script+=fillHistoSyst(histoname,'bdtoutput_'+plot.name,weight,systnames,systweights)
        script+=endCat()
    script+=endLoop()
    script+=getFoot()
    f=open(scriptname+'.cc','w')
    f.write(script)
    f.close()



def createScript(scriptname,programpath,processname,filenames,outfilename,maxevents,skipevents,cmsswpath,suffix):
    script="#!/bin/bash \n"
    if cmsswpath!='':
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

def askYesNo(question):
    print question
    yes = set(['yes','y', 'ye', ''])
    no = set(['no','n'])
    choice = raw_input().lower()
    if choice in yes:
        return True
    elif choice in no:
        return False
    else:
        print "Please respond with 'yes' or 'no'"
        return askYesNo(question)

def submitToNAF(scripts):
    jobids=[]
    for script in scripts:
        print 'submitting',script
        command=['qsub', '-cwd', '-S', '/bin/bash','-l', 'h=bird*', '-hard','-l', 'os=sld6', '-l' ,'h_vmem=2000M', '-l', 's_vmem=2000M' ,'-o', '/dev/null', '-e', '/dev/null', script]
        a = subprocess.Popen(command, stdout=subprocess.PIPE,stderr=subprocess.STDOUT,stdin=subprocess.PIPE)
        output = a.communicate()[0]
        jobidstring = output.split()
        for jid in jobidstring:
	  if jid.isdigit():
	    jobid=int(jid)
	    print "this job's ID is", jobid
            jobids.append(jobid)
            break
    return jobids

def do_qstat(jobids):
    allfinished=False
    while not allfinished:
        time.sleep(10)
        a = subprocess.Popen(['qstat'], stdout=subprocess.PIPE,stderr=subprocess.STDOUT,stdin=subprocess.PIPE)
        qstat=a.communicate()[0]
        lines=qstat.split('\n')
        nrunning=0
        for line in lines:
            words=line.split()
            for jid in words:
	       if jid.isdigit():
	         jobid=int(jid)
                 if jobid in jobids:
                   nrunning+=1
                 break
        if nrunning>0:
            print nrunning,'jobs running'
        else:
            allfinished=True

def get_scripts_outputs_and_nentries(samples,maxevents,scriptsfolder,plotspath,programpath,cmsswpath):
    scripts=[]
    outputs=[]
    nentries=[]    
    for s in samples:
        print 'creating scripts for',s.name,'from',s.path
        ntotal_events=0
        njob=0
        events_in_files=0
        files_to_submit=[]
        for fn in s.files:
            f=ROOT.TFile(fn)
            t=f.Get('MVATree')
            events_in_file=t.GetEntries()
            # if the file is larger than maxevents it is analyzed in portions of nevents
            if events_in_file > maxevents:
                for ijob in range(events_in_file/maxevents+1):
                    njob+=1
                    skipevents=(ijob)*maxevents       
                    scriptname=scriptsfolder+'/'+s.nick+'_'+str(njob)+'.sh'
                    processname=s.nick
                    filenames=fn
                    outfilename=plotspath+s.nick+'_'+str(njob)+'.root'
                    createScript(scriptname,programpath,processname,filenames,outfilename,maxevents,skipevents,cmsswpath,'')
                    scripts.append(scriptname)
                    outputs.append(outfilename)
                    nentries.append(events_in_file)
                    ntotal_events+=events_in_file
            # else additional files are appended to list of files to be submitted
            else :
                files_to_submit+=[fn]
                events_in_files+=events_in_file
                if events_in_files>maxevents or fn==s.files[-1]:
                    njob+=1
                    skipevents=0
                    scriptname=scriptsfolder+'/'+s.nick+'_'+str(njob)+'.sh'
                    processname=s.nick
                    filenames=' '.join(files_to_submit)
                    outfilename=plotspath+s.nick+'_'+str(njob)+'.root'
                    createScript(scriptname,programpath,processname,filenames,outfilename,events_in_files,skipevents,cmsswpath,'')
                    scripts.append(scriptname)
                    outputs.append(outfilename)
                    nentries.append(events_in_files)
                    ntotal_events+=events_in_files
                    files_to_submit=[]
                    events_in_files=0
        # submit remaining scripts (can happen if the last file was large)
        if len(files_to_submit)>0:
            njob+=1
            skipevents=0
            scriptname=scriptsfolder+'/'+s.nick+'_'+str(njob)+'.sh'
            processname=s.nick
            filenames=' '.join(files_to_submit)
            outfilename=plotspath+s.nick+'_'+str(njob)+'.root'
            createScript(scriptname,programpath,processname,filenames,outfilename,events_in_files,skipevents,cmsswpath,'')
            scripts.append(scriptname)
            outputs.append(outfilename)
            nentries.append(events_in_files)
            ntotal_events+=events_in_files
            files_to_submit=[]
            events_in_files=0

        print ntotal_events,'events found in',s.name
    return scripts,outputs,nentries

def check_jobs(scripts,outputs,nentries):
    failed_jobs=[]
    for script,o,n in zip(scripts,outputs,nentries):
        if not os.path.exists(o+'.cutflow.txt'):
            failed_jobs.append(script)
            continue
        f=open(o+'.cutflow.txt')
        processed_entries=-1
        for line in f:
            s=line.split(' : ')
            if len(s)>2 and 'all' in s[1]:
                processed_entries=int(s[2])
                break
        if n!=processed_entries:
            failed_jobs.append(script)
    return failed_jobs

def plotParallel(name,maxevents,plots,samples,catnames=[""],catselections=["1"],systnames=[""],systweights=["1"]):
    workdir=os.getcwd()+'/workdir/'+name
    outputpath=workdir+'/output.root'

    if not os.path.exists('workdir'):
        os.makedirs('workdir')
    if not os.path.exists(workdir):
        os.makedirs(workdir)
    else:
        if askYesNo('plot existing histograms?'):
            return outputpath
        workdirold=workdir+datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        os.rename(workdir,workdirold)
        os.makedirs(workdir)
    if not os.path.exists(workdir):
        os.makedirs(workdir)
    cmsswpath=os.environ['CMSSW_BASE']
    programpath=workdir+'/'+name
    print 'creating c++ program'
    createProgram(programpath,plots,samples,catnames,catselections,systnames,systweights)
    if not os.path.exists(programpath+'.cc'):
        print 'could not create c++ program'
        sys.exit()
    print 'compiling c++ program'
    compileProgram(programpath)
    if not os.path.exists(programpath):
        print 'could not compile c++ program'
        sys.exit()
    print 'creating folders'
    scriptsfolder=workdir+'/'+name+'_scripts'
    if not os.path.exists(scriptsfolder):
        os.makedirs(scriptsfolder)
    plotspath=workdir+'/'+name+'_plots/'
    if not os.path.exists(plotspath):
        os.makedirs(plotspath)
    if not os.path.exists(workdir):
        print 'could not create workdirs'
        sys.exit()
    print 'creating scripts'
    scripts,outputs,nentries=get_scripts_outputs_and_nentries(samples,maxevents,scriptsfolder,plotspath,programpath,cmsswpath)
    print 'submitting scripts'
    jobids=submitToNAF(scripts)
    do_qstat(jobids)

    print 'checking outputs'
    failed_jobs=check_jobs(scripts,outputs,nentries)
    retries=0
    while retries<=3 and len(failed_jobs)>0:
        retries+=1
        print 'the following jobs failed'
        for j in failed_jobs:
            print j
        print 'resubmitting'
        jobids=submitToNAF(failed_jobs)
        do_qstat(jobids)
        failed_jobs=check_jobs(scripts,outputs,nentries)
    if retries>=10:
        print 'could not submit jobs'
        sys.exit()
    print 'hadd output'
    subprocess.call(['hadd', outputpath]+outputs)
    print 'done'
    return  outputpath
