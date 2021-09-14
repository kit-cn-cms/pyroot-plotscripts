
class SFHelper {
   public:
    SFHelper();
    ~SFHelper();
    float GetScaleFactor(std::string identifier, auto x, bool use_edge_bins);
    std::vector<float> GetScaleFactorPlusUnc(std::string identifier, auto x, bool use_edge_bins);
    void  Reset();
    void  AddScaleFactorHistogram(std::string identifier, std::string path_to_file, std::string histogram_name);
    float GetHistogramLowerEdge(std::string identifier);
    
    void  AddScaleFactorHistogram2D(std::string identifier, std::string path_to_file, std::string histogram_name);
    std::vector<float> GetScaleFactorPlusUnc2D(std::string identifier, auto x, auto y, bool use_edge_bins);

   private:
    std::map< std::string, TH1D* > scalefactor_map;
    std::map< std::string, TH2D* > scalefactor_map_2D;
    bool                           initialized = false;
};

SFHelper::SFHelper() {}

void SFHelper::AddScaleFactorHistogram(std::string identifier, std::string path_to_file, std::string histogram_name)
{
    TFile* scalefactor_file = nullptr;
    TH1D*  scalefactor_hist = nullptr;
    if (path_to_file != "") { scalefactor_file = TFile::Open(path_to_file.c_str(), "READ"); }
    else {
        std::cout << "SFHelper: no scale factor file given" << std::endl;
        throw std::exception();
    }
    if (scalefactor_file) {
        std::cout << "opened file " << path_to_file << std::endl;
        scalefactor_hist = (TH1D*) scalefactor_file->Get(histogram_name.c_str());
        if (scalefactor_hist) {
            std::cout << "loaded histogram " << histogram_name << " from file " << path_to_file << std::endl;
            scalefactor_hist->SetDirectory(0);
            scalefactor_map[identifier] = scalefactor_hist;
            initialized              = true;
        }
        else {
            std::cout << "SFHelper: scale factor histogram not found in file " << scalefactor_file << std::endl;
            throw std::exception();
        }
        scalefactor_file->Close();
    }
    else {
        std::cout << "SFHelper: scale factor file not read" << std::endl;
        throw std::exception();
    }
}

void SFHelper::Reset()
{
    scalefactor_map.clear();
    initialized = false;
}

float SFHelper::GetScaleFactor(std::string identifier, auto x, bool use_edge_bins)
{
    if (!initialized) {
        std::cout << "SFHelper: not initiliazed" << std::endl;
        throw std::exception();
    }

    if (scalefactor_map.find(identifier) == scalefactor_map.end()) return 1.;

    // std::cout << identifier << " " << "hist " << scalefactor_map[identifier]->GetName() << std::endl;

    // std::cout << "x " << x << std::endl;

    int   bin      = -1;
    float sf       = 1.;

    // std::cout << "xmin " << scalefactor_map[identifier]->GetXaxis()->GetXmin() << std::endl;
    // std::cout << "xmax " << scalefactor_map[identifier]->GetXaxis()->GetXmax() << std::endl;
    
    if (use_edge_bins) {
        x = std::max(float(x),float(scalefactor_map[identifier]->GetXaxis()->GetXmin()+0.001));
        x = std::min(float(x),float(scalefactor_map[identifier]->GetXaxis()->GetXmax()-0.001));
    }

    bool x_in_range = (x > scalefactor_map[identifier]->GetXaxis()->GetXmin()) && (x < scalefactor_map[identifier]->GetXaxis()->GetXmax());

    if (x_in_range) {
        bin      = scalefactor_map[identifier]->FindBin(x);
        sf       = scalefactor_map[identifier]->GetBinContent(bin);
    }
    // std::cout << "bin " << bin << std::endl;
    // std::cout << "sf " << sf << std::endl;

    if (sf != 0.)
        return sf;
    else
        return 1.;
}

std::vector<float> SFHelper::GetScaleFactorPlusUnc(std::string identifier, auto x, bool use_edge_bins)
{
    if (!initialized) {
        std::cout << "SFHelper: not initiliazed" << std::endl;
        throw std::exception();
    }

    std::vector<float> sfs{1.0,1.0,1.0};
    if (scalefactor_map.find(identifier) == scalefactor_map.end()) return sfs;

    // std::cout << identifier << " " << "hist " << scalefactor_map[identifier]->GetName() << std::endl;

    // std::cout << "x " << x << std::endl;

    int   bin      = -1;

    // std::cout << "xmin " << scalefactor_map[identifier]->GetXaxis()->GetXmin() << std::endl;
    // std::cout << "xmax " << scalefactor_map[identifier]->GetXaxis()->GetXmax() << std::endl;
    
    if (use_edge_bins) {
        x = std::max(float(x),float(scalefactor_map[identifier]->GetXaxis()->GetXmin()+0.001));
        x = std::min(float(x),float(scalefactor_map[identifier]->GetXaxis()->GetXmax()-0.001));
    }

    bool x_in_range = (x > scalefactor_map[identifier]->GetXaxis()->GetXmin()) && (x < scalefactor_map[identifier]->GetXaxis()->GetXmax());

    if (x_in_range) {
        bin      = scalefactor_map[identifier]->FindBin(x);
        sfs[0]   = scalefactor_map[identifier]->GetBinContent(bin);
        sfs[1]   = sfs[0] + scalefactor_map[identifier]->GetBinError(bin);
        sfs[2]   = sfs[0] - scalefactor_map[identifier]->GetBinError(bin);
    }
    // std::cout << "bin " << bin << std::endl;
    // std::cout << "sf " << sf << std::endl;

    if (sfs[0] > 0. && sfs[1] > 0. && sfs[2] > 0.)
        return sfs;
    else
        return std::vector<float>{1.0,1.0,1.0};
}

