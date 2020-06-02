
class CSVWeightSFHelper {
   public:
    CSVWeightSFHelper();
    ~CSVWeightSFHelper();
    float GetScaleFactor(std::string process, auto x, auto y);
    void  Reset();
    void  AddScaleFactorHistogram(std::string process, std::string path_to_file, std::string histogram_name);

   private:
    std::map< std::string, TH2D* > scalefactor_map;
    bool                           initialized = false;
};

CSVWeightSFHelper::CSVWeightSFHelper() {}

void CSVWeightSFHelper::AddScaleFactorHistogram(std::string process, std::string path_to_file, std::string histogram_name)
{
    TFile* scalefactor_file = nullptr;
    TH2D*  scalefactor_hist = nullptr;
    if (path_to_file != "") { scalefactor_file = TFile::Open(path_to_file.c_str(), "READ"); }
    else {
        std::cout << "CSVWeightSFHelper: no scale factor file given" << std::endl;
        throw std::exception();
    }
    if (scalefactor_file) {
        scalefactor_hist = (TH2D*) scalefactor_file->Get(histogram_name.c_str());
        if (scalefactor_hist) {
            scalefactor_hist->SetDirectory(0);
            scalefactor_map[process] = scalefactor_hist;
            initialized              = true;
        }
        else {
            std::cout << "CSVWeightSFHelper: scale factor histogram not found in file " << scalefactor_file << std::endl;
            throw std::exception();
        }
        scalefactor_file->Close();
    }
    else {
        std::cout << "CSVWeightSFHelper: scale factor file not read" << std::endl;
        throw std::exception();
    }
}

void CSVWeightSFHelper::Reset()
{
    scalefactor_map.clear();
    initialized = false;
}

float CSVWeightSFHelper::GetScaleFactor(std::string process, auto x, auto y)
{
    if (!initialized) {
        std::cout << "CSVWeightSFHelper: not initiliazed" << std::endl;
        throw std::exception();
    }

    if (scalefactor_map.find(process) == scalefactor_map.end()) return 1.;

    // std::cout << "hist " << scalefactor_map[process] << std::endl;

    // std::cout << "x " << x << std::endl;
    // std::cout << "y " << y << std::endl;

    int   bin      = -1;
    float sf       = 1.;
    float sf_error = 0.;

    // std::cout << "xmin " << scalefactor_map[process]->GetXaxis()->GetXmin() << std::endl;
    // std::cout << "xmax " << scalefactor_map[process]->GetXaxis()->GetXmax() << std::endl;

    // std::cout << "ymin " << scalefactor_map[process]->GetYaxis()->GetXmin() << std::endl;
    // std::cout << "ymax " << scalefactor_map[process]->GetYaxis()->GetXmax() << std::endl;

    bool x_in_range = (x > scalefactor_map[process]->GetXaxis()->GetXmin()) && (x < scalefactor_map[process]->GetXaxis()->GetXmax());
    bool y_in_range = (y > scalefactor_map[process]->GetYaxis()->GetXmin()) && (y < scalefactor_map[process]->GetYaxis()->GetXmax());

    if (x_in_range && y_in_range) {
        bin      = scalefactor_map[process]->FindBin(x, y);
        sf       = scalefactor_map[process]->GetBinContent(bin);
        sf_error = scalefactor_map[process]->GetBinError(bin);
    }

    // std::cout << "sf " << sf << std::endl;
    // std::cout << "sf err " << sf_error << std::endl;

    if (sf > 0.)
        return sf;
    else
        return 1.;
}

CSVWeightSFHelper::~CSVWeightSFHelper() {}
