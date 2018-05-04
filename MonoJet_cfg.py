import sys
import os
sys.path.append('pyroot-plotscripts-base')
sys.path.append('pyroot-plotscripts-base/limittools')

from scriptgenerator import *
from plotutils import *

weightSystNames=["",
                 "_CMS_btag_lfUp","_CMS_btag_lfDown","_CMS_btag_hfUp","_CMS_btag_hfDown",
                 "_CMS_btag_hfstats1Up","_CMS_btag_hfstats1Down","_CMS_btag_lfstats1Up","_CMS_btag_lfstats1Down",
                 "_CMS_btag_hfstats2Up","_CMS_btag_hfstats2Down","_CMS_btag_lfstats2Up","_CMS_btag_lfstats2Down",
                 "_CMS_btag_cferr1Up","_CMS_btag_cferr1Down","_CMS_btag_cferr2Up","_CMS_btag_cferr2Down",
                 "_Weight_PUUp","_WeightPUDown",
                 "_Weight_scale_variation_muRUp","_Weight_scale_variation_muRDown","_Weight_scale_variation_muFUp","_Weight_scale_variation_muFDown",
                 ]

common_weight= "1.0*Weight_GEN_nom*Weight_CSV*Weight_pu69p2"

systWeights=[   "NomWeight:="+common_weight+"*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_CSVLFup:="+common_weight+"*Weight_CSVLFup*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_CSVLFdown:="+common_weight+"*Weight_CSVLFdown*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_CSVHFup:="+common_weight+"*Weight_CSVHFup*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_CSVHFdown:="+common_weight+"*Weight_CSVHFdown*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_CSVHFStats1up:="+common_weight+"*Weight_CSVHFStats1up*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_CSVHFStats1down:="+common_weight+"*Weight_CSVHFStats1down*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_CSVLFStats1up:="+common_weight+"*Weight_CSVLFStats1up*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_CSVLFStats1down:="+common_weight+"*Weight_CSVLFStats1down*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_CSVHFStats2up:="+common_weight+"*Weight_CSVHFStats2up*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_CSVHFStats2down:="+common_weight+"*Weight_CSVHFStats2down*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_CSVLFStats2up:="+common_weight+"*Weight_CSVLFStats2up*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_CSVLFStats2down:="+common_weight+"*Weight_CSVLFStats2down*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_CSVCErr1up:="+common_weight+"*Weight_CSVCErr1up*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_CSVCErr1down:="+common_weight+"*Weight_CSVCErr1down*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_CSVCErr2up:="+common_weight+"*Weight_CSVCErr2up*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_CSVCErr2down:="+common_weight+"*Weight_CSVCErr2down*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_PUup:="+common_weight+"*Weight_pu69p2Up/Weight_pu69p2*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_PUdown:="+common_weight+"*Weight_pu69p2Down/Weight_pu69p2*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_scale_variation_muRup:="+common_weight+"*fabs(Weight_scale_variation_muR_2p0_muF_1p0)*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_scale_variation_muRdown:="+common_weight+"*fabs(Weight_scale_variation_muR_0p5_muF_1p0)*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_scale_variation_muFup:="+common_weight+"*fabs(Weight_scale_variation_muR_1p0_muF_2p0)*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_scale_variation_muFdown:="+common_weight+"*fabs(Weight_scale_variation_muR_1p0_muF_0p5)*(DoWeights==1)+(DoWeights==0)*1.0",
                ]
otherSystNames=[
                    "_CMS_scale_jUp","_CMS_scale_jDown",
                    "_CMS_res_jUp","_CMS_res_jDown"
    ]
otherSystFileNames=[
                        "JESup","JESdown",
                        "JERup","JERdown"
    ]

MCWeight='35.91823'

path_ntuples = "/nfs/dust/cms/user/mwassmer/DarkMatter/ntuples"

sampleDict=SampleDictionary()
sampleDict.doPrintout()

sel_MET="*(Triggered_HLT_PFMET170_X==1||Triggered_HLT_PFMETNoMu100_PFMHTNoMu100_IDTight_X==1||Triggered_HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_X==1||Triggered_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_X==1||Triggered_HLT_PFMETNoMu90_PFMHTNoMu90_IDTight_X==1)"

