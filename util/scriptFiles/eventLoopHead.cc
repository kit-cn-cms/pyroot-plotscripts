timerTotal->Start();
// loop over all events
long nentries = chain->GetEntries();
cout << "total number of events: " << nentries << endl;

for (long iEntry = skipevents; iEntry < nentries; iEntry++) {
    if(iEntry==maxevents) break;
    if(iEntry%10000==0) cout << "analyzing event " << iEntry << " of " << nentries << " Total events" << endl;
    
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

    std::string currentfilename = "";
    currentfilename         = chain->GetCurrentFile()->GetName();
    bool wlnujets_ht = processname.find("wlnujets")!=std::string::npos && currentfilename.find("WJetsToLNu_HT")!=std::string::npos;
    //std::cout << "wlnujets_ht flag: " << wlnujets_ht << std::endl;
    //std::cout << "file name " << currentfilename << std::endl;
    //int hasTrigger          = 0;
    //if (currentfilename.Index("withTrigger") != -1) { hasTrigger = 1; }
    eventsAnalyzed++;
    sumOfWeights += Weight;


    totalTimeGetEntry += timerGetEntry->RealTime();
    timerCalculateSFs->Start();
    
    // HEM veto
    bool internalNOHEMEvent = true;
    internalNOHEMEvent = !HEM_veto(LooseJet_Eta.get(),LooseJet_Phi.get(),N_LooseJets);
    //std::cout << "NO HEM event: " << internalNOHEMEvent << std::endl;

    // weights for higher-order vjets reweighting based on Lindert paper
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

    float internalBosonWeight_W_low_pt_Up = 1.0;
    float internalBosonWeight_W_low_pt_Down = 1.0;
    
    float internalBosonWeight_G_low_pt_Up = 1.0;
    float internalBosonWeight_G_low_pt_Down = 1.0;

    if ((processname.find("wlnujets") != std::string::npos && W_Pt > 100. && wlnujets_ht) || (processname.find("zlljets") != std::string::npos && Z_Pt > 100.) ||
        (processname.find("znunujets") != std::string::npos && Z_Pt > 100.) || (processname.find("gammajets") != std::string::npos && Gamma_Pt > 100.)) {
        if (BosonWeight_nominal>0.){
        internalBosonWeight           = BosonWeight_nominal;
        internalBosonWeight_QCD1Up    = BosonWeight_QCD1Up/internalBosonWeight;
        internalBosonWeight_QCD1Down  = BosonWeight_QCD1Down/internalBosonWeight;
        internalBosonWeight_QCD2Up    = BosonWeight_QCD2Up/internalBosonWeight;
        internalBosonWeight_QCD2Down  = BosonWeight_QCD2Down/internalBosonWeight;
        internalBosonWeight_QCD3Up    = BosonWeight_QCD3Up/internalBosonWeight;
        internalBosonWeight_QCD3Down  = BosonWeight_QCD3Down/internalBosonWeight;
        internalBosonWeight_EW1Up     = BosonWeight_EW1Up/internalBosonWeight;
        internalBosonWeight_EW1Down   = BosonWeight_EW1Down/internalBosonWeight;
        internalBosonWeight_EW2Up     = BosonWeight_EW2Up/internalBosonWeight;
        internalBosonWeight_EW2Down   = BosonWeight_EW2Down/internalBosonWeight;
        internalBosonWeight_EW3Up     = BosonWeight_EW3Up/internalBosonWeight;
        internalBosonWeight_EW3Down   = BosonWeight_EW3Down/internalBosonWeight;
        internalBosonWeight_MixedUp   = BosonWeight_MixedUp/internalBosonWeight;
        internalBosonWeight_MixedDown = BosonWeight_MixedDown/internalBosonWeight;
        internalBosonWeight_AlphaSUp  = BosonWeight_AlphaUp/internalBosonWeight;
        internalBosonWeight_AlphaSDown= BosonWeight_AlphaDown/internalBosonWeight;
        internalBosonWeight_muRUp     = BosonWeight_muRUp/internalBosonWeight;
        internalBosonWeight_muRDown   = BosonWeight_muRDown/internalBosonWeight;
        internalBosonWeight_muFUp     = BosonWeight_muFUp/internalBosonWeight;
        internalBosonWeight_muFDown   = BosonWeight_muFDown/internalBosonWeight;
        }
    }
    
    // additional uncertainty for low pt w bosons because of missing HT 0To70
    //if (processname.find("wlnujets") != std::string::npos && W_Pt > 30. && W_Pt < 100.){
    //    internalBosonWeight_W_low_pt_Up = 1.5;
    //    internalBosonWeight_W_low_pt_Down = 0.5;
    //}
    
    // additional uncertainty for lower pt isolated photons because of crude isolation calculation and and weird corrections behavior in this range
    if (processname.find("gammajets") != std::string::npos && Gamma_Pt > 100. && Gamma_Pt < 290.){
        internalBosonWeight_G_low_pt_Up = 1.5;
        internalBosonWeight_G_low_pt_Down = 0.5;
    }

    // monojet higher-order vjets k factors
    float qcd_nlo_sf = 1.0;
    float ewk_nlo_sf = 1.0;
    float internalBosonWeight_monojet = 1.0;
    float internalBosonWeight_monojet_low_pt_up = 1.0;
    float internalBosonWeight_monojet_low_pt_down = 1.0;
    if (processname.find("wlnujets") != std::string::npos && W_Pt > 0. && wlnujets_ht) {
        qcd_nlo_sf = qcd_nlo_wlnu.GetScaleFactor("qcd_nlo_wlnu", W_Pt, true);
        ewk_nlo_sf = ewk_nlo_wlnu.GetScaleFactor("ewk_nlo_wlnu", W_Pt, true);
        internalBosonWeight_monojet = qcd_nlo_sf*ewk_nlo_sf;
        if ((W_Pt < qcd_nlo_wlnu.GetHistogramLowerEdge("qcd_nlo_wlnu")) || (W_Pt < ewk_nlo_wlnu.GetHistogramLowerEdge("ewk_nlo_wlnu"))) {
            internalBosonWeight_monojet_low_pt_up = 1.5;
            internalBosonWeight_monojet_low_pt_down = 0.5;
            if (W_Pt > 30.) {
                //internalBosonWeight_monojet = internalBosonWeight;
                float k_factor_ratio = internalBosonWeight/internalBosonWeight_monojet;
                internalBosonWeight_W_low_pt_Up = (k_factor_ratio > 1.0) ? k_factor_ratio : 1.001;
                internalBosonWeight_W_low_pt_Down = 0.999;
            }
        }
    }
    else if (processname.find("znunujets") != std::string::npos && Z_Pt > 0.) {
        qcd_nlo_sf = qcd_nlo_znunu.GetScaleFactor("qcd_nlo_znunu", Z_Pt, true);
        ewk_nlo_sf = ewk_nlo_z.GetScaleFactor("ewk_nlo_z", Z_Pt, true);
        internalBosonWeight_monojet = qcd_nlo_sf*ewk_nlo_sf;
        if ((Z_Pt < qcd_nlo_znunu.GetHistogramLowerEdge("qcd_nlo_znunu")) || (Z_Pt < ewk_nlo_z.GetHistogramLowerEdge("ewk_nlo_z"))) {
            internalBosonWeight_monojet_low_pt_up = 1.5;
            internalBosonWeight_monojet_low_pt_down = 0.5;
        }
    }
    else if (processname.find("zlljets") != std::string::npos && Z_Pt > 0.) {
        qcd_nlo_sf = qcd_nlo_zll.GetScaleFactor("qcd_nlo_zll", Z_Pt, true);
        ewk_nlo_sf = ewk_nlo_z.GetScaleFactor("ewk_nlo_z", Z_Pt, true);
        internalBosonWeight_monojet = qcd_nlo_sf*ewk_nlo_sf;
        if ((Z_Pt < qcd_nlo_zll.GetHistogramLowerEdge("qcd_nlo_zll")) || (Z_Pt < ewk_nlo_z.GetHistogramLowerEdge("ewk_nlo_z"))) {
            internalBosonWeight_monojet_low_pt_up = 1.5;
            internalBosonWeight_monojet_low_pt_down = 0.5;
        }
    }
    else if (processname.find("gammajets") != std::string::npos && N_GenPhotons > 0) {
        float lead_gen_photon_pt = *std::max_element(GenPhoton_Pt.get(),GenPhoton_Pt.get()+N_GenPhotons);
        //std::cout << "lead gen photon pt " << lead_gen_photon_pt << std::endl;
        qcd_nlo_sf = qcd_nlo_gamma.GetScaleFactor("qcd_nlo_gamma", lead_gen_photon_pt, true);
        ewk_nlo_sf = ewk_nlo_gamma.GetScaleFactor("ewk_nlo_gamma", lead_gen_photon_pt, true);
        if(dataera == "2016"){
            internalBosonWeight_monojet = qcd_nlo_sf*ewk_nlo_sf;
        }
        else if(dataera == "2017" || dataera == "2018"){
            internalBosonWeight_monojet = ewk_nlo_sf;
        }
        else {
            std::cout << "NO VALID DATAERA CHOSEN!!" << std::endl;
            std::cout << "dataera: " << dataera << std::endl;
        }
        if ((lead_gen_photon_pt < qcd_nlo_gamma.GetHistogramLowerEdge("qcd_nlo_gamma")) || (lead_gen_photon_pt < ewk_nlo_gamma.GetHistogramLowerEdge("ewk_nlo_gamma"))) {
            internalBosonWeight_monojet_low_pt_up = 1.5;
            internalBosonWeight_monojet_low_pt_down = 0.5;
        }
    }
    
    //std::cout << "NLO QCD SF from monojet: " << qcd_nlo_sf << std::endl;
    //std::cout << "NLO EWK SF from monojet: " << ewk_nlo_sf << std::endl;
    //std::cout << "COMBINED SF from monojet: " << internalBosonWeight_monojet << std::endl;
    
    // use Lindert theory corrections in any case at the moment
    //if (processname.find("gammajets") != std::string::npos){
    //    internalBosonWeight_monojet = internalBosonWeight;
    //}
    
    // additional uncertainty for for v+heavy flavor jet events
    float vjets_hf_up = 1.0;
    float vjets_hf_down = 1.0;
    float vjets_cf_up = 1.0;
    float vjets_cf_down = 1.0;
    float vjets_lf_up = 1.0;
    float vjets_lf_down = 1.0;
    if ((processname.find("wlnujets") != std::string::npos) || (processname.find("zlljets") != std::string::npos) ||
        (processname.find("znunujets") != std::string::npos) || (processname.find("gammajets") != std::string::npos)) {
        if (N_BQuarks > 0) {
            vjets_hf_up = 2.0;
            vjets_hf_down = 0.0;
        }
        else if (N_CQuarks > 0) {
            vjets_cf_up = 1.3;
            vjets_cf_down = 0.7;
        }
        else {
            vjets_lf_up = 1.15;
            vjets_lf_down = 0.85;
        }
    }
    
    // DarkHiggs PU Weights
    float internalPUWeight = 1.0;
    float internalPUWeight_Up = 1.0;
    float internalPUWeight_Down = 1.0;

    internalPUWeight = pu_helper.GetScaleFactor("Nom", N_GenPVs, false);
    internalPUWeight_Up = pu_helper.GetScaleFactor("Up", N_GenPVs, false);
    internalPUWeight_Down = pu_helper.GetScaleFactor("Down", N_GenPVs, false);
    
    // tau sfs
    float internalTauSF = 1.0;
    float internalTauSFUp = 1.0;
    float internalTauSFDown = 1.0;
    for (uint iTau = 0; iTau < N_Taus; iTau++) {
        internalTauSF *= tau_sfs.GetScaleFactor("tau_sfs", Tau_Pt[iTau], true);
        internalTauSFUp *= tau_sfs.GetScaleFactor("tau_sfs_up", Tau_Pt[iTau], true);
        internalTauSFDown *= tau_sfs.GetScaleFactor("tau_sfs_down", Tau_Pt[iTau], true);
    }
    //std::cout << "Tau Weight: " << internalTauSF << std::endl;
    //std::cout << "Tau Weight Up: " << internalTauSFUp << std::endl;
    //std::cout << "Tau Weight Down: " << internalTauSFDown << std::endl;
    
    // electron ID sfs
    float internalEleIDLooseSF = 1.0;
    float internalEleIDLooseSFUp = 1.0;
    float internalEleIDLooseSFDown = 1.0;
    
    float internalEleIDTightSF = 1.0;
    float internalEleIDTightSFUp = 1.0;
    float internalEleIDTightSFDown = 1.0;
    
    for (uint iEleLoose = 0; iEleLoose < N_LooseElectrons; iEleLoose++) {
        std::vector<float> ele_sfs = eleID_sfs.GetScaleFactorPlusUnc2D("veto_ID_sfs", LooseElectron_Eta_Supercluster[iEleLoose], LooseElectron_Pt[iEleLoose], true);
        internalEleIDLooseSF *= ele_sfs[0];
        internalEleIDLooseSFUp *= ele_sfs[1];
        internalEleIDLooseSFDown *= ele_sfs[2];
    }
    for (uint iEleTight = 0; iEleTight < N_TightElectrons; iEleTight++) {
        std::vector<float> ele_sfs = eleID_sfs.GetScaleFactorPlusUnc2D("tight_ID_sfs", Electron_Eta_Supercluster[iEleTight], Electron_Pt[iEleTight], true);
        internalEleIDTightSF *= ele_sfs[0];
        internalEleIDTightSFUp *= ele_sfs[1];
        internalEleIDTightSFDown *= ele_sfs[2];
    }
    
    //std::cout << "N_LooseELectrons: " << N_LooseElectrons << std::endl;
    //std::cout << "N_TightELectrons: " << N_TightElectrons << std::endl;
    //std::cout << "ele id loose sf: " << internalEleIDLooseSF << std::endl;
    //std::cout << "ele id loose sf up: " << internalEleIDLooseSFUp << std::endl;
    //std::cout << "ele id loose sf down: " << internalEleIDLooseSFDown << std::endl;
    //std::cout << "ele id tight sf: " << internalEleIDTightSF << std::endl;
    //std::cout << "ele id tight sf up: " << internalEleIDTightSFUp << std::endl;
    //std::cout << "ele id tight sf down: " << internalEleIDTightSFDown << std::endl;
    
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
    
    float weight_sdm_corr = 1.0;
    if(N_AK15Jets>0) weight_sdm_corr = get_msd_weight(AK15Jet_Pt[0], AK15Jet_Eta[0]);

    // hack against prefireweight with 2018 signal samples
    //if(processname.find("vectormonotop")!=std::string::npos) {
    //    Weight_L1_Prefire = 1.0;
    //    Weight_L1_Prefire_Up = 1.0;
    //    Weight_L1_Prefire_Down = 1.0;
    //}
    
    float DeltaPhi_Photon_MET = -999.0;
    float DeltaPhi_Photon_Hadr_Recoil = -999.0;
    if (N_LoosePhotons>0){
        DeltaPhi_Photon_MET = fabs(TVector2::Phi_mpi_pi(Evt_Phi_MET - LoosePhoton_Phi[0]));
        DeltaPhi_Photon_Hadr_Recoil = fabs(TVector2::Phi_mpi_pi(Hadr_Recoil_Phi - LoosePhoton_Phi[0]));
    }
    
    // tau veto weights
    float internalTauVetoWeight = 1.;
    float internalTauVetoWeightUp = 1.;
    float internalTauVetoWeightDown = 1.;
    if (N_Taus > 0) {
        internalTauVetoWeight = 1.-internalTauSF;
        internalTauVetoWeightUp = 1.-internalTauSFUp;
        internalTauVetoWeightDown = 1.-internalTauSFDown;
    }
    //std::cout << "Tau Veto Weight: " << internalTauVetoWeight << std::endl;
    //std::cout << "Tau Veto Weight Up: " << internalTauVetoWeightUp << std::endl;
    //std::cout << "Tau Veto Weight Down: " << internalTauVetoWeightDown << std::endl;
    
    //float internal_M_W_transverse = -999.;
    //float internal_MET_Pt = -999.;
    //float internal_MET_Phi = -999.;

    //std::pair<double,double> correctedMET = METXYCorr_Met_MetPhi(Evt_Pt_MET, Evt_Phi_MET, Evt_Run, std::stoi(dataera), DoWeights, N_PrimaryVertices);
    //internal_MET_Pt = correctedMET.first;
    //internal_MET_Phi = correctedMET.second;
    
    //if((N_TightElectrons==1 && N_TightMuons==0) || (N_TightElectrons==0 && N_TightMuons==1)){
    //    float lepton_pt = N_TightElectrons==1 ? Electron_Pt[0] : Muon_Pt[0];
    //    float lepton_phi = N_TightElectrons==1 ? Electron_Phi[0] : Muon_Phi[0];
    //    internal_M_W_transverse = TMath::Sqrt(2*lepton_pt*internal_MET_Pt*(1-TMath::Cos(TVector2::Phi_mpi_pi(lepton_phi-internal_MET_Phi))));
    //    //std::cout << "MET Pt uncorrected: " << Evt_Pt_MET << std::endl;
    //    //std::cout << "MET Pt corrected: " << internal_MET_Pt << std::endl;
    //    //std::cout << "MET Phi uncorrected: " << Evt_Phi_MET << std::endl;
    //    //std::cout << "MET Phi corrected: " << internal_MET_Phi << std::endl;
    //    //std::cout << "mw trans uncorrected: " << M_W_transverse[0] << std::endl;
    //    //std::cout << "mw trans corrected: " << internal_M_W_transverse << std::endl;
    //}
    
    
    //float internalMETPhiSF_SR_El = 1.0;
    //float internalMETPhiSF_SR_Mu = 1.0;
    //float internalMETPhiSF_CR_WEl = 1.0;
    //float internalMETPhiSF_CR_WMu = 1.0;
    //float internalMETPhiSF_CR_ttbarEl = 1.0;
    //float internalMETPhiSF_CR_ttbarMu = 1.0;
    
    //internalMETPhiSF_SR_El = METPhi_SFs.GetScaleFactor("SR_El", DeltaPhi_LooseElectron_MET[0], false);
    //internalMETPhiSF_SR_Mu = METPhi_SFs.GetScaleFactor("SR_Mu", DeltaPhi_LooseMuon_MET[0], false);
    //internalMETPhiSF_CR_WEl = METPhi_SFs.GetScaleFactor("CR_WEl", DeltaPhi_LooseElectron_MET[0], false);
    //internalMETPhiSF_CR_WMu = METPhi_SFs.GetScaleFactor("CR_WMu", DeltaPhi_LooseMuon_MET[0], false);
    //internalMETPhiSF_CR_ttbarEl = METPhi_SFs.GetScaleFactor("CR_ttbarEl", DeltaPhi_LooseElectron_MET[0], false);
    //internalMETPhiSF_CR_ttbarMu = METPhi_SFs.GetScaleFactor("CR_ttbarMu", DeltaPhi_LooseMuon_MET[0], false);

    //std::cout << "MET Phi SF SR_El " << internalMETPhiSF_SR_El << std::endl;
    //std::cout << "MET Phi SF SR_Mu " << internalMETPhiSF_SR_Mu << std::endl;
    //std::cout << "MET Phi SF CR_WEl " << internalMETPhiSF_CR_WEl << std::endl;
    //std::cout << "MET Phi SF CR_WMu " << internalMETPhiSF_CR_WMu << std::endl;
    //std::cout << "MET Phi SF CR_ttbarEl " << internalMETPhiSF_CR_ttbarEl << std::endl;
    //std::cout << "MET Phi SF CR_ttbarMu " << internalMETPhiSF_CR_ttbarMu << std::endl;
    
    //float internalMETPhiSF = 1.0;
    //if(N_TightMuons==0 && N_TightElectrons==1 && N_BTagsM==1) internalMETPhiSF = internalMETPhiSF_SR_El;
    //else if (N_TightMuons==1 && N_TightElectrons==0 && N_BTagsM==1) internalMETPhiSF = internalMETPhiSF_SR_Mu;
    //else if(N_TightMuons==0 && N_TightElectrons==1 && N_BTagsM==0) internalMETPhiSF = internalMETPhiSF_CR_WEl;
    //else if(N_TightMuons==1 && N_TightElectrons==0 && N_BTagsM==0) internalMETPhiSF = internalMETPhiSF_CR_WMu;
    //else if(N_TightMuons==0 && N_TightElectrons==1 && N_BTagsM>=2) internalMETPhiSF = internalMETPhiSF_CR_ttbarEl;
    //else if(N_TightMuons==1 && N_TightElectrons==0 && N_BTagsM>=2) internalMETPhiSF = internalMETPhiSF_CR_ttbarMu;

    //std::cout << "MET Phi SF " << internalMETPhiSF << std::endl;
    
