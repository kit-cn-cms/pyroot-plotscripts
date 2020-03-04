#include "HistHelper.h"
// Helper for Histofunctions and Definitions

HistHelper::HistHelper(bool skip, std::string variation_, std::string origName_, std::string suffix_)
{
    skipWeightSysts = skip;
    variation = variation_;
    origName = origName_;
    suffix = suffix_;

    //PLACEHOLDERFORINITHISTOS
}

// helper function to fill plots more efficiently
void HistHelper::helperFillHisto(const std::vector<structHelpFillHisto>& paramVec, const double& val)
{
    for (const auto& singleParams : paramVec)
    // singleParams: histo, var, weight
    {
        if ((singleParams.weight) != 0)
            singleParams.histo->Fill(fmin(singleParams.histo->GetXaxis()->GetXmax() - 1e-6, fmax(singleParams.histo->GetXaxis()->GetXmin() + 1e-6, val)), singleParams.weight);
    }
}

// helper function to fill plots more efficiently
void HistHelper::helperFillTwoDimHisto(const std::vector<structHelpFillTwoDimHisto>& paramVec, const double& val1, const double& val2)
{
    for (const auto& singleParams : paramVec)
    // singleParams: histo, var1, var2, weight
    {
        if ((singleParams.weight) != 0)
            singleParams.histo->Fill(fmin(singleParams.histo->GetXaxis()->GetXmax() - 1e-6, fmax(singleParams.histo->GetXaxis()->GetXmin() + 1e-6, val1)), fmin(singleParams.histo->GetYaxis()->GetXmax() - 1e-6, fmax(singleParams.histo->GetYaxis()->GetXmin() + 1e-6, val2)), singleParams.weight);
    }
}

void HistHelper::helperFillSingleHisto1D(TH1* histo, float weight, float val)
{
    if (weight != 0)
        histo->Fill(fmin(histo->GetXaxis()->GetXmax() - 1e-6, fmax(histo->GetXaxis()->GetXmin() + 1e-6, val)), weight);
}

void HistHelper::helperFillSingleHisto2D(TH2* histo, float weight, float val1, float val2)
{
    if (weight != 0)
        histo->Fill(fmin(histo->GetXaxis()->GetXmax() - 1e-6, fmax(histo->GetXaxis()->GetXmin() + 1e-6, val1)), fmin(histo->GetYaxis()->GetXmax() - 1e-6, fmax(histo->GetYaxis()->GetXmin() + 1e-6, val2)), weight);
}

void HistHelper::FillHistos(std::map<std::string, std::tuple<float, float, float>> PlotWeightMap)
{
    // weight_Vars = weight, var1, var2
    for( auto const& [histLabel, weight_vars] : PlotWeightMap ){
        if (std::get<2>(weight_vars) == -999) {
            helperFillSingleHisto1D(histos1D[histLabel].get(),std::get<0>(weight_vars), std::get<1>(weight_vars));
        }
        else {
            helperFillSingleHisto2D(histos2D[histLabel].get(),std::get<0>(weight_vars), std::get<1>(weight_vars), std::get<2>(weight_vars));
        }
    }

}