"""
Triggered_HLT_EcalHT800
Triggered_HLT_Ele105_CaloIdVT_GsfTrkIdT
Triggered_HLT_Ele27_WPTight
Triggered_HLT_PFMET170_X
Triggered_HLT_PFMETNoMu100_PFMHTNoMu100_IDTight
Triggered_HLT_PFMETNoMu110_PFMHTNoMu110_IDTight
Triggered_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight
Triggered_HLT_PFMETNoMu90_PFMHTNoMu90_IDTight
Triggered_HLT_Photon165_HE10
Triggered_HLT_Photon175
"""
"""
Sample('Z(#nu#nu)+jets p_{T,Z}=50-100',ROOT.kBlue,path_ntuples+'/DYJetsToNuNu_PtZ-50To100*/*nominal*.root',"1.13*3"+"*"+MCWeight+sel_MET,'Z_nunu_jets_e',[""],samDict=sampleDict),
Sample('Z(#nu#nu)+jets p_{T,Z}=100-250',ROOT.kBlue+2,path_ntuples+'/DYJetsToNuNu_PtZ-100To250*/*nominal*.root',"1.11*3"+"*"+MCWeight+sel_MET,'Z_nunu_jets_a',[""],samDict=sampleDict),
Sample('Z(#nu#nu)+jets p_{T,Z}=250-400',ROOT.kBlue+4,path_ntuples+'/DYJetsToNuNu_PtZ-250To400*/*nominal*.root',"1.16*3"+"*"+MCWeight+sel_MET,'Z_nunu_jets_b',[""],samDict=sampleDict),
Sample('Z(#nu#nu)+jets p_{T,Z}=400-650',ROOT.kBlue+6,path_ntuples+'/DYJetsToNuNu_PtZ-400To650*/*nominal*.root',"1.25*3"+"*"+MCWeight+sel_MET,'Z_nunu_jets_c',[""],samDict=sampleDict),
Sample('Z(#nu#nu)+jets p_{T,Z}=650-Inf',ROOT.kBlue+8,path_ntuples+'/DYJetsToNuNu_PtZ-650ToInf*/*nominal*.root',"1.41*3"+"*"+MCWeight+sel_MET,'Z_nunu_jets_d',[""],samDict=sampleDict),
                                                                                               	
Sample('W(l#nu)+jets P_{T,W}=100-250',ROOT.kGreen-7,path_ntuples+'/WJetsToLNu_Pt-100To250*/*nominal*.root',"1.14*"+MCWeight+sel_MET,'W_lnu_jets_a',[""],samDict=sampleDict),
Sample('W(l#nu)+jets p_{T,W}=250-400',ROOT.kGreen-6,path_ntuples+'/WJetsToLNu_Pt-250To400*/*nominal*.root',"1.17*"+MCWeight+sel_MET,'W_lnu_jets_b',[""],samDict=sampleDict),
Sample('W(l#nu)+jets p_{T,W}=400-600',ROOT.kGreen-5,path_ntuples+'/WJetsToLNu_Pt-400To600*/*nominal*.root',"1.24*"+MCWeight+sel_MET,'W_lnu_jets_c',[""],samDict=sampleDict),
Sample('W(l#nu)+jets p_{T,W}=600-Inf',ROOT.kGreen-4,path_ntuples+'/WJetsToLNu_Pt-600ToInf*/*nominal*.root',"1.34*"+MCWeight+sel_MET,'W_lnu_jets_d',[""],samDict=sampleDict),
                                                                                               	                                                                                                
"""

samples_data = [
            Sample('data',ROOT.kBlack,path_ntuples+'/MET_Run2016*/*nominal*.root',"1."+sel_MET,'data_obs',[""],samDict=sampleDict),
            #Sample('test_d',ROOT.kGreen-7,path_ntuples+'/test/*nominal*.root',"1.",'test_d',[""],samDict=sampleDict)
        ]
