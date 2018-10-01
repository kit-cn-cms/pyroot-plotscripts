import ROOT
import numpy as np
import os
from copy import deepcopy
import array

def optimizeBinning(infname, signalsamples = [], backgroundsamples = [], additionalSamples = [], plots = [], 
                    systnames = [""], minBkgPerBin = 2.0, optMode = "SoverB",
                    considerStatUnc = False, maxBins = 100, minBins = 1, verbosity = 0):

    if len(signalsamples) == 0 or len(backgroundsamples) == 0:
        print "You called optimizeBinning without any samples. Not Reasonable. Sad!."
        exit(0)
    
    # copy existing ROOT file as a backup we will write stuff into the existing file name
    cmd = 'cp '+ infname + ' ' + infname.replace(".root", "_preRebinning.root")
    print("copying existing ROOT file as backup:")
    print(cmd)
    os.system(cmd)
    
            
    theclock = ROOT.TStopwatch()
    theclock.Start()
    theobjectlist = [] # dummy list to keep destructors from being called
    ROOT.gDirectory.cd('PyROOT:/')
    
    infile = ROOT.TFile(infname[:-5] + '_preRebinning.root',"READONLY")
    outfile = ROOT.TFile(infname,"RECREATE")    
            
    # loop over plots
    for plot in plots:
        theSignalClone = None
        theBkgClone = None

        #add signal samples
        sName = signalsamples[0].nick+'_'+plot.name
        print("getting " + str(sName))
        
        s0 = infile.Get(sName)
        theobjectlist.append(s0)
        theSignalClone = s0.Clone('signalClone_'+sName)

        for ss in signalsamples[1:]:
            sName = ss.nick+"_"+plot.name
            sx = infile.Get(sName)
            theobjectlist.append(sx)
            theSignalClone.Add(sx)

        #add background samples
        bName = backgroundsamples[0].nick+'_'+plot.name
        b0 = infile.Get(bName)
        theobjectlist.append(b0)
        theBkgClone = b0.Clone('backgroundClone_'+bName)

        for bs in backgroundsamples[1:]:
            bName = bs.nick+'_'+plot.name
            bx = infile.Get(bName)
            theobjectlist.append(bx)
            theBkgClone.Add(bx)

        if theSignalClone == None or theBkgClone == None:
            print "no histograms found for this:"
            print plot.name
            exit(0)

        theSignalClone.SetDirectory(0)
        theBkgClone.SetDirectory(0)
        theoptimizedBinEdges = getOptimizedBinEdges(theSignalClone, theBkgClone, optMode, 
                                            minBkgPerBin, maxBins, minBins, 
                                            considerStatUnc, verbosity)
        theBinEdgeArray = array.array("f",theoptimizedBinEdges)

        print "optimized bin edges for ", plot.name
        print theoptimizedBinEdges
        binninTextFile = open(infname[:-5]+'_binning.txt',"a")
        binninTextFile.write(plot.name+" : "+str(theoptimizedBinEdges)+"\n")
        binninTextFile.close()
        
        print "doing the rebinning for plot ", plot.name
        for sample in signalsamples+backgroundsamples+additionalSamples:
            for syst in systnames:
                ROOT.gDirectory.cd('PyROOT:/')
                key = sample.nick+'_'+plot.name+syst

                if verbosity >= 2:
                    print "at ", key

                thisHistoPreRebinning = infile.Get(key)
                if thisHistoPreRebinning == None:
                    continue

                thisHistoPreRebinning.SetDirectory(0)
                theobjectlist.append(thisHistoPreRebinning)
                outfile.cd()
                thisHistoPostRebinning = None

                if isinstance(thisHistoPreRebinning,ROOT.TH1D):
                    thisHistoPostRebinning = ROOT.TH1D(thisHistoPreRebinning.GetName(),
                                                thisHistoPreRebinning.GetTitle(),
                                                len(theoptimizedBinEdges)-1,
                                                theBinEdgeArray)
                elif isinstance(thisHistoPreRebinning,ROOT.TH1F):
                    thisHistoPostRebinning = ROOT.TH1F(thisHistoPreRebinning.GetName(),
                                                thisHistoPreRebinning.GetTitle(),
                                                len(theoptimizedBinEdges)-1,
                                                theBinEdgeArray)
                else:
                    print "not a supported histogram type", thisHistoPreRebinning
                    continue

                theobjectlist.append(thisHistoPostRebinning)
                thisHistoPostRebinning.SetDirectory(0)
                thisHistoPostRebinning.SetLineColor(thisHistoPreRebinning.GetLineColor())
                thisHistoPostRebinning.SetFillColor(thisHistoPreRebinning.GetFillColor())

                # now do the rebinning
                nbinsPre = thisHistoPreRebinning.GetNbinsX()
                for ibin in range(nbinsPre+2):
                    # find new bin
                    oldbincenter = thisHistoPreRebinning.GetBinCenter(ibin)
                    newbin = thisHistoPostRebinning.FindBin(oldbincenter)

                    # add bin contents
                    thisHistoPostRebinning.SetBinContent(newbin, 
                        thisHistoPostRebinning.GetBinContent(newbin)+thisHistoPreRebinning.GetBinContent(ibin))

                    # add errors
                    newbinerror = ROOT.TMath.Sqrt(
                        thisHistoPostRebinning.GetBinError(newbin)*thisHistoPostRebinning.GetBinError(newbin) + \
                        thisHistoPreRebinning.GetBinError(ibin)*thisHistoPreRebinning.GetBinError(ibin))
                    thisHistoPostRebinning.SetBinError(newbin, newbinerror)
                # now save in outfile
                outfile.cd()
                thisHistoPostRebinning.Write("",ROOT.TObject.kOverwrite)
        print "done with the rebinning for plot", plot.name
    
    outfile.Close()
            
    print "done witht the binning optimization"                    



