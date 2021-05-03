
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
import numpy as np

memexp = '(memDBp>=0.0)*(memDBp)+(memDBp<0.0)*(0.01)+(memDBp==1.0)*(0.01)'

def interfaces_STXS_ljets_ge4j_ge4t():
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
    
    interf_ljets_ge4j_ge4t_Reco_tHq_h_dr = vhi.variableHistoInterface(variable_name  = "Reco_tHq_h_dr",
                                            label          = "ljets_ge4j_ge4t_Reco_tHq_h_dr",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_tHq_h_dr.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_tHq_h_dr","")
    interf_ljets_ge4j_ge4t_Reco_tHq_h_dr.category_label = label
    interf_ljets_ge4j_ge4t_Reco_tHq_h_dr.bin_edges = [ 
                0.0,
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
                5.0
                ]
    interf_ljets_ge4j_ge4t_Reco_tHq_h_dr.histotitle = "Reco_tHq_h_dr"
    interf_ljets_ge4j_ge4t_Reco_tHq_h_dr.histoname = "ljets_ge4j_ge4t_Reco_tHq_h_dr"
    interf_ljets_ge4j_ge4t_Reco_tHq_h_dr.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_tHq_h_dr)
    
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

    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_m = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttH_log_toplep_m",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_m.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_m","")
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

    return interfaces


def plots_STXS_ljets_ge4j_ge4t(data = None):
    label = "\geq 4 jets, \geq 4 b-tags"
    # STXS variables
    interfaces = interfaces_STXS_ljets_ge4j_ge4t()

    for i in interfaces:
        i.category_label = label
    plots = init_plots_2D(interfaces = interfaces)
    if data:
        add_data_plots(plots = plots, data = data)
    return plots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_STXS_ljets_ge4j_ge4t(data)

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

def init_plots_2D(interfaces):
    plots = [] #init list of plotClasses objects to return
    dictionary = {}
    for i, interf in enumerate(interfaces):
        for interf2 in interfaces[i+1:]:
            binsX = None
            nbinsX = None
            xmin = None
            xmax = None
            binsY = None
            nbinsY = None
            ymin = None
            ymax = None
            
            # check if initialization uses bin edges or min/max vals
            # if 'subdict' contains the keyword 'bin_edges', an array
            # of type float is created from the corresponding python list.
            # Else, the min/maxvals are used 
            if not interf.bin_edges is None:
                binsX  = array("f", interf.bin_edges)
                nbinsX = len(binsX)-1 # last bin edge in array is overflow bin => subtract for nbins
                interf.nhistobins = nbinsX # update number of bins

            elif not (interf.minxval is None or interf.maxxval is None):
                nbinsX = interf.nhistobins
                xmax  = interf.maxxval
                xmin  = interf.minxval
            
            if not interf2.bin_edges is None:
                binsY  = array("f", interf2.bin_edges)
                nbinsY = len(binsY)-1 # last bin edge in array is overflow bin => subtract for nbins
                interf2.nhistobins = nbinsY # update number of bins
            elif not (interf2.minxval is None or interf2.maxxval is None):
                nbinsY = interf2.nhistobins
                ymax  = interf2.maxxval
                ymin  = interf2.minxval

            hname_2D = "{}_{}".format(interf.histoname, interf2.histoname)
            htitle_2D = "{}_{}".format(interf.histotitle, interf2.histotitle)
            if not binsX is None:
                if not binsY is None:
                    plots.append(
                            plotClasses.TwoDimPlot( histo = ROOT.TH2F(hname_2D,htitle_2D,nbinsX,binsX, nbinsY,binsY),
                                variable1 = interf.varname,
                                variable2 = interf2.varname,
                                selection = interf.selection,
                                label = interf.category_label))
                else: 
                    plots.append(
                            plotClasses.TwoDimPlot( histo = ROOT.TH2F(hname_2D,htitle_2D,nbinsX,binsX, nbinsY,ymin, ymax),
                                variable1 = interf.varname,
                                variable2 = interf2.varname,
                                selection = interf.selection,
                                label = interf.category_label))
            elif not (xmin is None or xmax is None):
                if not binsY is None:
                    plots.append(
                            plotClasses.TwoDimPlot( histo = ROOT.TH2F(hname_2D,htitle_2D,nbinsX,xmin, xmax, nbinsY,binsY),
                                variable1 = interf.varname,
                                variable2 = interf2.varname,
                                selection = interf.selection,
                                label = interf.category_label))
                else: 
                    plots.append(
                            plotClasses.TwoDimPlot( histo = ROOT.TH2F(hname_2D,htitle_2D,nbinsX,xmin, xmax, nbinsY,ymin, ymax),
                                variable1 = interf.varname,
                                variable2 = interf2.varname,
                                selection = interf.selection,
                                label = interf.category_label))
            else:
                s = "FATAL ERROR: Unable to load bin edges or min/max values for histogram!\n"
                s += "interface 1:\n{}".format(interf)
                s += "interface 2:\n{}".format(interf2)
                raise ValueError(s)

    return plots

def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
    