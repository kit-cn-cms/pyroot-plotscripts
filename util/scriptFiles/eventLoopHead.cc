timerTotal->Start();
// loop over all events
long nentries = chain->GetEntries();
cout << "total number of events: " << nentries << endl;

for (long iEntry = skipevents; iEntry < nentries; iEntry++) {
    // if(iEntry==maxevents) break;
    if (iEntry % 1000 == 0) cout << "analyzing event " << iEntry << endl;

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
    //if (Evt_ID != Int_t(Evt_ID)) {
    //    std::cout << "PROBLEM"
    //              << "Evt_ID " << Evt_ID << " " << Int_t(Evt_ID) << std::endl;
    //}

    //TString currentfilename = "";
    //currentfilename         = chain->GetCurrentFile()->GetName();
    //int hasTrigger          = 0;
    //if (currentfilename.Index("withTrigger") != -1) { hasTrigger = 1; }
    eventsAnalyzed++;
    sumOfWeights += Weight;


    totalTimeGetEntry += timerGetEntry->RealTime();
    timerCalculateSFs->Start();

    float internalBosonWeight           = 1.0;
    float internalBosonWeight_QCD1Up    = 1.0;
    float internalBosonWeight_QCD1Down  = 1.0;
    float internalBosonWeight_QCD2Up    = 1.0;
    float internalBosonWeight_QCD2Down  = 1.0;
    float internalBosonWeight_QCD3Up    = 1.0;
    float internalBosonWeight_QCD3Down  = 1.0;
    float internalBosonWeight_EW1Up     = 1.0;
    float internalBosonWeight_EW1Down   = 1.0;
    float internalBosonWeight_EW2Up     = 1.0;
    float internalBosonWeight_EW2Down   = 1.0;
    float internalBosonWeight_EW3Up     = 1.0;
    float internalBosonWeight_EW3Down   = 1.0;
    float internalBosonWeight_MixedUp   = 1.0;
    float internalBosonWeight_MixedDown = 1.0;
    float internalBosonWeight_AlphaSUp  = 1.0;
    float internalBosonWeight_AlphaSDown= 1.0;
    float internalBosonWeight_muRUp     = 1.0;
    float internalBosonWeight_muRDown   = 1.0;
    float internalBosonWeight_muFUp     = 1.0;
    float internalBosonWeight_muFDown   = 1.0;

    float weight_sdm_corr = 1.0;

    if ((processname.find("wlnujets") != std::string::npos && W_Pt > 100.) || (processname.find("zlljets") != std::string::npos && Z_Pt > 100.) ||
        (processname.find("znunujets") != std::string::npos && Z_Pt > 100.) || (processname.find("gammajets") != std::string::npos && Gamma_Pt > 100.)) {
        internalBosonWeight           = BosonWeight_nominal;
        internalBosonWeight_QCD1Up    = BosonWeight_QCD1Up;
        internalBosonWeight_QCD1Down  = BosonWeight_QCD1Down;
        internalBosonWeight_QCD2Up    = BosonWeight_QCD2Up;
        internalBosonWeight_QCD2Down  = BosonWeight_QCD2Down;
        internalBosonWeight_QCD3Up    = BosonWeight_QCD3Up;
        internalBosonWeight_QCD3Down  = BosonWeight_QCD3Down;
        internalBosonWeight_EW1Up     = BosonWeight_EW1Up;
        internalBosonWeight_EW1Down   = BosonWeight_EW1Down;
        internalBosonWeight_EW2Up     = BosonWeight_EW2Up;
        internalBosonWeight_EW2Down   = BosonWeight_EW2Down;
        internalBosonWeight_EW3Up     = BosonWeight_EW3Up;
        internalBosonWeight_EW3Down   = BosonWeight_EW3Down;
        internalBosonWeight_MixedUp   = BosonWeight_MixedUp;
        internalBosonWeight_MixedDown = BosonWeight_MixedDown;
        internalBosonWeight_AlphaSUp  = BosonWeight_AlphaUp;
        internalBosonWeight_AlphaSDown= BosonWeight_AlphaDown;
        internalBosonWeight_muRUp     = BosonWeight_muRUp;
        internalBosonWeight_muRDown   = BosonWeight_muRDown;
        internalBosonWeight_muFUp     = BosonWeight_muFUp;
        internalBosonWeight_muFDown   = BosonWeight_muFDown;
    }
    
    //float HT_Jets = 0.;
    //for(size_t m = 0;m<N_Jets;m++) HT_Jets+=Jet_Pt[m];
    
    //std::cout << "N_Jets: " << N_Jets << " HT: " << HT_Jets << std::endl;
    float internalCSVWeightSF_had = 1.0;
    internalCSVWeightSF_had = csv_calibration_helper_had.GetScaleFactor(process, N_Jets, HT_AK4Jets);
    float internalCSVWeightSF_lep = 1.0;
    internalCSVWeightSF_lep = csv_calibration_helper_lep.GetScaleFactor(process, N_Jets, HT_AK4Jets);
    
    //std::cout << " DeepJet patch had: " << internalCSVWeightSF_had << std::endl;
    //std::cout << " DeepJet patch lep: " << internalCSVWeightSF_lep << std::endl;

    // double primlepPt;
    // double primlepEta;
    // double primlepPhi;
    // double primlepM;
    // double primlepE;

    // primlepPt=Evt_Pt_PrimaryLepton;
    // primlepE=Evt_E_PrimaryLepton;
    // primlepPhi=Evt_Phi_PrimaryLepton;
    // primlepEta=Evt_Eta_PrimaryLepton;
    // primlepM=Evt_M_PrimaryLepton;

    totalTimeCalculateSFs += timerCalculateSFs->RealTime();

    // print stuff for synchronizing
    bool printSyncStuff = 0;
    //
    if (printSyncStuff) {
        std::cout << "event " << Evt_ID << std::endl;
        std::cout << "n Jets " << N_Jets << std::endl;
        std::cout << "m BTags " << N_BTagsM << std::endl;

        std::cout << "XS weight " << Weight_XS << std::endl;
        std::cout << "PU weight " << Weight_pu69p2 << std::endl;
    }
    
    bool DeltaR_AK4Jets_LooseElectron_Smaller_3p4;
    bool DeltaR_AK4Jets_LooseMuon_Smaller_3p4;
    DeltaR_AK4Jets_LooseElectron_Smaller_3p4 = check_if_every_element_smaller(DeltaR_AK4Jet_LooseElectron.get(), N_Jets*N_LooseElectrons, N_Jets*N_LooseElectrons, 3.4);
    DeltaR_AK4Jets_LooseMuon_Smaller_3p4 = check_if_every_element_smaller(DeltaR_AK4Jet_LooseMuon.get(), N_Jets*N_LooseMuons, N_Jets*N_LooseMuons, 3.4);
    //std::cout << "DeltaR_AK4Jets_LooseElectron_Smaller_3p4: " << DeltaR_AK4Jets_LooseElectron_Smaller_3p4 << std::endl;
    //std::cout << "DeltaR_AK4Jets_LooseMuon_Smaller_3p4: " << DeltaR_AK4Jets_LooseMuon_Smaller_3p4 << std::endl;
    
    bool DeltaPhi_AK4Jets_MET_Larger_0p5;
    DeltaPhi_AK4Jets_MET_Larger_0p5 = check_if_every_element_greater(DeltaPhi_AK4Jet_MET.get(), N_Jets, 4, 0.5);
    bool DeltaPhi_AK4Jets_Recoil_Larger_0p5;
    DeltaPhi_AK4Jets_Recoil_Larger_0p5 = check_if_every_element_greater(DeltaPhi_AK4Jet_Hadr_Recoil.get(), N_Jets, 4, 0.5);
    
    if(N_AK15Jets>0) weight_sdm_corr = get_msd_weight(AK15Jet_Pt[0], AK15Jet_Eta[0]);

    // hack against prefireweight with 2018 signal samples
    if(processname.find("vectormonotop")!=std::string::npos) {
        Weight_L1_Prefire = 1.0;
        Weight_L1_Prefire_Up = 1.0;
        Weight_L1_Prefire_Down = 1.0;
    }