def getEqualBinWidths(signalHisto, bkgHisto, minBkgPerBin, maxBins, minBins, verbosity = 0):
        nBinsOriginal = signalHisto.GetNbinsX()

        binLowEdgesOriginal = [signalHisto.GetBinLowEdge(i) for i in range(1, nBinsOriginal+2)]

        bkgBinContentsOriginal = [bkgHisto.GetBinContent(i) for i in range(1, nBinsOriginal+1)]
        sumBinContentsOriginal = [signalHisto.GetBinContent(i) + bkgHisto.GetBinContent(i) for i in range(1, nBinsOriginal+1)]

        minBorderBin = next((i for i, x in enumerate(sumBinContentsOriginal)           if x > 0))
        maxBorderBin = next((len(sumBinContentsOriginal) - 1 - i for i, x in enumerate(reversed(sumBinContentsOriginal)) if x > 0))

        borderBins = np.linspace(minBorderBin, maxBorderBin+1, minBins+1, endpoint=True, dtype=np.int)

        for i in range(minBins):
            bkgBinContents = [sum(bkgBinContentsOriginal[borderBins[j]:borderBins[j+1]]) for j in range(minBins)]
            if bkgBinContents[i] >= minBkgPerBin:
                firstEqualWidthBinLeft = i
                break

            while bkgBinContents[i] < minBkgPerBin:
                borderBins[i+1] += 1
                bkgBinContents = [sum(bkgBinContentsOriginal[borderBins[j]:borderBins[j+1]]) for j in range(minBins)]

            borderBins = np.concatenate([borderBins[:i+1], 
                np.linspace(borderBins[i+1], maxBorderBin + 1, minBins - i, endpoint=True, dtype=np.int)])

        for i in reversed(range(minBins)):
            bkgBinContents = [sum(bkgBinContentsOriginal[borderBins[j]:borderBins[j+1]]) for j in range(minBins)]
            if bkgBinContents[i] >= minBkgPerBin:
                break

            while bkgBinContents[i] < minBkgPerBin:
                borderBins[i] -= 1
                bkgBinContents = [sum(bkgBinContentsOriginal[borderBins[j]:borderBins[j+1]]) for j in range(minBins)]

            borderBins = np.concatenate(
                [borderBins[:firstEqualWidthBinLeft], 
                    np.linspace(borderBins[firstEqualWidthBinLeft], 
                                borderBins[i], i-firstEqualWidthBinLeft, 
                                endpoint=False, dtype=np.int), borderBins[i:]])

        listOfBinLowEdges = [binLowEdgesOriginal[i] for i in borderBins]

        return listOfBinLowEdges


