import sys
import os
import optparse
import importlib 
import ROOT

debug=0

#get bool information out of parser string
def stringtobool(variable):
    if isinstance(variable, bool):
       return variable
    if variable.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif variable.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

# get plotting style information parser>config>default for bool type
def getParserConfigDefaultBool(parser,config,plotoptions,defaultbool):
    if not parser is None:
        print "%s using parser specification: %s" % (config,parser)
        return stringtobool(parser)
    elif config in plotoptions:
        print "%s using config specification: %s" % (config,plotoptions[config])
        return stringtobool(plotoptions[config])
    else:
        print "%s using default specification: %s" % (config,defaultbool)
        return stringtobool(defaultbool)
# get plotting style information parser>config>default
def getParserConfigDefaultValue(parser,config,plotoptions,defaultvalue):
    if not parser is None:
        print "%s using parser specification: %s" % (config,parser)
        return parser
    elif config in plotoptions:
        print "%s using config specification: %s" % (config,plotoptions[config])
        return plotoptions[config]
    else:
        print "%s using default specification: %s" % (config,defaultvalue)
        return defaultvalue
"""
Enabling parser options
"""
usage="usage=%prog [options] \n"
usage+="USE: Plotscript.py --channelName=CHANNELNAME --rootfile=FILE --outputpath=PATH --directory=PATH --workdir=PATH --plotconfig=PLOTCONFIGNAME \n"

parser = optparse.OptionParser(usage=usage)

parser.add_option("--channelname", dest="channelName",
        help="NAME of the channel", metavar="channelName")
parser.add_option("--selectionlabel", dest="selectionlabel", default=None,
        help="label of the selection", metavar="selectionlabel")
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
parser.add_option("--data", dest="datakeyreplace", default="data_obs",
        help="Key replacement for the data sample", metavar="datakeyreplace")
parser.add_option("--datalabel", dest="datalabel", default="data",
        help="label of the data", metavar="datalabel")
parser.add_option("--signalscaling", dest="signalscaling", default=None,
        help="scale factor of the signal processes, -1 to scale with background integral", metavar="signalscaling")
parser.add_option("--lumilabel", dest="lumilabel", default=None,
        help="print luminosity label on canvas", metavar="lumilabel")
parser.add_option("--cmslabel", dest="cmslabel", default=None,
        help="print CMS label on canvas", metavar="cmslabel")
parser.add_option("--ratio", dest="ratio",  default=None,
        help="make ratio plot", metavar="ratio")
parser.add_option("--logarithmic", dest="logarithmic", default=None,
        help="enable logarithmic plots", metavar="logarithmic")
parser.add_option("--splitlegend", dest="splitlegend",  default=None,
        help="splits the legend in two", metavar="splitlegend")
parser.add_option("--normalize", dest="normalize",  default=None,
        help="normalizes plot", metavar="normalize")
parser.add_option("--shape", dest="shape",  default=None,
        help="drawing shape plot, default normalize and no data", metavar="shape")
parser.add_option("--combineflag", dest="combineflag", default=None,
        help="NAME of the combine plot", metavar="combineflag")
parser.add_option("--sortedprocesses", dest="sortedprocesses", default=None,
        help="List for the sequence of Processes", metavar="sortedprocesses")



(options, args) = parser.parse_args()

"""
Define parser options for further use
"""

# Define placeholders for the keys of the histograms
procIden    = "$PROCESS"
chIden      = "$CHANNEL"
sysIden     = "$SYSTEMATIC"
combineIden = "$FLAG"


combineflag             = options.combineflag
if combineflag:
    options.nominalKey  = "$FLAG/$CHANNEL/$PROCESS"
    nominalKey          = nominalKey.replace(combineIden, combineflag)


# build keys
if chIden in options.nominalKey:
    nominalKey      = options.nominalKey.replace(chIden, options.channelName)
else:
    nominalKey      = options.nominalKey

if chIden in options.nominalKey:
    systematicKey   = options.systematicKey.replace(chIden, options.channelName)
else:
    systematicKey   = options.systematicKey


# Define directories used to import stuff

tooldir     = options.directory+"/util/tools/"
plotconfig  = options.plotconfig
workdir     = options.workdir

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
plotconfigpath,plotconfigfile   = os.path.split(plotconfig)
plotconfigfile                  = plotconfigfile.replace('.py','')
sys.path.append(plotconfigpath)
pltcfg                          = importlib.import_module(plotconfigfile)
print "using plotconfig: %s" % (plotconfigfile)

samples         = pltcfg.samples
plottingsamples = pltcfg.plottingsamples
systematics     = pltcfg.systematics
plotoptions     = pltcfg.plotoptions

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
Plots       = importlib.import_module("Plots" )
PlotList    = {}
# load ROOT File
rootfilename    = options.Rootfile
rootFile        = ROOT.TFile(rootfilename, "readonly") 

# load data if avaliable and move under and overflow bin
dataKey     = nominalKey.replace(procIden, options.datakeyreplace)
dataHist    = rootFile.Get(dataKey)
print("    type of data hist is: "+str(type(dataHist)) )
if isinstance(dataHist, ROOT.TH1):
    dataHist.SetStats(False)
    Plots.moveOverUnderFlow(dataHist)
    print "using data: %s" % (dataKey)
