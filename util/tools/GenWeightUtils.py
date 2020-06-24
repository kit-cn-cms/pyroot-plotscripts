import pandas


class GenWeightNormalization():
    # -- init functions ---------------------------------------------
    def __init__(self, csvfile):
        self.csvfile = csvfile
        self.csv_dict = self.readCSVFile()
        self.weightList = self.getWeightVarsList()
        self.namespace_name = "GenNormMap"
        # print(self.weightList)
        # exit("DEBUG EXIT")

    
    # GetGenWeightAddVariablesList
    def getWeightVarsList(self):
        # get list of weight variables
        seen = set()
        weight_vars_list = []
        for key in self.csv_dict:
            if not key[1] in seen:
                seen.add(key[1])
                weight_vars_list.append(key[1])
        return weight_vars_list



    # ReadGenWeightNormalizations
    def readCSVFile(self):
        # read csv file as dictionary
        csv_dict = {}
        data = pandas.read_csv(self.csvfile)
        data["sample_name_modified"] = pandas.Series(
            (x.replace("_","").replace("-","").replace("newpmx","") for x in data.name.values),
            index = data.index)
        for index in range(len(data.weight.values)):
            csv_dict[ (data.sample_name_modified[index], data.weight[index]) ] = data.final_weight[index]

        return csv_dict
    # ---------------------------------------------------------------


    
    # GetGenWeightNormVetoList
    def getVetolist(self):
        # get vetolist for CC program
        # weightVetoList = []
        # for weight in self.weightList:
        #     weightVetoList.append("internalNormFactor_"+weight)
        # return weightVetoList
        return ["internalNormFactors"]


    # DeclareGenWeightNormFactors
    def declareNormFactors(self):
        code = "\tstd::map< TString, float> internalNormFactors = \n  {\n"
        tmp = []
        for weight in sorted(self.weightList):
            tmp.append('\t{{ "{}", 1.0 }}'.format(weight))
        code += ",\n".join(tmp)
        code += "\n  };"
        return code

    def loadNormFactors(self):
        return "auto internalNormFactors = {}::internalNormFactors;\n".format(self.namespace_name)

    # AddGenWeightNormMap
    def addNormalizationMap(self):
        code = "\tstd::map<TString,float> GenWeight_Norm_Map = \n  {\n"
        tmp = []
        for key in sorted(self.csv_dict):
            tmp.append('\t{{ "{}_{}", {} }}'.format( key[0], key[1], 
                                                            self.csv_dict[key])
                        )
        code += ",\n".join(tmp)
        code += "\n  };"
        return code

    def declareFillFunction(self):
        """
        writes declaration for function which resets all values of input map
        to input value 
        """

        code = """
    void fillInternalNormFactors(std::map<TString, float>& input, const TString& currentSample, int& counter){
        TString keyword;
        for(auto& entry : input){
            keyword = TString::Format("%s_%s", currentSample.Data(), entry.first.Data());
            //std::cout << "loading " << keyword << std::endl;
            if( GenWeight_Norm_Map.find(keyword)!=GenWeight_Norm_Map.end()){
                //std::cout << "returning entry '" << GenWeight_Norm_Map[keyword];
                //std::cout << "' for keyword '" << keyword.Data() << "'" << std::endl;
                input.at(entry.first) = GenWeight_Norm_Map.at(keyword);
            }
            else if(counter<100) {
                std::cout << "WARNING: Could not find entry '"<< keyword.Data();
                std::cout << "' in GenWeight_Norm_Map!" << std::endl; 
                counter+=1;
            }
        }
        //exit(0);
    }
"""
        return code
    def declareNormalizationMapHeader(self):
        """
        function to declare namespace 'GenNormMap', which includes 
        -   std::map<TString, float> GenWeight_Norm_Map
            with all gen weight normalizations
        -   std::map<TString, float> internalNormFactors
            with gen weight normalizations for given sample
        -   function to fill internalNormFactors 
        """
        code = """
#ifndef {allcaps}
#include <map>
#include "TString.h"
namespace {namespace_name}{{
{init_normMap}

{init_normFactors}

{fill_function}
}}
#endif""".format( allcaps = self.namespace_name.upper(),
                namespace_name    = self.namespace_name,
              init_normMap      = self.addNormalizationMap(),
              init_normFactors  = self.declareNormFactors(),
              fill_function     = self.declareFillFunction())
        
        return code
    


    # ResetGenWeightNormFactors
    def resetNormalizationFactors(self):
        code = ""
        for weight in self.weightList:
            code += "internalNormFactor_"+weight+"= 0.0;\n"
        return code

    # RelateGenWeightMapToNormFactor
    def relateMapToNormalizationFactor(self):
        """
        load internal norm factors for the current sample.
        This uses the functions in namespace 'GenNormMap' and the
        'resetMap' function in plotHead.CC
        """
        code = """
        TString currentRelevantSampleNameForGenWeights = sampleDataBaseIdentifiers[currentfilename];
        resetMap(internalNormFactors, 1.0);
        GenNormMap::fillInternalNormFactors(internalNormFactors, currentRelevantSampleNameForGenWeights, warningCounter);
        """
        return code

