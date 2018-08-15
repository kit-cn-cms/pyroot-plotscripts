# comment 
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
import filecmp
import imp 
import types
import csv
from nafSubmit import *

ROOT.gROOT.SetBatch(True)

def getHead(dataBases,addCodeInterfaces=[]):
  
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
#include <TString.h>
#include <TH2D.h>
#include "LHAPDF/LHAPDF.h"
#include "TGraphAsymmErrors.h"
#include "TStopwatch.h"
#include <tuple>

"""
  for addCodeInt in addCodeInterfaces:
    retstr+=addCodeInt.getIncludeLines()
  
  if dataBases!=[]:
    retstr+="""
#include "/nfs/dust/cms/user/kelmorab/DataBaseCodeForScriptGenerator/MEMDataBaseSpring17/MEMDataBase/MEMDataBase/interface/MEMDataBase.h"
"""

  retstr+="""

using namespace std;
"""

  for addCodeInt in addCodeInterfaces:
    retstr+=addCodeInt.getAdditionalFunctionDefinitionLines()
  

  retstr+="""

// Event filter to be used with CSV files

class EventFilter {

  public:
    EventFilter(std::string filename);
    ~EventFilter();
    bool KeepEvent(Long64_t Evt_Run, Long64_t Evt_Lumi, Long64_t Evt_ID);
    int GetNFiltered();
    
  private:
    std::vector<long> vec_run;
  std::vector<long> vec_lumi;
  std::vector<long> vec_evt;
  int listLength;
  int nEventsFiltered;
  
  
    };
    
EventFilter::EventFilter( std::string filename){
  
  listLength=0;
  nEventsFiltered=0;
  
  std::ifstream eventList(filename);
  TString dump="";
  char comma;
  
  int count=0;
  bool readline=true;
  bool readTitle=false;
  long run;
  long lumi;
  long evt;
  
  if(filename!="" and filename!="NONE"){
    std::cout<<"reading Event list to be filtered"<<std::endl;
    
    eventList>>dump; eventList>>dump;
    while (eventList>>run>>comma>>lumi>>comma>>evt)
    {
      count++;
      std::cout<<count<<std::endl;
      std::cout<<comma<<std::endl;
      std::cout<<run<<" "<<lumi<<" "<<evt<<std::endl;
      vec_run.push_back(run);
      vec_lumi.push_back(lumi);
      vec_evt.push_back(evt);
    }
    
    eventList.close();
    std::cout<<"done reading the event filter list"<<std::endl;
    std::cout<<vec_run.size()<<" "<<vec_lumi.size()<<" "<<vec_evt.size()<<" "<<std::endl;
    listLength=vec_run.size();
  }
  
}

bool EventFilter::KeepEvent(Long64_t Evt_Run, Long64_t Evt_Lumi, Long64_t Evt_ID){
  bool eventToBeKept=true;
  for(int i=0; i<listLength; i++){
    if(vec_run.at(i)==Evt_Run and vec_lumi.at(i)==Evt_Lumi and vec_evt.at(i)==Evt_ID){
      eventToBeKept=false;
      break;
    }
  }
  if(eventToBeKept==false){nEventsFiltered++;}
  return eventToBeKept;
  
}

int EventFilter::GetNFiltered(){
  return nEventsFiltered;
}

  
//hacked Lepton SF Helper from MiniAODHelper

class LeptonSFHelper {

 public:
  LeptonSFHelper( );
  ~LeptonSFHelper( );

  float GetElectronSF(  float electronPt , float electronEta , int syst , std::string type  );
  float GetMuonSF(  float muonPt , float muonEta , int syst , std::string type  );
  float GetElectronElectronSF( float electronEta1, float electronEta2, int syst , std::string type);
  float GetMuonMuonSF( float muonEta1, float muonEta2, int syst , std::string type);
  float GetElectronMuonSF( float electronEta, float muonEta, int syst , std::string type);
  void  ChangeMuIsoHistos(bool is_DL);

 private:

  void SetElectronHistos( );
  void SetMuonHistos( );
  void SetElectronElectronHistos( );
  void SetMuonMuonHistos( );
  void SetElectronMuonHistos( );
  int findPoint(TGraphAsymmErrors& graph,float& x_);
  float getValue(TGraphAsymmErrors& graph,float& x_,int syst);

  TH2F *h_ele_ID_abseta_pt_ratioGtoH;
  TH2F *h_ele_ID_abseta_pt_ratioBtoF;

  TH2F *h_ele_TRIGGER_abseta_pt_ratio;
  TH2F *h_ele_ISO_abseta_pt_ratio;
  TH2F *h_ele_GFS_abseta_pt_ratio;

  TH2F *h_mu_ID_abseta_pt_ratio;
  TH1D *h_mu_HIP_eta_ratio;
  TH2F *h_mu_TRIGGER_abseta_pt;
  TH2F *h_mu_ISO_abseta_pt_ratio;
  
    TH2F *h_mu_ID_abseta_pt_ratioBtoF;
  TGraphAsymmErrors *h_mu_HIP_eta_ratioBtoF;
  TH2F *h_mu_TRIGGER_abseta_ptBtoF;
  TH2F *h_mu_ISO_abseta_pt_ratioBtoF;

  TH2F *h_mu_ID_abseta_pt_ratioGtoH;
  TGraphAsymmErrors *h_mu_HIP_eta_ratioGtoH;
  TH2F *h_mu_TRIGGER_abseta_ptGtoH;
  TH2F *h_mu_ISO_abseta_pt_ratioGtoH;

  
  TH2F *h_ele_ele_TRIGGER_abseta_abseta;
  TH2F *h_mu_mu_TRIGGER_abseta_abseta;
  TH2F *h_ele_mu_TRIGGER_abseta_abseta;

  float electronMaxPt;
  float electronMaxPtHigh;
  float electronMaxPtHigher;
  float muonMaxPt;
  float muonMaxPtHigh;
  float ljets_mu_BtoF_lumi;
  float ljets_mu_GtoH_lumi;
  float ljets_ele_BtoF_lumi;
  float ljets_ele_GtoH_lumi;  

};

//PUBLIC
LeptonSFHelper::LeptonSFHelper( ){

  //std::cout << "Initializing Lepton scale factors" << std::endl;

  SetElectronHistos( );
  SetMuonHistos( );
  SetElectronElectronHistos( );
  SetMuonMuonHistos( );
  SetElectronMuonHistos( );

  electronMaxPt = 150.0;
  electronMaxPtHigh= 201.0;
  electronMaxPtHigher=499.0;
  muonMaxPt = 119.0;
  muonMaxPtHigh = 499.0;
  
  ljets_mu_BtoF_lumi=19691.782;
  ljets_mu_GtoH_lumi=16226.452;
  ljets_ele_BtoF_lumi=19691.782;
  ljets_ele_GtoH_lumi=16226.452;

}

LeptonSFHelper::~LeptonSFHelper( ){

}

float LeptonSFHelper::GetElectronSF(  float electronPt , float electronEta , int syst , std::string type  ) {
  if ( electronPt == 0.0 ){ return 1.0; }

  int thisBin=0;

  float searchEta=electronEta;
  float searchPt=TMath::Min( electronPt , electronMaxPt ); // if e_pt < 150 use the corresponding bin
  if(searchPt==electronMaxPt) {searchPt=electronMaxPtHigher;}; // if e_pt >= 150 go to last bin by setting searchpt to 499
  if (type=="Trigger"){
    searchPt=TMath::Min( electronPt , electronMaxPtHigh ); // if pt > 200 use overflow bin by setting searchpt to 201
  }

  float nomval = 0;
  float error = 0;
  float upval = 0;
  float downval= 0;
  float nomvalBtoF = 0;
  float errorBtoF = 0;
  float upvalBtoF = 0;
  float downvalBtoF= 0;
  float nomvalGtoH = 0;
  float errorGtoH = 0;
  float upvalGtoH = 0;
  float downvalGtoH= 0;


  if ( type == "ID" ){

    thisBin = h_ele_ID_abseta_pt_ratioBtoF->FindBin( searchEta , searchPt );
    nomvalBtoF=h_ele_ID_abseta_pt_ratioBtoF->GetBinContent( thisBin );
    errorBtoF=h_ele_ID_abseta_pt_ratioBtoF->GetBinError( thisBin );
    upvalBtoF=nomvalBtoF+errorBtoF;
    downvalBtoF=nomvalBtoF-errorBtoF;

    thisBin = h_ele_ID_abseta_pt_ratioGtoH->FindBin( searchEta , searchPt );
    nomvalGtoH=h_ele_ID_abseta_pt_ratioGtoH->GetBinContent( thisBin );
    errorGtoH=h_ele_ID_abseta_pt_ratioGtoH->GetBinError( thisBin );
    upvalGtoH=nomvalGtoH+errorGtoH;
    downvalGtoH=nomvalGtoH-errorGtoH;
    
    nomval=(ljets_ele_BtoF_lumi*nomvalBtoF + ljets_ele_GtoH_lumi * nomvalGtoH)/(ljets_ele_BtoF_lumi+ljets_ele_GtoH_lumi);
    upval=(ljets_ele_BtoF_lumi*upvalBtoF + ljets_ele_GtoH_lumi * upvalGtoH)/(ljets_ele_BtoF_lumi+ljets_ele_GtoH_lumi);
    downval=(ljets_ele_BtoF_lumi*downvalBtoF + ljets_ele_GtoH_lumi * downvalGtoH)/(ljets_ele_BtoF_lumi+ljets_ele_GtoH_lumi);

  }
  else if ( type == "Trigger" ){

    thisBin = h_ele_TRIGGER_abseta_pt_ratio->FindBin( searchPt, searchEta );
    nomval=h_ele_TRIGGER_abseta_pt_ratio->GetBinContent( thisBin );
    error=h_ele_TRIGGER_abseta_pt_ratio->GetBinError( thisBin );
    upval=nomval+error;
    downval=nomval-error;

  }
  else if ( type == "Iso" ){

    thisBin = h_ele_ISO_abseta_pt_ratio->FindBin( searchEta , searchPt );
    nomval=h_ele_ISO_abseta_pt_ratio->GetBinContent( thisBin );
    error=h_ele_ISO_abseta_pt_ratio->GetBinError( thisBin );
    upval=nomval+error;  //DANGERZONE need to add pT depnednet 1% uncertainty
    downval=nomval-error;
    if(electronPt<20 || electronPt>80) {
        upval=upval*( 1.0+sqrt(0.01*0.01) );
        downval=downval*( 1.0-sqrt(0.01*0.01) );
    }

  }
  else if ( type == "GFS" ){

    thisBin = h_ele_GFS_abseta_pt_ratio->FindBin( searchEta , searchPt );
    nomval=h_ele_GFS_abseta_pt_ratio->GetBinContent( thisBin );
    error=h_ele_GFS_abseta_pt_ratio->GetBinError( thisBin );
    upval=nomval+error; //DANGERZONE need to add pT depnednet 1% uncertainty
    downval=nomval-error;
    if(electronPt<20 || electronPt>80) {
        upval=upval*( 1.0+sqrt(0.01*0.01) );
        downval=downval*( 1.0-sqrt(0.01*0.01) );
    }

  }
  else {

    std::cout << "Unknown Type. Supported Types are: ID, Trigger, Iso" << std::endl;
    nomval = -1;
    upval = -1;
    downval= -1;

  }

  if ( syst==-1 ){ return downval; }
  else if ( syst==1 ){ return upval; }
  else { return nomval; }

}

float LeptonSFHelper::GetMuonSF(  float muonPt , float muonEta , int syst , std::string type  ){
  if ( muonPt == 0.0 ){ return 1.0; }

  int thisBin=0;

  float searchEta=fabs( muonEta ); 
  float searchPt=TMath::Min( muonPt , muonMaxPt ); // if muonpt > 119 use last bin
  if (type=="Trigger"){
    searchPt=TMath::Min( muonPt , muonMaxPtHigh );// if muonpt > 499 use last bin
  }
  float nomval = 0;
  float error = 0;
  float upval = 0;
  float downval= 0;
  float nomvalBtoF = 0;
  float errorBtoF = 0;
  float upvalBtoF = 0;
  float downvalBtoF= 0;
  float nomvalGtoH = 0;
  float errorGtoH = 0;
  float upvalGtoH = 0;
  float downvalGtoH= 0;
  

  if ( type == "ID" ){

    thisBin = h_mu_ID_abseta_pt_ratioBtoF->FindBin(  searchPt, searchEta  );
    nomvalBtoF=h_mu_ID_abseta_pt_ratioBtoF->GetBinContent( thisBin );
    errorBtoF=h_mu_ID_abseta_pt_ratioBtoF->GetBinError( thisBin );
    upvalBtoF=( nomvalBtoF+errorBtoF );
    downvalBtoF=( nomvalBtoF-errorBtoF );
    upvalBtoF=upvalBtoF*( 1.0+sqrt(0.01*0.01+0.005*0.005) );
    downvalBtoF=downvalBtoF*( 1.0-sqrt(0.01*0.01+0.005*0.005) );
    
    thisBin = h_mu_ID_abseta_pt_ratioGtoH->FindBin(  searchPt, searchEta  );
    nomvalGtoH=h_mu_ID_abseta_pt_ratioGtoH->GetBinContent( thisBin );
    errorGtoH=h_mu_ID_abseta_pt_ratioGtoH->GetBinError( thisBin );
    upvalGtoH=( nomvalGtoH+errorGtoH );
    downvalGtoH=( nomvalGtoH-errorGtoH );
    upvalGtoH=upvalGtoH*( 1.0+sqrt(0.01*0.01+0.005*0.005) );
    downvalGtoH=downvalGtoH*( 1.0-sqrt(0.01*0.01+0.005*0.005) );

    nomval=(ljets_mu_BtoF_lumi*nomvalBtoF + ljets_mu_GtoH_lumi * nomvalGtoH)/(ljets_mu_BtoF_lumi+ljets_mu_GtoH_lumi);
    upval=(ljets_mu_BtoF_lumi*upvalBtoF + ljets_mu_GtoH_lumi * upvalGtoH)/(ljets_mu_BtoF_lumi+ljets_mu_GtoH_lumi);
    downval=(ljets_mu_BtoF_lumi*downvalBtoF + ljets_mu_GtoH_lumi * downvalGtoH)/(ljets_mu_BtoF_lumi+ljets_mu_GtoH_lumi);

  }
  else if ( type == "Trigger" ){

    thisBin = h_mu_TRIGGER_abseta_ptBtoF->FindBin(  searchPt, searchEta  );
    nomvalBtoF=h_mu_TRIGGER_abseta_ptBtoF->GetBinContent( thisBin );
    errorBtoF=h_mu_TRIGGER_abseta_ptBtoF->GetBinError( thisBin );
    upvalBtoF=( nomvalBtoF+errorBtoF );
    downvalBtoF=( nomvalBtoF-errorBtoF );
    
    thisBin = h_mu_TRIGGER_abseta_ptGtoH->FindBin(  searchPt, searchEta  );
    nomvalGtoH=h_mu_TRIGGER_abseta_ptGtoH->GetBinContent( thisBin );
    errorGtoH=h_mu_TRIGGER_abseta_ptGtoH->GetBinError( thisBin );
    upvalGtoH=( nomvalGtoH+errorGtoH );
    downvalGtoH=( nomvalGtoH-errorGtoH );

    nomval=(ljets_mu_BtoF_lumi*nomvalBtoF + ljets_mu_GtoH_lumi * nomvalGtoH)/(ljets_mu_BtoF_lumi+ljets_mu_GtoH_lumi);
    upval=(ljets_mu_BtoF_lumi*upvalBtoF + ljets_mu_GtoH_lumi * upvalGtoH)/(ljets_mu_BtoF_lumi+ljets_mu_GtoH_lumi);
    downval=(ljets_mu_BtoF_lumi*downvalBtoF + ljets_mu_GtoH_lumi * downvalGtoH)/(ljets_mu_BtoF_lumi+ljets_mu_GtoH_lumi);
    
  }
  else if ( type == "Iso" ){
    
    
    thisBin = h_mu_ISO_abseta_pt_ratioBtoF->FindBin(  searchPt, searchEta  );
    nomvalBtoF=h_mu_ISO_abseta_pt_ratioBtoF->GetBinContent( thisBin );
    errorBtoF=h_mu_ISO_abseta_pt_ratioBtoF->GetBinError( thisBin );
    upvalBtoF=( nomvalBtoF+errorBtoF );
    downvalBtoF=( nomvalBtoF-errorBtoF );
    upvalBtoF=upvalBtoF*(1.0+0.005  );
    downvalBtoF=downvalBtoF*(1.0-0.005 );
    
    thisBin = h_mu_ISO_abseta_pt_ratioGtoH->FindBin(  searchPt, searchEta  );
    nomvalGtoH=h_mu_ISO_abseta_pt_ratioGtoH->GetBinContent( thisBin );
    errorGtoH=h_mu_ISO_abseta_pt_ratioGtoH->GetBinError( thisBin );
    upvalGtoH=( nomvalGtoH+errorGtoH );
    downvalGtoH=( nomvalGtoH-errorGtoH );
    upvalGtoH=upvalGtoH*(1.0+0.005  );
    downvalGtoH=downvalGtoH*( 1.0-0.005 );

    nomval=(ljets_mu_BtoF_lumi*nomvalBtoF + ljets_mu_GtoH_lumi * nomvalGtoH)/(ljets_mu_BtoF_lumi+ljets_mu_GtoH_lumi);
    upval=(ljets_mu_BtoF_lumi*upvalBtoF + ljets_mu_GtoH_lumi * upvalGtoH)/(ljets_mu_BtoF_lumi+ljets_mu_GtoH_lumi);
    downval=(ljets_mu_BtoF_lumi*downvalBtoF + ljets_mu_GtoH_lumi * downvalGtoH)/(ljets_mu_BtoF_lumi+ljets_mu_GtoH_lumi);

  }

  else if ( type == "HIP" ){

    //thisBin = findPoint(h_mu_HIP_eta_ratioBtoF,searchEta );
    nomvalBtoF=getValue(*h_mu_HIP_eta_ratioBtoF,searchEta,0);
    //errorBtoF=h_mu_HIP_eta_ratioBtoF->GetBinError( thisBin );
    upvalBtoF=getValue(*h_mu_HIP_eta_ratioBtoF,searchEta,1);
    downvalBtoF=getValue(*h_mu_HIP_eta_ratioBtoF,searchEta,-1);
    
    //thisBin = h_mu_HIP_eta_ratioGtoH->FindBin( searchEta );
    nomvalGtoH=getValue(*h_mu_HIP_eta_ratioGtoH,searchEta,0);
    //errorGtoH=h_mu_HIP_eta_ratioGtoH->GetBinError( thisBin );
    upvalGtoH=getValue(*h_mu_HIP_eta_ratioGtoH,searchEta,1);
    downvalGtoH=getValue(*h_mu_HIP_eta_ratioGtoH,searchEta,-1);
    
    nomval=(ljets_mu_BtoF_lumi*nomvalBtoF + ljets_mu_GtoH_lumi * nomvalGtoH)/(ljets_mu_BtoF_lumi+ljets_mu_GtoH_lumi);
    upval=(ljets_mu_BtoF_lumi*upvalBtoF + ljets_mu_GtoH_lumi * upvalGtoH)/(ljets_mu_BtoF_lumi+ljets_mu_GtoH_lumi);
    downval=(ljets_mu_BtoF_lumi*downvalBtoF + ljets_mu_GtoH_lumi * downvalGtoH)/(ljets_mu_BtoF_lumi+ljets_mu_GtoH_lumi);
   
//     upval=upval*( 1.0+0.005 );
//     downval=downval*( 1.0-0.005 );


  }
  else {

    std::cout << "Unknown Type. Supported Types are: ID, Trigger, Iso" << std::endl;
    nomval = -1;
    upval = -1;
    downval= -1;

  }


  if ( syst==-1 ){ return downval; }
  else if ( syst==1 ){ return upval; }
  else { return nomval; }


}
float LeptonSFHelper::GetElectronElectronSF(  float electronEta1 , float electronEta2 , int syst , std::string type  ) {

  int thisBin=0;

  float searchEta1=fabs(electronEta1);
  float searchEta2=fabs(electronEta2);

  float nomval = 0;
  if ( type == "Trigger" ){

    thisBin = h_ele_ele_TRIGGER_abseta_abseta->FindBin( searchEta1 , searchEta2 );
    nomval = h_ele_ele_TRIGGER_abseta_abseta->GetBinContent( thisBin );

  }
  return nomval;
}
float LeptonSFHelper::GetMuonMuonSF(  float muonEta1 , float muonEta2 , int syst , std::string type  ) {
  int thisBin=0;

  float searchEta1=fabs(muonEta1);
  float searchEta2=fabs(muonEta2);

  float nomval = 0;
  if ( type == "Trigger" ){

    thisBin = h_mu_mu_TRIGGER_abseta_abseta->FindBin( searchEta1 , searchEta2 );
    nomval = h_mu_mu_TRIGGER_abseta_abseta->GetBinContent( thisBin );

  }
  return nomval;
}
float LeptonSFHelper::GetElectronMuonSF(  float electronEta , float muonEta , int syst , std::string type  ) {
  int thisBin=0;

  float searchEta1=fabs(electronEta);
  float searchEta2=fabs(muonEta);

  float nomval = 0;
  if ( type == "Trigger" ){

    thisBin = h_ele_mu_TRIGGER_abseta_abseta->FindBin( searchEta1 , searchEta2 );
    nomval= h_ele_mu_TRIGGER_abseta_abseta->GetBinContent( thisBin );

  }
  return nomval;
}

void LeptonSFHelper::ChangeMuIsoHistos(bool is_DL) {
    std::string ISOinputFileBtoF =  "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/oct202017/mu_ISO_EfficienciesAndSF_BCDEF.root";
    std::string ISOinputFileGtoH =  "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/oct202017/mu_ISO_EfficienciesAndSF_GH.root";
    TFile *f_ISOSFBtoF = new TFile(std::string(ISOinputFileBtoF).c_str(),"READ");
    TFile *f_ISOSFGtoH = new TFile(std::string(ISOinputFileGtoH).c_str(),"READ");
    if(is_DL) {
        h_mu_ISO_abseta_pt_ratioBtoF=(TH2F*)f_ISOSFBtoF->Get("LooseISO_TightID_pt_eta/pt_abseta_ratio");
        h_mu_ISO_abseta_pt_ratioGtoH=(TH2F*)f_ISOSFGtoH->Get("LooseISO_TightID_pt_eta/pt_abseta_ratio");
    }
    else {
        h_mu_ISO_abseta_pt_ratioBtoF=(TH2F*)f_ISOSFBtoF->Get("TightISO_TightID_pt_eta/pt_abseta_ratio");
        h_mu_ISO_abseta_pt_ratioGtoH=(TH2F*)f_ISOSFGtoH->Get("TightISO_TightID_pt_eta/pt_abseta_ratio");
    }
    delete f_ISOSFBtoF;
    delete f_ISOSFGtoH;
}

