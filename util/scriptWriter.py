import sys
import os
import subprocess
import stat
import ROOT
import glob
import json
import filecmp

# local imports 
import variablebox
import plotutils
import scriptfunctions 

###########################
#                         #
# S C R I P T W R I T E R #
#        C L A S S        #
###########################
class scriptWriter:
    def __init__(self, plotParaClass):
        ''' default init
         inheriting all public functions/varaibles from plotParallel class '''
        self.pp = plotParaClass
        self.ccPath = plotParaClass.ccPath
        self.systWeights = plotParaClass.systWeights




    ## main function for writing and compiling c++ code ##
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
            print( "c++ program was not created successfully -- exiting" )
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





    ## creating programm ##
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
        script = scriptfunctions.getHead(self.pp.plotbase, self.pp.dataBases, self.pp.addInterfaces)

        if self.pp.MEPDFCSVFile!="":
            script += scriptfunctions.DeclareMEPDFNormFactors(self.pp.MEPDFCSVFile)
            script += scriptfunctions.AddMEandPDFNormalizationsMap(self.pp.MEPDFCSVFile)
        
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
        script += scriptfunctions.initHistos(self.pp.categoryNames, self.pp.systNames, 
                                        self.pp.configData.getDiscriminatorPlots())

        # start event loop
        script += scriptfunctions.DefineLHAPDF()
        startLoopStub = scriptfunctions.startLoop(self.pp.plotbase)

        if castStub!="":
            startLoopStub = startLoopStub.replace("//PLACEHOLDERFORCASTLINES", castStub)
        script += startLoopStub
        script += self.initLoop()

        # plotting
        script += self.eventLoop(tree)

        script += "     totalTimeFillHistograms+=timerFillHistograms->RealTime();\n"

        # finish loop
        script+=scriptfunctions.endLoop()
        
        for addCodeInt in self.pp.addInterfaces:
            script += "\n"
            script += addCodeInt.getTestCallLines()
            script += "\n"
        
        # get program footer
        script += scriptfunctions.getFoot(self.pp.addInterfaces)

        # write program text to file
        with open(self.ccPath ,'w') as scriptf:
            scriptf.write(script)
        print(self.ccPath + " written")





    ## compiling programm ##
    def compileProgram(self):
        p = subprocess.Popen(['root-config', '--cflags', '--libs'], 
                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()

        # getting dnnfiles
        dnnfiles=[]
        for addCodeInt in self.pp.addInterfaces:
            if addCodeInt.usesPythonLibraries:
                ppyc = subprocess.Popen(['python-config', '--cflags'], 
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                outpyc, errpyc = ppyc.communicate()
                ppyl = subprocess.Popen(['python-config', '--ldflags'], 
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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





    ## utilities for writeCC ##
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
            vetolist += scriptfunctions.GetMEPDFVetoList(self.pp.MEPDFCSVFile)

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
                
        # set self.vetolist so it can be accessed everywhere in the cls
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
        variables.initVarsFromExprList(self.systWeights, tree)

        systWeights = []
        for systweight in self.pp.systWeights:
            if ":=" in systweight:
                    systWeights.append(systweight.split(":=")[0])
            else:
                    systWeights.append(systweight)
        self.systWeights = systWeights

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
        
    def initLoop(self):
        script = ""
        script += "     timerMapping->Start();\n"
        if self.pp.MEPDFCSVFile!="":
            script += scriptfunctions.ResetMEPDFNormFactors(self.pp.MEPDFCSVFile)
            script += scriptfunctions.RelateMEPDFMapToNormFactor(self.pp.MEPDFCSVFile)
            script += scriptfunctions.PutPDFWeightsinVector(self.pp.MEPDFCSVFile)
            script += scriptfunctions.UseLHAPDF()
        script += "     totalTimeMapping+=timerMapping->RealTime();\n"

        script += "     timerEvalDNN->Start();\n"
        for addCodeInt in self.pp.addInterfaces:
            script += addCodeInt.getVariableInitInsideEventLoopLines()
        script += "     totalTimeEvalDNN+=timerEvalDNN->RealTime();\n"

        script += "     timerSampleWeight->Start();\n"
        script += '        float sampleweight=1;\n'
        script += scriptfunctions.encodeSampleSelection(self.pp.samplesData.allSamples, self.variables)
        script += "     totalTimeSampleWeight+=timerSampleWeight->RealTime();\n"
        
        script += "     timerReadDataBase->Start();\n"
        for db in self.pp.dataBases:
            script += scriptfunctions.readOutDataBase(db)    
        script += "\n"
        script += "     totalTimeReadDataBase+=timerReadDataBase->RealTime();\n"
        
        script += "     timerEvalDNN->Start();\n"
        for addCodeInt in self.pp.addInterfaces:
            script += addCodeInt.getEventLoopCodeLines()
            script += "\n"
        script += "     totalTimeEvalDNN+=timerEvalDNN->RealTime();\n"

        script += "     timerEvalWeightsAndBDT->Start();\n"
        # calculate varibles and get TMVA outputs
        script += self.variables.calculateVarsProgram()
        print("done")
        script += "     totalTimeEvalWeightsAndBDT+=timerEvalWeightsAndBDT->RealTime();\n"
        
        script += "     timerFillHistograms->Start();\n"

        return script

    def eventLoop(self, tree):
        script = ""
        # this class temporary saves variables, systNames and systWeights
        # this way these havent got to be given as arguments for every plot initiated
        plotClass = scriptfunctions.initPlots(self.variables, self.pp.systNames, self.systWeights)
        
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





    ## renaming script ##
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





    ## run scripts ##
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
        # TODO this thing needs to be done better, its kind of a mess
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
    




    ## hadd parallel script ##
    def writeHaddScript(self):
        # creating haddScript
        script = "import ROOT\n"
        script+= "import sys\n"
        script+= "import os\n"
        script+= "import subprocess\n" 
        script+= "outfname = sys.argv[1]\n"
        script+= "outlogname = sys.argv[2]\n"
        script+= "infiles = sys.argv[3:]\n"
        script+= "cmd = ['hadd', '-f', outfname] + infiles\n"
        script+= "worked = 'ERROR'\n"
        script+= "try:\n"
        script+= "\tsubprocess.check_output(cmd,stderr=subprocess.STDOUT)\n"
        script+= "\tworked='OK'\n"
        script+= "except subprocess.CalledProcessError, e:\n"
        script+= "\tworked='ERROR'\n"
        script+= "\tprint('hadding failed - errorlog:')\n"
        script+= "\tprint(e.output)\n"
        script+= "with open(outlogname,'w') as outlog:\n"
        script+= "\toutlog.write(worked)\n"

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
