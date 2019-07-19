import ROOT
import os
import sys
import importlib 

# local imports       
filedir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(filedir+"/tools")
import plotClasses
import Systematics

class catData:
    def __init__(self):
        self.categories         = {}
        self.datavariables      = []

    def getNEntries(self):
        return len(self.categories)


class configData:
    def __init__(self, analysisClass, variable_config, plot_config, execute_file = None):

        print("loading configdata ...")
        # name of files in config
        self.variable_config = variable_config
        self.plot_config = plot_config

        self.execute_file = execute_file

        self.analysis = analysisClass
        self.pltcfg = self.analysis.getPlotConfig()
        self.cfgdir = self.analysis.pyrootdir + "/configs/"
        self.Data = None

        if self.execute_file:
            self.saveFile()

    def saveFile(self):
        command = "cp {} {}/plottingscript.py".format(self.execute_file, self.analysis.workdir)
        print(command)
        os.system(command)        

    def initData(self):
        self.Data = catData()

    def getData():
        return self.Data

    def initSystematics(self,systconfig):

        print "loading systematics..."
        self.systconfig=systconfig
        processes=self.pltcfg.list_of_processes
        workdir=self.analysis.workdir
        outputpath=workdir+"/datacard.csv"
        self.systematics=Systematics.Systematics(self.cfgdir+"/"+systconfig+".csv", self.pltcfg.weightReplacements)
        self.systematics.getSystematicsForProcesses(processes)
        datacard_processes = self.pltcfg.datacard_processes
        self.systematics.makeCSV(datacard_processes,outputpath)
        for sample in self.pltcfg.samples:
            sample.setShapes(self.systematics.get_shape_systs(sample.nick))
        self.plots=self.systematics.plot_shapes()

    def writeConfigDataToWorkdir(self):
        # deprecated
        return

    def genDiscriminatorPlots(self, memexp, dnnInterface = None):
        if not self.plot_config:
            print("no plot config specified - generating plots from DNN checkpoints")
            if not dnnInterface: sys.exit("cannot load plots because no dnnInterface specified and no plotconfig")
            # loading dnn interface
            path = dnnInterface["interfacePath"]
            sys.path.append(os.path.dirname(path))
            dnnModule = importlib.import_module( path.split("/")[-1].replace(".py","") )
            interface = dnnModule.theInterface(
                dnnSet = dnnInterface["checkpointFiles"], 
                crossEvaluation = self.analysis.crossEvaluation)

            # generate new plot file
            cfg_string = interface.generatePlotConfig()

            # generate output file
            out_file = self.analysis.workdir + "/plotconfig_local.py"
            with open(out_file,"w") as f:
                f.write(cfg_string)
            print("wrote plot config to {}".format(out_file))

            self.plot_config = "plotconfig_local"
            sys.path.append(self.analysis.workdir)
        
        sys.path.append(self.cfgdir)
        fileName = self.plot_config
        configdatafile = importlib.import_module( fileName )
        configdatafile.memexp = memexp

        self.discriminatorPlots = configdatafile.getDiscriminatorPlots(self.Data, self.analysis.discrName)
        self.evtYieldCategories = configdatafile.evtYieldCategories()


    def getDiscriminatorPlots(self):
        return self.discriminatorPlots

    def getBinlabels(self):
        return self.Data.categories.keys()

    def getVariablelabels(self):
        return self.Data.datavariables

    def getAddVariables(self):
        sys.path.append(self.cfgdir)
        fileName = self.variable_config
        print("getting additional variables from "+str(fileName))
        addVarModule = importlib.import_module( fileName )
        self.addVars = addVarModule.getAddVars()

    def getSystSamples(self):
        systSamples = []

        # adding other samples
        for sample in self.samples:
            variationsysts=self.systematics.get_variation_systs(sample.nick)
            for sysName in variationsysts:
                newSel = sample.selection
                fileName=self.systematics.processes[sample.nick][sysName].expression
                if "/" in fileName:
                    newpath=fileName
                else:
                    newpath=sample.path.replace("nominal",fileName)
                #not enough samples ind hdamp up
                if "HDAMP" in sysName and sysName.endswith("Up"):
                    newSel += "*((N_GenTopHad==1 && N_GenTopLep==1)* %s + !(N_GenTopHad==1 && N_GenTopLep ==1)*1)" %str(round(1.0399, 2))

                systSamples.append( 
                    plotClasses.Sample( 
                        sample.name+sysName, 
                        sample.color, 
                        newpath, 
                        newSel, 
                        sample.nick+sysName, 
                        samDict = self.pltcfg.sampleDict ))

        return systSamples


    def initSamples(self):
        # TODO: find a better naming sceme for the lists of samples/names/weights
        # they are used at many different places and it is not at all obvious which are used where and what they really contain

        # list of samples
        self.samples = self.pltcfg.samples
        # debug printout
        print("-"*30+"\nsamples:")
        for sample in self.samples:
            print(sample.name)
        print("-"*30)        


        # list of controlsamples used in 'allSamples' list
        self.controlSamples = self.pltcfg.samplesDataControlPlots
        # debug printout
        print("-"*30+"\ncontrol samples:")
        for sample in self.controlSamples:
            print(sample.name)
        print("-"*30) 
        print self.systematics

        print "systSamples"
        # list of systematic samples used in 'allSamples' and 'allSystSamples' list
        self.systSamples = self.getSystSamples()

        
        print "allSamples"
        # list of samples used to write C program       
        self.allSamples = self.pltcfg.samples+self.controlSamples+self.getSystSamples()
        # TODO is this used anywhere?
        #self.allSystSamples = samples + systSamples

        print "all syst names"
        # list of samples used e.g. in renameHistos       
        self.allSystNames = self.systematics.get_all_weight_systs()+self.systematics.get_all_variation_systs()
        # list of syst names used in plotParallel
        self.weightSystNames = self.systematics.get_all_weight_systs()
        self.weightSystNames.insert(0,"")
        # list of syst names used in plotParallel
        self.otherSystNames = self.systematics.get_all_variation_systs()

        # list of syst weights used in plotParallel
        self.systWeights = self.systematics.get_all_weight_expressions()
        self.systWeights.insert(0,self.pltcfg.nominalweight)

    def getEventYieldCategories(self):
        return self.evtYieldCategories

