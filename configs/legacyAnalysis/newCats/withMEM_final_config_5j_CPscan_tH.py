
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


memexp = '(memDBp>=0.0)*(memDBp)+(memDBp<0.0)*(0.01)+(memDBp==1.0)*(0.01)'

def getDNNclass(cla):
    return "((N_Jets==5&&N_BTagsM>=4)*(DNNPredictedClass_5j_ge4t_classification=={}) + ((N_Jets>=6&&N_BTagsM>=4)*(DNNPredictedClass_ge6j_ge4t_classification=={})) )".format(cla, cla)

def getDNNoutput(cla):
    return "((N_Jets==5&&N_BTagsM>=4)*(DNNOutput_5j_ge4t_classification_node_{}) + ((N_Jets>=6&&N_BTagsM>=4)*(DNNOutput_ge6j_ge4t_classification_node_{})) )".format(cla, cla)

def crosscheck_variables(data = None, selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)", name = "ge4j_ge4t"):
    interfaces = []
    label = name
    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_{}_N_Jets".format(name),"N_Jets",7,3.5,10.5),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_{}_N_BTagsM".format(name),"N_BTagsM",7,3.5,10.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_{}_Evt_HT_tags".format(name),"Evt_HT_tags",50,100.0,1000.0),"Evt_HT_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_{}_Evt_HT_jets".format(name),"H_{T}(jets)",50,200.0,1500.0),"Evt_HT_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_{}_memDBp".format(name),"MEM",50,-2.,1.0),memexp,selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_{}_Evt_Pt_minDrTaggedJets".format(name),"Evt_Pt_minDrTaggedJets",50,0.0,800.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_{}_Evt_Dr_minDrTaggedJets".format(name),"Evt_Dr_minDrTaggedJets",30,0,4.0),"Evt_Dr_minDrTaggedJets",selection,label),
    ]

    # for i in range(4):
    #     plots += [        
    #     plotClasses.Plot(ROOT.TH1D("ljets_{}_TaggedJet_Pt_{}".format(name, i),"TaggedJet_Pt_{}".format(i),50,20.0,600.0),
    #                         "TaggedJet_Pt[{}]".format(i),selection,label),
    #     plotClasses.Plot(ROOT.TH1D("ljets_{}_TaggedJet_Eta_{}".format(name, i),"TaggedJet_Eta_{}".format(i),50,-5,5),
    #                         "TaggedJet_Eta[{}]".format(i),selection,label),
    #     ]
        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots


