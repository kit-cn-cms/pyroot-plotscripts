import sys
import os
import stat

# local imports
sys.path.append("tools")
import nafSubmit


# -- script for parallel drawing ------------------------------------------------------------------
def drawParallel(ListOfPlots, workdir, PathToSelf, opts=None):

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
    drawingSubmitInterface(ListOfScripts, ListOfPlots)

    return
# -------------------------------------------------------------------------------------------------
    


# -- interface for communicating with batch -------------------------------------------------------
def drawingSubmitInterface(ListOfScripts, ListOfPlots, nTries = 0):
    if nTries == 0:
        jobIDs = nafSubmit.submitArrayToNAF(ListOfScripts, "DrawPara")
        nafSubmit.do_qstat(jobIDs)
    elif nTries < 3:
        jobIDs = nafSubmit.submitToNAF(ListOfScripts)
        nafSubmit.do_qstat(jobIDs)
    else:
        print("draw parallel did not work after 3 tries - ABORTING")
        sys.exit(1)

    print("-"*50)
    print("check if draw parallel was terminated successfully")
    print("TODO") # TODO
    print("-"*50)
    if False:
        drawingSubmitInterface(ListOfScripts, ListOfPlots, nTries+1 )
    else:
        print("draw parallel terminated successfully")
        return
# -------------------------------------------------------------------------------------------------



# -- create a single draw script ------------------------------------------------------------------
def createDrawScript(iPlot, Plot, PathToSelf, scriptPath, opts=None):
    
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



