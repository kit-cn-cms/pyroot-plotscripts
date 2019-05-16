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
parser.add_option("--signal", dest="signal", default="$ttH",
        help="signal processes", metavar="signal")


(options, args) = parser.parse_args()

"""
Define parser options for further use
"""

# Define placeholders for the keys of the histograms
procIden    = "$PROCESS"
chIden      = "$CHANNEL"
sysIden     = "$SYSTEMATIC"

signal=options.signal.split(",")
print signal

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
upErrors=None
downErrors=None
# load samples
for sample in pltcfg.samples:
    print "NEW SAMPLE"
    print sample.nick
    # replace keys to get histogram key
    if procIden in nominalKey:
        sampleKey = nominalKey.replace(procIden, sample.nick)
    else:
        sampleKey=nominalKey
    rootHist = rootFile.Get(sampleKey)
    #moves underflow in the first and overflow in the last bin
    Plots.moveOverUnderFlow(rootHist)
    print("type of hist is: "+str(type(rootHist)) )
    if isinstance(rootHist, ROOT.TH1):
        PlotList[sample.nick]=Plots.Plot(rootHist,sample.nick,label=sample.name,color=sample.color)
        print "_"*130
        print sample.color

    # replace keys to get systematic key
    print "STARTING WITH SYSTEMATICS"
    if procIden in systematicKey:
        sampleSystKey = systematicKey.replace(procIden, sample.nick)
    else:
        sampleSystKey = systematicKey

    """
    create empty Error Band for sample to fill 
    """
    if not upErrors and not downErrors:
        upErrors=[0]*rootHist.GetNbinsX()
        downErrors=[0]*rootHist.GetNbinsX()

    for systematic in sample.getShapes():
        print systematic
        if sysIden in sampleSystKey:
            sampleHistKey = sampleSystKey.replace(sysIden, systematic)
        else:
            sampleHistKey = sampleSystKey
        upname=sampleHistKey+"Up"
        up= rootFile.Get(upname)
        downname=sampleHistKey+"Down"
        down= rootFile.Get(downname)
        
        if isinstance(up, ROOT.TH1) and isinstance(down, ROOT.TH1):
            Plots.moveOverUnderFlow(up)
            Plots.moveOverUnderFlow(down)

            for ibin in range(0, rootHist.GetNbinsX()):
                # get up down variations
                u_=up[ibin+1]-rootHist[ibin+1]
                d_=down[ibin+1]-rootHist[ibin+1]
                 # set max as up and min as down
                u = max(u_,d_)
                d = min(u_,d_)
                # only consider positive up and negative down variations
                u = max(0.,u)
                d = min(0.,d)
                upErrors[ibin]=ROOT.TMath.Sqrt( upErrors[ibin]*upErrors[ibin] + u*u )
                downErrors[ibin] = ROOT.TMath.Sqrt( downErrors[ibin]*downErrors[ibin] + d*d)
                if debug>99:
                    print "adding up/down ", u, d
                    print "total up/down now: ", upErrors[ibin], downErrors[ibin]
                    print "-"*50

        else:
            print("ERROR! can not use: "+str(systematic) )
            print("->type of up shape hist is: "+str(type(up)) )
            print("->type of down shape is: "+str(type(down)) )
      

"""
Make Error Bands
"""

AllHists=None
for sample in pltcfg.samples:
    print "ERROR BANDS"
    print sample
    if AllHists:
        AllHists.Add(PlotList[sample.nick].histo)
    else:
        AllHists=PlotList[sample.nick].histo

graph = ROOT.TGraphAsymmErrors(AllHists)
for i in range(len(upErrors)):
    graph.SetPointEYlow(i, downErrors[i])
    graph.SetPointEYhigh(i, upErrors[i])
    graph.SetPointEXlow(i, AllHists.GetBinWidth(i+1)/2.)
    graph.SetPointEXhigh(i, AllHists.GetBinWidth(i+1)/2.)
graph.SetFillStyle(3004)
graph.SetLineColor(ROOT.kBlack)
graph.SetFillColor(ROOT.kBlack)

print graph

"""
Combine Histograms for combined plot channels
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