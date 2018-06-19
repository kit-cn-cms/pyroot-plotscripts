import pandas
import ast
import ROOT
 
# local imports       
import plotClasses
import PDFutils
class configData:
    def __init__(self, pyrootdir, analysisClass, configDataBaseName = "", usedCategories = []):

        print("loading configdata ...")
        self.basename = configDataBaseName        
        self.pyrootdir = pyrootdir
        self.csvdir = pyrootdir + "/plottingscripts/configdata/"
        self.plotNumber = analysisClass.plotNumber

        # configdata
        self.Data = pandas.DataFrame(
            columns = ["categories", "nhistobins", "minxvals", "maxxvals", "discrs"])

        # data types of columns in .csv files
        self.colTypes = {"categories": ast.literal_eval, 
                            "nhistobins": int, 
                            "minxvals": float, 
                            "maxxvals": float, 
                            "discrs": str}

        # loop over usedCategories to load data and append to configdata lists
        for cat in usedCategories:
            catData = self.getCategoryData(cat)
            self.Data = self.Data.append(catData, ignore_index = True)

        # add plotPreselections and binlabels to DataFrame
        self.Data["plotPreselections"] = pandas.Series(
            (cat[0] for cat in self.Data.categories.values), index = self.Data.index)
        self.Data["binlabels"] = pandas.Series(
            (cat[1] for cat in self.Data.categories.values), index = self.Data.index)
        
        # get additionalPlotVariables from analysisClass
        # TODO rework this later into configData itself
        self.additionalPlotVariables = analysisClass.additionalPlotVariables

    
    def getDataFrame():
        return self.Data

    def getCategoryData(self, category):
        filename = self.csvdir+"/"+self.basename+"_"+category+".csv"
        print("loading " + filename)
        catDict = pandas.read_csv(filename, sep = ";", converters = self.colTypes)
        return catDict

    def writeConfigDataToWorkdir(self, workdir):
        with open(workdir+"/configData.csv", "w") as csvf:
            csvf.write("categories,nhistobins,minxvals,maxxvals,discrs")
            for i in range(self.Data.categories.size):
                line = "\n"
                line+= str(self.Data.categories[i])+";"
                line+= str(self.Data.nhistobins[i])+";"
                line+= str(self.Data.minxvals[i])+";"
                line+= str(self.Data.maxxvals[i])+";"
                line+= str(self.Data.discrs[i])
                csvf.write(line)
        print("wrote config data to workdir")
        print("path: "+str(workdir+"/configData.csv"))
        return

    def assertData(self):
        assert(self.Data.nhistobins.size == self.Data.maxxvals.size)
        assert(self.Data.nhistobins.size == self.Data.minxvals.size)
        assert(self.Data.nhistobins.size == self.Data.categories.size)
        assert(self.Data.nhistobins.size == self.Data.discrs.size)
    
    def printLengths(self):
        print("length of nhistobins       \t"+str(self.Data.nhistobins.size))
        print("length of minxvals         \t"+str(self.Data.minxvals.size))
        print("length of maxxvals         \t"+str(self.Data.maxxvals.size))
        print("length of discrs           \t"+str(self.Data.discrs.size))
        print("length of plotPreselections\t"+str(self.Data.plotPreselections.size))
        print("length of binlabels        \t"+str(self.Data.binlabels.size))   

    def genDiscriminatorPlots(self, discrname):
        discriminatorPlots = []
        for index, row in self.Data.iterrows():
            discriminatorPlots.append(
                plotClasses.Plot(
                    histo = ROOT.TH1F(
                        discrname+"_"+row["binlabels"], 
                        "final discriminator ("+row["binlabels"]+")", 
                        int(row["nhistobins"]), 
                        float(row["minxvals"]), 
                        float(row["maxxvals"])),
                    variable = row["discrs"],
                    selection = row["plotPreselections"],
                    label = row["binlabels"]))
        self.discriminatorPlots = discriminatorPlots

    def adjustDiscriminatorPlots(self):
        # select the discr plots for a certain plot number
        self.discriminatorPlotByNumber = [self.discriminatorPlots[int(self.plotNumber)]]
        print("this is the new discriminatorPlot:")
        print(self.discriminatorPlotByNumber)



    def getDiscriminatorPlots(self):
        # if discriminatorPlot
        if self.plotNumber:
            return self.discriminatorPlotByNumber
        else:
            return self.discriminatorPlots

    def getBinlabels(self):
        return self.Data.binlabels.values

    def getAddVariables(self):
        path = self.pyrootdir+"/plottingscripts/configdata/"+self.basename+"_addVariables.csv"
        print( "searching for additional variables in "+str(path))
        variables = pandas.read_csv(path)
        self.addVars = list(variables["addVars"].values)

    def getMEPDFAddVariables(self, csvfile):
        self.addVars += PDFutils.GetMEPDFadditionalVariablesList(csvfile)

    def printAddVariables(self, workdir):
        with open(workdir+"/additionalVariables.csv", "w") as csvf:
            csvf.write("addVars")
            for var in self.addVars:
                csvf.write("\n"+var)
        print("-"*50)
        print("all additional variables:")
        for var in self.addVars:
            print(var)
        print("additional variables saved to "+workdir+"/additionalVariables.csv")
        print("-"*50)
        return

    def getAdditionalDiscriminatorPlots(self, analysisClass, alwaysExecute=False):
        """ Function creates plot list for additional (input) variables
        Function checks if additionalPlotVariablesMap.py file exists.
        If yes, then it will try to use it for determination of the 
            amount of bins and the bin range of the plots.
            In case some variable cannot be mapped, 
            the variable will be added to existing file and user will get warned.
        If no, then it will construct such a dict and stop the further execution.
        
        mapFile is a dict with additionalPlotVariable as key and numberOfBins, 
            binLowerEdge, binUpperEdge as values contained in list
        """

        # Create dictionary for discriminators and preselections using additionalPlotVariables
        # Dictionary contains    additionalPlotVariable, numberOfBins, binLowerEdge, 
        #                        binUpperEdge ,discr, preselection, binLabel,            

        additionalPlotVarsDict_fromArgs = {}
        for index, row in self.Data.iterrows():
            for additionalPlotVariable in self.additionalPlotVariables:
                # Use fullVarName as key in class dict while additionalPlotVariable is key in map file
                fullVarName = row["discrs"] + '_' + row["binlabels"] + '_' + additionalPlotVariable
                additionalPlotVarsDict_fromArgs[fullVarName] = [additionalPlotVariable, 10, 0, 150, 
                            row["discrs"], row["plotPreselections"], row["binlabels"]]
        print("number of additional plot variables gathered from argv: " + \
                str(len(additionalPlotVarsDict_fromArgs)))
        
        # Stop further execution if dict file did not exist, 
        # map could not be read or variable could not be mapped.
        stopFurtherExecution = False

        # Try to open map (dict) file and read dict
        additionalPlotVarsDict_fromFile = {}
        # TODO adjust path
        if os.path.isfile('additionalPlotVariablesMap.py'):
            print 'Found additionalPlotVariablesMap.py file. Will try to open it now.'
            with open('additionalPlotVariablesMap.py') as mapFile:
                additionalPlotVarsDict_fromFile = eval(mapFile.read())
            if not additionalPlotVarsDict_fromFile:
                print "Could not read map from additionalPlotVariablesMap.py file or file is empty."
                print "Will update existing one and stop further execution."
                stopFurtherExecution = True
        else:
            print 'Did not find additionalPlotVariablesMap.py file. Will create one and stop further execution.'
            stopFurtherExecution = True
        print("number of additional plot variables gathered from file: " + \
                str(len(additionalPlotVarsDict_fromFile)))
        

        # Compare internal map with map from file and add additional keys if necessary
        print "Comparing map from additionalPlotVariablesMap.py file (or empty dict) \
                with internal map of additional plot variables."
        print "If necessary, adding keys from internal map to map file."
        missingKeysInFile = set()
        for classKey in additionalPlotVarsDict_fromArgs.keys():
            # Check for missing additionalPlotVariable description in map file
            # In map file additionalPlotVariable is the key while in class fullVarName
            mapFileKey = additionalPlotVarsDict_fromArgs[classKey][0]
            if not mapFileKey in additionalPlotVarsDict_fromFile:
                missingKeysInFile.add(mapFileKey)
            # otherwise replace internal key/value pair with external one
            else:
                # retrieve full value list
                tmpList = additionalPlotVarsDict_fromArgs[classKey]
                # and replace content with stored content
                # numberOfBins replacement
                tmpList[1] = additionalPlotVarsDict_fromFile[mapFileKey][0]
                # binLowerEdge replacement
                tmpList[2] = additionalPlotVarsDict_fromFile[mapFileKey][1]
                # binUpperEdge replacement
                tmpList[3] = additionalPlotVarsDict_fromFile[mapFileKey][2]
                additionalPlotVarsDict_fromArgs[classKey] = tmpList
        if missingKeysInFile:
            print "Found keys missing in map from file and required for plotting additional variables:"
            print missingKeysInFile 
            print "Will add keys to map file using default values."
            print "Afterwards will stop further execution."
            # Add missing keys to mapFile dictionary
            for missingKey in missingKeysInFile:
                additionalPlotVarsDict_fromFile[missingKey] = [10,0,150]
            stopFurtherExecution = True


        # Dedicated sort function, so that writen out dict is sorted    
        def sortByUsingLastPart(elem):
            return elem.rsplit('_')[-1]

        # Write dictionary to file
        with open('additionalPlotVariablesMap.py', 'w') as mapFile:
            mapFile.write('{\n')
            # sort dict and write entry for each additionalPlotVariable in file
            for mapFileKey in sorted(additionalPlotVarsDict_fromFile.iterkeys(), key=sortByUsingLastPart):
                # list contains numberOfBins, binLowerEdge, binUpperEdge
                tmpList = additionalPlotVarsDict_fromFile[mapFileKey]
                mapFile.write("""'""" + mapFileKey + """': [ """ + str(tmpList[0]) + ', ' + \
                                str(tmpList[1]) + ', ' + str(tmpList[2])    + """ ],\n""")
            mapFile.write('}')

        if stopFurtherExecution and not alwaysExecute:
            sys.exit('Stopping execution since mapping for additional variable plotting was not successful. \
                        \n Check the file additionalPlotVariablesMap.py and adjust it accordingly.')

        # construct list containing all additionalPlotVariables
        plotList = []
        for classKey in additionalPlotVarsDict_fromArgs.keys():
            currList = additionalPlotVarsDict_fromArgs[classKey]
            # Construct full var name, currList: additionalPlotVariable, numberOfBins, binLowerEdge, binUpperEdge, discr, preselection, binLabel
            fullVarName = currList[4] + '_' + currList[6] + '_' + currList[0]
            plotString = '''Plot(ROOT.TH1F("''' + fullVarName + '''", "add. var. (''' + fullVarName +  \
                         ''')",''' + str(currList[1]) + ',' + str(currList[2]) + ',' + str(currList[3]) + \
                         '''),"''' + currList[0] + '''","''' + currList[5] + '''","''' + currList[6] + '''")'''
            plotList.append(plotString)

        # Set variable to deactivate checkBins functionality in renameHistos, because otherwise it will take a long time.
        analysisClass.checkBins = False
        print "Set checkBins variable to false. Make sure, this variable is used in renameHistos."

        print "before adding stuff", self.discriminatorPlots
        # adding plots to discriminator plots 
        evaluatedPlotList = [eval(plt) for plt in plotList]
        self.discriminatorPlots.extend(evaluatedPlotList)
    
        print "after adding stuff", self.discriminatorPlots
        print("additional plots added to discriminatorPlots:")
        for plt in plotList:
            print(plt)