def getOptimizedBinEdges(signalHisto, bkgHisto, optMode = "SoverB", minBkgPerBin = 2.0, 
                            maxBins = 100, minBins = 1, considerStatUnc = False, verbosity=0):

    if signalHisto.GetNbinsX() != bkgHisto.GetNbinsX():
        print "ERROR: getOptimizedBinEdges: signal and background histograms have different binnings!"
        exit(0)

    if minBins > maxBins:
        print "you want minbins > maxBins"
        exit(0)

    if optMode == "equalBinWidth":
        return getEqualBinWidths(signalHisto, bkgHisto, minBkgPerBin, maxBins, minBins, verbosity)

    def getSoverB(S,B):
        if B > 0:
            return S/float(B)
        elif S > 0:
            return 99999.9
        else:
            return 0.0
        
    def getSignificance(S,B):
        if (S+B) > 0:
            return S/ROOT.TMath.Sqrt(S+B)
        elif S > 0:
            return 99999.9
        else:
            return 0.0
        
    def mergeBins(bin1, bin2, pointerToFoM, verbosity=0):
        # array has form [[bincontentsSignal,binErrorsSignal,bincontentsBackgound,binErrorsBackground, binlowedges, binwidths,FigureOfMerit,lookAt]]
        retbin = [ 
            bin1[0] + bin2[0],    # combine bin contents for signal
            float(ROOT.TMath.Sqrt(bin1[1]*bin1[1] + bin2[1]*bin2[1])), # combine stat uncertainties for signal 
            bin1[2] + bin2[2],    # combine bin contents for bkg
            float(ROOT.TMath.Sqrt(bin1[3]*bin1[3] + bin2[3]*bin2[3])), # combine stat uncertainties for bkg
            min(bin1[4], bin2[4]), # low edge of both bins
            bin1[5] + bin2[5],    # combine bin width
            getFom(bin1[0] + bin2[0], bin1[2] + bin2[2]),
            1.0 # reset is already good flag
            ]

        if verbosity >= 3:
            print "combined bins ", bin1, bin2
            print "to ", retbin
        return retbin
    
    getFom = None
    if optMode == "SoverB":
        getFom = getSoverB
    elif optMode == "Significance":
        getFom = getSignificance
    else:
        print "unknown optimization mode"
        exit(0)
    
    if considerStatUnc:
        print "Considering statistical uncertainty not yet implemented! Ignoring your wishes for now!"
    
    # TODO Think about including systematic shapes so that underfluctuations are covered by binning
    
    # get array representing the histograms
    # array has form [[bincontentsSignal,binErrorsSignal,bincontentsBackgound,binErrorsBackground, binlowedges, binwidths,FigureOfMerit, lookAt]]
    theArray = []
    
    nBinsOriginal = signalHisto.GetNbinsX()
        
    for ibin in range(nBinsOriginal+2): # ibin=0=underflow; ibin+1=last bin; bin nBinsOriginal+2 = overflow
        if verbosity >= 2:
            print "reading signal ", signalHisto.GetName()
            print "iBin, Content", ibin, signalHisto.GetBinContent(ibin)
            print "reading background ", bkgHisto.GetName()
            print "iBin, Content", ibin, bkgHisto.GetBinContent(ibin)
        theArray.append([signalHisto.GetBinContent(ibin), 
                        signalHisto.GetBinError(ibin), 
                        bkgHisto.GetBinContent(ibin), 
                        bkgHisto.GetBinError(ibin), 
                        signalHisto.GetBinLowEdge(ibin), 
                        signalHisto.GetBinWidth(ibin), 
                        getFom(signalHisto.GetBinContent(ibin),bkgHisto.GetBinContent(ibin)), 1])
    
    # make deep copy of original binning
    sarraycopy = deepcopy(theArray)
    
    # now cluster the bins together to get at least minimal background events into each bin
    clusteringDone = False
    nbins = len(theArray)
    if verbosity >= 2:
        print "array before any merging"
        print theArray
    niterations = 0
    while clusteringDone == False:
        niterations += 1
        nbins = len(theArray)
        if verbosity >= 2:
            print "Current nbins after iteration ", niterations, " : ", nbins
        if len(theArray) <= minBins:
            if verbosity >= 2:
                print "reached minimal number of bins", minBins
                break
        # find bin with highest Figure
        imax = zip(*theArray)[6].index(max(zip(*theArray)[6]))

        # in case there are multiple bins with highest FoM start from the rightmost one 
        if zip(*theArray)[6].count(max(zip(*theArray)[6])) > 1:	
            imax = len(theArray) - 1 - list(reversed(zip(*theArray)[6])).index(max(zip(*theArray)[6]))

        print "considering bin", imax, theArray[imax]

        # enough bkg?
        hasMinBkg = theArray[imax][2] > minBkgPerBin

        # large enough to allow for downfluctuation?
        canDownFluctuate = ( (theArray[imax][2]+theArray[imax][0]) - (theArray[imax][1]+theArray[imax][3]) ) >= 0.0

        # if we want to allow down fluctuation lets assume that we just do not have enought bkg in the bin
        if considerStatUnc == True and canDownFluctuate == False:
            hasMinBkg = False

        # would merging with neighbouring bin increase FoM?
        mergeRightIncreasesFoM = 0
        mergeLeftIncreasesFoM = 0
        hypotheticalBinLeft = []
        hypotheticalBinRight = []

        if imax != 0: # not the leftmost bin (underflow)
            hypotheticalBinLeft = mergeBins( theArray[imax-1], theArray[imax], getFom, verbosity )
            mergeLeftIncreasesFoM = hypotheticalBinLeft[6] - getFom( theArray[imax][0], theArray[imax][2] )

        if imax!=nbins-1: # not the rightmost bin (overflow)
            hypotheticalBinRight = mergeBins( theArray[imax+1], theArray[imax], getFom, verbosity )
            mergeRightIncreasesFoM = hypotheticalBinRight[6] - getFom( theArray[imax][0], theArray[imax][2] )
        
        if hasMinBkg and (mergeLeftIncreasesFoM <= 0 and mergeRightIncreasesFoM <= 0):
        # enough bkg in bin and no increase of FoM by merging
        # nothing to do then
        # Set FoM to -1
            theArray[imax][6] = -1
            if verbosity >= 2:
                print "bin does not need to be merged at the moment", imax, theArray[imax]

        else:
            # we either need more bkg or the merge increases the FoM
            if verbosity >= 2:
                print "merging bin ", imax, theArray[imax]
                print "with"
            if (mergeRightIncreasesFoM >= mergeLeftIncreasesFoM and imax != nbins-1) or (imax == 0):
                # right merge is better or left merge not possible
                if verbosity >= 2:
                    print "right bin", theArray[imax+1]
                    print "resulting bin", hypotheticalBinRight
                del theArray[imax+1]
                del theArray[imax]
                theArray.insert(imax, hypotheticalBinRight)
            elif (mergeLeftIncreasesFoM > mergeRightIncreasesFoM and imax != 0) or (imax == nbins-1):
                # left merge is better or right merge not possible
                if verbosity >= 2:
                    print "left bin", theArray[imax-1]
                    print "resulting bin", hypotheticalBinLeft
                del theArray[imax]
                del theArray[imax-1]
                theArray.insert(imax-1, hypotheticalBinLeft)
    
        # if all bins have been sufficiently merged all should have FoMs of -1
        if max(zip(*theArray)[6]) == -1:
            clusteringDone = True
            break

    if verbosity >= 2:
        print "First merging done. Checking the number of bins"

    # now we check if we have to many bins
    doReduceBins = False
    if len(theArray) > maxBins:
        doReduceBins = True
        if verbosity >= 2:
            print "We now still have to many bins. Will merge bins with bad ", optMode
    else:
        if verbosity >= 2:
            print "number of bins below maximum"
    
    # reset FoM entries
    nbins = len(theArray)
    for ibin in range(nbins):
        theArray[ibin][6] = getFom(theArray[ibin][0],theArray[ibin][2])
    # now we look for the bins with the worst FoM and merge those 
    while doReduceBins and len(theArray) >= maxBins:
        nbins = len(theArray)
        if verbosity >= 2:
            print "Current nbins after iteration ", niterations, " : ", nbins
        imin = zip(*theArray)[6].index(min(zip(*theArray)[6]))
        if verbosity >= 2:
            print "considering bin", imin, theArray[imin]
        FoMLeft = None
        FoMRight = None
        if imin != 0: # not the leftmost bin (underflow)
            FoMLeft = theArray[imin-1][6]	
        if imin != nbins-1: # not the rightmost bin (overflow)
            FoMRight = theArray[imin+1][6]
        if FoMLeft != None and FoMRight != None:
            if FoMLeft <= FoMRight:
                newbin = mergeBins(theArray[imin],theArray[imin-1],getFom, verbosity)
                del theArray[imin]
                del theArray[imin-1]
                theArray.insert(imin-1, newbin)
            else:
                newbin = mergeBins(theArray[imin],theArray[imin+1],getFom, verbosity)
                del theArray[imin+1]
                del theArray[imin]
                theArray.insert(imin,newbin)
        elif FoMRight != None:
            newbin = mergeBins(theArray[imin],theArray[imin+1],getFom, verbosity)
            del theArray[imin+1]
            del theArray[imin]
            theArray.insert(imin,newbin)
        elif FoMLeft != None:
            newbin = mergeBins(theArray[imin],theArray[imin-1],getFom, verbosity)
            del theArray[imin]
            del theArray[imin-1]
            theArray.insert(imin-1, newbin)

    # now we are done
    if verbosity >= 1:
        print "array after all merges"
        print theArray
    #extract binning information    
    listOfBinLowEdges = list(zip(*theArray)[4])
    listOfBinWidths = zip(*theArray)[5]
    listOfBinLowEdges.append(listOfBinLowEdges[-1]+listOfBinWidths[-1])
    return listOfBinLowEdges

