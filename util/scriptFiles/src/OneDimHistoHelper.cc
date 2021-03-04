#include "../interface/OneDimHistoHelper.h"

OneDimHistoHelper::~OneDimHistoHelper(){}


void OneDimHistoHelper::fillNecessaryHistograms (const std::string& plotname,
                              const float& NomWeight, const float& final_weight,
                              const std::map<std::string, float>& weight_expressions, 
                              const float& variable) const
{
  /*
    Basic idea: first collect all relevant templates for plot category 'plotname'.
    relevant templates are identified by cross referencing the list of all 
    weight expressions 'weight_expressions' with the current list of
    relevant systematics 'systematics'.

    After the templates are collected, they are filled in the 'helperFillHisto' function
  */
  std::vector<structHelpFillHisto> helpWeightVec;
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
  this->helperFillHisto(helpWeightVec, variable);
}

// helper function to fill plots more efficiently
void OneDimHistoHelper::helperFillHisto(const std::vector<structHelpFillHisto>& paramVec, const double& val) const
{
  /*
        Fill templates. First check whether the variable(s) to be filled are not in the under/overflow bin of the template.
        Then fill while considering the weight
    */
  for (const auto &singleParams: paramVec)
  // singleParams: histo, var, weight
  {
    if((singleParams.weight)!=0)
        singleParams.histo->Fill(fmin(singleParams.histo->GetXaxis()->GetXmax()-1e-6,fmax(singleParams.histo->GetXaxis()->GetXmin()+1e-6,val)),singleParams.weight);
  }
}
