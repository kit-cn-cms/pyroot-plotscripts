
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



def plots_ge4j_ge4t_top20(data = None):
    label = "\geq 4 jets, \geq 4 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"


    interf_ljets_ge4j_ge4t_top20_CSV_2 = vhi.variableHistoInterface(variable_name  = "CSV[2]",
                                            label          = "ljets_ge4j_ge4t_top20_CSV_2",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top20_CSV_2.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top20_CSV_2","")
    interf_ljets_ge4j_ge4t_top20_CSV_2.category_label = label
    interf_ljets_ge4j_ge4t_top20_CSV_2.bin_edges = [ 
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
    interf_ljets_ge4j_ge4t_top20_CSV_2.histotitle = "CSV[2]"
    interf_ljets_ge4j_ge4t_top20_CSV_2.histoname = "ljets_ge4j_ge4t_top20_CSV_2"
    interf_ljets_ge4j_ge4t_top20_CSV_2.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top20_CSV_2)
    
    interf_ljets_ge4j_ge4t_top20_Evt_CSV_avg = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg",
                                            label          = "ljets_ge4j_ge4t_top20_Evt_CSV_avg",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top20_Evt_CSV_avg.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top20_Evt_CSV_avg","")
    interf_ljets_ge4j_ge4t_top20_Evt_CSV_avg.category_label = label
    interf_ljets_ge4j_ge4t_top20_Evt_CSV_avg.bin_edges = [ 
                0.218,
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
    interf_ljets_ge4j_ge4t_top20_Evt_CSV_avg.histotitle = "Evt_CSV_avg"
    interf_ljets_ge4j_ge4t_top20_Evt_CSV_avg.histoname = "ljets_ge4j_ge4t_top20_Evt_CSV_avg"
    interf_ljets_ge4j_ge4t_top20_Evt_CSV_avg.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top20_Evt_CSV_avg)
    
    interf_ljets_ge4j_ge4t_top20_Evt_CSV_avg_tagged = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg_tagged",
                                            label          = "ljets_ge4j_ge4t_top20_Evt_CSV_avg_tagged",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top20_Evt_CSV_avg_tagged.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top20_Evt_CSV_avg_tagged","")
    interf_ljets_ge4j_ge4t_top20_Evt_CSV_avg_tagged.category_label = label
    interf_ljets_ge4j_ge4t_top20_Evt_CSV_avg_tagged.bin_edges = [ 
                0.342,
                0.412,
                0.44,
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
    interf_ljets_ge4j_ge4t_top20_Evt_CSV_avg_tagged.histotitle = "Evt_CSV_avg_tagged"
    interf_ljets_ge4j_ge4t_top20_Evt_CSV_avg_tagged.histoname = "ljets_ge4j_ge4t_top20_Evt_CSV_avg_tagged"
    interf_ljets_ge4j_ge4t_top20_Evt_CSV_avg_tagged.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top20_Evt_CSV_avg_tagged)
    
    interf_ljets_ge4j_ge4t_top20_Evt_Deta_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Deta_JetsAverage",
                                            label          = "ljets_ge4j_ge4t_top20_Evt_Deta_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top20_Evt_Deta_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top20_Evt_Deta_JetsAverage","")
    interf_ljets_ge4j_ge4t_top20_Evt_Deta_JetsAverage.category_label = label
    interf_ljets_ge4j_ge4t_top20_Evt_Deta_JetsAverage.bin_edges = [ 
                0.06,
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
                2.34,
                3.0
                ]
    interf_ljets_ge4j_ge4t_top20_Evt_Deta_JetsAverage.histotitle = "Evt_Deta_JetsAverage"
    interf_ljets_ge4j_ge4t_top20_Evt_Deta_JetsAverage.histoname = "ljets_ge4j_ge4t_top20_Evt_Deta_JetsAverage"
    interf_ljets_ge4j_ge4t_top20_Evt_Deta_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top20_Evt_Deta_JetsAverage)
    
    interf_ljets_ge4j_ge4t_top20_Evt_Deta_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Deta_TaggedJetsAverage",
                                            label          = "ljets_ge4j_ge4t_top20_Evt_Deta_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top20_Evt_Deta_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top20_Evt_Deta_TaggedJetsAverage","")
    interf_ljets_ge4j_ge4t_top20_Evt_Deta_TaggedJetsAverage.category_label = label
    interf_ljets_ge4j_ge4t_top20_Evt_Deta_TaggedJetsAverage.bin_edges = [ 
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
                2.52,
                3.0
                ]
    interf_ljets_ge4j_ge4t_top20_Evt_Deta_TaggedJetsAverage.histotitle = "Evt_Deta_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_top20_Evt_Deta_TaggedJetsAverage.histoname = "ljets_ge4j_ge4t_top20_Evt_Deta_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_top20_Evt_Deta_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top20_Evt_Deta_TaggedJetsAverage)
    
    interf_ljets_ge4j_ge4t_top20_Evt_HT_tags = vhi.variableHistoInterface(variable_name  = "Evt_HT_tags",
                                            label          = "ljets_ge4j_ge4t_top20_Evt_HT_tags",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top20_Evt_HT_tags.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top20_Evt_HT_tags","")
    interf_ljets_ge4j_ge4t_top20_Evt_HT_tags.category_label = label
    interf_ljets_ge4j_ge4t_top20_Evt_HT_tags.bin_edges = [ 
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
                838.0,
                874.0,
                910.0,
                946.0,
                982.0,
                1000.0
                ]
    interf_ljets_ge4j_ge4t_top20_Evt_HT_tags.histotitle = "Evt_HT_tags"
    interf_ljets_ge4j_ge4t_top20_Evt_HT_tags.histoname = "ljets_ge4j_ge4t_top20_Evt_HT_tags"
    interf_ljets_ge4j_ge4t_top20_Evt_HT_tags.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top20_Evt_HT_tags)
    
    interf_ljets_ge4j_ge4t_top20_Evt_M2_minDrTaggedJets = vhi.variableHistoInterface(variable_name  = "Evt_M2_minDrTaggedJets",
                                            label          = "ljets_ge4j_ge4t_top20_Evt_M2_minDrTaggedJets",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top20_Evt_M2_minDrTaggedJets.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top20_Evt_M2_minDrTaggedJets","")
    interf_ljets_ge4j_ge4t_top20_Evt_M2_minDrTaggedJets.category_label = label
    interf_ljets_ge4j_ge4t_top20_Evt_M2_minDrTaggedJets.bin_edges = [ 
                16.0,
                24.0,
                32.0,
                40.0,
                48.0,
                56.0,
                64.0,
                72.0,
                80.0,
                88.0,
                96.0,
                104.0,
                112.0,
                120.0,
                128.0,
                136.0,
                144.0,
                152.0,
                160.0,
                168.0,
                176.0,
                184.0,
                192.0,
                200.0,
                208.0,
                216.0,
                224.0,
                240.0,
                256.0,
                272.0,
                296.0,
                336.0,
                400.0
                ]
    interf_ljets_ge4j_ge4t_top20_Evt_M2_minDrTaggedJets.histotitle = "M_{2}( min #DeltaR(tag,tag) )"
    interf_ljets_ge4j_ge4t_top20_Evt_M2_minDrTaggedJets.histoname = "ljets_ge4j_ge4t_top20_Evt_M2_minDrTaggedJets"
    interf_ljets_ge4j_ge4t_top20_Evt_M2_minDrTaggedJets.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top20_Evt_M2_minDrTaggedJets)
    
    interf_ljets_ge4j_ge4t_top20_Evt_M_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_M_TaggedJetsAverage",
                                            label          = "ljets_ge4j_ge4t_top20_Evt_M_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top20_Evt_M_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top20_Evt_M_TaggedJetsAverage","")
    interf_ljets_ge4j_ge4t_top20_Evt_M_TaggedJetsAverage.category_label = label
    interf_ljets_ge4j_ge4t_top20_Evt_M_TaggedJetsAverage.bin_edges = [ 
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
                33.6,
                37.5,
                42.7,
                70.0
                ]
    interf_ljets_ge4j_ge4t_top20_Evt_M_TaggedJetsAverage.histotitle = "Evt_M_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_top20_Evt_M_TaggedJetsAverage.histoname = "ljets_ge4j_ge4t_top20_Evt_M_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_top20_Evt_M_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top20_Evt_M_TaggedJetsAverage)
    
    interf_ljets_ge4j_ge4t_top20_Evt_Pt_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Pt_JetsAverage",
                                            label          = "ljets_ge4j_ge4t_top20_Evt_Pt_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top20_Evt_Pt_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top20_Evt_Pt_JetsAverage","")
    interf_ljets_ge4j_ge4t_top20_Evt_Pt_JetsAverage.category_label = label
    interf_ljets_ge4j_ge4t_top20_Evt_Pt_JetsAverage.bin_edges = [ 
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
                227.4,
                246.2,
                265.0,
                312.0,
                500.0
                ]
    interf_ljets_ge4j_ge4t_top20_Evt_Pt_JetsAverage.histotitle = "Evt_Pt_JetsAverage"
    interf_ljets_ge4j_ge4t_top20_Evt_Pt_JetsAverage.histoname = "ljets_ge4j_ge4t_top20_Evt_Pt_JetsAverage"
    interf_ljets_ge4j_ge4t_top20_Evt_Pt_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top20_Evt_Pt_JetsAverage)
    
    interf_ljets_ge4j_ge4t_top20_Evt_Pt_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Pt_TaggedJetsAverage",
                                            label          = "ljets_ge4j_ge4t_top20_Evt_Pt_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top20_Evt_Pt_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top20_Evt_Pt_TaggedJetsAverage","")
    interf_ljets_ge4j_ge4t_top20_Evt_Pt_TaggedJetsAverage.category_label = label
    interf_ljets_ge4j_ge4t_top20_Evt_Pt_TaggedJetsAverage.bin_edges = [ 
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
                280.8,
                337.8,
                600.0
                ]
    interf_ljets_ge4j_ge4t_top20_Evt_Pt_TaggedJetsAverage.histotitle = "Evt_Pt_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_top20_Evt_Pt_TaggedJetsAverage.histoname = "ljets_ge4j_ge4t_top20_Evt_Pt_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_top20_Evt_Pt_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top20_Evt_Pt_TaggedJetsAverage)
    
    interf_ljets_ge4j_ge4t_top20_Evt_Pt_minDrTaggedJets = vhi.variableHistoInterface(variable_name  = "Evt_Pt_minDrTaggedJets",
                                            label          = "ljets_ge4j_ge4t_top20_Evt_Pt_minDrTaggedJets",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top20_Evt_Pt_minDrTaggedJets.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top20_Evt_Pt_minDrTaggedJets","")
    interf_ljets_ge4j_ge4t_top20_Evt_Pt_minDrTaggedJets.category_label = label
    interf_ljets_ge4j_ge4t_top20_Evt_Pt_minDrTaggedJets.bin_edges = [ 
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
    interf_ljets_ge4j_ge4t_top20_Evt_Pt_minDrTaggedJets.histotitle = "Evt_Pt_minDrTaggedJets"
    interf_ljets_ge4j_ge4t_top20_Evt_Pt_minDrTaggedJets.histoname = "ljets_ge4j_ge4t_top20_Evt_Pt_minDrTaggedJets"
    interf_ljets_ge4j_ge4t_top20_Evt_Pt_minDrTaggedJets.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top20_Evt_Pt_minDrTaggedJets)
    
    interf_ljets_ge4j_ge4t_top20_Evt_blr_transformed = vhi.variableHistoInterface(variable_name  = "Evt_blr_transformed",
                                            label          = "ljets_ge4j_ge4t_top20_Evt_blr_transformed",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top20_Evt_blr_transformed.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top20_Evt_blr_transformed","")
    interf_ljets_ge4j_ge4t_top20_Evt_blr_transformed.category_label = label
    interf_ljets_ge4j_ge4t_top20_Evt_blr_transformed.bin_edges = [ 
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
    interf_ljets_ge4j_ge4t_top20_Evt_blr_transformed.histotitle = "Evt_blr_transformed"
    interf_ljets_ge4j_ge4t_top20_Evt_blr_transformed.histoname = "ljets_ge4j_ge4t_top20_Evt_blr_transformed"
    interf_ljets_ge4j_ge4t_top20_Evt_blr_transformed.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top20_Evt_blr_transformed)
    
    interf_ljets_ge4j_ge4t_top20_N_Jets = vhi.variableHistoInterface(variable_name  = "N_Jets",
                                            label          = "ljets_ge4j_ge4t_top20_N_Jets",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top20_N_Jets.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top20_N_Jets","")
    interf_ljets_ge4j_ge4t_top20_N_Jets.category_label = label
    interf_ljets_ge4j_ge4t_top20_N_Jets.bin_edges = [ 
                3.5,
                4.5,
                5.5,
                6.5,
                7.5,
                8.5,
                9.5,
                10.5
                ]
    interf_ljets_ge4j_ge4t_top20_N_Jets.histotitle = "N_Jets"
    interf_ljets_ge4j_ge4t_top20_N_Jets.histoname = "ljets_ge4j_ge4t_top20_N_Jets"
    interf_ljets_ge4j_ge4t_top20_N_Jets.nhistobins = 7
    interfaces.append(interf_ljets_ge4j_ge4t_top20_N_Jets)
    
    interf_ljets_ge4j_ge4t_top20_Reco_JABDT_tHW_Jet_CSV_btop = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_Jet_CSV_btop",
                                            label          = "ljets_ge4j_ge4t_top20_Reco_JABDT_tHW_Jet_CSV_btop",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top20_Reco_JABDT_tHW_Jet_CSV_btop.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top20_Reco_JABDT_tHW_Jet_CSV_btop","")
    interf_ljets_ge4j_ge4t_top20_Reco_JABDT_tHW_Jet_CSV_btop.category_label = label
    interf_ljets_ge4j_ge4t_top20_Reco_JABDT_tHW_Jet_CSV_btop.bin_edges = [ 
                -1.5,
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
    interf_ljets_ge4j_ge4t_top20_Reco_JABDT_tHW_Jet_CSV_btop.histotitle = "Reco_JABDT_tHW_Jet_CSV_btop"
    interf_ljets_ge4j_ge4t_top20_Reco_JABDT_tHW_Jet_CSV_btop.histoname = "ljets_ge4j_ge4t_top20_Reco_JABDT_tHW_Jet_CSV_btop"
    interf_ljets_ge4j_ge4t_top20_Reco_JABDT_tHW_Jet_CSV_btop.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top20_Reco_JABDT_tHW_Jet_CSV_btop)
    
    interf_ljets_ge4j_ge4t_top20_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",
                                            label          = "ljets_ge4j_ge4t_top20_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top20_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top20_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt","")
    interf_ljets_ge4j_ge4t_top20_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.category_label = label
    interf_ljets_ge4j_ge4t_top20_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.bin_edges = [ 
                -1.5,
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
    interf_ljets_ge4j_ge4t_top20_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.histotitle = "Reco_JABDT_tHW_energy_fraction"
    interf_ljets_ge4j_ge4t_top20_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.histoname = "ljets_ge4j_ge4t_top20_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt"
    interf_ljets_ge4j_ge4t_top20_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top20_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt)
    
    interf_ljets_ge4j_ge4t_top20_Reco_JABDT_tHq_abs_ljet_eta = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHq_abs_ljet_eta",
                                            label          = "ljets_ge4j_ge4t_top20_Reco_JABDT_tHq_abs_ljet_eta",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top20_Reco_JABDT_tHq_abs_ljet_eta.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top20_Reco_JABDT_tHq_abs_ljet_eta","")
    interf_ljets_ge4j_ge4t_top20_Reco_JABDT_tHq_abs_ljet_eta.category_label = label
    interf_ljets_ge4j_ge4t_top20_Reco_JABDT_tHq_abs_ljet_eta.bin_edges = [ 
                -1.5,
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
                4.14,
                4.38,
                4.5
                ]
    interf_ljets_ge4j_ge4t_top20_Reco_JABDT_tHq_abs_ljet_eta.histotitle = "Reco_JABDT_tHq_abs_ljet_eta"
    interf_ljets_ge4j_ge4t_top20_Reco_JABDT_tHq_abs_ljet_eta.histoname = "ljets_ge4j_ge4t_top20_Reco_JABDT_tHq_abs_ljet_eta"
    interf_ljets_ge4j_ge4t_top20_Reco_JABDT_tHq_abs_ljet_eta.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top20_Reco_JABDT_tHq_abs_ljet_eta)
    
    interf_ljets_ge4j_ge4t_top20_Reco_tHq_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_tHq_bestJABDToutput",
                                            label          = "ljets_ge4j_ge4t_top20_Reco_tHq_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top20_Reco_tHq_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top20_Reco_tHq_bestJABDToutput","")
    interf_ljets_ge4j_ge4t_top20_Reco_tHq_bestJABDToutput.category_label = label
    interf_ljets_ge4j_ge4t_top20_Reco_tHq_bestJABDToutput.bin_edges = [ 
                -1.0,
                -0.286,
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
    interf_ljets_ge4j_ge4t_top20_Reco_tHq_bestJABDToutput.histotitle = "Reco_tHq_bestJABDToutput"
    interf_ljets_ge4j_ge4t_top20_Reco_tHq_bestJABDToutput.histoname = "ljets_ge4j_ge4t_top20_Reco_tHq_bestJABDToutput"
    interf_ljets_ge4j_ge4t_top20_Reco_tHq_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top20_Reco_tHq_bestJABDToutput)
    
    interf_ljets_ge4j_ge4t_top20_Reco_ttH_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_ttH_bestJABDToutput",
                                            label          = "ljets_ge4j_ge4t_top20_Reco_ttH_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top20_Reco_ttH_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top20_Reco_ttH_bestJABDToutput","")
    interf_ljets_ge4j_ge4t_top20_Reco_ttH_bestJABDToutput.category_label = label
    interf_ljets_ge4j_ge4t_top20_Reco_ttH_bestJABDToutput.bin_edges = [ 
                -1.0,
                -0.286,
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
    interf_ljets_ge4j_ge4t_top20_Reco_ttH_bestJABDToutput.histotitle = "Reco_ttH_bestJABDToutput"
    interf_ljets_ge4j_ge4t_top20_Reco_ttH_bestJABDToutput.histoname = "ljets_ge4j_ge4t_top20_Reco_ttH_bestJABDToutput"
    interf_ljets_ge4j_ge4t_top20_Reco_ttH_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top20_Reco_ttH_bestJABDToutput)
    
    interf_ljets_ge4j_ge4t_top20_Reco_ttH_toplep_m = vhi.variableHistoInterface(variable_name  = "Reco_ttH_toplep_m",
                                            label          = "ljets_ge4j_ge4t_top20_Reco_ttH_toplep_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top20_Reco_ttH_toplep_m.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top20_Reco_ttH_toplep_m","")
    interf_ljets_ge4j_ge4t_top20_Reco_ttH_toplep_m.category_label = label
    interf_ljets_ge4j_ge4t_top20_Reco_ttH_toplep_m.bin_edges = [ 
                -1.5,
                88.68,
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
                599.7,
                644.79,
                689.88,
                734.97,
                750.0
                ]
    interf_ljets_ge4j_ge4t_top20_Reco_ttH_toplep_m.histotitle = "Reco_ttH_toplep_m"
    interf_ljets_ge4j_ge4t_top20_Reco_ttH_toplep_m.histoname = "ljets_ge4j_ge4t_top20_Reco_ttH_toplep_m"
    interf_ljets_ge4j_ge4t_top20_Reco_ttH_toplep_m.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top20_Reco_ttH_toplep_m)
    
    interf_ljets_ge4j_ge4t_top20_Reco_ttbar_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_ttbar_bestJABDToutput",
                                            label          = "ljets_ge4j_ge4t_top20_Reco_ttbar_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top20_Reco_ttbar_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top20_Reco_ttbar_bestJABDToutput","")
    interf_ljets_ge4j_ge4t_top20_Reco_ttbar_bestJABDToutput.category_label = label
    interf_ljets_ge4j_ge4t_top20_Reco_ttbar_bestJABDToutput.bin_edges = [ 
                -0.4,
                -0.268,
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
                0.7
                ]
    interf_ljets_ge4j_ge4t_top20_Reco_ttbar_bestJABDToutput.histotitle = "Reco_ttbar_bestJABDToutput"
    interf_ljets_ge4j_ge4t_top20_Reco_ttbar_bestJABDToutput.histoname = "ljets_ge4j_ge4t_top20_Reco_ttbar_bestJABDToutput"
    interf_ljets_ge4j_ge4t_top20_Reco_ttbar_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top20_Reco_ttbar_bestJABDToutput)
    
    plots = init_plots_2D(interfaces = interfaces)    
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_ge4j_ge4t_top25(data = None):
    label = "\geq 4 jets, \geq 4 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"


    interf_ljets_ge4j_ge4t_top25_CSV_2 = vhi.variableHistoInterface(variable_name  = "CSV[2]",
                                            label          = "ljets_ge4j_ge4t_top25_CSV_2",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top25_CSV_2.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top25_CSV_2","")
    interf_ljets_ge4j_ge4t_top25_CSV_2.category_label = label
    interf_ljets_ge4j_ge4t_top25_CSV_2.minxval = 0.277
    interf_ljets_ge4j_ge4t_top25_CSV_2.maxxval = 1.0
    interf_ljets_ge4j_ge4t_top25_CSV_2.histotitle = "CSV[2]"
    interf_ljets_ge4j_ge4t_top25_CSV_2.histoname = "ljets_ge4j_ge4t_top25_CSV_2"
    interf_ljets_ge4j_ge4t_top25_CSV_2.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top25_CSV_2)
    
    interf_ljets_ge4j_ge4t_top25_Evt_CSV_avg = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg",
                                            label          = "ljets_ge4j_ge4t_top25_Evt_CSV_avg",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top25_Evt_CSV_avg.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top25_Evt_CSV_avg","")
    interf_ljets_ge4j_ge4t_top25_Evt_CSV_avg.category_label = label
    interf_ljets_ge4j_ge4t_top25_Evt_CSV_avg.minxval = 0.15
    interf_ljets_ge4j_ge4t_top25_Evt_CSV_avg.maxxval = 1.0
    interf_ljets_ge4j_ge4t_top25_Evt_CSV_avg.histotitle = "Evt_CSV_avg"
    interf_ljets_ge4j_ge4t_top25_Evt_CSV_avg.histoname = "ljets_ge4j_ge4t_top25_Evt_CSV_avg"
    interf_ljets_ge4j_ge4t_top25_Evt_CSV_avg.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top25_Evt_CSV_avg)
    
    interf_ljets_ge4j_ge4t_top25_Evt_CSV_avg_tagged = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg_tagged",
                                            label          = "ljets_ge4j_ge4t_top25_Evt_CSV_avg_tagged",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top25_Evt_CSV_avg_tagged.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top25_Evt_CSV_avg_tagged","")
    interf_ljets_ge4j_ge4t_top25_Evt_CSV_avg_tagged.category_label = label
    interf_ljets_ge4j_ge4t_top25_Evt_CSV_avg_tagged.minxval = 0.3
    interf_ljets_ge4j_ge4t_top25_Evt_CSV_avg_tagged.maxxval = 1.0
    interf_ljets_ge4j_ge4t_top25_Evt_CSV_avg_tagged.histotitle = "Evt_CSV_avg_tagged"
    interf_ljets_ge4j_ge4t_top25_Evt_CSV_avg_tagged.histoname = "ljets_ge4j_ge4t_top25_Evt_CSV_avg_tagged"
    interf_ljets_ge4j_ge4t_top25_Evt_CSV_avg_tagged.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top25_Evt_CSV_avg_tagged)
    
    interf_ljets_ge4j_ge4t_top25_Evt_Deta_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Deta_JetsAverage",
                                            label          = "ljets_ge4j_ge4t_top25_Evt_Deta_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top25_Evt_Deta_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top25_Evt_Deta_JetsAverage","")
    interf_ljets_ge4j_ge4t_top25_Evt_Deta_JetsAverage.category_label = label
    interf_ljets_ge4j_ge4t_top25_Evt_Deta_JetsAverage.minxval = 0.0
    interf_ljets_ge4j_ge4t_top25_Evt_Deta_JetsAverage.maxxval = 3.0
    interf_ljets_ge4j_ge4t_top25_Evt_Deta_JetsAverage.histotitle = "Evt_Deta_JetsAverage"
    interf_ljets_ge4j_ge4t_top25_Evt_Deta_JetsAverage.histoname = "ljets_ge4j_ge4t_top25_Evt_Deta_JetsAverage"
    interf_ljets_ge4j_ge4t_top25_Evt_Deta_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top25_Evt_Deta_JetsAverage)
    
    interf_ljets_ge4j_ge4t_top25_Evt_Deta_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Deta_TaggedJetsAverage",
                                            label          = "ljets_ge4j_ge4t_top25_Evt_Deta_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top25_Evt_Deta_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top25_Evt_Deta_TaggedJetsAverage","")
    interf_ljets_ge4j_ge4t_top25_Evt_Deta_TaggedJetsAverage.category_label = label
    interf_ljets_ge4j_ge4t_top25_Evt_Deta_TaggedJetsAverage.minxval = 0.0
    interf_ljets_ge4j_ge4t_top25_Evt_Deta_TaggedJetsAverage.maxxval = 3.0
    interf_ljets_ge4j_ge4t_top25_Evt_Deta_TaggedJetsAverage.histotitle = "Evt_Deta_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_top25_Evt_Deta_TaggedJetsAverage.histoname = "ljets_ge4j_ge4t_top25_Evt_Deta_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_top25_Evt_Deta_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top25_Evt_Deta_TaggedJetsAverage)
    
    interf_ljets_ge4j_ge4t_top25_Evt_Dr_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Dr_TaggedJetsAverage",
                                            label          = "ljets_ge4j_ge4t_top25_Evt_Dr_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top25_Evt_Dr_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top25_Evt_Dr_TaggedJetsAverage","")
    interf_ljets_ge4j_ge4t_top25_Evt_Dr_TaggedJetsAverage.category_label = label
    interf_ljets_ge4j_ge4t_top25_Evt_Dr_TaggedJetsAverage.minxval = 0.5
    interf_ljets_ge4j_ge4t_top25_Evt_Dr_TaggedJetsAverage.maxxval = 3.5
    interf_ljets_ge4j_ge4t_top25_Evt_Dr_TaggedJetsAverage.histotitle = "average #DeltaR(tags)"
    interf_ljets_ge4j_ge4t_top25_Evt_Dr_TaggedJetsAverage.histoname = "ljets_ge4j_ge4t_top25_Evt_Dr_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_top25_Evt_Dr_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top25_Evt_Dr_TaggedJetsAverage)
    
    interf_ljets_ge4j_ge4t_top25_Evt_HT_jets = vhi.variableHistoInterface(variable_name  = "Evt_HT_jets",
                                            label          = "ljets_ge4j_ge4t_top25_Evt_HT_jets",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top25_Evt_HT_jets.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top25_Evt_HT_jets","")
    interf_ljets_ge4j_ge4t_top25_Evt_HT_jets.category_label = label
    interf_ljets_ge4j_ge4t_top25_Evt_HT_jets.minxval = 200.0
    interf_ljets_ge4j_ge4t_top25_Evt_HT_jets.maxxval = 1500.0
    interf_ljets_ge4j_ge4t_top25_Evt_HT_jets.histotitle = "H_{T}(jets)"
    interf_ljets_ge4j_ge4t_top25_Evt_HT_jets.histoname = "ljets_ge4j_ge4t_top25_Evt_HT_jets"
    interf_ljets_ge4j_ge4t_top25_Evt_HT_jets.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top25_Evt_HT_jets)
    
    interf_ljets_ge4j_ge4t_top25_Evt_HT_tags = vhi.variableHistoInterface(variable_name  = "Evt_HT_tags",
                                            label          = "ljets_ge4j_ge4t_top25_Evt_HT_tags",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top25_Evt_HT_tags.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top25_Evt_HT_tags","")
    interf_ljets_ge4j_ge4t_top25_Evt_HT_tags.category_label = label
    interf_ljets_ge4j_ge4t_top25_Evt_HT_tags.minxval = 100.0
    interf_ljets_ge4j_ge4t_top25_Evt_HT_tags.maxxval = 1000.0
    interf_ljets_ge4j_ge4t_top25_Evt_HT_tags.histotitle = "Evt_HT_tags"
    interf_ljets_ge4j_ge4t_top25_Evt_HT_tags.histoname = "ljets_ge4j_ge4t_top25_Evt_HT_tags"
    interf_ljets_ge4j_ge4t_top25_Evt_HT_tags.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top25_Evt_HT_tags)
    
    interf_ljets_ge4j_ge4t_top25_Evt_M2_minDrTaggedJets = vhi.variableHistoInterface(variable_name  = "Evt_M2_minDrTaggedJets",
                                            label          = "ljets_ge4j_ge4t_top25_Evt_M2_minDrTaggedJets",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top25_Evt_M2_minDrTaggedJets.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top25_Evt_M2_minDrTaggedJets","")
    interf_ljets_ge4j_ge4t_top25_Evt_M2_minDrTaggedJets.category_label = label
    interf_ljets_ge4j_ge4t_top25_Evt_M2_minDrTaggedJets.minxval = 0.0
    interf_ljets_ge4j_ge4t_top25_Evt_M2_minDrTaggedJets.maxxval = 400.0
    interf_ljets_ge4j_ge4t_top25_Evt_M2_minDrTaggedJets.histotitle = "M_{2}( min #DeltaR(tag,tag) )"
    interf_ljets_ge4j_ge4t_top25_Evt_M2_minDrTaggedJets.histoname = "ljets_ge4j_ge4t_top25_Evt_M2_minDrTaggedJets"
    interf_ljets_ge4j_ge4t_top25_Evt_M2_minDrTaggedJets.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top25_Evt_M2_minDrTaggedJets)
    
    interf_ljets_ge4j_ge4t_top25_Evt_M_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_M_JetsAverage",
                                            label          = "ljets_ge4j_ge4t_top25_Evt_M_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top25_Evt_M_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top25_Evt_M_JetsAverage","")
    interf_ljets_ge4j_ge4t_top25_Evt_M_JetsAverage.category_label = label
    interf_ljets_ge4j_ge4t_top25_Evt_M_JetsAverage.minxval = 5.0
    interf_ljets_ge4j_ge4t_top25_Evt_M_JetsAverage.maxxval = 50.0
    interf_ljets_ge4j_ge4t_top25_Evt_M_JetsAverage.histotitle = "Evt_M_JetsAverage"
    interf_ljets_ge4j_ge4t_top25_Evt_M_JetsAverage.histoname = "ljets_ge4j_ge4t_top25_Evt_M_JetsAverage"
    interf_ljets_ge4j_ge4t_top25_Evt_M_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top25_Evt_M_JetsAverage)
    
    interf_ljets_ge4j_ge4t_top25_Evt_M_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_M_TaggedJetsAverage",
                                            label          = "ljets_ge4j_ge4t_top25_Evt_M_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top25_Evt_M_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top25_Evt_M_TaggedJetsAverage","")
    interf_ljets_ge4j_ge4t_top25_Evt_M_TaggedJetsAverage.category_label = label
    interf_ljets_ge4j_ge4t_top25_Evt_M_TaggedJetsAverage.minxval = 5.0
    interf_ljets_ge4j_ge4t_top25_Evt_M_TaggedJetsAverage.maxxval = 70.0
    interf_ljets_ge4j_ge4t_top25_Evt_M_TaggedJetsAverage.histotitle = "Evt_M_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_top25_Evt_M_TaggedJetsAverage.histoname = "ljets_ge4j_ge4t_top25_Evt_M_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_top25_Evt_M_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top25_Evt_M_TaggedJetsAverage)
    
    interf_ljets_ge4j_ge4t_top25_Evt_M_minDrLepTag = vhi.variableHistoInterface(variable_name  = "Evt_M_minDrLepTag",
                                            label          = "ljets_ge4j_ge4t_top25_Evt_M_minDrLepTag",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top25_Evt_M_minDrLepTag.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top25_Evt_M_minDrLepTag","")
    interf_ljets_ge4j_ge4t_top25_Evt_M_minDrLepTag.category_label = label
    interf_ljets_ge4j_ge4t_top25_Evt_M_minDrLepTag.minxval = 15.0
    interf_ljets_ge4j_ge4t_top25_Evt_M_minDrLepTag.maxxval = 400.0
    interf_ljets_ge4j_ge4t_top25_Evt_M_minDrLepTag.histotitle = "Evt_M_minDrLepTag"
    interf_ljets_ge4j_ge4t_top25_Evt_M_minDrLepTag.histoname = "ljets_ge4j_ge4t_top25_Evt_M_minDrLepTag"
    interf_ljets_ge4j_ge4t_top25_Evt_M_minDrLepTag.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top25_Evt_M_minDrLepTag)
    
    interf_ljets_ge4j_ge4t_top25_Evt_Pt_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Pt_JetsAverage",
                                            label          = "ljets_ge4j_ge4t_top25_Evt_Pt_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top25_Evt_Pt_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top25_Evt_Pt_JetsAverage","")
    interf_ljets_ge4j_ge4t_top25_Evt_Pt_JetsAverage.category_label = label
    interf_ljets_ge4j_ge4t_top25_Evt_Pt_JetsAverage.minxval = 30.0
    interf_ljets_ge4j_ge4t_top25_Evt_Pt_JetsAverage.maxxval = 500.0
    interf_ljets_ge4j_ge4t_top25_Evt_Pt_JetsAverage.histotitle = "Evt_Pt_JetsAverage"
    interf_ljets_ge4j_ge4t_top25_Evt_Pt_JetsAverage.histoname = "ljets_ge4j_ge4t_top25_Evt_Pt_JetsAverage"
    interf_ljets_ge4j_ge4t_top25_Evt_Pt_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top25_Evt_Pt_JetsAverage)
    
    interf_ljets_ge4j_ge4t_top25_Evt_Pt_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Pt_TaggedJetsAverage",
                                            label          = "ljets_ge4j_ge4t_top25_Evt_Pt_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top25_Evt_Pt_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top25_Evt_Pt_TaggedJetsAverage","")
    interf_ljets_ge4j_ge4t_top25_Evt_Pt_TaggedJetsAverage.category_label = label
    interf_ljets_ge4j_ge4t_top25_Evt_Pt_TaggedJetsAverage.minxval = 30.0
    interf_ljets_ge4j_ge4t_top25_Evt_Pt_TaggedJetsAverage.maxxval = 600.0
    interf_ljets_ge4j_ge4t_top25_Evt_Pt_TaggedJetsAverage.histotitle = "Evt_Pt_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_top25_Evt_Pt_TaggedJetsAverage.histoname = "ljets_ge4j_ge4t_top25_Evt_Pt_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_top25_Evt_Pt_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top25_Evt_Pt_TaggedJetsAverage)
    
    interf_ljets_ge4j_ge4t_top25_Evt_Pt_minDrTaggedJets = vhi.variableHistoInterface(variable_name  = "Evt_Pt_minDrTaggedJets",
                                            label          = "ljets_ge4j_ge4t_top25_Evt_Pt_minDrTaggedJets",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top25_Evt_Pt_minDrTaggedJets.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top25_Evt_Pt_minDrTaggedJets","")
    interf_ljets_ge4j_ge4t_top25_Evt_Pt_minDrTaggedJets.category_label = label
    interf_ljets_ge4j_ge4t_top25_Evt_Pt_minDrTaggedJets.minxval = 20.0
    interf_ljets_ge4j_ge4t_top25_Evt_Pt_minDrTaggedJets.maxxval = 600.0
    interf_ljets_ge4j_ge4t_top25_Evt_Pt_minDrTaggedJets.histotitle = "Evt_Pt_minDrTaggedJets"
    interf_ljets_ge4j_ge4t_top25_Evt_Pt_minDrTaggedJets.histoname = "ljets_ge4j_ge4t_top25_Evt_Pt_minDrTaggedJets"
    interf_ljets_ge4j_ge4t_top25_Evt_Pt_minDrTaggedJets.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top25_Evt_Pt_minDrTaggedJets)
    
    interf_ljets_ge4j_ge4t_top25_Evt_blr_transformed = vhi.variableHistoInterface(variable_name  = "Evt_blr_transformed",
                                            label          = "ljets_ge4j_ge4t_top25_Evt_blr_transformed",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top25_Evt_blr_transformed.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top25_Evt_blr_transformed","")
    interf_ljets_ge4j_ge4t_top25_Evt_blr_transformed.category_label = label
    interf_ljets_ge4j_ge4t_top25_Evt_blr_transformed.minxval = -2.5
    interf_ljets_ge4j_ge4t_top25_Evt_blr_transformed.maxxval = 15.0
    interf_ljets_ge4j_ge4t_top25_Evt_blr_transformed.histotitle = "Evt_blr_transformed"
    interf_ljets_ge4j_ge4t_top25_Evt_blr_transformed.histoname = "ljets_ge4j_ge4t_top25_Evt_blr_transformed"
    interf_ljets_ge4j_ge4t_top25_Evt_blr_transformed.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top25_Evt_blr_transformed)
    
    interf_ljets_ge4j_ge4t_top25_N_Jets = vhi.variableHistoInterface(variable_name  = "N_Jets",
                                            label          = "ljets_ge4j_ge4t_top25_N_Jets",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top25_N_Jets.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top25_N_Jets","")
    interf_ljets_ge4j_ge4t_top25_N_Jets.category_label = label
    interf_ljets_ge4j_ge4t_top25_N_Jets.minxval = 3.5
    interf_ljets_ge4j_ge4t_top25_N_Jets.maxxval = 10.5
    interf_ljets_ge4j_ge4t_top25_N_Jets.histotitle = "N_Jets"
    interf_ljets_ge4j_ge4t_top25_N_Jets.histoname = "ljets_ge4j_ge4t_top25_N_Jets"
    interf_ljets_ge4j_ge4t_top25_N_Jets.nhistobins = 7
    interfaces.append(interf_ljets_ge4j_ge4t_top25_N_Jets)
    
    interf_ljets_ge4j_ge4t_top25_Reco_JABDT_tHW_Jet_CSV_btop = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_Jet_CSV_btop",
                                            label          = "ljets_ge4j_ge4t_top25_Reco_JABDT_tHW_Jet_CSV_btop",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top25_Reco_JABDT_tHW_Jet_CSV_btop.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top25_Reco_JABDT_tHW_Jet_CSV_btop","")
    interf_ljets_ge4j_ge4t_top25_Reco_JABDT_tHW_Jet_CSV_btop.category_label = label
    interf_ljets_ge4j_ge4t_top25_Reco_JABDT_tHW_Jet_CSV_btop.minxval = -1.5
    interf_ljets_ge4j_ge4t_top25_Reco_JABDT_tHW_Jet_CSV_btop.maxxval = 1.0
    interf_ljets_ge4j_ge4t_top25_Reco_JABDT_tHW_Jet_CSV_btop.histotitle = "Reco_JABDT_tHW_Jet_CSV_btop"
    interf_ljets_ge4j_ge4t_top25_Reco_JABDT_tHW_Jet_CSV_btop.histoname = "ljets_ge4j_ge4t_top25_Reco_JABDT_tHW_Jet_CSV_btop"
    interf_ljets_ge4j_ge4t_top25_Reco_JABDT_tHW_Jet_CSV_btop.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top25_Reco_JABDT_tHW_Jet_CSV_btop)
    
    interf_ljets_ge4j_ge4t_top25_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",
                                            label          = "ljets_ge4j_ge4t_top25_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top25_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top25_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt","")
    interf_ljets_ge4j_ge4t_top25_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.category_label = label
    interf_ljets_ge4j_ge4t_top25_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.minxval = -1.5
    interf_ljets_ge4j_ge4t_top25_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.maxxval = 1.0
    interf_ljets_ge4j_ge4t_top25_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.histotitle = "Reco_JABDT_tHW_energy_fraction"
    interf_ljets_ge4j_ge4t_top25_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.histoname = "ljets_ge4j_ge4t_top25_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt"
    interf_ljets_ge4j_ge4t_top25_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top25_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt)
    
    interf_ljets_ge4j_ge4t_top25_Reco_JABDT_tHq_abs_ljet_eta = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHq_abs_ljet_eta",
                                            label          = "ljets_ge4j_ge4t_top25_Reco_JABDT_tHq_abs_ljet_eta",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top25_Reco_JABDT_tHq_abs_ljet_eta.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top25_Reco_JABDT_tHq_abs_ljet_eta","")
    interf_ljets_ge4j_ge4t_top25_Reco_JABDT_tHq_abs_ljet_eta.category_label = label
    interf_ljets_ge4j_ge4t_top25_Reco_JABDT_tHq_abs_ljet_eta.minxval = -1.5
    interf_ljets_ge4j_ge4t_top25_Reco_JABDT_tHq_abs_ljet_eta.maxxval = 4.5
    interf_ljets_ge4j_ge4t_top25_Reco_JABDT_tHq_abs_ljet_eta.histotitle = "Reco_JABDT_tHq_abs_ljet_eta"
    interf_ljets_ge4j_ge4t_top25_Reco_JABDT_tHq_abs_ljet_eta.histoname = "ljets_ge4j_ge4t_top25_Reco_JABDT_tHq_abs_ljet_eta"
    interf_ljets_ge4j_ge4t_top25_Reco_JABDT_tHq_abs_ljet_eta.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top25_Reco_JABDT_tHq_abs_ljet_eta)
    
    interf_ljets_ge4j_ge4t_top25_Reco_tHq_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_tHq_bestJABDToutput",
                                            label          = "ljets_ge4j_ge4t_top25_Reco_tHq_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top25_Reco_tHq_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top25_Reco_tHq_bestJABDToutput","")
    interf_ljets_ge4j_ge4t_top25_Reco_tHq_bestJABDToutput.category_label = label
    interf_ljets_ge4j_ge4t_top25_Reco_tHq_bestJABDToutput.minxval = -1.0
    interf_ljets_ge4j_ge4t_top25_Reco_tHq_bestJABDToutput.maxxval = 0.7
    interf_ljets_ge4j_ge4t_top25_Reco_tHq_bestJABDToutput.histotitle = "Reco_tHq_bestJABDToutput"
    interf_ljets_ge4j_ge4t_top25_Reco_tHq_bestJABDToutput.histoname = "ljets_ge4j_ge4t_top25_Reco_tHq_bestJABDToutput"
    interf_ljets_ge4j_ge4t_top25_Reco_tHq_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top25_Reco_tHq_bestJABDToutput)
    
    interf_ljets_ge4j_ge4t_top25_Reco_ttH_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_ttH_bestJABDToutput",
                                            label          = "ljets_ge4j_ge4t_top25_Reco_ttH_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top25_Reco_ttH_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top25_Reco_ttH_bestJABDToutput","")
    interf_ljets_ge4j_ge4t_top25_Reco_ttH_bestJABDToutput.category_label = label
    interf_ljets_ge4j_ge4t_top25_Reco_ttH_bestJABDToutput.minxval = -1.0
    interf_ljets_ge4j_ge4t_top25_Reco_ttH_bestJABDToutput.maxxval = 0.7
    interf_ljets_ge4j_ge4t_top25_Reco_ttH_bestJABDToutput.histotitle = "Reco_ttH_bestJABDToutput"
    interf_ljets_ge4j_ge4t_top25_Reco_ttH_bestJABDToutput.histoname = "ljets_ge4j_ge4t_top25_Reco_ttH_bestJABDToutput"
    interf_ljets_ge4j_ge4t_top25_Reco_ttH_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top25_Reco_ttH_bestJABDToutput)
    
    interf_ljets_ge4j_ge4t_top25_Reco_ttH_toplep_m = vhi.variableHistoInterface(variable_name  = "Reco_ttH_toplep_m",
                                            label          = "ljets_ge4j_ge4t_top25_Reco_ttH_toplep_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top25_Reco_ttH_toplep_m.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top25_Reco_ttH_toplep_m","")
    interf_ljets_ge4j_ge4t_top25_Reco_ttH_toplep_m.category_label = label
    interf_ljets_ge4j_ge4t_top25_Reco_ttH_toplep_m.minxval = -1.5
    interf_ljets_ge4j_ge4t_top25_Reco_ttH_toplep_m.maxxval = 750.0
    interf_ljets_ge4j_ge4t_top25_Reco_ttH_toplep_m.histotitle = "Reco_ttH_toplep_m"
    interf_ljets_ge4j_ge4t_top25_Reco_ttH_toplep_m.histoname = "ljets_ge4j_ge4t_top25_Reco_ttH_toplep_m"
    interf_ljets_ge4j_ge4t_top25_Reco_ttH_toplep_m.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top25_Reco_ttH_toplep_m)
    
    interf_ljets_ge4j_ge4t_top25_Reco_ttbar_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_ttbar_bestJABDToutput",
                                            label          = "ljets_ge4j_ge4t_top25_Reco_ttbar_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top25_Reco_ttbar_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top25_Reco_ttbar_bestJABDToutput","")
    interf_ljets_ge4j_ge4t_top25_Reco_ttbar_bestJABDToutput.category_label = label
    interf_ljets_ge4j_ge4t_top25_Reco_ttbar_bestJABDToutput.minxval = -0.4
    interf_ljets_ge4j_ge4t_top25_Reco_ttbar_bestJABDToutput.maxxval = 0.7
    interf_ljets_ge4j_ge4t_top25_Reco_ttbar_bestJABDToutput.histotitle = "Reco_ttbar_bestJABDToutput"
    interf_ljets_ge4j_ge4t_top25_Reco_ttbar_bestJABDToutput.histoname = "ljets_ge4j_ge4t_top25_Reco_ttbar_bestJABDToutput"
    interf_ljets_ge4j_ge4t_top25_Reco_ttbar_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top25_Reco_ttbar_bestJABDToutput)
    
    interf_ljets_ge4j_ge4t_top25_Reco_ttbar_toplep_m = vhi.variableHistoInterface(variable_name  = "Reco_ttbar_toplep_m",
                                            label          = "ljets_ge4j_ge4t_top25_Reco_ttbar_toplep_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top25_Reco_ttbar_toplep_m.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top25_Reco_ttbar_toplep_m","")
    interf_ljets_ge4j_ge4t_top25_Reco_ttbar_toplep_m.category_label = label
    interf_ljets_ge4j_ge4t_top25_Reco_ttbar_toplep_m.minxval = 80.0
    interf_ljets_ge4j_ge4t_top25_Reco_ttbar_toplep_m.maxxval = 500.0
    interf_ljets_ge4j_ge4t_top25_Reco_ttbar_toplep_m.histotitle = "Reco_ttbar_toplep_m"
    interf_ljets_ge4j_ge4t_top25_Reco_ttbar_toplep_m.histoname = "ljets_ge4j_ge4t_top25_Reco_ttbar_toplep_m"
    interf_ljets_ge4j_ge4t_top25_Reco_ttbar_toplep_m.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top25_Reco_ttbar_toplep_m)
    
    plots = init_plots(interfaces = interfaces)    
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_ge4j_ge4t_top30(data = None):
    label = "\geq 4 jets, \geq 4 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"


    interf_ljets_ge4j_ge4t_top30_CSV_2 = vhi.variableHistoInterface(variable_name  = "CSV[2]",
                                            label          = "ljets_ge4j_ge4t_top30_CSV_2",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_CSV_2.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_CSV_2","")
    interf_ljets_ge4j_ge4t_top30_CSV_2.category_label = label
    interf_ljets_ge4j_ge4t_top30_CSV_2.minxval = 0.277
    interf_ljets_ge4j_ge4t_top30_CSV_2.maxxval = 1.0
    interf_ljets_ge4j_ge4t_top30_CSV_2.histotitle = "CSV[2]"
    interf_ljets_ge4j_ge4t_top30_CSV_2.histoname = "ljets_ge4j_ge4t_top30_CSV_2"
    interf_ljets_ge4j_ge4t_top30_CSV_2.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top30_CSV_2)
    
    interf_ljets_ge4j_ge4t_top30_Evt_CSV_avg = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg",
                                            label          = "ljets_ge4j_ge4t_top30_Evt_CSV_avg",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_Evt_CSV_avg.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_Evt_CSV_avg","")
    interf_ljets_ge4j_ge4t_top30_Evt_CSV_avg.category_label = label
    interf_ljets_ge4j_ge4t_top30_Evt_CSV_avg.minxval = 0.15
    interf_ljets_ge4j_ge4t_top30_Evt_CSV_avg.maxxval = 1.0
    interf_ljets_ge4j_ge4t_top30_Evt_CSV_avg.histotitle = "Evt_CSV_avg"
    interf_ljets_ge4j_ge4t_top30_Evt_CSV_avg.histoname = "ljets_ge4j_ge4t_top30_Evt_CSV_avg"
    interf_ljets_ge4j_ge4t_top30_Evt_CSV_avg.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top30_Evt_CSV_avg)
    
    interf_ljets_ge4j_ge4t_top30_Evt_CSV_avg_tagged = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg_tagged",
                                            label          = "ljets_ge4j_ge4t_top30_Evt_CSV_avg_tagged",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_Evt_CSV_avg_tagged.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_Evt_CSV_avg_tagged","")
    interf_ljets_ge4j_ge4t_top30_Evt_CSV_avg_tagged.category_label = label
    interf_ljets_ge4j_ge4t_top30_Evt_CSV_avg_tagged.minxval = 0.3
    interf_ljets_ge4j_ge4t_top30_Evt_CSV_avg_tagged.maxxval = 1.0
    interf_ljets_ge4j_ge4t_top30_Evt_CSV_avg_tagged.histotitle = "Evt_CSV_avg_tagged"
    interf_ljets_ge4j_ge4t_top30_Evt_CSV_avg_tagged.histoname = "ljets_ge4j_ge4t_top30_Evt_CSV_avg_tagged"
    interf_ljets_ge4j_ge4t_top30_Evt_CSV_avg_tagged.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top30_Evt_CSV_avg_tagged)
    
    interf_ljets_ge4j_ge4t_top30_Evt_Deta_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Deta_JetsAverage",
                                            label          = "ljets_ge4j_ge4t_top30_Evt_Deta_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_Evt_Deta_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_Evt_Deta_JetsAverage","")
    interf_ljets_ge4j_ge4t_top30_Evt_Deta_JetsAverage.category_label = label
    interf_ljets_ge4j_ge4t_top30_Evt_Deta_JetsAverage.minxval = 0.0
    interf_ljets_ge4j_ge4t_top30_Evt_Deta_JetsAverage.maxxval = 3.0
    interf_ljets_ge4j_ge4t_top30_Evt_Deta_JetsAverage.histotitle = "Evt_Deta_JetsAverage"
    interf_ljets_ge4j_ge4t_top30_Evt_Deta_JetsAverage.histoname = "ljets_ge4j_ge4t_top30_Evt_Deta_JetsAverage"
    interf_ljets_ge4j_ge4t_top30_Evt_Deta_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top30_Evt_Deta_JetsAverage)
    
    interf_ljets_ge4j_ge4t_top30_Evt_Deta_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Deta_TaggedJetsAverage",
                                            label          = "ljets_ge4j_ge4t_top30_Evt_Deta_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_Evt_Deta_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_Evt_Deta_TaggedJetsAverage","")
    interf_ljets_ge4j_ge4t_top30_Evt_Deta_TaggedJetsAverage.category_label = label
    interf_ljets_ge4j_ge4t_top30_Evt_Deta_TaggedJetsAverage.minxval = 0.0
    interf_ljets_ge4j_ge4t_top30_Evt_Deta_TaggedJetsAverage.maxxval = 3.0
    interf_ljets_ge4j_ge4t_top30_Evt_Deta_TaggedJetsAverage.histotitle = "Evt_Deta_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_top30_Evt_Deta_TaggedJetsAverage.histoname = "ljets_ge4j_ge4t_top30_Evt_Deta_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_top30_Evt_Deta_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top30_Evt_Deta_TaggedJetsAverage)
    
    interf_ljets_ge4j_ge4t_top30_Evt_Dr_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Dr_TaggedJetsAverage",
                                            label          = "ljets_ge4j_ge4t_top30_Evt_Dr_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_Evt_Dr_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_Evt_Dr_TaggedJetsAverage","")
    interf_ljets_ge4j_ge4t_top30_Evt_Dr_TaggedJetsAverage.category_label = label
    interf_ljets_ge4j_ge4t_top30_Evt_Dr_TaggedJetsAverage.minxval = 0.5
    interf_ljets_ge4j_ge4t_top30_Evt_Dr_TaggedJetsAverage.maxxval = 3.5
    interf_ljets_ge4j_ge4t_top30_Evt_Dr_TaggedJetsAverage.histotitle = "average #DeltaR(tags)"
    interf_ljets_ge4j_ge4t_top30_Evt_Dr_TaggedJetsAverage.histoname = "ljets_ge4j_ge4t_top30_Evt_Dr_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_top30_Evt_Dr_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top30_Evt_Dr_TaggedJetsAverage)
    
    interf_ljets_ge4j_ge4t_top30_Evt_HT_jets = vhi.variableHistoInterface(variable_name  = "Evt_HT_jets",
                                            label          = "ljets_ge4j_ge4t_top30_Evt_HT_jets",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_Evt_HT_jets.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_Evt_HT_jets","")
    interf_ljets_ge4j_ge4t_top30_Evt_HT_jets.category_label = label
    interf_ljets_ge4j_ge4t_top30_Evt_HT_jets.minxval = 200.0
    interf_ljets_ge4j_ge4t_top30_Evt_HT_jets.maxxval = 1500.0
    interf_ljets_ge4j_ge4t_top30_Evt_HT_jets.histotitle = "H_{T}(jets)"
    interf_ljets_ge4j_ge4t_top30_Evt_HT_jets.histoname = "ljets_ge4j_ge4t_top30_Evt_HT_jets"
    interf_ljets_ge4j_ge4t_top30_Evt_HT_jets.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top30_Evt_HT_jets)
    
    interf_ljets_ge4j_ge4t_top30_Evt_HT_tags = vhi.variableHistoInterface(variable_name  = "Evt_HT_tags",
                                            label          = "ljets_ge4j_ge4t_top30_Evt_HT_tags",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_Evt_HT_tags.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_Evt_HT_tags","")
    interf_ljets_ge4j_ge4t_top30_Evt_HT_tags.category_label = label
    interf_ljets_ge4j_ge4t_top30_Evt_HT_tags.minxval = 100.0
    interf_ljets_ge4j_ge4t_top30_Evt_HT_tags.maxxval = 1000.0
    interf_ljets_ge4j_ge4t_top30_Evt_HT_tags.histotitle = "Evt_HT_tags"
    interf_ljets_ge4j_ge4t_top30_Evt_HT_tags.histoname = "ljets_ge4j_ge4t_top30_Evt_HT_tags"
    interf_ljets_ge4j_ge4t_top30_Evt_HT_tags.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top30_Evt_HT_tags)
    
    interf_ljets_ge4j_ge4t_top30_Evt_M2_minDrTaggedJets = vhi.variableHistoInterface(variable_name  = "Evt_M2_minDrTaggedJets",
                                            label          = "ljets_ge4j_ge4t_top30_Evt_M2_minDrTaggedJets",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_Evt_M2_minDrTaggedJets.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_Evt_M2_minDrTaggedJets","")
    interf_ljets_ge4j_ge4t_top30_Evt_M2_minDrTaggedJets.category_label = label
    interf_ljets_ge4j_ge4t_top30_Evt_M2_minDrTaggedJets.minxval = 0.0
    interf_ljets_ge4j_ge4t_top30_Evt_M2_minDrTaggedJets.maxxval = 400.0
    interf_ljets_ge4j_ge4t_top30_Evt_M2_minDrTaggedJets.histotitle = "M_{2}( min #DeltaR(tag,tag) )"
    interf_ljets_ge4j_ge4t_top30_Evt_M2_minDrTaggedJets.histoname = "ljets_ge4j_ge4t_top30_Evt_M2_minDrTaggedJets"
    interf_ljets_ge4j_ge4t_top30_Evt_M2_minDrTaggedJets.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top30_Evt_M2_minDrTaggedJets)
    
    interf_ljets_ge4j_ge4t_top30_Evt_M_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_M_JetsAverage",
                                            label          = "ljets_ge4j_ge4t_top30_Evt_M_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_Evt_M_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_Evt_M_JetsAverage","")
    interf_ljets_ge4j_ge4t_top30_Evt_M_JetsAverage.category_label = label
    interf_ljets_ge4j_ge4t_top30_Evt_M_JetsAverage.minxval = 5.0
    interf_ljets_ge4j_ge4t_top30_Evt_M_JetsAverage.maxxval = 50.0
    interf_ljets_ge4j_ge4t_top30_Evt_M_JetsAverage.histotitle = "Evt_M_JetsAverage"
    interf_ljets_ge4j_ge4t_top30_Evt_M_JetsAverage.histoname = "ljets_ge4j_ge4t_top30_Evt_M_JetsAverage"
    interf_ljets_ge4j_ge4t_top30_Evt_M_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top30_Evt_M_JetsAverage)
    
    interf_ljets_ge4j_ge4t_top30_Evt_M_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_M_TaggedJetsAverage",
                                            label          = "ljets_ge4j_ge4t_top30_Evt_M_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_Evt_M_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_Evt_M_TaggedJetsAverage","")
    interf_ljets_ge4j_ge4t_top30_Evt_M_TaggedJetsAverage.category_label = label
    interf_ljets_ge4j_ge4t_top30_Evt_M_TaggedJetsAverage.minxval = 5.0
    interf_ljets_ge4j_ge4t_top30_Evt_M_TaggedJetsAverage.maxxval = 70.0
    interf_ljets_ge4j_ge4t_top30_Evt_M_TaggedJetsAverage.histotitle = "Evt_M_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_top30_Evt_M_TaggedJetsAverage.histoname = "ljets_ge4j_ge4t_top30_Evt_M_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_top30_Evt_M_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top30_Evt_M_TaggedJetsAverage)
    
    interf_ljets_ge4j_ge4t_top30_Evt_M_minDrLepTag = vhi.variableHistoInterface(variable_name  = "Evt_M_minDrLepTag",
                                            label          = "ljets_ge4j_ge4t_top30_Evt_M_minDrLepTag",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_Evt_M_minDrLepTag.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_Evt_M_minDrLepTag","")
    interf_ljets_ge4j_ge4t_top30_Evt_M_minDrLepTag.category_label = label
    interf_ljets_ge4j_ge4t_top30_Evt_M_minDrLepTag.minxval = 15.0
    interf_ljets_ge4j_ge4t_top30_Evt_M_minDrLepTag.maxxval = 400.0
    interf_ljets_ge4j_ge4t_top30_Evt_M_minDrLepTag.histotitle = "Evt_M_minDrLepTag"
    interf_ljets_ge4j_ge4t_top30_Evt_M_minDrLepTag.histoname = "ljets_ge4j_ge4t_top30_Evt_M_minDrLepTag"
    interf_ljets_ge4j_ge4t_top30_Evt_M_minDrLepTag.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top30_Evt_M_minDrLepTag)
    
    interf_ljets_ge4j_ge4t_top30_Evt_Pt_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Pt_JetsAverage",
                                            label          = "ljets_ge4j_ge4t_top30_Evt_Pt_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_Evt_Pt_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_Evt_Pt_JetsAverage","")
    interf_ljets_ge4j_ge4t_top30_Evt_Pt_JetsAverage.category_label = label
    interf_ljets_ge4j_ge4t_top30_Evt_Pt_JetsAverage.minxval = 30.0
    interf_ljets_ge4j_ge4t_top30_Evt_Pt_JetsAverage.maxxval = 500.0
    interf_ljets_ge4j_ge4t_top30_Evt_Pt_JetsAverage.histotitle = "Evt_Pt_JetsAverage"
    interf_ljets_ge4j_ge4t_top30_Evt_Pt_JetsAverage.histoname = "ljets_ge4j_ge4t_top30_Evt_Pt_JetsAverage"
    interf_ljets_ge4j_ge4t_top30_Evt_Pt_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top30_Evt_Pt_JetsAverage)
    
    interf_ljets_ge4j_ge4t_top30_Evt_Pt_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Pt_TaggedJetsAverage",
                                            label          = "ljets_ge4j_ge4t_top30_Evt_Pt_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_Evt_Pt_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_Evt_Pt_TaggedJetsAverage","")
    interf_ljets_ge4j_ge4t_top30_Evt_Pt_TaggedJetsAverage.category_label = label
    interf_ljets_ge4j_ge4t_top30_Evt_Pt_TaggedJetsAverage.minxval = 30.0
    interf_ljets_ge4j_ge4t_top30_Evt_Pt_TaggedJetsAverage.maxxval = 600.0
    interf_ljets_ge4j_ge4t_top30_Evt_Pt_TaggedJetsAverage.histotitle = "Evt_Pt_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_top30_Evt_Pt_TaggedJetsAverage.histoname = "ljets_ge4j_ge4t_top30_Evt_Pt_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_top30_Evt_Pt_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top30_Evt_Pt_TaggedJetsAverage)
    
    interf_ljets_ge4j_ge4t_top30_Evt_Pt_minDrTaggedJets = vhi.variableHistoInterface(variable_name  = "Evt_Pt_minDrTaggedJets",
                                            label          = "ljets_ge4j_ge4t_top30_Evt_Pt_minDrTaggedJets",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_Evt_Pt_minDrTaggedJets.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_Evt_Pt_minDrTaggedJets","")
    interf_ljets_ge4j_ge4t_top30_Evt_Pt_minDrTaggedJets.category_label = label
    interf_ljets_ge4j_ge4t_top30_Evt_Pt_minDrTaggedJets.minxval = 20.0
    interf_ljets_ge4j_ge4t_top30_Evt_Pt_minDrTaggedJets.maxxval = 600.0
    interf_ljets_ge4j_ge4t_top30_Evt_Pt_minDrTaggedJets.histotitle = "Evt_Pt_minDrTaggedJets"
    interf_ljets_ge4j_ge4t_top30_Evt_Pt_minDrTaggedJets.histoname = "ljets_ge4j_ge4t_top30_Evt_Pt_minDrTaggedJets"
    interf_ljets_ge4j_ge4t_top30_Evt_Pt_minDrTaggedJets.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top30_Evt_Pt_minDrTaggedJets)
    
    interf_ljets_ge4j_ge4t_top30_Evt_blr_transformed = vhi.variableHistoInterface(variable_name  = "Evt_blr_transformed",
                                            label          = "ljets_ge4j_ge4t_top30_Evt_blr_transformed",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_Evt_blr_transformed.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_Evt_blr_transformed","")
    interf_ljets_ge4j_ge4t_top30_Evt_blr_transformed.category_label = label
    interf_ljets_ge4j_ge4t_top30_Evt_blr_transformed.minxval = -2.5
    interf_ljets_ge4j_ge4t_top30_Evt_blr_transformed.maxxval = 15.0
    interf_ljets_ge4j_ge4t_top30_Evt_blr_transformed.histotitle = "Evt_blr_transformed"
    interf_ljets_ge4j_ge4t_top30_Evt_blr_transformed.histoname = "ljets_ge4j_ge4t_top30_Evt_blr_transformed"
    interf_ljets_ge4j_ge4t_top30_Evt_blr_transformed.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top30_Evt_blr_transformed)
    
    interf_ljets_ge4j_ge4t_top30_Jet_Pt_0 = vhi.variableHistoInterface(variable_name  = "Jet_Pt[0]",
                                            label          = "ljets_ge4j_ge4t_top30_Jet_Pt_0",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_Jet_Pt_0.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_Jet_Pt_0","")
    interf_ljets_ge4j_ge4t_top30_Jet_Pt_0.category_label = label
    interf_ljets_ge4j_ge4t_top30_Jet_Pt_0.minxval = 0.0
    interf_ljets_ge4j_ge4t_top30_Jet_Pt_0.maxxval = 600.0
    interf_ljets_ge4j_ge4t_top30_Jet_Pt_0.histotitle = "p_{T} of leading jet"
    interf_ljets_ge4j_ge4t_top30_Jet_Pt_0.histoname = "ljets_ge4j_ge4t_top30_Jet_Pt_0"
    interf_ljets_ge4j_ge4t_top30_Jet_Pt_0.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top30_Jet_Pt_0)
    
    interf_ljets_ge4j_ge4t_top30_Jet_Pt_1 = vhi.variableHistoInterface(variable_name  = "Jet_Pt[1]",
                                            label          = "ljets_ge4j_ge4t_top30_Jet_Pt_1",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_Jet_Pt_1.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_Jet_Pt_1","")
    interf_ljets_ge4j_ge4t_top30_Jet_Pt_1.category_label = label
    interf_ljets_ge4j_ge4t_top30_Jet_Pt_1.minxval = 30.0
    interf_ljets_ge4j_ge4t_top30_Jet_Pt_1.maxxval = 500.0
    interf_ljets_ge4j_ge4t_top30_Jet_Pt_1.histotitle = "Jet_Pt[1]"
    interf_ljets_ge4j_ge4t_top30_Jet_Pt_1.histoname = "ljets_ge4j_ge4t_top30_Jet_Pt_1"
    interf_ljets_ge4j_ge4t_top30_Jet_Pt_1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top30_Jet_Pt_1)
    
    interf_ljets_ge4j_ge4t_top30_Jet_Pt_3 = vhi.variableHistoInterface(variable_name  = "Jet_Pt[3]",
                                            label          = "ljets_ge4j_ge4t_top30_Jet_Pt_3",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_Jet_Pt_3.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_Jet_Pt_3","")
    interf_ljets_ge4j_ge4t_top30_Jet_Pt_3.category_label = label
    interf_ljets_ge4j_ge4t_top30_Jet_Pt_3.minxval = 50.0
    interf_ljets_ge4j_ge4t_top30_Jet_Pt_3.maxxval = 200.0
    interf_ljets_ge4j_ge4t_top30_Jet_Pt_3.histotitle = "p_{T} of fourth jet"
    interf_ljets_ge4j_ge4t_top30_Jet_Pt_3.histoname = "ljets_ge4j_ge4t_top30_Jet_Pt_3"
    interf_ljets_ge4j_ge4t_top30_Jet_Pt_3.nhistobins = 30
    interfaces.append(interf_ljets_ge4j_ge4t_top30_Jet_Pt_3)
    
    interf_ljets_ge4j_ge4t_top30_N_Jets = vhi.variableHistoInterface(variable_name  = "N_Jets",
                                            label          = "ljets_ge4j_ge4t_top30_N_Jets",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_N_Jets.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_N_Jets","")
    interf_ljets_ge4j_ge4t_top30_N_Jets.category_label = label
    interf_ljets_ge4j_ge4t_top30_N_Jets.minxval = 3.5
    interf_ljets_ge4j_ge4t_top30_N_Jets.maxxval = 10.5
    interf_ljets_ge4j_ge4t_top30_N_Jets.histotitle = "N_Jets"
    interf_ljets_ge4j_ge4t_top30_N_Jets.histoname = "ljets_ge4j_ge4t_top30_N_Jets"
    interf_ljets_ge4j_ge4t_top30_N_Jets.nhistobins = 7
    interfaces.append(interf_ljets_ge4j_ge4t_top30_N_Jets)
    
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHW_Jet_CSV_btop = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_Jet_CSV_btop",
                                            label          = "ljets_ge4j_ge4t_top30_Reco_JABDT_tHW_Jet_CSV_btop",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHW_Jet_CSV_btop.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_Reco_JABDT_tHW_Jet_CSV_btop","")
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHW_Jet_CSV_btop.category_label = label
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHW_Jet_CSV_btop.minxval = -1.5
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHW_Jet_CSV_btop.maxxval = 1.0
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHW_Jet_CSV_btop.histotitle = "Reco_JABDT_tHW_Jet_CSV_btop"
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHW_Jet_CSV_btop.histoname = "ljets_ge4j_ge4t_top30_Reco_JABDT_tHW_Jet_CSV_btop"
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHW_Jet_CSV_btop.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHW_Jet_CSV_btop)
    
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",
                                            label          = "ljets_ge4j_ge4t_top30_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt","")
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.category_label = label
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.minxval = -1.5
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.maxxval = 1.0
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.histotitle = "Reco_JABDT_tHW_energy_fraction"
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.histoname = "ljets_ge4j_ge4t_top30_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt"
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt)
    
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHq_Jet_CSV_hdau1 = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHq_Jet_CSV_hdau1",
                                            label          = "ljets_ge4j_ge4t_top30_Reco_JABDT_tHq_Jet_CSV_hdau1",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHq_Jet_CSV_hdau1.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_Reco_JABDT_tHq_Jet_CSV_hdau1","")
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHq_Jet_CSV_hdau1.category_label = label
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHq_Jet_CSV_hdau1.minxval = -1.5
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHq_Jet_CSV_hdau1.maxxval = 1.0
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHq_Jet_CSV_hdau1.histotitle = "Reco_JABDT_tHq_Jet_CSV_hdau1"
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHq_Jet_CSV_hdau1.histoname = "ljets_ge4j_ge4t_top30_Reco_JABDT_tHq_Jet_CSV_hdau1"
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHq_Jet_CSV_hdau1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHq_Jet_CSV_hdau1)
    
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHq_abs_ljet_eta = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHq_abs_ljet_eta",
                                            label          = "ljets_ge4j_ge4t_top30_Reco_JABDT_tHq_abs_ljet_eta",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHq_abs_ljet_eta.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_Reco_JABDT_tHq_abs_ljet_eta","")
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHq_abs_ljet_eta.category_label = label
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHq_abs_ljet_eta.minxval = -1.5
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHq_abs_ljet_eta.maxxval = 4.5
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHq_abs_ljet_eta.histotitle = "Reco_JABDT_tHq_abs_ljet_eta"
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHq_abs_ljet_eta.histoname = "ljets_ge4j_ge4t_top30_Reco_JABDT_tHq_abs_ljet_eta"
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHq_abs_ljet_eta.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top30_Reco_JABDT_tHq_abs_ljet_eta)
    
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_ttH_Jet_CSV_hdau2 = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttH_Jet_CSV_hdau2",
                                            label          = "ljets_ge4j_ge4t_top30_Reco_JABDT_ttH_Jet_CSV_hdau2",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_ttH_Jet_CSV_hdau2.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_Reco_JABDT_ttH_Jet_CSV_hdau2","")
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_ttH_Jet_CSV_hdau2.category_label = label
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_ttH_Jet_CSV_hdau2.minxval = -1.5
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_ttH_Jet_CSV_hdau2.maxxval = 1.0
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_ttH_Jet_CSV_hdau2.histotitle = "Reco_JABDT_ttH_Jet_CSV_hdau2"
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_ttH_Jet_CSV_hdau2.histoname = "ljets_ge4j_ge4t_top30_Reco_JABDT_ttH_Jet_CSV_hdau2"
    interf_ljets_ge4j_ge4t_top30_Reco_JABDT_ttH_Jet_CSV_hdau2.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top30_Reco_JABDT_ttH_Jet_CSV_hdau2)
    
    interf_ljets_ge4j_ge4t_top30_Reco_tHq_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_tHq_bestJABDToutput",
                                            label          = "ljets_ge4j_ge4t_top30_Reco_tHq_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_Reco_tHq_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_Reco_tHq_bestJABDToutput","")
    interf_ljets_ge4j_ge4t_top30_Reco_tHq_bestJABDToutput.category_label = label
    interf_ljets_ge4j_ge4t_top30_Reco_tHq_bestJABDToutput.minxval = -1.0
    interf_ljets_ge4j_ge4t_top30_Reco_tHq_bestJABDToutput.maxxval = 0.7
    interf_ljets_ge4j_ge4t_top30_Reco_tHq_bestJABDToutput.histotitle = "Reco_tHq_bestJABDToutput"
    interf_ljets_ge4j_ge4t_top30_Reco_tHq_bestJABDToutput.histoname = "ljets_ge4j_ge4t_top30_Reco_tHq_bestJABDToutput"
    interf_ljets_ge4j_ge4t_top30_Reco_tHq_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top30_Reco_tHq_bestJABDToutput)
    
    interf_ljets_ge4j_ge4t_top30_Reco_ttH_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_ttH_bestJABDToutput",
                                            label          = "ljets_ge4j_ge4t_top30_Reco_ttH_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_Reco_ttH_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_Reco_ttH_bestJABDToutput","")
    interf_ljets_ge4j_ge4t_top30_Reco_ttH_bestJABDToutput.category_label = label
    interf_ljets_ge4j_ge4t_top30_Reco_ttH_bestJABDToutput.minxval = -1.0
    interf_ljets_ge4j_ge4t_top30_Reco_ttH_bestJABDToutput.maxxval = 0.7
    interf_ljets_ge4j_ge4t_top30_Reco_ttH_bestJABDToutput.histotitle = "Reco_ttH_bestJABDToutput"
    interf_ljets_ge4j_ge4t_top30_Reco_ttH_bestJABDToutput.histoname = "ljets_ge4j_ge4t_top30_Reco_ttH_bestJABDToutput"
    interf_ljets_ge4j_ge4t_top30_Reco_ttH_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top30_Reco_ttH_bestJABDToutput)
    
    interf_ljets_ge4j_ge4t_top30_Reco_ttH_toplep_m = vhi.variableHistoInterface(variable_name  = "Reco_ttH_toplep_m",
                                            label          = "ljets_ge4j_ge4t_top30_Reco_ttH_toplep_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_Reco_ttH_toplep_m.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_Reco_ttH_toplep_m","")
    interf_ljets_ge4j_ge4t_top30_Reco_ttH_toplep_m.category_label = label
    interf_ljets_ge4j_ge4t_top30_Reco_ttH_toplep_m.minxval = -1.5
    interf_ljets_ge4j_ge4t_top30_Reco_ttH_toplep_m.maxxval = 750.0
    interf_ljets_ge4j_ge4t_top30_Reco_ttH_toplep_m.histotitle = "Reco_ttH_toplep_m"
    interf_ljets_ge4j_ge4t_top30_Reco_ttH_toplep_m.histoname = "ljets_ge4j_ge4t_top30_Reco_ttH_toplep_m"
    interf_ljets_ge4j_ge4t_top30_Reco_ttH_toplep_m.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top30_Reco_ttH_toplep_m)
    
    interf_ljets_ge4j_ge4t_top30_Reco_ttbar_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_ttbar_bestJABDToutput",
                                            label          = "ljets_ge4j_ge4t_top30_Reco_ttbar_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_Reco_ttbar_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_Reco_ttbar_bestJABDToutput","")
    interf_ljets_ge4j_ge4t_top30_Reco_ttbar_bestJABDToutput.category_label = label
    interf_ljets_ge4j_ge4t_top30_Reco_ttbar_bestJABDToutput.minxval = -0.4
    interf_ljets_ge4j_ge4t_top30_Reco_ttbar_bestJABDToutput.maxxval = 0.7
    interf_ljets_ge4j_ge4t_top30_Reco_ttbar_bestJABDToutput.histotitle = "Reco_ttbar_bestJABDToutput"
    interf_ljets_ge4j_ge4t_top30_Reco_ttbar_bestJABDToutput.histoname = "ljets_ge4j_ge4t_top30_Reco_ttbar_bestJABDToutput"
    interf_ljets_ge4j_ge4t_top30_Reco_ttbar_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top30_Reco_ttbar_bestJABDToutput)
    
    interf_ljets_ge4j_ge4t_top30_Reco_ttbar_toplep_m = vhi.variableHistoInterface(variable_name  = "Reco_ttbar_toplep_m",
                                            label          = "ljets_ge4j_ge4t_top30_Reco_ttbar_toplep_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_top30_Reco_ttbar_toplep_m.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_top30_Reco_ttbar_toplep_m","")
    interf_ljets_ge4j_ge4t_top30_Reco_ttbar_toplep_m.category_label = label
    interf_ljets_ge4j_ge4t_top30_Reco_ttbar_toplep_m.minxval = 80.0
    interf_ljets_ge4j_ge4t_top30_Reco_ttbar_toplep_m.maxxval = 500.0
    interf_ljets_ge4j_ge4t_top30_Reco_ttbar_toplep_m.histotitle = "Reco_ttbar_toplep_m"
    interf_ljets_ge4j_ge4t_top30_Reco_ttbar_toplep_m.histoname = "ljets_ge4j_ge4t_top30_Reco_ttbar_toplep_m"
    interf_ljets_ge4j_ge4t_top30_Reco_ttbar_toplep_m.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_top30_Reco_ttbar_toplep_m)
    
    plots = init_plots(interfaces = interfaces)    
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_ge4j_3t_top20(data = None):
    label = "\geq 4 jets, 3 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM==3)&&(1.)"


    interf_ljets_ge4j_3t_top20_Evt_CSV_avg = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg",
                                            label          = "ljets_ge4j_3t_top20_Evt_CSV_avg",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top20_Evt_CSV_avg.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top20_Evt_CSV_avg","")
    interf_ljets_ge4j_3t_top20_Evt_CSV_avg.category_label = label
    interf_ljets_ge4j_3t_top20_Evt_CSV_avg.minxval = 0.15
    interf_ljets_ge4j_3t_top20_Evt_CSV_avg.maxxval = 1.0
    interf_ljets_ge4j_3t_top20_Evt_CSV_avg.histotitle = "Evt_CSV_avg"
    interf_ljets_ge4j_3t_top20_Evt_CSV_avg.histoname = "ljets_ge4j_3t_top20_Evt_CSV_avg"
    interf_ljets_ge4j_3t_top20_Evt_CSV_avg.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top20_Evt_CSV_avg)
    
    interf_ljets_ge4j_3t_top20_Evt_CSV_avg_tagged = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg_tagged",
                                            label          = "ljets_ge4j_3t_top20_Evt_CSV_avg_tagged",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top20_Evt_CSV_avg_tagged.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top20_Evt_CSV_avg_tagged","")
    interf_ljets_ge4j_3t_top20_Evt_CSV_avg_tagged.category_label = label
    interf_ljets_ge4j_3t_top20_Evt_CSV_avg_tagged.minxval = 0.3
    interf_ljets_ge4j_3t_top20_Evt_CSV_avg_tagged.maxxval = 1.0
    interf_ljets_ge4j_3t_top20_Evt_CSV_avg_tagged.histotitle = "Evt_CSV_avg_tagged"
    interf_ljets_ge4j_3t_top20_Evt_CSV_avg_tagged.histoname = "ljets_ge4j_3t_top20_Evt_CSV_avg_tagged"
    interf_ljets_ge4j_3t_top20_Evt_CSV_avg_tagged.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top20_Evt_CSV_avg_tagged)
    
    interf_ljets_ge4j_3t_top20_Evt_HT_jets = vhi.variableHistoInterface(variable_name  = "Evt_HT_jets",
                                            label          = "ljets_ge4j_3t_top20_Evt_HT_jets",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top20_Evt_HT_jets.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top20_Evt_HT_jets","")
    interf_ljets_ge4j_3t_top20_Evt_HT_jets.category_label = label
    interf_ljets_ge4j_3t_top20_Evt_HT_jets.minxval = 200.0
    interf_ljets_ge4j_3t_top20_Evt_HT_jets.maxxval = 1500.0
    interf_ljets_ge4j_3t_top20_Evt_HT_jets.histotitle = "H_{T}(jets)"
    interf_ljets_ge4j_3t_top20_Evt_HT_jets.histoname = "ljets_ge4j_3t_top20_Evt_HT_jets"
    interf_ljets_ge4j_3t_top20_Evt_HT_jets.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top20_Evt_HT_jets)
    
    interf_ljets_ge4j_3t_top20_Evt_HT_tags = vhi.variableHistoInterface(variable_name  = "Evt_HT_tags",
                                            label          = "ljets_ge4j_3t_top20_Evt_HT_tags",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top20_Evt_HT_tags.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top20_Evt_HT_tags","")
    interf_ljets_ge4j_3t_top20_Evt_HT_tags.category_label = label
    interf_ljets_ge4j_3t_top20_Evt_HT_tags.minxval = 100.0
    interf_ljets_ge4j_3t_top20_Evt_HT_tags.maxxval = 1000.0
    interf_ljets_ge4j_3t_top20_Evt_HT_tags.histotitle = "Evt_HT_tags"
    interf_ljets_ge4j_3t_top20_Evt_HT_tags.histoname = "ljets_ge4j_3t_top20_Evt_HT_tags"
    interf_ljets_ge4j_3t_top20_Evt_HT_tags.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top20_Evt_HT_tags)
    
    interf_ljets_ge4j_3t_top20_Evt_JetPt_over_JetE = vhi.variableHistoInterface(variable_name  = "Evt_JetPt_over_JetE",
                                            label          = "ljets_ge4j_3t_top20_Evt_JetPt_over_JetE",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top20_Evt_JetPt_over_JetE.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top20_Evt_JetPt_over_JetE","")
    interf_ljets_ge4j_3t_top20_Evt_JetPt_over_JetE.category_label = label
    interf_ljets_ge4j_3t_top20_Evt_JetPt_over_JetE.minxval = 0.0
    interf_ljets_ge4j_3t_top20_Evt_JetPt_over_JetE.maxxval = 1.0
    interf_ljets_ge4j_3t_top20_Evt_JetPt_over_JetE.histotitle = "Evt_JetPt_over_JetE"
    interf_ljets_ge4j_3t_top20_Evt_JetPt_over_JetE.histoname = "ljets_ge4j_3t_top20_Evt_JetPt_over_JetE"
    interf_ljets_ge4j_3t_top20_Evt_JetPt_over_JetE.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top20_Evt_JetPt_over_JetE)
    
    interf_ljets_ge4j_3t_top20_Evt_M_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_M_JetsAverage",
                                            label          = "ljets_ge4j_3t_top20_Evt_M_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top20_Evt_M_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top20_Evt_M_JetsAverage","")
    interf_ljets_ge4j_3t_top20_Evt_M_JetsAverage.category_label = label
    interf_ljets_ge4j_3t_top20_Evt_M_JetsAverage.minxval = 5.0
    interf_ljets_ge4j_3t_top20_Evt_M_JetsAverage.maxxval = 50.0
    interf_ljets_ge4j_3t_top20_Evt_M_JetsAverage.histotitle = "Evt_M_JetsAverage"
    interf_ljets_ge4j_3t_top20_Evt_M_JetsAverage.histoname = "ljets_ge4j_3t_top20_Evt_M_JetsAverage"
    interf_ljets_ge4j_3t_top20_Evt_M_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top20_Evt_M_JetsAverage)
    
    interf_ljets_ge4j_3t_top20_Evt_M_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_M_TaggedJetsAverage",
                                            label          = "ljets_ge4j_3t_top20_Evt_M_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top20_Evt_M_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top20_Evt_M_TaggedJetsAverage","")
    interf_ljets_ge4j_3t_top20_Evt_M_TaggedJetsAverage.category_label = label
    interf_ljets_ge4j_3t_top20_Evt_M_TaggedJetsAverage.minxval = 5.0
    interf_ljets_ge4j_3t_top20_Evt_M_TaggedJetsAverage.maxxval = 70.0
    interf_ljets_ge4j_3t_top20_Evt_M_TaggedJetsAverage.histotitle = "Evt_M_TaggedJetsAverage"
    interf_ljets_ge4j_3t_top20_Evt_M_TaggedJetsAverage.histoname = "ljets_ge4j_3t_top20_Evt_M_TaggedJetsAverage"
    interf_ljets_ge4j_3t_top20_Evt_M_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top20_Evt_M_TaggedJetsAverage)
    
    interf_ljets_ge4j_3t_top20_Evt_M_Total = vhi.variableHistoInterface(variable_name  = "Evt_M_Total",
                                            label          = "ljets_ge4j_3t_top20_Evt_M_Total",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top20_Evt_M_Total.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top20_Evt_M_Total","")
    interf_ljets_ge4j_3t_top20_Evt_M_Total.category_label = label
    interf_ljets_ge4j_3t_top20_Evt_M_Total.minxval = 200.0
    interf_ljets_ge4j_3t_top20_Evt_M_Total.maxxval = 3000.0
    interf_ljets_ge4j_3t_top20_Evt_M_Total.histotitle = "Evt_M_Total"
    interf_ljets_ge4j_3t_top20_Evt_M_Total.histoname = "ljets_ge4j_3t_top20_Evt_M_Total"
    interf_ljets_ge4j_3t_top20_Evt_M_Total.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top20_Evt_M_Total)
    
    interf_ljets_ge4j_3t_top20_Evt_Pt_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Pt_TaggedJetsAverage",
                                            label          = "ljets_ge4j_3t_top20_Evt_Pt_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top20_Evt_Pt_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top20_Evt_Pt_TaggedJetsAverage","")
    interf_ljets_ge4j_3t_top20_Evt_Pt_TaggedJetsAverage.category_label = label
    interf_ljets_ge4j_3t_top20_Evt_Pt_TaggedJetsAverage.minxval = 30.0
    interf_ljets_ge4j_3t_top20_Evt_Pt_TaggedJetsAverage.maxxval = 600.0
    interf_ljets_ge4j_3t_top20_Evt_Pt_TaggedJetsAverage.histotitle = "Evt_Pt_TaggedJetsAverage"
    interf_ljets_ge4j_3t_top20_Evt_Pt_TaggedJetsAverage.histoname = "ljets_ge4j_3t_top20_Evt_Pt_TaggedJetsAverage"
    interf_ljets_ge4j_3t_top20_Evt_Pt_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top20_Evt_Pt_TaggedJetsAverage)
    
    interf_ljets_ge4j_3t_top20_Evt_blr_transformed = vhi.variableHistoInterface(variable_name  = "Evt_blr_transformed",
                                            label          = "ljets_ge4j_3t_top20_Evt_blr_transformed",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top20_Evt_blr_transformed.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top20_Evt_blr_transformed","")
    interf_ljets_ge4j_3t_top20_Evt_blr_transformed.category_label = label
    interf_ljets_ge4j_3t_top20_Evt_blr_transformed.minxval = -2.5
    interf_ljets_ge4j_3t_top20_Evt_blr_transformed.maxxval = 15.0
    interf_ljets_ge4j_3t_top20_Evt_blr_transformed.histotitle = "Evt_blr_transformed"
    interf_ljets_ge4j_3t_top20_Evt_blr_transformed.histoname = "ljets_ge4j_3t_top20_Evt_blr_transformed"
    interf_ljets_ge4j_3t_top20_Evt_blr_transformed.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top20_Evt_blr_transformed)
    
    interf_ljets_ge4j_3t_top20_Evt_h1 = vhi.variableHistoInterface(variable_name  = "Evt_h1",
                                            label          = "ljets_ge4j_3t_top20_Evt_h1",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top20_Evt_h1.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top20_Evt_h1","")
    interf_ljets_ge4j_3t_top20_Evt_h1.category_label = label
    interf_ljets_ge4j_3t_top20_Evt_h1.minxval = -0.2
    interf_ljets_ge4j_3t_top20_Evt_h1.maxxval = 0.4
    interf_ljets_ge4j_3t_top20_Evt_h1.histotitle = "Evt_h1"
    interf_ljets_ge4j_3t_top20_Evt_h1.histoname = "ljets_ge4j_3t_top20_Evt_h1"
    interf_ljets_ge4j_3t_top20_Evt_h1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top20_Evt_h1)
    
    interf_ljets_ge4j_3t_top20_Jet_Pt_0 = vhi.variableHistoInterface(variable_name  = "Jet_Pt[0]",
                                            label          = "ljets_ge4j_3t_top20_Jet_Pt_0",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top20_Jet_Pt_0.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top20_Jet_Pt_0","")
    interf_ljets_ge4j_3t_top20_Jet_Pt_0.category_label = label
    interf_ljets_ge4j_3t_top20_Jet_Pt_0.minxval = 0.0
    interf_ljets_ge4j_3t_top20_Jet_Pt_0.maxxval = 600.0
    interf_ljets_ge4j_3t_top20_Jet_Pt_0.histotitle = "p_{T} of leading jet"
    interf_ljets_ge4j_3t_top20_Jet_Pt_0.histoname = "ljets_ge4j_3t_top20_Jet_Pt_0"
    interf_ljets_ge4j_3t_top20_Jet_Pt_0.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top20_Jet_Pt_0)
    
    interf_ljets_ge4j_3t_top20_N_Jets = vhi.variableHistoInterface(variable_name  = "N_Jets",
                                            label          = "ljets_ge4j_3t_top20_N_Jets",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top20_N_Jets.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top20_N_Jets","")
    interf_ljets_ge4j_3t_top20_N_Jets.category_label = label
    interf_ljets_ge4j_3t_top20_N_Jets.minxval = 3.5
    interf_ljets_ge4j_3t_top20_N_Jets.maxxval = 10.5
    interf_ljets_ge4j_3t_top20_N_Jets.histotitle = "N_Jets"
    interf_ljets_ge4j_3t_top20_N_Jets.histoname = "ljets_ge4j_3t_top20_N_Jets"
    interf_ljets_ge4j_3t_top20_N_Jets.nhistobins = 7
    interfaces.append(interf_ljets_ge4j_3t_top20_N_Jets)
    
    interf_ljets_ge4j_3t_top20_Reco_JABDT_tHW_Jet_CSV_btop = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_Jet_CSV_btop",
                                            label          = "ljets_ge4j_3t_top20_Reco_JABDT_tHW_Jet_CSV_btop",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top20_Reco_JABDT_tHW_Jet_CSV_btop.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top20_Reco_JABDT_tHW_Jet_CSV_btop","")
    interf_ljets_ge4j_3t_top20_Reco_JABDT_tHW_Jet_CSV_btop.category_label = label
    interf_ljets_ge4j_3t_top20_Reco_JABDT_tHW_Jet_CSV_btop.minxval = -1.5
    interf_ljets_ge4j_3t_top20_Reco_JABDT_tHW_Jet_CSV_btop.maxxval = 1.0
    interf_ljets_ge4j_3t_top20_Reco_JABDT_tHW_Jet_CSV_btop.histotitle = "Reco_JABDT_tHW_Jet_CSV_btop"
    interf_ljets_ge4j_3t_top20_Reco_JABDT_tHW_Jet_CSV_btop.histoname = "ljets_ge4j_3t_top20_Reco_JABDT_tHW_Jet_CSV_btop"
    interf_ljets_ge4j_3t_top20_Reco_JABDT_tHW_Jet_CSV_btop.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top20_Reco_JABDT_tHW_Jet_CSV_btop)
    
    interf_ljets_ge4j_3t_top20_Reco_JABDT_tHW_Jet_CSV_whaddau1 = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_Jet_CSV_whaddau1",
                                            label          = "ljets_ge4j_3t_top20_Reco_JABDT_tHW_Jet_CSV_whaddau1",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top20_Reco_JABDT_tHW_Jet_CSV_whaddau1.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top20_Reco_JABDT_tHW_Jet_CSV_whaddau1","")
    interf_ljets_ge4j_3t_top20_Reco_JABDT_tHW_Jet_CSV_whaddau1.category_label = label
    interf_ljets_ge4j_3t_top20_Reco_JABDT_tHW_Jet_CSV_whaddau1.minxval = -1.5
    interf_ljets_ge4j_3t_top20_Reco_JABDT_tHW_Jet_CSV_whaddau1.maxxval = 1.0
    interf_ljets_ge4j_3t_top20_Reco_JABDT_tHW_Jet_CSV_whaddau1.histotitle = "Reco_JABDT_tHW_Jet_CSV_whaddau1"
    interf_ljets_ge4j_3t_top20_Reco_JABDT_tHW_Jet_CSV_whaddau1.histoname = "ljets_ge4j_3t_top20_Reco_JABDT_tHW_Jet_CSV_whaddau1"
    interf_ljets_ge4j_3t_top20_Reco_JABDT_tHW_Jet_CSV_whaddau1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top20_Reco_JABDT_tHW_Jet_CSV_whaddau1)
    
    interf_ljets_ge4j_3t_top20_Reco_JABDT_ttH_Jet_CSV_btoplep = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttH_Jet_CSV_btoplep",
                                            label          = "ljets_ge4j_3t_top20_Reco_JABDT_ttH_Jet_CSV_btoplep",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top20_Reco_JABDT_ttH_Jet_CSV_btoplep.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top20_Reco_JABDT_ttH_Jet_CSV_btoplep","")
    interf_ljets_ge4j_3t_top20_Reco_JABDT_ttH_Jet_CSV_btoplep.category_label = label
    interf_ljets_ge4j_3t_top20_Reco_JABDT_ttH_Jet_CSV_btoplep.minxval = -1.5
    interf_ljets_ge4j_3t_top20_Reco_JABDT_ttH_Jet_CSV_btoplep.maxxval = 1.0
    interf_ljets_ge4j_3t_top20_Reco_JABDT_ttH_Jet_CSV_btoplep.histotitle = "Reco_JABDT_ttH_Jet_CSV_btoplep"
    interf_ljets_ge4j_3t_top20_Reco_JABDT_ttH_Jet_CSV_btoplep.histoname = "ljets_ge4j_3t_top20_Reco_JABDT_ttH_Jet_CSV_btoplep"
    interf_ljets_ge4j_3t_top20_Reco_JABDT_ttH_Jet_CSV_btoplep.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top20_Reco_JABDT_ttH_Jet_CSV_btoplep)
    
    interf_ljets_ge4j_3t_top20_Reco_tHW_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_tHW_bestJABDToutput",
                                            label          = "ljets_ge4j_3t_top20_Reco_tHW_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top20_Reco_tHW_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top20_Reco_tHW_bestJABDToutput","")
    interf_ljets_ge4j_3t_top20_Reco_tHW_bestJABDToutput.category_label = label
    interf_ljets_ge4j_3t_top20_Reco_tHW_bestJABDToutput.minxval = -1.0
    interf_ljets_ge4j_3t_top20_Reco_tHW_bestJABDToutput.maxxval = 0.6
    interf_ljets_ge4j_3t_top20_Reco_tHW_bestJABDToutput.histotitle = "Reco_tHW_bestJABDToutput"
    interf_ljets_ge4j_3t_top20_Reco_tHW_bestJABDToutput.histoname = "ljets_ge4j_3t_top20_Reco_tHW_bestJABDToutput"
    interf_ljets_ge4j_3t_top20_Reco_tHW_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top20_Reco_tHW_bestJABDToutput)
    
    interf_ljets_ge4j_3t_top20_Reco_ttH_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_ttH_bestJABDToutput",
                                            label          = "ljets_ge4j_3t_top20_Reco_ttH_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top20_Reco_ttH_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top20_Reco_ttH_bestJABDToutput","")
    interf_ljets_ge4j_3t_top20_Reco_ttH_bestJABDToutput.category_label = label
    interf_ljets_ge4j_3t_top20_Reco_ttH_bestJABDToutput.minxval = -1.0
    interf_ljets_ge4j_3t_top20_Reco_ttH_bestJABDToutput.maxxval = 0.7
    interf_ljets_ge4j_3t_top20_Reco_ttH_bestJABDToutput.histotitle = "Reco_ttH_bestJABDToutput"
    interf_ljets_ge4j_3t_top20_Reco_ttH_bestJABDToutput.histoname = "ljets_ge4j_3t_top20_Reco_ttH_bestJABDToutput"
    interf_ljets_ge4j_3t_top20_Reco_ttH_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top20_Reco_ttH_bestJABDToutput)
    
    interf_ljets_ge4j_3t_top20_Reco_ttbar_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_ttbar_bestJABDToutput",
                                            label          = "ljets_ge4j_3t_top20_Reco_ttbar_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top20_Reco_ttbar_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top20_Reco_ttbar_bestJABDToutput","")
    interf_ljets_ge4j_3t_top20_Reco_ttbar_bestJABDToutput.category_label = label
    interf_ljets_ge4j_3t_top20_Reco_ttbar_bestJABDToutput.minxval = -0.4
    interf_ljets_ge4j_3t_top20_Reco_ttbar_bestJABDToutput.maxxval = 0.7
    interf_ljets_ge4j_3t_top20_Reco_ttbar_bestJABDToutput.histotitle = "Reco_ttbar_bestJABDToutput"
    interf_ljets_ge4j_3t_top20_Reco_ttbar_bestJABDToutput.histoname = "ljets_ge4j_3t_top20_Reco_ttbar_bestJABDToutput"
    interf_ljets_ge4j_3t_top20_Reco_ttbar_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top20_Reco_ttbar_bestJABDToutput)
    
    plots = init_plots(interfaces = interfaces)    
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_ge4j_3t_top25(data = None):
    label = "\geq 4 jets, 3 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM==3)&&(1.)"


    interf_ljets_ge4j_3t_top25_Evt_CSV_avg = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg",
                                            label          = "ljets_ge4j_3t_top25_Evt_CSV_avg",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top25_Evt_CSV_avg.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top25_Evt_CSV_avg","")
    interf_ljets_ge4j_3t_top25_Evt_CSV_avg.category_label = label
    interf_ljets_ge4j_3t_top25_Evt_CSV_avg.bin_edges = [ 
                0.15,
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
                0.796,
                1.0
                ]
    interf_ljets_ge4j_3t_top25_Evt_CSV_avg.histotitle = "Evt_CSV_avg"
    interf_ljets_ge4j_3t_top25_Evt_CSV_avg.histoname = "ljets_ge4j_3t_top25_Evt_CSV_avg"
    interf_ljets_ge4j_3t_top25_Evt_CSV_avg.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top25_Evt_CSV_avg)
    
    interf_ljets_ge4j_3t_top25_Evt_CSV_avg_tagged = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg_tagged",
                                            label          = "ljets_ge4j_3t_top25_Evt_CSV_avg_tagged",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top25_Evt_CSV_avg_tagged.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top25_Evt_CSV_avg_tagged","")
    interf_ljets_ge4j_3t_top25_Evt_CSV_avg_tagged.category_label = label
    interf_ljets_ge4j_3t_top25_Evt_CSV_avg_tagged.bin_edges = [ 
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
    interf_ljets_ge4j_3t_top25_Evt_CSV_avg_tagged.histotitle = "Evt_CSV_avg_tagged"
    interf_ljets_ge4j_3t_top25_Evt_CSV_avg_tagged.histoname = "ljets_ge4j_3t_top25_Evt_CSV_avg_tagged"
    interf_ljets_ge4j_3t_top25_Evt_CSV_avg_tagged.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top25_Evt_CSV_avg_tagged)
    
    interf_ljets_ge4j_3t_top25_Evt_CSV_dev = vhi.variableHistoInterface(variable_name  = "Evt_CSV_dev",
                                            label          = "ljets_ge4j_3t_top25_Evt_CSV_dev",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top25_Evt_CSV_dev.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top25_Evt_CSV_dev","")
    interf_ljets_ge4j_3t_top25_Evt_CSV_dev.category_label = label
    interf_ljets_ge4j_3t_top25_Evt_CSV_dev.bin_edges = [ 
                0.005,
                0.01,
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
                0.24,
                0.245,
                0.25
                ]
    interf_ljets_ge4j_3t_top25_Evt_CSV_dev.histotitle = "Evt_CSV_dev"
    interf_ljets_ge4j_3t_top25_Evt_CSV_dev.histoname = "ljets_ge4j_3t_top25_Evt_CSV_dev"
    interf_ljets_ge4j_3t_top25_Evt_CSV_dev.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top25_Evt_CSV_dev)
    
    interf_ljets_ge4j_3t_top25_Evt_Dr_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Dr_TaggedJetsAverage",
                                            label          = "ljets_ge4j_3t_top25_Evt_Dr_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top25_Evt_Dr_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top25_Evt_Dr_TaggedJetsAverage","")
    interf_ljets_ge4j_3t_top25_Evt_Dr_TaggedJetsAverage.category_label = label
    interf_ljets_ge4j_3t_top25_Evt_Dr_TaggedJetsAverage.bin_edges = [ 
                0.56,
                0.62,
                0.68,
                0.74,
                0.8,
                0.86,
                0.92,
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
    interf_ljets_ge4j_3t_top25_Evt_Dr_TaggedJetsAverage.histotitle = "average #DeltaR(tags)"
    interf_ljets_ge4j_3t_top25_Evt_Dr_TaggedJetsAverage.histoname = "ljets_ge4j_3t_top25_Evt_Dr_TaggedJetsAverage"
    interf_ljets_ge4j_3t_top25_Evt_Dr_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top25_Evt_Dr_TaggedJetsAverage)
    
    interf_ljets_ge4j_3t_top25_Evt_HT_jets = vhi.variableHistoInterface(variable_name  = "Evt_HT_jets",
                                            label          = "ljets_ge4j_3t_top25_Evt_HT_jets",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top25_Evt_HT_jets.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top25_Evt_HT_jets","")
    interf_ljets_ge4j_3t_top25_Evt_HT_jets.category_label = label
    interf_ljets_ge4j_3t_top25_Evt_HT_jets.bin_edges = [ 
                200.0,
                226.0,
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
                1136.0,
                1162.0,
                1188.0,
                1214.0,
                1240.0,
                1266.0,
                1292.0,
                1318.0,
                1344.0,
                1370.0,
                1396.0,
                1422.0,
                1448.0,
                1474.0,
                1500.0
                ]
    interf_ljets_ge4j_3t_top25_Evt_HT_jets.histotitle = "H_{T}(jets)"
    interf_ljets_ge4j_3t_top25_Evt_HT_jets.histoname = "ljets_ge4j_3t_top25_Evt_HT_jets"
    interf_ljets_ge4j_3t_top25_Evt_HT_jets.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top25_Evt_HT_jets)
    
    interf_ljets_ge4j_3t_top25_Evt_HT_tags = vhi.variableHistoInterface(variable_name  = "Evt_HT_tags",
                                            label          = "ljets_ge4j_3t_top25_Evt_HT_tags",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top25_Evt_HT_tags.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top25_Evt_HT_tags","")
    interf_ljets_ge4j_3t_top25_Evt_HT_tags.category_label = label
    interf_ljets_ge4j_3t_top25_Evt_HT_tags.bin_edges = [ 
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
    interf_ljets_ge4j_3t_top25_Evt_HT_tags.histotitle = "Evt_HT_tags"
    interf_ljets_ge4j_3t_top25_Evt_HT_tags.histoname = "ljets_ge4j_3t_top25_Evt_HT_tags"
    interf_ljets_ge4j_3t_top25_Evt_HT_tags.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top25_Evt_HT_tags)
    
    interf_ljets_ge4j_3t_top25_Evt_JetPt_over_JetE = vhi.variableHistoInterface(variable_name  = "Evt_JetPt_over_JetE",
                                            label          = "ljets_ge4j_3t_top25_Evt_JetPt_over_JetE",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top25_Evt_JetPt_over_JetE.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top25_Evt_JetPt_over_JetE","")
    interf_ljets_ge4j_3t_top25_Evt_JetPt_over_JetE.category_label = label
    interf_ljets_ge4j_3t_top25_Evt_JetPt_over_JetE.bin_edges = [ 
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
    interf_ljets_ge4j_3t_top25_Evt_JetPt_over_JetE.histotitle = "Evt_JetPt_over_JetE"
    interf_ljets_ge4j_3t_top25_Evt_JetPt_over_JetE.histoname = "ljets_ge4j_3t_top25_Evt_JetPt_over_JetE"
    interf_ljets_ge4j_3t_top25_Evt_JetPt_over_JetE.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top25_Evt_JetPt_over_JetE)
    
    interf_ljets_ge4j_3t_top25_Evt_M_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_M_JetsAverage",
                                            label          = "ljets_ge4j_3t_top25_Evt_M_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top25_Evt_M_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top25_Evt_M_JetsAverage","")
    interf_ljets_ge4j_3t_top25_Evt_M_JetsAverage.category_label = label
    interf_ljets_ge4j_3t_top25_Evt_M_JetsAverage.bin_edges = [ 
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
                41.0,
                42.8,
                44.6,
                46.4,
                49.1,
                50.0
                ]
    interf_ljets_ge4j_3t_top25_Evt_M_JetsAverage.histotitle = "Evt_M_JetsAverage"
    interf_ljets_ge4j_3t_top25_Evt_M_JetsAverage.histoname = "ljets_ge4j_3t_top25_Evt_M_JetsAverage"
    interf_ljets_ge4j_3t_top25_Evt_M_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top25_Evt_M_JetsAverage)
    
    interf_ljets_ge4j_3t_top25_Evt_M_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_M_TaggedJetsAverage",
                                            label          = "ljets_ge4j_3t_top25_Evt_M_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top25_Evt_M_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top25_Evt_M_TaggedJetsAverage","")
    interf_ljets_ge4j_3t_top25_Evt_M_TaggedJetsAverage.category_label = label
    interf_ljets_ge4j_3t_top25_Evt_M_TaggedJetsAverage.bin_edges = [ 
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
                49.2,
                50.5,
                53.1,
                55.7,
                58.3,
                62.2,
                68.7,
                70.0
                ]
    interf_ljets_ge4j_3t_top25_Evt_M_TaggedJetsAverage.histotitle = "Evt_M_TaggedJetsAverage"
    interf_ljets_ge4j_3t_top25_Evt_M_TaggedJetsAverage.histoname = "ljets_ge4j_3t_top25_Evt_M_TaggedJetsAverage"
    interf_ljets_ge4j_3t_top25_Evt_M_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top25_Evt_M_TaggedJetsAverage)
    
    # interf_ljets_ge4j_3t_top25_Evt_M_Total = vhi.variableHistoInterface(variable_name  = "Evt_M_Total",
    #                                         label          = "ljets_ge4j_3t_top25_Evt_M_Total",
    #                                         selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    # interf_ljets_ge4j_3t_top25_Evt_M_Total.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top25_Evt_M_Total","")
    # interf_ljets_ge4j_3t_top25_Evt_M_Total.category_label = label
    # interf_ljets_ge4j_3t_top25_Evt_M_Total.bin_edges = [ 
    # 			256.0,
    # 			312.0,
    # 			368.0,
    # 			424.0,
    # 			480.0,
    # 			536.0,
    # 			592.0,
    # 			648.0,
    # 			704.0,
    # 			760.0,
    # 			816.0,
    # 			872.0,
    # 			928.0,
    # 			984.0,
    # 			1040.0,
    # 			1096.0,
    # 			1152.0,
    # 			1208.0,
    # 			1264.0,
    # 			1320.0,
    # 			1376.0,
    # 			1432.0,
    # 			1488.0,
    # 			1544.0,
    # 			1600.0,
    # 			1656.0,
    # 			1712.0,
    # 			1768.0,
    # 			1824.0,
    # 			1880.0,
    # 			1936.0,
    # 			1992.0,
    # 			2048.0,
    # 			2104.0,
    # 			2160.0,
    # 			2216.0,
    # 			2272.0,
    # 			2328.0,
    # 			2384.0,
    # 			2440.0,
    # 			2496.0,
    # 			2552.0,
    # 			2608.0,
    # 			2664.0,
    # 			2720.0,
    # 			2776.0,
    # 			2832.0,
    # 			2888.0,
    # 			2944.0,
    # 			3000.0
    # 			]
    # interf_ljets_ge4j_3t_top25_Evt_M_Total.histotitle = "Evt_M_Total"
    # interf_ljets_ge4j_3t_top25_Evt_M_Total.histoname = "ljets_ge4j_3t_top25_Evt_M_Total"
    # interf_ljets_ge4j_3t_top25_Evt_M_Total.nhistobins = 50
    # interfaces.append(interf_ljets_ge4j_3t_top25_Evt_M_Total)
    
    interf_ljets_ge4j_3t_top25_Evt_Pt_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Pt_TaggedJetsAverage",
                                            label          = "ljets_ge4j_3t_top25_Evt_Pt_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top25_Evt_Pt_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top25_Evt_Pt_TaggedJetsAverage","")
    interf_ljets_ge4j_3t_top25_Evt_Pt_TaggedJetsAverage.category_label = label
    interf_ljets_ge4j_3t_top25_Evt_Pt_TaggedJetsAverage.bin_edges = [ 
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
                417.6,
                440.4,
                474.6,
                520.2,
                588.6,
                600.0
                ]
    interf_ljets_ge4j_3t_top25_Evt_Pt_TaggedJetsAverage.histotitle = "Evt_Pt_TaggedJetsAverage"
    interf_ljets_ge4j_3t_top25_Evt_Pt_TaggedJetsAverage.histoname = "ljets_ge4j_3t_top25_Evt_Pt_TaggedJetsAverage"
    interf_ljets_ge4j_3t_top25_Evt_Pt_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top25_Evt_Pt_TaggedJetsAverage)
    
    interf_ljets_ge4j_3t_top25_Evt_Pt_minDrTaggedJets = vhi.variableHistoInterface(variable_name  = "Evt_Pt_minDrTaggedJets",
                                            label          = "ljets_ge4j_3t_top25_Evt_Pt_minDrTaggedJets",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top25_Evt_Pt_minDrTaggedJets.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top25_Evt_Pt_minDrTaggedJets","")
    interf_ljets_ge4j_3t_top25_Evt_Pt_minDrTaggedJets.category_label = label
    interf_ljets_ge4j_3t_top25_Evt_Pt_minDrTaggedJets.bin_edges = [ 
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
    interf_ljets_ge4j_3t_top25_Evt_Pt_minDrTaggedJets.histotitle = "Evt_Pt_minDrTaggedJets"
    interf_ljets_ge4j_3t_top25_Evt_Pt_minDrTaggedJets.histoname = "ljets_ge4j_3t_top25_Evt_Pt_minDrTaggedJets"
    interf_ljets_ge4j_3t_top25_Evt_Pt_minDrTaggedJets.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top25_Evt_Pt_minDrTaggedJets)
    
    interf_ljets_ge4j_3t_top25_Evt_blr_transformed = vhi.variableHistoInterface(variable_name  = "Evt_blr_transformed",
                                            label          = "ljets_ge4j_3t_top25_Evt_blr_transformed",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top25_Evt_blr_transformed.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top25_Evt_blr_transformed","")
    interf_ljets_ge4j_3t_top25_Evt_blr_transformed.category_label = label
    interf_ljets_ge4j_3t_top25_Evt_blr_transformed.bin_edges = [ 
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
                8.0,
                8.35,
                8.7,
                9.05,
                9.4,
                15.0
                ]
    interf_ljets_ge4j_3t_top25_Evt_blr_transformed.histotitle = "Evt_blr_transformed"
    interf_ljets_ge4j_3t_top25_Evt_blr_transformed.histoname = "ljets_ge4j_3t_top25_Evt_blr_transformed"
    interf_ljets_ge4j_3t_top25_Evt_blr_transformed.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top25_Evt_blr_transformed)
    
    interf_ljets_ge4j_3t_top25_Evt_h1 = vhi.variableHistoInterface(variable_name  = "Evt_h1",
                                            label          = "ljets_ge4j_3t_top25_Evt_h1",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top25_Evt_h1.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top25_Evt_h1","")
    interf_ljets_ge4j_3t_top25_Evt_h1.category_label = label
    interf_ljets_ge4j_3t_top25_Evt_h1.bin_edges = [ 
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
    interf_ljets_ge4j_3t_top25_Evt_h1.histotitle = "Evt_h1"
    interf_ljets_ge4j_3t_top25_Evt_h1.histoname = "ljets_ge4j_3t_top25_Evt_h1"
    interf_ljets_ge4j_3t_top25_Evt_h1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top25_Evt_h1)
    
    # interf_ljets_ge4j_3t_top25_Jet_Pt_0 = vhi.variableHistoInterface(variable_name  = "Jet_Pt[0]",
    #                                         label          = "ljets_ge4j_3t_top25_Jet_Pt_0",
    #                                         selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    # interf_ljets_ge4j_3t_top25_Jet_Pt_0.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top25_Jet_Pt_0","")
    # interf_ljets_ge4j_3t_top25_Jet_Pt_0.category_label = label
    # interf_ljets_ge4j_3t_top25_Jet_Pt_0.bin_edges = [ 
    # 			36.0,
    # 			48.0,
    # 			60.0,
    # 			72.0,
    # 			84.0,
    # 			96.0,
    # 			108.0,
    # 			120.0,
    # 			132.0,
    # 			144.0,
    # 			156.0,
    # 			168.0,
    # 			180.0,
    # 			192.0,
    # 			204.0,
    # 			216.0,
    # 			228.0,
    # 			240.0,
    # 			252.0,
    # 			264.0,
    # 			276.0,
    # 			288.0,
    # 			300.0,
    # 			312.0,
    # 			324.0,
    # 			336.0,
    # 			348.0,
    # 			360.0,
    # 			372.0,
    # 			384.0,
    # 			396.0,
    # 			408.0,
    # 			420.0,
    # 			432.0,
    # 			444.0,
    # 			456.0,
    # 			468.0,
    # 			480.0,
    # 			492.0,
    # 			504.0,
    # 			516.0,
    # 			528.0,
    # 			540.0,
    # 			552.0,
    # 			564.0,
    # 			576.0,
    # 			588.0,
    # 			600.0
    # 			]
    # interf_ljets_ge4j_3t_top25_Jet_Pt_0.histotitle = "p_{T} of leading jet"
    # interf_ljets_ge4j_3t_top25_Jet_Pt_0.histoname = "ljets_ge4j_3t_top25_Jet_Pt_0"
    # interf_ljets_ge4j_3t_top25_Jet_Pt_0.nhistobins = 50
    # interfaces.append(interf_ljets_ge4j_3t_top25_Jet_Pt_0)
    
    interf_ljets_ge4j_3t_top25_N_Jets = vhi.variableHistoInterface(variable_name  = "N_Jets",
                                            label          = "ljets_ge4j_3t_top25_N_Jets",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top25_N_Jets.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top25_N_Jets","")
    interf_ljets_ge4j_3t_top25_N_Jets.category_label = label
    interf_ljets_ge4j_3t_top25_N_Jets.bin_edges = [ 
                3.5,
                4.5,
                5.5,
                6.5,
                7.5,
                8.5,
                9.5,
                10.5
                ]
    interf_ljets_ge4j_3t_top25_N_Jets.histotitle = "N_Jets"
    interf_ljets_ge4j_3t_top25_N_Jets.histoname = "ljets_ge4j_3t_top25_N_Jets"
    interf_ljets_ge4j_3t_top25_N_Jets.nhistobins = 7
    interfaces.append(interf_ljets_ge4j_3t_top25_N_Jets)
    
    interf_ljets_ge4j_3t_top25_Reco_JABDT_tHW_Jet_CSV_btop = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_Jet_CSV_btop",
                                            label          = "ljets_ge4j_3t_top25_Reco_JABDT_tHW_Jet_CSV_btop",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top25_Reco_JABDT_tHW_Jet_CSV_btop.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top25_Reco_JABDT_tHW_Jet_CSV_btop","")
    interf_ljets_ge4j_3t_top25_Reco_JABDT_tHW_Jet_CSV_btop.category_label = label
    interf_ljets_ge4j_3t_top25_Reco_JABDT_tHW_Jet_CSV_btop.bin_edges = [ 
                -1.5,
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
    interf_ljets_ge4j_3t_top25_Reco_JABDT_tHW_Jet_CSV_btop.histotitle = "Reco_JABDT_tHW_Jet_CSV_btop"
    interf_ljets_ge4j_3t_top25_Reco_JABDT_tHW_Jet_CSV_btop.histoname = "ljets_ge4j_3t_top25_Reco_JABDT_tHW_Jet_CSV_btop"
    interf_ljets_ge4j_3t_top25_Reco_JABDT_tHW_Jet_CSV_btop.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top25_Reco_JABDT_tHW_Jet_CSV_btop)
    
    interf_ljets_ge4j_3t_top25_Reco_JABDT_tHW_Jet_CSV_whaddau1 = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_Jet_CSV_whaddau1",
                                            label          = "ljets_ge4j_3t_top25_Reco_JABDT_tHW_Jet_CSV_whaddau1",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top25_Reco_JABDT_tHW_Jet_CSV_whaddau1.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top25_Reco_JABDT_tHW_Jet_CSV_whaddau1","")
    interf_ljets_ge4j_3t_top25_Reco_JABDT_tHW_Jet_CSV_whaddau1.category_label = label
    interf_ljets_ge4j_3t_top25_Reco_JABDT_tHW_Jet_CSV_whaddau1.bin_edges = [ 
                -1.5,
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
    interf_ljets_ge4j_3t_top25_Reco_JABDT_tHW_Jet_CSV_whaddau1.histotitle = "Reco_JABDT_tHW_Jet_CSV_whaddau1"
    interf_ljets_ge4j_3t_top25_Reco_JABDT_tHW_Jet_CSV_whaddau1.histoname = "ljets_ge4j_3t_top25_Reco_JABDT_tHW_Jet_CSV_whaddau1"
    interf_ljets_ge4j_3t_top25_Reco_JABDT_tHW_Jet_CSV_whaddau1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top25_Reco_JABDT_tHW_Jet_CSV_whaddau1)
    
    interf_ljets_ge4j_3t_top25_Reco_JABDT_ttH_Jet_CSV_btoplep = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttH_Jet_CSV_btoplep",
                                            label          = "ljets_ge4j_3t_top25_Reco_JABDT_ttH_Jet_CSV_btoplep",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top25_Reco_JABDT_ttH_Jet_CSV_btoplep.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top25_Reco_JABDT_ttH_Jet_CSV_btoplep","")
    interf_ljets_ge4j_3t_top25_Reco_JABDT_ttH_Jet_CSV_btoplep.category_label = label
    interf_ljets_ge4j_3t_top25_Reco_JABDT_ttH_Jet_CSV_btoplep.bin_edges = [ 
                -1.5,
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
    interf_ljets_ge4j_3t_top25_Reco_JABDT_ttH_Jet_CSV_btoplep.histotitle = "Reco_JABDT_ttH_Jet_CSV_btoplep"
    interf_ljets_ge4j_3t_top25_Reco_JABDT_ttH_Jet_CSV_btoplep.histoname = "ljets_ge4j_3t_top25_Reco_JABDT_ttH_Jet_CSV_btoplep"
    interf_ljets_ge4j_3t_top25_Reco_JABDT_ttH_Jet_CSV_btoplep.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top25_Reco_JABDT_ttH_Jet_CSV_btoplep)
    
    interf_ljets_ge4j_3t_top25_Reco_tHW_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_tHW_bestJABDToutput",
                                            label          = "ljets_ge4j_3t_top25_Reco_tHW_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top25_Reco_tHW_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top25_Reco_tHW_bestJABDToutput","")
    interf_ljets_ge4j_3t_top25_Reco_tHW_bestJABDToutput.category_label = label
    interf_ljets_ge4j_3t_top25_Reco_tHW_bestJABDToutput.bin_edges = [ 
                -1.0,
                -0.424,
                -0.36,
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
                0.536,
                0.6
                ]
    interf_ljets_ge4j_3t_top25_Reco_tHW_bestJABDToutput.histotitle = "Reco_tHW_bestJABDToutput"
    interf_ljets_ge4j_3t_top25_Reco_tHW_bestJABDToutput.histoname = "ljets_ge4j_3t_top25_Reco_tHW_bestJABDToutput"
    interf_ljets_ge4j_3t_top25_Reco_tHW_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top25_Reco_tHW_bestJABDToutput)
    
    interf_ljets_ge4j_3t_top25_Reco_tHW_whad_dr = vhi.variableHistoInterface(variable_name  = "Reco_tHW_whad_dr",
                                            label          = "ljets_ge4j_3t_top25_Reco_tHW_whad_dr",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top25_Reco_tHW_whad_dr.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top25_Reco_tHW_whad_dr","")
    interf_ljets_ge4j_3t_top25_Reco_tHW_whad_dr.category_label = label
    interf_ljets_ge4j_3t_top25_Reco_tHW_whad_dr.bin_edges = [ 
                -1.5,
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
    interf_ljets_ge4j_3t_top25_Reco_tHW_whad_dr.histotitle = "Reco_tHW_whad_dr"
    interf_ljets_ge4j_3t_top25_Reco_tHW_whad_dr.histoname = "ljets_ge4j_3t_top25_Reco_tHW_whad_dr"
    interf_ljets_ge4j_3t_top25_Reco_tHW_whad_dr.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top25_Reco_tHW_whad_dr)
    
    interf_ljets_ge4j_3t_top25_Reco_tHq_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_tHq_bestJABDToutput",
                                            label          = "ljets_ge4j_3t_top25_Reco_tHq_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top25_Reco_tHq_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top25_Reco_tHq_bestJABDToutput","")
    interf_ljets_ge4j_3t_top25_Reco_tHq_bestJABDToutput.category_label = label
    interf_ljets_ge4j_3t_top25_Reco_tHq_bestJABDToutput.bin_edges = [ 
                -0.592,
                -0.524,
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
                0.564,
                0.7
                ]
    interf_ljets_ge4j_3t_top25_Reco_tHq_bestJABDToutput.histotitle = "Reco_tHq_bestJABDToutput"
    interf_ljets_ge4j_3t_top25_Reco_tHq_bestJABDToutput.histoname = "ljets_ge4j_3t_top25_Reco_tHq_bestJABDToutput"
    interf_ljets_ge4j_3t_top25_Reco_tHq_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top25_Reco_tHq_bestJABDToutput)
    
    interf_ljets_ge4j_3t_top25_Reco_ttH_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_ttH_bestJABDToutput",
                                            label          = "ljets_ge4j_3t_top25_Reco_ttH_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top25_Reco_ttH_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top25_Reco_ttH_bestJABDToutput","")
    interf_ljets_ge4j_3t_top25_Reco_ttH_bestJABDToutput.category_label = label
    interf_ljets_ge4j_3t_top25_Reco_ttH_bestJABDToutput.bin_edges = [ 
                -1.0,
                -0.49,
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
                0.7
                ]
    interf_ljets_ge4j_3t_top25_Reco_ttH_bestJABDToutput.histotitle = "Reco_ttH_bestJABDToutput"
    interf_ljets_ge4j_3t_top25_Reco_ttH_bestJABDToutput.histoname = "ljets_ge4j_3t_top25_Reco_ttH_bestJABDToutput"
    interf_ljets_ge4j_3t_top25_Reco_ttH_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top25_Reco_ttH_bestJABDToutput)
    
    # interf_ljets_ge4j_3t_top25_Reco_ttbar_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_ttbar_bestJABDToutput",
    #                                         label          = "ljets_ge4j_3t_top25_Reco_ttbar_bestJABDToutput",
    #                                         selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    # interf_ljets_ge4j_3t_top25_Reco_ttbar_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top25_Reco_ttbar_bestJABDToutput","")
    # interf_ljets_ge4j_3t_top25_Reco_ttbar_bestJABDToutput.category_label = label
    # interf_ljets_ge4j_3t_top25_Reco_ttbar_bestJABDToutput.bin_edges = [ 
    # 			-0.4,
    # 			-0.378,
    # 			-0.356,
    # 			-0.334,
    # 			-0.312,
    # 			-0.29,
    # 			-0.268,
    # 			-0.246,
    # 			-0.224,
    # 			-0.202,
    # 			-0.18,
    # 			-0.158,
    # 			-0.136,
    # 			-0.114,
    # 			-0.092,
    # 			-0.07,
    # 			-0.048,
    # 			-0.026,
    # 			-0.004,
    # 			0.018,
    # 			0.04,
    # 			0.062,
    # 			0.084,
    # 			0.106,
    # 			0.128,
    # 			0.15,
    # 			0.172,
    # 			0.194,
    # 			0.216,
    # 			0.238,
    # 			0.26,
    # 			0.282,
    # 			0.304,
    # 			0.326,
    # 			0.348,
    # 			0.37,
    # 			0.392,
    # 			0.414,
    # 			0.436,
    # 			0.458,
    # 			0.48,
    # 			0.502,
    # 			0.524,
    # 			0.546,
    # 			0.568,
    # 			0.59,
    # 			0.612,
    # 			0.7
    # 			]
    # interf_ljets_ge4j_3t_top25_Reco_ttbar_bestJABDToutput.histotitle = "Reco_ttbar_bestJABDToutput"
    # interf_ljets_ge4j_3t_top25_Reco_ttbar_bestJABDToutput.histoname = "ljets_ge4j_3t_top25_Reco_ttbar_bestJABDToutput"
    # interf_ljets_ge4j_3t_top25_Reco_ttbar_bestJABDToutput.nhistobins = 50
    # interfaces.append(interf_ljets_ge4j_3t_top25_Reco_ttbar_bestJABDToutput)
    
    plots = init_plots_2D(interfaces = interfaces)    
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_ge4j_3t_top30(data = None):
    label = "\geq 4 jets, 3 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM==3)&&(1.)"


    interf_ljets_ge4j_3t_top30_Evt_CSV_avg = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg",
                                            label          = "ljets_ge4j_3t_top30_Evt_CSV_avg",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top30_Evt_CSV_avg.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top30_Evt_CSV_avg","")
    interf_ljets_ge4j_3t_top30_Evt_CSV_avg.category_label = label
    interf_ljets_ge4j_3t_top30_Evt_CSV_avg.minxval = 0.15
    interf_ljets_ge4j_3t_top30_Evt_CSV_avg.maxxval = 1.0
    interf_ljets_ge4j_3t_top30_Evt_CSV_avg.histotitle = "Evt_CSV_avg"
    interf_ljets_ge4j_3t_top30_Evt_CSV_avg.histoname = "ljets_ge4j_3t_top30_Evt_CSV_avg"
    interf_ljets_ge4j_3t_top30_Evt_CSV_avg.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top30_Evt_CSV_avg)
    
    interf_ljets_ge4j_3t_top30_Evt_CSV_avg_tagged = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg_tagged",
                                            label          = "ljets_ge4j_3t_top30_Evt_CSV_avg_tagged",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top30_Evt_CSV_avg_tagged.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top30_Evt_CSV_avg_tagged","")
    interf_ljets_ge4j_3t_top30_Evt_CSV_avg_tagged.category_label = label
    interf_ljets_ge4j_3t_top30_Evt_CSV_avg_tagged.minxval = 0.3
    interf_ljets_ge4j_3t_top30_Evt_CSV_avg_tagged.maxxval = 1.0
    interf_ljets_ge4j_3t_top30_Evt_CSV_avg_tagged.histotitle = "Evt_CSV_avg_tagged"
    interf_ljets_ge4j_3t_top30_Evt_CSV_avg_tagged.histoname = "ljets_ge4j_3t_top30_Evt_CSV_avg_tagged"
    interf_ljets_ge4j_3t_top30_Evt_CSV_avg_tagged.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top30_Evt_CSV_avg_tagged)
    
    interf_ljets_ge4j_3t_top30_Evt_CSV_dev = vhi.variableHistoInterface(variable_name  = "Evt_CSV_dev",
                                            label          = "ljets_ge4j_3t_top30_Evt_CSV_dev",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top30_Evt_CSV_dev.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top30_Evt_CSV_dev","")
    interf_ljets_ge4j_3t_top30_Evt_CSV_dev.category_label = label
    interf_ljets_ge4j_3t_top30_Evt_CSV_dev.minxval = 0.0
    interf_ljets_ge4j_3t_top30_Evt_CSV_dev.maxxval = 0.25
    interf_ljets_ge4j_3t_top30_Evt_CSV_dev.histotitle = "Evt_CSV_dev"
    interf_ljets_ge4j_3t_top30_Evt_CSV_dev.histoname = "ljets_ge4j_3t_top30_Evt_CSV_dev"
    interf_ljets_ge4j_3t_top30_Evt_CSV_dev.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top30_Evt_CSV_dev)
    
    interf_ljets_ge4j_3t_top30_Evt_Dr_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Dr_TaggedJetsAverage",
                                            label          = "ljets_ge4j_3t_top30_Evt_Dr_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top30_Evt_Dr_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top30_Evt_Dr_TaggedJetsAverage","")
    interf_ljets_ge4j_3t_top30_Evt_Dr_TaggedJetsAverage.category_label = label
    interf_ljets_ge4j_3t_top30_Evt_Dr_TaggedJetsAverage.minxval = 0.5
    interf_ljets_ge4j_3t_top30_Evt_Dr_TaggedJetsAverage.maxxval = 3.5
    interf_ljets_ge4j_3t_top30_Evt_Dr_TaggedJetsAverage.histotitle = "average #DeltaR(tags)"
    interf_ljets_ge4j_3t_top30_Evt_Dr_TaggedJetsAverage.histoname = "ljets_ge4j_3t_top30_Evt_Dr_TaggedJetsAverage"
    interf_ljets_ge4j_3t_top30_Evt_Dr_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top30_Evt_Dr_TaggedJetsAverage)
    
    interf_ljets_ge4j_3t_top30_Evt_HT_jets = vhi.variableHistoInterface(variable_name  = "Evt_HT_jets",
                                            label          = "ljets_ge4j_3t_top30_Evt_HT_jets",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top30_Evt_HT_jets.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top30_Evt_HT_jets","")
    interf_ljets_ge4j_3t_top30_Evt_HT_jets.category_label = label
    interf_ljets_ge4j_3t_top30_Evt_HT_jets.minxval = 200.0
    interf_ljets_ge4j_3t_top30_Evt_HT_jets.maxxval = 1500.0
    interf_ljets_ge4j_3t_top30_Evt_HT_jets.histotitle = "H_{T}(jets)"
    interf_ljets_ge4j_3t_top30_Evt_HT_jets.histoname = "ljets_ge4j_3t_top30_Evt_HT_jets"
    interf_ljets_ge4j_3t_top30_Evt_HT_jets.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top30_Evt_HT_jets)
    
    interf_ljets_ge4j_3t_top30_Evt_HT_tags = vhi.variableHistoInterface(variable_name  = "Evt_HT_tags",
                                            label          = "ljets_ge4j_3t_top30_Evt_HT_tags",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top30_Evt_HT_tags.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top30_Evt_HT_tags","")
    interf_ljets_ge4j_3t_top30_Evt_HT_tags.category_label = label
    interf_ljets_ge4j_3t_top30_Evt_HT_tags.minxval = 100.0
    interf_ljets_ge4j_3t_top30_Evt_HT_tags.maxxval = 1000.0
    interf_ljets_ge4j_3t_top30_Evt_HT_tags.histotitle = "Evt_HT_tags"
    interf_ljets_ge4j_3t_top30_Evt_HT_tags.histoname = "ljets_ge4j_3t_top30_Evt_HT_tags"
    interf_ljets_ge4j_3t_top30_Evt_HT_tags.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top30_Evt_HT_tags)
    
    interf_ljets_ge4j_3t_top30_Evt_JetPt_over_JetE = vhi.variableHistoInterface(variable_name  = "Evt_JetPt_over_JetE",
                                            label          = "ljets_ge4j_3t_top30_Evt_JetPt_over_JetE",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top30_Evt_JetPt_over_JetE.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top30_Evt_JetPt_over_JetE","")
    interf_ljets_ge4j_3t_top30_Evt_JetPt_over_JetE.category_label = label
    interf_ljets_ge4j_3t_top30_Evt_JetPt_over_JetE.minxval = 0.0
    interf_ljets_ge4j_3t_top30_Evt_JetPt_over_JetE.maxxval = 1.0
    interf_ljets_ge4j_3t_top30_Evt_JetPt_over_JetE.histotitle = "Evt_JetPt_over_JetE"
    interf_ljets_ge4j_3t_top30_Evt_JetPt_over_JetE.histoname = "ljets_ge4j_3t_top30_Evt_JetPt_over_JetE"
    interf_ljets_ge4j_3t_top30_Evt_JetPt_over_JetE.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top30_Evt_JetPt_over_JetE)
    
    interf_ljets_ge4j_3t_top30_Evt_M2_minDrTaggedJets = vhi.variableHistoInterface(variable_name  = "Evt_M2_minDrTaggedJets",
                                            label          = "ljets_ge4j_3t_top30_Evt_M2_minDrTaggedJets",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top30_Evt_M2_minDrTaggedJets.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top30_Evt_M2_minDrTaggedJets","")
    interf_ljets_ge4j_3t_top30_Evt_M2_minDrTaggedJets.category_label = label
    interf_ljets_ge4j_3t_top30_Evt_M2_minDrTaggedJets.minxval = 0.0
    interf_ljets_ge4j_3t_top30_Evt_M2_minDrTaggedJets.maxxval = 400.0
    interf_ljets_ge4j_3t_top30_Evt_M2_minDrTaggedJets.histotitle = "M_{2}( min #DeltaR(tag,tag) )"
    interf_ljets_ge4j_3t_top30_Evt_M2_minDrTaggedJets.histoname = "ljets_ge4j_3t_top30_Evt_M2_minDrTaggedJets"
    interf_ljets_ge4j_3t_top30_Evt_M2_minDrTaggedJets.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top30_Evt_M2_minDrTaggedJets)
    
    interf_ljets_ge4j_3t_top30_Evt_M_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_M_JetsAverage",
                                            label          = "ljets_ge4j_3t_top30_Evt_M_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top30_Evt_M_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top30_Evt_M_JetsAverage","")
    interf_ljets_ge4j_3t_top30_Evt_M_JetsAverage.category_label = label
    interf_ljets_ge4j_3t_top30_Evt_M_JetsAverage.minxval = 5.0
    interf_ljets_ge4j_3t_top30_Evt_M_JetsAverage.maxxval = 50.0
    interf_ljets_ge4j_3t_top30_Evt_M_JetsAverage.histotitle = "Evt_M_JetsAverage"
    interf_ljets_ge4j_3t_top30_Evt_M_JetsAverage.histoname = "ljets_ge4j_3t_top30_Evt_M_JetsAverage"
    interf_ljets_ge4j_3t_top30_Evt_M_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top30_Evt_M_JetsAverage)
    
    interf_ljets_ge4j_3t_top30_Evt_M_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_M_TaggedJetsAverage",
                                            label          = "ljets_ge4j_3t_top30_Evt_M_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top30_Evt_M_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top30_Evt_M_TaggedJetsAverage","")
    interf_ljets_ge4j_3t_top30_Evt_M_TaggedJetsAverage.category_label = label
    interf_ljets_ge4j_3t_top30_Evt_M_TaggedJetsAverage.minxval = 5.0
    interf_ljets_ge4j_3t_top30_Evt_M_TaggedJetsAverage.maxxval = 70.0
    interf_ljets_ge4j_3t_top30_Evt_M_TaggedJetsAverage.histotitle = "Evt_M_TaggedJetsAverage"
    interf_ljets_ge4j_3t_top30_Evt_M_TaggedJetsAverage.histoname = "ljets_ge4j_3t_top30_Evt_M_TaggedJetsAverage"
    interf_ljets_ge4j_3t_top30_Evt_M_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top30_Evt_M_TaggedJetsAverage)
    
    interf_ljets_ge4j_3t_top30_Evt_M_Total = vhi.variableHistoInterface(variable_name  = "Evt_M_Total",
                                            label          = "ljets_ge4j_3t_top30_Evt_M_Total",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top30_Evt_M_Total.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top30_Evt_M_Total","")
    interf_ljets_ge4j_3t_top30_Evt_M_Total.category_label = label
    interf_ljets_ge4j_3t_top30_Evt_M_Total.minxval = 200.0
    interf_ljets_ge4j_3t_top30_Evt_M_Total.maxxval = 3000.0
    interf_ljets_ge4j_3t_top30_Evt_M_Total.histotitle = "Evt_M_Total"
    interf_ljets_ge4j_3t_top30_Evt_M_Total.histoname = "ljets_ge4j_3t_top30_Evt_M_Total"
    interf_ljets_ge4j_3t_top30_Evt_M_Total.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top30_Evt_M_Total)
    
    interf_ljets_ge4j_3t_top30_Evt_Pt_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Pt_TaggedJetsAverage",
                                            label          = "ljets_ge4j_3t_top30_Evt_Pt_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top30_Evt_Pt_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top30_Evt_Pt_TaggedJetsAverage","")
    interf_ljets_ge4j_3t_top30_Evt_Pt_TaggedJetsAverage.category_label = label
    interf_ljets_ge4j_3t_top30_Evt_Pt_TaggedJetsAverage.minxval = 30.0
    interf_ljets_ge4j_3t_top30_Evt_Pt_TaggedJetsAverage.maxxval = 600.0
    interf_ljets_ge4j_3t_top30_Evt_Pt_TaggedJetsAverage.histotitle = "Evt_Pt_TaggedJetsAverage"
    interf_ljets_ge4j_3t_top30_Evt_Pt_TaggedJetsAverage.histoname = "ljets_ge4j_3t_top30_Evt_Pt_TaggedJetsAverage"
    interf_ljets_ge4j_3t_top30_Evt_Pt_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top30_Evt_Pt_TaggedJetsAverage)
    
    interf_ljets_ge4j_3t_top30_Evt_Pt_minDrTaggedJets = vhi.variableHistoInterface(variable_name  = "Evt_Pt_minDrTaggedJets",
                                            label          = "ljets_ge4j_3t_top30_Evt_Pt_minDrTaggedJets",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top30_Evt_Pt_minDrTaggedJets.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top30_Evt_Pt_minDrTaggedJets","")
    interf_ljets_ge4j_3t_top30_Evt_Pt_minDrTaggedJets.category_label = label
    interf_ljets_ge4j_3t_top30_Evt_Pt_minDrTaggedJets.minxval = 20.0
    interf_ljets_ge4j_3t_top30_Evt_Pt_minDrTaggedJets.maxxval = 600.0
    interf_ljets_ge4j_3t_top30_Evt_Pt_minDrTaggedJets.histotitle = "Evt_Pt_minDrTaggedJets"
    interf_ljets_ge4j_3t_top30_Evt_Pt_minDrTaggedJets.histoname = "ljets_ge4j_3t_top30_Evt_Pt_minDrTaggedJets"
    interf_ljets_ge4j_3t_top30_Evt_Pt_minDrTaggedJets.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top30_Evt_Pt_minDrTaggedJets)
    
    interf_ljets_ge4j_3t_top30_Evt_blr_transformed = vhi.variableHistoInterface(variable_name  = "Evt_blr_transformed",
                                            label          = "ljets_ge4j_3t_top30_Evt_blr_transformed",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top30_Evt_blr_transformed.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top30_Evt_blr_transformed","")
    interf_ljets_ge4j_3t_top30_Evt_blr_transformed.category_label = label
    interf_ljets_ge4j_3t_top30_Evt_blr_transformed.minxval = -2.5
    interf_ljets_ge4j_3t_top30_Evt_blr_transformed.maxxval = 15.0
    interf_ljets_ge4j_3t_top30_Evt_blr_transformed.histotitle = "Evt_blr_transformed"
    interf_ljets_ge4j_3t_top30_Evt_blr_transformed.histoname = "ljets_ge4j_3t_top30_Evt_blr_transformed"
    interf_ljets_ge4j_3t_top30_Evt_blr_transformed.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top30_Evt_blr_transformed)
    
    interf_ljets_ge4j_3t_top30_Evt_h1 = vhi.variableHistoInterface(variable_name  = "Evt_h1",
                                            label          = "ljets_ge4j_3t_top30_Evt_h1",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top30_Evt_h1.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top30_Evt_h1","")
    interf_ljets_ge4j_3t_top30_Evt_h1.category_label = label
    interf_ljets_ge4j_3t_top30_Evt_h1.minxval = -0.2
    interf_ljets_ge4j_3t_top30_Evt_h1.maxxval = 0.4
    interf_ljets_ge4j_3t_top30_Evt_h1.histotitle = "Evt_h1"
    interf_ljets_ge4j_3t_top30_Evt_h1.histoname = "ljets_ge4j_3t_top30_Evt_h1"
    interf_ljets_ge4j_3t_top30_Evt_h1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top30_Evt_h1)
    
    interf_ljets_ge4j_3t_top30_Jet_Pt_0 = vhi.variableHistoInterface(variable_name  = "Jet_Pt[0]",
                                            label          = "ljets_ge4j_3t_top30_Jet_Pt_0",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top30_Jet_Pt_0.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top30_Jet_Pt_0","")
    interf_ljets_ge4j_3t_top30_Jet_Pt_0.category_label = label
    interf_ljets_ge4j_3t_top30_Jet_Pt_0.minxval = 0.0
    interf_ljets_ge4j_3t_top30_Jet_Pt_0.maxxval = 600.0
    interf_ljets_ge4j_3t_top30_Jet_Pt_0.histotitle = "p_{T} of leading jet"
    interf_ljets_ge4j_3t_top30_Jet_Pt_0.histoname = "ljets_ge4j_3t_top30_Jet_Pt_0"
    interf_ljets_ge4j_3t_top30_Jet_Pt_0.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top30_Jet_Pt_0)
    
    interf_ljets_ge4j_3t_top30_N_Jets = vhi.variableHistoInterface(variable_name  = "N_Jets",
                                            label          = "ljets_ge4j_3t_top30_N_Jets",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top30_N_Jets.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top30_N_Jets","")
    interf_ljets_ge4j_3t_top30_N_Jets.category_label = label
    interf_ljets_ge4j_3t_top30_N_Jets.minxval = 3.5
    interf_ljets_ge4j_3t_top30_N_Jets.maxxval = 10.5
    interf_ljets_ge4j_3t_top30_N_Jets.histotitle = "N_Jets"
    interf_ljets_ge4j_3t_top30_N_Jets.histoname = "ljets_ge4j_3t_top30_N_Jets"
    interf_ljets_ge4j_3t_top30_N_Jets.nhistobins = 7
    interfaces.append(interf_ljets_ge4j_3t_top30_N_Jets)
    
    interf_ljets_ge4j_3t_top30_Reco_JABDT_tHW_Jet_CSV_btop = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_Jet_CSV_btop",
                                            label          = "ljets_ge4j_3t_top30_Reco_JABDT_tHW_Jet_CSV_btop",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top30_Reco_JABDT_tHW_Jet_CSV_btop.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top30_Reco_JABDT_tHW_Jet_CSV_btop","")
    interf_ljets_ge4j_3t_top30_Reco_JABDT_tHW_Jet_CSV_btop.category_label = label
    interf_ljets_ge4j_3t_top30_Reco_JABDT_tHW_Jet_CSV_btop.minxval = -1.5
    interf_ljets_ge4j_3t_top30_Reco_JABDT_tHW_Jet_CSV_btop.maxxval = 1.0
    interf_ljets_ge4j_3t_top30_Reco_JABDT_tHW_Jet_CSV_btop.histotitle = "Reco_JABDT_tHW_Jet_CSV_btop"
    interf_ljets_ge4j_3t_top30_Reco_JABDT_tHW_Jet_CSV_btop.histoname = "ljets_ge4j_3t_top30_Reco_JABDT_tHW_Jet_CSV_btop"
    interf_ljets_ge4j_3t_top30_Reco_JABDT_tHW_Jet_CSV_btop.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top30_Reco_JABDT_tHW_Jet_CSV_btop)
    
    interf_ljets_ge4j_3t_top30_Reco_JABDT_tHW_Jet_CSV_whaddau1 = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_Jet_CSV_whaddau1",
                                            label          = "ljets_ge4j_3t_top30_Reco_JABDT_tHW_Jet_CSV_whaddau1",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top30_Reco_JABDT_tHW_Jet_CSV_whaddau1.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top30_Reco_JABDT_tHW_Jet_CSV_whaddau1","")
    interf_ljets_ge4j_3t_top30_Reco_JABDT_tHW_Jet_CSV_whaddau1.category_label = label
    interf_ljets_ge4j_3t_top30_Reco_JABDT_tHW_Jet_CSV_whaddau1.minxval = -1.5
    interf_ljets_ge4j_3t_top30_Reco_JABDT_tHW_Jet_CSV_whaddau1.maxxval = 1.0
    interf_ljets_ge4j_3t_top30_Reco_JABDT_tHW_Jet_CSV_whaddau1.histotitle = "Reco_JABDT_tHW_Jet_CSV_whaddau1"
    interf_ljets_ge4j_3t_top30_Reco_JABDT_tHW_Jet_CSV_whaddau1.histoname = "ljets_ge4j_3t_top30_Reco_JABDT_tHW_Jet_CSV_whaddau1"
    interf_ljets_ge4j_3t_top30_Reco_JABDT_tHW_Jet_CSV_whaddau1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top30_Reco_JABDT_tHW_Jet_CSV_whaddau1)
    
    interf_ljets_ge4j_3t_top30_Reco_JABDT_ttH_Jet_CSV_btoplep = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttH_Jet_CSV_btoplep",
                                            label          = "ljets_ge4j_3t_top30_Reco_JABDT_ttH_Jet_CSV_btoplep",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top30_Reco_JABDT_ttH_Jet_CSV_btoplep.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top30_Reco_JABDT_ttH_Jet_CSV_btoplep","")
    interf_ljets_ge4j_3t_top30_Reco_JABDT_ttH_Jet_CSV_btoplep.category_label = label
    interf_ljets_ge4j_3t_top30_Reco_JABDT_ttH_Jet_CSV_btoplep.minxval = -1.5
    interf_ljets_ge4j_3t_top30_Reco_JABDT_ttH_Jet_CSV_btoplep.maxxval = 1.0
    interf_ljets_ge4j_3t_top30_Reco_JABDT_ttH_Jet_CSV_btoplep.histotitle = "Reco_JABDT_ttH_Jet_CSV_btoplep"
    interf_ljets_ge4j_3t_top30_Reco_JABDT_ttH_Jet_CSV_btoplep.histoname = "ljets_ge4j_3t_top30_Reco_JABDT_ttH_Jet_CSV_btoplep"
    interf_ljets_ge4j_3t_top30_Reco_JABDT_ttH_Jet_CSV_btoplep.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top30_Reco_JABDT_ttH_Jet_CSV_btoplep)
    
    interf_ljets_ge4j_3t_top30_Reco_JABDT_ttbar_Jet_CSV_btoplep = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttbar_Jet_CSV_btoplep",
                                            label          = "ljets_ge4j_3t_top30_Reco_JABDT_ttbar_Jet_CSV_btoplep",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top30_Reco_JABDT_ttbar_Jet_CSV_btoplep.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top30_Reco_JABDT_ttbar_Jet_CSV_btoplep","")
    interf_ljets_ge4j_3t_top30_Reco_JABDT_ttbar_Jet_CSV_btoplep.category_label = label
    interf_ljets_ge4j_3t_top30_Reco_JABDT_ttbar_Jet_CSV_btoplep.minxval = 0.0
    interf_ljets_ge4j_3t_top30_Reco_JABDT_ttbar_Jet_CSV_btoplep.maxxval = 1.0
    interf_ljets_ge4j_3t_top30_Reco_JABDT_ttbar_Jet_CSV_btoplep.histotitle = "Reco_JABDT_ttbar_Jet_CSV_btoplep"
    interf_ljets_ge4j_3t_top30_Reco_JABDT_ttbar_Jet_CSV_btoplep.histoname = "ljets_ge4j_3t_top30_Reco_JABDT_ttbar_Jet_CSV_btoplep"
    interf_ljets_ge4j_3t_top30_Reco_JABDT_ttbar_Jet_CSV_btoplep.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top30_Reco_JABDT_ttbar_Jet_CSV_btoplep)
    
    interf_ljets_ge4j_3t_top30_Reco_JABDT_ttbar_Jet_CSV_whaddau1 = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttbar_Jet_CSV_whaddau1",
                                            label          = "ljets_ge4j_3t_top30_Reco_JABDT_ttbar_Jet_CSV_whaddau1",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top30_Reco_JABDT_ttbar_Jet_CSV_whaddau1.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top30_Reco_JABDT_ttbar_Jet_CSV_whaddau1","")
    interf_ljets_ge4j_3t_top30_Reco_JABDT_ttbar_Jet_CSV_whaddau1.category_label = label
    interf_ljets_ge4j_3t_top30_Reco_JABDT_ttbar_Jet_CSV_whaddau1.minxval = 0.0
    interf_ljets_ge4j_3t_top30_Reco_JABDT_ttbar_Jet_CSV_whaddau1.maxxval = 1.0
    interf_ljets_ge4j_3t_top30_Reco_JABDT_ttbar_Jet_CSV_whaddau1.histotitle = "Reco_JABDT_ttbar_Jet_CSV_whaddau1"
    interf_ljets_ge4j_3t_top30_Reco_JABDT_ttbar_Jet_CSV_whaddau1.histoname = "ljets_ge4j_3t_top30_Reco_JABDT_ttbar_Jet_CSV_whaddau1"
    interf_ljets_ge4j_3t_top30_Reco_JABDT_ttbar_Jet_CSV_whaddau1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top30_Reco_JABDT_ttbar_Jet_CSV_whaddau1)
    
    interf_ljets_ge4j_3t_top30_Reco_tHW_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_tHW_bestJABDToutput",
                                            label          = "ljets_ge4j_3t_top30_Reco_tHW_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top30_Reco_tHW_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top30_Reco_tHW_bestJABDToutput","")
    interf_ljets_ge4j_3t_top30_Reco_tHW_bestJABDToutput.category_label = label
    interf_ljets_ge4j_3t_top30_Reco_tHW_bestJABDToutput.minxval = -1.0
    interf_ljets_ge4j_3t_top30_Reco_tHW_bestJABDToutput.maxxval = 0.6
    interf_ljets_ge4j_3t_top30_Reco_tHW_bestJABDToutput.histotitle = "Reco_tHW_bestJABDToutput"
    interf_ljets_ge4j_3t_top30_Reco_tHW_bestJABDToutput.histoname = "ljets_ge4j_3t_top30_Reco_tHW_bestJABDToutput"
    interf_ljets_ge4j_3t_top30_Reco_tHW_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top30_Reco_tHW_bestJABDToutput)
    
    interf_ljets_ge4j_3t_top30_Reco_tHW_whad_dr = vhi.variableHistoInterface(variable_name  = "Reco_tHW_whad_dr",
                                            label          = "ljets_ge4j_3t_top30_Reco_tHW_whad_dr",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top30_Reco_tHW_whad_dr.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top30_Reco_tHW_whad_dr","")
    interf_ljets_ge4j_3t_top30_Reco_tHW_whad_dr.category_label = label
    interf_ljets_ge4j_3t_top30_Reco_tHW_whad_dr.minxval = -1.5
    interf_ljets_ge4j_3t_top30_Reco_tHW_whad_dr.maxxval = 5.0
    interf_ljets_ge4j_3t_top30_Reco_tHW_whad_dr.histotitle = "Reco_tHW_whad_dr"
    interf_ljets_ge4j_3t_top30_Reco_tHW_whad_dr.histoname = "ljets_ge4j_3t_top30_Reco_tHW_whad_dr"
    interf_ljets_ge4j_3t_top30_Reco_tHW_whad_dr.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top30_Reco_tHW_whad_dr)
    
    interf_ljets_ge4j_3t_top30_Reco_tHq_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_tHq_bestJABDToutput",
                                            label          = "ljets_ge4j_3t_top30_Reco_tHq_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top30_Reco_tHq_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top30_Reco_tHq_bestJABDToutput","")
    interf_ljets_ge4j_3t_top30_Reco_tHq_bestJABDToutput.category_label = label
    interf_ljets_ge4j_3t_top30_Reco_tHq_bestJABDToutput.minxval = -1.0
    interf_ljets_ge4j_3t_top30_Reco_tHq_bestJABDToutput.maxxval = 0.7
    interf_ljets_ge4j_3t_top30_Reco_tHq_bestJABDToutput.histotitle = "Reco_tHq_bestJABDToutput"
    interf_ljets_ge4j_3t_top30_Reco_tHq_bestJABDToutput.histoname = "ljets_ge4j_3t_top30_Reco_tHq_bestJABDToutput"
    interf_ljets_ge4j_3t_top30_Reco_tHq_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top30_Reco_tHq_bestJABDToutput)
    
    interf_ljets_ge4j_3t_top30_Reco_ttH_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_ttH_bestJABDToutput",
                                            label          = "ljets_ge4j_3t_top30_Reco_ttH_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top30_Reco_ttH_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top30_Reco_ttH_bestJABDToutput","")
    interf_ljets_ge4j_3t_top30_Reco_ttH_bestJABDToutput.category_label = label
    interf_ljets_ge4j_3t_top30_Reco_ttH_bestJABDToutput.minxval = -1.0
    interf_ljets_ge4j_3t_top30_Reco_ttH_bestJABDToutput.maxxval = 0.7
    interf_ljets_ge4j_3t_top30_Reco_ttH_bestJABDToutput.histotitle = "Reco_ttH_bestJABDToutput"
    interf_ljets_ge4j_3t_top30_Reco_ttH_bestJABDToutput.histoname = "ljets_ge4j_3t_top30_Reco_ttH_bestJABDToutput"
    interf_ljets_ge4j_3t_top30_Reco_ttH_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top30_Reco_ttH_bestJABDToutput)
    
    interf_ljets_ge4j_3t_top30_Reco_ttbar_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_ttbar_bestJABDToutput",
                                            label          = "ljets_ge4j_3t_top30_Reco_ttbar_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top30_Reco_ttbar_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top30_Reco_ttbar_bestJABDToutput","")
    interf_ljets_ge4j_3t_top30_Reco_ttbar_bestJABDToutput.category_label = label
    interf_ljets_ge4j_3t_top30_Reco_ttbar_bestJABDToutput.minxval = -0.4
    interf_ljets_ge4j_3t_top30_Reco_ttbar_bestJABDToutput.maxxval = 0.7
    interf_ljets_ge4j_3t_top30_Reco_ttbar_bestJABDToutput.histotitle = "Reco_ttbar_bestJABDToutput"
    interf_ljets_ge4j_3t_top30_Reco_ttbar_bestJABDToutput.histoname = "ljets_ge4j_3t_top30_Reco_ttbar_bestJABDToutput"
    interf_ljets_ge4j_3t_top30_Reco_ttbar_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top30_Reco_ttbar_bestJABDToutput)
    
    interf_ljets_ge4j_3t_top30_Reco_ttbar_toplep_m = vhi.variableHistoInterface(variable_name  = "Reco_ttbar_toplep_m",
                                            label          = "ljets_ge4j_3t_top30_Reco_ttbar_toplep_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top30_Reco_ttbar_toplep_m.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top30_Reco_ttbar_toplep_m","")
    interf_ljets_ge4j_3t_top30_Reco_ttbar_toplep_m.category_label = label
    interf_ljets_ge4j_3t_top30_Reco_ttbar_toplep_m.minxval = 80.0
    interf_ljets_ge4j_3t_top30_Reco_ttbar_toplep_m.maxxval = 500.0
    interf_ljets_ge4j_3t_top30_Reco_ttbar_toplep_m.histotitle = "Reco_ttbar_toplep_m"
    interf_ljets_ge4j_3t_top30_Reco_ttbar_toplep_m.histoname = "ljets_ge4j_3t_top30_Reco_ttbar_toplep_m"
    interf_ljets_ge4j_3t_top30_Reco_ttbar_toplep_m.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top30_Reco_ttbar_toplep_m)
    
    interf_ljets_ge4j_3t_top30_Reco_ttbar_whad_m = vhi.variableHistoInterface(variable_name  = "Reco_ttbar_whad_m",
                                            label          = "ljets_ge4j_3t_top30_Reco_ttbar_whad_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_top30_Reco_ttbar_whad_m.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_top30_Reco_ttbar_whad_m","")
    interf_ljets_ge4j_3t_top30_Reco_ttbar_whad_m.category_label = label
    interf_ljets_ge4j_3t_top30_Reco_ttbar_whad_m.minxval = 0.0
    interf_ljets_ge4j_3t_top30_Reco_ttbar_whad_m.maxxval = 600.0
    interf_ljets_ge4j_3t_top30_Reco_ttbar_whad_m.histotitle = "Reco_ttbar_whad_m"
    interf_ljets_ge4j_3t_top30_Reco_ttbar_whad_m.histoname = "ljets_ge4j_3t_top30_Reco_ttbar_whad_m"
    interf_ljets_ge4j_3t_top30_Reco_ttbar_whad_m.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_top30_Reco_ttbar_whad_m)
    
    plots = init_plots(interfaces = interfaces)    
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_dnn(data, discrname):

    ndefaultbins = 100
    interfaces = []


    # plots for ge4j_ge4t_top20

    interf_ljets_ge4j_ge4t_top20_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_top20_node_ttH",
                                            label          = "ljets_ge4j_ge4t_top20_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top20==0))")
    interf_ljets_ge4j_ge4t_top20_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top20==0))","ljets_ge4j_ge4t_top20_ttH_node","")
    interf_ljets_ge4j_ge4t_top20_ttH_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_top20_ttH_node.bin_edges = [ 
                0.1363,
                0.1437,
                0.1511,
                0.1584,
                0.1658,
                0.1732,
                0.1806,
                0.1879,
                0.1953,
                0.2027,
                0.2101,
                0.2174,
                0.2248,
                0.2322,
                0.2395,
                0.2469,
                0.2543,
                0.2617,
                0.269,
                0.2764,
                0.2838,
                0.2912,
                0.2985,
                0.3059,
                0.3133,
                0.3207,
                0.328,
                0.3354,
                0.3428,
                0.3502,
                0.3575,
                0.3649,
                0.3723,
                0.3796,
                0.387,
                0.3944,
                0.4018,
                0.4091,
                0.4165,
                0.4239,
                0.4313,
                0.4386,
                0.446,
                0.4534,
                0.4608,
                0.4681,
                0.4755,
                0.4829,
                0.4903,
                0.4976,
                0.505,
                0.5124,
                0.5197,
                0.5271,
                0.5345,
                0.5419,
                0.5492,
                0.5566,
                0.564,
                0.5714,
                0.5787,
                0.5861,
                0.5935,
                0.6009,
                0.6082,
                0.6156,
                0.623,
                0.6304,
                0.6377,
                0.6451,
                0.6525,
                0.6598,
                0.6672,
                0.6746,
                0.682,
                0.6893,
                0.6967,
                0.7041,
                0.7115,
                0.7188,
                0.7262,
                0.7336,
                0.741,
                0.7483,
                0.7557,
                0.7631,
                0.7705,
                0.7778,
                0.7852,
                0.7926,
                0.7999,
                0.8073,
                0.8147,
                0.8221,
                0.8294,
                0.8368,
                0.8442,
                0.8516,
                0.8589,
                0.8663,
                0.87
                ]
    interf_ljets_ge4j_ge4t_top20_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_top20_ttH_node)
    
    interf_ljets_ge4j_ge4t_top20_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_top20_node_ttmb",
                                            label          = "ljets_ge4j_ge4t_top20_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top20==1))")
    interf_ljets_ge4j_ge4t_top20_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top20==1))","ljets_ge4j_ge4t_top20_ttmb_node","")
    interf_ljets_ge4j_ge4t_top20_ttmb_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_top20_ttmb_node.bin_edges = [ 
                0.1366,
                0.1434,
                0.1503,
                0.1572,
                0.164,
                0.1709,
                0.1778,
                0.1846,
                0.1915,
                0.1984,
                0.2053,
                0.2121,
                0.219,
                0.2259,
                0.2327,
                0.2396,
                0.2465,
                0.2533,
                0.2602,
                0.2671,
                0.2739,
                0.2808,
                0.2877,
                0.2945,
                0.3014,
                0.3083,
                0.3152,
                0.322,
                0.3289,
                0.3358,
                0.3426,
                0.3495,
                0.3564,
                0.3632,
                0.3701,
                0.377,
                0.3838,
                0.3907,
                0.3976,
                0.4044,
                0.4113,
                0.4182,
                0.4251,
                0.4319,
                0.4388,
                0.4457,
                0.4525,
                0.4594,
                0.4663,
                0.4731,
                0.48,
                0.4869,
                0.4937,
                0.5006,
                0.5075,
                0.5143,
                0.5212,
                0.5281,
                0.5349,
                0.5418,
                0.5487,
                0.5556,
                0.5624,
                0.5693,
                0.5762,
                0.583,
                0.5899,
                0.5968,
                0.6036,
                0.6105,
                0.6174,
                0.6242,
                0.6311,
                0.638,
                0.6448,
                0.6517,
                0.6586,
                0.6655,
                0.6723,
                0.6792,
                0.6861,
                0.6929,
                0.6998,
                0.7067,
                0.7135,
                0.7204,
                0.7273,
                0.7341,
                0.741,
                0.7479,
                0.7547,
                0.7616,
                0.7685,
                0.7754,
                0.7822,
                0.7891,
                0.796,
                0.8028,
                0.8097,
                0.8166,
                0.82
                ]
    interf_ljets_ge4j_ge4t_top20_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_top20_ttmb_node)
    
    interf_ljets_ge4j_ge4t_top20_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_top20_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_top20_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top20==2))")
    interf_ljets_ge4j_ge4t_top20_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top20==2))","ljets_ge4j_ge4t_top20_tt2b_node","")
    interf_ljets_ge4j_ge4t_top20_tt2b_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_top20_tt2b_node.bin_edges = [ 
                0.1369,
                0.1431,
                0.1492,
                0.1554,
                0.1616,
                0.1677,
                0.1739,
                0.1801,
                0.1862,
                0.1924,
                0.1985,
                0.2047,
                0.2109,
                0.217,
                0.2232,
                0.2293,
                0.2355,
                0.2417,
                0.2478,
                0.254,
                0.2602,
                0.2663,
                0.2725,
                0.2786,
                0.2848,
                0.291,
                0.2971,
                0.3033,
                0.3094,
                0.3156,
                0.3218,
                0.3279,
                0.3341,
                0.3403,
                0.3464,
                0.3526,
                0.3587,
                0.3649,
                0.3711,
                0.3772,
                0.3834,
                0.3895,
                0.3957,
                0.4019,
                0.408,
                0.4142,
                0.4204,
                0.4265,
                0.4327,
                0.4388,
                0.445,
                0.4512,
                0.4573,
                0.4635,
                0.4696,
                0.4758,
                0.482,
                0.4881,
                0.4943,
                0.5005,
                0.5066,
                0.5128,
                0.5189,
                0.5251,
                0.5313,
                0.5374,
                0.5436,
                0.5497,
                0.5559,
                0.5621,
                0.5682,
                0.5744,
                0.5806,
                0.5867,
                0.5929,
                0.599,
                0.6052,
                0.6114,
                0.6175,
                0.6237,
                0.6298,
                0.636,
                0.6422,
                0.6483,
                0.6545,
                0.6607,
                0.6668,
                0.673,
                0.6791,
                0.6853,
                0.6915,
                0.6976,
                0.7038,
                0.7099,
                0.7161,
                0.7223,
                0.7284,
                0.7346,
                0.7408,
                0.7469,
                0.75
                ]
    interf_ljets_ge4j_ge4t_top20_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_top20_tt2b_node)
    
    interf_ljets_ge4j_ge4t_top20_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_top20_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_top20_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top20==3))")
    interf_ljets_ge4j_ge4t_top20_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top20==3))","ljets_ge4j_ge4t_top20_ttcc_node","")
    interf_ljets_ge4j_ge4t_top20_ttcc_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_top20_ttcc_node.bin_edges = [ 
                0.1381,
                0.1419,
                0.1458,
                0.1496,
                0.1534,
                0.1573,
                0.1611,
                0.1649,
                0.1688,
                0.1726,
                0.1765,
                0.1803,
                0.1841,
                0.188,
                0.1918,
                0.1957,
                0.1995,
                0.2033,
                0.2072,
                0.211,
                0.2148,
                0.2187,
                0.2225,
                0.2264,
                0.2302,
                0.234,
                0.2379,
                0.2417,
                0.2456,
                0.2494,
                0.2532,
                0.2571,
                0.2609,
                0.2647,
                0.2686,
                0.2724,
                0.2763,
                0.2801,
                0.2839,
                0.2878,
                0.2916,
                0.2955,
                0.2993,
                0.3031,
                0.307,
                0.3108,
                0.3146,
                0.3185,
                0.3223,
                0.3262,
                0.33,
                0.3338,
                0.3377,
                0.3415,
                0.3454,
                0.3492,
                0.353,
                0.3569,
                0.3607,
                0.3645,
                0.3684,
                0.3722,
                0.3761,
                0.3799,
                0.3837,
                0.3876,
                0.3914,
                0.3953,
                0.3991,
                0.4029,
                0.4068,
                0.4106,
                0.4144,
                0.4183,
                0.4221,
                0.426,
                0.4298,
                0.4336,
                0.4375,
                0.4413,
                0.4452,
                0.449,
                0.4528,
                0.4567,
                0.4605,
                0.4643,
                0.4682,
                0.472,
                0.4759,
                0.4797,
                0.4835,
                0.4874,
                0.4912,
                0.4951,
                0.4989,
                0.5027,
                0.5066,
                0.5104,
                0.5142,
                0.5181,
                0.52
                ]
    interf_ljets_ge4j_ge4t_top20_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_top20_ttcc_node)
    
    interf_ljets_ge4j_ge4t_top20_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_top20_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_top20_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top20==4))")
    interf_ljets_ge4j_ge4t_top20_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top20==4))","ljets_ge4j_ge4t_top20_ttlf_node","")
    interf_ljets_ge4j_ge4t_top20_ttlf_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_top20_ttlf_node.bin_edges = [ 
                0.1367,
                0.1433,
                0.15,
                0.1567,
                0.1633,
                0.17,
                0.1767,
                0.1833,
                0.19,
                0.1967,
                0.2033,
                0.21,
                0.2167,
                0.2233,
                0.23,
                0.2367,
                0.2433,
                0.25,
                0.2567,
                0.2633,
                0.27,
                0.2767,
                0.2833,
                0.29,
                0.2967,
                0.3033,
                0.31,
                0.3167,
                0.3233,
                0.33,
                0.3367,
                0.3433,
                0.35,
                0.3567,
                0.3633,
                0.37,
                0.3767,
                0.3833,
                0.39,
                0.3967,
                0.4033,
                0.41,
                0.4167,
                0.4233,
                0.43,
                0.4367,
                0.4433,
                0.45,
                0.4567,
                0.4633,
                0.47,
                0.4767,
                0.4833,
                0.49,
                0.4967,
                0.5033,
                0.51,
                0.5167,
                0.5233,
                0.53,
                0.5367,
                0.5433,
                0.55,
                0.5567,
                0.5633,
                0.57,
                0.5767,
                0.5833,
                0.59,
                0.5967,
                0.6033,
                0.61,
                0.6167,
                0.6233,
                0.63,
                0.6367,
                0.6433,
                0.65,
                0.6567,
                0.6633,
                0.67,
                0.6767,
                0.6833,
                0.69,
                0.6967,
                0.7033,
                0.71,
                0.7167,
                0.7233,
                0.73,
                0.7367,
                0.7433,
                0.75,
                0.7567,
                0.7633,
                0.77,
                0.7767,
                0.7833,
                0.79,
                0.7967,
                0.8
                ]
    interf_ljets_ge4j_ge4t_top20_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_top20_ttlf_node)
    
    interf_ljets_ge4j_ge4t_top20_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_top20_node_tHq",
                                            label          = "ljets_ge4j_ge4t_top20_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top20==5))")
    interf_ljets_ge4j_ge4t_top20_tHq_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top20==5))","ljets_ge4j_ge4t_top20_tHq_node","")
    interf_ljets_ge4j_ge4t_top20_tHq_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_top20_tHq_node.bin_edges = [ 
                0.1357,
                0.1443,
                0.153,
                0.1617,
                0.1704,
                0.1791,
                0.1878,
                0.1965,
                0.2052,
                0.2138,
                0.2225,
                0.2312,
                0.2399,
                0.2486,
                0.2573,
                0.266,
                0.2746,
                0.2833,
                0.292,
                0.3007,
                0.3094,
                0.3181,
                0.3268,
                0.3355,
                0.3441,
                0.3528,
                0.3615,
                0.3702,
                0.3789,
                0.3876,
                0.3963,
                0.4049,
                0.4136,
                0.4223,
                0.431,
                0.4397,
                0.4484,
                0.4571,
                0.4658,
                0.4744,
                0.4831,
                0.4918,
                0.5005,
                0.5092,
                0.5179,
                0.5266,
                0.5353,
                0.5439,
                0.5526,
                0.5613,
                0.57,
                0.5787,
                0.5874,
                0.5961,
                0.6047,
                0.6134,
                0.6221,
                0.6308,
                0.6395,
                0.6482,
                0.6569,
                0.6656,
                0.6742,
                0.6829,
                0.6916,
                0.7003,
                0.709,
                0.7177,
                0.7264,
                0.7351,
                0.7437,
                0.7524,
                0.7611,
                0.7698,
                0.7785,
                0.7872,
                0.7959,
                0.8045,
                0.8132,
                0.8219,
                0.8306,
                0.8393,
                0.848,
                0.8567,
                0.8654,
                0.874,
                0.8827,
                0.8914,
                0.9001,
                0.9088,
                0.9175,
                0.9262,
                0.9348,
                0.9435,
                0.9522,
                0.9609,
                0.9696,
                0.9783,
                0.987,
                0.9957,
                1.0
                ]
    interf_ljets_ge4j_ge4t_top20_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_top20_tHq_node)
    
    interf_ljets_ge4j_ge4t_top20_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_top20_node_tHW",
                                            label          = "ljets_ge4j_ge4t_top20_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top20==6))")
    interf_ljets_ge4j_ge4t_top20_tHW_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top20==6))","ljets_ge4j_ge4t_top20_tHW_node","")
    interf_ljets_ge4j_ge4t_top20_tHW_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_top20_tHW_node.bin_edges = [ 
                0.1357,
                0.1443,
                0.153,
                0.1617,
                0.1704,
                0.1791,
                0.1878,
                0.1965,
                0.2052,
                0.2138,
                0.2225,
                0.2312,
                0.2399,
                0.2486,
                0.2573,
                0.266,
                0.2746,
                0.2833,
                0.292,
                0.3007,
                0.3094,
                0.3181,
                0.3268,
                0.3355,
                0.3441,
                0.3528,
                0.3615,
                0.3702,
                0.3789,
                0.3876,
                0.3963,
                0.4049,
                0.4136,
                0.4223,
                0.431,
                0.4397,
                0.4484,
                0.4571,
                0.4658,
                0.4744,
                0.4831,
                0.4918,
                0.5005,
                0.5092,
                0.5179,
                0.5266,
                0.5353,
                0.5439,
                0.5526,
                0.5613,
                0.57,
                0.5787,
                0.5874,
                0.5961,
                0.6047,
                0.6134,
                0.6221,
                0.6308,
                0.6395,
                0.6482,
                0.6569,
                0.6656,
                0.6742,
                0.6829,
                0.6916,
                0.7003,
                0.709,
                0.7177,
                0.7264,
                0.7351,
                0.7437,
                0.7524,
                0.7611,
                0.7698,
                0.7785,
                0.7872,
                0.7959,
                0.8045,
                0.8132,
                0.8219,
                0.8306,
                0.8393,
                0.848,
                0.8567,
                0.8654,
                0.874,
                0.8827,
                0.8914,
                0.9001,
                0.9088,
                0.9175,
                0.9262,
                0.9348,
                0.9435,
                0.9522,
                0.9609,
                0.9696,
                0.9783,
                0.987,
                0.9957,
                1.0
                ]
    interf_ljets_ge4j_ge4t_top20_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_top20_tHW_node)
    


    # plots for ge4j_ge4t_top25

    interf_ljets_ge4j_ge4t_top25_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_top25_node_ttH",
                                            label          = "ljets_ge4j_ge4t_top25_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top25==0))")
    interf_ljets_ge4j_ge4t_top25_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top25==0))","ljets_ge4j_ge4t_top25_ttH_node","")
    interf_ljets_ge4j_ge4t_top25_ttH_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_top25_ttH_node.bin_edges = [ 
                0.1363,
                0.1437,
                0.1511,
                0.1584,
                0.1658,
                0.1732,
                0.1806,
                0.1879,
                0.1953,
                0.2027,
                0.2101,
                0.2174,
                0.2248,
                0.2322,
                0.2395,
                0.2469,
                0.2543,
                0.2617,
                0.269,
                0.2764,
                0.2838,
                0.2912,
                0.2985,
                0.3059,
                0.3133,
                0.3207,
                0.328,
                0.3354,
                0.3428,
                0.3502,
                0.3575,
                0.3649,
                0.3723,
                0.3796,
                0.387,
                0.3944,
                0.4018,
                0.4091,
                0.4165,
                0.4239,
                0.4313,
                0.4386,
                0.446,
                0.4534,
                0.4608,
                0.4681,
                0.4755,
                0.4829,
                0.4903,
                0.4976,
                0.505,
                0.5124,
                0.5197,
                0.5271,
                0.5345,
                0.5419,
                0.5492,
                0.5566,
                0.564,
                0.5714,
                0.5787,
                0.5861,
                0.5935,
                0.6009,
                0.6082,
                0.6156,
                0.623,
                0.6304,
                0.6377,
                0.6451,
                0.6525,
                0.6598,
                0.6672,
                0.6746,
                0.682,
                0.6893,
                0.6967,
                0.7041,
                0.7115,
                0.7188,
                0.7262,
                0.7336,
                0.741,
                0.7483,
                0.7557,
                0.7631,
                0.7705,
                0.7778,
                0.7852,
                0.7926,
                0.7999,
                0.8073,
                0.8147,
                0.8221,
                0.8294,
                0.8368,
                0.8442,
                0.8516,
                0.8589,
                0.8663,
                0.87
                ]
    interf_ljets_ge4j_ge4t_top25_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_top25_ttH_node)
    
    interf_ljets_ge4j_ge4t_top25_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_top25_node_ttmb",
                                            label          = "ljets_ge4j_ge4t_top25_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top25==1))")
    interf_ljets_ge4j_ge4t_top25_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top25==1))","ljets_ge4j_ge4t_top25_ttmb_node","")
    interf_ljets_ge4j_ge4t_top25_ttmb_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_top25_ttmb_node.bin_edges = [ 
                0.1369,
                0.1431,
                0.1494,
                0.1557,
                0.1619,
                0.1682,
                0.1744,
                0.1807,
                0.187,
                0.1932,
                0.1995,
                0.2058,
                0.212,
                0.2183,
                0.2245,
                0.2308,
                0.2371,
                0.2433,
                0.2496,
                0.2559,
                0.2621,
                0.2684,
                0.2746,
                0.2809,
                0.2872,
                0.2934,
                0.2997,
                0.306,
                0.3122,
                0.3185,
                0.3247,
                0.331,
                0.3373,
                0.3435,
                0.3498,
                0.3561,
                0.3623,
                0.3686,
                0.3748,
                0.3811,
                0.3874,
                0.3936,
                0.3999,
                0.4062,
                0.4124,
                0.4187,
                0.4249,
                0.4312,
                0.4375,
                0.4437,
                0.45,
                0.4563,
                0.4625,
                0.4688,
                0.4751,
                0.4813,
                0.4876,
                0.4938,
                0.5001,
                0.5064,
                0.5126,
                0.5189,
                0.5252,
                0.5314,
                0.5377,
                0.5439,
                0.5502,
                0.5565,
                0.5627,
                0.569,
                0.5753,
                0.5815,
                0.5878,
                0.594,
                0.6003,
                0.6066,
                0.6128,
                0.6191,
                0.6254,
                0.6316,
                0.6379,
                0.6441,
                0.6504,
                0.6567,
                0.6629,
                0.6692,
                0.6755,
                0.6817,
                0.688,
                0.6942,
                0.7005,
                0.7068,
                0.713,
                0.7193,
                0.7256,
                0.7318,
                0.7381,
                0.7443,
                0.7506,
                0.7569,
                0.76
                ]
    interf_ljets_ge4j_ge4t_top25_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_top25_ttmb_node)
    
    interf_ljets_ge4j_ge4t_top25_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_top25_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_top25_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top25==2))")
    interf_ljets_ge4j_ge4t_top25_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top25==2))","ljets_ge4j_ge4t_top25_tt2b_node","")
    interf_ljets_ge4j_ge4t_top25_tt2b_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_top25_tt2b_node.bin_edges = [ 
                0.1371,
                0.1429,
                0.1486,
                0.1544,
                0.1602,
                0.1659,
                0.1717,
                0.1774,
                0.1832,
                0.1889,
                0.1947,
                0.2005,
                0.2062,
                0.212,
                0.2177,
                0.2235,
                0.2292,
                0.235,
                0.2408,
                0.2465,
                0.2523,
                0.258,
                0.2638,
                0.2695,
                0.2753,
                0.2811,
                0.2868,
                0.2926,
                0.2983,
                0.3041,
                0.3098,
                0.3156,
                0.3214,
                0.3271,
                0.3329,
                0.3386,
                0.3444,
                0.3502,
                0.3559,
                0.3617,
                0.3674,
                0.3732,
                0.3789,
                0.3847,
                0.3905,
                0.3962,
                0.402,
                0.4077,
                0.4135,
                0.4192,
                0.425,
                0.4308,
                0.4365,
                0.4423,
                0.448,
                0.4538,
                0.4595,
                0.4653,
                0.4711,
                0.4768,
                0.4826,
                0.4883,
                0.4941,
                0.4998,
                0.5056,
                0.5114,
                0.5171,
                0.5229,
                0.5286,
                0.5344,
                0.5402,
                0.5459,
                0.5517,
                0.5574,
                0.5632,
                0.5689,
                0.5747,
                0.5805,
                0.5862,
                0.592,
                0.5977,
                0.6035,
                0.6092,
                0.615,
                0.6208,
                0.6265,
                0.6323,
                0.638,
                0.6438,
                0.6495,
                0.6553,
                0.6611,
                0.6668,
                0.6726,
                0.6783,
                0.6841,
                0.6898,
                0.6956,
                0.7014,
                0.7071,
                0.71
                ]
    interf_ljets_ge4j_ge4t_top25_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_top25_tt2b_node)
    
    interf_ljets_ge4j_ge4t_top25_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_top25_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_top25_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top25==3))")
    interf_ljets_ge4j_ge4t_top25_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top25==3))","ljets_ge4j_ge4t_top25_ttcc_node","")
    interf_ljets_ge4j_ge4t_top25_ttcc_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_top25_ttcc_node.bin_edges = [ 
                0.138,
                0.142,
                0.1459,
                0.1498,
                0.1538,
                0.1577,
                0.1617,
                0.1656,
                0.1695,
                0.1735,
                0.1774,
                0.1814,
                0.1853,
                0.1892,
                0.1932,
                0.1971,
                0.2011,
                0.205,
                0.2089,
                0.2129,
                0.2168,
                0.2208,
                0.2247,
                0.2286,
                0.2326,
                0.2365,
                0.2405,
                0.2444,
                0.2483,
                0.2523,
                0.2562,
                0.2602,
                0.2641,
                0.268,
                0.272,
                0.2759,
                0.2798,
                0.2838,
                0.2877,
                0.2917,
                0.2956,
                0.2995,
                0.3035,
                0.3074,
                0.3114,
                0.3153,
                0.3192,
                0.3232,
                0.3271,
                0.3311,
                0.335,
                0.3389,
                0.3429,
                0.3468,
                0.3508,
                0.3547,
                0.3586,
                0.3626,
                0.3665,
                0.3705,
                0.3744,
                0.3783,
                0.3823,
                0.3862,
                0.3902,
                0.3941,
                0.398,
                0.402,
                0.4059,
                0.4098,
                0.4138,
                0.4177,
                0.4217,
                0.4256,
                0.4295,
                0.4335,
                0.4374,
                0.4414,
                0.4453,
                0.4492,
                0.4532,
                0.4571,
                0.4611,
                0.465,
                0.4689,
                0.4729,
                0.4768,
                0.4808,
                0.4847,
                0.4886,
                0.4926,
                0.4965,
                0.5005,
                0.5044,
                0.5083,
                0.5123,
                0.5162,
                0.5202,
                0.5241,
                0.528,
                0.53
                ]
    interf_ljets_ge4j_ge4t_top25_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_top25_ttcc_node)
    
    interf_ljets_ge4j_ge4t_top25_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_top25_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_top25_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top25==4))")
    interf_ljets_ge4j_ge4t_top25_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top25==4))","ljets_ge4j_ge4t_top25_ttlf_node","")
    interf_ljets_ge4j_ge4t_top25_ttlf_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_top25_ttlf_node.bin_edges = [ 
                0.1366,
                0.1434,
                0.1502,
                0.1569,
                0.1637,
                0.1705,
                0.1772,
                0.184,
                0.1908,
                0.1975,
                0.2043,
                0.2111,
                0.2178,
                0.2246,
                0.2314,
                0.2381,
                0.2449,
                0.2517,
                0.2584,
                0.2652,
                0.272,
                0.2787,
                0.2855,
                0.2923,
                0.299,
                0.3058,
                0.3126,
                0.3193,
                0.3261,
                0.3329,
                0.3396,
                0.3464,
                0.3532,
                0.3599,
                0.3667,
                0.3735,
                0.3803,
                0.387,
                0.3938,
                0.4006,
                0.4073,
                0.4141,
                0.4209,
                0.4276,
                0.4344,
                0.4412,
                0.4479,
                0.4547,
                0.4615,
                0.4682,
                0.475,
                0.4818,
                0.4885,
                0.4953,
                0.5021,
                0.5088,
                0.5156,
                0.5224,
                0.5291,
                0.5359,
                0.5427,
                0.5494,
                0.5562,
                0.563,
                0.5697,
                0.5765,
                0.5833,
                0.5901,
                0.5968,
                0.6036,
                0.6104,
                0.6171,
                0.6239,
                0.6307,
                0.6374,
                0.6442,
                0.651,
                0.6577,
                0.6645,
                0.6713,
                0.678,
                0.6848,
                0.6916,
                0.6983,
                0.7051,
                0.7119,
                0.7186,
                0.7254,
                0.7322,
                0.7389,
                0.7457,
                0.7525,
                0.7592,
                0.766,
                0.7728,
                0.7795,
                0.7863,
                0.7931,
                0.7998,
                0.8066,
                0.81
                ]
    interf_ljets_ge4j_ge4t_top25_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_top25_ttlf_node)
    
    interf_ljets_ge4j_ge4t_top25_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_top25_node_tHq",
                                            label          = "ljets_ge4j_ge4t_top25_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top25==5))")
    interf_ljets_ge4j_ge4t_top25_tHq_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top25==5))","ljets_ge4j_ge4t_top25_tHq_node","")
    interf_ljets_ge4j_ge4t_top25_tHq_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_top25_tHq_node.bin_edges = [ 
                0.1357,
                0.1443,
                0.153,
                0.1617,
                0.1704,
                0.1791,
                0.1878,
                0.1965,
                0.2052,
                0.2138,
                0.2225,
                0.2312,
                0.2399,
                0.2486,
                0.2573,
                0.266,
                0.2746,
                0.2833,
                0.292,
                0.3007,
                0.3094,
                0.3181,
                0.3268,
                0.3355,
                0.3441,
                0.3528,
                0.3615,
                0.3702,
                0.3789,
                0.3876,
                0.3963,
                0.4049,
                0.4136,
                0.4223,
                0.431,
                0.4397,
                0.4484,
                0.4571,
                0.4658,
                0.4744,
                0.4831,
                0.4918,
                0.5005,
                0.5092,
                0.5179,
                0.5266,
                0.5353,
                0.5439,
                0.5526,
                0.5613,
                0.57,
                0.5787,
                0.5874,
                0.5961,
                0.6047,
                0.6134,
                0.6221,
                0.6308,
                0.6395,
                0.6482,
                0.6569,
                0.6656,
                0.6742,
                0.6829,
                0.6916,
                0.7003,
                0.709,
                0.7177,
                0.7264,
                0.7351,
                0.7437,
                0.7524,
                0.7611,
                0.7698,
                0.7785,
                0.7872,
                0.7959,
                0.8045,
                0.8132,
                0.8219,
                0.8306,
                0.8393,
                0.848,
                0.8567,
                0.8654,
                0.874,
                0.8827,
                0.8914,
                0.9001,
                0.9088,
                0.9175,
                0.9262,
                0.9348,
                0.9435,
                0.9522,
                0.9609,
                0.9696,
                0.9783,
                0.987,
                0.9957,
                1.0
                ]
    interf_ljets_ge4j_ge4t_top25_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_top25_tHq_node)
    
    interf_ljets_ge4j_ge4t_top25_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_top25_node_tHW",
                                            label          = "ljets_ge4j_ge4t_top25_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top25==6))")
    interf_ljets_ge4j_ge4t_top25_tHW_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top25==6))","ljets_ge4j_ge4t_top25_tHW_node","")
    interf_ljets_ge4j_ge4t_top25_tHW_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_top25_tHW_node.bin_edges = [ 
                0.1357,
                0.1443,
                0.153,
                0.1617,
                0.1704,
                0.1791,
                0.1878,
                0.1965,
                0.2052,
                0.2138,
                0.2225,
                0.2312,
                0.2399,
                0.2486,
                0.2573,
                0.266,
                0.2746,
                0.2833,
                0.292,
                0.3007,
                0.3094,
                0.3181,
                0.3268,
                0.3355,
                0.3441,
                0.3528,
                0.3615,
                0.3702,
                0.3789,
                0.3876,
                0.3963,
                0.4049,
                0.4136,
                0.4223,
                0.431,
                0.4397,
                0.4484,
                0.4571,
                0.4658,
                0.4744,
                0.4831,
                0.4918,
                0.5005,
                0.5092,
                0.5179,
                0.5266,
                0.5353,
                0.5439,
                0.5526,
                0.5613,
                0.57,
                0.5787,
                0.5874,
                0.5961,
                0.6047,
                0.6134,
                0.6221,
                0.6308,
                0.6395,
                0.6482,
                0.6569,
                0.6656,
                0.6742,
                0.6829,
                0.6916,
                0.7003,
                0.709,
                0.7177,
                0.7264,
                0.7351,
                0.7437,
                0.7524,
                0.7611,
                0.7698,
                0.7785,
                0.7872,
                0.7959,
                0.8045,
                0.8132,
                0.8219,
                0.8306,
                0.8393,
                0.848,
                0.8567,
                0.8654,
                0.874,
                0.8827,
                0.8914,
                0.9001,
                0.9088,
                0.9175,
                0.9262,
                0.9348,
                0.9435,
                0.9522,
                0.9609,
                0.9696,
                0.9783,
                0.987,
                0.9957,
                1.0
                ]
    interf_ljets_ge4j_ge4t_top25_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_top25_tHW_node)
    


    # plots for ge4j_ge4t_top30

    interf_ljets_ge4j_ge4t_top30_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_top30_node_ttH",
                                            label          = "ljets_ge4j_ge4t_top30_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top30==0))")
    interf_ljets_ge4j_ge4t_top30_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top30==0))","ljets_ge4j_ge4t_top30_ttH_node","")
    interf_ljets_ge4j_ge4t_top30_ttH_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_top30_ttH_node.bin_edges = [ 
                0.1363,
                0.1437,
                0.1511,
                0.1584,
                0.1658,
                0.1732,
                0.1806,
                0.1879,
                0.1953,
                0.2027,
                0.2101,
                0.2174,
                0.2248,
                0.2322,
                0.2395,
                0.2469,
                0.2543,
                0.2617,
                0.269,
                0.2764,
                0.2838,
                0.2912,
                0.2985,
                0.3059,
                0.3133,
                0.3207,
                0.328,
                0.3354,
                0.3428,
                0.3502,
                0.3575,
                0.3649,
                0.3723,
                0.3796,
                0.387,
                0.3944,
                0.4018,
                0.4091,
                0.4165,
                0.4239,
                0.4313,
                0.4386,
                0.446,
                0.4534,
                0.4608,
                0.4681,
                0.4755,
                0.4829,
                0.4903,
                0.4976,
                0.505,
                0.5124,
                0.5197,
                0.5271,
                0.5345,
                0.5419,
                0.5492,
                0.5566,
                0.564,
                0.5714,
                0.5787,
                0.5861,
                0.5935,
                0.6009,
                0.6082,
                0.6156,
                0.623,
                0.6304,
                0.6377,
                0.6451,
                0.6525,
                0.6598,
                0.6672,
                0.6746,
                0.682,
                0.6893,
                0.6967,
                0.7041,
                0.7115,
                0.7188,
                0.7262,
                0.7336,
                0.741,
                0.7483,
                0.7557,
                0.7631,
                0.7705,
                0.7778,
                0.7852,
                0.7926,
                0.7999,
                0.8073,
                0.8147,
                0.8221,
                0.8294,
                0.8368,
                0.8442,
                0.8516,
                0.8589,
                0.8663,
                0.87
                ]
    interf_ljets_ge4j_ge4t_top30_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_top30_ttH_node)
    
    interf_ljets_ge4j_ge4t_top30_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_top30_node_ttmb",
                                            label          = "ljets_ge4j_ge4t_top30_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top30==1))")
    interf_ljets_ge4j_ge4t_top30_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top30==1))","ljets_ge4j_ge4t_top30_ttmb_node","")
    interf_ljets_ge4j_ge4t_top30_ttmb_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_top30_ttmb_node.bin_edges = [ 
                0.1366,
                0.1434,
                0.1503,
                0.1572,
                0.164,
                0.1709,
                0.1778,
                0.1846,
                0.1915,
                0.1984,
                0.2053,
                0.2121,
                0.219,
                0.2259,
                0.2327,
                0.2396,
                0.2465,
                0.2533,
                0.2602,
                0.2671,
                0.2739,
                0.2808,
                0.2877,
                0.2945,
                0.3014,
                0.3083,
                0.3152,
                0.322,
                0.3289,
                0.3358,
                0.3426,
                0.3495,
                0.3564,
                0.3632,
                0.3701,
                0.377,
                0.3838,
                0.3907,
                0.3976,
                0.4044,
                0.4113,
                0.4182,
                0.4251,
                0.4319,
                0.4388,
                0.4457,
                0.4525,
                0.4594,
                0.4663,
                0.4731,
                0.48,
                0.4869,
                0.4937,
                0.5006,
                0.5075,
                0.5143,
                0.5212,
                0.5281,
                0.5349,
                0.5418,
                0.5487,
                0.5556,
                0.5624,
                0.5693,
                0.5762,
                0.583,
                0.5899,
                0.5968,
                0.6036,
                0.6105,
                0.6174,
                0.6242,
                0.6311,
                0.638,
                0.6448,
                0.6517,
                0.6586,
                0.6655,
                0.6723,
                0.6792,
                0.6861,
                0.6929,
                0.6998,
                0.7067,
                0.7135,
                0.7204,
                0.7273,
                0.7341,
                0.741,
                0.7479,
                0.7547,
                0.7616,
                0.7685,
                0.7754,
                0.7822,
                0.7891,
                0.796,
                0.8028,
                0.8097,
                0.8166,
                0.82
                ]
    interf_ljets_ge4j_ge4t_top30_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_top30_ttmb_node)
    
    interf_ljets_ge4j_ge4t_top30_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_top30_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_top30_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top30==2))")
    interf_ljets_ge4j_ge4t_top30_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top30==2))","ljets_ge4j_ge4t_top30_tt2b_node","")
    interf_ljets_ge4j_ge4t_top30_tt2b_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_top30_tt2b_node.bin_edges = [ 
                0.1373,
                0.1427,
                0.148,
                0.1534,
                0.1587,
                0.1641,
                0.1694,
                0.1748,
                0.1802,
                0.1855,
                0.1909,
                0.1962,
                0.2016,
                0.2069,
                0.2123,
                0.2176,
                0.223,
                0.2283,
                0.2337,
                0.239,
                0.2444,
                0.2497,
                0.2551,
                0.2605,
                0.2658,
                0.2712,
                0.2765,
                0.2819,
                0.2872,
                0.2926,
                0.2979,
                0.3033,
                0.3086,
                0.314,
                0.3193,
                0.3247,
                0.3301,
                0.3354,
                0.3408,
                0.3461,
                0.3515,
                0.3568,
                0.3622,
                0.3675,
                0.3729,
                0.3782,
                0.3836,
                0.3889,
                0.3943,
                0.3996,
                0.405,
                0.4104,
                0.4157,
                0.4211,
                0.4264,
                0.4318,
                0.4371,
                0.4425,
                0.4478,
                0.4532,
                0.4585,
                0.4639,
                0.4692,
                0.4746,
                0.4799,
                0.4853,
                0.4907,
                0.496,
                0.5014,
                0.5067,
                0.5121,
                0.5174,
                0.5228,
                0.5281,
                0.5335,
                0.5388,
                0.5442,
                0.5495,
                0.5549,
                0.5603,
                0.5656,
                0.571,
                0.5763,
                0.5817,
                0.587,
                0.5924,
                0.5977,
                0.6031,
                0.6084,
                0.6138,
                0.6191,
                0.6245,
                0.6298,
                0.6352,
                0.6406,
                0.6459,
                0.6513,
                0.6566,
                0.662,
                0.6673,
                0.67
                ]
    interf_ljets_ge4j_ge4t_top30_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_top30_tt2b_node)
    
    interf_ljets_ge4j_ge4t_top30_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_top30_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_top30_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top30==3))")
    interf_ljets_ge4j_ge4t_top30_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top30==3))","ljets_ge4j_ge4t_top30_ttcc_node","")
    interf_ljets_ge4j_ge4t_top30_ttcc_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_top30_ttcc_node.bin_edges = [ 
                0.1377,
                0.1423,
                0.1468,
                0.1514,
                0.1559,
                0.1605,
                0.165,
                0.1695,
                0.1741,
                0.1786,
                0.1832,
                0.1877,
                0.1923,
                0.1968,
                0.2014,
                0.2059,
                0.2105,
                0.215,
                0.2195,
                0.2241,
                0.2286,
                0.2332,
                0.2377,
                0.2423,
                0.2468,
                0.2514,
                0.2559,
                0.2605,
                0.265,
                0.2695,
                0.2741,
                0.2786,
                0.2832,
                0.2877,
                0.2923,
                0.2968,
                0.3014,
                0.3059,
                0.3105,
                0.315,
                0.3195,
                0.3241,
                0.3286,
                0.3332,
                0.3377,
                0.3423,
                0.3468,
                0.3514,
                0.3559,
                0.3605,
                0.365,
                0.3695,
                0.3741,
                0.3786,
                0.3832,
                0.3877,
                0.3923,
                0.3968,
                0.4014,
                0.4059,
                0.4105,
                0.415,
                0.4195,
                0.4241,
                0.4286,
                0.4332,
                0.4377,
                0.4423,
                0.4468,
                0.4514,
                0.4559,
                0.4605,
                0.465,
                0.4695,
                0.4741,
                0.4786,
                0.4832,
                0.4877,
                0.4923,
                0.4968,
                0.5014,
                0.5059,
                0.5105,
                0.515,
                0.5195,
                0.5241,
                0.5286,
                0.5332,
                0.5377,
                0.5423,
                0.5468,
                0.5514,
                0.5559,
                0.5605,
                0.565,
                0.5695,
                0.5741,
                0.5786,
                0.5832,
                0.5877,
                0.59
                ]
    interf_ljets_ge4j_ge4t_top30_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_top30_ttcc_node)
    
    interf_ljets_ge4j_ge4t_top30_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_top30_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_top30_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top30==4))")
    interf_ljets_ge4j_ge4t_top30_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top30==4))","ljets_ge4j_ge4t_top30_ttlf_node","")
    interf_ljets_ge4j_ge4t_top30_ttlf_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_top30_ttlf_node.bin_edges = [ 
                0.1368,
                0.1432,
                0.1495,
                0.1559,
                0.1623,
                0.1686,
                0.175,
                0.1814,
                0.1877,
                0.1941,
                0.2005,
                0.2068,
                0.2132,
                0.2195,
                0.2259,
                0.2323,
                0.2386,
                0.245,
                0.2514,
                0.2577,
                0.2641,
                0.2705,
                0.2768,
                0.2832,
                0.2895,
                0.2959,
                0.3023,
                0.3086,
                0.315,
                0.3214,
                0.3277,
                0.3341,
                0.3405,
                0.3468,
                0.3532,
                0.3595,
                0.3659,
                0.3723,
                0.3786,
                0.385,
                0.3914,
                0.3977,
                0.4041,
                0.4105,
                0.4168,
                0.4232,
                0.4295,
                0.4359,
                0.4423,
                0.4486,
                0.455,
                0.4614,
                0.4677,
                0.4741,
                0.4805,
                0.4868,
                0.4932,
                0.4995,
                0.5059,
                0.5123,
                0.5186,
                0.525,
                0.5314,
                0.5377,
                0.5441,
                0.5505,
                0.5568,
                0.5632,
                0.5695,
                0.5759,
                0.5823,
                0.5886,
                0.595,
                0.6014,
                0.6077,
                0.6141,
                0.6205,
                0.6268,
                0.6332,
                0.6395,
                0.6459,
                0.6523,
                0.6586,
                0.665,
                0.6714,
                0.6777,
                0.6841,
                0.6905,
                0.6968,
                0.7032,
                0.7095,
                0.7159,
                0.7223,
                0.7286,
                0.735,
                0.7414,
                0.7477,
                0.7541,
                0.7605,
                0.7668,
                0.77
                ]
    interf_ljets_ge4j_ge4t_top30_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_top30_ttlf_node)
    
    interf_ljets_ge4j_ge4t_top30_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_top30_node_tHq",
                                            label          = "ljets_ge4j_ge4t_top30_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top30==5))")
    interf_ljets_ge4j_ge4t_top30_tHq_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top30==5))","ljets_ge4j_ge4t_top30_tHq_node","")
    interf_ljets_ge4j_ge4t_top30_tHq_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_top30_tHq_node.bin_edges = [ 
                0.1357,
                0.1443,
                0.153,
                0.1617,
                0.1704,
                0.1791,
                0.1878,
                0.1965,
                0.2052,
                0.2138,
                0.2225,
                0.2312,
                0.2399,
                0.2486,
                0.2573,
                0.266,
                0.2746,
                0.2833,
                0.292,
                0.3007,
                0.3094,
                0.3181,
                0.3268,
                0.3355,
                0.3441,
                0.3528,
                0.3615,
                0.3702,
                0.3789,
                0.3876,
                0.3963,
                0.4049,
                0.4136,
                0.4223,
                0.431,
                0.4397,
                0.4484,
                0.4571,
                0.4658,
                0.4744,
                0.4831,
                0.4918,
                0.5005,
                0.5092,
                0.5179,
                0.5266,
                0.5353,
                0.5439,
                0.5526,
                0.5613,
                0.57,
                0.5787,
                0.5874,
                0.5961,
                0.6047,
                0.6134,
                0.6221,
                0.6308,
                0.6395,
                0.6482,
                0.6569,
                0.6656,
                0.6742,
                0.6829,
                0.6916,
                0.7003,
                0.709,
                0.7177,
                0.7264,
                0.7351,
                0.7437,
                0.7524,
                0.7611,
                0.7698,
                0.7785,
                0.7872,
                0.7959,
                0.8045,
                0.8132,
                0.8219,
                0.8306,
                0.8393,
                0.848,
                0.8567,
                0.8654,
                0.874,
                0.8827,
                0.8914,
                0.9001,
                0.9088,
                0.9175,
                0.9262,
                0.9348,
                0.9435,
                0.9522,
                0.9609,
                0.9696,
                0.9783,
                0.987,
                0.9957,
                1.0
                ]
    interf_ljets_ge4j_ge4t_top30_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_top30_tHq_node)
    
    interf_ljets_ge4j_ge4t_top30_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_top30_node_tHW",
                                            label          = "ljets_ge4j_ge4t_top30_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top30==6))")
    interf_ljets_ge4j_ge4t_top30_tHW_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_top30==6))","ljets_ge4j_ge4t_top30_tHW_node","")
    interf_ljets_ge4j_ge4t_top30_tHW_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_top30_tHW_node.bin_edges = [ 
                0.1357,
                0.1443,
                0.153,
                0.1617,
                0.1704,
                0.1791,
                0.1878,
                0.1965,
                0.2052,
                0.2138,
                0.2225,
                0.2312,
                0.2399,
                0.2486,
                0.2573,
                0.266,
                0.2746,
                0.2833,
                0.292,
                0.3007,
                0.3094,
                0.3181,
                0.3268,
                0.3355,
                0.3441,
                0.3528,
                0.3615,
                0.3702,
                0.3789,
                0.3876,
                0.3963,
                0.4049,
                0.4136,
                0.4223,
                0.431,
                0.4397,
                0.4484,
                0.4571,
                0.4658,
                0.4744,
                0.4831,
                0.4918,
                0.5005,
                0.5092,
                0.5179,
                0.5266,
                0.5353,
                0.5439,
                0.5526,
                0.5613,
                0.57,
                0.5787,
                0.5874,
                0.5961,
                0.6047,
                0.6134,
                0.6221,
                0.6308,
                0.6395,
                0.6482,
                0.6569,
                0.6656,
                0.6742,
                0.6829,
                0.6916,
                0.7003,
                0.709,
                0.7177,
                0.7264,
                0.7351,
                0.7437,
                0.7524,
                0.7611,
                0.7698,
                0.7785,
                0.7872,
                0.7959,
                0.8045,
                0.8132,
                0.8219,
                0.8306,
                0.8393,
                0.848,
                0.8567,
                0.8654,
                0.874,
                0.8827,
                0.8914,
                0.9001,
                0.9088,
                0.9175,
                0.9262,
                0.9348,
                0.9435,
                0.9522,
                0.9609,
                0.9696,
                0.9783,
                0.987,
                0.9957,
                1.0
                ]
    interf_ljets_ge4j_ge4t_top30_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_top30_tHW_node)
    


    # plots for ge4j_3t_top20

    interf_ljets_ge4j_3t_top20_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_top20_node_ttH",
                                            label          = "ljets_ge4j_3t_top20_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top20==0))")
    interf_ljets_ge4j_3t_top20_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top20==0))","ljets_ge4j_3t_top20_ttH_node","")
    interf_ljets_ge4j_3t_top20_ttH_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_top20_ttH_node.bin_edges = [ 
                0.1367,
                0.1433,
                0.1498,
                0.1564,
                0.163,
                0.1695,
                0.1761,
                0.1827,
                0.1892,
                0.1958,
                0.2024,
                0.2089,
                0.2155,
                0.2221,
                0.2286,
                0.2352,
                0.2418,
                0.2483,
                0.2549,
                0.2615,
                0.268,
                0.2746,
                0.2812,
                0.2877,
                0.2943,
                0.3009,
                0.3074,
                0.314,
                0.3206,
                0.3271,
                0.3337,
                0.3403,
                0.3468,
                0.3534,
                0.3599,
                0.3665,
                0.3731,
                0.3796,
                0.3862,
                0.3928,
                0.3993,
                0.4059,
                0.4125,
                0.419,
                0.4256,
                0.4322,
                0.4387,
                0.4453,
                0.4519,
                0.4584,
                0.465,
                0.4716,
                0.4781,
                0.4847,
                0.4913,
                0.4978,
                0.5044,
                0.511,
                0.5175,
                0.5241,
                0.5307,
                0.5372,
                0.5438,
                0.5504,
                0.5569,
                0.5635,
                0.5701,
                0.5766,
                0.5832,
                0.5897,
                0.5963,
                0.6029,
                0.6094,
                0.616,
                0.6226,
                0.6291,
                0.6357,
                0.6423,
                0.6488,
                0.6554,
                0.662,
                0.6685,
                0.6751,
                0.6817,
                0.6882,
                0.6948,
                0.7014,
                0.7079,
                0.7145,
                0.7211,
                0.7276,
                0.7342,
                0.7408,
                0.7473,
                0.7539,
                0.7605,
                0.767,
                0.7736,
                0.7802,
                0.7867,
                0.79
                ]
    interf_ljets_ge4j_3t_top20_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_top20_ttH_node)
    
    interf_ljets_ge4j_3t_top20_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_top20_node_ttmb",
                                            label          = "ljets_ge4j_3t_top20_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top20==1))")
    interf_ljets_ge4j_3t_top20_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top20==1))","ljets_ge4j_3t_top20_ttmb_node","")
    interf_ljets_ge4j_3t_top20_ttmb_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_top20_ttmb_node.bin_edges = [ 
                0.1382,
                0.1418,
                0.1455,
                0.1491,
                0.1527,
                0.1564,
                0.16,
                0.1636,
                0.1673,
                0.1709,
                0.1745,
                0.1782,
                0.1818,
                0.1855,
                0.1891,
                0.1927,
                0.1964,
                0.2,
                0.2036,
                0.2073,
                0.2109,
                0.2145,
                0.2182,
                0.2218,
                0.2255,
                0.2291,
                0.2327,
                0.2364,
                0.24,
                0.2436,
                0.2473,
                0.2509,
                0.2545,
                0.2582,
                0.2618,
                0.2655,
                0.2691,
                0.2727,
                0.2764,
                0.28,
                0.2836,
                0.2873,
                0.2909,
                0.2945,
                0.2982,
                0.3018,
                0.3055,
                0.3091,
                0.3127,
                0.3164,
                0.32,
                0.3236,
                0.3273,
                0.3309,
                0.3345,
                0.3382,
                0.3418,
                0.3455,
                0.3491,
                0.3527,
                0.3564,
                0.36,
                0.3636,
                0.3673,
                0.3709,
                0.3745,
                0.3782,
                0.3818,
                0.3855,
                0.3891,
                0.3927,
                0.3964,
                0.4,
                0.4036,
                0.4073,
                0.4109,
                0.4145,
                0.4182,
                0.4218,
                0.4255,
                0.4291,
                0.4327,
                0.4364,
                0.44,
                0.4436,
                0.4473,
                0.4509,
                0.4545,
                0.4582,
                0.4618,
                0.4655,
                0.4691,
                0.4727,
                0.4764,
                0.48,
                0.4836,
                0.4873,
                0.4909,
                0.4945,
                0.4982,
                0.5
                ]
    interf_ljets_ge4j_3t_top20_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_top20_ttmb_node)
    
    interf_ljets_ge4j_3t_top20_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_top20_node_tt2b",
                                            label          = "ljets_ge4j_3t_top20_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top20==2))")
    interf_ljets_ge4j_3t_top20_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top20==2))","ljets_ge4j_3t_top20_tt2b_node","")
    interf_ljets_ge4j_3t_top20_tt2b_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_top20_tt2b_node.bin_edges = [ 
                0.1369,
                0.1431,
                0.1494,
                0.1557,
                0.1619,
                0.1682,
                0.1744,
                0.1807,
                0.187,
                0.1932,
                0.1995,
                0.2058,
                0.212,
                0.2183,
                0.2245,
                0.2308,
                0.2371,
                0.2433,
                0.2496,
                0.2559,
                0.2621,
                0.2684,
                0.2746,
                0.2809,
                0.2872,
                0.2934,
                0.2997,
                0.306,
                0.3122,
                0.3185,
                0.3247,
                0.331,
                0.3373,
                0.3435,
                0.3498,
                0.3561,
                0.3623,
                0.3686,
                0.3748,
                0.3811,
                0.3874,
                0.3936,
                0.3999,
                0.4062,
                0.4124,
                0.4187,
                0.4249,
                0.4312,
                0.4375,
                0.4437,
                0.45,
                0.4563,
                0.4625,
                0.4688,
                0.4751,
                0.4813,
                0.4876,
                0.4938,
                0.5001,
                0.5064,
                0.5126,
                0.5189,
                0.5252,
                0.5314,
                0.5377,
                0.5439,
                0.5502,
                0.5565,
                0.5627,
                0.569,
                0.5753,
                0.5815,
                0.5878,
                0.594,
                0.6003,
                0.6066,
                0.6128,
                0.6191,
                0.6254,
                0.6316,
                0.6379,
                0.6441,
                0.6504,
                0.6567,
                0.6629,
                0.6692,
                0.6755,
                0.6817,
                0.688,
                0.6942,
                0.7005,
                0.7068,
                0.713,
                0.7193,
                0.7256,
                0.7318,
                0.7381,
                0.7443,
                0.7506,
                0.7569,
                0.76
                ]
    interf_ljets_ge4j_3t_top20_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_top20_tt2b_node)
    
    interf_ljets_ge4j_3t_top20_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_top20_node_ttcc",
                                            label          = "ljets_ge4j_3t_top20_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top20==3))")
    interf_ljets_ge4j_3t_top20_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top20==3))","ljets_ge4j_3t_top20_ttcc_node","")
    interf_ljets_ge4j_3t_top20_ttcc_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_top20_ttcc_node.bin_edges = [ 
                0.1383,
                0.1417,
                0.145,
                0.1483,
                0.1517,
                0.155,
                0.1583,
                0.1617,
                0.165,
                0.1683,
                0.1717,
                0.175,
                0.1783,
                0.1817,
                0.185,
                0.1883,
                0.1917,
                0.195,
                0.1983,
                0.2017,
                0.205,
                0.2083,
                0.2117,
                0.215,
                0.2183,
                0.2217,
                0.225,
                0.2283,
                0.2317,
                0.235,
                0.2383,
                0.2417,
                0.245,
                0.2483,
                0.2517,
                0.255,
                0.2583,
                0.2617,
                0.265,
                0.2683,
                0.2717,
                0.275,
                0.2783,
                0.2817,
                0.285,
                0.2883,
                0.2917,
                0.295,
                0.2983,
                0.3017,
                0.305,
                0.3083,
                0.3117,
                0.315,
                0.3183,
                0.3217,
                0.325,
                0.3283,
                0.3317,
                0.335,
                0.3383,
                0.3417,
                0.345,
                0.3483,
                0.3517,
                0.355,
                0.3583,
                0.3617,
                0.365,
                0.3683,
                0.3717,
                0.375,
                0.3783,
                0.3817,
                0.385,
                0.3883,
                0.3917,
                0.395,
                0.3983,
                0.4017,
                0.405,
                0.4083,
                0.4117,
                0.415,
                0.4183,
                0.4217,
                0.425,
                0.4283,
                0.4317,
                0.435,
                0.4383,
                0.4417,
                0.445,
                0.4483,
                0.4517,
                0.455,
                0.4583,
                0.4617,
                0.465,
                0.4683,
                0.47
                ]
    interf_ljets_ge4j_3t_top20_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_top20_ttcc_node)
    
    interf_ljets_ge4j_3t_top20_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_top20_node_ttlf",
                                            label          = "ljets_ge4j_3t_top20_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top20==4))")
    interf_ljets_ge4j_3t_top20_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top20==4))","ljets_ge4j_3t_top20_ttlf_node","")
    interf_ljets_ge4j_3t_top20_ttlf_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_top20_ttlf_node.bin_edges = [ 
                0.1364,
                0.1436,
                0.1508,
                0.1579,
                0.1651,
                0.1723,
                0.1794,
                0.1866,
                0.1938,
                0.201,
                0.2081,
                0.2153,
                0.2225,
                0.2296,
                0.2368,
                0.244,
                0.2512,
                0.2583,
                0.2655,
                0.2727,
                0.2798,
                0.287,
                0.2942,
                0.3014,
                0.3085,
                0.3157,
                0.3229,
                0.3301,
                0.3372,
                0.3444,
                0.3516,
                0.3587,
                0.3659,
                0.3731,
                0.3803,
                0.3874,
                0.3946,
                0.4018,
                0.4089,
                0.4161,
                0.4233,
                0.4305,
                0.4376,
                0.4448,
                0.452,
                0.4591,
                0.4663,
                0.4735,
                0.4807,
                0.4878,
                0.495,
                0.5022,
                0.5093,
                0.5165,
                0.5237,
                0.5309,
                0.538,
                0.5452,
                0.5524,
                0.5595,
                0.5667,
                0.5739,
                0.5811,
                0.5882,
                0.5954,
                0.6026,
                0.6097,
                0.6169,
                0.6241,
                0.6313,
                0.6384,
                0.6456,
                0.6528,
                0.6599,
                0.6671,
                0.6743,
                0.6815,
                0.6886,
                0.6958,
                0.703,
                0.7102,
                0.7173,
                0.7245,
                0.7317,
                0.7388,
                0.746,
                0.7532,
                0.7604,
                0.7675,
                0.7747,
                0.7819,
                0.789,
                0.7962,
                0.8034,
                0.8106,
                0.8177,
                0.8249,
                0.8321,
                0.8392,
                0.8464,
                0.85
                ]
    interf_ljets_ge4j_3t_top20_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_top20_ttlf_node)
    
    interf_ljets_ge4j_3t_top20_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_top20_node_tHq",
                                            label          = "ljets_ge4j_3t_top20_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top20==5))")
    interf_ljets_ge4j_3t_top20_tHq_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top20==5))","ljets_ge4j_3t_top20_tHq_node","")
    interf_ljets_ge4j_3t_top20_tHq_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_top20_tHq_node.bin_edges = [ 
                0.1358,
                0.1442,
                0.1527,
                0.1612,
                0.1697,
                0.1782,
                0.1867,
                0.1952,
                0.2036,
                0.2121,
                0.2206,
                0.2291,
                0.2376,
                0.2461,
                0.2545,
                0.263,
                0.2715,
                0.28,
                0.2885,
                0.297,
                0.3055,
                0.3139,
                0.3224,
                0.3309,
                0.3394,
                0.3479,
                0.3564,
                0.3648,
                0.3733,
                0.3818,
                0.3903,
                0.3988,
                0.4073,
                0.4158,
                0.4242,
                0.4327,
                0.4412,
                0.4497,
                0.4582,
                0.4667,
                0.4752,
                0.4836,
                0.4921,
                0.5006,
                0.5091,
                0.5176,
                0.5261,
                0.5345,
                0.543,
                0.5515,
                0.56,
                0.5685,
                0.577,
                0.5855,
                0.5939,
                0.6024,
                0.6109,
                0.6194,
                0.6279,
                0.6364,
                0.6448,
                0.6533,
                0.6618,
                0.6703,
                0.6788,
                0.6873,
                0.6958,
                0.7042,
                0.7127,
                0.7212,
                0.7297,
                0.7382,
                0.7467,
                0.7552,
                0.7636,
                0.7721,
                0.7806,
                0.7891,
                0.7976,
                0.8061,
                0.8145,
                0.823,
                0.8315,
                0.84,
                0.8485,
                0.857,
                0.8655,
                0.8739,
                0.8824,
                0.8909,
                0.8994,
                0.9079,
                0.9164,
                0.9248,
                0.9333,
                0.9418,
                0.9503,
                0.9588,
                0.9673,
                0.9758,
                0.98
                ]
    interf_ljets_ge4j_3t_top20_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_top20_tHq_node)
    
    interf_ljets_ge4j_3t_top20_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_top20_node_tHW",
                                            label          = "ljets_ge4j_3t_top20_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top20==6))")
    interf_ljets_ge4j_3t_top20_tHW_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top20==6))","ljets_ge4j_3t_top20_tHW_node","")
    interf_ljets_ge4j_3t_top20_tHW_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_top20_tHW_node.bin_edges = [ 
                0.1357,
                0.1443,
                0.153,
                0.1617,
                0.1704,
                0.1791,
                0.1878,
                0.1965,
                0.2052,
                0.2138,
                0.2225,
                0.2312,
                0.2399,
                0.2486,
                0.2573,
                0.266,
                0.2746,
                0.2833,
                0.292,
                0.3007,
                0.3094,
                0.3181,
                0.3268,
                0.3355,
                0.3441,
                0.3528,
                0.3615,
                0.3702,
                0.3789,
                0.3876,
                0.3963,
                0.4049,
                0.4136,
                0.4223,
                0.431,
                0.4397,
                0.4484,
                0.4571,
                0.4658,
                0.4744,
                0.4831,
                0.4918,
                0.5005,
                0.5092,
                0.5179,
                0.5266,
                0.5353,
                0.5439,
                0.5526,
                0.5613,
                0.57,
                0.5787,
                0.5874,
                0.5961,
                0.6047,
                0.6134,
                0.6221,
                0.6308,
                0.6395,
                0.6482,
                0.6569,
                0.6656,
                0.6742,
                0.6829,
                0.6916,
                0.7003,
                0.709,
                0.7177,
                0.7264,
                0.7351,
                0.7437,
                0.7524,
                0.7611,
                0.7698,
                0.7785,
                0.7872,
                0.7959,
                0.8045,
                0.8132,
                0.8219,
                0.8306,
                0.8393,
                0.848,
                0.8567,
                0.8654,
                0.874,
                0.8827,
                0.8914,
                0.9001,
                0.9088,
                0.9175,
                0.9262,
                0.9348,
                0.9435,
                0.9522,
                0.9609,
                0.9696,
                0.9783,
                0.987,
                0.9957,
                1.0
                ]
    interf_ljets_ge4j_3t_top20_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_top20_tHW_node)
    


    # plots for ge4j_3t_top25

    interf_ljets_ge4j_3t_top25_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_top25_node_ttH",
                                            label          = "ljets_ge4j_3t_top25_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top25==0))")
    interf_ljets_ge4j_3t_top25_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top25==0))","ljets_ge4j_3t_top25_ttH_node","")
    interf_ljets_ge4j_3t_top25_ttH_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_top25_ttH_node.bin_edges = [ 
                0.1366,
                0.1434,
                0.1502,
                0.1569,
                0.1637,
                0.1705,
                0.1772,
                0.184,
                0.1908,
                0.1975,
                0.2043,
                0.2111,
                0.2178,
                0.2246,
                0.2314,
                0.2381,
                0.2449,
                0.2517,
                0.2584,
                0.2652,
                0.272,
                0.2787,
                0.2855,
                0.2923,
                0.299,
                0.3058,
                0.3126,
                0.3193,
                0.3261,
                0.3329,
                0.3396,
                0.3464,
                0.3532,
                0.3599,
                0.3667,
                0.3735,
                0.3803,
                0.387,
                0.3938,
                0.4006,
                0.4073,
                0.4141,
                0.4209,
                0.4276,
                0.4344,
                0.4412,
                0.4479,
                0.4547,
                0.4615,
                0.4682,
                0.475,
                0.4818,
                0.4885,
                0.4953,
                0.5021,
                0.5088,
                0.5156,
                0.5224,
                0.5291,
                0.5359,
                0.5427,
                0.5494,
                0.5562,
                0.563,
                0.5697,
                0.5765,
                0.5833,
                0.5901,
                0.5968,
                0.6036,
                0.6104,
                0.6171,
                0.6239,
                0.6307,
                0.6374,
                0.6442,
                0.651,
                0.6577,
                0.6645,
                0.6713,
                0.678,
                0.6848,
                0.6916,
                0.6983,
                0.7051,
                0.7119,
                0.7186,
                0.7254,
                0.7322,
                0.7389,
                0.7457,
                0.7525,
                0.7592,
                0.766,
                0.7728,
                0.7795,
                0.7863,
                0.7931,
                0.7998,
                0.8066,
                0.81
                ]
    interf_ljets_ge4j_3t_top25_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_top25_ttH_node)
    
    interf_ljets_ge4j_3t_top25_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_top25_node_ttmb",
                                            label          = "ljets_ge4j_3t_top25_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top25==1))")
    interf_ljets_ge4j_3t_top25_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top25==1))","ljets_ge4j_3t_top25_ttmb_node","")
    interf_ljets_ge4j_3t_top25_ttmb_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_top25_ttmb_node.bin_edges = [ 
                0.1376,
                0.1424,
                0.1471,
                0.1519,
                0.1566,
                0.1614,
                0.1661,
                0.1709,
                0.1756,
                0.1804,
                0.1851,
                0.1898,
                0.1946,
                0.1993,
                0.2041,
                0.2088,
                0.2136,
                0.2183,
                0.2231,
                0.2278,
                0.2326,
                0.2373,
                0.2421,
                0.2468,
                0.2516,
                0.2563,
                0.2611,
                0.2658,
                0.2706,
                0.2753,
                0.2801,
                0.2848,
                0.2895,
                0.2943,
                0.299,
                0.3038,
                0.3085,
                0.3133,
                0.318,
                0.3228,
                0.3275,
                0.3323,
                0.337,
                0.3418,
                0.3465,
                0.3513,
                0.356,
                0.3608,
                0.3655,
                0.3703,
                0.375,
                0.3797,
                0.3845,
                0.3892,
                0.394,
                0.3987,
                0.4035,
                0.4082,
                0.413,
                0.4177,
                0.4225,
                0.4272,
                0.432,
                0.4367,
                0.4415,
                0.4462,
                0.451,
                0.4557,
                0.4605,
                0.4652,
                0.4699,
                0.4747,
                0.4794,
                0.4842,
                0.4889,
                0.4937,
                0.4984,
                0.5032,
                0.5079,
                0.5127,
                0.5174,
                0.5222,
                0.5269,
                0.5317,
                0.5364,
                0.5412,
                0.5459,
                0.5507,
                0.5554,
                0.5602,
                0.5649,
                0.5696,
                0.5744,
                0.5791,
                0.5839,
                0.5886,
                0.5934,
                0.5981,
                0.6029,
                0.6076,
                0.61
                ]
    interf_ljets_ge4j_3t_top25_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_top25_ttmb_node)
    
    interf_ljets_ge4j_3t_top25_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_top25_node_tt2b",
                                            label          = "ljets_ge4j_3t_top25_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top25==2))")
    interf_ljets_ge4j_3t_top25_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top25==2))","ljets_ge4j_3t_top25_tt2b_node","")
    interf_ljets_ge4j_3t_top25_tt2b_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_top25_tt2b_node.bin_edges = [ 
                0.1365,
                0.1435,
                0.1506,
                0.1577,
                0.1647,
                0.1718,
                0.1789,
                0.186,
                0.193,
                0.2001,
                0.2072,
                0.2142,
                0.2213,
                0.2284,
                0.2355,
                0.2425,
                0.2496,
                0.2567,
                0.2637,
                0.2708,
                0.2779,
                0.2849,
                0.292,
                0.2991,
                0.3062,
                0.3132,
                0.3203,
                0.3274,
                0.3344,
                0.3415,
                0.3486,
                0.3557,
                0.3627,
                0.3698,
                0.3769,
                0.3839,
                0.391,
                0.3981,
                0.4052,
                0.4122,
                0.4193,
                0.4264,
                0.4334,
                0.4405,
                0.4476,
                0.4546,
                0.4617,
                0.4688,
                0.4759,
                0.4829,
                0.49,
                0.4971,
                0.5041,
                0.5112,
                0.5183,
                0.5254,
                0.5324,
                0.5395,
                0.5466,
                0.5536,
                0.5607,
                0.5678,
                0.5748,
                0.5819,
                0.589,
                0.5961,
                0.6031,
                0.6102,
                0.6173,
                0.6243,
                0.6314,
                0.6385,
                0.6456,
                0.6526,
                0.6597,
                0.6668,
                0.6738,
                0.6809,
                0.688,
                0.6951,
                0.7021,
                0.7092,
                0.7163,
                0.7233,
                0.7304,
                0.7375,
                0.7445,
                0.7516,
                0.7587,
                0.7658,
                0.7728,
                0.7799,
                0.787,
                0.794,
                0.8011,
                0.8082,
                0.8153,
                0.8223,
                0.8294,
                0.8365,
                0.84
                ]
    interf_ljets_ge4j_3t_top25_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_top25_tt2b_node)
    
    interf_ljets_ge4j_3t_top25_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_top25_node_ttcc",
                                            label          = "ljets_ge4j_3t_top25_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top25==3))")
    interf_ljets_ge4j_3t_top25_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top25==3))","ljets_ge4j_3t_top25_ttcc_node","")
    interf_ljets_ge4j_3t_top25_ttcc_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_top25_ttcc_node.bin_edges = [ 
                0.1382,
                0.1418,
                0.1453,
                0.1488,
                0.1524,
                0.1559,
                0.1594,
                0.163,
                0.1665,
                0.1701,
                0.1736,
                0.1771,
                0.1807,
                0.1842,
                0.1877,
                0.1913,
                0.1948,
                0.1983,
                0.2019,
                0.2054,
                0.2089,
                0.2125,
                0.216,
                0.2195,
                0.2231,
                0.2266,
                0.2302,
                0.2337,
                0.2372,
                0.2408,
                0.2443,
                0.2478,
                0.2514,
                0.2549,
                0.2584,
                0.262,
                0.2655,
                0.269,
                0.2726,
                0.2761,
                0.2796,
                0.2832,
                0.2867,
                0.2903,
                0.2938,
                0.2973,
                0.3009,
                0.3044,
                0.3079,
                0.3115,
                0.315,
                0.3185,
                0.3221,
                0.3256,
                0.3291,
                0.3327,
                0.3362,
                0.3397,
                0.3433,
                0.3468,
                0.3504,
                0.3539,
                0.3574,
                0.361,
                0.3645,
                0.368,
                0.3716,
                0.3751,
                0.3786,
                0.3822,
                0.3857,
                0.3892,
                0.3928,
                0.3963,
                0.3998,
                0.4034,
                0.4069,
                0.4105,
                0.414,
                0.4175,
                0.4211,
                0.4246,
                0.4281,
                0.4317,
                0.4352,
                0.4387,
                0.4423,
                0.4458,
                0.4493,
                0.4529,
                0.4564,
                0.4599,
                0.4635,
                0.467,
                0.4706,
                0.4741,
                0.4776,
                0.4812,
                0.4847,
                0.4882,
                0.49
                ]
    interf_ljets_ge4j_3t_top25_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_top25_ttcc_node)
    
    interf_ljets_ge4j_3t_top25_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_top25_node_ttlf",
                                            label          = "ljets_ge4j_3t_top25_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top25==4))")
    interf_ljets_ge4j_3t_top25_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top25==4))","ljets_ge4j_3t_top25_ttlf_node","")
    interf_ljets_ge4j_3t_top25_ttlf_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_top25_ttlf_node.bin_edges = [ 
                0.1364,
                0.1436,
                0.1509,
                0.1582,
                0.1655,
                0.1727,
                0.18,
                0.1873,
                0.1945,
                0.2018,
                0.2091,
                0.2164,
                0.2236,
                0.2309,
                0.2382,
                0.2455,
                0.2527,
                0.26,
                0.2673,
                0.2745,
                0.2818,
                0.2891,
                0.2964,
                0.3036,
                0.3109,
                0.3182,
                0.3255,
                0.3327,
                0.34,
                0.3473,
                0.3545,
                0.3618,
                0.3691,
                0.3764,
                0.3836,
                0.3909,
                0.3982,
                0.4055,
                0.4127,
                0.42,
                0.4273,
                0.4345,
                0.4418,
                0.4491,
                0.4564,
                0.4636,
                0.4709,
                0.4782,
                0.4855,
                0.4927,
                0.5,
                0.5073,
                0.5145,
                0.5218,
                0.5291,
                0.5364,
                0.5436,
                0.5509,
                0.5582,
                0.5655,
                0.5727,
                0.58,
                0.5873,
                0.5945,
                0.6018,
                0.6091,
                0.6164,
                0.6236,
                0.6309,
                0.6382,
                0.6455,
                0.6527,
                0.66,
                0.6673,
                0.6745,
                0.6818,
                0.6891,
                0.6964,
                0.7036,
                0.7109,
                0.7182,
                0.7255,
                0.7327,
                0.74,
                0.7473,
                0.7545,
                0.7618,
                0.7691,
                0.7764,
                0.7836,
                0.7909,
                0.7982,
                0.8055,
                0.8127,
                0.82,
                0.8273,
                0.8345,
                0.8418,
                0.8491,
                0.8564,
                0.86
                ]
    interf_ljets_ge4j_3t_top25_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_top25_ttlf_node)
    
    interf_ljets_ge4j_3t_top25_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_top25_node_tHq",
                                            label          = "ljets_ge4j_3t_top25_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top25==5))")
    interf_ljets_ge4j_3t_top25_tHq_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top25==5))","ljets_ge4j_3t_top25_tHq_node","")
    interf_ljets_ge4j_3t_top25_tHq_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_top25_tHq_node.bin_edges = [ 
                0.1358,
                0.1442,
                0.1527,
                0.1612,
                0.1697,
                0.1782,
                0.1867,
                0.1952,
                0.2036,
                0.2121,
                0.2206,
                0.2291,
                0.2376,
                0.2461,
                0.2545,
                0.263,
                0.2715,
                0.28,
                0.2885,
                0.297,
                0.3055,
                0.3139,
                0.3224,
                0.3309,
                0.3394,
                0.3479,
                0.3564,
                0.3648,
                0.3733,
                0.3818,
                0.3903,
                0.3988,
                0.4073,
                0.4158,
                0.4242,
                0.4327,
                0.4412,
                0.4497,
                0.4582,
                0.4667,
                0.4752,
                0.4836,
                0.4921,
                0.5006,
                0.5091,
                0.5176,
                0.5261,
                0.5345,
                0.543,
                0.5515,
                0.56,
                0.5685,
                0.577,
                0.5855,
                0.5939,
                0.6024,
                0.6109,
                0.6194,
                0.6279,
                0.6364,
                0.6448,
                0.6533,
                0.6618,
                0.6703,
                0.6788,
                0.6873,
                0.6958,
                0.7042,
                0.7127,
                0.7212,
                0.7297,
                0.7382,
                0.7467,
                0.7552,
                0.7636,
                0.7721,
                0.7806,
                0.7891,
                0.7976,
                0.8061,
                0.8145,
                0.823,
                0.8315,
                0.84,
                0.8485,
                0.857,
                0.8655,
                0.8739,
                0.8824,
                0.8909,
                0.8994,
                0.9079,
                0.9164,
                0.9248,
                0.9333,
                0.9418,
                0.9503,
                0.9588,
                0.9673,
                0.9758,
                0.98
                ]
    interf_ljets_ge4j_3t_top25_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_top25_tHq_node)
    
    interf_ljets_ge4j_3t_top25_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_top25_node_tHW",
                                            label          = "ljets_ge4j_3t_top25_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top25==6))")
    interf_ljets_ge4j_3t_top25_tHW_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top25==6))","ljets_ge4j_3t_top25_tHW_node","")
    interf_ljets_ge4j_3t_top25_tHW_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_top25_tHW_node.bin_edges = [ 
                0.1357,
                0.1443,
                0.153,
                0.1617,
                0.1704,
                0.1791,
                0.1878,
                0.1965,
                0.2052,
                0.2138,
                0.2225,
                0.2312,
                0.2399,
                0.2486,
                0.2573,
                0.266,
                0.2746,
                0.2833,
                0.292,
                0.3007,
                0.3094,
                0.3181,
                0.3268,
                0.3355,
                0.3441,
                0.3528,
                0.3615,
                0.3702,
                0.3789,
                0.3876,
                0.3963,
                0.4049,
                0.4136,
                0.4223,
                0.431,
                0.4397,
                0.4484,
                0.4571,
                0.4658,
                0.4744,
                0.4831,
                0.4918,
                0.5005,
                0.5092,
                0.5179,
                0.5266,
                0.5353,
                0.5439,
                0.5526,
                0.5613,
                0.57,
                0.5787,
                0.5874,
                0.5961,
                0.6047,
                0.6134,
                0.6221,
                0.6308,
                0.6395,
                0.6482,
                0.6569,
                0.6656,
                0.6742,
                0.6829,
                0.6916,
                0.7003,
                0.709,
                0.7177,
                0.7264,
                0.7351,
                0.7437,
                0.7524,
                0.7611,
                0.7698,
                0.7785,
                0.7872,
                0.7959,
                0.8045,
                0.8132,
                0.8219,
                0.8306,
                0.8393,
                0.848,
                0.8567,
                0.8654,
                0.874,
                0.8827,
                0.8914,
                0.9001,
                0.9088,
                0.9175,
                0.9262,
                0.9348,
                0.9435,
                0.9522,
                0.9609,
                0.9696,
                0.9783,
                0.987,
                0.9957,
                1.0
                ]
    interf_ljets_ge4j_3t_top25_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_top25_tHW_node)
    


    # plots for ge4j_3t_top30

    interf_ljets_ge4j_3t_top30_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_top30_node_ttH",
                                            label          = "ljets_ge4j_3t_top30_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top30==0))")
    interf_ljets_ge4j_3t_top30_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top30==0))","ljets_ge4j_3t_top30_ttH_node","")
    interf_ljets_ge4j_3t_top30_ttH_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_top30_ttH_node.bin_edges = [ 
                0.1365,
                0.1435,
                0.1505,
                0.1574,
                0.1644,
                0.1714,
                0.1783,
                0.1853,
                0.1923,
                0.1992,
                0.2062,
                0.2132,
                0.2202,
                0.2271,
                0.2341,
                0.2411,
                0.248,
                0.255,
                0.262,
                0.2689,
                0.2759,
                0.2829,
                0.2898,
                0.2968,
                0.3038,
                0.3108,
                0.3177,
                0.3247,
                0.3317,
                0.3386,
                0.3456,
                0.3526,
                0.3595,
                0.3665,
                0.3735,
                0.3805,
                0.3874,
                0.3944,
                0.4014,
                0.4083,
                0.4153,
                0.4223,
                0.4292,
                0.4362,
                0.4432,
                0.4502,
                0.4571,
                0.4641,
                0.4711,
                0.478,
                0.485,
                0.492,
                0.4989,
                0.5059,
                0.5129,
                0.5198,
                0.5268,
                0.5338,
                0.5408,
                0.5477,
                0.5547,
                0.5617,
                0.5686,
                0.5756,
                0.5826,
                0.5895,
                0.5965,
                0.6035,
                0.6105,
                0.6174,
                0.6244,
                0.6314,
                0.6383,
                0.6453,
                0.6523,
                0.6592,
                0.6662,
                0.6732,
                0.6802,
                0.6871,
                0.6941,
                0.7011,
                0.708,
                0.715,
                0.722,
                0.7289,
                0.7359,
                0.7429,
                0.7498,
                0.7568,
                0.7638,
                0.7708,
                0.7777,
                0.7847,
                0.7917,
                0.7986,
                0.8056,
                0.8126,
                0.8195,
                0.8265,
                0.83
                ]
    interf_ljets_ge4j_3t_top30_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_top30_ttH_node)
    
    interf_ljets_ge4j_3t_top30_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_top30_node_ttmb",
                                            label          = "ljets_ge4j_3t_top30_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top30==1))")
    interf_ljets_ge4j_3t_top30_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top30==1))","ljets_ge4j_3t_top30_ttmb_node","")
    interf_ljets_ge4j_3t_top30_ttmb_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_top30_ttmb_node.bin_edges = [ 
                0.1376,
                0.1424,
                0.1471,
                0.1519,
                0.1566,
                0.1614,
                0.1661,
                0.1709,
                0.1756,
                0.1804,
                0.1851,
                0.1898,
                0.1946,
                0.1993,
                0.2041,
                0.2088,
                0.2136,
                0.2183,
                0.2231,
                0.2278,
                0.2326,
                0.2373,
                0.2421,
                0.2468,
                0.2516,
                0.2563,
                0.2611,
                0.2658,
                0.2706,
                0.2753,
                0.2801,
                0.2848,
                0.2895,
                0.2943,
                0.299,
                0.3038,
                0.3085,
                0.3133,
                0.318,
                0.3228,
                0.3275,
                0.3323,
                0.337,
                0.3418,
                0.3465,
                0.3513,
                0.356,
                0.3608,
                0.3655,
                0.3703,
                0.375,
                0.3797,
                0.3845,
                0.3892,
                0.394,
                0.3987,
                0.4035,
                0.4082,
                0.413,
                0.4177,
                0.4225,
                0.4272,
                0.432,
                0.4367,
                0.4415,
                0.4462,
                0.451,
                0.4557,
                0.4605,
                0.4652,
                0.4699,
                0.4747,
                0.4794,
                0.4842,
                0.4889,
                0.4937,
                0.4984,
                0.5032,
                0.5079,
                0.5127,
                0.5174,
                0.5222,
                0.5269,
                0.5317,
                0.5364,
                0.5412,
                0.5459,
                0.5507,
                0.5554,
                0.5602,
                0.5649,
                0.5696,
                0.5744,
                0.5791,
                0.5839,
                0.5886,
                0.5934,
                0.5981,
                0.6029,
                0.6076,
                0.61
                ]
    interf_ljets_ge4j_3t_top30_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_top30_ttmb_node)
    
    interf_ljets_ge4j_3t_top30_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_top30_node_tt2b",
                                            label          = "ljets_ge4j_3t_top30_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top30==2))")
    interf_ljets_ge4j_3t_top30_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top30==2))","ljets_ge4j_3t_top30_tt2b_node","")
    interf_ljets_ge4j_3t_top30_tt2b_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_top30_tt2b_node.bin_edges = [ 
                0.1364,
                0.1436,
                0.1508,
                0.1579,
                0.1651,
                0.1723,
                0.1794,
                0.1866,
                0.1938,
                0.201,
                0.2081,
                0.2153,
                0.2225,
                0.2296,
                0.2368,
                0.244,
                0.2512,
                0.2583,
                0.2655,
                0.2727,
                0.2798,
                0.287,
                0.2942,
                0.3014,
                0.3085,
                0.3157,
                0.3229,
                0.3301,
                0.3372,
                0.3444,
                0.3516,
                0.3587,
                0.3659,
                0.3731,
                0.3803,
                0.3874,
                0.3946,
                0.4018,
                0.4089,
                0.4161,
                0.4233,
                0.4305,
                0.4376,
                0.4448,
                0.452,
                0.4591,
                0.4663,
                0.4735,
                0.4807,
                0.4878,
                0.495,
                0.5022,
                0.5093,
                0.5165,
                0.5237,
                0.5309,
                0.538,
                0.5452,
                0.5524,
                0.5595,
                0.5667,
                0.5739,
                0.5811,
                0.5882,
                0.5954,
                0.6026,
                0.6097,
                0.6169,
                0.6241,
                0.6313,
                0.6384,
                0.6456,
                0.6528,
                0.6599,
                0.6671,
                0.6743,
                0.6815,
                0.6886,
                0.6958,
                0.703,
                0.7102,
                0.7173,
                0.7245,
                0.7317,
                0.7388,
                0.746,
                0.7532,
                0.7604,
                0.7675,
                0.7747,
                0.7819,
                0.789,
                0.7962,
                0.8034,
                0.8106,
                0.8177,
                0.8249,
                0.8321,
                0.8392,
                0.8464,
                0.85
                ]
    interf_ljets_ge4j_3t_top30_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_top30_tt2b_node)
    
    interf_ljets_ge4j_3t_top30_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_top30_node_ttcc",
                                            label          = "ljets_ge4j_3t_top30_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top30==3))")
    interf_ljets_ge4j_3t_top30_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top30==3))","ljets_ge4j_3t_top30_ttcc_node","")
    interf_ljets_ge4j_3t_top30_ttcc_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_top30_ttcc_node.bin_edges = [ 
                0.1382,
                0.1418,
                0.1455,
                0.1491,
                0.1527,
                0.1564,
                0.16,
                0.1636,
                0.1673,
                0.1709,
                0.1745,
                0.1782,
                0.1818,
                0.1855,
                0.1891,
                0.1927,
                0.1964,
                0.2,
                0.2036,
                0.2073,
                0.2109,
                0.2145,
                0.2182,
                0.2218,
                0.2255,
                0.2291,
                0.2327,
                0.2364,
                0.24,
                0.2436,
                0.2473,
                0.2509,
                0.2545,
                0.2582,
                0.2618,
                0.2655,
                0.2691,
                0.2727,
                0.2764,
                0.28,
                0.2836,
                0.2873,
                0.2909,
                0.2945,
                0.2982,
                0.3018,
                0.3055,
                0.3091,
                0.3127,
                0.3164,
                0.32,
                0.3236,
                0.3273,
                0.3309,
                0.3345,
                0.3382,
                0.3418,
                0.3455,
                0.3491,
                0.3527,
                0.3564,
                0.36,
                0.3636,
                0.3673,
                0.3709,
                0.3745,
                0.3782,
                0.3818,
                0.3855,
                0.3891,
                0.3927,
                0.3964,
                0.4,
                0.4036,
                0.4073,
                0.4109,
                0.4145,
                0.4182,
                0.4218,
                0.4255,
                0.4291,
                0.4327,
                0.4364,
                0.44,
                0.4436,
                0.4473,
                0.4509,
                0.4545,
                0.4582,
                0.4618,
                0.4655,
                0.4691,
                0.4727,
                0.4764,
                0.48,
                0.4836,
                0.4873,
                0.4909,
                0.4945,
                0.4982,
                0.5
                ]
    interf_ljets_ge4j_3t_top30_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_top30_ttcc_node)
    
    interf_ljets_ge4j_3t_top30_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_top30_node_ttlf",
                                            label          = "ljets_ge4j_3t_top30_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top30==4))")
    interf_ljets_ge4j_3t_top30_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top30==4))","ljets_ge4j_3t_top30_ttlf_node","")
    interf_ljets_ge4j_3t_top30_ttlf_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_top30_ttlf_node.bin_edges = [ 
                0.1364,
                0.1436,
                0.1508,
                0.1579,
                0.1651,
                0.1723,
                0.1794,
                0.1866,
                0.1938,
                0.201,
                0.2081,
                0.2153,
                0.2225,
                0.2296,
                0.2368,
                0.244,
                0.2512,
                0.2583,
                0.2655,
                0.2727,
                0.2798,
                0.287,
                0.2942,
                0.3014,
                0.3085,
                0.3157,
                0.3229,
                0.3301,
                0.3372,
                0.3444,
                0.3516,
                0.3587,
                0.3659,
                0.3731,
                0.3803,
                0.3874,
                0.3946,
                0.4018,
                0.4089,
                0.4161,
                0.4233,
                0.4305,
                0.4376,
                0.4448,
                0.452,
                0.4591,
                0.4663,
                0.4735,
                0.4807,
                0.4878,
                0.495,
                0.5022,
                0.5093,
                0.5165,
                0.5237,
                0.5309,
                0.538,
                0.5452,
                0.5524,
                0.5595,
                0.5667,
                0.5739,
                0.5811,
                0.5882,
                0.5954,
                0.6026,
                0.6097,
                0.6169,
                0.6241,
                0.6313,
                0.6384,
                0.6456,
                0.6528,
                0.6599,
                0.6671,
                0.6743,
                0.6815,
                0.6886,
                0.6958,
                0.703,
                0.7102,
                0.7173,
                0.7245,
                0.7317,
                0.7388,
                0.746,
                0.7532,
                0.7604,
                0.7675,
                0.7747,
                0.7819,
                0.789,
                0.7962,
                0.8034,
                0.8106,
                0.8177,
                0.8249,
                0.8321,
                0.8392,
                0.8464,
                0.85
                ]
    interf_ljets_ge4j_3t_top30_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_top30_ttlf_node)
    
    interf_ljets_ge4j_3t_top30_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_top30_node_tHq",
                                            label          = "ljets_ge4j_3t_top30_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top30==5))")
    interf_ljets_ge4j_3t_top30_tHq_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top30==5))","ljets_ge4j_3t_top30_tHq_node","")
    interf_ljets_ge4j_3t_top30_tHq_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_top30_tHq_node.bin_edges = [ 
                0.1357,
                0.1443,
                0.1529,
                0.1615,
                0.1701,
                0.1786,
                0.1872,
                0.1958,
                0.2044,
                0.213,
                0.2216,
                0.2302,
                0.2387,
                0.2473,
                0.2559,
                0.2645,
                0.2731,
                0.2817,
                0.2903,
                0.2988,
                0.3074,
                0.316,
                0.3246,
                0.3332,
                0.3418,
                0.3504,
                0.3589,
                0.3675,
                0.3761,
                0.3847,
                0.3933,
                0.4019,
                0.4105,
                0.419,
                0.4276,
                0.4362,
                0.4448,
                0.4534,
                0.462,
                0.4706,
                0.4791,
                0.4877,
                0.4963,
                0.5049,
                0.5135,
                0.5221,
                0.5307,
                0.5392,
                0.5478,
                0.5564,
                0.565,
                0.5736,
                0.5822,
                0.5908,
                0.5993,
                0.6079,
                0.6165,
                0.6251,
                0.6337,
                0.6423,
                0.6509,
                0.6594,
                0.668,
                0.6766,
                0.6852,
                0.6938,
                0.7024,
                0.711,
                0.7195,
                0.7281,
                0.7367,
                0.7453,
                0.7539,
                0.7625,
                0.7711,
                0.7796,
                0.7882,
                0.7968,
                0.8054,
                0.814,
                0.8226,
                0.8312,
                0.8397,
                0.8483,
                0.8569,
                0.8655,
                0.8741,
                0.8827,
                0.8913,
                0.8998,
                0.9084,
                0.917,
                0.9256,
                0.9342,
                0.9428,
                0.9514,
                0.9599,
                0.9685,
                0.9771,
                0.9857,
                0.99
                ]
    interf_ljets_ge4j_3t_top30_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_top30_tHq_node)
    
    interf_ljets_ge4j_3t_top30_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_top30_node_tHW",
                                            label          = "ljets_ge4j_3t_top30_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top30==6))")
    interf_ljets_ge4j_3t_top30_tHW_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_top30==6))","ljets_ge4j_3t_top30_tHW_node","")
    interf_ljets_ge4j_3t_top30_tHW_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_top30_tHW_node.bin_edges = [ 
                0.1357,
                0.1443,
                0.153,
                0.1617,
                0.1704,
                0.1791,
                0.1878,
                0.1965,
                0.2052,
                0.2138,
                0.2225,
                0.2312,
                0.2399,
                0.2486,
                0.2573,
                0.266,
                0.2746,
                0.2833,
                0.292,
                0.3007,
                0.3094,
                0.3181,
                0.3268,
                0.3355,
                0.3441,
                0.3528,
                0.3615,
                0.3702,
                0.3789,
                0.3876,
                0.3963,
                0.4049,
                0.4136,
                0.4223,
                0.431,
                0.4397,
                0.4484,
                0.4571,
                0.4658,
                0.4744,
                0.4831,
                0.4918,
                0.5005,
                0.5092,
                0.5179,
                0.5266,
                0.5353,
                0.5439,
                0.5526,
                0.5613,
                0.57,
                0.5787,
                0.5874,
                0.5961,
                0.6047,
                0.6134,
                0.6221,
                0.6308,
                0.6395,
                0.6482,
                0.6569,
                0.6656,
                0.6742,
                0.6829,
                0.6916,
                0.7003,
                0.709,
                0.7177,
                0.7264,
                0.7351,
                0.7437,
                0.7524,
                0.7611,
                0.7698,
                0.7785,
                0.7872,
                0.7959,
                0.8045,
                0.8132,
                0.8219,
                0.8306,
                0.8393,
                0.848,
                0.8567,
                0.8654,
                0.874,
                0.8827,
                0.8914,
                0.9001,
                0.9088,
                0.9175,
                0.9262,
                0.9348,
                0.9435,
                0.9522,
                0.9609,
                0.9696,
                0.9783,
                0.987,
                0.9957,
                1.0
                ]
    interf_ljets_ge4j_3t_top30_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_top30_tHW_node)
    

    for interf in interfaces:
        l = interf.label
        interf.histoname = discrname+"_"+l if not discrname == "" else l 
        interf.histotitle = "final discriminator ({})".format(l)
        interf.selection = interf.category[0]

    DNNPlots = init_plots(interfaces = interfaces, data = data)
    return DNNPlots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_ge4j_ge4t_top20(data)
    # discriminatorPlots += plots_ge4j_ge4t_top25(data)
    # discriminatorPlots += plots_ge4j_ge4t_top30(data)
    # discriminatorPlots += plots_ge4j_3t_top20(data)
    discriminatorPlots += plots_ge4j_3t_top25(data)
    # discriminatorPlots += plots_ge4j_3t_top30(data)
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

            hname_2D = "{}_vs_{}".format(interf.histoname, interf2.histoname)
            htitle_2D = "{}_vs_{}".format(interf.histotitle, interf2.histotitle)
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
    