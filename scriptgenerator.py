import sys
import os
import subprocess
import time
import datetime
import stat
import re
import ROOT
import xml.etree.ElementTree as ET
import variablebox
import plotutils

ROOT.gROOT.SetBatch(True)

def getHead1():
  return """
#include "TChain.h"
#include "TString.h"
#include "TBranch.h"
#include "TLorentzVector.h"
#include "TFile.h"
#include "TH1F.h"
#include "TH2F.h"
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include "TMVA/Reader.h"

using namespace std;
"""

def getHead2():
  return """
void plot(){
  TH1F::SetDefaultSumw2();

/*
  std::string csvHFfile="/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/csv_rwt_fit_hf_v2_final_2017_3_29test.root";
  std::string csvLFfile="/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/csv_rwt_fit_lf_v2_final_2017_3_29test.root";
  

  CSVHelper* internalCSVHelper= new CSVHelper(csvHFfile,csvLFfile, 5);
*/
 

"""


def getHead3():
  return """
  // open files
  TChain* chain = new TChain("MVATree");
  char* filenames = getenv ("FILENAMES");
  char* outfilename = getenv ("OUTFILENAME");
  string processname = string(getenv ("PROCESSNAME"));
  TString procname (processname);
  string suffix = string(getenv ("SUFFIX"));
  int lastevent = atoi(getenv ("LASTEVENT"));
  int firstevent = atoi(getenv ("FIRSTEVENT"));
  
  int eventsAnalyzed=0;
  float sumOfWeights=0;
  
  int DoWeights=1;
  int DoABCDsyst=0;
  int DoMCDataWeights=1;
  int DoMCDataWeights_ttbaronly=0;
  int DoMCDataWeights_ST_tW=0;
  int DoMCDataWeights_ST_t=0;
  int DoMCDataWeights_ST_s=0;
  int murmuf1500=0;
  int murmuf1750=0;
  int murmuf2000=0;
  int murmuf2250=0;
  int murmuf2500=0;
  int murmuf2750=0;
  int murmuf3000=0;
  int murmuf3500=0;
  int murmuf4000=0;
  int murmufGstar1500=0;
  int murmufGstar1750=0;
  int murmufGstar2000=0;
  int murmufGstar2250=0;
  int murmufGstar2500=0;
  int murmufGstar2750=0;
  int murmufGstar3000=0;
  int murmufGstar3500=0;
  int murmufGstar4000=0;  
  
  TString DATAstr ("DATA");
  TString ttbarstr ("ttbar");
  TString ST_tWstr ("ST_tW");
  TString ST_tstr ("ST_t");
  TString ST_sstr ("ST_s");
  TString STstr ("ST");
  TString QCDstr ("QCD");
  TString SCstr ("SC");
  TString Sigstr ("Sig");
  
  TString Sigstr1500 ("Zprime1500");
  TString Sigstr1750 ("Zprime1750");
  TString Sigstr2000 ("Zprime2000");
  TString Sigstr2250 ("Zprime2250");
  TString Sigstr2500 ("Zprime2500");
  TString Sigstr2750 ("Zprime2750");
  TString Sigstr3000 ("Zprime3000");
  TString Sigstr3500 ("Zprime3500");
  TString Sigstr4000 ("Zprime4000");  
  
  TString SigGstarstr1500 ("Gstar1500");
  TString SigGstarstr1750 ("Gstar1750");
  TString SigGstarstr2000 ("Gstar2000");
  TString SigGstarstr2250 ("Gstar2250");
  TString SigGstarstr2500 ("Gstar2500");
  TString SigGstarstr2750 ("Gstar2750");
  TString SigGstarstr3000 ("Gstar3000");
  TString SigGstarstr3500 ("Gstar3500");
  TString SigGstarstr4000 ("Gstar4000");    
  
  
  //if(processname=="SingleEl" || processname=="SingleMu"){DoWeights=0; std::cout<<"is data, dont use nominal weihgts"<<std::endl;}
  //if(processname=="SingleEl" || processname=="SingleMu"){DoWeights=0; std::cout<<"is data, dont use nominal weihgts"<<std::endl;}
  //if(processname=="Data" || processname=="data" || processname=="QCDMadgraph" || processname=="QCDPythia8" || procname.Contains("")){DoWeights=0;DoMCDataWeights=0 std::cout<<"is data or QCD, dont use nominal weihgts"<<std::endl;}
  //if(processname=="QCDMadgraph" || processname=="QCDPythia8"){DoABCDsyst=1; DoMCDataWeights=0; std::cout<<"is QCD, use ABCD systematics"<<std::endl;}
  //if(processname=="ttbar" || "ttbar_JESup" || "ttbar_JESup" || "ttbar_JERup" || "ttbar_JERup" || processname=="t#bar{t} + jets" || processname=="Signal" || processname=="SC"){DoMCDataWeights=1; std::cout<<"is ttbar or signal, use MCDataSF nominal weihgts"<<std::endl;}
  //if(processname=="ttbar" || "ttbar_JESup" || "ttbar_JESup" || "ttbar_JERup" || "ttbar_JERup" || processname=="t#bar{t} + jets"){DoMCDataWeights_ttbaronly=1; std::cout<<"is ttbar, use MCDataSF nominal weihgts"<<std::endl;}

  if(bool(procname.Contains(DATAstr))){DoABCDsyst=1; DoWeights=0; DoMCDataWeights=0; std::cout<<"is data or QCD, dont use nominal weihgts"<<std::endl;}
  if(bool(procname.Contains(QCDstr))){DoABCDsyst=1; DoMCDataWeights=0; std::cout<<"is QCD, use ABCD systematics"<<std::endl;}
  if(bool(procname.Contains(ttbarstr)) || bool(procname.Contains(SCstr)) || bool(procname.Contains(Sigstr))|| bool(procname.Contains(STstr))){DoMCDataWeights=1; std::cout<<"is ttbar or signal, use MCDataSF nominal weihgts"<<std::endl;}
  if(bool(procname.Contains(ttbarstr))){DoMCDataWeights_ttbaronly=1; std::cout<<"is ttbar, use MCDataSF nominal weihgts"<<std::endl;}
  if(bool(procname.Contains(SCstr)) || bool(procname.Contains(Sigstr))|| bool(procname.Contains(STstr))){DoMCDataWeights_ttbaronly=0; std::cout<<"is ttbar, use MCDataSF nominal weihgts"<<std::endl;}
  
  
  if(bool(procname.Contains(ST_tWstr))){DoMCDataWeights_ST_tW=1;}
  if(bool(procname.Contains(ST_tstr))){DoMCDataWeights_ST_t=1;}
  if(bool(procname.Contains(ST_sstr))){DoMCDataWeights_ST_s=1;}
  
  if(bool(procname.Contains(Sigstr1500))){murmuf1500=1;}
  if(bool(procname.Contains(Sigstr1750))){murmuf1750=1;}
  if(bool(procname.Contains(Sigstr2000))){murmuf2000=1;}
  if(bool(procname.Contains(Sigstr2250))){murmuf2250=1;}
  if(bool(procname.Contains(Sigstr2500))){murmuf2500=1;}
  if(bool(procname.Contains(Sigstr2750))){murmuf2750=1;}
  if(bool(procname.Contains(Sigstr3000))){murmuf3000=1;}
  if(bool(procname.Contains(Sigstr3500))){murmuf3500=1;}
  if(bool(procname.Contains(Sigstr4000))){murmuf4000=1;}
  
  if(bool(procname.Contains(SigGstarstr1500))){murmufGstar1500=1;}
  if(bool(procname.Contains(SigGstarstr1750))){murmufGstar1750=1;}
  if(bool(procname.Contains(SigGstarstr2000))){murmufGstar2000=1;}
  if(bool(procname.Contains(SigGstarstr2250))){murmufGstar2250=1;}
  if(bool(procname.Contains(SigGstarstr2500))){murmufGstar2500=1;}
  if(bool(procname.Contains(SigGstarstr2750))){murmufGstar2750=1;}
  if(bool(procname.Contains(SigGstarstr3000))){murmufGstar3000=1;}
  if(bool(procname.Contains(SigGstarstr3500))){murmufGstar3500=1;}
  if(bool(procname.Contains(SigGstarstr4000))){murmufGstar4000=1;}  

  string buf;
  stringstream ss(filenames); 
  while (ss >> buf){
    chain->Add(buf.c_str());
  }
  chain->SetBranchStatus("*",0);

  TFile* outfile=new TFile(outfilename,"RECREATE");    

  // initialize variables from tree
"""

