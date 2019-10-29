#ifndef LEPTONSFHELPER
#define LEPTONSFHELPER 
#include "TH1F.h"
#include "TH2F.h"
#include <string>
//hacked Lepton SF Helper from MiniAODHelper

class LeptonSFHelper {

 public:
  LeptonSFHelper(std::string dataera_, std::string basedir_);
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

  TH2F *h_ele_ID_abseta_pt_ratioBtoF;

  TH2F *h_ele_TRIGGER_abseta_pt_ratio;
  TH2F *h_ele_ISO_abseta_pt_ratio;
  TH2F *h_ele_GFS_abseta_pt_ratio;
  TH2F *h_ele_GFS_abseta_pt_ratio_lowEt;

  TH2F *h_mu_ID_abseta_pt_ratio;
  TH1D *h_mu_HIP_eta_ratio;
  TH2F *h_mu_TRIGGER_abseta_pt;
  TH2F *h_mu_ISO_abseta_pt_ratio;
  
  TH2F *h_mu_ID_abseta_pt_ratioBtoF;
  TGraphAsymmErrors *h_mu_HIP_eta_ratioBtoF;
  TH2F *h_mu_TRIGGER_abseta_ptBtoF;
  TH2F *h_mu_ISO_abseta_pt_ratioBtoF;

  //TH2F *h_mu_ID_abseta_pt_ratioGtoH;
  //TGraphAsymmErrors *h_mu_HIP_eta_ratioGtoH;
  //TH2F *h_mu_TRIGGER_abseta_ptGtoH;
  //TH2F *h_mu_ISO_abseta_pt_ratioGtoH;

  
  TH2F *h_ele_ele_TRIGGER_abseta_abseta;
  TH2F *h_mu_mu_TRIGGER_abseta_abseta;
  TH2F *h_ele_mu_TRIGGER_abseta_abseta;

  float electronLowPtRangeCut;
  float electronMaxPt;
  float electronMinPt;
  float electronMinPtLowPt;
  float electronMaxPtLowPt;
  
  float electronMaxPtHigh;
  float electronMaxPtHigher;
  float electronMaxEta;
  float electronMaxEtaLow;
  
  
  float muonMaxPt;
  float muonMaxPtHigh;
  float muonMinPt;
  float muonMinPtHigh;
  float muonMaxEta;
  
  float ljets_mu_BtoF_lumi;
  //float ljets_mu_GtoH_lumi;
  float ljets_ele_BtoF_lumi;
  //float ljets_ele_GtoH_lumi; 

  std::string dataera;
  std::string plotscriptBaseDir;
};
#endif