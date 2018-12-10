import ROOT
import os
import sys
import importlib 

# local imports       
filedir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(filedir+"/tools")
import plotClasses
import PDFutils

class catData:
    def __init__(self):
        self.discrs = []
        self.nhistobins = []
        self.minxvals = []
        self.maxxvals = []
        self.categories = []

        self.plotPreselections = []
        self.binlabels = []

    def getNEntries(self):
        return len(self.discrs)

    def getEntry(self, i):
        return {
            "discr":            self.discrs[i],
            "nhistobins":       self.nhistobins[i],
            "minxvals":         self.minxvals[i],
            "maxxvals":         self.maxxvals[i],
            "category":         self.categories[i],
            "plotPreselection": self.plotPreselections[i],
            "binlabel":         self.binlabels[i]}

class configData:
    def __init__(self, analysisClass, configDataBaseName = ""):

        print("loading configdata ...")
        # name of files in config
        self.basename = configDataBaseName
        self.analysis = analysisClass
        self.pltcfg = self.analysis.getPlotConfig()
        self.cfgdir = self.analysis.pyrootdir + "/configs/"
        self.plotNumber = analysisClass.plotNumber
        self.Data = None

    def initData(self):
        self.Data = catData()

    def getData():
        return self.Data

    def writeConfigDataToWorkdir(self):
        if self.Data == None:
            print("there is no config data")
            return

        with open(self.analysis.workdir+"/configData.csv", "w") as csvf:
            csvf.write("categories,nhistobins,minxvals,maxxvals,discrs")
            for i in range(len(self.Data.categories)):
                line = "\n"
                line+= str(self.Data.categories[i])+";"
                line+= str(self.Data.nhistobins[i])+";"
                line+= str(self.Data.minxvals[i])+";"
                line+= str(self.Data.maxxvals[i])+";"
                line+= str(self.Data.discrs[i])
                csvf.write(line)
        print("wrote config data to workdir")
        print("path: "+str(self.analysis.workdir+"/configData.csv"))
        return

    def genDiscriminatorPlots(self, memexp):
        sys.path.append(self.cfgdir)
        fileName = self.basename+"_plots"
        configdatafile = importlib.import_module( fileName )
        configdatafile.memexp = memexp

        self.discriminatorPlots = configdatafile.getDiscriminatorPlots(self.Data, self.analysis.discrName)
        self.evtYieldCategories = configdatafile.evtYieldCategories()


    def getDiscriminatorPlotByNumber(self):
        # select the discr plots for a certain plot number
        self.discriminatorPlotByNumber = [self.discriminatorPlots[int(self.analysis.plotNumber)]]
        print("this is the new discriminatorPlot:")
        print(self.discriminatorPlotByNumber)



    def getDiscriminatorPlots(self):
        # if discriminatorPlot
        if not self.analysis.plotNumber == None:
            return self.discriminatorPlotByNumber
        else:
            return self.discriminatorPlots

    def getBinlabels(self):
        return self.Data.binlabels

    def getAddVariables(self):
        sys.path.append(self.cfgdir)
        fileName = self.basename+"_addVariables"
        print("getting additional variables from "+str(fileName))
        addVarModule = importlib.import_module( fileName )
        self.addVars = addVarModule.getAddVars()

    def getMEPDFAddVariables(self, csvfile):
        self.addVars += PDFutils.GetMEPDFadditionalVariablesList(csvfile)

    def printAddVariables(self):
        with open(self.analysis.workdir+"/additionalVariables.csv", "w") as csvf:
            csvf.write("addVars")
            for var in self.addVars:
                csvf.write("\n"+var)
        print("-"*50)
        print("all additional variables:")
        for var in self.addVars:
            print(var)
        print("additional variables saved to "+self.analysis.workdir+"/additionalVariables.csv")
        print("-"*50)
        return

    def getAdditionalDiscriminatorPlots(self, alwaysExecute = False):
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
        print(self.Data.discrs)
        #for index, row in self.Data.iterrows():
        for index in range(self.Data.getNEntries()):
            row = self.Data.getEntry(index)
            for additionalPlotVariable in self.addVars: #self.additionalPlotVariables:
                # Use fullVarName as key in class dict while additionalPlotVariable is key in map file
                fullVarName = row["discr"] + '_' + row["binlabel"] + '_' + additionalPlotVariable
                additionalPlotVarsDict_fromArgs[fullVarName] = [additionalPlotVariable, 10, 0, 150, 
                            row["discr"], row["plotPreselection"], row["binlabel"]]
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
        self.analysis.checkBins = False
        print "Set checkBins variable to false. Make sure, this variable is used in renameHistos."

        print "before adding stuff", self.discriminatorPlots
        # adding plots to discriminator plots 
        evaluatedPlotList = [eval(plt) for plt in plotList]
        self.discriminatorPlots.extend(evaluatedPlotList)
    
        print "after adding stuff", self.discriminatorPlots
        print("additional plots added to discriminatorPlots:")
        for plt in plotList:
            print(plt)


    def initSamples(self):
        # TODO: find a better naming sceme for the lists of samples/names/weights
        # they are used at many different places and it is not at all obvious which are used where and what they really contain

        sys.path.append(self.cfgdir)
        fileName = self.basename+"_samples"

        # imports file in cfgdir with given name as samplesData file
        # this file should have a function
        #       getSamples, getControlSamples, getSystSamples
        # where the samples lists are created, and functions
        #       getAllSystNames, getWeightSystNames, getOtherSystNames
        # where lists of names are created, and functions
        #       getSystWeights
        # where lists of weights are created
        samplesData = importlib.import_module( fileName )
        
        # list of samples
        self.samples = samplesData.getSamples( self.pltcfg )
        # debug printout
        print("-"*30+"\nsamples:")
        for sample in self.samples:
            print(sample.name)
        print("-"*30)        


        # list of controlsamples used in 'allSamples' list
        self.controlSamples = samplesData.getControlSamples( self.pltcfg )
        # debug printout
        print("-"*30+"\ncontrol samples:")
        for sample in self.controlSamples:
            print(sample.name)
        print("-"*30) 

        # list of systematic samples used in 'allSamples' and 'allSystSamples' list
        self.systSamples = samplesData.getSystSamples( self.pltcfg, self.analysis, self.samples )
        

        # list of samples used to write C program       
        self.allSamples = samplesData.getAllSamples( self.pltcfg, self.analysis, self.samples)
        # TODO is this used anywhere?
        #self.allSystSamples = samples + systSamples


        # list of samples used e.g. in renameHistos       
        self.allSystNames = samplesData.getAllSystNames( self.pltcfg )
        # list of syst names used in plotParallel
        self.weightSystNames = samplesData.getWeightSystNames( self.pltcfg )
        # list of syst names used in plotParallel
        self.otherSystNames = samplesData.getOtherSystNames( self.pltcfg )

        # list of syst weights used in plotParallel
        self.systWeights = samplesData.getSystWeights( self.pltcfg )


    def getEventYieldCategories(self):
        return self.evtYieldCategories