def loadaddobjects(additionalobjectsfromaddtionalrootfile):
    returnscript="""   """
    
    for objectcode in additionalobjectsfromaddtionalrootfile:
        returnscript+=objectcode
    return returnscript

def closeaddfiles():
    return """
  //SFfile->Close();

"""

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


def initTwoDimHistoWithProcessNameAndSuffix(name,nbinsX=10,xminX=0,xmaxX=0,nbinsY=10,xminY=0,xmaxY=0,title_=''):
  if title_=='':
    title=name
  else:
    title=title_

  return '  TH2F* h_'+name+'=new TH2F((processname+"_'+name+'"+suffix).c_str(),"'+title+'",'+str(nbinsX)+','+str(xminX)+','+str(xmaxX)+','+str(nbinsY)+','+str(xminY)+','+str(xmaxY)+');\n'



def fillHistoSyst(name,varname,weight,systnames,systweights,OnlyFirst=False):
  text='      float weight_'+name+'='+weight+';\n'
  for sn,sw in zip(systnames,systweights):
    text+=fillHisto(name,sn,varname,'('+sw+')*(weight_'+name+')',OnlyFirst)
  return text


def fillTwoDimHistoSyst(name,varname1,varname2,weight,systnames,systweights,OnlyFirst=False):
  text='      float weight_'+name+'='+weight+';\n'
  for sn,sw in zip(systnames,systweights):
    text+=fillTwoDimHisto(name,sn,varname1,varname2,'('+sw+')*(weight_'+name+')',OnlyFirst)
  return text


