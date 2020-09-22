import ROOT
import controlPlots_rebin
import sys
import numpy as np

def getBinning(h, iterations = 1):
    entries = np.array([h.GetBinContent(i+1) for i in range(h.GetNbinsX())])
    print(len(entries))
    indices = getMedianBins(entries, maxit = iterations)
    binEdges = [h.GetXaxis().GetBinLowEdge(1)]
    binContents = []
    allIndices = [0]+indices
    for i, idx in enumerate(indices):
        binEdges.append(h.GetXaxis().GetBinUpEdge(idx))
        binContents.append(sum(entries[allIndices[i]:allIndices[i+1]]))
    binEdges.append(h.GetXaxis().GetBinUpEdge(h.GetNbinsX()))
    binContents.append(sum(entries[allIndices[-1]:]))
    print(binContents)
    print(np.std(binContents))
    return binEdges
    
def getMedianBins(entries, offset = 0, it = 1, maxit = 1):
    split = 0
    minDiff = sum(entries)
    while abs( sum(entries[:split+1]) - sum(entries[split+1:]) ) <= minDiff and split < len(entries)-1:
        minDiff = abs( sum(entries[:split+1]) - sum(entries[split+1:]) )
        split += 1
    if it < maxit:
        binEdges = getMedianBins(entries[:split], offset = 0, it = it+1, maxit = maxit)
        binEdges.append(split)
        binEdges += getMedianBins(entries[split:], offset = split, it = it+1, maxit = maxit)
    else:
        binEdges = [split]
    binEdges = [offset+b for b in binEdges]
    return binEdges

line = "\t\tplotClasses.Plot(ROOT.TH1D(cat+\"_{var}\",\"{title}\",{nBins},\n\t\t\tarray(\"f\", {binArray})),\n\t\t\t\"{branch}\",selection, label),\n"

inputFile = sys.argv[1]
templates = ROOT.TFile(inputFile)

cat = "jt64_"
plots = controlPlots_rebin.plots_ge6j_ge4t(data = None)
nBins = 10
lines = []
for p in plots:
    print(p.name)
    h = templates.Get("data_obs__"+p.name)
    binEdges = getBinning(h, iterations = 3)
    #nEvts = h.Integral()/nBins
    #print("number of events per bin: {}".format(nEvts))
    #binEdges = []
    #binContent = []
    #binEdges.append(h.GetXaxis().GetBinLowEdge(1))
    #y = 0
    #for iBin in range(h.GetNbinsX()):
    #    y += h.GetBinContent(iBin+1)
    #    if (y > nEvts or y+h.GetBinContent(iBin+2) > nEvts*1.03) or (y > nEvts*0.95 and y+h.GetBinContent(iBin+2) > nEvts*1.05):
    #        binEdges.append(h.GetXaxis().GetBinUpEdge(iBin+1))
    #        binContent.append(y)
    #        y = 0
    #if y > 0:
    #    binContent.append(y)
    #    binEdges.append(h.GetXaxis().GetBinUpEdge(h.GetNbinsX()))
    #else:
    #    binEdges[-1] = h.GetXaxis().GetBinUpEdge(h.GetNbinsX())
    



    binEdges = [float("{:.5f}".format(b)) for b in binEdges]
    print(binEdges)
    #print(binContent)
    print(len(binEdges))
    print("\n\n")
    lines.append(line.format(
        var         = p.name.replace(cat,""),
        title       = h.GetTitle(),
        nBins       = len(binEdges)-1,
        binArray    = str(binEdges),
        branch      = p.variable,
        selection   = p.selection,
        label       = p.label))
    
print("\n".join(lines))
    

