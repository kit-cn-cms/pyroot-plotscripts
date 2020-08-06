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
    
    // DarkHiggs PU Weights
    float internalPUWeight_2018 = 1.0;
    float internalPUWeight_2018_Up = 1.0;
    float internalPUWeight_2018_Down = 1.0;
    float internalPUWeight_2017 = 1.0;
    float internalPUWeight_2017_Up = 1.0;
    float internalPUWeight_2017_Down = 1.0;
    float internalPUWeight_2016 = 1.0;
    float internalPUWeight_2016_Up = 1.0;
    float internalPUWeight_2016_Down = 1.0;

    internalPUWeight_2018 = pu_helper.GetScaleFactor("2018", N_GenPVs);
    internalPUWeight_2018_Up = pu_helper.GetScaleFactor("2018Up", N_GenPVs);
    internalPUWeight_2018_Down = pu_helper.GetScaleFactor("2018Down", N_GenPVs);
    internalPUWeight_2017 = pu_helper.GetScaleFactor("2017", N_GenPVs);
    internalPUWeight_2017_Up = pu_helper.GetScaleFactor("2017Up", N_GenPVs);
    internalPUWeight_2017_Down = pu_helper.GetScaleFactor("2017Down", N_GenPVs);
    internalPUWeight_2016 = pu_helper.GetScaleFactor("2016", N_GenPVs);
    internalPUWeight_2016_Up = pu_helper.GetScaleFactor("2016Up", N_GenPVs);
    internalPUWeight_2016_Down = pu_helper.GetScaleFactor("2016Down", N_GenPVs);
    
    //float HT_Jets = 0.;
    //for(size_t m = 0;m<N_Jets;m++) HT_Jets+=Jet_Pt[m];
    
    //std::cout << "N_Jets: " << N_Jets << " HT: " << HT_Jets << std::endl;

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
    std::vector<double> jetPts;    
    std::vector<double> jetEtas;    
    std::vector<double> jetCSVs;    
    std::vector<int> jetFlavors;    

    std::vector<double> jetPts_outside;    
    std::vector<double> jetEtas_outside;    
    std::vector<double> jetCSVs_outside;    
    std::vector<int> jetFlavors_outside;   

    std::vector<double> jetPts_outside_untagged_medium;    
    std::vector<double> jetEtas_outside_untagged_medium;    
    std::vector<int> jetFlavors_outside_untagged_medium;    
    
    std::vector<double> jetPts_outside_tagged_medium;    
    std::vector<double> jetEtas_outside_tagged_medium;    
    std::vector<int> jetFlavors_outside_tagged_medium; 
 
    std::vector<double> jetPts_outside_untagged_loose;    
    std::vector<double> jetEtas_outside_untagged_loose;    
    std::vector<int> jetFlavors_outside_untagged_loose;    
    
    std::vector<double> jetPts_outside_tagged_loose;    
    std::vector<double> jetEtas_outside_tagged_loose;    
    std::vector<int> jetFlavors_outside_tagged_loose; 

    for(int ijet =0; ijet<N_Jets; ijet++){
        jetPts.push_back(Jet_Pt[ijet]);
        jetEtas.push_back(Jet_Eta[ijet]);
        jetCSVs.push_back(Jet_CSV[ijet]);
        jetFlavors.push_back(Jet_Flav[ijet]);
    }


    // AK4 Jets outside AK15 Jet -> medium tags
    for(int ijet =0; ijet<N_JetsMediumUntagged_outside_lead_AK15Jet; ijet++){
        jetPts_outside_untagged_medium.push_back(JetMediumUntagged_outside_lead_AK15Jet_Pt[ijet]);
        jetEtas_outside_untagged_medium.push_back(JetMediumUntagged_outside_lead_AK15Jet_Eta[ijet]);
        jetFlavors_outside_untagged_medium.push_back(JetMediumUntagged_outside_lead_AK15Jet_Flav[ijet]);

        jetPts_outside.push_back(JetMediumUntagged_outside_lead_AK15Jet_Pt[ijet]);
        jetEtas_outside.push_back(JetMediumUntagged_outside_lead_AK15Jet_Eta[ijet]);
        jetFlavors_outside.push_back(JetMediumUntagged_outside_lead_AK15Jet_Flav[ijet]);
    }
    for(int ijet =0; ijet<N_JetsMediumTagged_outside_lead_AK15Jet; ijet++){
        jetPts_outside_tagged_medium.push_back(JetMediumTagged_outside_lead_AK15Jet_Pt[ijet]);
        jetEtas_outside_tagged_medium.push_back(JetMediumTagged_outside_lead_AK15Jet_Eta[ijet]);
        jetFlavors_outside_tagged_medium.push_back(JetMediumTagged_outside_lead_AK15Jet_Flav[ijet]);
    
        jetPts_outside.push_back(JetMediumTagged_outside_lead_AK15Jet_Pt[ijet]);
        jetEtas_outside.push_back(JetMediumTagged_outside_lead_AK15Jet_Eta[ijet]);
        jetFlavors_outside.push_back(JetMediumTagged_outside_lead_AK15Jet_Flav[ijet]);
    }
    // AK4 Jets outside AK15 Jet -> loose tags
    for(int ijet =0; ijet<N_JetsLooseUntagged_outside_lead_AK15Jet; ijet++){
        jetPts_outside_untagged_loose.push_back(JetLooseUntagged_outside_lead_AK15Jet_Pt[ijet]);
        jetEtas_outside_untagged_loose.push_back(JetLooseUntagged_outside_lead_AK15Jet_Eta[ijet]);
        jetFlavors_outside_untagged_loose.push_back(JetLooseUntagged_outside_lead_AK15Jet_Flav[ijet]);
    }
    for(int ijet =0; ijet<N_JetsLooseTagged_outside_lead_AK15Jet; ijet++){
        jetPts_outside_tagged_loose.push_back(JetLooseTagged_outside_lead_AK15Jet_Pt[ijet]);
        jetEtas_outside_tagged_loose.push_back(JetLooseTagged_outside_lead_AK15Jet_Eta[ijet]);
        jetFlavors_outside_tagged_loose.push_back(JetLooseTagged_outside_lead_AK15Jet_Flav[ijet]);
    }
    
    // Method 1a, according to https://twiki.cern.ch/twiki/bin/view/CMS/BTagSFMethods
    // float internalCSVweight_loose=internalBtagSFHelper_loose->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,"central","central");
    // float internalCSVweight_looseLFUP=internalBtagSFHelper_loose->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,"up","central");
    // float internalCSVweight_looseLFDOWN=internalBtagSFHelper_loose->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,"down","central");
    // float internalCSVweight_looseHFUP=internalBtagSFHelper_loose->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,"central","up");
    // float internalCSVweight_looseHFDOWN=internalBtagSFHelper_loose->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,"central","down");
 
    // float internalCSVweight_medium=internalBtagSFHelper_medium->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,"central","central");
    // float internalCSVweight_mediumLFUP=internalBtagSFHelper_medium->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,"up","central");
    // float internalCSVweight_mediumLFDOWN=internalBtagSFHelper_medium->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,"down","central");
    // float internalCSVweight_mediumHFUP=internalBtagSFHelper_medium->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,"central","up");
    // float internalCSVweight_mediumHFDOWN=internalBtagSFHelper_medium->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,"central","down");

    // float internalCSVweight_medium_outside=internalBtagSFHelper_medium_outside->getCSVWeight(jetPts_outside_tagged_medium,jetEtas_outside_tagged_medium,jetFlavors_outside_tagged_medium,
    //                                                                                         jetPts_outside_untagged_medium,jetEtas_outside_untagged_medium,jetFlavors_outside_untagged_medium,
    //                                                                                         "central","central");
    // float internalCSVweight_medium_outsideLFUP=internalBtagSFHelper_medium_outside->getCSVWeight(jetPts_outside_tagged_medium,jetEtas_outside_tagged_medium,jetFlavors_outside_tagged_medium,
    //                                                                                              jetPts_outside_untagged_medium,jetEtas_outside_untagged_medium,jetFlavors_outside_untagged_medium,
    //                                                                                              "up","central");
    // float internalCSVweight_medium_outsideLFDOWN=internalBtagSFHelper_medium_outside->getCSVWeight(jetPts_outside_tagged_medium,jetEtas_outside_tagged_medium,jetFlavors_outside_tagged_medium,
    //                                                                                                jetPts_outside_untagged_medium,jetEtas_outside_untagged_medium,jetFlavors_outside_untagged_medium,
    //                                                                                                "down","central");
    // float internalCSVweight_medium_outsideHFUP=internalBtagSFHelper_medium_outside->getCSVWeight(jetPts_outside_tagged_medium,jetEtas_outside_tagged_medium,jetFlavors_outside_tagged_medium,
    //                                                                                              jetPts_outside_untagged_medium,jetEtas_outside_untagged_medium,jetFlavors_outside_untagged_medium,
    //                                                                                              "central","up");
    // float internalCSVweight_medium_outsideHFDOWN=internalBtagSFHelper_medium_outside->getCSVWeight( jetPts_outside_tagged_medium,jetEtas_outside_tagged_medium,jetFlavors_outside_tagged_medium,
    //                                                                                                 jetPts_outside_untagged_medium,jetEtas_outside_untagged_medium,jetFlavors_outside_untagged_medium,
    //                                                                                                 "central","down");

    // float internalCSVweight_loose_outside=internalBtagSFHelper_loose_outside->getCSVWeight(jetPts_outside_tagged_loose,jetEtas_outside_tagged_loose,jetFlavors_outside_tagged_loose,
    //                                                                                         jetPts_outside_untagged_loose,jetEtas_outside_untagged_loose,jetFlavors_outside_untagged_loose,
    //                                                                                         "central","central");
    // float internalCSVweight_loose_outsideLFUP=internalBtagSFHelper_loose_outside->getCSVWeight(jetPts_outside_tagged_loose,jetEtas_outside_tagged_loose,jetFlavors_outside_tagged_loose,
    //                                                                                              jetPts_outside_untagged_loose,jetEtas_outside_untagged_loose,jetFlavors_outside_untagged_loose,
    //                                                                                              "up","central");
    // float internalCSVweight_loose_outsideLFDOWN=internalBtagSFHelper_loose_outside->getCSVWeight(jetPts_outside_tagged_loose,jetEtas_outside_tagged_loose,jetFlavors_outside_tagged_loose,
    //                                                                                                jetPts_outside_untagged_loose,jetEtas_outside_untagged_loose,jetFlavors_outside_untagged_loose,
    //                                                                                                "down","central");
    // float internalCSVweight_loose_outsideHFUP=internalBtagSFHelper_loose_outside->getCSVWeight(jetPts_outside_tagged_loose,jetEtas_outside_tagged_loose,jetFlavors_outside_tagged_loose,
    //                                                                                              jetPts_outside_untagged_loose,jetEtas_outside_untagged_loose,jetFlavors_outside_untagged_loose,
    //                                                                                              "central","up");
    // float internalCSVweight_loose_outsideHFDOWN=internalBtagSFHelper_loose_outside->getCSVWeight( jetPts_outside_tagged_loose,jetEtas_outside_tagged_loose,jetFlavors_outside_tagged_loose,
    //                                                                                                 jetPts_outside_untagged_loose,jetEtas_outside_untagged_loose,jetFlavors_outside_untagged_loose,
    //                                                                                                 "central","down");


    // Method 1b, according to https://twiki.cern.ch/twiki/bin/view/CMS/BTagSFMethods, modified according to Matteo from LPC
    // float internalCSVweight_loose_outside_zerotag=internalBtagSFHelper_loose_outside->getCSVWeight_MethodOneB_ge1t(jetPts_outside,jetEtas_outside,jetFlavors_outside, "central","central",false);
    // float internalCSVweight_loose_outsideLFUP_zerotag=internalBtagSFHelper_loose_outside->getCSVWeight_MethodOneB_ge1t(jetPts_outside,jetEtas_outside,jetFlavors_outside, "up","central",false);
    // float internalCSVweight_loose_outsideLFDOWN_zerotag=internalBtagSFHelper_loose_outside->getCSVWeight_MethodOneB_ge1t(jetPts_outside,jetEtas_outside,jetFlavors_outside, "down","central",false);
    // float internalCSVweight_loose_outsideHFUP_zerotag=internalBtagSFHelper_loose_outside->getCSVWeight_MethodOneB_ge1t(jetPts_outside,jetEtas_outside,jetFlavors_outside, "central","up",false);
    // float internalCSVweight_loose_outsideHFDOWN_zerotag=internalBtagSFHelper_loose_outside->getCSVWeight_MethodOneB_ge1t(jetPts_outside,jetEtas_outside,jetFlavors_outside, "central","down",false);

    // float internalCSVweight_loose_outside_onetag=internalBtagSFHelper_loose_outside->getCSVWeight_MethodOneB_ge1t(jetPts_outside,jetEtas_outside,jetFlavors_outside, "central","central",true);
    // float internalCSVweight_loose_outsideLFUP_onetag=internalBtagSFHelper_loose_outside->getCSVWeight_MethodOneB_ge1t(jetPts_outside,jetEtas_outside,jetFlavors_outside, "up","central",true);
    // float internalCSVweight_loose_outsideLFDOWN_onetag=internalBtagSFHelper_loose_outside->getCSVWeight_MethodOneB_ge1t(jetPts_outside,jetEtas_outside,jetFlavors_outside, "down","central",true);
    // float internalCSVweight_loose_outsideHFUP_onetag=internalBtagSFHelper_loose_outside->getCSVWeight_MethodOneB_ge1t(jetPts_outside,jetEtas_outside,jetFlavors_outside, "central","up",true);
    // float internalCSVweight_loose_outsideHFDOWN_onetag=internalBtagSFHelper_loose_outside->getCSVWeight_MethodOneB_ge1t(jetPts_outside,jetEtas_outside,jetFlavors_outside, "central","down",true);

    // float internalCSVweight_medium_zerotag=internalBtagSFHelper_medium->getCSVWeight_MethodOneB_ge1t(jetPts_outside,jetEtas_outside,jetFlavors_outside, "central","central",false);
    // float internalCSVweight_mediumLFUP_zerotag=internalBtagSFHelper_medium->getCSVWeight_MethodOneB_ge1t(jetPts_outside,jetEtas_outside,jetFlavors_outside, "up","central",false);
    // float internalCSVweight_mediumLFDOWN_zerotag=internalBtagSFHelper_medium->getCSVWeight_MethodOneB_ge1t(jetPts_outside,jetEtas_outside,jetFlavors_outside, "down","central",false);
    // float internalCSVweight_mediumHFUP_zerotag=internalBtagSFHelper_medium->getCSVWeight_MethodOneB_ge1t(jetPts_outside,jetEtas_outside,jetFlavors_outside, "central","up",false);
    // float internalCSVweight_mediumHFDOWN_zerotag=internalBtagSFHelper_medium->getCSVWeight_MethodOneB_ge1t(jetPts_outside,jetEtas_outside,jetFlavors_outside, "central","down",false);

    // float internalCSVweight_medium_onetag=internalBtagSFHelper_medium->getCSVWeight_MethodOneB_1t(jetPts_outside,jetEtas_outside,jetFlavors_outside, "central","central",false);
    // float internalCSVweight_mediumLFUP_onetag=internalBtagSFHelper_medium->getCSVWeight_MethodOneB_1t(jetPts_outside,jetEtas_outside,jetFlavors_outside, "up","central",false);
    // float internalCSVweight_mediumLFDOWN_onetag=internalBtagSFHelper_medium->getCSVWeight_MethodOneB_1t(jetPts_outside,jetEtas_outside,jetFlavors_outside, "down","central",false);
    // float internalCSVweight_mediumHFUP_onetag=internalBtagSFHelper_medium->getCSVWeight_MethodOneB_1t(jetPts_outside,jetEtas_outside,jetFlavors_outside, "central","up",false);
    // float internalCSVweight_mediumHFDOWN_onetag=internalBtagSFHelper_medium->getCSVWeight_MethodOneB_1t(jetPts_outside,jetEtas_outside,jetFlavors_outside, "central","down",false);


    // only jets outside of AK15 -> hadronic analysis
    auto internalCSVweight_loose_outside_0B         = internalBtagSFHelper_loose_outside->getCSVWeight_0B(jetPts_outside,jetEtas_outside,jetFlavors_outside, "central","central");
    auto internalCSVweight_loose_outside_LFUP_0B    = internalBtagSFHelper_loose_outside->getCSVWeight_0B(jetPts_outside,jetEtas_outside,jetFlavors_outside, "up","central");
    auto internalCSVweight_loose_outside_LFDOWN_0B  = internalBtagSFHelper_loose_outside->getCSVWeight_0B(jetPts_outside,jetEtas_outside,jetFlavors_outside, "down","central");
    auto internalCSVweight_loose_outside_HFUP_0B    = internalBtagSFHelper_loose_outside->getCSVWeight_0B(jetPts_outside,jetEtas_outside,jetFlavors_outside, "central","up");
    auto internalCSVweight_loose_outside_HFDOWN_0B  = internalBtagSFHelper_loose_outside->getCSVWeight_0B(jetPts_outside,jetEtas_outside,jetFlavors_outside, "central","down");

    // calculate actual event weights
    double internalCSVweight_loose_outside_0B_final         = divideSavely(internalCSVweight_loose_outside_0B.first,internalCSVweight_loose_outside_0B.second);
    double internalCSVweight_loose_outside_LFUP_0B_final    = divideSavely(internalCSVweight_loose_outside_LFUP_0B.first,internalCSVweight_loose_outside_LFUP_0B.second);
    double internalCSVweight_loose_outside_LFDOWN_0B_final  = divideSavely(internalCSVweight_loose_outside_LFDOWN_0B.first,internalCSVweight_loose_outside_LFDOWN_0B.second);
    double internalCSVweight_loose_outside_HFUP_0B_final    = divideSavely(internalCSVweight_loose_outside_HFUP_0B.first,internalCSVweight_loose_outside_HFUP_0B.second);
    double internalCSVweight_loose_outside_HFDOWN_0B_final  = divideSavely(internalCSVweight_loose_outside_HFDOWN_0B.first,internalCSVweight_loose_outside_HFDOWN_0B.second);

    double internalCSVweight_loose_outside_ge1B_final        = divideSavely((1-internalCSVweight_loose_outside_0B.first),(1-internalCSVweight_loose_outside_0B.second));
    double internalCSVweight_loose_outside_LFUP_ge1B_final   = divideSavely((1-internalCSVweight_loose_outside_LFUP_0B.first),(1-internalCSVweight_loose_outside_LFUP_0B.second));
    double internalCSVweight_loose_outside_LFDOWN_ge1B_final = divideSavely((1-internalCSVweight_loose_outside_LFDOWN_0B.first),(1-internalCSVweight_loose_outside_LFDOWN_0B.second));
    double internalCSVweight_loose_outside_HFUP_ge1B_final   = divideSavely((1-internalCSVweight_loose_outside_HFUP_0B.first),(1-internalCSVweight_loose_outside_HFUP_0B.second));
    double internalCSVweight_loose_outside_HFDOWN_ge1B_final = divideSavely((1-internalCSVweight_loose_outside_HFDOWN_0B.first),(1-internalCSVweight_loose_outside_HFDOWN_0B.second));

    // all jets -> leptopnic analysis
    auto internalCSVweight_medium_0B        = internalBtagSFHelper_medium->getCSVWeight_0B(jetPts,jetEtas,jetFlavors, "central","central");
    auto internalCSVweight_medium_LFUP_0B   = internalBtagSFHelper_medium->getCSVWeight_0B(jetPts,jetEtas,jetFlavors, "up","central");
    auto internalCSVweight_medium_LFDOWN_0B = internalBtagSFHelper_medium->getCSVWeight_0B(jetPts,jetEtas,jetFlavors, "down","central");
    auto internalCSVweight_medium_HFUP_0B   = internalBtagSFHelper_medium->getCSVWeight_0B(jetPts,jetEtas,jetFlavors, "central","up");
    auto internalCSVweight_medium_HFDOWN_0B = internalBtagSFHelper_medium->getCSVWeight_0B(jetPts,jetEtas,jetFlavors, "central","down");

    auto internalCSVweight_medium_1B        = internalBtagSFHelper_medium->getCSVWeight_1B(jetPts,jetEtas,jetFlavors, "central","central");
    auto internalCSVweight_medium_LFUP_1B   = internalBtagSFHelper_medium->getCSVWeight_1B(jetPts,jetEtas,jetFlavors, "up","central");
    auto internalCSVweight_medium_LFDOWN_1B = internalBtagSFHelper_medium->getCSVWeight_1B(jetPts,jetEtas,jetFlavors, "down","central");
    auto internalCSVweight_medium_HFUP_1B   = internalBtagSFHelper_medium->getCSVWeight_1B(jetPts,jetEtas,jetFlavors, "central","up");
    auto internalCSVweight_medium_HFDOWN_1B = internalBtagSFHelper_medium->getCSVWeight_1B(jetPts,jetEtas,jetFlavors, "central","down");

    // calculate actual event weights
    double internalCSVweight_medium_0B_final         = divideSavely(internalCSVweight_medium_0B.first,internalCSVweight_medium_0B.second);
    double internalCSVweight_medium_LFUP_0B_final    = divideSavely(internalCSVweight_medium_LFUP_0B.first,internalCSVweight_medium_LFUP_0B.second);
    double internalCSVweight_medium_LFDOWN_0B_final  = divideSavely(internalCSVweight_medium_LFDOWN_0B.first,internalCSVweight_medium_LFDOWN_0B.second);
    double internalCSVweight_medium_HFUP_0B_final    = divideSavely(internalCSVweight_medium_HFUP_0B.first,internalCSVweight_medium_HFUP_0B.second);
    double internalCSVweight_medium_HFDOWN_0B_final  = divideSavely(internalCSVweight_medium_HFDOWN_0B.first,internalCSVweight_medium_HFDOWN_0B.second);

    double internalCSVweight_medium_ge1B_final        = divideSavely((1-internalCSVweight_medium_0B.first),(1-internalCSVweight_medium_0B.second));
    double internalCSVweight_medium_LFUP_ge1B_final   = divideSavely((1-internalCSVweight_medium_LFUP_0B.first),(1-internalCSVweight_medium_LFUP_0B.second));
    double internalCSVweight_medium_LFDOWN_ge1B_final = divideSavely((1-internalCSVweight_medium_LFDOWN_0B.first),(1-internalCSVweight_medium_LFDOWN_0B.second));
    double internalCSVweight_medium_HFUP_ge1B_final   = divideSavely((1-internalCSVweight_medium_HFUP_0B.first),(1-internalCSVweight_medium_HFUP_0B.second));
    double internalCSVweight_medium_HFDOWN_ge1B_final = divideSavely((1-internalCSVweight_medium_HFDOWN_0B.first),(1-internalCSVweight_medium_HFDOWN_0B.second));

    double internalCSVweight_medium_1B_final        = divideSavely((internalCSVweight_medium_1B.first),(internalCSVweight_medium_1B.second));
    double internalCSVweight_medium_LFUP_1B_final   = divideSavely((internalCSVweight_medium_LFUP_1B.first),(internalCSVweight_medium_LFUP_1B.second));
    double internalCSVweight_medium_LFDOWN_1B_final = divideSavely((internalCSVweight_medium_LFDOWN_1B.first),(internalCSVweight_medium_LFDOWN_1B.second));
    double internalCSVweight_medium_HFUP_1B_final   = divideSavely((internalCSVweight_medium_HFUP_1B.first),(internalCSVweight_medium_HFUP_1B.second));
    double internalCSVweight_medium_HFDOWN_1B_final = divideSavely((internalCSVweight_medium_HFDOWN_1B.first),(internalCSVweight_medium_HFDOWN_1B.second));

    double internalCSVweight_medium_ge2B_final        = divideSavely((1-internalCSVweight_medium_0B.first-internalCSVweight_medium_1B.first),(1-internalCSVweight_medium_0B.second-internalCSVweight_medium_1B.second));
    double internalCSVweight_medium_LFUP_ge2B_final   = divideSavely((1-internalCSVweight_medium_LFUP_0B.first-internalCSVweight_medium_LFUP_1B.first),(1-internalCSVweight_medium_LFUP_0B.second-internalCSVweight_medium_LFUP_1B.second));
    double internalCSVweight_medium_LFDOWN_ge2B_final = divideSavely((1-internalCSVweight_medium_LFDOWN_0B.first-internalCSVweight_medium_LFDOWN_1B.first),(1-internalCSVweight_medium_LFDOWN_0B.second-internalCSVweight_medium_LFDOWN_1B.second));
    double internalCSVweight_medium_HFUP_ge2B_final   = divideSavely((1-internalCSVweight_medium_HFUP_0B.first-internalCSVweight_medium_HFUP_1B.first),(1-internalCSVweight_medium_HFUP_0B.second-internalCSVweight_medium_HFUP_1B.second));
    double internalCSVweight_medium_HFDOWN_ge2B_final = divideSavely((1-internalCSVweight_medium_HFDOWN_0B.first-internalCSVweight_medium_HFDOWN_1B.first),(1-internalCSVweight_medium_HFDOWN_0B.second-internalCSVweight_medium_HFDOWN_1B.second));

