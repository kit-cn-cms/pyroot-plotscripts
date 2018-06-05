import sys
import os
import ROOT

sys.path.append('pyroot-plotscripts-base')
sys.path.append('pyroot-plotscripts-base/limittools')
sys.path.append('limittools')

from scriptgenerator import *
from plotutils import *
from limittools import renameHistos
from limittools import addPseudoData
from limittools import addRealData
from limittools import makeDatacards
# UPDATE
from limittools import makeDatacardsParallel
from limittools import calcLimits
from limittools import replaceQ2scale

from MonoJetUnfolded_cfg import *

jobname = "MonoJet_Plots"

plotselection_inclusive = ""
plotlabel_inclusive = "#slash{E}_{T}>250 GeV"
plots_inclusive = [
    Plot(ROOT.TH1F("Evt_Pt_GenMET", "Gen #slash{E}_{T}", 50, 0., 1000.),
         "Gen #slash{E}_{T}", plotselection_inclusive, plotlabel_inclusive),
]

plots = plots_inclusive

THEoutputpath = "/nfs/dust/cms/user/swieland/Darkmatter/DM_Unfolding/rootfiles/"
print "---------------------------------------------"
print "THEoutputpath=", THEoutputpath
print "---------------------------------------------"
if type(THEoutputpath) == str:
    outputpath = THEoutputpath
else:
    outputpath = THEoutputpath[0]

outputpath = THEoutputpath + "/data.root"
print "---------------------------------------------"
print "outputpath=", outputpath
print "---------------------------------------------"

print 'Create lists needed later'
# background samples
listOfHistoLists_background = createHistoLists_fromSuperHistoFile(
    outputpath, samples_background, plots, 1)
lolT_background = transposeLOL(listOfHistoLists_background)
print "listOfHistoLists_background=", listOfHistoLists_background
print "listOfHistoListsTransposed_background=", lolT_background
# signal samples
listOfHistoLists_signal = createHistoLists_fromSuperHistoFile(
    outputpath, samples_signal, plots, 1)
lolT_signal = transposeLOL(listOfHistoLists_signal)
print "listOfHistoLists_signal=", listOfHistoLists_signal
print "listOfHistoListsTransposed_signal=", lolT_signal
# unfolded
lUnfoldedData = createUnfoldedHistoList(
    outputpath, "unfolded_Evt_Pt_GenMET", unfoldedSystNames)
print "Making MC Control plots"

lll = createLLL_fromSuperHistoFileSyst(
    outputpath, samples_background, plots, MCSystnames)
# for ll in lll:
# 	for l in ll:
# 		for item in l:
# 			print item

# for hist in lUnfoldedData:
# 	print hist
labels = [plot.label for plot in plots]
xlabel="unfolded #slash{E}_{T}"

plotUnfoldedDataMCanWsyst(lUnfolded=lUnfoldedData, listOfHistoLists=transposeLOL(lolT_background), samples=samples_background,
                          listOfhistosOnTop=lolT_signal[0], sampleOnTop=samples_signal[0], factor=-1, name=jobname, listOflll=[[lll, 3354, ROOT.kBlack, True]], xlabel=xlabel, logscale=True, label=labels, ratio=True, blinded=False, verbosity=0)