def startLoop():
  return """  
  // loop over all events
  long nentries = chain->GetEntries(); 
  cout << "total number of events: " << nentries << endl;
  
  for (long iEntry=firstevent;iEntry<nentries;iEntry++) {
    if(iEntry>lastevent) break;
    if(iEntry%10000==0) cout << "analyzing event " << iEntry << endl;
    
    chain->GetEntry(iEntry); 
    
    TString currentfilename="";
    currentfilename = chain->GetCurrentFile()->GetName();   
    int hasTrigger=0;
    if(currentfilename.Index("withTrigger")!=-1){hasTrigger=1;};
    eventsAnalyzed++;
    sumOfWeights+=Weight;

  // DANGERZONE

/*  
  std::vector<double> jetPts;    
  std::vector<double> jetEtas;    
  std::vector<double> jetPhis; 
  std::vector<double> jetMasses;
  std::vector<double> jetEnergies; 
  std::vector<double> jetCSVs;    
  std::vector<int> jetFlavors;    
    
  for(int ijet =0; ijet<N_Jets; ijet++){
	jetPts.push_back(Jet_Pt[ijet]);
	jetEtas.push_back(Jet_Eta[ijet]);
	jetCSVs.push_back(Jet_CSV[ijet]);
	jetFlavors.push_back(Jet_Flav[ijet]);
	jetMasses.push_back(Jet_M[ijet]);
	jetPhis.push_back(Jet_Phi[ijet]);
	jetEnergies.push_back(Jet_E[ijet]);
  }
  
  float internalCSVweight=1.0;
  float internalCSVweight_CSVHFUp=1.0;
  float internalCSVweight_CSVHFDown=1.0;
  float internalCSVweight_CSVLFUp=1.0;
  float internalCSVweight_CSVLFDown=1.0;
  float internalCSVweight_CSVLFStats1Up=1.0;
  float internalCSVweight_CSVLFStats1Down=1.0;
  float internalCSVweight_CSVLFStats2Up=1.0;
  float internalCSVweight_CSVLFStats2Down=1.0;
  float internalCSVweight_CSVHFStats1Up=1.0;
  float internalCSVweight_CSVHFStats1Down=1.0;
  float internalCSVweight_CSVHFStats2Up=1.0;
  float internalCSVweight_CSVHFStats2Down=1.0;
  float internalCSVweight_CSVCErr1Up=1.0;
  float internalCSVweight_CSVCErr1Down=1.0;
  float internalCSVweight_CSVCErr2Up=1.0;
  float internalCSVweight_CSVCErr2Down=1.0;  
  
  double tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF;
  
  internalCSVweight=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,internalSystName,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF);
  internalCSVweight_CSVHFUp=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,11,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVHFDown=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,12,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVLFUp=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,9,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVLFDown=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,10,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  
  internalCSVweight_CSVLFStats1Up=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,17,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVLFStats1Down=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,18,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVLFStats2Up=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,19,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVLFStats2Down=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,20,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  
  internalCSVweight_CSVHFStats1Up=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,13,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVHFStats1Down=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,14,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVHFStats2Up=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,15,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVHFStats2Down=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,16,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  
  internalCSVweight_CSVCErr1Up=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,21,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVCErr1Down=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,22,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVCErr2Up=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,23,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVCErr2Down=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,24,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  */


    
"""


def encodeSampleSelection(samples,variables):
  text=''
  for sample in samples:
    arrayselection=variables.checkArrayLengths(sample.selection)
    if arrayselection=='':
      arrayselection ='1' 
    sselection=sample.selection
    if sselection=='':
      sselection='1'
    text+= '    if(processname=="'+sample.nick+'" && (!('+arrayselection+') || ('+sselection+')==0) ) continue;\n'
    text+= '    else if(processname=="'+sample.nick+'") sampleweight='+sselection+';\n'
  return text


def startCat(catweight,variables):
  text='\n    // staring category\n'

  arrayselection=variables.checkArrayLengths(catweight)
  if catweight=='':
    catweight='1'
  if arrayselection=='':
    arrayselection ='1' 
  text+='    if((('+arrayselection+')*('+catweight+'))!=0) {\n'
  text+='      float categoryweight='+catweight+';\n'
  return text


def endCat():
  return '    }\n    // end of category\n\n'


def fillHisto(histoname, sn,var,weight,OnlyFirst=False):
  text= '        if(('+weight+')!=0){\n'
  text+='          h_'+histoname+sn+'->Fill(fmin(h_'+histoname+sn+'->GetXaxis()->GetXmax()-1e-6,fmax(h_'+histoname+sn+'->GetXaxis()->GetXmin()+1e-6,'+var+')),'+weight+');\n'
  if OnlyFirst:
    #text+='         break;}\n'
    #text+='         std::cout<<"filled '+var+'= "<<'+var+'<<" into '+histo+' "<<h_'+histo+'<<" with weight "<<'+weight+'<<endl;   break;}\n'
    #text+='         std::cout<<"filled '+var+'= "<<'+var+'<<" into '+histoname+sn+' "<<h_'+histoname+sn+'<<" with weight "<<'+weight+'<<endl;   '+histoname+'_foundfirst=true;}\n'
    text+='         '+histoname+'_foundfirst=true;}\n'
  else:
    text+='         }\n'
  return text


def fillTwoDimHisto(histoname, sn,var1,var2,weight,OnlyFirst=False):
  text= '        if(('+weight+')!=0)\n'
  text+='          h_'+histoname+sn+'->Fill(fmin(h_'+histoname+sn+'->GetXaxis()->GetXmax()-1e-6,fmax(h_'+histoname+sn+'->GetXaxis()->GetXmin()+1e-6,'+var1+')),fmin(h_'+histoname+sn+'->GetYaxis()->GetXmax()-1e-6,fmax(h_'+histoname+sn+'->GetYaxis()->GetXmin()+1e-6,'+var2+')),'+weight+');\n'
  
  if OnlyFirst:
    text+='         '+histoname+'_foundfirst=true;}\n'
  else:
    text+= '         }\n'
  return text


