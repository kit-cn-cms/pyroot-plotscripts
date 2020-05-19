
import sys
import os
filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = os.path.dirname(filedir)
basedir = os.path.dirname(pyrootdir)
sys.path.append(pyrootdir)
sys.path.append(basedir)

import util.tools.plotClasses as plotClasses
import util.variableHistoInterface as vhi
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

# memexp = '(memDBp>=0.0)*(memDBp)+(memDBp<0.0)*(0.01)+(memDBp==1.0)*(0.01)'
memexp = '(memDBp>=0.0)*(memDBp)+(memDBp<0.0)*(0.01)+(memDBp==1.0)*(1.1)'

yieldExpression = "(N_Jets==4 && N_BTagsM==3)*1"
yieldExpression+="+(N_Jets==4 && N_BTagsM>=4)*2"
yieldExpression+="+(N_Jets==5 && N_BTagsM==3)*3"
yieldExpression+="+(N_Jets==5 && N_BTagsM>=4)*4"
yieldExpression+="+(N_Jets>=6 && N_BTagsM==3)*5"
yieldExpression+="+(N_Jets>=6 && N_BTagsM>=4)*6"

def plots_crossCheck(cat,selection,label):
    plots = [
        # plotClasses.Plot(ROOT.TH1D(cat+"_memDBp","MEM",30,0.0,1.0),"memDBp",selection,label),
        plotClasses.TwoDimPlot(ROOT.TH2F(cat+"_crosscheck_N_BTagsM","number of B tags (orig tree vs friend tree)",6,3.5,9.5,6,3.5,9.5),
            "N_BTagsM","MEMDB.N_BTagsM",selection,label),
        plotClasses.TwoDimPlot(ROOT.TH2F(cat+"_N_BTagsM_vs_MEM","number of B tags vs MEM",6,3.5,9.5,40,0.0,1.2),
            "N_BTagsM",memexp,selection,label),
        plotClasses.TwoDimPlot(ROOT.TH2F(cat+"_N_Jets_vs_MEM","number of Jets vs MEM",9,0.5,9.5,40,0.0,1.2),
            "N_Jets",memexp,selection,label),
    ]
    return plots

def plots_control(cat,selection,label):
    plots = [
        plotClasses.Plot(ROOT.TH1D(cat+"_memDBp","MEM",40,0.0,1.2),memexp,selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_evtYield","yields",6,0.5,6.5),yieldExpression,selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_N_PV","N_PrimaryVertices",80,0,80),"N_PrimaryVertices",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Electron_Pt","p_{T}(electron)",50,0,400),"Electron_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Electron_E","E(electron)",50,0,450),"Electron_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Electron_Eta","#eta(electron)",50,-2.5,2.5),"Electron_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Electron_Phi","#phi(electron)",50,-3.3,3.3),"Electron_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Muon_Pt","p_{T}(muon)",50,0,300),"Muon_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Muon_E","E(muon)",50,0,450),"Muon_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Muon_Eta","#eta(muon)",50,-2.5,2.5),"Muon_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Muon_Phi","#phi(muon)",50,-3.3,3.3),"Muon_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Lepton_Pt","p_{T}(lepton)",50,0,300),"LooseLepton_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Lepton_E","E(lepton)",50,0,450),"LooseLepton_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Lepton_Eta","#eta(lepton)",50,-2.5,2.5),"LooseLepton_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Lepton_Phi","#phi(lepton)",50,-3.3,3.3),"LooseLepton_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_TightLepton_Pt","p_{T}(tight lepton)",50,0,300),"TightLepton_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_TightLepton_E","E(tight lepton)",50,0,450),"TightLepton_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_TightLepton_Eta","#eta(tight lepton)",50,-2.5,2.5),"TightLepton_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_TightLepton_Phi","#phi(tight lepton)",50,-3.3,3.3),"TightLepton_Phi[0]",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_N_BTagsM","N_BTagsM",8,2.5,10.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_N_Jets","N_Jets",9,3.5,12.5),"N_Jets",selection,label),

        # plotClasses.Plot(ROOT.TH1D(cat+"_N_Jets_Ele","N_Jets_Ele",9,3.5,12.5),"N_Jets","(" + selection + "&& (N_LooseMuons==0 && N_TightElectrons==1))",label),
        # plotClasses.Plot(ROOT.TH1D(cat+"_N_BTagsM_Ele","N_BTagsM_Ele",8,2.5,10.5),"N_BTagsM","(" + selection + "&& (N_LooseMuons==0 && N_TightElectrons==1))",label),

        # plotClasses.Plot(ROOT.TH1D(cat+"_N_Jets_Muon","N_Jets_Muon",9,3.5,12.5),"N_Jets","(" + selection + "&& (N_LooseMuons==0 && N_TightElectrons==1))",label),
        # plotClasses.Plot(ROOT.TH1D(cat+"_N_BTagsM_Muon","N_BTagsM_Muon",8,2.5,10.5),"N_BTagsM","(" + selection + "&& (N_LooseElectrons==0 && N_TightMuons==1))",label),


        plotClasses.Plot(ROOT.TH1D(cat+"_N_ForwardJets","N_ForwardJets",6,0.5,6.5),"N_ForwardJets",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_ForwardJet_Pt","ForwardJet_Pt",40,20,400),"ForwardJet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_ForwardJet_Eta","ForwardJet_Eta",30,-5.5,5.5),"ForwardJet_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_ForwardJet_M","ForwardJet_M",30,0.0,50.0),"ForwardJet_M",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_ForwardJet_Phi","ForwardJet_Phi",30,-3.3,3.3),"ForwardJet_Phi",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_CSV","CSV",30,0,1),"CSV",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_DeepJetCSV","Jet_DeepJetCSV",30,0.0,1.0),"Jet_DeepJetCSV",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV","Jet_CSV",30,0.0,1.0),"Jet_CSV",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_0","Jet CSV[0]",30,0.3,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_1","Jet CSV[1]",30,0.3,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_2","Jet CSV[2]",30,0.3,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_3","Jet CSV[3]",30,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_4","Jet CSV[4]",30,0.0,1.0),"Jet_CSV[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_5","Jet CSV[5]",30,0.0,1.0),"Jet_CSV[5]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_6","Jet CSV[6]",30,0.0,1.0),"Jet_CSV[6]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_0","CSV[0]",30,0.3,1.0),"CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_1","CSV[1]",30,0.3,1.0),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_2","CSV[2]",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_3","CSV[3]",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_4","CSV[3]",30,0.0,1.0),"CSV[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_5","CSV[3]",30,0.0,1.0),"CSV[5]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_6","CSV[3]",30,0.0,1.0),"CSV[6]",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_0","Jet_Pt[0]",30,20,500),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_1","Jet_Pt[1]",30,20,500),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_2","Jet_Pt[2]",30,20,350),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_3","Jet_Pt[3]",30,20,250),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_4","Jet_Pt[4]",30,20,250),"Jet_Pt[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_5","Jet_Pt[5]",30,20,250),"Jet_Pt[5]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_6","Jet_Pt[6]",30,20,250),"Jet_Pt[6]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_0","Jet_Eta[0]",30,-2.5,2.5),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_1","Jet_Eta[1]",30,-2.5,2.5),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_2","Jet_Eta[2]",30,-2.5,2.5),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_3","Jet_Eta[3]",30,-2.5,2.5),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_4","Jet_Eta[4]",30,-2.5,2.5),"Jet_Eta[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_5","Jet_Eta[5]",30,-2.5,2.5),"Jet_Eta[5]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_6","Jet_Eta[6]",30,-2.5,2.5),"Jet_Eta[6]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Phi_0","Jet_Phi[0]",30,-3.3,3.3),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Phi_1","Jet_Phi[1]",30,-3.3,3.3),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Phi_2","Jet_Phi[2]",30,-3.3,3.3),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Phi_3","Jet_Phi[3]",30,-3.3,3.3),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Phi_4","Jet_Phi[4]",30,-3.3,3.3),"Jet_Phi[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Phi_5","Jet_Phi[5]",30,-3.3,3.3),"Jet_Phi[5]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Phi_6","Jet_Phi[6]",30,-3.3,3.3),"Jet_Phi[6]",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_E","Jet_E",60,0,800),"Jet_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta","Jet_Eta",30,-2.5,2.5),"Jet_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_M","Jet_M",30,0.0,50.0),"Jet_M",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Phi","Jet_Phi",30,-3.3,3.3),"Jet_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt","Jet_Pt",40,20,400),"Jet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_LooseJet_E","LooseJet_E",100,0,1000),"LooseJet_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_LooseJet_Eta","LooseJet_Eta",40,-4,4),"LooseJet_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_LooseJet_M","LooseJet_M",30,0,60),"LooseJet_M",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_LooseJet_Phi","LooseJet_Phi",30,-3.3,3.3),"LooseJet_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_LooseJet_Pt","LooseJet_Pt",40,20,400),"LooseJet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_TaggedJet_E","TaggedJet_E",60,0,800),"TaggedJet_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_TaggedJet_Eta","TaggedJet_Eta",30,-2.5,2.5),"TaggedJet_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_TaggedJet_M","TaggedJet_M",30,0,50),"TaggedJet_M",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_TaggedJet_Phi","TaggedJet_Phi",30,-3.3,3.3),"TaggedJet_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_TaggedJet_Pt","TaggedJet_Pt",30,20,400),"TaggedJet_Pt",selection,label),
        ]
    return plots

