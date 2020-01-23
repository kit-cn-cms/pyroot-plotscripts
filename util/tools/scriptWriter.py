import sys
import os
import subprocess
import stat
import ROOT
import glob
import json
import filecmp
import pandas

# local imports 
import GenWeightUtils
import plotClasses
import scriptfunctions 
import variableCancer
###########################
#                         #
# S C R I P T W R I T E R #
#        C L A S S        #
###########################

cmssw_head ="""export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
export SCRAM_ARCH={scram_arch}
cd {cmssw_base}/src
eval `scram runtime -sh`
cd - 
"""

class scriptWriter:
    def __init__(self, plotParaClass):
        ''' default init
         inheriting all public functions/varaibles from plotParallel class '''
        self.pp = plotParaClass
        self.ccPath = plotParaClass.ccPath
        self.systWeights = plotParaClass.systWeights
        self.sampleForVariableSetup = plotParaClass.sampleForVariableSetup
        if self.pp.useGenWeightNormMap:
            # initialize class to handle genWeight normalization stuff
            self.genWeightNormalization = GenWeightUtils.GenWeightNormalization(self.pp.rateFactorsFile)


    ## main function for writing and compiling c++ code ##
    def writeCC(self):
        print("#"*50)
        print("starting to write and compile c++ code")
        print("c++ path is "+self.ccPath)
        print("#"*50)
        ccExists = os.path.exists(self.ccPath)
        if ccExists:
            print("c++ file already exists - check if this needs to be updated.")
            print("moving it to backup")
            cmd = "mv -v "+self.ccPath+" "+self.ccPath+"Backup"
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
            if codeDiffers: print( "c++ codes differ" )

        # check if needs to be compiled
        if codeDiffers:
            print( "compiling c++ program" )
            # compiling programm
            self.compileProgram()
        else:
            print( "c++ code already existed without differences -- skipping compilation" )
        
        # check if compiling was successful
        fname = ".".join(self.ccPath.split(".")[:-1])
        if not os.path.exists(fname):
            print("ERROR: Did not find file '{}'".format(fname))
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
        print("getting tree to setup with")
        if self.sampleForVariableSetup:
            samplesToCheck = [self.sampleForVariableSetup]
        else:
            samplesToCheck = self.pp.configData.allSamples
        for i in range(len(samplesToCheck)):
            thistreeisgood = False
            for j in range(len(samplesToCheck[i].files)):
                f = ROOT.TFile(samplesToCheck[i].files[j])
                tree = f.Get('MVATree')
                if tree.GetEntries() > 0:
                    print("using "+str(samplesToCheck[i].files[j])+" to determine variable types")
                    thistreeisgood = True
                    break
            if thistreeisgood:
                break

        # initialize variables with variablebox
        self.initVariables(tree)
        
        # write program
        # start writing program
        script = scriptfunctions.getHead(   basepath          = self.pp.analysis.pyrootdir, 
                                            dataBases         = self.pp.dataBases, 
                                            memDB_path        = self.pp.memDBpath, 
                                            addCodeInterfaces = self.pp.addInterfaces)

        if self.pp.useGenWeightNormMap:
            script += self.genWeightNormalization.declareNormFactors()
            script += self.genWeightNormalization.addNormalizationMap()
        
        for db in self.pp.dataBases:
            script += scriptfunctions.InitDataBase(db)
        for addCodeInt in self.pp.addInterfaces:
            script += addCodeInt.getBeforeLoopLines()
            
        # initialize all variables
        initStub, castStub = self.varManager.writeVariableInitialization()
        script += initStub
        script += self.varManager.writeBranchAdresses()

        # initialize TMVA Readers
        script += self.varManager.writeTMVAReader()

        # initialize histograms in all categories and for all systematics
        script += scriptfunctions.initHistos(
            catnames  = self.pp.categoryNames, 
            systnames = self.pp.systNames, 
            plots     = self.pp.configData.getDiscriminatorPlots(),
            nom_histname_template = self.pp.nominalHistoKey, 
            syst_histname_template = self.pp.systHistoKey)

        # start event loop
        #if self.pp.useGenWeightNormMap:
        #    script += scriptfunctions.DefineLHAPDF()
        startLoopStub = scriptfunctions.startLoop(self.pp.analysis.pyrootdir)

        if castStub!="":
            startLoopStub = startLoopStub.replace("//PLACEHOLDERFORCASTLINES", castStub)
        startLoopStub = startLoopStub.replace("//PLACEHOLDERFORVARIABLERESET",self.varManager.resetVariableInitialization())
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

        # check if all variables are initialized correctly - exit otherwise
        self.varManager.checkVariableInitialization()



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
        
        #lhapdf=[' `/cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/lhapdf/6.1.6-ikhhed2/bin/lhapdf-config --cflags --ldflags`']
        lhapdf=[' `/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/lhapdf/6.2.1-fmblme/bin/lhapdf-config --cflags --ldflags`']

        # getting databases
        memDBccfiles=[]
        if self.pp.useDataBases:
            memDBccfiles=glob.glob('/nfs/dust/cms/user/swieland/ttH_legacy/MEMdatabase/CodeforScriptGenerator/MEMDataBase/MEMDataBase/src/*.cc') 
            #TODO update the dataBases code

        # improve ram usage and reduce garbage of g++ compiler
        improveRAM = '--param ggc-min-expand=100 --param ggc-min-heapsize=2400000'
        # if python cflags are used -O3 optimization is set, resulting in long compilation times, set it back to default -O0
        resetCompilerOpt = '-O0'

        # include path for scriptFiles folder
        print "pyroot dir: " + self.pp.analysis.pyrootdir
        scriptFilesPath = os.path.join(self.pp.analysis.pyrootdir, *("util/scriptFiles".split("/")))
        if not os.path.exists(scriptFilesPath):
            sys.exit("ERROR: Could not find path with scriptFiles in '{}'".format(scriptFilesPath))

        print("creating compile command")
        # cmd= ['g++']+[improveRAM]+out[:-1].replace("\n"," ").split(' ')+dnnfiles+lhapdf+['-lTMVA']+memDBccfiles+[resetCompilerOpt]+[self.ccPath,'-o',self.ccPath.replace(".cc","")]
        cmd = ['g++']+[improveRAM]
        cmd += out[:-1].split()
        # add necessary libraries and file paths
        cmd += dnnfiles+lhapdf+['-lTMVA'] + ["-I"+scriptFilesPath]
        cmd += memDBccfiles+[resetCompilerOpt]
        cmd += [self.ccPath,'-o',self.ccPath.replace(".cc","")]
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
        
        dataFrame = pandas.read_csv(self.pp.analysis.pyrootdir+"/data/vetolist.csv")
        vetolist = list(dataFrame.vetolist)

        #self.pp.MEPDFCSVFile = self.pp.plotbase + /data/rate_factors_onlyinternal_powhegpythia.csv
        if self.pp.useGenWeightNormMap:
            vetolist += self.genWeightNormalization.getVetolist()

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
        # initialize variables objects
        variableManager = variableCancer.VariableManager(tree, self.vetolist)
        variableManager.add( ["Weight", "Weight_CSV", "Weight_XS"] )
        
        # get additional variables
        if len(self.pp.configData.addVars) > 0:
            variableManager.add( self.pp.configData.addVars )

        # get DNN variables
        for interface in self.pp.addInterfaces:
            variableManager.add( interface.getVariables() )

        # get systematic weight variables
        variableManager.add( self.systWeights )

        systWeights = []
        for w in self.systWeights:
            if ":=" in w:   systWeights.append( w.split(":=")[0] )
            else:           systWeights.append(w)
        self.systWeights = systWeights

        # get sample selection variables
        for sample in self.pp.configData.allSamples:
            variableManager.add( sample.selection )

        # get category selection variables
        variableManager.add( self.pp.categorySelections )

        # get variables used in plots
        for plot in self.pp.configData.getDiscriminatorPlots():
            if plot.dim == 1:
                variableManager.add( plot.variable )
            if plot.dim == 2:
                variableManager.add( plot.variable1 )
                variableManager.add( plot.variable2 )

            variableManager.add( plot.selection )
     
        # run the variable initialization program
        variableManager.run()
        self.varManager = variableManager


    def initLoop(self):
        script = ""
        script += "     timerMapping->Start();\n"
        if self.pp.useGenWeightNormMap:
            # script += self.genWeightNormalization.resetNormalizationFactors()
            script += self.genWeightNormalization.relateMapToNormalizationFactor()

        script += "     totalTimeMapping+=timerMapping->RealTime();\n"

        script += "     timerEvalDNN->Start();\n"
        for addCodeInt in self.pp.addInterfaces:
            script += addCodeInt.getVariableInitInsideEventLoopLines()
        script += "     totalTimeEvalDNN+=timerEvalDNN->RealTime();\n"

        script += "     timerEvalWeightsAndBDT->Start();\n"
        # calculate varibles and get TMVA outputs
        script += self.varManager.calculateVariables()
        script += "     totalTimeEvalWeightsAndBDT+=timerEvalWeightsAndBDT->RealTime();\n"

        script += "     timerEvalDNN->Start();\n"
        for addCodeInt in self.pp.addInterfaces:
            script += addCodeInt.getEventLoopCodeLines()
            script += "\n"
        script += "     totalTimeEvalDNN+=timerEvalDNN->RealTime();\n"

        script += "     timerSampleWeight->Start();\n"
        script += '        float sampleweight=1;\n'
        script += scriptfunctions.encodeSampleSelection(self.pp.configData.allSamples, self.varManager)
        script += "     totalTimeSampleWeight+=timerSampleWeight->RealTime();\n"
        
        script += "     timerReadDataBase->Start();\n"
        for db in self.pp.dataBases:
            script += scriptfunctions.readOutDataBase(db)    
        script += "\n"
        script += "     totalTimeReadDataBase+=timerReadDataBase->RealTime();\n"
                
        script += "     timerFillHistograms->Start();\n"

        return script

    def eventLoop(self, tree):
        script = ""
        # this class temporary saves variables, systNames and systWeights
        # this way these havent got to be given as arguments for every plot initiated
        plotClass = scriptfunctions.initPlots(self.varManager, self.pp.systNames, self.systWeights)
        
        for catname, catselection in zip(self.pp.categoryNames, self.pp.categorySelections):
            # for every category
            plotText = plotClass.startCat(catselection)
            # plot everything
            for plot in self.pp.configData.getDiscriminatorPlots():
                plotText += plotClass.initPlot(plot, tree, catname)
            # finish category
            plotText += plotClass.endCat()
            script += plotText
        
        return script





    ## cleanup script (during plot parallel) ##
    # comment: this could be integrated into "cleanupHistos"
    def writeCleanupScript(self):
        script = """
import sys
import os
sys.path.append('{path}')
import cleanupHistos

filename     = os.getenv('OUTFILENAME')

process      = os.getenv('ORIGNAME')
syst_key     = os.getenv('SYSTHISTKEY')
separator    = os.getenv('SEPARATOR')

outname      = filename.replace('.root','_original.root')
systematics  = "{systpath}"

nHistsBefore, nHistsAfter = cleanupHistos.cleanupHistos(filename, outname, process, 
                                                        systematics, syst_key, separator, 
                                                        replace_config = "{replace_config}")
with open(outname.replace('.root','_cleanedUp.txt'), 'w') as f:
    f.write('{{}} : {{}}'.format(nHistsBefore, nHistsAfter))
  """.format(path = os.path.join(self.pp.analysis.pyrootdir,"util"),
            systpath = self.pp.configData.local_syst_path,
            replace_config = self.pp.configData.replace_config)
        # write script to file
        with open(self.ccPath.replace(".cc","_cleanupHistos.py"), "w") as srcfile:
            srcfile.write(script)

    def writeMergeSystsScript(self):
        script = """
import sys
import os
sys.path.append('{path}')
import combine_intermid_systs

filename     = os.getenv('INFILE')

process      = os.getenv('ORIGNAME')
nom_key      = os.getenv('NOMHISTKEY')
syst_key     = os.getenv('SYSTHISTKEY')
separator    = os.getenv('SEPARATOR')
syst_csvpath = "{systpath}"

print(process)
combine_intermid_systs.combine_intermid_syst(   h_nominal_key   = nom_key, 
                                                h_syst_key      = syst_key, 
                                                rfile_path      = filename,
                                                replace_config  = "{replace_config}",
                                                processes       = process,
                                                separator       = separator,
                                                syst_csvpath    = syst_csvpath
                                            )
""".format(path = os.path.join(self.pp.analysis.pyrootdir,"util"),
            systpath = self.pp.configData.local_syst_path,
            replace_config = self.pp.configData.replace_config)
        # write script to file
        script_path = self.ccPath.replace(".cc","_combineSysts.py")
        with open(script_path, "w") as srcfile:
            srcfile.write(script)
        return script_path


    ## run scripts ##
    def writeRunScripts(self):
        # init outputs
        self.scripts = []
        self.cleanup_scripts = []
        self.outputs = []
        self.nentries = []
        self.samplewiseMaps = {}

        # loading tree info from json file
        SaveTreeInformation = {}
        LoadedTreeInformation = {}
        if self.pp.jsonFile != "":
            print("Loading file with tree event information")
            with open(self.pp.jsonFile,"r") as jsonfile:
                LoadedTreeInformation = json.load(jsonfile)

    
        # looping over samples
        for sample in self.pp.configData.allSamples:
            print("creating scripts for "+str(sample.name))
            #print '\ncreating scripts for',sample.name,'from',sample.path
            self.samplewiseMaps[sample.nick] = []

            nEvents = 0
            nJob = 0
            nEventsInFiles = 0

            filterFile = sample.filterFile
            filesToSubmit = []

            # looping over files in sample
            for filename in sample.files:
                nEventsInFile = 0
                
                # search for entry in json file to extract number of events per file
                if LoadedTreeInformation != {} and filename in LoadedTreeInformation:
                    nEventsInFile = LoadedTreeInformation[filename]
                else:
                    f = ROOT.TFile(filename)
                    tree = f.Get('MVATree')
                    nEventsInFile = tree.GetEntries()

                SaveTreeInformation[filename] = nEventsInFile

                
                # if the file is larger than self.maxevents it is analyzed in portions of nevents
                if nEventsInFile > self.pp.maxevents:
                    for ijob in range(nEventsInFile / self.pp.maxevents + 1):
                        nJob += 1
                        writeOptions = {"skipEvents": (ijob)*self.pp.maxevents}

                        self.writeSingleScript(sample, filename, nJob, filterFile, writeOptions)
                    self.nentries.append(nEventsInFile)
                    nEvents += nEventsInFile

                # else additional files are appended to list of files to be submitted
                else :
                    filesToSubmit += [filename]
                    nEventsInFiles += nEventsInFile
                    if nEventsInFiles > self.pp.maxevents or filename == sample.files[-1] or len(filesToSubmit)>400: 
                        nJob += 1
                        filenames = ' '.join(filesToSubmit)
                        self.writeSingleScript(sample, filenames, nJob, filterFile)

                        self.nentries.append(nEventsInFiles)
                        nEvents += nEventsInFiles

                        filesToSubmit = []
                        nEventsInFiles = 0
                        
                # If self.options["testrun"] = true, only use small number of files             
                if self.pp.analysis.testrun: 
                    break

            # submit remaining scripts (can happen if the last file was large)
            if len(filesToSubmit) > 0:
                nJob += 1
                filenames = ' '.join(filesToSubmit)
                self.writeSingleScript(sample, filenames, nJob, filterFile)
                
                self.nentries.append(nEventsInFiles)
                nEvents += nEventsInFiles

                filesToSubmit = []
                nEventsInFiles = 0

            print '\t', nEvents, 'events found'
        
        # save tree information to json file
        #treejson = json.dumps(SaveTreeInformation)
        with open(self.pp.analysis.workdir+'/'+"treejson.json","w") as jsonfile:
            json.dump(SaveTreeInformation, jsonfile, indent = 2, separators = (",", ": "))
            #jsonfile.write(treejson)
        print "Saved information about events in trees to ", self.pp.analysis.workdir+'/'+"treejson.json"
        returnData = {  "scripts": self.scripts,
                        "cleanup": self.cleanup_scripts,
                        "outputs": self.outputs, 
                        "entries": self.nentries, 
                        "maps": self.samplewiseMaps}
        return returnData
    

    def writeSingleScript(self, sample, filenames, nJob, filterFile, writeOptions = {}):
        # defaults
        maxevents = writeOptions.get("maxevents", self.pp.maxevents)
        processname = sample.nick
        outfilename = self.pp.plotPath+processname+'_'+str(nJob)+'.root'
        scriptname = self.pp.scriptsPath+'/'+processname+'_'+str(nJob)+'.sh'
        cleanupname = self.pp.scriptsPath+"/"+processname+"_cleanup_"+str(nJob)+".sh"
        origName = sample.origName
        suffix = writeOptions.get("suffix", "")
        skipevents = writeOptions.get("skipEvents", 0)

        # check options
        if self.pp.analysis.testrun and maxevents < 100:
            maxevents = 100

        # writing script
        script = "#!/bin/bash \n"
        if self.pp.cmsswpath != '':
            script += cmssw_head.format(scram_arch = os.environ['SCRAM_ARCH'], 
                                        cmssw_base = self.pp.cmsswpath)
        script += 'export PLOTSCRIPTBASEDIR="'+self.pp.analysis.pyrootdir+'"\n'
        script += 'export DATAERA="'+self.pp.analysis.dataera+'"\n'
        script += 'export PROCESSNAME="'+processname+'"\n'
        script += 'export FILENAMES="'+filenames+'"\n'
        script += 'export OUTFILENAME="'+outfilename+'"\n'
        script += 'export MAXEVENTS="'+str(maxevents)+'"\n'
        script += 'export SKIPEVENTS="'+str(skipevents)+'"\n'
        script += 'export SUFFIX="'+suffix+'"\n'
        script += 'export EVENTFILTERFILE="'+str(filterFile)+'"\n'
        script += 'export ORIGNAME="'+str(origName)+'"\n'
        script += "export NOMHISTKEY='{}'\n".format(self.pp.nominalHistoKey)
        script += "export SYSTHISTKEY='{}'\n".format(self.pp.systHistoKey)
        script += 'export SEPARATOR="{}"\n'.format(self.pp.histNameSeparator)
        #DANGERZONE
        pPscript = script + ".".join(self.ccPath.split(".")[:-1])+'\n'
        cleanup  = script + 'python '+self.ccPath.replace('.cc','_cleanupHistos.py')+'\n'
        if self.pp.configData.replace_config:
            cleanup  += 'python '+self.ccPath.replace('.cc','_combineSysts.py')+'\n'

        # writing script to file and chmodding
        with open(scriptname, "w") as f:
            f.write(pPscript)
        st = os.stat(scriptname)
        os.chmod(scriptname, st.st_mode | stat.S_IEXEC)

        with open(cleanupname, "w") as f:
            f.write(cleanup)
        st = os.stat(cleanupname)
        os.chmod(cleanupname, st.st_mode | stat.S_IEXEC)

        # saving script info to lists
        self.scripts.append(scriptname)
        self.cleanup_scripts.append(cleanupname)
        self.outputs.append(outfilename)
        self.samplewiseMaps[processname].append(outfilename)

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
        script+= "print('hadding \\n' + '\\n'.join(infiles))\n"
        script+= "print('outputfile: '+str(outfname))\n"
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
        self.haddScript = self.pp.analysis.workdir+'/haddScript.py'
        with open(self.haddScript, "w") as sf:
            sf.write(script)
        print("haddScript written to "+self.haddScript)


    def writeHaddShell(self, scriptname, haddedRootName, haddedLogName, sampleData):
        script = "#!/bin/bash \n"
        if self.pp.cmsswpath!='':
            script += cmssw_head.format(scram_arch = os.environ['SCRAM_ARCH'], 
                                        cmssw_base = self.pp.cmsswpath)
        script += 'python '+self.haddScript+' '+haddedRootName+' '
        script += haddedLogName+' '+' '.join(sampleData)+'\n'

        # saving shell script
        with open(scriptname, "w") as f:
            f.write(script)

        # chmodding shell script
        st = os.stat(scriptname)
        os.chmod(scriptname, st.st_mode | stat.S_IEXEC)

    def writeSystMergeScript(self, out_path, script_path, **options):
        """
        script to write .sh script that merge systematics for one process.
        Inputs:
        out_path            :   path where the script is to be written
        script_path         :   path to python script that will be called
        additional keywords :   variables that will be exported in the .sh script
                                keywords will be variable names, values are
                                the exported values
        
        current list of required values in this script:
        ORIGNAME    : original name of the process
        INFILE      : path to .root file with histograms
        NOMHISTKEY  : nominal key template for histogram names
        SYSTHISTKEY : key template for histograms of systematic variations
        SEPARATOR   : string that separates the keywords in the key templates
        """
        # writing script
        script = "#!/bin/bash \n"
        if self.pp.cmsswpath != '':
            script += cmssw_head.format(scram_arch = os.environ['SCRAM_ARCH'], 
                                        cmssw_base = self.pp.cmsswpath)
        # export additional variables 
        for name in options:
            script += "export {}='{}'\n".format(name, options[name])
        script += "\npython {}".format(script_path)

        # writing script to file and chmodding
        with open(out_path, "w") as f:
            f.write(script)
        st = os.stat(out_path)
        os.chmod(out_path, st.st_mode | stat.S_IEXEC)

        if os.path.exists(out_path):
            return out_path
        else:
            return None