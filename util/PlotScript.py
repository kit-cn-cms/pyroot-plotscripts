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
parser.add_option("--plotconfig", dest="plotconfig",
        help="Name of plot config", metavar="plotconfig")
parser.add_option("--systconfig", dest="systconfig",
        help="Name of systematics config", metavar="systconfig")
parser.add_option("--nominalkey", dest="nominalKey", default="$PROCESS_$CHANNEL",
        help="KEY of the systematics histograms", metavar="nominalKey")
parser.add_option("--systematickey", dest="systematicKey", default="$PROCESS_$CHANNEL_$SYSTEMATIC",
        help="KEY of the nominal histograms", metavar="systematicKey")

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
configdir = options.directory+"/configs/"
utildir = options.directory+"/util/"
systconfig=configdir+options.systconfig+".csv"
plotconfig=configdir+options.plotconfig+".py"

# checks if paths given exist
if not path.exists(options.Rootfile):
    sys.exit("ERROR: rootfile does not exist!")
elif not path.exists(systconfig):
    sys.exit("ERROR: systconfig does not exist!")
elif not path.exists(plotconfig):
    sys.exit("ERROR: plotconfig does not exist!")

"""
start loading configs
"""

print '''
# ========================================================
# loading configs
# ========================================================
    '''
# loading plt_X.py config

sys.path.append(configdir)
pltcfg = importlib.import_module( options.plotconfig )

# loading X_systematics.py config
sys.path.append(utildir+"/tools/")
print(utildir)
Systematics = importlib.import_module("Systematics")
print(dir(Systematics))
processes=pltcfg.list_of_processes
systematics=Systematics.Systematics(systconfig)
systematics.plotSystematicsForProcesses(processes)
for sample in pltcfg.samples:
    sample.setShapes(systematics.get_shape_systs(sample.nick))


"""
start loading  histograms
"""
print '''
# ========================================================
# loading histograms and creating Errorbands
# ========================================================
    '''
# import plot class
Plots = importlib.import_module("Plots" )
PlotList = []
# load ROOT File
rootFile = ROOT.TFile(options.Rootfile, "readonly")  
# load samples
for sample in pltcfg.samples:
    Plotlist.append(Plots.buildHistogramAndErrorBand(rootfile=rootfile,sample=sample,
    				nominalKey=nominalKey,systematicKey=systematicKey))
"""
Combine Histograms for combined plot channels
TODO change strukture
"""

for sample in pltcfg.plottingsamples:
    combinedHist = None
    for process in sample.addsamples:
        if combinedHist:
            combinedHist.Add(PlotList[process].histo)
            del PlotList[process]
        else:
            combinedHist = PlotList[process].histo
            del PlotList[process] 
    PlotList[sample.nick]=Plots.Plot(combinedHist, sample.nick, color=sample.color, label=sample.name)
"""
Signal and Background difference
"""
sigHists=[]
sigLabels=[]
bkgHists=[]
bkgLabels=[]
for plotname in PlotList:
    hist=PlotList[plotname].histo
    color=PlotList[plotname].color
    label=PlotList[plotname].label
    hist.SetStats(False)
    print "-"*130
    print color
    if plotname in signal:
        hist.SetLineColor( color )
        hist.SetFillColor(0)
        hist.SetLineWidth(2)
        sigHists.append(hist)
        sigLabels.append(label)
    else:
        hist.SetLineColor(ROOT.kBlack )
        hist.SetFillColor(color)
        hist.SetLineWidth(1)
        bkgHists.append(hist)
        bkgLabels.append(label)

print sigHists 
print sigLabels
print bkgHists     
print bkgLabels  

canvas=Plots.drawHistsOnCanvas(sigHists,bkgHists,options.channelName,ratio="#frac{scaled Signal}{Background}",errorband=graph)

# setup legend
legend = Plots.getLegend()

# add signal entry
for i, h in enumerate(sigHists):
    legend.AddEntry(h, sigLabels[i], "L")

# # add background entries
for i, h in enumerate(bkgHists):
    legend.AddEntry(h, bkgLabels[i], "F")

# draw legend
legend.Draw("same")

# add ROC score if activated
# if self.printROCScore and len(signalIndex)==1:
# setup.printROCScore(canvas, nodeROC, plotOptions["ratio"])

# # add lumi or private work label to plot
# if self.privateWork:
# setup.printPrivateWork(canvas, plotOptions["ratio"], nodePlot = True)
# else:
# setup.printLumi(canvas, ratio = plotOptions["ratio"])

Plots.saveCanvas(canvas,options.directory+"/workdir/"+options.channelName+"discriminator.pdf")