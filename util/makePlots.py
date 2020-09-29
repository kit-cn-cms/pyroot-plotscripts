import sys
import os
import stat
import json
import pprint
import configClass as configClass
import analysisClass as analysisClass

filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = "/".join(filedir.split("/")[:-1])

sys.path.append(pyrootdir+"/configs")
sys.path.append(filedir+"/tools")
import nafInterface



def makePlots(configData, nominal_key = "$PROCESS_$CHANNEL", syst_key = "$PROCESS_$CHANNEL_$SYSTEMATIC"):

    ListOfPlots     = configData.getDiscriminatorPlots()
    workdir         = configData.analysis.workdir
    pyrootdir       = configData.analysis.pyrootdir
    plotconfig      = createPlotConfig( configData = configData,
                                        workdir = workdir,
                                        nominal_key = nominal_key,
                                        syst_key = syst_key )
    rootfile        = configData.analysis.rootPath

    # create output folders
    print('creating output folders')
    scriptPath = workdir+'/plottingScripts/'
    if not os.path.exists(scriptPath):
        os.makedirs(scriptPath)

    ListOfScripts = []
    print('Creating Scripts to Make Plots')
    for Plot in ListOfPlots:
        print('    - {plot}' .format(plot=Plot.name)) 
        ListOfScripts.append( createPlotScript(channel=Plot.name,pyrootdir=pyrootdir, 
                                                    workdir=workdir, scriptPath=scriptPath,
                                                    plotconfig=plotconfig,
                                                    rootfile=rootfile, 
                                                    selectionlabel=Plot.label)
                            )


    print "Submitting ", len(ListOfScripts), " PlotScripts"
    nafInterface.drawInterface(ListOfScripts, ListOfPlots)

    return


    # creates plot wrapper of the plotting information
def init_plottingsamples(plotsample):
    returndict ={
                "label": plotsample.name,
                "typ": plotsample.typ,
                "color": plotsample.color,
                "addSamples":plotsample.addsamples,
                }
    return returndict
def createPlotConfig(configData,workdir, nominal_key, syst_key):
    #get plotting information 

    plotinfo = {
        "signalScaling"     : configData.analysis.signalScaling,
        #"datalabel"         : "data",
        "data"              : "data_obs",
        
        "cmslabel"          : configData.analysis.cmslabel,
        "normalize"         : bool(configData.analysis.normalize),
        "ratio"             : configData.analysis.ratio,
        "logarithmic"       : bool(configData.analysis.logarithmic),
        "splitLegend"       : bool(configData.analysis.splitLegend),
        "shape"             : bool(configData.analysis.shape),
      
        "statErrorband"     : True,
        "nominalKey"        : nominal_key,
        "systematicKey"     : syst_key,
    }


    ####################################################
    datalabel = configData.analysis.usePseudoData
    if datalabel:
        if isinstance(datalabel,bool):
            datalabel = "simData"
    else:
        if isinstance(datalabel,bool):
            datalabel = "data"
    plotinfo["datalabel"] = datalabel
    ####################################################


    lumiLabel           = configData.analysis.lumiLabel
    if lumiLabel:
        if isinstance(lumiLabel,bool):
            lumiLabel   = configData.analysis.getLumi()
    plotinfo["lumiLabel"] = lumiLabel

    samples = {}
    #samples named in the rootfile
    for sample in configData.pltcfg.samples:
        samples[sample.nick]= {
        "plot": sample.plot, 
        "info": {
            "label": sample.name,
            "typ": sample.typ,
            "color": sample.color,
            }
        }

    #combined samples
    plottingsamples={}
    for plotsample in configData.pltcfg.plottingsamples:
        print plotsample
        if isinstance(plotsample, list):
            for p in plotsample:
                plottingsamples[p.nick] = init_plottingsamples(p)
        else:
            plottingsamples[plotsample.nick] = init_plottingsamples(plotsample)
    
    sortedProcesses   = configData.pltcfg.sortedProcesses

    #systematics to be plotted
    systematics=configData.plots
    print systematics

    #writes config to file
    outputpath=workdir+'/plotconfig.py'
    print outputpath
    pretty_options = {
        "indent" : 4,
        "width" : 1,
        }

    configstring = """#samples named in the rootfile
samples = {samplestring}

#combined samples
plottingsamples = {plottingsamplesstr}

#systematics to be plotted
systematics = {systematicsstring}

# order of the stack processes, descending from top to bottom
sortedprocesses = {sortedprocstring}

#options for the plotting style
plotoptions = {plotoptionstring}
""".format( samplestring = pprint.pformat(samples, **pretty_options),
            plottingsamplesstr = pprint.pformat(plottingsamples, **pretty_options),
            systematicsstring = pprint.pformat(systematics, **pretty_options),
            sortedprocstring = pprint.pformat(sortedProcesses, **pretty_options),
            plotoptionstring = pprint.pformat(plotinfo, **pretty_options),
            )
    configstring = configstring[:-2] + """,
    # "combineflag" : "shapes_prefit"/"shapes_fit_s",
    # "signallabel" : "Signal"
}
    """
    with open(outputpath,'w') as outfile:
        outfile.write(configstring)
    return outputpath

# creates PlotScript to make plots for a specific channel
def createPlotScript(channel,pyrootdir,workdir,scriptPath,
                        plotconfig,rootfile,selectionlabel,
                        nominal_key = "$PROCESS_$CHANNEL", syst_key = "$PROCESS_$CHANNEL_$SYSTEMATIC"):

    pathtoself=pyrootdir+'/util/'
    cmsswpath = os.environ['CMSSW_BASE']
    script="#!/bin/bash"
    if cmsswpath != '':
        script += """
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
export SCRAM_ARCH={scram_arch}
export OUTFILENAME="{outfilename}"
cd {cmsswpath}/src
eval `scram runtime -sh`
cd - 
""".format(scram_arch = os.environ['SCRAM_ARCH'], outfilename = "plot" +str(channel),
            cmsswpath = cmsswpath)

    script += 'python '+pathtoself+'PlotScript.py --plotconfig="'+plotconfig+'" '
    script += ' --channelname="'+channel+'" '
    script += ' --selectionlabel="'+selectionlabel+'"'
    script += ' --rootfile="'+rootfile+'" '
    script += ' --directory="'+pyrootdir+'"'
    script += ' --systematicfile="'+workdir+"/systematics.csv"+'"' 
    script += ' --workdir="'+workdir+'"\n'


    scriptPath = scriptPath+'makePlots_'+str(channel)+'.sh'

    # write and chmod shell scripts
    with open(scriptPath, "w") as sf:
        sf.write(script)
    st = os.stat(scriptPath)
    os.chmod(scriptPath, st.st_mode | stat.S_IEXEC)
    os.chdir(os.path.dirname(pathtoself))

    return scriptPath
  