def endLoop():
  return """
  }\n // end of event loop
"""


def varLoop(i,n):
  return '    if('+n+'>0){\n      for(uint '+str(i)+'=0; '+str(i)+'<'+str(n)+'; '+str(i)+'++)'

def checkLoopsize(size_of_Loop):
  return 


def getFoot1():
  return """
  outfile->cd();
  outfile->Write();



"""
   
def getFoot2():
  return """

  outfile->Close();
  std::ofstream f_nevents((string(outfilename)+".cutflow.txt").c_str());
  f_nevents << "0" << " : " << "all" << " : " << eventsAnalyzed << " : " << sumOfWeights <<endl;
  f_nevents.close();
}

int main(){
  plot();
}    
"""   

def compileProgram(scriptname):
  p = subprocess.Popen(['root-config', '--cflags', '--libs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  out, err = p.communicate()
  cmd= ['g++']+out[:-1].split(' ')+['-lTMVA']+[scriptname+'.cc','-o',scriptname]
  subprocess.call(cmd)


def createProgram(scriptname,plots,samples,catnames=[""],catselections=["1"],systnames=[""],allsystweights=["1"],additionalvariables=[], additionalfunctions=[], additionalobjectsfromaddtionalrootfile=[],OnlyFirstList_=None):
  
  #Set default Value for OnlyFirstList
  if OnlyFirstList_ == None:
    OnlyFirstList = len(plots)*[False]
  else:
    OnlyFirstList = OnlyFirstList_
  
  
  # collect variables
  # list varibles that should not be written to the program automatically
  
  
  
  vetolist=['DoWeights','DoABCDsyst','DoMCDataWeights','DoMCDataWeights_ttbaronly','DoMCDataWeights_ST_tW','DoMCDataWeights_ST_t','DoMCDataWeights_ST_s','murmuf1500','murmuf1750','murmuf2000','murmuf2250','murmuf2500','murmuf2750','murmuf3000','murmuf3500','murmuf4000','murmufGstar1500','murmufGstar1750','murmufGstar2000','murmufGstar2250','murmufGstar2500','murmufGstar2750','murmufGstar3000','murmufGstar3500','murmufGstar4000']
  vetolist=vetolist+['processname','DoWeights','TMath','cout','for','int', 'if', 'cout', ';','<','i','i++','*=', 'temp','testea', 'anti_btag + 2', 'float','anti_loose_btag(Sideband_top_withbtag_anti_Topfirst_Bottoms_CSVv2,N_Sideband_top_withbtag_anti_Topfirst_Bottoms)','anti_loose_btag(Sideband_bottom_anti_Topfirst_Bottoms_CSVv2,N_Sideband_bottom_anti_Topfirst_Bottoms)' ]+['QCDMadgraph_Graph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M','QCDMadgraph_Graph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt','QCDMadgraph_Graph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt','QCDMadgraph_Graph_SF_SB_top_anti_Signal_Topfirst_Ws_Pt','QCDMadgraph_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M','QCDMadgraph_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt','QCDMadgraph_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt','QCDMadgraph_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt','QCDPythia8_Graph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M','QCDPythia8_Graph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt','QCDPythia8_Graph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt','QCDPythia8_Graph_SF_SB_top_anti_Signal_Topfirst_Ws_Pt','QCDPythia8_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M','QCDPythia8_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt','QCDPythia8_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt','QCDPythia8_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt','true', 'abs(', 'abs']+['abs( QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M)','abs( QCDPythia8_SF_SB_bottom_anti_Signal_Tops_Pt-QCDMadgraph_SF_SB_bottom_anti_Signal_Tops_Pt)']+['bbarportionweight(N_AK4_bottom_tag_candidates)','bbarportionweight(N_AK4_bottom_tag_candidates)']+['IsnoSignal_notopbtag(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD)','IsnoSignal_withtopbtag(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD)','IsnoSignal_inclusive(Zprimes_ABCD_M, Tprimes_ABCD_M, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD)']+['pow(',')',',']+['pow(1+0.06,1.0/3.0','pow(1-0.06,1.0/3.0)','pow(1+0.08,1.0/3.0)','pow(1-0.08,1.0/3.0)','pow(1+0.35,1.0/3.0)','pow(1-0.35,1.0/3.0)','pow(1+0.06,1.0/3.0)','pow(1-0.06,1.0/3.0)','pow(1+0.08,1.0/3.0)','pow(1-0.08,1.0/3.0)','pow(1+0.6,1.0/3.0)','pow(1-0.6,1.0/3.0)','pow(1+0.005,1.0/7.0)','pow(1-0.005,1.0/7.0)','pow(1+0.06,1.0/7.0)','pow(1-0.06,1.0/7.0)','pow(1+0.02,1.0/7.0)','pow(1-0.02,1.0/7.0)','pow(1+0.8,1.0/7.0)','pow(1-0.8,1.0/7.0)','pow(1-0.06,1.0/3.0)','pow(1+0.10,1.0/3.0)','pow(1-0.10,1.0/3.0)','pow(1+0.02,1.0/3.0)','pow(1-0.02,1.0/3.0)','pow(1+0.12,1.0/3.0)','pow(1-0.12,1.0/3.0)','pow(1+0.01,1.0/3.0)','pow(1-0.01,1.0/3.0)','pow(1+0.08,1.0/7.0)','pow(1-0.08,1.0/7.0)','pow(1+0.05,1.0/7.0)','pow(1-0.05,1.0/7.0)','pow(1+0.02,1.0/7.0)','pow(1-0.02,1.0/7.0)']+['ABCD_Category(','const','const*']
  vetolist=vetolist+['"CatA_withtopbtag"','"CatB_withtopbtag"','"CatC_withtopbtag"','"CatD_withtopbtag"','"CatE_withtopbtag"','"CatF_withtopbtag"','"CatG_withtopbtag"','"CatH_withtopbtag"'+'"CatA_notopbtag"','"CatB_notopbtag"','"CatC_notopbtag"','"CatD_notopbtag"','"CatE_notopbtag"','"CatF_notopbtag"','"CatG_notopbtag"','"CatH_notopbtag"','"CatA_inclusive"','"CatB_inclusive"','"CatC_inclusive"','"CatD_inclusive"','"CatE_inclusive"','"CatF_inclusive"','"CatG_inclusive"','"CatH_inclusive"']+['CatA_withtopbtag','CatB_withtopbtag','CatC_withtopbtag','CatD_withtopbtag','CatE_withtopbtag','CatF_withtopbtag','CatG_withtopbtag','CatH_withtopbtag'+'CatA_notopbtag','CatB_notopbtag','CatC_notopbtag','CatD_notopbtag','CatE_notopbtag','CatF_notopbtag','CatG_notopbtag','CatH_notopbtag','CatA_inclusive','CatB_inclusive','CatC_inclusive','CatD_inclusive','CatE_inclusive','CatF_inclusive','CatG_inclusive','CatH_inclusive']+['1.0*( ABCD_Category( Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD)=="CatA_withtopbtag")','1.0*( ABCD_Category( Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD)=="CatH_withtopbtag")'] #+['bportionweightup','bportionweightdown']#+['bportionweightup','bportionweightdown']  

  for i in range(1,100):
      vetolist=vetolist+["Weight_pdf_refac_"+str(i)]

  # initialize variables object
  variables = variablebox.Variables(vetolist)
  
  # get tree for variable check
  tree = ROOT.TTree()
  for i in range(len(samples)):
    thistreeisgood=False
    for j in range(len(samples[i].files)):
      f=ROOT.TFile(samples[i].files[j])
      tree=f.Get('MVATree')
      if tree.GetEntries()>0:
        print 'using',samples[i].files[j],'to determine variable types'
        thistreeisgood=True
        break
    if thistreeisgood:
      break
	
  # get standard variables
  standardvars=['Weight','Weight_CSV','Weight_XS']
  variables.initVarsFromExprList(standardvars,tree)
  
  # get additional variables
  if len(additionalvariables)>0:
    print 'looking for additionalvariables ',len(additionalvariables)
    variables.initVarsFromExprList(additionalvariables,tree)
  
  # get systematic weight variables
  variables.initVarsFromExprList(allsystweights,tree)
    
  systweights=[]
  for systweight in allsystweights:
    if ":=" in systweight:
	    systweights.append(systweight.split(":=")[0])
    else:
	    systweights.append(systweight)
        
  # get sample selection variables
  for sample in samples:
    variables.initVarsFromExpr(sample.selection,tree)
  
  # get category selection variables
  variables.initVarsFromExprList(catselections,tree)
  
  # get variables used in plots
  for plot in plots:
    if isinstance(plot,plotutils.Plot):
      variables.initVarsFromExpr(plot.variable,tree)
    if isinstance(plot,plotutils.TwoDimPlot):
      variables.initVarsFromExpr(plot.variable1,tree)
      variables.initVarsFromExpr(plot.variable2,tree)
  
    variables.initVarsFromExpr(plot.selection,tree)
  
  
  print variables
  # write program
  # start writing program
  script=""
  script+=getHead1()
  
  # initialize additional functions
  for f in additionalfunctions:
    script+=(f+";\n")
  
  script+=getHead2()
  # open additional objects from different root files
  script+=loadaddobjects(additionalobjectsfromaddtionalrootfile)
  
  script+=getHead3()
    
  # initialize all variables 
  script+=variables.initVarsProgram()
  script+=variables.initBranchAddressesProgram()

  # initialize TMVA Readers
  script+=variables.setupTMVAReadersProgram()
  

  
  # initialize histograms in all categories and for all systematics
  for c in catnames:
    for plot in plots:
      if isinstance(plot,plotutils.TwoDimPlot):
        t=plot.histo.GetTitle()+";"+plot.histo.GetXaxis().GetTitle()+";"+plot.histo.GetYaxis().GetTitle()
        n=plot.histo.GetName()
        mxX=plot.histo.GetXaxis().GetXmax()
        mnX=plot.histo.GetXaxis().GetXmin()
        nbX=plot.histo.GetNbinsX()
        mxY=plot.histo.GetYaxis().GetXmax()
        mnY=plot.histo.GetYaxis().GetXmin()
        nbY=plot.histo.GetNbinsY()
        for s in systnames:
          script+=initTwoDimHistoWithProcessNameAndSuffix(c+n+s,nbX,mnX,mxX,nbY,mnY,mxY,t)
      else:
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
  script+="\n"
  
  # calculate varibles and get TMVA outputs
  script+=variables.calculateVarsProgram()
  
  # start plotting      
  for cn,cs in zip(catnames,catselections):
    
     # for every category
    script+=startCat(cs,variables)

    # plot everything
    # plot one dimensional plots
    for plot, OnlyFirst in zip(plots, OnlyFirstList):
      if isinstance(plot,plotutils.TwoDimPlot):
        continue
      
      n=plot.histo.GetName()
      ex=plot.variable
      pw=plot.selection
      if pw=='':
        pw='1'
      
      # prepare loop over array variables
      variablenames_without_index=variables.varsNoIndex(ex) 
      variablenames_without_index+=variables.varsNoIndex(pw)
      
      # get size of array
      size_of_loop=None
      print 'SIZE OF LOOP', size_of_loop
      for v in variablenames_without_index:
        if not v in variables.variables:
          continue
        if variables.variables[v].arraylength != None:
          assert size_of_loop == None or size_of_loop == variables.variables[v].arraylength
          size_of_loop=variables.variables[v].arraylength
        print 'SIZE OF LOOP', size_of_loop
      
      histoname=cn+n
      script+="\n"
      #if size_of_loop!=None:
      print 'SIZE OF LOOP', size_of_loop
      if (size_of_loop!=None and size_of_loop>0):
        exi=variables.getArrayEntries(ex,"i")
        pwi=variables.getArrayEntries(pw,"i")
        #script+=checkLoopsize(size_of_loop)
        #script+="{\n"
        script+="    bool "+histoname+"_foundfirst=false; \n"
        script+=varLoop("i",size_of_loop)                    
        script+="{\n"
        script+="      if("+histoname+"_foundfirst) break;\n"
        arrayselection=variables.checkArrayLengths(','.join([ex,pw]))
        weight='('+arrayselection+')*('+pwi+')*Weight*categoryweight*sampleweight'
        print histoname
        print exi
        print weight
        script+=fillHistoSyst(histoname,exi,weight,systnames,systweights, OnlyFirst)
        script+="      }\n"
        script+="    }\n"
      else:
        script+="      if(true){\n"  
        arrayselection=variables.checkArrayLengths(','.join([ex,pw]))
        weight='('+arrayselection+')*('+pw+')*Weight*categoryweight*sampleweight'
        script+=fillHistoSyst(histoname,ex,weight,systnames,systweights)
        script+="    }\n"
    # plot two dimensional plots
    for plot, OnlyFirst in zip(plots, OnlyFirstList):
        if not isinstance(plot,plotutils.TwoDimPlot):
            continue
        
        n=plot.histo.GetName()
        exX=plot.variable1
        exY=plot.variable2
        pw=plot.selection
        if pw=='':
          pw='1'
        
        # prepare loop over array variables
        variablenames_without_index=variables.varsNoIndex(exX)
        variablenames_without_index+=variables.varsNoIndex(exY)
        variablenames_without_index+=variables.varsNoIndex(pw)
        
        # get size of array
        size_of_loop=None
        for v in variablenames_without_index:
          if not v in variables.variables:
            continue
          if variables.variables[v].arraylength != None:
            assert size_of_loop == None or size_of_loop == variables.variables[v].arraylength
            size_of_loop=variables.variables[v].arraylength
            
        
        histoname=cn+n
        script+="\n"
        if size_of_loop!=None:
          exiX=variables.getArrayEntries(exX,"i")
          exiY=variables.getArrayEntries(exY,"i")
          pwi=variables.getArrayEntries(pw,"i")
          script+=varLoop("i",size_of_loop)                    
          script+="{\n"
          arrayselection=variables.checkArrayLengths(','.join([exX,exY,pw]))
          weight='('+arrayselection+')*('+pwi+')*Weight*categoryweight*sampleweight'
          script+=fillTwoDimHistoSyst(histoname,exiX,exiY,weight,systnames,systweights, OnlyFirst)
          #script+="      }\n"
          script+="    }\n"
        else:
          script+="      if(true){\n"  
          arrayselection=variables.checkArrayLengths(','.join([exX,exY,pw]))
          weight='('+arrayselection+')*('+pw+')*Weight*categoryweight*sampleweight'
          script+=fillTwoDimHistoSyst(histoname,exX,exY,weight,systnames,systweights)
    
    # finish category
    script+=endCat()

  # finish loop
  script+=endLoop()
  
  # get program footer
  script+=getFoot1()
  script+=closeaddfiles()
  script+=getFoot2()
  
  # write program text to file
  f=open(scriptname+'.cc','w')
  f.write(script)
  f.close()


def createScript(scriptname,programpath,processname,filenames,outfilename,lastevent,firstevent,cmsswpath,suffix):
  script="#!/bin/bash \n"
  if cmsswpath!='':
    script+="export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch \n"
    script+="source $VO_CMS_SW_DIR/cmsset_default.sh \n"
    script+='cd '+cmsswpath+'/src\neval `scram runtime -sh`\n'
    script+='cd - \n'
  script+='export PROCESSNAME="'+processname+'"\n'
  script+='export FILENAMES="'+filenames+'"\n'
  script+='export OUTFILENAME="'+outfilename+'"\n'
  script+='export LASTEVENT="'+str(lastevent)+'"\n'
  script+='export FIRSTEVENT="'+str(firstevent)+'"\n'
  script+='export SUFFIX="'+suffix+'"\n'
  script+=programpath+'\n'
  #DANGERZONE
  script+='python '+programpath+'_rename.py\n'
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
    #print 'I am here: ', os.getcwd()
    command=['qsub', '-cwd', '-S', '/bin/bash','-l', 'h=bird*', '-hard','-l', 'os=sld6', '-l' ,'h_vmem=3500M', '-l', 's_vmem=3500M' ,'-o', os.getcwd()+'/logs/$JOB_NAME.o$JOB_ID', '-e', os.getcwd()+'/logs/$JOB_NAME.e$JOB_ID', script]
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
      print f
      events_in_file=t.GetEntries()
      # if the file is larger than maxevents it is analyzed in portions of nevents
      if events_in_file > maxevents:
        for ijob in range(events_in_file/maxevents+1):
          njob+=1
          firstevent=(ijob)*maxevents
          if ijob<(events_in_file/maxevents):
            nentries.append(maxevents)
            ntotal_events+=maxevents
            lastevent=firstevent+maxevents-1
          else:
            nentries.append(events_in_file-maxevents*ijob)
            ntotal_events+=(events_in_file-maxevents*ijob)
            lastevent=events_in_file-1
          scriptname=scriptsfolder+'/'+s.nick+'_'+str(njob)+'.sh'
          processname=s.nick
          filenames=fn
          outfilename=plotspath+s.nick+'_'+str(njob)+'.root'
          createScript(scriptname,programpath,processname,filenames,outfilename,lastevent,firstevent,cmsswpath,'')
          scripts.append(scriptname)
          outputs.append(outfilename)

              
      # else additional files are appended to list of files to be submitted
      else :
        files_to_submit+=[fn]
        events_in_files+=events_in_file
        if events_in_files>maxevents or fn==s.files[-1]:
          njob+=1
          firstevent=0
          scriptname=scriptsfolder+'/'+s.nick+'_'+str(njob)+'.sh'
          processname=s.nick
          filenames=' '.join(files_to_submit)
          outfilename=plotspath+s.nick+'_'+str(njob)+'.root'
          createScript(scriptname,programpath,processname,filenames,outfilename,events_in_files,firstevent,cmsswpath,'')
          scripts.append(scriptname)
          outputs.append(outfilename)
          nentries.append(events_in_files)
          ntotal_events+=events_in_files
          files_to_submit=[]
          events_in_files=0
              
    # submit remaining scripts (can happen if the last file was large)
    if len(files_to_submit)>0:
      njob+=1
      firstevent=0
      scriptname=scriptsfolder+'/'+s.nick+'_'+str(njob)+'.sh'
      processname=s.nick
      filenames=' '.join(files_to_submit)
      outfilename=plotspath+s.nick+'_'+str(njob)+'.root'
      createScript(scriptname,programpath,processname,filenames,outfilename,events_in_files,firstevent,cmsswpath,'')
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


def plotParallel(name,maxevents,plots,samples,catnames=[""],catselections=["1"],systnames=[""],systweights=["1"],additionalvariables=[],additionalfunctions=[],additionalobjectsfromaddtionalrootfile=[], OnlyFirstList=None,otherSystnames=[]):
  workdir=os.getcwd()+'/workdir/'+name
  outputpath=workdir+'/output.root'
  
  # create workdir folder
  print 'creating workdir folder'
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
  
  # create c++ program
  print 'creating c++ program'
  createProgram(programpath,plots,samples,catnames,catselections,systnames,systweights,additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile,OnlyFirstList)
  if not os.path.exists(programpath+'.cc'):
    print 'could not create c++ program'
    sys.exit()
  print 'compiling c++ program'
  compileProgram(programpath)
  if not os.path.exists(programpath):
    print 'could not compile c++ program'
    sys.exit()
    
  #create script to rename histograms
  createRenameScript(programpath,systnames+otherSystnames)
  
  
  
  # create output folders
  print 'creating output folders'
  scriptsfolder=workdir+'/'+name+'_scripts'
  if not os.path.exists(scriptsfolder):
    os.makedirs(scriptsfolder)
  plotspath=workdir+'/'+name+'_plots/'
  if not os.path.exists(plotspath):
    os.makedirs(plotspath)
  if not os.path.exists(workdir):
    print 'could not create workdirs'
    sys.exit()
  
  # create run scripts
  print 'creating run scripts'
  scripts,outputs,nentries=get_scripts_outputs_and_nentries(samples,maxevents,scriptsfolder,plotspath,programpath,cmsswpath)
  
  # submit run scripts
  print 'submitting scripts'
  jobids=submitToNAF(scripts)
  do_qstat(jobids)
  
  # check outputs
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
    
  # hadd outputs
  print 'hadd output'
  subprocess.call(['hadd', outputpath]+outputs)
  print 'done'
  return  outputpath



def createRenameScript(scriptname,systematics):
  header= """
import ROOT
import sys
import os
from subprocess import call
filename=os.getenv("OUTFILENAME")
"""
  
  body="""
def renameHistosParallel(infname,sysnames,prune=False):
  cmd="cp -v "+infname+" "+infname.replace(".root","_original.root")
  theclock=ROOT.TStopwatch()
  theclock.Start()
  call(cmd,shell=True)
  print sysnames
  #infile=ROOT.TFile(infname,"READ")
  outfile=ROOT.TFile(infname,"UPDATE")
  keylist=outfile.GetListOfKeys()
  theobjectlist=[]
  listOfKeyNames=[]
  for ikey, key in enumerate(keylist):
    listOfKeyNames.append(key.GetName())
  
  for ikey, key in enumerate(listOfKeyNames):
    thisname=key
    #thish=outfile.Get(thisname)
    thish=None
    newname=thisname
    do=True
    #if do and "PSscaleUp" in thisname and "Q2scale" in thisname and thisname[-2:]=="Up":
      #tmp=thisname
      #tmp=tmp.replace('_CMS_ttH_PSscaleUp','')
      #print 'stripped',tmp
      #newname=tmp.replace('Q2scale','CombinedScale')
    #if "PSscaleDown" in thisname and "Q2scale" in thisname and thisname[-4:]=="Down":
      #tmp=thisname
      #tmp=tmp.replace('_CMS_ttH_PSscaleDown','')
      #newname=tmp.replace('Q2scale','CombinedScale')
    if "dummy" in thisname:
      continue
      
    nsysts=0
    nominalfound=False
    for sys in sysnames:
      if sys in newname:
	newname=newname.replace(sys,"")
	newname+=sys
	nsysts+=1
      if 'nominal' in newname:
        nominalfound=True
	
    if "JES" in thisname or "JER" in thisname or "_ttH_scaleFSR" in thisname or "_ttH_scaleISR" in thisname or "_ttH_FSR" in thisname or "_ttH_ISR" in thisname or "_ttH_hdamp" in thisname or "ttH_ue" in thisname or (("CMS_scale_" in thisname or "CMS_res_" in thisname) and ("_jUp" in thisname or "_jDown" in thisname)) :
      if nsysts>2 and (not nominalfound):
        thish=outfile.Get(thisname)
        theobjectlist.append(thish)
	print nsysts, " systs: removing ", thisname
	outfile.Delete(thisname)
	outfile.Delete(thisname+";1")
	continue
    	
    #filter histograms for systs not belonging to the samples 
    #for now until we have NNPDF syst for other samples
    #if prune:
      #if "CMS_ttH_NNPDF" in thisname:
	#if thisname.split("_",1)[0]+"_" not in ["ttbarPlus2B_","ttbarPlusB_","ttbarPlusBBbar_","ttbarPlusCCbar_","ttbarOther_"]:
	  #print "wrong syst: removing histogram", thisname
	  #continue
      #if "CMS_ttH_Q2scale_ttbarOther" in thisname and "ttbarOther"!=thisname.split("_",1)[0]:
	#print "wrong syst: removing histogram", thisname
	#continue
      #if ("CMS_ttH_Q2scale_ttbarPlusBUp" in thisname or "CMS_ttH_Q2scale_ttbarPlusBDown" in thisname ) and "ttbarPlusB"!=thisname.split("_",1)[0] :
	#print "wrong syst: removing histogram", thisname
	#continue
      #if "CMS_ttH_Q2scale_ttbarPlusBBbar" in thisname and "ttbarPlusBBbar"!=thisname.split("_",1)[0] :
	#print "wrong syst: removing histogram", thisname
	#continue
      #if "CMS_ttH_Q2scale_ttbarPlusCCbar" in thisname and "ttbarPlusCCbar"!=thisname.split("_",1)[0] :
	#print "wrong syst: removing histogram", thisname
	#continue
      #if "CMS_ttH_Q2scale_ttbarPlus2B" in thisname and "ttbarPlus2B"!=thisname.split("_",1)[0] :
	#print "wrong syst: removing histogram", thisname
	#continue
    
    #add ttbar type to systematics name for PS scale
    #if "CMS_ttH_PSscaleUp" in newname or "CMS_ttH_PSscaleDown" in newname:
      
      #ttbartype=""
      #if "ttbarOther"==thisname.split("_",1)[0]:
	#ttbartype="ttbarOther"
      #elif "ttbarPlusB"==thisname.split("_",1)[0] :
	#ttbartype="ttbarPlusB"
      #elif "ttbarPlusBBbar"==thisname.split("_",1)[0] :
	#ttbartype="ttbarPlusBBbar"
      #elif "ttbarPlusCCbar"==thisname.split("_",1)[0] :
	#ttbartype="ttbarPlusCCbar"
      #elif "ttbarPlus2B"==thisname.split("_",1)[0] :
	#ttbartype="ttbarPlus2B"
      #else:
	#print "wrong syst: removing histogram", thisname
	#continue
      
      #if "CMS_ttH_PSscaleUp" in newname:
	#newname=newname.replace("CMS_ttH_PSscaleUp","CMS_ttH_PSscale_"+ttbartype+"Up")
      #elif "CMS_ttH_PSscaleDown" in newname:
	#newname=newname.replace("CMS_ttH_PSscaleDown","CMS_ttH_PSscale_"+ttbartype+"Down")
      #else:
	#print "wrong syst: removing histogram", thisname
    if newname!=thisname:
      print "changed ", thisname, " to ", newname  
      thish=outfile.Get(thisname)
      theobjectlist.append(thish)
      thish.SetName(newname)
      #outfile.cd()
      thish.Write()
      outfile.Delete(thisname+";1")
  
  outfile.Close()
  #infile.Close()    
  print "The renaming took ", theclock.RealTime()
  
renameHistosParallel(filename,systematics,False) 
  
  """
  
  script=header
  script+="systematics="+str(systematics)+"\n"
  script+=body
  
  scrfile=open(scriptname+"_rename.py","w")
  scrfile.write(script)
  scrfile.close()
    
    
