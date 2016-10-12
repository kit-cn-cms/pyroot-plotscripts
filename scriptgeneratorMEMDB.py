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
import glob
import json

ROOT.gROOT.SetBatch(True)

def getHead(dataBases):
  
  retstr="""
#include "TChain.h"
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
#include <algorithm>
#include <map>
#include "TStopwatch.h"
"""

  if dataBases!=[]:
    retstr+="""
#include "/nfs/dust/cms/user/kelmorab/DataBaseCodeForScriptGenerator/MEMDataBase/MEMDataBase/interface/MEMDataBase.h"
"""
  retstr+="""

using namespace std;

class EleTriggerHelper
{
  public:
    EleTriggerHelper();
    double GetSF(double electronPt, double electronEta, int syst);
  private:
    TH2D *h_abseta_pt_ratio;

};

EleTriggerHelper::EleTriggerHelper()
{
    std::string inputFile = "/nfs/dust/cms/user/asaibel/DataFilesForScriptGenerator/ElTriggerPerformance_Sep27.root";

    TFile *f_electronTriggerSF= new TFile(std::string(inputFile).c_str(),"READ");

    h_abseta_pt_ratio=(TH2D*)f_electronTriggerSF->Get("electrontrig_sf_eta_pt");

}

double EleTriggerHelper::GetSF(double electronPt, double electronEta, int syst){
  if(electronPt==0.0){return 1.0;}
  //std::cout<<electronPt<<" "<<electronEta<<std::endl;
  int thisbin=0;
  double searcheta=electronEta;
  double searchpt=TMath::Min(electronPt,499.0);

  thisbin = h_abseta_pt_ratio->FindBin(searcheta,searchpt);
  double nomval=h_abseta_pt_ratio->GetBinContent(thisbin);
  double error=h_abseta_pt_ratio->GetBinError(thisbin);
  double upval=nomval+error;
  double downval=nomval-error;

  // if(syst==0){std::cout<<"Trigger SF "<<std::endl; std::cout<<nomval<<" "<<upval<<" "<<downval<<std::endl;}

  if (syst==-1){return downval;}
  else if (syst==1){return upval;}
  else {return nomval;}
}

class MuTriggerHelper
{
  public:
    MuTriggerHelper();
    double GetSF(double muonPt, double muonEta, int syst);

  private:
    TH2D *h_mu_TRIGGER_abseta_pt;

};

MuTriggerHelper::MuTriggerHelper()
{
    std::string inputFile = "/nfs/dust/cms/user/asaibel/DataFilesForScriptGenerator/MuonTriggerPerformance_Sep06.root";

    TFile *f_muonTriggerSF= new TFile(std::string(inputFile).c_str(),"READ");

    h_mu_TRIGGER_abseta_pt=(TH2D*)f_muonTriggerSF->Get("muontrig_sf_abseta_pt");


}

double MuTriggerHelper::GetSF(double muonPt, double muonEta, int syst){
  if(muonPt==0.0){return 1.0;}
  //std::cout<<muonPt<<" "<<muonEta<<std::endl;
  int thisBin=0;
  double searchEta=fabs(muonEta);
  double searchPt=TMath::Min(muonPt,499.0);

  thisBin = h_mu_TRIGGER_abseta_pt->FindBin(searchEta,searchPt);
  double nomval=h_mu_TRIGGER_abseta_pt->GetBinContent(thisBin);
  double error=h_mu_TRIGGER_abseta_pt->GetBinError(thisBin);
  double upval=nomval+error;
  double downval=nomval-error;


  // if(syst==0){std::cout<<"Trigger SF "<<std::endl; std::cout<<nomval<<" "<<upval<<" "<<downval<<std::endl;}

  if (syst==-1){return downval;}
  else if (syst==1){return upval;}
  else {return nomval;}
}

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

std::cout<<"processname" <<processname<<std::endl;
    std::cout<<"suffix" <<suffix<<std::endl;

  std::vector<TString> databaseRelevantFilenames;

  int eventsAnalyzed=0;
  float sumOfWeights=0;

  int DoWeights=1;

  //initialize Trigger Helper
  EleTriggerHelper electronTriggerHelper=EleTriggerHelper();
  MuTriggerHelper muonTriggerHelper=MuTriggerHelper();

  if(processname=="SingleEl" || processname=="SingleMu"){DoWeights=0; std::cout<<"is data, dont use nominal weihgts"<<std::endl;}


  // read in samples to add to chain and get relevant names for the database
  std::map<TString, TString> sampleDataBaseIdentifiers;
  std::map<TString, std::map<TString, long>> sampleDataBaseFoundEvents;
  std::map<TString, std::map<TString, long>> sampleDataBaseLostEvents;
    
  
  string buf;
  stringstream ss(filenames); 
  while (ss >> buf){
    chain->Add(buf.c_str());
    TString thisfilename = buf.c_str();
    TString originalfilename=buf.c_str();
    std::cout<<"file "<<buf.c_str()<<" "<<thisfilename<<std::endl; // karim debug 
    // cut of directories
    thisfilename.Replace(0,thisfilename.Last('/')+1,"");
    //cut if trailing tree and root
    thisfilename.Replace(thisfilename.Last('_'),thisfilename.Length(),"");
    //remove number
    int lastUnderscore=thisfilename.Last('_');
    thisfilename.Replace(thisfilename.Last('_'),1,"");
    thisfilename.Replace(thisfilename.Last('_'),lastUnderscore-thisfilename.Last('_'),"");
    //remove remaining underscores
    while(thisfilename.Last('_')>=0){ thisfilename.Replace(thisfilename.Last('_'),1,"");}
    std::cout<<" relevant database name "<<thisfilename<<std::endl;
    sampleDataBaseIdentifiers[originalfilename]=thisfilename;
    //check if already in vectr
    if(! (std::find(databaseRelevantFilenames.begin(),databaseRelevantFilenames.end(),thisfilename)!=databaseRelevantFilenames.end()  )){
      databaseRelevantFilenames.push_back(thisfilename.Copy());
      //sampleDataBaseFoundEvents["jt42"][thisfilename]=0;
      //sampleDataBaseLostEvents["jt42"][thisfilename]=0;
      //sampleDataBaseFoundEvents["jt52"][thisfilename]=0;
      //sampleDataBaseLostEvents["jt52"][thisfilename]=0;
      //sampleDataBaseFoundEvents["jt62"][thisfilename]=0;
      //sampleDataBaseLostEvents["jt62"][thisfilename]=0;
      sampleDataBaseFoundEvents["jt43"][thisfilename]=0;
      sampleDataBaseLostEvents["jt43"][thisfilename]=0;
      sampleDataBaseFoundEvents["jt53"][thisfilename]=0;
      sampleDataBaseLostEvents["jt53"][thisfilename]=0;
      sampleDataBaseFoundEvents["jt63"][thisfilename]=0;
      sampleDataBaseLostEvents["jt63"][thisfilename]=0;
      sampleDataBaseFoundEvents["jt44"][thisfilename]=0;
      sampleDataBaseLostEvents["jt44"][thisfilename]=0;
      sampleDataBaseFoundEvents["jt54"][thisfilename]=0;
      sampleDataBaseLostEvents["jt54"][thisfilename]=0;
      sampleDataBaseFoundEvents["jt64"][thisfilename]=0;
      sampleDataBaseLostEvents["jt64"][thisfilename]=0;
    }
  }
  std::cout<<"relevant db samplenames"<<std::endl;
  for(unsigned int isn=0; isn<databaseRelevantFilenames.size();isn++){
    std::cout<<databaseRelevantFilenames.at(isn)<<std::endl;
    }
    
  chain->SetBranchStatus("*",0);

  TFile* outfile=new TFile(outfilename,"RECREATE");

  TStopwatch* totalWatch= new TStopwatch();
  TStopwatch* databaseWatch= new TStopwatch();
  double memTime=0;

  int nEventsVetoed=0;
  int Evt_ID;
  int Evt_Run;
  int Evt_Lumi;
  
  chain->SetBranchStatus("Evt_ID",1);
  chain->SetBranchStatus("Evt_Run",1);
  chain->SetBranchStatus("Evt_Lumi",1);
  
  chain->SetBranchAddress("Evt_ID",&Evt_ID);
  chain->SetBranchAddress("Evt_Run",&Evt_Run);
  chain->SetBranchAddress("Evt_Lumi",&Evt_Lumi);


  // initialize variables from tree
"""
  return retstr

