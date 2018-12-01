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

from MonoJetUnfoldedControl_cfg import *

jobname = "MonoJet_ControlPlots"

plotselection_inclusive = ""
plotlabel_inclusive = ""
plotlabel_fakes = "fakes"
plotlabel_misses = "misses"
plots_inclusive = [
    Plot(ROOT.TH1F("GenMET", "generated #slash{E}_{T} [GeV/c]", 50, 0., 1000.),
         "generated #slash{E}_{T} [GeV/c]", plotselection_inclusive, plotlabel_inclusive),

    Plot(ROOT.TH1F("MET", "#slash{E}_{T} [GeV/c]", 50, 0., 1000.),
         "#slash{E}_{T} [GeV/c]", plotselection_inclusive, plotlabel_inclusive),

    Plot(ROOT.TH1F("Evt_Phi_MET", "#slash{E}_{T} #phi", 50, 0., 1000.),
         "#slash{E}_{T} #phi", plotselection_inclusive, plotlabel_inclusive),

    Plot(ROOT.TH1F("Evt_Phi_GenMET", "generated #slash{E}_{T} #phi", 50, 0., 1000.),
         "generated #slash{E}_{T} #phi", plotselection_inclusive, plotlabel_inclusive),

    Plot(ROOT.TH1F("Jet_Eta", "ak4-jets #eta", 50, 0., 1000.),
         "ak4-jets #eta", plotselection_inclusive, plotlabel_inclusive),

    Plot(ROOT.TH1F("Jet_Pt", "ak4-jets p_{T} [GeV/c]", 50, 0., 1000.),
         "ak4-jets p_{T} [GeV/c]", plotselection_inclusive, plotlabel_inclusive),

    Plot(ROOT.TH1F("Jet_Phi", "ak4-jets #phi", 50, 0., 1000.),
         "ak4-jets #phi", plotselection_inclusive, plotlabel_inclusive),

    Plot(ROOT.TH1F("Jet_Chf", "ak4-jets CHF", 50, 0., 1000.),
         "ak4-jets CHF", plotselection_inclusive, plotlabel_inclusive),

    Plot(ROOT.TH1F("Jet_Nhf", "ak4-jets NHF", 50, 0., 1000.),
         "ak4-jets NHF", plotselection_inclusive, plotlabel_inclusive),

    Plot(ROOT.TH1F("Jet_EtaAK8", "ak8-jets #eta", 50, 0., 1000.),
         "ak8-jets #eta", plotselection_inclusive, plotlabel_inclusive),

    Plot(ROOT.TH1F("Jet_PtAK8", "ak8-jets p_{T} [GeV/c]", 50, 0., 1000.),
         "ak8-jets p_{T} [GeV/c]", plotselection_inclusive, plotlabel_inclusive),

    Plot(ROOT.TH1F("Jet_PhiAK8", "ak8-jets #phi", 50, 0., 1000.),
         "ak8-jets #phi", plotselection_inclusive, plotlabel_inclusive),

    Plot(ROOT.TH1F("N_Jets", "number of ak4-jets", 50, 0., 1000.),
         "number of ak4-jets", plotselection_inclusive, plotlabel_inclusive),

    Plot(ROOT.TH1F("fakes", "hadr. recoil |#vec{U}| [GeV/c]", 50, 0., 1000.),
         "hadr. recoil |#vec{U}| [Gev/c]", plotselection_inclusive, plotlabel_fakes),

    Plot(ROOT.TH1F("misses", "hadr. recoil |#vec{U}| [GeV/c]", 50, 0., 1000.),
         "hadr. recoil |#vec{U}| [Gev/c]", plotselection_inclusive, plotlabel_misses),

    Plot(ROOT.TH1F("h_W_Pt", "W p_{T} [GeV/c]", 50, 0., 1000.),
         "W p_{T} [GeV]", plotselection_inclusive, plotlabel_inclusive),

    Plot(ROOT.TH1F("h_Z_Pt", "Z p_{T} [GeV/c]", 50, 0., 1000.),
         "Z p_{T} [GeV]", plotselection_inclusive, plotlabel_inclusive),

    Plot(ROOT.TH1F("Hadr_Recoil_Pt", "hadr. recoil |#vec{U}| [GeV/c]", 50, 0., 1000.),
         "hadr. recoil #vec{U} [GeV/c]", plotselection_inclusive, plotlabel_inclusive),

    Plot(ROOT.TH1F("Hadr_Recoil_Phi", "hadr. recoil #vec{U} #phi", 50, 0., 1000.),
         "hadr. recoil |#vec{U}| #phi", plotselection_inclusive, plotlabel_inclusive),

    Plot(ROOT.TH1F("GenHadr_Recoil_Pt", "generated generated hadr. recoil |#vec{U}| [GeV/c]", 50, 0., 1000.),
         "generated hadr. recoil |#vec{U}| [GeV/c]", plotselection_inclusive, plotlabel_inclusive),
    
    Plot(ROOT.TH1F("GenHadr_Recoil_Phi", "generated hadr. recoil #phi", 50, 0., 1000.),
         "generated hadr. recoil #phi", plotselection_inclusive, plotlabel_inclusive),

    Plot(ROOT.TH1F("N_LooseLeptons", "# loose leptons", 50, 0., 1000.),
         "# loose leptons", plotselection_inclusive, plotlabel_inclusive),

    Plot(ROOT.TH1F("CaloMET", "#slash{E}_{T,Calo}", 50, 0., 1000.),
         "#slash{E}_{T,Calo}", plotselection_inclusive, plotlabel_inclusive),

    Plot(ROOT.TH1F("CaloMET_PFMET_ratio", "#slash{E}_{T,Calo} #slash{E}_{T,PF} ratio", 50, 0., 1000.),
         "#slash{E}_{T,Calo} #slash{E}_{T,PF} ratio", plotselection_inclusive, plotlabel_inclusive),

    Plot(ROOT.TH1F("dPhi_Jet_MET", "#Delta #phi (#slash{E}_{T},ak4-jets)", 50, 0., 1000.),
         "#Delta #phi (#slash{E}_{T},ak4-jets)", plotselection_inclusive, plotlabel_inclusive),



  # TH1F* h_Jet_PtAK8 = 0;
  # std::map<std::string, TH1F*> h_Jet_PtAK8Sys;

  # TH1F* h_Jet_EtaAK8 = 0;
  # std::map<std::string, TH1F*> h_Jet_EtaAK8Sys;

  # TH1F* h_Jet_PhiAK8 = 0;
  # std::map<std::string, TH1F*> h_Jet_PhiAK8Sys;

  # TH1F* h_Jet_Chf = 0;
  # std::map<std::string, TH1F*> h_Jet_ChfSys;

  # TH1F* h_Jet_Nhf = 0;
  # std::map<std::string, TH1F*> h_Jet_NhfSys;

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

outputpath = THEoutputpath + "/histos.root"
outputpathSignal = "/nfs/dust/cms/user/swieland/Darkmatter/DM_Unfolding/rootfiles/signals.root"
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
    outputpath, samples_signal, plots, 1, isSignal=True)
