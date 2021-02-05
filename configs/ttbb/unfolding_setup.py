import ROOT

indices = [0, -4, -7, -9, -10, -8, -6, -3, +1, +2, -2, -5, -1, +3, +4]

def generateGenLevelBins(plotClasses, sampleDict, doReadTrees,
        copyClass, variable, binEdges, nameTag, labelTag, 
        color = ROOT.kYellow, plot = False, type = "signal"):
    nicks = []
    samples = []
    ranges = [[binEdges[i], binEdges[i+1]] for i in range(len(binEdges)-1)]

    print("generating unfolding generator level bins")
    for iBin, binRange in enumerate(ranges):
        selection = "({var}>{lo}&&{var}<={hi})".format(
            var = variable, lo = binRange[0], hi = binRange[1])

        nickname  = copyClass.nick+"_{}_genBin_{}".format(nameTag, iBin)
        label     = copyClass.name+" ({} bin{})".format(labelTag, iBin)
        print(selection)

        binSample = plotClasses.Sample(
            label, color+indices[iBin], copyClass.path,
            copyClass.selection+"*"+selection, nickname,
            samDict = sampleDict, readTrees=doReadTrees,
            plot = plot, typ = type)

        samples.append(binSample)
        nicks.append(nickname)

    return samples, nicks


def generateRecoBins(label, selection, tag, binEdges, bins_per_bin, variable, nameTag, labelTag):
    ranges = [[binEdges[i], binEdges[i+1]] for i in range(len(binEdges)-1)]
    newLabels = []
    newSelections = []
    newTags = []
    binRanges = []
    nBins = []
    for iBin, binRange in enumerate(ranges):
        l = label+" ({} bin{})".format(labelTag, iBin)
        s = selection+"*({var}>{lo}&&{var}<={hi})".format(
            var = variable, lo = binRange[0], hi = binRange[1])
        t = tag+"_"+nameTag+"_recoBin_{}".format(iBin)
        newLabels.append(l)
        newSelections.append(s)
        newTags.append(t)
        binRanges.append(binRange)
        if not type(bins_per_bin) == list:
            nBins.append(bins_per_bin)
        else:
            nBins.append(bins_per_bin[iBin])
    return zip(newLabels, newSelections, newTags, binRanges, nBins)