def plots_inputfeatures_ge4j_ge4t(data = None):
    label = "\geq 4 jets, \geq 4 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"
    
    interf_ljets_ge4j_ge4t_Evt_CSV_avg_tagged = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg_tagged",
                                            label          = "ljets_ge4j_ge4t_Evt_CSV_avg_tagged",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_CSV_avg_tagged.category_label = label
    interf_ljets_ge4j_ge4t_Evt_CSV_avg_tagged.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_CSV_avg_tagged","")
    interf_ljets_ge4j_ge4t_Evt_CSV_avg_tagged.bin_edges = [ 
				0.412,
				0.468,
				0.496,
				0.51,
				0.524,
				0.538,
				0.552,
				0.566,
				0.58,
				0.594,
				0.608,
				0.622,
				0.636,
				0.65,
				0.664,
				0.678,
				0.692,
				0.706,
				0.72,
				0.734,
				0.748,
				0.762,
				0.776,
				0.79,
				0.804,
				0.818,
				0.832,
				0.846,
				0.86,
				0.874,
				0.888,
				0.902,
				0.916,
				0.93,
				0.944,
				0.958,
				0.972,
				0.986,
				1.0
				]
    interf_ljets_ge4j_ge4t_Evt_CSV_avg_tagged.histotitle = "Evt_CSV_avg_tagged"
    interf_ljets_ge4j_ge4t_Evt_CSV_avg_tagged.histoname = "ljets_ge4j_ge4t_Evt_CSV_avg_tagged"
    interf_ljets_ge4j_ge4t_Evt_CSV_avg_tagged.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_CSV_avg_tagged)

    interf_ljets_ge4j_ge4t_Evt_CSV_avg = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg",
                                            label          = "ljets_ge4j_ge4t_Evt_CSV_avg",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_CSV_avg.category_label = label
    interf_ljets_ge4j_ge4t_Evt_CSV_avg.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_CSV_avg","")
    interf_ljets_ge4j_ge4t_Evt_CSV_avg.bin_edges = [ 
                0.252,
                0.286,
                0.303,
                0.32,
                0.337,
                0.354,
                0.371,
                0.388,
                0.405,
                0.422,
                0.439,
                0.456,
                0.473,
                0.49,
                0.507,
                0.524,
                0.541,
                0.558,
                0.575,
                0.592,
                0.609,
                0.626,
                0.643,
                0.66,
                0.677,
                0.694,
                0.711,
                0.728,
                0.745,
                0.762,
                0.779,
                0.796,
                0.813,
                0.83,
                0.847,
                0.864,
                0.881,
                0.898,
                0.915,
                0.932,
                0.949,
                0.966,
                0.983,
                1.0
                ]
    interf_ljets_ge4j_ge4t_Evt_CSV_avg.histotitle = "Evt_CSV_avg"
    interf_ljets_ge4j_ge4t_Evt_CSV_avg.histoname = "ljets_ge4j_ge4t_Evt_CSV_avg"
    interf_ljets_ge4j_ge4t_Evt_CSV_avg.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_CSV_avg)

    interf_ljets_ge4j_ge4t_Evt_M_minDrLepTag = vhi.variableHistoInterface(variable_name  = "Evt_M_minDrLepTag",
                                            label          = "ljets_ge4j_ge4t_Evt_M_minDrLepTag",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_M_minDrLepTag.category_label = label
    interf_ljets_ge4j_ge4t_Evt_M_minDrLepTag.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_M_minDrLepTag","")
    interf_ljets_ge4j_ge4t_Evt_M_minDrLepTag.bin_edges = [ 
				15.0,
				22.7,
				30.4,
				38.1,
				45.8,
				53.5,
				61.2,
				68.9,
				76.6,
				84.3,
				92.0,
				99.7,
				107.4,
				115.1,
				122.8,
				130.5,
				138.2,
				145.9,
				153.6,
				161.3,
				169.0,
				176.7,
				184.4,
				192.1,
				199.8,
				215.2,
				230.6,
				253.7,
				292.2,
				338.4,
				400.0
				]
    interf_ljets_ge4j_ge4t_Evt_M_minDrLepTag.histotitle = "Evt_M_minDrLepTag"
    interf_ljets_ge4j_ge4t_Evt_M_minDrLepTag.histoname = "ljets_ge4j_ge4t_Evt_M_minDrLepTag"
    interf_ljets_ge4j_ge4t_Evt_M_minDrLepTag.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_M_minDrLepTag)

    interf_ljets_ge4j_ge4t_Evt_Pt_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Pt_JetsAverage",
                                            label          = "ljets_ge4j_ge4t_Evt_Pt_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_Pt_JetsAverage.category_label = label
    interf_ljets_ge4j_ge4t_Evt_Pt_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_Pt_JetsAverage","")
    interf_ljets_ge4j_ge4t_Evt_Pt_JetsAverage.bin_edges = [ 
				39.4,
				48.8,
				58.2,
				67.6,
				77.0,
				86.4,
				95.8,
				105.2,
				114.6,
				124.0,
				133.4,
				142.8,
				152.2,
				161.6,
				171.0,
				180.4,
				189.8,
				199.2,
				208.6,
				218.0,
				236.8,
				265.0,
				302.6,
				500.0
				]
    interf_ljets_ge4j_ge4t_Evt_Pt_JetsAverage.histotitle = "Evt_Pt_JetsAverage"
    interf_ljets_ge4j_ge4t_Evt_Pt_JetsAverage.histoname = "ljets_ge4j_ge4t_Evt_Pt_JetsAverage"
    interf_ljets_ge4j_ge4t_Evt_Pt_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_Pt_JetsAverage)

    interf_ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets = vhi.variableHistoInterface(variable_name  = "Evt_Pt_minDrTaggedJets",
                                            label          = "ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets.category_label = label
    interf_ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets","")
    interf_ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets.bin_edges = [ 
				43.2,
				54.8,
				66.4,
				78.0,
				89.6,
				101.2,
				112.8,
				124.4,
				136.0,
				147.6,
				159.2,
				170.8,
				182.4,
				194.0,
				205.6,
				217.2,
				228.8,
				240.4,
				252.0,
				263.6,
				275.2,
				286.8,
				298.4,
				310.0,
				321.6,
				333.2,
				344.8,
				356.4,
				368.0,
				379.6,
				391.2,
				402.8,
				414.4,
				426.0,
				449.2,
				472.4,
				495.6,
				518.8,
				553.6,
				588.4,
				600.0
				]
    interf_ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets.histotitle = "Evt_Pt_minDrTaggedJets"
    interf_ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets.histoname = "ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets"
    interf_ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets)

    interf_ljets_ge4j_3t_Evt_Deta_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Deta_TaggedJetsAverage",
                                            label          = "ljets_ge4j_3t_Evt_Deta_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_Deta_TaggedJetsAverage.category_label = label
    interf_ljets_ge4j_3t_Evt_Deta_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_Deta_TaggedJetsAverage","")
    interf_ljets_ge4j_3t_Evt_Deta_TaggedJetsAverage.bin_edges = [ 
				0.0,
				0.06,
				0.12,
				0.18,
				0.24,
				0.3,
				0.36,
				0.42,
				0.48,
				0.54,
				0.6,
				0.66,
				0.72,
				0.78,
				0.84,
				0.9,
				0.96,
				1.02,
				1.08,
				1.14,
				1.2,
				1.26,
				1.32,
				1.38,
				1.44,
				1.5,
				1.56,
				1.62,
				1.68,
				1.74,
				1.8,
				1.86,
				1.92,
				1.98,
				2.04,
				2.1,
				2.16,
				2.22,
				2.28,
				2.34,
				2.4,
				2.46,
				2.52,
				2.58,
				2.64,
				2.7,
				2.76,
				2.82,
				2.88,
				2.94,
				3.0
				]
    interf_ljets_ge4j_3t_Evt_Deta_TaggedJetsAverage.histotitle = "Evt_Deta_TaggedJetsAverage"
    interf_ljets_ge4j_3t_Evt_Deta_TaggedJetsAverage.histoname = "ljets_ge4j_3t_Evt_Deta_TaggedJetsAverage"
    interf_ljets_ge4j_3t_Evt_Deta_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_Deta_TaggedJetsAverage)

    interf_ljets_ge4j_ge4t_Evt_Deta_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Deta_JetsAverage",
                                            label          = "ljets_ge4j_ge4t_Evt_Deta_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_Deta_JetsAverage.category_label = label
    interf_ljets_ge4j_ge4t_Evt_Deta_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_Deta_JetsAverage","")
    interf_ljets_ge4j_ge4t_Evt_Deta_JetsAverage.bin_edges = [ 
				0.24,
				0.36,
				0.42,
				0.48,
				0.54,
				0.6,
				0.66,
				0.72,
				0.78,
				0.84,
				0.9,
				0.96,
				1.02,
				1.08,
				1.14,
				1.2,
				1.26,
				1.32,
				1.38,
				1.44,
				1.5,
				1.56,
				1.62,
				1.68,
				1.74,
				1.8,
				1.86,
				1.92,
				2.04,
				2.16,
				3.0
				]
    interf_ljets_ge4j_ge4t_Evt_Deta_JetsAverage.histotitle = "Evt_Deta_JetsAverage"
    interf_ljets_ge4j_ge4t_Evt_Deta_JetsAverage.histoname = "ljets_ge4j_ge4t_Evt_Deta_JetsAverage"
    interf_ljets_ge4j_ge4t_Evt_Deta_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_Deta_JetsAverage)

    interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau2 = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttbar_Jet_CSV_whaddau2",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau2",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau2.category_label = label
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau2.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau2","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau2.bin_edges = [ 
				0.0,
				0.02,
				0.04,
				0.06,
				0.08,
				0.1,
				0.14,
				0.2,
				0.3,
				0.32,
				0.34,
				0.36,
				0.38,
				0.4,
				0.42,
				0.44,
				0.46,
				0.48,
				0.5,
				0.52,
				0.54,
				0.56,
				0.58,
				0.6,
				0.62,
				0.64,
				0.66,
				0.68,
				0.7,
				0.72,
				0.74,
				0.76,
				0.78,
				0.8,
				0.84,
				0.88,
				0.94,
				1.0
				]
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau2.histotitle = "Reco_JABDT_ttbar_Jet_CSV_whaddau2"
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau2.histoname = "ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau2"
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau2.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau2)

    interf_ljets_ge4j_ge4t_Reco_ttbar_toplep_m = vhi.variableHistoInterface(variable_name  = "Reco_ttbar_toplep_m",
                                            label          = "ljets_ge4j_ge4t_Reco_ttbar_toplep_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_ttbar_toplep_m.category_label = label
    interf_ljets_ge4j_ge4t_Reco_ttbar_toplep_m.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_ttbar_toplep_m","")
    interf_ljets_ge4j_ge4t_Reco_ttbar_toplep_m.bin_edges = [ 
				105.2,
				113.6,
				122.0,
				130.4,
				138.8,
				147.2,
				155.6,
				164.0,
				172.4,
				180.8,
				189.2,
				197.6,
				206.0,
				214.4,
				222.8,
				231.2,
				239.6,
				248.0,
				256.4,
				264.8,
				273.2,
				281.6,
				290.0,
				298.4,
				306.8,
				315.2,
				332.0,
				348.8,
				365.6,
				390.8,
				416.0,
				458.0,
				491.6,
				500.0
				]
    interf_ljets_ge4j_ge4t_Reco_ttbar_toplep_m.histotitle = "Reco_ttbar_toplep_m"
    interf_ljets_ge4j_ge4t_Reco_ttbar_toplep_m.histoname = "ljets_ge4j_ge4t_Reco_ttbar_toplep_m"
    interf_ljets_ge4j_ge4t_Reco_ttbar_toplep_m.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_ttbar_toplep_m)

    interf_ljets_ge4j_3t_Reco_tHq_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_tHq_bestJABDToutput",
                                            label          = "ljets_ge4j_3t_Reco_tHq_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_tHq_bestJABDToutput.category_label = label
    interf_ljets_ge4j_3t_Reco_tHq_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_tHq_bestJABDToutput","")
    interf_ljets_ge4j_3t_Reco_tHq_bestJABDToutput.bin_edges = [ 
				-0.558,
				-0.49,
				-0.456,
				-0.422,
				-0.388,
				-0.354,
				-0.32,
				-0.286,
				-0.252,
				-0.218,
				-0.184,
				-0.15,
				-0.116,
				-0.082,
				-0.048,
				-0.014,
				0.02,
				0.054,
				0.088,
				0.122,
				0.156,
				0.19,
				0.224,
				0.258,
				0.292,
				0.326,
				0.36,
				0.394,
				0.428,
				0.462,
				0.496,
				0.53,
				0.7
				]
    interf_ljets_ge4j_3t_Reco_tHq_bestJABDToutput.histotitle = "Reco_tHq_bestJABDToutput"
    interf_ljets_ge4j_3t_Reco_tHq_bestJABDToutput.histoname = "ljets_ge4j_3t_Reco_tHq_bestJABDToutput"
    interf_ljets_ge4j_3t_Reco_tHq_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_tHq_bestJABDToutput)

    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_abs_ljet_eta = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHq_abs_ljet_eta",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_tHq_abs_ljet_eta",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_abs_ljet_eta.category_label = label
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_abs_ljet_eta.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_tHq_abs_ljet_eta","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_abs_ljet_eta.bin_edges = [ 
				-0.5,
				-0.06,
				0.06,
				0.18,
				0.3,
				0.42,
				0.54,
				0.66,
				0.78,
				0.9,
				1.02,
				1.14,
				1.26,
				1.38,
				1.5,
				1.62,
				1.74,
				1.86,
				1.98,
				2.1,
				2.22,
				2.34,
				2.46,
				2.58,
				2.7,
				2.82,
				2.94,
				3.06,
				3.18,
				3.3,
				3.42,
				3.54,
				3.66,
				3.78,
				3.9,
				4.02,
				4.26,
				4.5
				]
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_abs_ljet_eta.histotitle = "Reco_JABDT_tHq_abs_ljet_eta"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_abs_ljet_eta.histoname = "ljets_ge4j_ge4t_Reco_JABDT_tHq_abs_ljet_eta"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_abs_ljet_eta.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_abs_ljet_eta)

    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1 = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHq_Jet_CSV_hdau1",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1.category_label = label
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1.bin_edges = [ 
				-0.5,
				0.0,
				0.1,
				0.3,
				0.35,
				0.4,
				0.45,
				0.5,
				0.55,
				0.6,
				0.65,
				0.7,
				0.75,
				0.8,
				0.85,
				0.9,
				0.95,
				1.0
				]
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1.histotitle = "Reco_JABDT_tHq_Jet_CSV_hdau1"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1.histoname = "ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1)

    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_Jet_CSV_btop",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.category_label = label
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.bin_edges = [ 
				-0.5,
				-0.1,
				0.35,
				0.4,
				0.45,
				0.5,
				0.55,
				0.6,
				0.65,
				0.7,
				0.75,
				0.8,
				0.85,
				0.9,
				0.95,
				1.0
				]
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.histotitle = "Reco_JABDT_tHW_Jet_CSV_btop"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.histoname = "ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop)

    plots = init_plots_vhi(interfaces = interfaces)    
    if data:
        add_data_plots(plots=plots,data=data)
    return plots

