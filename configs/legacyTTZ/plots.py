
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



# def plots_ge4j_ge3t(data = None):
#     label = "\geq 4 jets, \geq 3 b-tags"
#     interfaces = []
#     selection = "(N_Jets>=4&&N_BTagsM>=3)&&(1.)"

#     plots = [
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_B1_btagValue","btag value of first Z b-jet",30,0.0,1.0),"dnnZ_ft_RecoX_B1_btagValue",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_B1_E","energy of first Z b-jet",30,0.,500.),"dnnZ_ft_RecoX_B1_E",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_B1_Eta","#eta of first Z b-jet",30,-2.4,2.4),"dnnZ_ft_RecoX_B1_Eta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_B1_Pt","p_{T} of first Z b-jet",30,0.,500.),"dnnZ_ft_RecoX_B1_Pt",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_B2_btagValue","btag value of second Z b-jet",30,0.0,1.0),"dnnZ_ft_RecoX_B2_btagValue",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_B2_E","energy of second Z b-jet",30,0.,500.),"dnnZ_ft_RecoX_B2_E",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_B2_Eta","#eta of second Z b-jet",30,-2.4,2.4),"dnnZ_ft_RecoX_B2_Eta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_B2_Pt","p_{T} of second Z b-jet",30,0.,500.),"dnnZ_ft_RecoX_B2_Pt",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_X_E","reconstructed Z boson energy",30,0.,1000.),"dnnZ_ft_RecoX_X_E",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_X_Eta","reconstructed Z boson #eta",30,-2.4,2.4),"dnnZ_ft_RecoX_X_Eta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_X_M","reconstructed Z boson mass [GeV]",50,0.,250.),"dnnZ_ft_RecoX_X_M",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_X_Pt","Reconstructed Z boson p_{T}",30,0.,500.),"dnnZ_ft_RecoX_X_Pt",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_dEta","#Delta #eta of Z b-jets",30,0.0,4.0),"dnnZ_ft_RecoX_X_dEta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_dPhi","#Delta #phi of Z b-jets",30,0.0,3.141),"dnnZ_ft_RecoX_X_dPhi",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_dR","#DeltaR of Z b-jets",30,0.0,4.0),"dnnZ_ft_RecoX_X_dR",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_DNNOutput","Z boson reconstruction DNN output",50,0.,1.0),"dnnZ_ft_RecoX_DNNOutput",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_transformedDNNOutput","transformed Z boson reconstruction DNN output",50,-6.,6.0),"dnnZ_ft_RecoX_transformedDNNOutput",selection,label),

#         #plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_newTransformedOutput","transformed Z boson reconstruction DNN output",50,-6.,6.0),"newTransformedOutput",selection,label),


#         # random test plots
# 	plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_N_Jets","jet multiplicty",7,3.5,10.5),"N_Jets",selection,label),
# 	plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_Jet_Pt","p_{T} of jets",100,0.,1000.),"Jet_Pt",selection,label),
# 	plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_Jet_Pt_0","p_{T} of leading jet",100,0.,1000.),"Jet_Pt[0]",selection,label),



#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_B1_btagValue","btag value of first H b-jet",30,0.0,1.0),"dnnH_ft_RecoX_B1_btagValue",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_B1_E","energy of first H b-jet",30,0.,500.),"dnnH_ft_RecoX_B1_E",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_B1_Eta","#eta of first H b-jet",30,-2.4,2.4),"dnnH_ft_RecoX_B1_Eta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_B1_Pt","p_{T} of first H b-jet",30,0.,500.),"dnnH_ft_RecoX_B1_Pt",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_B2_btagValue","btag value of second H b-jet",30,0.0,1.0),"dnnH_ft_RecoX_B2_btagValue",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_B2_E","energy of second H b-jet",30,0.,500.),"dnnH_ft_RecoX_B2_E",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_B2_Eta","#eta of second H b-jet",30,-2.4,2.4),"dnnH_ft_RecoX_B2_Eta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_B2_Pt","p_{T} of second H b-jet",30,0.,500.),"dnnH_ft_RecoX_B2_Pt",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_X_E","reconstructed H boson energy",30,0.,1000.),"dnnH_ft_RecoX_X_E",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_X_Eta","reconstructed H boson #eta",30,-2.4,2.4),"dnnH_ft_RecoX_X_Eta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_X_M","reconstructed H boson mass [GeV]",50,0.,250.),"dnnH_ft_RecoX_X_M",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_X_Pt","Reconstructed H boson p_{T}",30,0.,500.),"dnnH_ft_RecoX_X_Pt",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_dEta","#Delta #eta of H b-jets",30,0.0,4.0),"dnnH_ft_RecoX_X_dEta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_dPhi","#Delta #phi of H b-jets",30,0.0,3.141),"dnnH_ft_RecoX_X_dPhi",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_dR","#DeltaR of H b-jets",30,0.0,4.0),"dnnH_ft_RecoX_X_dR",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_DNNOutput","H boson reconstruction DNN output",50,0.,1.0),"dnnH_ft_RecoX_DNNOutput",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_transformedDNNOutput","transformed H boson reconstruction DNN output",50,-6.,6.0),"dnnH_ft_RecoX_transformedDNNOutput",selection,label),

