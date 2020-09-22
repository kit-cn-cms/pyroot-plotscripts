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


def generateRecoBins(label, selection, tag, binEdges, variable, nameTag, labelTag):
    ranges = [[binEdges[i], binEdges[i+1]] for i in range(len(binEdges)-1)]
    newLabels = []
    newSelections = []
    newTags = []
    for iBin, binRange in enumerate(ranges):
        l = label+" ({} bin{})".format(labelTag, iBin)
        s = selection+"*({var}>{lo}&&{var}<={hi})".format(
            var = variable, lo = binRange[0], hi = binRange[1])
        t = tag+"_"+nameTag+"_recoBin_{}".format(iBin)
        newLabels.append(l)
        newSelections.append(s)
        newTags.append(t)
    return zip(newLabels, newSelections, newTags)

reco_bins = []
gen_bins  = []

genSel  = ""
recoSel = ""
recoLabel = ""
recoTag = ""

gen_variable = ""
reco_variable = ""

name_tag = ""
gen_label_tag = ""
reco_label_tag = ""

