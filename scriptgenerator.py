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
    std::cout<<h_abseta_pt_ratio<<std::endl;
    std::cout<<"done setting up muon ID SF"<<std::endl;
}

double MuIDHelper::GetSF(double muonPt, double muonEta, int syst){
  if(muonPt==0.0){return 1.0;}

  std::cout<<muonPt<<" "<<muonEta<<std::endl;
  int thisbin=0;
  double searcheta=fabs(muonEta);
  double searchpt=TMath::Min(muonPt,120.0);
  
  thisbin = h_abseta_pt_ratio->FindBin(searcheta,searchpt);
  double nomval=h_abseta_pt_ratio->GetBinContent(thisbin);
  double error=h_abseta_pt_ratio->GetBinError(thisbin);
  double upval=(nomval+error)*(1.0+0.01);
  double downval=(nomval-error)*(1.0-0.01);
  if(syst==0){std::cout<<"ID SF "<<std::endl; std::cout<<nomval<<" "<<upval<<" "<<downval<<std::endl;}
  
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
    std::cout<<h_abseta_pt_ratio<<std::endl;
    std::cout<<"done setting up muon Iso SF"<<std::endl;
}

double MuIsoHelper::GetSF(double muonPt, double muonEta, int syst){
  if(muonPt==0.0){return 1.0;}

  std::cout<<muonPt<<" "<<muonEta<<std::endl;
  int thisbin=0;
  double searcheta=fabs(muonEta);
  double searchpt=TMath::Min(muonPt,120.0);
  
  thisbin = h_abseta_pt_ratio->FindBin(searcheta,searchpt);
  double nomval=h_abseta_pt_ratio->GetBinContent(thisbin);
  double error=h_abseta_pt_ratio->GetBinError(thisbin);
  double upval=(nomval+error)*(1.0+0.005);
  double downval=(nomval-error)*(1.0-0.005);
  if(syst==0){std::cout<<"Iso SF "<<std::endl; std::cout<<nomval<<" "<<upval<<" "<<downval<<std::endl;}
  
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
    TH2D *h_abseta_pt_ratio;
};

MuTriggerHelper::MuTriggerHelper()
{
    std::string inputFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/SingleMuonTrigger_Z_RunCD_Reco76X_Feb15.root";

    TFile *f_muonTriggerSF = new TFile(std::string(inputFile).c_str(),"READ");

    h_abseta_pt_ratio=(TH2D*)f_muonTriggerSF->Get("runD_IsoMu20_OR_IsoTkMu20_HLTv4p3_PtEtaBins/abseta_pt_ratio");
    std::cout<<h_abseta_pt_ratio<<std::endl;
    std::cout<<"done setting up muon Trigger SF"<<std::endl;
}

double MuTriggerHelper::GetSF(double muonPt, double muonEta, int syst){
  if(muonPt==0.0){return 1.0;}
  std::cout<<muonPt<<" "<<muonEta<<std::endl;
  int thisbin=0;
  double searcheta=fabs(muonEta);
  double searchpt=TMath::Min(muonPt,120.0);
  
  thisbin = h_abseta_pt_ratio->FindBin(searcheta,searchpt);
  double nomval=h_abseta_pt_ratio->GetBinContent(thisbin);
  double error=h_abseta_pt_ratio->GetBinError(thisbin);
  double upval=(nomval+error)*(1.0+0.005);
  double downval=(nomval-error)*(1.0-0.005);
  if(syst==0){std::cout<<"Trigger SF "<<std::endl; std::cout<<nomval<<" "<<upval<<" "<<downval<<std::endl;}
  
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

  string buf;
  stringstream ss(filenames); 
  while (ss >> buf){
    chain->Add(buf.c_str());
  }
  if (buf.find("JESDOWN")!=string::npos){internalSystName=7;}
  if (buf.find("JESUP")!=string::npos){internalSystName=8;}
  if (buf.find("JERDOWN")!=string::npos){internalSystName=0;}
  if (buf.find("JERUP")!=string::npos){internalSystName=0;}
  std::cout<<internalSystName<<std::endl;
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
    text+='if(abs(Weight_CSV-csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,internalSystName,csvWgtHF,csvWgtLF,csvWgtCF))>0.0001){std::cout<<"diff "<<Weight_CSV<<" "<<csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,internalSystName,csvWgtHF,csvWgtLF,csvWgtCF)<<std::endl;}'
    
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
    f=ROOT.TFile(samples[0].files[0])
    print 'using',samples[0].files[0],'to determining variable types'
    tree=f.Get('MVATree')
    
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
    vetolist=['internalSystName','csvWgtCF','csvReweighter','csvWgtLF','csvWgtHF','jetPts','jetEtas','jetCSVs','jetFlavors','DoWeights','muonTriggerHelper','muonIsoHelper','muonIDHelper','muonPt','muonEta']
    for upv in unprunedvariablesnames:
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