#         #plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_newTransformedOutput","transformed Higgs boson reconstruction DNN output",50,-6.,6.0),"newTransformedOutput",selection,label),
#         ]

        
#    if data:
#        add_data_plots(plots=plots,data=data)
#    return plots



# def plots_4j_ge3t(data = None):
#     label = "4 jets, \geq 3 b-tags"
#     interfaces = []
#     selection = "(N_Jets==4&&N_BTagsM>=3)&&(1.)"

#     plots = [
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_B1_btagValue","btag value of first Z b-jet",30,0.0,1.0),"dnnZ_ft_RecoX_B1_btagValue",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_B1_E","energy of first Z b-jet",30,0.,500.),"dnnZ_ft_RecoX_B1_E",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_B1_Eta","#eta of first Z b-jet",30,-2.4,2.4),"dnnZ_ft_RecoX_B1_Eta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_B1_Pt","p_{T} of first Z b-jet",30,0.,500.),"dnnZ_ft_RecoX_B1_Pt",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_B2_btagValue","btag value of second Z b-jet",30,0.0,1.0),"dnnZ_ft_RecoX_B2_btagValue",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_B2_E","energy of second Z b-jet",30,0.,500.),"dnnZ_ft_RecoX_B2_E",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_B2_Eta","#eta of second Z b-jet",30,-2.4,2.4),"dnnZ_ft_RecoX_B2_Eta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_B2_Pt","p_{T} of second Z b-jet",30,0.,500.),"dnnZ_ft_RecoX_B2_Pt",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_X_E","reconstructed Z boson energy",30,0.,1000.),"dnnZ_ft_RecoX_X_E",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_X_Eta","reconstructed Z boson #eta",30,-2.4,2.4),"dnnZ_ft_RecoX_X_Eta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_X_M","reconstructed Z boson mass [GeV]",50,0.,250.),"dnnZ_ft_RecoX_X_M",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_X_Pt","Reconstructed Z boson p_{T}",30,0.,500.),"dnnZ_ft_RecoX_X_Pt",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_dEta","#Delta #eta of Z b-jets",30,0.0,4.0),"dnnZ_ft_RecoX_X_dEta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_dPhi","#Delta #phi of Z b-jets",30,0.0,3.141),"dnnZ_ft_RecoX_X_dPhi",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_dR","#DeltaR of Z b-jets",30,0.0,4.0),"dnnZ_ft_RecoX_X_dR",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_DNNOutput","Z boson reconstruction DNN output",50,0.,1.0),"dnnZ_ft_RecoX_DNNOutput",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_transformedDNNOutput","transformed Z boson reconstruction DNN output",50,-6.,6.0),"dnnZ_ft_RecoX_transformedDNNOutput",selection,label),

#         #plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_newTransformedOutput","transformed Z boson reconstruction DNN output",50,-6.,6.0),"newTransformedOutput",selection,label),


#         # random test plots
# 	plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_N_Jets","jet multiplicty",7,3.5,10.5),"N_Jets",selection,label),
# 	plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Jet_Pt","p_{T} of jets",100,0.,1000.),"Jet_Pt",selection,label),
# 	plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Jet_Pt_0","p_{T} of leading jet",100,0.,1000.),"Jet_Pt[0]",selection,label),



