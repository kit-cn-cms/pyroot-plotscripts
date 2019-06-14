import sys
import os
import stat
import configClass as configClass
import analysisClass as analysisClass

filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = "/".join(filedir.split("/")[:-1])

sys.path.append(pyrootdir+"/configs")
sys.path.append(filedir+"/tools")
import nafInterface



def makePlots(configData):
    # get Information from configData
    ListOfPlots     = configData.getDiscriminatorPlots()
    workdir         = configData.analysis.workdir
    config          = configData.analysis.plotConfig
    syst_config     = configData.systconfig
    pyrootdir       = configData.analysis.pyrootdir
    rootfile        = configData.analysis.rootPath
    signalScaling   = configData.analysis.signalScaling
    lumiLabel       = configData.analysis.lumiLabel
    privateWork     = configData.analysis.privateWork
    ratio           = configData.analysis.ratio
    logarithmic     = configData.analysis.logarithmic

    # create output folders
    print('creating output folders')
    scriptPath = workdir+'/PlotScripts/'
    if not os.path.exists(scriptPath):
        os.makedirs(scriptPath)

    ListOfScripts = []
    #print('Creating Scripts for Parallel Drawing')
    for Plot in ListOfPlots:
        print "-"*130
        print Plot.name
        ListOfScripts.append( createPlotScript(channel=Plot.name,pyrootdir=pyrootdir, 
        										workdir=workdir, scriptPath=scriptPath,
                                                plotconfig=config, systconfig=syst_config,
                                                rootfile=rootPath, signalScaling=signalScaling,
                                                lumiLabel=lumiLabel, privateWork=privateWork,
                                                ratio=ratio, logarithmic=logarithmic ) )

    print "Submitting ", len(ListOfScripts), " DrawScripts"
    nafInterface.drawInterface(ListOfScripts, ListOfPlots)

    return

def createPlotScript(channel,pyrootdir,workdir,scriptPath,
                        plotconfig,systconfig,rootfile,signalScaling,
                        lumiLabel,privateWork,ratio,logarithmic):
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
    script += ' --rootfile="'+rootfile+'" '
    script += ' --directory="'+pyrootdir+'"' 
    script += ' --workdir="'+workdir+'"' 
    script += ' --systconfig="'+systconfig+'"'
    script += ' --signalscaling="'+signalScaling+'"'
    script += ' --lumilabel="'+lumiLabel+'"'
    script += ' --privatework="'+privateWork+'"'
    script += ' --ratio="'+ratio+'"'
    script += ' --logarithmic="'+logarithmic+'"\n'

    scriptPath = scriptPath+'makePlots'+str(channel)+'.sh'

    # write and chmod shell scripts
    with open(scriptPath, "w") as sf:
        sf.write(script)
    st = os.stat(scriptPath)
    os.chmod(scriptPath, st.st_mode | stat.S_IEXEC)
    os.chdir(os.path.dirname(pathtoself))

    return scriptPath
  

