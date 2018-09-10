import sys
import os
import nafSubmit
#############################
# parallel plotting
#############################
def plotInterface(jobData, skipPlotParallel = False, maxTries = 10, nTries = 0):
    if skipPlotParallel:
        jobData = plotTerminationCheck( jobData )
        if len(jobData["scripts"]) > 0 or len(jobData["outputs"]) > 0:
            print("not all plotParallel scripts did terminate successfully - resubmitting")
        else:
            print("all plotParallel scripts have terminated successfully - skipping plotParallel")
            return

    submitOptions = {"PeriodicHold": 4500}
    if nTries == 0:
        print("submitting plotParallel scripts as array job")
        jobIDs = nafSubmit.submitArrayToNAF(jobData["scripts"], "plotPara", submitOptions = submitOptions)
    elif nTries < maxTries:
        print("resubmitting plotParallel scripts as single jobs")
        jobIDs = nafSubmit.submitToNAF(jobData["scripts"], submitOptions = submitOptions)
    else:
        print("plotParallel did not work after "+str(maxTries)+" tries - ABORTING")
        sys.exit(1)

    # monitor running
    nafSubmit.monitorJobStatus(jobIDs) 
    # check fo termination of jobs
    undoneJobData = plotTerminationCheck(jobData)

    if len(undoneJobData["scripts"]) > 0 or len(undoneJobData["outputs"]) > 0:
        return plotInterface( undoneJobData, maxTries = maxTries, nTries = nTries+1 )

    print("plotParallel submit interface has terminated successfully")

def plotTerminationCheck(jobData):
    # counters
    undoneJobData = {}
    undoneJobData["scripts"] = []
    undoneJobData["outputs"] = []
    undoneJobData["entries"] = []
    samplewiseMaps = {}
    noCutflow = 0
    wrongEntry = 0

    for script, output, entries, mapKey in zip(jobData["scripts"], jobData["outputs"], jobData["entries"], jobData["maps"]):
        if os.path.exists(output+".cutflow.txt"):
            cfFile = open(output+".cutflow.txt")
            processedEntries = -1
            for line in cfFile:
                splitLine = line.split(" : ")
                if len(splitLine) > 2 and "all" in splitLine[1]:
                    processedEntries = int(splitLine[2])
                    break
            if entries == processedEntries:
                continue
            else:
                wrongEntry += 1            
        else:
            noCutflow += 1
        
        undoneJobData["scripts"].append( script )
        undoneJobData["outputs"].append( output ) 
        undoneJobData["entries"].append( entries ) 
        samplewiseMaps[mapKey] = jobData["maps"][mapKey]

    undoneJobData["maps"] = samplewiseMaps
    print("-"*50)
    print("done checking job outputs after plotpara - results:")
    print("jobs without cutflow file:     " +str(noCutflow))
    print("jobs with wrong entry in file: " +str(wrongEntry))
    print("-"*50)
    return undoneJobData






#############################
# parallel hadding
#############################
def haddInterface(jobsToSubmit, outfilesFromSubmit, maxTries = 10, nTries = 0):
    if nTries == 0:
        print("submitting haddParallel scripts as array job")
        jobIDs = nafSubmit.submitArrayToNAF(jobsToSubmit, "haddPara")
    elif nTries < maxTries:
        print("resubmitting haddParallel scripts as single jobs")
        jobIDs = nafSubmit.submitToNAF(jobsToSubmit)
    else:
        print("hadding did not work after "+str(maxTries)+" tries - ABORTING")
        sys.exit(1)

    # monitor running
    nafSubmit.monitorJobStatus(jobIDs)
    # check for termination of jobs
    undoneJobs, undoneOutFiles = haddTerminationCheck(jobsToSubmit, outfilesFromSubmit)

    if len(undoneJobs) > 0 or len(undoneOutFiles) > 0:
        return haddInterface( undoneJobs, undoneOutFiles, maxTries, nTries+1 )
    
    print("haddParallel submit interface has terminated successfully")

def haddTerminationCheck(outputScripts, outputFiles):
    # counters
    undoneJobs = []
    undoneOutFiles = []
    noFile = 0
    wrongEntry = 0
    wrongLen = 0

    # looping over jobs to find missing pieces
    for job, jobscript in zip(outputFiles, outputScripts):
        log = job.replace(".root", ".log")
        if os.path.exists(job) and os.path.exists(log):
            with open(log, "r") as logf:
                jobfile = list(logf)
            if len(jobfile) == 1:
                if jobfile[0] == "OK":
                    continue
                else:
                    wrongEntry += 1
            else:
                wrongLen += 1
        else:
            noFile += 1

        undoneJobs.append(jobscript)
        undoneOutFiles.append(job)

    print("-"*50)
    print("done checking job outputs after haddpara - results:")
    print("jobs without log file:       " + str(noFile))
    print("jobs with wrong log file:    " +str(wrongLen))
    print("jobs with ERROR in log file: " + str(wrongEntry))
    print("-"*50)
    return undoneJobs, undoneOutFiles


    