def plots_inputfeatures_ge4j_3t(data = None):
    label = "\geq 4 jets, 3 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM==3)&&(1.)"

    interf_ljets_ge4j_3t_Evt_Deta_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Deta_JetsAverage",
                                            label          = "ljets_ge4j_3t_Evt_Deta_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_Deta_JetsAverage.category_label = label
    interf_ljets_ge4j_3t_Evt_Deta_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_Deta_JetsAverage","")
    interf_ljets_ge4j_3t_Evt_Deta_JetsAverage.bin_edges = [ 
				0.06,
				0.12,
				0.18,
				0.24,
				0.3,
				0.36,
				0.42,
				0.48,
				0.54,
				0.6,
				0.66,
				0.72,
				0.78,
				0.84,
				0.9,
				0.96,
				1.02,
				1.08,
				1.14,
				1.2,
				1.26,
				1.32,
				1.38,
				1.44,
				1.5,
				1.56,
				1.62,
				1.68,
				1.74,
				1.8,
				1.86,
				1.92,
				1.98,
				2.04,
				2.1,
				2.16,
				2.22,
				2.28,
				2.34,
				2.4,
				2.46,
				2.52,
				2.64,
				3.0
				]
    interf_ljets_ge4j_3t_Evt_Deta_JetsAverage.histotitle = "Evt_Deta_JetsAverage"
    interf_ljets_ge4j_3t_Evt_Deta_JetsAverage.histoname = "ljets_ge4j_3t_Evt_Deta_JetsAverage"
    interf_ljets_ge4j_3t_Evt_Deta_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_Deta_JetsAverage)

    interf_ljets_ge4j_3t_Evt_M_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_M_TaggedJetsAverage",
                                            label          = "ljets_ge4j_3t_Evt_M_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_M_TaggedJetsAverage.category_label = label
    interf_ljets_ge4j_3t_Evt_M_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_M_TaggedJetsAverage","")
    interf_ljets_ge4j_3t_Evt_M_TaggedJetsAverage.bin_edges = [ 
				5.0,
				6.3,
				7.6,
				8.9,
				10.2,
				11.5,
				12.8,
				14.1,
				15.4,
				16.7,
				18.0,
				19.3,
				20.6,
				21.9,
				23.2,
				24.5,
				25.8,
				27.1,
				28.4,
				29.7,
				31.0,
				32.3,
				33.6,
				34.9,
				36.2,
				37.5,
				38.8,
				40.1,
				41.4,
				42.7,
				44.0,
				45.3,
				46.6,
				47.9,
				50.5,
				54.4,
				59.6,
				68.7,
				70.0
				]
    interf_ljets_ge4j_3t_Evt_M_TaggedJetsAverage.histotitle = "Evt_M_TaggedJetsAverage"
    interf_ljets_ge4j_3t_Evt_M_TaggedJetsAverage.histoname = "ljets_ge4j_3t_Evt_M_TaggedJetsAverage"
    interf_ljets_ge4j_3t_Evt_M_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_M_TaggedJetsAverage)

    interf_ljets_ge4j_3t_Evt_CSV_avg = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg",
                                            label          = "ljets_ge4j_3t_Evt_CSV_avg",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_CSV_avg.category_label = label
    interf_ljets_ge4j_3t_Evt_CSV_avg.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_CSV_avg","")
    interf_ljets_ge4j_3t_Evt_CSV_avg.bin_edges = [ 
				0.167,
				0.184,
				0.201,
				0.218,
				0.235,
				0.252,
				0.269,
				0.286,
				0.303,
				0.32,
				0.337,
				0.354,
				0.371,
				0.388,
				0.405,
				0.422,
				0.439,
				0.456,
				0.473,
				0.49,
				0.507,
				0.524,
				0.541,
				0.558,
				0.575,
				0.592,
				0.609,
				0.626,
				0.643,
				0.66,
				0.677,
				0.694,
				0.711,
				0.728,
				0.745,
				0.762,
				0.779,
				1.0
				]
    interf_ljets_ge4j_3t_Evt_CSV_avg.histotitle = "Evt_CSV_avg"
    interf_ljets_ge4j_3t_Evt_CSV_avg.histoname = "ljets_ge4j_3t_Evt_CSV_avg"
    interf_ljets_ge4j_3t_Evt_CSV_avg.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_CSV_avg)

    interf_ljets_ge4j_3t_Evt_blr_transformed = vhi.variableHistoInterface(variable_name  = "Evt_blr_transformed",
                                            label          = "ljets_ge4j_3t_Evt_blr_transformed",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_blr_transformed.category_label = label
    interf_ljets_ge4j_3t_Evt_blr_transformed.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_blr_transformed","")
    interf_ljets_ge4j_3t_Evt_blr_transformed.bin_edges = [ 
				-2.5,
				-2.15,
				-1.8,
				-1.45,
				-1.1,
				-0.75,
				-0.4,
				-0.05,
				0.3,
				0.65,
				1.0,
				1.35,
				1.7,
				2.05,
				2.4,
				2.75,
				3.1,
				3.45,
				3.8,
				4.15,
				4.5,
				4.85,
				5.2,
				5.55,
				5.9,
				6.25,
				6.6,
				6.95,
				7.3,
				7.65,
				8.35,
				15.0
				]
    interf_ljets_ge4j_3t_Evt_blr_transformed.histotitle = "Evt_blr_transformed"
    interf_ljets_ge4j_3t_Evt_blr_transformed.histoname = "ljets_ge4j_3t_Evt_blr_transformed"
    interf_ljets_ge4j_3t_Evt_blr_transformed.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_blr_transformed)

    interf_ljets_ge4j_3t_Reco_ttbar_toplep_m = vhi.variableHistoInterface(variable_name  = "Reco_ttbar_toplep_m",
                                            label          = "ljets_ge4j_3t_Reco_ttbar_toplep_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_ttbar_toplep_m.category_label = label
    interf_ljets_ge4j_3t_Reco_ttbar_toplep_m.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_ttbar_toplep_m","")
    interf_ljets_ge4j_3t_Reco_ttbar_toplep_m.bin_edges = [ 
				88.4,
				96.8,
				105.2,
				113.6,
				122.0,
				130.4,
				138.8,
				147.2,
				155.6,
				164.0,
				172.4,
				180.8,
				189.2,
				197.6,
				206.0,
				214.4,
				222.8,
				231.2,
				239.6,
				248.0,
				256.4,
				264.8,
				273.2,
				281.6,
				290.0,
				298.4,
				306.8,
				315.2,
				323.6,
				332.0,
				340.4,
				348.8,
				357.2,
				365.6,
				374.0,
				382.4,
				390.8,
				399.2,
				407.6,
				416.0,
				424.4,
				432.8,
				441.2,
				449.6,
				458.0,
				466.4,
				474.8,
				483.2,
				491.6,
				500.0
				]
    interf_ljets_ge4j_3t_Reco_ttbar_toplep_m.histotitle = "Reco_ttbar_toplep_m"
    interf_ljets_ge4j_3t_Reco_ttbar_toplep_m.histoname = "ljets_ge4j_3t_Reco_ttbar_toplep_m"
    interf_ljets_ge4j_3t_Reco_ttbar_toplep_m.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_ttbar_toplep_m)

    interf_ljets_ge4j_3t_Reco_ttbar_whad_m = vhi.variableHistoInterface(variable_name  = "Reco_ttbar_whad_m",
                                            label          = "ljets_ge4j_3t_Reco_ttbar_whad_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_ttbar_whad_m.category_label = label
    interf_ljets_ge4j_3t_Reco_ttbar_whad_m.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_ttbar_whad_m","")
    interf_ljets_ge4j_3t_Reco_ttbar_whad_m.bin_edges = [ 
				12.0,
				24.0,
				36.0,
				48.0,
				60.0,
				72.0,
				84.0,
				96.0,
				108.0,
				120.0,
				132.0,
				144.0,
				156.0,
				168.0,
				180.0,
				192.0,
				204.0,
				216.0,
				228.0,
				240.0,
				252.0,
				264.0,
				276.0,
				288.0,
				300.0,
				312.0,
				324.0,
				336.0,
				348.0,
				360.0,
				372.0,
				384.0,
				396.0,
				408.0,
				420.0,
				432.0,
				444.0,
				456.0,
				468.0,
				480.0,
				492.0,
				504.0,
				516.0,
				528.0,
				540.0,
				552.0,
				564.0,
				576.0,
				588.0,
				600.0
				]
    interf_ljets_ge4j_3t_Reco_ttbar_whad_m.histotitle = "Reco_ttbar_whad_m"
    interf_ljets_ge4j_3t_Reco_ttbar_whad_m.histoname = "ljets_ge4j_3t_Reco_ttbar_whad_m"
    interf_ljets_ge4j_3t_Reco_ttbar_whad_m.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_ttbar_whad_m)

    interf_ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_btoplep = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttH_Jet_CSV_btoplep",
                                            label          = "ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_btoplep",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_ttbar_whad_m.category_label = label
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_btoplep.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_btoplep","")
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_btoplep.bin_edges = [ 
				-0.5,
				0.0,
				0.05,
				0.1,
				0.15,
				0.2,
				0.25,
				0.3,
				0.35,
				0.4,
				0.45,
				0.5,
				0.55,
				0.6,
				0.65,
				0.7,
				0.75,
				0.8,
				0.85,
				0.9,
				0.95,
				1.0
				]
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_btoplep.histotitle = "Reco_JABDT_ttH_Jet_CSV_btoplep"
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_btoplep.histoname = "ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_btoplep"
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_btoplep.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_btoplep)

    interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_wb_m = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_log_wb_m",
                                            label          = "ljets_ge4j_3t_Reco_JABDT_tHW_log_wb_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_wb_m.category_label = label
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_wb_m.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_JABDT_tHW_log_wb_m","")
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_wb_m.bin_edges = [ 
				2,
				2.7,
				3.1,
				3.3,
				3.5,
				3.7,
				3.9,
				4.1,
				4.3,
				4.5,
				4.7,
				4.9,
				5.1,
				5.3,
				5.5,
				5.7,
				5.9,
				6.1,
				6.3,
				6.5,
				6.7,
				6.9,
				7.1,
				7.3,
				7.5,
				7.7,
				7.9,
				8.5
				]
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_wb_m.histotitle = "Reco_JABDT_tHW_log_wb_m"
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_wb_m.histoname = "ljets_ge4j_3t_Reco_JABDT_tHW_log_wb_m"
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_wb_m.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_wb_m)

    plots = init_plots_vhi(interfaces = interfaces)    
    if data:
        add_data_plots(plots=plots,data=data)
    return plots

