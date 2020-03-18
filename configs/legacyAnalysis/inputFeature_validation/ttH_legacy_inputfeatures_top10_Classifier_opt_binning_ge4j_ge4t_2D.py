
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

def plots_ljets_ge4j_ge4t(data = None):

    label = "\geq 4 jets, \geq 4 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"

    # ==============================save zone ===========================================

    if not memexp == "":
        interf_ljets_ge4j_ge4t_memDBp = vhi.variableHistoInterface(variable_name  = memexp,
                                                label          = "ljets_ge4j_ge4t_memDBp",
                                                selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
        interf_ljets_ge4j_ge4t_memDBp.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ge4j_ge4t_memDBp","")
        interf_ljets_ge4j_ge4t_memDBp.category_label = label
        interf_ljets_ge4j_ge4t_memDBp.bin_edges = [ 
                    0.0,
                    0.0333,
                    0.0667,
                    0.1,
                    0.1333,
                    0.1667,
                    0.2,
                    0.2333,
                    0.2667,
                    0.3,
                    0.3333,
                    0.3667,
                    0.4,
                    0.4333,
                    0.4667,
                    0.5,
                    0.5333,
                    0.5667,
                    0.6,
                    0.6333,
                    0.6667,
                    0.7,
                    0.7333,
                    0.7667,
                    0.8,
                    0.8333,
                    0.8667,
                    0.9,
                    0.9333,
                    0.9667,
                    1.0
                    ]
        interf_ljets_ge4j_ge4t_memDBp.histotitle = "MEM"
        interf_ljets_ge4j_ge4t_memDBp.histoname = "ljets_ge4j_ge4t_memDBp"
        interf_ljets_ge4j_ge4t_memDBp.nhistobins = 30
        interfaces.append(interf_ljets_ge4j_ge4t_memDBp)

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

    interf_ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Deta_TaggedJetsAverage",
                                            label          = "ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage","")
    interf_ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage.bin_edges = [ 
                0.06,
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
                2.46,
                3.0
                ]
    interf_ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage.histotitle = "Evt_Deta_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage.histoname = "ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage)

    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1 = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHq_Jet_CSV_hdau1",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1.bin_edges = [ 
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
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1.histotitle = "Reco_JABDT_tHq_Jet_CSV_hdau1"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1.histoname = "ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1)

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
    interf_ljets_ge4j_ge4t_CSV_2.histotitle = "CSV[2]"
    interf_ljets_ge4j_ge4t_CSV_2.histoname = "ljets_ge4j_ge4t_CSV_2"
    interf_ljets_ge4j_ge4t_CSV_2.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_CSV_2)

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

    interf_ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_ttbar_bestJABDToutput",
                                            label          = "ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput","")
    interf_ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput.bin_edges = [ 
                -0.29,
                -0.246,
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
                0.7
                ]
    interf_ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput.histotitle = "Reco_ttbar_bestJABDToutput"
    interf_ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput.histoname = "ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput"
    interf_ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput)

    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_Jet_CSV_btop",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.bin_edges = [ 
                -0.5,
                0.0,
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

    interf_ljets_ge4j_ge4t_Reco_tHW_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_tHW_bestJABDToutput",
                                            label          = "ljets_ge4j_ge4t_Reco_tHW_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_tHW_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_tHW_bestJABDToutput","")
    interf_ljets_ge4j_ge4t_Reco_tHW_bestJABDToutput.bin_edges = [ 
                -1.0,
                -0.5,
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
    interf_ljets_ge4j_ge4t_Reco_tHW_bestJABDToutput.histotitle = "Reco_tHW_bestJABDToutput"
    interf_ljets_ge4j_ge4t_Reco_tHW_bestJABDToutput.histoname = "ljets_ge4j_ge4t_Reco_tHW_bestJABDToutput"
    interf_ljets_ge4j_ge4t_Reco_tHW_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_tHW_bestJABDToutput)

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

    interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_tHq_bestJABDToutput",
                                            label          = "ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput","")
    interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput.bin_edges = [ 
                -1.0,
                -0.6,
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
                0.7
                ]
    interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput.histotitle = "Reco_tHq_bestJABDToutput"
    interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput.histoname = "ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput"
    interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput)

    interf_ljets_ge4j_ge4t_Reco_ttbar_toplep_m = vhi.variableHistoInterface(variable_name  = "Reco_ttbar_toplep_m",
                                            label          = "ljets_ge4j_ge4t_Reco_ttbar_toplep_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_ttbar_toplep_m.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_ttbar_toplep_m","")
    interf_ljets_ge4j_ge4t_Reco_ttbar_toplep_m.bin_edges = [ 
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
                458.0,
                474.8,
                491.6,
                500.0
                ]
    interf_ljets_ge4j_ge4t_Reco_ttbar_toplep_m.histotitle = "Reco_ttbar_toplep_m"
    interf_ljets_ge4j_ge4t_Reco_ttbar_toplep_m.histoname = "ljets_ge4j_ge4t_Reco_ttbar_toplep_m"
    interf_ljets_ge4j_ge4t_Reco_ttbar_toplep_m.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_ttbar_toplep_m)

    interf_ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_ttH_bestJABDToutput",
                                            label          = "ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput","")
    interf_ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput.bin_edges = [ 
                -1.0,
                -0.5,
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
    interf_ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput.histotitle = "Reco_ttH_bestJABDToutput"
    interf_ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput.histoname = "ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput"
    interf_ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput)

    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_energy_fraction = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_tHW_energy_fraction",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_energy_fraction.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_tHW_energy_fraction","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_energy_fraction.bin_edges = [ 
                -0.5,
                0.0,
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
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_energy_fraction.histotitle = "Reco_JABDT_tHW_energy_fraction"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_energy_fraction.histoname = "ljets_ge4j_ge4t_Reco_JABDT_tHW_energy_fraction"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_energy_fraction.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_energy_fraction)

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

    interf_ljets_ge4j_ge4t_Reco_ttH_toplep_m = vhi.variableHistoInterface(variable_name  = "Reco_ttH_toplep_m",
                                            label          = "ljets_ge4j_ge4t_Reco_ttH_toplep_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_ttH_toplep_m.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_ttH_toplep_m","")
    interf_ljets_ge4j_ge4t_Reco_ttH_toplep_m.bin_edges = [ 
                -1.5,
                0.0,
                103.71,
                118.74,
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
                344.19,
                359.22,
                374.25,
                389.28,
                404.31,
                419.34,
                434.37,
                449.4,
                464.43,
                479.46,
                509.52,
                539.58,
                569.64,
                614.73,
                674.85,
                734.97,
                750.0
                ]
    interf_ljets_ge4j_ge4t_Reco_ttH_toplep_m.histotitle = "Reco_ttH_toplep_m"
    interf_ljets_ge4j_ge4t_Reco_ttH_toplep_m.histoname = "ljets_ge4j_ge4t_Reco_ttH_toplep_m"
    interf_ljets_ge4j_ge4t_Reco_ttH_toplep_m.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_ttH_toplep_m)

    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_Jet_CSV_hdau2 = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttH_Jet_CSV_hdau2",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_ttH_Jet_CSV_hdau2",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_Jet_CSV_hdau2.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_ttH_Jet_CSV_hdau2","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_Jet_CSV_hdau2.bin_edges = [ 
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
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_whaddau1.histotitle = "Reco_JABDT_tHW_Jet_CSV_whaddau1"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_whaddau1.histoname = "ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_whaddau1"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_whaddau1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_whaddau1)

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
                0.1,
                0.12,
                0.14,
                0.16,
                0.18,
                0.2,
                0.22,
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
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau1.histotitle = "Reco_JABDT_ttbar_Jet_CSV_whaddau1"
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau1.histoname = "ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau1"
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau1)

    interf_ljets_ge4j_ge4t_Evt_Deta_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Deta_JetsAverage",
                                            label          = "ljets_ge4j_ge4t_Evt_Deta_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_Deta_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_Deta_JetsAverage","")
    interf_ljets_ge4j_ge4t_Evt_Deta_JetsAverage.bin_edges = [ 
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
                3.0
                ]
    interf_ljets_ge4j_ge4t_Evt_Deta_JetsAverage.histotitle = "Evt_Deta_JetsAverage"
    interf_ljets_ge4j_ge4t_Evt_Deta_JetsAverage.histoname = "ljets_ge4j_ge4t_Evt_Deta_JetsAverage"
    interf_ljets_ge4j_ge4t_Evt_Deta_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_Deta_JetsAverage)

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
                0.12,
                0.14,
                0.16,
                0.18,
                0.2,
                0.22,
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
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau2.histotitle = "Reco_JABDT_ttbar_Jet_CSV_whaddau2"
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau2.histoname = "ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau2"
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau2.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau2)

    # ===================================================================================

    
    for i in interfaces:
        i.category_label = label
    plots = init_plots_2D(interfaces = interfaces)    
    if data:
        add_data_plots(plots=plots,data=data)
    return plots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_ljets_ge4j_ge4t(data)

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
    