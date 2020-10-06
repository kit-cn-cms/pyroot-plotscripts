// struct to store information 1D histograms
struct Plot1DInfoStruct {
    std::string          identifier;
    std::string          title;
    int                  nbins;
    std::vector< float > edges;
    // std::unique_ptr<TH1> histoptr;
};

// Helper struct to fill plots more efficiently
// Until GCC 4.9 struct cannot have init values if one wants to initialize it with bracket lists
struct structHelpFillHisto {
    TH1*   histo;
    double weight;
};

// helper function to fill plots more efficiently
void helperFillHisto(const std::vector< structHelpFillHisto >& paramVec, const double& val)
{
    for (const auto& singleParams : paramVec)
    // singleParams: histo, var, weight
    {
        if ((singleParams.weight) != 0)
            singleParams.histo->Fill(fmin(singleParams.histo->GetXaxis()->GetXmax() - 1e-6, fmax(singleParams.histo->GetXaxis()->GetXmin() + 1e-6, val)),
                                     singleParams.weight);
    }
}

// Helper struct to fill plots more efficiently
// Until GCC 4.9 struct cannot have init values if one wants to initialize it with bracket lists
struct Plot2DInfoStruct {
    std::string          identifier;
    std::string          title;
    int                  nbinsx;
    std::vector< float > edges_x;
    int                  nbinsy;
    std::vector< float > edges_y;
    // std::unique_ptr<TH2> histoptr;
};

struct structHelpFillTwoDimHisto {
    TH2*   histo;
    double weight;
};

// helper function to fill plots more efficiently
void helperFillTwoDimHisto(const std::vector< structHelpFillTwoDimHisto >& paramVec, const double& val1, const double& val2)
{
    for (const auto& singleParams : paramVec)
    // singleParams: histo, var1, var2, weight
    {
        if ((singleParams.weight) != 0)
            singleParams.histo->Fill(fmin(singleParams.histo->GetXaxis()->GetXmax() - 1e-6, fmax(singleParams.histo->GetXaxis()->GetXmin() + 1e-6, val1)),
                                     fmin(singleParams.histo->GetYaxis()->GetXmax() - 1e-6, fmax(singleParams.histo->GetYaxis()->GetXmin() + 1e-6, val2)),
                                     singleParams.weight);
    }
}

inline bool check_if_every_element_smaller(auto* array, int number_of_elements, int max_number_of_elements, float value){
    if(number_of_elements == 0) return false;
    for(int i=0;(i<number_of_elements) && (i<max_number_of_elements);i++){
        if(array[i]>value){
            return false;
        }
    }
    return true;
}
inline bool check_if_every_element_greater(auto* array, int number_of_elements, int max_number_of_elements, float value){
    if(number_of_elements == 0) return false;
    for(int i=0;(i<number_of_elements) && (i<max_number_of_elements);i++){
        if(array[i]<value){
            return false;
        }
    }
    return true;
}

inline bool HEM_veto(auto* eta, auto* phi, int n_jets){
    if(n_jets==0) return false;
    for(int i=0;i<n_jets;i++){
        if((eta[i]<-1.3 && eta[i]>-3.2) && (phi[i]>-1.57 && phi[i]<-0.87)) return true;
    }
    return false;
}

inline double divideSavely(double num, double den, double returnVal = 1.){
    if (den == 0.){
        return returnVal;
    }
    else return num/den;
}

