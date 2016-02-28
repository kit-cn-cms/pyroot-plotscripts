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
#include "TH2F.h"
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include "TMVA/Reader.h"

using namespace std;

class EleIDHelper
{
  public:
    EleIDHelper();
    double GetSF(double electronPt, double electronEta, int syst);

  private:
    TH2D *h_abseta_pt_ratio;
};

EleIDHelper::EleIDHelper()
{
    std::string inputFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/ScaleFactor_GsfElectronToRECO_passingTrigWP80.txt.egamma_SF2D.root";

    TFile *f_electronIDSF = new TFile(std::string(inputFile).c_str(),"READ");

    h_abseta_pt_ratio=(TH2D*)f_electronIDSF->Get("EGamma_SF2D");
    //std::cout<<h_abseta_pt_ratio<<std::endl;
    //std::cout<<"done setting up electron ID SF"<<std::endl;
}

double EleIDHelper::GetSF(double electronPt, double electronEta, int syst){
  if(electronPt==0.0){return 1.0;}

  //std::cout<<electronPt<<" "<<electronEta<<std::endl;
  int thisbin=0;
  double searcheta=electronEta;
  double searchpt=TMath::Min(electronPt,150.0);
  
  thisbin = h_abseta_pt_ratio->FindBin(searcheta,searchpt);
  double nomval=h_abseta_pt_ratio->GetBinContent(thisbin);
  //double error=h_abseta_pt_ratio->GetBinError(thisbin);
  //double upval=(nomval+error)*(1.0+0.01);
  //double downval=(nomval-error)*(1.0-0.01);
  double upval=nomval*(1.0+0.02);
  double downval=nomval*(1.0-0.02);
  
  //if(syst==0){std::cout<<"ID SF "<<std::endl; std::cout<<nomval<<" "<<upval<<" "<<downval<<std::endl;}
  
  if (syst==-1){return downval;}
  else if (syst==1){return upval;}
  else {return nomval;}
}

class EleIsoHelper
{
  public:
    EleIsoHelper();
    double GetSF(double electronPt, double electronEta, int syst);

  private:
    TH2D *h_abseta_pt_ratio;
};

EleIsoHelper::EleIsoHelper()
{
    std::string inputFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Isolation_SF.root";

    TFile *f_electronIsoSF = new TFile(std::string(inputFile).c_str(),"READ");

    h_abseta_pt_ratio=(TH2D*)f_electronIsoSF->Get("IsolationSF");
    //std::cout<<h_abseta_pt_ratio<<std::endl;
    //std::cout<<"done setting up electron Iso SF"<<std::endl;
}

double EleIsoHelper::GetSF(double electronPt, double electronEta, int syst){
  if(electronPt==0.0){return 1.0;}

  int thisbin=0;
  double searcheta=electronEta;
  double searchpt=TMath::Min(electronPt,150.0);
  
  thisbin = h_abseta_pt_ratio->FindBin(searcheta,searchpt);
  double nomval=h_abseta_pt_ratio->GetBinContent(thisbin);
  //double error=h_abseta_pt_ratio->GetBinError(thisbin);
  double upval=nomval*(1.0+0.02);
  double downval=nomval*(1.0-0.02);
  //if(syst==0){std::cout<<"Iso SF "<<std::endl; std::cout<<nomval<<" "<<upval<<" "<<downval<<std::endl;}
  
  if (syst==-1){return downval;}
  else if (syst==1){return upval;}
  else {return nomval;}
}


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
    std::string inputFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/eleTrig_SF.root";

    TFile *f_electronTriggerSF= new TFile(std::string(inputFile).c_str(),"READ");

    h_abseta_pt_ratio=(TH2D*)f_electronTriggerSF->Get("h_eleTrig_SF");

}

double EleTriggerHelper::GetSF(double electronPt, double electronEta, int syst){
  if(electronPt==0.0){return 1.0;}
  //std::cout<<electronPt<<" "<<electronEta<<std::endl;
  int thisbin=0;
  double searcheta=electronEta;
  double searchpt=TMath::Min(electronPt,150.0);
  
  thisbin = h_abseta_pt_ratio->FindBin(searchpt,searcheta);
  double nomval=h_abseta_pt_ratio->GetBinContent(thisbin);
  //double error=h_abseta_pt_ratio->GetBinError(thisbin);
  double upval=nomval*(1.0+0.02);
  double downval=nomval*(1.0-0.02);
    
  // if(syst==0){std::cout<<"Trigger SF "<<std::endl; std::cout<<nomval<<" "<<upval<<" "<<downval<<std::endl;}
  
  if (syst==-1){return downval;}
  else if (syst==1){return upval;}
  else {return nomval;}
}


//----------------------------------------

class MuIDHelper
{
  public:
    MuIDHelper();
    double GetSF(double muonPt, double muonEta, int syst);

  private:
    TH2D *h_abseta_pt_ratio;
};

MuIDHelper::MuIDHelper()
{
    std::string inputFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/MuonID_Z_RunCD_Reco76X_Feb15.root";

    TFile *f_muonIDSF = new TFile(std::string(inputFile).c_str(),"READ");

    h_abseta_pt_ratio=(TH2D*)f_muonIDSF->Get("MC_NUM_TightIDandIPCut_DEN_genTracks_PAR_pt_spliteta_bin1/abseta_pt_ratio");
    //std::cout<<h_abseta_pt_ratio<<std::endl;
    //std::cout<<"done setting up muon ID SF"<<std::endl;
}

double MuIDHelper::GetSF(double muonPt, double muonEta, int syst){
  if(muonPt==0.0){return 1.0;}

  //std::cout<<muonPt<<" "<<muonEta<<std::endl;
  int thisbin=0;
  double searcheta=fabs(muonEta);
  double searchpt=TMath::Min(muonPt,115.0);
  
  thisbin = h_abseta_pt_ratio->FindBin(searcheta,searchpt);
  double nomval=h_abseta_pt_ratio->GetBinContent(thisbin);
  double error=h_abseta_pt_ratio->GetBinError(thisbin);
  //double upval=(nomval+error)*(1.0+0.01);
  //double downval=(nomval-error)*(1.0-0.01);
  double upval=nomval*(1.0+0.02);
  double downval=nomval*(1.0-0.02);
  
  //if(syst==0){std::cout<<"ID SF "<<std::endl; std::cout<<nomval<<" "<<upval<<" "<<downval<<std::endl;}
  
  if (syst==-1){return downval;}
  else if (syst==1){return upval;}
  else {return nomval;}
}

class MuIsoHelper
{
  public:
    MuIsoHelper();
    double GetSF(double muonPt, double muonEta, int syst);

  private:
    TH2D *h_abseta_pt_ratio;
};

MuIsoHelper::MuIsoHelper()
{
    std::string inputFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/MuonIso_Z_RunCD_Reco76X_Feb15.root";

    TFile *f_muonIsoSF = new TFile(std::string(inputFile).c_str(),"READ");

    h_abseta_pt_ratio=(TH2D*)f_muonIsoSF->Get("MC_NUM_TightRelIso_DEN_TightID_PAR_pt_spliteta_bin1/abseta_pt_ratio");
    //std::cout<<h_abseta_pt_ratio<<std::endl;
    //std::cout<<"done setting up muon Iso SF"<<std::endl;
}

