import pandas


class GenWeightNormalization():
    # -- init functions ---------------------------------------------
    def __init__(self, csvfile, loadSTXSnorms):
        self.csvfile = csvfile
        self.csv_dict = self.readCSVFile("final_weight_sl_analysis")
        self.fractions = {}
        self.fractions["ttbb"] = self.readCSVFile("ratio_ttB_varied_vs_nom_5FS")
        self.fractions["ttcc"] = self.readCSVFile("ratio_ttC_varied_vs_nom_5FS")
        self.fractions["ttlf"] = self.readCSVFile("ratio_ttLF_varied_vs_nom_5FS")
        if loadSTXSnorms:
            self.fractions["TTH_PTH_0_60"] = self.readCSVFile("fiducial_xs_norm_TTH_PTH_0_60")
            self.fractions["TTH_PTH_60_120"] = self.readCSVFile("fiducial_xs_norm_TTH_PTH_60_120")
            self.fractions["TTH_PTH_120_200"] = self.readCSVFile("fiducial_xs_norm_TTH_PTH_120_200")
            self.fractions["TTH_PTH_200_300"] = self.readCSVFile("fiducial_xs_norm_TTH_PTH_200_300")
            self.fractions["TTH_PTH_300_450"] = self.readCSVFile("fiducial_xs_norm_TTH_PTH_300_450")
            self.fractions["TTH_PTH_GT450"] = self.readCSVFile("fiducial_xs_norm_TTH_PTH_GT450")
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
    def readCSVFile(self, keyword):
        # read csv file as dictionary
        csv_dict = {}
        data = pandas.read_csv(self.csvfile)
        data["sample_name_modified"] = pandas.Series(
            (x.replace("_","").replace("-","").replace("newpmx","") for x in data["sample"].values),
            index = data.index)
        for index in range(len(data.variation.values)):
            csv_dict[ (data.sample_name_modified[index], data.variation[index]) ] = data[keyword][index]

        return csv_dict
    # ---------------------------------------------------------------


    
    # GetGenWeightNormVetoList
    def getVetolist(self):
        # get vetolist for CC program
        # weightVetoList = []
        # for weight in self.weightList:
        #     weightVetoList.append("internalNormFactor_"+weight)
        # return weightVetoList
        vetolist = ["internalNormFactors"]
        vetolist += ["fracRatio_{}".format(x) for x in self.fractions.keys()]
        vetolist.append("isFourFSsample")
        return vetolist


    def initMap(self, map_name, default = 1.0):
        code = "\tstd::map< TString, float> {} = \n  {{\n".format(map_name)
        tmp = []
        for weight in sorted(self.weightList):
            tmp.append('\t{{ "{name}", {default} }}'.format(name = weight, default = default))
        code += ",\n".join(tmp)
        code += "\n  };\n"
        return code
    # DeclareGenWeightNormFactors
    def declareNormFactors(self):
        code = self.initMap("internalNormFactors")
        for k in self.fractions:
            code += self.initMap("fracRatio_{}".format(k))
        return code

    def loadNormFactors(self):
        code = "auto internalNormFactors = {}::internalNormFactors;\n".format(self.namespace_name)
        for k in self.fractions:
            code += "auto fracRatio_{key} = {name}::fracRatio_{key};\n".format(name = self.namespace_name, key = k)
        return code

    def generateDictLines(self, dic, indent = "\t", debug = False):
        tmp = []
        code = ""
        for key in sorted(dic):
            if dic[key] == -1: continue
            tmp.append('{}{{ "{}_{}", {} }}'.format( indent, key[0], key[1], dic[key]) )
            if debug: break
        code += ",\n".join(tmp)
        return code

    # AddGenWeightNormMap
    def addNormalizationMap(self):
        code = "\tstd::map<TString,float> GenWeight_Norm_Map = \n  {\n"
        code += self.generateDictLines(self.csv_dict)
        code += "\n  };"
        for k in self.fractions:
            code += "\tstd::map<TString,float> private_fracRatio_{} = \n  {{\n".format(k)
            code += self.generateDictLines(self.fractions[k])
            code += "\n  };"
        return code

    

    def declareFillFunction(self):
        """
        writes declaration for function which resets all values of input map
        to input value 
        """
        code = """void fillInternalNormFactors(std::map<TString, float>& input, const TString& currentSample, 
                                int& counter, std::map<TString, float>& source = {}::GenWeight_Norm_Map)""".format(self.namespace_name)
        code += """
    {
        TString keyword;
        for(auto& entry : input){
            keyword = TString::Format("%s_%s", currentSample.Data(), entry.first.Data());
            //std::cout << "loading " << keyword << std::endl;
            if( source.find(keyword)!=source.end()){
                //std::cout << "returning entry '" << source[keyword];
                //std::cout << "' for keyword '" << keyword.Data() << "'" << std::endl;
                input.at(entry.first) = source.at(keyword);
            }
            else if(counter<100) {
                std::cout << "WARNING: Could not find entry '"<< keyword.Data();
                std::cout << "' in source!" << std::endl; 
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
        isFourFSsample = 0.;
        if (currentRelevantSampleNameForGenWeights.BeginsWith("TTbb")){{
            isFourFSsample = 1.;
        }}
        resetMap(internalNormFactors, 1.0);
        {}::fillInternalNormFactors(internalNormFactors, currentRelevantSampleNameForGenWeights, warningCounter);
        """.format(self.namespace_name)
        for k in self.fractions:
            code += """
        resetMap(fracRatio_{key}, 1.0);
        {namespace}::fillInternalNormFactors(fracRatio_{key}, currentRelevantSampleNameForGenWeights, warningCounter, {namespace}::private_fracRatio_{key});
        """.format(namespace = self.namespace_name, key = k)
        return code