//PRIVATE

void LeptonSFHelper::SetElectronHistos( ){

  std::string IDinputFileBtoF = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/oct202017/ele_ID_SF_tight_BCDEF.root";
  std::string IDinputFileGtoH = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/oct202017/ele_ID_SF_tight_GH.root";

  std::string TRIGGERinputFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/oct202017/ele_TriggerSF_Run2016All_v1.root";
  std::string ISOinputFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/oct202017/ele_Reco_EGM2D.root"; // DANGERZONE: no iso SF yet??
  std::string GFSinputFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/oct202017/ele_Reco_EGM2D.root";

  TFile *f_IDSFBtoF = new TFile(std::string(IDinputFileBtoF).c_str(),"READ");
  TFile *f_IDSFGtoH = new TFile(std::string(IDinputFileGtoH).c_str(),"READ");
  
  TFile *f_TRIGGERSF = new TFile(std::string(TRIGGERinputFile).c_str(),"READ");
  TFile *f_ISOSF = new TFile(std::string(ISOinputFile).c_str(),"READ");
  TFile *f_GFSSF = new TFile(std::string(GFSinputFile).c_str(),"READ");

  h_ele_ID_abseta_pt_ratioGtoH=(TH2F*)f_IDSFGtoH->Get("EGamma_SF2D");
  h_ele_ID_abseta_pt_ratioBtoF=(TH2F*)f_IDSFBtoF->Get("EGamma_SF2D");
  h_ele_TRIGGER_abseta_pt_ratio = (TH2F*)f_TRIGGERSF->Get("Ele27_WPTight_Gsf");
  h_ele_ISO_abseta_pt_ratio = (TH2F*)f_ISOSF->Get("EGamma_SF2D");
  h_ele_GFS_abseta_pt_ratio = (TH2F*)f_GFSSF->Get("EGamma_SF2D");

}

void LeptonSFHelper::SetMuonHistos( ){

  std::string IDinputFileBtoF = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/oct202017/mu_ID_EfficienciesAndSF_BCDEF.root";
  std::string IDinputFileGtoH = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/oct202017/mu_ID_EfficienciesAndSF_GH.root";

  std::string TRIGGERinputFileBtoF =  "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/oct202017/mu_TRIGGER_BtoF.root";
  std::string TRIGGERinputFileGtoH =  "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/oct202017/mu_TRIGGER_GtoH.root";

  std::string ISOinputFileBtoF =  "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/oct202017/mu_ISO_EfficienciesAndSF_BCDEF.root";
  std::string ISOinputFileGtoH =  "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/oct202017/mu_ISO_EfficienciesAndSF_GH.root";
  
  std::string HIPinputFileBtoF =  "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/oct202017/HIP_BCDEF.root";
  std::string HIPinputFileGtoH =  "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/oct202017/HIP_GH.root";


  TFile *f_IDSFBtoF = new TFile(std::string(IDinputFileBtoF).c_str(),"READ");
  TFile *f_IDSFGtoH = new TFile(std::string(IDinputFileGtoH).c_str(),"READ");
  
  TFile *f_HIPSFBtoF = new TFile(std::string(HIPinputFileBtoF).c_str(),"READ");
  TFile *f_HIPSFGtoH = new TFile(std::string(HIPinputFileGtoH).c_str(),"READ");

  
  TFile *f_TRIGGERSFBtoF = new TFile(std::string(TRIGGERinputFileBtoF).c_str(),"READ");
  TFile *f_TRIGGERSFGtoH = new TFile(std::string(TRIGGERinputFileGtoH).c_str(),"READ");

  TFile *f_ISOSFBtoF = new TFile(std::string(ISOinputFileBtoF).c_str(),"READ");
  TFile *f_ISOSFGtoH = new TFile(std::string(ISOinputFileGtoH).c_str(),"READ");

  h_mu_ID_abseta_pt_ratioBtoF = (TH2F*)f_IDSFBtoF->Get("MC_NUM_TightID_DEN_genTracks_PAR_pt_eta/pt_abseta_ratio");
  h_mu_ID_abseta_pt_ratioGtoH = (TH2F*)f_IDSFGtoH->Get("MC_NUM_TightID_DEN_genTracks_PAR_pt_eta/pt_abseta_ratio");

  h_mu_HIP_eta_ratioBtoF = (TGraphAsymmErrors*)f_HIPSFBtoF->Get("ratio_eff_aeta_dr030e030_corr");
  h_mu_HIP_eta_ratioGtoH = (TGraphAsymmErrors*)f_HIPSFGtoH->Get("ratio_eff_aeta_dr030e030_corr");

  h_mu_TRIGGER_abseta_ptBtoF= (TH2F*)f_TRIGGERSFBtoF->Get("IsoMu24_OR_IsoTkMu24_PtEtaBins/pt_abseta_ratio");
  h_mu_TRIGGER_abseta_ptGtoH= (TH2F*)f_TRIGGERSFGtoH->Get("IsoMu24_OR_IsoTkMu24_PtEtaBins/pt_abseta_ratio");

  h_mu_ISO_abseta_pt_ratioBtoF = (TH2F*)f_ISOSFBtoF->Get("TightISO_TightID_pt_eta/pt_abseta_ratio");
  h_mu_ISO_abseta_pt_ratioGtoH = (TH2F*)f_ISOSFGtoH->Get("TightISO_TightID_pt_eta/pt_abseta_ratio");

}

void LeptonSFHelper::SetElectronElectronHistos( ){
  std::string TRIGGERinputFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/oct202017/triggerSummary_ee_ReReco2016_ttH.root";

  TFile *f_TRIGGERSF = new TFile(std::string(TRIGGERinputFile).c_str(),"READ");

  h_ele_ele_TRIGGER_abseta_abseta = (TH2F*)f_TRIGGERSF->Get("scalefactor_eta2d_with_syst");
}

void LeptonSFHelper::SetMuonMuonHistos( ){
  std::string TRIGGERinputFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/oct202017/triggerSummary_mumu_ReReco2016_ttH.root";

  TFile *f_TRIGGERSF = new TFile(std::string(TRIGGERinputFile).c_str(),"READ");

  h_mu_mu_TRIGGER_abseta_abseta = (TH2F*)f_TRIGGERSF->Get("scalefactor_eta2d_with_syst");
}

void LeptonSFHelper::SetElectronMuonHistos( ){
  std::string TRIGGERinputFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/oct202017/triggerSummary_emu_ReReco2016_ttH.root";

  TFile *f_TRIGGERSF = new TFile(std::string(TRIGGERinputFile).c_str(),"READ");

  h_ele_mu_TRIGGER_abseta_abseta = (TH2F*)f_TRIGGERSF->Get("scalefactor_eta2d_with_syst");
}

int LeptonSFHelper::findPoint(TGraphAsymmErrors& graph,float& x_) {
    double x=0.;
    double y=0.;
    for(int i=0;i<graph.GetN();i++) {
        graph.GetPoint(i,x,y);
        double l=0.;
        double r=0.;
        l = x-graph.GetErrorXlow(i);
        r = x+graph.GetErrorXhigh(i);
        if((l<=x_) && (x_<r)) {return i;}
    }
    return -1;
}

float LeptonSFHelper::getValue(TGraphAsymmErrors& graph,float& x_,int syst) {
    int i = findPoint(graph,x_);
    if(i<0) {std::cerr << "x-value " << x_ << " cannot be assigned to a valid point" << std::endl;}
    double x=0.;
    double y=0.;
    graph.GetPoint(i,x,y);
    float y_=y;
    if(syst==1) {return y_+graph.GetErrorYhigh(i);}
    else if(syst==-1) {return y_-graph.GetErrorYlow(i);}
    else {return y_;}
}

// Systematics enum from MiniAODHelper. Needed for the CSV helper (date 26.06.2017)

class Systematics {
public:
  enum Type {
    NA,

    // total JEC uncertainties
    JESup,			
    JESdown,			

    // individual JEC uncertainties up
    JESAbsoluteStatup,
    JESAbsoluteScaleup,
    JESAbsoluteFlavMapup,
    JESAbsoluteMPFBiasup,
    JESFragmentationup,
    JESSinglePionECALup,
    JESSinglePionHCALup,
    JESFlavorQCDup,
    JESTimePtEtaup,
    JESRelativeJEREC1up,
    JESRelativeJEREC2up,
    JESRelativeJERHFup,
    JESRelativePtBBup,
    JESRelativePtEC1up,
    JESRelativePtEC2up,
    JESRelativePtHFup,
    JESRelativeBalup,
    JESRelativeFSRup,
    JESRelativeStatFSRup,
    JESRelativeStatECup,
    JESRelativeStatHFup,
    JESPileUpDataMCup,
    JESPileUpPtRefup,
    JESPileUpPtBBup,
    JESPileUpPtEC1up,
    JESPileUpPtEC2up,
    JESPileUpPtHFup,
    JESPileUpMuZeroup,
    JESPileUpEnvelopeup,
    JESSubTotalPileUpup,
    JESSubTotalRelativeup,
    JESSubTotalPtup,
    JESSubTotalScaleup,
    JESSubTotalAbsoluteup,
    JESSubTotalMCup,
    JESTotalup,
    JESTotalNoFlavorup,
    JESTotalNoTimeup,
    JESTotalNoFlavorNoTimeup,
    JESFlavorZJetup,
    JESFlavorPhotonJetup,
    JESFlavorPureGluonup,
    JESFlavorPureQuarkup,
    JESFlavorPureCharmup,
    JESFlavorPureBottomup,
    JESTimeRunBCDup,
    JESTimeRunEFup,
    JESTimeRunGup,
    JESTimeRunHup,
    JESCorrelationGroupMPFInSituup,
    JESCorrelationGroupIntercalibrationup,
    JESCorrelationGroupbJESup,
    JESCorrelationGroupFlavorup,
    JESCorrelationGroupUncorrelatedup,
    
    // individual JEC uncertainties down
    JESAbsoluteStatdown,
    JESAbsoluteScaledown,
    JESAbsoluteFlavMapdown,
    JESAbsoluteMPFBiasdown,
    JESFragmentationdown,
    JESSinglePionECALdown,
    JESSinglePionHCALdown,
    JESFlavorQCDdown,
    JESTimePtEtadown,
    JESRelativeJEREC1down,
    JESRelativeJEREC2down,
    JESRelativeJERHFdown,
    JESRelativePtBBdown,
    JESRelativePtEC1down,
    JESRelativePtEC2down,
    JESRelativePtHFdown,
    JESRelativeBaldown,
    JESRelativeFSRdown,
    JESRelativeStatFSRdown,
    JESRelativeStatECdown,
    JESRelativeStatHFdown,
    JESPileUpDataMCdown,
    JESPileUpPtRefdown,
    JESPileUpPtBBdown,
    JESPileUpPtEC1down,
    JESPileUpPtEC2down,
    JESPileUpPtHFdown,
    JESPileUpMuZerodown,
    JESPileUpEnvelopedown,
    JESSubTotalPileUpdown,
    JESSubTotalRelativedown,
    JESSubTotalPtdown,
    JESSubTotalScaledown,
    JESSubTotalAbsolutedown,
    JESSubTotalMCdown,
    JESTotaldown,
    JESTotalNoFlavordown,
    JESTotalNoTimedown,
    JESTotalNoFlavorNoTimedown,
    JESFlavorZJetdown,
    JESFlavorPhotonJetdown,
    JESFlavorPureGluondown,
    JESFlavorPureQuarkdown,
    JESFlavorPureCharmdown,
    JESFlavorPureBottomdown,
    JESTimeRunBCDdown,
    JESTimeRunEFdown,
    JESTimeRunGdown,
    JESTimeRunHdown,
    JESCorrelationGroupMPFInSitudown,
    JESCorrelationGroupIntercalibrationdown,
    JESCorrelationGroupbJESdown,
    JESCorrelationGroupFlavordown,
    JESCorrelationGroupUncorrelateddown,
    
    // JER uncertainty
    JERup,			
    JERdown,

    hfSFup,
    hfSFdown,
    lfSFdown,
    lfSFup,

    TESup,
    TESdown,

    CSVLFup,
    CSVLFdown,
    CSVHFup,
    CSVHFdown,
    CSVHFStats1up,
    CSVHFStats1down,
    CSVLFStats1up,
    CSVLFStats1down,
    CSVHFStats2up,
    CSVHFStats2down,
    CSVLFStats2up,
    CSVLFStats2down,
    CSVCErr1up,
    CSVCErr1down,
    CSVCErr2up,
    CSVCErr2down 
  };

  // convert between string and int representation
  static Type get(const std::string& name);
  static std::string toString(const Type type);

  // true if type is one of the JEC-related uncertainties and up
  static bool isJECUncertaintyUp(const Type type);

  // true if type is one of the JEC-related uncertainties and down
  static bool isJECUncertaintyDown(const Type type);

  // true if type is one of the JEC-related uncertainties
  static bool isJECUncertainty(const Type type);

  // return the label that is used by JetCorrectorParametersCollection
  // to label the uncertainty type. See also:
  // https://cmssdt.cern.ch/SDT/doxygen/CMSSW_8_0_23/doc/html/dc/d33/classJetCorrectorParametersCollection.html#afb3d4c6fd711ca23d89e0625a22dc483 for a list of in principle valid labels. Whether the uncertainty
  static std::string GetJECUncertaintyLabel(const Type type);

  static std::vector<Systematics::Type> getTypeVector();


private:
  static std::map<Type,std::string> typeStringMap_;
  static std::map<std::string,Type> stringTypeMap_;
  static std::map<Type,std::string> typeLabelMap_;

  static void init();
  static bool isInit();
  static void add(Systematics::Type typeUp, Systematics::Type typeDn, const std::string& name, const std::string& label);
};

std::map<Systematics::Type,std::string> Systematics::typeStringMap_ = std::map<Systematics::Type,std::string>();
std::map<std::string,Systematics::Type> Systematics::stringTypeMap_ = std::map<std::string,Systematics::Type>();
std::map<Systematics::Type,std::string> Systematics::typeLabelMap_  = std::map<Systematics::Type,std::string>();


void Systematics::init() {
  add( JESup,JESdown,"JES","Uncertainty");
  add( JERup,JERdown,"JER","JER");
  add( JESAbsoluteStatup,        JESAbsoluteStatdown,        "JESAbsoluteStat",          "AbsoluteStat"        );             
  add( JESAbsoluteScaleup,       JESAbsoluteScaledown,       "JESAbsoluteScale",         "AbsoluteScale"       );             
  add( JESAbsoluteFlavMapup,     JESAbsoluteFlavMapdown,     "JESAbsoluteFlavMap",       "AbsoluteFlavMap"     );                             
  add( JESAbsoluteMPFBiasup,     JESAbsoluteMPFBiasdown,     "JESAbsoluteMPFBias",       "AbsoluteMPFBias"     );                             
  add( JESFragmentationup,       JESFragmentationdown,       "JESFragmentation",         "Fragmentation"       );             
  add( JESSinglePionECALup,      JESSinglePionECALdown,      "JESSinglePionECAL",        "SinglePionECAL"      );                             
  add( JESSinglePionHCALup,      JESSinglePionHCALdown,      "JESSinglePionHCAL",        "SinglePionHCAL"      );                             
  add( JESFlavorQCDup,           JESFlavorQCDdown,           "JESFlavorQCD",             "FlavorQCD"           );                        
  add( JESTimePtEtaup,           JESTimePtEtadown,           "JESTimePtEta",             "TimePtEta"           );                        
  add( JESRelativeJEREC1up,      JESRelativeJEREC1down,      "JESRelativeJEREC1",        "RelativeJEREC1"      );                             
  add( JESRelativeJEREC2up,      JESRelativeJEREC2down,      "JESRelativeJEREC2",        "RelativeJEREC2"      );                             
  add( JESRelativeJERHFup,       JESRelativeJERHFdown,       "JESRelativeJERHF",         "RelativeJERHF"       );             
  add( JESRelativePtBBup,        JESRelativePtBBdown,        "JESRelativePtBB",          "RelativePtBB"        );             
  add( JESRelativePtEC1up,       JESRelativePtEC1down,       "JESRelativePtEC1",         "RelativePtEC1"       );             
  add( JESRelativePtEC2up,       JESRelativePtEC2down,       "JESRelativePtEC2",         "RelativePtEC2"       );             
  add( JESRelativePtHFup,        JESRelativePtHFdown,        "JESRelativePtHF",          "RelativePtHF"        );             
  add( JESRelativeBalup,         JESRelativeBaldown,         "JESRelativeBal",           "RelativeBal"         );                        
  add( JESRelativeFSRup,         JESRelativeFSRdown,         "JESRelativeFSR",           "RelativeFSR"         );                        
  add( JESRelativeStatFSRup,     JESRelativeStatFSRdown,     "JESRelativeStatFSR",       "RelativeStatFSR"     );                             
  add( JESRelativeStatECup,      JESRelativeStatECdown,      "JESRelativeStatEC",        "RelativeStatEC"      );                             
  add( JESRelativeStatHFup,      JESRelativeStatHFdown,      "JESRelativeStatHF",        "RelativeStatHF"      );                             
  add( JESPileUpDataMCup,        JESPileUpDataMCdown,        "JESPileUpDataMC",          "PileUpDataMC"        );             
  add( JESPileUpPtRefup,         JESPileUpPtRefdown,         "JESPileUpPtRef",           "PileUpPtRef"         );                        
  add( JESPileUpPtBBup,          JESPileUpPtBBdown,          "JESPileUpPtBB",            "PileUpPtBB"          );                        
  add( JESPileUpPtEC1up,         JESPileUpPtEC1down,         "JESPileUpPtEC1",           "PileUpPtEC1"         );                        
  add( JESPileUpPtEC2up,         JESPileUpPtEC2down,         "JESPileUpPtEC2",           "PileUpPtEC2"         );                        
  add( JESPileUpPtHFup,          JESPileUpPtHFdown,          "JESPileUpPtHF",            "PileUpPtHF"          );                        
  add( JESPileUpMuZeroup,        JESPileUpMuZerodown,        "JESPileUpMuZero",          "PileUpMuZero"        );             
  add( JESPileUpEnvelopeup,      JESPileUpEnvelopedown,      "JESPileUpEnvelope",        "PileUpEnvelope"      );                             
  add( JESSubTotalPileUpup,      JESSubTotalPileUpdown,      "JESSubTotalPileUp",        "SubTotalPileUp"      );                             
  add( JESSubTotalRelativeup,    JESSubTotalRelativedown,    "JESSubTotalRelative",      "SubTotalRelative"    );                             
  add( JESSubTotalPtup,          JESSubTotalPtdown,          "JESSubTotalPt",            "SubTotalPt"          );                        
  add( JESSubTotalScaleup,       JESSubTotalScaledown,       "JESSubTotalScale",         "SubTotalScale"       );             
  add( JESSubTotalAbsoluteup,    JESSubTotalAbsolutedown,    "JESSubTotalAbsolute",      "SubTotalAbsolute"    );                             
  add( JESSubTotalMCup,          JESSubTotalMCdown,          "JESSubTotalMC",            "SubTotalMC"          );                        
  add( JESTotalup,               JESTotaldown,               "JESTotal",                 "Total"               );                 
  add( JESTotalNoFlavorup,       JESTotalNoFlavordown,       "JESTotalNoFlavor",         "TotalNoFlavor"       );             
  add( JESTotalNoTimeup,         JESTotalNoTimedown,         "JESTotalNoTime",           "TotalNoTime"         );                        
  add( JESTotalNoFlavorNoTimeup, JESTotalNoFlavorNoTimedown, "JESTotalNoFlavorNoTime",   "TotalNoFlavorNoTime" );                    
  add( JESFlavorZJetup,          JESFlavorZJetdown,          "JESFlavorZJet",            "FlavorZJet"          );                        
  add( JESFlavorPhotonJetup,     JESFlavorPhotonJetdown,     "JESFlavorPhotonJet",       "FlavorPhotonJet"     );                             
  add( JESFlavorPureGluonup,     JESFlavorPureGluondown,     "JESFlavorPureGluon",       "FlavorPureGluon"     );                             
  add( JESFlavorPureQuarkup,     JESFlavorPureQuarkdown,     "JESFlavorPureQuark",       "FlavorPureQuark"     );                             
  add( JESFlavorPureCharmup,     JESFlavorPureCharmdown,     "JESFlavorPureCharm",       "FlavorPureCharm"     );                             
  add( JESFlavorPureBottomup,    JESFlavorPureBottomdown,    "JESFlavorPureBottom",      "FlavorPureBottom"    );                             
  add( JESTimeRunBCDup,          JESTimeRunBCDdown,          "JESTimeRunBCD",            "TimeRunBCD"          );                  
  add( JESTimeRunEFup,           JESTimeRunEFdown,           "JESTimeRunEF",             "TimeRunEF"           );                        
  add( JESTimeRunGup,            JESTimeRunGdown,            "JESTimeRunG",              "TimeRunG"            );                                 
  add( JESTimeRunHup,            JESTimeRunHdown,            "JESTimeRunH",              "TimeRunH"            );   
  add( CSVLFup,                  CSVLFdown,                  "CSVLF",                    "LF"                  );
  add( CSVHFup,                  CSVHFdown,                  "CSVHF",                    "HF"                  );
  add( CSVLFStats1up,            CSVLFStats1down,            "CSVLFStats1",              "LFStats1"            );
  add( CSVHFStats1up,            CSVHFStats1down,            "CSVHFStats1",              "HFStats1"            );
  add( CSVLFStats2up,            CSVLFStats2down,            "CSVLFStats2",              "LFStats2"            );
  add( CSVHFStats2up,            CSVHFStats2down,            "CSVHFStats2",              "HFStats2"            );
  add( CSVCErr1up,               CSVCErr1down,               "CSVcErr1",                 "CErr1"               );
  add( CSVCErr2up,               CSVCErr2down,               "CSVcErr2",                 "CErr2"               );
}

bool Systematics::isInit() {
  return typeStringMap_.size()>1;
}

