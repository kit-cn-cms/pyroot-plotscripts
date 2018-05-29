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

plotselection_inclusive = "1.*DeltaPhi_Jet_MET[0]>1."
plotlabel_inclusive = "#slash{E}_{T}>250 GeV"
plots_inclusive = [
    Plot(ROOT.TH1F("Evt_Pt_GenMET", "Gen #slash{E}_{T}", 50, 0., 1500.),
         "Gen #slash{E}_{T}", plotselection_inclusive, plotlabel_inclusive),
]

plots = plots_inclusive

allsystnames = weightSystNames+otherSystNames

THEoutputpath = "workdir"
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
listOfHistoLists_unfolded = createHistoLists_fromSuperHistoFile(
    outputpath, samples_unfolded, plots, 1)
print "listOfHistoLists_unfolded=", listOfHistoLists_unfolded

print "Making MC Control plots"

lll = createLLL_fromSuperHistoFileSyst(
    outputpath, samples_background, plots, allsystnames)
# print "lll=", lll

lUnfoldedData = createUnfoldedHistoList(
    outputpath, "unfolded_Evt_Pt_GenMET", allsystnames)
# print "lUnfoldedData=", lUnfoldedData
labels = [plot.label for plot in plots]
# plotDataMCanWsyst(listOfHistoListsData=listOfHistoLists_unfolded, listOfHistoLists=transposeLOL(lolT_background), samples=samples_background,
                  # listOfhistosOnTop=lolT_signal[0], sampleOnTop=samples_signal[0], factor=-1, name=jobname, listOflll=[[lll, 3354, ROOT.kBlack, True]], logscale=True, label=labels, ratio=True, blinded=False, verbosity=2)

plotUnfoldedDataMCanWsyst(lUnfolded=lUnfoldedData, listOfHistoLists=transposeLOL(lolT_background), samples=samples_background,
                  listOfhistosOnTop=lolT_signal[0], sampleOnTop=samples_signal[0], factor=-1, name=jobname, listOflll=[[lll, 3354, ROOT.kBlack, True]], logscale=True, label=labels, ratio=True, blinded=False, verbosity=2)