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

inline bool check_if_every_element_smaller(auto* array, int number_of_elements, float value){
    if(number_of_elements == 0) return false;
    for(int i=0;i<number_of_elements;i++){
        if(array[i]>value){
            return false;
        }
    }
    return true;
}
inline bool check_if_every_element_greater(auto* array, int number_of_elements, float value){
    if(number_of_elements == 0) return false;
    for(int i=0;i<number_of_elements;i++){
        if(array[i]<value){
            return false;
        }
    }
    return true;
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

    // initialize CSV Weight Scale Factor Helper
    std::string process = "";
    process = processname;
    if(processname.find("_CMS_JES")!=std::string::npos) process = processname.substr(0,processname.find("_CMS_JES"));
    if(processname.find("_CMS_JER")!=std::string::npos) process = processname.substr(0,processname.find("_CMS_JER"));
    if(processname.find("vectormonotop")!=std::string::npos) process = "vectormonotop";
    CSVWeightSFHelper csv_calibration_helper_had;
    csv_calibration_helper_had.AddScaleFactorHistogram("znunujets","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/csv_weight_sfs/CSV_Patches_had_znunujets_"+dataera+".root","csv_patches_Hadr_Recoil_Pt_AK15Jet_Pt_0");
    csv_calibration_helper_had.AddScaleFactorHistogram("wlnujets","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/csv_weight_sfs/CSV_Patches_had_wlnujets_"+dataera+".root","csv_patches_Hadr_Recoil_Pt_AK15Jet_Pt_0");
    csv_calibration_helper_had.AddScaleFactorHistogram("zlljets","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/csv_weight_sfs/CSV_Patches_had_zlljets_"+dataera+".root","csv_patches_Hadr_Recoil_Pt_AK15Jet_Pt_0");
    csv_calibration_helper_had.AddScaleFactorHistogram("gammajets","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/csv_weight_sfs/CSV_Patches_had_gammajets_"+dataera+".root","csv_patches_Hadr_Recoil_Pt_AK15Jet_Pt_0");
    csv_calibration_helper_had.AddScaleFactorHistogram("ttbar","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/csv_weight_sfs/CSV_Patches_had_ttbar_"+dataera+".root","csv_patches_Hadr_Recoil_Pt_AK15Jet_Pt_0");
    csv_calibration_helper_had.AddScaleFactorHistogram("singlet","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/csv_weight_sfs/CSV_Patches_had_singlet_"+dataera+".root","csv_patches_Hadr_Recoil_Pt_AK15Jet_Pt_0");
    csv_calibration_helper_had.AddScaleFactorHistogram("diboson","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/csv_weight_sfs/CSV_Patches_had_diboson_"+dataera+".root","csv_patches_Hadr_Recoil_Pt_AK15Jet_Pt_0");
    csv_calibration_helper_had.AddScaleFactorHistogram("qcd","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/csv_weight_sfs/CSV_Patches_had_qcd_"+dataera+".root","csv_patches_Hadr_Recoil_Pt_AK15Jet_Pt_0");
    csv_calibration_helper_had.AddScaleFactorHistogram("vectormonotop","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/csv_weight_sfs/CSV_Patches_had_vectormonotop_"+dataera+".root","csv_patches_Hadr_Recoil_Pt_AK15Jet_Pt_0");
    CSVWeightSFHelper csv_calibration_helper_lep;
    csv_calibration_helper_lep.AddScaleFactorHistogram("znunujets","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/csv_weight_sfs/CSV_Patches_lep_znunujets_"+dataera+".root","csv_patches_M_W_transverse_0_Evt_Pt_MET");
    csv_calibration_helper_lep.AddScaleFactorHistogram("wlnujets","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/csv_weight_sfs/CSV_Patches_lep_wlnujets_"+dataera+".root","csv_patches_M_W_transverse_0_Evt_Pt_MET");
    csv_calibration_helper_lep.AddScaleFactorHistogram("zlljets","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/csv_weight_sfs/CSV_Patches_lep_zlljets_"+dataera+".root","csv_patches_M_W_transverse_0_Evt_Pt_MET");
    csv_calibration_helper_lep.AddScaleFactorHistogram("gammajets","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/csv_weight_sfs/CSV_Patches_lep_gammajets_"+dataera+".root","csv_patches_M_W_transverse_0_Evt_Pt_MET");
    csv_calibration_helper_lep.AddScaleFactorHistogram("ttbar","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/csv_weight_sfs/CSV_Patches_lep_ttbar_"+dataera+".root","csv_patches_M_W_transverse_0_Evt_Pt_MET");
    csv_calibration_helper_lep.AddScaleFactorHistogram("singlet","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/csv_weight_sfs/CSV_Patches_lep_singlet_"+dataera+".root","csv_patches_M_W_transverse_0_Evt_Pt_MET");
    csv_calibration_helper_lep.AddScaleFactorHistogram("diboson","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/csv_weight_sfs/CSV_Patches_lep_diboson_"+dataera+".root","csv_patches_M_W_transverse_0_Evt_Pt_MET");
    csv_calibration_helper_lep.AddScaleFactorHistogram("qcd","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/csv_weight_sfs/CSV_Patches_lep_qcd_"+dataera+".root","csv_patches_M_W_transverse_0_Evt_Pt_MET");
    csv_calibration_helper_lep.AddScaleFactorHistogram("vectormonotop","/nfs/dust/cms/user/mwassmer/MonoTop/pyroot-plotscripts/data/csv_weight_sfs/CSV_Patches_lep_vectormonotop_"+dataera+".root","csv_patches_M_W_transverse_0_Evt_Pt_MET");
    

    // Hack for subsampling test
    // if(processname=="SingleEl" || processname=="SingleMu"){DoWeights=0; std::cout<<"is data, dont use nominal weihgts"<<std::endl;}
    if ((processname.find("SingleEl") != std::string::npos) || (processname.find("SingleMu") != std::string::npos) ||
        (processname.find("MET") != std::string::npos) || (processname.find("SinglePh") != std::string::npos)) {
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