#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_B1_btagValue","btag value of first H b-jet",30,0.0,1.0),"dnnH_ft_RecoX_B1_btagValue",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_B1_E","energy of first H b-jet",30,0.,500.),"dnnH_ft_RecoX_B1_E",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_B1_Eta","#eta of first H b-jet",30,-2.4,2.4),"dnnH_ft_RecoX_B1_Eta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_B1_Pt","p_{T} of first H b-jet",30,0.,500.),"dnnH_ft_RecoX_B1_Pt",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_B2_btagValue","btag value of second H b-jet",30,0.0,1.0),"dnnH_ft_RecoX_B2_btagValue",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_B2_E","energy of second H b-jet",30,0.,500.),"dnnH_ft_RecoX_B2_E",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_B2_Eta","#eta of second H b-jet",30,-2.4,2.4),"dnnH_ft_RecoX_B2_Eta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_B2_Pt","p_{T} of second H b-jet",30,0.,500.),"dnnH_ft_RecoX_B2_Pt",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_X_E","reconstructed H boson energy",30,0.,1000.),"dnnH_ft_RecoX_X_E",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_X_Eta","reconstructed H boson #eta",30,-2.4,2.4),"dnnH_ft_RecoX_X_Eta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_X_M","reconstructed H boson mass [GeV]",50,0.,250.),"dnnH_ft_RecoX_X_M",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_X_Pt","Reconstructed H boson p_{T}",30,0.,500.),"dnnH_ft_RecoX_X_Pt",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_dEta","#Delta #eta of H b-jets",30,0.0,4.0),"dnnH_ft_RecoX_X_dEta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_dPhi","#Delta #phi of H b-jets",30,0.0,3.141),"dnnH_ft_RecoX_X_dPhi",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_dR","#DeltaR of H b-jets",30,0.0,4.0),"dnnH_ft_RecoX_X_dR",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_DNNOutput","H boson reconstruction DNN output",50,0.,1.0),"dnnH_ft_RecoX_DNNOutput",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_transformedDNNOutput","transformed H boson reconstruction DNN output",50,-6.,6.0),"dnnH_ft_RecoX_transformedDNNOutput",selection,label),

#         #plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_newTransformedOutput","transformed Higgs boson reconstruction DNN output",50,-6.,6.0),"newTransformedOutput",selection,label),
#         ]

        
#     if data:
#         add_data_plots(plots=plots,data=data)
#     return plots




# def plots_5j_ge3t(data = None):
#     label = "5 jets, \geq 3 b-tags"
#     interfaces = []
#     selection = "(N_Jets==5&&N_BTagsM>=3)&&(1.)"

#     plots = [
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_B1_btagValue","btag value of first Z b-jet",30,0.0,1.0),"dnnZ_ft_RecoX_B1_btagValue",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_B1_E","energy of first Z b-jet",30,0.,500.),"dnnZ_ft_RecoX_B1_E",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_B1_Eta","#eta of first Z b-jet",30,-2.4,2.4),"dnnZ_ft_RecoX_B1_Eta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_B1_Pt","p_{T} of first Z b-jet",30,0.,500.),"dnnZ_ft_RecoX_B1_Pt",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_B2_btagValue","btag value of second Z b-jet",30,0.0,1.0),"dnnZ_ft_RecoX_B2_btagValue",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_B2_E","energy of second Z b-jet",30,0.,500.),"dnnZ_ft_RecoX_B2_E",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_B2_Eta","#eta of second Z b-jet",30,-2.4,2.4),"dnnZ_ft_RecoX_B2_Eta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_B2_Pt","p_{T} of second Z b-jet",30,0.,500.),"dnnZ_ft_RecoX_B2_Pt",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_X_E","reconstructed Z boson energy",30,0.,1000.),"dnnZ_ft_RecoX_X_E",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_X_Eta","reconstructed Z boson #eta",30,-2.4,2.4),"dnnZ_ft_RecoX_X_Eta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_X_M","reconstructed Z boson mass [GeV]",50,0.,250.),"dnnZ_ft_RecoX_X_M",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_X_Pt","Reconstructed Z boson p_{T}",30,0.,500.),"dnnZ_ft_RecoX_X_Pt",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_dEta","#Delta #eta of Z b-jets",30,0.0,4.0),"dnnZ_ft_RecoX_X_dEta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_dPhi","#Delta #phi of Z b-jets",30,0.0,3.141),"dnnZ_ft_RecoX_X_dPhi",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_dR","#DeltaR of Z b-jets",30,0.0,4.0),"dnnZ_ft_RecoX_X_dR",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_DNNOutput","Z boson reconstruction DNN output",50,0.,1.0),"dnnZ_ft_RecoX_DNNOutput",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_transformedDNNOutput","transformed Z boson reconstruction DNN output",50,-6.,6.0),"dnnZ_ft_RecoX_transformedDNNOutput",selection,label),