def plots_inputfeatures_STXS_ge4j_ge4t(data = None):
    label = "\geq 4 jets, \geq 4 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"
    interf_ljets_ge4j_ge4t_Reco_tHq_h_pt = vhi.variableHistoInterface(variable_name  = "Reco_tHq_h_pt",
                                            label          = "ljets_ge4j_ge4t_Reco_tHq_h_pt",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_tHq_h_pt.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_tHq_h_pt","")
    interf_ljets_ge4j_ge4t_Reco_tHq_h_pt.category_label = label
    interf_ljets_ge4j_ge4t_Reco_tHq_h_pt.bin_edges = [ 
                0.0,
                12.0,
                24.0,
                36.0,
                48.0,
                60.0,
                72.0,
                84.0,
                96.0,
                108.0,
                120.0,
                132.0,
                144.0,
                156.0,
                168.0,
                180.0,
                192.0,
                204.0,
                216.0,
                228.0,
                240.0,
                252.0,
                264.0,
                276.0,
                288.0,
                300.0,
                312.0,
                324.0,
                336.0,
                348.0,
                360.0,
                372.0,
                384.0,
                396.0,
                408.0,
                420.0,
                444.0,
                456.0,
                480.0,
                504.0,
                540.0,
                588.0,
                600.0
                ]
    interf_ljets_ge4j_ge4t_Reco_tHq_h_pt.histotitle = "Reco_tHq_h_pt"
    interf_ljets_ge4j_ge4t_Reco_tHq_h_pt.histoname = "ljets_ge4j_ge4t_Reco_tHq_h_pt"
    interf_ljets_ge4j_ge4t_Reco_tHq_h_pt.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_tHq_h_pt)

    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_log_h_pt = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHq_log_h_pt",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_tHq_log_h_pt",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_log_h_pt.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_tHq_log_h_pt","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_log_h_pt.category_label = label
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_log_h_pt.bin_edges = [ 
                0.0,
                0.01,
                2.1,
                2.38,
                2.52,
                2.66,
                2.8,
                2.94,
                3.08,
                3.22,
                3.36,
                3.5,
                3.64,
                3.78,
                3.92,
                4.06,
                4.2,
                4.34,
                4.48,
                4.62,
                4.76,
                4.9,
                5.04,
                5.18,
                5.32,
                5.46,
                5.6,
                5.74,
                5.88,
                6.02,
                6.16,
                6.3,
                6.44,
                7.0
                ]
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_log_h_pt.histotitle = "Reco_JABDT_tHq_log_h_pt"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_log_h_pt.histoname = "ljets_ge4j_ge4t_Reco_JABDT_tHq_log_h_pt"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_log_h_pt.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_log_h_pt)

    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt.category_label = label
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt.bin_edges = [ 
                -1.5,
                3.3,
                3.45,
                3.6,
                3.75,
                3.9,
                4.05,
                4.2,
                4.35,
                4.5,
                4.65,
                4.8,
                4.95,
                5.1,
                6.0
                ]
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt.histotitle = "Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt.histoname = "ljets_ge4j_ge4t_Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt)

    interf_ljets_ge4j_ge4t_Reco_tHW_h_pt = vhi.variableHistoInterface(variable_name  = "Reco_tHW_h_pt",
                                            label          = "ljets_ge4j_ge4t_Reco_tHW_h_pt",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_tHW_h_pt.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_tHW_h_pt","")
    interf_ljets_ge4j_ge4t_Reco_tHW_h_pt.category_label = label
    interf_ljets_ge4j_ge4t_Reco_tHW_h_pt.bin_edges = [ 
                -1.5,
                10.53,
                22.56,
                34.59,
                46.62,
                58.65,
                70.68,
                82.71,
                94.74,
                106.77,
                118.8,
                130.83,
                142.86,
                154.89,
                166.92,
                178.95,
                190.98,
                203.01,
                215.04,
                227.07,
                239.1,
                251.13,
                263.16,
                275.19,
                287.22,
                299.25,
                311.28,
                323.31,
                335.34,
                347.37,
                371.43,
                407.52,
                443.61,
                503.76,
                575.94,
                600.0
                ]
    interf_ljets_ge4j_ge4t_Reco_tHW_h_pt.histotitle = "Reco_tHW_h_pt"
    interf_ljets_ge4j_ge4t_Reco_tHW_h_pt.histoname = "ljets_ge4j_ge4t_Reco_tHW_h_pt"
    interf_ljets_ge4j_ge4t_Reco_tHW_h_pt.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_tHW_h_pt)

    interf_ljets_ge4j_ge4t_Reco_tHW_h_dr = vhi.variableHistoInterface(variable_name  = "Reco_tHW_h_dr",
                                            label          = "ljets_ge4j_ge4t_Reco_tHW_h_dr",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_tHW_h_dr.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_tHW_h_dr","")
    interf_ljets_ge4j_ge4t_Reco_tHW_h_dr.category_label = label
    interf_ljets_ge4j_ge4t_Reco_tHW_h_dr.bin_edges = [ 
                -1.5,
                0.37,
                0.48,
                0.59,
                0.7,
                0.81,
                0.92,
                1.03,
                1.14,
                1.25,
                1.36,
                1.47,
                1.58,
                1.69,
                1.8,
                1.91,
                2.02,
                2.13,
                2.24,
                2.35,
                2.46,
                2.57,
                2.68,
                2.79,
                2.9,
                3.01,
                3.12,
                3.34,
                4.0
                ]
    interf_ljets_ge4j_ge4t_Reco_tHW_h_dr.histotitle = "Reco_tHW_h_dr"
    interf_ljets_ge4j_ge4t_Reco_tHW_h_dr.histoname = "ljets_ge4j_ge4t_Reco_tHW_h_dr"
    interf_ljets_ge4j_ge4t_Reco_tHW_h_dr.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_tHW_h_dr)

    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_log_h_pt = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_log_h_pt",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_tHW_log_h_pt",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_log_h_pt.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_tHW_log_h_pt","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_log_h_pt.category_label = label
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_log_h_pt.bin_edges = [ 
                0.0,
                0.01,
                1.82,
                2.1,
                2.38,
                2.52,
                2.66,
                2.8,
                2.94,
                3.08,
                3.22,
                3.36,
                3.5,
                3.64,
                3.78,
                3.92,
                4.06,
                4.2,
                4.34,
                4.48,
                4.62,
                4.76,
                4.9,
                5.04,
                5.18,
                5.32,
                5.46,
                5.6,
                5.74,
                5.88,
                6.02,
                6.16,
                6.3,
                6.44,
                6.58,
                7.0
                ]
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_log_h_pt.histotitle = "Reco_JABDT_tHW_log_h_pt"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_log_h_pt.histoname = "ljets_ge4j_ge4t_Reco_JABDT_tHW_log_h_pt"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_log_h_pt.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_log_h_pt)

    interf_ljets_ge4j_ge4t_Reco_ttH_h_dr = vhi.variableHistoInterface(variable_name  = "Reco_ttH_h_dr",
                                            label          = "ljets_ge4j_ge4t_Reco_ttH_h_dr",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_ttH_h_dr.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_ttH_h_dr","")
    interf_ljets_ge4j_ge4t_Reco_ttH_h_dr.category_label = label
    interf_ljets_ge4j_ge4t_Reco_ttH_h_dr.bin_edges = [ 
                -1.5,
                0.0,
                0.48,
                0.59,
                0.7,
                0.81,
                0.92,
                1.03,
                1.14,
                1.25,
                1.36,
                1.47,
                1.58,
                1.69,
                1.8,
                1.91,
                2.02,
                2.13,
                2.24,
                2.35,
                2.46,
                2.57,
                2.68,
                2.79,
                2.9,
                3.01,
                3.12,
                3.23,
                3.34,
                3.45,
                3.78,
                4.0
                ]
    interf_ljets_ge4j_ge4t_Reco_ttH_h_dr.histotitle = "Reco_ttH_h_dr"
    interf_ljets_ge4j_ge4t_Reco_ttH_h_dr.histoname = "ljets_ge4j_ge4t_Reco_ttH_h_dr"
    interf_ljets_ge4j_ge4t_Reco_ttH_h_dr.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_ttH_h_dr)

    interf_ljets_ge4j_ge4t_Reco_ttH_h_m = vhi.variableHistoInterface(variable_name  = "Reco_ttH_h_m",
                                            label          = "ljets_ge4j_ge4t_Reco_ttH_h_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_ttH_h_m.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_ttH_h_m","")
    interf_ljets_ge4j_ge4t_Reco_ttH_h_m.category_label = label
    interf_ljets_ge4j_ge4t_Reco_ttH_h_m.bin_edges = [ 
                80.0,
                82.0,
                84.0,
                86.0,
                88.0,
                90.0,
                92.0,
                94.0,
                96.0,
                98.0,
                100.0,
                102.0,
                104.0,
                106.0,
                108.0,
                110.0,
                112.0,
                114.0,
                116.0,
                118.0,
                120.0,
                122.0,
                124.0,
                126.0,
                128.0,
                130.0,
                132.0,
                134.0,
                136.0,
                138.0,
                140.0,
                142.0,
                144.0,
                146.0,
                148.0,
                150.0,
                152.0,
                154.0,
                156.0,
                158.0,
                160.0,
                164.0,
                168.0,
                174.0,
                178.0,
                180.0
                ]
    interf_ljets_ge4j_ge4t_Reco_ttH_h_m.histotitle = "Reco_ttH_h_m"
    interf_ljets_ge4j_ge4t_Reco_ttH_h_m.histoname = "ljets_ge4j_ge4t_Reco_ttH_h_m"
    interf_ljets_ge4j_ge4t_Reco_ttH_h_m.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_ttH_h_m)

    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_h_pt = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttH_log_h_pt",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_ttH_log_h_pt",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_h_pt.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_ttH_log_h_pt","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_h_pt.category_label = label
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_h_pt.bin_edges = [ 
				0.0,
				1.2,
				1.8,
				2.2,
				2.4,
				2.6,
				2.8,
				3.0,
				3.2,
				3.4,
				3.6,
				3.8,
				4.0,
				4.2,
				4.4,
				4.6,
				4.8,
				5.0,
				5.2,
				5.4,
				5.6,
				5.8,
				6.0,
				6.2,
				6.4,
				]
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_h_pt.histotitle = "Reco_JABDT_ttH_log_h_pt"
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_h_pt.histoname = "ljets_ge4j_ge4t_Reco_JABDT_ttH_log_h_pt"
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_h_pt)

    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_m = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttH_log_toplep_m",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_m.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_m","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_m.category_label = label
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_m.bin_edges = [ 
                -1.5,
                4.2,
                4.8,
                4.98,
                5.16,
                5.34,
                5.52,
                5.7,
                5.88,
                6.06,
                6.24,
                6.42,
                6.6,
                6.78,
                7.5
                ]
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_m.histotitle = "Reco_JABDT_ttH_log_toplep_m"
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_m.histoname = "ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_m"
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_m.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_m)

    interf_ljets_ge4j_ge4t_Evt_Pt_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Pt_TaggedJetsAverage",
                                            label          = "ljets_ge4j_ge4t_Evt_Pt_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_Pt_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_Pt_TaggedJetsAverage","")
    interf_ljets_ge4j_ge4t_Evt_Pt_TaggedJetsAverage.category_label = label
    interf_ljets_ge4j_ge4t_Evt_Pt_TaggedJetsAverage.bin_edges = [ 
                30.0,
                41.4,
                52.8,
                64.2,
                75.6,
                87.0,
                98.4,
                109.8,
                121.2,
                132.6,
                144.0,
                155.4,
                166.8,
                178.2,
                189.6,
                201.0,
                212.4,
                235.2,
                269.4,
                600.0
                ]
    interf_ljets_ge4j_ge4t_Evt_Pt_TaggedJetsAverage.histotitle = "Evt_Pt_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_Evt_Pt_TaggedJetsAverage.histoname = "ljets_ge4j_ge4t_Evt_Pt_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_Evt_Pt_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_Pt_TaggedJetsAverage)

    interf_ljets_ge4j_ge4t_Evt_Dr_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Dr_TaggedJetsAverage",
                                            label          = "ljets_ge4j_ge4t_Evt_Dr_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_Dr_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_Dr_TaggedJetsAverage","")
    interf_ljets_ge4j_ge4t_Evt_Dr_TaggedJetsAverage.category_label = label
    interf_ljets_ge4j_ge4t_Evt_Dr_TaggedJetsAverage.bin_edges = [ 
                1.16,
                1.34,
                1.46,
                1.52,
                1.58,
                1.64,
                1.7,
                1.76,
                1.82,
                1.88,
                1.94,
                2.0,
                2.06,
                2.12,
                2.18,
                2.24,
                2.3,
                2.36,
                2.42,
                2.48,
                2.54,
                2.6,
                2.66,
                2.72,
                2.78,
                2.84,
                2.9,
                2.96,
                3.02,
                3.08,
                3.2,
                3.5
                ]
    interf_ljets_ge4j_ge4t_Evt_Dr_TaggedJetsAverage.histotitle = "average #DeltaR(tags)"
    interf_ljets_ge4j_ge4t_Evt_Dr_TaggedJetsAverage.histoname = "ljets_ge4j_ge4t_Evt_Dr_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_Evt_Dr_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_Dr_TaggedJetsAverage)

    interf_ljets_ge4j_ge4t_Evt_M_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_M_TaggedJetsAverage",
                                            label          = "ljets_ge4j_ge4t_Evt_M_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_M_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_M_TaggedJetsAverage","")
    interf_ljets_ge4j_ge4t_Evt_M_TaggedJetsAverage.category_label = label
    interf_ljets_ge4j_ge4t_Evt_M_TaggedJetsAverage.bin_edges = [ 
                6.3,
                7.6,
                8.9,
                10.2,
                11.5,
                12.8,
                14.1,
                15.4,
                16.7,
                18.0,
                19.3,
                20.6,
                21.9,
                23.2,
                24.5,
                25.8,
                27.1,
                28.4,
                29.7,
                31.0,
                33.6,
                37.5,
                42.7,
                70.0
                ]
    interf_ljets_ge4j_ge4t_Evt_M_TaggedJetsAverage.histotitle = "Evt_M_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_Evt_M_TaggedJetsAverage.histoname = "ljets_ge4j_ge4t_Evt_M_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_Evt_M_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_M_TaggedJetsAverage)

    # ge4j_ge4t_Evt_Pt_minDrTaggedJets -> already in classifier vars
    # ge4j_ge4t_Evt_Pt_JetsAverage -> already in classifier vars

    plots = init_plots_vhi(interfaces = interfaces)    
    if data:
        add_data_plots(plots=plots,data=data)
    return plots

