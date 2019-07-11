import sys
import os
import optparse
import importlib 
import ROOT

debug=0

"""
Enabling parser options
"""
usage="usage=%prog [options] \n"
usage+="USE: Plotscript.py --channelName=CHANNELNAME --rootfile=FILE --outputfile=FILE --directory=PATH -csvfile=FILE \n"

parser = optparse.OptionParser(usage=usage)

parser.add_option("--channelname", dest="channelName",
        help="NAME of the channel", metavar="channelName")
parser.add_option("--rootfile", dest="Rootfile",
        help="ROOTFILE including the data used to create the plots", metavar="/path/to/rootfile")
parser.add_option("--outputpath", dest="outputpath",
        help="output path", metavar="/path/to/outputpath")
parser.add_option("--directory", dest="directory",
         help="PATH to pyroot plotscript directory", metavar="/path/to/directory")
parser.add_option("--workdir", dest="workdir",
         help="PATH to workdir", metavar="/path/to/workdir")
parser.add_option("--plotconfig", dest="plotconfig",
        help="Name of plot config", metavar="plotconfig")
parser.add_option("--nominalkey", dest="nominalKey", default="$PROCESS_$CHANNEL",
        help="KEY of the systematics histograms", metavar="nominalKey")
parser.add_option("--systematickey", dest="systematicKey", default="$PROCESS_$CHANNEL_$SYSTEMATIC",
        help="KEY of the nominal histograms", metavar="systematicKey")
parser.add_option("--datakeyreplace", dest="datakeyreplace", default="data_obs",
        help="Key replacement for the data sample", metavar="datakeyreplace")
parser.add_option("--datalabel", dest="datalabel", default="data",
        help="label of the data", metavar="datalabel")
parser.add_option("--signalscaling", dest="signalscaling", default="-1",
        help="scale factor of the signal processes, -1 to scale with background integral", metavar="signalscaling")
parser.add_option("--lumilabel", dest="lumilabel", default=False,
        help="print luminosity label on canvas", metavar="lumilabel")
parser.add_option("--privatework", dest="privatework", action = "store_true", default=False,
        help="print privatework label on canvas", metavar="privatework")
parser.add_option("--ratio", dest="ratio",  default="#frac{data}{MC Background}",
        help="make ratio plot", metavar="ratio")
parser.add_option("--logarithmic", dest="logarithmic", action = "store_true", default=False,
        help="enable logarithmic plots", metavar="logarithmic")


(options, args) = parser.parse_args()

"""
Define parser options for further use
"""

# Define placeholders for the keys of the histograms
procIden    = "$PROCESS"
chIden      = "$CHANNEL"
sysIden     = "$SYSTEMATIC"

print "-"*130
print options.logarithmic

if chIden in options.nominalKey:
    nominalKey = options.nominalKey.replace(chIden, options.channelName)
else:
    nominalKey=options.nominalKey

if chIden in options.nominalKey:
    systematicKey = options.systematicKey.replace(chIden, options.channelName)
else:
    systematicKey=options.systematicKey


# Define directories used to import stuff

tooldir = options.directory+"/util/tools/"
plotconfig=options.plotconfig
workdir=options.workdir

# checks if paths given exist
if not os.path.exists(options.Rootfile):
    sys.exit("ERROR: rootfile does not exist!")
elif not os.path.exists(plotconfig):
    sys.exit("ERROR: plotconfig does not exist!")

"""
start loading plotconfig
"""

print '''
# ========================================================
# loading config
# ========================================================
    '''
plotconfigpath,plotconfigfile=os.path.split(plotconfig)
print plotconfigpath
print "-"*130
print plotconfigfile
print "-"*130
plotconfigfile=plotconfigfile.replace('.py','')
print plotconfigfile
print "-"*130
sys.path.append(plotconfigpath)


