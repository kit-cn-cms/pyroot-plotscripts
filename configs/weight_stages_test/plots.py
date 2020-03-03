
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

def plots_inclusive(data=None):
    label = "\geq 4 jets, \geq 3 b-tags (DeepCSV)"
    selection = "(N_Jets>=4&&N_BTagsM_DeepCSV>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("inclusive_Evt_N_Jets","N_Jets",4,3.5,7.5),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Evt_N_BTagsM","N_BTagsM_DeepCSV",3,2.5,5.5),"N_BTagsM_DeepCSV",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_yield","yield",1,0.,1.),"1",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Jet_Pt_0","hardest jet pt",50,0.,1000.),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_HT_jets","Evt_HT_jets",50,0.,1000.),"Evt_HT_jets",selection,label),
        #plotClasses.Plot(ROOT.TH1D("inclusive_Electron_Pt","p_{T}(electron)",50,0,400),"Electron_Pt[0]",selection,label),
        #plotClasses.Plot(ROOT.TH1D("inclusive_Muon_Pt","p_{T}(muon)",50,0,300),"Muon_Pt[0]",selection,label),
        #plotClasses.Plot(ROOT.TH1D("inclusive_Lepton_Pt","p_{T}(lepton)",50,0,300),"LooseLepton_Pt[0]",selection,label),

        ]

    label = "\geq 4 jets, \geq 4 b-tags (DeepCSV)"
    selection = "(N_Jets>=4&&N_BTagsM_DeepCSV>=4)"

    plots+= [
        plotClasses.Plot(ROOT.TH1D("tags4_Evt_N_Jets","N_Jets",4,3.5,7.5),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("tags4_Evt_N_BTagsM","N_BTagsM_DeepCSV",3,2.5,5.5),"N_BTagsM_DeepCSV",selection,label),
        plotClasses.Plot(ROOT.TH1D("tags4_yield","yield",1,0.,1.),"1",selection,label),
        plotClasses.Plot(ROOT.TH1D("tags4_Jet_Pt_0","hardest jet pt",50,0.,1000.),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("tags4_HT_jets","Evt_HT_jets",50,0.,1000.),"Evt_HT_jets",selection,label),
        #plotClasses.Plot(ROOT.TH1D("tags4_Electron_Pt","p_{T}(electron)",50,0,400),"Electron_Pt[0]",selection,label),
        #plotClasses.Plot(ROOT.TH1D("tags4_Muon_Pt","p_{T}(muon)",50,0,300),"Muon_Pt[0]",selection,label),
        #plotClasses.Plot(ROOT.TH1D("tags4_Lepton_Pt","p_{T}(lepton)",50,0,300),"LooseLepton_Pt[0]",selection,label),

        ]


    label = "\geq 4 jets, \geq 0 b-tags (DeepCSV)"
    selection = "(N_Jets>=4&&N_BTagsM_DeepCSV>=0)"

    plots += [
        plotClasses.Plot(ROOT.TH1D("inclusive_0BTag_Evt_N_Jets","N_Jets",4,3.5,7.5),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_0BTag_Evt_N_BTagsM","N_BTagsM_DeepCSV",5,0.5,5.5),"N_BTagsM_DeepCSV",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_0BTag_yield","yield",1,0.,1.),"1",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_0BTag_Jet_Pt_0","hardest jet pt",50,0.,1000.),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_0BTag_HT_jets","Evt_HT_jets",50,0.,1000.),"Evt_HT_jets",selection,label),
        #plotClasses.Plot(ROOT.TH1D("inclusive_Electron_Pt","p_{T}(electron)",50,0,400),"Electron_Pt[0]",selection,label),
        #plotClasses.Plot(ROOT.TH1D("inclusive_Muon_Pt","p_{T}(muon)",50,0,300),"Muon_Pt[0]",selection,label),
        #plotClasses.Plot(ROOT.TH1D("inclusive_Lepton_Pt","p_{T}(lepton)",50,0,300),"LooseLepton_Pt[0]",selection,label),

        ]


 



    if data:
        add_data_plots(plots=plots,data=data)

    return plots
    


