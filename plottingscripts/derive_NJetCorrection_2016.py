#!/usr/bin/python2
import sys
import os
import imp
import inspect
import optparse
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = "/".join(filedir.split("/")[:-1])

sys.path.append(pyrootdir)

# local imports
import util.analysisClass as analysisClass
import util.configClass as configClass
import util.monitorTools as monitorTools
import util.plotParallel as plotParallel
import util.makePlots as makePlots
import util.haddParallel as haddParallel
import util.checkHistos as checkHistos
import util.makeDatacards as makeDatacards

def main(pyrootdir, opts):
    print '''
    # ========================================================
    # welcome to main function - defining some variables
    # ========================================================
    '''
    # name of the analysis (i.e. workdir name)
    name = 'SFSFderivation/2016'

    # path to workdir subfolder where all information should be saved
    workdir = pyrootdir + "/workdir/" + name

    # signal process
    signalProcess = "ttH"

    # dataera
    dataera = "2016"

    # Name of final discriminator, should not contain underscore
    nom_histname_template = "$PROCESS__$CHANNEL"
    syst_histname_template = nom_histname_template + "__$SYSTEMATIC"
    histname_separator = "__"


    # configs
    config          = "SFSFderivation/samples_2016"
    variable_cfg    = "SFSFderivation/additionalVariables"
    plot_cfg        = "SFSFderivation/plots"
    syst_cfg        = "SFSFderivation/systs"

    # script options
    analysisOptions = {
        # general options
        "usePseudoData":        True,
        "testrun":              False,  # test run with less samples
        "stopAfterCompile":     False,   # stop script after compiling
        "haddFromWildcard":     True,
        # the skipX options try to skip the submission of files to the batch system
        # before skipping the output is crosschecked
        # if the output is not complete, the skipped part is done anyways
        "skipPlotParallel":     opts.skipPlotParallel,
        "skipHaddParallel":     opts.skipHaddParallel,
        "skipHaddFromWildcard": opts.skipHaddFromWildcard,
        }
    
    print '''
    # ========================================================
    # initializing analysisClass 
    # ========================================================
    '''

    # save a lot of useful information concerning the analysis
    analysis = analysisClass.analysisConfig(
        workdir         = workdir, 
        pyrootdir       = pyrootdir, 
        signalProcess   = signalProcess, 
        pltcfgName      = config,
        #discrName       = discrName,
        dataera         = dataera)

    
    analysis.initAnalysisOptions( analysisOptions )

    pltcfg = analysis.initPlotConfig()
    print "We will import the following plotconfig: ", analysis.getPlotConfig()

    # loading monitorTools module locally
    monitor = monitorTools.init(analysis.workdir)
    monitor.printClass(analysis, "init")

    print '''
    # ========================================================
    # prepare configdata
    # ========================================================
    '''

    configData = configClass.configData(
        analysisClass   = analysis,
        variable_config = variable_cfg,
        plot_config     = plot_cfg,
        execute_file    = os.path.realpath(inspect.getsourcefile(lambda:0)))

    configData.initSystematics(systconfig = syst_cfg)

    configData.initData()

    # get the discriminator plots
    configData.genDiscriminatorPlots(memexp = "", dnnInterface=None)
    configData.writeConfigDataToWorkdir()
    monitor.printClass(configData, "init")
    print '''    
    # ========================================================
    # define additional variables necessary for selection in plotparallel
    # ========================================================
    '''
    configData.getAddVariables() # also adds DNN variables

    print '''    
    # ========================================================
    # loading samples and samples data
    # ========================================================
    '''
    configData.initSamples()
    

    print '''
    # ========================================================
    # done with preprocessing
    # ========================================================
    '''

    # plot everything, except during drawParallel step
    # Create file for data cards
    print '''
    # ========================================================
    # starting with plotParallel step
    # ========================================================
    '''
    
    with monitor.Timer("plotParallel"):
        # initialize plotParallel class 
        pP = plotParallel.plotParallel(
            analysis        = analysis,
            configData      = configData,
            nominalHistKey  = nom_histname_template,
            systHistKey     = syst_histname_template,
            separator       = histname_separator)

        monitor.printClass(pP, "init")
        # set some changed values
        pP.setMaxEvts(200000)
        pP.setSampleForVariableSetup(configData.samples[1])

        # run plotParallel
        pP.run()

    pP.checkTermination()
    monitor.printClass(pP, "after plotParallel")

    # hadd histo files before renaming. The histograms are actually already renamed. 
    # But the checkbins thingy will not have been done yet.
    print '''
    # ========================================================
    # hadding from wildcard
    # ========================================================
    '''
    with monitor.Timer("haddFilesFromWildCard"):
        haddParallel.haddSplitter( 
            input               = pP.getHaddOutPath(),
            outName             = analysis.ppRootPath,
            subName             = "haddParts",
            nHistosRemainSame   = True,
            skipHadd            = analysis.skipHaddFromWildcard)
     

    # infile
    infile = ROOT.TFile(analysis.ppRootPath)

    # outfiles
    outfile_path = analysis.workdir+"/SFratios.root"
    outfile = ROOT.TFile(outfile_path, "RECREATE")
    weightString = ""

    # basic selections and weights
    weightString += """
        "selection_hbb:=((abs(GenHiggs_DecProd1_PDGID)==5 && abs(GenHiggs_DecProd2_PDGID)==5))",
        "selection_nonhbb:=((abs(GenHiggs_DecProd1_PDGID)!=5 && abs(GenHiggs_DecProd2_PDGID)!=5))",
        "selection_ttsl:=(N_GenTopLep==1)",
        "selection_ttdl:=(N_GenTopLep==2)",
        "selection_ttfh:=(N_GenTopLep==0)",

        "selection_ttbb:=(GenEvt_I_TTPlusBB==3&&GenEvt_I_TTPlusCC==0)",
        "selection_ttb:=(GenEvt_I_TTPlusBB==1&&GenEvt_I_TTPlusCC==0)",
        "selection_tt2b:=(GenEvt_I_TTPlusBB==2&&GenEvt_I_TTPlusCC==0)",
        "selection_ttcc:=(GenEvt_I_TTPlusBB==1&&GenEvt_I_TTPlusCC==1)",
        "selection_ttlf:=(GenEvt_I_TTPlusBB==0&&GenEvt_I_TTPlusCC==0)",


"""


    # loop over variables
    for plot in configData.getDiscriminatorPlots():
        weightString += "\n"
        channel = plot.name
        # loop over samples
        for sample in configData.samples:
            weightString += "\n"
            process = sample.nick
     
            # get the nominal histogram for that combination
            nom = infile.Get(
                nom_histname_template.replace("$PROCESS", process).replace("$CHANNEL", channel)
                )
            
            # loop over systematics
            for syst in configData.allSystNames:
                print("calculating SFs for {}, {}, {}".format(channel, process, syst))

                systHist = infile.Get(
                    syst_histname_template.replace("$PROCESS", process).replace("$CHANNEL", channel).replace("$SYSTEMATIC", syst)
                    )
                ratioHist = nom.Clone()
                ratioHist.Divide(systHist)

                outName = "SF_$CHANNEL__$PROCESS__$SYSTEMATIC".replace("$PROCESS", process).replace("$CHANNEL", channel).replace("$SYSTEMATIC", syst)

                # add ratio as weight expression to output file
                weightExpression = ""
                for iBin in range(ratioHist.GetNbinsX()):
                    if ratioHist.GetBinCenter(iBin+1) < 4: continue
                    weight="(({}=={})*{})+".format(
                        channel,
                        int(ratioHist.GetBinCenter(iBin+1)),
                        ratioHist.GetBinContent(iBin+1)
                        )
                    if int(iBin) == int(ratioHist.GetNbinsX()-1):
                        weight = weight.replace("==",">=").replace("+","")
                    weightExpression += weight                    
                
                #hardcoded shit
                if syst == "btag_sfUp": continue
                if syst == "btag_sfDown": outName = outName.replace("btag_sfDown", "btag_NOMINAL")
                weightString+="        \"weight_"+outName+":=({})\",\n".format(weightExpression)

                # save ratio hist
                outfile.cd()
                ratioHist.Write(outName)

    print("\nsummarizing weights ...\n")
    # more hardcoded stuff
    weightString +="\n\n\n"
    weightTemplate = "weight_SF_$CHANNEL__$PROCESS__$SYSTEMATIC"
    for plot in configData.getDiscriminatorPlots():
        weightString += "\n"
        channel = plot.name
 
        for syst in configData.allSystNames:
            if syst == "btag_sfUp": continue
            systName = syst
            if syst == "btag_sfDown":
                systName = "btag_NOMINAL"

            weightString += "\n\n"
            # generate one weight for ttH, tthf, ttcc and ttlf
            weightName = "sf_$CHANNEL__$PROCESS__$SYSTEMATIC".replace("$CHANNEL", channel).replace("$SYSTEMATIC", systName)
            
            # ttH
            expression = ""
            expression += "(selection_hbb*"+weightTemplate.replace("$PROCESS", "ttH_bb").replace("$CHANNEL", channel).replace("$SYSTEMATIC", systName)+")"
            expression +="+(selection_nonhbb*"+weightTemplate.replace("$PROCESS", "ttH_nonbb").replace("$CHANNEL", channel).replace("$SYSTEMATIC", systName)+")"
            
            weightString+="        \""+weightName.replace("$PROCESS", "ttH")+":=({})\",\n".format(expression)

            # tthf
            expression = ""
            expression += "(selection_ttdl*selection_ttb*"+weightTemplate.replace("$PROCESS", "ttb_4FS_DL").replace("$CHANNEL", channel).replace("$SYSTEMATIC", systName)+")"
            expression +="+(selection_ttdl*selection_tt2b*"+weightTemplate.replace("$PROCESS", "tt2b_4FS_DL").replace("$CHANNEL", channel).replace("$SYSTEMATIC", systName)+")"
            expression +="+(selection_ttdl*selection_ttbb*"+weightTemplate.replace("$PROCESS", "ttbb_4FS_DL").replace("$CHANNEL", channel).replace("$SYSTEMATIC", systName)+")"
            expression +="+(selection_ttsl*selection_ttb*"+weightTemplate.replace("$PROCESS", "ttb_4FS_SL").replace("$CHANNEL", channel).replace("$SYSTEMATIC", systName)+")"
            expression +="+(selection_ttsl*selection_tt2b*"+weightTemplate.replace("$PROCESS", "tt2b_4FS_SL").replace("$CHANNEL", channel).replace("$SYSTEMATIC", systName)+")"
            expression +="+(selection_ttsl*selection_ttbb*"+weightTemplate.replace("$PROCESS", "ttbb_4FS_SL").replace("$CHANNEL", channel).replace("$SYSTEMATIC", systName)+")"
            #expression +="+(selection_ttfh*selection_ttb*"+weightTemplate.replace("$PROCESS", "ttb_4FS_FH").replace("$CHANNEL", channel).replace("$SYSTEMATIC", systName)+")"
            #expression +="+(selection_ttfh*selection_tt2b*"+weightTemplate.replace("$PROCESS", "tt2b_4FS_FH").replace("$CHANNEL", channel).replace("$SYSTEMATIC", systName)+")"
            #expression +="+(selection_ttfh*selection_ttbb*"+weightTemplate.replace("$PROCESS", "ttbb_4FS_FH").replace("$CHANNEL", channel).replace("$SYSTEMATIC", systName)+")"
            
            weightString+="        \""+weightName.replace("$PROCESS", "ttbb")+":=({})\",\n".format(expression)

            # ttcc
            expression = ""
            expression += "(selection_ttdl*selection_ttcc*"+weightTemplate.replace("$PROCESS", "ttcc_DL").replace("$CHANNEL", channel).replace("$SYSTEMATIC", systName)+")"
            expression +="+(selection_ttsl*selection_ttcc*"+weightTemplate.replace("$PROCESS", "ttcc_SL").replace("$CHANNEL", channel).replace("$SYSTEMATIC", systName)+")"
            expression +="+(selection_ttfh*selection_ttcc*"+weightTemplate.replace("$PROCESS", "ttcc_FH").replace("$CHANNEL", channel).replace("$SYSTEMATIC", systName)+")"
            
            weightString+="        \""+weightName.replace("$PROCESS", "ttcc")+":=({})\",\n".format(expression)

            # ttlf
            expression = ""
            expression += "(selection_ttdl*selection_ttlf*"+weightTemplate.replace("$PROCESS", "ttlf_DL").replace("$CHANNEL", channel).replace("$SYSTEMATIC", systName)+")"
            expression +="+(selection_ttsl*selection_ttlf*"+weightTemplate.replace("$PROCESS", "ttlf_SL").replace("$CHANNEL", channel).replace("$SYSTEMATIC", systName)+")"
            expression +="+(selection_ttfh*selection_ttlf*"+weightTemplate.replace("$PROCESS", "ttlf_FH").replace("$CHANNEL", channel).replace("$SYSTEMATIC", systName)+")"
            
            weightString+="        \""+weightName.replace("$PROCESS", "ttlf")+":=({})\",\n".format(expression)
    

            # combined weight
            weightString+="\n"
            expression = ""
            expression += "(isTTbarSample==1)*("+weightName.replace("$PROCESS", "ttlf")+"+"+weightName.replace("$PROCESS", "ttcc")+"+"+weightName.replace("$PROCESS", "ttbb")+")"
            expression += "+(isTthSample==1)*("+weightName.replace("$PROCESS", "ttH")+")"
            expression += "+(isTTbarSample==0&&isTthSample==0)*(1.)"

            weightString+="        \""+weightName.replace("_$PROCESS_","")+":=({})\",\n\n\n\n".format(expression)
            print("calculated usable weight: {}".format(weightName.replace("_$PROCESS_","")))            
   
    # save weight expressions
    with open(outfile_path.replace(".root",".txt"), "w") as f:
        f.write(weightString)
    print("\nadd content of {} to additionalVariables.py and apply usable weights in syst.csv and sample config\n".format(outfile_path.replace(".root",".txt")))

    outfile.Close()

if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option("--skipPlotParallel",     dest = "skipPlotParallel",      action = "store_true", default = False)
    parser.add_option("--skipHaddParallel",     dest = "skipHaddParallel",      action = "store_true", default = False)
    parser.add_option("--skipHaddFromWildcard", dest = "skipHaddFromWildcard",  action = "store_true", default = False)

    (opts, args) = parser.parse_args()
    main(pyrootdir, opts)