void Systematics::add(Systematics::Type typeUp, Systematics::Type typeDn, const std::string& name, const std::string& label) {
  typeStringMap_[typeUp] = name+"up";
  typeStringMap_[typeDn] = name+"down";
  stringTypeMap_[name+"up"] = typeUp;
  stringTypeMap_[name+"down"] = typeDn;
  typeLabelMap_[typeUp] = label;
  typeLabelMap_[typeDn] = label;
}

// added method to get a vector of all systematics
std::vector<Systematics::Type> Systematics::getTypeVector() {
  if( !isInit() ) init();
  std::vector<Systematics::Type> outvector;
  outvector.push_back(NA);
  for(auto it : typeStringMap_ ){
    std::cout<<it.first<<" "<<it.second<<std::endl;
    outvector.push_back(it.first);
    }
  return outvector;
}

Systematics::Type Systematics::get(const std::string& name) {
  if( name == "" ) return NA;

  if( !isInit() ) init();

  std::map<std::string,Systematics::Type>::const_iterator it = stringTypeMap_.find(name);
  if( it == stringTypeMap_.end() ) {
    std::cout << "ERROR: No uncertainty with name " << name << " will use nominal "<<std::endl;
    return Systematics::NA;
  } else {
    return it->second;
  }
}

std::string Systematics::toString(const Type type) {
  if( type == NA ) return "";

  if( !isInit() ) init();

  std::map<Systematics::Type,std::string>::const_iterator it = typeStringMap_.find(type);
  if( it == typeStringMap_.end() ) {
    std::cout << "ERROR: No uncertainty with name " << type << " will use nominal "<<std::endl;
    return "";
  } else {
    return it->second;
  }
}

bool Systematics::isJECUncertaintyUp(const Type type) {
  const std::string str = toString(type);
  return str.find("JES")==0 && str.find("up")==str.size()-2;
}

bool Systematics::isJECUncertaintyDown(const Type type) {
  const std::string str = toString(type);
  return str.find("JES")==0 && str.find("down") == str.size()-4;
}

bool Systematics::isJECUncertainty(const Type type) {
  return isJECUncertaintyUp(type) || isJECUncertaintyDown(type);
}

std::string Systematics::GetJECUncertaintyLabel(const Type type) {
  if( !isInit() ) init();
  std::map<Systematics::Type,std::string>::const_iterator it = typeLabelMap_.find(type);
  if( it == typeLabelMap_.end() ) {
    return "";
  } else {
    return it->second;
  }
}

// hacked in CSV helper . Factorized JES. (date 26.06.2017)
class CSVHelper
{
public:
  // nHFptBins specifies how many of these pt bins are used:
  // (jetPt >= 19.99 && jetPt < 30), (jetPt >= 30 && jetPt < 40), (jetPt >= 40 && jetPt < 60), 
  // (jetPt >= 60 && jetPt < 100), (jetPt >= 100 && jetPt < 160), (jetPt >= 160 && jetPt < 10000).
  // If nHFptBins < 6, the last on is inclusive (eg jetPt >=100 && jetPt < 10000 for nHFptBins=5).
  // The SFs from data have 5 bins, the pseudo data scale factors 6 bins.
    
  // standard constructor
  CSVHelper();
  // another constructor
  CSVHelper(const std::string& hf, const std::string& lf, const int& nHFptBins=5,const int& nLFptBins=4,const int& nLFetaBins=3,const std::vector<Systematics::Type>& jecsysts = std::vector<Systematics::Type>(1,Systematics::NA));
  // destructor
  ~CSVHelper();
  // function to set up the needed stuff
  void init(const std::string& hf, const std::string& lf, const int& nHFptBins,const int& nLFptBins,const int& nLFetaBins,const std::vector<Systematics::Type>& jecsysts);
  // function to get the csv weight
  double getCSVWeight(const std::vector<double>& jetPts,
		      const std::vector<double>& jetEtas,
		      const std::vector<double>& jetCSVs,
		      const std::vector<int>& jetFlavors,
		      const Systematics::Type syst,
		      double &csvWgtHF,
		      double &csvWgtLF,
		      double &csvWgtCF) const;

  // If there is no SF for a jet because it is out of acceptance
  // of SF, an SF of 1 is used for this jet. Intended when running
  // on MC with a more inclusive selection.
  // USE WITH CARE!
  void allowJetsOutOfBinning(const bool allow) { allowJetsOutOfBinning_ = allow; }


private:
  bool isInit_;
  int nHFptBins_;//number of pt bins in hf(including c flavour) histograms
  int nLFptBins_;//number of pt bins in lf histograms
  int nLFetaBins_;//number of eta bins in lf histograms
  bool allowJetsOutOfBinning_;

  std::vector< std::vector<TH1*> > h_csv_wgt_hf;//vector to store pointers to the needed hf histograms
  std::vector< std::vector<TH1*> > c_csv_wgt_hf;//vector to store pointers to the needed c flavour histograms
  std::vector< std::vector< std::vector<TH1*> > > h_csv_wgt_lf;//vector to store pointers to the needed lf histograms
  // vector for the csv systematics
  std::vector<Systematics::Type> csvsysts = {   
                                                Systematics::CSVLFup,
                                                Systematics::CSVLFdown,
                                                Systematics::CSVHFup,
                                                Systematics::CSVHFdown,
                                                Systematics::CSVHFStats1up,
                                                Systematics::CSVHFStats1down,
                                                Systematics::CSVLFStats1up,
                                                Systematics::CSVLFStats1down,
                                                Systematics::CSVHFStats2up,
                                                Systematics::CSVHFStats2down,
                                                Systematics::CSVLFStats2up,
                                                Systematics::CSVLFStats2down,
                                                Systematics::CSVCErr1up,
                                                Systematics::CSVCErr1down,
                                                Systematics::CSVCErr2up,
                                                Systematics::CSVCErr2down
                                            };
  // vector for all desired systematics -> csv+jec systematics  
  std::vector<Systematics::Type> systs;
  // function to get the histograms from the provided root files
  void fillCSVHistos(TFile *fileHF, TFile *fileLF, const std::vector<Systematics::Type>& systs);
  // function which reads the desired histogram from the provided root file
  TH1* readHistogram(TFile* file, const TString& name) const;
};

CSVHelper::CSVHelper()
  : isInit_(false), nHFptBins_(0),nLFptBins_(0),nLFetaBins_(0), allowJetsOutOfBinning_(false) {}


CSVHelper::CSVHelper(const std::string& hf, const std::string& lf, const int& nHFptBins,const int& nLFptBins,const int& nLFetaBins, const std::vector<Systematics::Type>& jecsysts)
  : isInit_(false), nHFptBins_(0),nLFptBins_(0),nLFetaBins_(0), allowJetsOutOfBinning_(false) {
  init(hf,lf,nHFptBins,nLFptBins,nLFetaBins,jecsysts);
}


CSVHelper::~CSVHelper() {
  for(auto& i: h_csv_wgt_hf ) {
    for(auto& j: i) {
      if( j ) delete j;
    }
  }
  for(auto& i: c_csv_wgt_hf ) {
    for(auto& j: i) {
      if( j ) delete j;
    }
  }
  for(auto& i: h_csv_wgt_lf ) {
    for(auto& j: i) {
      for(auto& k: j) {
	if( k ) delete k;
      }
    }
  }
}


void CSVHelper::init(const std::string& hf, const std::string& lf, const int& nHFptBins,const int& nLFptBins,const int& nLFetaBins,const std::vector<Systematics::Type>& jecsysts) {
  std::cout << "Initializing b-tag scale factors" <<  std::endl;
  std::cout<< "  HF : " << hf << " (" << nHFptBins << " pt bins)" <<  std::endl;
  std::cout<< "  LF : " << lf << " (" << nLFptBins << " pt bins)"  <<  std::endl;
  std::cout<< "  LF : " << lf << " (" << nLFetaBins << " eta bins)" <<  std::endl;

  nHFptBins_ = nHFptBins;
  nLFptBins_ = nLFptBins;
  nLFetaBins_ = nLFetaBins;
  
  //combine the vector with the csv systematics and the jec systematics into one vector
  systs.reserve(csvsysts.size()+jecsysts.size());
  systs.insert(systs.end(),jecsysts.begin(),jecsysts.end());
  systs.insert(systs.end(),csvsysts.begin(),csvsysts.end());
  
  const std::string inputFileHF = hf.size() > 0 ? hf : "data/csv_rwt_hf_IT_FlatSF.root";
  const std::string inputFileLF = lf.size() > 0 ? lf : "data/csv_rwt_lf_IT_FlatSF.root";

  TFile *f_CSVwgt_HF = new TFile(std::string(inputFileHF).c_str());
  TFile *f_CSVwgt_LF = new TFile(std::string(inputFileLF).c_str());
  fillCSVHistos(f_CSVwgt_HF, f_CSVwgt_LF,systs);
  f_CSVwgt_HF->Close();
  f_CSVwgt_LF->Close();
  delete f_CSVwgt_HF;
  delete f_CSVwgt_LF;

  isInit_ = true;
}



// fill the histograms (done once)
void
CSVHelper::fillCSVHistos(TFile *fileHF, TFile *fileLF, const std::vector<Systematics::Type>& systs)
{
  const size_t nSys = systs.size();//purity,stats1,stats2 with up/down + jec systs including nominal variation
  h_csv_wgt_hf = std::vector< std::vector<TH1*> >(nSys,std::vector<TH1*>(nHFptBins_,NULL));
  c_csv_wgt_hf = std::vector< std::vector<TH1*> >(nSys,std::vector<TH1*>(nHFptBins_,NULL));
  h_csv_wgt_lf = std::vector< std::vector< std::vector<TH1*> > >(nSys,std::vector< std::vector<TH1*> >(nLFptBins_,std::vector<TH1*>(nLFetaBins_,NULL)));
  TString syst_csv_suffix = "final";
  // loop over all the available systematics
  for (size_t iSys = 0; iSys < nSys; iSys++) {
    // some string cosmetics to search for the correct histogram in the root files  
    TString systematic = Systematics::toString(systs[iSys]);
    TString systematic_original = systematic;
    
    systematic.ReplaceAll("up","Up");
    systematic.ReplaceAll("down","Down");
    systematic.ReplaceAll("CSV","");
    std::cout << "adding histograms for systematic " << systematic << std::endl;
    if(systematic.Contains("Stats")) {
        systematic.ReplaceAll("HF","");
        systematic.ReplaceAll("LF","");
    }
    if(systematic!="") {systematic="_"+systematic;}
    
    if(systematic_original.Contains("HFStats")){
        systematic_original.ReplaceAll("HFStats","LFStats");
    }
    else if(systematic_original.Contains("LFStats")){
        systematic_original.ReplaceAll("LFStats","HFStats");
    }
    // loop over all pt bins of the different jet flavours
    for (int iPt = 0; iPt < nHFptBins_; iPt++) {
        TString name = Form("csv_ratio_Pt%i_Eta0_%s", iPt, (syst_csv_suffix+systematic).Data());
        // only read the histogram if it exits in the root file
        if(fileHF->GetListOfKeys()->Contains(name) && !(systematic_original.Contains("HF"))) {
            h_csv_wgt_hf.at(iSys).at(iPt) = readHistogram(fileHF,name);
            std::cout << "added " << name << " from HF file" << std::endl;
        }
        else {
            h_csv_wgt_hf.at(iSys).at(iPt) = readHistogram(fileHF,name.ReplaceAll(systematic,""));
        }
    }
    for (int iPt = 0; iPt < nHFptBins_; iPt++) {
        TString name = Form("c_csv_ratio_Pt%i_Eta0_%s", iPt, (syst_csv_suffix+systematic).Data());
        if(fileHF->GetListOfKeys()->Contains(name)) {
            c_csv_wgt_hf.at(iSys).at(iPt) = readHistogram(fileHF,name);
            std::cout << "added " << name << " from HF file" << std::endl;
        }
        else {
            c_csv_wgt_hf.at(iSys).at(iPt) = readHistogram(fileHF,name.ReplaceAll(systematic,""));
        }
    }
    for (int iPt = 0; iPt < nLFptBins_; iPt++) {
        for (int iEta = 0; iEta < nLFetaBins_; iEta++) {
            TString name = Form("csv_ratio_Pt%i_Eta%i_%s", iPt, iEta, (syst_csv_suffix+systematic).Data());
            if(fileLF->GetListOfKeys()->Contains(name) && !(systematic_original.Contains("LF"))) {
                h_csv_wgt_lf.at(iSys).at(iPt).at(iEta) = readHistogram(fileLF,name);
                std::cout << "added " << name << " from LF file" << std::endl;
            }
            else {
                h_csv_wgt_lf.at(iSys).at(iPt).at(iEta) = readHistogram(fileLF,name.ReplaceAll(systematic,""));
            }
        }
    }
  }
}


TH1* CSVHelper::readHistogram(TFile* file, const TString& name) const {
  TH1* h = NULL;
  file->GetObject(name,h);
  if( h==NULL ) {
      std::cout<< "Could not find CSV SF histogram '" << name  << " in file " << file->GetName() << std::endl;
  }
  h->SetDirectory(0);
  
  return h;
}


double
CSVHelper::getCSVWeight(const std::vector<double>& jetPts,
			const std::vector<double>& jetEtas,
			const std::vector<double>& jetCSVs,
			const std::vector<int>& jetFlavors,
			const Systematics::Type syst,
			double &csvWgtHF,
			double &csvWgtLF,
			double &csvWgtCF) const
{
  if( !isInit_ ) {
    std::cout<<"CSVHelper: Not initualized"<<std::endl;
  }
  // search for the position of the desired systematic in the systs vector
  const int iSys = std::find(systs.begin(),systs.end(),syst)-systs.begin();
  
  //std::cout << "Systematic index " << iSys << std::endl;
  // initialize the weight for the different jet flavours with 1
  double csvWgthf = 1.;
  double csvWgtC = 1.;
  double csvWgtlf = 1.;
  
  // loop over all jets in the event and calculate the final weight by multiplying the single jet scale factors
  for (size_t iJet = 0; iJet < jetPts.size(); iJet++) {
    const double csv = jetCSVs.at(iJet);
    const double jetPt = jetPts.at(iJet);
    const double jetAbsEta = fabs(jetEtas.at(iJet));
    const int flavor = jetFlavors.at(iJet);

    int iPt = -1;
    int iEta = -1;
    // pt binning for heavy flavour jets
    if(abs(flavor)>3) {
        if (jetPt >= 19.99 && jetPt < 30)
            iPt = 0;
        else if (jetPt >= 30 && jetPt < 50)
            iPt = 1;
        else if (jetPt >= 50 && jetPt < 70)
            iPt = 2;
        else if (jetPt >= 70 && jetPt < 100)
            iPt = 3;
        else if (jetPt >= 100 && jetPt < 160)
            iPt = 4;
        else if (jetPt >= 160)
            iPt = 5;
    }
    // pt binning for light flavour jets
    else {
        if (jetPt >= 19.99 && jetPt < 30)
            iPt = 0;
        else if (jetPt >= 30 && jetPt < 40)
            iPt = 1;
        else if (jetPt >= 40 && jetPt < 60)
            iPt = 2;
        else if (jetPt >= 60 && jetPt < 100)
            iPt = 3;
        else if (jetPt >= 100 && jetPt < 160)
            iPt = 4;
        else if (jetPt >= 160)
            iPt = 5;
    }
    // light flavour jets also have eta bins
    if (jetAbsEta >= 0 && jetAbsEta < 0.8)
      iEta = 0;
    else if (jetAbsEta >= 0.8 && jetAbsEta < 1.6)
      iEta = 1;
    else if (jetAbsEta >= 1.6 && jetAbsEta < 2.41)
      iEta = 2;
    
    if (iPt < 0 || iEta < 0) {
      if( true ) continue;
      std::cout << "couldn't find Pt, Eta bins for this b-flavor jet, jetPt = " << jetPt << ", jetAbsEta = " << jetAbsEta<<std::endl;
      exit(0);
    }
    
    //std::cout << "program is in front of calculating the csv weights " << std::endl;
    // b flavour jet
    if (abs(flavor) == 5) {
        //std::cout << "b flavor jet " << std::endl;
      // RESET iPt to maximum pt bin (only 5 bins for new SFs)
      if(iPt>=nHFptBins_){
	iPt=nHFptBins_-1;
      }
      if(h_csv_wgt_hf.at(iSys).at(iPt)) {
        const int useCSVBin = (csv >= 0.) ? h_csv_wgt_hf.at(iSys).at(iPt)->FindBin(csv) : 1;
        const double iCSVWgtHF = h_csv_wgt_hf.at(iSys).at(iPt)->GetBinContent(useCSVBin);
        if (iCSVWgtHF != 0) csvWgthf *= iCSVWgtHF;
      }
    } // c flavour jet
    else if (abs(flavor) == 4) {
        //std::cout << "c flavor jet " << std::endl;
      // RESET iPt to maximum pt bin (only 5 bins for new SFs)
      if(iPt>=nHFptBins_){
	iPt=nHFptBins_-1;
      }
      if(c_csv_wgt_hf.at(iSys).at(iPt)) {
        const int useCSVBin = (csv >= 0.) ? c_csv_wgt_hf.at(iSys).at(iPt)->FindBin(csv) : 1;
        const double iCSVWgtC = c_csv_wgt_hf.at(iSys).at(iPt)->GetBinContent(useCSVBin);
        if (iCSVWgtC != 0) csvWgtC *= iCSVWgtC;
      }
    } // light flavour jet
    else {
        //std::cout << "light flavor jet " << std::endl;
      if (iPt >= nLFptBins_) iPt = nLFptBins_-1; /// [30-40], [40-60] and [60-10000] only 3 Pt bins for lf
      if(h_csv_wgt_lf.at(iSys).at(iPt).at(iEta)) {
        const int useCSVBin = (csv >= 0.) ? h_csv_wgt_lf.at(iSys).at(iPt).at(iEta)->FindBin(csv) : 1;
        const double iCSVWgtLF = h_csv_wgt_lf.at(iSys).at(iPt).at(iEta)->GetBinContent(useCSVBin);
        if (iCSVWgtLF != 0) csvWgtlf *= iCSVWgtLF;
      }
    }
  }

  const double csvWgtTotal = csvWgthf * csvWgtC * csvWgtlf;

  csvWgtHF = csvWgthf;
  csvWgtLF = csvWgtlf;
  csvWgtCF = csvWgtC;

  return csvWgtTotal;
}

// BosonHelper for reweighting of W/W to NuNu Processes

class BosonHelper
{
  public:
    // see the definition/implementation file for a description of the functions 
    BosonHelper(TString path_to_sf_file_W, TString path_to_sf_file_Zvv, TString path_to_sf_file_Zll);
    ~BosonHelper();
    double GetScaleFactorW(float W_Pt, string label);
    double GetScaleFactorZvv(float Z_Pt, string label);
    double GetScaleFactorZll(float Z_Pt, string label);
    void Reset();
    void LoadWFile(TString path_to_sf_file_);
    void LoadZvvFile(TString path_to_sf_file_);
    void LoadZllFile(TString path_to_sf_file_);
      
  private:
    // pointer for the root file containing the desired histograms
    TFile* scalefactor_fileW = 0;
    TFile* scalefactor_fileZvv = 0;
    TFile* scalefactor_fileZll = 0;
    // path to the root file
    TString path_to_sf_file = "";
    // histograms containing the scale factors for electron and muon channel separately
    TH1D* WbosonWeight_nominal = 0;
    TH1D* WbosonWeight_QCD1Up = 0;
    TH1D* WbosonWeight_QCD1Down = 0;
    TH1D* WbosonWeight_QCD2Up = 0;
    TH1D* WbosonWeight_QCD2Down = 0;
    TH1D* WbosonWeight_QCD3Up = 0;
    TH1D* WbosonWeight_QCD3Down = 0;
    TH1D* WbosonWeight_EW1Up = 0;
    TH1D* WbosonWeight_EW1Down = 0;
    TH1D* WbosonWeight_EW2Up = 0;
    TH1D* WbosonWeight_EW2Down = 0;
    TH1D* WbosonWeight_EW3Up = 0;
    TH1D* WbosonWeight_EW3Down = 0;
    TH1D* WbosonWeight_MixedUp = 0;
    TH1D* WbosonWeight_MixedDown = 0;
    TH1D* WbosonWeight_AlphaUp = 0;
    TH1D* WbosonWeight_AlphaDown = 0;
    TH1D* WbosonWeight_muRUp = 0;
    TH1D* WbosonWeight_muRDown = 0;
    TH1D* WbosonWeight_muFUp = 0;
    TH1D* WbosonWeight_muFDown = 0;

    TH1D* ZvvbosonWeight_nominal = 0;
    TH1D* ZvvbosonWeight_QCD1Up = 0;
    TH1D* ZvvbosonWeight_QCD1Down = 0;
    TH1D* ZvvbosonWeight_QCD2Up = 0;
    TH1D* ZvvbosonWeight_QCD2Down = 0;
    TH1D* ZvvbosonWeight_QCD3Up = 0;
    TH1D* ZvvbosonWeight_QCD3Down = 0;
    TH1D* ZvvbosonWeight_EW1Up = 0;
    TH1D* ZvvbosonWeight_EW1Down = 0;
    TH1D* ZvvbosonWeight_EW2Up = 0;
    TH1D* ZvvbosonWeight_EW2Down = 0;
    TH1D* ZvvbosonWeight_EW3Up = 0;
    TH1D* ZvvbosonWeight_EW3Down = 0;
    TH1D* ZvvbosonWeight_MixedUp = 0;
    TH1D* ZvvbosonWeight_MixedDown = 0;
    TH1D* ZvvbosonWeight_AlphaUp = 0;
    TH1D* ZvvbosonWeight_AlphaDown = 0;
    TH1D* ZvvbosonWeight_muRUp = 0;
    TH1D* ZvvbosonWeight_muRDown = 0;
    TH1D* ZvvbosonWeight_muFUp = 0;
    TH1D* ZvvbosonWeight_muFDown = 0;
    