#############################
# renaming histos
#############################
def renameInterface(jobsToSubmit, outfilesFromSubmit, maxTries = 10, nTries = 0):
    # shellList = renamescriptlist = listOfJobsToSubmit
    # outFileList = outnamelist = listOfJobOutFilesToGetFromSubmit
    if len(jobsToSubmit) != len(outfilesFromSubmit):
        print("number of jobs should be equal to number of output files - ABORTING")
        sys.exit(1)

    if nTries == 0:
        print("submitting rename scripts as array job")
        jobIDs = nafSubmit.submitArrayToNAF(jobsToSubmit, arrayName = "renamePara")
    elif nTries < maxTries:
        print("resubmitting rename scripts as single jobs")
        jobIDs = nafSubmit.submitToNAF(jobsToSubmit)
    else:
        print("renaming did not work after "+str(maxTries)+" tries - ABORTING")
        sys.exit(1)

    # monitor running of jobs
    nafSubmit.monitorJobStatus(jobIDs)
    # checking for undone jobs
    undoneJobs, undoneFiles = renameTerminationCheck(jobsToSubmit, outfilesFromSubmit)

    if len(undoneJobs) > 0 or len(undoneFiles) > 0:
        return renameInterface(undoneJobs, undoneFiles, maxTries, nTries+1)

    print("renamingHistos submit interface has terminated successfully")

def renameTerminationCheck(shellScripts, outputFiles):
    # count undone jobs
    undoneJobs = []
    undoneOutFiles = []
    noFile = 0

    for job, outFile in zip(shellScripts, outputFiles):
        if not os.path.exists(outFile):
            noFile += 1
            undoneJobs.append( job )
            undoneOutFiles.append( outFile )

    print("-"*50)
    print("done checking job outputs after renaming histos - results:")
    print("jobs without output file: " + str(noFile))
    print("-"*50)
    return undoneJobs, undoneOutFiles





#############################
# making datacards
#############################
def datacardInterface(jobsToSubmit, datacardFiles, maxTries = 10, nTries = 0):
    if nTries == 0:
        print("submitting datacardmaking scripts as array job")
        jobIDs = nafSubmit.submitArrayToNAF(jobsToSubmit, arrayName = "cardmakingPara")
    elif nTries < maxTries:
        print("resubmitting datacardmaking scripts as single jobs")
        jobIDs = nafSubmit.submitToNAF(jobsToSubmit)
    else:
        print("making datacards did not work after "+str(maxTries)+" tries -ABORTING")
        sys.exit(1)

    # monitoring running of jobs
    nafSubmit.monitorJobStatus(jobIDs)
    # checking output
    undoneJobs, undoneCards = datacardTerminationCheck(jobsToSubmit, datacardFiles)

    if len(undoneCards) > 0 or len(undoneJobs) > 0:
        return datacardInterface(undoneShells, undoneCards, maxTries, nTries+1)
    
    print("makingDatacards submit interface has terminated successfully")

def datacardTerminationCheck(shellScripts, datacardFiles):
    undoneJobs = []
    undoneCards = []
    noCard = 0

    for job, card in zip(shellScripts, datacardFiles):
        if not os.path.exists(card):
            noCard += 1
            undoneJobs.append( job )
            undoneCards.append( card )

    print("-"*50)
    print("done checking job outputs after making datacards - results:")
    print("jobs without datacard file: " + str(noCard))
    print("-"*50)
    return undoneJobs, undoneCards





#############################
# parallel drawing
#############################
def drawInterface(jobsToSubmit, outputPlots, nTries = 0):
    if nTries == 0:
        print("submitting drawParallel scripts as array job")
        jobIDs = nafSubmit.submitArrayToNAF(jobsToSubmit, "drawPara")
    elif nTries < maxTries:
        print("resubmitting drawParallel scripts as single jobs")
        jobIDs = nafSubmit.submitToNAF(jobsToSubmit)
    else:
        print("draw parallel did not work after "+str(maxTries)+" tries - ABORTING")
        sys.exit(1)
    
    # monitoring running jobs
    nafSubmit.monitorJobStatus(jobIDs)
    # checking output
    undoneScripts, undonePlots = drawTerminationCheck(jobsToSubmit, outputPlots)

    if len(undoneScripts) > 0 or len(undonePlots) > 0:
        return drawInterface(undoneScripts, undonePlots, maxTries, nTries+1)

    print("drawParallel submit interface has terminated successfully")

def drawTerminationCheck(jobsToSubmit, outputPlots):
    print("no check for the termination of draw Parallel has been implemented yet...")
    undoneJobs = []
    undonePlots = []
    return undoneJobs, undonePlots