def InitDataBase(thisDataBase=[]):
  thisDataBaseName=thisDataBase[0]
  thisDataBasePath=thisDataBase[1]
 
  rstr= """
  // book the database
  
  """
  
  rstr+="  std::vector<MEMDataBase*> "+thisDataBaseName+"DB; \n"
  rstr+="  for(unsigned int isn=0; isn<databaseRelevantFilenames.size();isn++){ \n"
  rstr+="  "+thisDataBaseName+"DB.push_back(new MEMDataBase(\""+thisDataBasePath+"\"));"+"\n"
  rstr+="  "+thisDataBaseName+"DB.back()->AddSample(databaseRelevantFilenames.at(isn),databaseRelevantFilenames.at(isn)+\"_index.txt\");\n"
  rstr+="  "+thisDataBaseName+"DB.back()->PrintStructure();\n"
  rstr+="  std::cout<<\"loaded database for \"<<databaseRelevantFilenames.at(isn)<<std::endl;\n"
  rstr+="  }\n"
  rstr+="  double "+thisDataBaseName+"p=-99.9;\n"
  rstr+="  double "+thisDataBaseName+"p_sig=-99.9;\n"
  rstr+="  double "+thisDataBaseName+"p_bkg=-99.9;\n"
  rstr+="  double "+thisDataBaseName+"p_err_sig=-99.9;\n"
  rstr+="  double "+thisDataBaseName+"p_err_bkg=-99.9;\n"
  rstr+="  double "+thisDataBaseName+"n_perm_sig=-99.9;\n"
  rstr+="  double "+thisDataBaseName+"n_perm_bkg=-99.9;\n"
  rstr+="  DataBaseMEMResult* "+thisDataBaseName+"DummyResultPointer= new DataBaseMEMResult();\n"
  rstr+="  int "+thisDataBaseName+"FoundResult = 1;\n"
  
  return rstr

