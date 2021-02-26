
import sys
import os
filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = os.path.dirname(filedir)
basedir = os.path.dirname(pyrootdir)
sys.path.append(pyrootdir)
sys.path.append(basedir)

import util.tools.plotClasses as plotClasses
import ROOT
from array import array
from copy import deepcopy
import unfolding_setup as unfolding_setup


memexp = ""
reco_bins = []
gen_bins  = []
n_bins_per_bin = []

genSel  = ""
recoSel = ""
recoLabel = ""
recoTag = ""

gen_variable = ""
reco_variable = ""

name_tag = ""
gen_label_tag = ""
reco_label_tag = ""


evtYields = "(N_Jets==4&&N_BTagsM==3)*1"
evtYields+="+(N_Jets==4&&N_BTagsM>=4)*2"
evtYields+="+(N_Jets==5&&N_BTagsM==3)*3"
evtYields+="+(N_Jets==5&&N_BTagsM>=4)*4"
evtYields+="+(N_Jets>=6&&N_BTagsM==3)*5"
evtYields+="+(N_Jets>=6&&N_BTagsM>=4)*6"


def plots_control(cat,selection,label):
    plots = [
        plotClasses.Plot(ROOT.TH1D(cat+"_yields","yield",6,0.5,6.5),evtYields,selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_N_BTagsM","b-tagged jet multiplicity",5,2.5,7.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_N_Jets","jet multiplicity",7,3.5,10.5),"N_Jets",selection,label),
        ]
    dummy = [
        plotClasses.Plot(ROOT.TH1D(cat+"_N_PV","number of primary vertices",80,0,80),"N_PrimaryVertices",selection,label),

        #plotClasses.Plot(ROOT.TH1D(cat+"_Electron_Pt","p_{T}(electron) [GeV]",30,30,530),"Electron_Pt[0]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Electron_Eta","#eta(electron)",25,-2.4,2.4),"Electron_Eta[0]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Electron_Phi","#phi(electron)",25,-3.1416,3.1416),"Electron_Phi[0]",selection,label),

        #plotClasses.Plot(ROOT.TH1D(cat+"_Muon_Pt","p_{T}(muon) [GeV]",30,30,530),"Muon_Pt[0]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Muon_Eta","#eta(muon)",25,-2.4,2.4),"Muon_Eta[0]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Muon_Phi","#phi(muon)",25,-3.1416,3.1416),"Muon_Phi[0]",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_Lepton_Pt","p_{T}(lepton) [GeV]",25,30,530),"LooseLepton_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Lepton_Eta","#eta(lepton)",24,-2.4,2.4),"LooseLepton_Eta[0]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Lepton_Phi","#phi(lepton)",25,-3.1416,3.1416),"LooseLepton_Phi[0]",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta","#eta(jets)",24,-2.4,2.4),"Jet_Eta",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Phi","#phi(jets)",25,-3.1416,3.1416),"Jet_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt","p_{T}(jets) [GeV]",35, 30., 730),"Jet_Pt",selection,label),


        plotClasses.Plot(ROOT.TH1D(cat+"_CSV","btag value",30,0.0,1.0),"CSV",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV","Jet_CSV",30,0.0,1.0),"Jet_CSV",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_0","btag value of first jet",30,0.0,1.0),"Jet_CSV[0]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_1","btag value of second jet",30,0.0,1.0),"Jet_CSV[1]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_2","btag value of third jet",30,0.0,1.0),"Jet_CSV[2]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_3","btag value of fourth jet",30,0.0,1.0),"Jet_CSV[3]",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_0","highest btag value",30,0.0,1.0),"CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_1","second highest btag value",30,0.0,1.0),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_2","third highest btag value",30,0.0,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_3","fourth highest btag value",30,0.0,1.0),"CSV[3]",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_HT","H_{T} [GeV]",30,0.0,2000.0),"Evt_HT",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Evt_HT_tags","H_{T}(tagged jets) [GeV]",30,0.0,1000.0),"Evt_HT_tags",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_MET","MET [GeV]",30,10.0,300),"Evt_MET",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Evt_MET_Phi","MET Phi",30,-3.3,3.3),"Evt_MET_Phi",selection,label),

        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_0","leading jet p_{T} [GeV]",30,30.,730.),"Jet_Pt[0]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_1","subleading jet p_{T} [GeV]",30,30.,530.),"Jet_Pt[1]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_2","3rd highest jet p_{T} [GeV]",30,30.,430.),"Jet_Pt[2]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_3","4th highest jet p_{T} [GeV]",30,30.,300.),"Jet_Pt[3]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_4","5th highest jet p_{T} [GeV]",30,30.,300.),"Jet_Pt[4]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_5","6th highest jet p_{T} [GeV]",30,30.,300.),"Jet_Pt[5]",selection,label),

        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_0","#eta of first jet",25,-2.4,2.4),"Jet_Eta[0]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_1","#eta of second jet",25,-2.4,2.4),"Jet_Eta[1]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_2","#eta of third jet",25,-2.4,2.4),"Jet_Eta[2]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_3","#eta of fourth jet",25,-2.4,2.4),"Jet_Eta[3]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_4","#eta of fifth jet",25,-2.4,2.4),"Jet_Eta[4]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_5","#eta of sixth jet",25,-2.4,2.4),"Jet_Eta[5]",selection,label),

        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Phi_0","#phi of first jet",25,-3.1416,3.1416),"Jet_Phi[0]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Phi_1","#phi of second jet",25,-3.1416,3.1416),"Jet_Phi[1]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Phi_2","#phi of third jet",25,-3.1416,3.1416),"Jet_Phi[2]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Phi_3","#phi of fourth jet",25,-3.1416,3.1416),"Jet_Phi[3]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Phi_4","#phi of fifth jet",25,-3.1416,3.1416),"Jet_Phi[4]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Phi_5","#phi of sixth jet",25,-3.1416,3.1416),"Jet_Phi[5]",selection,label),

        #plotClasses.Plot(ROOT.TH1D(cat+"_Evt_Dr_minDrLepJet","Evt_Dr_minDrLepJet",30,0.0,4.0),"Evt_Dr_minDrLepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_Dr_minDrTaggedJets","min #DeltaR(bb)",32,0.3,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_Pt_minDrTaggedJets","p_{T} of min #DeltaR(bb) [GeV]",40,0.0,400.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_M2_minDrTaggedJets","inv. mass of min #DeltaR(bb) [GeV]",40,0.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        ]
    return plots

