import sys
from os import path
import optparse
import importlib 
import ROOT


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
    # loading histograms
    # ========================================================
    '''
# import plot class
Plots = importlib.import_module("Plots" )
PlotList = {}
# load ROOT File
rootFile = ROOT.TFile(options.Rootfile, "readonly")  
# load samples
for sample in pltcfg.samples:
    print "NEW SAMPLE"
    # replace keys to get histogram key
    if procIden in nominalKey:
        sampleKey = nominalKey.replace(procIden, sample.nick)
    else:
        sampleKey=nominalKey
    print sampleKey
    rootHist = rootFile.Get(sampleKey)
    PlotList[sample.nick]=Plots.Plot(rootHist,sample.nick)
    print("    type of hist is: "+str(type(rootHist)) )

    # replace keys to get systematic key
    print "STARTING WITH SYSTEMATICS"
    if procIden in systematicKey:
        sampleSystKey = systematicKey.replace(procIden, sample.nick)
    else:
        sampleSystKey = systematicKey
    print sampleSystKey
    for systematic in sample.getShapes():
        print systematic
        if sysIden in sampleSystKey:
            sampleHistKey = sampleSystKey.replace(sysIden, systematic)
        else:
            sampleHistKey = sampleSystKey
        print sampleHistKey
        upname=sampleHistKey+"Up"
        print upname
        up= rootFile.Get(upname)
        downname=sampleHistKey+"Down"
        print downname
        down= rootFile.Get(downname)
        print("    type of up shape hist is: "+str(type(up)) )
        print("    type of down shape is: "+str(type(down)) )
        #TODO: Error message if not TH1F Type and delete systematic
        #PlotList[sample.nick].add_uncertainty(systematic,up,down)


"""
Combine Histograms for combined plot channels
"""

for sample in pltcfg.plottingsamples:
    print sample
    hists=[]
    combinedHist = None
    for process in sample.addsamples:
        print process
        if combinedHist:
            combinedHist.Add(PlotList[process].histo)
            del PlotList[process]
        else:
            combinedHist = PlotList[process].histo 
    
    PlotList[sample.nick]=Plots.Plot(combinedHist, sample.nick)


