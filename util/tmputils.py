import pandas
import ast
import plotutils
import ROOT

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
                        filtername = None ):
        self.systnames += systNames
        for sample in self.samples:
            if filternicks:
                if sample.nick not in filternicks:
                    continue
            if filtername:
                if not sample.name == filtername:      
                    continue
            for name, filename in zip(systNames, systfileNames):
                selection = sample.selection.replace( eval(selReplace[0]), eval(selReplace[1]) )
                selection = selection.replace( eval(selReplace2[0]), eval(selReplace2[1]) )
                path = sample.path.replace( eval(pathReplace[0]), eval(pathReplace[1]) )
                
                self.systsamples.append(
                    plotutils.Sample(
                        sample.name + name, 
                        sample.color,
                        path,
                        selection,
                        sample.nick + name,
                        samDict=self.pltcfg.sampleDict) )
                        
    def addAllSamples(self, addNames):
        self.allsamples = self.samples + self.samples_data + self.systsamples
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
    
    def printLengths(self):
        print("length of nhistobins       \t"+str(len(self.nhistobins)))
        print("length of minxvals         \t"+str(len(self.minxvals)))
        print("length of maxxvals         \t"+str(len(self.maxxvals)))
        print("length of discrs           \t"+str(len(self.discrs)))
        print("length of plotPreselections\t"+str(len(self.plotPreselections)))
        print("length of binlabels        \t"+str(len(self.binlabels)))       
        zipped = zip(self.discrs,self.plotPreselections,self.binlabels,self.nhistobins,self.minxvals,self.maxxvals)
        print("length of zipped data      \t"+str(len(zipped)))

    def genDiscriminatorPlots(self, discrname):
        self.discriminatorPlots = []
        zippedData = zip(self.discrs,self.plotPreselections,self.binlabels,self.nhistobins,self.minxvals,self.maxxvals)
        for discr, preselection, binlabel, nbin, minv, maxv in zippedData:
            self.discriminatorPlots.append(
                plotutils.Plot(
                    histo = ROOT.TH1F(discrname+"_"+binlabel, "final discriminator ("+binlabel+")", nbin, minv, maxv),
                    variable = discr,
                    selection = preselection,
                    label = binlabel))

    def addAdditionalDiscriminatorPlots(self, plotlist):
        evaluatedPlotList = [eval(plt) for plt in plotlist]
        self.additionalPlotList = evaluatedPlotList
        self.discriminatorPlots.extend(self.additionalPlotList)               
        print("additional plots added to discriminatorPlots:")
        for plt in plotlist:
            print(plt)

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