def plots_ge4j_ge3t_CSV(data=None):
    label = "\geq 4 jets, \geq 3 b-tags (DeepCSV)"
    selection = "(N_Jets>=4&&N_BTagsM_DeepCSV>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_N_PV","N_PrimaryVertices",50,0,80),"N_PrimaryVertices",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Electron_Pt","p_{T}(electron)",50,0,400),"Electron_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Electron_E","E(electron)",50,0,450),"Electron_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Electron_Eta","#eta(electron)",50,-2.5,2.5),"Electron_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Electron_Phi","#phi(electron)",50,-3.3,3.3),"Electron_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Muon_Pt","p_{T}(muon)",50,0,300),"Muon_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Muon_E","E(muon)",50,0,450),"Muon_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Muon_Eta","#eta(muon)",50,-2.5,2.5),"Muon_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Muon_Phi","#phi(muon)",50,-3.3,3.3),"Muon_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Lepton_Pt","p_{T}(lepton)",50,0,300),"LooseLepton_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Lepton_E","E(lepton)",50,0,450),"LooseLepton_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Lepton_Eta","#eta(lepton)",50,-2.5,2.5),"LooseLepton_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Lepton_Phi","#phi(lepton)",50,-3.3,3.3),"LooseLepton_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_TightLepton_Pt","p_{T}(tight lepton)",50,0,300),"TightLepton_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_TightLepton_E","E(tight lepton)",50,0,450),"TightLepton_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_TightLepton_Eta","#eta(tight lepton)",50,-2.5,2.5),"TightLepton_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_TightLepton_Phi","#phi(tight lepton)",50,-3.3,3.3),"TightLepton_Phi[0]",selection,label),

        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_N_BTagsM","N_BTagsM",8,2.5,10.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_N_Jets","N_Jets",9,3.5,12.5),"N_Jets",selection,label),

        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_CSV","CSV",30,0,1),"CSV",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_DeepJetCSV","Jet_DeepJetCSV",30,0.0,1.0),"Jet_DeepJetCSV",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_CSV","Jet_CSV",30,0.0,1.0),"Jet_CSV",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_CSV_0","Jet CSV[0]",30,0.3,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_CSV_1","Jet CSV[1]",30,0.3,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_CSV_2","Jet CSV[2]",30,0.3,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_CSV_3","Jet CSV[3]",30,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_CSV_0","CSV[0]",30,0.3,1.0),"CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_CSV_1","CSV[1]",30,0.3,1.0),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_CSV_2","CSV[2]",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_CSV_3","CSV[3]",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_CSV_min_tagged","min b-tag value of tagged jets",30,0.3,1.0),"Evt_CSV_min_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_CSV_avg","average b-tag value",30,0.1,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.5),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_TaggedJetsAverage","average #DeltaR Tags",30,0.3,4.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_E_TaggedJetsAverage","average E(tags)",50,0.0,700.0),"Evt_E_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Eta_TaggedJetsAverage","average #eta of tagged Jets",50,-2.5,2.5),"Evt_Eta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_HT","H_{T}",50,150.0,2000.0),"Evt_HT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",40,0.0,600.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_MET","MET",30,10.0,300),"Evt_MET",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_MET_Phi","MET Phi",30,-3.3,3.3),"Evt_MET_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,3.0,35.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Pt_TaggedJetsAverage","average p_{T}(tags)",30,20.0,300.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_TaggedJetPt_over_TaggedJetE","p_{T}(tags)/E(tags)",30,0.2,1.0),"Evt_TaggedJetPt_over_TaggedJetE",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M2_closestTo125TaggedJets","M2_closestTo125TaggedJets",30,0.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),

        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Deta_maxDetaTagTag","Evt_Deta_maxDetaTagTag",30,0.0,2.0),"Evt_Deta_maxDetaTagTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_sphericity_jets","Evt_sphericity_jets",30,0.0,1.0),"Evt_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_sphericity_tags","Evt_sphericity_tags",30,0.0,1.0),"Evt_sphericity_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_blr","Evt_blr",30,-0.05,1.0),"Evt_blr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_blr_transformed","Evt_blr_transformed",30,-6.0,16.0),"Evt_blr_transformed",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_Pt_0","Jet_Pt[0]",30,20,500),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_Pt_2","Jet_Pt[2]",30,20,350),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_HT_tags","Evt_HT_tags",50,50.0,1200.0),"Evt_HT_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_minDrLepTag","Evt_M_minDrLepTag",30,0.0,350.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_CSV_avg_tagged","Evt_CSV_avg_tagged",30,0.3,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_maxDrJets","Evt_Dr_maxDrJets",30,1.5,6.0),"Evt_Dr_maxDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_minDrLepTag","Evt_Dr_minDrLepTag",30,0.3,3.5),"Evt_Dr_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_minDrTaggedJets","Evt_Dr_minDrTaggedJets",30,0.3,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_HT_wo_MET","Evt_HT_wo_MET",50,100.0,1600.0),"Evt_HT_wo_MET",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Pt_minDrJets","Evt_Pt_minDrJets",40,1.0,600.0),"Evt_Pt_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Pt_minDrTaggedJets","Evt_Pt_minDrTaggedJets",40,0.0,600.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",30,1.0,4.0),"Evt_Dr_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_minDrJets","Evt_Dr_minDrJets",30,0.3,3.2),"Evt_Dr_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Deta_maxDetaJetJet","Evt_Deta_maxDetaJetJet",30,0.0,1.8),"Evt_Deta_maxDetaJetJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_transverse_sphericity_jets","Evt_transverse_sphericity_jets", 30,0.0,1.0),"Evt_transverse_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_CSV_dev_tagged","Evt_CSV_dev_tagged",30,0.0,0.12),"Evt_CSV_dev_tagged",selection,label),

        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_E","Jet_E",60,0,800),"Jet_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_Eta","Jet_Eta",30,-2.5,2.5),"Jet_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_M","Jet_M",30,0.0,50.0),"Jet_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_Phi","Jet_Phi",30,-3.3,3.3),"Jet_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_Pt","Jet_Pt",40,20,400),"Jet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_LooseJet_E","LooseJet_E",100,0,1000),"LooseJet_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_LooseJet_Eta","LooseJet_Eta",40,-4,4),"LooseJet_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_LooseJet_M","LooseJet_M",30,0,60),"LooseJet_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_LooseJet_Phi","LooseJet_Phi",30,-3.3,3.3),"LooseJet_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_LooseJet_Pt","LooseJet_Pt",40,20,400),"LooseJet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_TaggedJet_E","TaggedJet_E",60,0,800),"TaggedJet_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_TaggedJet_Eta","TaggedJet_Eta",30,-2.5,2.5),"TaggedJet_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_TaggedJet_M","TaggedJet_M",30,0,50),"TaggedJet_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_TaggedJet_Phi","TaggedJet_Phi",30,-3.3,3.3),"TaggedJet_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_TaggedJet_Pt","TaggedJet_Pt",30,20,400),"TaggedJet_Pt",selection,label),
        ]

   

    if data:
        add_data_plots(plots=plots,data=data)

    return plots


