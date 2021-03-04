#if !defined(BASEHISTOHELPERH)
#define BASEHISTOHELPERH

#include "TH1.h"
#include "TH1F.h"
#include "TH2F.h"
#include <map>
#include <vector>
#include <string>


class BaseHistoHelper{
    public:
        // Helper struct to fill plots more efficiently
        // Until GCC 4.9 struct cannot have init values if one wants to initialize it with bracket lists
        struct structHelpFillHisto{
            TH1* histo;
            double weight;
        };
        struct structHelpFillTwoDimHisto{
            TH2* histo;
            double weight;
        };

        BaseHistoHelper() {}
        
        virtual ~BaseHistoHelper() {}

        void push_back(std::string plotname, std::shared_ptr<TH1> histo){
            histo_map[plotname] = histo;
            histo_map[plotname]->SetDirectory(0);
        }
        
        std::vector<std::string>& GetSystematics(){return systematics;}
        void SetSystematics( std::vector<std::string>& input) {
            systematics = input;
        }
        std::string& GetCurrentVariation(){return variation;}
        void SetCurrentVariation( std::string& input) {
            variation = input;
        }
        bool& GetSkipWeightSysts(){return skipWeightSysts;}
        void SetSkipWeightSysts( bool& input) {
            skipWeightSysts = input;
        }
        std::map<std::string, std::shared_ptr<TH1>>& GetHistoMap(){return histo_map;}
        void SetHistoMap(std::map<std::string, std::shared_ptr<TH1>>& input) {
            histo_map = input;
            std::cout << "set map with following entries:" << std::endl;
            for(auto entry: histo_map){
                std::cout << "\t" << entry.first << std::endl;
            }
        }
    protected:
        std::vector<std::string> systematics;
        std::map<std::string, std::shared_ptr<TH1>> histo_map;
        std::string variation;
        bool skipWeightSysts;
};



#endif // BASEHISTOHELPERH
