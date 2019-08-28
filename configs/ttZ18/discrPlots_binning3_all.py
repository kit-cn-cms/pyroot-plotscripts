
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



def plots_dnn(data, discrname):

    ndefaultbins = 14
    category_dict = {}
    this_dict = {}




    # plots for ge4j_ge4t_4NodeDNN

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge4t_4NodeDNN==0))","ljets_ge4j_ge4t_4NodeDNN_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_4NodeDNN_node_ttZ"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2219,
				0.3342,
				0.4465,
				0.5588,
				0.615,
				0.6712,
				0.7273,
				0.7835,
				0.8396,
				0.8958,
				0.98
				]
    this_dict["ljets_ge4j_ge4t_4NodeDNN_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge4t_4NodeDNN==1))","ljets_ge4j_ge4t_4NodeDNN_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_4NodeDNN_node_tthf"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2238,
				0.4331,
				0.5377,
				0.6423,
				0.7469,
				0.93
				]
    this_dict["ljets_ge4j_ge4t_4NodeDNN_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge4t_4NodeDNN==2))","ljets_ge4j_ge4t_4NodeDNN_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_4NodeDNN_node_ttcc"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2358,
				0.62
				]
    this_dict["ljets_ge4j_ge4t_4NodeDNN_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge4t_4NodeDNN==3))","ljets_ge4j_ge4t_4NodeDNN_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_4NodeDNN_node_ttlf"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2285,
				0.81
				]
    this_dict["ljets_ge4j_ge4t_4NodeDNN_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge4j_ge4t_5NodeDNN

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge4t_5NodeDNN==0))","ljets_ge4j_ge4t_5NodeDNN_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_5NodeDNN_node_ttZ"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1719,
				0.2842,
				0.3965,
				0.5088,
				0.565,
				0.6212,
				0.6773,
				0.7335,
				0.7896,
				0.8458,
				0.93
				]
    this_dict["ljets_ge4j_ge4t_5NodeDNN_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge4t_5NodeDNN==1))","ljets_ge4j_ge4t_5NodeDNN_ttmb_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_5NodeDNN_node_ttmb"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1777,
				0.3562,
				0.4454,
				0.5346,
				0.6238,
				0.78
				]
    this_dict["ljets_ge4j_ge4t_5NodeDNN_ttmb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge4t_5NodeDNN==2))","ljets_ge4j_ge4t_5NodeDNN_tt2b_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_5NodeDNN_node_tt2b"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1838,
				0.3131,
				0.3777,
				0.4423,
				0.5069,
				0.62
				]
    this_dict["ljets_ge4j_ge4t_5NodeDNN_tt2b_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge4t_5NodeDNN==3))","ljets_ge4j_ge4t_5NodeDNN_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_5NodeDNN_node_ttcc"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1862,
				0.56
				]
    this_dict["ljets_ge4j_ge4t_5NodeDNN_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge4t_5NodeDNN==4))","ljets_ge4j_ge4t_5NodeDNN_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_5NodeDNN_node_ttlf"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1808,
				0.7
				]
    this_dict["ljets_ge4j_ge4t_5NodeDNN_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge4j_ge4t_ttHNodeDNN

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge4t_ttHNodeDNN==0))","ljets_ge4j_ge4t_ttHNodeDNN_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_ttHNodeDNN_node_ttZ"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1785,
				0.2646,
				0.3508,
				0.4369,
				0.48,
				0.5231,
				0.5662,
				0.6092,
				0.6523,
				0.6954,
				0.76
				]
    this_dict["ljets_ge4j_ge4t_ttHNodeDNN_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge4t_ttHNodeDNN==1))","ljets_ge4j_ge4t_ttHNodeDNN_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_ttHNodeDNN_node_ttH"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1808,
				0.3346,
				0.4115,
				0.4885,
				0.5654,
				0.7
				]
    this_dict["ljets_ge4j_ge4t_ttHNodeDNN_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge4t_ttHNodeDNN==2))","ljets_ge4j_ge4t_ttHNodeDNN_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_ttHNodeDNN_node_tthf"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1738,
				0.3831,
				0.4877,
				0.5923,
				0.6969,
				0.88
				]
    this_dict["ljets_ge4j_ge4t_ttHNodeDNN_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge4t_ttHNodeDNN==3))","ljets_ge4j_ge4t_ttHNodeDNN_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_ttHNodeDNN_node_ttcc"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1827,
				0.65
				]
    this_dict["ljets_ge4j_ge4t_ttHNodeDNN_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge4t_ttHNodeDNN==4))","ljets_ge4j_ge4t_ttHNodeDNN_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_ttHNodeDNN_node_ttlf"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1808,
				0.7
				]
    this_dict["ljets_ge4j_ge4t_ttHNodeDNN_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge6j_ge3t_4NodeDNN

    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge6j_ge3t_4NodeDNN==0))","ljets_ge6j_ge3t_4NodeDNN_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_4NodeDNN_node_ttZ"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2227,
				0.3319,
				0.4412,
				0.5504,
				0.605,
				0.6596,
				0.7142,
				0.7688,
				0.8235,
				0.8781,
				0.96
				]
    this_dict["ljets_ge6j_ge3t_4NodeDNN_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge6j_ge3t_4NodeDNN==1))","ljets_ge6j_ge3t_4NodeDNN_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_4NodeDNN_node_tthf"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2277,
				0.4062,
				0.4954,
				0.5846,
				0.6738,
				0.83
				]
    this_dict["ljets_ge6j_ge3t_4NodeDNN_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge6j_ge3t_4NodeDNN==2))","ljets_ge6j_ge3t_4NodeDNN_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_4NodeDNN_node_ttcc"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2365,
				0.6
				]
    this_dict["ljets_ge6j_ge3t_4NodeDNN_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge6j_ge3t_4NodeDNN==3))","ljets_ge6j_ge3t_4NodeDNN_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_4NodeDNN_node_ttlf"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2315,
				0.73
				]
    this_dict["ljets_ge6j_ge3t_4NodeDNN_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge6j_ge3t_5NodeDNN

    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge6j_ge3t_5NodeDNN==0))","ljets_ge6j_ge3t_5NodeDNN_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_5NodeDNN_node_ttZ"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1719,
				0.2842,
				0.3965,
				0.5088,
				0.565,
				0.6212,
				0.6773,
				0.7335,
				0.7896,
				0.8458,
				0.93
				]
    this_dict["ljets_ge6j_ge3t_5NodeDNN_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge6j_ge3t_5NodeDNN==1))","ljets_ge6j_ge3t_5NodeDNN_ttmb_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_5NodeDNN_node_ttmb"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1815,
				0.3292,
				0.4031,
				0.4769,
				0.5508,
				0.68
				]
    this_dict["ljets_ge6j_ge3t_5NodeDNN_ttmb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge6j_ge3t_5NodeDNN==2))","ljets_ge6j_ge3t_5NodeDNN_tt2b_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_5NodeDNN_node_tt2b"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1738,
				0.3831,
				0.4877,
				0.5923,
				0.6969,
				0.88
				]
    this_dict["ljets_ge6j_ge3t_5NodeDNN_tt2b_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge6j_ge3t_5NodeDNN==3))","ljets_ge6j_ge3t_5NodeDNN_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_5NodeDNN_node_ttcc"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1869,
				0.54
				]
    this_dict["ljets_ge6j_ge3t_5NodeDNN_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge6j_ge3t_5NodeDNN==4))","ljets_ge6j_ge3t_5NodeDNN_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_5NodeDNN_node_ttlf"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1835,
				0.63
				]
    this_dict["ljets_ge6j_ge3t_5NodeDNN_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge6j_ge3t_ttHNodeDNN

    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge6j_ge3t_ttHNodeDNN==0))","ljets_ge6j_ge3t_ttHNodeDNN_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_ttHNodeDNN_node_ttZ"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1754,
				0.2738,
				0.3723,
				0.4708,
				0.52,
				0.5692,
				0.6185,
				0.6677,
				0.7169,
				0.7662,
				0.84
				]
    this_dict["ljets_ge6j_ge3t_ttHNodeDNN_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge6j_ge3t_ttHNodeDNN==1))","ljets_ge6j_ge3t_ttHNodeDNN_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_ttHNodeDNN_node_ttH"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1796,
				0.3427,
				0.4242,
				0.5058,
				0.5873,
				0.73
				]
    this_dict["ljets_ge6j_ge3t_ttHNodeDNN_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge6j_ge3t_ttHNodeDNN==2))","ljets_ge6j_ge3t_ttHNodeDNN_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_ttHNodeDNN_node_tthf"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.175,
				0.375,
				0.475,
				0.575,
				0.675,
				0.85
				]
    this_dict["ljets_ge6j_ge3t_ttHNodeDNN_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge6j_ge3t_ttHNodeDNN==3))","ljets_ge6j_ge3t_ttHNodeDNN_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_ttHNodeDNN_node_ttcc"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.185,
				0.59
				]
    this_dict["ljets_ge6j_ge3t_ttHNodeDNN_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge6j_ge3t_ttHNodeDNN==4))","ljets_ge6j_ge3t_ttHNodeDNN_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_ttHNodeDNN_node_ttlf"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1819,
				0.67
				]
    this_dict["ljets_ge6j_ge3t_ttHNodeDNN_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for le5j_ge3t_4NodeDNN

    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_le5j_ge3t_4NodeDNN==0))","ljets_le5j_ge3t_4NodeDNN_ttZ_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_4NodeDNN_node_ttZ"
    category_dict["catlabel"] = "\leq 5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2212,
				0.3365,
				0.4519,
				0.5673,
				0.625,
				0.6827,
				0.7404,
				0.7981,
				0.8558,
				0.9135,
				1.0
				]
    this_dict["ljets_le5j_ge3t_4NodeDNN_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_le5j_ge3t_4NodeDNN==1))","ljets_le5j_ge3t_4NodeDNN_tthf_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_4NodeDNN_node_tthf"
    category_dict["catlabel"] = "\leq 5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2265,
				0.4142,
				0.5081,
				0.6019,
				0.6958,
				0.86
				]
    this_dict["ljets_le5j_ge3t_4NodeDNN_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_le5j_ge3t_4NodeDNN==2))","ljets_le5j_ge3t_4NodeDNN_ttcc_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_4NodeDNN_node_ttcc"
    category_dict["catlabel"] = "\leq 5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2362,
				0.61
				]
    this_dict["ljets_le5j_ge3t_4NodeDNN_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_le5j_ge3t_4NodeDNN==3))","ljets_le5j_ge3t_4NodeDNN_ttlf_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_4NodeDNN_node_ttlf"
    category_dict["catlabel"] = "\leq 5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2292,
				0.79
				]
    this_dict["ljets_le5j_ge3t_4NodeDNN_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for le5j_ge3t_5NodeDNN

    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_le5j_ge3t_5NodeDNN==0))","ljets_le5j_ge3t_5NodeDNN_ttZ_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_5NodeDNN_node_ttZ"
    category_dict["catlabel"] = "\leq 5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1692,
				0.2923,
				0.4154,
				0.5385,
				0.6,
				0.6615,
				0.7231,
				0.7846,
				0.8462,
				0.9077,
				1.0
				]
    this_dict["ljets_le5j_ge3t_5NodeDNN_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_le5j_ge3t_5NodeDNN==1))","ljets_le5j_ge3t_5NodeDNN_ttmb_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_5NodeDNN_node_ttmb"
    category_dict["catlabel"] = "\leq 5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.185,
				0.305,
				0.365,
				0.425,
				0.485,
				0.59
				]
    this_dict["ljets_le5j_ge3t_5NodeDNN_ttmb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_le5j_ge3t_5NodeDNN==2))","ljets_le5j_ge3t_5NodeDNN_tt2b_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_5NodeDNN_node_tt2b"
    category_dict["catlabel"] = "\leq 5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1715,
				0.3992,
				0.5131,
				0.6269,
				0.7408,
				0.94
				]
    this_dict["ljets_le5j_ge3t_5NodeDNN_tt2b_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_le5j_ge3t_5NodeDNN==3))","ljets_le5j_ge3t_5NodeDNN_ttcc_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_5NodeDNN_node_ttcc"
    category_dict["catlabel"] = "\leq 5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1885,
				0.5
				]
    this_dict["ljets_le5j_ge3t_5NodeDNN_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_le5j_ge3t_5NodeDNN==4))","ljets_le5j_ge3t_5NodeDNN_ttlf_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_5NodeDNN_node_ttlf"
    category_dict["catlabel"] = "\leq 5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1692,
				1.0
				]
    this_dict["ljets_le5j_ge3t_5NodeDNN_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for le5j_ge3t_ttHNodeDNN

    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_le5j_ge3t_ttHNodeDNN==0))","ljets_le5j_ge3t_ttHNodeDNN_ttZ_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_ttHNodeDNN_node_ttZ"
    category_dict["catlabel"] = "\leq 5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1754,
				0.2738,
				0.3723,
				0.4708,
				0.52,
				0.5692,
				0.6185,
				0.6677,
				0.7169,
				0.7662,
				0.84
				]
    this_dict["ljets_le5j_ge3t_ttHNodeDNN_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_le5j_ge3t_ttHNodeDNN==1))","ljets_le5j_ge3t_ttHNodeDNN_ttH_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_ttHNodeDNN_node_ttH"
    category_dict["catlabel"] = "\leq 5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1804,
				0.3373,
				0.4158,
				0.4942,
				0.5727,
				0.71
				]
    this_dict["ljets_le5j_ge3t_ttHNodeDNN_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_le5j_ge3t_ttHNodeDNN==2))","ljets_le5j_ge3t_ttHNodeDNN_tthf_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_ttHNodeDNN_node_tthf"
    category_dict["catlabel"] = "\leq 5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1742,
				0.3804,
				0.4835,
				0.5865,
				0.6896,
				0.87
				]
    this_dict["ljets_le5j_ge3t_ttHNodeDNN_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_le5j_ge3t_ttHNodeDNN==3))","ljets_le5j_ge3t_ttHNodeDNN_ttcc_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_ttHNodeDNN_node_ttcc"
    category_dict["catlabel"] = "\leq 5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1865,
				0.55
				]
    this_dict["ljets_le5j_ge3t_ttHNodeDNN_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_le5j_ge3t_ttHNodeDNN==4))","ljets_le5j_ge3t_ttHNodeDNN_ttlf_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_ttHNodeDNN_node_ttlf"
    category_dict["catlabel"] = "\leq 5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1715,
				0.94
				]
    this_dict["ljets_le5j_ge3t_ttHNodeDNN_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for 5j_ge3t_4NodeDNN

    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_5j_ge3t_4NodeDNN==0))","ljets_5j_ge3t_4NodeDNN_ttZ_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_4NodeDNN_node_ttZ"
    category_dict["catlabel"] = "5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2215,
				0.3354,
				0.4492,
				0.5631,
				0.62,
				0.6769,
				0.7338,
				0.7908,
				0.8477,
				0.9046,
				0.99
				]
    this_dict["ljets_5j_ge3t_4NodeDNN_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_5j_ge3t_4NodeDNN==1))","ljets_5j_ge3t_4NodeDNN_tthf_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_4NodeDNN_node_tthf"
    category_dict["catlabel"] = "5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2277,
				0.4062,
				0.4954,
				0.5846,
				0.6738,
				0.83
				]
    this_dict["ljets_5j_ge3t_4NodeDNN_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_5j_ge3t_4NodeDNN==2))","ljets_5j_ge3t_4NodeDNN_ttcc_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_4NodeDNN_node_ttcc"
    category_dict["catlabel"] = "5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2392,
				0.53
				]
    this_dict["ljets_5j_ge3t_4NodeDNN_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_5j_ge3t_4NodeDNN==3))","ljets_5j_ge3t_4NodeDNN_ttlf_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_4NodeDNN_node_ttlf"
    category_dict["catlabel"] = "5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2312,
				0.74
				]
    this_dict["ljets_5j_ge3t_4NodeDNN_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for 5j_ge3t_5NodeDNN

    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_5j_ge3t_5NodeDNN==0))","ljets_5j_ge3t_5NodeDNN_ttZ_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_5NodeDNN_node_ttZ"
    category_dict["catlabel"] = "5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1712,
				0.2865,
				0.4019,
				0.5173,
				0.575,
				0.6327,
				0.6904,
				0.7481,
				0.8058,
				0.8635,
				0.95
				]
    this_dict["ljets_5j_ge3t_5NodeDNN_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_5j_ge3t_5NodeDNN==1))","ljets_5j_ge3t_5NodeDNN_ttmb_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_5NodeDNN_node_ttmb"
    category_dict["catlabel"] = "5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1819,
				0.3265,
				0.3988,
				0.4712,
				0.5435,
				0.67
				]
    this_dict["ljets_5j_ge3t_5NodeDNN_ttmb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_5j_ge3t_5NodeDNN==2))","ljets_5j_ge3t_5NodeDNN_tt2b_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_5NodeDNN_node_tt2b"
    category_dict["catlabel"] = "5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1781,
				0.3535,
				0.4412,
				0.5288,
				0.6165,
				0.77
				]
    this_dict["ljets_5j_ge3t_5NodeDNN_tt2b_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_5j_ge3t_5NodeDNN==3))","ljets_5j_ge3t_5NodeDNN_ttcc_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_5NodeDNN_node_ttcc"
    category_dict["catlabel"] = "5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1896,
				0.47
				]
    this_dict["ljets_5j_ge3t_5NodeDNN_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_5j_ge3t_5NodeDNN==4))","ljets_5j_ge3t_5NodeDNN_ttlf_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_5NodeDNN_node_ttlf"
    category_dict["catlabel"] = "5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1823,
				0.66
				]
    this_dict["ljets_5j_ge3t_5NodeDNN_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for 5j_ge3t_ttHNodeDNN

    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_5j_ge3t_ttHNodeDNN==0))","ljets_5j_ge3t_ttHNodeDNN_ttZ_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_ttHNodeDNN_node_ttZ"
    category_dict["catlabel"] = "5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.175,
				0.275,
				0.375,
				0.475,
				0.525,
				0.575,
				0.625,
				0.675,
				0.725,
				0.775,
				0.85
				]
    this_dict["ljets_5j_ge3t_ttHNodeDNN_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_5j_ge3t_ttHNodeDNN==1))","ljets_5j_ge3t_ttHNodeDNN_ttH_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_ttHNodeDNN_node_ttH"
    category_dict["catlabel"] = "5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1804,
				0.3373,
				0.4158,
				0.4942,
				0.5727,
				0.71
				]
    this_dict["ljets_5j_ge3t_ttHNodeDNN_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_5j_ge3t_ttHNodeDNN==2))","ljets_5j_ge3t_ttHNodeDNN_tthf_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_ttHNodeDNN_node_tthf"
    category_dict["catlabel"] = "5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1754,
				0.3723,
				0.4708,
				0.5692,
				0.6677,
				0.84
				]
    this_dict["ljets_5j_ge3t_ttHNodeDNN_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_5j_ge3t_ttHNodeDNN==3))","ljets_5j_ge3t_ttHNodeDNN_ttcc_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_ttHNodeDNN_node_ttcc"
    category_dict["catlabel"] = "5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1869,
				0.54
				]
    this_dict["ljets_5j_ge3t_ttHNodeDNN_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_5j_ge3t_ttHNodeDNN==4))","ljets_5j_ge3t_ttHNodeDNN_ttlf_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_ttHNodeDNN_node_ttlf"
    category_dict["catlabel"] = "5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1796,
				0.73
				]
    this_dict["ljets_5j_ge3t_ttHNodeDNN_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge4j_ge3t_4NodeDNN

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t_4NodeDNN==0))","ljets_ge4j_ge3t_4NodeDNN_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_4NodeDNN_node_ttZ"
    category_dict["catlabel"] = "\geq 4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2219,
				0.3342,
				0.4465,
				0.5588,
				0.615,
				0.6712,
				0.7273,
				0.7835,
				0.8396,
				0.8958,
				0.98
				]
    this_dict["ljets_ge4j_ge3t_4NodeDNN_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t_4NodeDNN==1))","ljets_ge4j_ge3t_4NodeDNN_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_4NodeDNN_node_tthf"
    category_dict["catlabel"] = "\geq 4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2277,
				0.4062,
				0.4954,
				0.5846,
				0.6738,
				0.83
				]
    this_dict["ljets_ge4j_ge3t_4NodeDNN_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t_4NodeDNN==2))","ljets_ge4j_ge3t_4NodeDNN_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_4NodeDNN_node_ttcc"
    category_dict["catlabel"] = "\geq 4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2323,
				0.71
				]
    this_dict["ljets_ge4j_ge3t_4NodeDNN_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t_4NodeDNN==3))","ljets_ge4j_ge3t_4NodeDNN_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_4NodeDNN_node_ttlf"
    category_dict["catlabel"] = "\geq 4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2273,
				0.84
				]
    this_dict["ljets_ge4j_ge3t_4NodeDNN_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge4j_ge3t_5NodeDNN

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t_5NodeDNN==0))","ljets_ge4j_ge3t_5NodeDNN_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_5NodeDNN_node_ttZ"
    category_dict["catlabel"] = "\geq 4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1708,
				0.2877,
				0.4046,
				0.5215,
				0.58,
				0.6385,
				0.6969,
				0.7554,
				0.8138,
				0.8723,
				0.96
				]
    this_dict["ljets_ge4j_ge3t_5NodeDNN_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t_5NodeDNN==1))","ljets_ge4j_ge3t_5NodeDNN_ttmb_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_5NodeDNN_node_ttmb"
    category_dict["catlabel"] = "\geq 4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1815,
				0.3292,
				0.4031,
				0.4769,
				0.5508,
				0.68
				]
    this_dict["ljets_ge4j_ge3t_5NodeDNN_ttmb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t_5NodeDNN==2))","ljets_ge4j_ge3t_5NodeDNN_tt2b_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_5NodeDNN_node_tt2b"
    category_dict["catlabel"] = "\geq 4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1746,
				0.3777,
				0.4792,
				0.5808,
				0.6823,
				0.86
				]
    this_dict["ljets_ge4j_ge3t_5NodeDNN_tt2b_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t_5NodeDNN==3))","ljets_ge4j_ge3t_5NodeDNN_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_5NodeDNN_node_ttcc"
    category_dict["catlabel"] = "\geq 4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1881,
				0.51
				]
    this_dict["ljets_ge4j_ge3t_5NodeDNN_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t_5NodeDNN==4))","ljets_ge4j_ge3t_5NodeDNN_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_5NodeDNN_node_ttlf"
    category_dict["catlabel"] = "\geq 4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1692,
				1.0
				]
    this_dict["ljets_ge4j_ge3t_5NodeDNN_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge4j_ge3t_ttHNodeDNN

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t_ttHNodeDNN==0))","ljets_ge4j_ge3t_ttHNodeDNN_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_ttHNodeDNN_node_ttZ"
    category_dict["catlabel"] = "\geq 4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1765,
				0.2704,
				0.3642,
				0.4581,
				0.505,
				0.5519,
				0.5988,
				0.6458,
				0.6927,
				0.7396,
				0.81
				]
    this_dict["ljets_ge4j_ge3t_ttHNodeDNN_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t_ttHNodeDNN==1))","ljets_ge4j_ge3t_ttHNodeDNN_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_ttHNodeDNN_node_ttH"
    category_dict["catlabel"] = "\geq 4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.18,
				0.34,
				0.42,
				0.5,
				0.58,
				0.72
				]
    this_dict["ljets_ge4j_ge3t_ttHNodeDNN_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t_ttHNodeDNN==2))","ljets_ge4j_ge3t_ttHNodeDNN_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_ttHNodeDNN_node_tthf"
    category_dict["catlabel"] = "\geq 4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1758,
				0.3696,
				0.4665,
				0.5635,
				0.6604,
				0.83
				]
    this_dict["ljets_ge4j_ge3t_ttHNodeDNN_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t_ttHNodeDNN==3))","ljets_ge4j_ge3t_ttHNodeDNN_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_ttHNodeDNN_node_ttcc"
    category_dict["catlabel"] = "\geq 4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1854,
				0.58
				]
    this_dict["ljets_ge4j_ge3t_ttHNodeDNN_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t_ttHNodeDNN==4))","ljets_ge4j_ge3t_ttHNodeDNN_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_ttHNodeDNN_node_ttlf"
    category_dict["catlabel"] = "\geq 4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1765,
				0.81
				]
    this_dict["ljets_ge4j_ge3t_ttHNodeDNN_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for 4j_ge3t_4NodeDNN

    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_4j_ge3t_4NodeDNN==0))","ljets_4j_ge3t_4NodeDNN_ttZ_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_4NodeDNN_node_ttZ"
    category_dict["catlabel"] = "4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2212,
				0.3365,
				0.4519,
				0.5673,
				0.625,
				0.6827,
				0.7404,
				0.7981,
				0.8558,
				0.9135,
				1.0
				]
    this_dict["ljets_4j_ge3t_4NodeDNN_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_4j_ge3t_4NodeDNN==1))","ljets_4j_ge3t_4NodeDNN_tthf_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_4NodeDNN_node_tthf"
    category_dict["catlabel"] = "4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2265,
				0.4142,
				0.5081,
				0.6019,
				0.6958,
				0.86
				]
    this_dict["ljets_4j_ge3t_4NodeDNN_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_4j_ge3t_4NodeDNN==2))","ljets_4j_ge3t_4NodeDNN_ttcc_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_4NodeDNN_node_ttcc"
    category_dict["catlabel"] = "4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.235,
				0.64
				]
    this_dict["ljets_4j_ge3t_4NodeDNN_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_4j_ge3t_4NodeDNN==3))","ljets_4j_ge3t_4NodeDNN_ttlf_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_4NodeDNN_node_ttlf"
    category_dict["catlabel"] = "4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2308,
				0.75
				]
    this_dict["ljets_4j_ge3t_4NodeDNN_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for 4j_ge3t_5NodeDNN

    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_4j_ge3t_5NodeDNN==0))","ljets_4j_ge3t_5NodeDNN_ttZ_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_5NodeDNN_node_ttZ"
    category_dict["catlabel"] = "4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1692,
				0.2923,
				0.4154,
				0.5385,
				0.6,
				0.6615,
				0.7231,
				0.7846,
				0.8462,
				0.9077,
				1.0
				]
    this_dict["ljets_4j_ge3t_5NodeDNN_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_4j_ge3t_5NodeDNN==1))","ljets_4j_ge3t_5NodeDNN_ttmb_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_5NodeDNN_node_ttmb"
    category_dict["catlabel"] = "4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1838,
				0.3131,
				0.3777,
				0.4423,
				0.5069,
				0.62
				]
    this_dict["ljets_4j_ge3t_5NodeDNN_ttmb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_4j_ge3t_5NodeDNN==2))","ljets_4j_ge3t_5NodeDNN_tt2b_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_5NodeDNN_node_tt2b"
    category_dict["catlabel"] = "4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1696,
				0.4127,
				0.5342,
				0.6558,
				0.7773,
				0.99
				]
    this_dict["ljets_4j_ge3t_5NodeDNN_tt2b_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_4j_ge3t_5NodeDNN==3))","ljets_4j_ge3t_5NodeDNN_ttcc_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_5NodeDNN_node_ttcc"
    category_dict["catlabel"] = "4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1892,
				0.48
				]
    this_dict["ljets_4j_ge3t_5NodeDNN_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_4j_ge3t_5NodeDNN==4))","ljets_4j_ge3t_5NodeDNN_ttlf_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_5NodeDNN_node_ttlf"
    category_dict["catlabel"] = "4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1785,
				0.76
				]
    this_dict["ljets_4j_ge3t_5NodeDNN_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for 4j_ge3t_ttHNodeDNN

    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_4j_ge3t_ttHNodeDNN==0))","ljets_4j_ge3t_ttHNodeDNN_ttZ_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_ttHNodeDNN_node_ttZ"
    category_dict["catlabel"] = "4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1815,
				0.2554,
				0.3292,
				0.4031,
				0.44,
				0.4769,
				0.5138,
				0.5508,
				0.5877,
				0.6246,
				0.68
				]
    this_dict["ljets_4j_ge3t_ttHNodeDNN_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_4j_ge3t_ttHNodeDNN==1))","ljets_4j_ge3t_ttHNodeDNN_ttH_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_ttHNodeDNN_node_ttH"
    category_dict["catlabel"] = "4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1812,
				0.3319,
				0.4073,
				0.4827,
				0.5581,
				0.69
				]
    this_dict["ljets_4j_ge3t_ttHNodeDNN_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_4j_ge3t_ttHNodeDNN==2))","ljets_4j_ge3t_ttHNodeDNN_tthf_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_ttHNodeDNN_node_tthf"
    category_dict["catlabel"] = "4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1727,
				0.3912,
				0.5004,
				0.6096,
				0.7188,
				0.91
				]
    this_dict["ljets_4j_ge3t_ttHNodeDNN_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_4j_ge3t_ttHNodeDNN==3))","ljets_4j_ge3t_ttHNodeDNN_ttcc_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_ttHNodeDNN_node_ttcc"
    category_dict["catlabel"] = "4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1873,
				0.53
				]
    this_dict["ljets_4j_ge3t_ttHNodeDNN_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_4j_ge3t_ttHNodeDNN==4))","ljets_4j_ge3t_ttHNodeDNN_ttlf_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_ttHNodeDNN_node_ttlf"
    category_dict["catlabel"] = "4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1788,
				0.75
				]
    this_dict["ljets_4j_ge3t_ttHNodeDNN_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge4j_3t_4NodeDNN

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_3t_4NodeDNN==0))","ljets_ge4j_3t_4NodeDNN_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_4NodeDNN_node_ttZ"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2227,
				0.3319,
				0.4412,
				0.5504,
				0.605,
				0.6596,
				0.7142,
				0.7688,
				0.8235,
				0.8781,
				0.96
				]
    this_dict["ljets_ge4j_3t_4NodeDNN_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_3t_4NodeDNN==1))","ljets_ge4j_3t_4NodeDNN_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_4NodeDNN_node_tthf"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2269,
				0.4115,
				0.5038,
				0.5962,
				0.6885,
				0.85
				]
    this_dict["ljets_ge4j_3t_4NodeDNN_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_3t_4NodeDNN==2))","ljets_ge4j_3t_4NodeDNN_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_4NodeDNN_node_ttcc"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2369,
				0.59
				]
    this_dict["ljets_ge4j_3t_4NodeDNN_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_3t_4NodeDNN==3))","ljets_ge4j_3t_4NodeDNN_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_4NodeDNN_node_ttlf"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2215,
				0.99
				]
    this_dict["ljets_ge4j_3t_4NodeDNN_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge4j_3t_5NodeDNN

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_3t_5NodeDNN==0))","ljets_ge4j_3t_5NodeDNN_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_5NodeDNN_node_ttZ"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.17,
				0.29,
				0.41,
				0.53,
				0.59,
				0.65,
				0.71,
				0.77,
				0.83,
				0.89,
				0.98
				]
    this_dict["ljets_ge4j_3t_5NodeDNN_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_3t_5NodeDNN==1))","ljets_ge4j_3t_5NodeDNN_ttmb_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_5NodeDNN_node_ttmb"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1815,
				0.3292,
				0.4031,
				0.4769,
				0.5508,
				0.68
				]
    this_dict["ljets_ge4j_3t_5NodeDNN_ttmb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_3t_5NodeDNN==2))","ljets_ge4j_3t_5NodeDNN_tt2b_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_5NodeDNN_node_tt2b"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1692,
				0.4154,
				0.5385,
				0.6615,
				0.7846,
				1.0
				]
    this_dict["ljets_ge4j_3t_5NodeDNN_tt2b_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_3t_5NodeDNN==3))","ljets_ge4j_3t_5NodeDNN_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_5NodeDNN_node_ttcc"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1881,
				0.51
				]
    this_dict["ljets_ge4j_3t_5NodeDNN_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_3t_5NodeDNN==4))","ljets_ge4j_3t_5NodeDNN_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_5NodeDNN_node_ttlf"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1777,
				0.78
				]
    this_dict["ljets_ge4j_3t_5NodeDNN_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge4j_3t_ttHNodeDNN

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_3t_ttHNodeDNN==0))","ljets_ge4j_3t_ttHNodeDNN_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_ttHNodeDNN_node_ttZ"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1746,
				0.2762,
				0.3777,
				0.4792,
				0.53,
				0.5808,
				0.6315,
				0.6823,
				0.7331,
				0.7838,
				0.86
				]
    this_dict["ljets_ge4j_3t_ttHNodeDNN_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_3t_ttHNodeDNN==1))","ljets_ge4j_3t_ttHNodeDNN_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_ttHNodeDNN_node_ttH"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1773,
				0.3588,
				0.4496,
				0.5404,
				0.6312,
				0.79
				]
    this_dict["ljets_ge4j_3t_ttHNodeDNN_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_3t_ttHNodeDNN==2))","ljets_ge4j_3t_ttHNodeDNN_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_ttHNodeDNN_node_tthf"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1754,
				0.3723,
				0.4708,
				0.5692,
				0.6677,
				0.84
				]
    this_dict["ljets_ge4j_3t_ttHNodeDNN_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_3t_ttHNodeDNN==3))","ljets_ge4j_3t_ttHNodeDNN_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_ttHNodeDNN_node_ttcc"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1862,
				0.56
				]
    this_dict["ljets_ge4j_3t_ttHNodeDNN_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_3t_ttHNodeDNN==4))","ljets_ge4j_3t_ttHNodeDNN_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_ttHNodeDNN_node_ttlf"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1692,
				1.0
				]
    this_dict["ljets_ge4j_3t_ttHNodeDNN_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    

    for l in this_dict:
        this_dict[l]["histoname"] = discrname+"_"+l
        this_dict[l]["histotitle"] = "final discriminator ({})".format(l)
        this_dict[l]["plotPreselections"] = this_dict[l]["category"][0]

    DNNPlots = init_plots(dictionary = this_dict, data = data)
    return DNNPlots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_dnn(data, discrname)

    return discriminatorPlots


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
    