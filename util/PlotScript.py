import sys
from os import path
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

(options, args) = parser.parse_args()

"""
Define parser options for further use
"""

# Define placeholders for the keys of the histograms
procIden    = "$PROCESS"
chIden      = "$CHANNEL"
sysIden     = "$SYSTEMATIC"



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
if not path.exists(options.Rootfile):
    sys.exit("ERROR: rootfile does not exist!")
elif not path.exists(plotconfig):
    sys.exit("ERROR: plotconfig does not exist!")

"""
start loading plotconfig
"""

print '''
# ========================================================
# loading config
# ========================================================
    '''
plotconfigpath,plotconfigfile=path.split(plotconfig)
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
# returning sorted Lists and Histograms necessary to draw the legend
canvas, errorband, ratioerrorband, sortedSignal, sigHists, sortedBackground, bkgHists =Plots.drawHistsOnCanvas(PlotList,options.channelName,data=dataHist,ratio="#frac{data}{MC Background}",errorband=True)

# drawing the legend
legend = Plots.getLegend()
legend.AddEntry(dataHist,options.datalabel,"P")
for i,signal in enumerate(sortedSignal):
    legend.AddEntry(sigHists[i], PlotList[signal].label, "L")
for i,background in enumerate(sortedBackground):
    legend.AddEntry(bkgHists[i], PlotList[background].label, "F")
legend.Draw("same")

# add ROC score if activated
# if self.printROCScore and len(signalIndex)==1:
# setup.printROCScore(canvas, nodeROC, plotOptions["ratio"])

# # add lumi or private work label to plot
# if self.privateWork:
# setup.printPrivateWork(canvas, plotOptions["ratio"], nodePlot = True)
# else:
# setup.printLumi(canvas, ratio = plotOptions["ratio"])

Plots.saveCanvas(canvas,workdir+"/"+options.channelName+"discriminator.pdf")