//    if(N_BTagsM>=2){
//        std::cout << "-------------" << std::endl;
//        std::cout << "internalCSVweight_loose_outside_0B_final: " << internalCSVweight_loose_outside_0B_final << std::endl;
//        // std::cout << "internalCSVweight_loose_outside_zerotag: " << internalCSVweight_loose_outside_zerotag << std::endl;
//        std::cout << "internalCSVweight_loose_outside_ge1B_final: " << internalCSVweight_loose_outside_ge1B_final << std::endl;
//         std::cout << "internalCSVweight_loose_outside_onetag: " << internalCSVweight_loose_outside_onetag << std::endl;
//        std::cout << "internalCSVweight_medium_0B_final: " << internalCSVweight_medium_0B_final << std::endl;
//        std::cout << "internalCSVweight_medium_ge1B_final: " << internalCSVweight_medium_ge1B_final << std::endl;
//        std::cout << "internalCSVweight_medium_ge2B_final: " << internalCSVweight_medium_ge2B_final << std::endl;
//        std::cout << "internalCSVweight_medium_0B.first: " << internalCSVweight_medium_0B.first << std::endl;
//        std::cout << "internalCSVweight_medium_1B.first: " << internalCSVweight_medium_1B.first << std::endl;
//        std::cout << "internalCSVweight_medium_0B.second: " << internalCSVweight_medium_0B.second << std::endl;
//        std::cout << "internalCSVweight_medium_1B.second: " << internalCSVweight_medium_1B.second << std::endl;
//    }
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
    bool DeltaPhi_AK4Jets_MET_Larger_0p7;
    DeltaPhi_AK4Jets_MET_Larger_0p7 = check_if_every_element_greater(DeltaPhi_AK4Jet_MET.get(), N_Jets, N_Jets, 0.7);
    bool DeltaPhi_AK4Jets_Recoil_Larger_0p8;
    DeltaPhi_AK4Jets_Recoil_Larger_0p8 = check_if_every_element_greater(DeltaPhi_AK4Jet_Hadr_Recoil.get(), N_Jets, N_Jets, 0.8);
    
    //bool AK15Jets_NHF_Smaller_0p8;
    //AK15Jets_NHF_Smaller_0p8 = check_if_every_element_smaller(AK15Jet_NHF.get(), N_AK15Jets, N_AK15Jets, 0.8);
    //bool AK15Jets_CHF_Larger_0p1;
    //AK15Jets_CHF_Larger_0p1 = check_if_every_element_greater(AK15Jet_CHF.get(), N_AK15Jets, N_AK15Jets, 0.1);
    
    bool min_AK15Jet_pt = check_if_every_element_greater(AK15Jet_Pt.get(), N_AK15Jets, N_AK15Jets, 160.);
    
    if(N_AK15Jets>0) weight_sdm_corr = get_msd_weight(AK15Jet_Pt[0], AK15Jet_Eta[0]);

    // hack against prefireweight with 2018 signal samples
    //if(processname.find("vectormonotop")!=std::string::npos) {
    //    Weight_L1_Prefire = 1.0;
    //    Weight_L1_Prefire_Up = 1.0;
    //    Weight_L1_Prefire_Down = 1.0;
    //}