# data in combine in TGraphAsymmErrors, get TH1 out of it
elif isinstance(dataHist, ROOT.TGraphAsymmErrors):
    dataHist = Plots.GetHistoFromTGraphAE(dataHist)
    Plots.moveOverUnderFlow(dataHist)
    dataHist.SetStats(False)
else:
    print "ERROR: Not using data!"
    dataHist=None

# load samples
print "start loading  samples" 
for sample in samples:
    color   = samples[sample]['color']
    typ     = samples[sample]['typ']
    label   = samples[sample]['label']
    if combineflag:
        PlotList[sample] = Plots.getHistogramAndErrorband(rootFile=rootFile,sample=sample,
                                                        color=color,typ=typ,label=label,
                                                        nominalKey=nominalKey,procIden=procIden)
    else:
        PlotList[sample] = Plots.buildHistogramAndErrorBand(rootFile=rootFile,sample=sample,
                                                        color=color,typ=typ,label=label,
                                                        systematics=systematics,
                                                        nominalKey=nominalKey,procIden=procIden,
                                                        systematicKey=systematicKey,sysIden=sysIden)

"""
Combine Histograms and errorbands for combined plot channels
"""
for sample in plottingsamples:
    color       = plottingsamples[sample]['color']
    typ         = plottingsamples[sample]['typ']
    label       = plottingsamples[sample]['label']
    addsamples  = plottingsamples[sample]['addSamples']
    PlotList = Plots.addSamples(sample=sample,color=color,typ=typ,label=label,
                                    addsamples=addsamples,PlotList=PlotList,combineflag=combineflag)

"""
Get errorband and signalhist in case of combine output file,
else no signal
"""
if combineflag:
    if combineflag=="shapes_fit_s":
        bkgKey = nominalKey.replace(procIden, "total")
        totalsignalkey  = nominalKey.replace(procIden, "total_signal")
        totalsignal     = rootFile.Get(totalsignalkey)
        PlotList["sig"] = Plots.Plot(totalsignal,sample,label="Total signal",
                                        typ=signal, OverUnderFlowInc=True)
    else:
        bkgKey = nominalKey.replace(procIden, "total_background")
    # from total background or total background+signal prediction histogram in mlfit file, get the error band
    background = rootFile.Get(bkgKey)
    errorband = Plots.GetErrorGraph(background)
else:
    errorband = None





print '''
# ========================================================
# plotting histograms and Errorbands
# ========================================================
    '''

#get plotting style information, prioritized by parser>config>default
signalscaling   = getParserConfigDefaultValue(parser=options.signalscaling,config="signalscaling",
                                            plotoptions=plotoptions,defaultvalue=-1)
ratio           = getParserConfigDefaultValue(parser=options.ratio,config="ratio",
                                            plotoptions=plotoptions,defaultvalue="#frac{data}{MC Background}")
lumilabel       = getParserConfigDefaultValue(parser=options.lumilabel,config="lumilabel",
                                            plotoptions=plotoptions,defaultvalue=False)
cmslabel        = getParserConfigDefaultValue(parser=options.cmslabel,config="cmslabel",
                                            plotoptions=plotoptions,defaultvalue=False)
sortedProcesses = getParserConfigDefaultValue(parser=options.sortedprocesses,config="sortedprocesses",
                                            plotoptions=plotoptions,defaultvalue=False)
logarithmic     = getParserConfigDefaultBool(parser=options.logarithmic,config="logarithmic",
                                            plotoptions=plotoptions,defaultbool=False)
splitlegend     = getParserConfigDefaultBool(parser=options.splitlegend,config="splitlegend",
                                            plotoptions=plotoptions,defaultbool=False)
normalize       = getParserConfigDefaultBool(parser=options.normalize,config="normalize",
                                            plotoptions=plotoptions,defaultbool=False)
shape           = getParserConfigDefaultBool(parser=options.shape,config="shape",
                                            plotoptions=plotoptions,defaultbool=False)
if shape:
    dataHist        = None
    ratio           = False
    normalize       = True

"""

"""


DrawHistogramObject = Plots.DrawHistograms(PlotList,options.channelName,
                                data=dataHist,ratio=ratio, 
                                signalscaling=int(signalscaling),
                                errorband=errorband, logoption=logarithmic,
                                normalize=normalize,splitlegend=splitlegend,
                                combineflag=combineflag,shape=shape,
                                sortedProcesses=sortedProcesses)

DrawHistogramObject.drawHistsOnCanvas()

DrawHistogramObject.builtLegend()
# add lumi or private work label to plot
if cmslabel:
    DrawHistogramObject.printCMSLabel(cmslabel=cmslabel)
if lumilabel:
    DrawHistogramObject.printLumi(lumi = lumilabel)

#add selection label to plot
if options.selectionlabel:
    DrawHistogramObject.printCategoryLabel(catLabel = options.selectionlabel)
plotpath = workdir+"/outputPlots/"
if not os.path.exists(plotpath):
        os.makedirs(plotpath)


DrawHistogramObject.saveCanvas(path = plotpath+"/"+options.channelName+".pdf")

