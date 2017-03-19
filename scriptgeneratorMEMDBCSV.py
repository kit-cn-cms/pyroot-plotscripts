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

//hacked Lepton SF Helper from MiniAODHelper


class LeptonSFHelper {

 public:
  LeptonSFHelper( );
  ~LeptonSFHelper( );

  float GetElectronSF(  float electronPt , float electronEta , int syst , std::string type  );
  float GetMuonSF(  float muonPt , float muonEta , int syst , std::string type  );
  
 private:

  void SetElectronHistos( );
  void SetMuonHistos( );

  TH2F *h_ele_ID_abseta_pt_ratio;
  TH2F *h_ele_TRIGGER_abseta_pt_ratio;
  TH2F *h_ele_ISO_abseta_pt_ratio;
  TH2F *h_ele_GFS_abseta_pt_ratio;

    TH2F *h_mu_ID_abseta_pt_ratioBtoF;
  TH1D *h_mu_HIP_eta_ratioBtoF;
  TH2F *h_mu_TRIGGER_abseta_ptBtoF;
  TH2F *h_mu_ISO_abseta_pt_ratioBtoF;

    TH2F *h_mu_ID_abseta_pt_ratioGtoH;
  TH1D *h_mu_HIP_eta_ratioGtoH;
  TH2F *h_mu_TRIGGER_abseta_ptGtoH;
  TH2F *h_mu_ISO_abseta_pt_ratioGtoH;

  float electronMaxPt;
  float electronMaxPtHigh;
  float muonMaxPt;
  float muonMaxPtHigh;
  float ljets_mu_BtoF_lumi;
  float ljets_mu_GtoH_lumi;
  

};

LeptonSFHelper::LeptonSFHelper( ){

  //std::cout << "Initializing Lepton scale factors" << std::endl;

  SetElectronHistos( );
  SetMuonHistos( );

  electronMaxPt = 199.0;
  electronMaxPtHigh=250.0;
  muonMaxPt = 119.0;
  muonMaxPtHigh = 499.0;
  
  ljets_mu_BtoF_lumi=19691.782;
  ljets_mu_GtoH_lumi=16226.452;


}

LeptonSFHelper::~LeptonSFHelper( ){

}

