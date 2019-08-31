
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



def evtYieldCategories():
    return [
    ("(N_Jets>=6&&N_BTagsM==2)","6j2t",""),
    ("(N_Jets==4&&N_BTagsM==3)","4j3t",""),
    ("(N_Jets==5&&N_BTagsM==3)","5j3t",""),
    ("(N_Jets>=6&&N_BTagsM==3)","6j3t",""),
    ("(N_Jets==4&&N_BTagsM>=4)","4j4t",""),
    ("(N_Jets==5&&N_BTagsM>=4)","5j4t",""),
    ("(N_Jets>=6&&N_BTagsM>=4)","6j4t","")
    ]

memexp = ""

def reco_plots(data=None):
    label = "\geq 6 jets, \geq 3 b-tags"
    selection = "(N_Jets>=6&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("control_Chi2_Z","#chi^{2}(Z)",40,0.0,10.0),"RecoTTZ_Chi2Z",selection,label),
        plotClasses.Plot(ROOT.TH1D("control_Chi2_Z_log","log(#chi^{2}(Z))",40,-10,7),"log(RecoTTZ_Chi2Z+1e-30)",selection,label),
        #plotClasses.Plot(ROOT.TH1D("control_Chi2_Z_over_H_likelihood","#chi^{2}(Z)/#chi^{2}(H)",40,0.0,20.0),"RecoTTZ_Chi2Z/(RecoTTH_Chi2Higgs+1e-30)",selection,label),
        #plotClasses.Plot(ROOT.TH1D("control_Chi2_Z_percentage","#chi^{2}(Z)/(#chi^{2}(Z) + #chi^{2}(H))",40,0.0,1.0),"RecoTTZ_Chi2Z/(RecoTTH_Chi2Higgs+RecoTTZ_Chi2Z)",selection,label),
        #plotClasses.Plot(ROOT.TH1D("control_Chi2_Higgs","#chi^{2}(H)",40,0.0,10.0),"RecoTTH_Chi2Higgs",selection,label),
        #plotClasses.Plot(ROOT.TH1D("control_Chi2_Higgs_log","log(#chi^{2}(H))",40,-10,7),"log(RecoTTH_Chi2Higgs+1e-30)",selection,label),

        plotClasses.Plot(ROOT.TH1D("control_RecoTTZ_TopHad_M_log","log(M(t_{had}))",40,4.5,6.5),"log(RecoTTZ_TopHad_M)",selection,label),
        plotClasses.Plot(ROOT.TH1D("control_RecoTTZ_TopLep_M_log","log(M(t_{lep}))",40,4.5,6.5),"log(RecoTTZ_TopLep_M)",selection,label),
        plotClasses.Plot(ROOT.TH1D("control_RecoTTZ_Z_M_log","log(M(Z))",40,3.5,6.5),"log(RecoTTZ_Z_M)",selection,label),

        plotClasses.Plot(ROOT.TH1D("control_Evt_blr","b-tag likelihood ratio",40,0.,1.),"Evt_blr",selection,label),
        plotClasses.Plot(ROOT.TH1D("control_Evt_blr_transformed","transformed b-tag likelihood ratio",40,-7,15.),"Evt_blr_transformed",selection,label),
        ]
    if data:
        add_data_plots(plots=plots,data=data)

    return plots