    TH1D* ZllbosonWeight_nominal = 0;
    TH1D* ZllbosonWeight_QCD1Up = 0;
    TH1D* ZllbosonWeight_QCD1Down = 0;
    TH1D* ZllbosonWeight_QCD2Up = 0;
    TH1D* ZllbosonWeight_QCD2Down = 0;
    TH1D* ZllbosonWeight_QCD3Up = 0;
    TH1D* ZllbosonWeight_QCD3Down = 0;
    TH1D* ZllbosonWeight_EW1Up = 0;
    TH1D* ZllbosonWeight_EW1Down = 0;
    TH1D* ZllbosonWeight_EW2Up = 0;
    TH1D* ZllbosonWeight_EW2Down = 0;
    TH1D* ZllbosonWeight_EW3Up = 0;
    TH1D* ZllbosonWeight_EW3Down = 0;
    TH1D* ZllbosonWeight_MixedUp = 0;
    TH1D* ZllbosonWeight_MixedDown = 0;
    TH1D* ZllbosonWeight_AlphaUp = 0;
    TH1D* ZllbosonWeight_AlphaDown = 0;
    TH1D* ZllbosonWeight_muRUp = 0;
    TH1D* ZllbosonWeight_muRDown = 0;
    TH1D* ZllbosonWeight_muFUp = 0;
    TH1D* ZllbosonWeight_muFDown = 0;
    
    // flag if the file and the histograms were read properly
    bool Winitialized = false;
    bool Zvvinitialized = false;
    bool Zllinitialized = false;
};

BosonHelper::BosonHelper(TString path_to_sf_file_W, TString path_to_sf_file_Zvv, TString path_to_sf_file_Zll)
{
  // just the constructor which loads a root file containing the histograms with the scale factors using the LoadFile function
  LoadWFile(path_to_sf_file_W);
  LoadZvvFile(path_to_sf_file_Zvv);
  LoadZllFile(path_to_sf_file_Zll);
}

void BosonHelper::LoadWFile(TString path_to_sf_file_)
{
  // this function loads the file given by a string and initializes the 2 needed histograms if the file was loaded correctly
  path_to_sf_file = path_to_sf_file_;
  if(path_to_sf_file!="")
  {
    scalefactor_fileW = TFile::Open(path_to_sf_file);
  }
  if(scalefactor_fileW)
  {
    WbosonWeight_nominal =   (TH1D*)scalefactor_fileW->Get("evj_NNLO_NLO_nnn_nnn_n");
    WbosonWeight_QCD1Up =    (TH1D*)scalefactor_fileW->Get("evj_NNLO_NLO_unn_nnn_n");
    WbosonWeight_QCD1Down =  (TH1D*)scalefactor_fileW->Get("evj_NNLO_NLO_dnn_nnn_n");
    WbosonWeight_QCD2Up =    (TH1D*)scalefactor_fileW->Get("evj_NNLO_NLO_nun_nnn_n");
    WbosonWeight_QCD2Down =  (TH1D*)scalefactor_fileW->Get("evj_NNLO_NLO_ndn_nnn_n");
    WbosonWeight_QCD3Up =    (TH1D*)scalefactor_fileW->Get("evj_NNLO_NLO_nnu_nnn_n");
    WbosonWeight_QCD3Down =  (TH1D*)scalefactor_fileW->Get("evj_NNLO_NLO_nnd_nnn_n");
    WbosonWeight_EW1Up =     (TH1D*)scalefactor_fileW->Get("evj_NNLO_NLO_nnn_unn_n");
    WbosonWeight_EW1Down =   (TH1D*)scalefactor_fileW->Get("evj_NNLO_NLO_nnn_dnn_n");
    WbosonWeight_EW2Up =     (TH1D*)scalefactor_fileW->Get("evj_NNLO_NLO_nnn_nun_n");
    WbosonWeight_EW2Down =   (TH1D*)scalefactor_fileW->Get("evj_NNLO_NLO_nnn_ndn_n");
    WbosonWeight_EW3Up =     (TH1D*)scalefactor_fileW->Get("evj_NNLO_NLO_nnn_nnu_n");
    WbosonWeight_EW3Down =   (TH1D*)scalefactor_fileW->Get("evj_NNLO_NLO_nnn_nnd_n");
    WbosonWeight_MixedUp =   (TH1D*)scalefactor_fileW->Get("evj_NNLO_NLO_nnn_nnn_u");
    WbosonWeight_MixedDown = (TH1D*)scalefactor_fileW->Get("evj_NNLO_NLO_nnn_nnn_d");
    WbosonWeight_AlphaUp =   (TH1D*)scalefactor_fileW->Get("evj_NNLO_NLO_nnn_nnn_n_alpha_up");
    WbosonWeight_AlphaDown = (TH1D*)scalefactor_fileW->Get("evj_NNLO_NLO_nnn_nnn_n_alpha_down");
    WbosonWeight_muRUp =     (TH1D*)scalefactor_fileW->Get("evj_NNLO_NLO_nnn_nnn_n_Weight_scale_variation_muR_2p0_muF_1p0");
    WbosonWeight_muRDown =   (TH1D*)scalefactor_fileW->Get("evj_NNLO_NLO_nnn_nnn_n_Weight_scale_variation_muR_0p5_muF_1p0");
    WbosonWeight_muFUp =     (TH1D*)scalefactor_fileW->Get("evj_NNLO_NLO_nnn_nnn_n_Weight_scale_variation_muR_1p0_muF_2p0");
    WbosonWeight_muFDown =   (TH1D*)scalefactor_fileW->Get("evj_NNLO_NLO_nnn_nnn_n_Weight_scale_variation_muR_1p0_muF_0p5");
    Winitialized = true;
  }
}

void BosonHelper::LoadZvvFile(TString path_to_sf_file_)
{
  // this function loads the file given by a string and initializes the 2 needed histograms if the file was loaded correctly
  path_to_sf_file = path_to_sf_file_;
  if(path_to_sf_file!="")
  {
    scalefactor_fileZvv = TFile::Open(path_to_sf_file);
  }
  if(scalefactor_fileZvv)
  {
    ZvvbosonWeight_nominal =   (TH1D*)scalefactor_fileZvv->Get("vvj_NNLO_NLO_nnn_nnn_n");
    ZvvbosonWeight_QCD1Up =    (TH1D*)scalefactor_fileZvv->Get("vvj_NNLO_NLO_unn_nnn_n");
    ZvvbosonWeight_QCD1Down =  (TH1D*)scalefactor_fileZvv->Get("vvj_NNLO_NLO_dnn_nnn_n");
    ZvvbosonWeight_QCD2Up =    (TH1D*)scalefactor_fileZvv->Get("vvj_NNLO_NLO_nun_nnn_n");
    ZvvbosonWeight_QCD2Down =  (TH1D*)scalefactor_fileZvv->Get("vvj_NNLO_NLO_ndn_nnn_n");
    ZvvbosonWeight_QCD3Up =    (TH1D*)scalefactor_fileZvv->Get("vvj_NNLO_NLO_nnu_nnn_n");
    ZvvbosonWeight_QCD3Down =  (TH1D*)scalefactor_fileZvv->Get("vvj_NNLO_NLO_nnd_nnn_n");
    ZvvbosonWeight_EW1Up =     (TH1D*)scalefactor_fileZvv->Get("vvj_NNLO_NLO_nnn_unn_n");
    ZvvbosonWeight_EW1Down =   (TH1D*)scalefactor_fileZvv->Get("vvj_NNLO_NLO_nnn_dnn_n");
    ZvvbosonWeight_EW2Up =     (TH1D*)scalefactor_fileZvv->Get("vvj_NNLO_NLO_nnn_nun_n");
    ZvvbosonWeight_EW2Down =   (TH1D*)scalefactor_fileZvv->Get("vvj_NNLO_NLO_nnn_ndn_n");
    ZvvbosonWeight_EW3Up =     (TH1D*)scalefactor_fileZvv->Get("vvj_NNLO_NLO_nnn_nnu_n");
    ZvvbosonWeight_EW3Down =   (TH1D*)scalefactor_fileZvv->Get("vvj_NNLO_NLO_nnn_nnd_n");
    ZvvbosonWeight_MixedUp =   (TH1D*)scalefactor_fileZvv->Get("vvj_NNLO_NLO_nnn_nnn_u");
    ZvvbosonWeight_MixedDown = (TH1D*)scalefactor_fileZvv->Get("vvj_NNLO_NLO_nnn_nnn_d");
    ZvvbosonWeight_AlphaUp =   (TH1D*)scalefactor_fileZvv->Get("vvj_NNLO_NLO_nnn_nnn_n_alpha_up");
    ZvvbosonWeight_AlphaDown = (TH1D*)scalefactor_fileZvv->Get("vvj_NNLO_NLO_nnn_nnn_n_alpha_down");
    ZvvbosonWeight_muRUp =     (TH1D*)scalefactor_fileZvv->Get("vvj_NNLO_NLO_nnn_nnn_n_Weight_scale_variation_muR_2p0_muF_1p0");
    ZvvbosonWeight_muRDown =   (TH1D*)scalefactor_fileZvv->Get("vvj_NNLO_NLO_nnn_nnn_n_Weight_scale_variation_muR_0p5_muF_1p0");
    ZvvbosonWeight_muFUp =     (TH1D*)scalefactor_fileZvv->Get("vvj_NNLO_NLO_nnn_nnn_n_Weight_scale_variation_muR_1p0_muF_2p0");
    ZvvbosonWeight_muFDown =   (TH1D*)scalefactor_fileZvv->Get("vvj_NNLO_NLO_nnn_nnn_n_Weight_scale_variation_muR_1p0_muF_0p5");
    Zvvinitialized = true;
  }
}

void BosonHelper::LoadZllFile(TString path_to_sf_file_)
{
  // this function loads the file given by a string and initializes the 2 needed histograms if the file was loaded correctly
  path_to_sf_file = path_to_sf_file_;
  if(path_to_sf_file!="")
  {
    scalefactor_fileZll = TFile::Open(path_to_sf_file);
  }
  if(scalefactor_fileZll)
  {
    ZllbosonWeight_nominal =   (TH1D*)scalefactor_fileZll->Get("eej_NNLO_NLO_nnn_nnn_n");
    ZllbosonWeight_QCD1Up =    (TH1D*)scalefactor_fileZll->Get("eej_NNLO_NLO_unn_nnn_n");
    ZllbosonWeight_QCD1Down =  (TH1D*)scalefactor_fileZll->Get("eej_NNLO_NLO_dnn_nnn_n");
    ZllbosonWeight_QCD2Up =    (TH1D*)scalefactor_fileZll->Get("eej_NNLO_NLO_nun_nnn_n");
    ZllbosonWeight_QCD2Down =  (TH1D*)scalefactor_fileZll->Get("eej_NNLO_NLO_ndn_nnn_n");
    ZllbosonWeight_QCD3Up =    (TH1D*)scalefactor_fileZll->Get("eej_NNLO_NLO_nnu_nnn_n");
    ZllbosonWeight_QCD3Down =  (TH1D*)scalefactor_fileZll->Get("eej_NNLO_NLO_nnd_nnn_n");
    ZllbosonWeight_EW1Up =     (TH1D*)scalefactor_fileZll->Get("eej_NNLO_NLO_nnn_unn_n");
    ZllbosonWeight_EW1Down =   (TH1D*)scalefactor_fileZll->Get("eej_NNLO_NLO_nnn_dnn_n");
    ZllbosonWeight_EW2Up =     (TH1D*)scalefactor_fileZll->Get("eej_NNLO_NLO_nnn_nun_n");
    ZllbosonWeight_EW2Down =   (TH1D*)scalefactor_fileZll->Get("eej_NNLO_NLO_nnn_ndn_n");
    ZllbosonWeight_EW3Up =     (TH1D*)scalefactor_fileZll->Get("eej_NNLO_NLO_nnn_nnu_n");
    ZllbosonWeight_EW3Down =   (TH1D*)scalefactor_fileZll->Get("eej_NNLO_NLO_nnn_nnd_n");
    ZllbosonWeight_MixedUp =   (TH1D*)scalefactor_fileZll->Get("eej_NNLO_NLO_nnn_nnn_u");
    ZllbosonWeight_MixedDown = (TH1D*)scalefactor_fileZll->Get("eej_NNLO_NLO_nnn_nnn_d");
    ZllbosonWeight_AlphaUp =   (TH1D*)scalefactor_fileZll->Get("eej_NNLO_NLO_nnn_nnn_n_alpha_up");
    ZllbosonWeight_AlphaDown = (TH1D*)scalefactor_fileZll->Get("eej_NNLO_NLO_nnn_nnn_n_alpha_down");
    ZllbosonWeight_muRUp =     (TH1D*)scalefactor_fileZll->Get("eej_NNLO_NLO_nnn_nnn_n_Weight_scale_variation_muR_2p0_muF_1p0");
    ZllbosonWeight_muRDown =   (TH1D*)scalefactor_fileZll->Get("eej_NNLO_NLO_nnn_nnn_n_Weight_scale_variation_muR_0p5_muF_1p0");
    ZllbosonWeight_muFUp =     (TH1D*)scalefactor_fileZll->Get("eej_NNLO_NLO_nnn_nnn_n_Weight_scale_variation_muR_1p0_muF_2p0");
    ZllbosonWeight_muFDown =   (TH1D*)scalefactor_fileZll->Get("eej_NNLO_NLO_nnn_nnn_n_Weight_scale_variation_muR_1p0_muF_0p5");
    Zllinitialized = true;
  }
}

void BosonHelper::Reset()
{
  // resets all member data
  scalefactor_fileW = 0;
  scalefactor_fileZvv = 0;
  scalefactor_fileZll = 0;
  path_to_sf_file = "";
  WbosonWeight_nominal = 0;
  WbosonWeight_QCD1Up = 0;
  WbosonWeight_QCD1Down = 0;
  WbosonWeight_QCD2Up = 0;
  WbosonWeight_QCD2Down = 0;
  WbosonWeight_QCD3Up = 0;
  WbosonWeight_QCD3Down = 0;
  WbosonWeight_EW1Up = 0;
  WbosonWeight_EW1Down = 0;
  WbosonWeight_EW2Up = 0;
  WbosonWeight_EW2Down = 0;
  WbosonWeight_EW3Up = 0;
  WbosonWeight_EW3Down = 0;
  WbosonWeight_MixedUp = 0;
  WbosonWeight_MixedDown = 0;
  WbosonWeight_AlphaUp = 0;
  WbosonWeight_AlphaDown = 0;
  WbosonWeight_muRUp = 0;
  WbosonWeight_muRDown = 0;
  WbosonWeight_muFUp = 0;
  WbosonWeight_muFDown = 0;

  ZvvbosonWeight_nominal = 0;
  ZvvbosonWeight_QCD1Up = 0;
  ZvvbosonWeight_QCD1Down = 0;
  ZvvbosonWeight_QCD2Up = 0;
  ZvvbosonWeight_QCD2Down = 0;
  ZvvbosonWeight_QCD3Up = 0;
  ZvvbosonWeight_QCD3Down = 0;
  ZvvbosonWeight_EW1Up = 0;
  ZvvbosonWeight_EW1Down = 0;
  ZvvbosonWeight_EW2Up = 0;
  ZvvbosonWeight_EW2Down = 0;
  ZvvbosonWeight_EW3Up = 0;
  ZvvbosonWeight_EW3Down = 0;
  ZvvbosonWeight_MixedUp = 0;
  ZvvbosonWeight_MixedDown = 0;
  ZvvbosonWeight_AlphaUp = 0;
  ZvvbosonWeight_AlphaDown = 0;
  ZvvbosonWeight_muRUp = 0;
  ZvvbosonWeight_muRDown = 0;
  ZvvbosonWeight_muFUp = 0;
  ZvvbosonWeight_muFDown = 0;
  
  ZllbosonWeight_nominal = 0;
  ZllbosonWeight_QCD1Up = 0;
  ZllbosonWeight_QCD1Down = 0;
  ZllbosonWeight_QCD2Up = 0;
  ZllbosonWeight_QCD2Down = 0;
  ZllbosonWeight_QCD3Up = 0;
  ZllbosonWeight_QCD3Down = 0;
  ZllbosonWeight_EW1Up = 0;
  ZllbosonWeight_EW1Down = 0;
  ZllbosonWeight_EW2Up = 0;
  ZllbosonWeight_EW2Down = 0;
  ZllbosonWeight_EW3Up = 0;
  ZllbosonWeight_EW3Down = 0;
  ZllbosonWeight_MixedUp = 0;
  ZllbosonWeight_MixedDown = 0;
  ZllbosonWeight_AlphaUp = 0;
  ZllbosonWeight_AlphaDown = 0;
  ZllbosonWeight_muRUp = 0;
  ZllbosonWeight_muRDown = 0;
  ZllbosonWeight_muFUp = 0;
  ZllbosonWeight_muFDown = 0;
  
  Winitialized = false;
  Zvvinitialized = false;
  Zllinitialized = false;
}

double BosonHelper::GetScaleFactorW(float W_Pt, string label)
{
  // this function gets the scale factor for a event dependent on the Pt of the W Boson
  if(!Winitialized) return 0.;
  int bin = -1;
  double sf = 0.;
  if (label == "nominal"){
    bin = WbosonWeight_nominal->FindBin(W_Pt);
    sf = WbosonWeight_nominal->GetBinContent(bin);
  }
  else if (label == "QCD1Up"){
    bin = WbosonWeight_QCD1Up->FindBin(W_Pt);
    sf = WbosonWeight_QCD1Up->GetBinContent(bin);  
  }
  else if (label == "QCD1Down"){
    bin = WbosonWeight_QCD1Down->FindBin(W_Pt);
    sf = WbosonWeight_QCD1Down->GetBinContent(bin);  
  }
  else if (label == "QCD2Up"){
    bin = WbosonWeight_QCD2Up->FindBin(W_Pt);
    sf = WbosonWeight_QCD2Up->GetBinContent(bin);  
  }
  else if (label == "QCD2Down"){
    bin = WbosonWeight_QCD2Down->FindBin(W_Pt);
    sf = WbosonWeight_QCD2Down->GetBinContent(bin);  
  }
  else if (label == "QCD3Up"){
    bin = WbosonWeight_QCD3Up->FindBin(W_Pt);
    sf = WbosonWeight_QCD3Up->GetBinContent(bin);  
  }
  else if (label == "QCD3Down"){
    bin = WbosonWeight_QCD3Down->FindBin(W_Pt);
    sf = WbosonWeight_QCD3Down->GetBinContent(bin);  
  }

  else if (label == "EW1Up"){
    bin = WbosonWeight_EW1Up->FindBin(W_Pt);
    sf = WbosonWeight_EW1Up->GetBinContent(bin);  
  }
  else if (label == "EW1Down"){
    bin = WbosonWeight_EW1Down->FindBin(W_Pt);
    sf = WbosonWeight_EW1Down->GetBinContent(bin);  
  }
  else if (label == "EW2Up"){
    bin = WbosonWeight_EW2Up->FindBin(W_Pt);
    sf = WbosonWeight_EW2Up->GetBinContent(bin);  
  }
  else if (label == "EW2Down"){
    bin = WbosonWeight_EW2Down->FindBin(W_Pt);
    sf = WbosonWeight_EW2Down->GetBinContent(bin);  
  }
  else if (label == "EW3Up"){
    bin = WbosonWeight_EW3Up->FindBin(W_Pt);
    sf = WbosonWeight_EW3Up->GetBinContent(bin);  
  }
  else if (label == "EW3Down"){
    bin = WbosonWeight_EW3Down->FindBin(W_Pt);
    sf = WbosonWeight_EW3Down->GetBinContent(bin);  
  }
  else if (label == "MixedUp"){
    bin = WbosonWeight_MixedUp->FindBin(W_Pt);
    sf = WbosonWeight_MixedUp->GetBinContent(bin);  
  }
  else if (label == "MixedDown"){
    bin = WbosonWeight_MixedDown->FindBin(W_Pt);
    sf = WbosonWeight_MixedDown->GetBinContent(bin);  
  }
  else if (label == "AlphaUp") {
    bin = WbosonWeight_AlphaUp->FindBin(W_Pt);
    sf = WbosonWeight_AlphaUp->GetBinContent(bin);  
  }
  else if (label == "AlphaDown") {
    bin = WbosonWeight_AlphaDown->FindBin(W_Pt);
    sf = WbosonWeight_AlphaDown->GetBinContent(bin);  
  }
  else if (label == "muRUp") {
    bin = WbosonWeight_muRUp->FindBin(W_Pt);
    sf = WbosonWeight_muRUp->GetBinContent(bin);  
  }
  else if (label == "muRDown") {
    bin = WbosonWeight_muRDown->FindBin(W_Pt);
    sf = WbosonWeight_muRDown->GetBinContent(bin);  
  }
  else if (label == "muFUp") {
    bin = WbosonWeight_muFUp->FindBin(W_Pt);
    sf = WbosonWeight_muFUp->GetBinContent(bin);  
  }
  else if (label == "muFDown") {
    bin = WbosonWeight_muFDown->FindBin(W_Pt);
    sf = WbosonWeight_muFDown->GetBinContent(bin);  
  }
  if(W_Pt<=30.) sf = 1.;
  return sf;
}

