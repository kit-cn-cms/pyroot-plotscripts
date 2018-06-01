import pandas
import ast
import plotutils

class samplesData:
    def __init__(self, pltcfg):
        self.pltcfg = pltcfg
        self.samples = self.pltcfg.samplesLimits
        self.samples_data = self.pltcfg.samplesDataControlPlots

        self.systsamples = []
        self.systnames = []

    def addSystSamples(self, systNames, systfileNames,
                        pathReplace = ["''","''"],
                        selReplace = ["''","''"],
                        selReplace2 = ["''","''"],
                        filternicks = None,
                        filternames = None ):
        systnames += systNames
        for sample in self.samples:
            if filternicks:
                if sample.nick not in filternicks:
                    continue
            if filternames:
                if sample.name not in filternames:      
                    continue
            for name, filename in zip(systNames, systfileNames):
                selection = sample.selection.replace(eval(selReplace[0]),eval(selReplace[1]))
                selection = selection.replace( eval(selReplace2[0]), eval(selReplace2[1]) )
                self.systsamples.append(
                    plotutils.Sample(
                        sample.name + name, 
                        sample.color,
                        sample.path.replace(eval(pathReplace[0]),eval(pathReplace[1])),
                        selection,
                        sample.nick + name,
                        samDict=self.pltcfg.sampleDict) )
                        
    def addAllSamples(self, addNames):
        self.allsamples = self.samples + self.systsamples
        self.allsystnames = addNames + self.systnames
                        
        
class configData:
    def __init__(self, pyrootdir, name = "", usedCategories = []):

        print("loading configdata ...")
        self.__basename = name        
        self.__pyrootdir = pyrootdir
        self.__csvdir = pyrootdir + "/plottingscripts/configdata/"
        # configdata
        self.categories = []
        self.nhistobins = []
        self.minxvals = []
        self.maxxvals = []
        self.discrs = []

        # data types of columns in .csv files
        self.__colTypes = {"categories": ast.literal_eval, "nhistobins": int, "minxvals": float, "maxxvals": float, "discrs": str}

        # loop over usedCategories to load data and append to configdata lists
        for cat in usedCategories:
            catDict = self.__getCategories(cat)
            
            self.__addCatToConfig(catDict)

        self.plotPreselections = [cat[0] for cat in self.categories]
        self.binlabels = [cat[1] for cat in self.categories]

    def __getCategories(self, category):
        catDict = pandas.read_csv(self.__csvdir+"/"+self.__basename+"_"+category+".csv",
                                    sep = ";", converters = self.__colTypes)
        return catDict

    def __addCatToConfig(self, catDict):
        self.categories += list( catDict["categories"].values )
        self.nhistobins += list( catDict["nhistobins"].values )
        self.minxvals += list( catDict["minxvals"].values )
        self.maxxvals += list( catDict["maxxvals"].values )
        self.discrs += list( catDict["discrs"].values )
        return 

    def writeConfigDataToWorkdir(self, workdir):
        with open(workdir+"/configData.csv", "w") as csvf:
            csvf.write("categories,nhistobins,minxvals,maxxvals,discrs")
            for i in range(len(self.categories)):
                line = "\n"
                line+= str(self.categories[i])+";"
                line+= str(self.nhistobins[i])+";"
                line+= str(self.minxvals[i])+";"
                line+= str(self.maxxvals[i])+";"
                line+= str(self.discrs[i])
                csvf.write(line)
        print("wrote config data to workdir")
        print("path: "+str(workdir+"/configData.csv"))
        return

    def assertData(self):
        assert(len(self.nhistobins) == len(self.maxxvals))
        assert(len(self.nhistobins) == len(self.minxvals))
        assert(len(self.nhistobins) == len(self.categories))
        assert(len(self.nhistobins) == len(self.discrs))
        

def getAddVariables(pyrootdir, name = ""):
    path = pyrootdir+"/plottingscripts/configdata/"+name+"_addVariables.csv"
    print( "searching for additional variables in "+str(path))
    variables = pandas.read_csv(path)
    return list(variables["addVars"].values)

def saveAddVariablesToWorkdir(workdir, addvars, printToConsole = True):
    with open(workdir+"/additionalVariables.csv", "w") as csvf:
        csvf.write("addVars")
        for var in addvars:
            csvf.write("\n"+var)
    # print to console
    if printToConsole == True:
        print("-"*50)
        print("all additional variables:")
        for var in addvars:
            print(var)
        print("-"*50)
    print("additional variables saved to "+workdir+"/additionalVariables.csv")
    return
