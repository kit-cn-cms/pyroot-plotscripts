#ifndef HISTHELPER
#define HISTHELPER

#include <iostream>
#include <vector>
#include "TH1F.h"
#include "TH2F.h"
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <algorithm>
#include <map>
#include "TStopwatch.h"
#include <TString.h>
#include <TH2D.h>

// Helper for Histofunctions and Definitions
class HistHelper {

public:
    HistHelper(bool skip, std::string variation_, std::string origName_, std::string suffix);
    ~HistHelper();

    // structs to store information 1D histograms
    struct Plot1DInfoStruct {
        std::string identifier;
        std::string title;
        int nbins;
        std::vector<float> edges;
        //std::unique_ptr<TH1> histoptr;
    };

    // structs to store information 1D histograms
    struct Plot2DInfoStruct {
        std::string identifier;
        std::string title;
        int nbinsx;
        std::vector<float> edges_x;
        int nbinsy;
        std::vector<float> edges_y;
        //std::unique_ptr<TH2> histoptr;
    };

    // Helper struct to fill plots more efficiently
    // Until GCC 4.9 struct cannot have init values if one wants to initialize it with bracket lists
    struct structHelpFillHisto {
        TH1* histo;
        double weight;
    };

    struct structHelpFillTwoDimHisto {
        TH2* histo;
        double weight;
    };

    void helperFillHisto(const std::vector<structHelpFillHisto>& paramVec, const double& val);
    void helperFillTwoDimHisto(const std::vector<structHelpFillTwoDimHisto>& paramVec, const double& val1, const double& val2);
    void FillHistos(std::map<std::string, std::tuple<float, float, float>> PlotWeightMap);
    void helperFillSingleHisto1D(TH1* histo, float weight, float val);
    void helperFillSingleHisto2D(TH2* histo, float weight, float val1, float val2);

    double variable = -999;
    double variable1 = -999;
    double variable2 = -999;

    std::vector<std::string> systematics;
    std::map<std::string, Plot1DInfoStruct> plotinfo1D;
    std::map<std::string, Plot2DInfoStruct> plotinfo2D;
    std::map<std::string, std::unique_ptr<TH1>> histos1D;
    std::map<std::string, std::unique_ptr<TH2>> histos2D;
    TString histname;
    bool skipWeightSysts = false;
    std::string variation;
    std::string origName;
    std::string suffix;
    

private:
};

#endif // HISTHELPER