double BosonHelper::GetScaleFactorZvv(float Z_Pt, string label)
{
  // this function gets the scale factor for a event dependent on the Pt of the Z Boson
  if(!Zvvinitialized) return 0.;
  int bin = -1;
  double sf = 0.;
  if (label == "nominal"){
    bin = ZvvbosonWeight_nominal->FindBin(Z_Pt);
    sf = ZvvbosonWeight_nominal->GetBinContent(bin);
  }
  else if (label == "QCD1Up"){
    bin = ZvvbosonWeight_QCD1Up->FindBin(Z_Pt);
    sf = ZvvbosonWeight_QCD1Up->GetBinContent(bin);  
  }
  else if (label == "QCD1Down"){
    bin = ZvvbosonWeight_QCD1Down->FindBin(Z_Pt);
    sf = ZvvbosonWeight_QCD1Down->GetBinContent(bin);  
  }
  else if (label == "QCD2Up"){
    bin = ZvvbosonWeight_QCD2Up->FindBin(Z_Pt);
    sf = ZvvbosonWeight_QCD2Up->GetBinContent(bin);  
  }
  else if (label == "QCD2Down"){
    bin = ZvvbosonWeight_QCD2Down->FindBin(Z_Pt);
    sf = ZvvbosonWeight_QCD2Down->GetBinContent(bin);  
  }
  else if (label == "QCD3Up"){
    bin = ZvvbosonWeight_QCD3Up->FindBin(Z_Pt);
    sf = ZvvbosonWeight_QCD3Up->GetBinContent(bin);  
  }
  else if (label == "QCD3Down"){
    bin = ZvvbosonWeight_QCD3Down->FindBin(Z_Pt);
    sf = ZvvbosonWeight_QCD3Down->GetBinContent(bin);  
  }

  else if (label == "EW1Up"){
    bin = ZvvbosonWeight_EW1Up->FindBin(Z_Pt);
    sf = ZvvbosonWeight_EW1Up->GetBinContent(bin);  
  }
  else if (label == "EW1Down"){
    bin = ZvvbosonWeight_EW1Down->FindBin(Z_Pt);
    sf = ZvvbosonWeight_EW1Down->GetBinContent(bin);  
  }
  else if (label == "EW2Up"){
    bin = ZvvbosonWeight_EW2Up->FindBin(Z_Pt);
    sf = ZvvbosonWeight_EW2Up->GetBinContent(bin);  
  }
  else if (label == "EW2Down"){
    bin = ZvvbosonWeight_EW2Down->FindBin(Z_Pt);
    sf = ZvvbosonWeight_EW2Down->GetBinContent(bin);  
  }
  else if (label == "EW3Up"){
    bin = ZvvbosonWeight_EW3Up->FindBin(Z_Pt);
    sf = ZvvbosonWeight_EW3Up->GetBinContent(bin);  
  }
  else if (label == "EW3Down"){
    bin = ZvvbosonWeight_EW3Down->FindBin(Z_Pt);
    sf = ZvvbosonWeight_EW3Down->GetBinContent(bin);  
  }
  else if (label == "MixedUp"){
    bin = ZvvbosonWeight_MixedUp->FindBin(Z_Pt);
    sf = ZvvbosonWeight_MixedUp->GetBinContent(bin);  
  }
  else if (label == "MixedDown"){
    bin = ZvvbosonWeight_MixedDown->FindBin(Z_Pt);
    sf = ZvvbosonWeight_MixedDown->GetBinContent(bin);  
  }
  else if (label == "AlphaUp") {
    bin = ZvvbosonWeight_AlphaUp->FindBin(Z_Pt);
    sf = ZvvbosonWeight_AlphaUp->GetBinContent(bin);  
  }
  else if (label == "AlphaDown") {
    bin = ZvvbosonWeight_AlphaDown->FindBin(Z_Pt);
    sf = ZvvbosonWeight_AlphaDown->GetBinContent(bin);  
  }
  else if (label == "muRUp") {
    bin = ZvvbosonWeight_muRUp->FindBin(Z_Pt);
    sf = ZvvbosonWeight_muRUp->GetBinContent(bin);  
  }
  else if (label == "muRDown") {
    bin = ZvvbosonWeight_muRDown->FindBin(Z_Pt);
    sf = ZvvbosonWeight_muRDown->GetBinContent(bin);  
  }
  else if (label == "muFUp") {
    bin = ZvvbosonWeight_muFUp->FindBin(Z_Pt);
    sf = ZvvbosonWeight_muFUp->GetBinContent(bin);  
  }
  else if (label == "muFDown") {
    bin = ZvvbosonWeight_muFDown->FindBin(Z_Pt);
    sf = ZvvbosonWeight_muFDown->GetBinContent(bin);  
  }
  if(Z_Pt<=30.) sf = 1.;
  return sf;
}


double BosonHelper::GetScaleFactorZll(float Z_Pt, string label)
{
  // this function gets the scale factor for a event dependent on the Pt of the Z Boson
  if(!Zllinitialized) return 0.;
  int bin = -1;
  double sf = 0.;
  if (label == "nominal"){
    bin = ZllbosonWeight_nominal->FindBin(Z_Pt);
    sf = ZllbosonWeight_nominal->GetBinContent(bin);
  }
  else if (label == "QCD1Up"){
    bin = ZllbosonWeight_QCD1Up->FindBin(Z_Pt);
    sf = ZllbosonWeight_QCD1Up->GetBinContent(bin);  
  }
  else if (label == "QCD1Down"){
    bin = ZllbosonWeight_QCD1Down->FindBin(Z_Pt);
    sf = ZllbosonWeight_QCD1Down->GetBinContent(bin);  
  }
  else if (label == "QCD2Up"){
    bin = ZllbosonWeight_QCD2Up->FindBin(Z_Pt);
    sf = ZllbosonWeight_QCD2Up->GetBinContent(bin);  
  }
  else if (label == "QCD2Down"){
    bin = ZllbosonWeight_QCD2Down->FindBin(Z_Pt);
    sf = ZllbosonWeight_QCD2Down->GetBinContent(bin);  
  }
  else if (label == "QCD3Up"){
    bin = ZllbosonWeight_QCD3Up->FindBin(Z_Pt);
    sf = ZllbosonWeight_QCD3Up->GetBinContent(bin);  
  }
  else if (label == "QCD3Down"){
    bin = ZllbosonWeight_QCD3Down->FindBin(Z_Pt);
    sf = ZllbosonWeight_QCD3Down->GetBinContent(bin);  
  }

  else if (label == "EW1Up"){
    bin = ZllbosonWeight_EW1Up->FindBin(Z_Pt);
    sf = ZllbosonWeight_EW1Up->GetBinContent(bin);  
  }
  else if (label == "EW1Down"){
    bin = ZllbosonWeight_EW1Down->FindBin(Z_Pt);
    sf = ZllbosonWeight_EW1Down->GetBinContent(bin);  
  }
  else if (label == "EW2Up"){
    bin = ZllbosonWeight_EW2Up->FindBin(Z_Pt);
    sf = ZllbosonWeight_EW2Up->GetBinContent(bin);  
  }
  else if (label == "EW2Down"){
    bin = ZllbosonWeight_EW2Down->FindBin(Z_Pt);
    sf = ZllbosonWeight_EW2Down->GetBinContent(bin);  
  }
  else if (label == "EW3Up"){
    bin = ZllbosonWeight_EW3Up->FindBin(Z_Pt);
    sf = ZllbosonWeight_EW3Up->GetBinContent(bin);  
  }
  else if (label == "EW3Down"){
    bin = ZllbosonWeight_EW3Down->FindBin(Z_Pt);
    sf = ZllbosonWeight_EW3Down->GetBinContent(bin);  
  }
  else if (label == "MixedUp"){
    bin = ZllbosonWeight_MixedUp->FindBin(Z_Pt);
    sf = ZllbosonWeight_MixedUp->GetBinContent(bin);  
  }
  else if (label == "MixedDown"){
    bin = ZllbosonWeight_MixedDown->FindBin(Z_Pt);
    sf = ZllbosonWeight_MixedDown->GetBinContent(bin);  
  }
  else if (label == "AlphaUp") {
    bin = ZllbosonWeight_AlphaUp->FindBin(Z_Pt);
    sf = ZllbosonWeight_AlphaUp->GetBinContent(bin);  
  }
  else if (label == "AlphaDown") {
    bin = ZllbosonWeight_AlphaDown->FindBin(Z_Pt);
    sf = ZllbosonWeight_AlphaDown->GetBinContent(bin);  
  }
  else if (label == "muRUp") {
    bin = ZllbosonWeight_muRUp->FindBin(Z_Pt);
    sf = ZllbosonWeight_muRUp->GetBinContent(bin);  
  }
  else if (label == "muRDown") {
    bin = ZllbosonWeight_muRDown->FindBin(Z_Pt);
    sf = ZllbosonWeight_muRDown->GetBinContent(bin);  
  }
  else if (label == "muFUp") {
    bin = ZllbosonWeight_muFUp->FindBin(Z_Pt);
    sf = ZllbosonWeight_muFUp->GetBinContent(bin);  
  }
  else if (label == "muFDown") {
    bin = ZllbosonWeight_muFDown->FindBin(Z_Pt);
    sf = ZllbosonWeight_muFDown->GetBinContent(bin);  
  }
  if(Z_Pt<=30.) sf = 1.;
  return sf;
}


// QCD Helper to retrieve scale factor for QCD Estimation with iso inverted ntuples

class QCDHelper
{
	public:
		// see the definition/implementation file for a description of the functions 
		QCDHelper(TString path_to_sf_file_);
		~QCDHelper();
		double GetScaleFactor(int n_jets, int n_btags, int n_isoinverted_electrons, int n_isoinverted_muons);
		double GetScaleFactorError(int n_jets, int n_btags, int n_isoinverted_electrons, int n_isoinverted_muons);
		double GetScaleFactorErrorUp(int n_jets, int n_btags, int n_isoinverted_electrons, int n_isoinverted_muons);
		double GetScaleFactorErrorDown(int n_jets, int n_btags, int n_isoinverted_electrons, int n_isoinverted_muons);
		void Reset();
		void LoadFile(TString path_to_sf_file_);
			
	private:
		// pointer for the root file containing the desired histograms
		TFile* scalefactor_file = 0;
		// path to the root file
		TString path_to_sf_file = "";
		// histograms containing the scale factors for electron and muon channel separately
		TH2D* Mu_SF = 0;
		TH2D* El_SF = 0;
		// flag if the file and the histograms were read properly
		bool initialized = false;
};

QCDHelper::QCDHelper(TString path_to_sf_file_)
{
	// just the constructor which loads a root file containing the histograms with the scale factors using the LoadFile function
	LoadFile(path_to_sf_file_);
}

void QCDHelper::LoadFile(TString path_to_sf_file_)
{
	// this function loads the file given by a string and initializes the 2 needed histograms if the file was loaded correctly
	path_to_sf_file = path_to_sf_file_;
	if(path_to_sf_file!="")
	{
		scalefactor_file = TFile::Open(path_to_sf_file);
	}
	if(scalefactor_file)
	{
		El_SF = (TH2D*)scalefactor_file->Get("El_FakeSF");
		Mu_SF = (TH2D*)scalefactor_file->Get("Mu_FakeSF");
		initialized = true;
	}
}

void QCDHelper::Reset()
{
	// resets all member data
	scalefactor_file = 0;
	path_to_sf_file = "";
	Mu_SF = 0;
	El_SF = 0;
	initialized = false;
}

double QCDHelper::GetScaleFactor(int n_jets, int n_btags, int n_isoinverted_electrons, int n_isoinverted_muons)
{
	// this function gets the scale factor for a event dependent on the number of jets,btags and the lepton flavor
	if(!initialized) return 0.;
	int bin = -1;
	double sf = 0.;
	int N_jets = n_jets>6 ? 6 : n_jets;
	int N_btags = n_btags>4 ? 4 : n_btags;
	if(n_isoinverted_electrons==1&&n_isoinverted_muons==0) 
	{
		bin = El_SF->GetBin(N_jets+1,N_btags+1);
		sf = El_SF->GetBinContent(bin);
		// the values in the file are not correct for electron 6j4b category and have to be set manually
		if(N_jets>=6&&N_btags>=4)
		{
			sf = 1.8;
		}
	}
	else if(n_isoinverted_electrons==0&&n_isoinverted_muons==1)
	{
		bin = Mu_SF->GetBin(N_jets+1,N_btags+1);
		sf = Mu_SF->GetBinContent(bin);
	}
	else 
	{
		return 0.;
	}
	return sf<=0. ? 0.001 : sf;
}

double QCDHelper::GetScaleFactorError(int n_jets, int n_btags, int n_isoinverted_electrons, int n_isoinverted_muons)
{
	// this function gets the error on the scale factor for a event dependent on the number of jets,btags and the lepton flavor
	if(!initialized) return 0.;
	int bin = -1;
	double sf_err = 0.;
	int N_jets = n_jets>6 ? 6 : n_jets;
	int N_btags = n_btags>4 ? 4 : n_btags;
	if(n_isoinverted_electrons==1&&n_isoinverted_muons==0) 
	{
		bin = El_SF->GetBin(N_jets+1,N_btags+1);
		sf_err = El_SF->GetBinError(bin);
		// the values in the file are not correct for electron 6j4b category and have to be set manually
		if(N_jets>=6&&N_btags>=4)
		{
			sf_err = 2.0;
		}
	}
	else if(n_isoinverted_electrons==0&&n_isoinverted_muons==1)
	{
		bin = Mu_SF->GetBin(N_jets+1,N_btags+1);
		sf_err = Mu_SF->GetBinError(bin);
	}
	else 
	{
		return 0.;
	}
	return sf_err<0. ? 0. : sf_err;
}

double QCDHelper::GetScaleFactorErrorUp(int n_jets, int n_btags, int n_isoinverted_electrons, int n_isoinverted_muons)
{
	// gets the scale factor + error
	if(!initialized) return 0.;
	double sf = GetScaleFactor(n_jets,n_btags,n_isoinverted_electrons,n_isoinverted_muons);
	double sf_err = GetScaleFactorError(n_jets,n_btags,n_isoinverted_electrons,n_isoinverted_muons);
	return sf+sf_err <=0. ? 0.002 : sf+sf_err;
}

double QCDHelper::GetScaleFactorErrorDown(int n_jets, int n_btags, int n_isoinverted_electrons, int n_isoinverted_muons)
{
	// gets the scale factor - error
	if(!initialized) return 0.;
	double sf = GetScaleFactor(n_jets,n_btags,n_isoinverted_electrons,n_isoinverted_muons);
	double sf_err = GetScaleFactorError(n_jets,n_btags,n_isoinverted_electrons,n_isoinverted_muons);
	return sf-sf_err <=0. ? 0.0005 : sf-sf_err;
}

QCDHelper::~QCDHelper()
{
	// destructor which closes the file if it was loaded in the first place
	if(initialized) scalefactor_file->Close();
}





// Helper struct to fill plots more efficiently
// Until GCC 4.9 struct cannot have init values if one wants to initialize it with bracket lists
struct structHelpFillHisto{
  TH1* histo;
  double var;
  double weight;
};

// helper function to fill plots more efficiently
void helperFillHisto(const std::vector<structHelpFillHisto>& paramVec)
{
  for (const auto &singleParams: paramVec)
  // singleParams: histo, var, weight
  {
    if((singleParams.weight)!=0)
      singleParams.histo->Fill(fmin(singleParams.histo->GetXaxis()->GetXmax()-1e-6,fmax(singleParams.histo->GetXaxis()->GetXmin()+1e-6,singleParams.var)),singleParams.weight);
  }
}

// Helper struct to fill plots more efficiently
// Until GCC 4.9 struct cannot have init values if one wants to initialize it with bracket lists
struct structHelpFillTwoDimHisto{
  TH2* histo;
  double var1;
  double var2;
  double weight;
};

// helper function to fill plots more efficiently
void helperFillTwoDimHisto(const std::vector<structHelpFillTwoDimHisto>& paramVec)
{
  for (const auto &singleParams: paramVec)
  // singleParams: histo, var1, var2, weight
  {
    if((singleParams.weight)!=0)
      singleParams.histo->Fill(fmin(singleParams.histo->GetXaxis()->GetXmax()-1e-6,fmax(singleParams.histo->GetXaxis()->GetXmin()+1e-6,singleParams.var1)),fmin(singleParams.histo->GetXaxis()->GetXmax()-1e-6,fmax(singleParams.histo->GetXaxis()->GetXmin()+1e-6,singleParams.var2)),singleParams.weight);
  }
}

