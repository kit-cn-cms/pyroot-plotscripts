  timerTotal->Start();
  // loop over all events
  long nentries = chain->GetEntries();
  cout << "total number of events: " << nentries << endl;

  for (long iEntry=skipevents;iEntry<nentries;iEntry++) {
    //if(iEntry==maxevents) break;
    if(iEntry%10000==0) cout << "analyzing event " << iEntry << endl;
    
    timerGetEntry->Start();
    //PLACEHOLDERFORVARIABLERESET
    chain->GetEntry(iEntry);
//    if(evtIDisIntBranch==1){
//      Evt_ID=Evt_ID_INT;
//      Evt_Lumi=Evt_Lumi_INT;
//      Evt_Run=Evt_Run_INT;
//      }
    
    //PLACEHOLDERFORCASTLINES
    
    
//     std::cout<<"Evt_ID "<<Evt_ID <<" "<<Int_t(Evt_ID)<<" "<<std::endl;
     if(Evt_ID!=Int_t(Evt_ID)){std::cout<<"PROBLEM"<<"Evt_ID "<<Evt_ID <<" "<<Int_t(Evt_ID)<<std::endl;}
//    std::cout<<"NJEts "<<N_Jets<<" "<<N_JetsLONGDUMMY<<std::endl;
//    std::cout<<"NBtagsM "<<N_BTagsM<<" "<<N_BTagsMLONGDUMMY<<std::endl;
  ///////////////////////////////////////////
  /////////////////DANGERZONE!!!/////////////
  ////Hack to handle bad default values ////
  //////////////////////////////////////////
    if (Reco_ttH_tophad_m == -999) Reco_ttH_tophad_m=-1;
    if (Reco_ttH_h_phi == -999) Reco_ttH_h_phi=-4;
    if (Reco_ttH_h_eta == -999) Reco_ttH_h_eta=-3;
    if (Reco_ttH_tophad_pt == -999) Reco_ttH_tophad_pt=-1;
    if (Reco_ttH_whad_dr == -999) Reco_ttH_whad_dr=-1;
    if (Reco_ttH_whaddau_m2 == -999) Reco_ttH_whaddau_m2=-1;
    if (Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt == -999) Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt=-1;
    // if (Reco_ttH_toplep_m == -999) Reco_ttH_toplep_m=-1;
    // "Reco_ttH_h_phi":{-999:-4},
    // "Reco_ttH_h_eta":{-999:-3},
    // "Reco_ttH_tophad_pt":{-999:-1},
    // "Reco_ttH_whad_dr":{-999:-1},
    // "Reco_ttH_whaddau_m2":{-999:-1},
    // "Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt":{-999:-1},
    // "Reco_ttH_toplep_m":{-999:-1}


    TString currentfilename="";
    currentfilename = chain->GetCurrentFile()->GetName();   
    int hasTrigger=0;
    if(currentfilename.Index("withTrigger")!=-1){hasTrigger=1;}
    eventsAnalyzed++;
    sumOfWeights+=Weight;
    
    // skip events in the filter list
    if(evtFilter->KeepEvent(Evt_Run,Evt_Lumi,Evt_ID)==false){
      std::cout<<"skipping event "<<Evt_Run<<" "<<Evt_Lumi<<" "<<Evt_ID<<std::endl;
      continue;
      }
    

	// Do weighting correctly if data driven QCD sample is used: use the weights for MC part and not for Data part
	if(processname=="QCD" or processname=="QCD_CMS_ttH_QCDScaleFactorUp" or processname=="QCD_CMS_ttH_QCDScaleFactorDown") {
		if(currentfilename.Contains("SingleElectron")){
			DoWeights=0;
			electron_data=1;
			muon_data=0;
		} 
		else if(currentfilename.Contains("SingleMuon")) {
			DoWeights=0;
			muon_data=1;
			electron_data=0;
		}
		else {
			DoWeights=1;
			muon_data=0;
			electron_data=0;
		}
	}
  
  // DANGERZONE
  // Only Works for SL events at the moment
  // Lepton SFs 
     double muonPt=0.0;
     double muonEta=0.0;
     double electronEta=0.0;
     double electronPt=0.0;
    
    //if(chain->GetBranch("Electron_Pt_BeforeRun2Calibration") && chain->GetBranch("Electron_Eta_Supercluster") && chain->GetBranch("Muon_Pt_BeForeRC")){
    //if(false){
      //std::cout<<"using superclister and stuff"<<std::endl;
      if(chain->GetBranch("Electron_Pt_BeforeRun2Calibration") && chain->GetBranch("Electron_Eta_Supercluster")){
//      if(N_TightMuons==1){muonPt=Muon_Pt_BeForeRC[0]; muonEta=Muon_Eta[0];}
      if(N_TightMuons==1){muonPt=Muon_Pt[0]; muonEta=Muon_Eta[0];}
      else{muonPt=0.0; muonEta=0.0;}
      if(N_TightElectrons==1){electronPt=Electron_Pt_BeforeRun2Calibration[0]; electronEta=Electron_Eta_Supercluster[0];}
      else{electronPt=0.0; electronEta=0.0;}
    }
    else{
      if(N_TightMuons==1){muonPt=Muon_Pt[0]; muonEta=Muon_Eta[0];}
      else{muonPt=0.0; muonEta=0.0;}
      if(N_TightElectrons==1){electronPt=Electron_Pt[0]; electronEta=Electron_Eta[0];}
      else{electronPt=0.0; electronEta=0.0;}
    }
    
    totalTimeGetEntry+=timerGetEntry->RealTime();
    timerCalculateSFs->Start();
    
    float internalEleTriggerWeight=1.0;
    float internalEleTriggerWeightUp=1.0;
    float internalEleTriggerWeightDown=1.0;
    float internalEleIDWeight=1.0;
    float internalEleIDWeightUp=1.0;
    float internalEleIDWeightDown=1.0;
    float internalEleIsoWeight=1.0;
    float internalEleIsoWeightUp=1.0;
    float internalEleIsoWeightDown=1.0;
    float internalEleGFSWeight=1.0;
    float internalEleGFSWeightUp=1.0;
    float internalEleGFSWeightDown=1.0;
    
    float internalMuTriggerWeight=1.0;
    float internalMuTriggerWeightUp=1.0;
    float internalMuTriggerWeightDown=1.0;
    float internalMuIDWeight=1.0;
    float internalMuIDWeightUp=1.0;
    float internalMuIDWeightDown=1.0;
    float internalMuIsoWeight=1.0;
    float internalMuIsoWeightUp=1.0;
    float internalMuIsoWeightDown=1.0;
    float internalMuHIPWeight=1.0;
    float internalMuHIPWeightUp=1.0;
    float internalMuHIPWeightDown=1.0;
   
    if(N_TightMuons==1){
      internalMuTriggerWeight=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,0,"Trigger");
      internalMuTriggerWeightUp=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,1,"Trigger");
      internalMuTriggerWeightDown=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,-1,"Trigger");
      
      internalMuIDWeight=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,0,"ID");
      internalMuIDWeightUp=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,1,"ID");
      internalMuIDWeightDown=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,-1,"ID");
      
      internalMuIsoWeight=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,0,"Iso");
      internalMuIsoWeightUp=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,1,"Iso");
      internalMuIsoWeightDown=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,-1,"Iso");
      
      internalMuHIPWeight=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,0,"HIP");
      internalMuHIPWeightUp=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,1,"HIP");
      internalMuHIPWeightDown=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,-1,"HIP");
    }
   
    if(N_TightElectrons==1){
      internalEleTriggerWeight=internalLeptonSFHelper->GetElectronSF(electronPt,electronEta,0,"Trigger");
      internalEleTriggerWeightUp=internalLeptonSFHelper->GetElectronSF(electronPt,electronEta,1,"Trigger");
      internalEleTriggerWeightDown=internalLeptonSFHelper->GetElectronSF(electronPt,electronEta,-1,"Trigger");
      
      internalEleIDWeight=internalLeptonSFHelper->GetElectronSF(electronPt,electronEta,0,"ID");
      internalEleIDWeightUp=internalLeptonSFHelper->GetElectronSF(electronPt,electronEta,1,"ID");
      internalEleIDWeightDown=internalLeptonSFHelper->GetElectronSF(electronPt,electronEta,-1,"ID");
      
      internalEleIsoWeight=internalLeptonSFHelper->GetElectronSF(electronPt,electronEta,0,"Iso");
      internalEleIsoWeightUp=internalLeptonSFHelper->GetElectronSF(electronPt,electronEta,1,"Iso");
      internalEleIsoWeightDown=internalLeptonSFHelper->GetElectronSF(electronPt,electronEta,-1,"Iso");
      
      internalEleGFSWeight=internalLeptonSFHelper->GetElectronSF(electronPt,electronEta,0,"GFS");
      internalEleGFSWeightUp=internalLeptonSFHelper->GetElectronSF(electronPt,electronEta,1,"GFS");
      internalEleGFSWeightDown=internalLeptonSFHelper->GetElectronSF(electronPt,electronEta,-1,"GFS");
    }
   
   
  std::vector<double> jetPts;    
  std::vector<double> jetEtas;    
  std::vector<double> jetPhis; 
  std::vector<double> jetMasses;
  std::vector<double> jetEnergies; 
  std::vector<double> jetCSVs;    
  std::vector<int> jetFlavors;    
    
  for(int ijet =0; ijet<N_Jets; ijet++){
	jetPts.push_back(Jet_Pt[ijet]);
	jetEtas.push_back(Jet_Eta[ijet]);
	jetCSVs.push_back(Jet_CSV[ijet]);
	jetFlavors.push_back(Jet_Flav[ijet]);
	jetMasses.push_back(Jet_M[ijet]);
	jetPhis.push_back(Jet_Phi[ijet]);
	jetEnergies.push_back(Jet_E[ijet]);
  }
  
  double primlepPt;    
  double primlepEta;    
  double primlepPhi; 
  double primlepM;
  double primlepE; 
  
  primlepPt=Evt_Pt_PrimaryLepton;
  primlepE=Evt_E_PrimaryLepton;
  primlepPhi=Evt_Phi_PrimaryLepton;
  primlepEta=Evt_Eta_PrimaryLepton;
  primlepM=Evt_M_PrimaryLepton;
  
  float internalCSVweight=1.0;
  float internalCSVweight_CSVHFUp=1.0;
  float internalCSVweight_CSVHFDown=1.0;
  float internalCSVweight_CSVLFUp=1.0;
  float internalCSVweight_CSVLFDown=1.0;
  float internalCSVweight_CSVLFStats1Up=1.0;
  float internalCSVweight_CSVLFStats1Down=1.0;
  float internalCSVweight_CSVLFStats2Up=1.0;
  float internalCSVweight_CSVLFStats2Down=1.0;
  float internalCSVweight_CSVHFStats1Up=1.0;
  float internalCSVweight_CSVHFStats1Down=1.0;
  float internalCSVweight_CSVHFStats2Up=1.0;
  float internalCSVweight_CSVHFStats2Down=1.0;
  float internalCSVweight_CSVCErr1Up=1.0;
  float internalCSVweight_CSVCErr1Down=1.0;
  float internalCSVweight_CSVCErr2Up=1.0;
  float internalCSVweight_CSVCErr2Down=1.0;  
  
  float internalQCDweight = 0.0;
  float internalQCDweightup = 0.0;
  float internalQCDweightdown = 0.0;
  
  float internalPDFweight = 0.0;
  float internalPDFweightUp = 0.0;
  float internalPDFweightDown = 0.0;
  
  float internalISRweightup = 0.0;
  float internalISRweightdown = 0.0;
  float internalFSRweightup = 0.0;
  float internalFSRweightdown = 0.0;
  float internalHDAMPweightup = 0.0;
  float internalHDAMPweightdown = 0.0;
  float internalUEweightup = 0.0;
  float internalUEweightdown = 0.0;
  
  double tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF;
  
  internalCSVweight=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,internalSystType,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF);
  internalCSVweight_CSVHFUp=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVHFup,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVHFDown=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVHFdown,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVLFUp=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVLFup,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVLFDown=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVLFdown,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  
  internalCSVweight_CSVLFStats1Up=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVLFStats1up,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVLFStats1Down=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVLFStats1down,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVLFStats2Up=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVLFStats2up,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVLFStats2Down=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVLFStats2down,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  
  internalCSVweight_CSVHFStats1Up=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVHFStats1up,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVHFStats1Down=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVHFStats1down,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVHFStats2Up=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVHFStats2up,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVHFStats2Down=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVHFStats2down,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  
  internalCSVweight_CSVCErr1Up=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVCErr1up,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVCErr1Down=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVCErr1down,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVCErr2Up=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVCErr2up,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVCErr2Down=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,Systematics::CSVCErr2down,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  
  //internalQCDweight=internalQCDHelper->GetScaleFactor(N_Jets,N_BTagsM,N_TightElectrons,N_TightMuons);
  //internalQCDweightup=internalQCDHelper->GetScaleFactorErrorUp(N_Jets,N_BTagsM,N_TightElectrons,N_TightMuons);
  //internalQCDweightdown=internalQCDHelper->GetScaleFactorErrorDown(N_Jets,N_BTagsM,N_TightElectrons,N_TightMuons);
  
  //int ttbar_subprocess = internalttbarsysthelper->GetTtbarSubProcess(GenEvt_I_TTPlusCC,GenEvt_I_TTPlusBB);
  //internalISRweightup = internalttbarsysthelper->GetISRScaleFactorUp(ttbar_subprocess,N_Jets);
  //internalISRweightdown = internalttbarsysthelper->GetISRScaleFactorDown(ttbar_subprocess,N_Jets);
  //internalFSRweightup = internalttbarsysthelper->GetFSRScaleFactorUp(ttbar_subprocess,N_Jets);
  //internalFSRweightdown = internalttbarsysthelper->GetFSRScaleFactorDown(ttbar_subprocess,N_Jets);
  //internalHDAMPweightup = internalttbarsysthelper->GetHDAMPScaleFactorUp(ttbar_subprocess,N_Jets);
  //internalHDAMPweightdown = internalttbarsysthelper->GetHDAMPScaleFactorDown(ttbar_subprocess,N_Jets);
  //internalUEweightup = internalttbarsysthelper->GetUEScaleFactorUp(ttbar_subprocess,N_Jets);
  //internalUEweightdown = internalttbarsysthelper->GetUEScaleFactorDown(ttbar_subprocess,N_Jets);
  
  totalTimeCalculateSFs+=timerCalculateSFs->RealTime();

 
  // print stuff for synchronizing
  bool printSyncStuff=0;
  //
  if(printSyncStuff){
    std::cout<<"event "<<Evt_ID<<std::endl;
    std::cout<<"n Jets "<<N_Jets<<std::endl;
    std::cout<<"m BTags "<<N_BTagsM<<std::endl;
    
    std::cout<<"XS weight "<<Weight_XS<<std::endl;
    std::cout<<"PU weight "<<Weight_pu69p2<<std::endl;
    std::cout<<"ele ID weight (both) "<<internalEleIDWeight<<std::endl;
    std::cout<<"ele Reco weight (both) "<<internalEleGFSWeight<<std::endl;
    std::cout<<"ele trigger weight "<<internalEleTriggerWeight<<std::endl;
    std::cout<<"mu ID weight (both) "<<internalMuIDWeight<<std::endl;
    std::cout<<"mu Tracking weight (both) "<<internalMuHIPWeight<<std::endl;
    std::cout<<"mu ISO weight (both) "<<internalMuIsoWeight<<std::endl;
    std::cout<<"mu trigger weight "<<internalMuTriggerWeight<<std::endl;
    std::cout<<"CSV weight "<<internalCSVweight<<std::endl;
 }   
