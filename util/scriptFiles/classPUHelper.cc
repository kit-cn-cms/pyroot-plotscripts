
class PUHelper {
   public:
    PUHelper();
    ~PUHelper();
    float GetScaleFactor(std::string era, auto x);
    void  Reset();
    void  AddScaleFactorHistogram(std::string era, std::string path_to_file, std::string histogram_name);

   private:
    std::map< std::string, TH1D* > scalefactor_map;
    bool                           initialized = false;
};

PUHelper::PUHelper() {}

void PUHelper::AddScaleFactorHistogram(std::string era, std::string path_to_file, std::string histogram_name)
{
    TFile* scalefactor_file = nullptr;
    TH1D*  scalefactor_hist = nullptr;
    if (path_to_file != "") { scalefactor_file = TFile::Open(path_to_file.c_str(), "READ"); }
    else {
        std::cout << "PUHelper: no scale factor file given" << std::endl;
        throw std::exception();
    }
    if (scalefactor_file) {
        std::cout << "opened file " << path_to_file << std::endl;
        scalefactor_hist = (TH1D*) scalefactor_file->Get(histogram_name.c_str());
        if (scalefactor_hist) {
            std::cout << "loaded histogram " << histogram_name << " from file " << path_to_file << std::endl;
            scalefactor_hist->SetDirectory(0);
            scalefactor_map[era] = scalefactor_hist;
            initialized              = true;
        }
        else {
            std::cout << "PUHelper: scale factor histogram not found in file " << scalefactor_file << std::endl;
            throw std::exception();
        }
        scalefactor_file->Close();
    }
    else {
        std::cout << "PUHelper: scale factor file not read" << std::endl;
        throw std::exception();
    }
}

void PUHelper::Reset()
{
    scalefactor_map.clear();
    initialized = false;
}

float PUHelper::GetScaleFactor(std::string era, auto x)
{
    if (!initialized) {
        std::cout << "PUHelper: not initiliazed" << std::endl;
        throw std::exception();
    }

    if (scalefactor_map.find(era) == scalefactor_map.end()) return 1.;

    // std::cout << era << " " << "hist " << scalefactor_map[era]->GetName() << std::endl;

    // std::cout << "x " << x << std::endl;

    int   bin      = -1;
    float sf       = 1.;

    // std::cout << "xmin " << scalefactor_map[era]->GetXaxis()->GetXmin() << std::endl;
    // std::cout << "xmax " << scalefactor_map[era]->GetXaxis()->GetXmax() << std::endl;

    bool x_in_range = (x > scalefactor_map[era]->GetXaxis()->GetXmin()) && (x < scalefactor_map[era]->GetXaxis()->GetXmax());

    if (x_in_range) {
        bin      = scalefactor_map[era]->FindBin(x);
        sf       = scalefactor_map[era]->GetBinContent(bin);
    }
    // std::cout << "bin " << bin << std::endl;
    // std::cout << "sf " << sf << std::endl;

    if (sf > 0.)
        return sf;
    else
        return 1.;
}

PUHelper::~PUHelper() {}
