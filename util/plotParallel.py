# comment 
import sys
import os
import subprocess
import time
import datetime
import stat
import ROOT
import variablebox
import plotutils
import PDFutils
import glob
import json
import filecmp
import imp 
import types
import csv
import runTimer
import scriptfunctions 
import nafSubmit

###########################
#                         #
# S C R I P T W R I T E R #
#                         #
###########################
class scriptWriter:
    def __init__(self, plotParaClass):
        # inheriting all public functions/varaibles from plotParallel class
        #self = plotParaClass
        self.pp = plotParaClass
        self.ccPath = plotParaClass.ccPath

    ## main function for writing and compiling c++ code ###########################################
    def writeCC(self):
        print("#"*50)
        print("starting to write and compile c++ code")
        print("c++ path is "+self.ccPath)
        print("#"*50)
        ccExists = os.path.exists(self.ccPath)
        if ccExists:
            print("c++ file already exists - check if this needs to be updated.")
            cmd = "cp -v "+self.ccPath+" "+self.ccPath+"Backup"
            print("cmd: "+cmd)
            subprocess.call(cmd, shell = True)

        print("creating c++ programm")
        self.createProgram()
        
        # check if createProgram was succesfull
        if not os.path.exists(self.ccPath):
            print( "could not create c++ program - exiting" )
            sys.exit(-1)

        # check whether code differs from backup
        codeDiffers = True
        if ccExists:
            print( "comparing c++ codes ..." )
            codeDiffers = not filecmp.cmp(self.ccPath+"Backup", self.ccPath)
        if codeDiffers:
            print( "c++ codes differ" )
            print( "compiling c++ program" )
            # compiling programm
            self.compileProgram()
        else:
            print( "c++ program already existing !! check if this is reasonable" )
            cmd = "cp -v "+self.ccPath[:-3]+"Backup "+self.ccPath[:-3]
            subprocess.call(cmd, shell = True)
        
        # check if compiling was successful
        if not os.path.exists(self.ccPath[:-3]):
            print( "could not compile c++ program - exiting" )
            sys.exit(-1)
        print("#"*50)
        print(" done with writing and compiling c++ program")
        print("#"*50)

    # -- compiling programm -----------------------------------------------------------------------
    def compileProgram(self):
        p = subprocess.Popen(['root-config', '--cflags', '--libs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()

        # getting dnnfiles
        dnnfiles=[]
        for addCodeInt in self.pp.addInterfaces:
            if addCodeInt.usesPythonLibraries:
                ppyc = subprocess.Popen(['python-config', '--cflags'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                outpyc, errpyc = ppyc.communicate()
                ppyl = subprocess.Popen(['python-config', '--ldflags'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                outpyl, errpyl = ppyl.communicate()
                print "communicated"
                # get library path for python
                print "outpyc", outpyc
                pythonincludepath = outpyc.split(" ")[0]
                pythonlibrarypath = pythonincludepath.replace("-I","-L").replace("include/python2.7","lib")
                dnnfiles = outpyc[:-1].replace("\n"," ").split(' ')+[pythonlibrarypath]+outpyl[:-1].replace("\n"," ").split(' ')
                break
            
        for addCodeInt in self.pp.addInterfaces:
            if addCodeInt.includeString != "":
                dnnfiles += addCodeInt.includeString.split(" ")
            if addCodeInt.libraryString != "":
                dnnfiles += addCodeInt.libraryString.split(" ")
         
        print("dnnfiles:")     
        print dnnfiles
        
        lhapdf=[' `/cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/lhapdf/6.1.6-ikhhed2/bin/lhapdf-config --cflags --ldflags`']
        
        # getting databases
        memDBccfiles=[]
        if self.pp.useDataBases:
            memDBccfiles=glob.glob('/nfs/dust/cms/user/kelmorab/DataBaseCodeForScriptGenerator/MEMDataBaseSpring17/MEMDataBase/MEMDataBase/src/*.cc') 
            #TODO update the dataBases code

        # improve ram usage and reduce garbage of g++ compiler
        improveRAM = '--param ggc-min-expand=100 --param ggc-min-heapsize=2400000'
        # if python cflags are used -O3 optimization is set, resulting in long compilation times, set it back to default -O0
        resetCompilerOpt = '-O0'

        print("creating compile command")
        cmd= ['g++']+[improveRAM]+out[:-1].replace("\n"," ").split(' ')+dnnfiles+lhapdf+['-lTMVA']+memDBccfiles+[resetCompilerOpt]+[self.ccPath,'-o',self.ccPath.replace(".cc","")]
        print "compile command:"
        cmdstring = " ".join(cmd)
        print cmdstring
        
        cmdPath = self.ccPath.replace(".cc","_gccCommand.txt")
        print("writing compile command to "+cmdPath)

        with open(cmdPath,"w") as cmdf:
            cmdf.write(cmdstring+"\n")
        
        print("trying to compile - output would be "+self.ccPath.replace(".cc",""))
        try:
            print subprocess.check_output([cmdstring],stderr=subprocess.STDOUT,shell=True)
        except subprocess.CalledProcessError, e:
            print "Compile command:\n", e.cmd
            print "Compile failed with error:\n", e.output

    # -- creating programm --------------------------------------------------------------------
    def createProgram(self):
        # generate a vetolist for variables that should not be generated automatically
        self.genVetolist()
        
        # get tree for variable check
        tree = ROOT.TTree()
        for i in range(len(self.pp.samplesData.allSamples)):
            thistreeisgood = False
            for j in range(len(self.pp.samplesData.allSamples[i].files)):
                f = ROOT.TFile(self.pp.samplesData.allSamples[i].files[j])
                tree = f.Get('MVATree')
                if tree.GetEntries() > 0:
                    print 'using',self.pp.samplesData.allSamples[i].files[j],'to determine variable types'
                    thistreeisgood = True
                    break
            if thistreeisgood:
                break

        # initialize variables with variablebox
        self.initVariables(tree)
        
        # write program
        # start writing program
        script = scriptfunctions.getHead(self.pp.plotbase, self.pp.dataBases,self.pp.addInterfaces)

        if self.pp.MEPDFCSVFile!="":
            script += PDFutils.DeclareMEPDFNormFactors(self.pp.MEPDFCSVFile)
            script += PDFutils.AddMEandPDFNormalizationsMap(self.pp.MEPDFCSVFile)
        
        for db in self.pp.dataBases:
            script += scriptfunctions.InitDataBase(db)
        for addCodeInt in self.pp.addInterfaces:
            script += addCodeInt.getBeforeLoopLines()
            
        # initialize all variables
        initStub, castStub = self.variables.initVarsProgram()
        script += initStub
        script += self.variables.initBranchAddressesProgram()

        # initialize TMVA Readers
        script += self.variables.setupTMVAReadersProgram()

        # initialize histograms in all categories and for all systematics
        script += scriptfunctions.initHistos(self.pp.categoryNames, self.pp.systNames, self.pp.configData.getDiscriminatorPlots())

        # start event loop
        script += PDFutils.DefineLHAPDF()
        startLoopStub = scriptfunctions.startLoop(self.pp.plotbase)

        if castStub!="":
            startLoopStub = startLoopStub.replace("//PLACEHOLDERFORCASTLINES", castStub)
        script += startLoopStub
        script += self.initLoop()

        # plotting
        script += self.eventLoop(tree)

        script+="     totalTimeFillHistograms+=timerFillHistograms->RealTime();\n"
        # finish loop
        script+=scriptfunctions.endLoop()
        
        for addCodeInt in self.pp.addInterfaces:
            script+="\n"
            script+=addCodeInt.getTestCallLines()
            script+="\n"
        
        # get program footer
        script += scriptfunctions.getFoot(self.pp.addInterfaces)

        # write program text to file
        with open(self.ccPath ,'w') as scriptf:
            scriptf.write(script)
        print(self.ccPath + " written")

    # -- utilities for creating the programm ------------------------------------------------------
    def genVetolist(self):
        # collect variables
        # list varibles that should not be written to the program automatically
        vetolist = ['processname', 'DoWeights', 'TMath', 'electronPt', 'electronEta', 'muonPt', 
                    'muonEta', 'muonTriggerHelper', 'electronTriggerHelper', 'hasTrigger', 
                    'internalCSVweight', 'internalCSVweight_CSVHFUp', 'internalCSVweight_CSVHFDown', 
                    'internalCSVweight_CSVLFUp', 'internalCSVweight_CSVLFDown', 
                    'internalCSVweight_CSVLFStats1Up', 'internalCSVweight_CSVLFStats1Down',
                    'internalCSVweight_CSVLFStats2Up', 'internalCSVweight_CSVLFStats2Down', 
                    'internalCSVweight_CSVHFStats1Up', 'internalCSVweight_CSVHFStats1Down', 
                    'internalCSVweight_CSVHFStats2Up', 'internalCSVweight_CSVHFStats2Down',
                    'internalCSVweight_CSVCErr1Up', 'internalCSVweight_CSVCErr1Down', 
                    'internalCSVweight_CSVCErr2Up', 'internalCSVweight_CSVCErr2Down',
                    "internalEleTriggerWeight", "internalEleTriggerWeightUp", "internalEleTriggerWeightDown",
                    "internalEleIDWeight", "internalEleIDWeightUp", "internalEleIDWeightDown",
                    "internalEleIsoWeight", "internalEleIsoWeightUp", "internalEleIsoWeightDown",
                    "internalEleGFSWeight", "internalEleGFSWeightUp", "internalEleGFSWeightDown",
                    "internalMuTriggerWeight", "internalMuTriggerWeightUp", "internalMuTriggerWeightDown",
                    "internalMuIDWeight", "internalMuIDWeightUp", "internalMuIDWeightDown",
                    "internalMuIsoWeight", "internalMuIsoWeightUp", "internalMuIsoWeightDown",
                    "internalMuHIPWeight", "internalMuHIPWeightUp", "internalMuHIPWeightDown",
                    "internalQCDweight", "internalQCDweightup", "internalQCDweightdown",
                    "electron_data", "muon_data",
                    "internalPDFweightUp", "internalPDFweightDown", "internalPDFweight",
                    "internalISRweightdown", "internalISRweightup", "internalFSRweightdown", "internalFSRweightup",
                    "internalHDAMPweightdown", "internalHDAMPweightup", "internalUEweightdown", "internalUEweightup"]

        #self.pp.MEPDFCSVFile = self.pp.plotbase + /txtfiles/rate_factors_onlyinternal_powhegpythia.csv
        if self.pp.MEPDFCSVFile!="":
            vetolist += PDFutils.GetMEPDFVetoList(self.pp.MEPDFCSVFile)

        for addCodeInt in self.pp.addInterfaces:
            vetolist += addCodeInt.getExternalyCallableVariables()
            
        for db in self.pp.dataBases:
            vetolist.append(db[0]+"p")
            vetolist.append(db[0]+"p_sig")
            vetolist.append(db[0]+"p_bkg")
            vetolist.append(db[0]+"p_err_sig")
            vetolist.append(db[0]+"p_err_bkg")
            vetolist.append(db[0]+"n_perm_sig")
            vetolist.append(db[0]+"n_perm_bkg")
            vetolist.append(db[0]+"FoundResult")
                
        self.vetolist = vetolist

    def initVariables(self, tree):
        # initialize variables object
        variables = variablebox.Variables(self.vetolist)
        
        # get standard variables
        standardvars = ['Weight','Weight_CSV','Weight_XS']
        variables.initVarsFromExprList(standardvars, tree)

        # get additional variables
        if len(self.pp.configData.addVars) > 0:
            variables.initVarsFromExprList(self.pp.configData.addVars, tree)

        # get systematic weight variables
        variables.initVarsFromExprList(self.pp.systWeights, tree)

        systWeights = []
        for systweight in self.pp.systWeights:
            if ":=" in systweight:
                    systWeights.append(systweight.split(":=")[0])
            else:
                    systWeights.append(systweight)
        self.pp.systWeights = systWeights

        # get sample selection variables
        for sample in self.pp.samplesData.allSamples:
            variables.initVarsFromExpr(sample.selection, tree)

        # get category selection variables
        variables.initVarsFromExprList(self.pp.categorySelections, tree)

        # get variables used in plots
        for plot in self.pp.configData.getDiscriminatorPlots():
            if isinstance(plot, plotutils.Plot):
                variables.initVarsFromExpr(plot.variable, tree)
            if isinstance(plot, plotutils.TwoDimPlot):
                variables.initVarsFromExpr(plot.variable1, tree)
                variables.initVarsFromExpr(plot.variable2, tree)

            variables.initVarsFromExpr(plot.selection, tree)

        self.variables = variables
        print "knie"
        print tree
        print type(tree)
        
    def initLoop(self):
        script = ""
        script += "     timerMapping->Start();\n"
        if self.pp.MEPDFCSVFile!="":
            script+=PDFutils.ResetMEPDFNormFactors(self.pp.MEPDFCSVFile)
            script+=PDFutils.RelateMEPDFMapToNormFactor(self.pp.MEPDFCSVFile)
            script+=PDFutils.PutPDFWeightsinVector(self.pp.MEPDFCSVFile)
            script+=PDFutils.UseLHAPDF()
        script+="     totalTimeMapping+=timerMapping->RealTime();\n"

        script+="     timerEvalDNN->Start();\n"
        for addCodeInt in self.pp.addInterfaces:
            script+=addCodeInt.getVariableInitInsideEventLoopLines()
        script+="     totalTimeEvalDNN+=timerEvalDNN->RealTime();\n"

        script+="     timerSampleWeight->Start();\n"
        script+='        float sampleweight=1;\n'
        script+=scriptfunctions.encodeSampleSelection(self.pp.samplesData.allSamples, self.variables)
        script+="     totalTimeSampleWeight+=timerSampleWeight->RealTime();\n"
        
        script+="     timerReadDataBase->Start();\n"
        for db in self.pp.dataBases:
            script+=scriptfunctions.readOutDataBase(db)    
        script+="\n"
        script+="     totalTimeReadDataBase+=timerReadDataBase->RealTime();\n"
        
        script+="     timerEvalDNN->Start();\n"
        for addCodeInt in self.pp.addInterfaces:
            script+=addCodeInt.getEventLoopCodeLines()
            script+="\n"
        script+="     totalTimeEvalDNN+=timerEvalDNN->RealTime();\n"

        script+="     timerEvalWeightsAndBDT->Start();\n"
        # calculate varibles and get TMVA outputs
        script+=self.variables.calculateVarsProgram()
        print("done")
        script+="     totalTimeEvalWeightsAndBDT+=timerEvalWeightsAndBDT->RealTime();\n"
        
        script+="     timerFillHistograms->Start();\n"

        return script

    def eventLoop(self, tree):
        script = ""
        # this class temporary saves variables, systNames and systWeights
        # this way these havent got to be given as arguments for every plot initiated
        plotClass = scriptfunctions.initPlots(self.variables, self.pp.systNames, self.pp.systWeights)
        
        for catname, catselection in zip(self.pp.categoryNames,self.pp.categorySelections):
            # for every category
            script += plotClass.startCat(catselection)
            # plot everything
            # plot one dimensional plot
            for plot in self.pp.configData.getDiscriminatorPlots():
                if isinstance(plot, plotutils.Plot):
                    script += plotClass.initOneDimPlot(plot, tree, catname)
            # plot two dimensional self.configData.getDiscriminatorPlots()
            for plot in self.pp.configData.getDiscriminatorPlots():
                if isinstance(plot,plotutils.TwoDimPlot):
                    script += plotClass.initTwoDimPlot(plot, catname)
            # finish category
            script += plotClass.endCat()

        return script

    ## script for renaming ########################################################################
    def writeRenameScript(self):
        script = "import ROOT\n"
        script += "import sys\n"
        script += "import os\n"
        script += "from subprocess import call\n"
        script += "filename=os.getenv('OUTFILENAME')\n\n"

        script += "systematics="+str(self.pp.samplesData.allNames)+"\n"

        with open(self.pp.plotbase+"/txtfiles/renameBody", "r") as f:
            body = f.read()

        script += body
  
        with open(self.ccPath.replace(".cc","_rename.py"), "w") as srcfile:
            srcfile.write(script)

    ## functions for writing run code #############################################################
    def writeRunScripts(self):
        # init outputs
        scripts=[]
        outputs=[]
        nentries=[]
        samplewiseMaps={}

        # loading tree info from json file
        SaveTreeInforamtion={}
        LoadedTreeInformation={}
        if self.pp.jsonFile != "":
            print "Loading file with tree event information"
            with open(self.pp.jsonFile,"r") as jsonfile:
                jsonstring = list(jsonfile)[0]
                LoadedTreeInformation = json.loads(jsonstring)
    
        # looping over samples
        for sample in self.pp.samplesData.allSamples:
            print 'creating scripts for',sample.name,'from',sample.path
            samplewiseMaps[sample.nick] = []
            ntotal_events = 0
            njob = 0
            events_in_files = 0
            filterFile = sample.filterFile
            files_to_submit = []
            # looping over files in sample
            for filename in sample.files:
                events_in_file = 0

                if LoadedTreeInformation != {} and filename in LoadedTreeInformation:
                    events_in_file = LoadedTreeInformation[filename]
                else:
                    f = ROOT.TFile(filename)
                    tree = f.Get('MVATree')
                    events_in_file = tree.GetEntries()

                SaveTreeInforamtion[filename] = events_in_file

                # if the file is larger than self.maxevents it is analyzed in portions of nevents
                if events_in_file > self.pp.maxevents:
                    for ijob in range(events_in_file / self.pp.maxevents + 1):
                        njob += 1
                        skipevents = (ijob)*self.pp.maxevents
                        scriptname = self.pp.scriptsPath+'/'+sample.nick+'_'+str(njob)+'.sh'
                        processname = sample.nick
                        filenames = filename
                        outfilename = self.pp.plotPath+sample.nick+'_'+str(njob)+'.root'
                        processname = sample.nick
                        # creating script
                        self.CreateScript(scriptname, outfilename, filenames, processname, self.pp.maxevents, skipevents, filterFile)
                        
                        scripts.append(scriptname)
                        outputs.append(outfilename)
                        samplewiseMaps[sample.nick].append(outfilename)
                        nentries.append(events_in_file)
                        ntotal_events += events_in_file

                # else additional files are appended to list of files to be submitted
                else :
                    files_to_submit += [filename]
                    events_in_files += events_in_file
                    if events_in_files > self.pp.maxevents or filename == sample.files[-1] or len(files_to_submit)>400: 
                        njob += 1
                        skipevents = 0
                        scriptname = self.pp.scriptsPath+'/'+sample.nick+'_'+str(njob)+'.sh'
                        processname = sample.nick
                        filenames = ' '.join(files_to_submit)
                        outfilename = self.pp.plotPath+sample.nick+'_'+str(njob)+'.root'
                        # creating script
                        self.writeSingleScript(scriptname, outfilename, filenames, processname, events_in_files, skipevents, filterFile)

                        scripts.append(scriptname)
                        outputs.append(outfilename)
                        samplewiseMaps[sample.nick].append(outfilename)
                        nentries.append(events_in_files)
                        ntotal_events += events_in_files
                        files_to_submit = []
                        events_in_files = 0
                        
                # If self.options["cirun"] = true, only use small number of files             
                if self.pp.options["cirun"]: 
                    break

            # submit remaining scripts (can happen if the last file was large)
            if len(files_to_submit) > 0:
                njob += 1
                skipevents = 0
                scriptname = self.pp.scriptsPath+'/'+sample.nick+'_'+str(njob)+'.sh'
                processname = sample.nick
                filenames = ' '.join(files_to_submit)
                outfilename = self.pp.plotPath+sample.nick+'_'+str(njob)+'.root'
                # creating script
                self.writeSingleScript(scriptname, outfilename, filename, processname, events_in_files, skipevents, filterFile)
                
                scripts.append(scriptname)
                outputs.append(outfilename)
                samplewiseMaps[sample.nick].append(outfilename)
                nentries.append(events_in_files)
                ntotal_events += events_in_files
                files_to_submit = []
                events_in_files=0

            print ntotal_events, 'events found in', sample.name
        
        # save tree information to json file
        treejson = json.dumps(SaveTreeInforamtion)
        with open(self.pp.workdir+'/'+"treejson.json","w") as jsonfile:
            jsonfile.write(treejson)

        print "Saved information about events in trees to ", self.pp.workdir+'/'+"treejson.json"
        return scripts, outputs, nentries, samplewiseMaps

    def writeSingleScript(self, scriptname, outfilename, filenames, processname, maxevents, skipevents, filterFile = "", suffix = ""):
        if self.pp.options["cirun"] and maxevents < 100:
            maxevents = 100

        script = "#!/bin/bash \n"
        if self.pp.cmsswpath != '':
            script += "export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch \n"
            script += "source $VO_CMS_SW_DIR/cmsset_default.sh \n"
            script += "export SCRAM_ARCH="+os.environ['SCRAM_ARCH']+"\n"
            script += 'cd '+self.pp.cmsswpath+'/src\n'
            script += 'eval `scram runtime -sh`\n'
            script += 'cd - \n'
        script += 'export PROCESSNAME="'+processname+'"\n'
        script += 'export FILENAMES="'+filenames+'"\n'
        script += 'export OUTFILENAME="'+outfilename+'"\n'
        script += 'export MAXEVENTS="'+str(maxevents)+'"\n'
        script += 'export SKIPEVENTS="'+str(skipevents)+'"\n'
        script += 'export SUFFIX="'+suffix+'"\n'
        script += 'export EVENTFILTERFILE="'+str(filterFile)+'"\n'
        script += self.ccPath[:-3]+'\n'
        #DANGERZONE
        script += 'python '+self.ccPath.replace('.cc','_rename.py')+'\n'
        
        with open(scriptname, "w") as f:
            f.write(script)
        st = os.stat(scriptname)
        os.chmod(scriptname, st.st_mode | stat.S_IEXEC)
    
    ## function for writing hadd parallel code #################################################### 
    def writeHaddScript(self):
        # creating haddScript
        script = "import ROOT\n"
        script+= "import sys\n"
        script+= "import os\n"
        script+= "import subprocess\n" 
        script+= "outfname=sys.argv[1]\n"
        script+= "outlogname=sys.argv[2]\n"
        script+= "infiles=sys.argv[3:]\n"
        script+= "cmd='hadd '+outfname+' '+' '.join(infiles)\n"
        script+= "worked=False\n"
        script+= "try:\n"
        script+= "\tsubprocess.check_output(cmd,shell=True,stderr=subprocess.STDOUT)\n"
        script+= "\tworked=True\n"
        script+= "except subprocess.CalledProcessError, e:\n"
        script+= "\tworked=False\n"
        script+= "outlog=open(outlogname,'w')\n"
        script+= "if worked:\n"
        script+= "\toutlog.write('OK')\n"
        script+= "else:\n"
        script+= "\toutlog.write('ERROR')\n"
        script+= "outlog.close()\n"

        # saving hadd script
        self.haddScript = self.pp.workdir+'/haddScript.py'
        with open(self.haddScript, "w") as sf:
            sf.write(script)
        print("haddScript written to "+self.haddScript)


    def writeHaddShell(self, scriptname, haddedRootName, haddedLogName, sampleData):
        script = "#!/bin/bash \n"
        if self.pp.cmsswpath!='':
            script += "export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch \n"
            script += "source $VO_CMS_SW_DIR/cmsset_default.sh \n"
            script += "export SCRAM_ARCH="+os.environ['SCRAM_ARCH']+"\n"
            script += 'cd '+self.pp.cmsswpath+'/src\neval `scram runtime -sh`\n'
            script += 'cd - \n'
        script += 'python '+self.haddScript+' '+haddedRootName+' '
        script += haddedLogName+' '+' '.join(sampleData)+'\n'

        # saving shell script
        with open(scriptname, "w") as f:
            f.write(script)

        # chmodding shell script
        st = os.stat(scriptname)
        os.chmod(scriptname, st.st_mode | stat.S_IEXEC)

###################################################################################################








###########################
#                         #
# P L O T P A R A L L E L #
#                         #
###########################
class plotParallel:
    def __init__(self, workdir, pltcfg, configData, samplesData):
        self.workdir = workdir
        # get pyroot-plotscript directory
        self.plotbase = self.workdir.split("/")
        while not self.plotbase[-1] == "pyroot-plotscripts":
            self.plotbase.pop(-1)
        self.plotbase = "/".join(self.plotbase)

        if pltcfg and configData and samplesData:
            self.rootPath = self.workdir + "/output.root"
            self.analysisName = self.workdir.split("/")[-1]

            self.maxevents = 5000000
            self.configData = configData
            self.samplesData = samplesData
            self.pltcfg = pltcfg

            self.finished = False
            self.haddFiles = None

            # defaults
            self.categoryNames = [""]
            self.categorySelections = ["1."]        
            
            self.systNames = self.pltcfg.weightSystNames
            self.systWeights = self.pltcfg.systWeights

            self.jsonFile = ""
            self.dataBases = []
            self.useDataBases = False
            self.addInterfaces = []
            self.MEPDFCSVFile = ""
            
            self.options = {"cirun": False,
                            "stopAfterCompile": False,
                            "haddParallel": False,
                            "useOldRoot": False}
            
            ## check cmssw
            self.cmsswpath = os.environ['CMSSW_BASE']
            if not "CMSSW" in self.cmsswpath:
                print "you need CMSSW for this to work. Exiting!"
                exit(0)
            self.cmsswversion = os.environ['CMSSW_VERSION']

    # emptyclass ----------------------------------------------------------------------------------
    @classmethod
    def empty(cls, workdir, rootFilePath):
        emptycls = plotParallel(workdir,None,None,None)
        emptycls.setEmptyValues(rootFilePath)
        return emptycls

    def setEmptyValues(self, path):
        outPath = path.replace("_limitInput","")
        if not os.path.exists(path):
            self.limitPath = workdir + "/output.root"
        else:
            self.limitPath = path
        self.finished = True

        print("initialized empty plotParallel with limitPath set to: "+str(self.limitPath))
    # ---------------------------------------------------------------------------------------------


    ## setters ####################################################################################
    def setCatnames(self, categoryNames):
        self.categoryNames = categoryNames

    def setCatSelections(self, categorySelections):
        self.categorySelections = categorySelections

    def setSystNames(self, systNames):
        self.systNames = systNames
    
    def setSystWeights(self, systWeights):
        self.systWeights = systWeights

    def setJson(self, jsonFile):
        self.jsonFile = jsonFile

    def setDataBases(self, dataBases):
        self.dataBases = dataBases
        if self.dataBases != []:
            self.useDataBases = True

    def setAddInterfaces(self, interfaces):
        interfaceCounter = 0
        for interface in interfaces:
            interfaceCounter += 1
            if isinstance( interface, basestring ):
                addModule = "addModule" + str(interfaceCounter)
                print( "loading module: " + str(interface) + " as " + addModule + " module." )
                self.addInterfaces.append( imp.load_source(addModule, interface).theInterface())
            elif isinstance( interface, types.InstanceType ):
                print( "appending class object initiated by user: " + str(interface) )
                self.addInterfaces.append(interface)
            else:
                print( "unknown additional code interface type: " + str(interface) )
        
    def setMEPDFCSV(self, csvfile):
        self.MEPDFCSVFile = csvfile
        
    def setMaxEvts(self, maxevts):
        self.maxevents = maxevts

    def setOptions(self, opts):
        for opt in opts:
            if opt in self.options:
                self.options[opt] = opts[opt]
                print( str(opt) + " set to " + str(opts[opt]))
    ## end setters ################################################################################
    ## getters ####################################################################################

    def getRootPath(self):
        if self.finished:
            return self.rootPath
        else:
            print("plotParallel.run() has not terminated successfully")
            print("                or has not been called yet -- exiting")
            sys.exit()

    def getHaddOutPath(self):
        return self.workdir+"/HaddOutputs/*.root"
    
    def getHaddFiles(self):
        return self.haddFiles

    def getLimitPath(self):
        return self.limitPath
    
    ## end getters ################################################################################
    ## public functions ###########################################################################

    def checkTermination(self):
        if self.finished:
            print("plotParallel was finished successfully")
            return True
        else:
            print("plotParallel was not finished successfully or has not been run at all - exiting")
            sys.exit(-1)

    def checkHaddFiles(self):
        if self.haddFiles:
            return True
        else:
            return False

    def initlimitPath_exists(self):
        self.limitPath = self.rootPath.replace(".root","_limitInput.root")
        return os.path.exists(self.limitPath)
    
    ## end public functions #######################################################################
    ## private functions ##########################################################################

    def globHaddFiles(self):
        allFiles = glob.glob(self.getHaddOutPath())
        allFiles = [f for f in allFiles if not "_renamed_" in f]
        return allFiles

    ## NAF submit interface for parallel plotting #################################################
    def plotSubmitInterface(self, scripts, outputs, nEntries):
        # submit run scripts
        print 'submitting scripts'
        submitOptions = {"PeriodicHold": 1500}
        jobIDs = nafSubmit.submitArrayToNAF(scripts, "PlotPara", submitOptions = submitOptions)
        # monitoring running of jobs
        nafSubmit.do_qstat(jobIDs)

        # checking outputs
        print 'checking outputs'
        failedJobs = self.plotCheckJobs(scripts,outputs,nEntries)
        retries=0
        maxRetries = 10
        while retries <= maxRetries and len(failedJobs)>0:
            retries+=1
            print 'the following jobs failed'
            for job in failedJobs:
                print job
            if len(failedJobs)>=0.6*len(scripts):
                print( "!"*50 )
                print( "! more than 60 percent of your jobs failed. check: ")
                print( "\tA) code and logfiles" )
                print( "\tB) status of batch system" )
            print 'resubmitting as single jobs'
            jobIDs = nafSubmit.submitToNAF(failedJobs, submitOptions = submitOptions)
            nafSubmit.do_qstat(jobIDs)
            failedJobs = self.plotCheckJobs(scripts,outputs,nEntries)
            if retries>=maxRetries:
                sys.exit("submission of jobs was not success full after multiple tries - exiting")
    
    def plotCheckJobs(self,scripts,outputs,nEntries):
        print("-"*50)
        print("checking job output after plotpara")
        failedJobs=[]
        noCutflow = 0
        wrongEntry = 0
        for script,o,n in zip(scripts,outputs,nEntries):
            if not os.path.exists(o+'.cutflow.txt'):
                failedJobs.append(script)
                noCutflow += 1
                continue
            f=open(o+'.cutflow.txt')
            processed_entries=-1
            for line in f:
                s=line.split(' : ')
                if len(s)>2 and 'all' in s[1]:
                    processed_entries=int(s[2])
                    break
            if not n == processed_entries:
                failedJobs.append(script)
                wrongEntry += 1
        print("done checking job outputs after plotpara - results:")
        print("jobs without cutflow file: " + str(noCutflow))
        print("jobs with wrong entry in cutflow file: " + str(wrongEntry))
        print("-"*50)
        return failedJobs


    ## main function of plot parallel #############################################################
    def run(self):
        # check whether to use the already existing root file
        if os.path.exists(self.rootPath):
            if self.options["useOldRoot"]:
                if not self.options["haddParallel"]:
                    print("old root file found && no parallel hadding")
                    print("using old root file")
                    self.finished = True
                    return
                else:
                    print("old root file found && parallel hadding activated")
                    print("using old root file and saving haddFiles")
                    self.haddFiles = self.globHaddFiles()
                    print("type of haddFiles: " + str(type(self.haddFiles)) )
                    self.finished = True
                    return
                    
        # moving the old instance of workdir to a backup and copying C-file
        if os.path.exists(self.rootPath):
            oldWorkdir = self.workdir+datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            os.rename(self.workdir, oldWorkdir)
            os.makedirs(self.workdir)

            cmd = "cp -v "+oldWorkdir+"/"+self.analysisName+".cc "+self.workdir+"/"+self.analysisName+".cc"
            subprocess.call(cmd, shell = True)
            cmd = "cp -v "+oldWorkdir+"/"+self.analysisName+" "+self.workdir+"/"+self.analysisName+"Backup"
            subprocess.call(cmd, shell = True)
        elif not os.path.exists(self.workdir):
            os.makedirs(self.workdir)

        # creating c++ programm
        self.ccPath = self.workdir + "/" + self.analysisName + ".cc"
        writer = scriptWriter(self)
        writer.writeCC()

        # create rename script
        # TODO look at rename script code and maybe also move to class
        writer.writeRenameScript()

        # creating output folders
        print( "creating output folders" )
        self.scriptsPath = self.workdir + "/scripts/"
        self.plotPath = self.workdir + "/plots/"
        if not os.path.exists(self.scriptsPath):
            os.makedirs(self.scriptsPath)
        if not os.path.exists(self.plotPath):
            os.makedirs(self.plotPath)

        # creating run script
        print( "creating run scripts" )
        # tuple consists of (scripts, outputs, nentries, samplewiseMaps)
        self.runscriptTuple = writer.writeRunScripts()

        # check if we should stop
        if self.options["stopAfterCompile"]:
            print( "compiling is done and stopAfterCompile option is activated - exiting" )
            self.finished = True
            sys.exit(0)

        # job submission
        self.plotSubmitInterface(*self.runscriptTuple[:-1])
        print("all jobs have terminated successfully")
        print("="*40)
        print("now we can start the hadd output")

        # starting on hadd output
        with runTimer.Timer("haddoutput"):
            hP = haddParallel(self)
            self.haddFiles = hP.run(writer)
            print("type of haddFiles: " + str(type(self.haddFiles)) )
            self.finished = True
            return 
        
        # if we get here, something unexpected went wrong
        self.finished = False
        return -1
    

###########################
#                         #
# H A D D P A R A L L E L #
#                         #
###########################
class haddParallel:
    def __init__(self, plotParaClass):
        self.inputmap = plotParaClass.runscriptTuple[-1]
        self.outputs = plotParaClass.runscriptTuple[1]
        self.haddParallel = plotParaClass.options["haddParallel"]    
        self.workdir = plotParaClass.workdir
        self.rootPath = plotParaClass.rootPath
        
    ## NAF submit interface for parallel hadding ##################################################
    def haddSubmitInterface(self, listOfOutScripts, listOfOutFiles):
        firstTry = True
        nJobsDone = 0
        nTries = 0

        jobsToSubmit = listOfOutScripts
        outfilesFromSubmit = listOfOutFiles
        
        while len(jobsToSubmit) > 0 or len(outfilesFromSubmit) > 0 or nJobsDone != len(listOfOutFiles):
            nTries += 1
            if nTries >= 10:
                print("hadding did not work after 5 tries. ABORTING")
                exit(1)
            if firstTry:
                print("submitting haddParallel scripts")
                jobids = nafSubmit.submitArrayToNAF(jobsToSubmit, "haddPara")
                nafSubmit.do_qstat(jobids)
                firstTry = False            
            else:
                print("hadding did not work the last time - resubmitting as single scripts")
                jobids = nafSubmit.submitToNAF(jobsToSubmit)
                nafSubmit.do_qstat(jobids)
            
            # check if each hadd worked
            jobsToSubmit, outfilesFromSubmit, nJobsDone = self.haddCheckJobs(listOfOutScripts, listOfOutFiles)

    def haddCheckJobs(self, listOfOutScripts, listOfOutFiles):
        jobsToSubmit = []
        outfilesFromSubmit = []
        nJobsDone = 0

        noFile = 0
        wrongEntry = 0
        wrongLen = 0
        for job, jobscript in zip(listOfOutFiles,listOfOutScripts):
            isOk = True
            log = job.replace(".root", ".log")
            if os.path.exists(job) and os.path.exists(log):
                with open(log, "r") as logf:
                    jobfile = list(logf)
                if len(jobfile) == 1:
                    if jobfile[0] != "OK":
                        isOk = False
                        wrongEntry += 1
                else:
                    isOk = False
                    wrongLen += 1
            else:
                isOk = False
                noFile += 1

            if isOk:
                nJobsDone += 1
            else:
                jobsToSubmit.append(jobscript)
                outfilesFromSubmit.append(job)

        print("done checking job outputs after haddpara - results:")
        print("jobs without log file: " + str(noFile))
        print("jobs with wrong log file: " +str(wrongLen))
        print("jobs with ERROR in log file: " + str(wrongEntry))
        print("-"*50)
        return jobsToSubmit, outfilesFromSubmit, nJobsDone

    def addHaddFiles(self):
        files = [self.rootPath]
        if self.haddFiles:
            files.extend(self.haddFiles)
        return files

    ## main function for parallel hadding  #########################################################
    def run(self, writer):
        if not self.haddParallel:
            print("not doing parallel hadding ...")
            try:
                rootFiles = self.addHaddFiles()
                subprocess.check_output( ["hadd", rootFiles] + self.outputs,
                                            stderr = subprocess.STDOUT )
            except subprocess.CalledProcessorError, e:
                print( "hadd failed with the following error:")
                print( e.output)
                sys.exit(-1)

            print("hadd output worked")
            return rootFiles

        # doing the actual harallel histogram adding
        writer.writeHaddScript()

        # initializing lists
        listOfOutScripts = []
        listOfOutFiles = []

        # initializing folder        
        self.haddScriptFolder = self.workdir+'/HaddScripts/'
        self.haddOutputFolder = self.workdir+'/HaddOutputs/'
        if not os.path.exists(self.haddScriptFolder):
            os.makedirs(self.haddScriptFolder)
        if not os.path.exists(self.haddOutputFolder):
            os.makedirs(self.haddOutputFolder)

        print("looping over samples in samplewiseMaps")
        for sample in self.inputmap:
            print sample
            
            # writing shell script
            scriptname = self.haddScriptFolder+'haddscript_'+sample+'.sh'
            haddedRootName = self.haddOutputFolder+'/'+sample+'_hadded.root'
            haddedLogName = self.haddOutputFolder+'/'+sample+'_hadded.log'
            writer.writeHaddShell(scriptname, haddedRootName, haddedLogName, self.inputmap[sample])

            # add root names and shell names to lists
            listOfOutFiles.append(haddedRootName)
            listOfOutScripts.append(scriptname)
        
        # job submission
        self.haddSubmitInterface(listOfOutScripts, listOfOutFiles)
        print("all jobs have terminated successfully")
        print("="*40)

        return listOfOutFiles



# -------------------------------------------------------------------------------------------------
# to be sorted
# -------------------------------------------------------------------------------------------------
def haddFilesFromWildCard(outname="",inwildcard="",totalNumberOfHistosNeedsToRemainTheSame=False):
  infiles=glob.glob(inwildcard)
  print 'hadd from wildcard'
  print outname, inwildcard
  haddclock=ROOT.TStopwatch()
  haddclock.Start()
  nfilesPerHadd=50
  nHistosBefore=0
  nHistosAfter=0
  if totalNumberOfHistosNeedsToRemainTheSame:
    # count number if histos before hadding
    print "counting histos BEFORE hadding from wildcard"
    nHistos=0
    for inf in infiles:
      theInf=ROOT.TFile(inf,"READ")
      keylist=theInf.GetListOfKeys()
      nHistos+=len(keylist)
      theInf.Close()
    nHistosBefore=nHistos  
  if len(infiles)<nfilesPerHadd:
    cmd='hadd'+' '+outname+' '+' '.join(infiles)
    print "hadding "+"\n".join(infiles)
    print "outname: "+str(outname)
    subprocess.call(cmd,shell=True)
  else:
    parts=[]
    subpartfiles=[]
    totalsubpartfiles=[]
    for iinf, inf in enumerate(infiles):
      subpartfiles.append(inf)
      totalsubpartfiles.append(inf)
      if iinf%(nfilesPerHadd-1)==0 or inf==infiles[-1]:
        partname=outname.replace(".root","_part_"+str(len(parts))+".root")
        parts.append(partname)
        cmd='hadd'+' '+partname+' '+' '.join(subpartfiles)
        print "hadding "+"\n".join(subpartfiles)
        print "outname: "+str(partname)
        subprocess.call(cmd,shell=True)
        subpartfiles=[]
    if len(totalsubpartfiles)!=len(infiles):
      print "OHOHOH HADDINGFROMWILDCARD missed or used some files twice!!!"
      exit(1)
    # now add the parts
    print "-"*50+"\nsubfiles were hadded, now hadding the whole thing together\n"+"-"*50
    cmd='hadd'+' '+outname+' '+' '.join(parts)
    print "hadding "+"\n".join(parts)
    print "outname: "+str(outname)
    subprocess.call(cmd,shell=True)
  
  if totalNumberOfHistosNeedsToRemainTheSame:
    # count number if histos before hadding
    print "counting histos AFTER hadding from wildcard"
    nHistos=0
    for inf in [outname]:
      theInf=ROOT.TFile(inf,"READ")
      keylist=theInf.GetListOfKeys()
      nHistos+=len(keylist)
      theInf.Close()
    nHistosAfter=nHistos
    if nHistosAfter!=nHistosBefore:
      print "haddFilesFromWildCard did not lead to the same number of histograms before and after the hadding!!!!"
      exit(1)
  print 'done'
  haddtime=haddclock.RealTime()
  print "hadding took ", haddtime
  return  outname



def DrawParallel(ListOfPlots,workdir,PathToSelf,opts=None):
    ListofScripts=[]
    # create output folders
    print 'creating output folders'
    scriptsfolder=workdir+'/DrawScripts/'
    if not os.path.exists(scriptsfolder):
      os.makedirs(scriptsfolder)

    print "Creating Scripts for Parallel Drawing"
    for iPlot, Plot in enumerate(ListOfPlots):
        ListofScripts.append(createSingleDrawScript(iPlot,Plot,PathToSelf,scriptsfolder,opts=None))

    print "Submitting ", len(ListofScripts), " DrawScripts"
    # print ListofScripts
    # jobids=nafSubmit.submitToNAF(["DrawScripts/DrawParallel0.sh"])
    #jobids=nafSubmit.submitToNAF(ListofScripts)
    jobids=nafSubmit.submitArrayToNAF(ListofScripts,"DrawPara")
    print jobids
    nafSubmit.do_qstat(jobids)


def createSingleDrawScript(iPlot,Plot,PathToSelf,scriptsfolder,opts=None):
  # print "still needs to be implemented"
  cmsswpath=os.environ['CMSSW_BASE']
  script="#!/bin/bash \n"
  if cmsswpath!='':
    script+="export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch \n"
    script+="source $VO_CMS_SW_DIR/cmsset_default.sh \n"
    script+="export SCRAM_ARCH="+os.environ['SCRAM_ARCH']+"\n"
    script+='export OUTFILENAME="'+"plot" +str(iPlot)+'"\n'
    script+='cd '+cmsswpath+'/src\neval `scram runtime -sh`\n'
    script+='cd - \n'
  # Parse commandline options if available to script  
  commandLineOptions = ''
  if opts != None:
    for opt, arg in opts:
      if arg != None:
        commandLineOptions = commandLineOptions + ' ' + opt + '=' + arg
      else:
        commandLineOptions = commandLineOptions + ' ' + opt
  script+='python '+PathToSelf+" -p "+str(iPlot)+ ' ' + commandLineOptions + ' noPlotParallel\n'
  # script+="mv *.pdf " +os.getcwd()+"/plot"+str(iPlot)+".pdf\n"


  scriptname=scriptsfolder+'DrawParallel'+str(iPlot)+'.sh'

  # path = os.getcwd()+"/DrawScripts" 
  # if not os.path.exists(path):
  #   os.makedirs(path)
  # os.chdir(path)
  
  f=open(scriptname,'w')
  f.write(script)
  f.close()
  st = os.stat(scriptname)
  os.chmod(scriptname, st.st_mode | stat.S_IEXEC)
  os.chdir(os.path.dirname(PathToSelf))

  # PathToShellScript=path+scriptname
  # return PathToShellScript
  # return "DrawScripts/"+scriptname
  return scriptname




def askYesNo(question):
  print question
  yes = set(['yes','y', 'ye', ''])
  no = set(['no','n'])
  choice = raw_input().lower()
  if choice in yes:
    return True
  elif choice in no:
    return False
  else:
    print "Please respond with 'yes' or 'no'"
    return askYesNo(question)