void plot(){
  TH1F::SetDefaultSumw2();

  // create vector of systematics
  std::vector<Systematics::Type> v_SystTypes = Systematics::getTypeVector();
  //for(auto itsyst : v_SystTypes){std::cout<< " Know :" << itsyst << std::endl;}
  char currentdir[1024];
  getcwd(currentdir, sizeof(currentdir));
  string workingdir(currentdir);

  TString WBoson_file = workingdir + "/TheoryXS_evj.root";
  TString ZvvBoson_file = workingdir + "/TheoryXS_vvj.root";
  TString ZllBoson_file = workingdir + "/TheoryXS_eej.root";

  std::string csvHFfile="/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/factorized_jes/csv_rwt_fit_hf_v2_final_2017_6_7_all.root";
  std::string csvLFfile="/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/factorized_jes/csv_rwt_fit_lf_v2_final_2017_6_7_all.root";
  TString qcd_file = "/nfs/dust/cms/user/mwassmer/QCD_Estimation_September17/QCD_Estimation/QCD_Estimation_FakeScaleFactor_nominal.root";
  
  CSVHelper* internalCSVHelper= new CSVHelper(csvHFfile,csvLFfile, 5,4,3,v_SystTypes);
  LeptonSFHelper* internalLeptonSFHelper= new LeptonSFHelper();
  QCDHelper* internalQCDHelper = new QCDHelper(qcd_file);
  BosonHelper* internalBosonHelper = new BosonHelper(WBoson_file, ZvvBoson_file, ZllBoson_file);

  // open files
  TChain* chain = new TChain("MVATree");
  char* filenames = getenv ("FILENAMES");
  char* outfilename = getenv ("OUTFILENAME");
  string processname = string(getenv ("PROCESSNAME"));
  string suffix = string(getenv ("SUFFIX"));
  int maxevents = atoi(getenv ("MAXEVENTS"));
  int skipevents = atoi(getenv ("SKIPEVENTS"));
  string eventFilterFile = string(getenv("EVENTFILTERFILE"));

  std::cout<<"processname" <<processname<<std::endl;
  std::cout<<"suffix" <<suffix<<std::endl;

  std::vector<TString> databaseRelevantFilenames;

  // create event filter class
  EventFilter* evtFilter = new EventFilter(eventFilterFile);

  int eventsAnalyzed=0;
  float sumOfWeights=0;

  int DoWeights=1;
  int electron_data=0;
  int muon_data=0;
  int DoWbosonReweighting = 0;
  int DoZbosonReweighting = 0;

  //initialize Trigger Helper

  if(processname=="MET" || processname=="data_obs"){DoWeights=0; std::cout<<"is data, dont use nominal weights"<<std::endl;}
  if(processname.find("w_lnu_jets")!=std::string::npos){DoWbosonReweighting=1; std::cout<<"is W Sample -> apply Reweighting"<<std::endl;}
  if(processname.find("z_nunu_jets")!=std::string::npos){DoZbosonReweighting=1; std::cout<<"is Z Sample -> apply Reweighting"<<std::endl;}



  // read in samples to add to chain and get relevant names for the database
  std::map<TString, TString> sampleDataBaseIdentifiers;
  std::map<TString, std::map<TString, long>> sampleDataBaseFoundEvents;
  std::map<TString, std::map<TString, long>> sampleDataBaseLostEvents;
  std::map<TString, TString> sampleTranslationMapCPP ;

  // vector to hold the jes uncertainty names
  std::vector<TString> SystListForDataBase;
  
  
  Systematics::Type internalSystType=Systematics::NA;
  
  // DANGERZONE
  // This will not work if mixing multiple systematics in one job!!
  TString globalFileNameForSystType="";
  
  string buf;
  stringstream ss(filenames); 
  TString samplename_in_database="";
  while (ss >> buf){
    chain->Add(buf.c_str());
    TString thisfilename = buf.c_str();
    TString originalfilename=buf.c_str();
    //std::cout<<"file "<<buf.c_str()<<" "<<thisfilename<<std::endl; // karim debug 
    // cut of directories
    thisfilename.Replace(0,thisfilename.Last('/')+1,"");
    //cut of trailing tree and root
    thisfilename.Replace(thisfilename.Last('_'),thisfilename.Length(),"");
    // copy the string for figuring out internalSystType
    TString filenameforSytType=TString(thisfilename);
    // remove syst name in case of JES or JER. Not needed in current database format
    //std::cout<<thisfilename<<std::endl;
    if(thisfilename.Contains("JES")==1 or thisfilename.Contains("JER")==1 or thisfilename.Contains("nominal")==1){
      thisfilename.Replace(thisfilename.Last('_'),thisfilename.Length()-1,"");
      }
    //std::cout<<thisfilename<<std::endl;
    //remove number
    int lastUnderscore=thisfilename.Last('_');
    //thisfilename.Replace(thisfilename.Last('_'),1,"");
    //thisfilename.Replace(thisfilename.Last('_'),lastUnderscore-thisfilename.Last('_'),"");
    thisfilename.Replace(thisfilename.Last('_'),thisfilename.Length(),"");
    //remove remaining underscores
    while(thisfilename.Last('_')>=0){ thisfilename.Replace(thisfilename.Last('_'),1,"");}
    std::cout<<" relevant database name "<<thisfilename<<std::endl;
        
   sampleDataBaseIdentifiers[originalfilename]=thisfilename;
    
    //check if already in vectr
    TString translatedFileNameForDataBase;
    """
  jsonfileWithSampleTranslation=open('/nfs/dust/cms/user/kelmorab/DataBaseCodeForScriptGenerator/MEMDataBaseSpring17/MEMDataBase/MEMDataBase/test/sampleNameMap.json',"r")
  jsonstringWithSampleTranslation=jsonfileWithSampleTranslation.read()
  sampleTranslationMapPython=json.loads(jsonstringWithSampleTranslation)
  for transSample in sampleTranslationMapPython:
    retstr+="sampleTranslationMapCPP[TString(\""+transSample+"\")]=TString(\""+sampleTranslationMapPython[transSample]+"\");\n"
  
  retstr+="""
  
    translatedFileNameForDataBase=sampleTranslationMapCPP[thisfilename];
    if(processname=="QCD" or processname=="QCD_CMS_ttH_QCDScaleFactorUp" or processname=="QCD_CMS_ttH_QCDScaleFactorDown"){
      translatedFileNameForDataBase+="QCD";
      }
    samplename_in_database=translatedFileNameForDataBase;
    if(! (std::find(databaseRelevantFilenames.begin(),databaseRelevantFilenames.end(),translatedFileNameForDataBase)!=databaseRelevantFilenames.end()  )){
      databaseRelevantFilenames.push_back(translatedFileNameForDataBase.Copy());
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
  
  // now figure out internalSystType
  filenameforSytType.Replace(0,filenameforSytType.Last('_')+1,"");
  // nominal is the empty string here
  if(filenameforSytType=="nominal"){filenameforSytType="";}
  internalSystType = Systematics::get(filenameforSytType.Data());
  std::cout<<"internal systematic filename, int and typename "<<filenameforSytType<<" "<<internalSystType<<" "<<Systematics::toString(internalSystType)<<std::endl;
  if(filenameforSytType!=TString(Systematics::toString(internalSystType))){std::cout<<"ERROR could not recover systematic from enum"<<std::endl; exit(0);}
  globalFileNameForSystType=filenameforSytType;
  }// end loop of filename parsing
  
  
  TString vecNameForDataBase="mem_p";
  if(globalFileNameForSystType!=""){
    TString vecNameForDataBaseBuffer=globalFileNameForSystType;
    if(globalFileNameForSystType.Contains("JES")==1){vecNameForDataBaseBuffer.Replace(0,3,"");}
    vecNameForDataBase="mem_"+vecNameForDataBaseBuffer+"_p";
    }
  std::vector<TString> vec_memStrings;
  vec_memStrings.push_back(vecNameForDataBase);
  
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
  Long64_t Evt_ID;
  Long64_t Evt_Run;
  Long64_t Evt_Lumi;
  
  Int_t Evt_ID_INT;
  Int_t Evt_Run_INT;
  Int_t Evt_Lumi_INT;

  chain->SetBranchStatus("Evt_ID",1);
  chain->SetBranchStatus("Evt_Run",1);
  chain->SetBranchStatus("Evt_Lumi",1);
  
  // figure out what kind of branch this is
  bool evtIDisIntBranch=1;
  //TBranch* evtBranch=chain->GetBranch("Evt_ID");
  //TString branchNameString=TString(evtBranch->GetTitle());
  //if(branchNameString.Contains("/L")){
  //  evtIDisIntBranch=0;
    chain->SetBranchAddress("Evt_ID",&Evt_ID);
    chain->SetBranchAddress("Evt_Run",&Evt_Run);
    chain->SetBranchAddress("Evt_Lumi",&Evt_Lumi);
  //}
  //else{
  //chain->SetBranchAddress("Evt_ID",&Evt_ID_INT);
  //chain->SetBranchAddress("Evt_Run",&Evt_Run_INT);
  //chain->SetBranchAddress("Evt_Lumi",&Evt_Lumi_INT);
//}
  
  // some timers 
  double totalTime=0;
  double totalTimeGetEntry=0;
  double totalTimeFillHistograms=0;
  double totalTimeReadDataBase=0;
  double totalTimeEvalDNN=0;
  double totalTimeEvalWeightsAndBDT=0;
  double totalTimeSampleWeight=0;
  double totalTimeCalculateSFs=0;
  double totalTimeMapping=0;
  
  TStopwatch* timerGetEntry=new TStopwatch();
  TStopwatch* timerFillHistograms=new TStopwatch();
  TStopwatch* timerReadDataBase=new TStopwatch();
  TStopwatch* timerEvalDNN=new TStopwatch();
  TStopwatch* timerEvalWeightsAndBDT=new TStopwatch();
  TStopwatch* timerSampleWeight=new TStopwatch();
  TStopwatch* timerCalculateSFs=new TStopwatch();
  TStopwatch* timerTotal=new TStopwatch();
  TStopwatch* timerMapping=new TStopwatch();
  

 
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
  rstr+="  "+thisDataBaseName+"DB.push_back(new MEMDataBase(\""+thisDataBasePath+"\",vec_memStrings));"+"\n"
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
  rstr+="  DataBaseMEMResult* "+thisDataBaseName+"DummyResultPointer= new DataBaseMEMResult(vec_memStrings);\n"
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
  
  rstr+="  "+thisDataBaseName+"p="+thisDataBaseName+"DummyResultPointer->p_vec[0];\n"
  rstr+="  "+thisDataBaseName+"p_sig="+thisDataBaseName+"DummyResultPointer->p_sig;\n"
  rstr+="  "+thisDataBaseName+"p_bkg="+thisDataBaseName+"DummyResultPointer->p_bkg;\n"
  rstr+="  "+thisDataBaseName+"p_err_sig="+thisDataBaseName+"DummyResultPointer->p_err_sig;\n"
  rstr+="  "+thisDataBaseName+"p_err_bkg="+thisDataBaseName+"DummyResultPointer->p_err_bkg;\n"
  rstr+="  "+thisDataBaseName+"n_perm_sig="+thisDataBaseName+"DummyResultPointer->n_perm_sig;\n"
  rstr+="  "+thisDataBaseName+"n_perm_bkg="+thisDataBaseName+"DummyResultPointer->n_perm_bkg;\n"
  
  rstr+="""
    TString currentRelevantSampleName=sampleDataBaseIdentifiers[currentfilename];
    TString translatedCurrentRelevantSampleName=sampleTranslationMapCPP[currentRelevantSampleName];
    if(processname=="QCD" or processname=="QCD_CMS_ttH_QCDScaleFactorUp" or processname=="QCD_CMS_ttH_QCDScaleFactorDown"){
      translatedCurrentRelevantSampleName+="QCD";
      }
    //std::cout<<currentfilename<<" "<<currentRelevantSampleName<<" "<<translatedCurrentRelevantSampleName<<std::endl;
  """
  
  rstr+=" // loop over subsamples of this database\n"
  rstr+="    int nfoundresults=0;\n"
  
  rstr+="  if((N_BTagsM>=3 && N_Jets>=6) || (N_BTagsM>=4 && (N_Jets==4 || N_Jets==5))){ \n"
  rstr+="  databaseWatch->Start(); \n"
  
  rstr+="  for(unsigned int isn=0; isn<"+thisDataBaseName+"DB.size();isn++){ \n"
  rstr+="    if(databaseRelevantFilenames.at(isn)==translatedCurrentRelevantSampleName){;\n"
  rstr+="         DataBaseMEMResult "+thisDataBaseName+"Result = "+thisDataBaseName+"DB.at(isn)->GetMEMResult(databaseRelevantFilenames.at(isn),Evt_Run,Evt_Lumi,Evt_ID);\n"

  #rstr+="        std::cout<<\" p p_sig p_bkg p_err_sig p_err_bkg n_perm_sig n_perm_bkg \"<<"+thisDataBaseName+"p<<\" \"<<"+thisDataBaseName+"p_sig<<\"   \"<<"+thisDataBaseName+"p_bkg<<\" \"<<"+thisDataBaseName+"p_err_sig<<\" \"<<"+thisDataBaseName+"p_err_bkg<<\" \"<<"+thisDataBaseName+"n_perm_sig<<\" \"<<"+thisDataBaseName+"n_perm_bkg<<\" \"<<std::endl;\n"
  
  rstr+="        // check if the event was found using the default values. If any event was found the return values should be different and the resuilt will be replaced\n"
  #rstr+="        if(("+thisDataBaseName+"Result.p != "+thisDataBaseName+"DummyResultPointer->p) or ("+thisDataBaseName+"Result.p_sig != "+thisDataBaseName+"DummyResultPointer->p_sig) or ("+thisDataBaseName+"Result.p_bkg != "+thisDataBaseName+"DummyResultPointer->p_bkg) or ("+thisDataBaseName+"Result.p_err_sig != "+thisDataBaseName+"DummyResultPointer->p_err_sig) or ("+thisDataBaseName+"Result.p_err_bkg != "+thisDataBaseName+"DummyResultPointer->p_err_bkg) or ("+thisDataBaseName+"Result.n_perm_sig != "+thisDataBaseName+"DummyResultPointer->n_perm_sig) or ("+thisDataBaseName+"Result.n_perm_bkg != "+thisDataBaseName+"DummyResultPointer->n_perm_bkg)){\n"
  rstr+="        if(("+thisDataBaseName+"Result.p_vec[0] != -99)){\n"
  rstr+="        nfoundresults+=1;"

  rstr+="      "+thisDataBaseName+"p="+thisDataBaseName+"Result.p_vec[0];\n"
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
  rstr+="    std::cout<<\"WARNING found not exaclty one result \"<<nfoundresults<<\" \"<<currentRelevantSampleName<<\" \"<<Evt_ID<<\" \"<<N_Jets<<\" \"<<N_BTagsM<<std::endl;\n"
  rstr+="    if(N_BTagsM>=3){\n"
  rstr+="      std::cout<<\"VETO this event\"<<\" \"<<currentRelevantSampleName<<\" \"<<Evt_ID<<\" \"<<N_Jets<<\" \"<<N_BTagsM<<std::endl;\n"
  rstr+="      //std::cout<<\"RedoThisEvent\"<<\" \"<<currentRelevantSampleName<<\" \"<<currentfilename<<\" \"<<Evt_Run<<\" \"<<Evt_Lumi<<\" \"<<Evt_ID<<std::endl;\n"
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
  rstr+="  //std::cout<<\"FOUNDEVENT\"<<\" \"<<currentRelevantSampleName<<\" \"<<Evt_ID<<\" \"<<N_Jets<<\" \"<<N_BTagsM<<std::endl;\n"
  rstr+=" }\n"
  rstr+="  databaseWatch->Stop(); memTime+=databaseWatch->RealTime();\n"
  if skipNonExistingEvent:
    rstr+="  if("+thisDataBaseName+"FoundResult==0 and N_BTagsM>=3){ std::cout<<\"skipping\"<<std::endl; continue; }\n"
  rstr+="  }\n"
  #if skipNonExistingEvent:
    #rstr+="  if("+thisDataBaseName+"FoundResult==0 and N_BTagsM>=3){ std::cout<<\"skipping\"<<std::endl; continue; }\n"
  
  rstr+="  //std::cout<<\"FINAL p p_sig p_bkg p_err_sig p_err_bkg n_perm_sig n_perm_bkg \"<<"+thisDataBaseName+"p<<\" \"<<"+thisDataBaseName+"p_sig<<\" \"<<"+thisDataBaseName+"p_bkg<<\" \"<<"+thisDataBaseName+"p_err_sig<<\" \"<<"+thisDataBaseName+"p_err_bkg<<\" \"<<"+thisDataBaseName+"n_perm_sig<<\" \"<<"+thisDataBaseName+"n_perm_bkg<<\" \"<<std::endl;\n"
  return rstr
  

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
  # Write all individual systnames and systweights in nested vector to use together with function allowing variadic vector size -> speed-up of compilation and less code lines
  text+='     std::vector<structHelpFillHisto> helpWeightVec_' + name + ' = {'
  for sn,sw in zip(systnames,systweights):
    text+='       { ' + 'h_'+name+sn + ', double(' + varname + '), ' + '('+sw+')*(weight_'+name+')' + '},'
  # finish vector
  text+='     };\n'
  # call helper fill histo function which is defined in the beginning
  text+='     helperFillHisto(helpWeightVec_' + name + ');\n' 
  return text

def fillTwoDimHistoSyst(name,varname1,varname2,weight,systnames,systweights):
  text='      float weight_'+name+'='+weight+';\n'
  # Write all individual systnames and systweights in nested vector to use together with function allowing variadic vector size -> speed-up of compilation and less code lines
  text+='     std::vector<structHelpFillTwoDimHisto> helpWeightVec_' + name + ' = {'
  for sn,sw in zip(systnames,systweights):
    text+='       { ' + 'h_'+name+sn + ', ' + varname1 + ', ' + varname2 + ', ' + '('+sw+')*(weight_'+name+')' + '},'
  # finish vector
  text+='     };\n'
  # call helper fill histo function which is defined in the beginning
  text+='     helperFillTwoDimHisto(helpWeightVec_' + name + ');\n' 
  return text

def startLoop():
  return """
  timerTotal->Start();
  // loop over all events
  long nentries = chain->GetEntries();
  cout << "total number of events: " << nentries << endl;

  for (long iEntry=skipevents;iEntry<nentries;iEntry++) {
    if(iEntry==maxevents) break;
    if(iEntry%10000==0) cout << "analyzing event " << iEntry << endl;
    
    timerGetEntry->Start();
    chain->GetEntry(iEntry);
//    if(evtIDisIntBranch==1){
//      Evt_ID=Evt_ID_INT;
//      Evt_Lumi=Evt_Lumi_INT;
//      Evt_Run=Evt_Run_INT;
//      }
    
    //PLACEHOLDERFORCASTLINES
    
    
//     std::cout<<"Evt_ID "<<Evt_ID <<" "<<Int_t(Evt_ID)<<" "<<std::endl;
     if(Evt_ID!=Int_t(Evt_ID)){std::cout<<"PROBLEM"<<"Evt_ID "<<Evt_ID <<" "<<Int_t(Evt_ID)<<std::endl;}
//    std::cout<<"NJEts "<<N_Jets<<" "<<N_JetsLONGDUMMY<<std::endl;
//    std::cout<<"NBtagsM "<<N_BTagsM<<" "<<N_BTagsMLONGDUMMY<<std::endl;

    TString currentfilename="";
    currentfilename = chain->GetCurrentFile()->GetName();   
    int hasTrigger=0;
    if(currentfilename.Index("withTrigger")!=-1){hasTrigger=1;}
    eventsAnalyzed++;
    sumOfWeights+=Weight;
    
    // skip events in the filter list
    if(evtFilter->KeepEvent(Evt_Run,Evt_Lumi,Evt_ID)==false){
      std::cout<<"skipping event "<<Evt_Run<<" "<<Evt_Lumi<<" "<<Evt_ID<<std::endl;
      continue;
      }
    

	// Do weighting correctly if data driven QCD sample is used: use the weights for MC part and not for Data part
	if(processname=="QCD" or processname=="QCD_CMS_ttH_QCDScaleFactorUp" or processname=="QCD_CMS_ttH_QCDScaleFactorDown") {
		if(currentfilename.Contains("SingleElectron")){
			DoWeights=0;
			electron_data=1;
			muon_data=0;
		} 
		else if(currentfilename.Contains("SingleMuon")) {
			DoWeights=0;
			muon_data=1;
			electron_data=0;
		}
		else {
			DoWeights=1;
			muon_data=0;
			electron_data=0;
		}
	}
  
  // DANGERZONE
  // Only Works for SL events at the moment
  // Lepton SFs 
     double muonPt=0.0;
     double muonEta=0.0;
     double electronEta=0.0;
     double electronPt=0.0;
    
    if(chain->GetBranch("Electron_Pt_BeforeRun2Calibration") && chain->GetBranch("Electron_Eta_Supercluster") && chain->GetBranch("Muon_Pt_BeForeRC")){
      //std::cout<<"using superclister and stuff"<<std::endl;
      if(N_TightMuons==1){muonPt=Muon_Pt_BeForeRC[0]; muonEta=Muon_Eta[0];}
      else{muonPt=0.0; muonEta=0.0;}
      if(N_TightElectrons==1){electronPt=Electron_Pt_BeforeRun2Calibration[0]; electronEta=Electron_Eta_Supercluster[0];}
      else{electronPt=0.0; electronEta=0.0;}
    }
    else{
      if(N_TightMuons==1){muonPt=Muon_Pt[0]; muonEta=Muon_Eta[0];}
      else{muonPt=0.0; muonEta=0.0;}
      if(N_TightElectrons==1){electronPt=Electron_Pt[0]; electronEta=Electron_Eta[0];}
      else{electronPt=0.0; electronEta=0.0;}
    }
    
    totalTimeGetEntry+=timerGetEntry->RealTime();
    timerCalculateSFs->Start();
    
    float internalEleTriggerWeight=1.0;
    float internalEleTriggerWeightUp=1.0;
    float internalEleTriggerWeightDown=1.0;
    float internalEleIDWeight=1.0;
    float internalEleIDWeightUp=1.0;
    float internalEleIDWeightDown=1.0;
    float internalEleIsoWeight=1.0;
    float internalEleIsoWeightUp=1.0;
    float internalEleIsoWeightDown=1.0;
    float internalEleGFSWeight=1.0;
    float internalEleGFSWeightUp=1.0;
    float internalEleGFSWeightDown=1.0;
    
    float internalMuTriggerWeight=1.0;
    float internalMuTriggerWeightUp=1.0;
    float internalMuTriggerWeightDown=1.0;
    float internalMuIDWeight=1.0;
    float internalMuIDWeightUp=1.0;
    float internalMuIDWeightDown=1.0;
    float internalMuIsoWeight=1.0;
    float internalMuIsoWeightUp=1.0;
    float internalMuIsoWeightDown=1.0;
    float internalMuHIPWeight=1.0;
    float internalMuHIPWeightUp=1.0;
    float internalMuHIPWeightDown=1.0;
   
    if(N_TightMuons==1){
      internalMuTriggerWeight=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,0,"Trigger");
      internalMuTriggerWeightUp=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,1,"Trigger");
      internalMuTriggerWeightDown=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,-1,"Trigger");
      
      internalMuIDWeight=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,0,"ID");
      internalMuIDWeightUp=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,1,"ID");
      internalMuIDWeightDown=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,-1,"ID");
      
      internalMuIsoWeight=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,0,"Iso");
      internalMuIsoWeightUp=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,1,"Iso");
      internalMuIsoWeightDown=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,-1,"Iso");
      
      internalMuHIPWeight=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,0,"HIP");
      internalMuHIPWeightUp=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,1,"HIP");
      internalMuHIPWeightDown=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,-1,"HIP");
    }
   
    if(N_TightElectrons==1){
      internalEleTriggerWeight=internalLeptonSFHelper->GetElectronSF(electronPt,electronEta,0,"Trigger");
      internalEleTriggerWeightUp=internalLeptonSFHelper->GetElectronSF(electronPt,electronEta,1,"Trigger");
      internalEleTriggerWeightDown=internalLeptonSFHelper->GetElectronSF(electronPt,electronEta,-1,"Trigger");
      
      internalEleIDWeight=internalLeptonSFHelper->GetElectronSF(electronPt,electronEta,0,"ID");
      internalEleIDWeightUp=internalLeptonSFHelper->GetElectronSF(electronPt,electronEta,1,"ID");
      internalEleIDWeightDown=internalLeptonSFHelper->GetElectronSF(electronPt,electronEta,-1,"ID");
      
      internalEleIsoWeight=internalLeptonSFHelper->GetElectronSF(electronPt,electronEta,0,"Iso");
      internalEleIsoWeightUp=internalLeptonSFHelper->GetElectronSF(electronPt,electronEta,1,"Iso");
      internalEleIsoWeightDown=internalLeptonSFHelper->GetElectronSF(electronPt,electronEta,-1,"Iso");
      
      internalEleGFSWeight=internalLeptonSFHelper->GetElectronSF(electronPt,electronEta,0,"GFS");
      internalEleGFSWeightUp=internalLeptonSFHelper->GetElectronSF(electronPt,electronEta,1,"GFS");
      internalEleGFSWeightDown=internalLeptonSFHelper->GetElectronSF(electronPt,electronEta,-1,"GFS");
    }
   
   
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
  
  double primlepPt;    
  double primlepEta;    
  double primlepPhi; 
  double primlepM;
  double primlepE; 
  
  primlepPt=Evt_Pt_PrimaryLepton;
  primlepE=Evt_E_PrimaryLepton;
  primlepPhi=Evt_Phi_PrimaryLepton;
  primlepEta=Evt_Eta_PrimaryLepton;
  primlepM=Evt_M_PrimaryLepton;
  
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
  
  float internalQCDweight = 0.0;
  float internalQCDweightup = 0.0;
  float internalQCDweightdown = 0.0;
  
  float internalPDFweight = 0.0;
  float internalPDFweightUp = 0.0;
  float internalPDFweightDown = 0.0;
  
  float internalISRweightup = 0.0;
  float internalISRweightdown = 0.0;
  float internalFSRweightup = 0.0;
  float internalFSRweightdown = 0.0;
  float internalHDAMPweightup = 0.0;
  float internalHDAMPweightdown = 0.0;
  float internalUEweightup = 0.0;
  float internalUEweightdown = 0.0;

  float internalBosonWeight_nominal = 1.0;
  float internalBosonWeight_QCD1Up = 1.0;
  float internalBosonWeight_QCD1Down = 1.0;
  float internalBosonWeight_QCD2Up = 1.0;
  float internalBosonWeight_QCD2Down = 1.0;
  float internalBosonWeight_QCD3Up = 1.0;
  float internalBosonWeight_QCD3Down = 1.0;
  float internalBosonWeight_EW1Up = 1.0;
  float internalBosonWeight_EW1Down = 1.0;
  float internalBosonWeight_EW2Up = 1.0;
  float internalBosonWeight_EW2Down = 1.0;
  float internalBosonWeight_EW3Up = 1.0;
  float internalBosonWeight_EW3Down = 1.0;
  float internalBosonWeight_MixedUp = 1.0;
  float internalBosonWeight_MixedDown = 1.0;
  float internalBosonWeight_AlphaUp = 1.0;
  float internalBosonWeight_AlphaDown = 1.0;
  float internalBosonWeight_muRUp = 1.0;
  float internalBosonWeight_muRDown = 1.0;
  float internalBosonWeight_muFUp = 1.0;
  float internalBosonWeight_muFDown = 1.0;


  double tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF;
  
  internalCSVweight=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,internalSystType,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF);
  internalCSVweight_CSVHFUp=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVHFup,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVHFDown=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVHFdown,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVLFUp=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVLFup,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVLFDown=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVLFdown,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  
  internalCSVweight_CSVLFStats1Up=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVLFStats1up,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVLFStats1Down=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVLFStats1down,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVLFStats2Up=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVLFStats2up,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVLFStats2Down=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVLFStats2down,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  
  internalCSVweight_CSVHFStats1Up=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVHFStats1up,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVHFStats1Down=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVHFStats1down,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVHFStats2Up=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVHFStats2up,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVHFStats2Down=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVHFStats2down,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  
  internalCSVweight_CSVCErr1Up=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVCErr1up,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVCErr1Down=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVCErr1down,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVCErr2Up=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVCErr2up,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVCErr2Down=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVCErr2down,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  
  internalQCDweight=internalQCDHelper->GetScaleFactor(N_Jets,N_BTagsM,N_TightElectrons,N_TightMuons);
  internalQCDweightup=internalQCDHelper->GetScaleFactorErrorUp(N_Jets,N_BTagsM,N_TightElectrons,N_TightMuons);
  internalQCDweightdown=internalQCDHelper->GetScaleFactorErrorDown(N_Jets,N_BTagsM,N_TightElectrons,N_TightMuons);
  
  if(processname.find("w_lnu_jets")!=std::string::npos){
  internalBosonWeight_nominal = internalBosonHelper->GetScaleFactorW(W_Pt, "nominal");
  internalBosonWeight_QCD1Up = internalBosonHelper->GetScaleFactorW(W_Pt, "QCD1Up"); 
  internalBosonWeight_QCD1Down = internalBosonHelper->GetScaleFactorW(W_Pt, "QCD1Down");
  internalBosonWeight_QCD2Up = internalBosonHelper->GetScaleFactorW(W_Pt, "QCD2Up"); 
  internalBosonWeight_QCD2Down = internalBosonHelper->GetScaleFactorW(W_Pt, "QCD2Down");
  internalBosonWeight_QCD3Up = internalBosonHelper->GetScaleFactorW(W_Pt, "QCD3Up");
  internalBosonWeight_QCD3Down = internalBosonHelper->GetScaleFactorW(W_Pt, "QCD3Down");

  internalBosonWeight_EW1Up = internalBosonHelper->GetScaleFactorW(W_Pt, "EW1Up");
  internalBosonWeight_EW1Down = internalBosonHelper->GetScaleFactorW(W_Pt, "EW1Down");
  internalBosonWeight_EW2Up = internalBosonHelper->GetScaleFactorW(W_Pt, "EW2Up");
  internalBosonWeight_EW2Down = internalBosonHelper->GetScaleFactorW(W_Pt, "EW2Down");
  internalBosonWeight_EW3Up = internalBosonHelper->GetScaleFactorW(W_Pt, "EW3Up"); 
  internalBosonWeight_EW3Down = internalBosonHelper->GetScaleFactorW(W_Pt, "EW3Down");

  internalBosonWeight_MixedUp = internalBosonHelper->GetScaleFactorW(W_Pt, "MixedUp");
  internalBosonWeight_MixedDown = internalBosonHelper->GetScaleFactorW(W_Pt, "MixedDown");
  
  internalBosonWeight_AlphaUp = internalBosonHelper->GetScaleFactorW(W_Pt, "AlphaUp");
  internalBosonWeight_AlphaDown = internalBosonHelper->GetScaleFactorW(W_Pt, "AlphaDown");
  
  internalBosonWeight_muRUp = internalBosonHelper->GetScaleFactorW(W_Pt, "muRUp");
  internalBosonWeight_muRDown = internalBosonHelper->GetScaleFactorW(W_Pt, "muRDown");
  
  internalBosonWeight_muFUp = internalBosonHelper->GetScaleFactorW(W_Pt, "muFUp");
  internalBosonWeight_muFDown = internalBosonHelper->GetScaleFactorW(W_Pt, "muFDown");
  }
  if(processname.find("z_nunu_jets")!=std::string::npos){
  internalBosonWeight_nominal = internalBosonHelper->GetScaleFactorZvv(Z_Pt, "nominal");
  internalBosonWeight_QCD1Up = internalBosonHelper->GetScaleFactorZvv(Z_Pt, "QCD1Up"); 
  internalBosonWeight_QCD1Down = internalBosonHelper->GetScaleFactorZvv(Z_Pt, "QCD1Down");
  internalBosonWeight_QCD2Up = internalBosonHelper->GetScaleFactorZvv(Z_Pt, "QCD2Up");
  internalBosonWeight_QCD2Down = internalBosonHelper->GetScaleFactorZvv(Z_Pt, "QCD2Down");
  internalBosonWeight_QCD3Up = internalBosonHelper->GetScaleFactorZvv(Z_Pt, "QCD3Up"); 
  internalBosonWeight_QCD3Down = internalBosonHelper->GetScaleFactorZvv(Z_Pt, "QCD3Down");

  internalBosonWeight_EW1Up = internalBosonHelper->GetScaleFactorZvv(Z_Pt, "EW1Up"); 
  internalBosonWeight_EW1Down = internalBosonHelper->GetScaleFactorZvv(Z_Pt, "EW1Down");
  internalBosonWeight_EW2Up = internalBosonHelper->GetScaleFactorZvv(Z_Pt, "EW2Up"); 
  internalBosonWeight_EW2Down = internalBosonHelper->GetScaleFactorZvv(Z_Pt, "EW2Down");
  internalBosonWeight_EW3Up = internalBosonHelper->GetScaleFactorZvv(Z_Pt, "EW3Up"); 
  internalBosonWeight_EW3Down = internalBosonHelper->GetScaleFactorZvv(Z_Pt, "EW3Down");

  internalBosonWeight_MixedUp = internalBosonHelper->GetScaleFactorZvv(Z_Pt, "MixedUp"); 
  internalBosonWeight_MixedDown = internalBosonHelper->GetScaleFactorZvv(Z_Pt, "MixedDown");
  
  internalBosonWeight_AlphaUp = internalBosonHelper->GetScaleFactorZvv(Z_Pt, "AlphaUp");
  internalBosonWeight_AlphaDown = internalBosonHelper->GetScaleFactorZvv(Z_Pt, "AlphaDown");
  
  internalBosonWeight_muRUp = internalBosonHelper->GetScaleFactorZvv(Z_Pt, "muRUp");
  internalBosonWeight_muRDown = internalBosonHelper->GetScaleFactorZvv(Z_Pt, "muRDown");
  
  internalBosonWeight_muFUp = internalBosonHelper->GetScaleFactorZvv(Z_Pt, "muFUp");
  internalBosonWeight_muFDown = internalBosonHelper->GetScaleFactorZvv(Z_Pt, "muFDown");
  }
  if(processname.find("z_ll_jets")!=std::string::npos){
  internalBosonWeight_nominal = internalBosonHelper->GetScaleFactorZll(Z_Pt, "nominal");
  internalBosonWeight_QCD1Up = internalBosonHelper->GetScaleFactorZll(Z_Pt, "QCD1Up"); 
  internalBosonWeight_QCD1Down = internalBosonHelper->GetScaleFactorZll(Z_Pt, "QCD1Down");
  internalBosonWeight_QCD2Up = internalBosonHelper->GetScaleFactorZll(Z_Pt, "QCD2Up");
  internalBosonWeight_QCD2Down = internalBosonHelper->GetScaleFactorZll(Z_Pt, "QCD2Down");
  internalBosonWeight_QCD3Up = internalBosonHelper->GetScaleFactorZll(Z_Pt, "QCD3Up"); 
  internalBosonWeight_QCD3Down = internalBosonHelper->GetScaleFactorZll(Z_Pt, "QCD3Down");

  internalBosonWeight_EW1Up = internalBosonHelper->GetScaleFactorZll(Z_Pt, "EW1Up"); 
  internalBosonWeight_EW1Down = internalBosonHelper->GetScaleFactorZll(Z_Pt, "EW1Down");
  internalBosonWeight_EW2Up = internalBosonHelper->GetScaleFactorZll(Z_Pt, "EW2Up"); 
  internalBosonWeight_EW2Down = internalBosonHelper->GetScaleFactorZll(Z_Pt, "EW2Down");
  internalBosonWeight_EW3Up = internalBosonHelper->GetScaleFactorZll(Z_Pt, "EW3Up"); 
  internalBosonWeight_EW3Down = internalBosonHelper->GetScaleFactorZll(Z_Pt, "EW3Down");

  internalBosonWeight_MixedUp = internalBosonHelper->GetScaleFactorZll(Z_Pt, "MixedUp"); 
  internalBosonWeight_MixedDown = internalBosonHelper->GetScaleFactorZll(Z_Pt, "MixedDown");
  
  internalBosonWeight_AlphaUp = internalBosonHelper->GetScaleFactorZll(Z_Pt, "AlphaUp");
  internalBosonWeight_AlphaDown = internalBosonHelper->GetScaleFactorZll(Z_Pt, "AlphaDown");
  
  internalBosonWeight_muRUp = internalBosonHelper->GetScaleFactorZll(Z_Pt, "muRUp");
  internalBosonWeight_muRDown = internalBosonHelper->GetScaleFactorZll(Z_Pt, "muRDown");
  
  internalBosonWeight_muFUp = internalBosonHelper->GetScaleFactorZll(Z_Pt, "muFUp");
  internalBosonWeight_muFDown = internalBosonHelper->GetScaleFactorZll(Z_Pt, "muFDown");
  }
  
  
  totalTimeCalculateSFs+=timerCalculateSFs->RealTime();

 
  // print stuff for synchronizing
  bool printSyncStuff=0;
  //
  if(printSyncStuff){
    std::cout<<"event "<<Evt_ID<<std::endl;
    std::cout<<"n Jets "<<N_Jets<<std::endl;
    std::cout<<"m BTags "<<N_BTagsM<<std::endl;
    
    std::cout<<"XS weight "<<Weight_XS<<std::endl;
    std::cout<<"PU weight "<<Weight_pu69p2<<std::endl;
    std::cout<<"ele ID weight (both) "<<internalEleIDWeight<<std::endl;
    std::cout<<"ele Reco weight (both) "<<internalEleGFSWeight<<std::endl;
    std::cout<<"ele trigger weight "<<internalEleTriggerWeight<<std::endl;
    std::cout<<"mu ID weight (both) "<<internalMuIDWeight<<std::endl;
    std::cout<<"mu Tracking weight (both) "<<internalMuHIPWeight<<std::endl;
    std::cout<<"mu ISO weight (both) "<<internalMuIsoWeight<<std::endl;
    std::cout<<"mu trigger weight "<<internalMuTriggerWeight<<std::endl;
    std::cout<<"CSV weight "<<internalCSVweight<<std::endl;
 }   
 
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

# DEPRECATED: can be removed in the future
def fillHisto(histo,var,weight):
  text= '        if(('+weight+')!=0)\n'
  text+='          h_'+histo+'->Fill(fmin(h_'+histo+'->GetXaxis()->GetXmax()-1e-6,fmax(h_'+histo+'->GetXaxis()->GetXmin()+1e-6,'+var+')),'+weight+');\n'
  return text

# DEPRECATED: can be removed in the future
def fillTwoDimHisto(histo,var1,var2,weight):
  text= '        if(('+weight+')!=0)\n'
  text+='          h_'+histo+'->Fill(fmin(h_'+histo+'->GetXaxis()->GetXmax()-1e-6,fmax(h_'+histo+'->GetXaxis()->GetXmin()+1e-6,'+var1+')),fmin(h_'+histo+'->GetYaxis()->GetXmax()-1e-6,fmax(h_'+histo+'->GetYaxis()->GetXmin()+1e-6,'+var2+')),'+weight+');\n'
  return text


def endLoop():
  return """
  }\n // end of event loop
  totalTime+=timerTotal->RealTime();
  std::cout<<"skipped a total of "<<evtFilter->GetNFiltered()<<std::endl;
"""


def varLoop(i,n):
  return '      for(uint '+str(i)+'=0; '+str(i)+'<'+str(n)+'; '+str(i)+'++)'


def getFoot(addCodeInterfaces):
  rstr= """
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
"""
  
  for addCodeInt in addCodeInterfaces:
    rstr+=addCodeInt.getCleanUpLines()


  rstr+="""
  
  std::cout<<"time getting event: "<<totalTimeGetEntry<<std::endl;
  std::cout<<"time calculating SFs: "<<totalTimeCalculateSFs<<std::endl;
  std::cout<<"time reading DBs: "<<totalTimeReadDataBase<<std::endl;
  std::cout<<"time Eval DNN: "<<totalTimeEvalDNN<<std::endl;
  std::cout<<"time Eval weights and BDTs: "<<totalTimeEvalWeightsAndBDT<<std::endl;
  std::cout<<"time for sampel weight: "<<totalTimeSampleWeight<<std::endl;
  std::cout<<"time filling histos: "<<totalTimeFillHistograms<<std::endl;
  std::cout<<"time mapping values: "<<totalTimeMapping<<std::endl;
  std::cout<<"time spent in event loop: "<<totalTime<<std::endl;

  
}

