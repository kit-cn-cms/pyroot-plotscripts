import sys
import os
import stat
import json
import configClass as configClass
import analysisClass as analysisClass

filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = "/".join(filedir.split("/")[:-1])

sys.path.append(pyrootdir+"/configs")
sys.path.append(filedir+"/tools")
import nafInterface



def makePlots(configData):

    ListOfPlots     = configData.getDiscriminatorPlots()
    workdir         = configData.analysis.workdir
    pyrootdir       = configData.analysis.pyrootdir
    plotconfig      = createPlotConfig(configData,workdir)
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
                                                    selectionlabel=Plot.label) )


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
def createPlotConfig(configData,workdir):
    #get plotting information
    signalScaling       = configData.analysis.signalScaling
    lumiLabel           = configData.analysis.lumiLabel
    if lumiLabel:
        if isinstance(lumiLabel,bool):
            lumiLabel   = configData.analysis.getLumi()
    cmslabel            = configData.analysis.cmslabel
    normalize           = configData.analysis.normalize
    ratio               = configData.analysis.ratio
    logarithmic         = configData.analysis.logarithmic
    splitLegend         = configData.analysis.splitLegend
    shape               = configData.analysis.shape
    sortedProcesses     = configData.pltcfg.sortedProcesses

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
        

    #systematics to be plotted
    systematics=configData.plots
    print systematics

    #writes config to file
    outputpath=workdir+'/plotconfig.py'
    print outputpath

    with open(outputpath,'w') as outfile:
        outfile.write('#samples named in the rootfile\n')
        outfile.write('samples = {\n')
        for key, value in samples.items():
            outfile.write(" "*8)
            if not value["plot"]: outfile.write("#") 
            outfile.write('"%s":%s,\n' % (key, value["info"]))
        outfile.write(' '*4+'}\n')
        outfile.write('\n')
        outfile.write('#combined samples\n')
        outfile.write('plottingsamples = {\n')
        for key, value in plottingsamples.items():
            outfile.write(' '*8+'"%s":%s,\n' % (key, value))
        outfile.write(' '*4+'}\n')
        outfile.write('\n')
        outfile.write('#systematics to be plotted\n')
        outfile.write('systematics = [\n')
        for systematic in systematics:
            if systematic.startswith('#'):
                systematic.replace('#','')
                outfile.write(' '*8+'#"'+systematic+'",\n')
            else:
                outfile.write(' '*8+'"'+systematic+'",\n')
        outfile.write(' '*4+']\n')
        outfile.write('\n')

        outfile.write('# order of the stack processes, descending from top to bottom\n')      
        outfile.write('sortedprocesses='+str(sortedProcesses)+'\n')
        outfile.write('\n')

        outfile.write('#options for the plotting style\n')
        outfile.write('plotoptions = {\n')

        outfile.write(' '*4+'# "pdftag":"matti_schrode_KIT_cool",\n')

        outfile.write('\n')
        outfile.write(' '*4+'"data":"data_obs",\n')

        outfile.write('\n')
        outfile.write(' '*4+'"ratio":"'+str(ratio)+'",\n')
        outfile.write(' '*4+'"logarithmic":'+str(logarithmic)+',\n')
        outfile.write(' '*4+'"shape":'+str(shape)+',\n')
        outfile.write(' '*4+'"normalize":'+str(normalize)+',\n')

        outfile.write('\n')
        outfile.write(' '*4+'"signalscaling":'+str(signalScaling)+',\n')
        outfile.write(' '*4+'"lumilabel":'+str(lumiLabel)+',\n')
        outfile.write(' '*4+'"cmslabel":"'+str(cmslabel)+'",\n')
        outfile.write(' '*4+'"splitlegend":'+str(splitLegend)+',\n')
        outfile.write(' '*4+'"datalabel":"data",\n')
        outfile.write(' '*4+'"statErrorband": True,\n')
    
        outfile.write('\n')
        outfile.write(' '*4+'#use for combine plots, use shapes_prefit for prefit and shapes_fit_s for post fit\n')
        outfile.write(' '*4+'#only uses total signal and does not split signal processes\n')
        outfile.write('\n')
        outfile.write(' '*4+'# "combineflag":"shapes_prefit"/"shapes_fit_s",\n')
        outfile.write(' '*4+'# "signallabel":"Signal",\n')

        outfile.write(' '*4+'}\n')

    return outputpath

# creates PlotScript to make plots for a specific channel
def createPlotScript(channel,pyrootdir,workdir,scriptPath,
                        plotconfig,rootfile,selectionlabel):

    pathtoself=pyrootdir+'/util/'
    cmsswpath = os.environ['CMSSW_BASE']
    script="#!/bin/bash \n"
    if cmsswpath != '':
        script += "export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch \n"
        script += "source $VO_CMS_SW_DIR/cmsset_default.sh \n"
        script += "export SCRAM_ARCH="+os.environ['SCRAM_ARCH']+"\n"
        script += 'export OUTFILENAME="'+"plot" +str(channel)+'"\n'
        script += 'cd '+cmsswpath+'/src\n'
        script += 'eval `scram runtime -sh`\n'
        script += 'cd - \n'

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
  

