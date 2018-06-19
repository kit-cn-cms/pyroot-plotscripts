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
      if( allowJetsOutOfBinning_ ) continue;
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

class ttbarsysthelper
{
    public:
        ttbarsysthelper();
        ~ttbarsysthelper();
        float GetISRScaleFactorUp(int& ttbar_subprocess,int& njets);
        float GetISRScaleFactorDown(int& ttbar_subprocess,int& njets);
        float GetFSRScaleFactorUp(int& ttbar_subprocess,int& njets);
        float GetFSRScaleFactorDown(int& ttbar_subprocess,int& njets);
        float GetHDAMPScaleFactorUp(int& ttbar_subprocess,int& njets);
        float GetHDAMPScaleFactorDown(int& ttbar_subprocess,int& njets);
        float GetUEScaleFactorUp(int& ttbar_subprocess,int& njets);
        float GetUEScaleFactorDown(int& ttbar_subprocess,int& njets);
        int GetTtbarSubProcess(int& GenEvt_I_TTPlusCC,int& GenEvt_I_TTPlusBB);
    
    private:
        // int is number of jets and float the corresponding scale factor
        std::map<std::pair<int,int>,float> ISRUp;
        std::map<std::pair<int,int>,float> ISRDown;
        std::map<std::pair<int,int>,float> FSRUp;
        std::map<std::pair<int,int>,float> FSRDown;
        std::map<std::pair<int,int>,float> HDAMPUp;
        std::map<std::pair<int,int>,float> HDAMPDown;
        std::map<std::pair<int,int>,float> UEUp;
        std::map<std::pair<int,int>,float> UEDown;
        
};

