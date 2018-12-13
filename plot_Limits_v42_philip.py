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
from limittools import addRealDataAllHistos
from limittools import addPseudoDataAllHistos
from limittools import makeDatacardsParallel
from limittools import calcLimits
from limittools import replaceQ2scale
import dnnInputVariableListV1

from analysisClass import *
from plotconfig_v42 import *


def main(argv):

    #Create analysis object with output name
    name='limits_v42_1D_philip'
    analysis=Analysis(name,argv,'/nfs/dust/cms/user/pkeicher/ttH_2018/pyroot-plotscripts/workdir/'+name+'/output_limitInput.root', signalProcess='ttH')
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
    Plot(ROOT.TH1D(plotprefix+"forth_jet_pt","forth_jet_pt",30,30.0249652863,309.913513184),"Jet_Pt[3]",plotselection,plotlabel),
    Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_transverse_sphericity_jets","BDT_common5_input_transverse_sphericity_jets",30,0,1),"BDT_common5_input_transverse_sphericity_jets",plotselection,plotlabel),
    Plot(ROOT.TH1D(plotprefix+"Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",30,31.2903900146,933.360778809),"Evt_M2_TaggedJetsAverage",plotselection,plotlabel),
    Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h3","BDT_common5_input_h3",30,-0.204661205411,0.267688572407),"BDT_common5_input_h3",plotselection,plotlabel),
    Plot(ROOT.TH1D(plotprefix+"MEM","MEM",30,0.,1.),memexp,plotselection,plotlabel),
    Plot(ROOT.TH1D(plotprefix+"second_highest_CSV","second_highest_CSV",30,-0.1,1),"CSV[1]",plotselection,plotlabel),
    Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Min","Evt_CSV_Min",30,-0.10000000149,0.49388423562),"Evt_CSV_Min",plotselection,plotlabel),
    Plot(ROOT.TH1D(plotprefix+"second_jet_Eta","second_jet_Eta",30,-2.5,2.5),"Jet_Eta[1]",plotselection,plotlabel),
    Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH_transformed","Evt_blr_ETH_transformed",30,-11.6342458725,7.72277259827),"Evt_blr_ETH_transformed",plotselection,plotlabel),
    Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRTaggedJets","#Delta R of closest tagged jets",50,0.,5.0),"Evt_Dr_MinDeltaRTaggedJets",plotselection,plotlabel),
    Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Average_Tagged","Evt_CSV_Average_Tagged",30,0.510232031345,0.999261438847),"Evt_CSV_Average_Tagged",plotselection,plotlabel),
    Plot(ROOT.TH1D(plotprefix+"secon_jet_CSV","secon_jet_CSV",30,-0.1,1),"Jet_CSV[1]",plotselection,plotlabel),
    Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Average","Evt_CSV_Average",30,-0.1,1),"Evt_CSV_Average",plotselection,plotlabel),
    Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Min_Tagged","Evt_CSV_Min_Tagged",30,-0.1,1),"Evt_CSV_Min_Tagged",plotselection,plotlabel),
    Plot(ROOT.TH1D(plotprefix+"N_BTagsT","N_BTagsT",30,3,9),"N_BTagsT",plotselection,plotlabel),
    Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_HT_tag","BDT_common5_input_HT_tag",30,0,500),"BDT_common5_input_HT_tag",plotselection,plotlabel),
    Plot(ROOT.TH1D(plotprefix+"Evt_M_JetsAverage","Evt_M_JetsAverage",30,3.29856276512,44.2075080872),"Evt_M_JetsAverage",plotselection,plotlabel),

    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_tag","BDT_common5_input_maxeta_jet_tag",30,0.0153507888317,1.70412755013),"BDT_common5_input_maxeta_jet_tag",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h1","BDT_common5_input_h1",30,-0.212307035923,0.35206374526),"BDT_common5_input_h1",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_Eta_JetsAverage","Evt_Eta_JetsAverage",30,-2.12773942947,2.08718776703),"Evt_Eta_JetsAverage",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",30,17.7154808044,695.161621094),"Evt_M_MinDeltaRTaggedJets",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",30,0.00678177690133,3.07771205902),"Evt_Deta_TaggedJetsAverage",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRJets","Evt_M_MinDeltaRJets",30,17.5331268311,525.740600586),"Evt_M_MinDeltaRJets",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRTaggedJets","Evt_Pt_MinDeltaRTaggedJets",30,3.66161417961,1058.72937012),"Evt_Pt_MinDeltaRTaggedJets",plotselection,plotlabel),
    # # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_best_higgs_mass","BDT_common5_input_best_higgs_mass",30,-9.89999961853,-9.89999961853),"BDT_common5_input_best_higgs_mass",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MET","BDT_common5_input_MET",30,20.0141143799,797.977478027),"BDT_common5_input_MET",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_Deta_JetsAverage","BDT_common5_input_Evt_Deta_JetsAverage",30,0.0160637889057,2.87777733803),"BDT_common5_input_Evt_Deta_JetsAverage",plotselection,plotlabel),
    # # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dEta_fn","BDT_common5_input_dEta_fn",30,0.0,0.0),"BDT_common5_input_dEta_fn",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_highest_btag","BDT_common5_input_second_highest_btag",30,0.495228797197,0.999705314636),"BDT_common5_input_second_highest_btag",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",30,0.39203491807,0.861888766289),"BDT_common5_input_Evt_CSV_Average",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_jet_pt","BDT_common5_input_fourth_jet_pt",30,30.0002193451,250.223922729),"BDT_common5_input_fourth_jet_pt",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_Jet_MaxDeta_Jets","Evt_Jet_MaxDeta_Jets",30,0.121551506221,4.91741514206),"Evt_Jet_MaxDeta_Jets",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h2","BDT_common5_input_h2",30,-0.143690168858,0.323251962662),"BDT_common5_input_h2",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_HT","BDT_common5_input_HT",30,132.306671143,1587.16906738),"BDT_common5_input_HT",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","BDT_common5_input_closest_tagged_dijet_mass",30,17.7154808044,695.161621094),"BDT_common5_input_closest_tagged_dijet_mass",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_lowest_btag","BDT_common5_input_lowest_btag",30,0.494100779295,0.998709440231),"BDT_common5_input_lowest_btag",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_min_dr_tagged_jets","BDT_common5_input_min_dr_tagged_jets",30,0.385989964008,3.63247466087),"BDT_common5_input_min_dr_tagged_jets",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_highest_btag","BDT_common5_input_third_highest_btag",30,0.494100779295,0.998709440231),"BDT_common5_input_third_highest_btag",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_aplanarity","BDT_common5_input_aplanarity",30,0.000618859136011,0.422741800547),"BDT_common5_input_aplanarity",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_jet","BDT_common5_input_maxeta_jet_jet",30,0.0153507888317,1.70412755013),"BDT_common5_input_maxeta_jet_jet",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",30,4.77056932449,86.1115493774),"Evt_M_TaggedJetsAverage",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_E_PrimaryLepton","Evt_E_PrimaryLepton",30,26.0633449554,1159.93566895),"Evt_E_PrimaryLepton",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","BDT_common5_input_dr_between_lep_and_closest_jet",30,0.401996731758,3.46800780296),"BDT_common5_input_dr_between_lep_and_closest_jet",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_btag_disc_btags","BDT_common5_input_avg_btag_disc_btags",30,0.510232031345,0.999261498451),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_M3","BDT_common5_input_M3",30,43.2903137207,1823.53161621),"BDT_common5_input_M3",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","BDT_common5_input_pt_all_jets_over_E_all_jets",30,0.214973345399,0.991197884083),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h0","BDT_common5_input_h0",30,0.0868039056659,0.374159216881),"BDT_common5_input_h0",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_Eta_PrimaryLepton","Evt_Eta_PrimaryLepton",30,-2.39761805534,2.39831805229),"Evt_Eta_PrimaryLepton",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_M_MedianTaggedJets","Evt_M_MedianTaggedJets",30,28.5928039551,1081.63232422),"Evt_M_MedianTaggedJets",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_M3","Evt_M3",30,43.2903137207,1823.53161621),"Evt_M3",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH","Evt_blr_ETH",30,8.8574261099e-06,0.999557554722),"Evt_blr_ETH",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_Pt_PrimaryLepton","Evt_Pt_PrimaryLepton",30,26.0189743042,482.720306396),"Evt_Pt_PrimaryLepton",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_all_sum_pt_with_met","BDT_common5_input_all_sum_pt_with_met",30,210.941055298,2186.35107422),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","BDT_common5_input_avg_dr_tagged_jets",30,0.529255628586,4.04872560501),"BDT_common5_input_avg_dr_tagged_jets",plotselection,plotlabel),
    # # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fifth_highest_CSV","BDT_common5_input_fifth_highest_CSV",30,-1.0,-1.0),"BDT_common5_input_fifth_highest_CSV",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonJet","Evt_Dr_MinDeltaRLeptonJet",30,0.401996731758,3.46800780296),"Evt_Dr_MinDeltaRLeptonJet",plotselection,plotlabel),
    # # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",30,-99.0,348.864746094),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",30,0.0,348.864746094),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","BDT_common5_input_dev_from_avg_disc_btags",30,1.11453601903e-07,0.0563487485051),"BDT_common5_input_dev_from_avg_disc_btags",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_tag_tag","BDT_common5_input_maxeta_tag_tag",30,0.00584077835083,1.54131996632),"BDT_common5_input_maxeta_tag_tag",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_jet_pt","BDT_common5_input_second_jet_pt",30,31.6028022766,586.674255371),"BDT_common5_input_second_jet_pt",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRJets","Evt_Dr_MinDeltaRJets",30,0.385989964008,3.03341078758),"Evt_Dr_MinDeltaRJets",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",30,0.868540763855,3.79916119576),"Evt_Dr_JetsAverage",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Mlb","BDT_common5_input_Mlb",30,16.8300380707,542.308776855),"BDT_common5_input_Mlb",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_Dr_TaggedJetsAverage","Evt_Dr_TaggedJetsAverage",30,0.529255568981,4.04872560501),"Evt_Dr_TaggedJetsAverage",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_first_jet_pt","BDT_common5_input_first_jet_pt",30,34.1141548157,929.538879395),"BDT_common5_input_first_jet_pt",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonTaggedJet","Evt_Dr_MinDeltaRLeptonTaggedJet",30,0.401996731758,3.77427482605),"Evt_Dr_MinDeltaRLeptonTaggedJet",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRJets","Evt_Pt_MinDeltaRJets",30,9.22135257721,1058.72937012),"Evt_Pt_MinDeltaRJets",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_sphericity","BDT_common5_input_sphericity",30,0.0127841513604,0.931054353714),"BDT_common5_input_sphericity",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_highest_btag","BDT_common5_input_fourth_highest_btag",30,-0.10000000149,0.49388423562),"BDT_common5_input_fourth_highest_btag",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MHT","BDT_common5_input_MHT",30,0.857420027256,660.852966309),"BDT_common5_input_MHT",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_invariant_mass_of_everything","BDT_common5_input_invariant_mass_of_everything",30,249.554244995,3475.234375),"BDT_common5_input_invariant_mass_of_everything",plotselection,plotlabel),
    ]


    plotlabel="1 lepton, 4 jets, 4 b-tags"
    plotselection=categoriesJT[4][0]
    plotprefix="s44_"
    # weights_Final_44_MEMBDTv2.xml
    plots44=[
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",20,0.6,1.0),"BDT_common5_input_Evt_CSV_Average",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"MEM","MEM",20,0.0,1.0),memexp,plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_Deta_JetsAverage","BDT_common5_input_Evt_Deta_JetsAverage",20,0.0,3.4),"BDT_common5_input_Evt_Deta_JetsAverage",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_HT","BDT_common5_input_HT",20,0.0,1000.0),"BDT_common5_input_HT",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_M3","BDT_common5_input_M3",20,0.0,600.0),"BDT_common5_input_M3",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MET","BDT_common5_input_MET",20,0.0,300.0),"BDT_common5_input_MET",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MHT","BDT_common5_input_MHT",20,0.0,250.0),"BDT_common5_input_MHT",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Mlb","BDT_common5_input_Mlb",20,0.0,250.0),"BDT_common5_input_Mlb",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_all_sum_pt_with_met","BDT_common5_input_all_sum_pt_with_met",20,200,900.0),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_aplanarity","BDT_common5_input_aplanarity",20,0.0,0.4),"BDT_common5_input_aplanarity",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_btag_disc_btags","BDT_common5_input_avg_btag_disc_btags",20,0.8,1.0),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","BDT_common5_input_avg_dr_tagged_jets",20,0.0,5.0),"BDT_common5_input_avg_dr_tagged_jets",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_best_higgs_mass","BDT_common5_input_best_higgs_mass",20,0.0,200.0),"BDT_common5_input_best_higgs_mass",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","BDT_common5_input_closest_tagged_dijet_mass",20,0.0,250.0),"BDT_common5_input_closest_tagged_dijet_mass",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dEta_fn","BDT_common5_input_dEta_fn",20,0.0,5.0),"BDT_common5_input_dEta_fn",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","BDT_common5_input_dev_from_avg_disc_btags",20,0.0,0.02),"BDT_common5_input_dev_from_avg_disc_btags",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","BDT_common5_input_dr_between_lep_and_closest_jet",20,0.0,3.0),"BDT_common5_input_dr_between_lep_and_closest_jet",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fifth_highest_CSV","BDT_common5_input_fifth_highest_CSV",20,-0.1,1.0),"BDT_common5_input_fifth_highest_CSV",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_first_jet_pt","BDT_common5_input_first_jet_pt",20,0.0,500.0),"BDT_common5_input_first_jet_pt",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_highest_btag","BDT_common5_input_fourth_highest_btag",20,0.8,1.0),"BDT_common5_input_fourth_highest_btag",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_jet_pt","BDT_common5_input_fourth_jet_pt",20,0.0,300.0),"BDT_common5_input_fourth_jet_pt",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h0","BDT_common5_input_h0",20,0.15,0.45),"BDT_common5_input_h0",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h1","BDT_common5_input_h1",20,-0.2,0.2),"BDT_common5_input_h1",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h2","BDT_common5_input_h2",20,-0.2,0.3),"BDT_common5_input_h2",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h3","BDT_common5_input_h3",20,-0.2,0.2),"BDT_common5_input_h3",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_invariant_mass_of_everything","BDT_common5_input_invariant_mass_of_everything",20,500.0,1200.0),"BDT_common5_input_invariant_mass_of_everything",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_lowest_btag","BDT_common5_input_lowest_btag",20,0.8,1.0),"BDT_common5_input_lowest_btag",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_jet","BDT_common5_input_maxeta_jet_jet",20,0.0,2.0),"BDT_common5_input_maxeta_jet_jet",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_tag","BDT_common5_input_maxeta_jet_tag",20,0.0,2.0),"BDT_common5_input_maxeta_jet_tag",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_tag_tag","BDT_common5_input_maxeta_tag_tag",20,0.0,2.0),"BDT_common5_input_maxeta_tag_tag",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_min_dr_tagged_jets","BDT_common5_input_min_dr_tagged_jets",20,0.0,5.0),"BDT_common5_input_min_dr_tagged_jets",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","BDT_common5_input_pt_all_jets_over_E_all_jets",20,0.0,1.0),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_highest_btag","BDT_common5_input_second_highest_btag",20,0.8,1.0),"BDT_common5_input_second_highest_btag",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_jet_pt","BDT_common5_input_second_jet_pt",20,0.0,300.0),"BDT_common5_input_second_jet_pt",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_sphericity","BDT_common5_input_sphericity",20,0.0,1.0),"BDT_common5_input_sphericity",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",20,40.0,230.0),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_highest_btag","BDT_common5_input_third_highest_btag",20,0.8,1.0),"BDT_common5_input_third_highest_btag",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_jet_pt","BDT_common5_input_third_jet_pt",20,0.0,300.0),"BDT_common5_input_third_jet_pt",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Average_Tagged","Evt_CSV_Average_Tagged",20,0.82,1.0),"Evt_CSV_Average_Tagged",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Min","Evt_CSV_Min",20,0.0,1.0),"Evt_CSV_Min",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",20,0.0,3.0),"Evt_Deta_TaggedJetsAverage",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",20,0.0,5.0),"Evt_Dr_JetsAverage",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRJets","Evt_Dr_MinDeltaRJets",20,0.0,3.0),"Evt_Dr_MinDeltaRJets",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonJet","Evt_Dr_MinDeltaRLeptonJet",20,0.0,3.0),"Evt_Dr_MinDeltaRLeptonJet",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonTaggedJet","Evt_Dr_MinDeltaRLeptonTaggedJet",20,0.0,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_Dr_TaggedJetsAverage","Evt_Dr_TaggedJetsAverage",20,0.0,5.0),"Evt_Dr_TaggedJetsAverage",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_E_PrimaryLepton","Evt_E_PrimaryLepton",20,0.0,500.0),"Evt_E_PrimaryLepton",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_Eta_JetsAverage","Evt_Eta_JetsAverage",20,-3.0,3.0),"Evt_Eta_JetsAverage",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_Eta_PrimaryLepton","Evt_Eta_PrimaryLepton",20,-3,3),"Evt_Eta_PrimaryLepton",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_Jet_MaxDeta_Jets","Evt_Jet_MaxDeta_Jets",20,0,5),"Evt_Jet_MaxDeta_Jets",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",20,0.0,400.0),"Evt_M2_TaggedJetsAverage",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_M3","Evt_M3",20,0.0,400.0),"Evt_M3",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_M_JetsAverage","Evt_M_JetsAverage",20,0.0,30.0),"Evt_M_JetsAverage",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_M_MedianTaggedJets","Evt_M_MedianTaggedJets",20,30.0,400.0),"Evt_M_MedianTaggedJets",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRJets","Evt_M_MinDeltaRJets",20,10.0,250.0),"Evt_M_MinDeltaRJets",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",20,10.0,300.0),"Evt_M_MinDeltaRTaggedJets",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",20,0.0,50.0),"Evt_M_TaggedJetsAverage",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRJets","Evt_Pt_MinDeltaRJets",20,0.0,400.0),"Evt_Pt_MinDeltaRJets",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRTaggedJets","Evt_Pt_MinDeltaRTaggedJets",20,0.0,400.0),"Evt_Pt_MinDeltaRTaggedJets",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_Pt_PrimaryLepton","Evt_Pt_PrimaryLepton",20,0.0,400.0),"Evt_Pt_PrimaryLepton",plotselection,plotlabel),    
        # Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH","Evt_blr_ETH",20,0.0,1.1),"Evt_blr_ETH",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH_transformed","Evt_blr_ETH_transformed",20,-10.0,10.0),"Evt_blr_ETH_transformed",plotselection,plotlabel),
        
    ]


    plotlabel="1 lepton, 5 jets, 3 b-tags"
    plotselection=categoriesJT[2][0]
    plotprefix="s53_"
    plots53=[
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_aplanarity_tags","BDT_common5_input_aplanarity_tags",30,0.,1.),"BDT_common5_input_aplanarity_tags",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"second_jet_Pt","second_jet_Pt",30,30.0249652863,309.913513184),"Jet_Pt[1]",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"third_jet_CSV","secon_jet_CSV",30,-0.1,1),"Jet_CSV[2]",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_max_dR_jj","BDT_common5_input_max_dR_jj",30,0.,5),"BDT_common5_input_max_dR_jj",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_M_JetsAverage","Evt_M_JetsAverage",30,2.6179523468,22.3616428375),"Evt_M_JetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_sphericity_jets","BDT_common5_input_sphericity_jets",30,0.,1),"BDT_common5_input_sphericity_jets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"third_jet_Pt","third_jet_Pt",30,30.0249652863,500),"Jet_Pt[2]",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH_transformed","Evt_blr_ETH_transformed",30,-8.87575912476,8.36474990845),"Evt_blr_ETH_transformed",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","BDT_common5_input_dev_from_avg_disc_btags",30,8.26003621057e-09,0.0561485365033),"BDT_common5_input_dev_from_avg_disc_btags",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonTaggedJet","Evt_Dr_MinDeltaRLeptonTaggedJet",30,0.400092959404,3.55373048782),"Evt_Dr_MinDeltaRLeptonTaggedJet",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","BDT_common5_input_closest_tagged_dijet_mass",30,18.6768493652,701.629150391),"BDT_common5_input_closest_tagged_dijet_mass",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Min_Tagged","Evt_CSV_Min_Tagged",30,-0.1,1),"Evt_CSV_Min_Tagged",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"highest_CSV","highest_CSV",30,-0.1,1),"CSV[0]",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Average_Tagged","Evt_CSV_Average_Tagged",30,0.519650936127,0.999474525452),"Evt_CSV_Average_Tagged",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_HT_tag","BDT_common5_input_HT_tag",30,0,500),"BDT_common5_input_HT_tag",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_HT","Sum p_{T}",30,0,1500),"Evt_HT",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Average","Evt_CSV_Average",30,0.,1),"Evt_CSV_Average",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRTaggedJets","#Delta R of closest tagged jets",50,0.,5.0),"Evt_Dr_MinDeltaRTaggedJets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"MEM","MEM",30,0,1.),memexp,plotselection,plotlabel),

        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_tag","BDT_common5_input_maxeta_jet_tag",30,0.03415389359,1.73617899418),"BDT_common5_input_maxeta_jet_tag",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h1","BDT_common5_input_h1",30,-0.198400422931,0.352122873068),"BDT_common5_input_h1",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_Eta_JetsAverage","Evt_Eta_JetsAverage",30,-1.93795931339,1.94079625607),"Evt_Eta_JetsAverage",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h3","BDT_common5_input_h3",30,-0.19060048461,0.264392465353),"BDT_common5_input_h3",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",30,18.6768493652,701.629150391),"Evt_M_MinDeltaRTaggedJets",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",30,0.0169842243195,3.15213322639),"Evt_Deta_TaggedJetsAverage",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRJets","Evt_M_MinDeltaRJets",30,17.7097072601,540.701599121),"Evt_M_MinDeltaRJets",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRTaggedJets","Evt_Pt_MinDeltaRTaggedJets",30,4.4967417717,875.85534668),"Evt_Pt_MinDeltaRTaggedJets",plotselection,plotlabel),
        # # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_best_higgs_mass","BDT_common5_input_best_higgs_mass",30,-9.89999961853,-9.89999961853),"BDT_common5_input_best_higgs_mass",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_jet_pt","BDT_common5_input_third_jet_pt",30,31.0593643188,367.438354492),"BDT_common5_input_third_jet_pt",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MET","BDT_common5_input_MET",30,20.0078697205,916.307006836),"BDT_common5_input_MET",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_Deta_JetsAverage","BDT_common5_input_Evt_Deta_JetsAverage",30,0.0950130447745,2.65379357338),"BDT_common5_input_Evt_Deta_JetsAverage",plotselection,plotlabel),
        # # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dEta_fn","BDT_common5_input_dEta_fn",30,0.0,0.0),"BDT_common5_input_dEta_fn",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_highest_btag","BDT_common5_input_second_highest_btag",30,0.496706932783,0.999739229679),"BDT_common5_input_second_highest_btag",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_jet_pt","BDT_common5_input_fourth_jet_pt",30,30.0574455261,226.817321777),"BDT_common5_input_fourth_jet_pt",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_Jet_MaxDeta_Jets","Evt_Jet_MaxDeta_Jets",30,0.297038376331,4.75924253464),"Evt_Jet_MaxDeta_Jets",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h2","BDT_common5_input_h2",30,-0.117575153708,0.337553173304),"BDT_common5_input_h2",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_HT","BDT_common5_input_HT",30,171.348709106,1767.02282715),"BDT_common5_input_HT",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_lowest_btag","BDT_common5_input_lowest_btag",30,0.494100898504,0.999379396439),"BDT_common5_input_lowest_btag",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_min_dr_tagged_jets","BDT_common5_input_min_dr_tagged_jets",30,0.400978267193,3.46708679199),"BDT_common5_input_min_dr_tagged_jets",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_highest_btag","BDT_common5_input_third_highest_btag",30,0.494100898504,0.999379396439),"BDT_common5_input_third_highest_btag",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_aplanarity","BDT_common5_input_aplanarity",30,0.00109776912723,0.453897118568),"BDT_common5_input_aplanarity",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_jet","BDT_common5_input_maxeta_jet_jet",30,0.0430857762694,1.73617899418),"BDT_common5_input_maxeta_jet_jet",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",30,5.09458208084,53.9921302795),"Evt_M_TaggedJetsAverage",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_E_PrimaryLepton","Evt_E_PrimaryLepton",30,26.194316864,1154.0982666),"Evt_E_PrimaryLepton",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","BDT_common5_input_dr_between_lep_and_closest_jet",30,0.400092959404,3.35898637772),"BDT_common5_input_dr_between_lep_and_closest_jet",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_btag_disc_btags","BDT_common5_input_avg_btag_disc_btags",30,0.519650936127,0.999474525452),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_M3","BDT_common5_input_M3",30,47.1682891846,3078.03637695),"BDT_common5_input_M3",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","BDT_common5_input_pt_all_jets_over_E_all_jets",30,0.233425289392,0.986175239086),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h0","BDT_common5_input_h0",30,0.130814537406,0.398144483566),"BDT_common5_input_h0",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_Eta_PrimaryLepton","Evt_Eta_PrimaryLepton",30,-2.39770889282,2.39823579788),"Evt_Eta_PrimaryLepton",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",30,32.8312149048,1103.22045898),"Evt_M2_TaggedJetsAverage",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_M_MedianTaggedJets","Evt_M_MedianTaggedJets",30,29.3009853363,1153.92272949),"Evt_M_MedianTaggedJets",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_M3","Evt_M3",30,47.1682891846,3078.03637695),"Evt_M3",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH","Evt_blr_ETH",30,0.000139715935802,0.999767124653),"Evt_blr_ETH",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_Pt_PrimaryLepton","Evt_Pt_PrimaryLepton",30,26.0137710571,675.206176758),"Evt_Pt_PrimaryLepton",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_all_sum_pt_with_met","BDT_common5_input_all_sum_pt_with_met",30,245.993301392,2657.89892578),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","BDT_common5_input_avg_dr_tagged_jets",30,0.529578566551,4.09861135483),"BDT_common5_input_avg_dr_tagged_jets",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fifth_highest_CSV","BDT_common5_input_fifth_highest_CSV",30,-0.10000000149,0.474201887846),"BDT_common5_input_fifth_highest_CSV",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonJet","Evt_Dr_MinDeltaRLeptonJet",30,0.400092959404,3.35898637772),"Evt_Dr_MinDeltaRLeptonJet",plotselection,plotlabel),
        # # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",30,-99.0,348.854248047),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",30,0.0,348.854248047),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"MEM","MEM",30,0.,1.),memexp,plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_tag_tag","BDT_common5_input_maxeta_tag_tag",30,0.00718557322398,1.54748666286),"BDT_common5_input_maxeta_tag_tag",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_jet_pt","BDT_common5_input_second_jet_pt",30,32.9910621643,665.84942627),"BDT_common5_input_second_jet_pt",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRJets","Evt_Dr_MinDeltaRJets",30,0.397356927395,2.24220538139),"Evt_Dr_MinDeltaRJets",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",30,1.1808822155,3.56335401535),"Evt_Dr_JetsAverage",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Mlb","BDT_common5_input_Mlb",30,17.1313037872,573.15612793),"BDT_common5_input_Mlb",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Min","Evt_CSV_Min",30,-0.10000000149,0.474201887846),"Evt_CSV_Min",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_Dr_TaggedJetsAverage","Evt_Dr_TaggedJetsAverage",30,0.529578626156,4.09861135483),"Evt_Dr_TaggedJetsAverage",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_first_jet_pt","BDT_common5_input_first_jet_pt",30,38.9418678284,1323.05517578),"BDT_common5_input_first_jet_pt",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRJets","Evt_Pt_MinDeltaRJets",30,43.2985229492,1342.04992676),"Evt_Pt_MinDeltaRJets",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_highest_btag","BDT_common5_input_fourth_highest_btag",30,-0.10000000149,0.494023233652),"BDT_common5_input_fourth_highest_btag",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MHT","BDT_common5_input_MHT",30,1.43388545513,925.815917969),"BDT_common5_input_MHT",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_invariant_mass_of_everything","BDT_common5_input_invariant_mass_of_everything",30,303.694122314,4137.55224609),"BDT_common5_input_invariant_mass_of_everything",plotselection,plotlabel),
    ]


    plotlabel="1 lepton, 5 jets, #geq4 b-tags"
    plotselection=categoriesJT[5][0]
    plotprefix="s54_"
    plots54=[
        # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",20,0.6,1.0),"BDT_common5_input_Evt_CSV_Average",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"MEM","MEM",20,0.0,1.0),memexp,plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_Deta_JetsAverage","BDT_common5_input_Evt_Deta_JetsAverage",20,0.0,3.4),"BDT_common5_input_Evt_Deta_JetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_HT","BDT_common5_input_HT",20,0.0,1000.0),"BDT_common5_input_HT",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_M3","BDT_common5_input_M3",20,0.0,600.0),"BDT_common5_input_M3",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MET","BDT_common5_input_MET",20,0.0,300.0),"BDT_common5_input_MET",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MHT","BDT_common5_input_MHT",20,0.0,250.0),"BDT_common5_input_MHT",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Mlb","BDT_common5_input_Mlb",20,0.0,250.0),"BDT_common5_input_Mlb",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_all_sum_pt_with_met","BDT_common5_input_all_sum_pt_with_met",20,200,900.0),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_aplanarity","BDT_common5_input_aplanarity",20,0.0,0.4),"BDT_common5_input_aplanarity",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_btag_disc_btags","BDT_common5_input_avg_btag_disc_btags",20,0.8,1.0),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","BDT_common5_input_avg_dr_tagged_jets",20,0.0,5.0),"BDT_common5_input_avg_dr_tagged_jets",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_best_higgs_mass","BDT_common5_input_best_higgs_mass",20,0.0,200.0),"BDT_common5_input_best_higgs_mass",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","BDT_common5_input_closest_tagged_dijet_mass",20,0.0,250.0),"BDT_common5_input_closest_tagged_dijet_mass",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dEta_fn","BDT_common5_input_dEta_fn",20,0.0,5.0),"BDT_common5_input_dEta_fn",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","BDT_common5_input_dev_from_avg_disc_btags",20,0.0,0.02),"BDT_common5_input_dev_from_avg_disc_btags",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","BDT_common5_input_dr_between_lep_and_closest_jet",20,0.0,3.0),"BDT_common5_input_dr_between_lep_and_closest_jet",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fifth_highest_CSV","BDT_common5_input_fifth_highest_CSV",20,-0.1,1.0),"BDT_common5_input_fifth_highest_CSV",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_first_jet_pt","BDT_common5_input_first_jet_pt",20,0.0,500.0),"BDT_common5_input_first_jet_pt",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_highest_btag","BDT_common5_input_fourth_highest_btag",20,0.8,1.0),"BDT_common5_input_fourth_highest_btag",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_jet_pt","BDT_common5_input_fourth_jet_pt",20,0.0,300.0),"BDT_common5_input_fourth_jet_pt",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h0","BDT_common5_input_h0",20,0.15,0.45),"BDT_common5_input_h0",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h1","BDT_common5_input_h1",20,-0.2,0.2),"BDT_common5_input_h1",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h2","BDT_common5_input_h2",20,-0.2,0.3),"BDT_common5_input_h2",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h3","BDT_common5_input_h3",20,-0.2,0.2),"BDT_common5_input_h3",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_invariant_mass_of_everything","BDT_common5_input_invariant_mass_of_everything",20,500.0,1200.0),"BDT_common5_input_invariant_mass_of_everything",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_lowest_btag","BDT_common5_input_lowest_btag",20,0.8,1.0),"BDT_common5_input_lowest_btag",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_jet","BDT_common5_input_maxeta_jet_jet",20,0.0,2.0),"BDT_common5_input_maxeta_jet_jet",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_tag","BDT_common5_input_maxeta_jet_tag",20,0.0,2.0),"BDT_common5_input_maxeta_jet_tag",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_tag_tag","BDT_common5_input_maxeta_tag_tag",20,0.0,2.0),"BDT_common5_input_maxeta_tag_tag",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_min_dr_tagged_jets","BDT_common5_input_min_dr_tagged_jets",20,0.0,5.0),"BDT_common5_input_min_dr_tagged_jets",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","BDT_common5_input_pt_all_jets_over_E_all_jets",20,0.0,1.0),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_highest_btag","BDT_common5_input_second_highest_btag",20,0.8,1.0),"BDT_common5_input_second_highest_btag",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_jet_pt","BDT_common5_input_second_jet_pt",20,0.0,300.0),"BDT_common5_input_second_jet_pt",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_sphericity","BDT_common5_input_sphericity",20,0.0,1.0),"BDT_common5_input_sphericity",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",20,40.0,230.0),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_highest_btag","BDT_common5_input_third_highest_btag",20,0.8,1.0),"BDT_common5_input_third_highest_btag",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_jet_pt","BDT_common5_input_third_jet_pt",20,0.0,300.0),"BDT_common5_input_third_jet_pt",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Average_Tagged","Evt_CSV_Average_Tagged",20,0.82,1.0),"Evt_CSV_Average_Tagged",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Min","Evt_CSV_Min",20,0.0,1.0),"Evt_CSV_Min",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",20,0.0,3.0),"Evt_Deta_TaggedJetsAverage",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",20,0.0,5.0),"Evt_Dr_JetsAverage",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRJets","Evt_Dr_MinDeltaRJets",20,0.0,3.0),"Evt_Dr_MinDeltaRJets",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonJet","Evt_Dr_MinDeltaRLeptonJet",20,0.0,3.0),"Evt_Dr_MinDeltaRLeptonJet",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonTaggedJet","Evt_Dr_MinDeltaRLeptonTaggedJet",20,0.0,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"Evt_Dr_TaggedJetsAverage","Evt_Dr_TaggedJetsAverage",20,0.0,5.0),"Evt_Dr_TaggedJetsAverage",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"Evt_E_PrimaryLepton","Evt_E_PrimaryLepton",20,0.0,500.0),"Evt_E_PrimaryLepton",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"Evt_Eta_JetsAverage","Evt_Eta_JetsAverage",20,-3.0,3.0),"Evt_Eta_JetsAverage",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"Evt_Eta_PrimaryLepton","Evt_Eta_PrimaryLepton",20,-3,3),"Evt_Eta_PrimaryLepton",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"Evt_Jet_MaxDeta_Jets","Evt_Jet_MaxDeta_Jets",20,0,5),"Evt_Jet_MaxDeta_Jets",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",20,0.0,400.0),"Evt_M2_TaggedJetsAverage",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"Evt_M3","Evt_M3",20,0.0,400.0),"Evt_M3",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"Evt_M_JetsAverage","Evt_M_JetsAverage",20,0.0,30.0),"Evt_M_JetsAverage",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"Evt_M_MedianTaggedJets","Evt_M_MedianTaggedJets",20,30.0,400.0),"Evt_M_MedianTaggedJets",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRJets","Evt_M_MinDeltaRJets",20,10.0,250.0),"Evt_M_MinDeltaRJets",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",20,10.0,300.0),"Evt_M_MinDeltaRTaggedJets",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",20,0.0,50.0),"Evt_M_TaggedJetsAverage",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRJets","Evt_Pt_MinDeltaRJets",20,0.0,400.0),"Evt_Pt_MinDeltaRJets",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRTaggedJets","Evt_Pt_MinDeltaRTaggedJets",20,0.0,400.0),"Evt_Pt_MinDeltaRTaggedJets",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"Evt_Pt_PrimaryLepton","Evt_Pt_PrimaryLepton",20,0.0,400.0),"Evt_Pt_PrimaryLepton",plotselection,plotlabel),    
        ##Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH","Evt_blr_ETH",20,0.0,1.1),"Evt_blr_ETH",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH_transformed","Evt_blr_ETH_transformed",20,-10.0,10.0),"Evt_blr_ETH_transformed",plotselection,plotlabel),
        
        ##Plot(ROOT.TH1D(plotprefix+"Reco_Sum_LikelihoodRatio","Reco_Sum_LikelihoodRatio",20,-0.1,1),"Reco_Sum_LikelihoodRatio",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"Reco_Sum_LikelihoodTimesMERatio","Reco_Sum_LikelihoodTimesMERatio",20,-0.1,1),"Reco_Sum_LikelihoodTimesMERatio",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"Reco_TTBBME_best_TTLikelihood_comb","Reco_TTBBME_best_TTLikelihood_comb",20,-0.1,1),"Reco_TTBBME_best_TTLikelihood_comb",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",20,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",20,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihood_best_TTBBLikelihood","Reco_TTBBLikelihood_best_TTBBLikelihood",20,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihood",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb","Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",20,-0.1,1),"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Reco_Dr_BB_best_TTLikelihood","Reco_Dr_BB_best_TTLikelihood",20,-0.1,1),"Reco_Dr_BB_best_TTLikelihood",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Reco_TTBBME_off_best_TTLikelihood_comb","Reco_TTBBME_off_best_TTLikelihood_comb",20,-0.1,1),"Reco_TTBBME_off_best_TTLikelihood_comb",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb","Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",20,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",plotselection,plotlabel),
    ]


    plotlabel="1 lepton, #geq6 jets, 2 b-tags"
    plotselection=categoriesJT[0][0]
    plotprefix="s62_"
    plots62=[
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",30,0.6,1.0),"BDT_common5_input_Evt_CSV_Average",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_Deta_JetsAverage","BDT_common5_input_Evt_Deta_JetsAverage",30,0.0,3.4),"BDT_common5_input_Evt_Deta_JetsAverage",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_HT","BDT_common5_input_HT",30,0.0,1000.0),"BDT_common5_input_HT",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_M3","BDT_common5_input_M3",30,0.0,600.0),"BDT_common5_input_M3",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MET","BDT_common5_input_MET",30,0.0,300.0),"BDT_common5_input_MET",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MHT","BDT_common5_input_MHT",30,0.0,250.0),"BDT_common5_input_MHT",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Mlb","BDT_common5_input_Mlb",30,0.0,250.0),"BDT_common5_input_Mlb",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_all_sum_pt_with_met","BDT_common5_input_all_sum_pt_with_met",30,200,900.0),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_aplanarity","BDT_common5_input_aplanarity",30,0.0,0.4),"BDT_common5_input_aplanarity",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_btag_disc_btags","BDT_common5_input_avg_btag_disc_btags",30,0.8,1.0),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","BDT_common5_input_avg_dr_tagged_jets",30,0.0,5.0),"BDT_common5_input_avg_dr_tagged_jets",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_best_higgs_mass","BDT_common5_input_best_higgs_mass",30,0.0,200.0),"BDT_common5_input_best_higgs_mass",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","BDT_common5_input_closest_tagged_dijet_mass",30,0.0,250.0),"BDT_common5_input_closest_tagged_dijet_mass",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dEta_fn","BDT_common5_input_dEta_fn",30,0.0,5.0),"BDT_common5_input_dEta_fn",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","BDT_common5_input_dev_from_avg_disc_btags",30,0.0,0.02),"BDT_common5_input_dev_from_avg_disc_btags",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","BDT_common5_input_dr_between_lep_and_closest_jet",30,0.0,3.0),"BDT_common5_input_dr_between_lep_and_closest_jet",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fifth_highest_CSV","BDT_common5_input_fifth_highest_CSV",30,-0.1,1.0),"BDT_common5_input_fifth_highest_CSV",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_first_jet_pt","BDT_common5_input_first_jet_pt",30,0.0,500.0),"BDT_common5_input_first_jet_pt",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_highest_btag","BDT_common5_input_fourth_highest_btag",30,-0.1,1.0),"BDT_common5_input_fourth_highest_btag",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_jet_pt","BDT_common5_input_fourth_jet_pt",30,0.0,300.0),"BDT_common5_input_fourth_jet_pt",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h0","BDT_common5_input_h0",30,0.15,0.45),"BDT_common5_input_h0",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h1","BDT_common5_input_h1",30,-0.2,0.2),"BDT_common5_input_h1",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h2","BDT_common5_input_h2",30,-0.2,0.3),"BDT_common5_input_h2",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h3","BDT_common5_input_h3",30,-0.2,0.2),"BDT_common5_input_h3",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_invariant_mass_of_everything","BDT_common5_input_invariant_mass_of_everything",30,500.0,1200.0),"BDT_common5_input_invariant_mass_of_everything",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_lowest_btag","BDT_common5_input_lowest_btag",30,0.8,1.0),"BDT_common5_input_lowest_btag",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_jet","BDT_common5_input_maxeta_jet_jet",30,0.0,2.0),"BDT_common5_input_maxeta_jet_jet",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_tag","BDT_common5_input_maxeta_jet_tag",30,0.0,2.0),"BDT_common5_input_maxeta_jet_tag",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_tag_tag","BDT_common5_input_maxeta_tag_tag",30,0.0,2.0),"BDT_common5_input_maxeta_tag_tag",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_min_dr_tagged_jets","BDT_common5_input_min_dr_tagged_jets",30,0.0,5.0),"BDT_common5_input_min_dr_tagged_jets",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","BDT_common5_input_pt_all_jets_over_E_all_jets",30,0.0,1.0),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_highest_btag","BDT_common5_input_second_highest_btag",30,0.8,1.0),"BDT_common5_input_second_highest_btag",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_jet_pt","BDT_common5_input_second_jet_pt",30,0.0,300.0),"BDT_common5_input_second_jet_pt",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_sphericity","BDT_common5_input_sphericity",30,0.0,1.0),"BDT_common5_input_sphericity",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",30,40.0,230.0),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_highest_btag","BDT_common5_input_third_highest_btag",30,0.8,1.0),"BDT_common5_input_third_highest_btag",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_jet_pt","BDT_common5_input_third_jet_pt",30,0.0,300.0),"BDT_common5_input_third_jet_pt",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Average_Tagged","Evt_CSV_Average_Tagged",30,0.82,1.0),"Evt_CSV_Average_Tagged",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Min","Evt_CSV_Min",30,0.0,1.0),"Evt_CSV_Min",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",30,0.0,5.0),"Evt_Dr_JetsAverage",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRJets","Evt_Dr_MinDeltaRJets",30,0.0,3.0),"Evt_Dr_MinDeltaRJets",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonJet","Evt_Dr_MinDeltaRLeptonJet",30,0.0,3.0),"Evt_Dr_MinDeltaRLeptonJet",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonTaggedJet","Evt_Dr_MinDeltaRLeptonTaggedJet",30,0.0,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"Evt_Dr_TaggedJetsAverage","Evt_Dr_TaggedJetsAverage",30,0.0,5.0),"Evt_Dr_TaggedJetsAverage",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"Evt_E_PrimaryLepton","Evt_E_PrimaryLepton",30,0.0,500.0),"Evt_E_PrimaryLepton",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"Evt_Eta_JetsAverage","Evt_Eta_JetsAverage",30,-3.0,3.0),"Evt_Eta_JetsAverage",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"Evt_Eta_PrimaryLepton","Evt_Eta_PrimaryLepton",30,-3,3),"Evt_Eta_PrimaryLepton",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"Evt_Jet_MaxDeta_Jets","Evt_Jet_MaxDeta_Jets",30,0,5),"Evt_Jet_MaxDeta_Jets",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",30,0.0,400.0),"Evt_M2_TaggedJetsAverage",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"Evt_M3","Evt_M3",30,0.0,400.0),"Evt_M3",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"Evt_M_JetsAverage","Evt_M_JetsAverage",30,0.0,30.0),"Evt_M_JetsAverage",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"Evt_M_MedianTaggedJets","Evt_M_MedianTaggedJets",30,30.0,400.0),"Evt_M_MedianTaggedJets",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRJets","Evt_M_MinDeltaRJets",30,10.0,250.0),"Evt_M_MinDeltaRJets",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",30,10.0,300.0),"Evt_M_MinDeltaRTaggedJets",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",30,0.0,50.0),"Evt_M_TaggedJetsAverage",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRJets","Evt_Pt_MinDeltaRJets",30,0.0,400.0),"Evt_Pt_MinDeltaRJets",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRTaggedJets","Evt_Pt_MinDeltaRTaggedJets",30,0.0,400.0),"Evt_Pt_MinDeltaRTaggedJets",plotselection,plotlabel),
        ###Plot(ROOT.TH1D(plotprefix+"Evt_Pt_PrimaryLepton","Evt_Pt_PrimaryLepton",30,0.0,400.0),"Evt_Pt_PrimaryLepton",plotselection,plotlabel),    
        ###Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH","Evt_blr_ETH",30,0.0,1.1),"Evt_blr_ETH",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH_transformed","Evt_blr_ETH_transformed",30,-10.0,10.0),"Evt_blr_ETH_transformed",plotselection,plotlabel),
    ]


    plotlabel="1 lepton, #geq6 jets, 3 b-tags"
    plotselection=categoriesJT[3][0]
    plotprefix="s63_"
    plots63=[
    Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_max_dR_bb","BDT_common5_input_max_dR_bb",30,0.,5),"BDT_common5_input_max_dR_bb",plotselection,plotlabel),
    Plot(ROOT.TH1D(plotprefix+"Evt_Dr_TaggedJetsAverage","Evt_Dr_TaggedJetsAverage",30,0.545018851757,4.16827630997),"Evt_Dr_TaggedJetsAverage",plotselection,plotlabel),
    Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_transverse_sphericity_tags","BDT_common5_input_transverse_sphericity_tags",30,0,1),"BDT_common5_input_transverse_sphericity_tags",plotselection,plotlabel),
    Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_transverse_sphericity_jets","BDT_common5_input_transverse_sphericity_jets",30,0,1),"BDT_common5_input_transverse_sphericity_jets",plotselection,plotlabel),
    Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRLeptonTaggedJet","Evt_M_MinDeltaRLeptonTaggedJet",30,0.,5),"Evt_M_MinDeltaRLeptonTaggedJet",plotselection,plotlabel),
    Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","BDT_common5_input_closest_tagged_dijet_mass",30,18.015329361,861.33190918),"BDT_common5_input_closest_tagged_dijet_mass",plotselection,plotlabel),
    Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRTaggedJets","#Delta R of closest tagged jets",50,0.,5.0),"Evt_Dr_MinDeltaRTaggedJets",plotselection,plotlabel),
    Plot(ROOT.TH1D(plotprefix+"Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",30,28.9838237762,946.658508301),"Evt_M2_TaggedJetsAverage",plotselection,plotlabel),
    Plot(ROOT.TH1D(plotprefix+"MEM","MEM",30,0,1.),memexp,plotselection,plotlabel),
    Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_HT_tag","BDT_common5_input_HT_tag",30,0,500),"BDT_common5_input_HT_tag",plotselection,plotlabel),
    Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Average","Evt_CSV_Average",30,0.0,1),"Evt_CSV_Average",plotselection,plotlabel),
    Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Average_Tagged","Evt_CSV_Average_Tagged",30,0.505652368069,0.999587237835),"Evt_CSV_Average_Tagged",plotselection,plotlabel),
    Plot(ROOT.TH1D(plotprefix+"Evt_M_JetsAverage","Evt_M_JetsAverage",30,1.71226847172,23.9440631866),"Evt_M_JetsAverage",plotselection,plotlabel),
    Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Min_Tagged","Evt_CSV_Min_Tagged",30,-0.1,1),"Evt_CSV_Min_Tagged",plotselection,plotlabel),


    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_tag","BDT_common5_input_maxeta_jet_tag",30,0.0199760980904,1.81036174297),"BDT_common5_input_maxeta_jet_tag",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h1","BDT_common5_input_h1",30,-0.175212517381,0.371365427971),"BDT_common5_input_h1",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_Eta_JetsAverage","Evt_Eta_JetsAverage",30,-1.99048137665,1.937494874),"Evt_Eta_JetsAverage",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h3","BDT_common5_input_h3",30,-0.178277373314,0.231585070491),"BDT_common5_input_h3",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",30,18.015329361,861.33190918),"Evt_M_MinDeltaRTaggedJets",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",30,0.0116489725187,3.16538500786),"Evt_Deta_TaggedJetsAverage",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRJets","Evt_M_MinDeltaRJets",30,16.2207489014,515.06829834),"Evt_M_MinDeltaRJets",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRTaggedJets","Evt_Pt_MinDeltaRTaggedJets",30,2.59846401215,910.948730469),"Evt_Pt_MinDeltaRTaggedJets",plotselection,plotlabel),
    # # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_best_higgs_mass","BDT_common5_input_best_higgs_mass",30,-9.89999961853,-9.89999961853),"BDT_common5_input_best_higgs_mass",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_jet_pt","BDT_common5_input_third_jet_pt",30,31.5342140198,583.186706543),"BDT_common5_input_third_jet_pt",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MET","BDT_common5_input_MET",30,20.0631408691,1000.58435059),"BDT_common5_input_MET",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_Deta_JetsAverage","BDT_common5_input_Evt_Deta_JetsAverage",30,0.190533682704,2.39203691483),"BDT_common5_input_Evt_Deta_JetsAverage",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dEta_fn","BDT_common5_input_dEta_fn",30,0.00763740483671,8.3930015564),"BDT_common5_input_dEta_fn",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_highest_btag","BDT_common5_input_second_highest_btag",30,0.498569428921,0.999660074711),"BDT_common5_input_second_highest_btag",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_jet_pt","BDT_common5_input_fourth_jet_pt",30,30.7466239929,345.313690186),"BDT_common5_input_fourth_jet_pt",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_Jet_MaxDeta_Jets","Evt_Jet_MaxDeta_Jets",30,0.338057726622,4.56032848358),"Evt_Jet_MaxDeta_Jets",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h2","BDT_common5_input_h2",30,-0.101943947375,0.329278439283),"BDT_common5_input_h2",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_HT","BDT_common5_input_HT",30,221.376083374,2875.97949219),"BDT_common5_input_HT",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_lowest_btag","BDT_common5_input_lowest_btag",30,0.494103521109,0.999403715134),"BDT_common5_input_lowest_btag",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_min_dr_tagged_jets","BDT_common5_input_min_dr_tagged_jets",30,0.406043827534,3.42316508293),"BDT_common5_input_min_dr_tagged_jets",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_highest_btag","BDT_common5_input_third_highest_btag",30,0.494103521109,0.999403715134),"BDT_common5_input_third_highest_btag",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_aplanarity","BDT_common5_input_aplanarity",30,0.00118113146164,0.416283935308),"BDT_common5_input_aplanarity",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_jet","BDT_common5_input_maxeta_jet_jet",30,0.124032519758,1.81036174297),"BDT_common5_input_maxeta_jet_jet",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",30,4.21863889694,89.321144104),"Evt_M_TaggedJetsAverage",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_E_PrimaryLepton","Evt_E_PrimaryLepton",30,26.5162811279,1009.42108154),"Evt_E_PrimaryLepton",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","BDT_common5_input_dr_between_lep_and_closest_jet",30,0.407905042171,3.45566606522),"BDT_common5_input_dr_between_lep_and_closest_jet",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_btag_disc_btags","BDT_common5_input_avg_btag_disc_btags",30,0.505652368069,0.99958717823),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_M3","BDT_common5_input_M3",30,49.9820327759,4132.41210938),"BDT_common5_input_M3",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","BDT_common5_input_pt_all_jets_over_E_all_jets",30,0.249926298857,0.963635444641),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h0","BDT_common5_input_h0",30,0.142892166972,0.443892478943),"BDT_common5_input_h0",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH_transformed","Evt_blr_ETH_transformed",30,-5.9987578392,8.41789054871),"Evt_blr_ETH_transformed",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_Eta_PrimaryLepton","Evt_Eta_PrimaryLepton",30,-2.37992596626,2.39206981659),"Evt_Eta_PrimaryLepton",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_M_MedianTaggedJets","Evt_M_MedianTaggedJets",30,22.1278095245,1173.1661377),"Evt_M_MedianTaggedJets",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_M3","Evt_M3",30,49.9820327759,4132.41210938),"Evt_M3",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH","Evt_blr_ETH",30,0.00247568916529,0.999779164791),"Evt_blr_ETH",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_Pt_PrimaryLepton","Evt_Pt_PrimaryLepton",30,26.0013599396,508.246490479),"Evt_Pt_PrimaryLepton",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_all_sum_pt_with_met","BDT_common5_input_all_sum_pt_with_met",30,298.321655273,3568.77685547),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","BDT_common5_input_avg_dr_tagged_jets",30,0.545018851757,4.16827630997),"BDT_common5_input_avg_dr_tagged_jets",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fifth_highest_CSV","BDT_common5_input_fifth_highest_CSV",30,-0.10000000149,0.474233090878),"BDT_common5_input_fifth_highest_CSV",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonJet","Evt_Dr_MinDeltaRLeptonJet",30,0.407905042171,3.45566606522),"Evt_Dr_MinDeltaRLeptonJet",plotselection,plotlabel),
    # # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",30,-99.0,348.618499756),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",30,0,348.618499756),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","BDT_common5_input_dev_from_avg_disc_btags",30,1.70702545432e-08,0.0561579428613),"BDT_common5_input_dev_from_avg_disc_btags",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_tag_tag","BDT_common5_input_maxeta_tag_tag",30,0.00698812818155,1.55675554276),"BDT_common5_input_maxeta_tag_tag",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_jet_pt","BDT_common5_input_second_jet_pt",30,35.4962425232,731.420898438),"BDT_common5_input_second_jet_pt",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRJets","Evt_Dr_MinDeltaRJets",30,0.392195224762,2.09709501266),"Evt_Dr_MinDeltaRJets",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",30,1.12257039547,3.20988988876),"Evt_Dr_JetsAverage",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Mlb","BDT_common5_input_Mlb",30,16.8238983154,1124.39477539),"BDT_common5_input_Mlb",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Min","Evt_CSV_Min",30,-0.10000000149,0.279780119658),"Evt_CSV_Min",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_first_jet_pt","BDT_common5_input_first_jet_pt",30,43.4657363892,1262.56518555),"BDT_common5_input_first_jet_pt",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonTaggedJet","Evt_Dr_MinDeltaRLeptonTaggedJet",30,0.407905042171,4.54733037949),"Evt_Dr_MinDeltaRLeptonTaggedJet",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRJets","Evt_Pt_MinDeltaRJets",30,42.2100982666,822.556640625),"Evt_Pt_MinDeltaRJets",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_sphericity","BDT_common5_input_sphericity",30,0.0167866591364,0.877822458744),"BDT_common5_input_sphericity",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_highest_btag","BDT_common5_input_fourth_highest_btag",30,0.00973574817181,0.493763923645),"BDT_common5_input_fourth_highest_btag",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MHT","BDT_common5_input_MHT",30,0.594647943974,775.840087891),"BDT_common5_input_MHT",plotselection,plotlabel),
    # Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_invariant_mass_of_everything","BDT_common5_input_invariant_mass_of_everything",30,363.370880127,6764.74121094),"BDT_common5_input_invariant_mass_of_everything",plotselection,plotlabel),
    ]

    plotlabel="1 lepton, #geq6 jets, #geq4 b-tags"
    plotselection=categoriesJT[6][0]
    plotprefix="s64"
    plots64=[
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",20,0.6,1.0),"BDT_common5_input_Evt_CSV_Average",plotselection,plotlabel),
        # Plot(ROOT.TH1D(plotprefix+"MEM","MEM",20,0.0,1.0),memexp,plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_Deta_JetsAverage","BDT_common5_input_Evt_Deta_JetsAverage",20,0.0,3.4),"BDT_common5_input_Evt_Deta_JetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_HT","BDT_common5_input_HT",20,0.0,1000.0),"BDT_common5_input_HT",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_M3","BDT_common5_input_M3",20,0.0,600.0),"BDT_common5_input_M3",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MET","BDT_common5_input_MET",20,0.0,300.0),"BDT_common5_input_MET",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MHT","BDT_common5_input_MHT",20,0.0,250.0),"BDT_common5_input_MHT",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Mlb","BDT_common5_input_Mlb",20,0.0,250.0),"BDT_common5_input_Mlb",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_all_sum_pt_with_met","BDT_common5_input_all_sum_pt_with_met",20,200,900.0),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_aplanarity","BDT_common5_input_aplanarity",20,0.0,0.4),"BDT_common5_input_aplanarity",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_btag_disc_btags","BDT_common5_input_avg_btag_disc_btags",20,0.8,1.0),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","BDT_common5_input_avg_dr_tagged_jets",20,0.0,5.0),"BDT_common5_input_avg_dr_tagged_jets",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_best_higgs_mass","BDT_common5_input_best_higgs_mass",20,0.0,200.0),"BDT_common5_input_best_higgs_mass",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","BDT_common5_input_closest_tagged_dijet_mass",20,0.0,250.0),"BDT_common5_input_closest_tagged_dijet_mass",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dEta_fn","BDT_common5_input_dEta_fn",20,0.0,5.0),"BDT_common5_input_dEta_fn",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","BDT_common5_input_dev_from_avg_disc_btags",20,0.0,0.02),"BDT_common5_input_dev_from_avg_disc_btags",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","BDT_common5_input_dr_between_lep_and_closest_jet",20,0.0,3.0),"BDT_common5_input_dr_between_lep_and_closest_jet",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fifth_highest_CSV","BDT_common5_input_fifth_highest_CSV",20,-0.1,1.0),"BDT_common5_input_fifth_highest_CSV",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_first_jet_pt","BDT_common5_input_first_jet_pt",20,0.0,500.0),"BDT_common5_input_first_jet_pt",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_highest_btag","BDT_common5_input_fourth_highest_btag",20,0.8,1.0),"BDT_common5_input_fourth_highest_btag",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_jet_pt","BDT_common5_input_fourth_jet_pt",20,0.0,300.0),"BDT_common5_input_fourth_jet_pt",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h0","BDT_common5_input_h0",20,0.15,0.45),"BDT_common5_input_h0",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h1","BDT_common5_input_h1",20,-0.2,0.2),"BDT_common5_input_h1",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h2","BDT_common5_input_h2",20,-0.2,0.3),"BDT_common5_input_h2",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h3","BDT_common5_input_h3",20,-0.2,0.2),"BDT_common5_input_h3",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_invariant_mass_of_everything","BDT_common5_input_invariant_mass_of_everything",20,500.0,1200.0),"BDT_common5_input_invariant_mass_of_everything",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_lowest_btag","BDT_common5_input_lowest_btag",20,0.8,1.0),"BDT_common5_input_lowest_btag",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_jet","BDT_common5_input_maxeta_jet_jet",20,0.0,2.0),"BDT_common5_input_maxeta_jet_jet",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_tag","BDT_common5_input_maxeta_jet_tag",20,0.0,2.0),"BDT_common5_input_maxeta_jet_tag",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_tag_tag","BDT_common5_input_maxeta_tag_tag",20,0.0,2.0),"BDT_common5_input_maxeta_tag_tag",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_min_dr_tagged_jets","BDT_common5_input_min_dr_tagged_jets",20,0.0,5.0),"BDT_common5_input_min_dr_tagged_jets",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","BDT_common5_input_pt_all_jets_over_E_all_jets",20,0.0,1.0),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_highest_btag","BDT_common5_input_second_highest_btag",20,0.8,1.0),"BDT_common5_input_second_highest_btag",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_jet_pt","BDT_common5_input_second_jet_pt",20,0.0,300.0),"BDT_common5_input_second_jet_pt",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_sphericity","BDT_common5_input_sphericity",20,0.0,1.0),"BDT_common5_input_sphericity",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",20,40.0,230.0),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotselection,plotlabel),
        ##Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_highest_btag","BDT_common5_input_third_highest_btag",20,0.8,1.0),"BDT_common5_input_third_highest_btag",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_jet_pt","BDT_common5_input_third_jet_pt",20,0.0,300.0),"BDT_common5_input_third_jet_pt",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Average_Tagged","Evt_CSV_Average_Tagged",20,0.82,1.0),"Evt_CSV_Average_Tagged",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Min","Evt_CSV_Min",20,0.0,1.0),"Evt_CSV_Min",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",20,0.0,3.0),"Evt_Deta_TaggedJetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",20,0.0,5.0),"Evt_Dr_JetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRJets","Evt_Dr_MinDeltaRJets",20,0.0,3.0),"Evt_Dr_MinDeltaRJets",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonJet","Evt_Dr_MinDeltaRLeptonJet",20,0.0,3.0),"Evt_Dr_MinDeltaRLeptonJet",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonTaggedJet","Evt_Dr_MinDeltaRLeptonTaggedJet",20,0.0,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Evt_Dr_TaggedJetsAverage","Evt_Dr_TaggedJetsAverage",20,0.0,5.0),"Evt_Dr_TaggedJetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Evt_E_PrimaryLepton","Evt_E_PrimaryLepton",20,0.0,500.0),"Evt_E_PrimaryLepton",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Evt_Eta_JetsAverage","Evt_Eta_JetsAverage",20,-3.0,3.0),"Evt_Eta_JetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Evt_Eta_PrimaryLepton","Evt_Eta_PrimaryLepton",20,-3,3),"Evt_Eta_PrimaryLepton",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Evt_Jet_MaxDeta_Jets","Evt_Jet_MaxDeta_Jets",20,0,5),"Evt_Jet_MaxDeta_Jets",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",20,0.0,400.0),"Evt_M2_TaggedJetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Evt_M3","Evt_M3",20,0.0,400.0),"Evt_M3",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Evt_M_JetsAverage","Evt_M_JetsAverage",20,0.0,30.0),"Evt_M_JetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Evt_M_MedianTaggedJets","Evt_M_MedianTaggedJets",20,30.0,400.0),"Evt_M_MedianTaggedJets",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRJets","Evt_M_MinDeltaRJets",20,10.0,250.0),"Evt_M_MinDeltaRJets",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",20,10.0,300.0),"Evt_M_MinDeltaRTaggedJets",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",20,0.0,50.0),"Evt_M_TaggedJetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRJets","Evt_Pt_MinDeltaRJets",20,0.0,400.0),"Evt_Pt_MinDeltaRJets",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRTaggedJets","Evt_Pt_MinDeltaRTaggedJets",20,0.0,400.0),"Evt_Pt_MinDeltaRTaggedJets",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Evt_Pt_PrimaryLepton","Evt_Pt_PrimaryLepton",20,0.0,400.0),"Evt_Pt_PrimaryLepton",plotselection,plotlabel),    
        #Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH","Evt_blr_ETH",20,0.0,1.1),"Evt_blr_ETH",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH_transformed","Evt_blr_ETH_transformed",20,-10.0,10.0),"Evt_blr_ETH_transformed",plotselection,plotlabel),
        
        #Plot(ROOT.TH1D(plotprefix+"Reco_Sum_LikelihoodRatio","Reco_Sum_LikelihoodRatio",20,-0.1,1),"Reco_Sum_LikelihoodRatio",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Reco_Sum_LikelihoodTimesMERatio","Reco_Sum_LikelihoodTimesMERatio",20,-0.1,1),"Reco_Sum_LikelihoodTimesMERatio",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Reco_TTBBME_best_TTLikelihood_comb","Reco_TTBBME_best_TTLikelihood_comb",20,-0.1,1),"Reco_TTBBME_best_TTLikelihood_comb",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",20,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",20,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihood_best_TTBBLikelihood","Reco_TTBBLikelihood_best_TTBBLikelihood",20,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihood",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb","Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",20,-0.1,1),"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Reco_Dr_BB_best_TTLikelihood","Reco_Dr_BB_best_TTLikelihood",20,-0.1,1),"Reco_Dr_BB_best_TTLikelihood",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Reco_TTBBME_off_best_TTLikelihood_comb","Reco_TTBBME_off_best_TTLikelihood_comb",20,-0.1,1),"Reco_TTBBME_off_best_TTLikelihood_comb",plotselection,plotlabel),
        #Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb","Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",20,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",plotselection,plotlabel),
    ]
    
    plots+=plots64+plots63+plots54+plots53+plots44+plots43
    discriminatorPlots=plots
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