def readOutDataBase(thisDataBase=[]):
  thisDataBaseName=thisDataBase[0]
  thisDataBasePath=thisDataBase[1]
  skipNonExistingEvent=thisDataBase[2]
  
  rstr= """
  // read the database
    //std::cout<<std::endl<<"run lumi event "<<Evt_Run<<" "<<Evt_Lumi<<" "<<Evt_ID<<std::endl;
  """
  
  rstr+="  "+thisDataBaseName+"p="+thisDataBaseName+"DummyResultPointer->p;\n"
  rstr+="  "+thisDataBaseName+"p_sig="+thisDataBaseName+"DummyResultPointer->p_sig;\n"
  rstr+="  "+thisDataBaseName+"p_bkg="+thisDataBaseName+"DummyResultPointer->p_bkg;\n"
  rstr+="  "+thisDataBaseName+"p_err_sig="+thisDataBaseName+"DummyResultPointer->p_err_sig;\n"
  rstr+="  "+thisDataBaseName+"p_err_bkg="+thisDataBaseName+"DummyResultPointer->p_err_bkg;\n"
  rstr+="  "+thisDataBaseName+"n_perm_sig="+thisDataBaseName+"DummyResultPointer->n_perm_sig;\n"
  rstr+="  "+thisDataBaseName+"n_perm_bkg="+thisDataBaseName+"DummyResultPointer->n_perm_bkg;\n"
  
  rstr+="""
    //get name of current file so that the correct db can be read
    // already done in this version due to trigger stuff
    //TString currentfilename="";
    //currentfilename = chain->GetCurrentFile()->GetName();    
    //std::cout<<"current fileanme for this event "<<currentfilename<<std::endl; // karim debug 
    // cut of directories
    //currentfilename.Replace(0,currentfilename.Last('/')+1,"");
    //cut if trailing tree and root
    //currentfilename.Replace(currentfilename.Last('_'),currentfilename.Length(),"");
    //remove number
    //int lastUnderscore=currentfilename.Last('_');
    //currentfilename.Replace(currentfilename.Last('_'),1,"");
    //currentfilename.Replace(currentfilename.Last('_'),lastUnderscore-currentfilename.Last('_'),"");
    //remove remaining underscores
    //while(currentfilename.Last('_')>=0){ currentfilename.Replace(currentfilename.Last('_'),1,"");}
    TString currentRelevantSampleName=sampleDataBaseIdentifiers[currentfilename];
    //std::cout<<" relevant database name "<<currentRelevantSampleName<<std::endl;
  """
  
  rstr+=" // loop over subsamples of this database\n"
  rstr+="    int nfoundresults=0;\n"
  
  rstr+="  if(N_BTagsM>=3){ \n"
  rstr+="  databaseWatch->Start(); \n"
  
  rstr+="  for(unsigned int isn=0; isn<"+thisDataBaseName+"DB.size();isn++){ \n"
  rstr+="    if(databaseRelevantFilenames.at(isn)==currentRelevantSampleName){;\n"
  rstr+="         DataBaseMEMResult "+thisDataBaseName+"Result = "+thisDataBaseName+"DB.at(isn)->GetMEMResult(databaseRelevantFilenames.at(isn),Evt_Run,Evt_Lumi,Evt_ID);\n"

  #rstr+="        std::cout<<\" p p_sig p_bkg p_err_sig p_err_bkg n_perm_sig n_perm_bkg \"<<"+thisDataBaseName+"p<<\" \"<<"+thisDataBaseName+"p_sig<<\"   \"<<"+thisDataBaseName+"p_bkg<<\" \"<<"+thisDataBaseName+"p_err_sig<<\" \"<<"+thisDataBaseName+"p_err_bkg<<\" \"<<"+thisDataBaseName+"n_perm_sig<<\" \"<<"+thisDataBaseName+"n_perm_bkg<<\" \"<<std::endl;\n"
  
  rstr+="        // check if the event was found using the default values. If any event was found the return values should be different and the resuilt will be replaced\n"
  #rstr+="        if(("+thisDataBaseName+"Result.p != "+thisDataBaseName+"DummyResultPointer->p) or ("+thisDataBaseName+"Result.p_sig != "+thisDataBaseName+"DummyResultPointer->p_sig) or ("+thisDataBaseName+"Result.p_bkg != "+thisDataBaseName+"DummyResultPointer->p_bkg) or ("+thisDataBaseName+"Result.p_err_sig != "+thisDataBaseName+"DummyResultPointer->p_err_sig) or ("+thisDataBaseName+"Result.p_err_bkg != "+thisDataBaseName+"DummyResultPointer->p_err_bkg) or ("+thisDataBaseName+"Result.n_perm_sig != "+thisDataBaseName+"DummyResultPointer->n_perm_sig) or ("+thisDataBaseName+"Result.n_perm_bkg != "+thisDataBaseName+"DummyResultPointer->n_perm_bkg)){\n"
  rstr+="        if(("+thisDataBaseName+"Result.p != -99)){\n"
  rstr+="        nfoundresults+=1;"

  rstr+="      "+thisDataBaseName+"p="+thisDataBaseName+"Result.p;\n"
  rstr+="      "+thisDataBaseName+"p_sig="+thisDataBaseName+"Result.p_sig;\n"
  rstr+="      "+thisDataBaseName+"p_bkg="+thisDataBaseName+"Result.p_bkg;\n"
  rstr+="      "+thisDataBaseName+"p_err_sig="+thisDataBaseName+"Result.p_err_sig;\n"
  rstr+="      "+thisDataBaseName+"p_err_bkg="+thisDataBaseName+"Result.p_err_bkg;\n"
  rstr+="      "+thisDataBaseName+"n_perm_sig="+thisDataBaseName+"Result.n_perm_sig;\n"
  rstr+="      "+thisDataBaseName+"n_perm_bkg="+thisDataBaseName+"Result.n_perm_bkg;\n"
  #rstr+="      std::cout<<\"found database entry \"<<std::endl;\n"
  rstr+="    }\n"
  rstr+="    }\n"
  rstr+="  }// end db loop \n"
  rstr+="    if(nfoundresults!=1){\n"
  rstr+="    //std::cout<<\"WARNING found not exaclty one result \"<<nfoundresults<<\" \"<<currentRelevantSampleName<<\" \"<<Evt_ID<<\" \"<<N_Jets<<\" \"<<N_BTagsM<<std::endl;\n"
  rstr+="    if(N_BTagsM>=3){\n"
  rstr+="      std::cout<<\"VETO this event\"<<\" \"<<currentRelevantSampleName<<\" \"<<Evt_ID<<\" \"<<N_Jets<<\" \"<<N_BTagsM<<std::endl;\n"
  rstr+="      std::cout<<\"RedoThisEvent\"<<\" \"<<currentRelevantSampleName<<\" \"<<currentfilename<<\" \"<<Evt_Run<<\" \"<<Evt_Lumi<<\" \"<<Evt_ID<<std::endl;\n"
  rstr+="      "+thisDataBaseName+"FoundResult=0;\n"
  rstr+="      nEventsVetoed+=1;\n"
  rstr+="""
	       if(N_Jets==4 && N_BTagsM==3){sampleDataBaseLostEvents["jt43"][currentRelevantSampleName]+=1;}
	       else if(N_Jets==4 && N_BTagsM>=4){sampleDataBaseLostEvents["jt44"][currentRelevantSampleName]+=1;}  
	       else if(N_Jets==5 && N_BTagsM==3){sampleDataBaseLostEvents["jt53"][currentRelevantSampleName]+=1;}  
	       else if(N_Jets==5 && N_BTagsM>=4){sampleDataBaseLostEvents["jt54"][currentRelevantSampleName]+=1;}  
	       else if(N_Jets>=6 && N_BTagsM==3){sampleDataBaseLostEvents["jt63"][currentRelevantSampleName]+=1;}  
	       else if(N_Jets>=6 && N_BTagsM>=4){sampleDataBaseLostEvents["jt64"][currentRelevantSampleName]+=1;}  
	"""
  rstr+="    }\n"
  rstr+="  }\n"
  rstr+="  else{\n"
  rstr+="      "+thisDataBaseName+"FoundResult=1;\n"
  rstr+="""
	       if(N_Jets==4 && N_BTagsM==3){sampleDataBaseFoundEvents["jt43"][currentRelevantSampleName]+=1;}
	       else if(N_Jets==4 && N_BTagsM>=4){sampleDataBaseFoundEvents["jt44"][currentRelevantSampleName]+=1;}  
	       else if(N_Jets==5 && N_BTagsM==3){sampleDataBaseFoundEvents["jt53"][currentRelevantSampleName]+=1;}  
	       else if(N_Jets==5 && N_BTagsM>=4){sampleDataBaseFoundEvents["jt54"][currentRelevantSampleName]+=1;}  
	       else if(N_Jets>=6 && N_BTagsM==3){sampleDataBaseFoundEvents["jt63"][currentRelevantSampleName]+=1;}  
	       else if(N_Jets>=6 && N_BTagsM>=4){sampleDataBaseFoundEvents["jt64"][currentRelevantSampleName]+=1;}  
      """  
  #rstr+="  std::cout<<\"FOUNDEVENT\"<<\" \"<<currentRelevantSampleName<<\" \"<<Evt_ID<<\" \"<<N_Jets<<\" \"<<N_BTagsM<<std::endl;\n"
  rstr+=" }\n"
  rstr+="  databaseWatch->Stop(); memTime+=databaseWatch->RealTime();\n"
  if skipNonExistingEvent:
    rstr+="  if("+thisDataBaseName+"FoundResult==0 and N_BTagsM>=3){ std::cout<<\"skipping\"<<std::endl; continue; }\n"
  rstr+="  }\n"
  #if skipNonExistingEvent:
    #rstr+="  if("+thisDataBaseName+"FoundResult==0 and N_BTagsM>=3){ std::cout<<\"skipping\"<<std::endl; continue; }\n"
  
  #rstr+="  std::cout<<\"FINAL p p_sig p_bkg p_err_sig p_err_bkg n_perm_sig n_perm_bkg \"<<"+thisDataBaseName+"p<<\" \"<<"+thisDataBaseName+"p_sig<<\" \"<<"+thisDataBaseName+"p_bkg<<\" \"<<"+thisDataBaseName+"p_err_sig<<\" \"<<"+thisDataBaseName+"p_err_bkg<<\" \"<<"+thisDataBaseName+"n_perm_sig<<\" \"<<"+thisDataBaseName+"n_perm_bkg<<\" \"<<std::endl;\n"
  
  return rstr
  
  
  # Todo write this function that loops over the vector and books the databases and creates the variables ->CHECK
  # write a function that creates the event lumi and run variales and sets the branches  ->CHECK
  # write a function that reads every database. In case of the vector check every one for the -2 return values ->CHECK
  # need to change those return values for blr from -2 to -100 or something -> CHECK?
  # need to set those variables to initalized ones -> CHECK
  # add those functions in the appropriate places ->CHECK
  # need to update the linked database code to the most current one. Also maybe create extra branch or handle the headers differently -> CHECK

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


