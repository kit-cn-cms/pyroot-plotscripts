import xml.etree.ElementTree as ET
import re
import subprocess
import ROOT

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

def varsIn(expr):
    variablescandidates = re.findall(r"[\w]+", expr)
    variables=[]
    for v in variablescandidates:
        if v[0].isalpha() or v[0]=='_':
            variables.append(v)
    return variables


def varsNoIndex(expr):
    # find all words not followed by [
    variablescandidates = re.findall(r"\w+\b(?!\[)", expr)
    variables=[]
    for v in variablescandidates:
        if v[0].isalpha() or v[0]=='_':
            variables.append(v)
    return variables

def varsWithMaxIndex(expr,arraylength):
    # find all words not followed by [
    variablescandidates = re.findall(r"\w+\b(?=\[)", expr)    
    variables=[]
    maxidxs=[]
    for v in variablescandidates:
        if v[0].isalpha() or v[0]=='_':
            variables.append(v)
    variables=list(set(variables))
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

def checkArrayLengths(ex,arraylength):
    maxidxs=varsWithMaxIndex(ex,arraylength)
    arrayselection="1"
    for v in maxidxs.keys():
        arrayselection+='&&'+v+'>'+str(maxidxs[v])
    return arrayselection

def getArrayEntries(expr,arraylength,i):
    newexpr=expr
    variables=varsNoIndex(expr)
    for v in variables:
        if v in arraylength.keys():            
            # substitute v by v[i]
            newexpr=re.sub(v+"(?!\[)",v+'['+str(i)+']',newexpr)
    return newexpr

def getVartypesAndLength(variables,tree):
    vartypes={}
    arraylength={}
    for v in variables:
        b=tree.GetBranch(v).GetTitle()
        vartypes[v]=b.split('/')[1]
        varisarray=b.split('/')[0][-1]==']'
        if varisarray:
            arraylength[v]= re.findall(r"\[(.*?)\]",b.split('/')[0])[0]
            variables.append(arraylength[v])
            vartypes[arraylength[v]]='I'
    return vartypes,arraylength

def startLoop():
    return """  
  // loop over all events
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

def encodeSampleSelection(samples,arraylength):
    text=''
    for sample in samples:
        arrayselection=checkArrayLengths(sample.selection,arraylength)
        text+= '    if(processname=="'+sample.name+'" && (!('+arrayselection+') || ('+sample.selection+')==0) ) continue;\n'
    return text

def startCat(eventweight,arraylength):
    text='\n    // staring category\n'
    arrayselection=checkArrayLengths(eventweight,arraylength)
    text+='    if((('+arrayselection+')*('+eventweight+'))!=0) {\n'
    return text

def endCat():
    return '    }\n    // end of category\n\n'


def fillHisto(histo,var,weight):
    return '      if(('+weight+')!=0) h_'+histo+'->Fill('+var+','+weight+');\n'

def endLoop():
    return """  }\n // end of event loop

"""
def varLoop(i,n):
    return '      for(uint '+str(i)+'=0; '+str(i)+'<'+str(n)+'; '+str(i)+'++)'


def getFoot():
    return """  outfile->Write();
  outfile->Close();
}

int main(){
  plot();
}
"""

def initVarsFromTree(vs,typemap,arraylength):
    r=""
    for v in vs:
        if v in arraylength.keys():
            if v in typemap:
                r+=initVarFromTree(v,typemap[v],True)
            else:
                r+=initVarFromTree(v,'F',True)
        else:
            if v in typemap:
                r+=initVarFromTree(v,typemap[v])
            else:
                r+=initVarFromTree(v)
    r+='\n'
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

def createScript(scriptname,plots,samples,catnames=[""],catselections=["1"],systnames=[""],systweights=["1"]):
    f=ROOT.TFile(samples[0].path)
    tree=f.Get('MVATree')
    
    eventweight='Weight'
    # variables is the list of variables to be read from tree
    variablescandidates=varsIn(eventweight) #extract all words
    variablescandidates+=varsIn(','.join(catselections))
    variablescandidates+=varsIn(','.join(systweights))   

    # extract variablescandidates of all plots
    for plot in plots:
        variablescandidates+=varsIn(plot.variable)
        variablescandidates+=varsIn(plot.selection)
    for s in samples:
        variablescandidates+=varsIn(s.selection)

    # remove duplicates
    variablescandidates=list(set(variablescandidates))
    # remove everything not a true variable (e.g. number)
    variables=[]
    for v in variablescandidates:
        if v[0].isalpha() or v[0]=='_':
            variables.append(v)

    # remove duplicates
    variables=list(set(variables))

    vartypes,arraylength=getVartypesAndLength(variables,tree)
    # remove duplicates
    variables=list(set(variables))

    # start writing script
    script=""
    script+=getHead()
    script+=initVarsFromTree(variables,'F'*len(variables),arraylength)

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
    script+=encodeSampleSelection(samples,arraylength)
    for cn,cs in zip(catnames,catselections):
        script+=startCat(cs,arraylength)
        for plot in plots:
            n=plot.histo.GetName()
            ex=plot.variable
            pw=plot.selection

            if pw=='': pw='1'
            for sn,sw in zip(systnames,systweights):
                vars_in_plot=varsNoIndex(ex)
                vars_in_plot+=varsNoIndex(pw)
                lengthvar=""
                for v in vars_in_plot:
                    if v in arraylength.keys():
                        assert lengthvar == "" or lengthvar == arraylength[v]
                        lengthvar=arraylength[v]
                if lengthvar!="":
                    exi=getArrayEntries(ex,arraylength,"i")
                    pwi=getArrayEntries(pw,arraylength,"i")
                    swi=getArrayEntries(sw,arraylength,"i")
                    script+=varLoop("i",lengthvar)                    
                    arrayselection=checkArrayLengths(ex,arraylength)
                    script+=fillHisto(cn+'_'+n+sn,exi,'('+arrayselection+')*('+pwi+')*('+eventweight+')*('+swi+')')
                else:
                    script+=fillHisto(cn+'_'+n+sn,ex,'('+pw+')*('+eventweight+')*('+sw+')')
        script+=endCat()
    script+=endLoop()
    script+=getFoot()
    f=open(scriptname+'.cc','w')
    f.write(script)
    f.close()