pltcfg = importlib.import_module(plotconfigfile)
samples=pltcfg.samples
plottingsamples=pltcfg.plottingsamples
systematics=pltcfg.systematics

"""
start loading  histograms
"""
print '''
# ========================================================
# loading histograms and creating Errorbands
# ========================================================
    '''
# import plot class
sys.path.append(tooldir)
Plots = importlib.import_module("Plots" )
PlotList = {}
# load ROOT File
rootfilename = options.Rootfile
rootFile = ROOT.TFile(rootfilename, "readonly") 

# load data and move under and overflow bin
dataKey = nominalKey.replace(procIden, options.datakeyreplace)
dataHist=rootFile.Get(dataKey)
dataHist.SetStats(False)
Plots.moveOverUnderFlow(dataHist)

# load samples
for sample in samples:
    color=samples[sample]['color']
    typ=samples[sample]['typ']
    label=samples[sample]['label']
    PlotList[sample]=Plots.buildHistogramAndErrorBand(rootFile=rootFile,sample=sample,color=color,typ=typ,label=label,systematics=systematics,
    				nominalKey=nominalKey,procIden=procIden,systematicKey=systematicKey,sysIden=sysIden)

"""
Combine Histograms and errorbands for combined plot channels
"""
for sample in plottingsamples:
    color=plottingsamples[sample]['color']
    typ=plottingsamples[sample]['typ']
    label=plottingsamples[sample]['label']
    addsamples=plottingsamples[sample]['addSamples']
    PlotList=Plots.addSamples(sample=sample,color=color,typ=typ,label=label,addsamples=addsamples,PlotList=PlotList)

print '''
# ========================================================
# plotting histograms and Errorbands
# ========================================================
    '''
"""
returning sorted Lists and Histograms necessary to draw the legend
and everything ROOT related
"""
canvas, errorband, ratioerrorband, sortedSignal, sigHists, sortedBackground, bkgHists =Plots.drawHistsOnCanvas(PlotList,options.channelName,
                                                                                        data=dataHist,ratio=options.ratio, 
                                                                                        signalscaling=int(options.signalscaling),
                                                                                        errorband=True, logoption=options.logarithmic)

# drawing the legend
#one legend:
legendinone=False
if legendinone:
    legend = Plots.getLegend2()
    legend.AddEntry(dataHist,options.datalabel,"P")

    for i,signal in enumerate(sortedSignal):
        legend.AddEntry(sigHists[i], PlotList[signal].label, "L")
    for i,background in enumerate(sortedBackground):
        legend.AddEntry(bkgHists[i], PlotList[background].label, "F")
    legend.Draw("same")
else:
    legend1 = Plots.getLegend1()
    legend2 = Plots.getLegend2()
    legend1.AddEntry(dataHist,options.datalabel,"P")

    legendentries=len(sortedSignal)+len(sortedBackground)
    n=0
    for i,signal in enumerate(sortedSignal):
        if n<legendentries/2:
            legend1.AddEntry(sigHists[i], PlotList[signal].label, "L")
        else:
            legend2.AddEntry(sigHists[i], PlotList[signal].label, "L")
        n+=1
    for i,background in enumerate(sortedBackground):
        if n<legendentries/2:
            legend1.AddEntry(bkgHists[i], PlotList[background].label, "F")
        else:
            legend2.AddEntry(bkgHists[i], PlotList[background].label, "F")
        n+=1
    legend1.Draw("same")
    legend2.Draw("same")

# add lumi or private work label to plot
if options.privatework:
    Plots.printPrivateWork(canvas, ratio=options.ratio, nodePlot = True)
if options.lumilabel:
    Plots.printLumi(canvas, lumi=options.lumilabel, ratio = options.ratio)

plotpath=workdir+"/outputPlots/"
if not os.path.exists(plotpath):
        os.makedirs(plotpath)


Plots.saveCanvas(canvas,plotpath+"/"+options.channelName+"discriminator.pdf")

