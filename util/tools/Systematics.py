import os
import sys
import pandas
from collections import OrderedDict

class SystematicsForProcess:
    def __init__(self,name,process,typ,construction,expression=None,plot=None):
        self.name=name
        self.process=process 
        self.typ=typ 
        self.construction=construction 
        self.expression=expression
        self.plot=plot


class Systematics:
    def __init__(self,systematicconfig,weightDictionary = {}):
        print "loading systematics config ..."
        self.systematics=pandas.read_csv(systematicconfig,sep=",")
        self.systematics.fillna("-", inplace=True)
        self.weightDictionary = weightDictionary

        self.__dict_weight_systs = self.construct_syst_dict("weight")
        self.__dict_variation_systs = self.construct_syst_dict("variation")
        self.__dict_rate_systs = self.construct_syst_dict("rate")

    def construct_syst_dict(self, construct_type):
        syst_dict = OrderedDict()
        systs = self.systematics.loc[self.systematics["Construction"] == construct_type]
        for i,systematic in systs.iterrows():
            systName=systematic["Uncertainty"]
            if systName.startswith("#"):
                continue
            #adds variable name to list of weightsysts
            
            name_var=systName+"Up"
            expr = self.replaceDummies(systematic["Up"])
            syst_dict[name_var] = expr
            name_var=systName+"Down"
            expr = self.replaceDummies(systematic["Down"])
            syst_dict[name_var] = expr
        return syst_dict
    """
    get all variables that shall be used, 
    for each shape variable makes two variables
    with Up and Down added at the end to find 
    them in the ROOT File
    """ 
    def getSystematicsForProcesses(self,list_of_processes):
        self.processes={}
        for process in list_of_processes:
            self.processes[process]={}
        for i,systematic in self.systematics.iterrows():
            name=systematic["Uncertainty"]
            if name.startswith("#"):
                continue
            typ=systematic["Type"]
            construction=systematic["Construction"]
            Up=self.replaceDummies(systematic["Up"])
            if Up=="-":
                Up=None
            Down=self.replaceDummies(systematic["Down"])
            if Down=="-":
                Down=None
            for process in list_of_processes:
                if systematic[process] is not "-":
                    if Up:
                        up=name+"Up"    
                        self.processes[process][up]=SystematicsForProcess(up,process,typ,construction,Up)
                    if Down:
                        down=name+"Down"
                        self.processes[process][down]=SystematicsForProcess(down,process,typ,construction,Down)
                    if not Up and not Down:
                        self.processes[process][name]=SystematicsForProcess(name,process,typ,construction)

    def construct_pdf_relic_systs(self):
        pass

    # only gets variables to plot, without variation of name with up and down!
    def plotSystematicsForProcesses(self,list_of_processes):
        self.processes={}
        for process in list_of_processes:
            self.processes[process]={}
        for i,systematic in self.systematics.iterrows():
            name=systematic["Uncertainty"]
            if name.startswith("#"):
                continue
            plot=str(systematic["Plot"])
            if plot=="-":
                continue
            typ=systematic["Type"]
            construction=systematic["Construction"]
            for process in list_of_processes:
                if systematic[process] is not "-":
                    self.processes[process][name]=SystematicsForProcess(name,process,typ,construction,
                                                                            plot=plot)

    #returns weight systematics for specific process
    def get_weight_systs(self,process):
        weightsysts=[]
        for systematic in self.processes[process]:
            if self.processes[process][systematic].construction=="weight":
                #adds variable name to list of weightsysts
                weightsysts.append(systematic)
        return weightsysts
    #returns variation systematics for specific process
    def get_variation_systs(self,process):
        variationsysts=[]
        for systematic in self.processes[process]:
            if self.processes[process][systematic].construction=="variation":
                #adds variable name to list of variationsysts
                variationsysts.append(systematic)
        return variationsysts
    #returns all rate systematics
    def get_rate_systs(self,process):
        ratesysts=[]
        for systematic in self.processes[process]:
            if self.processes[process][systematic].construction=="rate":
                #adds variable name to list of ratesysts
                ratesysts.append(systematic)
        return ratesysts
    #returns all shape systematics
    def get_shape_systs(self,process):
        shape_systs=self.get_weight_systs(process)+self.get_variation_systs(process)
        return shape_systs

    #returns all weight systematics
    def get_all_weight_systs(self):
        """
        function to return names of weight systematics
        return list of strings
        """
        return self.__dict_weight_systs.keys()

    def get_all_weight_expressions(self):
        """
        function to return expressions for weight systematics
        returns list of strings
        """
        return self.__dict_weight_systs.values()

    #returns all variation systematics
    def get_all_variation_systs(self):
        variationsysts=[]
        for i,systematic in self.systematics.iterrows():
            if systematic["Uncertainty"].startswith("#"):
                continue
            if systematic["Construction"]=="variation":
                #adds variable name to list of variationsysts
                systName=systematic["Uncertainty"]
                up=systName+"Up"
                down=systName+"Down"
                variationsysts.append(up)
                variationsysts.append(down)
        return variationsysts
    #returns all rate systematics
    def get_all_rate_systs(self):
        ratesysts=[]
        for i,systematic in self.systematics.iterrows():
            if systematic["Uncertainty"].startswith("#"):
                continue
            if systematic["Construction"]=="rate":
                #adds variable name to list of ratesysts
                ratesysts.append(systematic["Uncertainty"])
        return ratesysts

    def makeCSV(self,list_of_processes,outputpath):
        header=["Uncertainty","Type"]
        header+=list_of_processes
        #only get information for processes that are included
        newCSV=self.systematics[header]
        #delete all uncertainties that start with "#" or "-"
        newCSV = newCSV[~newCSV["Uncertainty"].astype(str).str.startswith("#")]
        newCSV.to_csv(outputpath, index=False)

    def plot_shapes(self):
        plotShapes=[]
        for i,systematic in self.systematics.iterrows():
            if systematic["Uncertainty"].startswith("#"):
                continue

            if "shape" in systematic["Type"]:
                systName=systematic["Uncertainty"]
                if not str(systematic["Plot"])=="-":
                    plotShapes.append(systName)
                else:
                    plotShapes.append("#"+systName)
                print systName
        return plotShapes

    def replaceDummies(self, variationString):
        for dummy in self.weightDictionary:
            variationString = variationString.replace(dummy, self.weightDictionary[dummy])
        
        variationString = variationString.replace("\"","")
        return variationString