ttbarsysthelper::ttbarsysthelper()
{
    // first number in pair: 0->ttlf,1->ttcc,2->ttb,3->tt2b,4->ttbb
    // second number in pair: njets
    ISRUp[std::pair<int,int>(0,4)] = 0.987;
    ISRUp[std::pair<int,int>(0,5)] = 1.007;
    ISRUp[std::pair<int,int>(0,6)] = 1.062;
    ISRUp[std::pair<int,int>(1,4)] = 1.013;
    ISRUp[std::pair<int,int>(1,5)] = 1.013;
    ISRUp[std::pair<int,int>(1,6)] = 1.078;
    ISRUp[std::pair<int,int>(2,4)] = 1.016;
    ISRUp[std::pair<int,int>(2,5)] = 1.025;
    ISRUp[std::pair<int,int>(2,6)] = 1.09;
    ISRUp[std::pair<int,int>(3,4)] = 0.932;
    ISRUp[std::pair<int,int>(3,5)] = 1.025;
    ISRUp[std::pair<int,int>(3,6)] = 1.055;
    ISRUp[std::pair<int,int>(4,4)] = 1.024;
    ISRUp[std::pair<int,int>(4,5)] = 1.02;
    ISRUp[std::pair<int,int>(4,6)] = 1.074;
    
    ISRDown[std::pair<int,int>(0,4)] = 1.006;
    ISRDown[std::pair<int,int>(0,5)] = 0.969;
    ISRDown[std::pair<int,int>(0,6)] = 0.929;
    ISRDown[std::pair<int,int>(1,4)] = 0.969;
    ISRDown[std::pair<int,int>(1,5)] = 0.958;
    ISRDown[std::pair<int,int>(1,6)] = 0.91;
    ISRDown[std::pair<int,int>(2,4)] = 0.982;
    ISRDown[std::pair<int,int>(2,5)] = 0.973;
    ISRDown[std::pair<int,int>(2,6)] = 0.902;
    ISRDown[std::pair<int,int>(3,4)] = 1.024;
    ISRDown[std::pair<int,int>(3,5)] = 0.977;
    ISRDown[std::pair<int,int>(3,6)] = 0.936;
    ISRDown[std::pair<int,int>(4,4)] = 0.967;
    ISRDown[std::pair<int,int>(4,5)] = 0.948;
    ISRDown[std::pair<int,int>(4,6)] = 0.888;
    
    FSRUp[std::pair<int,int>(0,4)] = 0.817;
    FSRUp[std::pair<int,int>(0,5)] = 0.765;
    FSRUp[std::pair<int,int>(0,6)] = 0.75;
    FSRUp[std::pair<int,int>(1,4)] = 1.061;
    FSRUp[std::pair<int,int>(1,5)] = 1.013;
    FSRUp[std::pair<int,int>(1,6)] = 1.023;
    FSRUp[std::pair<int,int>(2,4)] = 1.018;
    FSRUp[std::pair<int,int>(2,5)] = 1.015;
    FSRUp[std::pair<int,int>(2,6)] = 1.01;
    FSRUp[std::pair<int,int>(3,4)] = 1.067;
    FSRUp[std::pair<int,int>(3,5)] = 1.031;
    FSRUp[std::pair<int,int>(3,6)] = 1.067;
    FSRUp[std::pair<int,int>(4,4)] = 1.024;
    FSRUp[std::pair<int,int>(4,5)] = 1.019;
    FSRUp[std::pair<int,int>(4,6)] = 1.06;
    
    FSRDown[std::pair<int,int>(0,4)] = 1.029;
    FSRDown[std::pair<int,int>(0,5)] = 1.052;
    FSRDown[std::pair<int,int>(0,6)] = 1.073;
    FSRDown[std::pair<int,int>(1,4)] = 0.858;
    FSRDown[std::pair<int,int>(1,5)] = 0.885;
    FSRDown[std::pair<int,int>(1,6)] = 0.846;
    FSRDown[std::pair<int,int>(2,4)] = 0.906;
    FSRDown[std::pair<int,int>(2,5)] = 0.908;
    FSRDown[std::pair<int,int>(2,6)] = 0.893;
    FSRDown[std::pair<int,int>(3,4)] = 0.795;
    FSRDown[std::pair<int,int>(3,5)] = 0.865;
    FSRDown[std::pair<int,int>(3,6)] = 0.844;
    FSRDown[std::pair<int,int>(4,4)] = 0.841;
    FSRDown[std::pair<int,int>(4,5)] = 0.871;
    FSRDown[std::pair<int,int>(4,6)] = 0.853;
    
    HDAMPUp[std::pair<int,int>(0,4)] = 0.994;
    HDAMPUp[std::pair<int,int>(0,5)] = 1.008;
    HDAMPUp[std::pair<int,int>(0,6)] = 1.029;
    HDAMPUp[std::pair<int,int>(1,4)] = 1.013;
    HDAMPUp[std::pair<int,int>(1,5)] = 1.013;
    HDAMPUp[std::pair<int,int>(1,6)] = 1.042;
    HDAMPUp[std::pair<int,int>(2,4)] = 1.016;
    HDAMPUp[std::pair<int,int>(2,5)] = 1.034;
    HDAMPUp[std::pair<int,int>(2,6)] = 1.046;
    HDAMPUp[std::pair<int,int>(3,4)] = 1.024;
    HDAMPUp[std::pair<int,int>(3,5)] = 1.023;
    HDAMPUp[std::pair<int,int>(3,6)] = 1.07;
    HDAMPUp[std::pair<int,int>(4,4)] = 1.038;
    HDAMPUp[std::pair<int,int>(4,5)] = 1.018;
    HDAMPUp[std::pair<int,int>(4,6)] = 1.041;
    
    HDAMPDown[std::pair<int,int>(0,4)] = 1.006;
    HDAMPDown[std::pair<int,int>(0,5)] = 0.971;
    HDAMPDown[std::pair<int,int>(0,6)] = 0.935;
    HDAMPDown[std::pair<int,int>(1,4)] = 0.965;
    HDAMPDown[std::pair<int,int>(1,5)] = 0.97;
    HDAMPDown[std::pair<int,int>(1,6)] = 0.932;
    HDAMPDown[std::pair<int,int>(2,4)] = 0.978;
    HDAMPDown[std::pair<int,int>(2,5)] = 0.949;
    HDAMPDown[std::pair<int,int>(2,6)] = 0.919;
    HDAMPDown[std::pair<int,int>(3,4)] = 0.922;
    HDAMPDown[std::pair<int,int>(3,5)] = 0.917;
    HDAMPDown[std::pair<int,int>(3,6)] = 0.942;
    HDAMPDown[std::pair<int,int>(4,4)] = 0.938;
    HDAMPDown[std::pair<int,int>(4,5)] = 0.927;
    HDAMPDown[std::pair<int,int>(4,6)] = 0.918;
    
    UEUp[std::pair<int,int>(0,4)] = 0.994;
    UEUp[std::pair<int,int>(0,5)] = 0.989;
    UEUp[std::pair<int,int>(0,6)] = 1.003;
    UEUp[std::pair<int,int>(1,4)] = 1.013;
    UEUp[std::pair<int,int>(1,5)] = 1.013;
    UEUp[std::pair<int,int>(1,6)] = 1.005;
    UEUp[std::pair<int,int>(2,4)] = 0.984;
    UEUp[std::pair<int,int>(2,5)] = 1.016;
    UEUp[std::pair<int,int>(2,6)] = 1.01;
    UEUp[std::pair<int,int>(3,4)] = 0.976;
    UEUp[std::pair<int,int>(3,5)] = 0.977;
    UEUp[std::pair<int,int>(3,6)] = 1.013;
    UEUp[std::pair<int,int>(4,4)] = 0.976;
    UEUp[std::pair<int,int>(4,5)] = 0.98;
    UEUp[std::pair<int,int>(4,6)] = 1.01;
    
    UEDown[std::pair<int,int>(0,4)] = 1.006;
    UEDown[std::pair<int,int>(0,5)] = 1.008;
    UEDown[std::pair<int,int>(0,6)] = 0.997;
    UEDown[std::pair<int,int>(1,4)] = 0.974;
    UEDown[std::pair<int,int>(1,5)] = 0.987;
    UEDown[std::pair<int,int>(1,6)] = 0.983;
    UEDown[std::pair<int,int>(2,4)] = 1.017;
    UEDown[std::pair<int,int>(2,5)] = 0.984;
    UEDown[std::pair<int,int>(2,6)] = 0.988;
    UEDown[std::pair<int,int>(3,4)] = 1.024;
    UEDown[std::pair<int,int>(3,5)] = 1.023;
    UEDown[std::pair<int,int>(3,6)] = 0.987;
    UEDown[std::pair<int,int>(4,4)] = 1.024;
    UEDown[std::pair<int,int>(4,5)] = 1.019;
    UEDown[std::pair<int,int>(4,6)] = 0.99;
}