def plots_controlregion(cat,selection,label):
    plots = [
        plotClasses.Plot(ROOT.TH1D(cat+"_N_BTagsM","b-tagged jet multiplicity",5,2.5,7.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_N_Jets","jet multiplicity",5,3.5,8.5),"N_Jets",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_0","btag value of first jet",30,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_1","btag value of second jet",30,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_2","btag value of third jet",30,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_3","btag value of fourth jet",30,0.0,1.0),"Jet_CSV[3]",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_0","highest btag value",21,0.3,1.0),"CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_1","second highest btag value",21,0.3,1.0),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_2","third highest btag value",21,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_3","fourth highest btag value",9,0.0,0.3),"CSV[3]",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_HT","H_{T} [GeV]",30,0.0,1500.0),"Evt_HT",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_HT_tags","H_{T}(tagged jets) [GeV]",30,0.0,750.0),"Evt_HT_tags",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_0","leading jet p_{T} [GeV]",25,30.,530.),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_1","subleading jet p_{T} [GeV]",25,30.,430.),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_2","3rd highest jet p_{T} [GeV]",25,30.,230.),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_3","4th highest jet p_{T} [GeV]",30,30.,150.),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_4","5th highest jet p_{T} [GeV]",30,30.,150.),"Jet_Pt[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_5","6th highest jet p_{T} [GeV]",35,30.,100.),"Jet_Pt[5]",selection,label),

        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_0","#eta of first jet",24,-2.4,2.4),"Jet_Eta[0]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_1","#eta of second jet",24,-2.4,2.4),"Jet_Eta[1]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_2","#eta of third jet",24,-2.4,2.4),"Jet_Eta[2]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_3","#eta of fourth jet",24,-2.4,2.4),"Jet_Eta[3]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_4","#eta of fifth jet",24,-2.4,2.4),"Jet_Eta[4]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_5","#eta of sixth jet",24,-2.4,2.4),"Jet_Eta[5]",selection,label),
        ]
    return plots