float SFHelper::GetHistogramLowerEdge(std::string identifier)
{
   if (!initialized) {
        std::cout << "SFHelper: not initiliazed" << std::endl;
        throw std::exception();
    }
    
    if (scalefactor_map.find(identifier) == scalefactor_map.end()) return 999999.;
    
    float lower_edge = scalefactor_map[identifier]->GetXaxis()->GetXmin();
    
    return lower_edge;
}

void SFHelper::AddScaleFactorHistogram2D(std::string identifier, std::string path_to_file, std::string histogram_name)
{
    TFile* scalefactor_file = nullptr;
    TH2D*  scalefactor_hist = nullptr;
    if (path_to_file != "") { scalefactor_file = TFile::Open(path_to_file.c_str(), "READ"); }
    else {
        std::cout << "SFHelper: no scale factor file given" << std::endl;
        throw std::exception();
    }
    if (scalefactor_file) {
        std::cout << "opened file " << path_to_file << std::endl;
        scalefactor_hist = (TH2D*) scalefactor_file->Get(histogram_name.c_str());
        if (scalefactor_hist) {
            std::cout << "loaded histogram " << histogram_name << " from file " << path_to_file << std::endl;
            scalefactor_hist->SetDirectory(0);
            scalefactor_map_2D[identifier] = scalefactor_hist;
            initialized              = true;
        }
        else {
            std::cout << "SFHelper: scale factor histogram not found in file " << scalefactor_file << std::endl;
            throw std::exception();
        }
        scalefactor_file->Close();
    }
    else {
        std::cout << "SFHelper: scale factor file not read" << std::endl;
        throw std::exception();
    }
}

std::vector<float> SFHelper::GetScaleFactorPlusUnc2D(std::string identifier, auto x, auto y, bool use_edge_bins)
{
    if (!initialized) {
        std::cout << "SFHelper: not initiliazed" << std::endl;
        throw std::exception();
    }

    std::vector<float> sfs{1.0,1.0,1.0};
    if (scalefactor_map_2D.find(identifier) == scalefactor_map_2D.end()) return sfs;

    // std::cout << identifier << " " << "hist " << scalefactor_map[identifier]->GetName() << std::endl;

    // std::cout << "x " << x << std::endl;

    int   bin      = -1;

    // std::cout << "xmin " << scalefactor_map[identifier]->GetXaxis()->GetXmin() << std::endl;
    // std::cout << "xmax " << scalefactor_map[identifier]->GetXaxis()->GetXmax() << std::endl;
    
    if (use_edge_bins) {
        x = std::max(float(x),float(scalefactor_map_2D[identifier]->GetXaxis()->GetXmin()+0.001));
        x = std::min(float(x),float(scalefactor_map_2D[identifier]->GetXaxis()->GetXmax()-0.001));
        y = std::max(float(y),float(scalefactor_map_2D[identifier]->GetYaxis()->GetXmin()+0.001));
        y = std::min(float(y),float(scalefactor_map_2D[identifier]->GetYaxis()->GetXmax()-0.001));
    }

    bool x_in_range = (x > scalefactor_map_2D[identifier]->GetXaxis()->GetXmin()) && (x < scalefactor_map_2D[identifier]->GetXaxis()->GetXmax());
    bool y_in_range = (y > scalefactor_map_2D[identifier]->GetYaxis()->GetXmin()) && (y < scalefactor_map_2D[identifier]->GetYaxis()->GetXmax());

    if (x_in_range and y_in_range) {
        bin      = scalefactor_map_2D[identifier]->FindBin(x,y);
        sfs[0]   = scalefactor_map_2D[identifier]->GetBinContent(bin);
        sfs[1]   = sfs[0] + scalefactor_map_2D[identifier]->GetBinError(bin);
        sfs[2]   = sfs[0] - scalefactor_map_2D[identifier]->GetBinError(bin);
    }
    // std::cout << "bin " << bin << std::endl;
    // std::cout << "sf " << sf << std::endl;

    if (sfs[0] > 0. && sfs[1] > 0. && sfs[2] > 0.)
        return sfs;
    else
        return std::vector<float>{1.0,1.0,1.0};
}

SFHelper::~SFHelper() {}
