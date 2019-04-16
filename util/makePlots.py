import sys
import os

filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = "/".join(filedir.split("/")[:-1])

sys.path.append(pyrootdir+"/configs")




def makePlots(ListOfPlots, workdir):

    print ListOfPlots
    print('creating output folders')
    scriptPath = workdir+'/DrawScripts/'
    #if not os.path.exists(scriptPath):
    #    os.makedirs(scriptPath)
    ListOfScripts = []
    #print('Creating Scripts for Parallel Drawing')
    for iPlot, Plot in enumerate(ListOfPlots):
        print "-"*130
        print iPlot
        print Plot
        print Plot.name
        print Plot.histo
        print Plot.variable
        print Plot.selection
        print Plot.label
        #ListOfScripts.append( createDrawScript(iPlot, Plot, scriptPath, opts=None) )

    #print "Submitting ", len(ListOfScripts), " DrawScripts"
    #nafInterface.drawInterface(ListOfScripts, ListOfPlots)

    return

def createDrawScript(iPlot, Plot, scriptPath, opts=None):
    
    cmsswpath = os.environ['CMSSW_BASE']
    script="#!/bin/bash \n"
    if cmsswpath != '':
        script += "export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch \n"
        script += "source $VO_CMS_SW_DIR/cmsset_default.sh \n"
        script += "export SCRAM_ARCH="+os.environ['SCRAM_ARCH']+"\n"
        script += 'export OUTFILENAME="'+"plot" +str(iPlot)+'"\n'
        script += 'cd '+cmsswpath+'/src\n'
        script += 'eval `scram runtime -sh`\n'
        script += 'cd - \n'

    script += 'python '+scriptPath+" -p "+str(iPlot)+ ' '  + ' noPlotParallel\n'

    scriptPath = scriptPath+'DrawParallel'+str(iPlot)+'.sh'
    print script

