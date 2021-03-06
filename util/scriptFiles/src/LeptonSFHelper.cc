#include "../interface/LeptonSFHelper.h"
//hacked Lepton SF Helper from MiniAODHelper

//PUBLIC
LeptonSFHelper::LeptonSFHelper(std::string dataera_, std::string basedir_){

  // std::cout << "Initializing Lepton scale factors" << std::endl;
  
  dataera = dataera_;
  plotscriptBaseDir = basedir_;

  SetElectronHistos( );
  SetMuonHistos( );
  SetElectronElectronHistos( );
  SetMuonMuonHistos( );
  SetElectronMuonHistos( );


  electronLowPtRangeCut=20.0;
  electronMaxPt = 150.0;
  electronMinPt = 20.0;
  electronMinPtLowPt = 10;
  electronMaxPtLowPt = 19.9; 
  electronMaxPtHigh= 201.0;
  electronMaxPtHigher= 499.0;  //TH2 histos from Fall17 are binned up to 500 GeV
  electronMaxEta=2.49;
  electronMaxEtaLow=2.19;
  
  
  
  muonMaxPt = 119.0;
  muonMaxPtHigh = 1199.;       //TH2 Trigger SF histos from Fall17 are binned up to 1200 GEV 
  muonMinPt = 20.0;
  muonMinPtHigh = 29.0;
  
  muonMaxEta = 2.39;
}

LeptonSFHelper::~LeptonSFHelper( ){

}

