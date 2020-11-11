// struct to store information 1D histograms
struct Plot1DInfoStruct{
    std::string identifier;
    std::string title;
    int nbins;
    std::vector<float> edges;
    //std::unique_ptr<TH1> histoptr;
};


// Helper struct to fill plots more efficiently
// Until GCC 4.9 struct cannot have init values if one wants to initialize it with bracket lists
struct structHelpFillHisto{
  TH1* histo;
  double weight;
};

// helper function to fill plots more efficiently
void helperFillHisto(const std::vector<structHelpFillHisto>& paramVec, const double& val)
{
  for (const auto &singleParams: paramVec)
  // singleParams: histo, var, weight
  {
    if((singleParams.weight)!=0)
        singleParams.histo->Fill(fmin(singleParams.histo->GetXaxis()->GetXmax()-1e-6,fmax(singleParams.histo->GetXaxis()->GetXmin()+1e-6,val)),singleParams.weight);
  }
}

// Helper struct to fill plots more efficiently
// Until GCC 4.9 struct cannot have init values if one wants to initialize it with bracket lists
struct Plot2DInfoStruct{
    std::string identifier;
    std::string title;
    int nbinsx;
    std::vector<float> edges_x;
    int nbinsy;
    std::vector<float> edges_y;
    //std::unique_ptr<TH2> histoptr;
};

struct structHelpFillTwoDimHisto{
  TH2* histo;
  double weight;
};

// helper function to fill plots more efficiently
void helperFillTwoDimHisto(const std::vector<structHelpFillTwoDimHisto>& paramVec, const double& val1, const double& val2)
{
  for (const auto &singleParams: paramVec)
  // singleParams: histo, var1, var2, weight
  {
    if((singleParams.weight)!=0)
        singleParams.histo->Fill(fmin(singleParams.histo->GetXaxis()->GetXmax()-1e-6,fmax(singleParams.histo->GetXaxis()->GetXmin()+1e-6,val1)),fmin(singleParams.histo->GetYaxis()->GetXmax()-1e-6,fmax(singleParams.histo->GetYaxis()->GetXmin()+1e-6,val2)),singleParams.weight);
  }
}

void resetMap(std::map<TString, float>& input, const float& val = 1){
  for(auto& entry : input){
    entry.second = val;
  }
}

void plot(){
  TH1F::SetDefaultSumw2();

  // open files
  TChain* chain = new TChain("MVATree");
//PLACEHOLDERFRIENDTREEINIT

  char* filenames = getenv ("FILENAMES");
  char* outfilename = getenv ("OUTFILENAME");
  std::string plotscriptBaseDir = getenv ("PLOTSCRIPTBASEDIR");
  string processname = string(getenv ("PROCESSNAME"));
  string suffix = string(getenv ("SUFFIX"));
  int maxevents = atoi(getenv ("MAXEVENTS"));
  int skipevents = atoi(getenv ("SKIPEVENTS"));
  string eventFilterFile = string(getenv("EVENTFILTERFILE"));
  std::string dataera = string(getenv ("DATAERA"));
  std::string variation = string(getenv ("VARIATION"));
  std::string origName = string(getenv ("ORIGNAME"));

  // create vector of systematics

  std::cout<<"processname: " <<processname<<std::endl;
  std::cout<<"suffix: " <<suffix<<std::endl;
  bool skipWeightSysts = false;
  if (variation != "") {
    skipWeightSysts = true;
  }
  if (TString(processname).Contains("SingleMu") or TString(processname).Contains("SingleEl") or TString(processname).Contains("EGamma") or TString(processname).Contains("MET")){
    std::cout << "Detected Data Sample, going to skip weight systematics" << std::endl;
    skipWeightSysts = true;
  }

  if (skipWeightSysts) {
    std::cout << "Detected syst varied or Data Sample, going to skip weight systematics" << std::endl;
  }

  // create event filter class
  //EventFilter* evtFilter = new EventFilter(eventFilterFile);

  int eventsAnalyzed=0;
  float sumOfWeights=0;

  int DoWeights=1;
  int electron_data=0;
  int muon_data=0;

  // Hack for subsampling test
  if((processname.find("SingleEl")!= std::string::npos) || (processname.find("SingleMu")!= std::string::npos) || (processname.find("MET")!= std::string::npos)) {
    DoWeights = 0; std::cout<<"is data, dont use nominal weights!!!!"<<std::endl;
    }

  string buf;
  stringstream ss(filenames); 
  while (ss >> buf){
    chain->Add(buf.c_str());
    TString thisfilename = buf.c_str();
    TString originalfilename=buf.c_str();

    TString treename = buf.c_str();
    treename.Replace(0,treename.Last('/'),"");
    TString samplename = buf.c_str();
    samplename.ReplaceAll(treename,"");
    samplename.Replace(0,samplename.Last('/')+1,"");
    samplename+=treename;
    std::cout << "samplename "<<samplename<<std::endl;

//PLACEHOLDERFRIENDTREECHAINS
    
  }// end loop of filename parsing
  
//PLACEHOLDERFRIENDTREEADD
 
  chain->SetBranchStatus("*",0);

  TFile* outfile=new TFile(outfilename,"RECREATE");

  TStopwatch* totalWatch= new TStopwatch();

  Long64_t Evt_ID;
  Int_t Evt_Run;
  Int_t Evt_Lumi;
  
  Int_t Evt_ID_INT;
  Int_t Evt_Run_INT;
  Int_t Evt_Lumi_INT;

  chain->SetBranchStatus("Evt_ID",1);
  chain->SetBranchStatus("Evt_Run",1);
  chain->SetBranchStatus("Evt_Lumi",1);
  
  // figure out what kind of branch this is
  bool evtIDisIntBranch=1;
    chain->SetBranchAddress("Evt_ID",&Evt_ID);
    chain->SetBranchAddress("Evt_Run",&Evt_Run);
    chain->SetBranchAddress("Evt_Lumi",&Evt_Lumi);
  
  // some timers 
  double totalTime=0;
  double totalTimeGetEntry=0;
  double totalTimeFillHistograms=0;
  double totalTimeEvalDNN=0;
  double totalTimeEvalWeightsAndBDT=0;
  double totalTimeSampleWeight=0;
  double totalTimeMapping=0;
  
  TStopwatch* timerGetEntry=new TStopwatch();
  TStopwatch* timerFillHistograms=new TStopwatch();
  TStopwatch* timerEvalDNN=new TStopwatch();
  TStopwatch* timerEvalWeightsAndBDT=new TStopwatch();
  TStopwatch* timerSampleWeight=new TStopwatch();
  TStopwatch* timerTotal=new TStopwatch();
  TStopwatch* timerMapping=new TStopwatch();
  

 
  // initialize variables from tree