float get_msd_weight(float pt, float eta){
    // according to https://github.com/mcremone/decaf/blob/master/analysis/util/corrections.py#L202
    // gpar = np.array([1.00626, -1.06161, 0.0799900, 1.20454])
    // cpar = np.array([1.09302, -0.000150068, 3.44866e-07, -2.68100e-10, 8.67440e-14, -1.00114e-17])
    // fpar = np.array([1.27212, -0.000571640, 8.37289e-07, -5.20433e-10, 1.45375e-13, -1.50389e-17])
    // genw = gpar[0] + gpar[1]*np.power(pt*gpar[2], -gpar[3])
    // ptpow = np.power.outer(pt, np.arange(cpar.size))    
    // cenweight = np.dot(ptpow, cpar)
    // forweight = np.dot(ptpow, fpar)
    // weight = np.where(np.abs(eta)<1.3, cenweight, forweight)
    // return genw*weight
    std::vector<float> gpar = {1.00626, -1.06161, 0.0799900, 1.20454};
    std::vector<float> cpar = {1.09302, -0.000150068, 3.44866e-07, -2.68100e-10, 8.67440e-14, -1.00114e-17};
    std::vector<float> fpar = {1.27212, -0.000571640, 8.37289e-07, -5.20433e-10, 1.45375e-13, -1.50389e-17};
    float genw = gpar[0] + gpar[1]*pow(pt*gpar[2], -gpar[3]);
    std::vector<float> ptpow; 
    float cenweight = 0.;
    float forweight = 0.;
    for (int i = 0; i<cpar.size(); ++i){
        ptpow.push_back(pow(pt,i));
        cenweight += cpar[i]*pow(pt,i);
        forweight += fpar[i]*pow(pt,i);
    } 
    float weight = 0.;
    if (abs(eta)<1.3){
        weight = cenweight;
    }
    else {
        weight = forweight;
    }
    // std::cout << "--------" << std::endl;
    // std::cout << "getting msd correction weight for Pt: " << pt << " Eta: " << eta << std::endl;
    // std::cout << "genw*weight: " << genw*weight << std::endl;
    // std::cout << "genw: " << genw << std::endl;
    // std::cout << "weight: " << weight << std::endl;
    // std::cout << "cenweight: " << cenweight << std::endl;
    // std::cout << "forweight: " << forweight << std::endl;
    return genw*weight;
}


