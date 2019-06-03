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
print("Using plotconfig %s"%pltcfg)

# loading X_systematics.csv config
sys.path.append(utildir+"/tools/")
Systematics = importlib.import_module("Systematics")
processes=pltcfg.list_of_processes
systematics=Systematics.Systematics(systconfig)
systematics.plotSystematicsForProcesses(processes)
for sample in pltcfg.samples:
    sample.setShapes(systematics.get_shape_systs(sample.nick))
print("Using systematic config %s"%systconfig)

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
PlotList = {}
# load ROOT File
rootfilename = options.Rootfile
rootFile = ROOT.TFile(rootfilename, "readonly")  
# load samples
for sample in pltcfg.samples:
    PlotList[sample.nick]=Plots.buildHistogramAndErrorBand(rootFile=rootFile,sample=sample,
    				nominalKey=nominalKey,procIden=procIden,systematicKey=systematicKey,sysIden=sysIden)

"""
Combine Histograms and errorbands for combined plot channels
"""
for sample in pltcfg.plottingsamples:
    PlotList=Plots.addSamples(sample=sample,PlotList=PlotList)

print '''
# ========================================================
# plotting histograms and Errorbands
# ========================================================
    '''
canvas=Plots.drawHistsOnCanvas(PlotList,options.channelName,ratio="#frac{scaled Signal}{Background}",errorband=True)



# add ROC score if activated
# if self.printROCScore and len(signalIndex)==1:
# setup.printROCScore(canvas, nodeROC, plotOptions["ratio"])

# # add lumi or private work label to plot
# if self.privateWork:
# setup.printPrivateWork(canvas, plotOptions["ratio"], nodePlot = True)
# else:
# setup.printLumi(canvas, ratio = plotOptions["ratio"])

Plots.saveCanvas(canvas,options.directory+"/workdir/"+options.channelName+"discriminator.pdf")