float LeptonSFHelper::GetElectronSF(  float electronPt , float electronEta , int syst , std::string type  ) {
  if ( electronPt == 0.0 ){ return 1.0; }

  int thisBin=0;

  // restrict electron eta 
  float searchEta=electronEta;
  if(searchEta<0 and searchEta<=-electronMaxEta){searchEta=-electronMaxEta;}
  if(searchEta>0 and searchEta>=electronMaxEta){searchEta=electronMaxEta;}
  if(type=="Trigger"){
    if(searchEta<0 and searchEta<=-electronMaxEtaLow){searchEta=-electronMaxEtaLow;}
    if(searchEta>0 and searchEta>=electronMaxEtaLow){searchEta=electronMaxEtaLow;}
  }
    
  
  // restrict electron pT
  float searchPt=electronPt;
  if(searchPt>electronLowPtRangeCut){
    if(searchPt>=electronMaxPtHigher) {searchPt=electronMaxPtHigher;}; // if e_pt >= 500 go to last bin by setting searchPt to 499
    if(searchPt<electronMinPt){searchPt=electronMinPt;}; // if e_pt < 20 go to first bin by setting searchPt to 20
  }
  else{
  // these are now for the low pt Reco SF 
  if(searchPt>=electronMaxPtLowPt) {searchPt=electronMaxPtLowPt;}; // if e_pt >= 500 go to last bin by setting searchPtLowPt to 499
  if(searchPt<electronMinPtLowPt){searchPt=electronMinPtLowPt;}; // if e_pt < 20 go to first bin by setting searchPtLowPt to 20
  }
  //if (type=="Trigger"){
    //searchPt=TMath::Min( electronPt , electronMaxPtHigh ); // if pt > 200 use overflow bin by setting searchPt to 201
  //}
  

  float nomval = 0;
  float error = 0;
  float upval = 0;
  float downval= 0;
  float nomvalBtoF = 0;
  float errorBtoF = 0;
  float upvalBtoF = 0;
  float downvalBtoF= 0;
//   float nomvalGtoH = 0;
//   float errorGtoH = 0;
//   float upvalGtoH = 0;
//   float downvalGtoH= 0;


  if ( type == "ID" ){

    thisBin = h_ele_ID_abseta_pt_ratioBtoF->FindBin( searchEta , searchPt );
    nomvalBtoF=h_ele_ID_abseta_pt_ratioBtoF->GetBinContent( thisBin );
    errorBtoF=h_ele_ID_abseta_pt_ratioBtoF->GetBinError( thisBin );
    upvalBtoF=nomvalBtoF+errorBtoF;
    downvalBtoF=nomvalBtoF-errorBtoF;
    
//     thisBin = h_ele_ID_abseta_pt_ratioGtoH->FindBin( searchEta , searchPt );
//     nomvalGtoH=h_ele_ID_abseta_pt_ratioGtoH->GetBinContent( thisBin );
//     errorGtoH=h_ele_ID_abseta_pt_ratioGtoH->GetBinError( thisBin );
//     upvalGtoH=nomvalGtoH+errorGtoH;
//     downvalGtoH=nomvalGtoH-errorGtoH;
    
    nomval=nomvalBtoF;
    upval=upvalBtoF;
    downval=downvalBtoF;

  }
  else if ( type == "Trigger" ){

    thisBin = h_ele_TRIGGER_abseta_pt_ratio->FindBin( searchPt, searchEta );
    nomval=h_ele_TRIGGER_abseta_pt_ratio->GetBinContent( thisBin );
    error=h_ele_TRIGGER_abseta_pt_ratio->GetBinError( thisBin );
    upval=nomval+error;
    downval=nomval-error;


  }
  else if ( type == "Iso" ){
   // // NOT AVAILABLE at the moment
   // thisBin = h_ele_ISO_abseta_pt_ratio->FindBin( searchEta , searchPt );
   // nomval=h_ele_ISO_abseta_pt_ratio->GetBinContent( thisBin );
   // error=h_ele_ISO_abseta_pt_ratio->GetBinError( thisBin );
   // upval=nomval+error;  //DANGERZONE need to add pT depnednet 1% uncertainty
   // downval=nomval-error;
   // if(electronPt<20 || electronPt>80) {
   //     upval=upval*( 1.0+sqrt(0.01*0.01) );
   //     downval=downval*( 1.0-sqrt(0.01*0.01) );
   // }

  }
  else if ( type == "GFS" ){
    TH2F* current_reco_histo; //create pt dependend TH2F histo pointer to avoid copy-pasting the same code
    if(electronPt<electronLowPtRangeCut){ current_reco_histo = h_ele_GFS_abseta_pt_ratio_lowEt;}
    else  {current_reco_histo = h_ele_GFS_abseta_pt_ratio;}
    thisBin = current_reco_histo->FindBin( searchEta , searchPt );
    nomval=current_reco_histo->GetBinContent( thisBin );
    error=current_reco_histo->GetBinError( thisBin );
    upval=nomval+error; //DANGERZONE need to add pT depnednet 1% uncertainty
    downval=nomval-error;
    // if(electronPt<20 || electronPt>80) {
    //     upval=upval*( 1.0+sqrt(0.01*0.01) );
    //     downval=downval*( 1.0-sqrt(0.01*0.01) );
    // }

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
  if(searchEta>=muonMaxEta){searchEta=muonMaxEta;}
  float searchPt=TMath::Min( muonPt , muonMaxPt ); // if muonpt > 119 use last bin
  searchPt=TMath::Max(searchPt, muonMinPt);
  if (type=="Trigger"){
    searchPt=TMath::Min( muonPt , muonMaxPtHigh );// Trigger SF goes from 30 to 1119.0 GeV
    searchPt=TMath::Max( searchPt, muonMinPtHigh);
  }
  float nomval = 0;
  //float error = 0;
  float upval = 0;
  float downval= 0;
  float nomvalBtoF = 0;
  float errorBtoF = 0;
  float upvalBtoF = 0;
  float downvalBtoF= 0;
//   float nomvalGtoH = 0;
//   float errorGtoH = 0;
//   float upvalGtoH = 0;
//   float downvalGtoH= 0;
  

  if ( type == "ID" ){

    thisBin = h_mu_ID_abseta_pt_ratioBtoF->FindBin(  searchPt, searchEta  );
    nomvalBtoF=h_mu_ID_abseta_pt_ratioBtoF->GetBinContent( thisBin );
    errorBtoF=h_mu_ID_abseta_pt_ratioBtoF->GetBinError( thisBin );
    // current histogram contains systematic and statistical errors added in quadrature
    upvalBtoF=( nomvalBtoF+errorBtoF );
    downvalBtoF=( nomvalBtoF-errorBtoF );

    nomval=nomvalBtoF;
    upval=upvalBtoF;
    downval=downvalBtoF;

  }
  else if ( type == "Trigger" ){

    thisBin = h_mu_TRIGGER_abseta_ptBtoF->FindBin(  searchPt, searchEta  );
    nomvalBtoF=h_mu_TRIGGER_abseta_ptBtoF->GetBinContent( thisBin );
    errorBtoF=h_mu_TRIGGER_abseta_ptBtoF->GetBinError( thisBin );
    upvalBtoF=( nomvalBtoF+errorBtoF );
    downvalBtoF=( nomvalBtoF-errorBtoF );
    
//     thisBin = h_mu_TRIGGER_abseta_ptGtoH->FindBin(  searchPt, searchEta  );
//     nomvalGtoH=h_mu_TRIGGER_abseta_ptGtoH->GetBinContent( thisBin );
//     errorGtoH=h_mu_TRIGGER_abseta_ptGtoH->GetBinError( thisBin );
//     upvalGtoH=( nomvalGtoH+errorGtoH );
//     downvalGtoH=( nomvalGtoH-errorGtoH );

    nomval=nomvalBtoF;
    upval=upvalBtoF;
    downval=downvalBtoF;
    
  }
  else if ( type == "Iso" ){
    
    
    thisBin = h_mu_ISO_abseta_pt_ratioBtoF->FindBin(  searchPt, searchEta  );
    nomvalBtoF=h_mu_ISO_abseta_pt_ratioBtoF->GetBinContent( thisBin );
    errorBtoF=h_mu_ISO_abseta_pt_ratioBtoF->GetBinError( thisBin );
    // current histogram contains systematic and statistical errors added in quadrature
    upvalBtoF=( nomvalBtoF+errorBtoF );
    downvalBtoF=( nomvalBtoF-errorBtoF );

    nomval=nomvalBtoF;
    upval=upvalBtoF;
    downval=downvalBtoF;

  }

  else if ( type == "HIP" ){
    // NOT AVAILABLE at the moment
    //thisBin = findPoint(h_mu_HIP_eta_ratioBtoF,searchEta );
    //nomvalBtoF=getValue(*h_mu_HIP_eta_ratioBtoF,searchEta,0);
    //errorBtoF=h_mu_HIP_eta_ratioBtoF->GetBinError( thisBin );
    //upvalBtoF=getValue(*h_mu_HIP_eta_ratioBtoF,searchEta,1);
    //downvalBtoF=getValue(*h_mu_HIP_eta_ratioBtoF,searchEta,-1);
    
//     //thisBin = h_mu_HIP_eta_ratioGtoH->FindBin( searchEta );
//     nomvalGtoH=getValue(*h_mu_HIP_eta_ratioGtoH,searchEta,0);
//     //errorGtoH=h_mu_HIP_eta_ratioGtoH->GetBinError( thisBin );
//     upvalGtoH=getValue(*h_mu_HIP_eta_ratioGtoH,searchEta,1);
//     downvalGtoH=getValue(*h_mu_HIP_eta_ratioGtoH,searchEta,-1);
    
    //nomval=nomvalBtoF;
    //upval=upvalBtoF;
    //downval=downvalBtoF;
   
//     upval=upval*( 1.0+0.005 );
//     downval=downval*( 1.0-0.005 );


  }
  else {

    std::cout << "Unknown Type. Supported Types are: ID, Trigger, Iso, HIP" << std::endl;
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
    std::string ISOinputFileBtoF =  plotscriptBaseDir+"/data/triggerSFs/mu_ISO_EfficienciesAndSF_BCDEF.root";
//     std::string ISOinputFileGtoH =  "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Summer18_2017data/oct202017/mu_ISO_EfficienciesAndSF_GH.root";
    TFile *f_ISOSFBtoF = new TFile(std::string(ISOinputFileBtoF).c_str(),"READ");
//     TFile *f_ISOSFGtoH = new TFile(std::string(ISOinputFileGtoH).c_str(),"READ");
    if(is_DL) {
        h_mu_ISO_abseta_pt_ratioBtoF=(TH2F*)f_ISOSFBtoF->Get("LooseISO_TightID_pt_eta/pt_abseta_ratio");
//         h_mu_ISO_abseta_pt_ratioGtoH=(TH2F*)f_ISOSFGtoH->Get("LooseISO_TightID_pt_eta/pt_abseta_ratio");
    }
    else {
        h_mu_ISO_abseta_pt_ratioBtoF=(TH2F*)f_ISOSFBtoF->Get("TightISO_TightID_pt_eta/pt_abseta_ratio");
//         h_mu_ISO_abseta_pt_ratioGtoH=(TH2F*)f_ISOSFGtoH->Get("TightISO_TightID_pt_eta/pt_abseta_ratio");
    }
    delete f_ISOSFBtoF;
//     delete f_ISOSFGtoH;
}

//PRIVATE

void LeptonSFHelper::SetElectronHistos( ){
  
  std::string IDinputFileBtoF = plotscriptBaseDir+"/data/LeptonSFs/egammaEffi.txt_EGM2D_runBCDEF_passingTight94X.root";
  // std::string IDinputFileGtoH = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Summer18_2017data/oct202017/ele_ID_SF_tight_GH.root";

  std::string TRIGGERinputFile = "";
  std::string TRIGGERhistName  = "";
  if( dataera == "2017" || dataera == "2017_deepCSV") {
      TRIGGERinputFile = plotscriptBaseDir+"/data/triggerSFs/SingleEG_JetHT_Trigger_Scale_Factors_ttHbb2017_v3.root";
      TRIGGERhistName  = "ele28_ht150_OR_ele32_ele_pt_ele_sceta";
      }
  else if( dataera == "2018" || dataera == "2018_deepCSV" ) {
      TRIGGERinputFile = plotscriptBaseDir+"/data/triggerSFs/SingleEG_JetHT_Trigger_Scale_Factors_ttHbb2018_v3.root";
      TRIGGERhistName  = "ele28_ht150_OR_ele32_ele_pt_ele_sceta";
      }
  else if( dataera == "2016" || dataera == "2016_deepCSV" ) {
      TRIGGERinputFile = plotscriptBaseDir+"/data/triggerSFs/SingleEG_JetHT_Trigger_Scale_Factors_ttHbb2016_v4.root";
      TRIGGERhistName  = "ele27_ele_pt_ele_sceta";
      }

  //std::string ISOinputFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Summer18_2017data/oct202017/ele_Reco_EGM2D.root"; // DANGERZONE: no iso SF yet??
  std::string GFSinputFile = plotscriptBaseDir+"/data/LeptonSFs/egammaEffi.txt_EGM2D_runBCDEF_passingRECO.root"; //reco SFs for pt > 20
  std::string GFSinputFile_lowEt = plotscriptBaseDir+"/data/LeptonSFs/egammaEffi.txt_EGM2D_runBCDEF_passingRECO_lowEt.root"; //reco SFs for pt<20
  // std::string TRIGGERinputFile = GFSinputFile;  //not available yet
  // std::string ISOinputFile = GFSinputFile;      //not available yet

  TFile *f_IDSFBtoF = new TFile(std::string(IDinputFileBtoF).c_str(),"READ");
  //TFile *f_IDSFGtoH = new TFile(std::string(IDinputFileGtoH).c_str(),"READ");
  
  TFile *f_TRIGGERSF = new TFile(std::string(TRIGGERinputFile).c_str(),"READ");
  //TFile *f_ISOSF = new TFile(std::string(ISOinputFile).c_str(),"READ");
  TFile *f_GFSSF = new TFile(std::string(GFSinputFile).c_str(),"READ");
  TFile *f_GFSSF_lowEt = new TFile(std::string(GFSinputFile_lowEt).c_str(),"READ");

  //h_ele_ID_abseta_pt_ratioGtoH=(TH2F*)f_IDSFGtoH->Get("EGamma_SF2D");
  h_ele_ID_abseta_pt_ratioBtoF=(TH2F*)f_IDSFBtoF->Get("EGamma_SF2D");
  h_ele_TRIGGER_abseta_pt_ratio = (TH2F*)f_TRIGGERSF->Get(std::string(TRIGGERhistName).c_str());
  //h_ele_ISO_abseta_pt_ratio = (TH2F*)f_ISOSF->Get("EGamma_SF2D");
  h_ele_GFS_abseta_pt_ratio = (TH2F*)f_GFSSF->Get("EGamma_SF2D");
  h_ele_GFS_abseta_pt_ratio_lowEt = (TH2F*)f_GFSSF_lowEt->Get("EGamma_SF2D");

}

void LeptonSFHelper::SetMuonHistos( ){

  std::string IDinputFileBtoF = plotscriptBaseDir+"/data/LeptonSFs/Muon_RunBCDEF_SF_ID_syst.root";
  
  std::string ISOinputFileBtoF =  plotscriptBaseDir+"/data/LeptonSFs/Muon_RunBCDEF_SF_ISO_syst.root";
  
  std::string TRIGGERinputFileBtoF =  plotscriptBaseDir+"/data/LeptonSFs/Muon_Trigger_SF_EfficienciesAndSF_RunBtoF_Nov17Nov2017.root";
  
  TFile *f_IDSFBtoF = new TFile(std::string(IDinputFileBtoF).c_str(),"READ");
  
  TFile *f_ISOSFBtoF = new TFile(std::string(ISOinputFileBtoF).c_str(),"READ");
  
  TFile *f_TRIGGERSFBtoF = new TFile(std::string(TRIGGERinputFileBtoF).c_str(),"READ");
  
  h_mu_TRIGGER_abseta_ptBtoF= (TH2F*)f_TRIGGERSFBtoF->Get("IsoMu27_PtEtaBins/pt_abseta_ratio");
  
  h_mu_ID_abseta_pt_ratioBtoF = (TH2F*)f_IDSFBtoF->Get("NUM_TightID_DEN_genTracks_pt_abseta");
  
  h_mu_ISO_abseta_pt_ratioBtoF = (TH2F*)f_ISOSFBtoF->Get("NUM_TightRelIso_DEN_TightIDandIPCut_pt_abseta");
  
}

void LeptonSFHelper::SetElectronElectronHistos( ){
  std::string TRIGGERinputFile = plotscriptBaseDir+"/data/triggerSFs/triggerSummary_ee_ReReco2016_ttH.root";

  TFile *f_TRIGGERSF = new TFile(std::string(TRIGGERinputFile).c_str(),"READ");

  h_ele_ele_TRIGGER_abseta_abseta = (TH2F*)f_TRIGGERSF->Get("scalefactor_eta2d_with_syst");
}

void LeptonSFHelper::SetMuonMuonHistos( ){
  std::string TRIGGERinputFile = plotscriptBaseDir+"/data/triggerSFs/triggerSummary_mumu_ReReco2016_ttH.root";

  TFile *f_TRIGGERSF = new TFile(std::string(TRIGGERinputFile).c_str(),"READ");

  h_mu_mu_TRIGGER_abseta_abseta = (TH2F*)f_TRIGGERSF->Get("scalefactor_eta2d_with_syst");
}

void LeptonSFHelper::SetElectronMuonHistos( ){
  std::string TRIGGERinputFile = plotscriptBaseDir+"/data/triggerSFs/triggerSummary_emu_ReReco2016_ttH.root";

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