void plot()
{
    TH1F::SetDefaultSumw2();

    // open files
    TChain*     chain             = new TChain("MVATree");
    char*       filenames         = getenv("FILENAMES");
    char*       outfilename       = getenv("OUTFILENAME");
    std::string plotscriptBaseDir = getenv("PLOTSCRIPTBASEDIR");
    string      processname       = string(getenv("PROCESSNAME"));
    string      suffix            = string(getenv("SUFFIX"));
    int         maxevents         = atoi(getenv("MAXEVENTS"));
    int         skipevents        = atoi(getenv("SKIPEVENTS"));
    string      eventFilterFile   = string(getenv("EVENTFILTERFILE"));
    std::string dataera           = string(getenv("DATAERA"));

    // create vector of systematics
    std::vector< Systematics::Type > v_SystTypes = Systematics::getTypeVector();
    // for(auto itsyst : v_SystTypes){std::cout<< " Know :" << itsyst << std::endl;}

    std::cout << "processname: " << processname << std::endl;
    std::cout << "suffix: " << suffix << std::endl;

    std::vector< TString > databaseRelevantFilenames;

    int   eventsAnalyzed = 0;
    float sumOfWeights   = 0;

    int DoWeights     = 1;
    int isTthSample   = 0;
    int electron_data = 0;
    int muon_data     = 0;

    // BTAG SF Stuff
    std::string csvFile = "";
    std::string effFile = "";
    double wp_loose = 0.;
    double wp_medium = 0.;
    if( dataera == "2016" ) {
        csvFile=plotscriptBaseDir+"/data/CSV/sfs_deepjet_fixedWP_2016.csv";
        effFile=plotscriptBaseDir+"/data/CSV/btag_efficiencies_deepjet_pfmet_more_cuts_2016.root";
        wp_loose = 	0.0614;
        wp_medium = 0.3093;
        }
    else if( dataera == "2017" ) {
        csvFile=plotscriptBaseDir+"/data/CSV/sfs_deepjet_fixedWP_2017.csv";
        effFile=plotscriptBaseDir+"/data/CSV/btag_efficiencies_deepjet_pfmet_more_cuts_2017.root";
        wp_loose = 	0.0521;
        wp_medium = 0.3033;
        }
    else if( dataera == "2018" ) {
        csvFile=plotscriptBaseDir+"/data/CSV/sfs_deepjet_fixedWP_2018.csv";
        effFile=plotscriptBaseDir+"/data/CSV/btag_efficiencies_deepjet_pfmet_more_cuts_2018.root";
	    wp_loose = 	0.0494;
        wp_medium = 0.2770;
        }
    else {
        std::cout << "NO VALID DATAERA CHOSEN!!" << std::endl;
        std::cout << "dataera: " << dataera << std::endl;
    }

    BtagSFHelper* internalBtagSFHelper_loose= new BtagSFHelper(csvFile,effFile, "loose", wp_loose);
    BtagSFHelper* internalBtagSFHelper_medium= new BtagSFHelper(csvFile,effFile, "medium", wp_medium);
    BtagSFHelper* internalBtagSFHelper_loose_outside= new BtagSFHelper(csvFile,effFile, "loose_outside", wp_loose);
    BtagSFHelper* internalBtagSFHelper_medium_outside= new BtagSFHelper(csvFile,effFile, "medium_outside", wp_medium);

    // Dark Higgs Pileup weights
    SFHelper pu_helper;
    if( dataera == "2018" ) {
        pu_helper.AddScaleFactorHistogram("Nom","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/puweights/PileupHistograms_2018_69mb_pm5.root","pu_weights_central");
        pu_helper.AddScaleFactorHistogram("Up","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/puweights/PileupHistograms_2018_69mb_pm5.root","pu_weights_up");
        pu_helper.AddScaleFactorHistogram("Down","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/puweights/PileupHistograms_2018_69mb_pm5.root","pu_weights_down");
    }
    else if( dataera == "2017" ) {
        pu_helper.AddScaleFactorHistogram("Nom","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/puweights/PileupHistograms_2017_69mb_pm5.root","pu_weights_central");
        pu_helper.AddScaleFactorHistogram("Up","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/puweights/PileupHistograms_2017_69mb_pm5.root","pu_weights_up");
        pu_helper.AddScaleFactorHistogram("Down","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/puweights/PileupHistograms_2017_69mb_pm5.root","pu_weights_down");
    }
    else if( dataera == "2016" ) {
        pu_helper.AddScaleFactorHistogram("Nom","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/puweights/PileupHistograms_2016_69mb_pm5.root","pu_weights_central");
        pu_helper.AddScaleFactorHistogram("Up","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/puweights/PileupHistograms_2016_69mb_pm5.root","pu_weights_up");
        pu_helper.AddScaleFactorHistogram("Down","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/puweights/PileupHistograms_2016_69mb_pm5.root","pu_weights_down");
    }
    else {
        std::cout << "NO VALID DATAERA CHOSEN!!" << std::endl;
        std::cout << "dataera: " << dataera << std::endl;
    }

    // vjets nlo qcd k factors from monojet
    SFHelper qcd_nlo_znunu;
    SFHelper qcd_nlo_zll;
    SFHelper qcd_nlo_wlnu;
    SFHelper qcd_nlo_gamma;
    if ( dataera == "2018" || dataera == "2017") {
        qcd_nlo_znunu.AddScaleFactorHistogram("qcd_nlo_znunu","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/vjets_SFs/SF_QCD_NLO_ZJetsToNuNu.root","kfac_znn_filter");
        qcd_nlo_zll.AddScaleFactorHistogram("qcd_nlo_zll","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/vjets_SFs/SF_QCD_NLO_DYJetsToLL.root","kfac_dy_filter");
        qcd_nlo_wlnu.AddScaleFactorHistogram("qcd_nlo_wlnu","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/vjets_SFs/SF_QCD_NLO_WJetsToLNu.root","wjet_dress_monojet");
        qcd_nlo_gamma.AddScaleFactorHistogram("qcd_nlo_gamma","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/vjets_SFs/SF_QCD_NLO_GJets.root","gjets_stat1_monojet");
    }
    else if ( dataera == "2016" ) {
        qcd_nlo_znunu.AddScaleFactorHistogram("qcd_nlo_znunu","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/vjets_SFs/merged_kfactors_zjets.root","kfactor_monojet_qcd");
        qcd_nlo_zll.AddScaleFactorHistogram("qcd_nlo_zll","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/vjets_SFs/merged_kfactors_zjets.root","kfactor_monojet_qcd");
        qcd_nlo_wlnu.AddScaleFactorHistogram("qcd_nlo_wlnu","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/vjets_SFs/merged_kfactors_wjets.root","kfactor_monojet_qcd");
        qcd_nlo_gamma.AddScaleFactorHistogram("qcd_nlo_gamma","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/vjets_SFs/merged_kfactors_gjets.root","kfactor_monojet_qcd");
    }
    else {
        std::cout << "NO VALID DATAERA CHOSEN!!" << std::endl;
        std::cout << "dataera: " << dataera << std::endl;
    }
    
    // vjets nlo ewk k factors from monojet
    SFHelper ewk_nlo_z;
    ewk_nlo_z.AddScaleFactorHistogram("ewk_nlo_z","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/vjets_SFs/merged_kfactors_zjets.root","kfactor_monojet_ewk");
    SFHelper ewk_nlo_wlnu;
    ewk_nlo_wlnu.AddScaleFactorHistogram("ewk_nlo_wlnu","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/vjets_SFs/merged_kfactors_wjets.root","kfactor_monojet_ewk");
    SFHelper ewk_nlo_gamma;
    ewk_nlo_gamma.AddScaleFactorHistogram("ewk_nlo_gamma","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/vjets_SFs/merged_kfactors_gjets.root","kfactor_monojet_ewk");

    // tau scale factors
    SFHelper tau_sfs;
    if ( dataera == "2018" ) {
        tau_sfs.AddScaleFactorHistogram("tau_sfs","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/tau_SFs/tau_sf.root","tau_sf_VLoose_2018_cent");
        tau_sfs.AddScaleFactorHistogram("tau_sfs_up","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/tau_SFs/tau_sf.root","tau_sf_VLoose_2018_up");
        tau_sfs.AddScaleFactorHistogram("tau_sfs_down","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/tau_SFs/tau_sf.root","tau_sf_VLoose_2018_down");
    }
    else if ( dataera == "2017" ) {
        tau_sfs.AddScaleFactorHistogram("tau_sfs","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/tau_SFs/tau_sf.root","tau_sf_VLoose_2017_cent");
        tau_sfs.AddScaleFactorHistogram("tau_sfs_up","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/tau_SFs/tau_sf.root","tau_sf_VLoose_2017_up");
        tau_sfs.AddScaleFactorHistogram("tau_sfs_down","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/tau_SFs/tau_sf.root","tau_sf_VLoose_2017_down");
    }
    else if ( dataera == "2016" ) {
        tau_sfs.AddScaleFactorHistogram("tau_sfs","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/tau_SFs/tau_sf.root","tau_sf_VLoose_2016_cent");
        tau_sfs.AddScaleFactorHistogram("tau_sfs_up","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/tau_SFs/tau_sf.root","tau_sf_VLoose_2016_up");
        tau_sfs.AddScaleFactorHistogram("tau_sfs_down","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/tau_SFs/tau_sf.root","tau_sf_VLoose_2016_down");
    }
    else {
        std::cout << "NO VALID DATAERA CHOSEN!!" << std::endl;
        std::cout << "dataera: " << dataera << std::endl;
    }
    
    
    // electron ID scale factors
    SFHelper eleID_sfs;
    if ( dataera == "2018" ) {
        eleID_sfs.AddScaleFactorHistogram2D("veto_ID_sfs","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/electronSFs/2018_ElectronVeto_Fall17V2.root","EGamma_SF2D");
        eleID_sfs.AddScaleFactorHistogram2D("tight_ID_sfs","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/electronSFs/2018_ElectronTight_Fall17V2.root","EGamma_SF2D");
    }
    else if ( dataera == "2017" ) {
        eleID_sfs.AddScaleFactorHistogram2D("veto_ID_sfs","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/electronSFs/2017_ElectronVeto_Fall17V2.root","EGamma_SF2D");
        eleID_sfs.AddScaleFactorHistogram2D("tight_ID_sfs","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/electronSFs/2017_ElectronTight_Fall17V2.root","EGamma_SF2D");
    }
    else if ( dataera == "2016" ) {
        eleID_sfs.AddScaleFactorHistogram2D("veto_ID_sfs","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/electronSFs/2016_ElectronVeto_Fall17V2.root","EGamma_SF2D");
        eleID_sfs.AddScaleFactorHistogram2D("tight_ID_sfs","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/electronSFs/2016_ElectronTight_Fall17V2.root","EGamma_SF2D");
    }
    else {
        std::cout << "NO VALID DATAERA CHOSEN!!" << std::endl;
        std::cout << "dataera: " << dataera << std::endl;
    }
    
    // photon pt extrapolation uncertainty for 2017 and 2018 from mono-jet group
    SFHelper PhotonExtrapolationUnc;
    if ( dataera == "2018" ) {
        PhotonExtrapolationUnc.AddScaleFactorHistogram("photon_extrapolation_unc","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/photon_SFs/photon_medium_id_sf_v0.root","photon_medium_id_extrap_unc_2018");
    }
    else if ( dataera == "2017" ) {
        PhotonExtrapolationUnc.AddScaleFactorHistogram("photon_extrapolation_unc","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/photon_SFs/photon_medium_id_sf_v0.root","photon_medium_id_extrap_unc_2017");
    }
    else if ( dataera == "2016" ) {
    }
    else {
        std::cout << "NO VALID DATAERA CHOSEN!!" << std::endl;
        std::cout << "dataera: " << dataera << std::endl;
    }

    // MET Phi SFs
    //SFHelper METPhi_SFs;
    //METPhi_SFs.AddScaleFactorHistogram("SR_El","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/METPhiSFs/DeltaPhi_LooseLepton_MET_SFs.root","DeltaPhi_LooseElectron_MET_lep_SR_El_SFs");
    //METPhi_SFs.AddScaleFactorHistogram("SR_Mu","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/METPhiSFs/DeltaPhi_LooseLepton_MET_SFs.root","DeltaPhi_LooseMuon_MET_lep_SR_Mu_SFs");
    //METPhi_SFs.AddScaleFactorHistogram("CR_WEl","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/METPhiSFs/DeltaPhi_LooseLepton_MET_SFs.root","DeltaPhi_LooseElectron_MET_lep_CR_WEl_SFs");
    //METPhi_SFs.AddScaleFactorHistogram("CR_WMu","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/METPhiSFs/DeltaPhi_LooseLepton_MET_SFs.root","DeltaPhi_LooseMuon_MET_lep_CR_WMu_SFs");
    //METPhi_SFs.AddScaleFactorHistogram("CR_ttbarEl","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/METPhiSFs/DeltaPhi_LooseLepton_MET_SFs.root","DeltaPhi_LooseElectron_MET_lep_CR_ttbarEl_SFs");
    //METPhi_SFs.AddScaleFactorHistogram("CR_ttbarMu","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/METPhiSFs/DeltaPhi_LooseLepton_MET_SFs.root","DeltaPhi_LooseMuon_MET_lep_CR_ttbarMu_SFs");
    
    // Hack for subsampling test
    // if(processname=="SingleEl" || processname=="SingleMu"){DoWeights=0; std::cout<<"is data, dont use nominal weihgts"<<std::endl;}
    if ((processname.find("SingleEl") != std::string::npos) || (processname.find("SingleMu") != std::string::npos) ||
        (processname.find("MET") != std::string::npos && processname.find("Uncl")==std::string::npos) || (processname.find("SinglePh") != std::string::npos)) {
        DoWeights = 0;
        std::cout << "is data, dont use nominal weights!!!!" << std::endl;
    }


    // read in samples to add to chain and get relevant names for the database
    std::map< TString, TString >                   sampleDataBaseIdentifiers;
    std::map< TString, std::map< TString, long > > sampleDataBaseFoundEvents;
    std::map< TString, std::map< TString, long > > sampleDataBaseLostEvents;
    std::map< TString, TString >                   sampleTranslationMapCPP;

    // vector to hold the jes uncertainty names
    std::vector< TString > SystListForDataBase;

    Systematics::Type internalSystType = Systematics::NA;

    // DANGERZONE
    // This will not work if mixing multiple systematics in one job!!
    TString globalFileNameForSystType = "";

    string       buf;
    stringstream ss(filenames);
    TString      samplename_in_database = "";
    while (ss >> buf) {
        chain->Add(buf.c_str());
    }  // end loop of filename parsing


    chain->SetBranchStatus("*", 0);

    TFile* outfile = new TFile(outfilename, "RECREATE");

    TStopwatch* totalWatch    = new TStopwatch();
    TStopwatch* databaseWatch = new TStopwatch();
    double      memTime       = 0;

    int      nEventsVetoed = 0;
    Long64_t Evt_ID;
    Long64_t Evt_Run;
    Long64_t Evt_Lumi;

    Int_t Evt_ID_INT;
    Int_t Evt_Run_INT;
    Int_t Evt_Lumi_INT;

    chain->SetBranchStatus("Evt_ID", 1);
    chain->SetBranchStatus("Evt_Run", 1);
    chain->SetBranchStatus("Evt_Lumi", 1);

    // figure out what kind of branch this is
    bool evtIDisIntBranch = 1;
    // TBranch* evtBranch=chain->GetBranch("Evt_ID");
    // TString branchNameString=TString(evtBranch->GetTitle());
    // if(branchNameString.Contains("/L")){
    //  evtIDisIntBranch=0;
    chain->SetBranchAddress("Evt_ID", &Evt_ID);
    chain->SetBranchAddress("Evt_Run", &Evt_Run);
    chain->SetBranchAddress("Evt_Lumi", &Evt_Lumi);
    //}
    // else{
    // chain->SetBranchAddress("Evt_ID",&Evt_ID_INT);
    // chain->SetBranchAddress("Evt_Run",&Evt_Run_INT);
    // chain->SetBranchAddress("Evt_Lumi",&Evt_Lumi_INT);
    //}

    // some timers
    double totalTime                  = 0;
    double totalTimeGetEntry          = 0;
    double totalTimeFillHistograms    = 0;
    double totalTimeReadDataBase      = 0;
    double totalTimeEvalDNN           = 0;
    double totalTimeEvalWeightsAndBDT = 0;
    double totalTimeSampleWeight      = 0;
    double totalTimeCalculateSFs      = 0;
    double totalTimeMapping           = 0;

    TStopwatch* timerGetEntry          = new TStopwatch();
    TStopwatch* timerFillHistograms    = new TStopwatch();
    TStopwatch* timerReadDataBase      = new TStopwatch();
    TStopwatch* timerEvalDNN           = new TStopwatch();
    TStopwatch* timerEvalWeightsAndBDT = new TStopwatch();
    TStopwatch* timerSampleWeight      = new TStopwatch();
    TStopwatch* timerCalculateSFs      = new TStopwatch();
    TStopwatch* timerTotal             = new TStopwatch();
    TStopwatch* timerMapping           = new TStopwatch();

    // initialize variables from tree
