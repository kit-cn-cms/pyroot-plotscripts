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
  int maxevents = atoi(getenv ("MAXEVENTS"));

  string buf;
  stringstream ss(filenames); 
  while (ss >> buf){
    chain->Add(buf.c_str());
  }
  chain->SetBranchStatus("*",0);

  TFile* outfile=new TFile(outfilename,"RECREATE");    

  // initialize variables from tree
"""

def initDerived(var,t='F'):
    if t=='F':
        text='  float '+var+' = -999;\n'
    elif t=='I':
        text='  int '+var+' = -999;\n'
    else: "UNKNOWN TYPE",t
    return text

def initVar(var,t='F'):
    text= initDerived(var,t)
    text+='  chain->SetBranchAddress("'+var+'",&'+var+');\n'
    return text


def initHisto(var,nbins,xmin=0,xmax=0):
    return '  TH1F* h_'+var+'=new TH1F((processname+"_'+var+'").c_str(),"'+var+'",'+str(nbins)+','+str(xmin)+','+str(xmax)+');\n'

def initReader(name):
    text=''
    text+='  TMVA::Reader *r_'+name+' = new TMVA::Reader("Silent");\n'
    return text

def calculateDerived(names,expressions):
    text=''
    for n,e in zip(names,expressions):
        if n!=e:
            text+='    float '+n+' = '+e+';\n'
    return text

def addVariables(readername,expressions,names):
    text=''
    for e,n in zip(expressions,names):
        text+='  r_'+readername+'->AddVariable("'+e+'", &'+n+');\n'
    return text

def bookMVA(name,weightfile):
    return '  r_'+name+'->BookMVA("BDT","'+weightfile+'");\n'

def evaluateMVA(name,eventweight,systnames,systweights):
    text='      float output_'+name+' = r_'+name+'->EvaluateMVA("BDT");\n'
    for sn,sw in zip(systnames,systweights):
        text+= '      h_BDT_ljets'+name+sn+'->Fill(output_'+name+',('+sw+')*('+eventweight+'));\n'
    return text

def startLoop():
    return """  // loop over all events
  long nentries = chain->GetEntries(); 
  cout << "total number of events: " << nentries << endl;
  for (long iEntry=0;iEntry<nentries;iEntry++) {
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

def initVars(vs,typemap):
    r=""
    for v in vs:
        if v in typemap:
            r+=initVar(v,typemap[v])
        else:
            r+=initVar(v)
    return r


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

def createScriptFromWeights(scriptname,weightnames,catnames,catselections,systnames,systweights):
    eventweight='Weight'
    # variables is the list of variables to be read from tree
    variablescandidates=re.findall(r"[\w]+", eventweight) #extract all words
    variablescandidates=variablescandidates+re.findall(r"[\w]+", ','.join(catselections))
    variablescandidates=variablescandidates+re.findall(r"[\w]+", ','.join(systweights))

    
    variablescandidates=variablescandidates+['GenEvt_I_TTPlusCC','GenEvt_I_TTPlusBB']
    # everything not a float has to be defined
    vartypes={}
    vartypes['N_Jets']='I'
    vartypes['N_BTagsM']='I'
    vartypes['GenEvt_I_TTPlusCC']='I'
    vartypes['GenEvt_I_TTPlusBB']='I'

    # extract variablescandidates of all categories
    for weightname in weightnames:
        exprs,names,mins,maxs,types=parseWeights(weightname)
        for expr in exprs:
            vs=re.findall(r"[\w]+", expr)
            for v in vs:
                variablescandidates.append(v)
        for n,t in zip(names,types):
            vartypes[n]=t
    # remove duplicates
    variablescandidates=list(set(variablescandidates))
    # remove everything not a true variable (e.g. number)
    variables=[]
    for v in variablescandidates:
        if v[0].isalpha() or v[0]=='_':
            variables.append(v)

    script=""
    script+=getHead()
    script+=initVars(variables,vartypes)
    for n in names:
        if not n in variables:
            if n in vartypes:
                script+=initDerived(n,vartypes[n])
            else:
                script+=initDerived(n)
    for c,w in zip(catnames,weightnames):
        exprs,names,mins,maxs,types=parseWeights(w)
        for n,mn,mx in zip(names,mins,maxs):
            for s in systnames:
                script+=initHisto(c+'_'+n+s,50,mn,mx)
        script+=initReader(c)
        for s in systnames:
            script+=initHisto('BDT_ljets'+c+s,20,-1,1)
        script+=addVariables(c,exprs,names)
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
    p = subprocess.Popen(['root-config', '--cflags', '--libs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    cmd= ['g++']+out[:-1].split(' ')+['-lTMVA']+[scriptname+'.cc','-o',scriptname]
    subprocess.call(cmd)
