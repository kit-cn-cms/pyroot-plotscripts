
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
    label = "event yields"
    selection = "(N_Jets>=4&&N_BTagsM>=3)&&(1.)"
    plots = [
        plotClasses.Plot(ROOT.TH1D("inclusive_eventYields","event yields",6,0.5,6.5),jtYieldExpression,selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_yield","event yield",1,0,1),"0.5",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_nomWeight","weight",100,-0.2,0.2),"Weight_GEN_nom*Weight_CSV*Weight_XS*Weight_pu69p2",selection,label),
        ]

    if data:
        add_data_plots(plots=plots,data=data)
    return plots



def plots_ge6j_ge3t(data = None):
    label = "\geq 6 jets, \geq 3 b-tags"
    selection = "(N_Jets>=6&&N_BTagsM>=3)&&(1.)"

    plots = [
    #plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_CSV_2","third highest b-tag value",30,0.277,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_CSV_3","fourth highest b-tag value",30,0.0,0.7),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_CSV_avg","average b-tag value",30,0.12,0.7),"Evt_CSV_avg",selection,label),
#plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_CSV_avg_tagged","average b-tag value of tagged jets",30,0.4,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_CSV_dev","average deviation of b-tag value",30,0.02,0.24),"Evt_CSV_dev",selection,label),
        #plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_CSV_min_tagged","minimal b-tag value of tagged jets",30,0.277,1.0),"Evt_CSV_min_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_Deta_JetsAverage","#Delta#eta^{j,j}_{avg}",30,0.25,2.4),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_Deta_TaggedJetsAverage","#Delta#eta^{b,b}_{avg}",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        #plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_Dr_TaggedJetsAverage","#DeltaR^{b,b}_{avg}",30,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        #plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_Dr_minDrLepTag","#DeltaR^{l,j}_{min}",30,0.4,3.0),"Evt_Dr_minDrLepTag",selection,label),
        #plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_HT","H_{T}",30,300.0,1500.0),"Evt_HT",selection,label),
        #plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_HT_jets","H_{T} of jets",30,200.0,1200.0),"Evt_HT_jets",selection,label),
        #plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_HT_wo_MET","H_{T} without MET",30,300.0,1400.0),"Evt_HT_wo_MET",selection,label),
        #plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_M2_JetsAverage","m^{j,j}_{avg}",30,40.0,500.0),"Evt_M2_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_M2_TaggedJetsAverage","m^{b,b}_{avg} [GeV]",30,40.0,500.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_M2_closestTo125TaggedJets","m^{b,b} closest to 125 [GeV]",30,30.0,250.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_M2_closestTo91TaggedJets","m^{b,b} closest to 91 [GeV]",30,30.0,250.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_M2_minDrTaggedJets","m(#DeltaR^{b,b}_{min}) [GeV]",30,20.0,350.0),"Evt_M2_minDrTaggedJets",selection,label),
        #plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_MTW","m_{T}^{W}",30,0.0,250.0),"Evt_MTW",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_M_TaggedJetsAverage","m^{b}_{avg} [GeV]",30,5.0,35.0),"Evt_M_TaggedJetsAverage",selection,label),
        #plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_M_minDrLepTag","m(#DeltaR^{l,b}_{min})",30,20.0,250.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_Pt_minDrTaggedJets","p_{T}(#DeltaR^{b,b}_{min}) [GeV]",30,30.0,450.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_blr","b-tag likelihood ratio",30,0.3,1.0),"Evt_blr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_blr_transformed","transformed b-tag likelihood ratio",30,-1.0,12.0),"Evt_blr_transformed",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Jet_Pt_0","p_{T} of leading jet [GeV]",30,50.0,600.0),"Jet_Pt[0]",selection,label),
        #plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_N_BTagsL","number of b-tags (loose)",4,2.5,6.5),"N_BTagsL",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_N_BTagsM","number of b-tags (medium)",3,2.5,5.5),"N_BTagsM",selection,label),
    #plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_RecoTTZ_Chi2Total_log","t#bar{t}+Z reconstruction ln(#chi^{2})",30,-2.0,8.0),"RecoTTZ_Chi2Total_log",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_RecoTTZ_Chi2Z_log","t#bar{t}+Z reconstruction ln(#chi^{2})(Z)",30,-10.0,7.0),"RecoTTZ_Chi2Z_log",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_RecoTTZ_Z_M_log","t#bar{t}+Z reconstruction ln(m)(Z) [ln(GeV)]",30,3.5,6.0),"RecoTTZ_Z_M_log",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_RecoTTZ_Z_Pt","t#bar{t}+Z reconstruction p_{T}(Z) [GeV]",30,0.0,600.0),"RecoTTZ_Z_Pt",selection,label),
        ]

    if data:
        add_data_plots(plots=plots,data=data)
    return plots