#         #plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_newTransformedOutput","transformed Z boson reconstruction DNN output",50,-6.,6.0),"newTransformedOutput",selection,label),


#         # random test plots
# 	plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_N_Jets","jet multiplicty",7,3.5,10.5),"N_Jets",selection,label),
# 	plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Jet_Pt","p_{T} of jets",100,0.,1000.),"Jet_Pt",selection,label),
# 	plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Jet_Pt_0","p_{T} of leading jet",100,0.,1000.),"Jet_Pt[0]",selection,label),



#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_B1_btagValue","btag value of first H b-jet",30,0.0,1.0),"dnnH_ft_RecoX_B1_btagValue",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_B1_E","energy of first H b-jet",30,0.,500.),"dnnH_ft_RecoX_B1_E",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_B1_Eta","#eta of first H b-jet",30,-2.4,2.4),"dnnH_ft_RecoX_B1_Eta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_B1_Pt","p_{T} of first H b-jet",30,0.,500.),"dnnH_ft_RecoX_B1_Pt",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_B2_btagValue","btag value of second H b-jet",30,0.0,1.0),"dnnH_ft_RecoX_B2_btagValue",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_B2_E","energy of second H b-jet",30,0.,500.),"dnnH_ft_RecoX_B2_E",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_B2_Eta","#eta of second H b-jet",30,-2.4,2.4),"dnnH_ft_RecoX_B2_Eta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_B2_Pt","p_{T} of second H b-jet",30,0.,500.),"dnnH_ft_RecoX_B2_Pt",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_X_E","reconstructed H boson energy",30,0.,1000.),"dnnH_ft_RecoX_X_E",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_X_Eta","reconstructed H boson #eta",30,-2.4,2.4),"dnnH_ft_RecoX_X_Eta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_X_M","reconstructed H boson mass [GeV]",50,0.,250.),"dnnH_ft_RecoX_X_M",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_X_Pt","Reconstructed H boson p_{T}",30,0.,500.),"dnnH_ft_RecoX_X_Pt",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_dEta","#Delta #eta of H b-jets",30,0.0,4.0),"dnnH_ft_RecoX_X_dEta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_dPhi","#Delta #phi of H b-jets",30,0.0,3.141),"dnnH_ft_RecoX_X_dPhi",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_dR","#DeltaR of H b-jets",30,0.0,4.0),"dnnH_ft_RecoX_X_dR",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_DNNOutput","H boson reconstruction DNN output",50,0.,1.0),"dnnH_ft_RecoX_DNNOutput",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_transformedDNNOutput","transformed H boson reconstruction DNN output",50,-6.,6.0),"dnnH_ft_RecoX_transformedDNNOutput",selection,label),

