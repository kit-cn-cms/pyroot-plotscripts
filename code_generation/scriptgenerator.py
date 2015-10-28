import xml.etree.ElementTree as ET
import re
import subprocess

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

  string buf;
  stringstream ss(filenames); 
  while (ss >> buf){
    chain->Add(buf.c_str());
  }
  chain->SetBranchStatus("*",0);

  TFile* outfile=new TFile(outfilename,"RECREATE");    

  // initialize variables from tree
"""

def initVar(var,t='F',isarray=False):
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

def initVarFromTree(var,t='F',isarray=False):
    if isarray:
        text= initVar(var,t,True)
        text+='  chain->SetBranchAddress("'+var+'",'+var+');\n'
    else:
        text= initVar(var,t)
        text+='  chain->SetBranchAddress("'+var+'",&'+var+');\n'
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

def addVariablesToReader(readername,expressions,variablenames,isarray):
    text=''
    for e,n in zip(expressions,variablenames):
        text+='  r_'+readername+'->AddVariable("'+e+'", &'+n+');\n'
    return text

def bookMVA(name,weightfile):
    return '  r_'+name+'->BookMVA("BDT","'+weightfile+'");\n'

def evaluateMVA(name,eventweight,systnames,systweights):
    text='      float output_'+name+' = r_'+name+'->EvaluateMVA("BDT");\n'
    for sn,sw in zip(systnames,systweights):
        text+= '      h_BDT_ljets_'+name+sn+'->Fill(output_'+name+',('+sw+')*('+eventweight+'));\n'
    return text

def startLoop():
    return """  // loop over all events
  long nentries = chain->GetEntries(); 
  cout << "total number of events: " << nentries << endl;
  for (long iEntry=skipevents;iEntry<nentries;iEntry++) {
    if(iEntry==maxevents) break;
    if(iEntry%10000==0) cout << "analyzing event " << iEntry << endl;
    chain->GetEntry(iEntry); 
"""

def ttbarPlusX():
    text=''
    text+= '    if(processname=="ttbarPlusB" && GenEvt_I_TTPlusBB!=1) continue;\n'
    text+= '    if(processname=="ttbarPlus2B" && GenEvt_I_TTPlusBB!=2) continue;\n'
    text+= '    if(processname=="ttbarPlusBBbar" && GenEvt_I_TTPlusBB!=3) continue;\n'
    text+= '    if(processname=="ttbarPlusCCbar" && (GenEvt_I_TTPlusBB>0 || GenEvt_I_TTPlusCC<1)) continue;\n'
    text+= '    if(processname=="ttbarOther" && (GenEvt_I_TTPlusBB>0 || GenEvt_I_TTPlusCC>0)) continue;\n'
    return text


def startCat(eventweight):
    return '    if(('+eventweight+')!=0) {\n'

def endCat():
    return '    }\n'


def fillHisto(histo,var,weight):
    return '      h_'+histo+'->Fill('+var+','+weight+');\n'

def endLoop():
    return """  } // end of event loop
"""


def getFoot():
    return """  outfile->Write();
outfile->Close();
}

