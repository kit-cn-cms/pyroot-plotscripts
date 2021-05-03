#if !defined(BASEHISTOHELPERH)
#define BASEHISTOHELPERH

#include "TH1.h"
#include "TH1F.h"
#include "TH2F.h"
#include <map>
#include <vector>
#include <string>


template<class T> class BaseHistoHelper{
    public:
        // Helper struct to fill plots more efficiently
        // Until GCC 4.9 struct cannot have init values if one wants to initialize it with bracket lists
        struct structHelpFillHisto{
            T* histo;
            double weight;
        };
        struct structHelpFillTwoDimHisto{
            TH2* histo;
            double weight;
        };

        BaseHistoHelper(){
            std::cout << "initialized empty BaseHistoHelper!" << std::endl;
        }

        BaseHistoHelper(std::map<std::string, std::shared_ptr<T>> input_map):
        histo_map(input_map) {}

        BaseHistoHelper(std::string& input_variation, bool& input_skipWeightSysts, 
                            std::vector<std::string>& input_systematics):
            variation(input_variation), skipWeightSysts(input_skipWeightSysts),
            systematics(input_systematics)
        {  
        }
        
        virtual ~BaseHistoHelper() {}

        void push_back(std::string plotname, std::shared_ptr<T> histo){
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
        std::map<std::string, std::shared_ptr<T>>& GetHistoMap(){return histo_map;}
        void SetHistoMap(std::map<std::string, std::shared_ptr<T>>& input) {
            histo_map = input;
            std::cout << "set map with following entries:" << std::endl;
            for(auto entry: histo_map){
                std::cout << "\t" << entry.first << std::endl;
            }
        }
        void SetVerbosity(int input_verbosity){verbosity = input_verbosity;}
        int GetVerbosity(){return verbosity;}
    protected:
        std::vector<std::string> systematics;
        std::map<std::string, std::shared_ptr<T>> histo_map;
        std::string variation;
        bool skipWeightSysts;
        int verbosity = 0;
};



#endif // BASEHISTOHELPERH