def plots_dnn(data, discrname, jt_selection, jt_label):

    ndefaultbins = 50
    interfaces = []

    interf_classification_ttH_ttmb_node = vhi.variableHistoInterface(variable_name  = "(" + getDNNoutput("ttH") + "/ (" + getDNNoutput("ttH") + "+" + getDNNoutput("ttmb") + "+" + getDNNoutput("tt2b") + "))" ,
                                            label          = "ljets_"+jt_label+"_classification_ttH_ttmb_vs_slike",
                                            selection      = "()" )
    interf_classification_ttH_ttmb_node.category = ("((" + getDNNclass(0) + "||" + getDNNclass(1) + ")" + "&&(" + jt_selection +"))","ljets_"+jt_label+"_classification_ttH_ttmb_node","")
    interf_classification_ttH_ttmb_node.category_label = jt_label
    interf_classification_ttH_ttmb_node.minxval = 0.0
    interf_classification_ttH_ttmb_node.maxxval = 1.0
    interf_classification_ttH_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_classification_ttH_ttmb_node)

    interf_classification_ttH_node = vhi.variableHistoInterface(variable_name  =  getDNNoutput("ttH") ,
                                            label          = "ljets_"+jt_label+"_classification_ttH_node",
                                            selection      = "()" )
    interf_classification_ttH_node.category = ("((" + getDNNclass(0) + ")" + "&&(" + jt_selection +"))","ljets_"+jt_label+"_classification_ttH__node","")
    interf_classification_ttH_node.category_label = jt_label
    interf_classification_ttH_node.minxval = 0.0
    interf_classification_ttH_node.maxxval = 1.0
    interf_classification_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_classification_ttH_node)

    interf_classification_ttmb_node = vhi.variableHistoInterface(variable_name  =  getDNNoutput("ttmb") ,
                                            label          = "ljets_"+jt_label+"_classification_ttmb_node",
                                            selection      = "()" )
    interf_classification_ttmb_node.category = ("((" + getDNNclass(1) + ")" + "&&(" + jt_selection +"))","ljets_"+jt_label+"_classification_ttH__node","")
    interf_classification_ttmb_node.category_label = jt_label
    interf_classification_ttmb_node.minxval = 0.0
    interf_classification_ttmb_node.maxxval = 1.0
    interf_classification_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_classification_ttmb_node)

    interf_classification_tt2b_node = vhi.variableHistoInterface(variable_name  = getDNNoutput("tt2b"),
                                            label          = "ljets_"+jt_label+"_classification_tt2b_node",
                                            selection      = "()" )
    interf_classification_tt2b_node.category = ("(" + getDNNclass(2) + "&&(" + jt_selection +"))","ljets_"+jt_label+"_classification_tt2b_node","")
    interf_classification_tt2b_node.category_label = jt_label
    interf_classification_tt2b_node.minxval = 0.0
    interf_classification_tt2b_node.maxxval = 1.0
    interf_classification_tt2b_node.nhistobins = 1
    interfaces.append(interf_classification_tt2b_node)


    interf_classification_ttcc_node = vhi.variableHistoInterface(variable_name  = getDNNoutput("ttcc"),
                                            label          = "ljets_"+jt_label+"_classification_ttcc_node",
                                            selection      = "()" )
    interf_classification_ttcc_node.category = ("(" + getDNNclass(3) + "&&(" + jt_selection +"))","ljets_"+jt_label+"_classification_ttcc_node","")
    interf_classification_ttcc_node.category_label = jt_label
    interf_classification_ttcc_node.minxval = 0.0
    interf_classification_ttcc_node.maxxval = 1.0
    interf_classification_ttcc_node.nhistobins = 1
    interfaces.append(interf_classification_ttcc_node)


    interf_classification_ttlf_node = vhi.variableHistoInterface(variable_name  = getDNNoutput("ttlf"),
                                            label          = "ljets_"+jt_label+"_classification_ttlf_node",
                                            selection      = "()" )
    interf_classification_ttlf_node.category = ("(" + getDNNclass(4) + "&&(" + jt_selection +"))","ljets_"+jt_label+"_classification_ttlf_node","")
    interf_classification_ttlf_node.category_label = jt_label
    interf_classification_ttlf_node.minxval = 0.0
    interf_classification_ttlf_node.maxxval = 1.0
    interf_classification_ttlf_node.nhistobins = 1
    interfaces.append(interf_classification_ttlf_node)

    interf_classification_tHq_node = vhi.variableHistoInterface(variable_name  = getDNNoutput("tHq"),
                                            label          = "ljets_"+jt_label+"_classification_tHq_node",
                                            selection      = "()" )
    interf_classification_tHq_node.category = ("(" + getDNNclass(5) + "&&(" + jt_selection +"))","ljets_"+jt_label+"_classification_tHq_node","")
    interf_classification_tHq_node.category_label = jt_label
    interf_classification_tHq_node.minxval = 0.0
    interf_classification_tHq_node.maxxval = 1.0
    interf_classification_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_classification_tHq_node)

    interf_classification_tHW_node = vhi.variableHistoInterface(variable_name  = getDNNoutput("tHW"),
                                            label          = "ljets_"+jt_label+"_classification_tHW_node",
                                            selection      = "()" )
    interf_classification_tHW_node.category = ("(" + getDNNclass(6) + "&&(" + jt_selection +"))","ljets_"+jt_label+"_classification_tHW_node","")
    interf_classification_tHW_node.category_label = jt_label
    interf_classification_tHW_node.minxval = 0.0
    interf_classification_tHW_node.maxxval = 1.0
    interf_classification_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_classification_tHW_node)

    for interf in interfaces:
        l = interf.label
        interf.histoname = discrname+"_"+l if not discrname == "" else l 
        interf.histotitle = "final discriminator ({})".format(l)
        interf.selection = interf.category[0] 

    DNNPlots = init_plots_CPScan(interfaces = interfaces, data = data)
    return DNNPlots

def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_dnn(data, discrname, "(N_Jets==5&&N_BTagsM>=4)", "5j_ge4t")
    discriminatorPlots += plots_dnn(data, discrname, "(N_Jets>=6&&N_BTagsM>=4)", "ge6j_ge4t")

    # discriminatorPlots += crosscheck_variables(data, "(N_Jets==5&&N_BTagsM>=4)", "5j_ge4t")
    # discriminatorPlots += crosscheck_variables(data, "(N_Jets>=5&&N_BTagsM>=4)", "ge5j_ge4t")
    # discriminatorPlots += crosscheck_variables(data, "(N_Jets>=6&&N_BTagsM>=4)", "ge6j_ge4t")

    return discriminatorPlots

def init_plots_CPScan(interfaces, data = None, discrname = ''):
    plots = [] #init list of plotClasses objects to return
    for interf in interfaces:
        # check if initialization uses bin edges or min/max vals
        # if 'subdict' contains the keyword 'bin_edges', an array
        # of type float is created from the corresponding python list.
        # Else, the min/maxvals are used
        # float points
        points = [1,2,4,5]
        ptype  = "CPfloat" 
        
        for i in points:
            histoname = "P"+str(i)+'_'+discrname+"_"+interf.label
            histotitle = interf.histotitle
            weight = "*(weight_{}_{}/Weight_GEN_nom)".format(ptype, i)

            if not interf.bin_edges is None:
                bins  = array("f", interf.bin_edges)
                nbins = len(bins)-1 # last bin edge in array is overflow bin => subtract for nbins
                interf.nhistobins = nbins # update number of bins
                plots.append(
                    plotClasses.Plot(
                        histo = ROOT.TH1F(histoname,histotitle,nbins,bins),
                        variable = interf.varname,
                        selection = interf.selection + weight,
                        label= interf.category_label))
            elif not (interf.minxval is None or interf.maxxval is None):
                nbins = interf.nhistobins
                xmax  = interf.maxxval
                xmin  = interf.minxval
                plots.append(
                    plotClasses.Plot(
                        histo = ROOT.TH1F(histoname,histotitle,nbins,xmin, xmax),
                        variable = interf.varname,
                        selection = interf.selection + weight,
                        label = interf.category_label))
            else:
                print("FATAL ERROR: Unable to load bin edges or min/max values for histogram!")
                print(interf)
                raise ValueError
    if data:
        add_data_plots(plots=plots,data=data)
    return plots


def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
    