def plots_inputfeatures_STXS_ge4j_3t(data = None):
    label = "\geq 4 jets, 3 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM==3)&&(1.)"

    interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_h_m = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_log_h_m",
                                            label          = "ljets_ge4j_3t_Reco_JABDT_tHW_log_h_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_h_m.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_JABDT_tHW_log_h_m","")
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_h_m.category_label = label
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_h_m.bin_edges = [ 
                2.0,
                2.5,
                3.17,
                3.26,
                3.35,
                3.44,
                3.53,
                3.62,
                3.71,
                3.8,
                3.89,
                3.98,
                4.07,
                4.16,
                4.25,
                4.34,
                4.43,
                4.52,
                4.61,
                4.7,
                4.79,
                4.88,
                4.97,
                5.06,
                5.15,
                5.24,
                5.33,
                5.42,
                5.51,
                5.6,
                5.69,
                5.78,
                5.87,
                5.96,
                6.05,
                6.14,
                6.23,
                6.32,
                6.41,
                6.5
                ]
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_h_m.histotitle = "Reco_JABDT_tHW_log_h_m"
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_h_m.histoname = "ljets_ge4j_3t_Reco_JABDT_tHW_log_h_m"
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_h_m.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_h_m)

    interf_ljets_ge4j_3t_Reco_tHq_h_pt = vhi.variableHistoInterface(variable_name  = "Reco_tHq_h_pt",
                                            label          = "ljets_ge4j_3t_Reco_tHq_h_pt",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_tHq_h_pt.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_tHq_h_pt","")
    interf_ljets_ge4j_3t_Reco_tHq_h_pt.category_label = label
    interf_ljets_ge4j_3t_Reco_tHq_h_pt.bin_edges = [ 
                0.0,
                12.0,
                24.0,
                36.0,
                48.0,
                60.0,
                72.0,
                84.0,
                96.0,
                108.0,
                120.0,
                132.0,
                144.0,
                156.0,
                168.0,
                180.0,
                192.0,
                204.0,
                216.0,
                228.0,
                240.0,
                252.0,
                264.0,
                276.0,
                288.0,
                300.0,
                312.0,
                324.0,
                336.0,
                348.0,
                360.0,
                372.0,
                384.0,
                396.0,
                408.0,
                420.0,
                432.0,
                444.0,
                468.0,
                480.0,
                492.0,
                504.0,
                528.0,
                552.0,
                588.0,
                600.0
                ]
    interf_ljets_ge4j_3t_Reco_tHq_h_pt.histotitle = "Reco_tHq_h_pt"
    interf_ljets_ge4j_3t_Reco_tHq_h_pt.histoname = "ljets_ge4j_3t_Reco_tHq_h_pt"
    interf_ljets_ge4j_3t_Reco_tHq_h_pt.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_tHq_h_pt)

    interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_h_m = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHq_log_h_m",
                                            label          = "ljets_ge4j_3t_Reco_JABDT_tHq_log_h_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_h_m.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_JABDT_tHq_log_h_m","")
    interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_h_m.category_label = label
    interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_h_m.bin_edges = [ 
				3.252,
				3.336,
				3.42,
				3.504,
				3.588,
				3.672,
				3.756,
				3.84,
				3.924,
				4.008,
				4.092,
				4.176,
				4.26,
				4.344,
				4.428,
				4.512,
				4.596,
				4.68,
				4.764,
				4.848,
				4.932,
				5.016,
				5.1,
				5.184,
				5.268,
				5.352,
				5.436,
				5.52,
				5.604,
				5.688,
				5.772,
				5.856,
				5.94,
				6.024,
				6.108,
				6.192,
				6.276,
				6.36,
				6.444,
				6.528,
				6.612,
				6.696,
				6.78,
				6.948,
				7.116,
				7.2
				]
    interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_h_m.histotitle = "Reco_JABDT_tHq_log_h_m"
    interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_h_m.histoname = "ljets_ge4j_3t_Reco_JABDT_tHq_log_h_m"
    interfaces.append(interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_h_m)

    interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_h_pt = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHq_log_h_pt",
                                            label          = "ljets_ge4j_3t_Reco_JABDT_tHq_log_h_pt",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_h_pt.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_JABDT_tHq_log_h_pt","")
    interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_h_pt.category_label = label
    interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_h_pt.bin_edges = [ 
                0.7,
                1.4,
                1.68,
                1.96,
                2.1,
                2.24,
                2.38,
                2.52,
                2.66,
                2.8,
                2.94,
                3.08,
                3.22,
                3.36,
                3.5,
                3.64,
                3.78,
                3.92,
                4.06,
                4.2,
                4.34,
                4.48,
                4.62,
                4.76,
                4.9,
                5.04,
                5.18,
                5.32,
                5.46,
                5.6,
                5.74,
                5.88,
                6.02,
                6.16,
                6.3,
                7.0
                ]
    interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_h_pt.histotitle = "Reco_JABDT_tHq_log_h_pt"
    interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_h_pt.histoname = "ljets_ge4j_3t_Reco_JABDT_tHq_log_h_pt"
    interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_h_pt.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_h_pt)

    interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt",
                                            label          = "ljets_ge4j_3t_Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt","")
    interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt.category_label = label
    interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt.bin_edges = [ 
                3.36,
                3.42,
                3.48,
                3.54,
                3.6,
                3.66,
                3.72,
                3.78,
                3.84,
                3.9,
                3.96,
                4.02,
                4.08,
                4.14,
                4.2,
                4.26,
                4.32,
                4.38,
                4.44,
                4.5,
                4.56,
                4.62,
                4.68,
                4.74,
                4.8,
                4.86,
                4.92,
                4.98,
                5.04,
                5.1,
                5.16,
                5.22,
                5.28,
                5.34,
                5.4,
                5.46,
                5.52,
                5.58,
                5.7,
                5.94,
                6.0
                ]
    interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt.histotitle = "Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt"
    interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt.histoname = "ljets_ge4j_3t_Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt"
    interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt)

    interf_ljets_ge4j_3t_Reco_tHW_h_pt = vhi.variableHistoInterface(variable_name  = "Reco_tHW_h_pt",
                                            label          = "ljets_ge4j_3t_Reco_tHW_h_pt",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_tHW_h_pt.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_tHW_h_pt","")
    interf_ljets_ge4j_3t_Reco_tHW_h_pt.category_label = label
    interf_ljets_ge4j_3t_Reco_tHW_h_pt.bin_edges = [ 
                -1.5,
                0.0,
                22.56,
                34.59,
                46.62,
                58.65,
                70.68,
                82.71,
                94.74,
                106.77,
                118.8,
                130.83,
                142.86,
                154.89,
                166.92,
                178.95,
                190.98,
                203.01,
                215.04,
                227.07,
                239.1,
                251.13,
                263.16,
                275.19,
                287.22,
                299.25,
                311.28,
                323.31,
                335.34,
                347.37,
                359.4,
                371.43,
                383.46,
                395.49,
                407.52,
                419.55,
                431.58,
                443.61,
                455.64,
                467.67,
                479.7,
                503.76,
                539.85,
                587.97,
                600.0
                ]
    interf_ljets_ge4j_3t_Reco_tHW_h_pt.histotitle = "Reco_tHW_h_pt"
    interf_ljets_ge4j_3t_Reco_tHW_h_pt.histoname = "ljets_ge4j_3t_Reco_tHW_h_pt"
    interf_ljets_ge4j_3t_Reco_tHW_h_pt.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_tHW_h_pt)

    interf_ljets_ge4j_3t_Reco_tHW_h_dr = vhi.variableHistoInterface(variable_name  = "Reco_tHW_h_dr",
                                            label          = "ljets_ge4j_3t_Reco_tHW_h_dr",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_tHW_h_dr.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_tHW_h_dr","")
    interf_ljets_ge4j_3t_Reco_tHW_h_dr.category_label = label
    interf_ljets_ge4j_3t_Reco_tHW_h_dr.bin_edges = [ 
                -1.5,
                0.37,
                0.48,
                0.59,
                0.7,
                0.81,
                0.92,
                1.03,
                1.14,
                1.25,
                1.36,
                1.47,
                1.58,
                1.69,
                1.8,
                1.91,
                2.02,
                2.13,
                2.24,
                2.35,
                2.46,
                2.57,
                2.68,
                2.79,
                2.9,
                3.01,
                3.12,
                3.23,
                3.34,
                3.45,
                3.56,
                3.67,
                3.78,
                3.89,
                4.0
                ]
    interf_ljets_ge4j_3t_Reco_tHW_h_dr.histotitle = "Reco_tHW_h_dr"
    interf_ljets_ge4j_3t_Reco_tHW_h_dr.histoname = "ljets_ge4j_3t_Reco_tHW_h_dr"
    interf_ljets_ge4j_3t_Reco_tHW_h_dr.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_tHW_h_dr)

    interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_h_pt = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_log_h_pt",
                                            label          = "ljets_ge4j_3t_Reco_JABDT_tHW_log_h_pt",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_h_pt.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_JABDT_tHW_log_h_pt","")
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_h_pt.category_label = label
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_h_pt.bin_edges = [ 
                0.0,
                0.42,
                0.7,
                0.98,
                1.12,
                1.26,
                1.4,
                1.54,
                1.68,
                1.82,
                1.96,
                2.1,
                2.24,
                2.38,
                2.52,
                2.66,
                2.8,
                2.94,
                3.08,
                3.22,
                3.36,
                3.5,
                3.64,
                3.78,
                3.92,
                4.06,
                4.2,
                4.34,
                4.48,
                4.62,
                4.76,
                4.9,
                5.04,
                5.18,
                5.32,
                5.46,
                5.6,
                5.74,
                5.88,
                6.02,
                6.16,
                6.3,
                6.44,
                6.58,
                6.72,
                6.86,
                7.0
                ]
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_h_pt.histotitle = "Reco_JABDT_tHW_log_h_pt"
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_h_pt.histoname = "ljets_ge4j_3t_Reco_JABDT_tHW_log_h_pt"
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_h_pt.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_h_pt)

    interf_ljets_ge4j_3t_Reco_ttH_h_dr = vhi.variableHistoInterface(variable_name  = "Reco_ttH_h_dr",
                                            label          = "ljets_ge4j_3t_Reco_ttH_h_dr",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_ttH_h_dr.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_ttH_h_dr","")
    interf_ljets_ge4j_3t_Reco_ttH_h_dr.category_label = label
    interf_ljets_ge4j_3t_Reco_ttH_h_dr.bin_edges = [ 
                -1.5,
                0.37,
                0.48,
                0.59,
                0.7,
                0.81,
                0.92,
                1.03,
                1.14,
                1.25,
                1.36,
                1.47,
                1.58,
                1.69,
                1.8,
                1.91,
                2.02,
                2.13,
                2.24,
                2.35,
                2.46,
                2.57,
                2.68,
                2.79,
                2.9,
                3.01,
                3.12,
                3.23,
                3.34,
                3.45,
                3.56,
                3.67,
                3.78,
                3.89,
                4.0
                ]
    interf_ljets_ge4j_3t_Reco_ttH_h_dr.histotitle = "Reco_ttH_h_dr"
    interf_ljets_ge4j_3t_Reco_ttH_h_dr.histoname = "ljets_ge4j_3t_Reco_ttH_h_dr"
    interf_ljets_ge4j_3t_Reco_ttH_h_dr.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_ttH_h_dr)

    interf_ljets_ge4j_3t_Evt_Pt_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Pt_JetsAverage",
                                            label          = "ljets_ge4j_3t_Evt_Pt_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_Pt_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_Pt_JetsAverage","")
    interf_ljets_ge4j_3t_Evt_Pt_JetsAverage.category_label = label
    interf_ljets_ge4j_3t_Evt_Pt_JetsAverage.bin_edges = [ 
                30.0,
                39.4,
                48.8,
                58.2,
                67.6,
                77.0,
                86.4,
                95.8,
                105.2,
                114.6,
                124.0,
                133.4,
                142.8,
                152.2,
                161.6,
                171.0,
                180.4,
                189.8,
                199.2,
                208.6,
                218.0,
                227.4,
                236.8,
                246.2,
                255.6,
                265.0,
                274.4,
                283.8,
                293.2,
                302.6,
                312.0,
                321.4,
                340.2,
                368.4,
                406.0,
                443.6,
                500.0
                ]
    interf_ljets_ge4j_3t_Evt_Pt_JetsAverage.histotitle = "Evt_Pt_JetsAverage"
    interf_ljets_ge4j_3t_Evt_Pt_JetsAverage.histoname = "ljets_ge4j_3t_Evt_Pt_JetsAverage"
    interf_ljets_ge4j_3t_Evt_Pt_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_Pt_JetsAverage)

    interf_ljets_ge4j_3t_Evt_Pt_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Pt_TaggedJetsAverage",
                                            label          = "ljets_ge4j_3t_Evt_Pt_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_Pt_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_Pt_TaggedJetsAverage","")
    interf_ljets_ge4j_3t_Evt_Pt_TaggedJetsAverage.category_label = label
    interf_ljets_ge4j_3t_Evt_Pt_TaggedJetsAverage.bin_edges = [ 
                30.0,
                41.4,
                52.8,
                64.2,
                75.6,
                87.0,
                98.4,
                109.8,
                121.2,
                132.6,
                144.0,
                155.4,
                166.8,
                178.2,
                189.6,
                201.0,
                212.4,
                223.8,
                235.2,
                246.6,
                269.4,
                280.8,
                292.2,
                315.0,
                337.8,
                360.6,
                600.0
                ]
    interf_ljets_ge4j_3t_Evt_Pt_TaggedJetsAverage.histotitle = "Evt_Pt_TaggedJetsAverage"
    interf_ljets_ge4j_3t_Evt_Pt_TaggedJetsAverage.histoname = "ljets_ge4j_3t_Evt_Pt_TaggedJetsAverage"
    interf_ljets_ge4j_3t_Evt_Pt_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_Pt_TaggedJetsAverage)

    interf_ljets_ge4j_3t_Evt_Dr_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Dr_TaggedJetsAverage",
                                            label          = "ljets_ge4j_3t_Evt_Dr_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_Dr_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_Dr_TaggedJetsAverage","")
    interf_ljets_ge4j_3t_Evt_Dr_TaggedJetsAverage.category_label = label
    interf_ljets_ge4j_3t_Evt_Dr_TaggedJetsAverage.bin_edges = [ 
                0.74,
                0.86,
                0.98,
                1.04,
                1.1,
                1.16,
                1.22,
                1.28,
                1.34,
                1.4,
                1.46,
                1.52,
                1.58,
                1.64,
                1.7,
                1.76,
                1.82,
                1.88,
                1.94,
                2.0,
                2.06,
                2.12,
                2.18,
                2.24,
                2.3,
                2.36,
                2.42,
                2.48,
                2.54,
                2.6,
                2.66,
                2.72,
                2.78,
                2.84,
                2.9,
                2.96,
                3.02,
                3.08,
                3.14,
                3.2,
                3.26,
                3.32,
                3.38,
                3.44,
                3.5
                ]
    interf_ljets_ge4j_3t_Evt_Dr_TaggedJetsAverage.histotitle = "average #DeltaR(tags)"
    interf_ljets_ge4j_3t_Evt_Dr_TaggedJetsAverage.histoname = "ljets_ge4j_3t_Evt_Dr_TaggedJetsAverage"
    interf_ljets_ge4j_3t_Evt_Dr_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_Dr_TaggedJetsAverage)

    interf_ljets_ge4j_3t_TaggedJet_Pt_0 = vhi.variableHistoInterface(variable_name  = "TaggedJet_Pt[0]",
                                            label          = "ljets_ge4j_3t_TaggedJet_Pt_0",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_TaggedJet_Pt_0.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_TaggedJet_Pt_0","")
    interf_ljets_ge4j_3t_TaggedJet_Pt_0.category_label = label
    interf_ljets_ge4j_3t_TaggedJet_Pt_0.bin_edges = [ 
                30.0,
                41.4,
                52.8,
                64.2,
                75.6,
                87.0,
                98.4,
                109.8,
                121.2,
                132.6,
                144.0,
                155.4,
                166.8,
                178.2,
                189.6,
                201.0,
                212.4,
                223.8,
                235.2,
                246.6,
                258.0,
                269.4,
                280.8,
                292.2,
                303.6,
                315.0,
                326.4,
                337.8,
                349.2,
                360.6,
                372.0,
                383.4,
                394.8,
                406.2,
                417.6,
                429.0,
                451.8,
                474.6,
                486.0,
                520.2,
                554.4,
                588.6,
                600.0
                ]
    interf_ljets_ge4j_3t_TaggedJet_Pt_0.histotitle = "TaggedJet_Pt[0]"
    interf_ljets_ge4j_3t_TaggedJet_Pt_0.histoname = "ljets_ge4j_3t_TaggedJet_Pt_0"
    interf_ljets_ge4j_3t_TaggedJet_Pt_0.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_TaggedJet_Pt_0)


    plots = init_plots_vhi(interfaces = interfaces)    
    if data:
        add_data_plots(plots=plots,data=data)
    return plots