def fillHistoSyst(name,varname,weight,systnames,systweights):
  text='      float weight_'+name+'='+weight+';\n'
  for sn,sw in zip(systnames,systweights):
    text+=fillHisto(name+sn,varname,'('+sw+')*(weight_'+name+')')
  return text


def fillTwoDimHistoSyst(name,varname1,varname2,weight,systnames,systweights):
  text='      float weight_'+name+'='+weight+';\n'
  for sn,sw in zip(systnames,systweights):
    text+=fillTwoDimHisto(name+sn,varname1,varname2,'('+sw+')*(weight_'+name+')')
  return text


def startLoop():
  return """
  // loop over all events
  long nentries = chain->GetEntries();
  cout << "total number of events: " << nentries << endl;

  for (long iEntry=skipevents;iEntry<nentries;iEntry++) {
    if(iEntry==maxevents) break;
    if(iEntry%10000==0) cout << "analyzing event " << iEntry << endl;

    chain->GetEntry(iEntry);

    TString currentfilename="";
    currentfilename = chain->GetCurrentFile()->GetName();   
    int hasTrigger=0;
    if(currentfilename.Index("withTrigger")!=-1){hasTrigger=1;}
    eventsAnalyzed++;
    sumOfWeights+=Weight;

    // Trigger SF
  //  double muonPt=0.0;
 //   double muonEta=0.0;
 //   float muonPt=0.0;
//    float muonEta=0.0;
    

 //   if(N_TightMuons==1){muonPt=Muon_Pt[0]; muonEta=Muon_Eta[0];}
 //   else{muonPt=0.0; muonEta=0.0;}
  //  double electronPt=0.0;
   // double electronEta=0.0;

    //if(N_TightElectrons==1){electronPt=Electron_Pt[0]; electronEta=Electron_Eta[0];}
   // else{electronPt=0.0; electronEta=0.0;}
    //Debugging: print lepton pt, eta and the correspronding scale factor. 
  // /* std::cout << "Electron_Pt = " << electronPt << " , Electron_Eta = " << electronEta << std::endl;
//    std::cout << "corresponding scale factor = " << electronTriggerHelper.GetSF(electronPt,electronEta,0) << std::endl;
  //  std::cout << "Muon_Pt = " << muonPt << " , Muon_Eta = " << muonEta << std::endl;
  //  std::cout << "corresponding scale factor = " << muonTriggerHelper.GetSF(muonPt,muonEta,0) << std::endl;*/
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


def fillHisto(histo,var,weight):
  text= '        if(('+weight+')!=0)\n'
  text+='          h_'+histo+'->Fill(fmin(h_'+histo+'->GetXaxis()->GetXmax()-1e-6,fmax(h_'+histo+'->GetXaxis()->GetXmin()+1e-6,'+var+')),'+weight+');\n'
  return text


def fillTwoDimHisto(histo,var1,var2,weight):
  text= '        if(('+weight+')!=0)\n'
  text+='          h_'+histo+'->Fill(fmin(h_'+histo+'->GetXaxis()->GetXmax()-1e-6,fmax(h_'+histo+'->GetXaxis()->GetXmin()+1e-6,'+var1+')),fmin(h_'+histo+'->GetYaxis()->GetXmax()-1e-6,fmax(h_'+histo+'->GetYaxis()->GetXmin()+1e-6,'+var2+')),'+weight+');\n'
  return text


def endLoop():
  return """
  }\n // end of event loop