float LeptonSFHelper::GetElectronSF(  float electronPt , float electronEta , int syst , std::string type  ) {
  if ( electronPt == 0.0 ){ return 1.0; }

  int thisBin=0;

  float searchEta=electronEta;
  float searchPt=TMath::Min( electronPt , electronMaxPt );
  if (type=="Trigger"){
    searchPt=TMath::Min( electronPt , electronMaxPtHigh );
  }

  float nomval = 0;
  float error = 0;
  float upval = 0;
  float downval= 0;


  if ( type == "ID" ){

    thisBin = h_ele_ID_abseta_pt_ratio->FindBin( searchEta , searchPt );
    nomval=h_ele_ID_abseta_pt_ratio->GetBinContent( thisBin );
    error=h_ele_ID_abseta_pt_ratio->GetBinError( thisBin );

    upval=nomval+error;
    downval=nomval-error;

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

  }
  else if ( type == "GFS" ){

    thisBin = h_ele_GFS_abseta_pt_ratio->FindBin( searchEta , searchPt );
    nomval=h_ele_GFS_abseta_pt_ratio->GetBinContent( thisBin );
    error=h_ele_GFS_abseta_pt_ratio->GetBinError( thisBin );
    upval=nomval+error; //DANGERZONE need to add pT depnednet 1% uncertainty
    downval=nomval-error;

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
  float searchPt=TMath::Min( muonPt , muonMaxPt );
  if (type=="Trigger"){
    searchPt=TMath::Min( muonPt , muonMaxPtHigh );
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

    thisBin = h_mu_HIP_eta_ratioBtoF->FindBin( searchEta );
    nomvalBtoF=h_mu_HIP_eta_ratioBtoF->GetBinContent( thisBin );
    errorBtoF=h_mu_HIP_eta_ratioBtoF->GetBinError( thisBin );
    upvalBtoF=( nomvalBtoF+errorBtoF );
    downvalBtoF=( nomvalBtoF-errorBtoF );
    
    thisBin = h_mu_HIP_eta_ratioGtoH->FindBin( searchEta );
    nomvalGtoH=h_mu_HIP_eta_ratioGtoH->GetBinContent( thisBin );
    errorGtoH=h_mu_HIP_eta_ratioGtoH->GetBinError( thisBin );
    upvalGtoH=( nomvalGtoH+errorGtoH );
    downvalGtoH=( nomvalGtoH-errorGtoH );
    
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

void LeptonSFHelper::SetElectronHistos( ){

  std::string IDinputFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Spring150217/feb160317/ele_ID_SF.root";
  std::string TRIGGERinputFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Spring150217/feb160317/ele_TriggerSF_Run2016All_v1.root";
  std::string ISOinputFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Spring150217/feb160317/ele_Reco_EGM2D.root"; // DANGERZONE: no iso SF yet??
  std::string GFSinputFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Spring150217/feb160317/ele_Reco_EGM2D.root";

  TFile *f_IDSF = new TFile(std::string(IDinputFile).c_str(),"READ");
  TFile *f_TRIGGERSF = new TFile(std::string(TRIGGERinputFile).c_str(),"READ");
  TFile *f_ISOSF = new TFile(std::string(ISOinputFile).c_str(),"READ");
  TFile *f_GFSSF = new TFile(std::string(GFSinputFile).c_str(),"READ");

  h_ele_ID_abseta_pt_ratio = (TH2F*)f_IDSF->Get("EGamma_SF2D");
  h_ele_TRIGGER_abseta_pt_ratio = (TH2F*)f_TRIGGERSF->Get("Ele27_WPTight_Gsf");
  h_ele_ISO_abseta_pt_ratio = (TH2F*)f_ISOSF->Get("EGamma_SF2D");
  h_ele_GFS_abseta_pt_ratio = (TH2F*)f_GFSSF->Get("EGamma_SF2D");

}

void LeptonSFHelper::SetMuonHistos( ){

  std::string IDinputFileBtoF = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Spring150217/feb160317/mu_ID_EfficienciesAndSF_BCDEF.root";
  std::string IDinputFileGtoH = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Spring150217/feb160317/mu_ID_EfficienciesAndSF_GH.root";

  std::string TRIGGERinputFileBtoF =  "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Spring150217/feb160317/mu_TRIGGER_BtoF.root";
  std::string TRIGGERinputFileGtoH =  "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Spring150217/feb160317/mu_TRIGGER_GtoH.root";

  std::string ISOinputFileBtoF =  "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Spring150217/feb160317/mu_ISO_EfficienciesAndSF_BCDEF.root";
  std::string ISOinputFileGtoH =  "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Spring150217/feb160317/mu_ISO_EfficienciesAndSF_GH.root";
  
  std::string HIPinputFileBtoF =  "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Spring150217/feb160317/HIP_BCDEF_histos.root";
  std::string HIPinputFileGtoH =  "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Spring150217/feb160317/HIP_GH_histos.root";


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

  h_mu_HIP_eta_ratioBtoF = (TH1D*)f_HIPSFBtoF->Get("ratio_eff_aeta_dr030e030_corr");
  h_mu_HIP_eta_ratioGtoH = (TH1D*)f_HIPSFGtoH->Get("ratio_eff_aeta_dr030e030_corr");

  h_mu_TRIGGER_abseta_ptBtoF= (TH2F*)f_TRIGGERSFBtoF->Get("IsoMu24_OR_IsoTkMu24_PtEtaBins/pt_abseta_ratio");
  h_mu_TRIGGER_abseta_ptGtoH= (TH2F*)f_TRIGGERSFGtoH->Get("IsoMu24_OR_IsoTkMu24_PtEtaBins/pt_abseta_ratio");

  h_mu_ISO_abseta_pt_ratioBtoF = (TH2F*)f_ISOSFBtoF->Get("TightISO_TightID_pt_eta/pt_abseta_ratio");
  h_mu_ISO_abseta_pt_ratioGtoH = (TH2F*)f_ISOSFGtoH->Get("TightISO_TightID_pt_eta/pt_abseta_ratio");

}

// hacked in CSV helper
class CSVHelper
{
  public:
    // nHFptBins specifies how many of these pt bins are used:
    // (jetPt >= 19.99 && jetPt < 30), (jetPt >= 30 && jetPt < 40), (jetPt >= 40 && jetPt < 60), 
    // (jetPt >= 60 && jetPt < 100), (jetPt >= 100 && jetPt < 160), (jetPt >= 160 && jetPt < 10000).
    // If nHFptBins < 6, the last on is inclusive (eg jetPt >=100 && jetPt < 10000 for nHFptBins=5).
    // The SFs from data have 5 bins, the pseudo data scale factors 6 bins.
    CSVHelper();
  CSVHelper(const std::string& hf, const std::string& lf, const int nHFptBins=6);
  ~CSVHelper();

  void init(const std::string& hf, const std::string& lf, const int nHFptBins);

  double getCSVWeight(const std::vector<double>& jetPts,
		      const std::vector<double>& jetEtas,
		      const std::vector<double>& jetCSVs,
		      const std::vector<int>& jetFlavors,
		      const int iSys,
		      double &csvWgtHF,
		      double &csvWgtLF,
		      double &csvWgtCF) const;

  private:
    bool isInit_;
    int nHFptBins_;

    std::vector< std::vector<TH1*> > h_csv_wgt_hf;
    std::vector< std::vector<TH1*> > c_csv_wgt_hf;
    std::vector< std::vector< std::vector<TH1*> > > h_csv_wgt_lf;

    void fillCSVHistos(TFile *fileHF, TFile *fileLF);
    TH1* readHistogram(TFile* file, const TString& name) const;
};

CSVHelper::CSVHelper()
  : isInit_(false), nHFptBins_(0) {}


CSVHelper::CSVHelper(const std::string& hf, const std::string& lf, const int nHFptBins)
  : isInit_(false), nHFptBins_(0) {
  init(hf,lf,nHFptBins);
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


void CSVHelper::init(const std::string& hf, const std::string& lf, const int nHFptBins) {
  std::cout << "Initializing b-tag scale factors"<< "  HF : " << hf << " (" << nHFptBins << " pt bins)"<< "  LF : " << lf << std::endl;

  nHFptBins_ = nHFptBins;

  const std::string inputFileHF = hf.size() > 0 ? hf : "data/csv_rwt_hf_IT_FlatSF.root";
  const std::string inputFileLF = lf.size() > 0 ? lf : "data/csv_rwt_lf_IT_FlatSF.root";

  TFile *f_CSVwgt_HF = new TFile(inputFileHF.c_str());
  TFile *f_CSVwgt_LF = new TFile(inputFileLF.c_str());
  fillCSVHistos(f_CSVwgt_HF, f_CSVwgt_LF);
  f_CSVwgt_HF->Close();
  f_CSVwgt_LF->Close();
  delete f_CSVwgt_HF;
  delete f_CSVwgt_LF;

  isInit_ = true;
}

// fill the histograms (done once)
void
CSVHelper::fillCSVHistos(TFile *fileHF, TFile *fileLF)
{
  const size_t nSys = 9;
  const size_t nPt = 6;
  const size_t nEta = 3;
  h_csv_wgt_hf = std::vector< std::vector<TH1*> >(nSys,std::vector<TH1*>(nPt,NULL));
  c_csv_wgt_hf = std::vector< std::vector<TH1*> >(nSys,std::vector<TH1*>(nPt,NULL));
  h_csv_wgt_lf = std::vector< std::vector< std::vector<TH1*> > >(nSys,std::vector< std::vector<TH1*> >(nPt,std::vector<TH1*>(nEta,NULL)));

  // CSV reweighting /// only care about the nominal ones
  for (size_t iSys = 0; iSys < nSys; iSys++) {
    TString syst_csv_suffix_hf = "final";
    TString syst_csv_suffix_c = "final";
    TString syst_csv_suffix_lf = "final";

    switch (iSys) {
    case 0:
      // this is the nominal case
      break;
    case 1:
      // JESUp
      syst_csv_suffix_hf = "final_JESUp";
      syst_csv_suffix_lf = "final_JESUp";
      syst_csv_suffix_c = "final_cErr1Up";
      break;
    case 2:
      // JESDown
      syst_csv_suffix_hf = "final_JESDown";
      syst_csv_suffix_lf = "final_JESDown";
      syst_csv_suffix_c = "final_cErr1Down";
      break;
    case 3:
      // purity up
      syst_csv_suffix_hf = "final_LFUp";
      syst_csv_suffix_lf = "final_HFUp";
      syst_csv_suffix_c = "final_cErr2Up";
      break;
    case 4:
      // purity down
      syst_csv_suffix_hf = "final_LFDown";
      syst_csv_suffix_lf = "final_HFDown";
      syst_csv_suffix_c = "final_cErr2Down";
      break;
    case 5:
      // stats1 up
      syst_csv_suffix_hf = "final_Stats1Up";
      syst_csv_suffix_lf = "final_Stats1Up";
      break;
    case 6:
      // stats1 down
      syst_csv_suffix_hf = "final_Stats1Down";
      syst_csv_suffix_lf = "final_Stats1Down";
      break;
    case 7:
      // stats2 up
      syst_csv_suffix_hf = "final_Stats2Up";
      syst_csv_suffix_lf = "final_Stats2Up";
      break;
    case 8:
      // stats2 down
      syst_csv_suffix_hf = "final_Stats2Down";
      syst_csv_suffix_lf = "final_Stats2Down";
      break;
    }
    
    for (int iPt = 0; iPt < nHFptBins_; iPt++) {
      const TString name = Form("csv_ratio_Pt%i_Eta0_%s", iPt, syst_csv_suffix_hf.Data());
      h_csv_wgt_hf.at(iSys).at(iPt) = readHistogram(fileHF,name);
    }
    if (iSys < 5) {
      for (int iPt = 0; iPt < nHFptBins_; iPt++) {
	const TString name = Form("c_csv_ratio_Pt%i_Eta0_%s", iPt, syst_csv_suffix_c.Data());
	c_csv_wgt_hf.at(iSys).at(iPt) = readHistogram(fileHF,name);
      }
    }    
    for (int iPt = 0; iPt < 4; iPt++) {
      for (int iEta = 0; iEta < 3; iEta++) {
	const TString name = Form("csv_ratio_Pt%i_Eta%i_%s", iPt, iEta, syst_csv_suffix_lf.Data());
	h_csv_wgt_lf.at(iSys).at(iPt).at(iEta) = readHistogram(fileLF,name);
      }
    }
  }
}


TH1* CSVHelper::readHistogram(TFile* file, const TString& name) const {
  TH1* h = NULL;
  file->GetObject(name,h);
  if( h==NULL ) {
    std::cout<<"CSVHelper: DID nit find histograms"<<std::endl;
  }
  h->SetDirectory(0);
  
  return h;
}

double
CSVHelper::getCSVWeight(const std::vector<double>& jetPts,
			const std::vector<double>& jetEtas,
			const std::vector<double>& jetCSVs,
			const std::vector<int>& jetFlavors,
			const int iSys,
			double &csvWgtHF,
			double &csvWgtLF,
			double &csvWgtCF) const
{
  if( !isInit_ ) {
    std::cout<<"CSVHelper: Not initualized"<<std::endl;
  }

  int iSysHF = 0;
  switch (iSys) {
  case 7:
    iSysHF = 1;
    break; // JESUp
  case 8:
    iSysHF = 2;
    break; // JESDown
  case 9:
    iSysHF = 3;
    break; // LFUp
  case 10:
    iSysHF = 4;
    break; // LFDown
  case 13:
    iSysHF = 5;
    break; // Stats1Up
  case 14:
    iSysHF = 6;
    break; // Stats1Down
  case 15:
    iSysHF = 7;
    break; // Stats2Up
  case 16:
    iSysHF = 8;
    break; // Stats2Down
  default:
    iSysHF = 0;
    break; // NoSys
  }
  
  int iSysC = 0;
  switch (iSys) {
  case 21:
    iSysC = 1;
    break;
  case 22:
    iSysC = 2;
    break;
  case 23:
    iSysC = 3;
    break;
  case 24:
    iSysC = 4;
    break;
  default:
    iSysC = 0;
    break;
  }
  
  int iSysLF = 0;
  switch (iSys) {
  case 7:
    iSysLF = 1;
    break; // JESUp
  case 8:
    iSysLF = 2;
    break; // JESDown
  case 11:
    iSysLF = 3;
    break; // HFUp
  case 12:
    iSysLF = 4;
    break; // HFDown
  case 17:
    iSysLF = 5;
    break; // Stats1Up
  case 18:
    iSysLF = 6;
    break; // Stats1Down
  case 19:
    iSysLF = 7;
    break; // Stats2Up
  case 20:
    iSysLF = 8;
    break; // Stats2Down
  default:
    iSysLF = 0;
    break; // NoSys
  }

  double csvWgthf = 1.;
  double csvWgtC = 1.;
  double csvWgtlf = 1.;
  
  for (size_t iJet = 0; iJet < jetPts.size(); iJet++) {
    const double csv = jetCSVs.at(iJet);
    const double jetPt = jetPts.at(iJet);
    const double jetAbsEta = fabs(jetEtas.at(iJet));
    const int flavor = jetFlavors.at(iJet);

    int iPt = -1;
    int iEta = -1;
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
    
    if (jetAbsEta >= 0 && jetAbsEta < 0.8)
      iEta = 0;
    else if (jetAbsEta >= 0.8 && jetAbsEta < 1.6)
      iEta = 1;
    else if (jetAbsEta >= 1.6 && jetAbsEta < 2.41)
      iEta = 2;
    
    if (iPt < 0 || iEta < 0)
      std::cout<< "CSVHelper: couldn't find Pt, Eta bins for this b-flavor jet, jetPt = " << jetPt << ", jetAbsEta = " << jetAbsEta<<std::endl;
    
    if (abs(flavor) == 5) {
      // RESET iPt to maximum pt bin (only 5 bins for new SFs)
      if(iPt>=nHFptBins_){
	iPt=nHFptBins_-1;
      }
      const int useCSVBin = (csv >= 0.) ? h_csv_wgt_hf.at(iSysHF).at(iPt)->FindBin(csv) : 1;
      double iCSVWgtHF = h_csv_wgt_hf.at(iSysHF).at(iPt)->GetBinContent(useCSVBin);
      if (iCSVWgtHF==0){iCSVWgtHF=0.001;}
      if (iCSVWgtHF != 0){
	csvWgthf *= iCSVWgtHF;
	}
      
    } else if (abs(flavor) == 4) {
      // RESET iPt to maximum pt bin (only 5 bins for new SFs)
      if(iPt>=nHFptBins_){
	iPt=nHFptBins_-1;
      }
      const int useCSVBin = (csv >= 0.) ? c_csv_wgt_hf.at(iSysC).at(iPt)->FindBin(csv) : 1;
      double iCSVWgtC = c_csv_wgt_hf.at(iSysC).at(iPt)->GetBinContent(useCSVBin);
      if (iCSVWgtC==0){iCSVWgtC=0.001;}
      if (iCSVWgtC != 0)
	csvWgtC *= iCSVWgtC;
    } else {
      if (iPt >= 3)
	iPt = 3; /// [30-40], [40-60] and [60-10000] only 3 Pt bins for lf
      const int useCSVBin = (csv >= 0.) ? h_csv_wgt_lf.at(iSysLF).at(iPt).at(iEta)->FindBin(csv) : 1;
      double iCSVWgtLF = h_csv_wgt_lf.at(iSysLF).at(iPt).at(iEta)->GetBinContent(useCSVBin);
      if (iCSVWgtLF==0){iCSVWgtLF=0.001;}
      if (iCSVWgtLF != 0)
	csvWgtlf *= iCSVWgtLF;
    }
  }

  const double csvWgtTotal = csvWgthf * csvWgtC * csvWgtlf;

  csvWgtHF = csvWgthf;
  csvWgtLF = csvWgtlf;
  csvWgtCF = csvWgtC;

  return csvWgtTotal;
}


void plot(){
  TH1F::SetDefaultSumw2();

  std::string csvHFfile="/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/csv_rwt_fit_hf_v2_final_2017_1_10test.root";
  std::string csvLFfile="/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/csv_rwt_fit_lf_v2_final_2017_1_10test.root";
  
  CSVHelper* internalCSVHelper= new CSVHelper(csvHFfile,csvLFfile, 5);
  LeptonSFHelper* internalLeptonSFHelper= new LeptonSFHelper();

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

  if(processname=="SingleEl" || processname=="SingleMu"){DoWeights=0; std::cout<<"is data, dont use nominal weihgts"<<std::endl;}


  // read in samples to add to chain and get relevant names for the database
  std::map<TString, TString> sampleDataBaseIdentifiers;
  std::map<TString, std::map<TString, long>> sampleDataBaseFoundEvents;
  std::map<TString, std::map<TString, long>> sampleDataBaseLostEvents;
    
  int internalSystName=0;
  
  string buf;
  stringstream ss(filenames); 
  while (ss >> buf){
    chain->Add(buf.c_str());
    if (buf.find("JESDOWN")!=string::npos){internalSystName=8;}
    if (buf.find("JESUP")!=string::npos){internalSystName=7;}
    if (buf.find("JERDOWN")!=string::npos){internalSystName=0;}
    if (buf.find("JERUP")!=string::npos){internalSystName=0;}
    std::cout<<"internal sys for CSV "<<internalSystName<<std::endl;
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


  // DANGERZONE
  // Only Works for SL events at the moment
  // Lepton SFs 
     double muonPt=0.0;
     double muonEta=0.0;
     double electronEta=0.0;
     double electronPt=0.0;

    if(N_TightMuons==1){muonPt=Muon_Pt[0]; muonEta=Muon_Eta[0];}
    else{muonPt=0.0; muonEta=0.0;}
    if(N_TightElectrons==1){electronPt=Electron_Pt[0]; electronEta=Electron_Eta[0];}
    else{electronPt=0.0; electronEta=0.0;}
   
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
      internalEleTriggerWeight=internalLeptonSFHelper->GetElectronSF(muonPt,muonEta,0,"Trigger");
      internalEleTriggerWeightUp=internalLeptonSFHelper->GetElectronSF(muonPt,muonEta,1,"Trigger");
      internalEleTriggerWeightDown=internalLeptonSFHelper->GetElectronSF(muonPt,muonEta,-1,"Trigger");
      
      internalEleIDWeight=internalLeptonSFHelper->GetElectronSF(muonPt,muonEta,0,"ID");
      internalEleIDWeightUp=internalLeptonSFHelper->GetElectronSF(muonPt,muonEta,1,"ID");
      internalEleIDWeightDown=internalLeptonSFHelper->GetElectronSF(muonPt,muonEta,-1,"ID");
      
      internalEleIsoWeight=internalLeptonSFHelper->GetElectronSF(muonPt,muonEta,0,"Iso");
      internalEleIsoWeightUp=internalLeptonSFHelper->GetElectronSF(muonPt,muonEta,1,"Iso");
      internalEleIsoWeightDown=internalLeptonSFHelper->GetElectronSF(muonPt,muonEta,-1,"Iso");
      
      internalEleGFSWeight=internalLeptonSFHelper->GetElectronSF(muonPt,muonEta,0,"GFS");
      internalEleGFSWeightUp=internalLeptonSFHelper->GetElectronSF(muonPt,muonEta,1,"GFS");
      internalEleGFSWeightDown=internalLeptonSFHelper->GetElectronSF(muonPt,muonEta,-1,"GFS");
    }
   
   
  std::vector<double> jetPts;    
  std::vector<double> jetEtas;    
  std::vector<double> jetCSVs;    
  std::vector<int> jetFlavors;    
    
  for(int ijet =0; ijet<N_Jets; ijet++){
	jetPts.push_back(Jet_Pt[ijet]);
	jetEtas.push_back(Jet_Eta[ijet]);
	jetCSVs.push_back(Jet_CSV[ijet]);
	jetFlavors.push_back(Jet_Flav[ijet]);
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
  
  /*
  if(internalCSVweight!=Weight_CSV){std::cout<<"internalCSVweight "<<internalCSVweight<<" "<<Weight_CSV<<std::endl;}
  if(internalCSVweight_CSVHFUp!=Weight_CSVHFup){std::cout<<"internalCSVweight_CSVHFUp "<<internalCSVweight_CSVHFUp<<" "<<Weight_CSVHFup<<std::endl;}
  if(internalCSVweight_CSVHFDown!=Weight_CSVHFdown){std::cout<<"internalCSVweight_CSVHFDown "<<internalCSVweight_CSVHFDown<<" "<<Weight_CSVHFdown<<std::endl;}
  if(internalCSVweight_CSVLFUp!=Weight_CSVLFup){std::cout<<"internalCSVweight_CSVLFUp "<<internalCSVweight_CSVLFUp<<" "<<Weight_CSVLFup<<std::endl;}
 if(internalCSVweight_CSVLFDown!=Weight_CSVLFdown){ std::cout<<"internalCSVweight_CSVLFDown "<<internalCSVweight_CSVLFDown<<" "<<Weight_CSVLFdown<<std::endl;}
  
 if(internalCSVweight_CSVLFStats1Up!=Weight_CSVLFStats1up){ std::cout<<"internalCSVweight_CSVLFStats1Up "<<internalCSVweight_CSVLFStats1Up<<" "<<Weight_CSVLFStats1up<<std::endl;}
 if(internalCSVweight_CSVLFStats1Down!=Weight_CSVLFStats1down){ std::cout<<"internalCSVweight_CSVLFStats1Down "<<internalCSVweight_CSVLFStats1Down<<" "<<Weight_CSVLFStats1down<<std::endl;}
 if(internalCSVweight_CSVLFStats2Up!=Weight_CSVLFStats2up){ std::cout<<"internalCSVweight_CSVLFStats2Up "<<internalCSVweight_CSVLFStats2Up<<" "<<Weight_CSVLFStats2up<<std::endl;}
 if(internalCSVweight_CSVLFStats2Down!=Weight_CSVLFStats2down){ std::cout<<"internalCSVweight_CSVLFStats2Down "<<internalCSVweight_CSVLFStats2Down<<" "<<Weight_CSVLFStats2down<<std::endl;}
  
 if(internalCSVweight_CSVHFStats1Up!=Weight_CSVHFStats1up){ std::cout<<"internalCSVweight_CSVHFStats1Up "<<internalCSVweight_CSVHFStats1Up<<" "<<Weight_CSVHFStats1up<<std::endl;}
 if(internalCSVweight_CSVHFStats1Down!=Weight_CSVHFStats1down){ std::cout<<"internalCSVweight_CSVHFStats1Down "<<internalCSVweight_CSVHFStats1Down<<" "<<Weight_CSVHFStats1down<<std::endl;}
 if(internalCSVweight_CSVHFStats2Up!=Weight_CSVHFStats2up){ std::cout<<"internalCSVweight_CSVHFStats2Up "<<internalCSVweight_CSVHFStats2Up<<" "<<Weight_CSVHFStats2up<<std::endl;}
 if(internalCSVweight_CSVHFStats2Down!=Weight_CSVHFStats2down){ std::cout<<"internalCSVweight_CSVHFStats2Down "<<internalCSVweight_CSVHFStats2Down<<" "<<Weight_CSVHFStats2down<<std::endl;}
  
 if(internalCSVweight_CSVCErr1Up!=Weight_CSVCErr1up){ std::cout<<"internalCSVweight_CSVCErr1Up "<<internalCSVweight_CSVCErr1Up<<" "<<Weight_CSVCErr1up<<std::endl;}
 if(internalCSVweight_CSVCErr1Down!=Weight_CSVCErr1down){ std::cout<<"internalCSVweight_CSVCErr1Down "<<internalCSVweight_CSVCErr1Down<<" "<<Weight_CSVCErr1down<<std::endl;}
 if(internalCSVweight_CSVCErr2Up!=Weight_CSVCErr2up){ std::cout<<"internalCSVweight_CSVCErr2Up "<<internalCSVweight_CSVCErr2Up<<" "<<Weight_CSVCErr2up<<std::endl;}
 if(internalCSVweight_CSVCErr2Down!=Weight_CSVCErr2down){ std::cout<<"internalCSVweight_CSVCErr2Down "<<internalCSVweight_CSVCErr2Down<<" "<<Weight_CSVCErr2down<<std::endl;}
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

  vetolist=['processname','DoWeights','TMath','electronPt','electronEta','muonPt','muonEta','muonTriggerHelper','electronTriggerHelper','hasTrigger','internalCSVweight','internalCSVweight_CSVHFUp','internalCSVweight_CSVHFDown','internalCSVweight_CSVLFUp','internalCSVweight_CSVLFDown','internalCSVweight_CSVLFStats1Up','internalCSVweight_CSVLFStats1Down','internalCSVweight_CSVLFStats2Up','internalCSVweight_CSVLFStats2Down','internalCSVweight_CSVHFStats1Up','internalCSVweight_CSVHFStats1Down','internalCSVweight_CSVHFStats2Up','internalCSVweight_CSVHFStats2Down','internalCSVweight_CSVCErr1Up','internalCSVweight_CSVCErr1Down','internalCSVweight_CSVCErr2Up','internalCSVweight_CSVCErr2Down',
	    "internalEleTriggerWeight","internalEleTriggerWeightUp","internalEleTriggerWeightDown",
	    "internalEleIDWeight","internalEleIDWeightUp","internalEleIDWeightDown",
	    "internalEleIsoWeight","internalEleIsoWeightUp","internalEleIsoWeightDown",
	    "internalEleGFSWeight","internalEleGFSWeightUp","internalEleGFSWeightDown",
	    "internalMuTriggerWeight","internalMuTriggerWeightUp","internalMuTriggerWeightDown",
	    "internalMuIDWeight","internalMuIDWeightUp","internalMuIDWeightDown",
	    "internalMuIsoWeight","internalMuIsoWeightUp","internalMuIsoWeightDown",
	    "internalMuHIPWeight","internalMuHIPWeightUp","internalMuHIPWeightDown",
]
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