#baseline
def plots_ge4j_ge3t(data=None):
    label = "\geq 4 jets, \geq 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=3)"

    tag = "ge4j_ge3t"
    plots = plots_control(tag, selection, label)   
    plots += plots_crossCheck(tag, selection, label)   
     
    if data:
        add_data_plots(plots=plots,data=data)

    return plots

#analysis categories w/o forward stuff
def plots_ge4j_3t(data=None):
    label = "\geq 4 jets, 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM==3)"

    tag = "ge4j_3t"
    plots = plots_control(tag, selection, label)    

    if data:
        add_data_plots(plots=plots,data=data)

    return plots

def plots_ge4j_ge4t(data=None):
    label = "\geq 4 jets, \geq 4 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=4)"

    tag = "ge4j_ge4t"
    plots = plots_control(tag, selection, label)    
    plots += plots_crossCheck(tag, selection, label)   

    if data:
        add_data_plots(plots=plots,data=data)

    return plots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    #baseline
    discriminatorPlots += plots_ge4j_ge3t(data)
    # discriminatorPlots += plots_ge4j_3t(data)
    discriminatorPlots += plots_ge4j_ge4t(data)
    # input features
    discriminatorPlots += plots_inputfeatures_ge4j_3t(data)
    discriminatorPlots += plots_inputfeatures_ge4j_ge4t(data)
    
    # input features STXS
    discriminatorPlots += plots_inputfeatures_STXS_ge4j_3t(data)
    discriminatorPlots += plots_inputfeatures_STXS_ge4j_ge4t(data)

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

