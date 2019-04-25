import sys
import os
import stat

# local imports
filedir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(filedir+"/tools")
import nafInterface


# -- script for parallel drawing ------------------------------------------------------------------
def drawParallel(ListOfPlots, workdir, PathToSelf, opts=None):
    print("PathToSelf:" +str(PathToSelf))

    ListOfScripts = []

    # create output folders
    print('creating output folders')
    scriptPath = workdir+'/DrawScripts/'
    if not os.path.exists(scriptPath):
        os.makedirs(scriptPath)

    print "Creating Scripts for Parallel Drawing"
    for iPlot, Plot in enumerate(ListOfPlots):
        ListOfScripts.append( createDrawScript(iPlot, Plot, PathToSelf, scriptPath, opts=None) )

    print "Submitting ", len(ListOfScripts), " DrawScripts"
    nafInterface.drawInterface(ListOfScripts, ListOfPlots)

    return
# -------------------------------------------------------------------------------------------------
    




# -- create a single draw script ------------------------------------------------------------------
def createDrawScript(iPlot, Plot, PathToSelf, scriptPath, opts=None):
    
    cmsswpath = "/cvmfs/cms.cern.ch/slc6_amd64_gcc530/cms/cmssw-patch/CMSSW_8_0_26_patch2"
    script="#!/bin/bash \n"
    if cmsswpath != '':
        script += "export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch \n"
        script += "source $VO_CMS_SW_DIR/cmsset_default.sh \n"
        script += "export SCRAM_ARCH="+"slc6_amd64_gcc530"+"\n"
        script += 'export OUTFILENAME="'+"plot" +str(iPlot)+'"\n'
        script += 'cd '+cmsswpath+'/src\n'
        script += 'eval `scram runtime -sh`\n'
        script += 'cd - \n'

    # Parse commandline options if available to script    
    commandLineOptions = ''
    if opts != None:
        for opt, arg in opts:
            if arg != None:
                commandLineOptions = commandLineOptions + ' ' + opt + '=' + arg
            else:
                commandLineOptions = commandLineOptions + ' ' + opt

    script += 'python '+PathToSelf+" -p "+str(iPlot)+ ' ' + commandLineOptions + ' noPlotParallel\n'

    scriptPath = scriptPath+'DrawParallel'+str(iPlot)+'.sh'
    
    # write and chmod shell scripts
    with open(scriptPath, "w") as sf:
        sf.write(script)
    st = os.stat(scriptPath)
    os.chmod(scriptPath, st.st_mode | stat.S_IEXEC)
    os.chdir(os.path.dirname(PathToSelf))

    return scriptPath
# -------------------------------------------------------------------------------------------------