def plots_5j_ge3t(data = None):
    label = "5 jets, \geq 3 b-tags"
    selection = "(N_Jets==5&&N_BTagsM>=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_CSV_2","third highest b-tag value",30,0.277,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_CSV_3","fourth highest b-tag value",30,0.0,0.3),"CSV[3]",selection,label),
#plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_CSV_avg","average b-tag value",30,0.2,0.8),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_CSV_avg_tagged","average b-tag value of tagged jets",30,0.4,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_CSV_dev","average deviation of b-tag value",30,0.02,0.24),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_CSV_min","minimal b-tag value",30,0.0,0.1),"Evt_CSV_min",selection,label),
    #plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_Deta_JetsAverage","#Delta#eta^{j,j}_{avg}",30,0.25,2.5),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_Deta_TaggedJetsAverage","#Delta#eta^{b,b}_{avg}",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_Dr_JetsAverage","#DeltaR^{j,j}_{avg}",30,1.4,3.3),"Evt_Dr_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_Dr_TaggedJetsAverage","#DeltaR^{b,b}_{avg}",30,0.8,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_Dr_minDrJets","#DeltaR^{j,j}_{min}",30,0.4,2.),"Evt_Dr_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_Dr_minDrTaggedJets","#DeltaR^{b,b}_{min}",30,0.4,3.3),"Evt_Dr_minDrTaggedJets",selection,label),
        #plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_HT","H_{T}",30,250.0,1400.0),"Evt_HT",selection,label),
        #plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_HT_jets","H_{T} of jets",30,200.0,1200.0),"Evt_HT_jets",selection,label),
        #plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_M2_JetsAverage","m^{j,j}_{avg}",30,40.0,500.0),"Evt_M2_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_M2_TaggedJetsAverage","m^{b,b}_{avg} [GeV]",30,40.0,500.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_M2_closestTo125TaggedJets","m^{b,b} closest to 125 [GeV]",30,30.0,250.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_M2_closestTo91TaggedJets","m^{b,b} closest to 91 [GeV]",30,30.0,250.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_M2_minDrJets","m(#DeltaR^{j,j}_{min}) [GeV]",30,20.0,200.0),"Evt_M2_minDrJets",selection,label),
    #plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_M2_minDrTaggedJets","m(#DeltaR^{b,b}_{min})",30,20.0,350.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_M_TaggedJetsAverage","m^{b}_{avg} [GeV]",30,5.0,30.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_M_Total","m_{tot} [GeV]",30,400.0,2000.0),"Evt_M_Total",selection,label),
        #plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_Pt_JetsAverage","p_{T, avg}^{j,j}",30,40.0,250.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_Pt_minDrJets","p_{T}(#DeltaR^{j,j}_{min}) [GeV]",30,40.0,500.0),"Evt_Pt_minDrJets",selection,label),
    #plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_Pt_minDrTaggedJets","p_{T}(#DeltaR^{b,b}_{min})",30,30.0,400.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_blr","b-tag likelihood ratio",30,0.2,1.0),"Evt_blr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_blr_transformed","transformed b-tag likelihood ratio",30,-2.0,10.0),"Evt_blr_transformed",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_h1","second Fox-Wolfram moment",30,-0.2,0.35),"Evt_h1",selection,label),
        #plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Jet_Pt_0","p_{T} of leading jet",30,30.0,500.0),"Jet_Pt[0]",selection,label),
        #plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Jet_Pt_3","p_{T} of fourth jet",30,30.0,80.0),"Jet_Pt[3]",selection,label),
        #plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Jet_Pt_4","p_{T} of fifth jet",30,30.0,70.0),"Jet_Pt[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_RecoTTZ_Chi2Total_log","t#bar{t}+Z reconstruction ln(#chi^{2})",30,-3.0,9.0),"RecoTTZ_Chi2Total_log",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_RecoTTZ_Chi2WHad_log","t#bar{t}+Z reconstruction ln(#chi^{2})(W_{had})",30,-8.0,9.0),"RecoTTZ_Chi2WHad_log",selection,label),
        #plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_RecoTTZ_TopLep_BJet_Pt","t#bar{t}+Z reconstruction p_{T}(b_{lep})",30,30.0,300.0),"RecoTTZ_TopLep_BJet_Pt",selection,label),
        ]

    if data:
        add_data_plots(plots=plots,data=data)
    return plots



def plots_4j_ge3t(data = None):
    label = "4 jets, \geq 3 b-tags"
    selection = "(N_Jets==4&&N_BTagsM>=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_CSV_2","third highest b-tag value",30,0.277,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_CSV_3","fourth highest b-tag value",30,0.0,0.2),"CSV[3]",selection,label),
    #plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_CSV_avg","average b-tag value",30,0.277,0.9),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_CSV_avg_tagged","average b-tag value of tagged jets",30,0.277,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_CSV_dev","average deviation of b-tag value",30,0.0,0.19),"Evt_CSV_dev",selection,label),
#plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_CSV_min","minimal b-tag value",30,0.0,0.2),"Evt_CSV_min",selection,label),
#plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_CSV_min_tagged","minimal b-tag value of tagged jets",30,0.277,1.0),"Evt_CSV_min_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_Deta_JetsAverage","#Delta#eta^{j,j}_{avg}",30,0.2,2.5),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_Deta_TaggedJetsAverage","#Delta#eta^{b,b}_{avg}",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_Dr_minDrJets","#DeltaR^{j,j}_{min}",30,0.4,2.5),"Evt_Dr_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_Dr_minDrTaggedJets","#DeltaR^{b,b}_{min}",30,0.4,3),"Evt_Dr_minDrTaggedJets",selection,label),
        #plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_HT_tags","H_{T} of tagged jets",30,100.0,1000.0),"Evt_HT_tags",selection,label),
        #plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_HT_wo_MET","H_{T} without MET",30,200.0,1200.0),"Evt_HT_wo_MET",selection,label),
        #plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_M2_JetsAverage","m^{j,j}_{avg}",30,40.0,500.0),"Evt_M2_JetsAverage",selection,label),
    #plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_M2_TaggedJetsAverage","m^{b,b}_{avg}",30,40.0,450.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_M2_closestTo125TaggedJets","m^{b,b} closest to 125 [GeV]",30,30.0,250.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_M2_closestTo91TaggedJets","m^{b,b} closest to 91 [GeV]",30,30.0,250.0),"Evt_M2_closestTo91TaggedJets",selection,label),
    #plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_M2_minDrJets","m(#DeltaR^{j,j}_{min})",30,20.0,200.0),"Evt_M2_minDrJets",selection,label),
    #plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_M2_minDrTaggedJets","m(#DeltaR^{b,b}_{min})",30,20.0,300.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_MHT","missing H_{T} [GeV]",30,0.0,250.0),"Evt_MHT",selection,label),
    #plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_MTW","m_{T}^{W}",30,0.0,250.0),"Evt_MTW",selection,label),
        #plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_M_JetsAverage","m^{j}_{avg}",30,5.0,30.0),"Evt_M_JetsAverage",selection,label),
    #plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_M_TaggedJetsAverage","m^{b}_{avg}",30,5.0,30.0),"Evt_M_TaggedJetsAverage",selection,label),
        #plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_M_Total","m_{tot}",30,250.0,2000.0),"Evt_M_Total",selection,label),
        #plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_Pt_JetsAverage","p_{T, avg}^{j,j}",30,40.0,300.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_Pt_TaggedJetsAverage","p_{T, avg}^{b,b} [GeV]",30,40.0,250.0),"Evt_Pt_TaggedJetsAverage",selection,label),
    #plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_Pt_minDrJets","p_{T}(#DeltaR^{j,j}_{min})",30,40.0,450.0),"Evt_Pt_minDrJets",selection,label),
    #plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_Pt_minDrTaggedJets","p_{T}(#DeltaR^{b,b}_{min})",30,0.0,400.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_blr_transformed","transformed b-tag likelihood ratio",30,-2.0,8.0),"Evt_blr_transformed",selection,label),
        #plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_h1","second fox wolfram moment",30,-0.2,0.35),"Evt_h1",selection,label),
        #plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Jet_Pt_3","p_{T} of fourth jet",30,30.0,90.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_RecoTTZ_Chi2Total_log","t#bar{t}+Z reconstruction ln(#chi^{2})",30,-3.0,8.0),"RecoTTZ_Chi2Total_log",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_RecoTTZ_Chi2WHad_log","t#bar{t}+Z reconstruction ln(#chi^{2})(W_{had})",30,-10.0,8.0),"RecoTTZ_Chi2WHad_log",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_RecoTTZ_TopHad_M","t#bar{t}+Z reconstruction m(t_{had}) [GeV]",30,100.0,500.0),"RecoTTZ_TopHad_M",selection,label),
    #plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_RecoTTZ_TopHad_Pt","t#bar{t}+Z reconstruction p_{T}(t_{had})",30,0.0,500.0),"RecoTTZ_TopHad_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_RecoTTZ_TopHad_W_M","t#bar{t}+Z reconstruction m(W_{had}) [GeV]",30,20.0,250.0),"RecoTTZ_TopHad_W_M",selection,label),
        ]

    if data:
        add_data_plots(plots=plots,data=data)
    return plots





def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_ge6j_ge3t(data)
    discriminatorPlots += plots_5j_ge3t(data)
    discriminatorPlots += plots_4j_ge3t(data)
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
    
