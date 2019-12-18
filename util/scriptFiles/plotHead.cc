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

void plot(){
  TH1F::SetDefaultSumw2();

  // open files
  TChain* chain = new TChain("MVATree");
  char* filenames = getenv ("FILENAMES");
  char* outfilename = getenv ("OUTFILENAME");
  std::string plotscriptBaseDir = getenv ("PLOTSCRIPTBASEDIR");
  string processname = string(getenv ("PROCESSNAME"));
  string suffix = string(getenv ("SUFFIX"));
  int maxevents = atoi(getenv ("MAXEVENTS"));
  int skipevents = atoi(getenv ("SKIPEVENTS"));
  string eventFilterFile = string(getenv("EVENTFILTERFILE"));
  std::string dataera = string(getenv ("DATAERA"));

  // create vector of systematics
  std::vector<Systematics::Type> v_SystTypes = Systematics::getTypeVector();
  //for(auto itsyst : v_SystTypes){std::cout<< " Know :" << itsyst << std::endl;}


  std::string csvHFfile = "";
  std::string csvLFfile = "";
  if( dataera == "2017" ) {
      csvHFfile=plotscriptBaseDir+"/data/CSV/sfs_deepjet_2017_hf.root";
      csvLFfile=plotscriptBaseDir+"/data/CSV/sfs_deepjet_2017_lf.root";
      }
  else if( dataera == "2018" ) {
      csvHFfile=plotscriptBaseDir+"/data/CSV/sfs_deepjet_2018_hf.root";
      csvLFfile=plotscriptBaseDir+"/data/CSV/sfs_deepjet_2018_lf.root";
      }
  else if( dataera == "2016" ) {
      csvHFfile=plotscriptBaseDir+"/data/CSV/sfs_deepjet_2016_hf.root";
      csvLFfile=plotscriptBaseDir+"/data/CSV/sfs_deepjet_2016_lf.root";
      }
  else if( dataera == "2017_deepCSV" ) {
      csvHFfile="/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Summer18_2017data/DeepCSV_SF_V3_2017/deepCSV_sfs_hf.root";
      csvLFfile="/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Summer18_2017data/DeepCSV_SF_V3_2017/deepCSV_sfs_lf.root";
      }
  else {
      std::cout << "NO VALID DATAERA CHOSEN!!" << std::endl;
      std::cout << "dataera: " << dataera << std::endl;
      }

  TString qcd_file = "/nfs/dust/cms/user/mwassmer/QCD_Estimation_September17/QCD_Estimation/QCD_Estimation_FakeScaleFactor_nominal.root";
  
  CSVHelper* internalCSVHelper= new CSVHelper(csvHFfile,csvLFfile, 5,4,3,v_SystTypes);
  LeptonSFHelper* internalLeptonSFHelper= new LeptonSFHelper(dataera, plotscriptBaseDir);
  //QCDHelper* internalQCDHelper = new QCDHelper(qcd_file);
  //ttbarsysthelper* internalttbarsysthelper = new ttbarsysthelper();



  std::cout<<"processname: " <<processname<<std::endl;
  std::cout<<"suffix: " <<suffix<<std::endl;

  std::vector<TString> databaseRelevantFilenames;

  // create event filter class
  EventFilter* evtFilter = new EventFilter(eventFilterFile);

  int eventsAnalyzed=0;
  float sumOfWeights=0;

  int DoWeights=1;
  int isTthSample=0;
  int isTTbarSample=0;
  int electron_data=0;
  int muon_data=0;

  //initialize Trigger Helper

  // Hack for subsampling test
  //if(processname=="SingleEl" || processname=="SingleMu"){DoWeights=0; std::cout<<"is data, dont use nominal weihgts"<<std::endl;}
  if((processname.find("SingleEl")!= std::string::npos) || (processname.find("SingleMu")!= std::string::npos) || (processname.find("MET")!= std::string::npos)){DoWeights=0; std::cout<<"is data, dont use nominal weights!!!!"<<std::endl;}

  //Hack to find out if sample is ttH or other
  if((processname.find("ttH") != std::string::npos) ) {isTthSample=1; std::cout<<"This is a ttH sample!!!!"<<std::endl;}    
  else{ std::cout << "This is NOT a ttH sample!!!!"<<std::endl;}
  
  //Hack to find out if sample is ttbar or other
  if( (processname.find("tt") != std::string::npos) and (isTthSample ==0) 
      and not (processname.find("ttW") != std::string::npos or processname.find("ttZ") != std::string::npos or processname.find("ttV") != std::string::npos ) ) {
    isTTbarSample=1; 
    std::cout<<"This is a TTbar sample!!!!"<<std::endl;
  }    
  else{ std::cout << "This is NOT a TTbar sample!!!!"<<std::endl;}
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
    //remove remaining dashes
    while(thisfilename.Last('-')>=0){ thisfilename.Replace(thisfilename.Last('-'),1,"");}
    std::cout<<" relevant database name "<<thisfilename<<std::endl;
        
    if(thisfilename.Contains("SingleEl")){thisfilename="SingleElectron";}
    if(thisfilename.Contains("SingleMu")){thisfilename="SingleMuon";}
       
    // now replace remaining v2 and newmpx strings because of different namings in new MEM DB
    if(thisfilename.Contains("v2")==1){ thisfilename.ReplaceAll("v2","");}
    if(thisfilename.Contains("newpmx")==1){ thisfilename.ReplaceAll("newpmx","");}
    std::cout<<" relevant database name "<<thisfilename<<std::endl;
   sampleDataBaseIdentifiers[originalfilename]=thisfilename;
    
    //check if already in vectr
   // TString translatedFileNameForDataBase;


  //DANGERZONE
  // hardcode sample translation map for now
  std::cout<<"WARNING!: Hardcoded sampleTranslationMapCPP !"<<std::endl;
  sampleTranslationMapCPP[TString("TTToSemiLeptonicTuneCP5PSweights13TeVpowhegpythia8")]=TString("TTToSemiLeptonicTuneCP5PSweights13TeVpowhegpythia8");
  sampleTranslationMapCPP[TString("TTToSemiLeptonicTuneCP513TeVpowhegpythia8")]=TString("TTToSemiLeptonicTuneCP513TeVpowhegpythia8");

  sampleTranslationMapCPP[TString("TTTo2L2NuTuneCP5PSweights13TeVpowhegpythia8")]=TString("TTTo2L2NuTuneCP5PSweights13TeVpowhegpythia8");
  sampleTranslationMapCPP[TString("TTTo2L2NuTuneCP513TeVpowhegpythia8")]=TString("TTTo2L2NuTuneCP513TeVpowhegpythia8");

  sampleTranslationMapCPP[TString("TTToHadronicTuneCP5PSweights13TeVpowhegpythia8")]=TString("TTToHadronicTuneCP5PSweights13TeVpowhegpythia8");
  sampleTranslationMapCPP[TString("TTToHadronicTuneCP513TeVpowhegpythia8")]=TString("TTToHadronicTuneCP513TeVpowhegpythia8");

  sampleTranslationMapCPP[TString("ttHTobbM125TuneCP513TeVpowhegpythia8")]=TString("ttHTobbM125TuneCP513TeVpowhegpythia8");
  sampleTranslationMapCPP[TString("ttHToNonbbM125TuneCP513TeVpowhegpythia8")]=TString("ttHToNonbbM125TuneCP513TeVpowhegpythia8");


    samplename_in_database=thisfilename;
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