int main(){
  plot();
}
"""
  return rstr

def compileProgram(scriptname,usesDataBases,addCodeInterfaces):
  p = subprocess.Popen(['root-config', '--cflags', '--libs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  out, err = p.communicate()
  dnnfiles=[]
  for addCodeInt in addCodeInterfaces:
    if addCodeInt.usesPythonLibraries:
      ppyc = subprocess.Popen(['python-config', '--cflags'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      outpyc, errpyc = ppyc.communicate()
      ppyl = subprocess.Popen(['python-config', '--ldflags'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      outpyl, errpyl = ppyl.communicate()
      print "communicated"
      # get library path for python
      print outpyc
      pythonincludepath=outpyc.split(" ")[0]
      pythonlibrarypath=pythonincludepath.replace("-I","-L").replace("include/python2.7","lib")
      dnnfiles=outpyc[:-1].replace("\n"," ").split(' ')+[pythonlibrarypath]+outpyl[:-1].replace("\n"," ").split(' ')
      break
    
  for addCodeInt in addCodeInterfaces:
    if addCodeInt.includeString!="":
      dnnfiles+=addCodeInt.includeString.split(" ")
    if addCodeInt.libraryString!="":
      dnnfiles+=addCodeInt.libraryString.split(" ")
      
  print dnnfiles
  
  lhapdf=[' `/cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/lhapdf/6.1.6-ikhhed2/bin/lhapdf-config --cflags --ldflags`']
  
  memDBccfiles=[]
  if usesDataBases:
    memDBccfiles=glob.glob('/nfs/dust/cms/user/kelmorab/DataBaseCodeForScriptGenerator/MEMDataBaseSpring17/MEMDataBase/MEMDataBase/src/*.cc') 
    #TODO update the dataBases code
  # improve ram usage and reduce garbage of g++ compiler
  improveRAM = '--param ggc-min-expand=100 --param ggc-min-heapsize=2400000'
  # if python cflags are used -O3 optimization is set, resulting in long compilation times, set it back to default -O0
  resetCompilerOpt = '-O0'
  cmd= ['g++']+[improveRAM]+out[:-1].replace("\n"," ").split(' ')+dnnfiles+lhapdf+['-lTMVA']+memDBccfiles+[resetCompilerOpt]+[scriptname+'.cc','-o',scriptname]
  print cmd
  print ""
  cmdstring = " ".join(cmd)
  print cmdstring
  print ""
  compileOutFile=open(scriptname+'_gccCommand.txt',"w")
  compileOutFile.write(cmdstring+"\n")
  compileOutFile.close()
  try:
    print subprocess.check_output([cmdstring],stderr=subprocess.STDOUT,shell=True)
  except subprocess.CalledProcessError, e:
    print "Compile command:\n", e.cmd
    print "Compile failed with error:\n", e.output


def createProgram(scriptname,plots,samples,catnames=[""],catselections=["1"],systnames=[""],allsystweights=["1"],additionalvariables=[],dataBases=[],addCodeInterfaces=[]):

  # collect variables
  # list varibles that should not be written to the program automatically

  vetolist=['processname','DoWeights','TMath','electronPt','electronEta','muonPt','muonEta','muonTriggerHelper','electronTriggerHelper','hasTrigger','internalCSVweight','internalCSVweight_CSVHFUp','internalCSVweight_CSVHFDown','internalCSVweight_CSVLFUp','internalCSVweight_CSVLFDown','internalCSVweight_CSVLFStats1Up','internalCSVweight_CSVLFStats1Down','internalCSVweight_CSVLFStats2Up','internalCSVweight_CSVLFStats2Down','internalCSVweight_CSVHFStats1Up','internalCSVweight_CSVHFStats1Down','internalCSVweight_CSVHFStats2Up','internalCSVweight_CSVHFStats2Down','internalCSVweight_CSVCErr1Up','internalCSVweight_CSVCErr1Down','internalCSVweight_CSVCErr2Up','internalCSVweight_CSVCErr2Down',
	    "internalEleTriggerWeight","internalEleTriggerWeightUp","internalEleTriggerWeightDown",
	    "internalEleIDWeight","internalEleIDWeightUp","internalEleIDWeightDown",
	    "internalEleIsoWeight","internalEleIsoWeightUp","internalEleIsoWeightDown",
	    "internalEleGFSWeight","internalEleGFSWeightUp","internalEleGFSWeightDown",
	    "internalMuTriggerWeight","internalMuTriggerWeightUp","internalMuTriggerWeightDown",
	    "internalMuIDWeight","internalMuIDWeightUp","internalMuIDWeightDown",
	    "internalMuIsoWeight","internalMuIsoWeightUp","internalMuIsoWeightDown",
	    "internalMuHIPWeight","internalMuHIPWeightUp","internalMuHIPWeightDown",
	    "internalQCDweight","internalQCDweightup","internalQCDweightdown",
	    "electron_data","muon_data",
	    "internalPDFweightUp","internalPDFweightDown","internalPDFweight",
	    "internalISRweightdown","internalISRweightup","internalFSRweightdown","internalFSRweightup",
      "internalHDAMPweightdown","internalHDAMPweightup","internalUEweightdown","internalUEweightup",

      "internalBosonWeight_nominal",
      "internalBosonWeight_QCD1Up","internalBosonWeight_QCD1Down",
      "internalBosonWeight_QCD2Up","internalBosonWeight_QCD2Down",
      "internalBosonWeight_QCD3Up","internalBosonWeight_QCD3Down",
      "internalBosonWeight_EW1Up","internalBosonWeight_EW1Down",
      "internalBosonWeight_EW2Up","internalBosonWeight_EW2Down",
      "internalBosonWeight_EW3Up","internalBosonWeight_EW3Down",
      "internalBosonWeight_MixedUp","internalBosonWeight_MixedDown",

      "DoWbosonReweighting",
      "DoZbosonReweighting",
]

  #csv_file=os.getcwd()+"/rate_factors_onlyinternal_powhegpythia.csv"
  csv_file="/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/rate_factors_onlyinternal_powhegpythia.csv"

  vetolist+=GetMEPDFVetoList(csv_file)

  for addCodeInt in addCodeInterfaces:
    vetolist+=addCodeInt.getExternalyCallableVariables()
    
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
  #print variables
  
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
    #print additionalvariables
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
  script+=getHead(dataBases,addCodeInterfaces)
  #script+=DeclareMEPDFNormFactors(csv_file)
  #script+=AddMEandPDFNormalizationsMap(csv_file)
  
  for db in dataBases:
    script+=InitDataBase(db)
  for addCodeInt in addCodeInterfaces:
    script+=addCodeInt.getBeforeLoopLines()
    
  # initialize all variables
  initStub, castStub=variables.initVarsProgram()
  #print initStub
  #print castStub
  script+=initStub
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
  script+=DefineLHAPDF()
  startLoopStub=startLoop()
  if castStub!="":
    #print castStub
    startLoopStub=startLoopStub.replace("//PLACEHOLDERFORCASTLINES", castStub)
  script+=startLoopStub
  script+="   timerMapping->Start();\n"
  #script+=ResetMEPDFNormFactors(csv_file)
  #script+=RelateMEPDFMapToNormFactor(csv_file)
  script+=PutPDFWeightsinVector(csv_file)
  script+=UseLHAPDF()
  script+="   totalTimeMapping+=timerMapping->RealTime();\n"

  script+="   timerEvalDNN->Start();\n"
  for addCodeInt in addCodeInterfaces:
    script+=addCodeInt.getVariableInitInsideEventLoopLines()
  script+="   totalTimeEvalDNN+=timerEvalDNN->RealTime();\n"

  script+="   timerSampleWeight->Start();\n"
  script+='    float sampleweight=1;\n'
  script+=encodeSampleSelection(samples,variables)
  script+="   totalTimeSampleWeight+=timerSampleWeight->RealTime();\n"
  
  script+="   timerReadDataBase->Start();\n"
  for db in dataBases:
    script+=readOutDataBase(db)  
  script+="\n"
  script+="   totalTimeReadDataBase+=timerReadDataBase->RealTime();\n"
  
  script+="   timerEvalDNN->Start();\n"
  for addCodeInt in addCodeInterfaces:
    script+=addCodeInt.getEventLoopCodeLines()
    script+="\n"
  script+="   totalTimeEvalDNN+=timerEvalDNN->RealTime();\n"

  script+="   timerEvalWeightsAndBDT->Start();\n"
  # calculate varibles and get TMVA outputs
  script+=variables.calculateVarsProgram()
  script+="   totalTimeEvalWeightsAndBDT+=timerEvalWeightsAndBDT->RealTime();\n"
  
  script+="   timerFillHistograms->Start();\n"
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
        # Handle vector sub variables which have names like Jet_E_1, so that the variable Jet_E[1] is included instead
        if not ".xml" in ex and not hasattr(tree,ex):
          if "_" in ex:
            exOld = ex
            expressionPart1, expressionPart2 = ex.rsplit('_', 1)
            if hasattr(tree, expressionPart1) and expressionPart2.isdigit():
              ex = expressionPart1 + '[' + str(int(expressionPart2) -1) + ']' 
              print 'Found vector sub variable: ', exOld, ' which was converted to: ', ex
        
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
  script+="   totalTimeFillHistograms+=timerFillHistograms->RealTime();\n"
  # finish loop
  script+=endLoop()
  
  for addCodeInt in addCodeInterfaces:
    script+="\n"
    script+=addCodeInt.getTestCallLines()
    script+="\n"
  
  # get program footer
  script+=getFoot(addCodeInterfaces)

  # write program text to file
  f=open(scriptname+'.cc','w')
  f.write(script)
  f.close()

def DrawParallel(ListOfPlots,name,PathToSelf,opts=None):
    ListofScripts=[]
    workdir=os.getcwd()+'/workdir/'+name+'/DrawScripts/'
    # create output folders
    print 'creating output folders'
    scriptsfolder=workdir
    if not os.path.exists(scriptsfolder):
      os.makedirs(scriptsfolder)

    print "Creating Scripts for Parallel Drawing"
    for iPlot, Plot in enumerate(ListOfPlots):
        ListofScripts.append(createSingleDrawScript(iPlot,Plot,PathToSelf,scriptsfolder,opts=None))

    print "Submitting ", len(ListofScripts), " DrawScripts"
    # print ListofScripts
    # jobids=submitToNAF(["DrawScripts/DrawParallel0.sh"])
    #jobids=submitToNAF(ListofScripts)
    jobids=submitArrayToNAF(ListofScripts,"DrawPara")
    print jobids
    do_qstat(jobids)


def createSingleDrawScript(iPlot,Plot,PathToSelf,scriptsfolder,opts=None):
  # print "still needs to be implemented"
  cmsswpath=os.environ['CMSSW_BASE']
  script="#!/bin/bash \n"
  if cmsswpath!='':
    script+="export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch \n"
    script+="source $VO_CMS_SW_DIR/cmsset_default.sh \n"
    script+="export SCRAM_ARCH="+os.environ['SCRAM_ARCH']+"\n"
    script+='export OUTFILENAME="'+"plot" +str(iPlot)+'"\n'
    script+='cd '+cmsswpath+'/src\neval `scram runtime -sh`\n'
    script+='cd - \n'
  # Parse commandline options if available to script  
  commandLineOptions = ''
  if opts != None:
    for opt, arg in opts:
      if arg != None:
        commandLineOptions = commandLineOptions + ' ' + opt + '=' + arg
      else:
        commandLineOptions = commandLineOptions + ' ' + opt
  script+='python '+PathToSelf+" -p "+str(iPlot)+ ' ' + commandLineOptions + ' noPlotParallel\n'
  # script+="mv *.pdf " +os.getcwd()+"/plot"+str(iPlot)+".pdf\n"


  scriptname=scriptsfolder+'DrawParallel'+str(iPlot)+'.sh'

  # path = os.getcwd()+"/DrawScripts" 
  # if not os.path.exists(path):
  #   os.makedirs(path)
  # os.chdir(path)
  
  f=open(scriptname,'w')
  f.write(script)
  f.close()
  st = os.stat(scriptname)
  os.chmod(scriptname, st.st_mode | stat.S_IEXEC)
  os.chdir(os.path.dirname(PathToSelf))

  # PathToShellScript=path+scriptname
  # return PathToShellScript
  # return "DrawScripts/"+scriptname
  return scriptname


def createScript(scriptname,programpath,processname,filenames,outfilename,maxevents,skipevents,cmsswpath,suffix,cirun=False,filterFile="NONE"):
  if cirun:
    if maxevents<100:
      maxevents=100
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
  script+='export EVENTFILTERFILE="'+str(filterFile)+'"\n'  
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

def get_scripts_outputs_and_nentries(samples,maxevents,scriptsfolder,plotspath,programpath,cmsswpath,treejsonfile="",cirun=False):
  scripts=[]
  outputs=[]
  samplewiseoutputs={}
  nentries=[]
  SaveTreeInforamtion={}
  LoadedTreeInformation={}
  if treejsonfile!="":
    print "Loading file with tree event information"
    with open(treejsonfile,"r") as jsonfile:
      jsonstring=list(jsonfile)[0]
      LoadedTreeInformation=json.loads(jsonstring)
  for s in samples:
    print 'creating scripts for',s.name,'from',s.path
    samplewiseoutputs[s.nick]=[]
    ntotal_events=0
    njob=0
    events_in_files=0
    filterFile=s.filterFile
    files_to_submit=[]
    for fn in s.files:
      events_in_file=0
      if LoadedTreeInformation!={} and fn in LoadedTreeInformation:
	#print "using tree event information"
	events_in_file=LoadedTreeInformation[fn]
      else:
	#print "did not find this sample in the json file yet"
	#print "will add it"
        f=ROOT.TFile(fn)
        t=f.Get('MVATree')
        try:
            events_in_file=t.GetEntries()
        except:
            events_in_file=0
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
          createScript(scriptname,programpath,processname,filenames,outfilename,maxevents,skipevents,cmsswpath,'',cirun,filterFile)
          scripts.append(scriptname)
          outputs.append(outfilename)
          samplewiseoutputs[s.nick].append(outfilename)
          nentries.append(events_in_file)
          ntotal_events+=events_in_file

      # else additional files are appended to list of files to be submitted
      else :
        files_to_submit+=[fn]
        events_in_files+=events_in_file
        if events_in_files>maxevents or fn==s.files[-1] or len(files_to_submit)>400: #avoid too long argument list wiht the last or. I hope
          njob+=1
          skipevents=0
          scriptname=scriptsfolder+'/'+s.nick+'_'+str(njob)+'.sh'
          processname=s.nick
          filenames=' '.join(files_to_submit)
          outfilename=plotspath+s.nick+'_'+str(njob)+'.root'
          createScript(scriptname,programpath,processname,filenames,outfilename,events_in_files,skipevents,cmsswpath,'',cirun,filterFile)
          scripts.append(scriptname)
          outputs.append(outfilename)
          samplewiseoutputs[s.nick].append(outfilename)
          nentries.append(events_in_files)
          ntotal_events+=events_in_files
          files_to_submit=[]
          events_in_files=0
          
      # If cirun = true, only use small number of files       
      if cirun: 
        break

    # submit remaining scripts (can happen if the last file was large)
    if len(files_to_submit)>0:
      njob+=1
      skipevents=0
      scriptname=scriptsfolder+'/'+s.nick+'_'+str(njob)+'.sh'
      processname=s.nick
      filenames=' '.join(files_to_submit)
      outfilename=plotspath+s.nick+'_'+str(njob)+'.root'
      createScript(scriptname,programpath,processname,filenames,outfilename,events_in_files,skipevents,cmsswpath,'',cirun,filterFile)
      scripts.append(scriptname)
      outputs.append(outfilename)
      samplewiseoutputs[s.nick].append(outfilename)
      nentries.append(events_in_files)
      ntotal_events+=events_in_files
      files_to_submit=[]
      events_in_files=0

    print ntotal_events,'events found in',s.name
    if ntotal_events==0:
        print "skipping sample ",s.name
        continue
  
  # save tree information to json file
    treejson=json.dumps(SaveTreeInforamtion)
    jsonfile=open(scriptsfolder+'/'+"treejson.json","w")
    jsonfile.write(treejson)
    jsonfile.close()
    print "Saved information about events in trees to ", scriptsfolder+'/'+"treejson.json"
  return scripts,outputs,nentries,samplewiseoutputs

# the dataBases should be defined as follows e.g. [[memDB,path],[blrDB,path]]
def plotParallel(name,maxevents,plots,samples,catnames=[""],catselections=["1"],systnames=[""],systweights=["1"],additionalvariables=[],dataBases=[],treeInformationJsonFile="",otherSystnames=[],addCodeInterfacePaths=[],cirun=False,StopAfterCompileStep=False,haddParallel=False):
  cmsswpath=os.environ['CMSSW_BASE']
  if not "CMSSW" in cmsswpath:
    print "you need CMSSW for this to work. Exiting!"
    exit(0)
  cmsswversion=os.environ['CMSSW_VERSION']
  splitcmsswversion=cmsswversion.split("_")
  #if doAachenDNN and not int(splitcmsswversion[1])>=8:
    #print "You need at least CMSSW 8_0_26_patch2 for the DNNs from Aachen. Exiting!"
    #exit(0)
  #if doAachenDNN:
    #commonclassifierexists=os.path.exists(cmsswpath+"/src/TTH/CommonClassifier")
    #if not commonclassifierexists:
      #print "You need the common classifier package with the dnns and tf installed. Exiting!"
      #exit(0)
  workdir=os.getcwd()+'/workdir/'+name
  outputpath=workdir+'/output.root'

  addCodeInterfaces=[]

  codeInterfaceCounter = 0
  for acp in addCodeInterfacePaths:
    codeInterfaceCounter += 1
    if isinstance(acp, basestring):
        addModuleName = "addModule" + str(codeInterfaceCounter)
        print "loading module", acp, "as ", addModuleName, " module."
        addCodeInterfaces.append(imp.load_source(addModuleName,acp).theInterface())
    elif isinstance(acp, types.InstanceType):
        print "appending class object initiated by user: ", acp
        addCodeInterfaces.append(acp)
    else:
        print "Unknown additional code interface type: ", acp

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
      if haddParallel==True:
        allthefiles=glob.glob(workdir+"/HaddOutputs/*.root")
        allfilteredfiles=[]
        for f in allthefiles:
          if not "_renamed_" in f:
            allfilteredfiles.append(f)
        oldoutput=outputpath
        outputpath=[oldoutput]+allfilteredfiles
        return outputpath
      else:
        return outputpath
    workdirold=workdir+datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    os.rename(workdir,workdirold)
    os.makedirs(workdir)
    cmd='cp -v '+workdirold+'/'+name+'.cc'+' '+workdir+'/'+name+'.cc'
    subprocess.call(cmd,shell=True)
    cmd='cp -v '+workdirold+'/'+name+''+' '+workdir+'/'+name+'Backup'
    subprocess.call(cmd,shell=True)

  if not os.path.exists(workdir):
    os.makedirs(workdir)

  cmsswpath=os.environ['CMSSW_BASE']
  programpath=workdir+'/'+name

  # create c++ program
  # check if the program already exists
  alreadyWritten=os.path.exists(programpath+'.cc')
  print os.path.exists(programpath+'.cc')
  if alreadyWritten:
    print "a c++ program was written previously. Will check if this needs to be updated"
    cmd='cp -v '+programpath+'.cc'+' '+programpath+'.ccBackup'
    subprocess.call(cmd,shell=True)
  print 'creating c++ program'
  createProgram(programpath,plots,samples,catnames,catselections,systnames,systweights,additionalvariables, dataBases,addCodeInterfaces)
  if not os.path.exists(programpath+'.cc'):
    print 'could not create c++ program'
    sys.exit(-1)
  # check if the code changed
  codeWasChanged=True
  if alreadyWritten:
    print "comparing c++ code"
    print programpath+'.ccBackup' ," vs ", programpath+'.cc'
    codeWasChanged=not filecmp.cmp(programpath+'.ccBackup',programpath+'.cc')
  if codeWasChanged:
    print "c++ codes differ"
    print 'compiling c++ program'
    compileProgram(programpath, usesDataBases,addCodeInterfaces)
  else:
    print 'c++ program already existing !!!! Check if this is reasonable!!!'
    cmd = 'cp -v '+programpath+'Backup'+' '+programpath
    subprocess.call(cmd,shell=True)
  if not os.path.exists(programpath):
    print 'could not compile c++ program'
    sys.exit(-1)
    
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
    sys.exit(-1)

  # create run scripts
  print 'creating run scripts'
  scripts,outputs,nentries,samplewiseoutputs=get_scripts_outputs_and_nentries(samples,maxevents,scriptsfolder,plotspath,programpath,cmsswpath,treeInformationJsonFile,cirun)
  #DANGERZONE Submit jobs
  if StopAfterCompileStep==True:
    exit(0)
  helperSubmitNAFJobs(scripts,outputs,nentries)
  #raw_input()
  #raw_input()


  # hadd outputs
  # Check if hadd output worked, otherwise resubmit jobs a second time
  haddResubmit = False
  print 'hadd output starting'
  haddclock=ROOT.TStopwatch()
  haddclock.Start()
  if haddParallel==False:
    try:
      subprocess.check_output(['hadd -f', outputpath]+outputs,stderr=subprocess.STDOUT)
      print 'hadd output worked ', ('in the first place.' if not haddResubmit else 'in the second place.')
    except subprocess.CalledProcessError, e:
      if not haddResubmit:
          print 'Hadd failed with the following error in the first place:\n \n', e.output
          print '\n Resubmitting job script and then redoing hadd a second time.'
          haddResubmit = True
          helperSubmitNAFJobs(scripts,outputs,nentries)
          subprocess.check_output(['hadd -f', outputpath]+outputs,stderr=subprocess.STDOUT)
      else:
          print "Hadd failed a second time with the following error, stopping program: \n \n", e.output
          sys.exit(-1)
  
  else:
    resultingfiles=doParaHadding(name,samplewiseoutputs)
    oldoutput=outputpath
    outputpath=[oldoutput]+resultingfiles
  haddtime=haddclock.RealTime()
  print "hadding took ", haddtime
  return  outputpath


def doParaHadding(name,inmap={}):
  script= """
