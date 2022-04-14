
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



def plots_ge5j_ge4t(data = None):
    label = "\geq 5 jets, \geq 4 b-tags"
    interfaces = []
    selection = "(N_Jets>=5&&N_BTagsM>=4)&&(1.)"


    interf_ljets_ge5j_ge4t_CSV_2 = vhi.variableHistoInterface(variable_name  = "CSV[2]",
                                            label          = "ljets_ge5j_ge4t_CSV_2",
                                            selection      = "(N_Jets>=5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge5j_ge4t_CSV_2.category = ("(N_Jets>=5&&N_BTagsM>=4)&&(1.)","ljets_ge5j_ge4t_CSV_2","")
    interf_ljets_ge5j_ge4t_CSV_2.category_label = label
    interf_ljets_ge5j_ge4t_CSV_2.minxval = 0.277
    interf_ljets_ge5j_ge4t_CSV_2.maxxval = 1.0
    interf_ljets_ge5j_ge4t_CSV_2.histotitle = "CSV[2]"
    interf_ljets_ge5j_ge4t_CSV_2.histoname = "ljets_ge5j_ge4t_CSV_2"
    interf_ljets_ge5j_ge4t_CSV_2.nhistobins = 50
    interfaces.append(interf_ljets_ge5j_ge4t_CSV_2)
    
    interf_ljets_ge5j_ge4t_Evt_CSV_avg = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg",
                                            label          = "ljets_ge5j_ge4t_Evt_CSV_avg",
                                            selection      = "(N_Jets>=5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge5j_ge4t_Evt_CSV_avg.category = ("(N_Jets>=5&&N_BTagsM>=4)&&(1.)","ljets_ge5j_ge4t_Evt_CSV_avg","")
    interf_ljets_ge5j_ge4t_Evt_CSV_avg.category_label = label
    interf_ljets_ge5j_ge4t_Evt_CSV_avg.minxval = 0.15
    interf_ljets_ge5j_ge4t_Evt_CSV_avg.maxxval = 1.0
    interf_ljets_ge5j_ge4t_Evt_CSV_avg.histotitle = "Evt_CSV_avg"
    interf_ljets_ge5j_ge4t_Evt_CSV_avg.histoname = "ljets_ge5j_ge4t_Evt_CSV_avg"
    interf_ljets_ge5j_ge4t_Evt_CSV_avg.nhistobins = 50
    interfaces.append(interf_ljets_ge5j_ge4t_Evt_CSV_avg)
    
    interf_ljets_ge5j_ge4t_Evt_CSV_avg_tagged = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg_tagged",
                                            label          = "ljets_ge5j_ge4t_Evt_CSV_avg_tagged",
                                            selection      = "(N_Jets>=5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge5j_ge4t_Evt_CSV_avg_tagged.category = ("(N_Jets>=5&&N_BTagsM>=4)&&(1.)","ljets_ge5j_ge4t_Evt_CSV_avg_tagged","")
    interf_ljets_ge5j_ge4t_Evt_CSV_avg_tagged.category_label = label
    interf_ljets_ge5j_ge4t_Evt_CSV_avg_tagged.minxval = 0.3
    interf_ljets_ge5j_ge4t_Evt_CSV_avg_tagged.maxxval = 1.0
    interf_ljets_ge5j_ge4t_Evt_CSV_avg_tagged.histotitle = "Evt_CSV_avg_tagged"
    interf_ljets_ge5j_ge4t_Evt_CSV_avg_tagged.histoname = "ljets_ge5j_ge4t_Evt_CSV_avg_tagged"
    interf_ljets_ge5j_ge4t_Evt_CSV_avg_tagged.nhistobins = 50
    interfaces.append(interf_ljets_ge5j_ge4t_Evt_CSV_avg_tagged)
    
    interf_ljets_ge5j_ge4t_Evt_CSV_dev = vhi.variableHistoInterface(variable_name  = "Evt_CSV_dev",
                                            label          = "ljets_ge5j_ge4t_Evt_CSV_dev",
                                            selection      = "(N_Jets>=5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge5j_ge4t_Evt_CSV_dev.category = ("(N_Jets>=5&&N_BTagsM>=4)&&(1.)","ljets_ge5j_ge4t_Evt_CSV_dev","")
    interf_ljets_ge5j_ge4t_Evt_CSV_dev.category_label = label
    interf_ljets_ge5j_ge4t_Evt_CSV_dev.minxval = 0.0
    interf_ljets_ge5j_ge4t_Evt_CSV_dev.maxxval = 0.25
    interf_ljets_ge5j_ge4t_Evt_CSV_dev.histotitle = "Evt_CSV_dev"
    interf_ljets_ge5j_ge4t_Evt_CSV_dev.histoname = "ljets_ge5j_ge4t_Evt_CSV_dev"
    interf_ljets_ge5j_ge4t_Evt_CSV_dev.nhistobins = 50
    interfaces.append(interf_ljets_ge5j_ge4t_Evt_CSV_dev)
    
    interf_ljets_ge5j_ge4t_Evt_Deta_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Deta_JetsAverage",
                                            label          = "ljets_ge5j_ge4t_Evt_Deta_JetsAverage",
                                            selection      = "(N_Jets>=5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge5j_ge4t_Evt_Deta_JetsAverage.category = ("(N_Jets>=5&&N_BTagsM>=4)&&(1.)","ljets_ge5j_ge4t_Evt_Deta_JetsAverage","")
    interf_ljets_ge5j_ge4t_Evt_Deta_JetsAverage.category_label = label
    interf_ljets_ge5j_ge4t_Evt_Deta_JetsAverage.minxval = 0.0
    interf_ljets_ge5j_ge4t_Evt_Deta_JetsAverage.maxxval = 3.0
    interf_ljets_ge5j_ge4t_Evt_Deta_JetsAverage.histotitle = "Evt_Deta_JetsAverage"
    interf_ljets_ge5j_ge4t_Evt_Deta_JetsAverage.histoname = "ljets_ge5j_ge4t_Evt_Deta_JetsAverage"
    interf_ljets_ge5j_ge4t_Evt_Deta_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge5j_ge4t_Evt_Deta_JetsAverage)
    
    interf_ljets_ge5j_ge4t_Evt_Deta_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Deta_TaggedJetsAverage",
                                            label          = "ljets_ge5j_ge4t_Evt_Deta_TaggedJetsAverage",
                                            selection      = "(N_Jets>=5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge5j_ge4t_Evt_Deta_TaggedJetsAverage.category = ("(N_Jets>=5&&N_BTagsM>=4)&&(1.)","ljets_ge5j_ge4t_Evt_Deta_TaggedJetsAverage","")
    interf_ljets_ge5j_ge4t_Evt_Deta_TaggedJetsAverage.category_label = label
    interf_ljets_ge5j_ge4t_Evt_Deta_TaggedJetsAverage.minxval = 0.0
    interf_ljets_ge5j_ge4t_Evt_Deta_TaggedJetsAverage.maxxval = 3.0
    interf_ljets_ge5j_ge4t_Evt_Deta_TaggedJetsAverage.histotitle = "Evt_Deta_TaggedJetsAverage"
    interf_ljets_ge5j_ge4t_Evt_Deta_TaggedJetsAverage.histoname = "ljets_ge5j_ge4t_Evt_Deta_TaggedJetsAverage"
    interf_ljets_ge5j_ge4t_Evt_Deta_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge5j_ge4t_Evt_Deta_TaggedJetsAverage)
    
    interf_ljets_ge5j_ge4t_Evt_HT_jets = vhi.variableHistoInterface(variable_name  = "Evt_HT_jets",
                                            label          = "ljets_ge5j_ge4t_Evt_HT_jets",
                                            selection      = "(N_Jets>=5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge5j_ge4t_Evt_HT_jets.category = ("(N_Jets>=5&&N_BTagsM>=4)&&(1.)","ljets_ge5j_ge4t_Evt_HT_jets","")
    interf_ljets_ge5j_ge4t_Evt_HT_jets.category_label = label
    interf_ljets_ge5j_ge4t_Evt_HT_jets.minxval = 200.0
    interf_ljets_ge5j_ge4t_Evt_HT_jets.maxxval = 1500.0
    interf_ljets_ge5j_ge4t_Evt_HT_jets.histotitle = "H_{T}(jets)"
    interf_ljets_ge5j_ge4t_Evt_HT_jets.histoname = "ljets_ge5j_ge4t_Evt_HT_jets"
    interf_ljets_ge5j_ge4t_Evt_HT_jets.nhistobins = 50
    interfaces.append(interf_ljets_ge5j_ge4t_Evt_HT_jets)
    
    interf_ljets_ge5j_ge4t_Evt_HT_tags = vhi.variableHistoInterface(variable_name  = "Evt_HT_tags",
                                            label          = "ljets_ge5j_ge4t_Evt_HT_tags",
                                            selection      = "(N_Jets>=5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge5j_ge4t_Evt_HT_tags.category = ("(N_Jets>=5&&N_BTagsM>=4)&&(1.)","ljets_ge5j_ge4t_Evt_HT_tags","")
    interf_ljets_ge5j_ge4t_Evt_HT_tags.category_label = label
    interf_ljets_ge5j_ge4t_Evt_HT_tags.minxval = 100.0
    interf_ljets_ge5j_ge4t_Evt_HT_tags.maxxval = 1000.0
    interf_ljets_ge5j_ge4t_Evt_HT_tags.histotitle = "Evt_HT_tags"
    interf_ljets_ge5j_ge4t_Evt_HT_tags.histoname = "ljets_ge5j_ge4t_Evt_HT_tags"
    interf_ljets_ge5j_ge4t_Evt_HT_tags.nhistobins = 50
    interfaces.append(interf_ljets_ge5j_ge4t_Evt_HT_tags)
    
    interf_ljets_ge5j_ge4t_Evt_M2_minDrTaggedJets = vhi.variableHistoInterface(variable_name  = "Evt_M2_minDrTaggedJets",
                                            label          = "ljets_ge5j_ge4t_Evt_M2_minDrTaggedJets",
                                            selection      = "(N_Jets>=5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge5j_ge4t_Evt_M2_minDrTaggedJets.category = ("(N_Jets>=5&&N_BTagsM>=4)&&(1.)","ljets_ge5j_ge4t_Evt_M2_minDrTaggedJets","")
    interf_ljets_ge5j_ge4t_Evt_M2_minDrTaggedJets.category_label = label
    interf_ljets_ge5j_ge4t_Evt_M2_minDrTaggedJets.minxval = 0.0
    interf_ljets_ge5j_ge4t_Evt_M2_minDrTaggedJets.maxxval = 400.0
    interf_ljets_ge5j_ge4t_Evt_M2_minDrTaggedJets.histotitle = "M_{2}( min #DeltaR(tag,tag) )"
    interf_ljets_ge5j_ge4t_Evt_M2_minDrTaggedJets.histoname = "ljets_ge5j_ge4t_Evt_M2_minDrTaggedJets"
    interf_ljets_ge5j_ge4t_Evt_M2_minDrTaggedJets.nhistobins = 50
    interfaces.append(interf_ljets_ge5j_ge4t_Evt_M2_minDrTaggedJets)
    
    interf_ljets_ge5j_ge4t_Evt_M_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_M_JetsAverage",
                                            label          = "ljets_ge5j_ge4t_Evt_M_JetsAverage",
                                            selection      = "(N_Jets>=5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge5j_ge4t_Evt_M_JetsAverage.category = ("(N_Jets>=5&&N_BTagsM>=4)&&(1.)","ljets_ge5j_ge4t_Evt_M_JetsAverage","")
    interf_ljets_ge5j_ge4t_Evt_M_JetsAverage.category_label = label
    interf_ljets_ge5j_ge4t_Evt_M_JetsAverage.minxval = 5.0
    interf_ljets_ge5j_ge4t_Evt_M_JetsAverage.maxxval = 50.0
    interf_ljets_ge5j_ge4t_Evt_M_JetsAverage.histotitle = "Evt_M_JetsAverage"
    interf_ljets_ge5j_ge4t_Evt_M_JetsAverage.histoname = "ljets_ge5j_ge4t_Evt_M_JetsAverage"
    interf_ljets_ge5j_ge4t_Evt_M_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge5j_ge4t_Evt_M_JetsAverage)
    
    interf_ljets_ge5j_ge4t_Evt_M_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_M_TaggedJetsAverage",
                                            label          = "ljets_ge5j_ge4t_Evt_M_TaggedJetsAverage",
                                            selection      = "(N_Jets>=5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge5j_ge4t_Evt_M_TaggedJetsAverage.category = ("(N_Jets>=5&&N_BTagsM>=4)&&(1.)","ljets_ge5j_ge4t_Evt_M_TaggedJetsAverage","")
    interf_ljets_ge5j_ge4t_Evt_M_TaggedJetsAverage.category_label = label
    interf_ljets_ge5j_ge4t_Evt_M_TaggedJetsAverage.minxval = 5.0
    interf_ljets_ge5j_ge4t_Evt_M_TaggedJetsAverage.maxxval = 70.0
    interf_ljets_ge5j_ge4t_Evt_M_TaggedJetsAverage.histotitle = "Evt_M_TaggedJetsAverage"
    interf_ljets_ge5j_ge4t_Evt_M_TaggedJetsAverage.histoname = "ljets_ge5j_ge4t_Evt_M_TaggedJetsAverage"
    interf_ljets_ge5j_ge4t_Evt_M_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge5j_ge4t_Evt_M_TaggedJetsAverage)
    
    interf_ljets_ge5j_ge4t_Evt_Pt_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Pt_JetsAverage",
                                            label          = "ljets_ge5j_ge4t_Evt_Pt_JetsAverage",
                                            selection      = "(N_Jets>=5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge5j_ge4t_Evt_Pt_JetsAverage.category = ("(N_Jets>=5&&N_BTagsM>=4)&&(1.)","ljets_ge5j_ge4t_Evt_Pt_JetsAverage","")
    interf_ljets_ge5j_ge4t_Evt_Pt_JetsAverage.category_label = label
    interf_ljets_ge5j_ge4t_Evt_Pt_JetsAverage.minxval = 30.0
    interf_ljets_ge5j_ge4t_Evt_Pt_JetsAverage.maxxval = 500.0
    interf_ljets_ge5j_ge4t_Evt_Pt_JetsAverage.histotitle = "Evt_Pt_JetsAverage"
    interf_ljets_ge5j_ge4t_Evt_Pt_JetsAverage.histoname = "ljets_ge5j_ge4t_Evt_Pt_JetsAverage"
    interf_ljets_ge5j_ge4t_Evt_Pt_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge5j_ge4t_Evt_Pt_JetsAverage)
    
    interf_ljets_ge5j_ge4t_Evt_Pt_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Pt_TaggedJetsAverage",
                                            label          = "ljets_ge5j_ge4t_Evt_Pt_TaggedJetsAverage",
                                            selection      = "(N_Jets>=5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge5j_ge4t_Evt_Pt_TaggedJetsAverage.category = ("(N_Jets>=5&&N_BTagsM>=4)&&(1.)","ljets_ge5j_ge4t_Evt_Pt_TaggedJetsAverage","")
    interf_ljets_ge5j_ge4t_Evt_Pt_TaggedJetsAverage.category_label = label
    interf_ljets_ge5j_ge4t_Evt_Pt_TaggedJetsAverage.minxval = 30.0
    interf_ljets_ge5j_ge4t_Evt_Pt_TaggedJetsAverage.maxxval = 600.0
    interf_ljets_ge5j_ge4t_Evt_Pt_TaggedJetsAverage.histotitle = "Evt_Pt_TaggedJetsAverage"
    interf_ljets_ge5j_ge4t_Evt_Pt_TaggedJetsAverage.histoname = "ljets_ge5j_ge4t_Evt_Pt_TaggedJetsAverage"
    interf_ljets_ge5j_ge4t_Evt_Pt_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge5j_ge4t_Evt_Pt_TaggedJetsAverage)
    
    interf_ljets_ge5j_ge4t_Evt_Pt_minDrTaggedJets = vhi.variableHistoInterface(variable_name  = "Evt_Pt_minDrTaggedJets",
                                            label          = "ljets_ge5j_ge4t_Evt_Pt_minDrTaggedJets",
                                            selection      = "(N_Jets>=5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge5j_ge4t_Evt_Pt_minDrTaggedJets.category = ("(N_Jets>=5&&N_BTagsM>=4)&&(1.)","ljets_ge5j_ge4t_Evt_Pt_minDrTaggedJets","")
    interf_ljets_ge5j_ge4t_Evt_Pt_minDrTaggedJets.category_label = label
    interf_ljets_ge5j_ge4t_Evt_Pt_minDrTaggedJets.minxval = 20.0
    interf_ljets_ge5j_ge4t_Evt_Pt_minDrTaggedJets.maxxval = 600.0
    interf_ljets_ge5j_ge4t_Evt_Pt_minDrTaggedJets.histotitle = "Evt_Pt_minDrTaggedJets"
    interf_ljets_ge5j_ge4t_Evt_Pt_minDrTaggedJets.histoname = "ljets_ge5j_ge4t_Evt_Pt_minDrTaggedJets"
    interf_ljets_ge5j_ge4t_Evt_Pt_minDrTaggedJets.nhistobins = 50
    interfaces.append(interf_ljets_ge5j_ge4t_Evt_Pt_minDrTaggedJets)
    
    interf_ljets_ge5j_ge4t_Evt_blr_transformed = vhi.variableHistoInterface(variable_name  = "Evt_blr_transformed",
                                            label          = "ljets_ge5j_ge4t_Evt_blr_transformed",
                                            selection      = "(N_Jets>=5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge5j_ge4t_Evt_blr_transformed.category = ("(N_Jets>=5&&N_BTagsM>=4)&&(1.)","ljets_ge5j_ge4t_Evt_blr_transformed","")
    interf_ljets_ge5j_ge4t_Evt_blr_transformed.category_label = label
    interf_ljets_ge5j_ge4t_Evt_blr_transformed.minxval = -2.5
    interf_ljets_ge5j_ge4t_Evt_blr_transformed.maxxval = 15.0
    interf_ljets_ge5j_ge4t_Evt_blr_transformed.histotitle = "Evt_blr_transformed"
    interf_ljets_ge5j_ge4t_Evt_blr_transformed.histoname = "ljets_ge5j_ge4t_Evt_blr_transformed"
    interf_ljets_ge5j_ge4t_Evt_blr_transformed.nhistobins = 50
    interfaces.append(interf_ljets_ge5j_ge4t_Evt_blr_transformed)
    
    interf_ljets_ge5j_ge4t_N_Jets = vhi.variableHistoInterface(variable_name  = "N_Jets",
                                            label          = "ljets_ge5j_ge4t_N_Jets",
                                            selection      = "(N_Jets>=5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge5j_ge4t_N_Jets.category = ("(N_Jets>=5&&N_BTagsM>=4)&&(1.)","ljets_ge5j_ge4t_N_Jets","")
    interf_ljets_ge5j_ge4t_N_Jets.category_label = label
    interf_ljets_ge5j_ge4t_N_Jets.minxval = 3.5
    interf_ljets_ge5j_ge4t_N_Jets.maxxval = 10.5
    interf_ljets_ge5j_ge4t_N_Jets.histotitle = "N_Jets"
    interf_ljets_ge5j_ge4t_N_Jets.histoname = "ljets_ge5j_ge4t_N_Jets"
    interf_ljets_ge5j_ge4t_N_Jets.nhistobins = 7
    interfaces.append(interf_ljets_ge5j_ge4t_N_Jets)
    
    interf_ljets_ge5j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_Jet_CSV_btop",
                                            label          = "ljets_ge5j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop",
                                            selection      = "(N_Jets>=5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge5j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.category = ("(N_Jets>=5&&N_BTagsM>=4)&&(1.)","ljets_ge5j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop","")
    interf_ljets_ge5j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.category_label = label
    interf_ljets_ge5j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.minxval = -1.5
    interf_ljets_ge5j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.maxxval = 1.0
    interf_ljets_ge5j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.histotitle = "Reco_JABDT_tHW_Jet_CSV_btop"
    interf_ljets_ge5j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.histoname = "ljets_ge5j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop"
    interf_ljets_ge5j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.nhistobins = 50
    interfaces.append(interf_ljets_ge5j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop)
    
    interf_ljets_ge5j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",
                                            label          = "ljets_ge5j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",
                                            selection      = "(N_Jets>=5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge5j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.category = ("(N_Jets>=5&&N_BTagsM>=4)&&(1.)","ljets_ge5j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt","")
    interf_ljets_ge5j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.category_label = label
    interf_ljets_ge5j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.minxval = -1.5
    interf_ljets_ge5j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.maxxval = 1.0
    interf_ljets_ge5j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.histotitle = "Reco_JABDT_tHW_energy_fraction"
    interf_ljets_ge5j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.histoname = "ljets_ge5j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt"
    interf_ljets_ge5j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.nhistobins = 50
    interfaces.append(interf_ljets_ge5j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt)
    
    interf_ljets_ge5j_ge4t_Reco_JABDT_tHq_abs_ljet_eta = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHq_abs_ljet_eta",
                                            label          = "ljets_ge5j_ge4t_Reco_JABDT_tHq_abs_ljet_eta",
                                            selection      = "(N_Jets>=5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge5j_ge4t_Reco_JABDT_tHq_abs_ljet_eta.category = ("(N_Jets>=5&&N_BTagsM>=4)&&(1.)","ljets_ge5j_ge4t_Reco_JABDT_tHq_abs_ljet_eta","")
    interf_ljets_ge5j_ge4t_Reco_JABDT_tHq_abs_ljet_eta.category_label = label
    interf_ljets_ge5j_ge4t_Reco_JABDT_tHq_abs_ljet_eta.minxval = -1.5
    interf_ljets_ge5j_ge4t_Reco_JABDT_tHq_abs_ljet_eta.maxxval = 4.5
    interf_ljets_ge5j_ge4t_Reco_JABDT_tHq_abs_ljet_eta.histotitle = "Reco_JABDT_tHq_abs_ljet_eta"
    interf_ljets_ge5j_ge4t_Reco_JABDT_tHq_abs_ljet_eta.histoname = "ljets_ge5j_ge4t_Reco_JABDT_tHq_abs_ljet_eta"
    interf_ljets_ge5j_ge4t_Reco_JABDT_tHq_abs_ljet_eta.nhistobins = 50
    interfaces.append(interf_ljets_ge5j_ge4t_Reco_JABDT_tHq_abs_ljet_eta)
    
    interf_ljets_ge5j_ge4t_Reco_tHq_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_tHq_bestJABDToutput",
                                            label          = "ljets_ge5j_ge4t_Reco_tHq_bestJABDToutput",
                                            selection      = "(N_Jets>=5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge5j_ge4t_Reco_tHq_bestJABDToutput.category = ("(N_Jets>=5&&N_BTagsM>=4)&&(1.)","ljets_ge5j_ge4t_Reco_tHq_bestJABDToutput","")
    interf_ljets_ge5j_ge4t_Reco_tHq_bestJABDToutput.category_label = label
    interf_ljets_ge5j_ge4t_Reco_tHq_bestJABDToutput.minxval = -1.0
    interf_ljets_ge5j_ge4t_Reco_tHq_bestJABDToutput.maxxval = 0.7
    interf_ljets_ge5j_ge4t_Reco_tHq_bestJABDToutput.histotitle = "Reco_tHq_bestJABDToutput"
    interf_ljets_ge5j_ge4t_Reco_tHq_bestJABDToutput.histoname = "ljets_ge5j_ge4t_Reco_tHq_bestJABDToutput"
    interf_ljets_ge5j_ge4t_Reco_tHq_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge5j_ge4t_Reco_tHq_bestJABDToutput)
    
    interf_ljets_ge5j_ge4t_Reco_ttH_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_ttH_bestJABDToutput",
                                            label          = "ljets_ge5j_ge4t_Reco_ttH_bestJABDToutput",
                                            selection      = "(N_Jets>=5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge5j_ge4t_Reco_ttH_bestJABDToutput.category = ("(N_Jets>=5&&N_BTagsM>=4)&&(1.)","ljets_ge5j_ge4t_Reco_ttH_bestJABDToutput","")
    interf_ljets_ge5j_ge4t_Reco_ttH_bestJABDToutput.category_label = label
    interf_ljets_ge5j_ge4t_Reco_ttH_bestJABDToutput.minxval = -1.0
    interf_ljets_ge5j_ge4t_Reco_ttH_bestJABDToutput.maxxval = 0.7
    interf_ljets_ge5j_ge4t_Reco_ttH_bestJABDToutput.histotitle = "Reco_ttH_bestJABDToutput"
    interf_ljets_ge5j_ge4t_Reco_ttH_bestJABDToutput.histoname = "ljets_ge5j_ge4t_Reco_ttH_bestJABDToutput"
    interf_ljets_ge5j_ge4t_Reco_ttH_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge5j_ge4t_Reco_ttH_bestJABDToutput)
    
    interf_ljets_ge5j_ge4t_Reco_ttH_toplep_m = vhi.variableHistoInterface(variable_name  = "Reco_ttH_toplep_m",
                                            label          = "ljets_ge5j_ge4t_Reco_ttH_toplep_m",
                                            selection      = "(N_Jets>=5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge5j_ge4t_Reco_ttH_toplep_m.category = ("(N_Jets>=5&&N_BTagsM>=4)&&(1.)","ljets_ge5j_ge4t_Reco_ttH_toplep_m","")
    interf_ljets_ge5j_ge4t_Reco_ttH_toplep_m.category_label = label
    interf_ljets_ge5j_ge4t_Reco_ttH_toplep_m.minxval = -1.5
    interf_ljets_ge5j_ge4t_Reco_ttH_toplep_m.maxxval = 750.0
    interf_ljets_ge5j_ge4t_Reco_ttH_toplep_m.histotitle = "Reco_ttH_toplep_m"
    interf_ljets_ge5j_ge4t_Reco_ttH_toplep_m.histoname = "ljets_ge5j_ge4t_Reco_ttH_toplep_m"
    interf_ljets_ge5j_ge4t_Reco_ttH_toplep_m.nhistobins = 50
    interfaces.append(interf_ljets_ge5j_ge4t_Reco_ttH_toplep_m)
    
    interf_ljets_ge5j_ge4t_Reco_ttbar_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_ttbar_bestJABDToutput",
                                            label          = "ljets_ge5j_ge4t_Reco_ttbar_bestJABDToutput",
                                            selection      = "(N_Jets>=5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge5j_ge4t_Reco_ttbar_bestJABDToutput.category = ("(N_Jets>=5&&N_BTagsM>=4)&&(1.)","ljets_ge5j_ge4t_Reco_ttbar_bestJABDToutput","")
    interf_ljets_ge5j_ge4t_Reco_ttbar_bestJABDToutput.category_label = label
    interf_ljets_ge5j_ge4t_Reco_ttbar_bestJABDToutput.minxval = -0.4
    interf_ljets_ge5j_ge4t_Reco_ttbar_bestJABDToutput.maxxval = 0.7
    interf_ljets_ge5j_ge4t_Reco_ttbar_bestJABDToutput.histotitle = "Reco_ttbar_bestJABDToutput"
    interf_ljets_ge5j_ge4t_Reco_ttbar_bestJABDToutput.histoname = "ljets_ge5j_ge4t_Reco_ttbar_bestJABDToutput"
    interf_ljets_ge5j_ge4t_Reco_ttbar_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge5j_ge4t_Reco_ttbar_bestJABDToutput)
    
    interf_ljets_ge5j_ge4t_memDBp = vhi.variableHistoInterface(variable_name  = memexp,
                                            label          = "ljets_ge5j_ge4t_memDBp",
                                            selection      = "(N_Jets>=5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge5j_ge4t_memDBp.category = ("(N_Jets>=5&&N_BTagsM>=4)&&(1.)","ljets_ge5j_ge4t_memDBp","")
    interf_ljets_ge5j_ge4t_memDBp.category_label = label
    interf_ljets_ge5j_ge4t_memDBp.minxval = 0.0
    interf_ljets_ge5j_ge4t_memDBp.maxxval = 1.0
    interf_ljets_ge5j_ge4t_memDBp.histotitle = "MEM"
    interf_ljets_ge5j_ge4t_memDBp.histoname = "ljets_ge5j_ge4t_memDBp"
    interf_ljets_ge5j_ge4t_memDBp.nhistobins = 50
    interfaces.append(interf_ljets_ge5j_ge4t_memDBp)
    
    #plots = init_plots(interfaces = interfaces)
    plots = init_plots_2D(interfaces=interfaces)
    
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    
def plots_5j_ge4t(data = None):
    label = "5 jets, \geq 4 b-tags"
    interfaces = []
    selection = "(N_Jets==5&&N_BTagsM>=4)&&(1.)"


    interf_ljets_5j_ge4t_CSV_2 = vhi.variableHistoInterface(variable_name  = "CSV[2]",
                                            label          = "ljets_5j_ge4t_CSV_2",
                                            selection      = "(N_Jets==5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_5j_ge4t_CSV_2.category = ("(N_Jets==5&&N_BTagsM>=4)&&(1.)","ljets_5j_ge4t_CSV_2","")
    interf_ljets_5j_ge4t_CSV_2.category_label = label
    interf_ljets_5j_ge4t_CSV_2.minxval = 0.277
    interf_ljets_5j_ge4t_CSV_2.maxxval = 1.0
    interf_ljets_5j_ge4t_CSV_2.histotitle = "CSV[2]"
    interf_ljets_5j_ge4t_CSV_2.histoname = "ljets_5j_ge4t_CSV_2"
    interf_ljets_5j_ge4t_CSV_2.nhistobins = 50
    interfaces.append(interf_ljets_5j_ge4t_CSV_2)
    
    interf_ljets_5j_ge4t_Evt_CSV_avg = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg",
                                            label          = "ljets_5j_ge4t_Evt_CSV_avg",
                                            selection      = "(N_Jets==5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_5j_ge4t_Evt_CSV_avg.category = ("(N_Jets==5&&N_BTagsM>=4)&&(1.)","ljets_5j_ge4t_Evt_CSV_avg","")
    interf_ljets_5j_ge4t_Evt_CSV_avg.category_label = label
    interf_ljets_5j_ge4t_Evt_CSV_avg.minxval = 0.15
    interf_ljets_5j_ge4t_Evt_CSV_avg.maxxval = 1.0
    interf_ljets_5j_ge4t_Evt_CSV_avg.histotitle = "Evt_CSV_avg"
    interf_ljets_5j_ge4t_Evt_CSV_avg.histoname = "ljets_5j_ge4t_Evt_CSV_avg"
    interf_ljets_5j_ge4t_Evt_CSV_avg.nhistobins = 50
    interfaces.append(interf_ljets_5j_ge4t_Evt_CSV_avg)
    
    interf_ljets_5j_ge4t_Evt_CSV_avg_tagged = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg_tagged",
                                            label          = "ljets_5j_ge4t_Evt_CSV_avg_tagged",
                                            selection      = "(N_Jets==5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_5j_ge4t_Evt_CSV_avg_tagged.category = ("(N_Jets==5&&N_BTagsM>=4)&&(1.)","ljets_5j_ge4t_Evt_CSV_avg_tagged","")
    interf_ljets_5j_ge4t_Evt_CSV_avg_tagged.category_label = label
    interf_ljets_5j_ge4t_Evt_CSV_avg_tagged.minxval = 0.3
    interf_ljets_5j_ge4t_Evt_CSV_avg_tagged.maxxval = 1.0
    interf_ljets_5j_ge4t_Evt_CSV_avg_tagged.histotitle = "Evt_CSV_avg_tagged"
    interf_ljets_5j_ge4t_Evt_CSV_avg_tagged.histoname = "ljets_5j_ge4t_Evt_CSV_avg_tagged"
    interf_ljets_5j_ge4t_Evt_CSV_avg_tagged.nhistobins = 50
    interfaces.append(interf_ljets_5j_ge4t_Evt_CSV_avg_tagged)
    
    interf_ljets_5j_ge4t_Evt_Deta_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Deta_JetsAverage",
                                            label          = "ljets_5j_ge4t_Evt_Deta_JetsAverage",
                                            selection      = "(N_Jets==5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_5j_ge4t_Evt_Deta_JetsAverage.category = ("(N_Jets==5&&N_BTagsM>=4)&&(1.)","ljets_5j_ge4t_Evt_Deta_JetsAverage","")
    interf_ljets_5j_ge4t_Evt_Deta_JetsAverage.category_label = label
    interf_ljets_5j_ge4t_Evt_Deta_JetsAverage.minxval = 0.0
    interf_ljets_5j_ge4t_Evt_Deta_JetsAverage.maxxval = 3.0
    interf_ljets_5j_ge4t_Evt_Deta_JetsAverage.histotitle = "Evt_Deta_JetsAverage"
    interf_ljets_5j_ge4t_Evt_Deta_JetsAverage.histoname = "ljets_5j_ge4t_Evt_Deta_JetsAverage"
    interf_ljets_5j_ge4t_Evt_Deta_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_5j_ge4t_Evt_Deta_JetsAverage)
    
    interf_ljets_5j_ge4t_Evt_Deta_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Deta_TaggedJetsAverage",
                                            label          = "ljets_5j_ge4t_Evt_Deta_TaggedJetsAverage",
                                            selection      = "(N_Jets==5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_5j_ge4t_Evt_Deta_TaggedJetsAverage.category = ("(N_Jets==5&&N_BTagsM>=4)&&(1.)","ljets_5j_ge4t_Evt_Deta_TaggedJetsAverage","")
    interf_ljets_5j_ge4t_Evt_Deta_TaggedJetsAverage.category_label = label
    interf_ljets_5j_ge4t_Evt_Deta_TaggedJetsAverage.minxval = 0.0
    interf_ljets_5j_ge4t_Evt_Deta_TaggedJetsAverage.maxxval = 3.0
    interf_ljets_5j_ge4t_Evt_Deta_TaggedJetsAverage.histotitle = "Evt_Deta_TaggedJetsAverage"
    interf_ljets_5j_ge4t_Evt_Deta_TaggedJetsAverage.histoname = "ljets_5j_ge4t_Evt_Deta_TaggedJetsAverage"
    interf_ljets_5j_ge4t_Evt_Deta_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_5j_ge4t_Evt_Deta_TaggedJetsAverage)
    
    interf_ljets_5j_ge4t_Evt_HT_tags = vhi.variableHistoInterface(variable_name  = "Evt_HT_tags",
                                            label          = "ljets_5j_ge4t_Evt_HT_tags",
                                            selection      = "(N_Jets==5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_5j_ge4t_Evt_HT_tags.category = ("(N_Jets==5&&N_BTagsM>=4)&&(1.)","ljets_5j_ge4t_Evt_HT_tags","")
    interf_ljets_5j_ge4t_Evt_HT_tags.category_label = label
    interf_ljets_5j_ge4t_Evt_HT_tags.minxval = 100.0
    interf_ljets_5j_ge4t_Evt_HT_tags.maxxval = 1000.0
    interf_ljets_5j_ge4t_Evt_HT_tags.histotitle = "Evt_HT_tags"
    interf_ljets_5j_ge4t_Evt_HT_tags.histoname = "ljets_5j_ge4t_Evt_HT_tags"
    interf_ljets_5j_ge4t_Evt_HT_tags.nhistobins = 50
    interfaces.append(interf_ljets_5j_ge4t_Evt_HT_tags)
    
    interf_ljets_5j_ge4t_Evt_M2_minDrTaggedJets = vhi.variableHistoInterface(variable_name  = "Evt_M2_minDrTaggedJets",
                                            label          = "ljets_5j_ge4t_Evt_M2_minDrTaggedJets",
                                            selection      = "(N_Jets==5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_5j_ge4t_Evt_M2_minDrTaggedJets.category = ("(N_Jets==5&&N_BTagsM>=4)&&(1.)","ljets_5j_ge4t_Evt_M2_minDrTaggedJets","")
    interf_ljets_5j_ge4t_Evt_M2_minDrTaggedJets.category_label = label
    interf_ljets_5j_ge4t_Evt_M2_minDrTaggedJets.minxval = 0.0
    interf_ljets_5j_ge4t_Evt_M2_minDrTaggedJets.maxxval = 400.0
    interf_ljets_5j_ge4t_Evt_M2_minDrTaggedJets.histotitle = "M_{2}( min #DeltaR(tag,tag) )"
    interf_ljets_5j_ge4t_Evt_M2_minDrTaggedJets.histoname = "ljets_5j_ge4t_Evt_M2_minDrTaggedJets"
    interf_ljets_5j_ge4t_Evt_M2_minDrTaggedJets.nhistobins = 50
    interfaces.append(interf_ljets_5j_ge4t_Evt_M2_minDrTaggedJets)
    
    interf_ljets_5j_ge4t_Evt_M_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_M_TaggedJetsAverage",
                                            label          = "ljets_5j_ge4t_Evt_M_TaggedJetsAverage",
                                            selection      = "(N_Jets==5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_5j_ge4t_Evt_M_TaggedJetsAverage.category = ("(N_Jets==5&&N_BTagsM>=4)&&(1.)","ljets_5j_ge4t_Evt_M_TaggedJetsAverage","")
    interf_ljets_5j_ge4t_Evt_M_TaggedJetsAverage.category_label = label
    interf_ljets_5j_ge4t_Evt_M_TaggedJetsAverage.minxval = 5.0
    interf_ljets_5j_ge4t_Evt_M_TaggedJetsAverage.maxxval = 70.0
    interf_ljets_5j_ge4t_Evt_M_TaggedJetsAverage.histotitle = "Evt_M_TaggedJetsAverage"
    interf_ljets_5j_ge4t_Evt_M_TaggedJetsAverage.histoname = "ljets_5j_ge4t_Evt_M_TaggedJetsAverage"
    interf_ljets_5j_ge4t_Evt_M_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_5j_ge4t_Evt_M_TaggedJetsAverage)
    
    interf_ljets_5j_ge4t_Evt_Pt_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Pt_JetsAverage",
                                            label          = "ljets_5j_ge4t_Evt_Pt_JetsAverage",
                                            selection      = "(N_Jets==5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_5j_ge4t_Evt_Pt_JetsAverage.category = ("(N_Jets==5&&N_BTagsM>=4)&&(1.)","ljets_5j_ge4t_Evt_Pt_JetsAverage","")
    interf_ljets_5j_ge4t_Evt_Pt_JetsAverage.category_label = label
    interf_ljets_5j_ge4t_Evt_Pt_JetsAverage.minxval = 30.0
    interf_ljets_5j_ge4t_Evt_Pt_JetsAverage.maxxval = 500.0
    interf_ljets_5j_ge4t_Evt_Pt_JetsAverage.histotitle = "Evt_Pt_JetsAverage"
    interf_ljets_5j_ge4t_Evt_Pt_JetsAverage.histoname = "ljets_5j_ge4t_Evt_Pt_JetsAverage"
    interf_ljets_5j_ge4t_Evt_Pt_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_5j_ge4t_Evt_Pt_JetsAverage)
    
    interf_ljets_5j_ge4t_Evt_Pt_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Pt_TaggedJetsAverage",
                                            label          = "ljets_5j_ge4t_Evt_Pt_TaggedJetsAverage",
                                            selection      = "(N_Jets==5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_5j_ge4t_Evt_Pt_TaggedJetsAverage.category = ("(N_Jets==5&&N_BTagsM>=4)&&(1.)","ljets_5j_ge4t_Evt_Pt_TaggedJetsAverage","")
    interf_ljets_5j_ge4t_Evt_Pt_TaggedJetsAverage.category_label = label
    interf_ljets_5j_ge4t_Evt_Pt_TaggedJetsAverage.minxval = 30.0
    interf_ljets_5j_ge4t_Evt_Pt_TaggedJetsAverage.maxxval = 600.0
    interf_ljets_5j_ge4t_Evt_Pt_TaggedJetsAverage.histotitle = "Evt_Pt_TaggedJetsAverage"
    interf_ljets_5j_ge4t_Evt_Pt_TaggedJetsAverage.histoname = "ljets_5j_ge4t_Evt_Pt_TaggedJetsAverage"
    interf_ljets_5j_ge4t_Evt_Pt_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_5j_ge4t_Evt_Pt_TaggedJetsAverage)
    
    interf_ljets_5j_ge4t_Evt_Pt_minDrTaggedJets = vhi.variableHistoInterface(variable_name  = "Evt_Pt_minDrTaggedJets",
                                            label          = "ljets_5j_ge4t_Evt_Pt_minDrTaggedJets",
                                            selection      = "(N_Jets==5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_5j_ge4t_Evt_Pt_minDrTaggedJets.category = ("(N_Jets==5&&N_BTagsM>=4)&&(1.)","ljets_5j_ge4t_Evt_Pt_minDrTaggedJets","")
    interf_ljets_5j_ge4t_Evt_Pt_minDrTaggedJets.category_label = label
    interf_ljets_5j_ge4t_Evt_Pt_minDrTaggedJets.minxval = 20.0
    interf_ljets_5j_ge4t_Evt_Pt_minDrTaggedJets.maxxval = 600.0
    interf_ljets_5j_ge4t_Evt_Pt_minDrTaggedJets.histotitle = "Evt_Pt_minDrTaggedJets"
    interf_ljets_5j_ge4t_Evt_Pt_minDrTaggedJets.histoname = "ljets_5j_ge4t_Evt_Pt_minDrTaggedJets"
    interf_ljets_5j_ge4t_Evt_Pt_minDrTaggedJets.nhistobins = 50
    interfaces.append(interf_ljets_5j_ge4t_Evt_Pt_minDrTaggedJets)
    
    interf_ljets_5j_ge4t_Evt_blr_transformed = vhi.variableHistoInterface(variable_name  = "Evt_blr_transformed",
                                            label          = "ljets_5j_ge4t_Evt_blr_transformed",
                                            selection      = "(N_Jets==5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_5j_ge4t_Evt_blr_transformed.category = ("(N_Jets==5&&N_BTagsM>=4)&&(1.)","ljets_5j_ge4t_Evt_blr_transformed","")
    interf_ljets_5j_ge4t_Evt_blr_transformed.category_label = label
    interf_ljets_5j_ge4t_Evt_blr_transformed.minxval = -2.5
    interf_ljets_5j_ge4t_Evt_blr_transformed.maxxval = 15.0
    interf_ljets_5j_ge4t_Evt_blr_transformed.histotitle = "Evt_blr_transformed"
    interf_ljets_5j_ge4t_Evt_blr_transformed.histoname = "ljets_5j_ge4t_Evt_blr_transformed"
    interf_ljets_5j_ge4t_Evt_blr_transformed.nhistobins = 50
    interfaces.append(interf_ljets_5j_ge4t_Evt_blr_transformed)
    
    interf_ljets_5j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_Jet_CSV_btop",
                                            label          = "ljets_5j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop",
                                            selection      = "(N_Jets==5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_5j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.category = ("(N_Jets==5&&N_BTagsM>=4)&&(1.)","ljets_5j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop","")
    interf_ljets_5j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.category_label = label
    interf_ljets_5j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.minxval = -1.5
    interf_ljets_5j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.maxxval = 1.0
    interf_ljets_5j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.histotitle = "Reco_JABDT_tHW_Jet_CSV_btop"
    interf_ljets_5j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.histoname = "ljets_5j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop"
    interf_ljets_5j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.nhistobins = 50
    interfaces.append(interf_ljets_5j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop)
    
    interf_ljets_5j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",
                                            label          = "ljets_5j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",
                                            selection      = "(N_Jets==5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_5j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.category = ("(N_Jets==5&&N_BTagsM>=4)&&(1.)","ljets_5j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt","")
    interf_ljets_5j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.category_label = label
    interf_ljets_5j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.minxval = -1.5
    interf_ljets_5j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.maxxval = 1.0
    interf_ljets_5j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.histotitle = "Reco_JABDT_tHW_energy_fraction"
    interf_ljets_5j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.histoname = "ljets_5j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt"
    interf_ljets_5j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.nhistobins = 50
    interfaces.append(interf_ljets_5j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt)
    
    interf_ljets_5j_ge4t_Reco_JABDT_tHq_abs_ljet_eta = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHq_abs_ljet_eta",
                                            label          = "ljets_5j_ge4t_Reco_JABDT_tHq_abs_ljet_eta",
                                            selection      = "(N_Jets==5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_5j_ge4t_Reco_JABDT_tHq_abs_ljet_eta.category = ("(N_Jets==5&&N_BTagsM>=4)&&(1.)","ljets_5j_ge4t_Reco_JABDT_tHq_abs_ljet_eta","")
    interf_ljets_5j_ge4t_Reco_JABDT_tHq_abs_ljet_eta.category_label = label
    interf_ljets_5j_ge4t_Reco_JABDT_tHq_abs_ljet_eta.minxval = -1.5
    interf_ljets_5j_ge4t_Reco_JABDT_tHq_abs_ljet_eta.maxxval = 4.5
    interf_ljets_5j_ge4t_Reco_JABDT_tHq_abs_ljet_eta.histotitle = "Reco_JABDT_tHq_abs_ljet_eta"
    interf_ljets_5j_ge4t_Reco_JABDT_tHq_abs_ljet_eta.histoname = "ljets_5j_ge4t_Reco_JABDT_tHq_abs_ljet_eta"
    interf_ljets_5j_ge4t_Reco_JABDT_tHq_abs_ljet_eta.nhistobins = 50
    interfaces.append(interf_ljets_5j_ge4t_Reco_JABDT_tHq_abs_ljet_eta)
    
    interf_ljets_5j_ge4t_Reco_tHq_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_tHq_bestJABDToutput",
                                            label          = "ljets_5j_ge4t_Reco_tHq_bestJABDToutput",
                                            selection      = "(N_Jets==5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_5j_ge4t_Reco_tHq_bestJABDToutput.category = ("(N_Jets==5&&N_BTagsM>=4)&&(1.)","ljets_5j_ge4t_Reco_tHq_bestJABDToutput","")
    interf_ljets_5j_ge4t_Reco_tHq_bestJABDToutput.category_label = label
    interf_ljets_5j_ge4t_Reco_tHq_bestJABDToutput.minxval = -1.0
    interf_ljets_5j_ge4t_Reco_tHq_bestJABDToutput.maxxval = 0.7
    interf_ljets_5j_ge4t_Reco_tHq_bestJABDToutput.histotitle = "Reco_tHq_bestJABDToutput"
    interf_ljets_5j_ge4t_Reco_tHq_bestJABDToutput.histoname = "ljets_5j_ge4t_Reco_tHq_bestJABDToutput"
    interf_ljets_5j_ge4t_Reco_tHq_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_5j_ge4t_Reco_tHq_bestJABDToutput)
    
    interf_ljets_5j_ge4t_Reco_ttH_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_ttH_bestJABDToutput",
                                            label          = "ljets_5j_ge4t_Reco_ttH_bestJABDToutput",
                                            selection      = "(N_Jets==5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_5j_ge4t_Reco_ttH_bestJABDToutput.category = ("(N_Jets==5&&N_BTagsM>=4)&&(1.)","ljets_5j_ge4t_Reco_ttH_bestJABDToutput","")
    interf_ljets_5j_ge4t_Reco_ttH_bestJABDToutput.category_label = label
    interf_ljets_5j_ge4t_Reco_ttH_bestJABDToutput.minxval = -1.0
    interf_ljets_5j_ge4t_Reco_ttH_bestJABDToutput.maxxval = 0.7
    interf_ljets_5j_ge4t_Reco_ttH_bestJABDToutput.histotitle = "Reco_ttH_bestJABDToutput"
    interf_ljets_5j_ge4t_Reco_ttH_bestJABDToutput.histoname = "ljets_5j_ge4t_Reco_ttH_bestJABDToutput"
    interf_ljets_5j_ge4t_Reco_ttH_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_5j_ge4t_Reco_ttH_bestJABDToutput)
    
    interf_ljets_5j_ge4t_Reco_ttH_toplep_m = vhi.variableHistoInterface(variable_name  = "Reco_ttH_toplep_m",
                                            label          = "ljets_5j_ge4t_Reco_ttH_toplep_m",
                                            selection      = "(N_Jets==5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_5j_ge4t_Reco_ttH_toplep_m.category = ("(N_Jets==5&&N_BTagsM>=4)&&(1.)","ljets_5j_ge4t_Reco_ttH_toplep_m","")
    interf_ljets_5j_ge4t_Reco_ttH_toplep_m.category_label = label
    interf_ljets_5j_ge4t_Reco_ttH_toplep_m.minxval = -1.5
    interf_ljets_5j_ge4t_Reco_ttH_toplep_m.maxxval = 750.0
    interf_ljets_5j_ge4t_Reco_ttH_toplep_m.histotitle = "Reco_ttH_toplep_m"
    interf_ljets_5j_ge4t_Reco_ttH_toplep_m.histoname = "ljets_5j_ge4t_Reco_ttH_toplep_m"
    interf_ljets_5j_ge4t_Reco_ttH_toplep_m.nhistobins = 50
    interfaces.append(interf_ljets_5j_ge4t_Reco_ttH_toplep_m)
    
    interf_ljets_5j_ge4t_Reco_ttbar_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_ttbar_bestJABDToutput",
                                            label          = "ljets_5j_ge4t_Reco_ttbar_bestJABDToutput",
                                            selection      = "(N_Jets==5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_5j_ge4t_Reco_ttbar_bestJABDToutput.category = ("(N_Jets==5&&N_BTagsM>=4)&&(1.)","ljets_5j_ge4t_Reco_ttbar_bestJABDToutput","")
    interf_ljets_5j_ge4t_Reco_ttbar_bestJABDToutput.category_label = label
    interf_ljets_5j_ge4t_Reco_ttbar_bestJABDToutput.minxval = -0.4
    interf_ljets_5j_ge4t_Reco_ttbar_bestJABDToutput.maxxval = 0.7
    interf_ljets_5j_ge4t_Reco_ttbar_bestJABDToutput.histotitle = "Reco_ttbar_bestJABDToutput"
    interf_ljets_5j_ge4t_Reco_ttbar_bestJABDToutput.histoname = "ljets_5j_ge4t_Reco_ttbar_bestJABDToutput"
    interf_ljets_5j_ge4t_Reco_ttbar_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_5j_ge4t_Reco_ttbar_bestJABDToutput)
    
    interf_ljets_5j_ge4t_memDBp = vhi.variableHistoInterface(variable_name  = memexp,
                                            label          = "ljets_5j_ge4t_memDBp",
                                            selection      = "(N_Jets==5&&N_BTagsM>=4)&&(1.)")
    interf_ljets_5j_ge4t_memDBp.category = ("(N_Jets==5&&N_BTagsM>=4)&&(1.)","ljets_5j_ge4t_memDBp","")
    interf_ljets_5j_ge4t_memDBp.category_label = label
    interf_ljets_5j_ge4t_memDBp.minxval = 0.0
    interf_ljets_5j_ge4t_memDBp.maxxval = 1.0
    interf_ljets_5j_ge4t_memDBp.histotitle = "MEM"
    interf_ljets_5j_ge4t_memDBp.histoname = "ljets_5j_ge4t_memDBp"
    interf_ljets_5j_ge4t_memDBp.nhistobins = 50
    interfaces.append(interf_ljets_5j_ge4t_memDBp)
    
    #plots = init_plots(interfaces = interfaces) 
    plots = init_plots_2D(interfaces=interfaces)
   
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    
def plots_ge6j_ge4t(data = None):
    label = "\geq 6 jets, \geq 4 b-tags"
    interfaces = []
    selection = "(N_Jets>=6&&N_BTagsM>=4)&&(1.)"


    interf_ljets_ge6j_ge4t_CSV_2 = vhi.variableHistoInterface(variable_name  = "CSV[2]",
                                            label          = "ljets_ge6j_ge4t_CSV_2",
                                            selection      = "(N_Jets>=6&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge6j_ge4t_CSV_2.category = ("(N_Jets>=6&&N_BTagsM>=4)&&(1.)","ljets_ge6j_ge4t_CSV_2","")
    interf_ljets_ge6j_ge4t_CSV_2.category_label = label
    interf_ljets_ge6j_ge4t_CSV_2.minxval = 0.277
    interf_ljets_ge6j_ge4t_CSV_2.maxxval = 1.0
    interf_ljets_ge6j_ge4t_CSV_2.histotitle = "CSV[2]"
    interf_ljets_ge6j_ge4t_CSV_2.histoname = "ljets_ge6j_ge4t_CSV_2"
    interf_ljets_ge6j_ge4t_CSV_2.nhistobins = 50
    interfaces.append(interf_ljets_ge6j_ge4t_CSV_2)
    
    interf_ljets_ge6j_ge4t_Evt_CSV_avg = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg",
                                            label          = "ljets_ge6j_ge4t_Evt_CSV_avg",
                                            selection      = "(N_Jets>=6&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge6j_ge4t_Evt_CSV_avg.category = ("(N_Jets>=6&&N_BTagsM>=4)&&(1.)","ljets_ge6j_ge4t_Evt_CSV_avg","")
    interf_ljets_ge6j_ge4t_Evt_CSV_avg.category_label = label
    interf_ljets_ge6j_ge4t_Evt_CSV_avg.minxval = 0.15
    interf_ljets_ge6j_ge4t_Evt_CSV_avg.maxxval = 1.0
    interf_ljets_ge6j_ge4t_Evt_CSV_avg.histotitle = "Evt_CSV_avg"
    interf_ljets_ge6j_ge4t_Evt_CSV_avg.histoname = "ljets_ge6j_ge4t_Evt_CSV_avg"
    interf_ljets_ge6j_ge4t_Evt_CSV_avg.nhistobins = 50
    interfaces.append(interf_ljets_ge6j_ge4t_Evt_CSV_avg)
    
    interf_ljets_ge6j_ge4t_Evt_CSV_avg_tagged = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg_tagged",
                                            label          = "ljets_ge6j_ge4t_Evt_CSV_avg_tagged",
                                            selection      = "(N_Jets>=6&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge6j_ge4t_Evt_CSV_avg_tagged.category = ("(N_Jets>=6&&N_BTagsM>=4)&&(1.)","ljets_ge6j_ge4t_Evt_CSV_avg_tagged","")
    interf_ljets_ge6j_ge4t_Evt_CSV_avg_tagged.category_label = label
    interf_ljets_ge6j_ge4t_Evt_CSV_avg_tagged.minxval = 0.3
    interf_ljets_ge6j_ge4t_Evt_CSV_avg_tagged.maxxval = 1.0
    interf_ljets_ge6j_ge4t_Evt_CSV_avg_tagged.histotitle = "Evt_CSV_avg_tagged"
    interf_ljets_ge6j_ge4t_Evt_CSV_avg_tagged.histoname = "ljets_ge6j_ge4t_Evt_CSV_avg_tagged"
    interf_ljets_ge6j_ge4t_Evt_CSV_avg_tagged.nhistobins = 50
    interfaces.append(interf_ljets_ge6j_ge4t_Evt_CSV_avg_tagged)
    
    interf_ljets_ge6j_ge4t_Evt_Deta_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Deta_JetsAverage",
                                            label          = "ljets_ge6j_ge4t_Evt_Deta_JetsAverage",
                                            selection      = "(N_Jets>=6&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge6j_ge4t_Evt_Deta_JetsAverage.category = ("(N_Jets>=6&&N_BTagsM>=4)&&(1.)","ljets_ge6j_ge4t_Evt_Deta_JetsAverage","")
    interf_ljets_ge6j_ge4t_Evt_Deta_JetsAverage.category_label = label
    interf_ljets_ge6j_ge4t_Evt_Deta_JetsAverage.minxval = 0.0
    interf_ljets_ge6j_ge4t_Evt_Deta_JetsAverage.maxxval = 3.0
    interf_ljets_ge6j_ge4t_Evt_Deta_JetsAverage.histotitle = "Evt_Deta_JetsAverage"
    interf_ljets_ge6j_ge4t_Evt_Deta_JetsAverage.histoname = "ljets_ge6j_ge4t_Evt_Deta_JetsAverage"
    interf_ljets_ge6j_ge4t_Evt_Deta_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge6j_ge4t_Evt_Deta_JetsAverage)
    
    interf_ljets_ge6j_ge4t_Evt_Deta_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Deta_TaggedJetsAverage",
                                            label          = "ljets_ge6j_ge4t_Evt_Deta_TaggedJetsAverage",
                                            selection      = "(N_Jets>=6&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge6j_ge4t_Evt_Deta_TaggedJetsAverage.category = ("(N_Jets>=6&&N_BTagsM>=4)&&(1.)","ljets_ge6j_ge4t_Evt_Deta_TaggedJetsAverage","")
    interf_ljets_ge6j_ge4t_Evt_Deta_TaggedJetsAverage.category_label = label
    interf_ljets_ge6j_ge4t_Evt_Deta_TaggedJetsAverage.minxval = 0.0
    interf_ljets_ge6j_ge4t_Evt_Deta_TaggedJetsAverage.maxxval = 3.0
    interf_ljets_ge6j_ge4t_Evt_Deta_TaggedJetsAverage.histotitle = "Evt_Deta_TaggedJetsAverage"
    interf_ljets_ge6j_ge4t_Evt_Deta_TaggedJetsAverage.histoname = "ljets_ge6j_ge4t_Evt_Deta_TaggedJetsAverage"
    interf_ljets_ge6j_ge4t_Evt_Deta_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge6j_ge4t_Evt_Deta_TaggedJetsAverage)
    
    interf_ljets_ge6j_ge4t_Evt_HT_tags = vhi.variableHistoInterface(variable_name  = "Evt_HT_tags",
                                            label          = "ljets_ge6j_ge4t_Evt_HT_tags",
                                            selection      = "(N_Jets>=6&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge6j_ge4t_Evt_HT_tags.category = ("(N_Jets>=6&&N_BTagsM>=4)&&(1.)","ljets_ge6j_ge4t_Evt_HT_tags","")
    interf_ljets_ge6j_ge4t_Evt_HT_tags.category_label = label
    interf_ljets_ge6j_ge4t_Evt_HT_tags.minxval = 100.0
    interf_ljets_ge6j_ge4t_Evt_HT_tags.maxxval = 1000.0
    interf_ljets_ge6j_ge4t_Evt_HT_tags.histotitle = "Evt_HT_tags"
    interf_ljets_ge6j_ge4t_Evt_HT_tags.histoname = "ljets_ge6j_ge4t_Evt_HT_tags"
    interf_ljets_ge6j_ge4t_Evt_HT_tags.nhistobins = 50
    interfaces.append(interf_ljets_ge6j_ge4t_Evt_HT_tags)
    
    interf_ljets_ge6j_ge4t_Evt_M2_minDrTaggedJets = vhi.variableHistoInterface(variable_name  = "Evt_M2_minDrTaggedJets",
                                            label          = "ljets_ge6j_ge4t_Evt_M2_minDrTaggedJets",
                                            selection      = "(N_Jets>=6&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge6j_ge4t_Evt_M2_minDrTaggedJets.category = ("(N_Jets>=6&&N_BTagsM>=4)&&(1.)","ljets_ge6j_ge4t_Evt_M2_minDrTaggedJets","")
    interf_ljets_ge6j_ge4t_Evt_M2_minDrTaggedJets.category_label = label
    interf_ljets_ge6j_ge4t_Evt_M2_minDrTaggedJets.minxval = 0.0
    interf_ljets_ge6j_ge4t_Evt_M2_minDrTaggedJets.maxxval = 400.0
    interf_ljets_ge6j_ge4t_Evt_M2_minDrTaggedJets.histotitle = "M_{2}( min #DeltaR(tag,tag) )"
    interf_ljets_ge6j_ge4t_Evt_M2_minDrTaggedJets.histoname = "ljets_ge6j_ge4t_Evt_M2_minDrTaggedJets"
    interf_ljets_ge6j_ge4t_Evt_M2_minDrTaggedJets.nhistobins = 50
    interfaces.append(interf_ljets_ge6j_ge4t_Evt_M2_minDrTaggedJets)
    
    interf_ljets_ge6j_ge4t_Evt_M_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_M_TaggedJetsAverage",
                                            label          = "ljets_ge6j_ge4t_Evt_M_TaggedJetsAverage",
                                            selection      = "(N_Jets>=6&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge6j_ge4t_Evt_M_TaggedJetsAverage.category = ("(N_Jets>=6&&N_BTagsM>=4)&&(1.)","ljets_ge6j_ge4t_Evt_M_TaggedJetsAverage","")
    interf_ljets_ge6j_ge4t_Evt_M_TaggedJetsAverage.category_label = label
    interf_ljets_ge6j_ge4t_Evt_M_TaggedJetsAverage.minxval = 5.0
    interf_ljets_ge6j_ge4t_Evt_M_TaggedJetsAverage.maxxval = 70.0
    interf_ljets_ge6j_ge4t_Evt_M_TaggedJetsAverage.histotitle = "Evt_M_TaggedJetsAverage"
    interf_ljets_ge6j_ge4t_Evt_M_TaggedJetsAverage.histoname = "ljets_ge6j_ge4t_Evt_M_TaggedJetsAverage"
    interf_ljets_ge6j_ge4t_Evt_M_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge6j_ge4t_Evt_M_TaggedJetsAverage)
    
    interf_ljets_ge6j_ge4t_Evt_Pt_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Pt_JetsAverage",
                                            label          = "ljets_ge6j_ge4t_Evt_Pt_JetsAverage",
                                            selection      = "(N_Jets>=6&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge6j_ge4t_Evt_Pt_JetsAverage.category = ("(N_Jets>=6&&N_BTagsM>=4)&&(1.)","ljets_ge6j_ge4t_Evt_Pt_JetsAverage","")
    interf_ljets_ge6j_ge4t_Evt_Pt_JetsAverage.category_label = label
    interf_ljets_ge6j_ge4t_Evt_Pt_JetsAverage.minxval = 30.0
    interf_ljets_ge6j_ge4t_Evt_Pt_JetsAverage.maxxval = 500.0
    interf_ljets_ge6j_ge4t_Evt_Pt_JetsAverage.histotitle = "Evt_Pt_JetsAverage"
    interf_ljets_ge6j_ge4t_Evt_Pt_JetsAverage.histoname = "ljets_ge6j_ge4t_Evt_Pt_JetsAverage"
    interf_ljets_ge6j_ge4t_Evt_Pt_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge6j_ge4t_Evt_Pt_JetsAverage)
    
    interf_ljets_ge6j_ge4t_Evt_Pt_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Pt_TaggedJetsAverage",
                                            label          = "ljets_ge6j_ge4t_Evt_Pt_TaggedJetsAverage",
                                            selection      = "(N_Jets>=6&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge6j_ge4t_Evt_Pt_TaggedJetsAverage.category = ("(N_Jets>=6&&N_BTagsM>=4)&&(1.)","ljets_ge6j_ge4t_Evt_Pt_TaggedJetsAverage","")
    interf_ljets_ge6j_ge4t_Evt_Pt_TaggedJetsAverage.category_label = label
    interf_ljets_ge6j_ge4t_Evt_Pt_TaggedJetsAverage.minxval = 30.0
    interf_ljets_ge6j_ge4t_Evt_Pt_TaggedJetsAverage.maxxval = 600.0
    interf_ljets_ge6j_ge4t_Evt_Pt_TaggedJetsAverage.histotitle = "Evt_Pt_TaggedJetsAverage"
    interf_ljets_ge6j_ge4t_Evt_Pt_TaggedJetsAverage.histoname = "ljets_ge6j_ge4t_Evt_Pt_TaggedJetsAverage"
    interf_ljets_ge6j_ge4t_Evt_Pt_TaggedJetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge6j_ge4t_Evt_Pt_TaggedJetsAverage)
    
    interf_ljets_ge6j_ge4t_Evt_Pt_minDrTaggedJets = vhi.variableHistoInterface(variable_name  = "Evt_Pt_minDrTaggedJets",
                                            label          = "ljets_ge6j_ge4t_Evt_Pt_minDrTaggedJets",
                                            selection      = "(N_Jets>=6&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge6j_ge4t_Evt_Pt_minDrTaggedJets.category = ("(N_Jets>=6&&N_BTagsM>=4)&&(1.)","ljets_ge6j_ge4t_Evt_Pt_minDrTaggedJets","")
    interf_ljets_ge6j_ge4t_Evt_Pt_minDrTaggedJets.category_label = label
    interf_ljets_ge6j_ge4t_Evt_Pt_minDrTaggedJets.minxval = 20.0
    interf_ljets_ge6j_ge4t_Evt_Pt_minDrTaggedJets.maxxval = 600.0
    interf_ljets_ge6j_ge4t_Evt_Pt_minDrTaggedJets.histotitle = "Evt_Pt_minDrTaggedJets"
    interf_ljets_ge6j_ge4t_Evt_Pt_minDrTaggedJets.histoname = "ljets_ge6j_ge4t_Evt_Pt_minDrTaggedJets"
    interf_ljets_ge6j_ge4t_Evt_Pt_minDrTaggedJets.nhistobins = 50
    interfaces.append(interf_ljets_ge6j_ge4t_Evt_Pt_minDrTaggedJets)
    
    interf_ljets_ge6j_ge4t_Evt_blr_transformed = vhi.variableHistoInterface(variable_name  = "Evt_blr_transformed",
                                            label          = "ljets_ge6j_ge4t_Evt_blr_transformed",
                                            selection      = "(N_Jets>=6&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge6j_ge4t_Evt_blr_transformed.category = ("(N_Jets>=6&&N_BTagsM>=4)&&(1.)","ljets_ge6j_ge4t_Evt_blr_transformed","")
    interf_ljets_ge6j_ge4t_Evt_blr_transformed.category_label = label
    interf_ljets_ge6j_ge4t_Evt_blr_transformed.minxval = -2.5
    interf_ljets_ge6j_ge4t_Evt_blr_transformed.maxxval = 15.0
    interf_ljets_ge6j_ge4t_Evt_blr_transformed.histotitle = "Evt_blr_transformed"
    interf_ljets_ge6j_ge4t_Evt_blr_transformed.histoname = "ljets_ge6j_ge4t_Evt_blr_transformed"
    interf_ljets_ge6j_ge4t_Evt_blr_transformed.nhistobins = 50
    interfaces.append(interf_ljets_ge6j_ge4t_Evt_blr_transformed)
    
    interf_ljets_ge6j_ge4t_N_Jets = vhi.variableHistoInterface(variable_name  = "N_Jets",
                                            label          = "ljets_ge6j_ge4t_N_Jets",
                                            selection      = "(N_Jets>=6&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge6j_ge4t_N_Jets.category = ("(N_Jets>=6&&N_BTagsM>=4)&&(1.)","ljets_ge6j_ge4t_N_Jets","")
    interf_ljets_ge6j_ge4t_N_Jets.category_label = label
    interf_ljets_ge6j_ge4t_N_Jets.minxval = 3.5
    interf_ljets_ge6j_ge4t_N_Jets.maxxval = 10.5
    interf_ljets_ge6j_ge4t_N_Jets.histotitle = "N_Jets"
    interf_ljets_ge6j_ge4t_N_Jets.histoname = "ljets_ge6j_ge4t_N_Jets"
    interf_ljets_ge6j_ge4t_N_Jets.nhistobins = 7
    interfaces.append(interf_ljets_ge6j_ge4t_N_Jets)
    
    interf_ljets_ge6j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_Jet_CSV_btop",
                                            label          = "ljets_ge6j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop",
                                            selection      = "(N_Jets>=6&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge6j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.category = ("(N_Jets>=6&&N_BTagsM>=4)&&(1.)","ljets_ge6j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop","")
    interf_ljets_ge6j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.category_label = label
    interf_ljets_ge6j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.minxval = -1.5
    interf_ljets_ge6j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.maxxval = 1.0
    interf_ljets_ge6j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.histotitle = "Reco_JABDT_tHW_Jet_CSV_btop"
    interf_ljets_ge6j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.histoname = "ljets_ge6j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop"
    interf_ljets_ge6j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop.nhistobins = 50
    interfaces.append(interf_ljets_ge6j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop)
    
    interf_ljets_ge6j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",
                                            label          = "ljets_ge6j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",
                                            selection      = "(N_Jets>=6&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge6j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.category = ("(N_Jets>=6&&N_BTagsM>=4)&&(1.)","ljets_ge6j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt","")
    interf_ljets_ge6j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.category_label = label
    interf_ljets_ge6j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.minxval = -1.5
    interf_ljets_ge6j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.maxxval = 1.0
    interf_ljets_ge6j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.histotitle = "Reco_JABDT_tHW_energy_fraction"
    interf_ljets_ge6j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.histoname = "ljets_ge6j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt"
    interf_ljets_ge6j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt.nhistobins = 50
    interfaces.append(interf_ljets_ge6j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt)
    
    interf_ljets_ge6j_ge4t_Reco_JABDT_tHq_abs_ljet_eta = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHq_abs_ljet_eta",
                                            label          = "ljets_ge6j_ge4t_Reco_JABDT_tHq_abs_ljet_eta",
                                            selection      = "(N_Jets>=6&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge6j_ge4t_Reco_JABDT_tHq_abs_ljet_eta.category = ("(N_Jets>=6&&N_BTagsM>=4)&&(1.)","ljets_ge6j_ge4t_Reco_JABDT_tHq_abs_ljet_eta","")
    interf_ljets_ge6j_ge4t_Reco_JABDT_tHq_abs_ljet_eta.category_label = label
    interf_ljets_ge6j_ge4t_Reco_JABDT_tHq_abs_ljet_eta.minxval = -1.5
    interf_ljets_ge6j_ge4t_Reco_JABDT_tHq_abs_ljet_eta.maxxval = 4.5
    interf_ljets_ge6j_ge4t_Reco_JABDT_tHq_abs_ljet_eta.histotitle = "Reco_JABDT_tHq_abs_ljet_eta"
    interf_ljets_ge6j_ge4t_Reco_JABDT_tHq_abs_ljet_eta.histoname = "ljets_ge6j_ge4t_Reco_JABDT_tHq_abs_ljet_eta"
    interf_ljets_ge6j_ge4t_Reco_JABDT_tHq_abs_ljet_eta.nhistobins = 50
    interfaces.append(interf_ljets_ge6j_ge4t_Reco_JABDT_tHq_abs_ljet_eta)
    
    interf_ljets_ge6j_ge4t_Reco_tHq_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_tHq_bestJABDToutput",
                                            label          = "ljets_ge6j_ge4t_Reco_tHq_bestJABDToutput",
                                            selection      = "(N_Jets>=6&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge6j_ge4t_Reco_tHq_bestJABDToutput.category = ("(N_Jets>=6&&N_BTagsM>=4)&&(1.)","ljets_ge6j_ge4t_Reco_tHq_bestJABDToutput","")
    interf_ljets_ge6j_ge4t_Reco_tHq_bestJABDToutput.category_label = label
    interf_ljets_ge6j_ge4t_Reco_tHq_bestJABDToutput.minxval = -1.0
    interf_ljets_ge6j_ge4t_Reco_tHq_bestJABDToutput.maxxval = 0.7
    interf_ljets_ge6j_ge4t_Reco_tHq_bestJABDToutput.histotitle = "Reco_tHq_bestJABDToutput"
    interf_ljets_ge6j_ge4t_Reco_tHq_bestJABDToutput.histoname = "ljets_ge6j_ge4t_Reco_tHq_bestJABDToutput"
    interf_ljets_ge6j_ge4t_Reco_tHq_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge6j_ge4t_Reco_tHq_bestJABDToutput)
    
    interf_ljets_ge6j_ge4t_Reco_ttH_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_ttH_bestJABDToutput",
                                            label          = "ljets_ge6j_ge4t_Reco_ttH_bestJABDToutput",
                                            selection      = "(N_Jets>=6&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge6j_ge4t_Reco_ttH_bestJABDToutput.category = ("(N_Jets>=6&&N_BTagsM>=4)&&(1.)","ljets_ge6j_ge4t_Reco_ttH_bestJABDToutput","")
    interf_ljets_ge6j_ge4t_Reco_ttH_bestJABDToutput.category_label = label
    interf_ljets_ge6j_ge4t_Reco_ttH_bestJABDToutput.minxval = -1.0
    interf_ljets_ge6j_ge4t_Reco_ttH_bestJABDToutput.maxxval = 0.7
    interf_ljets_ge6j_ge4t_Reco_ttH_bestJABDToutput.histotitle = "Reco_ttH_bestJABDToutput"
    interf_ljets_ge6j_ge4t_Reco_ttH_bestJABDToutput.histoname = "ljets_ge6j_ge4t_Reco_ttH_bestJABDToutput"
    interf_ljets_ge6j_ge4t_Reco_ttH_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge6j_ge4t_Reco_ttH_bestJABDToutput)
    
    interf_ljets_ge6j_ge4t_Reco_ttH_toplep_m = vhi.variableHistoInterface(variable_name  = "Reco_ttH_toplep_m",
                                            label          = "ljets_ge6j_ge4t_Reco_ttH_toplep_m",
                                            selection      = "(N_Jets>=6&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge6j_ge4t_Reco_ttH_toplep_m.category = ("(N_Jets>=6&&N_BTagsM>=4)&&(1.)","ljets_ge6j_ge4t_Reco_ttH_toplep_m","")
    interf_ljets_ge6j_ge4t_Reco_ttH_toplep_m.category_label = label
    interf_ljets_ge6j_ge4t_Reco_ttH_toplep_m.minxval = -1.5
    interf_ljets_ge6j_ge4t_Reco_ttH_toplep_m.maxxval = 750.0
    interf_ljets_ge6j_ge4t_Reco_ttH_toplep_m.histotitle = "Reco_ttH_toplep_m"
    interf_ljets_ge6j_ge4t_Reco_ttH_toplep_m.histoname = "ljets_ge6j_ge4t_Reco_ttH_toplep_m"
    interf_ljets_ge6j_ge4t_Reco_ttH_toplep_m.nhistobins = 50
    interfaces.append(interf_ljets_ge6j_ge4t_Reco_ttH_toplep_m)
    
    interf_ljets_ge6j_ge4t_Reco_ttbar_bestJABDToutput = vhi.variableHistoInterface(variable_name  = "Reco_ttbar_bestJABDToutput",
                                            label          = "ljets_ge6j_ge4t_Reco_ttbar_bestJABDToutput",
                                            selection      = "(N_Jets>=6&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge6j_ge4t_Reco_ttbar_bestJABDToutput.category = ("(N_Jets>=6&&N_BTagsM>=4)&&(1.)","ljets_ge6j_ge4t_Reco_ttbar_bestJABDToutput","")
    interf_ljets_ge6j_ge4t_Reco_ttbar_bestJABDToutput.category_label = label
    interf_ljets_ge6j_ge4t_Reco_ttbar_bestJABDToutput.minxval = -0.4
    interf_ljets_ge6j_ge4t_Reco_ttbar_bestJABDToutput.maxxval = 0.7
    interf_ljets_ge6j_ge4t_Reco_ttbar_bestJABDToutput.histotitle = "Reco_ttbar_bestJABDToutput"
    interf_ljets_ge6j_ge4t_Reco_ttbar_bestJABDToutput.histoname = "ljets_ge6j_ge4t_Reco_ttbar_bestJABDToutput"
    interf_ljets_ge6j_ge4t_Reco_ttbar_bestJABDToutput.nhistobins = 50
    interfaces.append(interf_ljets_ge6j_ge4t_Reco_ttbar_bestJABDToutput)
    
    interf_ljets_ge6j_ge4t_memDBp = vhi.variableHistoInterface(variable_name  = memexp,
                                            label          = "ljets_ge6j_ge4t_memDBp",
                                            selection      = "(N_Jets>=6&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge6j_ge4t_memDBp.category = ("(N_Jets>=6&&N_BTagsM>=4)&&(1.)","ljets_ge6j_ge4t_memDBp","")
    interf_ljets_ge6j_ge4t_memDBp.category_label = label
    interf_ljets_ge6j_ge4t_memDBp.minxval = 0.0
    interf_ljets_ge6j_ge4t_memDBp.maxxval = 1.0
    interf_ljets_ge6j_ge4t_memDBp.histotitle = "MEM"
    interf_ljets_ge6j_ge4t_memDBp.histoname = "ljets_ge6j_ge4t_memDBp"
    interf_ljets_ge6j_ge4t_memDBp.nhistobins = 50
    interfaces.append(interf_ljets_ge6j_ge4t_memDBp)
    
    #plots = init_plots(interfaces = interfaces)    
    plots = init_plots_2D(interfaces=interfaces)
    if data:
        add_data_plots(plots=plots,data=data)
    return plots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_ge5j_ge4t(data)
    discriminatorPlots += plots_5j_ge4t(data)
    discriminatorPlots += plots_ge6j_ge4t(data)

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
    
