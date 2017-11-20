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
from limittools import makeDatacards
from limittools import makeDatacardsParallel
from limittools import calcLimits
from limittools import replaceQ2scale

from analysisClass import *
from plotconfig_v14ULTRAFAST import *


def main(argv):

    # Create analysis object with output name
    name='controlYields_v23Fast'
    #analysis=Analysis(name,argv,'/nfs/dust/cms/user/mharrend/doktorarbeit/latest/ttbb-cutbased-analysis_limitInput.root')
    analysis=Analysis(name,argv,'/nfs/dust/cms/user/kelmorab/plotscriptsSpring17/Sep17/pyroot-plotscripts/NOTDEFINED/output_limitInput.root ', signalProcess='ttH')
    #analysis=Analysis(name,argv,'/nfs/dust/cms/user/mharrend/doktorarbeit/output20170626-reference/workdir/ttbb-cutbased-analysis/output_limitInput.root')

    analysis.plotBlinded=False
    analysis.makeSimplePlots=False
    analysis.makeMCControlPlots=True
    analysis.makeDatacards=False
    analysis.checkBins=False
    analysis.makeEventYields=True

    # Make sure proper plotconfig is loaded for either ttbb or ttH
    #print "We will import the following plotconfig: ", analysis.getPlotConfig()
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
    samples=samplesControlPlots
    #samples=samplesLimits

    samples_data=samplesDataControlPlots


    # Name of final discriminator, should not contain underscore
    discrname='finaldiscr'
    # define MEM discriminator variable
    memexp='(memDBp>0.0)*(memDBp)+(memDBp<=0.0)*(0.01)+(memDBp==1.0)*(0.01)'

    # define BDT output variables
    bdtweightpath="/nfs/dust/cms/user/kelmorab/Spring17BDTWeights/"
    bdtset="Spring17v2"
    alternativebdtset="Spring17v3_ttbb"
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

                         'conditionFor_finalbdt_ljets_j4_t3:=(N_Jets==4 && N_BTagsM==3)',
                         'conditionFor_finalbdt_ljets_j4_t4:=(N_Jets==4 && N_BTagsM==4)',
                         'conditionFor_finalbdt_ljets_j5_t3:=(N_Jets==5 && N_BTagsM==3)',
                         'conditionFor_finalbdt_ljets_j5_tge4:=(N_Jets==5 && N_BTagsM>=4)',
                         'conditionFor_finalbdt_ljets_jge6_t2:=(N_Jets>=6 && N_BTagsM==2)',
                         'conditionFor_finalbdt_ljets_jge6_t3:=(N_Jets>=6 && N_BTagsM==3)',
                         'conditionFor_finalbdt_ljets_jge6_tge4:=(N_Jets>=6 && N_BTagsM>=4)',
                         'conditionFor_alternativebdt_ljets_jge6_tge4:=(N_Jets>=6 && N_BTagsM>=4)',
                         'conditionFor_alternativebdt_ljets_jge6_t3:=(N_Jets>=6 && N_BTagsM==3)',
                         'conditionFor_alternativebdt_ljets_j5_tge4:=(N_Jets==5 && N_BTagsM>=4)',
                         'conditionFor_alternativebdt_ljets_j4_t4:=(N_Jets==4 && N_BTagsM==4)',
                         "GenEvt_I_TTPlusBB","GenEvt_I_TTPlusCC",

             			 'finalbdt_ljets_j4_t2:=Evt_HT_Jets',
             			 'finalbdt_ljets_j5_t2:=Evt_HT_Jets',
                         'finalbdt_ljets_j4_t3:='+bdtweightpath+'/weights_Final_43_'+bdtset+'.xml',
                         'finalbdt_ljets_j4_t4:='+bdtweightpath+'/weights_Final_44_'+bdtset+'.xml',
                         'finalbdt_ljets_j5_t3:='+bdtweightpath+'/weights_Final_53_'+bdtset+'.xml',
                         'finalbdt_ljets_j5_tge4:='+bdtweightpath+'/weights_Final_54_'+bdtset+'.xml',
                         'finalbdt_ljets_jge6_t2:='+bdtweightpath+'/weights_Final_62_'+bdtset+'.xml',
                         'finalbdt_ljets_jge6_t3:='+bdtweightpath+'/weights_Final_63_'+bdtset+'.xml',
                         'finalbdt_ljets_jge6_tge4:='+bdtweightpath+'/weights_Final_64_'+bdtset+'.xml',
                         'alternativebdt_ljets_jge6_tge4:='+bdtweightpath+'/weights_Final_64_'+alternativebdtset+'.xml',
                         'alternativebdt_ljets_jge6_t3:='+bdtweightpath+'/weights_Final_63_'+alternativebdtset+'.xml',
                         'alternativebdt_ljets_j5_tge4:='+bdtweightpath+'/weights_Final_54_'+alternativebdtset+'.xml',
                         'alternativebdt_ljets_j4_t4:='+bdtweightpath+'/weights_Final_44_'+alternativebdtset+'.xml',
                         ]
    additionalvariables+=GetMEPDFadditionalVariablesList("/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/rate_factors_onlyinternal_powhegpythia.csv")
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

    categories2D=[
                  #("(N_Jets>=6&&N_BTagsM==2)","6j2t",""),
                  #("(N_Jets==4&&N_BTagsM==3)","4j3t",""),
                  #("(N_Jets==5&&N_BTagsM==3)","5j3t",""),
                  ("(N_Jets>=6&&N_BTagsM==3 && finalbdt_ljets_jge6_t3<0.17)","6j3t lo",""),
                  ("(N_Jets>=6&&N_BTagsM==3 && finalbdt_ljets_jge6_t3>=0.17)","6j3t hi",""),
                  ("(N_Jets==4&&N_BTagsM>=4 && finalbdt_ljets_j4_t4<0.22)","4j4t lo",""),
                  ("(N_Jets==4&&N_BTagsM>=4 && finalbdt_ljets_j4_t4>=0.22)","4j4t hi",""),
                  ("(N_Jets==5&&N_BTagsM>=4 && finalbdt_ljets_j5_tge4<0.22)","5j4t lo",""),
                  ("(N_Jets==5&&N_BTagsM>=4 && finalbdt_ljets_j5_tge4>=0.22)","5j4t hi",""),
                  ("(N_Jets>=6&&N_BTagsM>=4  && finalbdt_ljets_jge6_tge4<0.17)","6j4t lo",""),
                  ("(N_Jets>=6&&N_BTagsM>=4  && finalbdt_ljets_jge6_tge4>=0.17)","6j4t hi",""),
                  
    ]


    # selections for categories
    categories2Dsel="("+categories2D[0][0]
    for cat in categories2D[1:]:
      categories2Dsel+="||"+cat[0]
    categories2Dsel+=")"


    # category strings
    catstring2D="0"
    for i,cat in enumerate(categories2D):
        catstring2D+=("+"+str(i+1)+"*"+cat[0])


    # book plots
    plotlabel="1 lepton, #geq 4 jets, #geq 2 b-tags"
    plotlabelboosted="#splitline{1 lepton, #geq 4 jets, #geq 2 b-tags}{#geq 1 C/A 1.5 jet p_{T} > 200 GeV}"
    plotselection="(N_Jets>=4&&N_BTagsM>=2)"
    plots=[
        Plot(ROOT.TH1F("JT" ,"jet-tag categories",len(categoriesJT),0.5,0.5+len(categoriesJT)),catstringJT,categoriesJTsel,"1 lepton"),
        #Plot(ROOT.TH1F("splitJT" ,"jet-tag 2D categories",len(categories2D),0.5,0.5+len(categories2D)),catstring2D,categories2Dsel,"1 lepton"),
        
        #Plot(ROOT.TH1F("BCAT" ,"jet-tag + boosted categories",len(categoriesJTB),0.5,0.5+len(categoriesJTB)),catstringJTB,categoriesJTBsel,"1 lepton"),
        #Plot(ROOT.TH1F("N_Jets","Number of ak4 jets",7,3.5,10.5),"N_Jets",plotselection,plotlabel),
        #Plot(ROOT.TH1F("N_BTagsM","Number of b-tags",4,1.5,5.5),"N_BTagsM",plotselection,plotlabel),
        #Plot(ROOT.TH1F("CSV0","B-tag of leading jet",22,-.1,1),"Jet_CSV[0]",plotselection,plotlabel),
        #Plot(ROOT.TH1F("CSV1","B-tag of second jet",22,-.1,1),"Jet_CSV[1]",plotselection,plotlabel),
        #Plot(ROOT.TH1F("CSV","B-tag of all jets",22,-.1,1),"Jet_CSV",plotselection,plotlabel),
        
        #Plot(ROOT.TH1F("eta1","#eta of leading jet",50,-2.5,2.5),"Jet_Eta[0]",plotselection,plotlabel),
        #Plot(ROOT.TH1F("eta2","#eta of second jet",50,-2.5,2.5),"Jet_Eta[1]",plotselection,plotlabel),
        #Plot(ROOT.TH1F("phij1","#phi of leading jet",64,-3.2,3.2),"Jet_Phi[0]",plotselection,plotlabel),
        ###Plot(ROOT.TH1F("phij2","#phi of second jet",64,-3.2,3.2),"Jet_Phi[1]",plotselection,plotlabel),
        Plot(ROOT.TH1F("baseline","total events",1,0,3000),"Evt_HT_Jets",plotselection,plotlabel),
        #Plot(ROOT.TH1F("ptalljets","p_{T} of all jets",60,0,300),"Jet_Pt",plotselection,plotlabel),
        #Plot(ROOT.TH1F("etaalljets","#eta of all jets",60,-2.5,2.5),"Jet_Eta",plotselection,plotlabel),
        #Plot(ROOT.TH1F("pumvaalljets","PU MVA of all jets",60,0,1.0),"Jet_PileUpMVA",plotselection,plotlabel),
        #Plot(ROOT.TH1F("puidalljets","PU MVA of all jets",60,0,1.0),"Jet_PileUpID",plotselection,plotlabel),
        
        #Plot(ROOT.TH1F("csvalljets","csv of all jets",44,-.1,1),"Jet_CSV",plotselection,plotlabel),
        #Plot(ROOT.TH1F("leppt","lepton p_{T}",50,0,200),"LooseLepton_Pt[0]",plotselection,plotlabel),
        #Plot(ROOT.TH1F("lepeta","lepton #eta",50,-2.5,2.5),"LooseLepton_Eta[0]",plotselection,plotlabel),
        #Plot(ROOT.TH1F("elleppt","electron p_{T}",50,0,200),"Electron_Pt[0]",'Electron_Pt[0]>10',plotlabel),
        #Plot(ROOT.TH1F("ellepeta","electron #eta",50,-2.5,2.5),"Electron_Eta[0]",'Electron_Pt[0]>10',plotlabel),
        #Plot(ROOT.TH1F("muleppt","muon p_{T}",50,0,200),"Muon_Pt[0]",'Muon_Pt[0]>10',plotlabel),
        #Plot(ROOT.TH1F("mulepeta","muon #eta",50,-2.5,2.5),"Muon_Eta[0]",'Muon_Pt[0]>10',plotlabel),
    ]
    
    plotsAdditional=[
        #Plot(ROOT.TH1F("CSV0NPVgeq20","B-tag of leading jet (NPV#geq20)",22,-.1,1),"Jet_CSV[0]",plotselection+"*(N_PrimaryVertices>=20)",plotlabel),
        #Plot(ROOT.TH1F("CSV1NPVgeq20","B-tag of second jet (NPV#geq20)",22,-.1,1),"Jet_CSV[1]",plotselection+"*(N_PrimaryVertices>=20)",plotlabel),
        #Plot(ROOT.TH1F("CSVNPVgeq20","B-tag of all jets (NPV#geq20)",22,-.1,1),"Jet_CSV",plotselection+"*(N_PrimaryVertices>=20)",plotlabel),

        #Plot(ROOT.TH1F("CSV0NPV15to20","B-tag of leading jet (15#leqNPV#leq20)",22,-.1,1),"Jet_CSV[0]",plotselection+"*(N_PrimaryVertices<=20 && N_PrimaryVertices>=15)",plotlabel),
        #Plot(ROOT.TH1F("CSV1NPV15to20","B-tag of second jet (15#leqNPV#leq20)",22,-.1,1),"Jet_CSV[1]",plotselection+"*(N_PrimaryVertices<=20 && N_PrimaryVertices>=15)",plotlabel),
        #Plot(ROOT.TH1F("CSVNPV15to20","B-tag of all jets (15#leqNPV#leq20)",22,-.1,1),"Jet_CSV",plotselection+"*(N_PrimaryVertices<=20 && N_PrimaryVertices>=15)",plotlabel),

        #Plot(ROOT.TH1F("CSV0NPV10to15","B-tag of leading jet (10#leqNPV#leq15)",22,-.1,1),"Jet_CSV[0]",plotselection+"*(N_PrimaryVertices<=15 && N_PrimaryVertices>=10)",plotlabel),
        #Plot(ROOT.TH1F("CSV1NPV10to15","B-tag of second jet (10#leqNPV#leq15)",22,-.1,1),"Jet_CSV[1]",plotselection+"*(N_PrimaryVertices<=15 && N_PrimaryVertices>=10)",plotlabel),
        #Plot(ROOT.TH1F("CSVNPV10to15","B-tag of all jets (10#leqNPV#leq15)",22,-.1,1),"Jet_CSV",plotselection+"*(N_PrimaryVertices<=15 && N_PrimaryVertices>=10)",plotlabel),

        #Plot(ROOT.TH1F("CSV0NPV0to10","B-tag of leading jet (0#leqNPV#leq10)",22,-.1,1),"Jet_CSV[0]",plotselection+"*(N_PrimaryVertices<=10 && N_PrimaryVertices>=0)",plotlabel),
        #Plot(ROOT.TH1F("CSV1NPV0to10","B-tag of second jet (0#leqNPV#leq10)",22,-.1,1),"Jet_CSV[1]",plotselection+"*(N_PrimaryVertices<=10 && N_PrimaryVertices>=0)",plotlabel),
        #Plot(ROOT.TH1F("CSVNPV0to10","B-tag of all jets (0#leqNPV#leq10)",22,-.1,1),"Jet_CSV",plotselection+"*(N_PrimaryVertices<=10 && N_PrimaryVertices>=0)",plotlabel),


        Plot(ROOT.TH1F("pt1","p_{T} of leading jet",50,0,500),"Jet_Pt[0]",plotselection,plotlabel),
        Plot(ROOT.TH1F("pt2","p_{T} of second jet",50,0,500),"Jet_Pt[1]",plotselection,plotlabel),
        Plot(ROOT.TH1F("pt3","p_{T} of third jet",40,0,400),"Jet_Pt[2]",plotselection,plotlabel),
        Plot(ROOT.TH1F("pt4","p_{T} of fourth jet",60,0,300),"Jet_Pt[3]",plotselection,plotlabel),
        Plot(ROOT.TH1F("pt5","p_{T} of fifth jet",40,0,200),"Jet_Pt[4]",plotselection,plotlabel),
        Plot(ROOT.TH1F("pt6","p_{T} of sixth jet",40,0,200),"Jet_Pt[5]",plotselection,plotlabel),
        #Plot(ROOT.TH1F("pt2tagged","p_{T} of second tagged jet",50,0,500),"TaggedJet_Pt[1]",plotselection,plotlabel),
        #Plot(ROOT.TH1F("pt1tagged","p_{T} of leading tagged jet",50,0,500),"TaggedJet_Pt[0]",plotselection,plotlabel),
        #Plot(ROOT.TH1F("pt3tagged","p_{T} of third tagged jet",40,0,400),"TaggedJet_Pt[2]",plotselection,plotlabel),
        #Plot(ROOT.TH1F("pt4tagged","p_{T} of fourth tagged jet",60,0,300),"TaggedJet_Pt[3]",plotselection,plotlabel),

        #Plot(ROOT.TH1F("Prescale_HLT_Ele27_eta2p1_WPTight_Gsf_vX","Prescale_HLT_Ele27_eta2p1_WPTight_Gsf_vX",50,0,2.0),"Prescale_HLT_Ele27_eta2p1_WPTight_Gsf_vX",plotselection,plotlabel),
        #Plot(ROOT.TH1F("Prescale_HLT_IsoMu22_vX","Prescale_HLT_IsoMu22_vX",50,0,2.0),"Prescale_HLT_IsoMu22_vX",plotselection,plotlabel),
        #Plot(ROOT.TH1F("Prescale_HLT_IsoTkMu22_vX","Prescale_HLT_IsoTkMu22_vX",50,0,2.0),"Prescale_HLT_IsoTkMu22_vX",plotselection,plotlabel),

        Plot(ROOT.TH1F("eliso","electron relative isolation",50,0,0.15),"Electron_RelIso[0]",plotselection,plotlabel),
        Plot(ROOT.TH1F("muiso","muon relative isolation",50,0,0.15),"Muon_RelIso[0]",plotselection,plotlabel),
        Plot(ROOT.TH1F("MET","missing transverse energy",50,0,200),"Evt_Pt_MET",plotselection,plotlabel),
        Plot(ROOT.TH1F("METphi","MET #phi",64,-3.2,3.2),"Evt_Phi_MET",plotselection,plotlabel),
        Plot(ROOT.TH1F("N_PrimaryVertices","Reconstructed primary vertices",26,-.5,25.5),"N_PrimaryVertices",plotselection,plotlabel),
        Plot(ROOT.TH1F("blrAll","B-tagging likelihood ratio",44,-6,10),"TMath::Log(Evt_blr_ETH/(1-Evt_blr_ETH))",plotselection,plotlabel),
        Plot(ROOT.TH1F("Evt_M_MinDeltaRJets","dijet mass of closest jets",30,0.,150),"Evt_M_MinDeltaRJets",plotselection,plotlabel),
        Plot(ROOT.TH1F("Evt_M_MinDeltaRTaggedJets","mass of closest tagged jets",45,0.,450),"Evt_M_MinDeltaRTaggedJets",plotselection,plotlabel),
        Plot(ROOT.TH1F("Evt_Dr_MinDeltaRJets","#Delta R of closest jets",50,0.,5.0),"Evt_Dr_MinDeltaRJets",plotselection,plotlabel),
        Plot(ROOT.TH1F("Evt_Dr_MinDeltaRTaggedJets","#Delta R of closest tagged jets",50,0.,5.0),"Evt_Dr_MinDeltaRTaggedJets",plotselection,plotlabel),
        Plot(ROOT.TH1F("Evt_Jet_MaxDeta_Jets","max #Delta #eta (jet,jet)",50,0.,5.0),"Evt_Jet_MaxDeta_Jets",plotselection,plotlabel),
        Plot(ROOT.TH1F("Evt_TaggedJet_MaxDeta_Jets","max #Delta #eta (tag,jet)",50,0.,5.0),"Evt_TaggedJet_MaxDeta_Jets",plotselection,plotlabel),
        Plot(ROOT.TH1F("Evt_TaggedJet_MaxDeta_TaggedJets","max #Delta #eta (tag,tag)",60,0.,6.0),"Evt_TaggedJet_MaxDeta_TaggedJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F("Evt_H1","Evt_H1",60,-0.2,0.4),"Evt_H1",plotselection,plotlabel),
        #Plot(ROOT.TH1F("Evt_H2","Evt_H2",60,-0.2,0.4),"Evt_H2",plotselection,plotlabel),
        #Plot(ROOT.TH1F("Evt_H3","Evt_H3",50,-0.05,1.05),"Evt_H3",plotselection,plotlabel),
        #Plot(ROOT.TH1F("Evt_H4","Evt_H4",50,-0.15,0.35),"Evt_H4",plotselection,plotlabel),
        #Plot(ROOT.TH1F("Sphericity","Sphericity",50,0,1),"Evt_Sphericity",plotselection,plotlabel),
        #Plot(ROOT.TH1F("Aplanarity","Aplanarity",50,0,0.5),"Evt_Aplanarity",plotselection,plotlabel),
        Plot(ROOT.TH1F("Evt_Deta_UntaggedJetsAverage","avg. #Delta #eta of untagged jets",50,0.,4.5),"Evt_Deta_UntaggedJetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1F("Evt_Deta_TaggedJetsAverage","avg. #Delta #eta of tagged jets",50,0.,4.5),"Evt_Deta_TaggedJetsAverage",plotselection,plotlabel),
        
        #Plot(ROOT.TH1F("Reco_Sum_LikelihoodRatio","Reco_Sum_LikelihoodRatio",50,-0.1,1),"Reco_Sum_LikelihoodRatio",plotselection,plotlabel),
        #Plot(ROOT.TH1F("Reco_Sum_LikelihoodTimesMERatio","Reco_Sum_LikelihoodTimesMERatio",50,-0.1,1),"Reco_Sum_LikelihoodTimesMERatio",plotselection,plotlabel),
        Plot(ROOT.TH1F("BDT_common5_input_closest_tagged_dijet_mass","BDT_common5_input_closest_tagged_dijet_mass",50,-0.1,200),"BDT_common5_input_closest_tagged_dijet_mass",plotselection,plotlabel),
        Plot(ROOT.TH1F("Evt_Pt_MinDeltaRTaggedJets","Evt_Pt_MinDeltaRTaggedJets",50,-0.1,500),"Evt_Pt_MinDeltaRTaggedJets",plotselection,plotlabel),
        Plot(ROOT.TH1F("Evt_M_MedianTaggedJets","Evt_M_MedianTaggedJets",50,-0.1,300),"Evt_M_MedianTaggedJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F("Reco_TTBBME_best_TTLikelihood_comb","Reco_TTBBME_best_TTLikelihood_comb",50,-0.1,1),"Reco_TTBBME_best_TTLikelihood_comb",plotselection,plotlabel),
        #Plot(ROOT.TH1F("Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",50,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",plotselection,plotlabel),
        Plot(ROOT.TH1F("BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",50,50,200),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotselection,plotlabel),
        Plot(ROOT.TH1F("Evt_M_MinDeltaRLeptonJet","mass of lepton and closest jet",30,0.,150),"Evt_M_MinDeltaRLeptonJet",plotselection,plotlabel),
        #Plot(ROOT.TH1F("Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",50,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",plotselection,plotlabel),
        #Plot(ROOT.TH1F("Reco_TTBBLikelihood_best_TTBBLikelihood","Reco_TTBBLikelihood_best_TTBBLikelihood",50,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihood",plotselection,plotlabel),
        #Plot(ROOT.TH1F("Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb","Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",50,-0.1,1),"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",plotselection,plotlabel),
        #Plot(ROOT.TH1F("Reco_Dr_BB_best_TTLikelihood","Reco_Dr_BB_best_TTLikelihood",50,-0.1,1),"Reco_Dr_BB_best_TTLikelihood",plotselection,plotlabel),
        #Plot(ROOT.TH1F("Reco_TTBBME_off_best_TTLikelihood_comb","Reco_TTBBME_off_best_TTLikelihood_comb",50,-0.1,1),"Reco_TTBBME_off_best_TTLikelihood_comb",plotselection,plotlabel),
        #Plot(ROOT.TH1F("Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb","Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",50,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",plotselection,plotlabel),
        
        
    ]


    plotlabel="1 lepton, 4 jets, 2 b-tags"
    plotselection="((N_Jets==4&&N_BTagsM==2))"
    #plotselection="((N_Jets==4&&N_BTagsM==2)&&!"+boosted+")"

    plotprefix="4j2t"
    plots42=[
        Plot(ROOT.TH1F(plotprefix+"Evt_HT","Sum p_{T} jets",75,0,1500),"Evt_HT_Jets",plotselection,plotlabel),
    ]

    plotlabel="1 lepton, 5 jets, 2 b-tags"
    plotselection="((N_Jets==5&&N_BTagsM==2))"
    #plotselection="((N_Jets==5&&N_BTagsM==2)&&!"+boosted+")"

    plotprefix="s52_"
    plots52=[
        Plot(ROOT.TH1F(plotprefix+"Evt_HT","Sum p_{T} jets",75,0,1500),"Evt_HT_Jets",plotselection,plotlabel),
    ]

    plotlabel="1 lepton, 4 jets, 3 b-tags"
    plotselection=categoriesJT[1][0]
    plotprefix="s43_"
    plots43=[
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",30,0.6,1.0),"BDT_common5_input_Evt_CSV_Average",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_Evt_Deta_JetsAverage","BDT_common5_input_Evt_Deta_JetsAverage",30,0.0,3.4),"BDT_common5_input_Evt_Deta_JetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_HT","BDT_common5_input_HT",30,0.0,1000.0),"BDT_common5_input_HT",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_M3","BDT_common5_input_M3",30,0.0,600.0),"BDT_common5_input_M3",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_MET","BDT_common5_input_MET",30,0.0,300.0),"BDT_common5_input_MET",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_MHT","BDT_common5_input_MHT",30,0.0,250.0),"BDT_common5_input_MHT",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_Mlb","BDT_common5_input_Mlb",30,0.0,250.0),"BDT_common5_input_Mlb",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_all_sum_pt_with_met","BDT_common5_input_all_sum_pt_with_met",30,200,900.0),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_aplanarity","BDT_common5_input_aplanarity",30,0.0,0.4),"BDT_common5_input_aplanarity",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_btag_disc_btags","BDT_common5_input_avg_btag_disc_btags",30,0.8,1.0),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","BDT_common5_input_avg_dr_tagged_jets",30,0.0,5.0),"BDT_common5_input_avg_dr_tagged_jets",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_best_higgs_mass","BDT_common5_input_best_higgs_mass",30,0.0,200.0),"BDT_common5_input_best_higgs_mass",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","BDT_common5_input_closest_tagged_dijet_mass",30,0.0,250.0),"BDT_common5_input_closest_tagged_dijet_mass",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dEta_fn","BDT_common5_input_dEta_fn",30,0.0,5.0),"BDT_common5_input_dEta_fn",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","BDT_common5_input_dev_from_avg_disc_btags",30,0.0,0.02),"BDT_common5_input_dev_from_avg_disc_btags",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","BDT_common5_input_dr_between_lep_and_closest_jet",30,0.0,3.0),"BDT_common5_input_dr_between_lep_and_closest_jet",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fifth_highest_CSV","BDT_common5_input_fifth_highest_CSV",30,-0.1,1.0),"BDT_common5_input_fifth_highest_CSV",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_first_jet_pt","BDT_common5_input_first_jet_pt",30,0.0,500.0),"BDT_common5_input_first_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fourth_highest_btag","BDT_common5_input_fourth_highest_btag",30,-0.1,1.0),"BDT_common5_input_fourth_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fourth_jet_pt","BDT_common5_input_fourth_jet_pt",30,0.0,300.0),"BDT_common5_input_fourth_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h0","BDT_common5_input_h0",30,0.15,0.45),"BDT_common5_input_h0",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h1","BDT_common5_input_h1",30,-0.2,0.2),"BDT_common5_input_h1",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h2","BDT_common5_input_h2",30,-0.2,0.3),"BDT_common5_input_h2",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h3","BDT_common5_input_h3",30,-0.2,0.2),"BDT_common5_input_h3",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_invariant_mass_of_everything","BDT_common5_input_invariant_mass_of_everything",30,500.0,1200.0),"BDT_common5_input_invariant_mass_of_everything",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_lowest_btag","BDT_common5_input_lowest_btag",30,0.8,1.0),"BDT_common5_input_lowest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_jet_jet","BDT_common5_input_maxeta_jet_jet",30,0.0,2.0),"BDT_common5_input_maxeta_jet_jet",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_jet_tag","BDT_common5_input_maxeta_jet_tag",30,0.0,2.0),"BDT_common5_input_maxeta_jet_tag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_tag_tag","BDT_common5_input_maxeta_tag_tag",30,0.0,2.0),"BDT_common5_input_maxeta_tag_tag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_min_dr_tagged_jets","BDT_common5_input_min_dr_tagged_jets",30,0.0,5.0),"BDT_common5_input_min_dr_tagged_jets",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","BDT_common5_input_pt_all_jets_over_E_all_jets",30,0.0,1.0),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_second_highest_btag","BDT_common5_input_second_highest_btag",30,0.8,1.0),"BDT_common5_input_second_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_second_jet_pt","BDT_common5_input_second_jet_pt",30,0.0,300.0),"BDT_common5_input_second_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_sphericity","BDT_common5_input_sphericity",30,0.0,1.0),"BDT_common5_input_sphericity",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",30,40.0,230.0),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_third_highest_btag","BDT_common5_input_third_highest_btag",30,0.8,1.0),"BDT_common5_input_third_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_third_jet_pt","BDT_common5_input_third_jet_pt",30,0.0,300.0),"BDT_common5_input_third_jet_pt",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_CSV_Average_Tagged","Evt_CSV_Average_Tagged",30,0.82,1.0),"Evt_CSV_Average_Tagged",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_CSV_Min","Evt_CSV_Min",30,0.0,1.0),"Evt_CSV_Min",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",30,0.0,5.0),"Evt_Dr_JetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRJets","Evt_Dr_MinDeltaRJets",30,0.0,3.0),"Evt_Dr_MinDeltaRJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRLeptonJet","Evt_Dr_MinDeltaRLeptonJet",30,0.0,3.0),"Evt_Dr_MinDeltaRLeptonJet",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRLeptonTaggedJet","Evt_Dr_MinDeltaRLeptonTaggedJet",30,0.0,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_TaggedJetsAverage","Evt_Dr_TaggedJetsAverage",30,0.0,5.0),"Evt_Dr_TaggedJetsAverage",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_E_PrimaryLepton","Evt_E_PrimaryLepton",30,0.0,500.0),"Evt_E_PrimaryLepton",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_Eta_JetsAverage","Evt_Eta_JetsAverage",30,-3.0,3.0),"Evt_Eta_JetsAverage",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_Eta_PrimaryLepton","Evt_Eta_PrimaryLepton",30,-3,3),"Evt_Eta_PrimaryLepton",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_Jet_MaxDeta_Jets","Evt_Jet_MaxDeta_Jets",30,0,5),"Evt_Jet_MaxDeta_Jets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",30,0.0,400.0),"Evt_M2_TaggedJetsAverage",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_M3","Evt_M3",30,0.0,400.0),"Evt_M3",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_JetsAverage","Evt_M_JetsAverage",30,0.0,30.0),"Evt_M_JetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_MedianTaggedJets","Evt_M_MedianTaggedJets",30,30.0,400.0),"Evt_M_MedianTaggedJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_MinDeltaRJets","Evt_M_MinDeltaRJets",30,10.0,250.0),"Evt_M_MinDeltaRJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",30,10.0,300.0),"Evt_M_MinDeltaRTaggedJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",30,0.0,50.0),"Evt_M_TaggedJetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Pt_MinDeltaRJets","Evt_Pt_MinDeltaRJets",30,0.0,400.0),"Evt_Pt_MinDeltaRJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Pt_MinDeltaRTaggedJets","Evt_Pt_MinDeltaRTaggedJets",30,0.0,400.0),"Evt_Pt_MinDeltaRTaggedJets",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_Pt_PrimaryLepton","Evt_Pt_PrimaryLepton",30,0.0,400.0),"Evt_Pt_PrimaryLepton",plotselection,plotlabel),    
        #Plot(ROOT.TH1F(plotprefix+"Evt_blr_ETH","Evt_blr_ETH",30,0.0,1.1),"Evt_blr_ETH",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"Evt_blr_ETH_transformed","Evt_blr_ETH_transformed",30,-10.0,10.0),"Evt_blr_ETH_transformed",plotselection,plotlabel),
        
        
        #Plot(ROOT.TH1F(plotprefix+"Reco_Sum_LikelihoodRatio","Reco_Sum_LikelihoodRatio",50,-0.1,1),"Reco_Sum_LikelihoodRatio",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_Sum_LikelihoodTimesMERatio","Reco_Sum_LikelihoodTimesMERatio",50,-0.1,1),"Reco_Sum_LikelihoodTimesMERatio",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBME_best_TTLikelihood_comb","Reco_TTBBME_best_TTLikelihood_comb",50,-0.1,1),"Reco_TTBBME_best_TTLikelihood_comb",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",50,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",50,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBLikelihood_best_TTBBLikelihood","Reco_TTBBLikelihood_best_TTBBLikelihood",50,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihood",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb","Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",50,-0.1,1),"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_Dr_BB_best_TTLikelihood","Reco_Dr_BB_best_TTLikelihood",50,-0.1,1),"Reco_Dr_BB_best_TTLikelihood",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBME_off_best_TTLikelihood_comb","Reco_TTBBME_off_best_TTLikelihood_comb",50,-0.1,1),"Reco_TTBBME_off_best_TTLikelihood_comb",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb","Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",50,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",plotselection,plotlabel),
    ]


    plotlabel="1 lepton, 4 jets, 4 b-tags"
    plotselection=categoriesJT[4][0]
    plotprefix="s44_"
    # weights_Final_44_MEMBDTv2.xml
    plots44=[
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",20,0.6,1.0),"BDT_common5_input_Evt_CSV_Average",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_Evt_Deta_JetsAverage","BDT_common5_input_Evt_Deta_JetsAverage",20,0.0,3.4),"BDT_common5_input_Evt_Deta_JetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_HT","BDT_common5_input_HT",20,0.0,1000.0),"BDT_common5_input_HT",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_M3","BDT_common5_input_M3",20,0.0,600.0),"BDT_common5_input_M3",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_MET","BDT_common5_input_MET",20,0.0,300.0),"BDT_common5_input_MET",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_MHT","BDT_common5_input_MHT",20,0.0,250.0),"BDT_common5_input_MHT",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_Mlb","BDT_common5_input_Mlb",20,0.0,250.0),"BDT_common5_input_Mlb",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_all_sum_pt_with_met","BDT_common5_input_all_sum_pt_with_met",20,200,900.0),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_aplanarity","BDT_common5_input_aplanarity",20,0.0,0.4),"BDT_common5_input_aplanarity",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_btag_disc_btags","BDT_common5_input_avg_btag_disc_btags",20,0.8,1.0),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","BDT_common5_input_avg_dr_tagged_jets",20,0.0,5.0),"BDT_common5_input_avg_dr_tagged_jets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_best_higgs_mass","BDT_common5_input_best_higgs_mass",20,0.0,200.0),"BDT_common5_input_best_higgs_mass",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","BDT_common5_input_closest_tagged_dijet_mass",20,0.0,250.0),"BDT_common5_input_closest_tagged_dijet_mass",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dEta_fn","BDT_common5_input_dEta_fn",20,0.0,5.0),"BDT_common5_input_dEta_fn",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","BDT_common5_input_dev_from_avg_disc_btags",20,0.0,0.02),"BDT_common5_input_dev_from_avg_disc_btags",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","BDT_common5_input_dr_between_lep_and_closest_jet",20,0.0,3.0),"BDT_common5_input_dr_between_lep_and_closest_jet",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fifth_highest_CSV","BDT_common5_input_fifth_highest_CSV",20,-0.1,1.0),"BDT_common5_input_fifth_highest_CSV",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_first_jet_pt","BDT_common5_input_first_jet_pt",20,0.0,500.0),"BDT_common5_input_first_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fourth_highest_btag","BDT_common5_input_fourth_highest_btag",20,0.8,1.0),"BDT_common5_input_fourth_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fourth_jet_pt","BDT_common5_input_fourth_jet_pt",20,0.0,300.0),"BDT_common5_input_fourth_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h0","BDT_common5_input_h0",20,0.15,0.45),"BDT_common5_input_h0",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h1","BDT_common5_input_h1",20,-0.2,0.2),"BDT_common5_input_h1",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h2","BDT_common5_input_h2",20,-0.2,0.3),"BDT_common5_input_h2",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h3","BDT_common5_input_h3",20,-0.2,0.2),"BDT_common5_input_h3",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_invariant_mass_of_everything","BDT_common5_input_invariant_mass_of_everything",20,500.0,1200.0),"BDT_common5_input_invariant_mass_of_everything",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_lowest_btag","BDT_common5_input_lowest_btag",20,0.8,1.0),"BDT_common5_input_lowest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_jet_jet","BDT_common5_input_maxeta_jet_jet",20,0.0,2.0),"BDT_common5_input_maxeta_jet_jet",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_jet_tag","BDT_common5_input_maxeta_jet_tag",20,0.0,2.0),"BDT_common5_input_maxeta_jet_tag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_tag_tag","BDT_common5_input_maxeta_tag_tag",20,0.0,2.0),"BDT_common5_input_maxeta_tag_tag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_min_dr_tagged_jets","BDT_common5_input_min_dr_tagged_jets",20,0.0,5.0),"BDT_common5_input_min_dr_tagged_jets",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","BDT_common5_input_pt_all_jets_over_E_all_jets",20,0.0,1.0),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_second_highest_btag","BDT_common5_input_second_highest_btag",20,0.8,1.0),"BDT_common5_input_second_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_second_jet_pt","BDT_common5_input_second_jet_pt",20,0.0,300.0),"BDT_common5_input_second_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_sphericity","BDT_common5_input_sphericity",20,0.0,1.0),"BDT_common5_input_sphericity",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",20,40.0,230.0),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_third_highest_btag","BDT_common5_input_third_highest_btag",20,0.8,1.0),"BDT_common5_input_third_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_third_jet_pt","BDT_common5_input_third_jet_pt",20,0.0,300.0),"BDT_common5_input_third_jet_pt",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_CSV_Average_Tagged","Evt_CSV_Average_Tagged",20,0.82,1.0),"Evt_CSV_Average_Tagged",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_CSV_Min","Evt_CSV_Min",20,0.0,1.0),"Evt_CSV_Min",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",20,0.0,3.0),"Evt_Deta_TaggedJetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",20,0.0,5.0),"Evt_Dr_JetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRJets","Evt_Dr_MinDeltaRJets",20,0.0,3.0),"Evt_Dr_MinDeltaRJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRLeptonJet","Evt_Dr_MinDeltaRLeptonJet",20,0.0,3.0),"Evt_Dr_MinDeltaRLeptonJet",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRLeptonTaggedJet","Evt_Dr_MinDeltaRLeptonTaggedJet",20,0.0,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_TaggedJetsAverage","Evt_Dr_TaggedJetsAverage",20,0.0,5.0),"Evt_Dr_TaggedJetsAverage",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_E_PrimaryLepton","Evt_E_PrimaryLepton",20,0.0,500.0),"Evt_E_PrimaryLepton",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_Eta_JetsAverage","Evt_Eta_JetsAverage",20,-3.0,3.0),"Evt_Eta_JetsAverage",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_Eta_PrimaryLepton","Evt_Eta_PrimaryLepton",20,-3,3),"Evt_Eta_PrimaryLepton",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_Jet_MaxDeta_Jets","Evt_Jet_MaxDeta_Jets",20,0,5),"Evt_Jet_MaxDeta_Jets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",20,0.0,400.0),"Evt_M2_TaggedJetsAverage",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_M3","Evt_M3",20,0.0,400.0),"Evt_M3",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_JetsAverage","Evt_M_JetsAverage",20,0.0,30.0),"Evt_M_JetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_MedianTaggedJets","Evt_M_MedianTaggedJets",20,30.0,400.0),"Evt_M_MedianTaggedJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_MinDeltaRJets","Evt_M_MinDeltaRJets",20,10.0,250.0),"Evt_M_MinDeltaRJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",20,10.0,300.0),"Evt_M_MinDeltaRTaggedJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",20,0.0,50.0),"Evt_M_TaggedJetsAverage",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_Pt_MinDeltaRJets","Evt_Pt_MinDeltaRJets",20,0.0,400.0),"Evt_Pt_MinDeltaRJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Pt_MinDeltaRTaggedJets","Evt_Pt_MinDeltaRTaggedJets",20,0.0,400.0),"Evt_Pt_MinDeltaRTaggedJets",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_Pt_PrimaryLepton","Evt_Pt_PrimaryLepton",20,0.0,400.0),"Evt_Pt_PrimaryLepton",plotselection,plotlabel),    
        #Plot(ROOT.TH1F(plotprefix+"Evt_blr_ETH","Evt_blr_ETH",20,0.0,1.1),"Evt_blr_ETH",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"Evt_blr_ETH_transformed","Evt_blr_ETH_transformed",20,-10.0,10.0),"Evt_blr_ETH_transformed",plotselection,plotlabel),
        
        #Plot(ROOT.TH1F(plotprefix+"Reco_Sum_LikelihoodRatio","Reco_Sum_LikelihoodRatio",20,-0.1,1),"Reco_Sum_LikelihoodRatio",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_Sum_LikelihoodTimesMERatio","Reco_Sum_LikelihoodTimesMERatio",20,-0.1,1),"Reco_Sum_LikelihoodTimesMERatio",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBME_best_TTLikelihood_comb","Reco_TTBBME_best_TTLikelihood_comb",20,-0.1,1),"Reco_TTBBME_best_TTLikelihood_comb",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",20,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",20,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBLikelihood_best_TTBBLikelihood","Reco_TTBBLikelihood_best_TTBBLikelihood",20,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihood",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb","Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",20,-0.1,1),"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_Dr_BB_best_TTLikelihood","Reco_Dr_BB_best_TTLikelihood",20,-0.1,1),"Reco_Dr_BB_best_TTLikelihood",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBME_off_best_TTLikelihood_comb","Reco_TTBBME_off_best_TTLikelihood_comb",20,-0.1,1),"Reco_TTBBME_off_best_TTLikelihood_comb",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb","Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",20,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",plotselection,plotlabel),
    ]


    plotlabel="1 lepton, 5 jets, 3 b-tags"
    plotselection=categoriesJT[2][0]
    plotprefix="s53_"
    plots53=[
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",30,0.6,1.0),"BDT_common5_input_Evt_CSV_Average",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_Evt_Deta_JetsAverage","BDT_common5_input_Evt_Deta_JetsAverage",30,0.0,3.4),"BDT_common5_input_Evt_Deta_JetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_HT","BDT_common5_input_HT",30,0.0,1000.0),"BDT_common5_input_HT",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_M3","BDT_common5_input_M3",30,0.0,600.0),"BDT_common5_input_M3",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_MET","BDT_common5_input_MET",30,0.0,300.0),"BDT_common5_input_MET",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_MHT","BDT_common5_input_MHT",30,0.0,250.0),"BDT_common5_input_MHT",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_Mlb","BDT_common5_input_Mlb",30,0.0,250.0),"BDT_common5_input_Mlb",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_all_sum_pt_with_met","BDT_common5_input_all_sum_pt_with_met",30,200,900.0),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_aplanarity","BDT_common5_input_aplanarity",30,0.0,0.4),"BDT_common5_input_aplanarity",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_btag_disc_btags","BDT_common5_input_avg_btag_disc_btags",30,0.8,1.0),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","BDT_common5_input_avg_dr_tagged_jets",30,0.0,5.0),"BDT_common5_input_avg_dr_tagged_jets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_best_higgs_mass","BDT_common5_input_best_higgs_mass",30,0.0,200.0),"BDT_common5_input_best_higgs_mass",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","BDT_common5_input_closest_tagged_dijet_mass",30,0.0,250.0),"BDT_common5_input_closest_tagged_dijet_mass",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dEta_fn","BDT_common5_input_dEta_fn",30,0.0,5.0),"BDT_common5_input_dEta_fn",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","BDT_common5_input_dev_from_avg_disc_btags",30,0.0,0.02),"BDT_common5_input_dev_from_avg_disc_btags",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","BDT_common5_input_dr_between_lep_and_closest_jet",30,0.0,3.0),"BDT_common5_input_dr_between_lep_and_closest_jet",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fifth_highest_CSV","BDT_common5_input_fifth_highest_CSV",30,-0.1,1.0),"BDT_common5_input_fifth_highest_CSV",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_first_jet_pt","BDT_common5_input_first_jet_pt",30,0.0,500.0),"BDT_common5_input_first_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fourth_highest_btag","BDT_common5_input_fourth_highest_btag",30,-0.1,1.0),"BDT_common5_input_fourth_highest_btag",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fourth_jet_pt","BDT_common5_input_fourth_jet_pt",30,0.0,300.0),"BDT_common5_input_fourth_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h0","BDT_common5_input_h0",30,0.15,0.45),"BDT_common5_input_h0",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h1","BDT_common5_input_h1",30,-0.2,0.2),"BDT_common5_input_h1",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h2","BDT_common5_input_h2",30,-0.2,0.3),"BDT_common5_input_h2",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h3","BDT_common5_input_h3",30,-0.2,0.2),"BDT_common5_input_h3",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_invariant_mass_of_everything","BDT_common5_input_invariant_mass_of_everything",30,500.0,1200.0),"BDT_common5_input_invariant_mass_of_everything",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_lowest_btag","BDT_common5_input_lowest_btag",30,0.8,1.0),"BDT_common5_input_lowest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_jet_jet","BDT_common5_input_maxeta_jet_jet",30,0.0,2.0),"BDT_common5_input_maxeta_jet_jet",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_jet_tag","BDT_common5_input_maxeta_jet_tag",30,0.0,2.0),"BDT_common5_input_maxeta_jet_tag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_tag_tag","BDT_common5_input_maxeta_tag_tag",30,0.0,2.0),"BDT_common5_input_maxeta_tag_tag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_min_dr_tagged_jets","BDT_common5_input_min_dr_tagged_jets",30,0.0,5.0),"BDT_common5_input_min_dr_tagged_jets",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","BDT_common5_input_pt_all_jets_over_E_all_jets",30,0.0,1.0),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_second_highest_btag","BDT_common5_input_second_highest_btag",30,0.8,1.0),"BDT_common5_input_second_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_second_jet_pt","BDT_common5_input_second_jet_pt",30,0.0,300.0),"BDT_common5_input_second_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_sphericity","BDT_common5_input_sphericity",30,0.0,1.0),"BDT_common5_input_sphericity",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",30,40.0,230.0),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_third_highest_btag","BDT_common5_input_third_highest_btag",30,0.8,1.0),"BDT_common5_input_third_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_third_jet_pt","BDT_common5_input_third_jet_pt",30,0.0,300.0),"BDT_common5_input_third_jet_pt",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_CSV_Average_Tagged","Evt_CSV_Average_Tagged",30,0.82,1.0),"Evt_CSV_Average_Tagged",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_CSV_Min","Evt_CSV_Min",30,0.0,1.0),"Evt_CSV_Min",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",30,0.0,5.0),"Evt_Dr_JetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRJets","Evt_Dr_MinDeltaRJets",30,0.0,3.0),"Evt_Dr_MinDeltaRJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRLeptonJet","Evt_Dr_MinDeltaRLeptonJet",30,0.0,3.0),"Evt_Dr_MinDeltaRLeptonJet",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRLeptonTaggedJet","Evt_Dr_MinDeltaRLeptonTaggedJet",30,0.0,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_TaggedJetsAverage","Evt_Dr_TaggedJetsAverage",30,0.0,5.0),"Evt_Dr_TaggedJetsAverage",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_E_PrimaryLepton","Evt_E_PrimaryLepton",30,0.0,500.0),"Evt_E_PrimaryLepton",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_Eta_JetsAverage","Evt_Eta_JetsAverage",30,-3.0,3.0),"Evt_Eta_JetsAverage",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_Eta_PrimaryLepton","Evt_Eta_PrimaryLepton",30,-3,3),"Evt_Eta_PrimaryLepton",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_Jet_MaxDeta_Jets","Evt_Jet_MaxDeta_Jets",30,0,5),"Evt_Jet_MaxDeta_Jets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",30,0.0,400.0),"Evt_M2_TaggedJetsAverage",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_M3","Evt_M3",30,0.0,400.0),"Evt_M3",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_M_JetsAverage","Evt_M_JetsAverage",30,0.0,30.0),"Evt_M_JetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_MedianTaggedJets","Evt_M_MedianTaggedJets",30,30.0,400.0),"Evt_M_MedianTaggedJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_MinDeltaRJets","Evt_M_MinDeltaRJets",30,10.0,250.0),"Evt_M_MinDeltaRJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",30,10.0,300.0),"Evt_M_MinDeltaRTaggedJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",30,0.0,50.0),"Evt_M_TaggedJetsAverage",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_Pt_MinDeltaRJets","Evt_Pt_MinDeltaRJets",30,0.0,400.0),"Evt_Pt_MinDeltaRJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Pt_MinDeltaRTaggedJets","Evt_Pt_MinDeltaRTaggedJets",30,0.0,400.0),"Evt_Pt_MinDeltaRTaggedJets",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_Pt_PrimaryLepton","Evt_Pt_PrimaryLepton",30,0.0,400.0),"Evt_Pt_PrimaryLepton",plotselection,plotlabel),    
        ##Plot(ROOT.TH1F(plotprefix+"Evt_blr_ETH","Evt_blr_ETH",30,0.0,1.1),"Evt_blr_ETH",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"Evt_blr_ETH_transformed","Evt_blr_ETH_transformed",30,-10.0,10.0),"Evt_blr_ETH_transformed",plotselection,plotlabel),
        
        #Plot(ROOT.TH1F(plotprefix+"Reco_Sum_LikelihoodRatio","Reco_Sum_LikelihoodRatio",30,-0.1,1),"Reco_Sum_LikelihoodRatio",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_Sum_LikelihoodTimesMERatio","Reco_Sum_LikelihoodTimesMERatio",30,-0.1,1),"Reco_Sum_LikelihoodTimesMERatio",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBME_best_TTLikelihood_comb","Reco_TTBBME_best_TTLikelihood_comb",30,-0.1,1),"Reco_TTBBME_best_TTLikelihood_comb",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",30,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",30,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBLikelihood_best_TTBBLikelihood","Reco_TTBBLikelihood_best_TTBBLikelihood",30,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihood",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb","Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",30,-0.1,1),"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_Dr_BB_best_TTLikelihood","Reco_Dr_BB_best_TTLikelihood",30,-0.1,1),"Reco_Dr_BB_best_TTLikelihood",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBME_off_best_TTLikelihood_comb","Reco_TTBBME_off_best_TTLikelihood_comb",30,-0.1,1),"Reco_TTBBME_off_best_TTLikelihood_comb",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb","Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",30,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",plotselection,plotlabel),
    ]


    plotlabel="1 lepton, 5 jets, #geq4 b-tags"
    plotselection=categoriesJT[5][0]
    plotprefix="s54_"
    plots54=[
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",20,0.6,1.0),"BDT_common5_input_Evt_CSV_Average",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_Evt_Deta_JetsAverage","BDT_common5_input_Evt_Deta_JetsAverage",20,0.0,3.4),"BDT_common5_input_Evt_Deta_JetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_HT","BDT_common5_input_HT",20,0.0,1000.0),"BDT_common5_input_HT",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_M3","BDT_common5_input_M3",20,0.0,600.0),"BDT_common5_input_M3",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_MET","BDT_common5_input_MET",20,0.0,300.0),"BDT_common5_input_MET",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_MHT","BDT_common5_input_MHT",20,0.0,250.0),"BDT_common5_input_MHT",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_Mlb","BDT_common5_input_Mlb",20,0.0,250.0),"BDT_common5_input_Mlb",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_all_sum_pt_with_met","BDT_common5_input_all_sum_pt_with_met",20,200,900.0),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_aplanarity","BDT_common5_input_aplanarity",20,0.0,0.4),"BDT_common5_input_aplanarity",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_btag_disc_btags","BDT_common5_input_avg_btag_disc_btags",20,0.8,1.0),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","BDT_common5_input_avg_dr_tagged_jets",20,0.0,5.0),"BDT_common5_input_avg_dr_tagged_jets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_best_higgs_mass","BDT_common5_input_best_higgs_mass",20,0.0,200.0),"BDT_common5_input_best_higgs_mass",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","BDT_common5_input_closest_tagged_dijet_mass",20,0.0,250.0),"BDT_common5_input_closest_tagged_dijet_mass",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dEta_fn","BDT_common5_input_dEta_fn",20,0.0,5.0),"BDT_common5_input_dEta_fn",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","BDT_common5_input_dev_from_avg_disc_btags",20,0.0,0.02),"BDT_common5_input_dev_from_avg_disc_btags",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","BDT_common5_input_dr_between_lep_and_closest_jet",20,0.0,3.0),"BDT_common5_input_dr_between_lep_and_closest_jet",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fifth_highest_CSV","BDT_common5_input_fifth_highest_CSV",20,-0.1,1.0),"BDT_common5_input_fifth_highest_CSV",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_first_jet_pt","BDT_common5_input_first_jet_pt",20,0.0,500.0),"BDT_common5_input_first_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fourth_highest_btag","BDT_common5_input_fourth_highest_btag",20,0.8,1.0),"BDT_common5_input_fourth_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fourth_jet_pt","BDT_common5_input_fourth_jet_pt",20,0.0,300.0),"BDT_common5_input_fourth_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h0","BDT_common5_input_h0",20,0.15,0.45),"BDT_common5_input_h0",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h1","BDT_common5_input_h1",20,-0.2,0.2),"BDT_common5_input_h1",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h2","BDT_common5_input_h2",20,-0.2,0.3),"BDT_common5_input_h2",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h3","BDT_common5_input_h3",20,-0.2,0.2),"BDT_common5_input_h3",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_invariant_mass_of_everything","BDT_common5_input_invariant_mass_of_everything",20,500.0,1200.0),"BDT_common5_input_invariant_mass_of_everything",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_lowest_btag","BDT_common5_input_lowest_btag",20,0.8,1.0),"BDT_common5_input_lowest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_jet_jet","BDT_common5_input_maxeta_jet_jet",20,0.0,2.0),"BDT_common5_input_maxeta_jet_jet",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_jet_tag","BDT_common5_input_maxeta_jet_tag",20,0.0,2.0),"BDT_common5_input_maxeta_jet_tag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_tag_tag","BDT_common5_input_maxeta_tag_tag",20,0.0,2.0),"BDT_common5_input_maxeta_tag_tag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_min_dr_tagged_jets","BDT_common5_input_min_dr_tagged_jets",20,0.0,5.0),"BDT_common5_input_min_dr_tagged_jets",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","BDT_common5_input_pt_all_jets_over_E_all_jets",20,0.0,1.0),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_second_highest_btag","BDT_common5_input_second_highest_btag",20,0.8,1.0),"BDT_common5_input_second_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_second_jet_pt","BDT_common5_input_second_jet_pt",20,0.0,300.0),"BDT_common5_input_second_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_sphericity","BDT_common5_input_sphericity",20,0.0,1.0),"BDT_common5_input_sphericity",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",20,40.0,230.0),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_third_highest_btag","BDT_common5_input_third_highest_btag",20,0.8,1.0),"BDT_common5_input_third_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_third_jet_pt","BDT_common5_input_third_jet_pt",20,0.0,300.0),"BDT_common5_input_third_jet_pt",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_CSV_Average_Tagged","Evt_CSV_Average_Tagged",20,0.82,1.0),"Evt_CSV_Average_Tagged",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_CSV_Min","Evt_CSV_Min",20,0.0,1.0),"Evt_CSV_Min",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",20,0.0,3.0),"Evt_Deta_TaggedJetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",20,0.0,5.0),"Evt_Dr_JetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRJets","Evt_Dr_MinDeltaRJets",20,0.0,3.0),"Evt_Dr_MinDeltaRJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRLeptonJet","Evt_Dr_MinDeltaRLeptonJet",20,0.0,3.0),"Evt_Dr_MinDeltaRLeptonJet",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRLeptonTaggedJet","Evt_Dr_MinDeltaRLeptonTaggedJet",20,0.0,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_TaggedJetsAverage","Evt_Dr_TaggedJetsAverage",20,0.0,5.0),"Evt_Dr_TaggedJetsAverage",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_E_PrimaryLepton","Evt_E_PrimaryLepton",20,0.0,500.0),"Evt_E_PrimaryLepton",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_Eta_JetsAverage","Evt_Eta_JetsAverage",20,-3.0,3.0),"Evt_Eta_JetsAverage",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_Eta_PrimaryLepton","Evt_Eta_PrimaryLepton",20,-3,3),"Evt_Eta_PrimaryLepton",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_Jet_MaxDeta_Jets","Evt_Jet_MaxDeta_Jets",20,0,5),"Evt_Jet_MaxDeta_Jets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",20,0.0,400.0),"Evt_M2_TaggedJetsAverage",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_M3","Evt_M3",20,0.0,400.0),"Evt_M3",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_M_JetsAverage","Evt_M_JetsAverage",20,0.0,30.0),"Evt_M_JetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_MedianTaggedJets","Evt_M_MedianTaggedJets",20,30.0,400.0),"Evt_M_MedianTaggedJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_MinDeltaRJets","Evt_M_MinDeltaRJets",20,10.0,250.0),"Evt_M_MinDeltaRJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",20,10.0,300.0),"Evt_M_MinDeltaRTaggedJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",20,0.0,50.0),"Evt_M_TaggedJetsAverage",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_Pt_MinDeltaRJets","Evt_Pt_MinDeltaRJets",20,0.0,400.0),"Evt_Pt_MinDeltaRJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Pt_MinDeltaRTaggedJets","Evt_Pt_MinDeltaRTaggedJets",20,0.0,400.0),"Evt_Pt_MinDeltaRTaggedJets",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_Pt_PrimaryLepton","Evt_Pt_PrimaryLepton",20,0.0,400.0),"Evt_Pt_PrimaryLepton",plotselection,plotlabel),    
        ##Plot(ROOT.TH1F(plotprefix+"Evt_blr_ETH","Evt_blr_ETH",20,0.0,1.1),"Evt_blr_ETH",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"Evt_blr_ETH_transformed","Evt_blr_ETH_transformed",20,-10.0,10.0),"Evt_blr_ETH_transformed",plotselection,plotlabel),
        
        #Plot(ROOT.TH1F(plotprefix+"Reco_Sum_LikelihoodRatio","Reco_Sum_LikelihoodRatio",20,-0.1,1),"Reco_Sum_LikelihoodRatio",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_Sum_LikelihoodTimesMERatio","Reco_Sum_LikelihoodTimesMERatio",20,-0.1,1),"Reco_Sum_LikelihoodTimesMERatio",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBME_best_TTLikelihood_comb","Reco_TTBBME_best_TTLikelihood_comb",20,-0.1,1),"Reco_TTBBME_best_TTLikelihood_comb",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",20,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",20,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBLikelihood_best_TTBBLikelihood","Reco_TTBBLikelihood_best_TTBBLikelihood",20,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihood",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb","Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",20,-0.1,1),"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_Dr_BB_best_TTLikelihood","Reco_Dr_BB_best_TTLikelihood",20,-0.1,1),"Reco_Dr_BB_best_TTLikelihood",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBME_off_best_TTLikelihood_comb","Reco_TTBBME_off_best_TTLikelihood_comb",20,-0.1,1),"Reco_TTBBME_off_best_TTLikelihood_comb",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb","Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",20,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",plotselection,plotlabel),
    ]


    plotlabel="1 lepton, #geq6 jets, 2 b-tags"
    plotselection=categoriesJT[0][0]
    plotprefix="s62_"
    plots62=[
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",30,0.6,1.0),"BDT_common5_input_Evt_CSV_Average",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_Evt_Deta_JetsAverage","BDT_common5_input_Evt_Deta_JetsAverage",30,0.0,3.4),"BDT_common5_input_Evt_Deta_JetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_HT","BDT_common5_input_HT",30,0.0,1000.0),"BDT_common5_input_HT",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_M3","BDT_common5_input_M3",30,0.0,600.0),"BDT_common5_input_M3",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_MET","BDT_common5_input_MET",30,0.0,300.0),"BDT_common5_input_MET",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_MHT","BDT_common5_input_MHT",30,0.0,250.0),"BDT_common5_input_MHT",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_Mlb","BDT_common5_input_Mlb",30,0.0,250.0),"BDT_common5_input_Mlb",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_all_sum_pt_with_met","BDT_common5_input_all_sum_pt_with_met",30,200,900.0),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_aplanarity","BDT_common5_input_aplanarity",30,0.0,0.4),"BDT_common5_input_aplanarity",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_btag_disc_btags","BDT_common5_input_avg_btag_disc_btags",30,0.8,1.0),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","BDT_common5_input_avg_dr_tagged_jets",30,0.0,5.0),"BDT_common5_input_avg_dr_tagged_jets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_best_higgs_mass","BDT_common5_input_best_higgs_mass",30,0.0,200.0),"BDT_common5_input_best_higgs_mass",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","BDT_common5_input_closest_tagged_dijet_mass",30,0.0,250.0),"BDT_common5_input_closest_tagged_dijet_mass",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dEta_fn","BDT_common5_input_dEta_fn",30,0.0,5.0),"BDT_common5_input_dEta_fn",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","BDT_common5_input_dev_from_avg_disc_btags",30,0.0,0.02),"BDT_common5_input_dev_from_avg_disc_btags",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","BDT_common5_input_dr_between_lep_and_closest_jet",30,0.0,3.0),"BDT_common5_input_dr_between_lep_and_closest_jet",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fifth_highest_CSV","BDT_common5_input_fifth_highest_CSV",30,-0.1,1.0),"BDT_common5_input_fifth_highest_CSV",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_first_jet_pt","BDT_common5_input_first_jet_pt",30,0.0,500.0),"BDT_common5_input_first_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fourth_highest_btag","BDT_common5_input_fourth_highest_btag",30,-0.1,1.0),"BDT_common5_input_fourth_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fourth_jet_pt","BDT_common5_input_fourth_jet_pt",30,0.0,300.0),"BDT_common5_input_fourth_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h0","BDT_common5_input_h0",30,0.15,0.45),"BDT_common5_input_h0",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h1","BDT_common5_input_h1",30,-0.2,0.2),"BDT_common5_input_h1",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h2","BDT_common5_input_h2",30,-0.2,0.3),"BDT_common5_input_h2",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h3","BDT_common5_input_h3",30,-0.2,0.2),"BDT_common5_input_h3",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_invariant_mass_of_everything","BDT_common5_input_invariant_mass_of_everything",30,500.0,1200.0),"BDT_common5_input_invariant_mass_of_everything",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_lowest_btag","BDT_common5_input_lowest_btag",30,0.8,1.0),"BDT_common5_input_lowest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_jet_jet","BDT_common5_input_maxeta_jet_jet",30,0.0,2.0),"BDT_common5_input_maxeta_jet_jet",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_jet_tag","BDT_common5_input_maxeta_jet_tag",30,0.0,2.0),"BDT_common5_input_maxeta_jet_tag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_tag_tag","BDT_common5_input_maxeta_tag_tag",30,0.0,2.0),"BDT_common5_input_maxeta_tag_tag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_min_dr_tagged_jets","BDT_common5_input_min_dr_tagged_jets",30,0.0,5.0),"BDT_common5_input_min_dr_tagged_jets",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","BDT_common5_input_pt_all_jets_over_E_all_jets",30,0.0,1.0),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_second_highest_btag","BDT_common5_input_second_highest_btag",30,0.8,1.0),"BDT_common5_input_second_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_second_jet_pt","BDT_common5_input_second_jet_pt",30,0.0,300.0),"BDT_common5_input_second_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_sphericity","BDT_common5_input_sphericity",30,0.0,1.0),"BDT_common5_input_sphericity",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",30,40.0,230.0),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_third_highest_btag","BDT_common5_input_third_highest_btag",30,0.8,1.0),"BDT_common5_input_third_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_third_jet_pt","BDT_common5_input_third_jet_pt",30,0.0,300.0),"BDT_common5_input_third_jet_pt",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_CSV_Average_Tagged","Evt_CSV_Average_Tagged",30,0.82,1.0),"Evt_CSV_Average_Tagged",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_CSV_Min","Evt_CSV_Min",30,0.0,1.0),"Evt_CSV_Min",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",30,0.0,5.0),"Evt_Dr_JetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRJets","Evt_Dr_MinDeltaRJets",30,0.0,3.0),"Evt_Dr_MinDeltaRJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRLeptonJet","Evt_Dr_MinDeltaRLeptonJet",30,0.0,3.0),"Evt_Dr_MinDeltaRLeptonJet",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRLeptonTaggedJet","Evt_Dr_MinDeltaRLeptonTaggedJet",30,0.0,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_TaggedJetsAverage","Evt_Dr_TaggedJetsAverage",30,0.0,5.0),"Evt_Dr_TaggedJetsAverage",plotselection,plotlabel),
        ###Plot(ROOT.TH1F(plotprefix+"Evt_E_PrimaryLepton","Evt_E_PrimaryLepton",30,0.0,500.0),"Evt_E_PrimaryLepton",plotselection,plotlabel),
        ###Plot(ROOT.TH1F(plotprefix+"Evt_Eta_JetsAverage","Evt_Eta_JetsAverage",30,-3.0,3.0),"Evt_Eta_JetsAverage",plotselection,plotlabel),
        ###Plot(ROOT.TH1F(plotprefix+"Evt_Eta_PrimaryLepton","Evt_Eta_PrimaryLepton",30,-3,3),"Evt_Eta_PrimaryLepton",plotselection,plotlabel),
        ###Plot(ROOT.TH1F(plotprefix+"Evt_Jet_MaxDeta_Jets","Evt_Jet_MaxDeta_Jets",30,0,5),"Evt_Jet_MaxDeta_Jets",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",30,0.0,400.0),"Evt_M2_TaggedJetsAverage",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_M3","Evt_M3",30,0.0,400.0),"Evt_M3",plotselection,plotlabel),
        ###Plot(ROOT.TH1F(plotprefix+"Evt_M_JetsAverage","Evt_M_JetsAverage",30,0.0,30.0),"Evt_M_JetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_MedianTaggedJets","Evt_M_MedianTaggedJets",30,30.0,400.0),"Evt_M_MedianTaggedJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_MinDeltaRJets","Evt_M_MinDeltaRJets",30,10.0,250.0),"Evt_M_MinDeltaRJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",30,10.0,300.0),"Evt_M_MinDeltaRTaggedJets",plotselection,plotlabel),
        ###Plot(ROOT.TH1F(plotprefix+"Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",30,0.0,50.0),"Evt_M_TaggedJetsAverage",plotselection,plotlabel),
        ###Plot(ROOT.TH1F(plotprefix+"Evt_Pt_MinDeltaRJets","Evt_Pt_MinDeltaRJets",30,0.0,400.0),"Evt_Pt_MinDeltaRJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Pt_MinDeltaRTaggedJets","Evt_Pt_MinDeltaRTaggedJets",30,0.0,400.0),"Evt_Pt_MinDeltaRTaggedJets",plotselection,plotlabel),
        ###Plot(ROOT.TH1F(plotprefix+"Evt_Pt_PrimaryLepton","Evt_Pt_PrimaryLepton",30,0.0,400.0),"Evt_Pt_PrimaryLepton",plotselection,plotlabel),    
        ###Plot(ROOT.TH1F(plotprefix+"Evt_blr_ETH","Evt_blr_ETH",30,0.0,1.1),"Evt_blr_ETH",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"Evt_blr_ETH_transformed","Evt_blr_ETH_transformed",30,-5.0,5.0),"Evt_blr_ETH_transformed",plotselection,plotlabel),
    ]


    plotlabel="1 lepton, #geq6 jets, 3 b-tags"
    plotselection=categoriesJT[3][0]
    plotprefix="s63_"
    plots63=[
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",30,0.6,1.0),"BDT_common5_input_Evt_CSV_Average",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_Evt_Deta_JetsAverage","BDT_common5_input_Evt_Deta_JetsAverage",30,0.0,3.4),"BDT_common5_input_Evt_Deta_JetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_HT","BDT_common5_input_HT",30,0.0,1000.0),"BDT_common5_input_HT",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_M3","BDT_common5_input_M3",30,0.0,600.0),"BDT_common5_input_M3",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_MET","BDT_common5_input_MET",30,0.0,300.0),"BDT_common5_input_MET",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_MHT","BDT_common5_input_MHT",30,0.0,250.0),"BDT_common5_input_MHT",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_Mlb","BDT_common5_input_Mlb",30,0.0,250.0),"BDT_common5_input_Mlb",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_all_sum_pt_with_met","BDT_common5_input_all_sum_pt_with_met",30,200,900.0),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_aplanarity","BDT_common5_input_aplanarity",30,0.0,0.4),"BDT_common5_input_aplanarity",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_btag_disc_btags","BDT_common5_input_avg_btag_disc_btags",30,0.8,1.0),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","BDT_common5_input_avg_dr_tagged_jets",30,0.0,5.0),"BDT_common5_input_avg_dr_tagged_jets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_best_higgs_mass","BDT_common5_input_best_higgs_mass",30,0.0,200.0),"BDT_common5_input_best_higgs_mass",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","BDT_common5_input_closest_tagged_dijet_mass",30,0.0,250.0),"BDT_common5_input_closest_tagged_dijet_mass",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dEta_fn","BDT_common5_input_dEta_fn",30,0.0,5.0),"BDT_common5_input_dEta_fn",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","BDT_common5_input_dev_from_avg_disc_btags",30,0.0,0.02),"BDT_common5_input_dev_from_avg_disc_btags",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","BDT_common5_input_dr_between_lep_and_closest_jet",30,0.0,3.0),"BDT_common5_input_dr_between_lep_and_closest_jet",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fifth_highest_CSV","BDT_common5_input_fifth_highest_CSV",30,-0.1,1.0),"BDT_common5_input_fifth_highest_CSV",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_first_jet_pt","BDT_common5_input_first_jet_pt",30,0.0,500.0),"BDT_common5_input_first_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fourth_highest_btag","BDT_common5_input_fourth_highest_btag",30,-0.1,1.0),"BDT_common5_input_fourth_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fourth_jet_pt","BDT_common5_input_fourth_jet_pt",30,0.0,300.0),"BDT_common5_input_fourth_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h0","BDT_common5_input_h0",30,0.15,0.45),"BDT_common5_input_h0",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h1","BDT_common5_input_h1",30,-0.2,0.2),"BDT_common5_input_h1",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h2","BDT_common5_input_h2",30,-0.2,0.3),"BDT_common5_input_h2",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h3","BDT_common5_input_h3",30,-0.2,0.2),"BDT_common5_input_h3",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_invariant_mass_of_everything","BDT_common5_input_invariant_mass_of_everything",30,500.0,1200.0),"BDT_common5_input_invariant_mass_of_everything",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_lowest_btag","BDT_common5_input_lowest_btag",30,0.8,1.0),"BDT_common5_input_lowest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_jet_jet","BDT_common5_input_maxeta_jet_jet",30,0.0,2.0),"BDT_common5_input_maxeta_jet_jet",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_jet_tag","BDT_common5_input_maxeta_jet_tag",30,0.0,2.0),"BDT_common5_input_maxeta_jet_tag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_tag_tag","BDT_common5_input_maxeta_tag_tag",30,0.0,2.0),"BDT_common5_input_maxeta_tag_tag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_min_dr_tagged_jets","BDT_common5_input_min_dr_tagged_jets",30,0.0,5.0),"BDT_common5_input_min_dr_tagged_jets",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","BDT_common5_input_pt_all_jets_over_E_all_jets",30,0.0,1.0),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_second_highest_btag","BDT_common5_input_second_highest_btag",30,0.8,1.0),"BDT_common5_input_second_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_second_jet_pt","BDT_common5_input_second_jet_pt",30,0.0,300.0),"BDT_common5_input_second_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_sphericity","BDT_common5_input_sphericity",30,0.0,1.0),"BDT_common5_input_sphericity",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",30,40.0,230.0),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_third_highest_btag","BDT_common5_input_third_highest_btag",30,0.8,1.0),"BDT_common5_input_third_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_third_jet_pt","BDT_common5_input_third_jet_pt",30,0.0,300.0),"BDT_common5_input_third_jet_pt",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_CSV_Average_Tagged","Evt_CSV_Average_Tagged",30,0.82,1.0),"Evt_CSV_Average_Tagged",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_CSV_Min","Evt_CSV_Min",30,0.0,1.0),"Evt_CSV_Min",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",30,0.0,5.0),"Evt_Dr_JetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRJets","Evt_Dr_MinDeltaRJets",30,0.0,3.0),"Evt_Dr_MinDeltaRJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRLeptonJet","Evt_Dr_MinDeltaRLeptonJet",30,0.0,3.0),"Evt_Dr_MinDeltaRLeptonJet",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRLeptonTaggedJet","Evt_Dr_MinDeltaRLeptonTaggedJet",30,0.0,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_TaggedJetsAverage","Evt_Dr_TaggedJetsAverage",30,0.0,5.0),"Evt_Dr_TaggedJetsAverage",plotselection,plotlabel),
        ###Plot(ROOT.TH1F(plotprefix+"Evt_E_PrimaryLepton","Evt_E_PrimaryLepton",30,0.0,500.0),"Evt_E_PrimaryLepton",plotselection,plotlabel),
        ###Plot(ROOT.TH1F(plotprefix+"Evt_Eta_JetsAverage","Evt_Eta_JetsAverage",30,-3.0,3.0),"Evt_Eta_JetsAverage",plotselection,plotlabel),
        ###Plot(ROOT.TH1F(plotprefix+"Evt_Eta_PrimaryLepton","Evt_Eta_PrimaryLepton",30,-3,3),"Evt_Eta_PrimaryLepton",plotselection,plotlabel),
        ###Plot(ROOT.TH1F(plotprefix+"Evt_Jet_MaxDeta_Jets","Evt_Jet_MaxDeta_Jets",30,0,5),"Evt_Jet_MaxDeta_Jets",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",30,0.0,400.0),"Evt_M2_TaggedJetsAverage",plotselection,plotlabel),
        ###Plot(ROOT.TH1F(plotprefix+"Evt_M3","Evt_M3",30,0.0,400.0),"Evt_M3",plotselection,plotlabel),
        ###Plot(ROOT.TH1F(plotprefix+"Evt_M_JetsAverage","Evt_M_JetsAverage",30,0.0,30.0),"Evt_M_JetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_MedianTaggedJets","Evt_M_MedianTaggedJets",30,30.0,400.0),"Evt_M_MedianTaggedJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_MinDeltaRJets","Evt_M_MinDeltaRJets",30,10.0,250.0),"Evt_M_MinDeltaRJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",30,10.0,300.0),"Evt_M_MinDeltaRTaggedJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",30,0.0,50.0),"Evt_M_TaggedJetsAverage",plotselection,plotlabel),
        ###Plot(ROOT.TH1F(plotprefix+"Evt_Pt_MinDeltaRJets","Evt_Pt_MinDeltaRJets",30,0.0,400.0),"Evt_Pt_MinDeltaRJets",plotselection,plotlabel),
        ###Plot(ROOT.TH1F(plotprefix+"Evt_Pt_MinDeltaRTaggedJets","Evt_Pt_MinDeltaRTaggedJets",30,0.0,400.0),"Evt_Pt_MinDeltaRTaggedJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Pt_PrimaryLepton","Evt_Pt_PrimaryLepton",30,0.0,400.0),"Evt_Pt_PrimaryLepton",plotselection,plotlabel),    
        ##Plot(ROOT.TH1F(plotprefix+"Evt_blr_ETH","Evt_blr_ETH",30,0.0,1.1),"Evt_blr_ETH",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"Evt_blr_ETH_transformed","Evt_blr_ETH_transformed",30,-1.0,6.0),"Evt_blr_ETH_transformed",plotselection,plotlabel),
        
        #Plot(ROOT.TH1F(plotprefix+"Reco_Sum_LikelihoodRatio","Reco_Sum_LikelihoodRatio",30,-0.1,1),"Reco_Sum_LikelihoodRatio",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_Sum_LikelihoodTimesMERatio","Reco_Sum_LikelihoodTimesMERatio",30,-0.1,1),"Reco_Sum_LikelihoodTimesMERatio",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBME_best_TTLikelihood_comb","Reco_TTBBME_best_TTLikelihood_comb",30,-0.1,1),"Reco_TTBBME_best_TTLikelihood_comb",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",30,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",30,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBLikelihood_best_TTBBLikelihood","Reco_TTBBLikelihood_best_TTBBLikelihood",30,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihood",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb","Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",30,-0.1,1),"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_Dr_BB_best_TTLikelihood","Reco_Dr_BB_best_TTLikelihood",30,-0.1,1),"Reco_Dr_BB_best_TTLikelihood",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBME_off_best_TTLikelihood_comb","Reco_TTBBME_off_best_TTLikelihood_comb",30,-0.1,1),"Reco_TTBBME_off_best_TTLikelihood_comb",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb","Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",30,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",plotselection,plotlabel),
    ]

    plotlabel="1 lepton, #geq6 jets, #geq4 b-tags"
    plotselection=categoriesJT[6][0]
    plotprefix="s64"
    plots64=[
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",20,0.6,1.0),"BDT_common5_input_Evt_CSV_Average",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_Evt_Deta_JetsAverage","BDT_common5_input_Evt_Deta_JetsAverage",20,0.0,3.4),"BDT_common5_input_Evt_Deta_JetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_HT","BDT_common5_input_HT",20,0.0,1000.0),"BDT_common5_input_HT",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_M3","BDT_common5_input_M3",20,0.0,600.0),"BDT_common5_input_M3",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_MET","BDT_common5_input_MET",20,0.0,300.0),"BDT_common5_input_MET",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_MHT","BDT_common5_input_MHT",20,0.0,250.0),"BDT_common5_input_MHT",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_Mlb","BDT_common5_input_Mlb",20,0.0,250.0),"BDT_common5_input_Mlb",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_all_sum_pt_with_met","BDT_common5_input_all_sum_pt_with_met",20,200,900.0),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_aplanarity","BDT_common5_input_aplanarity",20,0.0,0.4),"BDT_common5_input_aplanarity",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_btag_disc_btags","BDT_common5_input_avg_btag_disc_btags",20,0.8,1.0),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","BDT_common5_input_avg_dr_tagged_jets",20,0.0,5.0),"BDT_common5_input_avg_dr_tagged_jets",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_best_higgs_mass","BDT_common5_input_best_higgs_mass",20,0.0,200.0),"BDT_common5_input_best_higgs_mass",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","BDT_common5_input_closest_tagged_dijet_mass",20,0.0,250.0),"BDT_common5_input_closest_tagged_dijet_mass",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dEta_fn","BDT_common5_input_dEta_fn",20,0.0,5.0),"BDT_common5_input_dEta_fn",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","BDT_common5_input_dev_from_avg_disc_btags",20,0.0,0.02),"BDT_common5_input_dev_from_avg_disc_btags",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","BDT_common5_input_dr_between_lep_and_closest_jet",20,0.0,3.0),"BDT_common5_input_dr_between_lep_and_closest_jet",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fifth_highest_CSV","BDT_common5_input_fifth_highest_CSV",20,-0.1,1.0),"BDT_common5_input_fifth_highest_CSV",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_first_jet_pt","BDT_common5_input_first_jet_pt",20,0.0,500.0),"BDT_common5_input_first_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fourth_highest_btag","BDT_common5_input_fourth_highest_btag",20,0.8,1.0),"BDT_common5_input_fourth_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fourth_jet_pt","BDT_common5_input_fourth_jet_pt",20,0.0,300.0),"BDT_common5_input_fourth_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h0","BDT_common5_input_h0",20,0.15,0.45),"BDT_common5_input_h0",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h1","BDT_common5_input_h1",20,-0.2,0.2),"BDT_common5_input_h1",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h2","BDT_common5_input_h2",20,-0.2,0.3),"BDT_common5_input_h2",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h3","BDT_common5_input_h3",20,-0.2,0.2),"BDT_common5_input_h3",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_invariant_mass_of_everything","BDT_common5_input_invariant_mass_of_everything",20,500.0,1200.0),"BDT_common5_input_invariant_mass_of_everything",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_lowest_btag","BDT_common5_input_lowest_btag",20,0.8,1.0),"BDT_common5_input_lowest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_jet_jet","BDT_common5_input_maxeta_jet_jet",20,0.0,2.0),"BDT_common5_input_maxeta_jet_jet",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_jet_tag","BDT_common5_input_maxeta_jet_tag",20,0.0,2.0),"BDT_common5_input_maxeta_jet_tag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_tag_tag","BDT_common5_input_maxeta_tag_tag",20,0.0,2.0),"BDT_common5_input_maxeta_tag_tag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_min_dr_tagged_jets","BDT_common5_input_min_dr_tagged_jets",20,0.0,5.0),"BDT_common5_input_min_dr_tagged_jets",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","BDT_common5_input_pt_all_jets_over_E_all_jets",20,0.0,1.0),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_second_highest_btag","BDT_common5_input_second_highest_btag",20,0.8,1.0),"BDT_common5_input_second_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_second_jet_pt","BDT_common5_input_second_jet_pt",20,0.0,300.0),"BDT_common5_input_second_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_sphericity","BDT_common5_input_sphericity",20,0.0,1.0),"BDT_common5_input_sphericity",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",20,40.0,230.0),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_third_highest_btag","BDT_common5_input_third_highest_btag",20,0.8,1.0),"BDT_common5_input_third_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_third_jet_pt","BDT_common5_input_third_jet_pt",20,0.0,300.0),"BDT_common5_input_third_jet_pt",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_CSV_Average_Tagged","Evt_CSV_Average_Tagged",20,0.82,1.0),"Evt_CSV_Average_Tagged",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_CSV_Min","Evt_CSV_Min",20,0.0,1.0),"Evt_CSV_Min",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",20,0.0,3.0),"Evt_Deta_TaggedJetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",20,0.0,5.0),"Evt_Dr_JetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRJets","Evt_Dr_MinDeltaRJets",20,0.0,3.0),"Evt_Dr_MinDeltaRJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRLeptonJet","Evt_Dr_MinDeltaRLeptonJet",20,0.0,3.0),"Evt_Dr_MinDeltaRLeptonJet",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRLeptonTaggedJet","Evt_Dr_MinDeltaRLeptonTaggedJet",20,0.0,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Dr_TaggedJetsAverage","Evt_Dr_TaggedJetsAverage",20,0.0,5.0),"Evt_Dr_TaggedJetsAverage",plotselection,plotlabel),
        ##Plot(ROOT.TH1F(plotprefix+"Evt_E_PrimaryLepton","Evt_E_PrimaryLepton",20,0.0,500.0),"Evt_E_PrimaryLepton",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Eta_JetsAverage","Evt_Eta_JetsAverage",20,-3.0,3.0),"Evt_Eta_JetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Eta_PrimaryLepton","Evt_Eta_PrimaryLepton",20,-3,3),"Evt_Eta_PrimaryLepton",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Jet_MaxDeta_Jets","Evt_Jet_MaxDeta_Jets",20,0,5),"Evt_Jet_MaxDeta_Jets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",20,0.0,400.0),"Evt_M2_TaggedJetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M3","Evt_M3",20,0.0,400.0),"Evt_M3",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_JetsAverage","Evt_M_JetsAverage",20,0.0,30.0),"Evt_M_JetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_MedianTaggedJets","Evt_M_MedianTaggedJets",20,30.0,400.0),"Evt_M_MedianTaggedJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_MinDeltaRJets","Evt_M_MinDeltaRJets",20,10.0,250.0),"Evt_M_MinDeltaRJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",20,10.0,300.0),"Evt_M_MinDeltaRTaggedJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",20,0.0,50.0),"Evt_M_TaggedJetsAverage",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Pt_MinDeltaRJets","Evt_Pt_MinDeltaRJets",20,0.0,400.0),"Evt_Pt_MinDeltaRJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Pt_MinDeltaRTaggedJets","Evt_Pt_MinDeltaRTaggedJets",20,0.0,400.0),"Evt_Pt_MinDeltaRTaggedJets",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Evt_Pt_PrimaryLepton","Evt_Pt_PrimaryLepton",20,0.0,400.0),"Evt_Pt_PrimaryLepton",plotselection,plotlabel),    
        #Plot(ROOT.TH1F(plotprefix+"Evt_blr_ETH","Evt_blr_ETH",20,0.0,1.1),"Evt_blr_ETH",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"Evt_blr_ETH_transformed","Evt_blr_ETH_transformed",20,-1.0,10.0),"Evt_blr_ETH_transformed",plotselection,plotlabel),
        
        #Plot(ROOT.TH1F(plotprefix+"Reco_Sum_LikelihoodRatio","Reco_Sum_LikelihoodRatio",20,-0.1,1),"Reco_Sum_LikelihoodRatio",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_Sum_LikelihoodTimesMERatio","Reco_Sum_LikelihoodTimesMERatio",20,-0.1,1),"Reco_Sum_LikelihoodTimesMERatio",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBME_best_TTLikelihood_comb","Reco_TTBBME_best_TTLikelihood_comb",20,-0.1,1),"Reco_TTBBME_best_TTLikelihood_comb",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",20,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",20,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBLikelihood_best_TTBBLikelihood","Reco_TTBBLikelihood_best_TTBBLikelihood",20,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihood",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb","Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",20,-0.1,1),"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_Dr_BB_best_TTLikelihood","Reco_Dr_BB_best_TTLikelihood",20,-0.1,1),"Reco_Dr_BB_best_TTLikelihood",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBME_off_best_TTLikelihood_comb","Reco_TTBBME_off_best_TTLikelihood_comb",20,-0.1,1),"Reco_TTBBME_off_best_TTLikelihood_comb",plotselection,plotlabel),
        #Plot(ROOT.TH1F(plotprefix+"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb","Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",20,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",plotselection,plotlabel),
    ]

    #plotprefix="dnn_"
    #plotsDNNcontrol=[
        #Plot(ROOT.TH1F(plotprefix+"43_ttHnode","DNN ttH node",20,0,1),"aachen_Out_ttH","((N_Jets>=4&&N_BTagsM==3))","1 lepton, #geq4jets, 3 b-tags"),
        #Plot(ROOT.TH1F(plotprefix+"43_ttbbnode","DNN ttbb node",20,0,1),"aachen_Out_ttbarBB","((N_Jets>=4&&N_BTagsM==3))","1 lepton, #geq4jets, 3 b-tags"),
        #Plot(ROOT.TH1F(plotprefix+"43_tt2bnode","DNN tt2b node",20,0,1),"aachen_Out_ttbar2B","((N_Jets>=4&&N_BTagsM==3))","1 lepton, #geq4jets, 3 b-tags"),
        #Plot(ROOT.TH1F(plotprefix+"43_ttbnode","DNN ttb node",20,0,1),"aachen_Out_ttbarB","((N_Jets>=4&&N_BTagsM==3))","1 lepton, #geq4jets, 3 b-tags"),
        #Plot(ROOT.TH1F(plotprefix+"43_ttlfnode","DNN ttlf node",20,0,1),"aachen_Out_ttbarOther","((N_Jets>=4&&N_BTagsM==3))","1 lepton, #geq4jets, 3 b-tags"),
        #Plot(ROOT.TH1F(plotprefix+"43_ttccnode","DNN ttcc node",20,0,1),"aachen_Out_ttbarCC","((N_Jets>=4&&N_BTagsM==3))","1 lepton, #geq4jets, 3 b-tags"),
    #]

    #plots+=plotsAdditional
    #plots+=plotsAdditional+plots64+plots63+plots62+plots54+plots53+plots44+plots43+plots42+plots52
    #plots+=plotsAdditional+plots64+plotsDNNcontrol
    discriminatorPlots=plots
    
    systsamples=[]
    for sample in samples:
        for sysname,sysfilename in zip(otherSystNames,otherSystFileNames):
            thisnewsel=sample.selection
            systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),thisnewsel,sample.nick+sysname,samDict=sampleDict))

    ## WARNING: Adjust Slice for samples if changing ttbar contributions

    # add Parton shower variation samples
    #for sample in samples[analysis.getTtbarSamplesLower() : analysis.getTtbarSamplesUpper()]: # only for ttbar samples
    for sample in samples:
        if sample.nick not in ['ttbarOther', 'ttbarPlusCCbar','ttbarPlusBBbar','ttbarPlusB','ttbarPlus2B']:
          continue
        for sysname,sysfilename in zip(PSSystNames,PSSystFileNames):
            thisoldsel=sample.selection
            thisnewsel=sample.selection.replace(ttbarMCWeight,"*1.0").replace(mcWeight+evenSel,mcWeightAll)
            print "adding sample for ", sysname
            print "selection ", thisnewsel
            print "instead of ", thisoldsel
            systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace(ttbarPathS,path_additionalSamples+"/ttbar_"+sysfilename+"/*nominal*.root"),thisnewsel,sample.nick+sysname,samDict=sampleDict))
    
        # add QCD sytematic for QCD sample
    for sample in samples:
        if sample.name!='QCD':
          continue
        for sysname,sysreplacestring in zip(QCDSystNames,QCDSystReplacementStrings):
          thisnewsel=sample.selection.replace("internalQCDweight",sysreplacestring)
          systsamples.append(Sample(sample.name+sysname,sample.color,sample.path,thisnewsel,sample.nick+sysname,samDict=sampleDict))
    
    
    allsamples=samples+systsamples
    allsystnames=weightSystNames+otherSystNames+PSSystNames+QCDSystNames


    ## define plots
    #discriminatorPlots=[]
    #print len(discrs),len(plotPreselections),len(binlabels),len(nhistobins),len(minxvals),len(maxxvals),
    #print len(zip(discrs,plotPreselections,binlabels,nhistobins,minxvals,maxxvals))
    #for discr,b,bl,nb,minx,maxx in zip(discrs,plotPreselections,binlabels,nhistobins,minxvals,maxxvals):
        #discriminatorPlots.append(Plot(ROOT.TH1F(discrname+"_"+bl,"final discriminator ("+bl+")",nb,minx,maxx),discr,b,bl))


    ## Check if additional (input) variables should be plotted and if necessary add them here to the discriminatorPlots
    #if analysis.additionalPlotVariables:
      ## Construct list with additional plot variables, will need name of discrs and plotPreselections for this
      #clearTextAdditionalPlotList = analysis.getAdditionalPlotVariables(discrs, plotPreselections, binlabels)
      #evalAdditionalPlotList = [eval(x) for x in clearTextAdditionalPlotList]
      #discriminatorPlots.extend(evalAdditionalPlotList)
      #print "Additional variables added to discriminatorPlots: \n", clearTextAdditionalPlotList


    # plot everything, except during drawParallel step
    # Create file for data cards
    if analysis.doDrawParallel==False or analysis.plotNumber == None :
        if not os.path.exists(analysis.rootFilePath):
            print "Doing plotParallel step since root file was not found."
            THEoutputpath=plotParallel(name,5000000,discriminatorPlots,samples+samples_data+systsamples,[''],['1.'],weightSystNames,systWeights,additionalvariables,[],"/nfs/dust/cms/user/kelmorab/treeJsons/treejson_Spring17_FAST.json",otherSystNames+PSSystNames+QCDSystNames,addCodeInterfacePaths=[],cirun=False,StopAfterCompileStep=False,haddParallel=True)
            # Allow start of an improved rebinning algorithm
            if type(THEoutputpath)==str:
              outputpath=THEoutputpath
            else:
              outputpath=THEoutputpath[0]
            if analysis.getActivatedOptimizedRebinning():
              if analysis.getSignalProcess() == 'ttbb':
                # samples[0:2]: tt+bb, tt+b, tt+2b as signal for S over b normalization
                optimizeBinning(outputpath,signalsamples=[samples[0:3]], backgroundsamples=samples[3:],additionalSamples=samples_data, plots=discriminatorPlots, systnames=allsystnames, minBkgPerBin=2.0, optMode=analysis.getOptimzedRebinning(),considerStatUnc=False, maxBins=20, minBins=2,verbosity=2)
              elif analysis.getSignalProcess() == 'ttH':
                # samples: ttH as signal. ttH_bb, ttH_XX as additional samples together with data. Rest: background samples
                optimizeBinning(outputpath,signalsamples=[samples[0]], backgroundsamples=samples[9:],additionalSamples=samples[1:9]+samples_data, plots=discriminatorPlots, systnames=allsystnames, minBkgPerBin=2.0, optMode=analysis.getOptimzedRebinning(),considerStatUnc=False, maxBins=20, minBins=2,verbosity=2)
              else:
                print 'Warning: Could not find signal process.'
            
            # hadd histo files before renaming. The histograms are actually already renamed. But the checkbins thingy will not have been done yet.
            print "hadding from wildcard"
            haddFilesFromWildCard(outputpath,outputpath[:-11]+"/HaddOutputs/*.root")
            # Deactivate check bins functionality in renameHistos if additional plot variables are added via analysis class
            renamedPath=outputpath[:-5]+'_limitInput.root'
            if os.path.exists(renamedPath):
              #if askYesNo('renamedFileExists. Repeat renaming?'):
              #  renameHistos(outputpath,renamedPath,allsystnames,analysis.getCheckBins(),False)
              print "renamed file already exists"
            else:
              if type(THEoutputpath)==str:
                renameHistos(outputpath,renamedPath,allsystnames,True,False)
              else:
                renameHistos(THEoutputpath[1:],renamedPath,allsystnames,True,False)
            #renameHistos(outputpath,outputpath[:-5]+'_limitInput.root',allsystnames,analysis.getCheckBins(),False)
            #addRealData(outputpath[:-5]+'_limitInput.root',[s.nick for s in samplesDataControlPlots],binlabels,discrname)
            #addPseudoData(outputpath[:-5]+'_limitInput.root',[s.nick for s in samples[9:]],binlabels,allsystnames,discrname)
            outputpath=outputpath[:-5]+'_limitInput.root'
        else:
            print "Not doing plotParallel step since root file was found."
            outputpath=analysis.rootFilePath
        print "outputpath: ", outputpath
    else:
        # Warning This time output path refers only to output.root
        # ToDo: Fix usage of output path and output limit path
        if not os.path.exists(analysis.rootFilePath[:-16]+'.root'):
            workdir=os.getcwd()+'/workdir/'+name
            outputpath=workdir+'/output.root'
        else:
            outputpath=analysis.rootFilePath[:-16]+'.root'

    ## make datacards
    #if (analysis.doDrawParallel==False or analysis.plotNumber == None) and analysis.makeDataCards == True :
        ##TODO
        ## 1. Implement small Epsilon case
        ## 2. Implement consisted Bin-by-Bin uncertainties
        #print "Making Data cards."
        #makeDatacards(outputpath,name+'/'+name+'_datacard',binlabels,doHdecay=True,discrname=discrname,datacardmaker=analysis.getDataCardMaker())


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
        lolT=transposeLOL(listOfHistoLists)
        listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,discriminatorPlots,1)

    # plot simple MC plots
    if (analysis.doDrawParallel==False or analysis.plotNumber != None) and analysis.makeSimplePlots==True :
        print "Making simple MC plots."
        writeLOLAndOneOnTop(transposeLOL(lolT[9:]),samples[9:],lolT[0],samples[0],-1,name+'/'+name+'_controlplots')
        writeListOfHistoListsAN(transposeLOL([lolT[0]]+lolT[9:]),[samples[0]]+samples[9:],"",name+'/'+name+'_shapes',True,False,False,'histo',False,True,False)

    # Make MC Control plots
    if (analysis.doDrawParallel==False or analysis.plotNumber != None) and analysis.makeMCControlPlots==True :
        print "Making MC Control plots"
        print "skipping"
        lll=createLLL_fromSuperHistoFileSyst(outputpath,samples[1:],discriminatorPlots,errorSystNamesNoQCD)
        #lllnoQCD=createLLL_fromSuperHistoFileSyst(outputpath,samples[1:],discriminatorPlots,errorSystNamesNoPSNoQCD)
        labels=[plot.label for plot in discriminatorPlots]
        plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],-2,name,[[lll,3354,ROOT.kBlack,True]],True,labels,True,analysis.plotBlinded)

    # Make yield table
    if (analysis.doDrawParallel==False or analysis.plotNumber != None) and analysis.makeEventYields==True :
        print "Making yield table."
        print "Will do only some plots"
        for hld,hl in zip(listOfHistoListsData,listOfHistoLists):
          #if not "JT" in hld[0].GetName():
            #continue
          #else:
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