double MuIsoHelper::GetSF(double muonPt, double muonEta, int syst){
  if(muonPt==0.0){return 1.0;}

  int thisbin=0;
  double searcheta=fabs(muonEta);
  double searchpt=TMath::Min(muonPt,115.0);
  
  thisbin = h_abseta_pt_ratio->FindBin(searcheta,searchpt);
  double nomval=h_abseta_pt_ratio->GetBinContent(thisbin);
  double error=h_abseta_pt_ratio->GetBinError(thisbin);
  double upval=nomval*(1.0+0.02);
  double downval=nomval*(1.0-0.02);
  //if(syst==0){std::cout<<"Iso SF "<<std::endl; std::cout<<nomval<<" "<<upval<<" "<<downval<<std::endl;}
  
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
    TH2D *h_abseta_pt_ratio4p2;
    TH2D *h_abseta_pt_ratio4p3;

};

MuTriggerHelper::MuTriggerHelper()
{
    std::string inputFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/SingleMuonTrigger_Z_RunCD_Reco76X_Feb15.root";

    TFile *f_muonTriggerSF= new TFile(std::string(inputFile).c_str(),"READ");

    h_abseta_pt_ratio4p3=(TH2D*)f_muonTriggerSF->Get("runD_IsoMu20_OR_IsoTkMu20_HLTv4p3_PtEtaBins/abseta_pt_ratio");

    h_abseta_pt_ratio4p2=(TH2D*)f_muonTriggerSF->Get("runD_IsoMu20_OR_IsoTkMu20_HLTv4p2_PtEtaBins/abseta_pt_ratio");

}

double MuTriggerHelper::GetSF(double muonPt, double muonEta, int syst){
  if(muonPt==0.0){return 1.0;}
  //std::cout<<muonPt<<" "<<muonEta<<std::endl;
  int thisbin=0;
  double searcheta=fabs(muonEta);
  double searchpt=TMath::Min(muonPt,115.0);
  
  thisbin = h_abseta_pt_ratio4p3->FindBin(searcheta,searchpt);
  double nomval4p3=h_abseta_pt_ratio4p3->GetBinContent(thisbin);
  double error4p3=h_abseta_pt_ratio4p3->GetBinError(thisbin);
  double upval4p3=nomval4p3*(1.0+0.02);
  double downval4p3=nomval4p3*(1.0-0.02);
  thisbin = h_abseta_pt_ratio4p2->FindBin(searcheta,searchpt);
  double nomval4p2=h_abseta_pt_ratio4p2->GetBinContent(thisbin);
  double error4p2=h_abseta_pt_ratio4p2->GetBinError(thisbin);
  double upval4p2=nomval4p2*(1.0+0.02);
  double downval4p2=nomval4p2*(1.0-0.02);
  
  double nomval=0.2843*nomval4p2+0.716*nomval4p3;
  double upval=0.2843*upval4p2+0.716*upval4p3;
  double downval=0.2843*downval4p2+0.716*downval4p3;
    
  // if(syst==0){std::cout<<"Trigger SF "<<std::endl; std::cout<<nomval<<" "<<upval<<" "<<downval<<std::endl;}
  
  if (syst==-1){return downval;}
  else if (syst==1){return upval;}
  else {return nomval;}
}



class CSVHelper
{
  public:
    // nHFptBins specifies how many of these pt bins are used:
    // (jetPt >= 19.99 && jetPt < 30), (jetPt >= 30 && jetPt < 40), (jetPt >= 40 && jetPt < 60), 
    // (jetPt >= 60 && jetPt < 100), (jetPt >= 100 && jetPt < 160), (jetPt >= 160 && jetPt < 10000).
    // If nHFptBins < 6, the last on is inclusive (eg jetPt >=100 && jetPt < 10000 for nHFptBins=5).
    // The SFs from data have 5 bins, the pseudo data scale factors 6 bins.
    CSVHelper(std::string hf="", std::string lf="", int nHFptBins=6);

    double getCSVWeight(std::vector<double> jetPts, std::vector<double> jetEtas, std::vector<double> jetCSVs,
                       std::vector<int> jetFlavors, int iSys, double &csvWgtHF, double &csvWgtLF, double &csvWgtCF);

  private:
    void fillCSVHistos(TFile *fileHF, TFile *fileLF);

    // CSV reweighting
    TH1D *h_csv_wgt_hf[9][6];
    TH1D *c_csv_wgt_hf[9][6];
    TH1D *h_csv_wgt_lf[9][4][3];
    const int nHFptBins;
};

CSVHelper::CSVHelper(std::string hf, std::string lf, int nHFptBins_):nHFptBins(nHFptBins_)
{
    std::string inputFileHF = hf.size() > 0 ? hf : "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/csv_rwt_fit_hf_76x_2016_02_08.root";
    std::string inputFileLF = lf.size() > 0 ? lf :"/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/csv_rwt_fit_lf_76x_2016_02_08.root";

    TFile *f_CSVwgt_HF = new TFile(std::string(inputFileHF).c_str());
    TFile *f_CSVwgt_LF = new TFile(std::string(inputFileLF).c_str());

    fillCSVHistos(f_CSVwgt_HF, f_CSVwgt_LF);
}

// fill the histograms (done once)
void
CSVHelper::fillCSVHistos(TFile *fileHF, TFile *fileLF)
{
    for (int iSys = 0; iSys < 9; iSys++) {
        for (int iPt = 0; iPt < 5; iPt++)
            h_csv_wgt_hf[iSys][iPt] = NULL;
        for (int iPt = 0; iPt < 3; iPt++) {
            for (int iEta = 0; iEta < 3; iEta++)
                h_csv_wgt_lf[iSys][iPt][iEta] = NULL;
        }
    }
    for (int iSys = 0; iSys < 5; iSys++) {
        for (int iPt = 0; iPt < 5; iPt++)
            c_csv_wgt_hf[iSys][iPt] = NULL;
    }

    // CSV reweighting /// only care about the nominal ones
    for (int iSys = 0; iSys < 9; iSys++) {
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

        for (int iPt = 0; iPt < nHFptBins; iPt++)
            h_csv_wgt_hf[iSys][iPt] =
                (TH1D *)fileHF->Get(Form("csv_ratio_Pt%i_Eta0_%s", iPt, syst_csv_suffix_hf.Data()));

        if (iSys < 5) {
            for (int iPt = 0; iPt < nHFptBins; iPt++)
                c_csv_wgt_hf[iSys][iPt] =
                    (TH1D *)fileHF->Get(Form("c_csv_ratio_Pt%i_Eta0_%s", iPt, syst_csv_suffix_c.Data()));
        }

        for (int iPt = 0; iPt < 4; iPt++) {
            for (int iEta = 0; iEta < 3; iEta++)
                h_csv_wgt_lf[iSys][iPt][iEta] =
                    (TH1D *)fileLF->Get(Form("csv_ratio_Pt%i_Eta%i_%s", iPt, iEta, syst_csv_suffix_lf.Data()));
        }
    }

    return;
}

