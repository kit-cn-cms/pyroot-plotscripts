#if !defined(ONDEDIMHISTOHELPERH)
#define ONDEDIMHISTOHELPERH

#include "TH1.h"
#include "TH1F.h"
#include "TH2F.h"
#include <map>
#include <vector>
#include <string>
#include "BaseHistoHelper.h"

class OneDimHistoHelper : public BaseHistoHelper{
    public:
       
        OneDimHistoHelper();
        OneDimHistoHelper(std::map<std::string, std::shared_ptr<TH1>> input_map);
        OneDimHistoHelper(std::string& input_variation, bool& input_skipWeightSysts, 
                            std::vector<std::string>& input_systematics) ;
        ~OneDimHistoHelper();

        void fillNecessaryHistograms (const std::string& plotname,
                              const float& NomWeight, const float& final_weight,
                              const std::map<std::string, float>& weight_expressions, 
                              const float& variable) const;
        
        void helperFillHisto(const std::vector<structHelpFillHisto>& paramVec, const double& val) const;

        // BaseHistoHelper::push_back(std::string plotname, std::shared_ptr<TH1> histo);
    private:
        
};



#endif // ONDEDIMHISTOHELPERH