# 3 and 4 tags with minimal node output values 
#'DNN_Out_4j3t_ttH',
#'DNN_Out_4j3t_ttbarBB',
#'DNN_Out_4j3t_ttbar2B',
#'DNN_Out_4j3t_ttbarB',
#'DNN_Out_4j3t_ttbarCC',
#'DNN_Out_4j3t_ttbarlf',
#'DNN_Out_5j3t_ttH',
#'DNN_Out_5j3t_ttbarBB',
#'DNN_Out_5j3t_ttbar2B',
#'DNN_Out_5j3t_ttbarB',
#'DNN_Out_5j3t_ttbarCC',
#'DNN_Out_5j3t_ttbarlf',
#'DNN_Out_6j3t_ttH',
#'DNN_Out_6j3t_ttbarBB',
#'DNN_Out_6j3t_ttbar2B',
#'DNN_Out_6j3t_ttbarB',
#'DNN_Out_6j3t_ttbarCC',
#'DNN_Out_6j3t_ttbarlf',


## only 3 tag events
#'DNN_Out_4j3t_ttH',
#'DNN_Out_4j3t_ttbarBB',
#'DNN_Out_4j3t_ttbar2B',
#'DNN_Out_4j3t_ttbarB',
#'DNN_Out_4j3t_ttbarCC',
#'DNN_Out_4j3t_ttbarlf',
#'DNN_Out_5j3t_ttH',
#'DNN_Out_5j3t_ttbarBB',
#'DNN_Out_5j3t_ttbar2B',
#'DNN_Out_5j3t_ttbarB',
#'DNN_Out_5j3t_ttbarCC',
#'DNN_Out_5j3t_ttbarlf',
#'DNN_Out_6j3t_ttH',
#'DNN_Out_6j3t_ttbarBB',
#'DNN_Out_6j3t_ttbar2B',
#'DNN_Out_6j3t_ttbarB',
#'DNN_Out_6j3t_ttbarCC',
#'DNN_Out_6j3t_ttbarlf',