def plots_ge4j_0t(data=None):
    label = "\geq 4 jets, \geq 0 b-tags (DeepCSV)"
    selection = "(N_Jets>=4&&N_BTagsM_DeepCSV>=0)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_N_PV","N_PrimaryVertices",50,0,80),"N_PrimaryVertices",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Electron_Pt","p_{T}(electron)",50,0,400),"Electron_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Electron_E","E(electron)",50,0,450),"Electron_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Electron_Eta","#eta(electron)",50,-2.5,2.5),"Electron_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Electron_Phi","#phi(electron)",50,-3.3,3.3),"Electron_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Muon_Pt","p_{T}(muon)",50,0,300),"Muon_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Muon_E","E(muon)",50,0,450),"Muon_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Muon_Eta","#eta(muon)",50,-2.5,2.5),"Muon_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Muon_Phi","#phi(muon)",50,-3.3,3.3),"Muon_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Lepton_Pt","p_{T}(lepton)",50,0,300),"LooseLepton_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Lepton_E","E(lepton)",50,0,450),"LooseLepton_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Lepton_Eta","#eta(lepton)",50,-2.5,2.5),"LooseLepton_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Lepton_Phi","#phi(lepton)",50,-3.3,3.3),"LooseLepton_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_TightLepton_Pt","p_{T}(tight lepton)",50,0,300),"TightLepton_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_TightLepton_E","E(tight lepton)",50,0,450),"TightLepton_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_TightLepton_Eta","#eta(tight lepton)",50,-2.5,2.5),"TightLepton_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_TightLepton_Phi","#phi(tight lepton)",50,-3.3,3.3),"TightLepton_Phi[0]",selection,label),

        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_N_BTagsM","N_BTagsM",8,2.5,10.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_N_Jets","N_Jets",9,3.5,12.5),"N_Jets",selection,label),

        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_CSV","CSV",30,0,1),"CSV",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_DeepJetCSV","Jet_DeepJetCSV",30,0.0,1.0),"Jet_DeepJetCSV",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_CSV","Jet_CSV",30,0.0,1.0),"Jet_CSV",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_CSV_0","Jet CSV[0]",30,0.3,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_CSV_1","Jet CSV[1]",30,0.3,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_CSV_2","Jet CSV[2]",30,0.3,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_CSV_3","Jet CSV[3]",30,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_CSV_0","CSV[0]",30,0.3,1.0),"CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_CSV_1","CSV[1]",30,0.3,1.0),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_CSV_2","CSV[2]",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_CSV_3","CSV[3]",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_CSV_min_tagged","min b-tag value of tagged jets",30,0.3,1.0),"Evt_CSV_min_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_CSV_avg","average b-tag value",30,0.1,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.5),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_TaggedJetsAverage","average #DeltaR Tags",30,0.3,4.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_E_TaggedJetsAverage","average E(tags)",50,0.0,700.0),"Evt_E_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Eta_TaggedJetsAverage","average #eta of tagged Jets",50,-2.5,2.5),"Evt_Eta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_HT","H_{T}",50,150.0,2000.0),"Evt_HT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",40,0.0,600.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_MET","MET",30,10.0,300),"Evt_MET",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_MET_Phi","MET Phi",30,-3.3,3.3),"Evt_MET_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,3.0,35.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Pt_TaggedJetsAverage","average p_{T}(tags)",30,20.0,300.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_TaggedJetPt_over_TaggedJetE","p_{T}(tags)/E(tags)",30,0.2,1.0),"Evt_TaggedJetPt_over_TaggedJetE",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M2_closestTo125TaggedJets","M2_closestTo125TaggedJets",30,0.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),

        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Deta_maxDetaTagTag","Evt_Deta_maxDetaTagTag",30,0.0,2.0),"Evt_Deta_maxDetaTagTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_sphericity_jets","Evt_sphericity_jets",30,0.0,1.0),"Evt_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_sphericity_tags","Evt_sphericity_tags",30,0.0,1.0),"Evt_sphericity_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_blr","Evt_blr",30,-0.05,1.0),"Evt_blr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_blr_transformed","Evt_blr_transformed",30,-6.0,16.0),"Evt_blr_transformed",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_Pt_0","Jet_Pt[0]",30,20,500),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_Pt_2","Jet_Pt[2]",30,20,350),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_HT_tags","Evt_HT_tags",50,50.0,1200.0),"Evt_HT_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_minDrLepTag","Evt_M_minDrLepTag",30,0.0,350.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_CSV_avg_tagged","Evt_CSV_avg_tagged",30,0.3,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_maxDrJets","Evt_Dr_maxDrJets",30,1.5,6.0),"Evt_Dr_maxDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_minDrLepTag","Evt_Dr_minDrLepTag",30,0.3,3.5),"Evt_Dr_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_minDrTaggedJets","Evt_Dr_minDrTaggedJets",30,0.3,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_HT_wo_MET","Evt_HT_wo_MET",50,100.0,1600.0),"Evt_HT_wo_MET",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Pt_minDrJets","Evt_Pt_minDrJets",40,1.0,600.0),"Evt_Pt_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Pt_minDrTaggedJets","Evt_Pt_minDrTaggedJets",40,0.0,600.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",30,1.0,4.0),"Evt_Dr_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_minDrJets","Evt_Dr_minDrJets",30,0.3,3.2),"Evt_Dr_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Deta_maxDetaJetJet","Evt_Deta_maxDetaJetJet",30,0.0,1.8),"Evt_Deta_maxDetaJetJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_transverse_sphericity_jets","Evt_transverse_sphericity_jets", 30,0.0,1.0),"Evt_transverse_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_CSV_dev_tagged","Evt_CSV_dev_tagged",30,0.0,0.12),"Evt_CSV_dev_tagged",selection,label),

        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_E","Jet_E",60,0,800),"Jet_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_Eta","Jet_Eta",30,-2.5,2.5),"Jet_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_M","Jet_M",30,0.0,50.0),"Jet_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_Phi","Jet_Phi",30,-3.3,3.3),"Jet_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_Pt","Jet_Pt",40,20,400),"Jet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_LooseJet_E","LooseJet_E",100,0,1000),"LooseJet_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_LooseJet_Eta","LooseJet_Eta",40,-4,4),"LooseJet_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_LooseJet_M","LooseJet_M",30,0,60),"LooseJet_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_LooseJet_Phi","LooseJet_Phi",30,-3.3,3.3),"LooseJet_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_LooseJet_Pt","LooseJet_Pt",40,20,400),"LooseJet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_TaggedJet_E","TaggedJet_E",60,0,800),"TaggedJet_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_TaggedJet_Eta","TaggedJet_Eta",30,-2.5,2.5),"TaggedJet_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_TaggedJet_M","TaggedJet_M",30,0,50),"TaggedJet_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_TaggedJet_Phi","TaggedJet_Phi",30,-3.3,3.3),"TaggedJet_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_TaggedJet_Pt","TaggedJet_Pt",30,20,400),"TaggedJet_Pt",selection,label),
        ]

   

    if data:
        add_data_plots(plots=plots,data=data)

    return plots



def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_inclusive(data)
    # discriminatorPlots += plots_ge4j_ge3t_CSV(data)
    # discriminatorPlots += plots_ge4j_0t(data)
    #discriminatorPlots += plots_ge4j_ge3t(data)
    #discriminatorPlots += plots_ge4j_3t(data)
    #discriminatorPlots += plots_ge4j_ge4t(data)
    #discriminatorPlots += plots_ge6j_ge3t(data)

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