def plots_unfolding(cat,selection,label):
    plots = [
        plotClasses.Plot(ROOT.TH1D(cat+"_N_BTagsM","b-tagged jet multiplicity",3,3.5,6.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_N_Jets","jet multiplicity",4,5.5,9.5),"N_Jets",selection,label),
        ]

    binEdges = [0., 0.05, 0.3, 0.4, 0.7, 0.95, 1.0]
    plots += [
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_0","btag value of first jet",len(binEdges)-1,array("f", binEdges)),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_1","btag value of second jet",len(binEdges)-1,array("f", binEdges)),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_2","btag value of third jet",len(binEdges)-1,array("f", binEdges)),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_3","btag value of fourth jet",len(binEdges)-1,array("f", binEdges)),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_4","btag value of fifth jet",len(binEdges)-1,array("f", binEdges)),"Jet_CSV[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_5","btag value of sixth jet",len(binEdges)-1,array("f", binEdges)),"Jet_CSV[5]",selection,label),
        ]

    binEdges = [0.5, 0.85, 0.95, 0.99, 1.0]
    plots += [
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_0","highest btag value",len(binEdges)-1,array("f", binEdges)),"CSV[0]",selection,label),
        ]

    binEdges = [0.3, 0.6, 0.7, 0.8, 0.9, 0.97, 1.0]
    plots += [
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_1","second highest btag value",len(binEdges)-1,array("f", binEdges)),"CSV[1]",selection,label),
        ]
    binEdges = [0.3,0.5,0.7,0.9,1.0]
    plots += [
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_2","third highest btag value",len(binEdges)-1,array("f", binEdges)),"CSV[2]",selection,label),
        ]
    
    binEdges = [0.3,0.4,0.6,0.8,1.0]
    plots += [
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_3","fourth highest btag value",len(binEdges)-1,array("f", binEdges)),"CSV[3]",selection,label),
        ]

    binEdges = [0., 0.02, 0.05, 0.1, 0.2, 0.5]
    plots += [
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_4","fifth highest btag value",len(binEdges)-1,array("f", binEdges)),"CSV[4]",selection,label),
        ]

    binEdges = [0., 0.01, 0.02,  0.05, 0.3]
    plots += [
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_5","sixth highest btag value",len(binEdges)-1,array("f", binEdges)),"CSV[5]",selection,label),
        ]

    binEdges = [30., 100., 150., 200., 300., 400., 700.]
    plots += [
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_0","leading jet p_{T} [GeV]",len(binEdges)-1,array("f", binEdges)),"Jet_Pt[0]",selection,label),
        ]

    binEdges = [25., 75., 100., 125., 150., 200., 500.]
    plots += [
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_1","subleading jet p_{T} [GeV]",len(binEdges)-1,array("f", binEdges)),"Jet_Pt[1]",selection,label),
        ]

    binEdges = [30., 60., 80., 125., 150,  350.]
    plots += [
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_2","3rd highest jet p_{T} [GeV]",len(binEdges)-1,array("f", binEdges)),"Jet_Pt[2]",selection,label),
        ]

    binEdges = [30., 50., 70., 100., 300.]
    plots += [
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_3","4th highest jet p_{T} [GeV]",len(binEdges)-1,array("f", binEdges)),"Jet_Pt[3]",selection,label),
        ]

    binEdges = [30., 40., 50., 60., 80., 150.]
    plots += [
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_4","5th highest jet p_{T} [GeV]",len(binEdges)-1,array("f", binEdges)),"Jet_Pt[4]",selection,label),
        ]

    binEdges = [30., 35., 40., 45., 50., 70., 150.]
    plots += [
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_5","6th highest jet p_{T} [GeV]",len(binEdges)-1,array("f", binEdges)),"Jet_Pt[5]",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_0","#eta of first jet",8,0,2.4),"abs(Jet_Eta[0])",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_1","#eta of second jet",8,0,2.4),"abs(Jet_Eta[1])",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_2","#eta of third jet",8,0,2.4),"abs(Jet_Eta[2])",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_3","#eta of fourth jet",8,0,2.4),"abs(Jet_Eta[3])",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_4","#eta of fifth jet",8,0,2.4),"abs(Jet_Eta[4])",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_5","#eta of sixth jet",8,0,2.4),"abs(Jet_Eta[5])",selection,label),
        ]

        #plotClasses.Plot(ROOT.TH1D(cat+"_Evt_Dr_minDrLepJet","Evt_Dr_minDrLepJet",30,0.0,4.0),"Evt_Dr_minDrLepJet",selection,label),
    binEdges = [0.]+[i*0.1 for i in range(5,19)]+[2., 3.]
    plots += [
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_Dr_minDrTaggedJets","min #DeltaR(bb)",len(binEdges)-1,array("f", binEdges)),"Evt_Dr_minDrTaggedJets",selection,label),
        ]

    binEdges = [0.]+[i*20 for i in range(3,19)]+[400., 550.]
    plots += [
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_Pt_minDrTaggedJets","p_{T} of min #DeltaR(bb) [GeV]",len(binEdges)-1,array("f", binEdges)),"Evt_Pt_minDrTaggedJets",selection,label),
        ]

    binEdges = [i*10 for i in range(3,19)]+[200., 300.]
    plots += [
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_M2_minDrTaggedJets","inv. mass of min #DeltaR(bb) [GeV]",len(binEdges)-1,array("f", binEdges)),"Evt_M2_minDrTaggedJets",selection,label),
        ]
    
    btag0vs1_expr = "(CSV[0]>=0.7264)*1 + (CSV[1]>=0.7264)*1"
    plots += [
        plotClasses.Plot(ROOT.TH1D(cat+"_btag0vs1","highest vs second highest btag value",3,-0.5,2.5),btag0vs1_expr,selection,label),
        ]
    btag0vs2_expr = "(CSV[0]>=0.7264)*1 + (CSV[2]>=0.7264)*1"
    plots += [
        plotClasses.Plot(ROOT.TH1D(cat+"_btag0vs2","highest vs third highest btag value",3,-0.5,2.5),btag0vs2_expr,selection,label),
        ]
    btag0vs3_expr = "(CSV[0]>=0.7264)*1 + (CSV[3]>=0.7264)*1"
    plots += [
        plotClasses.Plot(ROOT.TH1D(cat+"_btag0vs3","highest vs fourth highest btag value",3,-0.5,2.5),btag0vs3_expr,selection,label),
        ]

    btag1vs2_expr = "(CSV[1]>=0.7264)*1 + (CSV[2]>=0.7264)*1"
    plots += [
        plotClasses.Plot(ROOT.TH1D(cat+"_btag1vs2","second vs third highest btag value",3,-0.5,2.5),btag1vs2_expr,selection,label),
        ]
    btag1vs3_expr = "(CSV[1]>=0.7264)*1 + (CSV[3]>=0.7264)*1"
    plots += [
        plotClasses.Plot(ROOT.TH1D(cat+"_btag1vs3","second vs fourth highest btag value",3,-0.5,2.5),btag1vs3_expr,selection,label),
        ]

    btag2vs3_expr = "(CSV[2]>=0.7264)*1 + (CSV[3]>=0.7264)*1"
    plots += [
        plotClasses.Plot(ROOT.TH1D(cat+"_btag2vs3","third vs fourth highest btag value",3,-0.5,2.5),btag2vs3_expr,selection,label),
        ]

    return plots

