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

        if (verbosity >= 10){
          std::cout << "DEBUG OneDimHistoHelper::fillNecessaryHistograms" << std::endl;
          std::cout << "\tFilling " << plotname+systname << std::endl;
          std::cout << "\tweight_expression: " << weight_expressions.at(systname) << std::endl;
          std::cout << "\tfinal weight: " << final_weight << std::endl;
        }
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
  double xmin = 0;
  double xmax = 0;
  double final_x = 0;
  for (const auto &singleParams: paramVec)
  // singleParams: histo, var, weight
  {
    if((singleParams.weight)!=0){
        xmax = singleParams.histo->GetXaxis()->GetXmax()-1e-6;
        xmin = singleParams.histo->GetXaxis()->GetXmin()+1e-6;
        final_x = fmin(xmax,fmax(xmin,val));
        if (verbosity >= 10){
              std::cout << "DEBUG OneDimHistoHelper::helperFillHisto" << std::endl;
              std::cout << "\tFilling " << singleParams.histo->GetName() << std::endl;
              std::cout << "\txmin: " << xmin << std::endl;
              std::cout << "\txmax: " << xmax << std::endl;
              std::cout << "\tfinal_x: " << final_x << std::endl;
              std::cout << "\tvalue: " << val << std::endl;
              std::cout << "\tweight: " << singleParams.weight << std::endl;
            }
        singleParams.histo->Fill(final_x,singleParams.weight);
    }
    else{
      if (verbosity >= 10){
        std::cout << "DEBUG OneDimHistoHelper::helperFillHisto" << std::endl;
        std::cout << "weight for histogram '" << singleParams.histo->GetName() << "' is 0, skipping" << std::endl;
      }
    }
  }
}