"""


def varLoop(i,n):
  return '      for(uint '+str(i)+'=0; '+str(i)+'<'+str(n)+'; '+str(i)+'++)'


def getFoot():
  return """
  outfile->Write();
  outfile->Close();
  std::ofstream f_nevents((string(outfilename)+".cutflow.txt").c_str());
  f_nevents << "0" << " : " << "all" << " : " << eventsAnalyzed << " : " << sumOfWeights <<endl;
  f_nevents.close();
  std::cout<<"events vetoed because if missing mem "<<nEventsVetoed<<std::endl;
  std::cout<<"all done"<<std::endl;
  totalWatch->Stop();
  std::cout<<"total time "<<totalWatch->RealTime()<<std::endl;
  std::cout<<"time for databse "<<memTime<<std::endl;
  
  std::cout<<"All found events"<<std::endl;
  for(auto const &ent1 : sampleDataBaseFoundEvents) {
  // ent1.first is the first key
    for(auto const &ent2 : ent1.second) {
      // ent2.first is the second key
      // ent2.second is the data
      std::cout<<"FOUNDEVENTSINCAT "<<ent1.first<<" "<<ent2.first<<" "<<ent2.second<<std::endl;
    }
  }
  std::cout<<"All lost events"<<std::endl;
  for(auto const &ent1 : sampleDataBaseLostEvents) {
  // ent1.first is the first key
    for(auto const &ent2 : ent1.second) {
      // ent2.first is the second key
      // ent2.second is the data
      std::cout<<"LOSTEVENTSINCAT "<<ent1.first<<" "<<ent2.first<<" "<<ent2.second<<std::endl;
    }
  }

  
}

