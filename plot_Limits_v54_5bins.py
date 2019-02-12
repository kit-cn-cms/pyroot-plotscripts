#!/usr/bin/python2

import sys
import getopt
import os
import imp
import importlib
import inspect
import ROOT
sys.path.append('pyroot-plotscripts-base')
sys.path.append('pyroot-plotscripts-base/limittools')

from scriptgenerator import *
from plotutils import *
from limittools import renameHistos
from limittools import addPseudoData
from limittools import addRealData
from limittools import makeDatacardsParallel
from limittools import calcLimits
from limittools import replaceQ2scale
import dnnInputVariableListV1

from analysisClass import *
from plotconfig_v53 import *


def main(argv):

    #Create analysis object with output name
    name='limits_v54_bins'
    analysis=Analysis(name,argv,'/nfs/dust/cms/user/kelmorab/plotscripts18/newJEC/pyroot-plotscripts/workdir/'+name+'/output_limitInput.root', signalProcess='ttH')
    print os.path.exists(analysis.rootFilePath), "AAAARgh"
    #analysis=Analysis(name,argv,'/nfs/dust/cms/user/kelmorab/plotscripts18/July18/pyroot-plotscripts/NOTDEFINED/output_limitInput.root ', signalProcess='ttH')

    analysis.plotBlinded=False
    analysis.makeSimplePlots=True
    analysis.makeMCControlPlots=True
    analysis.makeDataCards=True
    analysis.makeEventYields=True
    

    # Make sure proper plotconfig is loaded for either ttbb or ttH
    print "We will import the following plotconfig: ", analysis.getPlotConfig()
    # make sure plotconfig gets imported into global namespace
    #globals().update(importlib.import_module(analysis.getPlotConfig()).__dict__)



    ## NNFlow interface
    # Create and configure NNFlow interface
    # NNFlowInterfacePath=os.getcwd()+'/pyroot-plotscripts-base/NNFlowInterface.py'
    # NNFlowInterface = imp.load_source("NNFlowInterface",NNFlowInterfacePath).theInterface()
    # NNFlowInterface.setDebugOutput(True)
    # NNFlowInterface.setModelFolderPath('/nfs/dust/cms/user/mharrend/doktorarbeit/tensorflowModels/neural_network_v3/multiclass_ttlight_ttcc_ttb_tt2b_ttbb_ttH_top_20/model')
    # NNFlowInterface.setModelName('multiclass_ttlight_ttcc_ttb_tt2b_ttbb_ttH_top_20.ckpt')
    # NNFlowInterface.update()
    #
    # print "NNFlowInterfacePath: ", NNFlowInterfacePath

    analysis.printChosenOptions()


    # samples
    #samples=samplesControlPlots
    samples=samplesLimits

    samples_data=samplesDataControlPlots


    # Name of final discriminator, should not contain underscore
    discrname='finaldiscr'
    # define MEM discriminator variable
    memexp='(memDBp>=0.0)*(memDBp)+(memDBp<0.0)*(0.01)+(memDBp==1.0)*(0.01)'

    # define BDT output variables
    bdtweightpath="/nfs/dust/cms/user/kelmorab/Spring17BDTWeights/"
    bdtset="Spring17v1"
    # define additional variables necessary for selection in plotparallel
    additionalvariables=["Jet_Pt", "Muon_Pt", "Electron_Pt",
                         "Jet_Eta", "Muon_Eta", "Electron_Eta",
                         "Muon_Pt_BeForeRC","Electron_Pt_BeforeRun2Calibration","Electron_Eta_Supercluster",
                         "Jet_CSV", "Jet_Flav", "N_Jets", "Jet_E", "Jet_Phi", "Jet_M",
                         "Evt_Pt_PrimaryLepton","Evt_E_PrimaryLepton","Evt_M_PrimaryLepton","Evt_Phi_PrimaryLepton","Evt_Eta_PrimaryLepton",
                         "Evt_Phi_MET","Evt_Pt_MET",
                         "Weight_CSV","Weight_CSVLFup","Weight_CSVLFdown","Weight_CSVHFup","Weight_CSVHFdown","Weight_CSVHFStats1up","Weight_CSVHFStats1down",
                         "Weight_CSVLFStats1up","Weight_CSVLFStats1down","Weight_CSVHFStats2up","Weight_CSVHFStats2down","Weight_CSVLFStats2up","Weight_CSVLFStats2down",
                         "Weight_CSVCErr1up","Weight_CSVCErr1down","Weight_CSVCErr2up","Weight_CSVCErr2down","Evt_blr_ETH","Evt_blr_ETH_transformed",
                         
             			 'finalbdt_ljets_j4_t2:=Evt_HT_Jets',
             			 'finalbdt_ljets_j5_t2:=Evt_HT_Jets',
                         'finalbdt_ljets_j4_t3:='+bdtweightpath+'/weights_Final_43_'+bdtset+'.xml',
                         'finalbdt_ljets_j4_t4:='+bdtweightpath+'/weights_Final_44_'+bdtset+'.xml',
                         'finalbdt_ljets_j5_t3:='+bdtweightpath+'/weights_Final_53_'+bdtset+'.xml',
                         'finalbdt_ljets_j5_tge4:='+bdtweightpath+'/weights_Final_54_'+bdtset+'.xml',
                         'finalbdt_ljets_jge6_t2:='+bdtweightpath+'/weights_Final_62_'+bdtset+'.xml',
                         'finalbdt_ljets_jge6_t3:='+bdtweightpath+'/weights_Final_63_'+bdtset+'.xml',
                         'finalbdt_ljets_jge6_tge4:='+bdtweightpath+'/weights_Final_64_'+bdtset+'.xml',
                         ]
    
    dnnInputVariables=list(set(dnnInputVariableListV1.all_variables_list))
    dnnInputVariables.remove("memDBp")
    additionalvariables+=dnnInputVariables
    
    # append variables needed by NNFlow Interface
    #additionalvariables.extend(NNFlowInterface.getAdditionalVariablesList())
    print "Debug output: Print additional variables list: ", additionalvariables


        # selections

    # definition of categories
    categoriesJT=[
                  ("(N_Jets>=6&&N_BTagsM==2)","6j2t",""),
                  ("(N_Jets==4&&N_BTagsM==3)","4j3t",""),
                  ("(N_Jets==5&&N_BTagsM==3)","5j3t",""),
                  ("(N_Jets>=6&&N_BTagsM==3)","6j3t",""),
                  ("(N_Jets==4&&N_BTagsM>=4)","4j4t",""),
                  ("(N_Jets==5&&N_BTagsM>=4)","5j4t",""),
                  ("(N_Jets>=6&&N_BTagsM>=4)","6j4t","")
    ]
 
    # selections for categories
    categoriesJTsel="("+categoriesJT[0][0]
    for cat in categoriesJT[1:]:
      categoriesJTsel+="||"+cat[0]
    categoriesJTsel+=")"


    # category strings
    catstringJT="0"
    for i,cat in enumerate(categoriesJT):
        catstringJT+=("+"+str(i+1)+"*"+cat[0])



    # book plots
    plotlabel="1 lepton, #geq 4 jets, #geq 2 b-tags"
    #plotlabelboosted="#splitline{1 lepton, #geq 4 jets, #geq 2 b-tags}{#geq 1 C/A 1.5 jet p_{T} > 200 GeV}"
    plotselection="(N_Jets>=4&&N_BTagsM>=2)"
    plots=[
        #Plot(ROOT.TH1D("JT" ,"jet-tag categories",len(categoriesJT),0.5,0.5+len(categoriesJT)),catstringJT,categoriesJTsel,"1 lepton"),
        #Plot(ROOT.TH1D("BCAT" ,"jet-tag + boosted categories",len(categoriesJTB),0.5,0.5+len(categoriesJTB)),catstringJTB,categoriesJTBsel,"1 lepton"),
        Plot(ROOT.TH1D("N_Jets","Number of ak4 jets",11,3.5,14.5),"N_Jets",plotselection,plotlabel),
        Plot(ROOT.TH1D("N_BTagsM","Number of b-tags",4,1.5,5.5),"N_BTagsM",plotselection,plotlabel),
        #Plot(ROOT.TH1D("CSV0","B-tag of leading jet",22,-.1,1),"Jet_CSV[0]",plotselection,plotlabel),
        #Plot(ROOT.TH1D("CSV1","B-tag of second jet",22,-.1,1),"Jet_CSV[1]",plotselection,plotlabel),
        #Plot(ROOT.TH1D("CSV","B-tag of all jets",22,-.1,1),"Jet_CSV",plotselection,plotlabel),
        
        #Plot(ROOT.TH1D("eta1","#eta of leading jet",50,-2.5,2.5),"Jet_Eta[0]",plotselection,plotlabel),
        #Plot(ROOT.TH1D("eta2","#eta of second jet",50,-2.5,2.5),"Jet_Eta[1]",plotselection,plotlabel),
        #Plot(ROOT.TH1D("phij1","#phi of leading jet",64,-3.2,3.2),"Jet_Phi[0]",plotselection,plotlabel),
        #Plot(ROOT.TH1D("phij2","#phi of second jet",64,-3.2,3.2),"Jet_Phi[1]",plotselection,plotlabel),
        #Plot(ROOT.TH1D("Evt_HT_Jets","Sum p_{T} jets",75,0,1500),"Evt_HT_Jets",plotselection,plotlabel),
        Plot(ROOT.TH1D("ptalljets","p_{T} of all jets",60,0,300),"Jet_Pt",plotselection,plotlabel),
        Plot(ROOT.TH1D("etaalljets","#eta of all jets",60,-2.5,2.5),"Jet_Eta",plotselection,plotlabel),
        #Plot(ROOT.TH1D("pumvaalljets","PU MVA of all jets",60,0,1.0),"Jet_PileUpMVA",plotselection,plotlabel),
        #Plot(ROOT.TH1D("puidalljets","PU MVA of all jets",60,0,1.0),"Jet_PileUpID",plotselection,plotlabel),
        
        Plot(ROOT.TH1D("csvalljets","DeepCSV of all jets",44,-.1,1),"Jet_CSV",plotselection,plotlabel),
        Plot(ROOT.TH1D("leppt","lepton p_{T}",50,0,200),"LooseLepton_Pt[0]",plotselection,plotlabel),
        Plot(ROOT.TH1D("lepeta","lepton #eta",50,-2.5,2.5),"LooseLepton_Eta[0]",plotselection,plotlabel),
        Plot(ROOT.TH1D("elleppt","electron p_{T}",50,0,200),"Electron_Pt[0]",'Electron_Pt[0]>10',plotlabel),
        Plot(ROOT.TH1D("ellepeta","electron #eta",50,-2.5,2.5),"Electron_Eta[0]",'Electron_Pt[0]>10',plotlabel),
        Plot(ROOT.TH1D("muleppt","muon p_{T}",50,0,200),"Muon_Pt[0]",'Muon_Pt[0]>10',plotlabel),
        Plot(ROOT.TH1D("mulepeta","muon #eta",50,-2.5,2.5),"Muon_Eta[0]",'Muon_Pt[0]>10',plotlabel),
        
        #Plot(ROOT.TH1D("N_AK8_Jets","Number of ak8 jets",10,0.5,10.5),"N_AK8Jets",plotselection,plotlabel),
       
        
        
    ]
    
    
    plotlabelboosted="#splitline{1 lepton, #geq 4 jets, #geq 2 b-tags}{#geq 1 Ak8 jet p_{T} > 200 GeV}"
    plotselectionboosted="(N_Jets>=4&&N_BTagsM>=2&&N_AK8Jets>=1)*(AK8Jet_Pt>200)"
    plotsAK8jets=[

       Plot(ROOT.TH1D("ptallak8jets","p_{T} of all ak8 jets",50,0,1000),"AK8Jet_Pt",plotselectionboosted,plotlabel),
        Plot(ROOT.TH1D("doublecsvallak8jets","double btag of all ak8 jets",44,-.1,1),"AK8Jet_DoubleCSV",plotselectionboosted,plotlabel),
        Plot(ROOT.TH1D("etaallak8jets","#eta of all ak8 jets",60,-2.5,2.5),"AK8Jet_Eta",plotselectionboosted,plotlabel),
        #Plot(ROOT.TH1D("AK8Jet_EnergyCorrelation_b1N2","AK8Jet_EnergyCorrelation_b1N2",50,0,1),"AK8Jet_EnergyCorrelation_b1N2",plotselectionboosted,plotlabel),
        #Plot(ROOT.TH1D("AK8Jet_EnergyCorrelation_b1N3","AK8Jet_EnergyCorrelation_b1N3",50,0,1),"AK8Jet_EnergyCorrelation_b1N3",plotselectionboosted,plotlabel),
        #Plot(ROOT.TH1D("AK8Jet_EnergyCorrelation_b2N2","AK8Jet_EnergyCorrelation_b2N2",50,0,1),"AK8Jet_EnergyCorrelation_b2N2",plotselectionboosted,plotlabel),
        #Plot(ROOT.TH1D("AK8Jet_EnergyCorrelation_b2N3","AK8Jet_EnergyCorrelation_b2N3",50,0,1),"AK8Jet_EnergyCorrelation_b2N3",plotselectionboosted,plotlabel),

        Plot(ROOT.TH1D("AK8Jet_Puppi_Softdrop_Mass","AK8Jet_Puppi_Softdrop_Mass",35,50,400),"AK8Jet_Puppi_Softdrop_Mass",plotselectionboosted,plotlabel),
        #Plot(ROOT.TH1D("AK8Jet_tau21","AK8 jet tau 21",50,0,1),"AK8Jet_Tau2/AK8Jet_Tau1",plotselectionboosted,plotlabel),
        #Plot(ROOT.TH1D("AK8Jet_tau32","AK8 jet tau 32",50,0,1),"AK8Jet_Tau3/AK8Jet_Tau2",plotselectionboosted,plotlabel),
        Plot(ROOT.TH1D("AK8Subjet1_DeepCSV","AK8Subjet1_DeepCSV",50,0,1),"AK8Subjet1_DeepCSV",plotselectionboosted,plotlabel),
        Plot(ROOT.TH1D("AK8Subjet2_DeepCSV","AK8Subjet2_DeepCSV",50,0,1),"AK8Subjet2_DeepCSV",plotselectionboosted,plotlabel),
        Plot(ROOT.TH1D("AK8Subjet1_Pt","AK8Subjet1_Pt",50,30,300),"AK8Subjet1_Pt",plotselectionboosted,plotlabel),
        Plot(ROOT.TH1D("AK8Subjet2_Pt","AK8Subjet2_Pt",50,30,300),"AK8Subjet2_Pt",plotselectionboosted,plotlabel),
        
        
        
        ]
      
      
      
    plotsAdditional=[
        #Plot(ROOT.TH1D("CSV0NPVgeq20","B-tag of leading jet (NPV#geq20)",22,-.1,1),"Jet_CSV[0]",plotselection+"*(N_PrimaryVertices>=20)",plotlabel),
        #Plot(ROOT.TH1D("CSV1NPVgeq20","B-tag of second jet (NPV#geq20)",22,-.1,1),"Jet_CSV[1]",plotselection+"*(N_PrimaryVertices>=20)",plotlabel),
        #Plot(ROOT.TH1D("CSVNPVgeq20","B-tag of all jets (NPV#geq20)",22,-.1,1),"Jet_CSV",plotselection+"*(N_PrimaryVertices>=20)",plotlabel),

        #Plot(ROOT.TH1D("CSV0NPV15to20","B-tag of leading jet (15#leqNPV#leq20)",22,-.1,1),"Jet_CSV[0]",plotselection+"*(N_PrimaryVertices<=20 && N_PrimaryVertices>=15)",plotlabel),
        #Plot(ROOT.TH1D("CSV1NPV15to20","B-tag of second jet (15#leqNPV#leq20)",22,-.1,1),"Jet_CSV[1]",plotselection+"*(N_PrimaryVertices<=20 && N_PrimaryVertices>=15)",plotlabel),
        #Plot(ROOT.TH1D("CSVNPV15to20","B-tag of all jets (15#leqNPV#leq20)",22,-.1,1),"Jet_CSV",plotselection+"*(N_PrimaryVertices<=20 && N_PrimaryVertices>=15)",plotlabel),

        #Plot(ROOT.TH1D("CSV0NPV10to15","B-tag of leading jet (10#leqNPV#leq15)",22,-.1,1),"Jet_CSV[0]",plotselection+"*(N_PrimaryVertices<=15 && N_PrimaryVertices>=10)",plotlabel),
        #Plot(ROOT.TH1D("CSV1NPV10to15","B-tag of second jet (10#leqNPV#leq15)",22,-.1,1),"Jet_CSV[1]",plotselection+"*(N_PrimaryVertices<=15 && N_PrimaryVertices>=10)",plotlabel),
        #Plot(ROOT.TH1D("CSVNPV10to15","B-tag of all jets (10#leqNPV#leq15)",22,-.1,1),"Jet_CSV",plotselection+"*(N_PrimaryVertices<=15 && N_PrimaryVertices>=10)",plotlabel),

        #Plot(ROOT.TH1D("CSV0NPV0to10","B-tag of leading jet (0#leqNPV#leq10)",22,-.1,1),"Jet_CSV[0]",plotselection+"*(N_PrimaryVertices<=10 && N_PrimaryVertices>=0)",plotlabel),
        #Plot(ROOT.TH1D("CSV1NPV0to10","B-tag of second jet (0#leqNPV#leq10)",22,-.1,1),"Jet_CSV[1]",plotselection+"*(N_PrimaryVertices<=10 && N_PrimaryVertices>=0)",plotlabel),
        #Plot(ROOT.TH1D("CSVNPV0to10","B-tag of all jets (0#leqNPV#leq10)",22,-.1,1),"Jet_CSV",plotselection+"*(N_PrimaryVertices<=10 && N_PrimaryVertices>=0)",plotlabel),


        Plot(ROOT.TH1D("pt1","p_{T} of leading jet",50,0,500),"Jet_Pt[0]",plotselection,plotlabel),
        Plot(ROOT.TH1D("pt2","p_{T} of second jet",50,0,500),"Jet_Pt[1]",plotselection,plotlabel),
        Plot(ROOT.TH1D("pt3","p_{T} of third jet",40,0,400),"Jet_Pt[2]",plotselection,plotlabel),
        Plot(ROOT.TH1D("pt4","p_{T} of fourth jet",60,0,300),"Jet_Pt[3]",plotselection,plotlabel),
        Plot(ROOT.TH1D("pt5","p_{T} of fifth jet",40,0,200),"Jet_Pt[4]",plotselection,plotlabel),
        Plot(ROOT.TH1D("pt6","p_{T} of sixth jet",40,0,200),"Jet_Pt[5]",plotselection,plotlabel),
        #Plot(ROOT.TH1D("pt2tagged","p_{T} of second tagged jet",50,0,500),"TaggedJet_Pt[1]",plotselection,plotlabel),
        #Plot(ROOT.TH1D("pt1tagged","p_{T} of leading tagged jet",50,0,500),"TaggedJet_Pt[0]",plotselection,plotlabel),
        #Plot(ROOT.TH1D("pt3tagged","p_{T} of third tagged jet",40,0,400),"TaggedJet_Pt[2]",plotselection,plotlabel),
        #Plot(ROOT.TH1D("pt4tagged","p_{T} of fourth tagged jet",60,0,300),"TaggedJet_Pt[3]",plotselection,plotlabel),

        #Plot(ROOT.TH1D("Prescale_HLT_Ele27_eta2p1_WPTight_Gsf_vX","Prescale_HLT_Ele27_eta2p1_WPTight_Gsf_vX",50,0,2.0),"Prescale_HLT_Ele27_eta2p1_WPTight_Gsf_vX",plotselection,plotlabel),
        #Plot(ROOT.TH1D("Prescale_HLT_IsoMu22_vX","Prescale_HLT_IsoMu22_vX",50,0,2.0),"Prescale_HLT_IsoMu22_vX",plotselection,plotlabel),
        #Plot(ROOT.TH1D("Prescale_HLT_IsoTkMu22_vX","Prescale_HLT_IsoTkMu22_vX",50,0,2.0),"Prescale_HLT_IsoTkMu22_vX",plotselection,plotlabel),

        Plot(ROOT.TH1D("eliso","electron relative isolation",50,0,0.15),"Electron_RelIso[0]",plotselection,plotlabel),
        Plot(ROOT.TH1D("muiso","muon relative isolation",50,0,0.15),"Muon_RelIso[0]",plotselection,plotlabel),
        Plot(ROOT.TH1D("MET","missing transverse energy",50,0,200),"Evt_Pt_MET",plotselection,plotlabel),
        Plot(ROOT.TH1D("METphi","MET #phi",64,-3.2,3.2),"Evt_Phi_MET",plotselection,plotlabel),
        Plot(ROOT.TH1D("N_PrimaryVertices","Reconstructed primary vertices",26,-.5,50.5),"N_PrimaryVertices",plotselection,plotlabel),
        Plot(ROOT.TH1D("blrAll","B-tagging likelihood ratio",44,-6,10),"TMath::Log(Evt_blr_ETH/(1-Evt_blr_ETH))",plotselection,plotlabel),
        #Plot(ROOT.TH1D("Evt_M_MinDeltaRJets","dijet mass of closest jets",30,0.,150),"Evt_M_MinDeltaRJets",plotselection,plotlabel),
        #Plot(ROOT.TH1D("Evt_M_MinDeltaRTaggedJets","mass of closest tagged jets",45,0.,450),"Evt_M_MinDeltaRTaggedJets",plotselection,plotlabel),
        #Plot(ROOT.TH1D("Evt_Dr_MinDeltaRJets","#Delta R of closest jets",50,0.,5.0),"Evt_Dr_MinDeltaRJets",plotselection,plotlabel),
        #Plot(ROOT.TH1D("Evt_Dr_MinDeltaRTaggedJets","#Delta R of closest tagged jets",50,0.,5.0),"Evt_Dr_MinDeltaRTaggedJets",plotselection,plotlabel),
        #Plot(ROOT.TH1D("Evt_Jet_MaxDeta_Jets","max #Delta #eta (jet,jet)",50,0.,5.0),"Evt_Jet_MaxDeta_Jets",plotselection,plotlabel),
        #Plot(ROOT.TH1D("Evt_TaggedJet_MaxDeta_Jets","max #Delta #eta (tag,jet)",50,0.,5.0),"Evt_TaggedJet_MaxDeta_Jets",plotselection,plotlabel),
        #Plot(ROOT.TH1D("Evt_TaggedJet_MaxDeta_TaggedJets","max #Delta #eta (tag,tag)",60,0.,6.0),"Evt_TaggedJet_MaxDeta_TaggedJets",plotselection,plotlabel),
        ##Plot(ROOT.TH1D("Evt_H1","Evt_H1",60,-0.2,0.4),"Evt_H1",plotselection,plotlabel),
        #Plot(ROOT.TH1D("Evt_H2","Evt_H2",60,-0.2,0.4),"Evt_H2",plotselection,plotlabel),
        #Plot(ROOT.TH1D("Evt_H3","Evt_H3",50,-0.05,1.05),"Evt_H3",plotselection,plotlabel),
        #Plot(ROOT.TH1D("Evt_H4","Evt_H4",50,-0.15,0.35),"Evt_H4",plotselection,plotlabel),
        #Plot(ROOT.TH1D("Sphericity","Sphericity",50,0,1),"Evt_Sphericity",plotselection,plotlabel),
        #Plot(ROOT.TH1D("Aplanarity","Aplanarity",50,0,0.5),"Evt_Aplanarity",plotselection,plotlabel),
        #Plot(ROOT.TH1D("Evt_Deta_UntaggedJetsAverage","avg. #Delta #eta of untagged jets",50,0.,4.5),"Evt_Deta_UntaggedJetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1D("Evt_Deta_TaggedJetsAverage","avg. #Delta #eta of tagged jets",50,0.,4.5),"Evt_Deta_TaggedJetsAverage",plotselection,plotlabel),
    ]


    plotlabel="1 lepton, 4 jets, 2 b-tags"
    plotselection="((N_Jets==4&&N_BTagsM==2))"
    #plotselection="((N_Jets==4&&N_BTagsM==2)&&!"+boosted+")"

    plotprefix="4j2t"
    plots42=[
        Plot(ROOT.TH1D(plotprefix+"Evt_HT","Sum p_{T} jets",75,0,1500),"Evt_HT_Jets",plotselection,plotlabel),
    ]

    plotlabel="1 lepton, 5 jets, 2 b-tags"
    plotselection="((N_Jets==5&&N_BTagsM==2))"
    #plotselection="((N_Jets==5&&N_BTagsM==2)&&!"+boosted+")"

    plotprefix="s52_"
    plots52=[
        Plot(ROOT.TH1D(plotprefix+"Evt_HT","Sum p_{T} jets",75,0,1500),"Evt_HT_Jets",plotselection,plotlabel),
    ]

    plotlabel="1 lepton, 4 jets, 3 b-tags"
    plotselection=categoriesJT[1][0]
    plotprefix="s43_"
    plots43=[
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",30,0.6,1.0),"BDT_common5_input_Evt_CSV_Average",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"MEM","MEM",30,0.0,1.0),memexp,plotselection,plotlabel),
        
    ]


    plotlabel="1 lepton, 4 jets, 4 b-tags"
    plotselection=categoriesJT[4][0]
    plotprefix="s44_"
    # weights_Final_44_MEMBDTv2.xml
    plots44=[
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",20,0.6,1.0),"BDT_common5_input_Evt_CSV_Average",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"MEM","MEM",20,0.0,1.0),memexp,plotselection,plotlabel),
       
    ]


    plotlabel="1 lepton, 5 jets, 3 b-tags"
    plotselection=categoriesJT[2][0]
    plotprefix="s53_"
    plots53=[
                Plot(ROOT.TH1D(plotprefix+"MEM","MEM",30,0.0,1.0),memexp,plotselection,plotlabel),
     
    ]


    plotlabel="1 lepton, 5 jets, #geq4 b-tags"
    plotselection=categoriesJT[5][0]
    plotprefix="s54_"
    plots54=[
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",20,0.6,1.0),"BDT_common5_input_Evt_CSV_Average",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"MEM","MEM",20,0.0,1.0),memexp,plotselection,plotlabel),
       
    ]


    plotlabel="1 lepton, #geq6 jets, 2 b-tags"
    plotselection=categoriesJT[0][0]
    plotprefix="s62_"
    plots62=[
    
    ]


    plotlabel="1 lepton, #geq6 jets, 3 b-tags"
    plotselection=categoriesJT[3][0]
    plotprefix="s63_"
    plots63=[
        ###Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",30,0.6,1.0),"BDT_common5_input_Evt_CSV_Average",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"MEM","MEM",30,0.0,1.0),memexp,plotselection,plotlabel),
        
    ]

    plotlabel="1 lepton, #geq6 jets, #geq4 b-tags"
    plotselection=categoriesJT[6][0]
    plotprefix="s64"
    plots64=[
        Plot(ROOT.TH1D(plotprefix+"MEM","MEM",20,0.0,1.0),memexp,plotselection,plotlabel),

    ]
    
    plots+=plots64+plots63+plots54+plots53+plots44+plots43
    #discriminatorPlots=plots

        # prepare discriminators
    categories=[]
    nhistobins=[]
    minxvals=[]
    maxxvals=[]
    discrs =[]
    
    # DNN classes DNN outputs
    categorienames_MultiDNN=[
              # 3 tag and 4 tag events
              ("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==0)","ljets_j4_tge3_ttHnode",""),
              ("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==1)","ljets_j4_tge3_ttbbnode",""),
              ("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==2)","ljets_j4_tge3_tt2bnode",""),
              ("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==3)","ljets_j4_tge3_ttbnode",""),
              ("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==4)","ljets_j4_tge3_ttccnode",""),
              ("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==5)","ljets_j4_tge3_ttlfnode",""),
              
              ("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==0)","ljets_j5_tge3_ttHnode",""),             
              ("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==1)","ljets_j5_tge3_ttbbnode",""),             
              ("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==2)","ljets_j5_tge3_tt2bnode",""),             
              ("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==3)","ljets_j5_tge3_ttbnode",""),             
              ("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==4)","ljets_j5_tge3_ttccnode",""),             
              ("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==5)","ljets_j5_tge3_ttlfnode",""),             


              ("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==0)","ljets_jge6_tge3_ttHnode",""),
              ("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==1)","ljets_jge6_tge3_ttbbnode",""),
              ("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==2)","ljets_jge6_tge3_tt2bnode",""),
              ("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==3)","ljets_jge6_tge3_ttbnode",""),
              ("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==4)","ljets_jge6_tge3_ttccnode",""),
              ("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==5)","ljets_jge6_tge3_ttlfnode",""),

              # 3 tag and 4 tag events with MIN node output cuts
              #("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==0&&DNN_Out_4j3t_ttH>0.25)","ljets_j4_tge3_discrCut_ttHnode",""),
              #("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==1&&DNN_Out_4j3t_ttbarBB>0.2)","ljets_j4_tge3_discrCut_ttbbnode",""),
              #("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==2&&DNN_Out_4j3t_ttbar2B>0.3)","ljets_j4_tge3_discrCut_tt2bnode",""),
              #("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==3&&DNN_Out_4j3t_ttbarB>0.3)","ljets_j4_tge3_discrCut_ttbnode",""),
              #("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==4&&DNN_Out_4j3t_ttbarCC>0.2)","ljets_j4_tge3_discrCut_ttccnode",""),
              #("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==5&&DNN_Out_4j3t_ttbarlf>0.35)","ljets_j4_tge3_discrCut_ttlfnode",""),
              
              #("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==0&&DNN_Out_5j3t_ttH>0.25)","ljets_j5_tge3_discrCut_ttHnode",""),             
              #("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==1&&DNN_Out_5j3t_ttbarBB>0.2)","ljets_j5_tge3_discrCut_ttbbnode",""),             
              #("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==2&&DNN_Out_5j3t_ttbar2B>0.3)","ljets_j5_tge3_discrCut_tt2bnode",""),             
              #("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==3&&DNN_Out_5j3t_ttbarB>0.3)","ljets_j5_tge3_discrCut_ttbnode",""),             
              #("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==4&&DNN_Out_5j3t_ttbarCC>0.2)","ljets_j5_tge3_discrCut_ttccnode",""),             
              #("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==5&&DNN_Out_5j3t_ttbarlf>0.35)","ljets_j5_tge3_discrCut_ttlfnode",""),             


              #("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==0&&DNN_Out_6j3t_ttH>0.25)","ljets_jge6_tge3_discrCut_ttHnode",""),
              #("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==1&&DNN_Out_6j3t_ttbarBB>0.2)","ljets_jge6_tge3_discrCut_ttbbnode",""),
              #("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==2&&DNN_Out_6j3t_ttbar2B>0.3)","ljets_jge6_tge3_discrCut_tt2bnode",""),
              #("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==3&&DNN_Out_6j3t_ttbarB>0.3)","ljets_jge6_tge3_discrCut_ttbnode",""),
              #("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==4&&DNN_Out_6j3t_ttbarCC>0.2)","ljets_jge6_tge3_discrCut_ttccnode",""),
              #("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==5&&DNN_Out_6j3t_ttbarlf>0.35)","ljets_jge6_tge3_discrCut_ttlfnode",""),

              #### only 3 tag events 
              #("(N_Jets==4&&N_BTagsM==3&&DNN_4j3t_pred_class==0)","ljets_j4_t3_ttHnode",""),
              #("(N_Jets==4&&N_BTagsM==3&&DNN_4j3t_pred_class==1)","ljets_j4_t3_ttbbnode",""),
              #("(N_Jets==4&&N_BTagsM==3&&DNN_4j3t_pred_class==2)","ljets_j4_t3_tt2bnode",""),
              #("(N_Jets==4&&N_BTagsM==3&&DNN_4j3t_pred_class==3)","ljets_j4_t3_ttbnode",""),
              #("(N_Jets==4&&N_BTagsM==3&&DNN_4j3t_pred_class==4)","ljets_j4_t3_ttccnode",""),
              #("(N_Jets==4&&N_BTagsM==3&&DNN_4j3t_pred_class==5)","ljets_j4_t3_ttlfnode",""),
              
              #("(N_Jets==5&&N_BTagsM==3&&DNN_5j3t_pred_class==0)","ljets_j5_t3_ttHnode",""),             
              #("(N_Jets==5&&N_BTagsM==3&&DNN_5j3t_pred_class==1)","ljets_j5_t3_ttbbnode",""),             
              #("(N_Jets==5&&N_BTagsM==3&&DNN_5j3t_pred_class==2)","ljets_j5_t3_tt2bnode",""),             
              #("(N_Jets==5&&N_BTagsM==3&&DNN_5j3t_pred_class==3)","ljets_j5_t3_ttbnode",""),             
              #("(N_Jets==5&&N_BTagsM==3&&DNN_5j3t_pred_class==4)","ljets_j5_t3_ttccnode",""),             
              #("(N_Jets==5&&N_BTagsM==3&&DNN_5j3t_pred_class==5)","ljets_j5_t3_ttlfnode",""),             


              #("(N_Jets>=6&&N_BTagsM==3&&DNN_6j3t_pred_class==0)","ljets_jge6_t3_ttHnode",""),
              #("(N_Jets>=6&&N_BTagsM==3&&DNN_6j3t_pred_class==1)","ljets_jge6_t3_ttbbnode",""),
              #("(N_Jets>=6&&N_BTagsM==3&&DNN_6j3t_pred_class==2)","ljets_jge6_t3_tt2bnode",""),
              #("(N_Jets>=6&&N_BTagsM==3&&DNN_6j3t_pred_class==3)","ljets_jge6_t3_ttbnode",""),
              #("(N_Jets>=6&&N_BTagsM==3&&DNN_6j3t_pred_class==4)","ljets_jge6_t3_ttccnode",""),
              #("(N_Jets>=6&&N_BTagsM==3&&DNN_6j3t_pred_class==5)","ljets_jge6_t3_ttlfnode",""),

              #### only 4 tag events 
              #("(N_Jets==4&&N_BTagsM>=4&&DNN_4j3t_pred_class==0)","ljets_j4_tge4_ttHnode",""),
              #("(N_Jets==4&&N_BTagsM>=4&&DNN_4j3t_pred_class==1)","ljets_j4_tge4_ttbbnode",""),
              #("(N_Jets==4&&N_BTagsM>=4&&DNN_4j3t_pred_class==2)","ljets_j4_tge4_tt2bnode",""),
              #("(N_Jets==4&&N_BTagsM>=4&&DNN_4j3t_pred_class==3)","ljets_j4_tge4_ttbnode",""),
              #("(N_Jets==4&&N_BTagsM>=4&&DNN_4j3t_pred_class==4)","ljets_j4_tge4_ttccnode",""),
              #("(N_Jets==4&&N_BTagsM>=4&&DNN_4j3t_pred_class==5)","ljets_j4_tge4_ttlfnode",""),
              
              #("(N_Jets==5&&N_BTagsM>=4&&DNN_5j3t_pred_class==0)","ljets_j5_tge4_ttHnode",""),             
              #("(N_Jets==5&&N_BTagsM>=4&&DNN_5j3t_pred_class==1)","ljets_j5_tge4_ttbbnode",""),             
              #("(N_Jets==5&&N_BTagsM>=4&&DNN_5j3t_pred_class==2)","ljets_j5_tge4_tt2bnode",""),             
              #("(N_Jets==5&&N_BTagsM>=4&&DNN_5j3t_pred_class==3)","ljets_j5_tge4_ttbnode",""),             
              #("(N_Jets==5&&N_BTagsM>=4&&DNN_5j3t_pred_class==4)","ljets_j5_tge4_ttccnode",""),             
              #("(N_Jets==5&&N_BTagsM>=4&&DNN_5j3t_pred_class==5)","ljets_j5_tge4_ttlfnode",""),             


              #("(N_Jets>=6&&N_BTagsM>=4&&DNN_6j3t_pred_class==0)","ljets_jge6_tge4_ttHnode",""),
              #("(N_Jets>=6&&N_BTagsM>=4&&DNN_6j3t_pred_class==1)","ljets_jge6_tge4_ttbbnode",""),
              #("(N_Jets>=6&&N_BTagsM>=4&&DNN_6j3t_pred_class==2)","ljets_jge6_tge4_tt2bnode",""),
              #("(N_Jets>=6&&N_BTagsM>=4&&DNN_6j3t_pred_class==3)","ljets_jge6_tge4_ttbnode",""),
              #("(N_Jets>=6&&N_BTagsM>=4&&DNN_6j3t_pred_class==4)","ljets_jge6_tge4_ttccnode",""),
              #("(N_Jets>=6&&N_BTagsM>=4&&DNN_6j3t_pred_class==5)","ljets_jge6_tge4_ttlfnode",""),

              ]
    
    
    discrs_MultiDNN=[
# 3 and 4 tags        
'DNN_Out_4j3t_ttH',
'DNN_Out_4j3t_ttbarBB',
'DNN_Out_4j3t_ttbar2B',
'DNN_Out_4j3t_ttbarB',
'DNN_Out_4j3t_ttbarCC',
'DNN_Out_4j3t_ttbarlf',
'DNN_Out_5j3t_ttH',
'DNN_Out_5j3t_ttbarBB',
'DNN_Out_5j3t_ttbar2B',
'DNN_Out_5j3t_ttbarB',
'DNN_Out_5j3t_ttbarCC',
'DNN_Out_5j3t_ttbarlf',
'DNN_Out_6j3t_ttH',
'DNN_Out_6j3t_ttbarBB',
'DNN_Out_6j3t_ttbar2B',
'DNN_Out_6j3t_ttbarB',
'DNN_Out_6j3t_ttbarCC',
'DNN_Out_6j3t_ttbarlf',

    ]

    # 3 and 4 tags
    nhistobins_MultiDNN=[5,  5 , 5, 5,5, 5,
                         5,  5 , 5, 5,5, 5,
                         5,  5 , 5, 5,5, 5, ]
    minxvals_MultiDNN=[0.16, 0.16, 0.16, 0.2, 0.2, 0.2,
                       0.16, 0.16, 0.2, 0.2, 0.2, 0.2,
                       0.16, 0.16, 0.2, 0.2, 0.2, 0.2        ]
    maxxvals_MultiDNN=[0.55, 0.6, 0.5, 0.35, 0.35, 0.43,
                       0.67, 0.65, 0.47, 0.35, 0.3, 0.4,
                       0.65, 0.7, 0.55, 0.4, 0.32, 0.43     ]

    discrs+=discrs_MultiDNN
    nhistobins+=nhistobins_MultiDNN
    minxvals+=minxvals_MultiDNN
    maxxvals+=maxxvals_MultiDNN
    categories+=categorienames_MultiDNN
    

            
    # get input for plotting function
    plotPreselections= [c[0] for c in categories]
    binlabels= [c[1] for c in categories]

    discriminatorPlots=[]
    DNNplots=[]
    print len(discrs),len(plotPreselections),len(binlabels),len(nhistobins),len(minxvals),len(maxxvals),
    assert(len(set([len(discrs),len(plotPreselections),len(binlabels),len(nhistobins),len(minxvals),len(maxxvals)]))==1)
    print len(zip(discrs,plotPreselections,binlabels,nhistobins,minxvals,maxxvals))
    for discr,b,bl,nb,minx,maxx in zip(discrs,plotPreselections,binlabels,nhistobins,minxvals,maxxvals):
        DNNplots.append(Plot(ROOT.TH1F(discrname+"_"+bl,"final discriminator ("+bl+")",nb,minx,maxx),discr,b,bl))
    discriminatorPlots+=DNNplots
    
    
    
    systsamples=[]
    for sample in samples:
        for sysname,sysfilename in zip(otherSystNames,otherSystFileNames):
            thisnewsel=sample.selection
            systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),thisnewsel,sample.nick+sysname,samDict=sampleDict))
            # now add the UE and hdamp samples only for ttbar 
        if sample.nick.startswith("ttbarPlus") or sample.nick == "ttbarOther":
                for ue_hdamp, ue_hdamp_file in zip(hdamp_ue_systnames_tt_all, hdamp_ue_filenames_tt_all):
                    thisnewsel=sample.selection
                    if "HDAMP" in ue_hdamp and ue_hdamp.endswith("Up"):
                        thisnewsel+= "*((N_GenTopHad==1 && N_GenTopLep==1)* %s + !(N_GenTopHad==1 && N_GenTopLep ==1)*1)" %str(round(1.0399, 2))
                    systsamples.append(Sample(sample.name+ue_hdamp,sample.color,ue_hdamp_file,thisnewsel,nsample.nick+ue_hdamp,samDict=sampleDict))
        if sample.nick=="ttbarOther":
                for ue_hdamp, ue_hdamp_file in zip(hdamp_ue_systnames_tt_lf, hdamp_ue_filenames_tt_lf):
                    thisnewsel=sample.selection
                    if "HDAMP" in ue_hdamp and ue_hdamp.endswith("Up"):
                        thisnewsel+= "*((N_GenTopHad==1 && N_GenTopLep==1)* %s + !(N_GenTopHad==1 && N_GenTopLep ==1)*1)" %str(round(1.0399, 2))
                    systsamples.append(Sample(sample.name+ue_hdamp,sample.color,ue_hdamp_file,thisnewsel,sample.nick+ue_hdamp,samDict=sampleDict))
        elif sample.nick=="ttbarPlusCCbar":
                for ue_hdamp, ue_hdamp_file in zip(hdamp_ue_systnames_tt_cc, hdamp_ue_filenames_tt_cc):
                    thisnewsel=sample.selection
                    if "HDAMP" in ue_hdamp and ue_hdamp.endswith("Up"):
                        thisnewsel+= "*((N_GenTopHad==1 && N_GenTopLep==1)* %s + !(N_GenTopHad==1 && N_GenTopLep ==1)*1)" %str(round(1.0399, 2))
                    systsamples.append(Sample(sample.name+ue_hdamp,sample.color,ue_hdamp_file,thisnewsel,sample.nick+ue_hdamp,samDict=sampleDict))
        elif sample.nick=="ttbarPlusB":
                for ue_hdamp, ue_hdamp_file in zip(hdamp_ue_systnames_tt_b, hdamp_ue_filenames_tt_b):
                    thisnewsel=sample.selection
                    if "HDAMP" in ue_hdamp and ue_hdamp.endswith("Up"):
                        thisnewsel+= "*((N_GenTopHad==1 && N_GenTopLep==1)* %s + !(N_GenTopHad==1 && N_GenTopLep ==1)*1)" %str(round(1.0399, 2))
                    systsamples.append(Sample(sample.name+ue_hdamp,sample.color,ue_hdamp_file,thisnewsel,sample.nick+ue_hdamp,samDict=sampleDict))
        elif sample.nick=="ttbarPlus2B":
                for ue_hdamp, ue_hdamp_file in zip(hdamp_ue_systnames_tt_2b, hdamp_ue_filenames_tt_2b):
                    thisnewsel=sample.selection
                    if "HDAMP" in ue_hdamp and ue_hdamp.endswith("Up"):
                        thisnewsel+= "*((N_GenTopHad==1 && N_GenTopLep==1)* %s + !(N_GenTopHad==1 && N_GenTopLep ==1)*1)" %str(round(1.0399, 2))
                    systsamples.append(Sample(sample.name+ue_hdamp,sample.color,ue_hdamp_file,thisnewsel,sample.nick+ue_hdamp,samDict=sampleDict))
        elif sample.nick=="ttbarPlusBBbar":
                for ue_hdamp, ue_hdamp_file in zip(hdamp_ue_systnames_tt_bb, hdamp_ue_filenames_tt_bb):
                    if "HDAMP" in ue_hdamp and ue_hdamp.endswith("Up"):
                        thisnewsel+= "*((N_GenTopHad==1 && N_GenTopLep==1)* %s + !(N_GenTopHad==1 && N_GenTopLep ==1)*1)" %str(round(1.0399, 2))
                    systsamples.append(Sample(sample.name+ue_hdamp,sample.color,ue_hdamp_file,thisnewsel,sample.nick+ue_hdamp,samDict=sampleDict))
                                
        

    ## WARNING: Adjust Slice for samples if changing ttbar contributions


    #allsamples=samples+systsamples
    #allsystnames=weightSystNames+otherSystNames+PSSystNames
    allsamples=samples
    allsystnames=weightSystNames+otherSystNames
    print allsystnames

    # plot everything, except during drawParallel step
    # Create file for data cards
    if analysis.doDrawParallel==False or analysis.plotNumber == None :
        #print type(analysis.rootFilePath), analysis.rootFilePath
        #print os.path.exists(analysis.rootFilePath)
        #raw_input()
        if not os.path.exists(analysis.rootFilePath):
        #if False:
            
            print "Doing plotParallel step since root file was not found.", analysis.rootFilePath
            THEoutputpath=plotParallel(name,350000,discriminatorPlots,samples+samples_data+systsamples,[''],['1.'],weightSystNames,systWeights,additionalvariables,[["memDB","/nfs/dust/cms/user/kelmorab/DataBases/MemDataBase_ttH_2018_newJEC",True]],"/nfs/dust/cms/user/kelmorab/plotscripts18/newJEC/pyroot-plotscripts/treejson_newJEC_V1.json",otherSystNames,addCodeInterfacePaths=["pyroot-plotscripts-base/dNNInterface_MattiSchrode_KIT_cool.py"],cirun=False,StopAfterCompileStep=False,haddParallel=True,useGenWeightNormMap=True,useThisSampleForVariableSetup=samples[9])
            #outputpath=plotParallel(name,5000000,discriminatorPlots,samples+samples_data+systsamples,[''],['1.'],weightSystNames,systWeights,additionalvariables,[["memDB","/nfs/dust/cms/user/kelmorab/DataBases/MemDataBase_Spring17_V1",False]],"/nfs/dust/cms/user/kelmorab/treeJsons/treejson_Spring17_v5_08102017.json",otherSystNames+PSSystNames+QCDSystNames,addCodeInterfacePaths=["pyroot-plotscripts-base/dNNInterface_V6.py"],cirun=False)
            
            if type(THEoutputpath)==str:
              outputpath=THEoutputpath
            else:
              outputpath=THEoutputpath[0]
              
            # Allow start of an improved rebinning algorithm
            if analysis.getActivatedOptimizedRebinning():
              if analysis.getSignalProcess() == 'ttbb':
                # samples[0:2]: tt+bb, tt+b, tt+2b as signal for S over b normalization
                optimizeBinning(outputpath,signalsamples=[samples[0:3]], backgroundsamples=samples[3:],additionalSamples=samples_data, plots=discriminatorPlots, systnames=allsystnames, minBkgPerBin=2.0, optMode=analysis.getOptimzedRebinning(),considerStatUnc=False, maxBins=20, minBins=2,verbosity=2)
              elif analysis.getSignalProcess() == 'ttH':
                # samples: ttH as signal. ttH_bb, ttH_XX as additional samples together with data. Rest: background samples
                optimizeBinning(outputpath,signalsamples=[samples[0]], backgroundsamples=samples[9:],additionalSamples=samples[1:9]+samples_data, plots=discriminatorPlots, systnames=allsystnames, minBkgPerBin=2.0, optMode=analysis.getOptimzedRebinning(),considerStatUnc=False, maxBins=20, minBins=2,verbosity=2)
              else:
                print 'Warning: Could not find signal process.'

            ## Deactivate check bins functionality in renameHistos if additional plot variables are added via analysis class
            ##renameHistos(outputpath,outputpath[:-5]+'_limitInput.root',allsystnames,analysis.getCheckBins(),False)
            #renamedPath=outputpath[:-5]+'_syst.root'
            #if os.path.exists(renamedPath):
              ##if askYesNo('renamedFileExists. Repeat renaming?'):
              ##  renameHistos(outputpath,renamedPath,allsystnames,analysis.getCheckBins(),False)
              #print "renamed file already exists"
            #else:
              #renameHistos(outputpath,renamedPath,allsystnames,analysis.getCheckBins(),False)
            # hadd histo files before renaming. The histograms are actually already renamed. But the checkbins thingy will not have been done yet.
            print "hadding from wildcard"
            haddFilesFromWildCard(outputpath,outputpath[:-11]+"/HaddOutputs/*.root",totalNumberOfHistosNeedsToRemainTheSame=True)
            # Deactivate check bins functionality in renameHistos if additional plot variables are added via analysis class
            renamedPath=outputpath[:-5]+'_limitInput.root'
            if os.path.exists(renamedPath):
              #if askYesNo('renamedFileExists. Repeat renaming?'):
              #  renameHistos(outputpath,renamedPath,allsystnames,analysis.getCheckBins(),False)
              print "renamed file already exists"
            else:
              if type(THEoutputpath)==str:
                renameHistos(outputpath,renamedPath,allsystnames,checkBins=True,prune=True,Epsilon=0.0)
              else:
                renameHistos(THEoutputpath[1:],renamedPath,allsystnames,checkBins=True,prune=True,Epsilon=0.0)

            #addRealDataAllHistos(renamedPath,[s.nick for s in samples_data],discriminatorPlots,forceOverwrite=True) # use this version for all histograms even if they do not follow the cat_disc_var naming scheme
            addRealData(outputpath[:-5]+'_limitInput.root',[s.nick for s in samples_data],binlabels,discrname)
            #addPseudoData(outputpath[:-5]+'_limitInput.root',[s.nick for s in samples[9:]],binlabels,allsystnames,discrname)
            #outputpath=outputpath[:-5]+'_limitInput.root'
            outputpath=outputpath[:-5]+'_limitInput.root'
        else:
            print "Not doing plotParallel step since root file was found.", 
            outputpath=analysis.rootFilePath
            print outputpath
        print "outputpath: ", outputpath
    else:
        # Warning This time output path refers only to output.root
        # ToDo: Fix usage of output path and output limit path
        if not os.path.exists(analysis.rootFilePath[:-16]+'.root'):
            workdir=os.getcwd()+'/workdir/'+name
            outputpath=workdir+'/output.root'
        else:
            outputpath=analysis.rootFilePath[:-16]+'.root'

    # make datacards
    if (analysis.doDrawParallel==False or analysis.plotNumber == None) and analysis.makeDataCards == True :
        #TODO
        # 1. Implement small Epsilon case
        # 2. Implement consisted Bin-by-Bin uncertainties
        #addRealData(outputpath,[s.nick for s in samples_data],binlabels,discrname)
        print "Making Data cards."
        makeDatacardsParallel(outputpath,name+'/'+name+'_datacard',binlabels,doHdecay=True,discrname=discrname,datacardmaker="mk_datacard_JESTest13TeVPara")


    # Invoke drawParallel step
    if analysis.doDrawParallel==True and analysis.plotNumber == None :
        # Hand over opts to keep commandline options
        print 'Starting DrawParallel'
        DrawParallel(discriminatorPlots,name,os.path.realpath(inspect.getsourcefile(lambda:0)),analysis.opts)

    # belongs to DrawParallel
    if analysis.doDrawParallel==True and analysis.plotNumber != None :
        discriminatorPlots=[discriminatorPlots[int(analysis.plotNumber)]]



    # Lists needed later, produce them only if needed, so check if subsequent step comes
    if (analysis.doDrawParallel==False or analysis.plotNumber != None) and (analysis.makeSimplePlots==True or analysis.makeMCControlPlots==True or analysis.makeEventYields==True):
        print 'Create lists needed later'
        listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,discriminatorPlots,1)
        print listOfHistoLists
        print ""
        lolT=transposeLOL(listOfHistoLists)
        listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,discriminatorPlots,1)
        listOfHistoListsPseudoData=createHistoLists_fromSuperHistoFile(outputpath,[samples[0]]+samples[9:],discriminatorPlots,1)

    # plot simple MC plots
    if (analysis.doDrawParallel==False or analysis.plotNumber != None) and analysis.makeSimplePlots==True :
        print "Making simple MC plots."
        writeLOLAndOneOnTop(transposeLOL(lolT[9:]),samples[9:],lolT[0],samples[0],-1,name+'/'+name+'_controlplots')
        writeListOfHistoListsAN(transposeLOL([lolT[0]]+lolT[9:]),[samples[0]]+samples[9:],"",name+'/'+name+'_shapes',True,False,False,'histo',False,True,False)
        #writeListOfHistoListsAN(transposeLOL([lolT[0]]+lolT[9:]),[samples[0]]+samples[9:],"",name+'/'+name+'_shapes',True,False,False,'histo',False,True,False)

    # Make MC Control plots
    if (analysis.doDrawParallel==False or analysis.plotNumber != None) and analysis.makeMCControlPlots==True :
        print "Making MC Control plots"
        print "skipping"
        lll=createLLL_fromSuperHistoFileSyst(outputpath,samples[9:],discriminatorPlots,errorSystNames)
        #lllCSV=createLLL_fromSuperHistoFileSyst(outputpath,samples[1:],discriminatorPlots,errorSystNamesCSV)
        #lllJES=createLLL_fromSuperHistoFileSyst(outputpath,samples[1:],discriminatorPlots,errorSystNamesJES)
        #lllGEN=createLLL_fromSuperHistoFileSyst(outputpath,samples[1:],discriminatorPlots,errorSystNamesGenWeights)
        
        labels=[plot.label for plot in discriminatorPlots]
        print ""
        print lll
        print ""
        print lolT
        print ""
        print listOfHistoListsData
        plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[9:]),samples[9:],lolT[0],samples[0],-2,name,[[lll,3354,ROOT.kBlack,True]],False,labels,True,analysis.plotBlinded,verbosity=0)
        plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[9:]),samples[9:],lolT[0],samples[0],-2,name+'_LOG',[[lll,3354,ROOT.kBlack,True]],True,labels,True,analysis.plotBlinded,verbosity=0)
        plotDataMCanWsyst(listOfHistoListsPseudoData,transposeLOL(lolT[9:]),samples[9:],lolT[0],samples[0],-2,name+'_PseudoData',[[lll,3354,ROOT.kBlack,True]],False,labels,True,analysis.plotBlinded,verbosity=0)
        plotDataMCanWsyst(listOfHistoListsPseudoData,transposeLOL(lolT[9:]),samples[9:],lolT[0],samples[0],-2,name+'_PseudoData'+'_LOG',[[lll,3354,ROOT.kBlack,True]],True,labels,True,analysis.plotBlinded,verbosity=0)
        
    # Make yield table
    if (analysis.doDrawParallel==False or analysis.plotNumber != None) and analysis.makeEventYields==True :
        print "Making yield table."
        print "Will do only some plots"
        for hld,hl in zip(listOfHistoListsData,listOfHistoLists):
          #if not ("JT" in hld[0].GetName() or "N_Jets" in hld[0].GetName()) or ("node" in hld[0].GetName() and not "minVal" in hld[0].GetName()):
          if not ("JT" in hld[0].GetName() or "N_Jets" in hld[0].GetName()) or ("node" in hld[0].GetName() and not "minVal" in hld[0].GetName()):
            continue
          else:
            hldName = hld[0].GetName()
            for h in hld+hl:
              for i,cat in enumerate(categoriesJT):
                h.GetXaxis().SetBinLabel(i+1,cat[1])
            tablepath=("/".join((outputpath.split('/'))[:-1]))+"/"+name+hldName+"_yields"
            eventYields(hld,hl,samples,tablepath)



if __name__ == "__main__":

   MainClock=ROOT.TStopwatch()
   MainClock.Start()
   main(sys.argv[1:])
   print "TOTAL Elapsed time since beginning of analysis script", MainClock.RealTime()