#         #plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_newTransformedOutput","transformed Higgs boson reconstruction DNN output",50,-6.,6.0),"newTransformedOutput",selection,label),
#         ]

        
#     if data:
#         add_data_plots(plots=plots,data=data)
#     return plots



    
def plots_ge6j_ge3t(data = None):
    label = "\geq 6 jets, \geq 3 b-tags"
    interfaces = []
    selection = "(N_Jets>=6&&N_BTagsM>=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_B1_btagValue","btag value of first Z b-jet",30,0.0,1.0),"dnnZ_ft_RecoX_B1_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_B1_E","energy of first Z b-jet",30,0.,500.),"dnnZ_ft_RecoX_B1_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_B1_Eta","#eta of first Z b-jet",30,-2.4,2.4),"dnnZ_ft_RecoX_B1_Eta",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_B1_Pt","p_{T} of first Z b-jet",30,0.,500.),"dnnZ_ft_RecoX_B1_Pt",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_B2_btagValue","btag value of second Z b-jet",30,0.0,1.0),"dnnZ_ft_RecoX_B2_btagValue",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_B2_E","energy of second Z b-jet",30,0.,500.),"dnnZ_ft_RecoX_B2_E",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_B2_Eta","#eta of second Z b-jet",30,-2.4,2.4),"dnnZ_ft_RecoX_B2_Eta",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_B2_Pt","p_{T} of second Z b-jet",30,0.,500.),"dnnZ_ft_RecoX_B2_Pt",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_X_E","reconstructed Z boson energy",30,0.,1000.),"dnnZ_ft_RecoX_X_E",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_X_Eta","reconstructed Z boson #eta",30,-2.4,2.4),"dnnZ_ft_RecoX_X_Eta",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_X_M","reconstructed Z boson mass [GeV]",50,0.,250.),"dnnZ_ft_RecoX_X_M",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_X_Pt","Reconstructed Z boson p_{T}",30,0.,500.),"dnnZ_ft_RecoX_X_Pt",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_dEta","#Delta #eta of Z b-jets",30,0.0,4.0),"dnnZ_ft_RecoX_X_dEta",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_dPhi","#Delta #phi of Z b-jets",30,0.0,3.141),"dnnZ_ft_RecoX_X_dPhi",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_dR","#DeltaR of Z b-jets",30,0.0,4.0),"dnnZ_ft_RecoX_X_dR",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_DNNOutput","Z boson reconstruction DNN output",50,0.,1.0),"dnnZ_ft_RecoX_DNNOutput",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_transformedDNNOutput","transformed Z boson reconstruction DNN output",50,-6.,6.0),"dnnZ_ft_RecoX_transformedDNNOutput",selection,label),
        
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_B1_btagValue","btag value of first H b-jet",30,0.0,1.0),"dnnH_ft_RecoX_B1_btagValue",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_B1_E","energy of first H b-jet",30,0.,500.),"dnnH_ft_RecoX_B1_E",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_B1_Eta","#eta of first H b-jet",30,-2.4,2.4),"dnnH_ft_RecoX_B1_Eta",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_B1_Pt","p_{T} of first H b-jet",30,0.,500.),"dnnH_ft_RecoX_B1_Pt",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_B2_btagValue","btag value of second H b-jet",30,0.0,1.0),"dnnH_ft_RecoX_B2_btagValue",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_B2_E","energy of second H b-jet",30,0.,500.),"dnnH_ft_RecoX_B2_E",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_B2_Eta","#eta of second H b-jet",30,-2.4,2.4),"dnnH_ft_RecoX_B2_Eta",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_B2_Pt","p_{T} of second H b-jet",30,0.,500.),"dnnH_ft_RecoX_B2_Pt",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_X_E","reconstructed H boson energy",30,0.,1000.),"dnnH_ft_RecoX_X_E",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_X_Eta","reconstructed H boson #eta",30,-2.4,2.4),"dnnH_ft_RecoX_X_Eta",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_X_M","reconstructed H boson mass [GeV]",50,0.,250.),"dnnH_ft_RecoX_X_M",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_X_Pt","Reconstructed H boson p_{T}",30,0.,500.),"dnnH_ft_RecoX_X_Pt",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_dEta","#Delta #eta of H b-jets",30,0.0,4.0),"dnnH_ft_RecoX_X_dEta",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_dPhi","#Delta #phi of H b-jets",30,0.0,3.141),"dnnH_ft_RecoX_X_dPhi",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_dR","#DeltaR of H b-jets",30,0.0,4.0),"dnnH_ft_RecoX_X_dR",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_DNNOutput","H boson reconstruction DNN output",50,0.,1.0),"dnnH_ft_RecoX_DNNOutput",selection,label),
#        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_transformedDNNOutput","transformed H boson reconstruction DNN output",50,-6.,6.0),"dnnH_ft_RecoX_transformedDNNOutput",selection,label),

        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    
# def plots_ge4j_ge4t(data = None):
#     label = "\geq 4 jets, \geq 4 b-tags"
#     interfaces = []
#     selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"

