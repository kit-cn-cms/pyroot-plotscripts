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
    ListOfPlots=configData.getDiscriminatorPlots()
    workdir=configData.analysis.workdir
    config=configData.analysis.plotConfig
    #plot_config=configData.plot_config
    syst_config=configData.systconfig
    pyrootdir=configData.analysis.pyrootdir

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
        										workdir=workdir, scriptPath=scriptPath,plotconfig=config,
        										systconfig=syst_config) )

    print "Submitting ", len(ListOfScripts), " DrawScripts"
    nafInterface.drawInterface(ListOfScripts, ListOfPlots)

    return

def createPlotScript(channel,pyrootdir,workdir,scriptPath,plotconfig,systconfig):
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
    script += ' --rootfile="/nfs/dust/cms/user/lreuter/forPhilip/plotscript/workdir/csvConfigAll/output_limitInput.root" '
    script += ' --directory="'+pyrootdir+'"' 
    script += ' --workdir="'+workdir+'"' 
    script += ' --systconfig="'+systconfig+'"\n'

    scriptPath = scriptPath+'makePlots'+str(channel)+'.sh'

    # write and chmod shell scripts
    with open(scriptPath, "w") as sf:
        sf.write(script)
    st = os.stat(scriptPath)
    os.chmod(scriptPath, st.st_mode | stat.S_IEXEC)
    os.chdir(os.path.dirname(pathtoself))

    return scriptPath
  