def init_plots_vhi(interfaces, data = None):
    plots = [] #init list of plotClasses objects to return
    dictionary = {}
    for interf in interfaces:

        # check if initialization uses bin edges or min/max vals
        # if 'subdict' contains the keyword 'bin_edges', an array
        # of type float is created from the corresponding python list.
        # Else, the min/maxvals are used 
        if not interf.bin_edges is None:
            bins  = array("f", interf.bin_edges)
            nbins = len(bins)-1 # last bin edge in array is overflow bin => subtract for nbins
            interf.nhistobins = nbins # update number of bins
            plots.append(
                plotClasses.Plot(
                    ROOT.TH1F(interf.histoname,interf.histotitle,nbins,bins),
                    interf.varname,interf.selection,interf.category_label))

        elif not (interf.minxval is None or interf.maxxval is None):
            nbins = interf.nhistobins
            xmax  = interf.maxxval
            xmin  = interf.minxval
            plots.append(
                plotClasses.Plot(
                    ROOT.TH1F(interf.histoname,interf.histotitle,nbins,xmin, xmax),
                    interf.varname,interf.selection,interf.category_label))
        else:
            print("FATAL ERROR: Unable to load bin edges or min/max values for histogram!")
            print(interf)
            raise ValueError
        dictionary[interf.label] = interf.getDictionary()

    if not data is None:
        data.categories.update(dictionary)

    return plots

def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
