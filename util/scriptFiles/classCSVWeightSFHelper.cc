
class CSVWeightSFHelper {
   public:
    // see the definition/implementation file for a description of the functions
    CSVWeightSFHelper(TString path_to_sf_file_);
    ~CSVWeightSFHelper();
    float GetScaleFactor(int n_jets, float ht_jets) const;
    void  Reset(TString path_to_sf_file_);

   private:
    // function to load root file with scale factor histogram
    void LoadFile(TString path_to_sf_file_);
    // pointer for the root file containing the desired histograms
    TFile* scalefactor_file = nullptr;
    // path to the root file
    TString path_to_sf_file = "";
    // histograms containing the scale factors for electron and muon channel separately
    TH2D* SF_hist = nullptr;
    // flag if the file and the histograms were read properly
    bool initialized = false;
};

CSVWeightSFHelper::CSVWeightSFHelper(TString path_to_sf_file_)
{
    // just the constructor which loads a root file containing the histograms with the scale factors using the LoadFile function
    LoadFile(path_to_sf_file_);
}

void CSVWeightSFHelper::LoadFile(TString path_to_sf_file_)
{
    // this function loads the file given by a string and initializes the 2 needed histograms if the file was loaded correctly
    path_to_sf_file = path_to_sf_file_;
    if (path_to_sf_file != "") { scalefactor_file = TFile::Open(path_to_sf_file); }
    else {
        std::cout << "CSVWeightSFHelper: no scale factor file given" << std::endl;
        throw std::exception();
    }
    if (scalefactor_file) {
        SF_hist = (TH2D*) scalefactor_file->Get("csv_weight_sfs_2018");
        if (SF_hist) { initialized = true; }
        else {
            std::cout << "CSVWeightSFHelper: scale factor histogram not found in file " << scalefactor_file << std::endl;
            throw std::exception();
        }
    }
}

void CSVWeightSFHelper::Reset(TString path_to_sf_file_)
{
    // resets all member data
    scalefactor_file = nullptr;
    path_to_sf_file  = "";
    SF_hist          = nullptr;
    initialized      = false;
    // load new file
    LoadFile(path_to_sf_file_);
}

float CSVWeightSFHelper::GetScaleFactor(int n_jets, float ht_jets) const
{
    // this function gets the scale factor for a event dependent on the number of jets,btags and the lepton flavor
    if (!initialized) {
        std::cout << "CSVWeightSFHelper: not initiliazed" << std::endl;
        throw std::exception();
    }
    int   bin     = -1;
    float sf      = 0.;
    int   N_jets  = n_jets > 6 ? 6 : n_jets;
    float HT_jets = ht_jets >= 2000. ? 1999. : ht_jets;
    bin           = SF_hist->FindBin(N_jets, HT_jets);
    sf            = SF_hist->GetBinContent(bin);
    return sf <= 0. ? 1. : sf;
}

CSVWeightSFHelper::~CSVWeightSFHelper()
{
    // destructor which closes the file if it was loaded in the first place
    if (initialized) scalefactor_file->Close();
}