## only 4 tag events 
#'DNN_Out_4j3t_ttH',
#'DNN_Out_4j3t_ttbarBB',
#'DNN_Out_4j3t_ttbar2B',
#'DNN_Out_4j3t_ttbarB',
#'DNN_Out_4j3t_ttbarCC',
#'DNN_Out_4j3t_ttbarlf',
#'DNN_Out_5j3t_ttH',
#'DNN_Out_5j3t_ttbarBB',
#'DNN_Out_5j3t_ttbar2B',
#'DNN_Out_5j3t_ttbarB',
#'DNN_Out_5j3t_ttbarCC',
#'DNN_Out_5j3t_ttbarlf',
#'DNN_Out_6j3t_ttH',
#'DNN_Out_6j3t_ttbarBB',
#'DNN_Out_6j3t_ttbar2B',
#'DNN_Out_6j3t_ttbarB',
#'DNN_Out_6j3t_ttbarCC',
#'DNN_Out_6j3t_ttbarlf',
    ]

    # 3 and 4 tags
    nhistobins_MultiDNN=[15,  15 , 15, 15,15, 15,
                         15, 15, 15, 15, 15, 15 ,
                         15, 15, 15, 12, 15, 15  ]
    minxvals_MultiDNN=[0.16, 0.16, 0.16, 0.2, 0.2, 0.2,
                       0.16, 0.16, 0.2, 0.2, 0.2, 0.2,
                       0.16, 0.16, 0.2, 0.2, 0.2, 0.2        ]
    maxxvals_MultiDNN=[0.75, 0.8, 0.65, 0.4, 0.4, 0.63,
                       0.85, 0.8, 0.6, 0.45, 0.4, 0.5,
                       0.85, 0.8, 0.65, 0.5, 0.4, 0.6     ]

    # 3 and 4 tags with minimal node output of 0.25
    #nhistobins_MultiDNN+=[15,  15 , 15, 15,15, 15,
                         #15, 15, 15, 15, 15, 15 ,
                         #15, 15, 15, 12, 15, 15  ]
    #minxvals_MultiDNN+=[0.3]*18
    #maxxvals_MultiDNN+=[0.75, 0.8, 0.65, 0.4, 0.4, 0.63,
                       #0.85, 0.8, 0.6, 0.45, 0.4, 0.5,
                       #0.85, 0.8, 0.65, 0.5, 0.4, 0.6     ]
    
    ## only 3 tags
    #nhistobins_MultiDNN+=[15,  15 , 15, 15,15, 15, 15, 15, 15, 15, 15, 15 , 15, 15, 15, 12, 15, 15  ]
    #minxvals_MultiDNN+=[0.16, 0.16, 0.16, 0.16, 0.2, 0.2,
                       #0.16, 0.16, 0.2, 0.16, 0.2, 0.2,
                       #0.16, 0.16, 0.16, 0.2, 0.2, 0.2        ]
    #maxxvals_MultiDNN+=[0.75, 0.8, 0.65, 0.4, 0.4, 0.63,
                       #0.85, 0.8, 0.6, 0.45, 0.4, 0.5,
                       #0.85, 0.8, 0.65, 0.5, 0.4, 0.6  ]

    ## only 4 tags
    #nhistobins_MultiDNN+=[9,  15 , 3, 3, 4, 5,
                          #10, 10, 4, 3, 4, 4 ,
                          #10, 10, 10, 4, 5, 5  ]
    #minxvals_MultiDNN+=[0.16, 0.25, 0.2, 0.2, 0.16, 0.16,
                        #0.2, 0.16, 0.2, 0.2, 0.2, 0.2,
                        #0.2, 0.2, 0.2, 0.2, 0.2, 0.2        ]
    #maxxvals_MultiDNN+=[0.85, 0.85, 0.3, 0.3, 0.3, 0.3,
                        #0.9, 0.9, 0.5, 0.35, 0.4, 0.5,
                        #0.9, 0.9, 0.45, 0.4, 0.4, 0.4     ]

    discrs+=discrs_MultiDNN
    nhistobins+=nhistobins_MultiDNN
    minxvals+=minxvals_MultiDNN
    maxxvals+=maxxvals_MultiDNN
    categories+=categorienames_MultiDNN
    
    # now do only MEM for 4 tag events 
    
    #categorienames_MEM=[
              
              #### only 4 tag events 
              #("(N_Jets==4&&N_BTagsM>=4)","ljets_j4_tge4_MEM",""),
              #("(N_Jets==5&&N_BTagsM>=4)","ljets_j5_tge4_MEM",""),             
              #("(N_Jets>=6&&N_BTagsM>=4)","ljets_jge6_tge4_MEM",""),
              #("(N_Jets>=6&&N_BTagsM==3)","ljets_jge6_t3_MEM",""),
              #]
    
    
    #discrs_MEM=[