lolT_signal = transposeLOL(listOfHistoLists_signal)
print "listOfHistoLists_signal=", listOfHistoLists_signal
print "listOfHistoListsTransposed_signal=", lolT_signal

# data
listOfHistoLists_data = createHistoLists_fromSuperHistoFile(
    outputpath, samples_data, plots, 1)
print "listOfHistoLists_data=", listOfHistoLists_data

print "Making MC Control plots"

lll = createLLL_fromSuperHistoFileSyst(
    outputpath, samples_background, plots, allSystnames)
# for ll in lll:
# for l in ll:
# for item in l:
# item.Print()

# for hist in lUnfoldedData:
#   print hist
labels = [plot.label for plot in plots]
# print labels
print "lolT_signal[0]:", lolT_signal[0]

plotDataMCanWsyst(listOfHistoLists_data, transposeLOL(lolT_background), samples_background,
                  lolT_signal[0], samples_signal[0], -1, jobname, [[lll, 3354, ROOT.kBlack, True]], True, labels, ratio=True, blinded=False, verbosity=0)

plotDataMCanWsyst(listOfHistoLists_data, transposeLOL(lolT_background), samples_background,
                  lolT_signal[0], samples_signal[0], -1, jobname+"_noRatio", [[lll, 3354, ROOT.kBlack, True]], True, labels, ratio=False, blinded=False, verbosity=0)