ttbarsysthelper::~ttbarsysthelper()
{
    // nothing to do here
}

float ttbarsysthelper::GetISRScaleFactorUp(int& ttbar_subprocess,int& njets)
{
    return njets<6 ? ISRUp[std::pair<int,int>(ttbar_subprocess,njets)] : ISRUp[std::pair<int,int>(ttbar_subprocess,6)];
}
float ttbarsysthelper::GetISRScaleFactorDown(int& ttbar_subprocess,int& njets)
{
    return njets<6 ? ISRDown[std::pair<int,int>(ttbar_subprocess,njets)] : ISRDown[std::pair<int,int>(ttbar_subprocess,6)];
}
float ttbarsysthelper::GetFSRScaleFactorUp(int& ttbar_subprocess,int& njets)
{
    return njets<6 ? FSRUp[std::pair<int,int>(ttbar_subprocess,njets)] : FSRUp[std::pair<int,int>(ttbar_subprocess,6)];
}
float ttbarsysthelper::GetFSRScaleFactorDown(int& ttbar_subprocess,int& njets)
{
    return njets<6 ? FSRDown[std::pair<int,int>(ttbar_subprocess,njets)] : FSRDown[std::pair<int,int>(ttbar_subprocess,6)];
}
float ttbarsysthelper::GetHDAMPScaleFactorUp(int& ttbar_subprocess,int& njets)
{
    return njets<6 ? HDAMPUp[std::pair<int,int>(ttbar_subprocess,njets)] : HDAMPUp[std::pair<int,int>(ttbar_subprocess,6)];
}
float ttbarsysthelper::GetHDAMPScaleFactorDown(int& ttbar_subprocess,int& njets)
{
    return njets<6 ? HDAMPDown[std::pair<int,int>(ttbar_subprocess,njets)] : HDAMPDown[std::pair<int,int>(ttbar_subprocess,6)];
}
float ttbarsysthelper::GetUEScaleFactorUp(int& ttbar_subprocess,int& njets)
{
    return njets<6 ? UEUp[std::pair<int,int>(ttbar_subprocess,njets)] : UEUp[std::pair<int,int>(ttbar_subprocess,6)];
}
float ttbarsysthelper::GetUEScaleFactorDown(int& ttbar_subprocess,int& njets)
{
    return njets<6 ? UEDown[std::pair<int,int>(ttbar_subprocess,njets)] : UEDown[std::pair<int,int>(ttbar_subprocess,6)];
}