import ROOT
import sys
import os
import subprocess 
outfname=sys.argv[1]
outlogname=sys.argv[2]
infiles=sys.argv[3:]
cmd='hadd -f '+outfname+' '+' '.join(infiles)
worked=False
try:
    subprocess.check_output(cmd,shell=True,stderr=subprocess.STDOUT)
    worked=True
except subprocess.CalledProcessError, e:
    worked=False

outlog=open(outlogname,"w")
if worked==True:
  outlog.write("OK")
else:
  outlog.write("ERROR")
outlog.close()
"""
  scriptfilename=os.getcwd()+'/workdir/'+name+'/haddScript.py'
  scriptfile=open(scriptfilename,"w")
  scriptfile.write(script)
  scriptfile.close()

  listOfOutScripts=[]
  listOfOutFiles=[]
  
  scriptfolder=os.getcwd()+'/workdir/'+name+'/HaddScripts/'
  outputfolder=os.getcwd()+'/workdir/'+name+'/HaddOutputs/'
  if not os.path.exists(scriptfolder):
    os.makedirs(scriptfolder)
  if not os.path.exists(outputfolder):
    os.makedirs(outputfolder)
  cmsswpath=os.environ['CMSSW_BASE']
  if not "CMSSW" in cmsswpath:
    print "you need CMSSW for this to work. Exiting!"
    exit(0)
  for sample in inmap:
    print sample
    scriptname=scriptfolder+'haddscript_'+sample+'.sh'
    script="#!/bin/bash \n"
    if cmsswpath!='':
      script+="export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch \n"
      script+="source $VO_CMS_SW_DIR/cmsset_default.sh \n"
      script+="export SCRAM_ARCH="+os.environ['SCRAM_ARCH']+"\n"
      script+='cd '+cmsswpath+'/src\neval `scram runtime -sh`\n'
      script+='cd - \n'
    script+='python '+scriptfilename+' '+outputfolder+'/'+sample+'_hadded.root'+' '+outputfolder+'/'+sample+'_hadded.log'+' '+' '.join(inmap[sample])+'\n'
    f=open(scriptname,'w')
    f.write(script)
    f.close()
    st = os.stat(scriptname)
    os.chmod(scriptname, st.st_mode | stat.S_IEXEC)
    listOfOutFiles.append(outputfolder+'/'+sample+'_hadded.root')
    listOfOutScripts.append(scriptname)
  
  firstTry=True
  listOfJobsToSubmit=listOfOutScripts
  listOfJobOutFilesToGetFromSubmit=listOfOutFiles
  nJobsDone=0
  nTries=0
  while len(listOfJobsToSubmit)>0 or len(listOfJobOutFilesToGetFromSubmit)>0 or nJobsDone!=len(listOfOutFiles):
    nTries+=1
    if nTries>=4:
      print "hadding did not work after 4 tries. ABORTING"
      exit(1)
    if firstTry:
      jobids=submitArrayToNAF(listOfJobsToSubmit, "haddPara")
      do_qstat(jobids)
      firstTry=False      
    else:
      jobids=submitToNAF(listOfJobsToSubmit)
      do_qstat(jobids)
    # check if each hadd worked
    listOfJobsToSubmit=[]
    listOfJobOutFilesToGetFromSubmit=[]
    nJobsDone=0
    for j, js in  zip(listOfOutFiles,listOfOutScripts):
      isOk=True
      if os.path.exists(j):
        jf=open(j.replace(".root",".log"),"r")
        jflist=list(jf)
        jf.close()
        if len(jflist)==1:
          if jflist[0]!="OK":
            isOk=False
        else:
          isOk=False
      else:
        isOk=False
      if isOk:
        nJobsDone+=1
      else:
        listOfJobsToSubmit.append(js)
        listOfJobOutFilesToGetFromSubmit.append(j)
  return listOfOutFiles

def haddFilesFromWildCard(outname="",inwildcard="",totalNumberOfHistosNeedsToRemainTheSame=False):
  infiles=glob.glob(inwildcard)
  print 'hadd from wildcard'
  print outname, inwildcard
  haddclock=ROOT.TStopwatch()
  haddclock.Start()
  nfilesPerHadd=100
  nHistosBefore=0
  nHistosAfter=0
  if totalNumberOfHistosNeedsToRemainTheSame:
    # count number if histos before hadding
    print "counting histos BEFORE hadding from wildcard"
    nHistos=0
    for inf in infiles:
      theInf=ROOT.TFile(inf,"READ")
      keylist=theInf.GetListOfKeys()
      nHistos+=len(keylist)
      theInf.Close()
    nHistosBefore=nHistos  
  if len(infiles)<nfilesPerHadd:
    cmd='hadd -f'+' '+outname+' '+' '.join(infiles)
    print cmd
    subprocess.call(cmd,shell=True)
  else:
    parts=[]
    subpartfiles=[]
    totalsubpartfiles=[]
    for iinf, inf in enumerate(infiles):
      subpartfiles.append(inf)
      totalsubpartfiles.append(inf)
      if iinf%(nfilesPerHadd-1)==0 or inf==infiles[-1]:
        partname=outname.replace(".root","_part_"+str(len(parts))+".root")
        parts.append(partname)
        cmd='hadd -f'+' '+partname+' '+' '.join(subpartfiles)
        print cmd
        subprocess.call(cmd,shell=True)
        subpartfiles=[]
    if len(totalsubpartfiles)!=len(infiles):
      print "OHOHOH HADDINGFROMWILDCARD missed or used some files twice!!!"
      exit(1)
    # now add the parts
    cmd='hadd -f'+' '+outname+' '+' '.join(parts)
    print cmd
    subprocess.call(cmd,shell=True)
  
  if totalNumberOfHistosNeedsToRemainTheSame:
    # count number if histos before hadding
    print "counting histos AFTER hadding from wildcard"
    nHistos=0
    for inf in [outname]:
      theInf=ROOT.TFile(inf,"READ")
      keylist=theInf.GetListOfKeys()
      nHistos+=len(keylist)
      theInf.Close()
    nHistosAfter=nHistos
    if nHistosAfter!=nHistosBefore:
      print "haddFilesFromWildCard did not lead to the same number of histograms before and after the hadding!!!!"
      exit(1)
  print 'done'
  haddtime=haddclock.RealTime()
  print "hadding took ", haddtime
  return  outname

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

    if "dummy" in thisname:
      continue
    nsysts=0
    for sys in sysnames:
      if sys in newname:
	newname=newname.replace(sys,"")
	newname+=sys
	nsysts+=1
	
    if "JES" in thisname or "JER" in thisname or "_ttH_scaleFSR" in thisname or "_ttH_scaleISR" in thisname or "_ttH_FSR" in thisname or "_ttH_ISR" in thisname or "_ttH_hdamp" in thisname or "ttH_ue" in thisname or "_ttHbb_scaleFSR" in thisname or "_ttHbb_scaleISR" in thisname or "_ttHbb_FSR" in thisname or "_ttHbb_ISR" in thisname or "_ttHbb_HDAMP" in thisname or "ttHbb_UE" in thisname or (("CMS_scale" in thisname or "CMS_res_" in thisname) and ("_jUp" in thisname or "_jDown" in thisname)) or "_CMS_ttH_QCDScaleFactor" in thisname or "_CMS_ttHbbFROMTREES" in thisname:
      if nsysts>2:
        thish=outfile.Get(thisname)
        theobjectlist.append(thish)
	print nsysts, " systs: removing ", thisname
	outfile.Delete(thisname)
	outfile.Delete(thisname+";1")
	continue

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
    
    
def ReadMEandPDFNormalizations(csv_file):
	mydict={}
	with open(csv_file) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			name_array=row['name'].split("/")
			sample_name_modified = name_array[1].replace("_","").replace("-","")
			initial_weight_name = row['weight']
			factor=row['factor']
			mydict[(sample_name_modified,initial_weight_name)]=factor
	return mydict
	
def AddMEandPDFNormalizationsMap(csv_file):
	mydict=ReadMEandPDFNormalizations(csv_file)
	code='std::map<TString,float> MEPDF_Norm_Map;\n'
	for key in mydict:
		code+='MEPDF_Norm_Map["'+key[0]+'_'+key[1]+'"]='+mydict[key]+';\n'
	return code
	
def GetMEPDFadditionalVariablesList(csv_file):
	#mydict=ReadMEandPDFNormalizations(csv_file)
	#seen = set()
	weight_vars_list=["Weight_pdf_variation_"+str(i+292201) for i in range(102)]
	#for key in mydict:
		#if not key[1] in seen:
			#seen.add(key[1])
			#weight_vars_list.append(key[1])
	return weight_vars_list

def RelateMEPDFMapToNormFactor(csv_file):
	weight_list=GetMEPDFadditionalVariablesList(csv_file)
	code=''
	code+="""
    TString currentRelevantSampleNameForMEPDF=sampleDataBaseIdentifiers[currentfilename];
    TString translatedCurrentRelevantSampleNameForMEPDF=sampleTranslationMapCPP[currentRelevantSampleNameForMEPDF];
    //std::cout<<"MEPDF relation "<<currentfilename<<" "<<currentRelevantSampleNameForMEPDF<<" "<<translatedCurrentRelevantSampleNameForMEPDF<<std::endl;
  """
	code+='if(MEPDF_Norm_Map.find('+'translatedCurrentRelevantSampleNameForMEPDF'+'+"_'+weight_list[0]+'")!=MEPDF_Norm_Map.end()){;\n'
	for weight in weight_list:
		code+='internalNormFactor_'+weight+'='+'MEPDF_Norm_Map['+'translatedCurrentRelevantSampleNameForMEPDF'+'+"_'+weight+'"];\n'
	code+='}\n'
	code+='//else{std::cout<<"did not find pdf weights in map "<<translatedCurrentRelevantSampleNameForMEPDF<<std::endl;}\n'
	code+='//std::cout<<"first internal pdf weight "<<'+'translatedCurrentRelevantSampleNameForMEPDF'+'+"_'+weight_list[0]+'" <<" "<< internalNormFactor_'+weight_list[0]+'<<std::endl;\n'
	return code
	
	
def GetMEPDFVetoList(csv_file):
	weight_list=GetMEPDFadditionalVariablesList(csv_file)
	weight_veto_list=[]
	for weight in weight_list:
		weight_veto_list.append('internalNormFactor_'+weight)
	return weight_veto_list
	
	
def DeclareMEPDFNormFactors(csv_file):
	code=''
	weight_list=GetMEPDFadditionalVariablesList(csv_file)
	for weight in weight_list:
		code+='float internalNormFactor_'+weight+'=0.0;\n'
	return code
def ResetMEPDFNormFactors(csv_file):
        code=''
        weight_list=GetMEPDFadditionalVariablesList(csv_file)
        for weight in weight_list:
                code+='internalNormFactor_'+weight+'=0.0;\n'
        return code	
def GetPDFadditionalVariablesList(csv_file):
	weight_list=GetMEPDFadditionalVariablesList(csv_file)
	pdf_weight_list=[]
	for weight in weight_list:
		if "pdf" in weight:
			pdf_weight_list.append(weight)
	return pdf_weight_list
	
def PutPDFWeightsinVector(csv_file):
	#pdf_weights=GetPDFadditionalVariablesList(csv_file)
	pdf_weights=["Weight_pdf_variation_"+str(i+292201) for i in range(102)]
	code='std::vector<double> pdf_weights;\n'
	code+='pdf_weights.push_back(1.);\n'
	for weight in pdf_weights:
		code+='pdf_weights.push_back('+weight+');\n'
	return code
def DefineLHAPDF():
    code='LHAPDF::PDFSet pdfSet("NNPDF30_nlo_nf_5_pdfas");\n'
    return code

def UseLHAPDF():
    code=''
    #code+='LHAPDF::PDFSet pdfSet("NNPDF30_nlo_as_0118");\n'
    code+='const LHAPDF::PDFUncertainty pdfUnc = pdfSet.uncertainty(pdf_weights, 68.);\n'
    code+='internalPDFweightUp   = pdfUnc.central + pdfUnc.errplus;\n'
    code+='internalPDFweightDown = pdfUnc.central - pdfUnc.errminus;\n'
    code+='internalPDFweight = pdfUnc.central;\n'
    code+='//std::cout<<"result pdf weights: central, down, up "<<pdfUnc.central<<" "<<internalPDFweightDown<< " "<<internalPDFweightUp<<std::endl;\n'
    return code

    
