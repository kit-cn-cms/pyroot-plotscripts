import os
import sys
import pandas
import importlib
from collections import OrderedDict
import pprint

class SystematicsForProcess:
    def __init__(self,name,process,typ,construction,expression=None,plot=None):
        self.name=name
        self.process=process 
        self.typ=typ 
        self.construction=construction 
        self.expression=expression
        self.plot=plot


class Systematics:
    def __init__(self,systematicconfig,weightDictionary = {}, replacing_config = None, relevantProcesses = []):
        print("loading systematics config ...")
        self.systematics=pandas.read_csv(systematicconfig,sep=",")
        self.systematics.fillna("-", inplace=True)
        self.relevantProcesses = relevantProcesses
        # drop not neccessary stuff, if relevantProcesses are given
        if len(self.relevantProcesses) != 0:
            columns = ['Uncertainty','Type','Construction','Up','Down','Plot']+self.relevantProcesses
            # drop all non relevant processes
            self.systematics.drop(self.systematics.columns.difference(columns), 1, inplace=True)
            # drop all non relevant systs
            self.systematics = self.systematics[columns]
            self.systematics = self.systematics[~self.systematics[self.relevantProcesses].eq('-', axis=0).all(axis=1)]
        self.weightDictionary = weightDictionary

        self.replacing_config = None
        self.init_replace_config(replacing_config)
        
        self.__dict_weight_systs = self.construct_syst_dict("weight")
        self.__dict_variation_systs = self.construct_syst_dict("variation")
        self.__dict_rate_systs = self.construct_syst_dict("rate")

    def init_replace_config(self, replacing_config):
        replace_module = None
        print("replacing config: {}".format(replacing_config))
        if replacing_config:
            try:
                cfg_dir = os.path.dirname(replacing_config)
                cfg_base = os.path.basename(replacing_config)
                if not cfg_dir in sys.path:
                    sys.path.append(cfg_dir)
                replace_module = importlib.import_module(cfg_base)
            except:
                print("ERROR: Could not import replacing config '{}'".format(replacing_config))
        if replace_module:
            try:
                self.replacing_config = replace_module.config
            except:
                print("ERROR: Could not load replacing config from '{}'".format(replacing_config))
        if self.replacing_config:
            print("WILL USE REPLACE CONFIGURATION FROM '{}'".format(replacing_config))

    def construct_syst_dict(self, construct_type):
        syst_dict = OrderedDict()
        systs = self.systematics.loc[self.systematics["Construction"] == construct_type]
        for i,systematic in systs.iterrows():
            systName=systematic["Uncertainty"]
            if systName.startswith("#"):
                continue
            #adds variable name to list of systs
            if self.replacing_config and systName in self.replacing_config:
                syst_dict.update(self.expand_uncertainties(systematic))
            else:
                expr_up = self.replaceDummies(systematic["Up"])
                expr_down = self.replaceDummies(systematic["Down"])
                if expr_up == "-" and expr_down == "-":
                    syst_dict[systName] = "-"
                elif expr_up == "-" or expr_down == "-":
                    syst_dict[systName] = expr_up if not expr_up == "-" else expr_down
                else:
                    name_var=systName+"Up"
                    syst_dict[name_var] = expr_up
                    name_var=systName+"Down"
                    syst_dict[name_var] = expr_down
        return syst_dict

    def replace_in_expression(self, insert_list, to_replace, systname, expression):
        new_systs = {}
        print("ATTENTION: REPLACING {}".format(systname))
        print("expression:")
        print(expression)
        for insert in insert_list:
            print("\t{}".format(insert))
            new_name = "_".join([systname, insert])
            new_systs[new_name] = expression.replace(to_replace, insert)
        return new_systs

    def expand_uncertainties(self, syst):
        expanded_systs = {}
        systName = syst["Uncertainty"]
        up_variation = self.replaceDummies(syst["Up"])
        down_variation = self.replaceDummies(syst["Down"])
        syst_variations = {}
        if up_variation == "-" or down_variation == "-":
            syst_variations[systName] = up_variation if not up_variation == "-" else down_variation
        else:
            syst_variations[systName+"Up"] = up_variation
            syst_variations[systName+"Down"] = down_variation
        infodict = self.replacing_config.get(systName, None)
        broken = True
        if infodict:
            to_replace = infodict.get("to_replace", None)
            if to_replace:
                expand_with = infodict.get("expand_with", None)
                if isinstance(expand_with, list):
                    for syst in syst_variations:
                        expr = syst_variations[syst]
                        if not to_replace in expr:
                            print("ERROR: cannot replace '{}' in '{}'".format(to_replace, syst))
                            broken = True
                            break
                            
                        expanded_systs.update(self.replace_in_expression(   insert_list = expand_with,
                                                                            to_replace = to_replace,
                                                                            systname = syst,
                                                                            expression = expr
                                                                            )
                                                )
                        broken = False
                else:
                    print("ERROR: Could not load keyword 'expand_with' from config!")
            else:
                print("ERROR: Could not load keyword 'to_replace' from config!")
        else:
            print("ERROR: Found no information for systematic '{}' in syst replacing config")
        if broken:
            print("Skipping uncertainty '{}'".format(systName))
            expanded_systs = {}
        return expanded_systs


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
            names = []
            typ=systematic["Type"]
            up = systematic["Up"]
            down = systematic["Down"]
            if up == "-" or down == "-":
                names.append(name)
            else:
                names = [name+x for x in ["Up", "Down"]]

            if self.replacing_config and name in self.replacing_config:
                expand_with = self.replacing_config.get(name, {}).get("expand_with",[])
                names = ["_".join([name, x]) for x in expand_with for name in names]

            for process in list_of_processes:
                if systematic[process] is not "-":
                    for n in names:
                        construction = "-"
                        expr = "-"
                        if n in self.__dict_weight_systs:
                            construction = "weight"
                            expr = self.__dict_weight_systs[n]
                        elif n in self.__dict_variation_systs:
                            construction = "variation"
                            expr = self.__dict_variation_systs[n]
                        elif n in self.__dict_rate_systs:
                            construction = "rate"
                            expr = self.__dict_rate_systs[n]
                        else:
                            print("WARNING: no systematics entry found for '{}'".format(n))
                            continue
                        self.processes[process][n]=SystematicsForProcess(n,process,typ,construction,expr)

    # # only gets variables to plot, without variation of name with up and down!
    # def plotSystematicsForProcesses(self,list_of_processes):
    #     self.processes={}
    #     for process in list_of_processes:
    #         self.processes[process]={}
    #     for i,systematic in self.systematics.iterrows():
    #         name=systematic["Uncertainty"]
    #         if name.startswith("#"):
    #             continue
    #         plot=str(systematic["Plot"])
    #         if plot=="-":
    #             continue
    #         typ=systematic["Type"]
    #         construction=systematic["Construction"]
    #         for process in list_of_processes:
    #             if systematic[process] is not "-":
    #                 self.processes[process][name]=SystematicsForProcess(name,process,typ,construction,
    #                                                                         plot=plot)

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
    
    def get_all_weight_systs_with_expressions(self):
        """function to return a dictionary with all weight 
        systematics and the corresponding expressions.
        The dictionary contains the weight uncertainties
        for all relevant processes

        Returns:
            [dict]: Dictionary for all relevant processes of format
                    {
                        "weight_uncertainty_name" : "expression"
                    }
        """
        # init dictionary to return
        rdict = {}
        # try to load the dictionary with uncertainties for the 
        # relevant processes. If this wasn't initialized before, the
        # property doesn't exist, which is why we try first
        try:
            source = self.processes
            # if this is successful, loop through all the processes and
            # collect the relevant weight systematics
            for p in source:
                # loop through the relevant processes
                proc_dict = source[p]
                # loop through the systematics
                for syst in proc_dict:
                    # first check that the construction of the entry is
                    # 'weight'
                    entry = proc_dict[syst]
                    if not entry.construction == "weight":
                        continue
                    # update the return dictionary. This will also 
                    # ensure that each systematic is present exactly
                    # once
                    rdict.update({syst: entry.expression})
        except:
            # if the dictionary with systematics for the relevant processes
            # is not initialized, use the dictionary with all weight
            # systematics
            rdict = self.__dict_weight_systs
        
        return rdict

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
                print (systName)
        return plotShapes

    def replaceDummies(self, variationString):
        for dummy in self.weightDictionary:
            variationString = variationString.replace(dummy, self.weightDictionary[dummy])
        
        variationString = variationString.strip('"')
        return variationString