int main(){
  plot();
}
"""

def initVarsFromTree(vs,typemap,isarray):
    r=""
    for v in vs:
        if v in isarray:
            if v in typemap:
                r+=initVarFromTree(v,typemap[v],isarray[v])
            else:
                r+=initVarFromTree(v,'F',isarray[v])
        else:
            if v in typemap:
                r+=initVarFromTree(v,typemap[v])
            else:
                r+=initVarFromTree(v)
    return r

def compileScript(scriptname):
    p = subprocess.Popen(['root-config', '--cflags', '--libs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    cmd= ['g++']+out[:-1].split(' ')+['-lTMVA']+[scriptname+'.cc','-o',scriptname]
    subprocess.call(cmd)


def parseWeights(weightfile):
    root = ET.parse(weightfile).getroot()
    exprs=[]
    names=[]
    mins=[]
    maxs=[]
    types=[]
    for var in root.iter('Variable'):
        exprs.append(var.get('Expression'))
        names.append(var.get('Internal'))
        mins.append(var.get('Min'))
        maxs.append(var.get('Max'))
        types.append(var.get('Type'))
    return exprs,names,mins,maxs,types

def createScriptFromWeights(scriptname,weightnames,catnames,catselections,bdtbinnings,systnames,systweights,intvars):
    eventweight='Weight'
    # variables is the list of variables to be read from tree
    variablescandidates=re.findall(r"[\w]+", eventweight) #extract all words
    variablescandidates=variablescandidates+re.findall(r"[\w]+", ','.join(catselections))
    variablescandidates=variablescandidates+re.findall(r"[\w]+", ','.join(systweights))   
    variablescandidates=variablescandidates+['GenEvt_I_TTPlusCC','GenEvt_I_TTPlusBB']

    # everything not a float has to be defined
    vartypes={}
    for i in intvars:
        vartypes[i]='I'
    vartypes['GenEvt_I_TTPlusCC']='I'
    vartypes['GenEvt_I_TTPlusBB']='I'

    isarray={}

    # extract variablescandidates of all weightfiles
    for weightname in weightnames:
        exprs,names,mins,maxs,types=parseWeights(weightname)
        for expr in exprs:
            vs=re.findall(r"[\w]+", expr)
            for v in vs:
                variablescandidates.append(v)
            for v in vs:
                if v+"[" in expr:
                    isarray[v]=True
            
        for n,t in zip(names,types):
            vartypes[n]=t
    # remove duplicates
    variablescandidates=list(set(variablescandidates))
    # remove everything not a true variable (e.g. number)
    variables=[]
    for v in variablescandidates:
        if v[0].isalpha() or v[0]=='_':
            variables.append(v)


    # start writing script
    script=""
    script+=getHead()
    script+=initVarsFromTree(variables,vartypes,isarray)
    # also init derived variables in bdt
    for n in names:
        if not n in variables:
            if n in vartypes:
                script+=initVar(n,vartypes[n])
            else:
                script+=initVar(n)

    for c,w,binning in zip(catnames,weightnames,bdtbinnings):
        exprs,names,mins,maxs,types=parseWeights(w)
        for n,mn,mx in zip(names,mins,maxs):
            for s in systnames:
                script+=initHistoWithProcessNameAndSuffix(c+'_'+n+s,50,mn,mx)
        script+=initReader(c)
        for s in systnames:
            script+=initHistoWithProcessNameAndSuffix('BDT_ljets_'+c+s,binning[0],binning[1],binning[-1])
        script+=addVariablesToReader(c,exprs,names,isarray)
        script+=bookMVA(c,w)
    script+=startLoop()
    script+=ttbarPlusX()
    script+=calculateDerived(names,exprs)
    for cn,cs,w in zip(catnames,catselections,weightnames):
        exprs,names,mins,maxs,types=parseWeights(w)
        script+=startCat(cs)
        for n,ex in zip(names,exprs):
            for sn,sw in zip(systnames,systweights):
                script+=fillHisto(cn+'_'+n+sn,ex,'('+eventweight+')*('+sw+')')
        script+=evaluateMVA(cn,eventweight,systnames,systweights)
        script+=endCat()
    script+=endLoop()
    script+=getFoot()
    f=open(scriptname+'.cc','w')
    f.write(script)
    f.close()

def createScript(scriptname,plots,sample,catnames=[""],catselections=["1"],systnames=[""],systweights=["1"]):
    eventweight='Weight'
    # variables is the list of variables to be read from tree
    variablescandidates=re.findall(r"[\w]+", eventweight) #extract all words
    variablescandidates=variablescandidates+re.findall(r"[\w]+", ','.join(catselections))
    variablescandidates=variablescandidates+re.findall(r"[\w]+", ','.join(systweights))   
#    variablescandidates=variablescandidates+['GenEvt_I_TTPlusCC','GenEvt_I_TTPlusBB']

    # everything not a float has to be defined
#    vartypes={}
#    for i in intvars:
#        vartypes[i]='I'
#    vartypes['GenEvt_I_TTPlusCC']='I'
#    vartypes['GenEvt_I_TTPlusBB']='I'


    # extract variablescandidates of all plots
    for plot in plots:
        variablescandidates+=re.findall(r"[\w]+", plot.variable)
        variablescandidates+=re.findall(r"[\w]+", plot.selection)
    #TODO: find out type -- assuming float

    # remove duplicates
    variablescandidates=list(set(variablescandidates))
    # remove everything not a true variable (e.g. number)
    variables=[]
    for v in variablescandidates:
        if v[0].isalpha() or v[0]=='_':
            variables.append(v)

    # start writing script
    script=""
    script+=getHead()
    script+=initVarsFromTree(variables,'F'*len(variables))

    for c in catnames:
        for plot in plots:
            t=plot.histo.GetTitle()
            n=plot.histo.GetName()
            mx=plot.histo.GetXaxis().GetXmax()
            mn=plot.histo.GetXaxis().GetXmin()
            nb=plot.histo.GetNbinsX()
            for s in systnames:
                script+=initHisto(c+'_'+n+s,nb,mn,mx,t)
    script+=startLoop()
#    script+=ttbarPlusX()
    for cn,cs in zip(catnames,catselections):
        script+=startCat(cs)
        for plot in plots:
            n=plot.histo.GetName()
            ex=plot.variable
            pw=plot.selection            
            for sn,sw in zip(systnames,systweights):
                script+=fillHisto(cn+'_'+n+sn,ex,'('+pw+')*('+eventweight+')*('+sw+')')
        script+=endCat()
    script+=endLoop()
    script+=getFoot()
    f=open(scriptname+'.cc','w')
    f.write(script)
    f.close()
