#if !defined(TWODIMHISTOHELPERH)
#define TWODIMHISTOHELPERH

#include "TH1.h"
#include "TH1F.h"
#include "TH2F.h"
#include <map>
#include <vector>
#include <string>
#include "BaseHistoHelper.h"

class TwoDimHistoHelper : public BaseHistoHelper<TH2>{
    public:
    //    TwoDimHistoHelper() {}
        ~TwoDimHistoHelper();

        void fillNecessaryHistograms (const std::string& plotname,
                              const float& NomWeight, const float& final_weight,
                              const std::map<std::string, float>& weight_expressions, 
                              const float& variable1, const float& variable2) const;
        
        void helperFillHisto(const std::vector<structHelpFillTwoDimHisto>& paramVec, 
                                const double& val1, const double& val2) const;

    private:
        
};



#endif // TWODIMHISTOHELPERH
