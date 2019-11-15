import pandas


class GenWeightNormalization():
    # -- init functions ---------------------------------------------
    def __init__(self, csvfile):
        self.csvfile = csvfile
        self.csv_dict = self.readCSVFile()
        self.weightList = self.getWeightVarsList()

    
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
            (x.split("/")[1].replace("_","").replace("-","") for x in data.name.values),
            index = data.index)
        for index in range(len(data.weight.values)):
            csv_dict[ (data.sample_name_modified[index], data.weight[index]) ] = data.factor[index]

        return csv_dict
    # ---------------------------------------------------------------


    
    # GetGenWeightNormVetoList
    def getVetolist(self):
        # get vetolist for CC program
        weightVetoList = []
        for weight in self.weightList:
            weightVetoList.append("internalNormFactor_"+weight)
        return weightVetoList


    # DeclareGenWeightNormFactors
    def declareNormFactors(self):
        code = ""
        for weight in self.weightList:
            code += "float internalNormFactor_"+weight+"= 1.0;\n"
        return code

    # AddGenWeightNormMap
    def addNormalizationMap(self):
        code = "std::map<TString,float> GenWeight_Norm_Map;\n"
        for key in self.csv_dict:
            code += 'GenWeight_Norm_Map["{}_{}"]={};\n'.format(str(key[0]),str(key[1]), str(self.csv_dict[key]))
        return code
    


    # ResetGenWeightNormFactors
    def resetNormalizationFactors(self):
        code = ""
        for weight in self.weightList:
            code += "internalNormFactor_"+weight+"= 0.0;\n"
        return code

    # RelateGenWeightMapToNormFactor
    def relateMapToNormalizationFactor(self):
        code = ""
        code += """
        TString currentRelevantSampleNameForGenWeights = sampleDataBaseIdentifiers[currentfilename];
        """
        for weight in self.weightList:
            
            code += """
    internalNormFactor_{weightName} = 1.0;
    if( GenWeight_Norm_Map.find({sampleNameVar}+"_{weightName}")!=GenWeight_Norm_Map.end()){{
        internalNormFactor_{weightName} = GenWeight_Norm_Map[{sampleNameVar}+"_{weightName}"];
    }}
    else if(warningCounter<100) std::cout << "WARNING: Could not find entry ' "<< {sampleNameVar} << "_{weightName}' in GenWeight_Norm_Map!" << std::endl; 
    warningCounter+=1;
            """.format(weightName = weight, sampleNameVar = "currentRelevantSampleNameForGenWeights")
        # uncomment the following lines for additional debug output about the weights down below
    #     code += """
    #     std::cout << "==================================================================================" << std::endl;
    # std::cout << "Filling 'dummyWeight_CMS_ttH_scaleMuR_ttbbNLO_Down' with" << std::endl;
    # std::cout << "internalNormFactor_weight_LHA_306000_nominal: " << internalNormFactor_weight_LHA_306000_nominal << std::endl;
    # std::cout << "internalNormFactor_weight_scale_variation_muR_1p0_muF_1p0: " << internalNormFactor_weight_scale_variation_muR_1p0_muF_1p0 << std::endl;
    # std::cout << "'internalNormFactor_weight_scale_variation_muR_2p0_muF_1p0: '" << internalNormFactor_weight_scale_variation_muR_2p0_muF_1p0 << std::endl;
    # std::cout << "'internalNormFactor_weight_scale_variation_muR_0p5_muF_1p0: '" << internalNormFactor_weight_scale_variation_muR_0p5_muF_1p0 << std::endl;    
    
    # std::cout << "'internalNormFactor_weight_scale_variation_muR_2p0_muF_1p0: '" << internalNormFactor_weight_scale_variation_muR_2p0_muF_1p0 << std::endl;
    # std::cout << "'internalNormFactor_weight_LHA_306000_down: '" << internalNormFactor_weight_LHA_306000_down << std::endl;
    # std::cout << "'internalNormFactor_weight_LHA_306000_up: '" << internalNormFactor_weight_LHA_306000_up << std::endl;
    # std::cout << "'internalNormFactor_weight_scale_variation_muR_1p0_muF_2p0: '" << internalNormFactor_weight_scale_variation_muR_1p0_muF_2p0 << std::endl;
    # std::cout << "'internalNormFactor_weight_LHA_320900_down: '" << internalNormFactor_weight_LHA_320900_down << std::endl;
    # std::cout << "'internalNormFactor_weight_scale_variation_muR_1p0_muF_0p5: '" << internalNormFactor_weight_scale_variation_muR_1p0_muF_0p5 << std::endl;
    # std::cout << "'internalNormFactor_weight_LHA_320900_up: '" << internalNormFactor_weight_LHA_320900_up << std::endl;
    # std::cout << "'internalNormFactor_weight_LHA_320900_nominal: '" << internalNormFactor_weight_LHA_320900_nominal << std::endl;
    # std::cout << "'internalNormFactor_weight_LHA_320900_up: '" << internalNormFactor_weight_LHA_320900_up << std::endl;
    # std::cout << "'internalNormFactor_weight_LHA_320900_down: '" << internalNormFactor_weight_LHA_320900_down << std::endl;
    # std::cout << "==================================================================================" << std::endl;
    # """
        return code