def control_plots(data=None):
    label = "\geq 4 jets, \geq 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("inclusive_Jet_Pt","p_{T} of all jets",30,20.0,400.0),"Jet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_N_BTagsM","number of b-tags (medium)",3,2.5,5.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_N_Jets","number of reconstructed jets",8,3.5,11.5),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_CSV_0","highest b-tag value",30,0.7,1.),"CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_JetCSV_0","b-tag value of leading jet",30,0.,1.),"Jet_CSV[0]",selection,label),

        plotClasses.Plot(ROOT.TH1D("inclusive_Electron_Pt","p_{T}(electron)",30,30,200),"Electron_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Electron_Eta","#eta(electron)",30,-2.5,2.5),"Electron_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Electron_Phi","#phi(electron)",30,-3.1416,3.1416),"Electron_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Muon_Pt","p_{T}(muon)",30,25,200),"Muon_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Muon_Eta","#eta(muon)",30,-2.5,2.5),"Muon_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Muon_Phi","#phi(muon)",30,-3.1416,3.1416),"Muon_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Lepton_Pt","p_{T}(lepton)",30,25,200),"LooseLepton_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Lepton_Eta","#eta(lepton)",30,-2.5,2.5),"LooseLepton_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Lepton_Phi","#phi(lepton)",30,-3.1416,3.1416),"LooseLepton_Phi[0]",selection,label),

        plotClasses.Plot(ROOT.TH1D("inclusive_Evt_blr","b-tag likelihood ratio",40,0.,1.),"Evt_blr",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Evt_blr_transformed","transformed b-tag likelihood ratio",40,-7,15.),"Evt_blr_transformed",selection,label),

        plotClasses.Plot(ROOT.TH1D("inclusive_CSV_2","third highest b-tag value",30,0.275,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_CSV_3","fourth highest b-tag value",30,0.0,0.3),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Evt_CSV_avg","average b-tag value",30,0.2,0.8),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Evt_CSV_avg_tagged","average b-tag value of tagged jets",30,0.35,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Evt_CSV_dev","average deviation of b-tag value",30,0.0,0.24),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Evt_CSV_dev_tagged","average deviation of b-tag value of tagged jets",30,0.0,0.12),"Evt_CSV_dev_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Evt_CSV_min_tagged","minimal b-tag value of tagged jets",30,0.28,1.0),"Evt_CSV_min_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",30,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Evt_Dr_minDrTaggedJets","#DeltaR( min #DeltaR(tag,tag) )",30,0.4,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Evt_HT","H_{T}",30,200.0,1700.0),"Evt_HT",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Evt_HT_jets","H_{T}(jets)",30,100.0,1500.0),"Evt_HT_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Evt_HT_wo_MET","H_{T} without MET",30,200.0,1500.0),"Evt_HT_wo_MET",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,50.0,550.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",30,20.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",30,20.0,300.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",30,20.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Evt_M3","M_{3} with highest p_{T}",30,50.0,1000.0),"Evt_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Evt_M_JetsAverage","average M(jets)",30,5.0,30.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,35.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Evt_M_minDrLepTag","M_{2}( min #DeltaR(lep,tag) )",30,25.0,250.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Evt_Pt_minDrJets","p_{T}( min #DeltaR(jet,jet) )",30,50.0,600.0),"Evt_Pt_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",30,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Jet_DeepJetCSV_0","DeepJet b-tag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Jet_Pt_0","p_{T} of leading jet",30,50.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_RecoTTZ_Chi2TopLep","ttZ reconstruction #chi^{2}(t_{lep})",30,0.0,100.0),"RecoTTZ_Chi2TopLep",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_RecoTTZ_Chi2Total","ttZ reconstruction #chi^{2}",30,0.0,200.0),"RecoTTZ_Chi2Total",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_RecoTTZ_Chi2WHad","ttZ reconstruction #chi^{2}(W_{had})",30,0.0,300.0),"RecoTTZ_Chi2WHad",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_RecoTTZ_TopHad_M","ttZ reconstruction M(t_{had})",30,100.0,500.0),"RecoTTZ_TopHad_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_RecoTTZ_TopLep_M","ttZ reconstruction M(t_{lep})",30,100.0,500.0),"RecoTTZ_TopLep_M",selection,label),

        ]
    if data:
        add_data_plots(plots=plots,data=data)

    return plots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += control_plots(data)
    discriminatorPlots += reco_plots(data)

    return discriminatorPlots


def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
    
