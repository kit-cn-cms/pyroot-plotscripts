


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
            code += "float internalNormFactor_"+weight+"= 0.0;\n"
        return code

    # AddGenWeightNormMap
    def addNormalizationMap(self):
        code = "std::map<TString,float> GenWeight_Norm_Map;\n"
        for key in self.csv_dict:
            code += "GenWeight_Norm_Map['"+key[0]+"_"+key[1]+"']="+self.csv_dict[key]+";\n"
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
        TString translatedCurrentRelevantSampleNameForGenWeights = sampleTranslationMapCPP[currentRelevantSampleNameForGenWeights];
        //std::cout<<'GenWeight relation '<<currentfilename<<" "<<currentRelevantSampleNameForGenWeight<<" "<<translatedCurrentRelevantSampleNameForGenWeights<<std::endl;
        """
        for weight in self.weightList:
            code += "internalNormFactor_"+weight+" = 1.0;\n"
        code += "if( GenWeight_Norm_Map.find("+"translatedCurrentRelevantSampleNameForGenWeights"+"+'_"+self.weightList[0]+"')!=GenWeight_NormMap.end()){;\n"
        for weight in self.weightList:
            code += "internalNormFactor_"+weight+"="+"GenWeight_Norm_Map["+"translatedCurrentRelevantSampleNameForGenWeights"+"+'_"+weight+"'];\n"
        code += "}\n"
        code += "else{ std::cout < 'did not find weights in map '<<translatedCurrentRelevantSampleNameForGenWeights<<std::endl;}\n"
        code += "//std::cout<<'first internal weight '<<"+"translatedCurrentRelevantSampleForGenWeights"+"+'_"+self.weightList[0]+"' <<' '<< internalNormFactor_"+self.weightList[0]+"<<std::endl;\n"
        return code