def reco_binned_plot(cat, selection, label, nBins, binRange):
    plots = [
        plotClasses.Plot(ROOT.TH1D(cat+"_recoBinned_"+name_tag,reco_label_tag,nBins,binRange[0],binRange[1]),reco_variable,selection,label)
        ]
    return plots

def genInfo(label, data = None):
    plots = [
        plotClasses.TwoDimPlot(ROOT.TH2D(
            "migrationMatrix_{}".format(name_tag),
            "migration matrix {}".format(reco_label_tag),
            len(reco_bins)-1, array("f", reco_bins),
            len(gen_bins)-1,  array("f", gen_bins)),
            "(-1)*(({recoSel})==0)+({recoVar})*(({recoSel})==1)".format(
                recoVar = reco_variable,
                recoSel = recoSel), 
            "(-1)*(({genSel})==0)+({genVar})*(({genSel})==1)".format(
                genVar = gen_variable,
                genSel = genSel),
            "1.",label = label),

        plotClasses.Plot(ROOT.TH1D(
            "recoSel_genBins_{}".format(name_tag),
            "gen. level {}".format(gen_label_tag),
            len(gen_bins)-1, array("f", gen_bins)),
            gen_variable,recoSel,"reco. selection"),

        plotClasses.Plot(ROOT.TH1D(
            "genSel_genBins_{}".format(name_tag),
            "gen. level {}".format(gen_label_tag),
            len(gen_bins)-1, array("f", gen_bins)),
            gen_variable,genSel,"gen. selection"),

        plotClasses.Plot(ROOT.TH1D(
            "noSel_genBins_{}".format(name_tag),
            "gen. level {}".format(gen_label_tag),
            len(gen_bins)-1, array("f", gen_bins)),
            gen_variable,"1.","no selection"),

        plotClasses.Plot(ROOT.TH1D(
            "recoSel_recoBins_{}".format(name_tag),
            "reco. level {}".format(reco_label_tag),
            len(reco_bins)-1, array("f", reco_bins)),
            reco_variable,recoSel, "reco. selection"),
        ]
    return plots

