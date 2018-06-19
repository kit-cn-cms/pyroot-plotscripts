 
    translatedFileNameForDataBase=sampleTranslationMapCC[thisfilename];
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