#complete sample xs weight
#z_nunu: 0.00001321
#w_lnu: 0.0000086564
samples_background = [
                        Sample('Z(#nu#nu)+jets',ROOT.kBlue,path_ntuples+'/DYJetsToNuNu_PtZ-*/*nominal*.root',"1.*3*0.971"+"*"+MCWeight+sel_MET,'z_nunu_jets',weightSystNames+otherSystNames,samDict=sampleDict),
                        #Sample('Z(#nu#nu)+jets p_{T,Z}=50-100',ROOT.kBlue+4,path_ntuples+'/DYJetsToNuNu_PtZ-50To100*/*nominal*.root',"3*0.971"+"*"+MCWeight+sel_MET,'z_nunu_jets_a',weightSystNames+otherSystNames,samDict=sampleDict),
                        #Sample('Z(#nu#nu)+jets p_{T,Z}=100-250',ROOT.kBlue+2,path_ntuples+'/DYJetsToNuNu_PtZ-100To250*/*nominal*.root',"3*0.971"+"*"+MCWeight+sel_MET,'z_nunu_jets_b',weightSystNames+otherSystNames,samDict=sampleDict),
                        #Sample('Z(#nu#nu)+jets p_{T,Z}=250-400',ROOT.kBlue,path_ntuples+'/DYJetsToNuNu_PtZ-250To400*/*nominal*.root',"3*0.971"+"*"+MCWeight+sel_MET,'z_nunu_jets_c',weightSystNames+otherSystNames,samDict=sampleDict),
                        #Sample('Z(#nu#nu)+jets p_{T,Z}=400-650',ROOT.kBlue-2,path_ntuples+'/DYJetsToNuNu_PtZ-400To650*/*nominal*.root',"3*0.971"+"*"+MCWeight+sel_MET,'z_nunu_jets_d',weightSystNames+otherSystNames,samDict=sampleDict),
                        #Sample('Z(#nu#nu)+jets p_{T,Z}=650-Inf',ROOT.kBlue-5,path_ntuples+'/DYJetsToNuNu_PtZ-650ToInf*/*nominal*.root',"3*0.971"+"*"+MCWeight+sel_MET,'z_nunu_jets_e',weightSystNames+otherSystNames,samDict=sampleDict),

                        Sample('W(l#nu)+jets',ROOT.kGreen,path_ntuples+'/WJetsToLNu_Pt-*/*nominal*.root',"1.*"+MCWeight+sel_MET,'w_lnu_jets',weightSystNames+otherSystNames,samDict=sampleDict),
                        #Sample('W(l#nu)+jets P_{T,W}=100-250',ROOT.kGreen,path_ntuples+'/WJetsToLNu_Pt-100To250*/*nominal*.root',"1.*"+MCWeight+sel_MET,'w_lnu_jets_a',weightSystNames+otherSystNames,samDict=sampleDict),
                        #Sample('W(l#nu)+jets p_{T,W}=250-400',ROOT.kGreen+2,path_ntuples+'/WJetsToLNu_Pt-250To400*/*nominal*.root',"1.*"+MCWeight+sel_MET,'w_lnu_jets_b',weightSystNames+otherSystNames,samDict=sampleDict),
                        #Sample('W(l#nu)+jets p_{T,W}=400-600',ROOT.kGreen+4,path_ntuples+'/WJetsToLNu_Pt-400To600*/*nominal*.root',"1.*"+MCWeight+sel_MET,'w_lnu_jets_c',weightSystNames+otherSystNames,samDict=sampleDict),
                        #Sample('W(l#nu)+jets p_{T,W}=600-Inf',ROOT.kGreen-6,path_ntuples+'/WJetsToLNu_Pt-600ToInf*/*nominal*.root',"1.*"+MCWeight+sel_MET,'w_lnu_jets_d',weightSystNames+otherSystNames,samDict=sampleDict),
                        
                        Sample('Diboson',ROOT.kViolet,path_ntuples+'/??_TuneCUETP8M1_13TeV-pythia8/*nominal*.root',"1."+"*"+MCWeight+sel_MET,'diboson',weightSystNames[:-4]+otherSystNames,samDict=sampleDict),
                        Sample('Single Top',ROOT.kViolet-1,path_ntuples+'/ST*/*nominal*.root',"1."+"*"+MCWeight+sel_MET,'singletop',weightSystNames[:-4]+otherSystNames,samDict=sampleDict),
                        Sample('t#bar{t}',ROOT.kViolet-2,path_ntuples+'/TT_Tune*/*nominal*.root',"1."+"*"+MCWeight+sel_MET,'ttbar',weightSystNames[:-4]+otherSystNames,samDict=sampleDict),
                        Sample('Z(ll)+jets',ROOT.kViolet-7,path_ntuples+'/DYJetsToLL*/*nominal*.root',"1."+"*"+MCWeight+sel_MET,'z_ll_jets',weightSystNames[:-4]+otherSystNames,samDict=sampleDict),
                        Sample('QCD',ROOT.kViolet+3,path_ntuples+'/QCD*/*nominal*.root',"1."+"*"+MCWeight+sel_MET,'qcd',weightSystNames[:-4]+otherSystNames,samDict=sampleDict),
                        Sample('#gamma +jets',ROOT.kViolet+7,path_ntuples+'/GJets*/*nominal*.root',"1."+"*"+MCWeight+sel_MET,'gamma_jets',weightSystNames[:-4]+otherSystNames,samDict=sampleDict)
                        ]

samples_signal = [
                        Sample('VM1000m300',ROOT.kRed,path_ntuples+'/DMV_NNPDF30_Axial_Mphi-1000_Mchi-300_gSM-0p25_gDM-1p0_v2_13TeV-powheg/*nominal*.root',"1."+"*"+MCWeight+sel_MET,'DMVMed1000DM300',weightSystNames[:-4],samDict=sampleDict),
                        #Sample('test_s',ROOT.kGreen-7,path_ntuples+'/test/*nominal*.root',"1."+"*"+MCWeight,'test_s',[""],samDict=sampleDict)
			#Sample('MET',ROOT.kBlack,path_ntuples+'/MET_Run2016*/*nominal*.root',"1."+sel_MET,'MET',samDict=sampleDict)    
    ]
