
import sys
import os
filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = os.path.dirname(filedir)
basedir = os.path.dirname(pyrootdir)
sys.path.append(pyrootdir)
sys.path.append(basedir)

import util.tools.plotClasses as plotClasses
import ROOT
from array import array
from copy import deepcopy


memexp = ""
jtYieldExpression = "(N_Jets==4&&N_BTagsM==3)*1"
jtYieldExpression+="+(N_Jets==5&&N_BTagsM==3)*2"
jtYieldExpression+="+(N_Jets>=6&&N_BTagsM==3)*3"
jtYieldExpression+="+(N_Jets==4&&N_BTagsM>=4)*4"
jtYieldExpression+="+(N_Jets==5&&N_BTagsM>=4)*5"
jtYieldExpression+="+(N_Jets>=6&&N_BTagsM>=4)*6"


def yields(data = None):
    label = "\geq 4 jets, \geq 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=3)&&(1.)"
    plots = [
        plotClasses.Plot(ROOT.TH1D("inclusive_eventYields","event yields",6,0.5,6.5),jtYieldExpression,selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_yield","event yield",1,0,1),"0.5",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",40,20.0,250.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        ]

    label = "\geq 4 jets, \geq 3 b-tags (sideband)"
    selection = "(N_Jets>=4&&N_BTagsM>=3)&&(Evt_M2_closestTo91TaggedJets<=70.||Evt_M2_closestTo91TaggedJets>=110.)"
    plots += [
        plotClasses.Plot(ROOT.TH1D("sideband_eventYields","event yields",6,0.5,6.5),jtYieldExpression,selection,label),
        plotClasses.Plot(ROOT.TH1D("sideband_yield","event yield",1,0,1),"0.5",selection,label),
        plotClasses.Plot(ROOT.TH1D("sideband_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",40,20.0,250.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        ]
    if data:
        add_data_plots(plots=plots,data=data)
    return plots



def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += yields(data)

    return discriminatorPlots


def translateName(name):
    name = name.replace("ljets_","")
    name = name.replace("ge6j_ge3t_","")
    name = name.replace("ge4j_ge3t_","")
    name = name.replace("ge4j_3t_","")
    name = name.replace("ge4j_ge4t_","")
    name = name.replace("4j_ge3t_","")
    name = name.replace("le5j_ge3t_","")
    name = name.replace("5j_ge3t_","")

    name = name.replace("ttZ_","t#bar{t}+Z ")
    name = name.replace("ttH_","t#bar{t}+H ")
    name = name.replace("ttbb_","t#bar{t}+b#bar{b} ")
    name = name.replace("ttlf_","t#bar{t}+lf ")
    name = name.replace("ttcc_","t#bar{t}+c#bar{c} ")
    return name

def init_plots(dictionary, data = None):
    plots = [] #init list of plotClasses objects to return
    for label in dictionary:
        subdict     = dictionary[label] #for easy access
        discr       = subdict["discr"] # load discriminator name
        sel         = subdict["plotPreselections"] # load selection
        histoname   = subdict["histoname"] # load histogram name
        histotitle  = subdict["histotitle"] # load histogram title
        catlabel    = subdict["catlabel"] # category label

        # check if initialization uses bin edges or min/max vals
        # if 'subdict' contains the keyword 'bin_edges', an array
        # of type float is created from the corresponding python list.
        # Else, the min/maxvals are used 
        if "bin_edges" in subdict:
            bins  = array("f", subdict["bin_edges"])
            nbins = len(bins)-1 # last bin edge in array is overflow bin => subtract for nbins
            subdict["nhistobins"] = nbins # update number of bins
            plots.append(
                plotClasses.Plot(
                    ROOT.TH1F(histoname,histotitle,nbins,bins),
                    discr,sel,catlabel))

        elif "minxval" in subdict and "maxxval" in subdict:
            nbins = subdict["nhistobins"]
            xmax  = subdict["maxxval"]
            xmin  = subdict["minxval"]
            plots.append(
                plotClasses.Plot(
                    ROOT.TH1F(histoname, histotitle,nbins,xmin, xmax),
                    discr,sel,catlabel))

    if not data is None:
        data.categories.update(dictionary)

    return plots

def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
    
