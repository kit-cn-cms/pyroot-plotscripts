import sys
import os
import subprocess
import datetime
import stat
import ROOT
import glob
import imp 
import types

# local imports
import nafSubmit

def drawParallel(ListOfPlots,workdir,PathToSelf,opts=None):
    ListofScripts=[]
    # create output folders
    print 'creating output folders'
    scriptsfolder=workdir+'/DrawScripts/'
    if not os.path.exists(scriptsfolder):
        os.makedirs(scriptsfolder)

    print "Creating Scripts for Parallel Drawing"
    for iPlot, Plot in enumerate(ListOfPlots):
        ListofScripts.append(createSingleDrawScript(iPlot,Plot,PathToSelf,scriptsfolder,opts=None))

    print "Submitting ", len(ListofScripts), " DrawScripts"
    # print ListofScripts
    # jobids=nafSubmit.submitToNAF(["DrawScripts/DrawParallel0.sh"])
    #jobids=nafSubmit.submitToNAF(ListofScripts)
    jobids=nafSubmit.submitArrayToNAF(ListofScripts,"DrawPara")
    print jobids
    nafSubmit.do_qstat(jobids)


def createSingleDrawScript(iPlot,Plot,PathToSelf,scriptsfolder,opts=None):
    # print "still needs to be implemented"
    cmsswpath=os.environ['CMSSW_BASE']
    script="#!/bin/bash \n"
    if cmsswpath!='':
        script+="export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch \n"
        script+="source $VO_CMS_SW_DIR/cmsset_default.sh \n"
        script+="export SCRAM_ARCH="+os.environ['SCRAM_ARCH']+"\n"
        script+='export OUTFILENAME="'+"plot" +str(iPlot)+'"\n'
        script+='cd '+cmsswpath+'/src\neval `scram runtime -sh`\n'
        script+='cd - \n'
    # Parse commandline options if available to script    
    commandLineOptions = ''
    if opts != None:
        for opt, arg in opts:
            if arg != None:
                commandLineOptions = commandLineOptions + ' ' + opt + '=' + arg
            else:
                commandLineOptions = commandLineOptions + ' ' + opt
    script+='python '+PathToSelf+" -p "+str(iPlot)+ ' ' + commandLineOptions + ' noPlotParallel\n'
    # script+="mv *.pdf " +os.getcwd()+"/plot"+str(iPlot)+".pdf\n"


    scriptname=scriptsfolder+'DrawParallel'+str(iPlot)+'.sh'

    # path = os.getcwd()+"/DrawScripts" 
    # if not os.path.exists(path):
    #     os.makedirs(path)
    # os.chdir(path)
    
    f=open(scriptname,'w')
    f.write(script)
    f.close()
    st = os.stat(scriptname)
    os.chmod(scriptname, st.st_mode | stat.S_IEXEC)
    os.chdir(os.path.dirname(PathToSelf))

    # PathToShellScript=path+scriptname
    # return PathToShellScript
    # return "DrawScripts/"+scriptname
    return scriptname




def askYesNo(question):
    print question
    yes = set(['yes','y', 'ye', ''])
    no = set(['no','n'])
    choice = raw_input().lower()
    if choice in yes:
        return True
    elif choice in no:
        return False
    else:
        print "Please respond with 'yes' or 'no'"
        return askYesNo(question)
