
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


memexp = ""



def plots_ge4j_ge4t(data = None):
    label = "\geq 4 jets, \geq 4 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"


    interf_ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Deta_TaggedJetsAverage",
                                            label          = "ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage","")
    interf_ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage.category_label = label
    interf_ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage.minxval = 0.0
    interf_ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage.maxxval = 3.0
    interf_ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage.histotitle = "Evt_Deta_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage.histoname = "ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage)
    
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
    
    interf_ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets = vhi.variableHistoInterface(variable_name  = "Evt_Dr_minDrTaggedJets",
                                            label          = "ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets","")
    interf_ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets.category_label = label
    interf_ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets.minxval = 0.35
    interf_ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets.maxxval = 2.5
    interf_ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets.histotitle = "Evt_Dr_minDrTaggedJets"
    interf_ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets.histoname = "ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets"
    interf_ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets)
    
    interf_ljets_ge4j_ge4t_Evt_HT = vhi.variableHistoInterface(variable_name  = "Evt_HT",
                                            label          = "ljets_ge4j_ge4t_Evt_HT",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_HT.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_HT","")
    interf_ljets_ge4j_ge4t_Evt_HT.category_label = label
    interf_ljets_ge4j_ge4t_Evt_HT.bin_edges = [ 
				260.0,
				290.0,
				320.0,
				350.0,
				380.0,
				410.0,
				440.0,
				470.0,
				500.0,
				530.0,
				560.0,
				590.0,
				620.0,
				650.0,
				680.0,
				710.0,
				740.0,
				770.0,
				800.0,
				830.0,
				860.0,
				890.0,
				920.0,
				950.0,
				980.0,
				1010.0,
				1040.0,
				1070.0,
				1100.0,
				1130.0,
				1160.0,
				1190.0,
				1250.0,
				1340.0,
				1400.0,
				1460.0,
				1550.0,
				1670.0,
				1700.0
				]
    interf_ljets_ge4j_ge4t_Evt_HT.histotitle = "H_{T}"
    interf_ljets_ge4j_ge4t_Evt_HT.histoname = "ljets_ge4j_ge4t_Evt_HT"
    interf_ljets_ge4j_ge4t_Evt_HT.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_HT)
    
    interf_ljets_ge4j_ge4t_Evt_HT_wo_MET = vhi.variableHistoInterface(variable_name  = "Evt_HT_wo_MET",
                                            label          = "ljets_ge4j_ge4t_Evt_HT_wo_MET",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_HT_wo_MET.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_HT_wo_MET","")
    interf_ljets_ge4j_ge4t_Evt_HT_wo_MET.category_label = label
    interf_ljets_ge4j_ge4t_Evt_HT_wo_MET.bin_edges = [ 
				200.0,
				252.0,
				278.0,
				304.0,
				330.0,
				356.0,
				382.0,
				408.0,
				434.0,
				460.0,
				486.0,
				512.0,
				538.0,
				564.0,
				590.0,
				616.0,
				642.0,
				668.0,
				694.0,
				720.0,
				746.0,
				772.0,
				798.0,
				824.0,
				850.0,
				876.0,
				902.0,
				928.0,
				954.0,
				980.0,
				1006.0,
				1032.0,
				1058.0,
				1084.0,
				1110.0,
				1162.0,
				1240.0,
				1292.0,
				1370.0,
				1474.0,
				1500.0
				]
    interf_ljets_ge4j_ge4t_Evt_HT_wo_MET.histotitle = "H_{T} without MET"
    interf_ljets_ge4j_ge4t_Evt_HT_wo_MET.histoname = "ljets_ge4j_ge4t_Evt_HT_wo_MET"
    interf_ljets_ge4j_ge4t_Evt_HT_wo_MET.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_HT_wo_MET)
    
    interf_ljets_ge4j_ge4t_Evt_Pt_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Pt_JetsAverage",
                                            label          = "ljets_ge4j_ge4t_Evt_Pt_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_Pt_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_Pt_JetsAverage","")
    interf_ljets_ge4j_ge4t_Evt_Pt_JetsAverage.category_label = label
    interf_ljets_ge4j_ge4t_Evt_Pt_JetsAverage.minxval = 30.0
    interf_ljets_ge4j_ge4t_Evt_Pt_JetsAverage.maxxval = 500.0
    interf_ljets_ge4j_ge4t_Evt_Pt_JetsAverage.histotitle = "Evt_Pt_JetsAverage"
    interf_ljets_ge4j_ge4t_Evt_Pt_JetsAverage.histoname = "ljets_ge4j_ge4t_Evt_Pt_JetsAverage"
    interf_ljets_ge4j_ge4t_Evt_Pt_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_Pt_JetsAverage)
    
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
    
    interf_ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets = vhi.variableHistoInterface(variable_name  = "Evt_Pt_minDrTaggedJets",
                                            label          = "ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets","")
    interf_ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets.category_label = label
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
    
    interf_ljets_ge4j_ge4t_Jet_Eta_0 = vhi.variableHistoInterface(variable_name  = "Jet_Eta[0]",
                                            label          = "ljets_ge4j_ge4t_Jet_Eta_0",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Jet_Eta_0.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Jet_Eta_0","")
    interf_ljets_ge4j_ge4t_Jet_Eta_0.category_label = label
    interf_ljets_ge4j_ge4t_Jet_Eta_0.bin_edges = [ 
				-2.4,
				-2.2,
				-2.0,
				-1.8,
				-1.6,
				-1.4,
				-1.2,
				-1.0,
				-0.8,
				-0.6,
				-0.4,
				-0.2,
				0.0,
				0.2,
				0.4,
				0.6,
				0.8,
				1.0,
				1.2,
				1.4,
				1.6,
				1.8,
				2.0,
				2.2,
				5.0
				]
    interf_ljets_ge4j_ge4t_Jet_Eta_0.histotitle = "Jet_eta[0]"
    interf_ljets_ge4j_ge4t_Jet_Eta_0.histoname = "ljets_ge4j_ge4t_Jet_Eta_0"
    interf_ljets_ge4j_ge4t_Jet_Eta_0.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Jet_Eta_0)
    
    interf_ljets_ge4j_ge4t_Jet_Eta_1 = vhi.variableHistoInterface(variable_name  = "Jet_Eta[1]",
                                            label          = "ljets_ge4j_ge4t_Jet_Eta_1",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Jet_Eta_1.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Jet_Eta_1","")
    interf_ljets_ge4j_ge4t_Jet_Eta_1.category_label = label
    interf_ljets_ge4j_ge4t_Jet_Eta_1.bin_edges = [ 
				-2.4,
				-2.2,
				-2.0,
				-1.8,
				-1.6,
				-1.4,
				-1.2,
				-1.0,
				-0.8,
				-0.6,
				-0.4,
				-0.2,
				0.0,
				0.2,
				0.4,
				0.6,
				0.8,
				1.0,
				1.2,
				1.4,
				1.6,
				1.8,
				2.0,
				2.2,
				5.0
				]
    interf_ljets_ge4j_ge4t_Jet_Eta_1.histotitle = "Jet_eta[1]"
    interf_ljets_ge4j_ge4t_Jet_Eta_1.histoname = "ljets_ge4j_ge4t_Jet_Eta_1"
    interf_ljets_ge4j_ge4t_Jet_Eta_1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Jet_Eta_1)
    
    interf_ljets_ge4j_ge4t_Jet_Eta_2 = vhi.variableHistoInterface(variable_name  = "Jet_Eta[2]",
                                            label          = "ljets_ge4j_ge4t_Jet_Eta_2",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Jet_Eta_2.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Jet_Eta_2","")
    interf_ljets_ge4j_ge4t_Jet_Eta_2.category_label = label
    interf_ljets_ge4j_ge4t_Jet_Eta_2.bin_edges = [ 
				-2.4,
				-2.2,
				-2.0,
				-1.8,
				-1.6,
				-1.4,
				-1.2,
				-1.0,
				-0.8,
				-0.6,
				-0.4,
				-0.2,
				0.0,
				0.2,
				0.4,
				0.6,
				0.8,
				1.0,
				1.2,
				1.4,
				1.6,
				1.8,
				2.0,
				2.2,
				5.0
				]
    interf_ljets_ge4j_ge4t_Jet_Eta_2.histotitle = "Jet_eta[2]"
    interf_ljets_ge4j_ge4t_Jet_Eta_2.histoname = "ljets_ge4j_ge4t_Jet_Eta_2"
    interf_ljets_ge4j_ge4t_Jet_Eta_2.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Jet_Eta_2)
    
    interf_ljets_ge4j_ge4t_Jet_Eta_3 = vhi.variableHistoInterface(variable_name  = "Jet_Eta[3]",
                                            label          = "ljets_ge4j_ge4t_Jet_Eta_3",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Jet_Eta_3.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Jet_Eta_3","")
    interf_ljets_ge4j_ge4t_Jet_Eta_3.category_label = label
    interf_ljets_ge4j_ge4t_Jet_Eta_3.bin_edges = [ 
				-2.4,
				-2.2,
				-2.0,
				-1.8,
				-1.6,
				-1.4,
				-1.2,
				-1.0,
				-0.8,
				-0.6,
				-0.4,
				-0.2,
				0.0,
				0.2,
				0.4,
				0.6,
				0.8,
				1.0,
				1.2,
				1.4,
				1.6,
				1.8,
				2.0,
				2.2,
				5.0
				]
    interf_ljets_ge4j_ge4t_Jet_Eta_3.histotitle = "Jet_eta[3]"
    interf_ljets_ge4j_ge4t_Jet_Eta_3.histoname = "ljets_ge4j_ge4t_Jet_Eta_3"
    interf_ljets_ge4j_ge4t_Jet_Eta_3.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Jet_Eta_3)
    
    interf_ljets_ge4j_ge4t_Jet_Eta_4 = vhi.variableHistoInterface(variable_name  = "Jet_Eta[4]",
                                            label          = "ljets_ge4j_ge4t_Jet_Eta_4",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Jet_Eta_4.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Jet_Eta_4","")
    interf_ljets_ge4j_ge4t_Jet_Eta_4.category_label = label
    interf_ljets_ge4j_ge4t_Jet_Eta_4.bin_edges = [ 
				-2.4,
				-2.2,
				-2.0,
				-1.8,
				-1.6,
				-1.4,
				-1.2,
				-1.0,
				-0.8,
				-0.6,
				-0.4,
				-0.2,
				0.0,
				0.2,
				0.4,
				0.6,
				0.8,
				1.0,
				1.2,
				1.4,
				1.6,
				1.8,
				2.0,
				2.2,
				5.0
				]
    interf_ljets_ge4j_ge4t_Jet_Eta_4.histotitle = "Jet_eta[4]"
    interf_ljets_ge4j_ge4t_Jet_Eta_4.histoname = "ljets_ge4j_ge4t_Jet_Eta_4"
    interf_ljets_ge4j_ge4t_Jet_Eta_4.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Jet_Eta_4)
    
    interf_ljets_ge4j_ge4t_Jet_Eta_5 = vhi.variableHistoInterface(variable_name  = "Jet_Eta[5]",
                                            label          = "ljets_ge4j_ge4t_Jet_Eta_5",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Jet_Eta_5.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Jet_Eta_5","")
    interf_ljets_ge4j_ge4t_Jet_Eta_5.category_label = label
    interf_ljets_ge4j_ge4t_Jet_Eta_5.bin_edges = [ 
				-2.4,
				-2.2,
				-2.0,
				-1.8,
				-1.6,
				-1.4,
				-1.2,
				-1.0,
				-0.8,
				-0.6,
				-0.4,
				-0.2,
				0.0,
				0.2,
				0.4,
				0.6,
				0.8,
				1.0,
				1.2,
				1.4,
				1.6,
				1.8,
				2.0,
				2.2,
				5.0
				]
    interf_ljets_ge4j_ge4t_Jet_Eta_5.histotitle = "Jet_eta[5]"
    interf_ljets_ge4j_ge4t_Jet_Eta_5.histoname = "ljets_ge4j_ge4t_Jet_Eta_5"
    interf_ljets_ge4j_ge4t_Jet_Eta_5.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Jet_Eta_5)
    
    interf_ljets_ge4j_ge4t_Jet_Pt_0 = vhi.variableHistoInterface(variable_name  = "Jet_Pt[0]",
                                            label          = "ljets_ge4j_ge4t_Jet_Pt_0",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Jet_Pt_0.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Jet_Pt_0","")
    interf_ljets_ge4j_ge4t_Jet_Pt_0.category_label = label
    interf_ljets_ge4j_ge4t_Jet_Pt_0.bin_edges = [ 
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
				360.6,
				372.0,
				394.8,
				417.6,
				440.4,
				463.2,
				497.4,
				531.6,
				588.6,
				600.0
				]
    interf_ljets_ge4j_ge4t_Jet_Pt_0.histotitle = "Jet_Pt[0]"
    interf_ljets_ge4j_ge4t_Jet_Pt_0.histoname = "ljets_ge4j_ge4t_Jet_Pt_0"
    interf_ljets_ge4j_ge4t_Jet_Pt_0.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Jet_Pt_0)
    
    interf_ljets_ge4j_ge4t_Jet_Pt_1 = vhi.variableHistoInterface(variable_name  = "Jet_Pt[1]",
                                            label          = "ljets_ge4j_ge4t_Jet_Pt_1",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Jet_Pt_1.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Jet_Pt_1","")
    interf_ljets_ge4j_ge4t_Jet_Pt_1.category_label = label
    interf_ljets_ge4j_ge4t_Jet_Pt_1.bin_edges = [ 
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
				246.6,
				258.0,
				269.4,
				292.2,
				315.0,
				360.6,
				429.0,
				600.0
				]
    interf_ljets_ge4j_ge4t_Jet_Pt_1.histotitle = "Jet_Pt[1]"
    interf_ljets_ge4j_ge4t_Jet_Pt_1.histoname = "ljets_ge4j_ge4t_Jet_Pt_1"
    interf_ljets_ge4j_ge4t_Jet_Pt_1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Jet_Pt_1)
    
    interf_ljets_ge4j_ge4t_Jet_Pt_2 = vhi.variableHistoInterface(variable_name  = "Jet_Pt[2]",
                                            label          = "ljets_ge4j_ge4t_Jet_Pt_2",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Jet_Pt_2.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Jet_Pt_2","")
    interf_ljets_ge4j_ge4t_Jet_Pt_2.category_label = label
    interf_ljets_ge4j_ge4t_Jet_Pt_2.bin_edges = [ 
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
				223.8,
				269.4,
				600.0
				]
    interf_ljets_ge4j_ge4t_Jet_Pt_2.histotitle = "Jet_Pt[2]"
    interf_ljets_ge4j_ge4t_Jet_Pt_2.histoname = "ljets_ge4j_ge4t_Jet_Pt_2"
    interf_ljets_ge4j_ge4t_Jet_Pt_2.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Jet_Pt_2)
    
    interf_ljets_ge4j_ge4t_Jet_Pt_3 = vhi.variableHistoInterface(variable_name  = "Jet_Pt[3]",
                                            label          = "ljets_ge4j_ge4t_Jet_Pt_3",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Jet_Pt_3.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Jet_Pt_3","")
    interf_ljets_ge4j_ge4t_Jet_Pt_3.category_label = label
    interf_ljets_ge4j_ge4t_Jet_Pt_3.bin_edges = [ 
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
				178.2,
				600.0
				]
    interf_ljets_ge4j_ge4t_Jet_Pt_3.histotitle = "Jet_Pt[3]"
    interf_ljets_ge4j_ge4t_Jet_Pt_3.histoname = "ljets_ge4j_ge4t_Jet_Pt_3"
    interf_ljets_ge4j_ge4t_Jet_Pt_3.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Jet_Pt_3)
    
    interf_ljets_ge4j_ge4t_Jet_Pt_4 = vhi.variableHistoInterface(variable_name  = "Jet_Pt[4]",
                                            label          = "ljets_ge4j_ge4t_Jet_Pt_4",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Jet_Pt_4.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Jet_Pt_4","")
    interf_ljets_ge4j_ge4t_Jet_Pt_4.category_label = label
    interf_ljets_ge4j_ge4t_Jet_Pt_4.bin_edges = [ 
				30.0,
				41.4,
				52.8,
				64.2,
				75.6,
				87.0,
				98.4,
				109.8,
				132.6,
				600.0
				]
    interf_ljets_ge4j_ge4t_Jet_Pt_4.histotitle = "Jet_Pt[4]"
    interf_ljets_ge4j_ge4t_Jet_Pt_4.histoname = "ljets_ge4j_ge4t_Jet_Pt_4"
    interf_ljets_ge4j_ge4t_Jet_Pt_4.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Jet_Pt_4)
    
    interf_ljets_ge4j_ge4t_Jet_Pt_5 = vhi.variableHistoInterface(variable_name  = "Jet_Pt[5]",
                                            label          = "ljets_ge4j_ge4t_Jet_Pt_5",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Jet_Pt_5.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Jet_Pt_5","")
    interf_ljets_ge4j_ge4t_Jet_Pt_5.category_label = label
    interf_ljets_ge4j_ge4t_Jet_Pt_5.bin_edges = [ 
				30.0,
				41.4,
				52.8,
				64.2,
				75.6,
				87.0,
				98.4,
				600.0
				]
    interf_ljets_ge4j_ge4t_Jet_Pt_5.histotitle = "Jet_Pt[5]"
    interf_ljets_ge4j_ge4t_Jet_Pt_5.histoname = "ljets_ge4j_ge4t_Jet_Pt_5"
    interf_ljets_ge4j_ge4t_Jet_Pt_5.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Jet_Pt_5)
    
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_hdau2 = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_Jet_CSV_hdau2",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_hdau2",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_hdau2.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_hdau2","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_hdau2.category_label = label
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_hdau2.minxval = -1.5
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_hdau2.maxxval = 1.0
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_hdau2.histotitle = "Reco_JABDT_tHW_Jet_CSV_hdau2"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_hdau2.histoname = "ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_hdau2"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_hdau2.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_hdau2)
    
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_log_h_m = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_log_h_m",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_tHW_log_h_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_log_h_m.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_tHW_log_h_m","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_log_h_m.category_label = label
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_log_h_m.bin_edges = [ 
				1.0,
				2.8,
				3.78,
				3.94,
				4.1,
				4.26,
				4.42,
				4.58,
				4.74,
				4.9,
				5.06,
				5.22,
				5.38,
				5.86,
				6.5
				]
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_log_h_m.histotitle = "Reco_JABDT_tHW_log_h_m"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_log_h_m.histoname = "ljets_ge4j_ge4t_Reco_JABDT_tHW_log_h_m"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_log_h_m.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_log_h_m)
    
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_log_wb_m = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_log_wb_m",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_tHW_log_wb_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_log_wb_m.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_tHW_log_wb_m","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_log_wb_m.category_label = label
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_log_wb_m.bin_edges = [ 
				1.5,
				2.5,
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
				6.9,
				8.5
				]
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_log_wb_m.histotitle = "Reco_JABDT_tHW_log_wb_m"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_log_wb_m.histoname = "ljets_ge4j_ge4t_Reco_JABDT_tHW_log_wb_m"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_log_wb_m.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_log_wb_m)
    
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.category_label = label
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.minxval = -1.5
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.maxxval = 1.0
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.histotitle = "Reco_JABDT_tHW_energy_fraction"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.histoname = "ljets_ge4j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt)
    
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
    
    interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_tHq_bestJABDToutput",
                                            label          = "ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput","")
    interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput.category_label = label
    interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput.minxval = -1.0
    interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput.maxxval = 0.7
    interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput.histotitle = "Reco_tHq_bestJABDToutput"
    interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput.histoname = "ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput"
    interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput)
    
    interf_ljets_ge4j_ge4t_Reco_tHq_h_dr = vhi.variableHistoInterface(variable_name  = "Reco_tHq_h_dr",
                                            label          = "ljets_ge4j_ge4t_Reco_tHq_h_dr",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_tHq_h_dr.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_tHq_h_dr","")
    interf_ljets_ge4j_ge4t_Reco_tHq_h_dr.category_label = label
    interf_ljets_ge4j_ge4t_Reco_tHq_h_dr.minxval = 0.0
    interf_ljets_ge4j_ge4t_Reco_tHq_h_dr.maxxval = 5.0
    interf_ljets_ge4j_ge4t_Reco_tHq_h_dr.histotitle = "Reco_tHq_h_dr"
    interf_ljets_ge4j_ge4t_Reco_tHq_h_dr.histoname = "ljets_ge4j_ge4t_Reco_tHq_h_dr"
    interf_ljets_ge4j_ge4t_Reco_tHq_h_dr.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_tHq_h_dr)
    
    interf_ljets_ge4j_ge4t_Reco_tHq_hdau_pt1 = vhi.variableHistoInterface(variable_name  = "Reco_tHq_hdau_pt1",
                                            label          = "ljets_ge4j_ge4t_Reco_tHq_hdau_pt1",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_tHq_hdau_pt1.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_tHq_hdau_pt1","")
    interf_ljets_ge4j_ge4t_Reco_tHq_hdau_pt1.category_label = label
    interf_ljets_ge4j_ge4t_Reco_tHq_hdau_pt1.minxval = 30.0
    interf_ljets_ge4j_ge4t_Reco_tHq_hdau_pt1.maxxval = 500.0
    interf_ljets_ge4j_ge4t_Reco_tHq_hdau_pt1.histotitle = "Reco_tHq_hdau_pt1"
    interf_ljets_ge4j_ge4t_Reco_tHq_hdau_pt1.histoname = "ljets_ge4j_ge4t_Reco_tHq_hdau_pt1"
    interf_ljets_ge4j_ge4t_Reco_tHq_hdau_pt1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_tHq_hdau_pt1)
    
    interf_ljets_ge4j_ge4t_Reco_ttH_h_dr = vhi.variableHistoInterface(variable_name  = "Reco_ttH_h_dr",
                                            label          = "ljets_ge4j_ge4t_Reco_ttH_h_dr",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_ttH_h_dr.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_ttH_h_dr","")
    interf_ljets_ge4j_ge4t_Reco_ttH_h_dr.category_label = label
    interf_ljets_ge4j_ge4t_Reco_ttH_h_dr.minxval = -1.5
    interf_ljets_ge4j_ge4t_Reco_ttH_h_dr.maxxval = 4.0
    interf_ljets_ge4j_ge4t_Reco_ttH_h_dr.histotitle = "Reco_ttH_h_dr"
    interf_ljets_ge4j_ge4t_Reco_ttH_h_dr.histoname = "ljets_ge4j_ge4t_Reco_ttH_h_dr"
    interf_ljets_ge4j_ge4t_Reco_ttH_h_dr.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_ttH_h_dr)
    
    interf_ljets_ge4j_ge4t_Reco_ttH_h_pt = vhi.variableHistoInterface(variable_name  = "Reco_ttH_h_pt",
                                            label          = "ljets_ge4j_ge4t_Reco_ttH_h_pt",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_ttH_h_pt.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_ttH_h_pt","")
    interf_ljets_ge4j_ge4t_Reco_ttH_h_pt.category_label = label
    interf_ljets_ge4j_ge4t_Reco_ttH_h_pt.bin_edges = [ 
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
				323.31,
				347.37,
				371.43,
				407.52,
				467.67,
				539.85,
				600.0
				]
    interf_ljets_ge4j_ge4t_Reco_ttH_h_pt.histotitle = "Reco_ttH_h_pt"
    interf_ljets_ge4j_ge4t_Reco_ttH_h_pt.histoname = "ljets_ge4j_ge4t_Reco_ttH_h_pt"
    interf_ljets_ge4j_ge4t_Reco_ttH_h_pt.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_ttH_h_pt)
    
    interf_ljets_ge4j_ge4t_Reco_ttH_hdau_m1 = vhi.variableHistoInterface(variable_name  = "Reco_ttH_hdau_m1",
                                            label          = "ljets_ge4j_ge4t_Reco_ttH_hdau_m1",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_ttH_hdau_m1.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_ttH_hdau_m1","")
    interf_ljets_ge4j_ge4t_Reco_ttH_hdau_m1.category_label = label
    interf_ljets_ge4j_ge4t_Reco_ttH_hdau_m1.bin_edges = [ 
				-1.5,
				0.0,
				6.15,
				7.68,
				9.21,
				10.74,
				12.27,
				13.8,
				15.33,
				16.86,
				18.39,
				19.92,
				21.45,
				22.98,
				24.51,
				26.04,
				27.57,
				29.1,
				32.16,
				35.22,
				41.34,
				47.46,
				65.82,
				75.0
				]
    interf_ljets_ge4j_ge4t_Reco_ttH_hdau_m1.histotitle = "Reco_ttH_hdau_m1"
    interf_ljets_ge4j_ge4t_Reco_ttH_hdau_m1.histoname = "ljets_ge4j_ge4t_Reco_ttH_hdau_m1"
    interf_ljets_ge4j_ge4t_Reco_ttH_hdau_m1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_ttH_hdau_m1)
    
    interf_ljets_ge4j_ge4t_TaggedJet_Pt_1 = vhi.variableHistoInterface(variable_name  = "TaggedJet_Pt[1]",
                                            label          = "ljets_ge4j_ge4t_TaggedJet_Pt_1",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_TaggedJet_Pt_1.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_TaggedJet_Pt_1","")
    interf_ljets_ge4j_ge4t_TaggedJet_Pt_1.category_label = label
    interf_ljets_ge4j_ge4t_TaggedJet_Pt_1.bin_edges = [ 
				30.0,
				43.4,
				56.8,
				70.2,
				83.6,
				97.0,
				110.4,
				123.8,
				137.2,
				150.6,
				164.0,
				177.4,
				190.8,
				204.2,
				231.0,
				257.8,
				284.6,
				351.6,
				700.0
				]
    interf_ljets_ge4j_ge4t_TaggedJet_Pt_1.histotitle = "TaggedJet_Pt[1]"
    interf_ljets_ge4j_ge4t_TaggedJet_Pt_1.histoname = "ljets_ge4j_ge4t_TaggedJet_Pt_1"
    interf_ljets_ge4j_ge4t_TaggedJet_Pt_1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_TaggedJet_Pt_1)
    
    plots = init_plots(interfaces = interfaces)    
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    
def plots_ge4j_3t(data = None):
    label = "\geq 4 jets, 3 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM==3)&&(1.)"


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
    
    interf_ljets_ge4j_3t_Evt_Dr_minDrTaggedJets = vhi.variableHistoInterface(variable_name  = "Evt_Dr_minDrTaggedJets",
                                            label          = "ljets_ge4j_3t_Evt_Dr_minDrTaggedJets",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_Dr_minDrTaggedJets.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_Dr_minDrTaggedJets","")
    interf_ljets_ge4j_3t_Evt_Dr_minDrTaggedJets.category_label = label
    interf_ljets_ge4j_3t_Evt_Dr_minDrTaggedJets.bin_edges = [ 
				0.393,
				0.436,
				0.479,
				0.522,
				0.565,
				0.608,
				0.651,
				0.694,
				0.737,
				0.78,
				0.823,
				0.866,
				0.909,
				0.952,
				0.995,
				1.038,
				1.081,
				1.124,
				1.167,
				1.21,
				1.253,
				1.296,
				1.339,
				1.382,
				1.425,
				1.468,
				1.511,
				1.554,
				1.597,
				1.64,
				1.683,
				1.726,
				1.769,
				1.812,
				1.855,
				1.898,
				1.941,
				1.984,
				2.027,
				2.07,
				2.113,
				2.156,
				2.199,
				2.242,
				2.285,
				2.328,
				2.371,
				2.414,
				2.457,
				2.5
				]
    interf_ljets_ge4j_3t_Evt_Dr_minDrTaggedJets.histotitle = "Evt_Dr_minDrTaggedJets"
    interf_ljets_ge4j_3t_Evt_Dr_minDrTaggedJets.histoname = "ljets_ge4j_3t_Evt_Dr_minDrTaggedJets"
    interf_ljets_ge4j_3t_Evt_Dr_minDrTaggedJets.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_Dr_minDrTaggedJets)
    
    interf_ljets_ge4j_3t_Evt_HT = vhi.variableHistoInterface(variable_name  = "Evt_HT",
                                            label          = "ljets_ge4j_3t_Evt_HT",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_HT.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_HT","")
    interf_ljets_ge4j_3t_Evt_HT.category_label = label
    interf_ljets_ge4j_3t_Evt_HT.bin_edges = [ 
				230.0,
				260.0,
				290.0,
				320.0,
				350.0,
				380.0,
				410.0,
				440.0,
				470.0,
				500.0,
				530.0,
				560.0,
				590.0,
				620.0,
				650.0,
				680.0,
				710.0,
				740.0,
				770.0,
				800.0,
				830.0,
				860.0,
				890.0,
				920.0,
				950.0,
				980.0,
				1010.0,
				1040.0,
				1070.0,
				1100.0,
				1130.0,
				1160.0,
				1190.0,
				1220.0,
				1250.0,
				1280.0,
				1310.0,
				1340.0,
				1370.0,
				1400.0,
				1430.0,
				1460.0,
				1490.0,
				1520.0,
				1580.0,
				1610.0,
				1670.0,
				1700.0
				]
    interf_ljets_ge4j_3t_Evt_HT.histotitle = "H_{T}"
    interf_ljets_ge4j_3t_Evt_HT.histoname = "ljets_ge4j_3t_Evt_HT"
    interf_ljets_ge4j_3t_Evt_HT.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_HT)
    
    interf_ljets_ge4j_3t_Evt_HT_tags = vhi.variableHistoInterface(variable_name  = "Evt_HT_tags",
                                            label          = "ljets_ge4j_3t_Evt_HT_tags",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_HT_tags.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_HT_tags","")
    interf_ljets_ge4j_3t_Evt_HT_tags.category_label = label
    interf_ljets_ge4j_3t_Evt_HT_tags.minxval = 100.0
    interf_ljets_ge4j_3t_Evt_HT_tags.maxxval = 1000.0
    interf_ljets_ge4j_3t_Evt_HT_tags.histotitle = "Evt_HT_tags"
    interf_ljets_ge4j_3t_Evt_HT_tags.histoname = "ljets_ge4j_3t_Evt_HT_tags"
    interf_ljets_ge4j_3t_Evt_HT_tags.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_HT_tags)
    
    interf_ljets_ge4j_3t_Evt_M_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_M_JetsAverage",
                                            label          = "ljets_ge4j_3t_Evt_M_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_M_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_M_JetsAverage","")
    interf_ljets_ge4j_3t_Evt_M_JetsAverage.category_label = label
    interf_ljets_ge4j_3t_Evt_M_JetsAverage.minxval = 5.0
    interf_ljets_ge4j_3t_Evt_M_JetsAverage.maxxval = 50.0
    interf_ljets_ge4j_3t_Evt_M_JetsAverage.histotitle = "Evt_M_JetsAverage"
    interf_ljets_ge4j_3t_Evt_M_JetsAverage.histoname = "ljets_ge4j_3t_Evt_M_JetsAverage"
    interf_ljets_ge4j_3t_Evt_M_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_M_JetsAverage)
    
    interf_ljets_ge4j_3t_Evt_Pt_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Pt_JetsAverage",
                                            label          = "ljets_ge4j_3t_Evt_Pt_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_Pt_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_Pt_JetsAverage","")
    interf_ljets_ge4j_3t_Evt_Pt_JetsAverage.category_label = label
    interf_ljets_ge4j_3t_Evt_Pt_JetsAverage.minxval = 30.0
    interf_ljets_ge4j_3t_Evt_Pt_JetsAverage.maxxval = 500.0
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
    
    interf_ljets_ge4j_3t_Evt_Pt_minDrTaggedJets = vhi.variableHistoInterface(variable_name  = "Evt_Pt_minDrTaggedJets",
                                            label          = "ljets_ge4j_3t_Evt_Pt_minDrTaggedJets",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_Pt_minDrTaggedJets.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_Pt_minDrTaggedJets","")
    interf_ljets_ge4j_3t_Evt_Pt_minDrTaggedJets.category_label = label
    interf_ljets_ge4j_3t_Evt_Pt_minDrTaggedJets.bin_edges = [ 
				20.0,
				31.6,
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
				437.6,
				449.2,
				460.8,
				472.4,
				484.0,
				495.6,
				507.2,
				518.8,
				530.4,
				542.0,
				553.6,
				565.2,
				576.8,
				588.4,
				600.0
				]
    interf_ljets_ge4j_3t_Evt_Pt_minDrTaggedJets.histotitle = "Evt_Pt_minDrTaggedJets"
    interf_ljets_ge4j_3t_Evt_Pt_minDrTaggedJets.histoname = "ljets_ge4j_3t_Evt_Pt_minDrTaggedJets"
    interf_ljets_ge4j_3t_Evt_Pt_minDrTaggedJets.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_Pt_minDrTaggedJets)
    
    interf_ljets_ge4j_3t_Jet_Eta_0 = vhi.variableHistoInterface(variable_name  = "Jet_Eta[0]",
                                            label          = "ljets_ge4j_3t_Jet_Eta_0",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Jet_Eta_0.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Jet_Eta_0","")
    interf_ljets_ge4j_3t_Jet_Eta_0.category_label = label
    interf_ljets_ge4j_3t_Jet_Eta_0.bin_edges = [ 
				-2.4,
				-2.2,
				-2.0,
				-1.8,
				-1.6,
				-1.4,
				-1.2,
				-1.0,
				-0.8,
				-0.6,
				-0.4,
				-0.2,
				0.0,
				0.2,
				0.4,
				0.6,
				0.8,
				1.0,
				1.2,
				1.4,
				1.6,
				1.8,
				2.0,
				2.2,
				5.0
				]
    interf_ljets_ge4j_3t_Jet_Eta_0.histotitle = "Jet_Eta[0]"
    interf_ljets_ge4j_3t_Jet_Eta_0.histoname = "ljets_ge4j_3t_Jet_Eta_0"
    interf_ljets_ge4j_3t_Jet_Eta_0.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Jet_Eta_0)
    
    interf_ljets_ge4j_3t_Jet_Eta_1 = vhi.variableHistoInterface(variable_name  = "Jet_Eta[1]",
                                            label          = "ljets_ge4j_3t_Jet_Eta_1",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Jet_Eta_1.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Jet_Eta_1","")
    interf_ljets_ge4j_3t_Jet_Eta_1.category_label = label
    interf_ljets_ge4j_3t_Jet_Eta_1.bin_edges = [ 
				-2.4,
				-2.2,
				-2.0,
				-1.8,
				-1.6,
				-1.4,
				-1.2,
				-1.0,
				-0.8,
				-0.6,
				-0.4,
				-0.2,
				0.0,
				0.2,
				0.4,
				0.6,
				0.8,
				1.0,
				1.2,
				1.4,
				1.6,
				1.8,
				2.0,
				2.2,
				5.0
				]
    interf_ljets_ge4j_3t_Jet_Eta_1.histotitle = "Jet_Eta[1]"
    interf_ljets_ge4j_3t_Jet_Eta_1.histoname = "ljets_ge4j_3t_Jet_Eta_1"
    interf_ljets_ge4j_3t_Jet_Eta_1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Jet_Eta_1)
    
    interf_ljets_ge4j_3t_Jet_Eta_2 = vhi.variableHistoInterface(variable_name  = "Jet_Eta[2]",
                                            label          = "ljets_ge4j_3t_Jet_Eta_2",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Jet_Eta_2.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Jet_Eta_2","")
    interf_ljets_ge4j_3t_Jet_Eta_2.category_label = label
    interf_ljets_ge4j_3t_Jet_Eta_2.bin_edges = [ 
				-2.4,
				-2.2,
				-2.0,
				-1.8,
				-1.6,
				-1.4,
				-1.2,
				-1.0,
				-0.8,
				-0.6,
				-0.4,
				-0.2,
				0.0,
				0.2,
				0.4,
				0.6,
				0.8,
				1.0,
				1.2,
				1.4,
				1.6,
				1.8,
				2.0,
				2.2,
				5.0
				]
    interf_ljets_ge4j_3t_Jet_Eta_2.histotitle = "Jet_Eta[2]"
    interf_ljets_ge4j_3t_Jet_Eta_2.histoname = "ljets_ge4j_3t_Jet_Eta_2"
    interf_ljets_ge4j_3t_Jet_Eta_2.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Jet_Eta_2)
    
    interf_ljets_ge4j_3t_Jet_Eta_3 = vhi.variableHistoInterface(variable_name  = "Jet_Eta[3]",
                                            label          = "ljets_ge4j_3t_Jet_Eta_3",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Jet_Eta_3.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Jet_Eta_3","")
    interf_ljets_ge4j_3t_Jet_Eta_3.category_label = label
    interf_ljets_ge4j_3t_Jet_Eta_3.bin_edges = [ 
				-2.4,
				-2.2,
				-2.0,
				-1.8,
				-1.6,
				-1.4,
				-1.2,
				-1.0,
				-0.8,
				-0.6,
				-0.4,
				-0.2,
				0.0,
				0.2,
				0.4,
				0.6,
				0.8,
				1.0,
				1.2,
				1.4,
				1.6,
				1.8,
				2.0,
				2.2,
				5.0
				]
    interf_ljets_ge4j_3t_Jet_Eta_3.histotitle = "Jet_Eta[3]"
    interf_ljets_ge4j_3t_Jet_Eta_3.histoname = "ljets_ge4j_3t_Jet_Eta_3"
    interf_ljets_ge4j_3t_Jet_Eta_3.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Jet_Eta_3)
    
    interf_ljets_ge4j_3t_Jet_Eta_4 = vhi.variableHistoInterface(variable_name  = "Jet_Eta[4]",
                                            label          = "ljets_ge4j_3t_Jet_Eta_4",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Jet_Eta_4.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Jet_Eta_4","")
    interf_ljets_ge4j_3t_Jet_Eta_4.category_label = label
    interf_ljets_ge4j_3t_Jet_Eta_4.bin_edges = [ 
				-2.4,
				-2.2,
				-2.0,
				-1.8,
				-1.6,
				-1.4,
				-1.2,
				-1.0,
				-0.8,
				-0.6,
				-0.4,
				-0.2,
				0.0,
				0.2,
				0.4,
				0.6,
				0.8,
				1.0,
				1.2,
				1.4,
				1.6,
				1.8,
				2.0,
				2.2,
				5.0
				]
    interf_ljets_ge4j_3t_Jet_Eta_4.histotitle = "Jet_Eta[4]"
    interf_ljets_ge4j_3t_Jet_Eta_4.histoname = "ljets_ge4j_3t_Jet_Eta_4"
    interf_ljets_ge4j_3t_Jet_Eta_4.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Jet_Eta_4)
    
    interf_ljets_ge4j_3t_Jet_Eta_5 = vhi.variableHistoInterface(variable_name  = "Jet_Eta[5]",
                                            label          = "ljets_ge4j_3t_Jet_Eta_5",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Jet_Eta_5.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Jet_Eta_5","")
    interf_ljets_ge4j_3t_Jet_Eta_5.category_label = label
    interf_ljets_ge4j_3t_Jet_Eta_5.bin_edges = [ 
				-2.4,
				-2.2,
				-2.0,
				-1.8,
				-1.6,
				-1.4,
				-1.2,
				-1.0,
				-0.8,
				-0.6,
				-0.4,
				-0.2,
				0.0,
				0.2,
				0.4,
				0.6,
				0.8,
				1.0,
				1.2,
				1.4,
				1.6,
				1.8,
				2.0,
				2.2,
				5.0
				]
    interf_ljets_ge4j_3t_Jet_Eta_5.histotitle = "Jet_Eta[5]"
    interf_ljets_ge4j_3t_Jet_Eta_5.histoname = "ljets_ge4j_3t_Jet_Eta_5"
    interf_ljets_ge4j_3t_Jet_Eta_5.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Jet_Eta_5)
    
    interf_ljets_ge4j_3t_Jet_Pt_0 = vhi.variableHistoInterface(variable_name  = "Jet_Pt[0]",
                                            label          = "ljets_ge4j_3t_Jet_Pt_0",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Jet_Pt_0.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Jet_Pt_0","")
    interf_ljets_ge4j_3t_Jet_Pt_0.category_label = label
    interf_ljets_ge4j_3t_Jet_Pt_0.bin_edges = [ 
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
				440.4,
				451.8,
				463.2,
				474.6,
				486.0,
				508.8,
				520.2,
				543.0,
				554.4,
				577.2,
				588.6,
				600.0
				]
    interf_ljets_ge4j_3t_Jet_Pt_0.histotitle = "Jet_Pt[0]"
    interf_ljets_ge4j_3t_Jet_Pt_0.histoname = "ljets_ge4j_3t_Jet_Pt_0"
    interf_ljets_ge4j_3t_Jet_Pt_0.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Jet_Pt_0)
    
    interf_ljets_ge4j_3t_Jet_Pt_1 = vhi.variableHistoInterface(variable_name  = "Jet_Pt[1]",
                                            label          = "ljets_ge4j_3t_Jet_Pt_1",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Jet_Pt_1.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Jet_Pt_1","")
    interf_ljets_ge4j_3t_Jet_Pt_1.category_label = label
    interf_ljets_ge4j_3t_Jet_Pt_1.bin_edges = [ 
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
				303.6,
				315.0,
				337.8,
				349.2,
				372.0,
				394.8,
				429.0,
				463.2,
				497.4,
				600.0
				]
    interf_ljets_ge4j_3t_Jet_Pt_1.histotitle = "Jet_Pt[1]"
    interf_ljets_ge4j_3t_Jet_Pt_1.histoname = "ljets_ge4j_3t_Jet_Pt_1"
    interf_ljets_ge4j_3t_Jet_Pt_1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Jet_Pt_1)
    
    interf_ljets_ge4j_3t_Jet_Pt_2 = vhi.variableHistoInterface(variable_name  = "Jet_Pt[2]",
                                            label          = "ljets_ge4j_3t_Jet_Pt_2",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Jet_Pt_2.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Jet_Pt_2","")
    interf_ljets_ge4j_3t_Jet_Pt_2.category_label = label
    interf_ljets_ge4j_3t_Jet_Pt_2.bin_edges = [ 
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
				280.8,
				303.6,
				372.0,
				600.0
				]
    interf_ljets_ge4j_3t_Jet_Pt_2.histotitle = "Jet_Pt[2]"
    interf_ljets_ge4j_3t_Jet_Pt_2.histoname = "ljets_ge4j_3t_Jet_Pt_2"
    interf_ljets_ge4j_3t_Jet_Pt_2.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Jet_Pt_2)
    
    interf_ljets_ge4j_3t_Jet_Pt_3 = vhi.variableHistoInterface(variable_name  = "Jet_Pt[3]",
                                            label          = "ljets_ge4j_3t_Jet_Pt_3",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Jet_Pt_3.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Jet_Pt_3","")
    interf_ljets_ge4j_3t_Jet_Pt_3.category_label = label
    interf_ljets_ge4j_3t_Jet_Pt_3.bin_edges = [ 
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
				189.6,
				201.0,
				223.8,
				600.0
				]
    interf_ljets_ge4j_3t_Jet_Pt_3.histotitle = "Jet_Pt[3]"
    interf_ljets_ge4j_3t_Jet_Pt_3.histoname = "ljets_ge4j_3t_Jet_Pt_3"
    interf_ljets_ge4j_3t_Jet_Pt_3.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Jet_Pt_3)
    
    interf_ljets_ge4j_3t_Jet_Pt_4 = vhi.variableHistoInterface(variable_name  = "Jet_Pt[4]",
                                            label          = "ljets_ge4j_3t_Jet_Pt_4",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Jet_Pt_4.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Jet_Pt_4","")
    interf_ljets_ge4j_3t_Jet_Pt_4.category_label = label
    interf_ljets_ge4j_3t_Jet_Pt_4.bin_edges = [ 
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
				166.8,
				600.0
				]
    interf_ljets_ge4j_3t_Jet_Pt_4.histotitle = "Jet_Pt[4]"
    interf_ljets_ge4j_3t_Jet_Pt_4.histoname = "ljets_ge4j_3t_Jet_Pt_4"
    interf_ljets_ge4j_3t_Jet_Pt_4.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Jet_Pt_4)
    
    interf_ljets_ge4j_3t_Jet_Pt_5 = vhi.variableHistoInterface(variable_name  = "Jet_Pt[5]",
                                            label          = "ljets_ge4j_3t_Jet_Pt_5",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Jet_Pt_5.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Jet_Pt_5","")
    interf_ljets_ge4j_3t_Jet_Pt_5.category_label = label
    interf_ljets_ge4j_3t_Jet_Pt_5.bin_edges = [ 
				30.0,
				41.4,
				52.8,
				64.2,
				75.6,
				87.0,
				98.4,
				121.2,
				600.0
				]
    interf_ljets_ge4j_3t_Jet_Pt_5.histotitle = "Jet_Pt[5]"
    interf_ljets_ge4j_3t_Jet_Pt_5.histoname = "ljets_ge4j_3t_Jet_Pt_5"
    interf_ljets_ge4j_3t_Jet_Pt_5.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Jet_Pt_5)
    
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
    
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_log_h_m = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttH_log_h_m",
                                            label          = "ljets_ge4j_3t_Reco_JABDT_ttH_log_h_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_log_h_m.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_JABDT_ttH_log_h_m","")
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_log_h_m.category_label = label
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_log_h_m.bin_edges = [ 
				1.5,
				2.2,
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
				5.25,
				5.4,
				5.55,
				5.7,
				5.85,
				6.0
				]
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_log_h_m.histotitle = "Reco_JABDT_ttH_log_h_m"
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_log_h_m.histoname = "ljets_ge4j_3t_Reco_JABDT_ttH_log_h_m"
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_log_h_m.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_JABDT_ttH_log_h_m)
    
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",
                                            label          = "ljets_ge4j_3t_Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt","")
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.category_label = label
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.bin_edges = [ 
				-1.0,
				0.0,
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
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.histotitle = "Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt"
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.histoname = "ljets_ge4j_3t_Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt"
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.nhistobins = 20
    interfaces.append(interf_ljets_ge4j_3t_Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt)
    
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
    
    interf_ljets_ge4j_3t_Reco_tHW_hdau_pt1 = vhi.variableHistoInterface(variable_name  = "Reco_tHW_hdau_pt1",
                                            label          = "ljets_ge4j_3t_Reco_tHW_hdau_pt1",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_tHW_hdau_pt1.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_tHW_hdau_pt1","")
    interf_ljets_ge4j_3t_Reco_tHW_hdau_pt1.category_label = label
    interf_ljets_ge4j_3t_Reco_tHW_hdau_pt1.bin_edges = [ 
				-1.5,
				0.0,
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
				383.46,
				407.52,
				431.58,
				455.64,
				503.76,
				575.94,
				600.0
				]
    interf_ljets_ge4j_3t_Reco_tHW_hdau_pt1.histotitle = "Reco_tHW_hdau_pt1"
    interf_ljets_ge4j_3t_Reco_tHW_hdau_pt1.histoname = "ljets_ge4j_3t_Reco_tHW_hdau_pt1"
    interf_ljets_ge4j_3t_Reco_tHW_hdau_pt1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_tHW_hdau_pt1)
    
    interf_ljets_ge4j_3t_Reco_tHq_h_dr = vhi.variableHistoInterface(variable_name  = "Reco_tHq_h_dr",
                                            label          = "ljets_ge4j_3t_Reco_tHq_h_dr",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_tHq_h_dr.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_tHq_h_dr","")
    interf_ljets_ge4j_3t_Reco_tHq_h_dr.category_label = label
    interf_ljets_ge4j_3t_Reco_tHq_h_dr.bin_edges = [ 
				0.4,
				0.5,
				0.6,
				0.7,
				0.8,
				0.9,
				1.0,
				1.1,
				1.2,
				1.3,
				1.4,
				1.5,
				1.6,
				1.7,
				1.8,
				1.9,
				2.0,
				2.1,
				2.2,
				2.3,
				2.4,
				2.5,
				2.6,
				2.7,
				2.8,
				2.9,
				3.0,
				3.1,
				3.2,
				3.3,
				3.4,
				3.5,
				3.6,
				4.2,
				5.0
				]
    interf_ljets_ge4j_3t_Reco_tHq_h_dr.histotitle = "Reco_tHq_h_dr"
    interf_ljets_ge4j_3t_Reco_tHq_h_dr.histoname = "ljets_ge4j_3t_Reco_tHq_h_dr"
    interf_ljets_ge4j_3t_Reco_tHq_h_dr.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_tHq_h_dr)
    
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
    
    interf_ljets_ge4j_3t_Reco_tHq_hdau_pt1 = vhi.variableHistoInterface(variable_name  = "Reco_tHq_hdau_pt1",
                                            label          = "ljets_ge4j_3t_Reco_tHq_hdau_pt1",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_tHq_hdau_pt1.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_tHq_hdau_pt1","")
    interf_ljets_ge4j_3t_Reco_tHq_hdau_pt1.category_label = label
    interf_ljets_ge4j_3t_Reco_tHq_hdau_pt1.bin_edges = [ 
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
				330.8,
				340.2,
				349.6,
				359.0,
				368.4,
				377.8,
				396.6,
				406.0,
				415.4,
				434.2,
				443.6,
				471.8,
				490.6,
				500.0
				]
    interf_ljets_ge4j_3t_Reco_tHq_hdau_pt1.histotitle = "Reco_tHq_hdau_pt1"
    interf_ljets_ge4j_3t_Reco_tHq_hdau_pt1.histoname = "ljets_ge4j_3t_Reco_tHq_hdau_pt1"
    interf_ljets_ge4j_3t_Reco_tHq_hdau_pt1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_tHq_hdau_pt1)
    
    interf_ljets_ge4j_3t_Reco_ttH_h_pt = vhi.variableHistoInterface(variable_name  = "Reco_ttH_h_pt",
                                            label          = "ljets_ge4j_3t_Reco_ttH_h_pt",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_ttH_h_pt.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_ttH_h_pt","")
    interf_ljets_ge4j_3t_Reco_ttH_h_pt.category_label = label
    interf_ljets_ge4j_3t_Reco_ttH_h_pt.bin_edges = [ 
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
				467.67,
				491.73,
				515.79,
				587.97,
				600.0
				]
    interf_ljets_ge4j_3t_Reco_ttH_h_pt.histotitle = "Reco_ttH_h_pt"
    interf_ljets_ge4j_3t_Reco_ttH_h_pt.histoname = "ljets_ge4j_3t_Reco_ttH_h_pt"
    interf_ljets_ge4j_3t_Reco_ttH_h_pt.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_ttH_h_pt)
    
    interf_ljets_ge4j_3t_Reco_ttH_hdau_pt1 = vhi.variableHistoInterface(variable_name  = "Reco_ttH_hdau_pt1",
                                            label          = "ljets_ge4j_3t_Reco_ttH_hdau_pt1",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_ttH_hdau_pt1.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_ttH_hdau_pt1","")
    interf_ljets_ge4j_3t_Reco_ttH_hdau_pt1.category_label = label
    interf_ljets_ge4j_3t_Reco_ttH_hdau_pt1.bin_edges = [ 
				-1.5,
				0.0,
				38.62,
				48.65,
				58.68,
				68.71,
				78.74,
				88.77,
				98.8,
				108.83,
				118.86,
				128.89,
				138.92,
				148.95,
				158.98,
				169.01,
				179.04,
				189.07,
				199.1,
				209.13,
				219.16,
				229.19,
				239.22,
				249.25,
				259.28,
				269.31,
				279.34,
				289.37,
				299.4,
				319.46,
				329.49,
				339.52,
				349.55,
				359.58,
				369.61,
				379.64,
				399.7,
				429.79,
				459.88,
				489.97,
				500.0
				]
    interf_ljets_ge4j_3t_Reco_ttH_hdau_pt1.histotitle = "Reco_ttH_hdau_pt1"
    interf_ljets_ge4j_3t_Reco_ttH_hdau_pt1.histoname = "ljets_ge4j_3t_Reco_ttH_hdau_pt1"
    interf_ljets_ge4j_3t_Reco_ttH_hdau_pt1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_ttH_hdau_pt1)
    
    interf_ljets_ge4j_3t_Reco_ttH_hdau_pt2 = vhi.variableHistoInterface(variable_name  = "Reco_ttH_hdau_pt2",
                                            label          = "ljets_ge4j_3t_Reco_ttH_hdau_pt2",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_ttH_hdau_pt2.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_ttH_hdau_pt2","")
    interf_ljets_ge4j_3t_Reco_ttH_hdau_pt2.category_label = label
    interf_ljets_ge4j_3t_Reco_ttH_hdau_pt2.bin_edges = [ 
				-1.5,
				0.0,
				30.74,
				34.77,
				38.8,
				42.83,
				46.86,
				50.89,
				54.92,
				58.95,
				62.98,
				67.01,
				71.04,
				75.07,
				79.1,
				83.13,
				87.16,
				91.19,
				95.22,
				99.25,
				103.28,
				107.31,
				111.34,
				115.37,
				119.4,
				123.43,
				127.46,
				131.49,
				135.52,
				139.55,
				143.58,
				147.61,
				151.64,
				159.7,
				167.76,
				183.88,
				195.97,
				200.0
				]
    interf_ljets_ge4j_3t_Reco_ttH_hdau_pt2.histotitle = "Reco_ttH_hdau_pt2"
    interf_ljets_ge4j_3t_Reco_ttH_hdau_pt2.histoname = "ljets_ge4j_3t_Reco_ttH_hdau_pt2"
    interf_ljets_ge4j_3t_Reco_ttH_hdau_pt2.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_ttH_hdau_pt2)
    
    interf_ljets_ge4j_3t_TaggedJet_M_0 = vhi.variableHistoInterface(variable_name  = "TaggedJet_M[0]",
                                            label          = "ljets_ge4j_3t_TaggedJet_M_0",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_TaggedJet_M_0.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_TaggedJet_M_0","")
    interf_ljets_ge4j_3t_TaggedJet_M_0.category_label = label
    interf_ljets_ge4j_3t_TaggedJet_M_0.bin_edges = [ 
				4.0,
				8.0,
				12.0,
				16.0,
				20.0,
				24.0,
				28.0,
				32.0,
				36.0,
				40.0,
				44.0,
				48.0,
				52.0,
				56.0,
				60.0,
				64.0,
				68.0,
				76.0,
				80.0,
				88.0,
				108.0,
				128.0,
				200.0
				]
    interf_ljets_ge4j_3t_TaggedJet_M_0.histotitle = "TaggedJet_M[0]"
    interf_ljets_ge4j_3t_TaggedJet_M_0.histoname = "ljets_ge4j_3t_TaggedJet_M_0"
    interf_ljets_ge4j_3t_TaggedJet_M_0.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_TaggedJet_M_0)
    
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
    
    plots = init_plots(interfaces = interfaces)    
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    
def plots_dnn(data, discrname):

    ndefaultbins = 15
    interfaces = []


    # plots for ge4j_ge4t

    interf_ljets_ge4j_ge4t_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_ttH",
                                            label          = "ljets_ge4j_ge4t_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==0))")
    interf_ljets_ge4j_ge4t_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==0))","ljets_ge4j_ge4t_ttH_node","")
    interf_ljets_ge4j_ge4t_ttH_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_ttH_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_ttH_node.maxxval = 0.39
    interf_ljets_ge4j_ge4t_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_ttH_node)
    
    interf_ljets_ge4j_ge4t_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_ttmb",
                                            label          = "ljets_ge4j_ge4t_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==1))")
    interf_ljets_ge4j_ge4t_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==1))","ljets_ge4j_ge4t_ttmb_node","")
    interf_ljets_ge4j_ge4t_ttmb_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_ttmb_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_ttmb_node.maxxval = 0.29
    interf_ljets_ge4j_ge4t_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_ttmb_node)
    
    interf_ljets_ge4j_ge4t_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==2))")
    interf_ljets_ge4j_ge4t_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==2))","ljets_ge4j_ge4t_tt2b_node","")
    interf_ljets_ge4j_ge4t_tt2b_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_tt2b_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_tt2b_node.maxxval = 0.42
    interf_ljets_ge4j_ge4t_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_tt2b_node)
    
    interf_ljets_ge4j_ge4t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==3))")
    interf_ljets_ge4j_ge4t_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==3))","ljets_ge4j_ge4t_ttcc_node","")
    interf_ljets_ge4j_ge4t_ttcc_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_ttcc_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_ttcc_node.maxxval = 0.27
    interf_ljets_ge4j_ge4t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_ttcc_node)
    
    interf_ljets_ge4j_ge4t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==4))")
    interf_ljets_ge4j_ge4t_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==4))","ljets_ge4j_ge4t_ttlf_node","")
    interf_ljets_ge4j_ge4t_ttlf_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_ttlf_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_ttlf_node.maxxval = 0.27
    interf_ljets_ge4j_ge4t_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_ttlf_node)
    
    interf_ljets_ge4j_ge4t_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_tHq",
                                            label          = "ljets_ge4j_ge4t_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==5))")
    interf_ljets_ge4j_ge4t_tHq_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==5))","ljets_ge4j_ge4t_tHq_node","")
    interf_ljets_ge4j_ge4t_tHq_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_tHq_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_tHq_node.maxxval = 0.59
    interf_ljets_ge4j_ge4t_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_tHq_node)
    
    interf_ljets_ge4j_ge4t_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_tHW",
                                            label          = "ljets_ge4j_ge4t_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==6))")
    interf_ljets_ge4j_ge4t_tHW_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==6))","ljets_ge4j_ge4t_tHW_node","")
    interf_ljets_ge4j_ge4t_tHW_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_tHW_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_tHW_node.maxxval = 0.96
    interf_ljets_ge4j_ge4t_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_tHW_node)
    


    # plots for ge4j_3t

    interf_ljets_ge4j_3t_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_ttH",
                                            label          = "ljets_ge4j_3t_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==0))")
    interf_ljets_ge4j_3t_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==0))","ljets_ge4j_3t_ttH_node","")
    interf_ljets_ge4j_3t_ttH_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_ttH_node.minxval = 0.14
    interf_ljets_ge4j_3t_ttH_node.maxxval = 0.37
    interf_ljets_ge4j_3t_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_ttH_node)
    
    interf_ljets_ge4j_3t_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_ttmb",
                                            label          = "ljets_ge4j_3t_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==1))")
    interf_ljets_ge4j_3t_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==1))","ljets_ge4j_3t_ttmb_node","")
    interf_ljets_ge4j_3t_ttmb_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_ttmb_node.minxval = 0.14
    interf_ljets_ge4j_3t_ttmb_node.maxxval = 0.28
    interf_ljets_ge4j_3t_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_ttmb_node)
    
    interf_ljets_ge4j_3t_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_tt2b",
                                            label          = "ljets_ge4j_3t_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==2))")
    interf_ljets_ge4j_3t_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==2))","ljets_ge4j_3t_tt2b_node","")
    interf_ljets_ge4j_3t_tt2b_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_tt2b_node.minxval = 0.14
    interf_ljets_ge4j_3t_tt2b_node.maxxval = 0.9
    interf_ljets_ge4j_3t_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_tt2b_node)
    
    interf_ljets_ge4j_3t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_ttcc",
                                            label          = "ljets_ge4j_3t_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==3))")
    interf_ljets_ge4j_3t_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==3))","ljets_ge4j_3t_ttcc_node","")
    interf_ljets_ge4j_3t_ttcc_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_ttcc_node.minxval = 0.14
    interf_ljets_ge4j_3t_ttcc_node.maxxval = 0.23
    interf_ljets_ge4j_3t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_ttcc_node)
    
    interf_ljets_ge4j_3t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_ttlf",
                                            label          = "ljets_ge4j_3t_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==4))")
    interf_ljets_ge4j_3t_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==4))","ljets_ge4j_3t_ttlf_node","")
    interf_ljets_ge4j_3t_ttlf_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_ttlf_node.minxval = 0.14
    interf_ljets_ge4j_3t_ttlf_node.maxxval = 0.39
    interf_ljets_ge4j_3t_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_ttlf_node)
    
    interf_ljets_ge4j_3t_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_tHq",
                                            label          = "ljets_ge4j_3t_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==5))")
    interf_ljets_ge4j_3t_tHq_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==5))","ljets_ge4j_3t_tHq_node","")
    interf_ljets_ge4j_3t_tHq_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_tHq_node.minxval = 0.14
    interf_ljets_ge4j_3t_tHq_node.maxxval = 0.83
    interf_ljets_ge4j_3t_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_tHq_node)
    
    interf_ljets_ge4j_3t_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_tHW",
                                            label          = "ljets_ge4j_3t_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==6))")
    interf_ljets_ge4j_3t_tHW_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==6))","ljets_ge4j_3t_tHW_node","")
    interf_ljets_ge4j_3t_tHW_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_tHW_node.minxval = 0.14
    interf_ljets_ge4j_3t_tHW_node.maxxval = 1.0
    interf_ljets_ge4j_3t_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_tHW_node)
    

    for interf in interfaces:
        l = interf.label
        interf.histoname = discrname+"_"+l
        interf.histotitle = "final discriminator ({})".format(l)
        interf.selection = interf.category[0]

    DNNPlots = init_plots(interfaces = interfaces, data = data)
    return DNNPlots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_ge4j_ge4t(data)
    discriminatorPlots += plots_ge4j_3t(data)
    discriminatorPlots += plots_dnn(data, discrname)

    return discriminatorPlots


def init_plots(interfaces, data = None):
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
    