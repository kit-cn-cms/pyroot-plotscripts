#include "../interface/OneDimHistoHelper.h"

OneDimHistoHelper::OneDimHistoHelper(){
    std::cout << "initialized empty OneDimHistoHelper!" << std::endl;
}

OneDimHistoHelper::OneDimHistoHelper(std::map<std::string, std::shared_ptr<TH1>> input_map)
{
  histo_map = input_map;
}
OneDimHistoHelper::OneDimHistoHelper(std::string& input_variation, bool& input_skipWeightSysts, 
                    std::vector<std::string>& input_systematics)
{
  variation = input_variation;
  skipWeightSysts = input_skipWeightSysts;
  systematics = input_systematics;    
}
OneDimHistoHelper::~OneDimHistoHelper(){}


void OneDimHistoHelper::fillNecessaryHistograms (const std::string& plotname,
                              const float& NomWeight, const float& final_weight,
                              const std::map<std::string, float>& weight_expressions, 
                              const float& variable) const
{
  std::vector<structHelpFillHisto> helpWeightVec;
  std::cout << "current map: " << std::endl;
  for(auto entry: histo_map){
        std::cout << "\t" << entry.first << std::endl;
    }
  std::cout << "OneDimHistoHelper::fillNecessaryHistograms: fill '" << plotname+variation <<"'" << std::endl;
  helpWeightVec.push_back({histo_map.at(plotname+variation).get(), ((NomWeight)*(final_weight))});
  if (!skipWeightSysts) { // append plots for weight systs if neccessary
    for(auto& systname : systematics){
      if (weight_expressions.find(systname) != weight_expressions.end()){
          std::cout << "OneDimHistoHelper::fillNecessaryHistograms: fill '" << plotname+systname <<"'" << std::endl;
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
  for (const auto &singleParams: paramVec)
  // singleParams: histo, var, weight
  {
    if((singleParams.weight)!=0)
        singleParams.histo->Fill(fmin(singleParams.histo->GetXaxis()->GetXmax()-1e-6,fmax(singleParams.histo->GetXaxis()->GetXmin()+1e-6,val)),singleParams.weight);
  }
}

// void OneDimHistoHelper::push_back(std::string plotname, std::shared_ptr<TH1> histo){
//     histo_map[plotname] = histo;
//     histo_map[plotname]->SetDirectory(0);
// }