#baseline
def plots_ge4j_ge3t(data=None):
    label = "\geq 4 jets, \geq 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=3)"

    tag = "jt43"
    plots = plots_control(tag, selection, label)    

    if data:
        add_data_plots(plots=plots,data=data)

    return plots

# control region
def plots_ge4j_3t(data=None):
    label = "\geq 4 jets, 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM==3)"

    tag = "cr"
    plots = plots_controlregion(tag, selection, label)    

    if data:
        add_data_plots(plots=plots,data=data)

    return plots

# unfolding region
def unfolding(data=None):
    label = recoLabel
    selection = recoSel
    tag = recoTag

    plots = plots_unfolding(tag, selection, label)    

    for l, s, t, binRange, nbins in unfolding_setup.generateRecoBins(
            label, selection, tag, reco_bins, n_bins_per_bin,
            variable = reco_variable, 
            nameTag = name_tag, labelTag = reco_label_tag):
        plots += plots_unfolding(t, s, l)
        plots += reco_binned_plot(t, s, l, 
            binRange = binRange, nBins = nbins)


    if data:
        add_data_plots(plots=plots,data=data)

    plots += genInfo(label, data)

    return plots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    #baseline
    discriminatorPlots += plots_ge4j_ge3t(data)
    discriminatorPlots += plots_ge4j_3t(data)
    discriminatorPlots += unfolding(data)
    return discriminatorPlots


def init_plots(dictionary, data = None):
    plots = [] #init list of plotClasses objects to return
    for label in dictionary:
        subdict = dictionary[label] #for easy access
        discr = subdict["discr"] # load discriminator name
        sel = subdict["plotPreselections"] # load selection
        histoname = subdict["histoname"] # load histogram name
        histotitle = subdict["histotitle"] # load histogram title

        # check if initialization uses bin edges or min/max vals
        # if 'subdict' contains the keyword 'bin_edges', an array
        # of type float is created from the corresponding python list.
        # Else, the min/maxvals are used
        if "bin_edges" in subdict:
            bins = array("f", subdict["bin_edges"])
            nbins = len(bins)-1 # last bin edge in array is overflow bin => subtract for nbins
            subdict["nhistobins"] = nbins # update number of bins
            plots.append(
                plotClasses.Plot(
                    ROOT.TH1F(histoname,histotitle,nbins,bins),
                    discr,sel,label))
        elif "minxval" in subdict and "maxxval" in subdict:
            nbins = subdict["nhistobins"]
            xmax  = subdict["maxxval"]
            xmin  = subdict["minxval"]
            plots.append(
                plotClasses.Plot(
                    ROOT.TH1F(histoname, histotitle,nbins,xmin, xmax),
                    discr,sel,label))
    if not data is None:
        data.categories.update(dictionary)
    return plots

def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