int ttbarsysthelper::GetTtbarSubProcess(int& GenEvt_I_TTPlusCC,int& GenEvt_I_TTPlusBB)
{
    // translate the flags available in the ntuples to the flag needed above for the ttbar subprocesses
    int i;
    if(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0) 
    {
        i=0;
    }
    else if(GenEvt_I_TTPlusCC==1)
    {
        i=1;
    }
    else if(GenEvt_I_TTPlusBB==1)
    {
        i=2;
    }
    else if(GenEvt_I_TTPlusBB==2)
    {
        i=3;
    }
    else if(GenEvt_I_TTPlusBB==3)
    {
        i=4;
    }
    else
    {
        std::cout << "!!! Error something went wrong during ttbar subprocess classification !!!" << std::endl;
        i=-1;
    }
    return i;
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

  std::string csvHFfile="/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/factorized_jes/csv_rwt_fit_hf_v2_final_2017_6_7_all.root";
  std::string csvLFfile="/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/factorized_jes/csv_rwt_fit_lf_v2_final_2017_6_7_all.root";
  TString qcd_file = "/nfs/dust/cms/user/mwassmer/QCD_Estimation_September17/QCD_Estimation/QCD_Estimation_FakeScaleFactor_nominal.root";
  
  CSVHelper* internalCSVHelper= new CSVHelper(csvHFfile,csvLFfile, 5,4,3,v_SystTypes);
  LeptonSFHelper* internalLeptonSFHelper= new LeptonSFHelper();
  QCDHelper* internalQCDHelper = new QCDHelper(qcd_file);
  ttbarsysthelper* internalttbarsysthelper = new ttbarsysthelper();

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

  //initialize Trigger Helper

  // Hack for subsampling test
  //if(processname=="SingleEl" || processname=="SingleMu"){DoWeights=0; std::cout<<"is data, dont use nominal weihgts"<<std::endl;}
  if((processname.find("SingleEl")!= std::string::npos) || (processname.find("SingleMu")!= std::string::npos)){DoWeights=0; std::cout<<"is data, dont use nominal weights!!!!"<<std::endl;}


  // read in samples to add to chain and get relevant names for the database
  std::map<TString, TString> sampleDataBaseIdentifiers;
  std::map<TString, std::map<TString, long>> sampleDataBaseFoundEvents;
  std::map<TString, std::map<TString, long>> sampleDataBaseLostEvents;
  std::map<TString, TString> sampleTranslationMapCC ;

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
