  
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

};

//PUBLIC
LeptonSFHelper::LeptonSFHelper( ){

  //std::cout << "Initializing Lepton scale factors" << std::endl;

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
    std::string ISOinputFileBtoF =  "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Summer18_2017data/oct202017/mu_ISO_EfficienciesAndSF_BCDEF.root";
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

  std::string IDinputFileBtoF = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Summer18_2017data/Fall17/egammaEffi.txt_EGM2D_runBCDEF_passingTight94X.root";
  // std::string IDinputFileGtoH = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Summer18_2017data/oct202017/ele_ID_SF_tight_GH.root";

  std::string TRIGGERinputFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Summer18_2017data/Fall17/SingleEG_JetHT_Trigger_Scale_Factors_ttHbb_Data_MC_v2.0.root";
  //std::string ISOinputFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Summer18_2017data/oct202017/ele_Reco_EGM2D.root"; // DANGERZONE: no iso SF yet??
  std::string GFSinputFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Summer18_2017data/Fall17/egammaEffi.txt_EGM2D_runBCDEF_passingRECO.root"; //reco SFs for pt > 20
  std::string GFSinputFile_lowEt = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Summer18_2017data/Fall17/egammaEffi.txt_EGM2D_runBCDEF_passingRECO_lowEt.root"; //reco SFs for pt<20
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
  h_ele_TRIGGER_abseta_pt_ratio = (TH2F*)f_TRIGGERSF->Get("SFs_ele_pt_ele_sceta_ele28_ht150_OR_ele35_2017BCDEF");
  //h_ele_ISO_abseta_pt_ratio = (TH2F*)f_ISOSF->Get("EGamma_SF2D");
  h_ele_GFS_abseta_pt_ratio = (TH2F*)f_GFSSF->Get("EGamma_SF2D");
  h_ele_GFS_abseta_pt_ratio_lowEt = (TH2F*)f_GFSSF_lowEt->Get("EGamma_SF2D");

}

void LeptonSFHelper::SetMuonHistos( ){

  std::string IDinputFileBtoF = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Summer18_2017data/Fall17/MuonIDSF_Errors_RunBtoF_Nov17Nov2017.root";
  
  std::string ISOinputFileBtoF =  "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Summer18_2017data/Fall17/MuonIsoSF_Errors_RunBtoF_Nov17Nov2017.root";
  
  std::string TRIGGERinputFileBtoF =  "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Summer18_2017data/Fall17/MuonTriggerSF_RunBtoF_Nov17Nov2017.root";
  
  TFile *f_IDSFBtoF = new TFile(std::string(IDinputFileBtoF).c_str(),"READ");
  
  TFile *f_ISOSFBtoF = new TFile(std::string(ISOinputFileBtoF).c_str(),"READ");
  
  TFile *f_TRIGGERSFBtoF = new TFile(std::string(TRIGGERinputFileBtoF).c_str(),"READ");
  
  h_mu_TRIGGER_abseta_ptBtoF= (TH2F*)f_TRIGGERSFBtoF->Get("IsoMu27_PtEtaBins/pt_abseta_ratio");
  
  h_mu_ID_abseta_pt_ratioBtoF = (TH2F*)f_IDSFBtoF->Get("NUM_TightID_DEN_genTracks_pt_abseta");
  
  h_mu_ISO_abseta_pt_ratioBtoF = (TH2F*)f_ISOSFBtoF->Get("NUM_TightRelIso_DEN_TightIDandIPCut_pt_abseta");
  
}

void LeptonSFHelper::SetElectronElectronHistos( ){
  std::string TRIGGERinputFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Summer18_2017data/oct202017/triggerSummary_ee_ReReco2016_ttH.root";

  TFile *f_TRIGGERSF = new TFile(std::string(TRIGGERinputFile).c_str(),"READ");

  h_ele_ele_TRIGGER_abseta_abseta = (TH2F*)f_TRIGGERSF->Get("scalefactor_eta2d_with_syst");
}

void LeptonSFHelper::SetMuonMuonHistos( ){
  std::string TRIGGERinputFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Summer18_2017data/oct202017/triggerSummary_mumu_ReReco2016_ttH.root";

  TFile *f_TRIGGERSF = new TFile(std::string(TRIGGERinputFile).c_str(),"READ");

  h_mu_mu_TRIGGER_abseta_abseta = (TH2F*)f_TRIGGERSF->Get("scalefactor_eta2d_with_syst");
}

void LeptonSFHelper::SetElectronMuonHistos( ){
  std::string TRIGGERinputFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Summer18_2017data/oct202017/triggerSummary_emu_ReReco2016_ttH.root";

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