int main(){
  plot();
}
"""


def compileProgram(scriptname,usesDataBases):
  p = subprocess.Popen(['root-config', '--cflags', '--libs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  out, err = p.communicate()
  memDBccfiles=[]
  if usesDataBases:
    memDBccfiles=glob.glob('/nfs/dust/cms/user/kelmorab/DataBaseCodeForScriptGenerator/MEMDataBase/MEMDataBase/src/*.cc') 
    #TODO update the dataBases code
  cmd= ['g++']+out[:-1].split(' ')+['-lTMVA']+memDBccfiles+[scriptname+'.cc','-o',scriptname]
  print cmd
  subprocess.call(cmd)


def createProgram(scriptname,plots,samples,catnames=[""],catselections=["1"],systnames=[""],allsystweights=["1"],additionalvariables=[],dataBases=[]):

  # collect variables
  # list varibles that should not be written to the program automatically

  vetolist=['processname','DoWeights','TMath','electronPt','electronEta','muonPt','muonEta','muonTriggerHelper','electronTriggerHelper','hasTrigger']
  for db in dataBases:
    vetolist.append(db[0]+"p")
    vetolist.append(db[0]+"p_sig")
    vetolist.append(db[0]+"p_bkg")
    vetolist.append(db[0]+"p_err_sig")
    vetolist.append(db[0]+"p_err_bkg")
    vetolist.append(db[0]+"n_perm_sig")
    vetolist.append(db[0]+"n_perm_bkg")
    vetolist.append(db[0]+"FoundResult")
    
  print vetolist # karim debug

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



  # write program
  # start writing program
  script=""
  script+=getHead(dataBases)
  
  for db in dataBases:
    script+=InitDataBase(db)

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
  for db in dataBases:
    script+=readOutDataBase(db)  
  script+="\n"

  # calculate varibles and get TMVA outputs
  script+=variables.calculateVarsProgram()

  # start plotting
  for cn,cs in zip(catnames,catselections):

     # for every category
    script+=startCat(cs,variables)

    # plot everything
    # plot one dimensional plots
    for plot in plots:
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
      for v in variablenames_without_index:
        if not v in variables.variables:
          continue
        if variables.variables[v].arraylength != None:
          assert size_of_loop == None or size_of_loop == variables.variables[v].arraylength
          size_of_loop=variables.variables[v].arraylength

      histoname=cn+n
      script+="\n"
      if size_of_loop!=None:
        exi=variables.getArrayEntries(ex,"i")
        pwi=variables.getArrayEntries(pw,"i")
        script+=varLoop("i",size_of_loop)
        script+="{\n"
        arrayselection=variables.checkArrayLengths(','.join([ex,pw]))
        weight='('+arrayselection+')*('+pwi+')*Weight_XS*categoryweight*sampleweight'
        print histoname
        print exi
        print weight
        script+=fillHistoSyst(histoname,exi,weight,systnames,systweights)
        script+="      }\n"
      else:
        arrayselection=variables.checkArrayLengths(','.join([ex,pw]))
        weight='('+arrayselection+')*('+pw+')*Weight_XS*categoryweight*sampleweight'
        script+=fillHistoSyst(histoname,ex,weight,systnames,systweights)

    # plot two dimensional plots
    for plot in plots:
        if not isinstance(plot,plotutils.TwoDimPlot):
          continue

        n=plot.histo.GetName()
        exX=plot.variable1
        exY=plot.variable2
        pw=plot.selection
        if pw=='':
          pw='1'

        # prepare loop over array variables
        variablenames_without_index=varsNoIndex(exX)
        variablenames_without_index+=varsNoIndex(exY)
        variablenames_without_index+=varsNoIndex(pw)

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
          exiY=variables.getArrayEntries(ex,"i")
          pwi=variables.getArrayEntries(pw,"i")
          script+=varLoop("i",size_of_loop)
          script+="{\n"
          arrayselection=variables.checkArrayLengths(','.join([exX,exY,pw]))
          weight='('+arrayselection+')*('+pwi+')*Weight_XS*categoryweight*sampleweight'
          script+=fillTwoDimHistoSyst(histoname,exiX,exiY,weight,systnames,systweights)
          script+="      }\n"
        else:
          arrayselection=variables.checkArrayLengths(','.join([ex,pw]),variables)
          weight='('+arrayselection+')*('+pw+')*Weight_XS*categoryweight*sampleweight'
          script+=fillTwoDimHistoSyst(histoname,exX,exY,weight,systnames,systweights)

    # finish category
    script+=endCat()

  # finish loop
  script+=endLoop()

  # get program footer
  script+=getFoot()

  # write program text to file
  f=open(scriptname+'.cc','w')
  f.write(script)
  f.close()


def createScript(scriptname,programpath,processname,filenames,outfilename,maxevents,skipevents,cmsswpath,suffix):
  script="#!/bin/bash \n"
  if cmsswpath!='':
    script+="export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch \n"
    script+="source $VO_CMS_SW_DIR/cmsset_default.sh \n"
    script+="export SCRAM_ARCH="+os.environ['SCRAM_ARCH']+"\n"
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
  logdir = os.getcwd()+"/logs"
  if not os.path.exists(logdir):
    os.makedirs(logdir)
  for script in scripts:
    print 'submitting',script
    command=['qsub', '-cwd', '-S', '/bin/bash','-l', 'h=bird*', '-hard','-l', 'os=sld6', '-l' ,'h_vmem=2000M', '-l', 's_vmem=2000M' ,'-o', logdir, '-e', logdir, script]
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


def get_scripts_outputs_and_nentries(samples,maxevents,scriptsfolder,plotspath,programpath,cmsswpath,treejsonfile=""):
  scripts=[]
  outputs=[]
  nentries=[]
  SaveTreeInforamtion={}
  LoadedTreeInformation={}
  if treejsonfile!="":
    print "Loading file with tree event information"
    jsonfile=open(treejsonfile,"r")
    jsonstring=list(jsonfile)[0]
    LoadedTreeInformation=json.loads(jsonstring)
  for s in samples:
    print 'creating scripts for',s.name,'from',s.path
    ntotal_events=0
    njob=0
    events_in_files=0
    files_to_submit=[]
    for fn in s.files:
      events_in_file=0
      if LoadedTreeInformation!={}:
	#print "using tree event information"
	events_in_file=LoadedTreeInformation[fn]
      else:
        f=ROOT.TFile(fn)
        t=f.Get('MVATree')
        events_in_file=t.GetEntries()
      SaveTreeInforamtion[fn]=events_in_file
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
  
  # save tree information to json file
  treejson=json.dumps(SaveTreeInforamtion)
  jsonfile=open(scriptsfolder+'/'+"treejson.json","w")
  jsonfile.write(treejson)
  jsonfile.close()
  print "Saved information about events in trees to ", scriptsfolder+'/'+"treejson.json"
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

# the dataBases should be defined as follows e.g. [[memDB,path],[blrDB,path]]
def plotParallel(name,maxevents,plots,samples,catnames=[""],catselections=["1"],systnames=[""],systweights=["1"],additionalvariables=[],dataBases=[],treeInformationJsonFile=""):
  workdir=os.getcwd()+'/workdir/'+name
  outputpath=workdir+'/output.root'

  usesDataBases=False
  if dataBases!=[]:
    usesDataBases=True

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
  createProgram(programpath,plots,samples,catnames,catselections,systnames,systweights,additionalvariables, dataBases)
  if not os.path.exists(programpath+'.cc'):
    print 'could not create c++ program'
    sys.exit()
  print 'compiling c++ program'
  compileProgram(programpath, usesDataBases)
  if not os.path.exists(programpath):
    print 'could not compile c++ program'
    sys.exit()

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
  scripts,outputs,nentries=get_scripts_outputs_and_nentries(samples,maxevents,scriptsfolder,plotspath,programpath,cmsswpath,treeInformationJsonFile)

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