double
CSVHelper::getCSVWeight(std::vector<double> jetPts, std::vector<double> jetEtas, std::vector<double> jetCSVs,
                       std::vector<int> jetFlavors, int iSys, double &csvWgtHF, double &csvWgtLF, double &csvWgtCF)
{
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

    for (int iJet = 0; iJet < int(jetPts.size()); iJet++) {
        double csv = jetCSVs[iJet];
        double jetPt = jetPts[iJet];
        double jetAbsEta = fabs(jetEtas[iJet]);
        int flavor = jetFlavors[iJet];

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
            std::cout << "Error, couldn't find Pt, Eta bins for this b-flavor jet, jetPt = " << jetPt
                      << ", jetAbsEta = " << jetAbsEta << std::endl;

        if (abs(flavor) == 5) {
	    // RESET iPt to maximum pt bin (only 5 bins for new SFs)
	    if(iPt>=nHFptBins){
		iPt=nHFptBins-1;
	    }
            int useCSVBin = (csv >= 0.) ? h_csv_wgt_hf[iSysHF][iPt]->FindBin(csv) : 1;
            double iCSVWgtHF = h_csv_wgt_hf[iSysHF][iPt]->GetBinContent(useCSVBin);
            if (iCSVWgtHF != 0)
                csvWgthf *= iCSVWgtHF;

        } else if (abs(flavor) == 4) {
	    // RESET iPt to maximum pt bin (only 5 bins for new SFs)
	    if(iPt>=nHFptBins){
		iPt=nHFptBins-1;
	    }
            int useCSVBin = (csv >= 0.) ? c_csv_wgt_hf[iSysC][iPt]->FindBin(csv) : 1;
            double iCSVWgtC = c_csv_wgt_hf[iSysC][iPt]->GetBinContent(useCSVBin);
            if (iCSVWgtC != 0)
                csvWgtC *= iCSVWgtC;
        } else {
            if (iPt >= 3)
                iPt = 3; /// [30-40], [40-60] and [60-10000] only 3 Pt bins for lf
            int useCSVBin = (csv >= 0.) ? h_csv_wgt_lf[iSysLF][iPt][iEta]->FindBin(csv) : 1;
            double iCSVWgtLF = h_csv_wgt_lf[iSysLF][iPt][iEta]->GetBinContent(useCSVBin);
            if (iCSVWgtLF != 0)
                csvWgtlf *= iCSVWgtLF;
        }
    }

    double csvWgtTotal = csvWgthf * csvWgtC * csvWgtlf;

    csvWgtHF = csvWgthf;
    csvWgtLF = csvWgtlf;
    csvWgtCF = csvWgtC;

    return csvWgtTotal;
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
  int eventsAnalyzed=0;
  float sumOfWeights=0;
  int internalSystName=0;
  double csvWgtHF, csvWgtLF, csvWgtCF;
  int DoWeights=1;
  if(processname=="SingleEl" || processname=="SingleMu"){DoWeights=0; std::cout<<"is data, dont use nominal weihgts"<<std::endl;}

  CSVHelper csvReweighter = CSVHelper("/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/csv_rwt_fit_hf_76x_2016_02_08.root","/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/csv_rwt_fit_lf_76x_2016_02_08.root",5);

  MuIDHelper muonIDHelper=MuIDHelper();
  MuIsoHelper muonIsoHelper=MuIsoHelper();
  MuTriggerHelper muonTriggerHelper=MuTriggerHelper();
  EleIDHelper electronIDHelper=EleIDHelper();
  EleIsoHelper electronIsoHelper=EleIsoHelper();
  EleTriggerHelper electronTriggerHelper=EleTriggerHelper();
  
  float JERUpWeight = 1.0;
  float JERDownWeight = 1.0;
  
  string buf;
  stringstream ss(filenames); 
  while (ss >> buf){
    chain->Add(buf.c_str());
  }
  if (buf.find("JESDOWN")!=string::npos){internalSystName=7;}
  if (buf.find("JESUP")!=string::npos){internalSystName=8;}
  if (buf.find("JERDOWN")!=string::npos){internalSystName=0;}
  if (buf.find("JERUP")!=string::npos){internalSystName=0;}
  //std::cout<<internalSystName<<std::endl;
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

def initTwoDimHistoWithProcessNameAndSuffix(name,nbinsX=10,xminX=0,xmaxX=0,nbinsY=10,xminY=0,xmaxY=0,title_=''):
    if title_=='':
        title=name
    else:
        title=title_

    return '  TH2F* h_'+name+'=new TH2F((processname+"_'+name+'"+suffix).c_str(),"'+title+'",'+str(nbinsX)+','+str(xminX)+','+str(xmaxX)+','+str(nbinsY)+','+str(xminY)+','+str(xmaxY)+');\n'

def initReader(name):
    text=''
    text+='  TMVA::Reader *r_'+name+' = new TMVA::Reader("Silent");\n'
    return text

def connectReaderToDummyVariable(name):
    text=''
    text+='  '+name+'=r_'+name+'->EvaluateMVA("BDT");\n'
    return text


def InitDerivedMVAVariable(names):
    print names
    text=''
    for n in names:
        text+='  float '+n+' = -999.0;\n'
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

def fillTwoDimHistoSyst(name,varname1,varname2,weight,systnames,systweights):
    text='      float weight_'+name+'='+weight+';\n'
    for sn,sw in zip(systnames,systweights):
        text+=fillTwoDimHisto(name+sn,varname1,varname2,'('+sw+')*(weight_'+name+')')
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
    double muonPt=0.0;
    double muonEta=0.0;
    
    if(N_TightMuons==1){muonPt=Muon_Pt[0]; muonEta=Muon_Eta[0];} 
    else{muonPt=0.0; muonEta=0.0;} 

    double electronPt=0.0;
    double electronEta=0.0;
    
    if(N_TightElectrons==1){electronPt=Electron_Pt[0]; electronEta=Electron_Eta[0];} 
    else{electronPt=0.0; electronEta=0.0;}
    
    float JERTTHUp          = ((0.999817311764*(N_Jets==4&&N_BTagsM==2))+(1.00011050701*(N_Jets==5&&N_BTagsM==2))+(0.99937492609*(N_Jets>=6&&N_BTagsM==2))+(0.998668551445*(N_Jets==4&&N_BTagsM==3))+(0.997254669666*(N_Jets==5&&N_BTagsM==3))+(0.999066412449*(N_Jets>=6&&N_BTagsM==3))+(0.997974276543*(N_Jets==4&&N_BTagsM>=4))+(0.99205738306*(N_Jets==5&&N_BTagsM>=4))+(0.996371328831*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTHBBUp        = ((1.0012370348*(N_Jets==4&&N_BTagsM==2))+(1.00015199184*(N_Jets==5&&N_BTagsM==2))+(0.998527228832*(N_Jets>=6&&N_BTagsM==2))+(0.999003887177*(N_Jets==4&&N_BTagsM==3))+(0.996920645237*(N_Jets==5&&N_BTagsM==3))+(0.998582601547*(N_Jets>=6&&N_BTagsM==3))+(0.998088777065*(N_Jets==4&&N_BTagsM>=4))+(0.992186248302*(N_Jets==5&&N_BTagsM>=4))+(0.996247768402*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTHCCUp        = ((1.00544202328*(N_Jets==4&&N_BTagsM==2))+(0.998624622822*(N_Jets==5&&N_BTagsM==2))+(1.00088405609*(N_Jets>=6&&N_BTagsM==2))+(0.988098919392*(N_Jets==4&&N_BTagsM==3))+(0.994389414787*(N_Jets==5&&N_BTagsM==3))+(0.997197210789*(N_Jets>=6&&N_BTagsM==3))+(0.944177687168*(N_Jets==4&&N_BTagsM>=4))+(1.0013538599*(N_Jets==5&&N_BTagsM>=4))+(1.01796555519*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTHTTUp        = ((0.998845696449*(N_Jets==4&&N_BTagsM==2))+(0.999661564827*(N_Jets==5&&N_BTagsM==2))+(1.00106012821*(N_Jets>=6&&N_BTagsM==2))+(0.996212303638*(N_Jets==4&&N_BTagsM==3))+(1.00131177902*(N_Jets==5&&N_BTagsM==3))+(1.00545287132*(N_Jets>=6&&N_BTagsM==3))+(1.03299260139*(N_Jets==4&&N_BTagsM>=4))+(1.02697110176*(N_Jets==5&&N_BTagsM>=4))+(0.988895177841*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTHGGUp        = ((0.984351873398*(N_Jets==4&&N_BTagsM==2))+(0.998820543289*(N_Jets==5&&N_BTagsM==2))+(1.00893437862*(N_Jets>=6&&N_BTagsM==2))+(1.0*(N_Jets==4&&N_BTagsM==3))+(1.12393069267*(N_Jets==5&&N_BTagsM==3))+(0.957889258862*(N_Jets>=6&&N_BTagsM==3))+(1.0*(N_Jets==4&&N_BTagsM>=4))+(1.0*(N_Jets==5&&N_BTagsM>=4))+(1.0*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTHGLUGLUUp    = ((0.996939301491*(N_Jets==4&&N_BTagsM==2))+(0.996565818787*(N_Jets==5&&N_BTagsM==2))+(1.00130987167*(N_Jets>=6&&N_BTagsM==2))+(1.00436687469*(N_Jets==4&&N_BTagsM==3))+(0.985964536667*(N_Jets==5&&N_BTagsM==3))+(0.998151183128*(N_Jets>=6&&N_BTagsM==3))+(1.0*(N_Jets==4&&N_BTagsM>=4))+(1.00110006332*(N_Jets==5&&N_BTagsM>=4))+(1.02388191223*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTHWWUp        = ((0.996340572834*(N_Jets==4&&N_BTagsM==2))+(1.00071108341*(N_Jets==5&&N_BTagsM==2))+(0.999866962433*(N_Jets>=6&&N_BTagsM==2))+(0.993735611439*(N_Jets==4&&N_BTagsM==3))+(1.00334370136*(N_Jets==5&&N_BTagsM==3))+(1.00164079666*(N_Jets>=6&&N_BTagsM==3))+(0.974233329296*(N_Jets==4&&N_BTagsM>=4))+(0.993894100189*(N_Jets==5&&N_BTagsM>=4))+(0.992114424706*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTHZZUp        = ((0.99169999361*(N_Jets==4&&N_BTagsM==2))+(1.00839984417*(N_Jets==5&&N_BTagsM==2))+(0.996844649315*(N_Jets>=6&&N_BTagsM==2))+(1.0035135746*(N_Jets==4&&N_BTagsM==3))+(0.995490133762*(N_Jets==5&&N_BTagsM==3))+(1.00040590763*(N_Jets>=6&&N_BTagsM==3))+(1.05204820633*(N_Jets==4&&N_BTagsM>=4))+(0.930224776268*(N_Jets==5&&N_BTagsM>=4))+(0.993218719959*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTHZGUp        = ((0.996787130833*(N_Jets==4&&N_BTagsM==2))+(0.990018665791*(N_Jets==5&&N_BTagsM==2))+(0.998834550381*(N_Jets>=6&&N_BTagsM==2))+(1.00195741653*(N_Jets==4&&N_BTagsM==3))+(1.00250411034*(N_Jets==5&&N_BTagsM==3))+(0.999686479568*(N_Jets>=6&&N_BTagsM==3))+(1.0*(N_Jets==4&&N_BTagsM>=4))+(1.0*(N_Jets==5&&N_BTagsM>=4))+(0.99796551466*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTLFUp         = ((0.998897075653*(N_Jets==4&&N_BTagsM==2))+(1.00081765652*(N_Jets==5&&N_BTagsM==2))+(1.00124669075*(N_Jets>=6&&N_BTagsM==2))+(0.996834516525*(N_Jets==4&&N_BTagsM==3))+(1.00057053566*(N_Jets==5&&N_BTagsM==3))+(0.999742150307*(N_Jets>=6&&N_BTagsM==3))+(0.982244491577*(N_Jets==4&&N_BTagsM>=4))+(1.01105821133*(N_Jets==5&&N_BTagsM>=4))+(1.01481699944*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTCCUp         = ((0.998970925808*(N_Jets==4&&N_BTagsM==2))+(0.997603237629*(N_Jets==5&&N_BTagsM==2))+(1.00229382515*(N_Jets>=6&&N_BTagsM==2))+(0.995214164257*(N_Jets==4&&N_BTagsM==3))+(0.999613106251*(N_Jets==5&&N_BTagsM==3))+(0.999891161919*(N_Jets>=6&&N_BTagsM==3))+(0.991523265839*(N_Jets==4&&N_BTagsM>=4))+(0.997544586658*(N_Jets==5&&N_BTagsM>=4))+(0.995744228363*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTBUp          = ((0.998170077801*(N_Jets==4&&N_BTagsM==2))+(0.996059775352*(N_Jets==5&&N_BTagsM==2))+(1.00474762917*(N_Jets>=6&&N_BTagsM==2))+(0.994872033596*(N_Jets==4&&N_BTagsM==3))+(0.997874617577*(N_Jets==5&&N_BTagsM==3))+(0.999351501465*(N_Jets>=6&&N_BTagsM==3))+(0.982555270195*(N_Jets==4&&N_BTagsM>=4))+(0.986198425293*(N_Jets==5&&N_BTagsM>=4))+(1.00102508068*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTtwoBUp       = ((0.998409450054*(N_Jets==4&&N_BTagsM==2))+(1.00296461582*(N_Jets==5&&N_BTagsM==2))+(1.00024020672*(N_Jets>=6&&N_BTagsM==2))+(0.993894338608*(N_Jets==4&&N_BTagsM==3))+(0.993970811367*(N_Jets==5&&N_BTagsM==3))+(1.00338232517*(N_Jets>=6&&N_BTagsM==3))+(0.97750544548*(N_Jets==4&&N_BTagsM>=4))+(0.990631461143*(N_Jets==5&&N_BTagsM>=4))+(0.996032714844*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTBBUp         = ((0.994340240955*(N_Jets==4&&N_BTagsM==2))+(1.00755405426*(N_Jets==5&&N_BTagsM==2))+(0.99849998951*(N_Jets>=6&&N_BTagsM==2))+(0.997601091862*(N_Jets==4&&N_BTagsM==3))+(1.00402545929*(N_Jets==5&&N_BTagsM==3))+(0.990340292454*(N_Jets>=6&&N_BTagsM==3))+(1.00384604931*(N_Jets==4&&N_BTagsM>=4))+(0.989267349243*(N_Jets==5&&N_BTagsM>=4))+(0.997949421406*(N_Jets>=6&&N_BTagsM>=4)));
    float JERSTUp           = ((1.00115859509*(N_Jets==4&&N_BTagsM==2))+(1.00402748585*(N_Jets==5&&N_BTagsM==2))+(1.00136303902*(N_Jets>=6&&N_BTagsM==2))+(0.998023688793*(N_Jets==4&&N_BTagsM==3))+(0.996269822121*(N_Jets==5&&N_BTagsM==3))+(1.00247299671*(N_Jets>=6&&N_BTagsM==3))+(1.0277608633*(N_Jets==4&&N_BTagsM>=4))+(0.967205405235*(N_Jets==5&&N_BTagsM>=4))+(1.01120901108*(N_Jets>=6&&N_BTagsM>=4)));
    float JERZJETSUp        = ((0.986613571644*(N_Jets==4&&N_BTagsM==2))+(0.93087542057*(N_Jets==5&&N_BTagsM==2))+(1.06827914715*(N_Jets>=6&&N_BTagsM==2))+(1.00000619888*(N_Jets==4&&N_BTagsM==3))+(1.74125385284*(N_Jets==5&&N_BTagsM==3))+(1.04399836063*(N_Jets>=6&&N_BTagsM==3))+(1.0*(N_Jets==4&&N_BTagsM>=4))+(1.0*(N_Jets==5&&N_BTagsM>=4))+(1.0*(N_Jets>=6&&N_BTagsM>=4)));
    float JERWJETSUp        = ((1.0017182827*(N_Jets==4&&N_BTagsM==2))+(1.00486624241*(N_Jets==5&&N_BTagsM==2))+(0.987593173981*(N_Jets>=6&&N_BTagsM==2))+(1.00414741039*(N_Jets==4&&N_BTagsM==3))+(1.02358448505*(N_Jets==5&&N_BTagsM==3))+(1.00841605663*(N_Jets>=6&&N_BTagsM==3))+(0.964459896088*(N_Jets==4&&N_BTagsM>=4))+(1.00593900681*(N_Jets==5&&N_BTagsM>=4))+(0.985216856003*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTWUp          = ((0.994187653065*(N_Jets==4&&N_BTagsM==2))+(1.00121879578*(N_Jets==5&&N_BTagsM==2))+(1.00024116039*(N_Jets>=6&&N_BTagsM==2))+(1.00224876404*(N_Jets==4&&N_BTagsM==3))+(0.993034243584*(N_Jets==5&&N_BTagsM==3))+(0.997025668621*(N_Jets>=6&&N_BTagsM==3))+(1.15991616249*(N_Jets==4&&N_BTagsM>=4))+(0.994125306606*(N_Jets==5&&N_BTagsM>=4))+(1.01136338711*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTZUp          = ((0.996260285378*(N_Jets==4&&N_BTagsM==2))+(0.996934473515*(N_Jets==5&&N_BTagsM==2))+(1.00602459908*(N_Jets>=6&&N_BTagsM==2))+(0.994053065777*(N_Jets==4&&N_BTagsM==3))+(1.00789821148*(N_Jets==5&&N_BTagsM==3))+(0.994761168957*(N_Jets>=6&&N_BTagsM==3))+(0.976114749908*(N_Jets==4&&N_BTagsM>=4))+(1.00990509987*(N_Jets==5&&N_BTagsM>=4))+(0.991571545601*(N_Jets>=6&&N_BTagsM>=4)));
    float JERDIBOSONUp      = ((1.00589513779*(N_Jets==4&&N_BTagsM==2))+(1.01406025887*(N_Jets==5&&N_BTagsM==2))+(1.0*(N_Jets>=6&&N_BTagsM==2))+(0.989874482155*(N_Jets==4&&N_BTagsM==3))+(1.0*(N_Jets==5&&N_BTagsM==3))+(1.0*(N_Jets>=6&&N_BTagsM==3))+(1.0*(N_Jets==4&&N_BTagsM>=4))+(1.0*(N_Jets==5&&N_BTagsM>=4))+(1.0*(N_Jets>=6&&N_BTagsM>=4)));

    float JERTTHDown        = ((1.00136291981*(N_Jets==4&&N_BTagsM==2))+(1.00013780594*(N_Jets==5&&N_BTagsM==2))+(0.999844908714*(N_Jets>=6&&N_BTagsM==2))+(1.00015258789*(N_Jets==4&&N_BTagsM==3))+(1.00154578686*(N_Jets==5&&N_BTagsM==3))+(1.00094556808*(N_Jets>=6&&N_BTagsM==3))+(1.00701463223*(N_Jets==4&&N_BTagsM>=4))+(1.00375950336*(N_Jets==5&&N_BTagsM>=4))+(1.00381302834*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTHBBDown      = ((1.00030219555*(N_Jets==4&&N_BTagsM==2))+(1.00127255917*(N_Jets==5&&N_BTagsM==2))+(1.00026750565*(N_Jets>=6&&N_BTagsM==2))+(1.00014674664*(N_Jets==4&&N_BTagsM==3))+(1.00148248672*(N_Jets==5&&N_BTagsM==3))+(1.00093400478*(N_Jets>=6&&N_BTagsM==3))+(1.00688540936*(N_Jets==4&&N_BTagsM>=4))+(1.00370049477*(N_Jets==5&&N_BTagsM>=4))+(1.0042746067*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTHCCDown      = ((1.00515520573*(N_Jets==4&&N_BTagsM==2))+(0.991133332253*(N_Jets==5&&N_BTagsM==2))+(1.001765728*(N_Jets>=6&&N_BTagsM==2))+(0.98540353775*(N_Jets==4&&N_BTagsM==3))+(1.01308715343*(N_Jets==5&&N_BTagsM==3))+(1.00345110893*(N_Jets>=6&&N_BTagsM==3))+(1.0*(N_Jets==4&&N_BTagsM>=4))+(1.00877714157*(N_Jets==5&&N_BTagsM>=4))+(1.00151407719*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTHTTDown      = ((1.00127065182*(N_Jets==4&&N_BTagsM==2))+(0.998830854893*(N_Jets==5&&N_BTagsM==2))+(0.999824523926*(N_Jets>=6&&N_BTagsM==2))+(1.00322043896*(N_Jets==4&&N_BTagsM==3))+(0.995092332363*(N_Jets==5&&N_BTagsM==3))+(0.997868359089*(N_Jets>=6&&N_BTagsM==3))+(1.03179514408*(N_Jets==4&&N_BTagsM>=4))+(1.01885581017*(N_Jets==5&&N_BTagsM>=4))+(1.00638473034*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTHGGDown      = ((1.02118360996*(N_Jets==4&&N_BTagsM==2))+(0.9747813344*(N_Jets==5&&N_BTagsM==2))+(1.00082159042*(N_Jets>=6&&N_BTagsM==2))+(1.0*(N_Jets==4&&N_BTagsM==3))+(1.03929936886*(N_Jets==5&&N_BTagsM==3))+(1.00677919388*(N_Jets>=6&&N_BTagsM==3))+(1.0*(N_Jets==4&&N_BTagsM>=4))+(1.0*(N_Jets==5&&N_BTagsM>=4))+(1.0*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTHGLUGLUDown  = ((0.996608793736*(N_Jets==4&&N_BTagsM==2))+(1.00034070015*(N_Jets==5&&N_BTagsM==2))+(1.00162160397*(N_Jets>=6&&N_BTagsM==2))+(0.979127645493*(N_Jets==4&&N_BTagsM==3))+(1.01215314865*(N_Jets==5&&N_BTagsM==3))+(1.00213634968*(N_Jets>=6&&N_BTagsM==3))+(1.0*(N_Jets==4&&N_BTagsM>=4))+(1.03923106194*(N_Jets==5&&N_BTagsM>=4))+(1.00365209579*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTHWWDown      = ((1.00463020802*(N_Jets==4&&N_BTagsM==2))+(0.99989169836*(N_Jets==5&&N_BTagsM==2))+(0.998459100723*(N_Jets>=6&&N_BTagsM==2))+(1.00550532341*(N_Jets==4&&N_BTagsM==3))+(0.999519348145*(N_Jets==5&&N_BTagsM==3))+(0.999773800373*(N_Jets>=6&&N_BTagsM==3))+(1.0*(N_Jets==4&&N_BTagsM>=4))+(0.998823583126*(N_Jets==5&&N_BTagsM>=4))+(0.99129730463*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTHZZDown      = ((1.01330661774*(N_Jets==4&&N_BTagsM==2))+(0.99330842495*(N_Jets==5&&N_BTagsM==2))+(0.998818397522*(N_Jets>=6&&N_BTagsM==2))+(1.02230024338*(N_Jets==4&&N_BTagsM==3))+(0.997246563435*(N_Jets==5&&N_BTagsM==3))+(1.00536549091*(N_Jets>=6&&N_BTagsM==3))+(1.02808511257*(N_Jets==4&&N_BTagsM>=4))+(0.991494834423*(N_Jets==5&&N_BTagsM>=4))+(1.0009469986*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTHZGDown      = ((1.00122249126*(N_Jets==4&&N_BTagsM==2))+(0.971344590187*(N_Jets==5&&N_BTagsM==2))+(0.990911066532*(N_Jets>=6&&N_BTagsM==2))+(1.0*(N_Jets==4&&N_BTagsM==3))+(1.0085542202*(N_Jets==5&&N_BTagsM==3))+(1.10668063164*(N_Jets>=6&&N_BTagsM==3))+(1.0*(N_Jets==4&&N_BTagsM>=4))+(1.0*(N_Jets==5&&N_BTagsM>=4))+(0.961641073227*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTLFDown       = ((1.00133597851*(N_Jets==4&&N_BTagsM==2))+(0.999052643776*(N_Jets==5&&N_BTagsM==2))+(0.998512923717*(N_Jets>=6&&N_BTagsM==2))+(1.00358808041*(N_Jets==4&&N_BTagsM==3))+(0.998682916164*(N_Jets==5&&N_BTagsM==3))+(0.999181449413*(N_Jets>=6&&N_BTagsM==3))+(0.995810568333*(N_Jets==4&&N_BTagsM>=4))+(1.00176930428*(N_Jets==5&&N_BTagsM>=4))+(0.994085848331*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTCCDown       = ((1.00124847889*(N_Jets==4&&N_BTagsM==2))+(1.00049638748*(N_Jets==5&&N_BTagsM==2))+(0.998141825199*(N_Jets>=6&&N_BTagsM==2))+(1.00068449974*(N_Jets==4&&N_BTagsM==3))+(1.00000929832*(N_Jets==5&&N_BTagsM==3))+(1.00092720985*(N_Jets>=6&&N_BTagsM==3))+(0.982166588306*(N_Jets==4&&N_BTagsM>=4))+(0.997252464294*(N_Jets==5&&N_BTagsM>=4))+(0.998431026936*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTBDown        = ((0.998960375786*(N_Jets==4&&N_BTagsM==2))+(1.00226354599*(N_Jets==5&&N_BTagsM==2))+(0.999038040638*(N_Jets>=6&&N_BTagsM==2))+(0.998452603817*(N_Jets==4&&N_BTagsM==3))+(1.0062892437*(N_Jets==5&&N_BTagsM==3))+(1.00038576126*(N_Jets>=6&&N_BTagsM==3))+(1.02469241619*(N_Jets==4&&N_BTagsM>=4))+(1.00381219387*(N_Jets==5&&N_BTagsM>=4))+(1.00088846684*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTtwoBDown     = ((1.00320780277*(N_Jets==4&&N_BTagsM==2))+(1.00415027142*(N_Jets==5&&N_BTagsM==2))+(0.999468445778*(N_Jets>=6&&N_BTagsM==2))+(1.0028847456*(N_Jets==4&&N_BTagsM==3))+(1.00213396549*(N_Jets==5&&N_BTagsM==3))+(1.00247776508*(N_Jets>=6&&N_BTagsM==3))+(1.01289510727*(N_Jets==4&&N_BTagsM>=4))+(1.02559661865*(N_Jets==5&&N_BTagsM>=4))+(1.00733244419*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTBBDown       = ((1.00213575363*(N_Jets==4&&N_BTagsM==2))+(0.991662204266*(N_Jets==5&&N_BTagsM==2))+(1.00258922577*(N_Jets>=6&&N_BTagsM==2))+(1.00053107738*(N_Jets==4&&N_BTagsM==3))+(1.00298380852*(N_Jets==5&&N_BTagsM==3))+(1.00672721863*(N_Jets>=6&&N_BTagsM==3))+(1.00585448742*(N_Jets==4&&N_BTagsM>=4))+(0.997686803341*(N_Jets==5&&N_BTagsM>=4))+(0.999555885792*(N_Jets>=6&&N_BTagsM>=4)));
    float JERSTDown         = ((0.998657763004*(N_Jets==4&&N_BTagsM==2))+(1.0033634901*(N_Jets==5&&N_BTagsM==2))+(1.0005261898*(N_Jets>=6&&N_BTagsM==2))+(1.00121629238*(N_Jets==4&&N_BTagsM==3))+(0.998826920986*(N_Jets==5&&N_BTagsM==3))+(1.0028141737*(N_Jets>=6&&N_BTagsM==3))+(1.02697753906*(N_Jets==4&&N_BTagsM>=4))+(0.926265954971*(N_Jets==5&&N_BTagsM>=4))+(1.00311923027*(N_Jets>=6&&N_BTagsM>=4)));
    float JERZJETSDown      = ((1.0971622467*(N_Jets==4&&N_BTagsM==2))+(0.903486192226*(N_Jets==5&&N_BTagsM==2))+(0.951054930687*(N_Jets>=6&&N_BTagsM==2))+(1.00000309944*(N_Jets==4&&N_BTagsM==3))+(1.18525123596*(N_Jets==5&&N_BTagsM==3))+(1.0*(N_Jets>=6&&N_BTagsM==3))+(1.0*(N_Jets==4&&N_BTagsM>=4))+(1.0*(N_Jets==5&&N_BTagsM>=4))+(1.0*(N_Jets>=6&&N_BTagsM>=4)));
    float JERWJETSDown      = ((1.00260686874*(N_Jets==4&&N_BTagsM==2))+(0.983129858971*(N_Jets==5&&N_BTagsM==2))+(0.984754621983*(N_Jets>=6&&N_BTagsM==2))+(0.996493935585*(N_Jets==4&&N_BTagsM==3))+(1.01907086372*(N_Jets==5&&N_BTagsM==3))+(1.0339192152*(N_Jets>=6&&N_BTagsM==3))+(1.01830470562*(N_Jets==4&&N_BTagsM>=4))+(0.999929785728*(N_Jets==5&&N_BTagsM>=4))+(1.02137517929*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTWDown        = ((1.00814962387*(N_Jets==4&&N_BTagsM==2))+(0.995132267475*(N_Jets==5&&N_BTagsM==2))+(1.00271260738*(N_Jets>=6&&N_BTagsM==2))+(0.99211537838*(N_Jets==4&&N_BTagsM==3))+(0.995414316654*(N_Jets==5&&N_BTagsM==3))+(1.00503349304*(N_Jets>=6&&N_BTagsM==3))+(0.992954730988*(N_Jets==4&&N_BTagsM>=4))+(1.00409662724*(N_Jets==5&&N_BTagsM>=4))+(1.00142645836*(N_Jets>=6&&N_BTagsM>=4)));
    float JERTTZDown        = ((0.998806297779*(N_Jets==4&&N_BTagsM==2))+(1.00877356529*(N_Jets==5&&N_BTagsM==2))+(1.00082218647*(N_Jets>=6&&N_BTagsM==2))+(0.994803130627*(N_Jets==4&&N_BTagsM==3))+(0.990593314171*(N_Jets==5&&N_BTagsM==3))+(0.995595753193*(N_Jets>=6&&N_BTagsM==3))+(1.00228822231*(N_Jets==4&&N_BTagsM>=4))+(1.00535929203*(N_Jets==5&&N_BTagsM>=4))+(1.01914823055*(N_Jets>=6&&N_BTagsM>=4)));
    float JERDIBOSONDown    = ((1.00646984577*(N_Jets==4&&N_BTagsM==2))+(1.01586461067*(N_Jets==5&&N_BTagsM==2))+(1.0005838871*(N_Jets>=6&&N_BTagsM==2))+(1.0*(N_Jets==4&&N_BTagsM==3))+(1.07564687729*(N_Jets==5&&N_BTagsM==3))+(0.62726187706*(N_Jets>=6&&N_BTagsM==3))+(1.0*(N_Jets==4&&N_BTagsM>=4))+(1.0*(N_Jets==5&&N_BTagsM>=4))+(1.0*(N_Jets>=6&&N_BTagsM>=4)));
    
    if(processname=="ttH"){
      JERUpWeight   = JERTTHUp;
      JERDownWeight = JERTTHDown;
    }
    if(processname=="ttH_hbb"){
      JERUpWeight   = JERTTHBBUp;
      JERDownWeight = JERTTHBBDown;
    }
    if(processname=="ttH_hcc"){
      JERUpWeight   = JERTTHCCUp;
      JERDownWeight = JERTTHCCDown;
    }
    if(processname=="ttH_htt"){
      JERUpWeight   = JERTTHTTUp;
      JERDownWeight = JERTTHTTDown;
    }
    if(processname=="ttH_hgg"){
      JERUpWeight   = JERTTHGGUp;
      JERDownWeight = JERTTHGGDown;
    }
    if(processname=="ttH_hgluglu"){
      JERUpWeight   = JERTTHGLUGLUUp;
      JERDownWeight = JERTTHGLUGLUDown;
    }
    if(processname=="ttH_hww"){
      JERUpWeight   = JERTTHWWUp;
      JERDownWeight = JERTTHWWDown;
    }
    if(processname=="ttH_hzz"){
      JERUpWeight   = JERTTHZZUp;
      JERDownWeight = JERTTHZZDown;
    }
    if(processname=="ttH_hzg"){
      JERUpWeight   = JERTTHZGUp;
      JERDownWeight = JERTTHZGDown;
    }
    if(processname=="ttbarOther"){
      JERUpWeight   = JERTTLFUp;
      JERDownWeight = JERTTLFDown;
    }
    if(processname=="ttbarPlusCCbar"){
      JERUpWeight   = JERTTCCUp;
      JERDownWeight = JERTTCCDown;
    }
    if(processname=="ttbarPlusB"){
      JERUpWeight   = JERTTBUp;
      JERDownWeight = JERTTBDown;
    }
    if(processname=="ttbarPlus2B"){
      JERUpWeight   = JERTTtwoBUp;
      JERDownWeight = JERTTtwoBDown;
    }
    if(processname=="ttbarPlusBBbar"){
      JERUpWeight   = JERTTBBUp;
      JERDownWeight = JERTTBBDown;
    }
    if(processname=="singlet"){
      JERUpWeight   = JERSTUp;
      JERDownWeight = JERSTDown;
    }
    if(processname=="zjets"){
      JERUpWeight   = JERZJETSUp;
      JERDownWeight = JERZJETSDown;
    }
    if(processname=="wjets"){
      JERUpWeight   = JERWJETSUp;
      JERDownWeight = JERWJETSDown;
    }
    if(processname=="ttbarW"){
      JERUpWeight   = JERTTWUp;
      JERDownWeight = JERTTWDown;
    }
    if(processname=="ttbarZ"){
      JERUpWeight   = JERTTZUp;
      JERDownWeight = JERTTZDown;
    }
    if(processname=="diboson"){
      JERUpWeight   = JERDIBOSONUp;
      JERDownWeight = JERDIBOSONDown;
    }
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
    #text+='if(abs(Weight_CSV-csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,internalSystName,csvWgtHF,csvWgtLF,csvWgtCF))>0.0001){std::cout<<"diff "<<Weight_CSV<<" "<<csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,internalSystName,csvWgtHF,csvWgtLF,csvWgtCF)<<std::endl;}'
    
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

def fillTwoDimHisto(histo,var1,var2,weight):
    text= '        if(('+weight+')!=0)\n'
    text+='          h_'+histo+'->Fill(fmin(h_'+histo+'->GetXaxis()->GetXmax()-1e-6,fmax(h_'+histo+'->GetXaxis()->GetXmin()+1e-6,'+var1+')),fmin(h_'+histo+'->GetYaxis()->GetXmax()-1e-6,fmax(h_'+histo+'->GetYaxis()->GetXmin()+1e-6,'+var2+')),'+weight+');\n'
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


def createProgram(scriptname,plots,samples,catnames=[""],catselections=["1"],systnames=[""],allsystweights=["1"]):
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
	
    systweights=[]
    systweightexpressions=[]
    derivedsystweights=[]
    for w in allsystweights:
      if ":=" in w:
	derivedsystweights.append(w.split(":=")[0])
	systweightexpressions.append(w.split(":=")[1])
      else:
	systweights.append(w)
    # variables is the list of variables to be read from tree
    variablesnames=['Weight','Weight_CSV','Weight_XS','Jet_CSV','Jet_Pt','Jet_Eta','Jet_Flav','Muon_Pt','Muon_Eta','Electron_Pt','Electron_Eta','N_Jets','N_TightMuons','N_TightElectrons']
    variablesnames+=varsIn(','.join(catselections))#extract all words
    variablesnames+=varsIn(','.join(systweights))   
    
    for sys in derivedsystweights:
      systweights.append(sys)
    
    # What happens here if a variable name contains a number??
    # extract variablesnames of all plots
    for plot in plots:
        if isinstance(plot,plotutils.Plot):
            variablesnames+=varsIn(plot.variable)
        variablesnames+=varsIn(plot.selection)
    for s in samples:
        variablesnames+=varsIn(s.selection)

    for plot in plots:
        if isinstance(plot,plotutils.TwoDimPlot):
            variablesnames+=varsIn(plot.variable1)
            variablesnames+=varsIn(plot.variable2)
        variablesnames+=varsIn(plot.selection)

    for plot in plots:
        if isinstance(plot,plotutils.MVAPlot):
            variablesnames+=varsIn(','.join(plot.input_exprs))
    
    variablesnames+=varsIn(','.join(systweightexpressions))
      
    # remove duplicates
    unprunedvariablesnames=list(set(variablesnames))
    #print unprunedvariablesnames
    variablesnames=[]
    dummyBDTvarList=[]
    vetolist=['processname','internalSystName','csvWgtCF','csvReweighter','csvWgtLF','csvWgtHF','jetPts','jetEtas','jetCSVs','jetFlavors','DoWeights','muonTriggerHelper','muonIsoHelper','muonIDHelper','muonPt','muonEta','electronTriggerHelper','electronIsoHelper','electronIDHelper','electronPt','electronEta','JERUpWeight','JERDownWeight']
    for upv in unprunedvariablesnames:
      if "splitdummybdt" in upv:
	print upv
	dummyBDTvarList.append(upv)
      if upv not in vetolist:
	variablesnames.append(upv)
    #print variablesnames

    # find out types of variables, length of arrays, and add length variables to variable list
    variables=getVartypesAndLength(variablesnames,tree)
    variablesmap={}
    for v in variables:
        variablesmap[v.name]=v
    # start writing script
    script=""
    script+=getHead()
    #print variablenames
    #print variables
    script+=initVarsFromTree(variables)
    
    innames=[]
    for plot in plots:
        if isinstance(plot,plotutils.MVAPlot):
	    for inname,inexpr in zip(plot.input_names, plot.input_exprs):
              if inname!=inexpr:
                innames.append(inname)
    
    for sys in derivedsystweights:
      innames.append(sys)
    innames=list(set(innames))
    script+=InitDerivedMVAVariable(innames)
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
	    #if "splitdummybdt" in plot.histo.GetTitle():
	      #continue
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
    for dv in dummyBDTvarList:
      script+=connectReaderToDummyVariable(dv)
    # calculate derived variables used in BDT
    input_names=[]
    input_exprs=[]
    for plot in plots:
        if isinstance(plot,plotutils.MVAPlot):
	    for inname,inexpr in zip(plot.input_names, plot.input_exprs):
              input_names.append(inname)
              input_exprs.append(inexpr)
    for sys, sysexp in zip(derivedsystweights,systweightexpressions):
      input_names.append(sys)
      input_exprs.append(sysexp)
      
    script+=calculateDerived(input_names,input_exprs)
    for cn,cs in zip(catnames,catselections):
        # for every category
        script+=startCat(cs,variables)
        # plot everything
        for plot in plots:
            if isinstance(plot,plotutils.MVAPlot) or isinstance(plot,plotutils.TwoDimPlot) : continue
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
                weight='('+arrayselection+')*('+pwi+')*Weight_XS*categoryweight*sampleweight'
                script+=fillHistoSyst(histoname,exi,weight,systnames,systweights)
                script+="      }\n"
            else:
                arrayselection=checkArrayLengths(','.join([ex,pw]),variables)
                weight='('+arrayselection+')*('+pw+')*Weight_XS*categoryweight*sampleweight'
                script+=fillHistoSyst(histoname,ex,weight,systnames,systweights)
        
        for plot in plots:
            if not isinstance(plot,plotutils.TwoDimPlot) : continue
            n=plot.histo.GetName()
            exX=plot.variable1
            exY=plot.variable2
            pw=plot.selection
            if pw=='': pw='1'
            variablenames_without_index=varsNoIndex(exX)
            variablenames_without_index+=varsNoIndex(exY)
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
                exiX=getArrayEntries(exX,variablesmap,"i")
                pwi=getArrayEntries(pw,variablesmap,"i")
                exiY=getArrayEntries(ex,variablesmap,"i")
                script+=varLoop("i",size_of_loop)                    
                script+="{\n"
                arrayselection=checkArrayLengths(','.join([exX,exY,pw]),variables)
                weight='('+arrayselection+')*('+pwi+')*Weight_XS*categoryweight*sampleweight'
                script+=fillTwoDimHistoSyst(histoname,exiX,exiY,weight,systnames,systweights)
                script+="      }\n"
            else:
                arrayselection=checkArrayLengths(','.join([ex,pw]),variables)
                weight='('+arrayselection+')*('+pw+')*Weight_XS*categoryweight*sampleweight'
                script+=fillTwoDimHistoSyst(histoname,exX,exY,weight,systnames,systweights)
        
        for plot in plots:
            histoname=cn+plot.name
            if isinstance(plot,plotutils.MVAPlot):
		#if "splitdummybdt" in plot.histo.GetTitle():
		  #continue
                script+=evaluateMVA(plot)
                weight='('+plot.selection+')*Weight_XS*categoryweight*sampleweight'
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
