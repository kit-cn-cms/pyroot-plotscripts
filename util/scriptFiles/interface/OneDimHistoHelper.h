#if !defined(ONEDIMHISTOHELPERH)
#define ONEDIMHISTOHELPERH

#include "TH1.h"
#include "TH1F.h"
#include "TH2F.h"
#include <map>
#include <vector>
#include <string>
#include "BaseHistoHelper.h"

class OneDimHistoHelper : public BaseHistoHelper<TH1>{
    public:
       
        ~OneDimHistoHelper();

        void fillNecessaryHistograms (const std::string& plotname,
                              const float& NomWeight, const float& final_weight,
                              const std::map<std::string, float>& weight_expressions, 
                              const float& variable) const;
        
        void helperFillHisto(const std::vector<structHelpFillHisto>& paramVec, const double& val) const;

    private:
        
};



#endif // ONEDIMHISTOHELPERH