#memexp,
#memexp,
#memexp,
#memexp,

    #]
    ##nhistobins_MultiDNN= [   7,   10,    12,   7,   7,    12,   7,   7,    7,   8,   7,    7,   7,   7,    7,   7,   7,    4,]
    ##minxvals_MultiDNN=   [ 0.2,  0.16, 0.17, 0.16,  0.16, 0.18, 0.2,  0.2, 0.18, 0.2,  0.16, 0.16, 0.17,  0.17, 0.21, 0.17,  0.17, 0.19,]
    ##maxxvals_MultiDNN=   [0.6,  0.6, 0.7,    0.6,  0.6, 0.7,    0.4,  0.4, 0.35,    0.55,  0.5, 0.55,    0.35,  0.35, 0.3,    0.5,  0.4, 0.3,]
    ##nhistobins_MultiDNN+=[12,12,7,7,7,7]
    ##minxvals_MultiDNN+=[0.17,0.18,0.18,0.16,0.21,0.19]
    ##maxxvals_MultiDNN+=[0.7,0.7,0.35,0.55,0.3,0.3]
    #nhistobins_MEM=[10,10,10,20]
    #minxvals_MEM=[0.0,0.0,0.0,0.0]
    #maxxvals_MEM=[1.0,1.0,1.0,1.0]
    
    #discrs+=discrs_MEM
    #nhistobins+=nhistobins_MEM
    #minxvals+=minxvals_MEM
    #maxxvals+=maxxvals_MEM
    #categories+=categorienames_MEM    

            
    # get input for plotting function
    # plotPreselections= [c[0] for c in categories]
    # binlabels= [c[1] for c in categories]

    # discriminatorPlots=[]
    # DNNplots=[]
    # print len(discrs),len(plotPreselections),len(binlabels),len(nhistobins),len(minxvals),len(maxxvals),
    # assert(len(set([len(discrs),len(plotPreselections),len(binlabels),len(nhistobins),len(minxvals),len(maxxvals)]))==1)
    # print len(zip(discrs,plotPreselections,binlabels,nhistobins,minxvals,maxxvals))
    # for discr,b,bl,nb,minx,maxx in zip(discrs,plotPreselections,binlabels,nhistobins,minxvals,maxxvals):
    #     DNNplots.append(Plot(ROOT.TH1F(discrname+"_"+bl,"final discriminator ("+bl+")",nb,minx,maxx),discr,b,bl))
    # discriminatorPlots+=DNNplots
    
    
    
    systsamples=[]
    for sample in samples:
        for sysname,sysfilename in zip(otherSystNames,otherSystFileNames):
            thisnewsel=sample.selection
            systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),thisnewsel,sample.nick+sysname,samDict=sampleDict))
            # now add the UE and hdamp samples only for ttbar 
        if sample.nick.startswith("ttbarPlus") or sample.nick == "ttbarOther":
                for ue_hdamp, ue_hdamp_file in zip(hdamp_ue_systnames_tt_all, hdamp_ue_filenames_tt_all):
                    systsamples.append(Sample(sample.name+ue_hdamp,sample.color,ue_hdamp_file,thisnewsel,sample.nick+ue_hdamp,samDict=sampleDict))
        if sample.nick=="ttbarOther":
                for ue_hdamp, ue_hdamp_file in zip(hdamp_ue_systnames_tt_lf, hdamp_ue_filenames_tt_lf):
                    systsamples.append(Sample(sample.name+ue_hdamp,sample.color,ue_hdamp_file,thisnewsel,sample.nick+ue_hdamp,samDict=sampleDict))
        if sample.nick=="ttbarPlusCCbar":
                for ue_hdamp, ue_hdamp_file in zip(hdamp_ue_systnames_tt_cc, hdamp_ue_filenames_tt_cc):
                    systsamples.append(Sample(sample.name+ue_hdamp,sample.color,ue_hdamp_file,thisnewsel,sample.nick+ue_hdamp,samDict=sampleDict))
        if sample.nick=="ttbarPlusB":
                for ue_hdamp, ue_hdamp_file in zip(hdamp_ue_systnames_tt_b, hdamp_ue_filenames_tt_b):
                    systsamples.append(Sample(sample.name+ue_hdamp,sample.color,ue_hdamp_file,thisnewsel,sample.nick+ue_hdamp,samDict=sampleDict))
        if sample.nick=="ttbarPlus2B":
                for ue_hdamp, ue_hdamp_file in zip(hdamp_ue_systnames_tt_2b, hdamp_ue_filenames_tt_2b):
                    systsamples.append(Sample(sample.name+ue_hdamp,sample.color,ue_hdamp_file,thisnewsel,sample.nick+ue_hdamp,samDict=sampleDict))
        if sample.nick=="ttbarPlusBBbar":
                for ue_hdamp, ue_hdamp_file in zip(hdamp_ue_systnames_tt_bb, hdamp_ue_filenames_tt_bb):
                    systsamples.append(Sample(sample.name+ue_hdamp,sample.color,ue_hdamp_file,thisnewsel,sample.nick+ue_hdamp,samDict=sampleDict))
                                

    ## WARNING: Adjust Slice for samples if changing ttbar contributions


    #allsamples=samples+systsamples
    #allsystnames=weightSystNames+otherSystNames+PSSystNames
    allsamples=samples
    allsystnames=weightSystNames+otherSystNames
    print allsystnames

    addRealDataAllHistos('/nfs/dust/cms/user/pkeicher/ttH_2018/pyroot-plotscripts/workdir/limits_v42_1D_philip/output_limitInput.root',[s.nick for s in samples_data],discriminatorPlots,forceOverwrite=True)# use this version for all histograms even if they do not follow the cat_disc_var naming scheme
    sys.exit("Done with 'addRealDataAllHistos'")
    # plot everything, except during drawParallel step
    # Create file for data cards
    if analysis.doDrawParallel==False or analysis.plotNumber == None :
        #print type(analysis.rootFilePath), analysis.rootFilePath
        #print os.path.exists(analysis.rootFilePath)
        #raw_input()
        if not os.path.exists(analysis.rootFilePath):
        #if False:
            
            print "Doing plotParallel step since root file was not found.", analysis.rootFilePath
            THEoutputpath=plotParallel(name,350000,discriminatorPlots,samples+samples_data+systsamples,[''],['1.'],weightSystNames,systWeights,additionalvariables,[["memDB","/nfs/dust/cms/user/kelmorab/DataBases/MemDataBase_ttH_2018",True]],"/nfs/dust/cms/user/pkeicher/ttH_2018/pyroot-plotscripts/treejson_v42.json",otherSystNames,addCodeInterfacePaths=["pyroot-plotscripts-base/dNNInterface_Keras_cool.py"],cirun=False,StopAfterCompileStep=False,haddParallel=True,useGenWeightNormMap=True,useThisSampleForVariableSetup=samples[9])
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

            addRealDataAllHistos(renamedPath,[s.nick for s in samples_data],discriminatorPlots,forceOverwrite=True) # use this version for all histograms even if they do not follow the cat_disc_var naming scheme
            #addRealData(renamedPath,[s.nick for s in samples_data],binlabels,discrname)
            # addDataAllHisto(outputpath[:-5]+'_limitInput.root',[s.nick for s in samples[9:]],binlabels,allsystnames,discrname)
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
