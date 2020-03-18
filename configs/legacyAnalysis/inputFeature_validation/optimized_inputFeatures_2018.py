
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



def plots_ljets_ge4j_3t(data = None):
    label = "\geq 4 jets, 3 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM==3)&&(1.)"
    
    # for combination
    interf_ljets_ge4j_3t_Evt_HT_jets = vhi.variableHistoInterface(variable_name  = "Evt_HT_jets",
                                            category_label = label,
                                            label          = "ljets_ge4j_3t_Evt_HT_jets")
    interf_ljets_ge4j_3t_Evt_HT_jets.category = (selection,"ljets_ge4j_3t_Evt_HT_jets","")

    interf_ljets_ge4j_3t_Evt_HT_jets.nhistobins = 1
    interf_ljets_ge4j_3t_Evt_HT_jets.bin_edges = [200.0,226.0,252.0,278.0,304.0,330.0,356.0,382.0,408.0,434.0,460.0,486.0,512.0,538.0,564.0,590.0,616.0,642.0,668.0,694.0,720.0,746.0,772.0,798.0,824.0,850.0,876.0,902.0,928.0,954.0,980.0,1006.0,1032.0,1058.0,1084.0,1110.0,1136.0,1162.0,1188.0,1214.0,1240.0,1266.0,1292.0,1318.0,1344.0,1370.0,1396.0,1422.0,1448.0,1474.0,1500.0]
    interf_ljets_ge4j_3t_Evt_HT_jets.histoname = "ljets_ge4j_3t_Evt_HT_jets"
    interf_ljets_ge4j_3t_Evt_HT_jets.histotitle = "H_{T}(jets)"
    interf_ljets_ge4j_3t_Evt_HT_jets.selection = interf_ljets_ge4j_3t_Evt_HT_jets.category[0]

    interfaces.append(interf_ljets_ge4j_3t_Evt_HT_jets)
 
 
    # top variables
    interf_ljets_ge4j_3t_CSV_1 = vhi.variableHistoInterface(variable_name  = "CSV[1]",
                                            label          = "ljets_ge4j_3t_CSV_1",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_CSV_1.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_CSV_1","")
    interf_ljets_ge4j_3t_CSV_1.bin_edges = [ 
                0.277,
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
    interf_ljets_ge4j_3t_CSV_1.histotitle = "CSV[1]"
    interf_ljets_ge4j_3t_CSV_1.histoname = "ljets_ge4j_3t_CSV_1"
    interf_ljets_ge4j_3t_CSV_1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_CSV_1)
    
    interf_ljets_ge4j_3t_CSV_2 = vhi.variableHistoInterface(variable_name  = "CSV[2]",
                                            label          = "ljets_ge4j_3t_CSV_2",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_CSV_2.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_CSV_2","")
    interf_ljets_ge4j_3t_CSV_2.bin_edges = [ 
                0.277,
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
    interf_ljets_ge4j_3t_CSV_2.histotitle = "CSV[2]"
    interf_ljets_ge4j_3t_CSV_2.histoname = "ljets_ge4j_3t_CSV_2"
    interf_ljets_ge4j_3t_CSV_2.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_CSV_2)
    
    interf_ljets_ge4j_3t_CSV_3 = vhi.variableHistoInterface(variable_name  = "CSV[3]",
                                            label          = "ljets_ge4j_3t_CSV_3",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_CSV_3.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_CSV_3","")
    interf_ljets_ge4j_3t_CSV_3.minxval = 0
    interf_ljets_ge4j_3t_CSV_3.maxxval = 0.277

    interf_ljets_ge4j_3t_CSV_3.histotitle = "CSV[3]"
    interf_ljets_ge4j_3t_CSV_3.histoname = "ljets_ge4j_3t_CSV_3"
    interf_ljets_ge4j_3t_CSV_3.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_CSV_3)
    
    interf_ljets_ge4j_3t_Evt_CSV_avg = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg",
                                            label          = "ljets_ge4j_3t_Evt_CSV_avg",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_CSV_avg.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_CSV_avg","")
    interf_ljets_ge4j_3t_Evt_CSV_avg.bin_edges = [ 
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
                # 1.0
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
                0.3,
                0.314,
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
                0.0,
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
                0.277,
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
                0.0,
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
    
    interf_ljets_ge4j_3t_Evt_JetPt_over_JetE = vhi.variableHistoInterface(variable_name  = "Evt_JetPt_over_JetE",
                                            label          = "ljets_ge4j_3t_Evt_JetPt_over_JetE",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_JetPt_over_JetE.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_JetPt_over_JetE","")
    interf_ljets_ge4j_3t_Evt_JetPt_over_JetE.bin_edges = [ 
                # 0.0,
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
    
    interf_ljets_ge4j_3t_Evt_M2_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_M2_TaggedJetsAverage",
                                            label          = "ljets_ge4j_3t_Evt_M2_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_M2_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_M2_TaggedJetsAverage","")
    interf_ljets_ge4j_3t_Evt_M2_TaggedJetsAverage.bin_edges = [ 
                40.0,
                69.2,
                98.4,
                127.6,
                156.8,
                186.0,
                215.2,
                244.4,
                273.6,
                302.8,
                332.0,
                361.2,
                390.4,
                419.6,
                448.8,
                478.0,
                507.2,
                536.4,
                565.6,
                594.8,
                624.0,
                653.2,
                682.4,
                711.6,
                740.8,
                770.0,
                799.2,
                828.4,
                857.6,
                886.8,
                945.2,
                1003.6,
                1062.0,
                1149.6,
                1208.0,
                1500.0
                ]
    interf_ljets_ge4j_3t_Evt_M2_TaggedJetsAverage.histotitle = "Evt_M2_TaggedJetsAverage"
    interf_ljets_ge4j_3t_Evt_M2_TaggedJetsAverage.histoname = "ljets_ge4j_3t_Evt_M2_TaggedJetsAverage"
    interf_ljets_ge4j_3t_Evt_M2_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_M2_TaggedJetsAverage)
    
    interf_ljets_ge4j_3t_Evt_M_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_M_TaggedJetsAverage",
                                            label          = "ljets_ge4j_3t_Evt_M_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_M_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_M_TaggedJetsAverage","")
    interf_ljets_ge4j_3t_Evt_M_TaggedJetsAverage.bin_edges = [ 
                4.5,
                6.41,
                8.32,
                10.23,
                12.14,
                14.05,
                15.96,
                17.87,
                19.78,
                21.69,
                23.6,
                25.51,
                27.42,
                29.33,
                31.24,
                33.15,
                35.06,
                36.97,
                38.88,
                40.79,
                42.7,
                44.61,
                46.52,
                48.43,
                50.34,
                52.25,
                56.07,
                63.71,
                71.35,
                100.0
                ]
    interf_ljets_ge4j_3t_Evt_M_TaggedJetsAverage.histotitle = "Evt_M_TaggedJetsAverage"
    interf_ljets_ge4j_3t_Evt_M_TaggedJetsAverage.histoname = "ljets_ge4j_3t_Evt_M_TaggedJetsAverage"
    interf_ljets_ge4j_3t_Evt_M_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_M_TaggedJetsAverage)
    
    interf_ljets_ge4j_3t_Evt_Pt_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Pt_JetsAverage",
                                            label          = "ljets_ge4j_3t_Evt_Pt_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_Pt_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_Pt_JetsAverage","")
    interf_ljets_ge4j_3t_Evt_Pt_JetsAverage.bin_edges = [ 
                30.0,
                45.4,
                60.8,
                76.2,
                91.6,
                107.0,
                122.4,
                137.8,
                153.2,
                168.6,
                184.0,
                199.4,
                214.8,
                230.2,
                245.6,
                261.0,
                276.4,
                291.8,
                307.2,
                322.6,
                338.0,
                353.4,
                368.8,
                399.6,
                430.4,
                476.6,
                # 800.0
                ]
    interf_ljets_ge4j_3t_Evt_Pt_JetsAverage.histotitle = "Evt_Pt_JetsAverage"
    interf_ljets_ge4j_3t_Evt_Pt_JetsAverage.histoname = "ljets_ge4j_3t_Evt_Pt_JetsAverage"
    interf_ljets_ge4j_3t_Evt_Pt_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_Pt_JetsAverage)
    
    interf_ljets_ge4j_3t_Evt_Pt_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Pt_TaggedJetsAverage",
                                            label          = "ljets_ge4j_3t_Evt_Pt_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_Pt_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_Pt_TaggedJetsAverage","")
    interf_ljets_ge4j_3t_Evt_Pt_TaggedJetsAverage.bin_edges = [ 
                30.0,
                49.4,
                68.8,
                88.2,
                107.6,
                127.0,
                146.4,
                165.8,
                185.2,
                204.6,
                224.0,
                243.4,
                262.8,
                282.2,
                301.6,
                321.0,
                340.4,
                359.8,
                379.2,
                398.6,
                418.0,
                437.4,
                476.2,
                495.6,
                534.4,
                650.8,
                # 1000.0
                ]
    interf_ljets_ge4j_3t_Evt_Pt_TaggedJetsAverage.histotitle = "Evt_Pt_TaggedJetsAverage"
    interf_ljets_ge4j_3t_Evt_Pt_TaggedJetsAverage.histoname = "ljets_ge4j_3t_Evt_Pt_TaggedJetsAverage"
    interf_ljets_ge4j_3t_Evt_Pt_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_Pt_TaggedJetsAverage)
    
    interf_ljets_ge4j_3t_Evt_Pt_minDrTaggedJets = vhi.variableHistoInterface(variable_name  = "Evt_Pt_minDrTaggedJets",
                                            label          = "ljets_ge4j_3t_Evt_Pt_minDrTaggedJets",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_Pt_minDrTaggedJets.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_Pt_minDrTaggedJets","")
    interf_ljets_ge4j_3t_Evt_Pt_minDrTaggedJets.bin_edges = [ 
                20.0,
                49.6,
                79.2,
                108.8,
                138.4,
                168.0,
                197.6,
                227.2,
                256.8,
                286.4,
                316.0,
                345.6,
                375.2,
                404.8,
                434.4,
                464.0,
                493.6,
                523.2,
                552.8,
                582.4,
                612.0,
                641.6,
                671.2,
                700.8,
                730.4,
                760.0,
                819.2,
                848.8,
                937.6,
                1115.2,
                # 1500.0
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
                # 15.0
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
    
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_hdau2 = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_Jet_CSV_hdau2",
                                            label          = "ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_hdau2",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_hdau2.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_hdau2","")
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_hdau2.bin_edges = [ 
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
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_hdau2.histotitle = "Reco_JABDT_tHW_Jet_CSV_hdau2"
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_hdau2.histoname = "ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_hdau2"
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_hdau2.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_hdau2)
    
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_whaddau1 = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_Jet_CSV_whaddau1",
                                            label          = "ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_whaddau1",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_whaddau1.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_whaddau1","")
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_whaddau1.bin_edges = [ 
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
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_whaddau1.histotitle = "Reco_JABDT_tHW_Jet_CSV_whaddau1"
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_whaddau1.histoname = "ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_whaddau1"
    interf_ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_whaddau1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_whaddau1)
    
    interf_ljets_ge4j_3t_Reco_JABDT_tHq_Jet_CSV_btop = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHq_Jet_CSV_btop",
                                            label          = "ljets_ge4j_3t_Reco_JABDT_tHq_Jet_CSV_btop",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_JABDT_tHq_Jet_CSV_btop.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_JABDT_tHq_Jet_CSV_btop","")
    interf_ljets_ge4j_3t_Reco_JABDT_tHq_Jet_CSV_btop.bin_edges = [ 
                # -1.5,
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
    interf_ljets_ge4j_3t_Reco_JABDT_tHq_Jet_CSV_btop.histotitle = "Reco_JABDT_tHq_Jet_CSV_btop"
    interf_ljets_ge4j_3t_Reco_JABDT_tHq_Jet_CSV_btop.histoname = "ljets_ge4j_3t_Reco_JABDT_tHq_Jet_CSV_btop"
    interf_ljets_ge4j_3t_Reco_JABDT_tHq_Jet_CSV_btop.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_JABDT_tHq_Jet_CSV_btop)
    
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_hdau1 = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttH_Jet_CSV_hdau1",
                                            label          = "ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_hdau1",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_hdau1.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_hdau1","")
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_hdau1.bin_edges = [ 
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
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_hdau1.histotitle = "Reco_JABDT_ttH_Jet_CSV_hdau1"
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_hdau1.histoname = "ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_hdau1"
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_hdau1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_hdau1)
    
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_hdau2 = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttH_Jet_CSV_hdau2",
                                            label          = "ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_hdau2",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_hdau2.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_hdau2","")
    interf_ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_hdau2.bin_edges = [ 
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
                # 0.0,
                4.16,
                4.32,
                4.48,
                4.64,
                4.8,
                4.96,
                5.12,
                5.28,
                5.44,
                5.6,
                5.76,
                5.92,
                6.08,
                6.24,
                6.4,
                6.56,
                6.72,
                6.88,
                7.04,
                7.2,
                7.36,
                7.52,
                7.68,
                7.84,
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
                # 0.0,
                3.04,
                3.2,
                3.36,
                3.52,
                3.68,
                3.84,
                4.0,
                4.16,
                4.32,
                4.48,
                4.64,
                4.8,
                4.96,
                5.12,
                5.28,
                5.44,
                5.6,
                5.76,
                5.92,
                6.08,
                6.24,
                6.4,
                6.56,
                6.72,
                6.88,
                7.04,
                7.2,
                7.36,
                7.52,
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
                -1.0,
                -0.6,
                # -0.36,
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
    interf_ljets_ge4j_3t_Reco_tHW_bestJABDToutput.histotitle = "Reco_tHW_bestJABDToutput"
    interf_ljets_ge4j_3t_Reco_tHW_bestJABDToutput.histoname = "ljets_ge4j_3t_Reco_tHW_bestJABDToutput"
    interf_ljets_ge4j_3t_Reco_tHW_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_tHW_bestJABDToutput)
    
    interf_ljets_ge4j_3t_Reco_tHW_top_h_dr = vhi.variableHistoInterface(variable_name  = "Reco_tHW_top_h_dr",
                                            label          = "ljets_ge4j_3t_Reco_tHW_top_h_dr",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_tHW_top_h_dr.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_tHW_top_h_dr","")
    interf_ljets_ge4j_3t_Reco_tHW_top_h_dr.bin_edges = [ 
                -1.5,
                -0.12,
                0.11,
                0.34,
                0.57,
                0.8,
                1.03,
                1.26,
                1.49,
                1.72,
                1.95,
                2.18,
                2.41,
                2.64,
                2.87,
                3.1,
                3.33,
                3.56,
                3.79,
                4.02,
                4.25,
                4.48,
                4.71,
                4.94,
                5.17,
                5.4,
                5.63,
                5.86,
                6.09,
                6.32,
                6.55,
                6.78,
                7.24,
                10.0
                ]
    interf_ljets_ge4j_3t_Reco_tHW_top_h_dr.histotitle = "Reco_tHW_top_h_dr"
    interf_ljets_ge4j_3t_Reco_tHW_top_h_dr.histoname = "ljets_ge4j_3t_Reco_tHW_top_h_dr"
    interf_ljets_ge4j_3t_Reco_tHW_top_h_dr.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_tHW_top_h_dr)
    
    interf_ljets_ge4j_3t_Reco_tHW_wb_h_dr = vhi.variableHistoInterface(variable_name  = "Reco_tHW_wb_h_dr",
                                            label          = "ljets_ge4j_3t_Reco_tHW_wb_h_dr",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_tHW_wb_h_dr.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_tHW_wb_h_dr","")
    interf_ljets_ge4j_3t_Reco_tHW_wb_h_dr.bin_edges = [ 
                -1.5,
                -0.12,
                # 0.11,
                0.34,
                0.57,
                0.8,
                1.03,
                1.26,
                1.49,
                1.72,
                1.95,
                2.18,
                2.41,
                2.64,
                2.87,
                3.1,
                3.33,
                3.56,
                3.79,
                4.02,
                4.25,
                4.48,
                4.71,
                4.94,
                5.17,
                5.4,
                5.63,
                5.86,
                6.09,
                6.32,
                6.55,
                6.78,
                7.01,
                7.24,
                7.7,
                # 10.0
                ]
    interf_ljets_ge4j_3t_Reco_tHW_wb_h_dr.histotitle = "Reco_tHW_wb_h_dr"
    interf_ljets_ge4j_3t_Reco_tHW_wb_h_dr.histoname = "ljets_ge4j_3t_Reco_tHW_wb_h_dr"
    interf_ljets_ge4j_3t_Reco_tHW_wb_h_dr.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_tHW_wb_h_dr)
    
    interf_ljets_ge4j_3t_Reco_tHq_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_tHq_bestJABDToutput",
                                            label          = "ljets_ge4j_3t_Reco_tHq_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_tHq_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_tHq_bestJABDToutput","")
    interf_ljets_ge4j_3t_Reco_tHq_bestJABDToutput.bin_edges = [ 
                # -1.0,
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
    interf_ljets_ge4j_3t_Reco_tHq_bestJABDToutput.histotitle = "Reco_tHq_bestJABDToutput"
    interf_ljets_ge4j_3t_Reco_tHq_bestJABDToutput.histoname = "ljets_ge4j_3t_Reco_tHq_bestJABDToutput"
    interf_ljets_ge4j_3t_Reco_tHq_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_tHq_bestJABDToutput)
    
    interf_ljets_ge4j_3t_Reco_ttH_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_ttH_bestJABDToutput",
                                            label          = "ljets_ge4j_3t_Reco_ttH_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_ttH_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_ttH_bestJABDToutput","")
    interf_ljets_ge4j_3t_Reco_ttH_bestJABDToutput.bin_edges = [ 
                -1.0,
                -0.6,
                # -0.456,
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
                # 0.7
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
                80.0,
                118.4,
                156.8,
                195.2,
                233.6,
                272.0,
                310.4,
                348.8,
                387.2,
                425.6,
                464.0,
                502.4,
                540.8,
                579.2,
                617.6,
                656.0,
                694.4,
                732.8,
                771.2,
                809.6,
                848.0,
                886.4,
                924.8,
                963.2,
                1040.0,
                1155.2,
                1308.8,
                2000.0
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
                0.0,
                40.0,
                80.0,
                120.0,
                160.0,
                200.0,
                240.0,
                280.0,
                320.0,
                360.0,
                400.0,
                440.0,
                480.0,
                520.0,
                560.0,
                600.0,
                640.0,
                680.0,
                720.0,
                760.0,
                800.0,
                840.0,
                880.0,
                920.0,
                960.0,
                1000.0,
                1040.0,
                1080.0,
                1120.0,
                1200.0,
                1280.0,
                1360.0,
                1440.0,
                1560.0,
                1720.0,
                1960.0,
                2000.0
                ]
    interf_ljets_ge4j_3t_Reco_ttbar_whad_m.histotitle = "Reco_ttbar_whad_m"
    interf_ljets_ge4j_3t_Reco_ttbar_whad_m.histoname = "ljets_ge4j_3t_Reco_ttbar_whad_m"
    interf_ljets_ge4j_3t_Reco_ttbar_whad_m.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_ttbar_whad_m)
    
    interf_ljets_ge4j_3t_Reco_ttbar_whaddau_m1 = vhi.variableHistoInterface(variable_name  = "Reco_ttbar_whaddau_m1",
                                            label          = "ljets_ge4j_3t_Reco_ttbar_whaddau_m1",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_ttbar_whaddau_m1.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_ttbar_whaddau_m1","")
    interf_ljets_ge4j_3t_Reco_ttbar_whaddau_m1.bin_edges = [ 
                0.0,
                5.0,
                10.0,
                15.0,
                20.0,
                25.0,
                30.0,
                35.0,
                40.0,
                45.0,
                50.0,
                55.0,
                60.0,
                65.0,
                70.0,
                75.0,
                80.0,
                85.0,
                90.0,
                95.0,
                105.0,
                120.0,
                # 250.0
                ]
    interf_ljets_ge4j_3t_Reco_ttbar_whaddau_m1.histotitle = "Reco_ttbar_whaddau_m1"
    interf_ljets_ge4j_3t_Reco_ttbar_whaddau_m1.histoname = "ljets_ge4j_3t_Reco_ttbar_whaddau_m1"
    interf_ljets_ge4j_3t_Reco_ttbar_whaddau_m1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_ttbar_whaddau_m1)
    
    interf_ljets_ge4j_3t_TaggedJet_M_0 = vhi.variableHistoInterface(variable_name  = "TaggedJet_M[0]",
                                            label          = "ljets_ge4j_3t_TaggedJet_M_0",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_TaggedJet_M_0.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_TaggedJet_M_0","")
    interf_ljets_ge4j_3t_TaggedJet_M_0.bin_edges = [ 
                0.0,
                5.0,
                10.0,
                15.0,
                20.0,
                25.0,
                30.0,
                35.0,
                40.0,
                45.0,
                50.0,
                55.0,
                60.0,
                65.0,
                70.0,
                75.0,
                80.0,
                85.0,
                90.0,
                95.0,
                100.0,
                105.0,
                110.0,
                115.0,
                125.0,
                150.0,
                # 250.0
                ]
    interf_ljets_ge4j_3t_TaggedJet_M_0.histotitle = "TaggedJet_M[0]"
    interf_ljets_ge4j_3t_TaggedJet_M_0.histoname = "ljets_ge4j_3t_TaggedJet_M_0"
    interf_ljets_ge4j_3t_TaggedJet_M_0.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_TaggedJet_M_0)
    
    interf_ljets_ge4j_3t_TaggedJet_M_1 = vhi.variableHistoInterface(variable_name  = "TaggedJet_M[1]",
                                            label          = "ljets_ge4j_3t_TaggedJet_M_1",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_TaggedJet_M_1.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_TaggedJet_M_1","")
    interf_ljets_ge4j_3t_TaggedJet_M_1.bin_edges = [ 
                0.0,
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
                72.0,
                80.0,
                96.0,
                # 200.0
                ]
    interf_ljets_ge4j_3t_TaggedJet_M_1.histotitle = "TaggedJet_M[1]"
    interf_ljets_ge4j_3t_TaggedJet_M_1.histoname = "ljets_ge4j_3t_TaggedJet_M_1"
    interf_ljets_ge4j_3t_TaggedJet_M_1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_TaggedJet_M_1)
    
    interf_ljets_ge4j_3t_TaggedJet_M_2 = vhi.variableHistoInterface(variable_name  = "TaggedJet_M[2]",
                                            label          = "ljets_ge4j_3t_TaggedJet_M_2",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_TaggedJet_M_2.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_TaggedJet_M_2","")
    interf_ljets_ge4j_3t_TaggedJet_M_2.bin_edges = [ 
                0.0,
                3.2,
                4.8,
                6.4,
                8.0,
                9.6,
                11.2,
                12.8,
                14.4,
                16.0,
                17.6,
                19.2,
                20.8,
                22.4,
                24.0,
                25.6,
                27.2,
                28.8,
                30.4,
                33.6,
                38.4,
                # 80.0
                ]
    interf_ljets_ge4j_3t_TaggedJet_M_2.histotitle = "TaggedJet_M[2]"
    interf_ljets_ge4j_3t_TaggedJet_M_2.histoname = "ljets_ge4j_3t_TaggedJet_M_2"
    interf_ljets_ge4j_3t_TaggedJet_M_2.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_TaggedJet_M_2)
    
    interf_ljets_ge4j_3t_TaggedJet_Pt_1 = vhi.variableHistoInterface(variable_name  = "TaggedJet_Pt[1]",
                                            label          = "ljets_ge4j_3t_TaggedJet_Pt_1",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_TaggedJet_Pt_1.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_TaggedJet_Pt_1","")
    interf_ljets_ge4j_3t_TaggedJet_Pt_1.bin_edges = [ 
                30.0,
                49.4,
                68.8,
                88.2,
                107.6,
                127.0,
                146.4,
                165.8,
                185.2,
                204.6,
                224.0,
                243.4,
                262.8,
                282.2,
                301.6,
                321.0,
                340.4,
                359.8,
                379.2,
                398.6,
                418.0,
                437.4,
                476.2,
                495.6,
                534.4,
                612.0,
                670.2,
                # 1000.0
                ]
    interf_ljets_ge4j_3t_TaggedJet_Pt_1.histotitle = "TaggedJet_Pt[1]"
    interf_ljets_ge4j_3t_TaggedJet_Pt_1.histoname = "ljets_ge4j_3t_TaggedJet_Pt_1"
    interf_ljets_ge4j_3t_TaggedJet_Pt_1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_TaggedJet_Pt_1)
    
    interf_ljets_ge4j_3t_TaggedJet_Pt_2 = vhi.variableHistoInterface(variable_name  = "TaggedJet_Pt[2]",
                                            label          = "ljets_ge4j_3t_TaggedJet_Pt_2",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_TaggedJet_Pt_2.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_TaggedJet_Pt_2","")
    interf_ljets_ge4j_3t_TaggedJet_Pt_2.bin_edges = [ 
                30.0,
                45.4,
                60.8,
                76.2,
                91.6,
                107.0,
                122.4,
                137.8,
                153.2,
                168.6,
                184.0,
                199.4,
                214.8,
                230.2,
                245.6,
                276.4,
                # 800.0
                ]
    interf_ljets_ge4j_3t_TaggedJet_Pt_2.histotitle = "TaggedJet_Pt[2]"
    interf_ljets_ge4j_3t_TaggedJet_Pt_2.histoname = "ljets_ge4j_3t_TaggedJet_Pt_2"
    interf_ljets_ge4j_3t_TaggedJet_Pt_2.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_TaggedJet_Pt_2)
    
    plots = init_plots(interfaces = interfaces, data = data)    
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    
def plots_ljets_ge4j_ge4t(data = None):
    label = "\geq 4 jets, \geq 4 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"

    # for combination
    interf_ljets_ge4j_ge4t_Evt_HT_jets = vhi.variableHistoInterface(variable_name  = "Evt_HT_jets",
                                            category_label = label,
                                            label          = "ljets_ge4j_ge4t_Evt_HT_jets")
    interf_ljets_ge4j_ge4t_Evt_HT_jets.category = (selection,"ljets_ge4j_ge4t_Evt_HT_jets","")

    interf_ljets_ge4j_ge4t_Evt_HT_jets.nhistobins = 1
    interf_ljets_ge4j_ge4t_Evt_HT_jets.bin_edges = [200.0,226.0,252.0,278.0,304.0,330.0,356.0,382.0,408.0,434.0,460.0,486.0,512.0,538.0,564.0,590.0,616.0,642.0,668.0,694.0,720.0,746.0,772.0,798.0,824.0,850.0,876.0,902.0,928.0,954.0,980.0,1006.0,1032.0,1058.0,1084.0,1110.0,1136.0,1162.0,1188.0,1214.0,1240.0,1266.0,1292.0,1318.0,1344.0,1370.0,1396.0,1422.0,1448.0,1474.0,1500.0]
    interf_ljets_ge4j_ge4t_Evt_HT_jets.histoname = "ljets_ge4j_ge4t_Evt_HT_jets"
    interf_ljets_ge4j_ge4t_Evt_HT_jets.histotitle = "H_{T}(jets)"
    interf_ljets_ge4j_ge4t_Evt_HT_jets.selection = interf_ljets_ge4j_ge4t_Evt_HT_jets.category[0]

    interfaces.append(interf_ljets_ge4j_ge4t_Evt_HT_jets)
 
    # top variables
    interf_ljets_ge4j_ge4t_CSV_1 = vhi.variableHistoInterface(variable_name  = "CSV[1]",
                                            label          = "ljets_ge4j_ge4t_CSV_1",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_CSV_1.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_CSV_1","")
    interf_ljets_ge4j_ge4t_CSV_1.bin_edges = [ 
                0.277,
                0.3493,
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
    interf_ljets_ge4j_ge4t_CSV_1.histotitle = "CSV[1]"
    interf_ljets_ge4j_ge4t_CSV_1.histoname = "ljets_ge4j_ge4t_CSV_1"
    interf_ljets_ge4j_ge4t_CSV_1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_CSV_1)
    
    interf_ljets_ge4j_ge4t_CSV_2 = vhi.variableHistoInterface(variable_name  = "CSV[2]",
                                            label          = "ljets_ge4j_ge4t_CSV_2",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_CSV_2.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_CSV_2","")
    interf_ljets_ge4j_ge4t_CSV_2.bin_edges = [ 
                0.277,
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
    interf_ljets_ge4j_ge4t_CSV_2.histotitle = "CSV[2]"
    interf_ljets_ge4j_ge4t_CSV_2.histoname = "ljets_ge4j_ge4t_CSV_2"
    interf_ljets_ge4j_ge4t_CSV_2.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_CSV_2)
    
    interf_ljets_ge4j_ge4t_CSV_3 = vhi.variableHistoInterface(variable_name  = "CSV[3]",
                                            label          = "ljets_ge4j_ge4t_CSV_3",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_CSV_3.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_CSV_3","")
    interf_ljets_ge4j_ge4t_CSV_3.bin_edges = [ 
                0.277,
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
                0.6963,
                0.7108,
                0.7397,
                0.7686,
                0.7976,
                0.8409,
                0.8843,
                0.9422,
                1.0
                ]
    interf_ljets_ge4j_ge4t_CSV_3.histotitle = "CSV[3]"
    interf_ljets_ge4j_ge4t_CSV_3.histoname = "ljets_ge4j_ge4t_CSV_3"
    interf_ljets_ge4j_ge4t_CSV_3.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_CSV_3)
    
    interf_ljets_ge4j_ge4t_Evt_CSV_avg = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg",
                                            label          = "ljets_ge4j_ge4t_Evt_CSV_avg",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_CSV_avg.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_CSV_avg","")
    interf_ljets_ge4j_ge4t_Evt_CSV_avg.bin_edges = [ 
                # 0.15,
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
                0.898,
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
                # 0.3,
                0.412,
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
                0.944,
                0.972,
                1.0
                ]
    interf_ljets_ge4j_ge4t_Evt_CSV_avg_tagged.histotitle = "Evt_CSV_avg_tagged"
    interf_ljets_ge4j_ge4t_Evt_CSV_avg_tagged.histoname = "ljets_ge4j_ge4t_Evt_CSV_avg_tagged"
    interf_ljets_ge4j_ge4t_Evt_CSV_avg_tagged.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_CSV_avg_tagged)
    
    interf_ljets_ge4j_ge4t_Evt_CSV_dev = vhi.variableHistoInterface(variable_name  = "Evt_CSV_dev",
                                            label          = "ljets_ge4j_ge4t_Evt_CSV_dev",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_CSV_dev.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_CSV_dev","")
    interf_ljets_ge4j_ge4t_Evt_CSV_dev.bin_edges = [ 
                0.0,
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
                0.205,
                0.25
                ]
    interf_ljets_ge4j_ge4t_Evt_CSV_dev.histotitle = "Evt_CSV_dev"
    interf_ljets_ge4j_ge4t_Evt_CSV_dev.histoname = "ljets_ge4j_ge4t_Evt_CSV_dev"
    interf_ljets_ge4j_ge4t_Evt_CSV_dev.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_CSV_dev)
    
    interf_ljets_ge4j_ge4t_Evt_CSV_min_tagged = vhi.variableHistoInterface(variable_name  = "Evt_CSV_min_tagged",
                                            label          = "ljets_ge4j_ge4t_Evt_CSV_min_tagged",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_CSV_min_tagged.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_CSV_min_tagged","")
    interf_ljets_ge4j_ge4t_Evt_CSV_min_tagged.bin_edges = [ 
                0.277,
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
                0.7108,
                0.7397,
                0.7686,
                0.812,
                0.8699,
                0.9277,
                1.0
                ]
    interf_ljets_ge4j_ge4t_Evt_CSV_min_tagged.histotitle = "Evt_CSV_min_tagged"
    interf_ljets_ge4j_ge4t_Evt_CSV_min_tagged.histoname = "ljets_ge4j_ge4t_Evt_CSV_min_tagged"
    interf_ljets_ge4j_ge4t_Evt_CSV_min_tagged.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_CSV_min_tagged)
    
    interf_ljets_ge4j_ge4t_Evt_Deta_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Deta_JetsAverage",
                                            label          = "ljets_ge4j_ge4t_Evt_Deta_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_Deta_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_Deta_JetsAverage","")
    interf_ljets_ge4j_ge4t_Evt_Deta_JetsAverage.bin_edges = [ 
                0.0,
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
                2.28,
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
                0.0,
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
                2.4,
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
                0.35,
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
                2.113,
                2.285,
                2.5
                ]
    interf_ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets.histotitle = "Evt_Dr_minDrTaggedJets"
    interf_ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets.histoname = "ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets"
    interf_ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets)
    
    interf_ljets_ge4j_ge4t_Evt_E_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_E_JetsAverage",
                                            label          = "ljets_ge4j_ge4t_Evt_E_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_E_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_E_JetsAverage","")
    interf_ljets_ge4j_ge4t_Evt_E_JetsAverage.bin_edges = [ 
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
                443.2,
                481.6,
                558.4,
                # 1000.0
                ]
    interf_ljets_ge4j_ge4t_Evt_E_JetsAverage.histotitle = "Evt_E_JetsAverage"
    interf_ljets_ge4j_ge4t_Evt_E_JetsAverage.histoname = "ljets_ge4j_ge4t_Evt_E_JetsAverage"
    interf_ljets_ge4j_ge4t_Evt_E_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_E_JetsAverage)
    
    interf_ljets_ge4j_ge4t_Evt_M2_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_M2_TaggedJetsAverage",
                                            label          = "ljets_ge4j_ge4t_Evt_M2_TaggedJetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_M2_TaggedJetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_M2_TaggedJetsAverage","")
    interf_ljets_ge4j_ge4t_Evt_M2_TaggedJetsAverage.bin_edges = [ 
                40.0,
                69.2,
                98.4,
                127.6,
                156.8,
                186.0,
                215.2,
                244.4,
                273.6,
                302.8,
                332.0,
                361.2,
                390.4,
                419.6,
                448.8,
                478.0,
                536.4,
                624.0,
                # 1500.0
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
                5.0,
                6.9,
                8.8,
                10.7,
                12.6,
                14.5,
                16.4,
                18.3,
                20.2,
                22.1,
                24.0,
                25.9,
                29.7,
                35.4,
                # 100.0
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
                4.5,
                6.41,
                8.32,
                10.23,
                12.14,
                14.05,
                15.96,
                17.87,
                19.78,
                21.69,
                23.6,
                25.51,
                27.42,
                29.33,
                33.15,
                38.88,
                # 100.0
                ]
    interf_ljets_ge4j_ge4t_Evt_M_TaggedJetsAverage.histotitle = "Evt_M_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_Evt_M_TaggedJetsAverage.histoname = "ljets_ge4j_ge4t_Evt_M_TaggedJetsAverage"
    interf_ljets_ge4j_ge4t_Evt_M_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_M_TaggedJetsAverage)
    
    interf_ljets_ge4j_ge4t_Evt_Pt_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Pt_JetsAverage",
                                            label          = "ljets_ge4j_ge4t_Evt_Pt_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_Pt_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_Pt_JetsAverage","")
    interf_ljets_ge4j_ge4t_Evt_Pt_JetsAverage.bin_edges = [ 
                30.0,
                45.4,
                60.8,
                76.2,
                91.6,
                107.0,
                122.4,
                137.8,
                153.2,
                168.6,
                184.0,
                199.4,
                214.8,
                245.6,
                291.8,
                # 800.0
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
                20.0,
                79.2,
                108.8,
                138.4,
                168.0,
                197.6,
                227.2,
                256.8,
                286.4,
                316.0,
                345.6,
                375.2,
                404.8,
                434.4,
                493.6,
                552.8,
                641.6,
                # 1500.0
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
                # -2.5,
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
                10.8,
                11.85,
                13.25,
                15.0
                ]
    interf_ljets_ge4j_ge4t_Evt_blr_transformed.histotitle = "Evt_blr_transformed"
    interf_ljets_ge4j_ge4t_Evt_blr_transformed.histoname = "ljets_ge4j_ge4t_Evt_blr_transformed"
    interf_ljets_ge4j_ge4t_Evt_blr_transformed.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_blr_transformed)
    
    interf_ljets_ge4j_ge4t_Evt_h0 = vhi.variableHistoInterface(variable_name  = "Evt_h0",
                                            label          = "ljets_ge4j_ge4t_Evt_h0",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_h0.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_h0","")
    interf_ljets_ge4j_ge4t_Evt_h0.bin_edges = [ 
                # 0.1,
                0.205,
                0.226,
                0.24,
                0.254,
                0.261,
                0.268,
                0.275,
                0.282,
                0.289,
                0.296,
                0.303,
                0.31,
                0.317,
                0.324,
                0.331,
                0.338,
                0.345,
                0.352,
                0.359,
                0.366,
                0.373,
                0.38,
                0.387,
                0.394,
                0.401,
                0.408,
                0.415,
                0.422,
                0.45
                ]
    interf_ljets_ge4j_ge4t_Evt_h0.histotitle = "Evt_h0"
    interf_ljets_ge4j_ge4t_Evt_h0.histoname = "ljets_ge4j_ge4t_Evt_h0"
    interf_ljets_ge4j_ge4t_Evt_h0.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_h0)
    
    interf_ljets_ge4j_ge4t_Jet_M_0 = vhi.variableHistoInterface(variable_name  = "Jet_M[0]",
                                            label          = "ljets_ge4j_ge4t_Jet_M_0",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Jet_M_0.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Jet_M_0","")
    interf_ljets_ge4j_ge4t_Jet_M_0.bin_edges = [ 
                2.7,
                7.446,
                12.192,
                16.938,
                21.684,
                26.43,
                31.176,
                35.922,
                40.668,
                45.414,
                50.16,
                54.906,
                59.652,
                64.398,
                73.89,
                83.382,
                92.874,
                # 240.0
                ]
    interf_ljets_ge4j_ge4t_Jet_M_0.histotitle = "Jet_M[0]"
    interf_ljets_ge4j_ge4t_Jet_M_0.histoname = "ljets_ge4j_ge4t_Jet_M_0"
    interf_ljets_ge4j_ge4t_Jet_M_0.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Jet_M_0)
    
    interf_ljets_ge4j_ge4t_Jet_Pt_1 = vhi.variableHistoInterface(variable_name  = "Jet_Pt[1]",
                                            label          = "ljets_ge4j_ge4t_Jet_Pt_1",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Jet_Pt_1.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Jet_Pt_1","")
    interf_ljets_ge4j_ge4t_Jet_Pt_1.bin_edges = [ 
                30.0,
                49.4,
                68.8,
                88.2,
                107.6,
                127.0,
                146.4,
                165.8,
                185.2,
                204.6,
                224.0,
                243.4,
                262.8,
                282.2,
                301.6,
                321.0,
                359.8,
                418.0,
                495.6,
                # 1000.0
                ]
    interf_ljets_ge4j_ge4t_Jet_Pt_1.histotitle = "Jet_Pt[1]"
    interf_ljets_ge4j_ge4t_Jet_Pt_1.histoname = "ljets_ge4j_ge4t_Jet_Pt_1"
    interf_ljets_ge4j_ge4t_Jet_Pt_1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Jet_Pt_1)
    
    interf_ljets_ge4j_ge4t_N_BTagsL = vhi.variableHistoInterface(variable_name  = "N_BTagsL",
                                            label          = "ljets_ge4j_ge4t_N_BTagsL",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_N_BTagsL.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_N_BTagsL","")
    interf_ljets_ge4j_ge4t_N_BTagsL.bin_edges = [ 
                3.5,
                4.5,
                5.5,
                6.5
                ]
    interf_ljets_ge4j_ge4t_N_BTagsL.histotitle = "N_BTagsL"
    interf_ljets_ge4j_ge4t_N_BTagsL.histoname = "ljets_ge4j_ge4t_N_BTagsL"
    interf_ljets_ge4j_ge4t_N_BTagsL.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_N_BTagsL)
    
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
    interf_ljets_ge4j_ge4t_N_BTagsM.nhistobins = 50
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
                -1.5,
                0,
                # 0.25,
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
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.histotitle = "Reco_JABDT_tHW_Jet_CSV_btop"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.histoname = "ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop)
    
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_btop = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHq_Jet_CSV_btop",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_btop",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_btop.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_btop","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_btop.bin_edges = [ 
                -1.5,
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
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_btop.histotitle = "Reco_JABDT_tHq_Jet_CSV_btop"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_btop.histoname = "ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_btop"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_btop.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_btop)
    
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1 = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHq_Jet_CSV_hdau1",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1.bin_edges = [ 
                -1.5,
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
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1.histotitle = "Reco_JABDT_tHq_Jet_CSV_hdau1"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1.histoname = "ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1)
    
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_log_top_m = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHq_log_top_m",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_tHq_log_top_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_log_top_m.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_tHq_log_top_m","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_log_top_m.bin_edges = [ 
                -1.5,
                4.0,
                4.62,
                4.79,
                4.96,
                5.13,
                5.3,
                5.47,
                5.64,
                5.81,
                5.98,
                6.15,
                6.32,
                7.0
                ]
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_log_top_m.histotitle = "Reco_JABDT_tHq_log_top_m"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_log_top_m.histoname = "ljets_ge4j_ge4t_Reco_JABDT_tHq_log_top_m"
    interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_log_top_m.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_tHq_log_top_m)
    
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_pt = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttH_log_toplep_pt",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_pt",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_pt.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_pt","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_pt.bin_edges = [ 
                -1.5,
                -1,
                2.92,
                3.26,
                3.43,
                3.6,
                3.77,
                3.94,
                4.11,
                4.28,
                4.45,
                4.62,
                4.79,
                4.96,
                5.13,
                5.3,
                5.47,
                5.64,
                5.81,
                5.98,
                6.15,
                6.32,
                7.0
                ]
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_pt.histotitle = "Reco_JABDT_ttH_log_toplep_pt"
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_pt.histoname = "ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_pt"
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_pt.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_pt)
    
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_btoplep = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttbar_Jet_CSV_btoplep",
                                            label          = "ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_btoplep",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_btoplep.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_btoplep","")
    interf_ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_btoplep.bin_edges = [ 
                # 0.0,
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
                0.1,
                0.12,
                0.16,
                0.2,
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
                0.92,
                0.94,
                0.98,
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
                0.12,
                0.16,
                0.2,
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
                0.92,
                0.98,
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
                -1.0,
                -0.5,
                -0.2,
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
    
    interf_ljets_ge4j_ge4t_Reco_tHW_hdau_m1 = vhi.variableHistoInterface(variable_name  = "Reco_tHW_hdau_m1",
                                            label          = "ljets_ge4j_ge4t_Reco_tHW_hdau_m1",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_tHW_hdau_m1.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_tHW_hdau_m1","")
    interf_ljets_ge4j_ge4t_Reco_tHW_hdau_m1.bin_edges = [ 
                -1.5,
                0,
                2.53,
                6.56,
                10.59,
                14.62,
                18.65,
                22.68,
                26.71,
                30.74,
                34.77,
                38.8,
                42.83,
                46.86,
                54.92,
                62.98,
                79.1,
                # 200.0
                ]
    interf_ljets_ge4j_ge4t_Reco_tHW_hdau_m1.histotitle = "Reco_tHW_hdau_m1"
    interf_ljets_ge4j_ge4t_Reco_tHW_hdau_m1.histoname = "ljets_ge4j_ge4t_Reco_tHW_hdau_m1"
    interf_ljets_ge4j_ge4t_Reco_tHW_hdau_m1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_tHW_hdau_m1)
    
    interf_ljets_ge4j_ge4t_Reco_tHW_hdau_phi1 = vhi.variableHistoInterface(variable_name  = "Reco_tHW_hdau_phi1",
                                            label          = "ljets_ge4j_ge4t_Reco_tHW_hdau_phi1",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_tHW_hdau_phi1.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_tHW_hdau_phi1","")
    interf_ljets_ge4j_ge4t_Reco_tHW_hdau_phi1.bin_edges = [ 
                -5.0,
                -3.2088,
                -3.046,
                -2.8832,
                -2.7204,
                -2.5575,
                -2.3947,
                -2.2319,
                -2.069,
                -1.9062,
                -1.7434,
                -1.5805,
                -1.4177,
                -1.2549,
                -1.092,
                -0.9292,
                -0.7664,
                -0.6035,
                -0.4407,
                -0.2779,
                -0.115,
                0.0478,
                0.2106,
                0.3735,
                0.5363,
                0.6991,
                0.862,
                1.0248,
                1.1876,
                1.3504,
                1.5133,
                1.6761,
                1.8389,
                2.0018,
                2.1646,
                2.3274,
                2.4903,
                2.6531,
                2.8159,
                2.9788,
                3.1416
                ]
    interf_ljets_ge4j_ge4t_Reco_tHW_hdau_phi1.histotitle = "Reco_tHW_hdau_phi1"
    interf_ljets_ge4j_ge4t_Reco_tHW_hdau_phi1.histoname = "ljets_ge4j_ge4t_Reco_tHW_hdau_phi1"
    interf_ljets_ge4j_ge4t_Reco_tHW_hdau_phi1.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_tHW_hdau_phi1)
    
    interf_ljets_ge4j_ge4t_Reco_tHW_top_h_dr = vhi.variableHistoInterface(variable_name  = "Reco_tHW_top_h_dr",
                                            label          = "ljets_ge4j_ge4t_Reco_tHW_top_h_dr",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_tHW_top_h_dr.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_tHW_top_h_dr","")
    interf_ljets_ge4j_ge4t_Reco_tHW_top_h_dr.bin_edges = [ 
                -1.5,
                0.,
                0.57,
                0.8,
                1.03,
                1.26,
                1.49,
                1.72,
                1.95,
                2.18,
                2.41,
                2.64,
                2.87,
                3.1,
                3.33,
                3.56,
                3.79,
                4.02,
                4.25,
                4.48,
                4.71,
                4.94,
                5.17,
                5.63,
                # 10.0
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
                0.,
                0.59,
                0.78,
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
                3.82,
                4.2,
                4.58,
                5.15,
                # 8.0
                ]
    interf_ljets_ge4j_ge4t_Reco_tHW_whad_dr.histotitle = "Reco_tHW_whad_dr"
    interf_ljets_ge4j_ge4t_Reco_tHW_whad_dr.histoname = "ljets_ge4j_ge4t_Reco_tHW_whad_dr"
    interf_ljets_ge4j_ge4t_Reco_tHW_whad_dr.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_tHW_whad_dr)
    
    interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_tHq_bestJABDToutput",
                                            label          = "ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput","")
    interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput.bin_edges = [ 
                -1.0,
                -0.6,
                -0.184,
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
    interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput.histotitle = "Reco_tHq_bestJABDToutput"
    interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput.histoname = "ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput"
    interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput)
    
    interf_ljets_ge4j_ge4t_Reco_tHq_h_m = vhi.variableHistoInterface(variable_name  = "Reco_tHq_h_m",
                                            label          = "ljets_ge4j_ge4t_Reco_tHq_h_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_tHq_h_m.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_tHq_h_m","")
    interf_ljets_ge4j_ge4t_Reco_tHq_h_m.bin_edges = [ 
                -1.5,
                0,
                38.53,
                78.56,
                118.59,
                158.62,
                198.65,
                # 2000.0
                ]
    interf_ljets_ge4j_ge4t_Reco_tHq_h_m.histotitle = "Reco_tHq_h_m"
    interf_ljets_ge4j_ge4t_Reco_tHq_h_m.histoname = "ljets_ge4j_ge4t_Reco_tHq_h_m"
    interf_ljets_ge4j_ge4t_Reco_tHq_h_m.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_tHq_h_m)
    
    interf_ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_ttH_bestJABDToutput",
                                            label          = "ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput","")
    interf_ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput.bin_edges = [ 
                -1.0,
                -0.4,
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
                # 0.7
                ]
    interf_ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput.histotitle = "Reco_ttH_bestJABDToutput"
    interf_ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput.histoname = "ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput"
    interf_ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput)
    
    interf_ljets_ge4j_ge4t_Reco_ttH_tophad_pt = vhi.variableHistoInterface(variable_name  = "Reco_ttH_tophad_pt",
                                            label          = "ljets_ge4j_ge4t_Reco_ttH_tophad_pt",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_ttH_tophad_pt.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_ttH_tophad_pt","")
    interf_ljets_ge4j_ge4t_Reco_ttH_tophad_pt.bin_edges = [ 
                -1.5,
                0,
                38.53,
                78.56,
                118.59,
                158.62,
                198.65,
                238.68,
                278.71,
                318.74,
                358.77,
                398.8,
                438.83,
                478.86,
                558.92,
                679.01,
                # 2000.0
                ]
    interf_ljets_ge4j_ge4t_Reco_ttH_tophad_pt.histotitle = "Reco_ttH_tophad_pt"
    interf_ljets_ge4j_ge4t_Reco_ttH_tophad_pt.histoname = "ljets_ge4j_ge4t_Reco_ttH_tophad_pt"
    interf_ljets_ge4j_ge4t_Reco_ttH_tophad_pt.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_ttH_tophad_pt)
    
    interf_ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_ttbar_bestJABDToutput",
                                            label          = "ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput","")
    interf_ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput.bin_edges = [ 
                # -0.4,
                -0.224,
                -0.18,
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
                0.7
                ]
    interf_ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput.histotitle = "Reco_ttbar_bestJABDToutput"
    interf_ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput.histoname = "ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput"
    interf_ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput)
    
    interf_ljets_ge4j_ge4t_TaggedJet_CSV_0 = vhi.variableHistoInterface(variable_name  = "TaggedJet_CSV[0]",
                                            label          = "ljets_ge4j_ge4t_TaggedJet_CSV_0",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_TaggedJet_CSV_0.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_TaggedJet_CSV_0","")
    interf_ljets_ge4j_ge4t_TaggedJet_CSV_0.bin_edges = [ 
                0.277,
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
    interf_ljets_ge4j_ge4t_TaggedJet_CSV_0.histotitle = "TaggedJet_CSV[0]"
    interf_ljets_ge4j_ge4t_TaggedJet_CSV_0.histoname = "ljets_ge4j_ge4t_TaggedJet_CSV_0"
    interf_ljets_ge4j_ge4t_TaggedJet_CSV_0.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_TaggedJet_CSV_0)
    
    interf_ljets_ge4j_ge4t_TaggedJet_CSV_3 = vhi.variableHistoInterface(variable_name  = "TaggedJet_CSV[3]",
                                            label          = "ljets_ge4j_ge4t_TaggedJet_CSV_3",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_TaggedJet_CSV_3.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_TaggedJet_CSV_3","")
    interf_ljets_ge4j_ge4t_TaggedJet_CSV_3.bin_edges = [ 
                0.277,
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
    interf_ljets_ge4j_ge4t_TaggedJet_CSV_3.histotitle = "TaggedJet_CSV[3]"
    interf_ljets_ge4j_ge4t_TaggedJet_CSV_3.histoname = "ljets_ge4j_ge4t_TaggedJet_CSV_3"
    interf_ljets_ge4j_ge4t_TaggedJet_CSV_3.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_TaggedJet_CSV_3)
    
    interf_ljets_ge4j_ge4t_TaggedJet_M_3 = vhi.variableHistoInterface(variable_name  = "TaggedJet_M[3]",
                                            label          = "ljets_ge4j_ge4t_TaggedJet_M_3",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_TaggedJet_M_3.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_TaggedJet_M_3","")
    interf_ljets_ge4j_ge4t_TaggedJet_M_3.bin_edges = [ 
                1.5,
                3.44,
                4.41,
                5.38,
                6.35,
                7.32,
                8.29,
                9.26,
                10.23,
                11.2,
                12.17,
                13.14,
                14.11,
                16.05,
                18.96,
                # 50.0
                ]
    interf_ljets_ge4j_ge4t_TaggedJet_M_3.histotitle = "TaggedJet_M[3]"
    interf_ljets_ge4j_ge4t_TaggedJet_M_3.histoname = "ljets_ge4j_ge4t_TaggedJet_M_3"
    interf_ljets_ge4j_ge4t_TaggedJet_M_3.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_TaggedJet_M_3)
    
    interf_ljets_ge4j_ge4t_TaggedJet_Pt_3 = vhi.variableHistoInterface(variable_name  = "TaggedJet_Pt[3]",
                                            label          = "ljets_ge4j_ge4t_TaggedJet_Pt_3",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_TaggedJet_Pt_3.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_TaggedJet_Pt_3","")
    interf_ljets_ge4j_ge4t_TaggedJet_Pt_3.bin_edges = [ 
                30.0,
                37.4,
                44.8,
                52.2,
                59.6,
                67.0,
                74.4,
                81.8,
                89.2,
                96.6,
                111.4,
                133.6,
                # 400.0
                ]
    interf_ljets_ge4j_ge4t_TaggedJet_Pt_3.histotitle = "TaggedJet_Pt[3]"
    interf_ljets_ge4j_ge4t_TaggedJet_Pt_3.histoname = "ljets_ge4j_ge4t_TaggedJet_Pt_3"
    interf_ljets_ge4j_ge4t_TaggedJet_Pt_3.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_TaggedJet_Pt_3)
    
    plots = init_plots(interfaces = interfaces, data = data)    
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_ljets_ge4j_3t(data)
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

def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
    