#include "../interface/TwoDimHistoHelper.h"

TwoDimHistoHelper::~TwoDimHistoHelper(){}

void TwoDimHistoHelper::fillNecessaryHistograms (const std::string& plotname,
                              const float& NomWeight, const float& final_weight,
                              const std::map<std::string, float>& weight_expressions, 
                              const float& variable1, const float& variable2) const
{
    /*
    Basic idea: first collect all relevant templates for plot category 'plotname'.
    relevant templates are identified by cross referencing the list of all 
    weight expressions 'weight_expressions' with the current list of
    relevant systematics 'systematics'.

    After the templates are collected, they are filled in the 'helperFillHisto' function
  */
  std::vector<structHelpFillTwoDimHisto> helpWeightVec;
  // the nominal template is always relevant, so add it to the list
  helpWeightVec.push_back({histo_map.at(plotname+variation).get(), ((NomWeight)*(final_weight))});
  if (!skipWeightSysts) { // append plots for weight systs if neccessary
    for(auto& systname : systematics){
      if (weight_expressions.find(systname) != weight_expressions.end()){
        helpWeightVec.push_back( { histo_map.at(plotname+systname).get(), 
                                    (weight_expressions.at(systname))*(final_weight) 
                                } );
      }
    } 
  }
  this->helperFillHisto(helpWeightVec, variable1, variable2);
}

// helper function to fill plots more efficiently
void TwoDimHistoHelper::helperFillHisto(const std::vector<structHelpFillTwoDimHisto>& paramVec, const double& val1, const double& val2) const
{
    /*
        Fill templates. First check whether the variable(s) to be filled are not in the under/overflow bin of the template.
        Then fill while considering the weight
    */
  for (const auto &singleParams: paramVec)
  // singleParams: histo, var1, var2, weight
  {
    if((singleParams.weight)!=0)
        singleParams.histo->Fill(fmin(singleParams.histo->GetXaxis()->GetXmax()-1e-6,fmax(singleParams.histo->GetXaxis()->GetXmin()+1e-6,val1)),
                                fmin(singleParams.histo->GetYaxis()->GetXmax()-1e-6,fmax(singleParams.histo->GetYaxis()->GetXmin()+1e-6,val2))
                                ,singleParams.weight);
  }
}
