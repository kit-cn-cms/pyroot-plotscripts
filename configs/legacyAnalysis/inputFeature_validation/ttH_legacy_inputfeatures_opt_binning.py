
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



def plots_ljets_ge4j_ge4t(data = None):
    label = "\geq 4 jets, \geq 4 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"


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

    interf_ljets_ge4j_ge4t_CSV_1 = vhi.variableHistoInterface(variable_name  = "CSV[1]",
                                            label          = "ljets_ge4j_ge4t_CSV_1",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_CSV_1.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_CSV_1","")
    interf_ljets_ge4j_ge4t_CSV_1.bin_edges = [ 
				0.3638,
				0.3927,
				0.4216,
				0.4505,
				0.465,
				0.4794,
				0.4939,
				0.5084,
				0.5228,
				0.5373,
				0.5517,
				0.5662,
				0.5807,
				0.5951,
				0.6096,
				0.624,
				0.6385,
				0.653,
				0.6674,
				0.6819,
				0.6963,
				0.7108,
				0.7253,
				0.7397,
				0.7542,
				0.7686,
				0.7831,
				0.7976,
				0.812,
				0.8265,
				0.8409,
				0.8554,
				0.8699,
				0.8843,
				0.8988,
				0.9132,
				0.9277,
				0.9422,
				0.9566,
				0.9711,
				0.9855,
				1.0
				]
    interf_ljets_ge4j_ge4t_CSV_1.histotitle = "CSV[1]"
    interf_ljets_ge4j_ge4t_CSV_1.histoname = "ljets_ge4j_ge4t_CSV_1"
    interf_ljets_ge4j_ge4t_CSV_1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_CSV_1)
    
    interf_ljets_ge4j_ge4t_CSV_2 = vhi.variableHistoInterface(variable_name  = "CSV[2]",
                                            label          = "ljets_ge4j_ge4t_CSV_2",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_CSV_2.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_CSV_2","")
    interf_ljets_ge4j_ge4t_CSV_2.bin_edges = [ 
				0.3204,
				0.3348,
				0.3493,
				0.3638,
				0.3782,
				0.3927,
				0.4071,
				0.4216,
				0.4361,
				0.4505,
				0.465,
				0.4794,
				0.4939,
				0.5084,
				0.5228,
				0.5373,
				0.5517,
				0.5662,
				0.5807,
				0.5951,
				0.6096,
				0.624,
				0.6385,
				0.653,
				0.6674,
				0.6819,
				0.6963,
				0.7108,
				0.7253,
				0.7397,
				0.7542,
				0.7686,
				0.7831,
				0.7976,
				0.812,
				0.8265,
				0.8409,
				0.8554,
				0.8699,
				0.8988,
				0.9132,
				0.9277,
				0.9566,
				0.9855,
				1.0
				]
    interf_ljets_ge4j_ge4t_CSV_2.histotitle = "CSV[2]"
    interf_ljets_ge4j_ge4t_CSV_2.histoname = "ljets_ge4j_ge4t_CSV_2"
    interf_ljets_ge4j_ge4t_CSV_2.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_CSV_2)
    
    interf_ljets_ge4j_ge4t_Evt_CSV_avg = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg",
                                            label          = "ljets_ge4j_ge4t_Evt_CSV_avg",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
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
    
    interf_ljets_ge4j_ge4t_Evt_CSV_avg_tagged = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg_tagged",
                                            label          = "ljets_ge4j_ge4t_Evt_CSV_avg_tagged",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
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
    
    interf_ljets_ge4j_ge4t_Evt_Deta_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Deta_JetsAverage",
                                            label          = "ljets_ge4j_ge4t_Evt_Deta_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
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
    
    interf_ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Deta_TaggedJetsAverage",
                                            label          = "ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage","")
    interf_ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage.bin_edges = [ 
				0.12,
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
				2.22,
				2.34,
				3.0
				]
    interf_ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage.histotitle = "Evt_Deta_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage.histoname = "ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage)
    
    interf_ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets = vhi.variableHistoInterface(variable_name  = "Evt_Dr_minDrTaggedJets",
                                            label          = "ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets","")
    interf_ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets.bin_edges = [ 
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
				2.156,
				2.242,
				2.371,
				2.5
				]
    interf_ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets.histotitle = "Evt_Dr_minDrTaggedJets"
    interf_ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets.histoname = "ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets"
    interf_ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets)
    
    interf_ljets_ge4j_ge4t_Evt_M2_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_M2_JetsAverage",
                                            label          = "ljets_ge4j_ge4t_Evt_M2_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_M2_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_M2_JetsAverage","")
    interf_ljets_ge4j_ge4t_Evt_M2_JetsAverage.bin_edges = [ 
				61.0,
				72.0,
				83.0,
				94.0,
				105.0,
				116.0,
				127.0,
				138.0,
				149.0,
				160.0,
				171.0,
				182.0,
				193.0,
				204.0,
				215.0,
				226.0,
				237.0,
				248.0,
				259.0,
				270.0,
				281.0,
				292.0,
				303.0,
				314.0,
				325.0,
				336.0,
				347.0,
				358.0,
				369.0,
				380.0,
				391.0,
				402.0,
				413.0,
				435.0,
				457.0,
				490.0,
				545.0,
				600.0
				]
    interf_ljets_ge4j_ge4t_Evt_M2_JetsAverage.histotitle = "Evt_M2_JetsAverage"
    interf_ljets_ge4j_ge4t_Evt_M2_JetsAverage.histoname = "ljets_ge4j_ge4t_Evt_M2_JetsAverage"
    interf_ljets_ge4j_ge4t_Evt_M2_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_M2_JetsAverage)
    
    interf_ljets_ge4j_ge4t_Evt_M2_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_M2_TaggedJetsAverage",
                                            label          = "ljets_ge4j_ge4t_Evt_M2_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_M2_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_M2_TaggedJetsAverage","")
    interf_ljets_ge4j_ge4t_Evt_M2_TaggedJetsAverage.bin_edges = [ 
				40.0,
				59.2,
				78.4,
				97.6,
				116.8,
				136.0,
				155.2,
				174.4,
				193.6,
				212.8,
				232.0,
				251.2,
				270.4,
				289.6,
				308.8,
				328.0,
				347.2,
				366.4,
				385.6,
				404.8,
				424.0,
				443.2,
				462.4,
				500.8,
				539.2,
				635.2,
				1000.0
				]
    interf_ljets_ge4j_ge4t_Evt_M2_TaggedJetsAverage.histotitle = "Evt_M2_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_Evt_M2_TaggedJetsAverage.histoname = "ljets_ge4j_ge4t_Evt_M2_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_Evt_M2_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_M2_TaggedJetsAverage)
    
    interf_ljets_ge4j_ge4t_Evt_M_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_M_JetsAverage",
                                            label          = "ljets_ge4j_ge4t_Evt_M_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_M_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_M_JetsAverage","")
    interf_ljets_ge4j_ge4t_Evt_M_JetsAverage.bin_edges = [ 
				5.9,
				6.8,
				7.7,
				8.6,
				9.5,
				10.4,
				11.3,
				12.2,
				13.1,
				14.0,
				14.9,
				15.8,
				16.7,
				17.6,
				18.5,
				19.4,
				20.3,
				21.2,
				22.1,
				23.0,
				23.9,
				24.8,
				25.7,
				26.6,
				28.4,
				30.2,
				32.9,
				37.4,
				50.0
				]
    interf_ljets_ge4j_ge4t_Evt_M_JetsAverage.histotitle = "Evt_M_JetsAverage"
    interf_ljets_ge4j_ge4t_Evt_M_JetsAverage.histoname = "ljets_ge4j_ge4t_Evt_M_JetsAverage"
    interf_ljets_ge4j_ge4t_Evt_M_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_M_JetsAverage)
    
    interf_ljets_ge4j_ge4t_Evt_M_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_M_TaggedJetsAverage",
                                            label          = "ljets_ge4j_ge4t_Evt_M_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_M_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_M_TaggedJetsAverage","")
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
    
    interf_ljets_ge4j_ge4t_Evt_M_minDrLepTag = vhi.variableHistoInterface(variable_name  = "Evt_M_minDrLepTag",
                                            label          = "ljets_ge4j_ge4t_Evt_M_minDrLepTag",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
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
    
    interf_ljets_ge4j_ge4t_Evt_blr_transformed = vhi.variableHistoInterface(variable_name  = "Evt_blr_transformed",
                                            label          = "ljets_ge4j_ge4t_Evt_blr_transformed",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_blr_transformed.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_blr_transformed","")
    interf_ljets_ge4j_ge4t_Evt_blr_transformed.bin_edges = [ 
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
				8.0,
				8.35,
				8.7,
				9.05,
				9.4,
				9.75,
				10.1,
				10.45,
				10.8,
				11.15,
				11.5,
				11.85,
				12.2,
				12.55,
				12.9,
				13.25,
				13.6,
				13.95,
				14.3,
				14.65,
				15.0
				]
    interf_ljets_ge4j_ge4t_Evt_blr_transformed.histotitle = "Evt_blr_transformed"
    interf_ljets_ge4j_ge4t_Evt_blr_transformed.histoname = "ljets_ge4j_ge4t_Evt_blr_transformed"
    interf_ljets_ge4j_ge4t_Evt_blr_transformed.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_blr_transformed)
    
    interf_ljets_ge4j_ge4t_N_BTagsM = vhi.variableHistoInterface(variable_name  = "N_BTagsM",
                                            label          = "ljets_ge4j_ge4t_N_BTagsM",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_N_BTagsM.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_N_BTagsM","")
    interf_ljets_ge4j_ge4t_N_BTagsM.bin_edges = [ 
				3.5,
				4.5,
				5.5
				]
    interf_ljets_ge4j_ge4t_N_BTagsM.histotitle = "N_BTagsM"
    interf_ljets_ge4j_ge4t_N_BTagsM.histoname = "ljets_ge4j_ge4t_N_BTagsM"
    interf_ljets_ge4j_ge4t_N_BTagsM.nhistobins = 5
    interfaces.append(interf_ljets_ge4j_ge4t_N_BTagsM)
    
    interf_ljets_ge4j_ge4t_N_Jets = vhi.variableHistoInterface(variable_name  = "N_Jets",
                                            label          = "ljets_ge4j_ge4t_N_Jets",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_N_Jets.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_N_Jets","")
    interf_ljets_ge4j_ge4t_N_Jets.bin_edges = [ 
				3.5,
				4.5,
				5.5,
				6.5,
				7.5,
				8.5,
				9.5,
				10.5
				]
    interf_ljets_ge4j_ge4t_N_Jets.histotitle = "N_Jets"
    interf_ljets_ge4j_ge4t_N_Jets.histoname = "ljets_ge4j_ge4t_N_Jets"
    interf_ljets_ge4j_ge4t_N_Jets.nhistobins = 7
    interfaces.append(interf_ljets_ge4j_ge4t_N_Jets)
    
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_Jet_CSV_btop",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
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
    
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_hdau2 = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_Jet_CSV_hdau2",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_hdau2",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_hdau2.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_hdau2","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_hdau2.bin_edges = [ 
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
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_hdau2.histotitle = "Reco_JABDT_tHW_Jet_CSV_hdau2"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_hdau2.histoname = "ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_hdau2"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_hdau2.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_hdau2)
    
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_whaddau1 = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_Jet_CSV_whaddau1",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_whaddau1",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_whaddau1.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_whaddau1","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_whaddau1.bin_edges = [ 
				-0.5,
				0.0,
				0.05,
				0.1,
				0.15,
				0.2,
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
				0.85,
				0.95,
				1.0
				]
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_whaddau1.histotitle = "Reco_JABDT_tHW_Jet_CSV_whaddau1"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_whaddau1.histoname = "ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_whaddau1"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_whaddau1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_whaddau1)
    
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.bin_edges = [ 
				-0.5,
				0.0,
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
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.histotitle = "Reco_JABDT_tHW_energy_fraction"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.histoname = "ljets_ge4j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt)
    
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_btop = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHq_Jet_CSV_btop",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_btop",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_btop.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_btop","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_btop.bin_edges = [ 
				-0.5,
				0.0,
				0.05,
				0.1,
				0.15,
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
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_btop.histotitle = "Reco_JABDT_tHq_Jet_CSV_btop"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_btop.histoname = "ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_btop"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_btop.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_btop)
    
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1 = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHq_Jet_CSV_hdau1",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
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
    
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_abs_ljet_eta = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHq_abs_ljet_eta",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_tHq_abs_ljet_eta",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
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
    
    # interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_ljet_e__M__btop_e = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHq_ljet_e__M__btop_e",
    #                                         label          = "ljets_ge4j_ge4t_Reco_JABDT_tHq_ljet_e__M__btop_e",
    #                                         selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    # interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_ljet_e__M__btop_e.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_tHq_ljet_e__M__btop_e","")
    # interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_ljet_e__M__btop_e.bin_edges = [ 
	# 			-640.0,
	# 			-400.0,
	# 			-280.0,
	# 			-220.0,
	# 			-160.0,
	# 			-100.0,
	# 			-40.0,
	# 			20.0,
	# 			80.0,
	# 			140.0,
	# 			200.0,
	# 			260.0,
	# 			320.0,
	# 			380.0,
	# 			440.0,
	# 			500.0,
	# 			560.0,
	# 			620.0,
	# 			680.0,
	# 			740.0,
	# 			800.0,
	# 			920.0,
	# 			1040.0,
	# 			1220.0,
	# 			1400.0,
	# 			1640.0,
	# 			1940.0,
	# 			2000.0
	# 			]
    # interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_ljet_e__M__btop_e.histotitle = "Reco_JABDT_tHq_ljet_e__M__btop_e"
    # interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_ljet_e__M__btop_e.histoname = "ljets_ge4j_ge4t_Reco_JABDT_tHq_ljet_e__M__btop_e"
    # interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_ljet_e__M__btop_e.nhistobins = 50
    # interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_ljet_e__M__btop_e)
    
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_Jet_CSV_btoplep = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttH_Jet_CSV_btoplep",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_ttH_Jet_CSV_btoplep",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_Jet_CSV_btoplep.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_ttH_Jet_CSV_btoplep","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_Jet_CSV_btoplep.bin_edges = [ 
				-0.5,
				0.0,
				0.05,
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
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_Jet_CSV_btoplep.histotitle = "Reco_JABDT_ttH_Jet_CSV_btoplep"
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_Jet_CSV_btoplep.histoname = "ljets_ge4j_ge4t_Reco_JABDT_ttH_Jet_CSV_btoplep"
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_Jet_CSV_btoplep.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_Jet_CSV_btoplep)
    
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_Jet_CSV_hdau2 = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttH_Jet_CSV_hdau2",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_ttH_Jet_CSV_hdau2",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_Jet_CSV_hdau2.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_ttH_Jet_CSV_hdau2","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_Jet_CSV_hdau2.bin_edges = [ 
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
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_Jet_CSV_hdau2.histotitle = "Reco_JABDT_ttH_Jet_CSV_hdau2"
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_Jet_CSV_hdau2.histoname = "ljets_ge4j_ge4t_Reco_JABDT_ttH_Jet_CSV_hdau2"
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_Jet_CSV_hdau2.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_Jet_CSV_hdau2)
    
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_m = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttH_log_toplep_m",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_m.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_m","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_m.bin_edges = [ 
				3.5,
				4.3,
				4.8,
				4.98,
				5.16,
				5.34,
				5.52,
				5.7,
				5.88,
				6.06,
				6.24,
				6.6,
				7.5
				]
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_m.histotitle = "Reco_JABDT_ttH_log_toplep_m"
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_m.histoname = "ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_m"
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_m.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_m)
    
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_btoplep = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttbar_Jet_CSV_btoplep",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_btoplep",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_btoplep.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_btoplep","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_btoplep.bin_edges = [ 
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
				0.82,
				0.84,
				0.86,
				0.88,
				0.9,
				0.92,
				0.94,
				0.96,
				0.98,
				1.0
				]
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_btoplep.histotitle = "Reco_JABDT_ttbar_Jet_CSV_btoplep"
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_btoplep.histoname = "ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_btoplep"
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_btoplep.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_btoplep)
    
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau1 = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttbar_Jet_CSV_whaddau1",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau1",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau1.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau1","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau1.bin_edges = [ 
				0.0,
				0.02,
				0.04,
				0.06,
				0.08,
				0.12,
				0.18,
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
				0.86,
				0.9,
				0.94,
				1.0
				]
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau1.histotitle = "Reco_JABDT_ttbar_Jet_CSV_whaddau1"
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau1.histoname = "ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau1"
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau1)
    
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau2 = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttbar_Jet_CSV_whaddau2",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau2",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
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
    
    interf_ljets_ge4j_ge4t_Reco_tHW_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_tHW_bestJABDToutput",
                                            label          = "ljets_ge4j_ge4t_Reco_tHW_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_tHW_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_tHW_bestJABDToutput","")
    interf_ljets_ge4j_ge4t_Reco_tHW_bestJABDToutput.bin_edges = [ 
				-0.8,
				-0.6,
				-0.104,
				-0.072,
				-0.04,
				-0.008,
				0.024,
				0.056,
				0.088,
				0.12,
				0.152,
				0.184,
				0.216,
				0.248,
				0.28,
				0.312,
				0.344,
				0.376,
				0.408,
				0.44,
				0.472,
				0.6
				]
    interf_ljets_ge4j_ge4t_Reco_tHW_bestJABDToutput.histotitle = "Reco_tHW_bestJABDToutput"
    interf_ljets_ge4j_ge4t_Reco_tHW_bestJABDToutput.histoname = "ljets_ge4j_ge4t_Reco_tHW_bestJABDToutput"
    interf_ljets_ge4j_ge4t_Reco_tHW_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_tHW_bestJABDToutput)
    
    interf_ljets_ge4j_ge4t_Reco_tHW_top_h_dr = vhi.variableHistoInterface(variable_name  = "Reco_tHW_top_h_dr",
                                            label          = "ljets_ge4j_ge4t_Reco_tHW_top_h_dr",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_tHW_top_h_dr.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_tHW_top_h_dr","")
    interf_ljets_ge4j_ge4t_Reco_tHW_top_h_dr.bin_edges = [ 
				-1.0,
				-0.5,
				0.97,
				1.16,
				1.35,
				1.54,
				1.73,
				1.92,
				2.11,
				2.3,
				2.49,
				2.68,
				2.87,
				3.06,
				3.25,
				3.44,
				3.63,
				3.82,
				4.01,
				4.2,
				4.39,
				4.58,
				5.15,
				8.0
				]
    interf_ljets_ge4j_ge4t_Reco_tHW_top_h_dr.histotitle = "Reco_tHW_top_h_dr"
    interf_ljets_ge4j_ge4t_Reco_tHW_top_h_dr.histoname = "ljets_ge4j_ge4t_Reco_tHW_top_h_dr"
    interf_ljets_ge4j_ge4t_Reco_tHW_top_h_dr.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_tHW_top_h_dr)
    
    interf_ljets_ge4j_ge4t_Reco_tHW_whad_dr = vhi.variableHistoInterface(variable_name  = "Reco_tHW_whad_dr",
                                            label          = "ljets_ge4j_ge4t_Reco_tHW_whad_dr",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_tHW_whad_dr.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_tHW_whad_dr","")
    interf_ljets_ge4j_ge4t_Reco_tHW_whad_dr.bin_edges = [ 
				-1.5,
				0.0,
				0.58,
				0.71,
				0.84,
				0.97,
				1.1,
				1.23,
				1.36,
				1.49,
				1.62,
				1.75,
				1.88,
				2.01,
				2.14,
				2.27,
				2.4,
				2.53,
				2.66,
				2.79,
				2.92,
				3.05,
				3.18,
				3.31,
				3.7,
				4.22,
				4.87,
				5.0
				]
    interf_ljets_ge4j_ge4t_Reco_tHW_whad_dr.histotitle = "Reco_tHW_whad_dr"
    interf_ljets_ge4j_ge4t_Reco_tHW_whad_dr.histoname = "ljets_ge4j_ge4t_Reco_tHW_whad_dr"
    interf_ljets_ge4j_ge4t_Reco_tHW_whad_dr.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_tHW_whad_dr)
    
    interf_ljets_ge4j_ge4t_Reco_tHW_whaddau_m1 = vhi.variableHistoInterface(variable_name  = "Reco_tHW_whaddau_m1",
                                            label          = "ljets_ge4j_ge4t_Reco_tHW_whaddau_m1",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_tHW_whaddau_m1.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_tHW_whaddau_m1","")
    interf_ljets_ge4j_ge4t_Reco_tHW_whaddau_m1.bin_edges = [ 
				-1.5,
				0.,
				6.62,
				8.65,
				10.68,
				12.71,
				14.74,
				16.77,
				18.8,
				20.83,
				22.86,
				24.89,
				26.92,
				28.95,
				30.98,
				35.04,
				39.1,
				43.16,
				49.25,
				63.46,
				100.0
				]
    interf_ljets_ge4j_ge4t_Reco_tHW_whaddau_m1.histotitle = "Reco_tHW_whaddau_m1"
    interf_ljets_ge4j_ge4t_Reco_tHW_whaddau_m1.histoname = "ljets_ge4j_ge4t_Reco_tHW_whaddau_m1"
    interf_ljets_ge4j_ge4t_Reco_tHW_whaddau_m1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_tHW_whaddau_m1)
    
    interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_tHq_bestJABDToutput",
                                            label          = "ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput","")
    interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput.bin_edges = [ 
				-1.0,
				-0.6,
				-0.15,
				-0.116,
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
				0.7
				]
    interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput.histotitle = "Reco_tHq_bestJABDToutput"
    interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput.histoname = "ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput"
    interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput)
    
    interf_ljets_ge4j_ge4t_Reco_tHq_costhetastar = vhi.variableHistoInterface(variable_name  = "Reco_tHq_costhetastar",
                                            label          = "ljets_ge4j_ge4t_Reco_tHq_costhetastar",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_tHq_costhetastar.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_tHq_costhetastar","")
    interf_ljets_ge4j_ge4t_Reco_tHq_costhetastar.bin_edges = [ 
				-1.5,
				-1.04,
				-0.92,
				-0.8,
				-0.68,
				-0.56,
				-0.44,
				-0.32,
				-0.2,
				-0.08,
				0.04,
				0.16,
				0.28,
				0.4,
				0.52,
				0.64,
				0.76,
				0.88,
				1.0
				]
    interf_ljets_ge4j_ge4t_Reco_tHq_costhetastar.histotitle = "Reco_tHq_costhetastar"
    interf_ljets_ge4j_ge4t_Reco_tHq_costhetastar.histoname = "ljets_ge4j_ge4t_Reco_tHq_costhetastar"
    interf_ljets_ge4j_ge4t_Reco_tHq_costhetastar.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_tHq_costhetastar)
    
    interf_ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_ttH_bestJABDToutput",
                                            label          = "ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput","")
    interf_ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput.bin_edges = [ 
				-1.0,
				-0.5,
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
				0.7
				]
    interf_ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput.histotitle = "Reco_ttH_bestJABDToutput"
    interf_ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput.histoname = "ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput"
    interf_ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput)
    
    interf_ljets_ge4j_ge4t_Reco_ttH_toplep_m = vhi.variableHistoInterface(variable_name  = "Reco_ttH_toplep_m",
                                            label          = "ljets_ge4j_ge4t_Reco_ttH_toplep_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_ttH_toplep_m.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_ttH_toplep_m","")
    interf_ljets_ge4j_ge4t_Reco_ttH_toplep_m.bin_edges = [ 
				-1.5,
				0.0,
				133.77,
				148.8,
				163.83,
				178.86,
				193.89,
				208.92,
				223.95,
				238.98,
				254.01,
				269.04,
				284.07,
				299.1,
				314.13,
				329.16,
				359.22,
				389.28,
				434.37,
				494.49,
				569.64,
				734.97,
				750.0
				]
    interf_ljets_ge4j_ge4t_Reco_ttH_toplep_m.histotitle = "Reco_ttH_toplep_m"
    interf_ljets_ge4j_ge4t_Reco_ttH_toplep_m.histoname = "ljets_ge4j_ge4t_Reco_ttH_toplep_m"
    interf_ljets_ge4j_ge4t_Reco_ttH_toplep_m.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_ttH_toplep_m)
    
    interf_ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_ttbar_bestJABDToutput",
                                            label          = "ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput","")
    interf_ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput.bin_edges = [ 
				-0.246,
				-0.158,
				-0.114,
				-0.07,
				-0.048,
				-0.026,
				-0.004,
				0.018,
				0.04,
				0.062,
				0.084,
				0.106,
				0.128,
				0.15,
				0.172,
				0.194,
				0.216,
				0.238,
				0.26,
				0.282,
				0.304,
				0.326,
				0.348,
				0.37,
				0.392,
				0.414,
				0.436,
				0.458,
				0.48,
				0.502,
				0.524,
				0.546,
				0.7
				]
    interf_ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput.histotitle = "Reco_ttbar_bestJABDToutput"
    interf_ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput.histoname = "ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput"
    interf_ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput)
    
    interf_ljets_ge4j_ge4t_Reco_ttbar_toplep_m = vhi.variableHistoInterface(variable_name  = "Reco_ttbar_toplep_m",
                                            label          = "ljets_ge4j_ge4t_Reco_ttbar_toplep_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
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
    
    interf_ljets_ge4j_ge4t_TaggedJet_M_0 = vhi.variableHistoInterface(variable_name  = "TaggedJet_M[0]",
                                            label          = "ljets_ge4j_ge4t_TaggedJet_M_0",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_TaggedJet_M_0.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_TaggedJet_M_0","")
    interf_ljets_ge4j_ge4t_TaggedJet_M_0.bin_edges = [ 
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
				56.0,
				64.0,
				80.0,
				200.0
				]
    interf_ljets_ge4j_ge4t_TaggedJet_M_0.histotitle = "TaggedJet_M[0]"
    interf_ljets_ge4j_ge4t_TaggedJet_M_0.histoname = "ljets_ge4j_ge4t_TaggedJet_M_0"
    interf_ljets_ge4j_ge4t_TaggedJet_M_0.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_TaggedJet_M_0)
    
    plots = init_plots(interfaces = interfaces)    
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    
def plots_ljets_ge4j_3t(data = None):
    label = "\geq 4 jets, 3 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM==3)&&(1.)"

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


    interf_ljets_ge4j_3t_CSV_1 = vhi.variableHistoInterface(variable_name  = "CSV[1]",
                                            label          = "ljets_ge4j_3t_CSV_1",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_CSV_1.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_CSV_1","")
    interf_ljets_ge4j_3t_CSV_1.bin_edges = [ 
				0.3059,
				0.3204,
				0.3348,
				0.3493,
				0.3638,
				0.3782,
				0.3927,
				0.4071,
				0.4216,
				0.4361,
				0.4505,
				0.465,
				0.4794,
				0.4939,
				0.5084,
				0.5228,
				0.5373,
				0.5517,
				0.5662,
				0.5807,
				0.5951,
				0.6096,
				0.624,
				0.6385,
				0.653,
				0.6674,
				0.6819,
				0.6963,
				0.7108,
				0.7253,
				0.7397,
				0.7542,
				0.7686,
				0.7831,
				0.7976,
				0.812,
				0.8265,
				0.8409,
				0.8554,
				0.8699,
				0.8843,
				0.8988,
				0.9132,
				0.9277,
				0.9422,
				0.9566,
				0.9711,
				0.9855,
				1.0
				]
    interf_ljets_ge4j_3t_CSV_1.histotitle = "CSV[1]"
    interf_ljets_ge4j_3t_CSV_1.histoname = "ljets_ge4j_3t_CSV_1"
    interf_ljets_ge4j_3t_CSV_1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_CSV_1)
    
    interf_ljets_ge4j_3t_Evt_CSV_avg = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg",
                                            label          = "ljets_ge4j_3t_Evt_CSV_avg",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
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
    
    interf_ljets_ge4j_3t_Evt_CSV_avg_tagged = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg_tagged",
                                            label          = "ljets_ge4j_3t_Evt_CSV_avg_tagged",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_CSV_avg_tagged.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_CSV_avg_tagged","")
    interf_ljets_ge4j_3t_Evt_CSV_avg_tagged.bin_edges = [ 
				0.328,
				0.342,
				0.356,
				0.37,
				0.384,
				0.398,
				0.412,
				0.426,
				0.44,
				0.454,
				0.468,
				0.482,
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
    interf_ljets_ge4j_3t_Evt_CSV_avg_tagged.histotitle = "Evt_CSV_avg_tagged"
    interf_ljets_ge4j_3t_Evt_CSV_avg_tagged.histoname = "ljets_ge4j_3t_Evt_CSV_avg_tagged"
    interf_ljets_ge4j_3t_Evt_CSV_avg_tagged.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_CSV_avg_tagged)
    
    interf_ljets_ge4j_3t_Evt_CSV_dev = vhi.variableHistoInterface(variable_name  = "Evt_CSV_dev",
                                            label          = "ljets_ge4j_3t_Evt_CSV_dev",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_CSV_dev.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_CSV_dev","")
    interf_ljets_ge4j_3t_Evt_CSV_dev.bin_edges = [ 
				0.005,
				0.015,
				0.02,
				0.025,
				0.03,
				0.035,
				0.04,
				0.045,
				0.05,
				0.055,
				0.06,
				0.065,
				0.07,
				0.075,
				0.08,
				0.085,
				0.09,
				0.095,
				0.1,
				0.105,
				0.11,
				0.115,
				0.12,
				0.125,
				0.13,
				0.135,
				0.14,
				0.145,
				0.15,
				0.155,
				0.16,
				0.165,
				0.17,
				0.175,
				0.18,
				0.185,
				0.19,
				0.195,
				0.2,
				0.205,
				0.21,
				0.215,
				0.22,
				0.225,
				0.23,
				0.235,
				0.25
				]
    interf_ljets_ge4j_3t_Evt_CSV_dev.histotitle = "Evt_CSV_dev"
    interf_ljets_ge4j_3t_Evt_CSV_dev.histoname = "ljets_ge4j_3t_Evt_CSV_dev"
    interf_ljets_ge4j_3t_Evt_CSV_dev.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_CSV_dev)
    
    interf_ljets_ge4j_3t_Evt_CSV_min_tagged = vhi.variableHistoInterface(variable_name  = "Evt_CSV_min_tagged",
                                            label          = "ljets_ge4j_3t_Evt_CSV_min_tagged",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_CSV_min_tagged.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_CSV_min_tagged","")
    interf_ljets_ge4j_3t_Evt_CSV_min_tagged.bin_edges = [ 
				0.2915,
				0.3059,
				0.3204,
				0.3348,
				0.3493,
				0.3638,
				0.3782,
				0.3927,
				0.4071,
				0.4216,
				0.4361,
				0.4505,
				0.465,
				0.4794,
				0.4939,
				0.5084,
				0.5228,
				0.5373,
				0.5517,
				0.5662,
				0.5807,
				0.5951,
				0.6096,
				0.624,
				0.6385,
				0.653,
				0.6674,
				0.6819,
				0.6963,
				0.7108,
				0.7253,
				0.7397,
				0.7542,
				0.7686,
				0.7831,
				0.7976,
				0.812,
				0.8265,
				0.8409,
				0.8554,
				0.8699,
				0.8843,
				0.8988,
				0.9132,
				0.9277,
				0.9422,
				0.9566,
				0.9711,
				0.9855,
				1.0
				]
    interf_ljets_ge4j_3t_Evt_CSV_min_tagged.histotitle = "Evt_CSV_min_tagged"
    interf_ljets_ge4j_3t_Evt_CSV_min_tagged.histoname = "ljets_ge4j_3t_Evt_CSV_min_tagged"
    interf_ljets_ge4j_3t_Evt_CSV_min_tagged.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_CSV_min_tagged)
    
    interf_ljets_ge4j_3t_Evt_Deta_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Deta_JetsAverage",
                                            label          = "ljets_ge4j_3t_Evt_Deta_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
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
    
    interf_ljets_ge4j_3t_Evt_Deta_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Deta_TaggedJetsAverage",
                                            label          = "ljets_ge4j_3t_Evt_Deta_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
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
    
    interf_ljets_ge4j_3t_Evt_Dr_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Dr_JetsAverage",
                                            label          = "ljets_ge4j_3t_Evt_Dr_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_Dr_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_Dr_JetsAverage","")
    interf_ljets_ge4j_3t_Evt_Dr_JetsAverage.bin_edges = [ 
				0.85,
				1.06,
				1.13,
				1.2,
				1.27,
				1.34,
				1.41,
				1.48,
				1.55,
				1.62,
				1.69,
				1.76,
				1.83,
				1.9,
				1.97,
				2.04,
				2.11,
				2.18,
				2.25,
				2.32,
				2.39,
				2.46,
				2.53,
				2.6,
				2.67,
				2.74,
				2.81,
				2.88,
				2.95,
				3.02,
				3.09,
				3.16,
				3.23,
				3.3,
				3.37,
				3.44,
				4.0
				]
    interf_ljets_ge4j_3t_Evt_Dr_JetsAverage.histotitle = "Evt_Dr_JetsAverage"
    interf_ljets_ge4j_3t_Evt_Dr_JetsAverage.histoname = "ljets_ge4j_3t_Evt_Dr_JetsAverage"
    interf_ljets_ge4j_3t_Evt_Dr_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_Dr_JetsAverage)
    
    interf_ljets_ge4j_3t_Evt_HT_tags = vhi.variableHistoInterface(variable_name  = "Evt_HT_tags",
                                            label          = "ljets_ge4j_3t_Evt_HT_tags",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_HT_tags.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_HT_tags","")
    interf_ljets_ge4j_3t_Evt_HT_tags.bin_edges = [ 
				100.0,
				118.0,
				136.0,
				154.0,
				172.0,
				190.0,
				208.0,
				226.0,
				244.0,
				262.0,
				280.0,
				298.0,
				316.0,
				334.0,
				352.0,
				370.0,
				388.0,
				406.0,
				424.0,
				442.0,
				460.0,
				478.0,
				496.0,
				514.0,
				532.0,
				550.0,
				568.0,
				586.0,
				604.0,
				622.0,
				640.0,
				658.0,
				676.0,
				694.0,
				712.0,
				730.0,
				748.0,
				766.0,
				784.0,
				802.0,
				820.0,
				838.0,
				856.0,
				874.0,
				892.0,
				910.0,
				928.0,
				946.0,
				964.0,
				982.0,
				1000.0
				]
    interf_ljets_ge4j_3t_Evt_HT_tags.histotitle = "Evt_HT_tags"
    interf_ljets_ge4j_3t_Evt_HT_tags.histoname = "ljets_ge4j_3t_Evt_HT_tags"
    interf_ljets_ge4j_3t_Evt_HT_tags.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_HT_tags)
    
    interf_ljets_ge4j_3t_Evt_JetPt_over_JetE = vhi.variableHistoInterface(variable_name  = "Evt_JetPt_over_JetE",
                                            label          = "ljets_ge4j_3t_Evt_JetPt_over_JetE",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_JetPt_over_JetE.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_JetPt_over_JetE","")
    interf_ljets_ge4j_3t_Evt_JetPt_over_JetE.bin_edges = [ 
				0.22,
				0.24,
				0.26,
				0.28,
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
				0.82,
				0.84,
				0.86,
				0.88,
				0.9,
				0.92,
				0.94,
				0.96,
				0.98,
				1.0
				]
    interf_ljets_ge4j_3t_Evt_JetPt_over_JetE.histotitle = "Evt_JetPt_over_JetE"
    interf_ljets_ge4j_3t_Evt_JetPt_over_JetE.histoname = "ljets_ge4j_3t_Evt_JetPt_over_JetE"
    interf_ljets_ge4j_3t_Evt_JetPt_over_JetE.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_JetPt_over_JetE)
    
    interf_ljets_ge4j_3t_Evt_M2_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_M2_JetsAverage",
                                            label          = "ljets_ge4j_3t_Evt_M2_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_M2_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_M2_JetsAverage","")
    interf_ljets_ge4j_3t_Evt_M2_JetsAverage.bin_edges = [ 
				50.0,
				61.0,
				72.0,
				83.0,
				94.0,
				105.0,
				116.0,
				127.0,
				138.0,
				149.0,
				160.0,
				171.0,
				182.0,
				193.0,
				204.0,
				215.0,
				226.0,
				237.0,
				248.0,
				259.0,
				270.0,
				281.0,
				292.0,
				303.0,
				314.0,
				325.0,
				336.0,
				347.0,
				358.0,
				369.0,
				380.0,
				391.0,
				402.0,
				413.0,
				424.0,
				435.0,
				446.0,
				457.0,
				468.0,
				479.0,
				490.0,
				501.0,
				512.0,
				523.0,
				534.0,
				545.0,
				556.0,
				567.0,
				589.0,
				600.0
				]
    interf_ljets_ge4j_3t_Evt_M2_JetsAverage.histotitle = "Evt_M2_JetsAverage"
    interf_ljets_ge4j_3t_Evt_M2_JetsAverage.histoname = "ljets_ge4j_3t_Evt_M2_JetsAverage"
    interf_ljets_ge4j_3t_Evt_M2_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_M2_JetsAverage)
    
    interf_ljets_ge4j_3t_Evt_M_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_M_JetsAverage",
                                            label          = "ljets_ge4j_3t_Evt_M_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_M_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_M_JetsAverage","")
    interf_ljets_ge4j_3t_Evt_M_JetsAverage.bin_edges = [ 
				5.0,
				5.9,
				6.8,
				7.7,
				8.6,
				9.5,
				10.4,
				11.3,
				12.2,
				13.1,
				14.0,
				14.9,
				15.8,
				16.7,
				17.6,
				18.5,
				19.4,
				20.3,
				21.2,
				22.1,
				23.0,
				23.9,
				24.8,
				25.7,
				26.6,
				27.5,
				28.4,
				29.3,
				30.2,
				31.1,
				32.0,
				32.9,
				33.8,
				34.7,
				35.6,
				36.5,
				37.4,
				38.3,
				39.2,
				40.1,
				41.9,
				44.6,
				49.1,
				50.0
				]
    interf_ljets_ge4j_3t_Evt_M_JetsAverage.histotitle = "Evt_M_JetsAverage"
    interf_ljets_ge4j_3t_Evt_M_JetsAverage.histoname = "ljets_ge4j_3t_Evt_M_JetsAverage"
    interf_ljets_ge4j_3t_Evt_M_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_M_JetsAverage)
    
    interf_ljets_ge4j_3t_Evt_M_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_M_TaggedJetsAverage",
                                            label          = "ljets_ge4j_3t_Evt_M_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
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
    
    interf_ljets_ge4j_3t_Evt_M_Total = vhi.variableHistoInterface(variable_name  = "Evt_M_Total",
                                            label          = "ljets_ge4j_3t_Evt_M_Total",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_M_Total.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_M_Total","")
    interf_ljets_ge4j_3t_Evt_M_Total.bin_edges = [ 
				256.0,
				312.0,
				368.0,
				424.0,
				480.0,
				536.0,
				592.0,
				648.0,
				704.0,
				760.0,
				816.0,
				872.0,
				928.0,
				984.0,
				1040.0,
				1096.0,
				1152.0,
				1208.0,
				1264.0,
				1320.0,
				1376.0,
				1432.0,
				1488.0,
				1544.0,
				1600.0,
				1656.0,
				1712.0,
				1768.0,
				1824.0,
				1880.0,
				1936.0,
				1992.0,
				2048.0,
				2104.0,
				2160.0,
				2216.0,
				2272.0,
				2328.0,
				2384.0,
				2440.0,
				2496.0,
				2552.0,
				2608.0,
				2664.0,
				2720.0,
				2776.0,
				2832.0,
				2888.0,
				2944.0,
				3000.0
				]
    interf_ljets_ge4j_3t_Evt_M_Total.histotitle = "Evt_M_Total"
    interf_ljets_ge4j_3t_Evt_M_Total.histoname = "ljets_ge4j_3t_Evt_M_Total"
    interf_ljets_ge4j_3t_Evt_M_Total.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_M_Total)
    
    interf_ljets_ge4j_3t_Evt_Pt_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Pt_JetsAverage",
                                            label          = "ljets_ge4j_3t_Evt_Pt_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_Pt_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_Pt_JetsAverage","")
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
				396.6,
				434.2,
				500.0
				]
    interf_ljets_ge4j_3t_Evt_Pt_JetsAverage.histotitle = "Evt_Pt_JetsAverage"
    interf_ljets_ge4j_3t_Evt_Pt_JetsAverage.histoname = "ljets_ge4j_3t_Evt_Pt_JetsAverage"
    interf_ljets_ge4j_3t_Evt_Pt_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_Pt_JetsAverage)
    
    interf_ljets_ge4j_3t_Evt_Pt_minDrTaggedJets = vhi.variableHistoInterface(variable_name  = "Evt_Pt_minDrTaggedJets",
                                            label          = "ljets_ge4j_3t_Evt_Pt_minDrTaggedJets",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_Pt_minDrTaggedJets.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_Pt_minDrTaggedJets","")
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
    
    interf_ljets_ge4j_3t_Evt_blr_transformed = vhi.variableHistoInterface(variable_name  = "Evt_blr_transformed",
                                            label          = "ljets_ge4j_3t_Evt_blr_transformed",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
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
    
    interf_ljets_ge4j_3t_Evt_h1 = vhi.variableHistoInterface(variable_name  = "Evt_h1",
                                            label          = "ljets_ge4j_3t_Evt_h1",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_h1.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_h1","")
    interf_ljets_ge4j_3t_Evt_h1.bin_edges = [ 
				-0.2,
				-0.188,
				-0.176,
				-0.164,
				-0.152,
				-0.14,
				-0.128,
				-0.116,
				-0.104,
				-0.092,
				-0.08,
				-0.068,
				-0.056,
				-0.044,
				-0.032,
				-0.02,
				-0.008,
				0.004,
				0.016,
				0.028,
				0.04,
				0.052,
				0.064,
				0.076,
				0.088,
				0.1,
				0.112,
				0.124,
				0.136,
				0.148,
				0.16,
				0.172,
				0.184,
				0.196,
				0.208,
				0.22,
				0.232,
				0.244,
				0.256,
				0.268,
				0.28,
				0.292,
				0.304,
				0.316,
				0.328,
				0.34,
				0.4
				]
    interf_ljets_ge4j_3t_Evt_h1.histotitle = "Evt_h1"
    interf_ljets_ge4j_3t_Evt_h1.histoname = "ljets_ge4j_3t_Evt_h1"
    interf_ljets_ge4j_3t_Evt_h1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_h1)
    
    interf_ljets_ge4j_3t_N_Jets = vhi.variableHistoInterface(variable_name  = "N_Jets",
                                            label          = "ljets_ge4j_3t_N_Jets",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_N_Jets.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_N_Jets","")
    interf_ljets_ge4j_3t_N_Jets.bin_edges = [ 
				3.5,
				4.5,
				5.5,
				6.5,
				7.5,
				8.5,
				9.5,
				10.5
				]
    interf_ljets_ge4j_3t_N_Jets.histotitle = "N_Jets"
    interf_ljets_ge4j_3t_N_Jets.histoname = "ljets_ge4j_3t_N_Jets"
    interf_ljets_ge4j_3t_N_Jets.nhistobins = 7
    interfaces.append(interf_ljets_ge4j_3t_N_Jets)
    
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_btop = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_Jet_CSV_btop",
                                            label          = "ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_btop",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_btop.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_btop","")
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_btop.bin_edges = [ 
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
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_btop.histotitle = "Reco_JABDT_tHW_Jet_CSV_btop"
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_btop.histoname = "ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_btop"
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_btop.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_btop)
    
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_whaddau1 = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_Jet_CSV_whaddau1",
                                            label          = "ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_whaddau1",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_whaddau1.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_whaddau1","")
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_whaddau1.bin_edges = [ 
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
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_whaddau1.histotitle = "Reco_JABDT_tHW_Jet_CSV_whaddau1"
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_whaddau1.histoname = "ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_whaddau1"
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_whaddau1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_whaddau1)
    
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_top_m = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_log_top_m",
                                            label          = "ljets_ge4j_3t_Reco_JABDT_tHW_log_top_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_top_m.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_JABDT_tHW_log_top_m","")
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_top_m.bin_edges = [ 
				3.5,
				4.2,
				4.39,
				4.58,
				4.77,
				4.96,
				5.15,
				5.34,
				5.53,
				5.72,
				5.91,
				6.1,
				6.29,
				6.48,
				6.67,
				6.86,
				7.05,
				7.43,
				8.0
				]
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_top_m.histotitle = "Reco_JABDT_tHW_log_top_m"
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_top_m.histoname = "ljets_ge4j_3t_Reco_JABDT_tHW_log_top_m"
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_top_m.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_top_m)
    
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_log_wb_m = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_log_wb_m",
                                            label          = "ljets_ge4j_3t_Reco_JABDT_tHW_log_wb_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
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
    
    interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_ljet_pt = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHq_log_ljet_pt",
                                            label          = "ljets_ge4j_3t_Reco_JABDT_tHq_log_ljet_pt",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_ljet_pt.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_JABDT_tHq_log_ljet_pt","")
    interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_ljet_pt.bin_edges = [ 
				3.36,
				3.45,
				3.54,
				3.63,
				3.72,
				3.81,
				3.9,
				3.99,
				4.08,
				4.17,
				4.26,
				4.35,
				4.44,
				4.53,
				4.62,
				4.71,
				4.8,
				4.89,
				4.98,
				5.07,
				5.16,
				5.25,
				5.34,
				5.43,
				5.52,
				5.61,
				5.7,
				5.79,
				5.88,
				5.97,
				6.06,
				6.15,
				6.24,
				6.33,
				6.42,
				6.51,
				6.6,
				6.78,
				7.5
				]
    interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_ljet_pt.histotitle = "Reco_JABDT_tHq_log_ljet_pt"
    interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_ljet_pt.histoname = "ljets_ge4j_3t_Reco_JABDT_tHq_log_ljet_pt"
    interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_ljet_pt.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_JABDT_tHq_log_ljet_pt)
    
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_btoplep = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttH_Jet_CSV_btoplep",
                                            label          = "ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_btoplep",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
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
    
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_hdau2 = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttH_Jet_CSV_hdau2",
                                            label          = "ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_hdau2",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_hdau2.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_hdau2","")
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_hdau2.bin_edges = [ 
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
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_hdau2.histotitle = "Reco_JABDT_ttH_Jet_CSV_hdau2"
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_hdau2.histoname = "ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_hdau2"
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_hdau2.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_hdau2)
    
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_btophad = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttbar_Jet_CSV_btophad",
                                            label          = "ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_btophad",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_btophad.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_btophad","")
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_btophad.bin_edges = [ 
				0.0,
				0.04,
				0.08,
				0.12,
				0.16,
				0.22,
				0.26,
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
				0.82,
				0.84,
				0.86,
				0.88,
				0.9,
				0.92,
				0.94,
				0.96,
				0.98,
				1.0
				]
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_btophad.histotitle = "Reco_JABDT_ttbar_Jet_CSV_btophad"
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_btophad.histoname = "ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_btophad"
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_btophad.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_btophad)
    
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_btoplep = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttbar_Jet_CSV_btoplep",
                                            label          = "ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_btoplep",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_btoplep.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_btoplep","")
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_btoplep.bin_edges = [ 
				0.0,
				0.02,
				0.04,
				0.06,
				0.08,
				0.1,
				0.12,
				0.16,
				0.2,
				0.24,
				0.28,
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
				0.82,
				0.84,
				0.86,
				0.88,
				0.9,
				0.92,
				0.94,
				0.96,
				0.98,
				1.0
				]
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_btoplep.histotitle = "Reco_JABDT_ttbar_Jet_CSV_btoplep"
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_btoplep.histoname = "ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_btoplep"
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_btoplep.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_btoplep)
    
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_whaddau1 = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttbar_Jet_CSV_whaddau1",
                                            label          = "ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_whaddau1",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_whaddau1.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_whaddau1","")
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_whaddau1.bin_edges = [ 
				0.0,
				0.02,
				0.04,
				0.06,
				0.08,
				0.1,
				0.12,
				0.14,
				0.16,
				0.18,
				0.2,
				0.22,
				0.24,
				0.26,
				0.28,
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
				0.82,
				0.84,
				0.86,
				0.88,
				0.9,
				0.92,
				0.94,
				0.96,
				0.98,
				1.0
				]
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_whaddau1.histotitle = "Reco_JABDT_ttbar_Jet_CSV_whaddau1"
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_whaddau1.histoname = "ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_whaddau1"
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_whaddau1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_whaddau1)
    
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_whaddau2 = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttbar_Jet_CSV_whaddau2",
                                            label          = "ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_whaddau2",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_whaddau2.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_whaddau2","")
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_whaddau2.bin_edges = [ 
				0.0,
				0.02,
				0.04,
				0.06,
				0.08,
				0.1,
				0.12,
				0.14,
				0.16,
				0.18,
				0.2,
				0.22,
				0.24,
				0.26,
				0.28,
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
				0.82,
				0.84,
				0.86,
				0.88,
				0.9,
				0.92,
				0.94,
				0.96,
				0.98,
				1.0
				]
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_whaddau2.histotitle = "Reco_JABDT_ttbar_Jet_CSV_whaddau2"
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_whaddau2.histoname = "ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_whaddau2"
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_whaddau2.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_whaddau2)
    
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_log_tophad_m = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttbar_log_tophad_m",
                                            label          = "ljets_ge4j_3t_Reco_JABDT_ttbar_log_tophad_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_log_tophad_m.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_JABDT_ttbar_log_tophad_m","")
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_log_tophad_m.bin_edges = [ 
				4.08,
				4.24,
				4.32,
				4.4,
				4.48,
				4.56,
				4.64,
				4.72,
				4.8,
				4.88,
				4.96,
				5.04,
				5.12,
				5.2,
				5.28,
				5.36,
				5.44,
				5.52,
				5.6,
				5.68,
				5.76,
				5.84,
				5.92,
				6.0,
				6.08,
				6.16,
				6.24,
				6.32,
				6.4,
				6.48,
				6.56,
				6.64,
				6.72,
				6.8,
				6.88,
				6.96,
				7.04,
				7.12,
				7.2,
				7.28,
				7.36,
				7.52,
				7.68,
				8.0
				]
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_log_tophad_m.histotitle = "Reco_JABDT_ttbar_log_tophad_m"
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_log_tophad_m.histoname = "ljets_ge4j_3t_Reco_JABDT_ttbar_log_tophad_m"
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_log_tophad_m.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_JABDT_ttbar_log_tophad_m)
    
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_log_whad_m = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttbar_log_whad_m",
                                            label          = "ljets_ge4j_3t_Reco_JABDT_ttbar_log_whad_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_log_whad_m.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_JABDT_ttbar_log_whad_m","")
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_log_whad_m.bin_edges = [ 
				3.0,
				3.1,
				3.2,
				3.3,
				3.4,
				3.5,
				3.6,
				3.7,
				3.8,
				3.9,
				4.0,
				4.1,
				4.2,
				4.3,
				4.4,
				4.5,
				4.6,
				4.7,
				4.8,
				4.9,
				5.0,
				5.1,
				5.2,
				5.3,
				5.4,
				5.5,
				5.6,
				5.7,
				5.8,
				5.9,
				6.0,
				6.1,
				6.2,
				6.3,
				6.4,
				6.5,
				6.6,
				6.7,
				6.8,
				6.9,
				7.0,
				7.1,
				7.2,
				7.4,
				8.0
				]
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_log_whad_m.histotitle = "Reco_JABDT_ttbar_log_whad_m"
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_log_whad_m.histoname = "ljets_ge4j_3t_Reco_JABDT_ttbar_log_whad_m"
    interf_ljets_ge4j_3t_Reco_JABDT_ttbar_log_whad_m.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_JABDT_ttbar_log_whad_m)
    
    interf_ljets_ge4j_3t_Reco_tHW_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_tHW_bestJABDToutput",
                                            label          = "ljets_ge4j_3t_Reco_tHW_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_tHW_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_tHW_bestJABDToutput","")
    interf_ljets_ge4j_3t_Reco_tHW_bestJABDToutput.bin_edges = [ 
				-0.8,
				-0.6,
				-0.328,
				-0.296,
				-0.264,
				-0.232,
				-0.2,
				-0.168,
				-0.136,
				-0.104,
				-0.072,
				-0.04,
				-0.008,
				0.024,
				0.056,
				0.088,
				0.12,
				0.152,
				0.184,
				0.216,
				0.248,
				0.28,
				0.312,
				0.344,
				0.376,
				0.408,
				0.44,
				0.472,
				0.504,
				0.6
				]
    interf_ljets_ge4j_3t_Reco_tHW_bestJABDToutput.histotitle = "Reco_tHW_bestJABDToutput"
    interf_ljets_ge4j_3t_Reco_tHW_bestJABDToutput.histoname = "ljets_ge4j_3t_Reco_tHW_bestJABDToutput"
    interf_ljets_ge4j_3t_Reco_tHW_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_tHW_bestJABDToutput)
    
    interf_ljets_ge4j_3t_Reco_tHW_whad_dr = vhi.variableHistoInterface(variable_name  = "Reco_tHW_whad_dr",
                                            label          = "ljets_ge4j_3t_Reco_tHW_whad_dr",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_tHW_whad_dr.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_tHW_whad_dr","")
    interf_ljets_ge4j_3t_Reco_tHW_whad_dr.bin_edges = [ 
				0.25,
				0.32,
				0.45,
				0.58,
				0.71,
				0.84,
				0.97,
				1.1,
				1.23,
				1.36,
				1.49,
				1.62,
				1.75,
				1.88,
				2.01,
				2.14,
				2.27,
				2.4,
				2.53,
				2.66,
				2.79,
				2.92,
				3.05,
				3.18,
				3.31,
				3.44,
				3.57,
				3.7,
				3.83,
				3.96,
				4.09,
				4.22,
				4.35,
				4.48,
				4.61,
				4.74,
				4.87,
				5.0
				]
    interf_ljets_ge4j_3t_Reco_tHW_whad_dr.histotitle = "Reco_tHW_whad_dr"
    interf_ljets_ge4j_3t_Reco_tHW_whad_dr.histoname = "ljets_ge4j_3t_Reco_tHW_whad_dr"
    interf_ljets_ge4j_3t_Reco_tHW_whad_dr.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_tHW_whad_dr)
    
    interf_ljets_ge4j_3t_Reco_tHq_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_tHq_bestJABDToutput",
                                            label          = "ljets_ge4j_3t_Reco_tHq_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
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
    
    interf_ljets_ge4j_3t_Reco_tHq_ljet_m = vhi.variableHistoInterface(variable_name  = "Reco_tHq_ljet_m",
                                            label          = "ljets_ge4j_3t_Reco_tHq_ljet_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_tHq_ljet_m.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_tHq_ljet_m","")
    interf_ljets_ge4j_3t_Reco_tHq_ljet_m.bin_edges = [ 
				10.0,
				11.3,
				12.6,
				13.9,
				15.2,
				16.5,
				17.8,
				19.1,
				20.4,
				21.7,
				23.0,
				24.3,
				25.6,
				26.9,
				28.2,
				29.5,
				30.8,
				32.1,
				33.4,
				34.7,
				36.0,
				37.3,
				38.6,
				39.9,
				41.2,
				42.5,
				43.8,
				45.1,
				46.4,
				47.7,
				49.0,
				50.3,
				51.6,
				52.9,
				54.2,
				55.5,
				56.8,
				58.1,
				59.4,
				60.7,
				63.3,
				65.9,
				68.5,
				71.1,
				73.7,
				75.0
				]
    interf_ljets_ge4j_3t_Reco_tHq_ljet_m.histotitle = "Reco_tHq_ljet_m"
    interf_ljets_ge4j_3t_Reco_tHq_ljet_m.histoname = "ljets_ge4j_3t_Reco_tHq_ljet_m"
    interf_ljets_ge4j_3t_Reco_tHq_ljet_m.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_tHq_ljet_m)
    
    interf_ljets_ge4j_3t_Reco_ttH_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_ttH_bestJABDToutput",
                                            label          = "ljets_ge4j_3t_Reco_ttH_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_ttH_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_ttH_bestJABDToutput","")
    interf_ljets_ge4j_3t_Reco_ttH_bestJABDToutput.bin_edges = [ 
				-0.8,
				-0.7,
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
				0.7
				]
    interf_ljets_ge4j_3t_Reco_ttH_bestJABDToutput.histotitle = "Reco_ttH_bestJABDToutput"
    interf_ljets_ge4j_3t_Reco_ttH_bestJABDToutput.histoname = "ljets_ge4j_3t_Reco_ttH_bestJABDToutput"
    interf_ljets_ge4j_3t_Reco_ttH_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_ttH_bestJABDToutput)
    
    interf_ljets_ge4j_3t_Reco_ttbar_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_ttbar_bestJABDToutput",
                                            label          = "ljets_ge4j_3t_Reco_ttbar_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_ttbar_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_ttbar_bestJABDToutput","")
    interf_ljets_ge4j_3t_Reco_ttbar_bestJABDToutput.bin_edges = [ 
				-0.4,
				-0.378,
				-0.356,
				-0.334,
				-0.312,
				-0.29,
				-0.268,
				-0.246,
				-0.224,
				-0.202,
				-0.18,
				-0.158,
				-0.136,
				-0.114,
				-0.092,
				-0.07,
				-0.048,
				-0.026,
				-0.004,
				0.018,
				0.04,
				0.062,
				0.084,
				0.106,
				0.128,
				0.15,
				0.172,
				0.194,
				0.216,
				0.238,
				0.26,
				0.282,
				0.304,
				0.326,
				0.348,
				0.37,
				0.392,
				0.414,
				0.436,
				0.458,
				0.48,
				0.502,
				0.524,
				0.546,
				0.568,
				0.59,
				0.612,
				0.7
				]
    interf_ljets_ge4j_3t_Reco_ttbar_bestJABDToutput.histotitle = "Reco_ttbar_bestJABDToutput"
    interf_ljets_ge4j_3t_Reco_ttbar_bestJABDToutput.histoname = "ljets_ge4j_3t_Reco_ttbar_bestJABDToutput"
    interf_ljets_ge4j_3t_Reco_ttbar_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_ttbar_bestJABDToutput)
    
    interf_ljets_ge4j_3t_Reco_ttbar_toplep_m = vhi.variableHistoInterface(variable_name  = "Reco_ttbar_toplep_m",
                                            label          = "ljets_ge4j_3t_Reco_ttbar_toplep_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
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
    
    plots = init_plots(interfaces = interfaces)    
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    
def plots_dnn(data, discrname):

    ndefaultbins = 30
    interfaces = []


    # plots for ljets_ge4j_ge4t

    interf_ljets_ljets_ge4j_ge4t_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ljets_ge4j_ge4t_node_ttH",
                                            label          = "ljets_ljets_ge4j_ge4t_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ljets_ge4j_ge4t==0))")
    interf_ljets_ljets_ge4j_ge4t_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ljets_ge4j_ge4t==0))","ljets_ljets_ge4j_ge4t_ttH_node","")
    interf_ljets_ljets_ge4j_ge4t_ttH_node.minxval = 0.14
    interf_ljets_ljets_ge4j_ge4t_ttH_node.maxxval = 0.78
    interf_ljets_ljets_ge4j_ge4t_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ljets_ge4j_ge4t_ttH_node)
    
    interf_ljets_ljets_ge4j_ge4t_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ljets_ge4j_ge4t_node_ttmb",
                                            label          = "ljets_ljets_ge4j_ge4t_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ljets_ge4j_ge4t==1))")
    interf_ljets_ljets_ge4j_ge4t_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ljets_ge4j_ge4t==1))","ljets_ljets_ge4j_ge4t_ttmb_node","")
    interf_ljets_ljets_ge4j_ge4t_ttmb_node.minxval = 0.14
    interf_ljets_ljets_ge4j_ge4t_ttmb_node.maxxval = 0.39
    interf_ljets_ljets_ge4j_ge4t_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ljets_ge4j_ge4t_ttmb_node)
    
    interf_ljets_ljets_ge4j_ge4t_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ljets_ge4j_ge4t_node_tt2b",
                                            label          = "ljets_ljets_ge4j_ge4t_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ljets_ge4j_ge4t==2))")
    interf_ljets_ljets_ge4j_ge4t_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ljets_ge4j_ge4t==2))","ljets_ljets_ge4j_ge4t_tt2b_node","")
    interf_ljets_ljets_ge4j_ge4t_tt2b_node.minxval = 0.14
    interf_ljets_ljets_ge4j_ge4t_tt2b_node.maxxval = 0.41
    interf_ljets_ljets_ge4j_ge4t_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ljets_ge4j_ge4t_tt2b_node)
    
    interf_ljets_ljets_ge4j_ge4t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ljets_ge4j_ge4t_node_ttcc",
                                            label          = "ljets_ljets_ge4j_ge4t_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ljets_ge4j_ge4t==3))")
    interf_ljets_ljets_ge4j_ge4t_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ljets_ge4j_ge4t==3))","ljets_ljets_ge4j_ge4t_ttcc_node","")
    interf_ljets_ljets_ge4j_ge4t_ttcc_node.minxval = 0.14
    interf_ljets_ljets_ge4j_ge4t_ttcc_node.maxxval = 0.51
    interf_ljets_ljets_ge4j_ge4t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ljets_ge4j_ge4t_ttcc_node)
    
    interf_ljets_ljets_ge4j_ge4t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ljets_ge4j_ge4t_node_ttlf",
                                            label          = "ljets_ljets_ge4j_ge4t_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ljets_ge4j_ge4t==4))")
    interf_ljets_ljets_ge4j_ge4t_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ljets_ge4j_ge4t==4))","ljets_ljets_ge4j_ge4t_ttlf_node","")
    interf_ljets_ljets_ge4j_ge4t_ttlf_node.minxval = 0.14
    interf_ljets_ljets_ge4j_ge4t_ttlf_node.maxxval = 0.52
    interf_ljets_ljets_ge4j_ge4t_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ljets_ge4j_ge4t_ttlf_node)
    
    interf_ljets_ljets_ge4j_ge4t_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ljets_ge4j_ge4t_node_tHq",
                                            label          = "ljets_ljets_ge4j_ge4t_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ljets_ge4j_ge4t==5))")
    interf_ljets_ljets_ge4j_ge4t_tHq_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ljets_ge4j_ge4t==5))","ljets_ljets_ge4j_ge4t_tHq_node","")
    interf_ljets_ljets_ge4j_ge4t_tHq_node.minxval = 0.14
    interf_ljets_ljets_ge4j_ge4t_tHq_node.maxxval = 1.0
    interf_ljets_ljets_ge4j_ge4t_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ljets_ge4j_ge4t_tHq_node)
    
    interf_ljets_ljets_ge4j_ge4t_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ljets_ge4j_ge4t_node_tHW",
                                            label          = "ljets_ljets_ge4j_ge4t_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ljets_ge4j_ge4t==6))")
    interf_ljets_ljets_ge4j_ge4t_tHW_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ljets_ge4j_ge4t==6))","ljets_ljets_ge4j_ge4t_tHW_node","")
    interf_ljets_ljets_ge4j_ge4t_tHW_node.minxval = 0.14
    interf_ljets_ljets_ge4j_ge4t_tHW_node.maxxval = 1.0
    interf_ljets_ljets_ge4j_ge4t_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ljets_ge4j_ge4t_tHW_node)
    


    # plots for ljets_ge4j_3t

    interf_ljets_ljets_ge4j_3t_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ljets_ge4j_3t_node_ttH",
                                            label          = "ljets_ljets_ge4j_3t_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ljets_ge4j_3t==0))")
    interf_ljets_ljets_ge4j_3t_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ljets_ge4j_3t==0))","ljets_ljets_ge4j_3t_ttH_node","")
    interf_ljets_ljets_ge4j_3t_ttH_node.minxval = 0.14
    interf_ljets_ljets_ge4j_3t_ttH_node.maxxval = 0.6
    interf_ljets_ljets_ge4j_3t_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ljets_ge4j_3t_ttH_node)
    
    interf_ljets_ljets_ge4j_3t_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ljets_ge4j_3t_node_ttmb",
                                            label          = "ljets_ljets_ge4j_3t_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ljets_ge4j_3t==1))")
    interf_ljets_ljets_ge4j_3t_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ljets_ge4j_3t==1))","ljets_ljets_ge4j_3t_ttmb_node","")
    interf_ljets_ljets_ge4j_3t_ttmb_node.minxval = 0.14
    interf_ljets_ljets_ge4j_3t_ttmb_node.maxxval = 0.36
    interf_ljets_ljets_ge4j_3t_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ljets_ge4j_3t_ttmb_node)
    
    interf_ljets_ljets_ge4j_3t_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ljets_ge4j_3t_node_tt2b",
                                            label          = "ljets_ljets_ge4j_3t_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ljets_ge4j_3t==2))")
    interf_ljets_ljets_ge4j_3t_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ljets_ge4j_3t==2))","ljets_ljets_ge4j_3t_tt2b_node","")
    interf_ljets_ljets_ge4j_3t_tt2b_node.minxval = 0.14
    interf_ljets_ljets_ge4j_3t_tt2b_node.maxxval = 0.87
    interf_ljets_ljets_ge4j_3t_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ljets_ge4j_3t_tt2b_node)
    
    interf_ljets_ljets_ge4j_3t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ljets_ge4j_3t_node_ttcc",
                                            label          = "ljets_ljets_ge4j_3t_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ljets_ge4j_3t==3))")
    interf_ljets_ljets_ge4j_3t_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ljets_ge4j_3t==3))","ljets_ljets_ge4j_3t_ttcc_node","")
    interf_ljets_ljets_ge4j_3t_ttcc_node.minxval = 0.14
    interf_ljets_ljets_ge4j_3t_ttcc_node.maxxval = 0.42
    interf_ljets_ljets_ge4j_3t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ljets_ge4j_3t_ttcc_node)
    
    interf_ljets_ljets_ge4j_3t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ljets_ge4j_3t_node_ttlf",
                                            label          = "ljets_ljets_ge4j_3t_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ljets_ge4j_3t==4))")
    interf_ljets_ljets_ge4j_3t_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ljets_ge4j_3t==4))","ljets_ljets_ge4j_3t_ttlf_node","")
    interf_ljets_ljets_ge4j_3t_ttlf_node.minxval = 0.14
    interf_ljets_ljets_ge4j_3t_ttlf_node.maxxval = 0.69
    interf_ljets_ljets_ge4j_3t_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ljets_ge4j_3t_ttlf_node)
    
    interf_ljets_ljets_ge4j_3t_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ljets_ge4j_3t_node_tHq",
                                            label          = "ljets_ljets_ge4j_3t_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ljets_ge4j_3t==5))")
    interf_ljets_ljets_ge4j_3t_tHq_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ljets_ge4j_3t==5))","ljets_ljets_ge4j_3t_tHq_node","")
    interf_ljets_ljets_ge4j_3t_tHq_node.minxval = 0.14
    interf_ljets_ljets_ge4j_3t_tHq_node.maxxval = 0.99
    interf_ljets_ljets_ge4j_3t_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ljets_ge4j_3t_tHq_node)
    
    interf_ljets_ljets_ge4j_3t_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ljets_ge4j_3t_node_tHW",
                                            label          = "ljets_ljets_ge4j_3t_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ljets_ge4j_3t==6))")
    interf_ljets_ljets_ge4j_3t_tHW_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ljets_ge4j_3t==6))","ljets_ljets_ge4j_3t_tHW_node","")
    interf_ljets_ljets_ge4j_3t_tHW_node.minxval = 0.14
    interf_ljets_ljets_ge4j_3t_tHW_node.maxxval = 1.0
    interf_ljets_ljets_ge4j_3t_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ljets_ge4j_3t_tHW_node)
    

    for interf in interfaces:
        l = interf.label
        interf.histoname = discrname+"_"+l
        interf.histotitle = "final discriminator ({})".format(l)
        interf.selection = interf.category[0]

    DNNPlots = init_plots(interfaces = interfaces, data = data)
    return DNNPlots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_ljets_ge4j_ge4t(data)
    discriminatorPlots += plots_ljets_ge4j_3t(data)
    # discriminatorPlots += plots_dnn(data, discrname)

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
    