#     plots = [
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnZ_ft_RecoX_B1_btagValue","btag value of first Z b-jet",30,0.0,1.0),"dnnZ_ft_RecoX_B1_btagValue",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnZ_ft_RecoX_B1_E","energy of first Z b-jet",30,0.,500.),"dnnZ_ft_RecoX_B1_E",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnZ_ft_RecoX_B1_Eta","#eta of first Z b-jet",30,-2.4,2.4),"dnnZ_ft_RecoX_B1_Eta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnZ_ft_RecoX_B1_Pt","p_{T} of first Z b-jet",30,0.,500.),"dnnZ_ft_RecoX_B1_Pt",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnZ_ft_RecoX_B2_btagValue","btag value of second Z b-jet",30,0.0,1.0),"dnnZ_ft_RecoX_B2_btagValue",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnZ_ft_RecoX_B2_E","energy of second Z b-jet",30,0.,500.),"dnnZ_ft_RecoX_B2_E",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnZ_ft_RecoX_B2_Eta","#eta of second Z b-jet",30,-2.4,2.4),"dnnZ_ft_RecoX_B2_Eta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnZ_ft_RecoX_B2_Pt","p_{T} of second Z b-jet",30,0.,500.),"dnnZ_ft_RecoX_B2_Pt",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnZ_ft_RecoX_X_E","reconstructed Z boson energy",30,0.,1000.),"dnnZ_ft_RecoX_X_E",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnZ_ft_RecoX_X_Eta","reconstructed Z boson #eta",30,-2.4,2.4),"dnnZ_ft_RecoX_X_Eta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnZ_ft_RecoX_X_M","reconstructed Z boson mass [GeV]",50,0.,250.),"dnnZ_ft_RecoX_X_M",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnZ_ft_RecoX_X_Pt","Reconstructed Z boson p_{T}",30,0.,500.),"dnnZ_ft_RecoX_X_Pt",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnZ_ft_RecoX_dEta","#Delta #eta of Z b-jets",30,0.0,4.0),"dnnZ_ft_RecoX_X_dEta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnZ_ft_RecoX_dPhi","#Delta #phi of Z b-jets",30,0.0,3.141),"dnnZ_ft_RecoX_X_dPhi",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnZ_ft_RecoX_dR","#DeltaR of Z b-jets",30,0.0,4.0),"dnnZ_ft_RecoX_X_dR",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnZ_ft_RecoX_DNNOutput","Z boson reconstruction DNN output",50,0.,1.0),"dnnZ_ft_RecoX_DNNOutput",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnZ_ft_RecoX_transformedDNNOutput","transformed Z boson reconstruction DNN output",50,-6.0,6.0),"dnnZ_ft_RecoX_transformedDNNOutput",selection,label),
        
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnH_ft_RecoX_B1_btagValue","btag value of first H b-jet",30,0.0,1.0),"dnnH_ft_RecoX_B1_btagValue",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnH_ft_RecoX_B1_E","energy of first H b-jet",30,0.,500.),"dnnH_ft_RecoX_B1_E",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnH_ft_RecoX_B1_Eta","#eta of first H b-jet",30,-2.4,2.4),"dnnH_ft_RecoX_B1_Eta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnH_ft_RecoX_B1_Pt","p_{T} of first H b-jet",30,0.,500.),"dnnH_ft_RecoX_B1_Pt",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnH_ft_RecoX_B2_btagValue","btag value of second H b-jet",30,0.0,1.0),"dnnH_ft_RecoX_B2_btagValue",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnH_ft_RecoX_B2_E","energy of second H b-jet",30,0.,500.),"dnnH_ft_RecoX_B2_E",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnH_ft_RecoX_B2_Eta","#eta of second H b-jet",30,-2.4,2.4),"dnnH_ft_RecoX_B2_Eta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnH_ft_RecoX_B2_Pt","p_{T} of second H b-jet",30,0.,500.),"dnnH_ft_RecoX_B2_Pt",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnH_ft_RecoX_X_E","reconstructed H boson energy",30,0.,1000.),"dnnH_ft_RecoX_X_E",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnH_ft_RecoX_X_Eta","reconstructed H boson #eta",30,-2.4,2.4),"dnnH_ft_RecoX_X_Eta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnH_ft_RecoX_X_M","reconstructed H boson mass [GeV]",50,0.,250.),"dnnH_ft_RecoX_X_M",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnH_ft_RecoX_X_Pt","Reconstructed H boson p_{T}",30,0.,500.),"dnnH_ft_RecoX_X_Pt",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnH_ft_RecoX_dEta","#Delta #eta of H b-jets",30,0.0,4.0),"dnnH_ft_RecoX_X_dEta",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnH_ft_RecoX_dPhi","#Delta #phi of H b-jets",30,0.0,3.141),"dnnH_ft_RecoX_X_dPhi",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnH_ft_RecoX_dR","#DeltaR of H b-jets",30,0.0,4.0),"dnnH_ft_RecoX_X_dR",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnH_ft_RecoX_DNNOutput","H boson reconstruction DNN output",50,0.,1.0),"dnnH_ft_RecoX_DNNOutput",selection,label),
#         plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_dnnH_ft_RecoX_transformedDNNOutput","transformed H boson reconstruction DNN output",50,-6.0,6.0),"dnnH_ft_RecoX_transformedDNNOutput",selection,label),

#         ]

        
#     if data:
#         add_data_plots(plots=plots,data=data)
#     return plots
    
def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    #discriminatorPlots += plots_ge4j_ge3t(data)
    discriminatorPlots += plots_ge6j_ge3t(data)
    #discriminatorPlots += plots_ge4j_ge4t(data)

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
    
