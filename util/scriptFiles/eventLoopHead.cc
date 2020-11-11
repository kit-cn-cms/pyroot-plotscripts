  timerTotal->Start();
  // loop over all events
  long nentries = chain->GetEntries();
  cout << "total number of events: " << nentries << endl;
	int warningCounter = 0;    

  for (long iEntry=skipevents;iEntry<nentries;iEntry++) {
    if(iEntry==maxevents) break;
    if(iEntry%10000==0) cout << "analyzing event " << iEntry << " of " << nentries << " Total events" << endl;
    
    timerGetEntry->Start();
    //PLACEHOLDERFORVARIABLERESET
    chain->GetEntry(iEntry);
    
    //PLACEHOLDERFORCASTLINES
    
    
     if(Evt_ID!=Int_t(Evt_ID)){
       std::cout<<"PROBLEM "<<"Evt_ID "<<Evt_ID <<" "<<Int_t(Evt_ID)<<std::endl;
       std::cout << "recasting Long to Int " << std::endl;
       Evt_ID = Int_t(Evt_ID);
       }

    TString currentfilename="";
    currentfilename = chain->GetCurrentFile()->GetName();   
    eventsAnalyzed++;
    
    // skip events in the filter list
    //if(evtFilter->KeepEvent(Evt_Run,Evt_Lumi,Evt_ID)==false){
    //  std::cout<<"skipping event "<<Evt_Run<<" "<<Evt_Lumi<<" "<<Evt_ID<<std::endl;
    //  continue;
    //  }
    

    totalTimeGetEntry+=timerGetEntry->RealTime();
