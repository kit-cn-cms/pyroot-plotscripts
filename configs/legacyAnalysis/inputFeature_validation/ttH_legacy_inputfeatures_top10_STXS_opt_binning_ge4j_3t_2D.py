
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

def interfaces_STXS_ljets_ge4j_3t():
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

    interf_ljets_ge4j_3t_Evt_HT_jets = vhi.variableHistoInterface(variable_name  = "Evt_HT_jets",
                                            label          = "ljets_ge4j_3t_Evt_HT_jets",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_HT_jets.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_HT_jets","")
    interf_ljets_ge4j_3t_Evt_HT_jets.category_label = label
    interf_ljets_ge4j_3t_Evt_HT_jets.bin_edges = [ 
                150.0,
                181.0,
                212.0,
                243.0,
                274.0,
                305.0,
                336.0,
                367.0,
                398.0,
                429.0,
                460.0,
                491.0,
                522.0,
                553.0,
                584.0,
                615.0,
                646.0,
                677.0,
                708.0,
                739.0,
                770.0,
                801.0,
                832.0,
                863.0,
                894.0,
                925.0,
                956.0,
                987.0,
                1018.0,
                1049.0,
                1080.0,
                1111.0,
                1142.0,
                1173.0,
                1204.0,
                1235.0,
                1266.0,
                1297.0,
                1328.0,
                1359.0,
                1390.0,
                1421.0,
                1452.0,
                1483.0,
                1514.0,
                1545.0,
                1576.0,
                1607.0,
                1638.0,
                1669.0,
                1700.0
                ]
    interf_ljets_ge4j_3t_Evt_HT_jets.histotitle = "H_{T}(jets)"
    interf_ljets_ge4j_3t_Evt_HT_jets.histoname = "ljets_ge4j_3t_Evt_HT_jets"
    interf_ljets_ge4j_3t_Evt_HT_jets.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_HT_jets)
    
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

    # overlapp with classifier

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
                964.0,
                982.0,
                1000.0
                ]
    interf_ljets_ge4j_3t_Evt_HT_tags.histotitle = "Evt_HT_tags"
    interf_ljets_ge4j_3t_Evt_HT_tags.histoname = "ljets_ge4j_3t_Evt_HT_tags"
    interf_ljets_ge4j_3t_Evt_HT_tags.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_HT_tags)

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
                406.0,
                443.6,
                500.0
                ]
    interf_ljets_ge4j_3t_Evt_Pt_JetsAverage.histotitle = "Evt_Pt_JetsAverage"
    interf_ljets_ge4j_3t_Evt_Pt_JetsAverage.histoname = "ljets_ge4j_3t_Evt_Pt_JetsAverage"
    interf_ljets_ge4j_3t_Evt_Pt_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_Pt_JetsAverage)

    interf_ljets_ge4j_3t_Reco_tHW_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_tHW_bestJABDToutput",
                                            label          = "ljets_ge4j_3t_Reco_tHW_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_tHW_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_tHW_bestJABDToutput","")
    interf_ljets_ge4j_3t_Reco_tHW_bestJABDToutput.bin_edges = [ 
                -1.0,
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
                46.6,
                47.9,
                50.5,
                53.1,
                57.0,
                60.9,
                68.7,
                70.0
                ]
    interf_ljets_ge4j_3t_Evt_M_TaggedJetsAverage.histotitle = "Evt_M_TaggedJetsAverage"
    interf_ljets_ge4j_3t_Evt_M_TaggedJetsAverage.histoname = "ljets_ge4j_3t_Evt_M_TaggedJetsAverage"
    interf_ljets_ge4j_3t_Evt_M_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_M_TaggedJetsAverage)

    return interfaces

def plots_STXS_ljets_ge4j_3t(data = None):
    label = "\geq 4 jets, 3 b-tags"
    # STXS variables
    interfaces = interfaces_STXS_ljets_ge4j_3t()
    plots = init_plots_2D(interfaces = interfaces)
    if data:
        add_data_plots(plots = plots, data = data)
    return plots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    
    discriminatorPlots += plots_STXS_ljets_ge4j_3t(data)

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
    