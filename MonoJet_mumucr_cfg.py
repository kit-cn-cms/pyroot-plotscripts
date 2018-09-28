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
                 "_Weight_PUUp","_Weight_PUDown",
                 "_Weight_MuonSFIDUp","_Weight_MuonSFIDDown","_Weight_MuonSFIsoUp","_Weight_MuonSFIsoDown","_Weight_MuonSFHIPUp","_Weight_MuonSFHIPDown","_Weight_MuonSFTriggerUp","_Weight_MuonSFTriggerDown",
                 "_Weight_scale_variation_muRUp","_Weight_scale_variation_muRDown","_Weight_scale_variation_muFUp","_Weight_scale_variation_muFDown",
                 "_Weight_PDFUp","_Weight_PDFDown"
                 ]


common_weight= "1.0*Weight_GEN_nom*Weight_CSV*Weight_pu69p2*internalBosonWeight_nominal*Weight_MuonSFID*Weight_MuonSFIso*Weight_MuonSFHIP*((Weight_MuonSFTrigger>0)*Weight_MuonSFTrigger+(Weight_MuonSFTrigger<=0)*1.)"


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
                "dummyWeight_MuonSFIDup:="+common_weight+"*Weight_MuonSFID_Up/Weight_MuonSFID*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_MuonSFIDdown:="+common_weight+"*Weight_MuonSFID_Down/Weight_MuonSFID*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_MuonSFIsoup:="+common_weight+"*Weight_MuonSFIso_Up/Weight_MuonSFIso*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_MuonSFIsodown:="+common_weight+"*Weight_MuonSFIso_Down/Weight_MuonSFIso*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_MuonSFHIPup:="+common_weight+"*Weight_MuonSFHIP_Up/Weight_MuonSFHIP*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_MuonSFHIPdown:="+common_weight+"*Weight_MuonSFHIP_Down/Weight_MuonSFHIP*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_MuonSFTriggerup:="+common_weight+"*((Weight_MuonSFTrigger_Up>0)*Weight_MuonSFTrigger_Up+(Weight_MuonSFTrigger_Up<=0)*1.)/((Weight_MuonSFTrigger>0)*Weight_MuonSFTrigger+(Weight_MuonSFTrigger<=0)*1.)*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_MuonSFTriggerdown:="+common_weight+"*((Weight_MuonSFTrigger_Down>0)*Weight_MuonSFTrigger_Down+(Weight_MuonSFTrigger_Down<=0)*1.)/((Weight_MuonSFTrigger>0)*Weight_MuonSFTrigger+(Weight_MuonSFTrigger<=0)*1.)*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_scale_variation_muRup:="+common_weight+"*internalBosonWeight_muRUp/internalBosonWeight_nominal*fabs(Weight_scale_variation_muR_2p0_muF_1p0)*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_scale_variation_muRdown:="+common_weight+"*internalBosonWeight_muRDown/internalBosonWeight_nominal*fabs(Weight_scale_variation_muR_0p5_muF_1p0)*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_scale_variation_muFup:="+common_weight+"*internalBosonWeight_muFUp/internalBosonWeight_nominal*fabs(Weight_scale_variation_muR_1p0_muF_2p0)*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_scale_variation_muFdown:="+common_weight+"*internalBosonWeight_muFDown/internalBosonWeight_nominal*fabs(Weight_scale_variation_muR_1p0_muF_0p5)*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_PDFup:="+common_weight+"*(Weight_LHA_292200_up>0.)*Weight_LHA_292200_up*(DoWeights==1)+(DoWeights==0)*1.0",
                "dummyWeight_PDFdown:="+common_weight+"*(Weight_LHA_292200_down>0.)*Weight_LHA_292200_down*(DoWeights==1)+(DoWeights==0)*1.0"
                ]
otherSystNames=[
                    "_CMS_scale_jUp","_CMS_scale_jDown",
                    "_CMS_res_jUp","_CMS_res_jDown"
    ]
otherSystFileNames=[
                        "JESup","JESdown",
                        "JERup","JERdown"
    ]

BosonSystNames=[
       "_BosonWeight_QCD1Up","_BosonWeight_QCD1Down",
       "_BosonWeight_QCD2Up","_BosonWeight_QCD2Down",
       "_BosonWeight_QCD3Up","_BosonWeight_QCD3Down",
       "_BosonWeight_EW1Up","_BosonWeight_EW1Down",
       #"_BosonWeight_EW2Up","_BosonWeight_EW2Down",
       #"_BosonWeight_EW3Up","_BosonWeight_EW3Down",
       #"_BosonWeight_MixedUp","_BosonWeight_MixedDown",
       #"_BosonWeight_AlphaUp","_BosonWeight_AlphaDown",
]
BosonWeights=[
       "dummyWeight_Boson_QCD1Up:="+common_weight+"*internalBosonWeight_QCD1Up/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       "dummyWeight_Boson_QCD1Down:="+common_weight+"*internalBosonWeight_QCD1Down/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       "dummyWeight_Boson_QCD2Up:="+common_weight+"*internalBosonWeight_QCD2Up/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       "dummyWeight_Boson_QCD2Down:="+common_weight+"*internalBosonWeight_QCD2Down/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       "dummyWeight_Boson_QCD3Up:="+common_weight+"*internalBosonWeight_QCD3Up/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       "dummyWeight_Boson_QCD3Down:="+common_weight+"*internalBosonWeight_QCD3Down/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",

       "dummyWeight_Boson_EW1Up:="+common_weight+"*internalBosonWeight_EW1Up/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       "dummyWeight_Boson_EW1Down:="+common_weight+"*internalBosonWeight_EW1Down/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       #"dummyWeight_Boson_EW2Up:="+common_weight+"*internalBosonWeight_EW2Up/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       #"dummyWeight_Boson_EW2Down:="+common_weight+"*internalBosonWeight_EW2Down/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       #"dummyWeight_Boson_EW3Up:="+common_weight+"*internalBosonWeight_EW3Up/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       #"dummyWeight_Boson_EW3Down:="+common_weight+"*internalBosonWeight_EW3Down/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",

       #"dummyWeight_Boson_MixedUp:="+common_weight+"*internalBosonWeight_MixedUp/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       #"dummyWeight_Boson_MixedDown:="+common_weight+"*internalBosonWeight_MixedDown/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       
       #"dummyWeight_Boson_AlphaUp:="+common_weight+"*internalBosonWeight_AlphaUp/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       #"dummyWeight_Boson_AlphaDown:="+common_weight+"*internalBosonWeight_AlphaDown/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
]

ZvvBosonSystNames = [
    
     "_ZvvBosonWeight_EW2Up","_ZvvBosonWeight_EW2Down",
     "_ZvvBosonWeight_EW3Up","_ZvvBosonWeight_EW3Down",
     "_ZvvBosonWeight_MixedUp","_ZvvBosonWeight_MixedDown",
     "_ZvvBosonWeight_AlphaUp","_ZvvBosonWeight_AlphaDown",
    ]

ZllBosonSystNames = [
    
     "_ZllBosonWeight_EW2Up","_ZllBosonWeight_EW2Down",
     "_ZllBosonWeight_EW3Up","_ZllBosonWeight_EW3Down",
     "_ZllBosonWeight_MixedUp","_ZllBosonWeight_MixedDown",
     "_ZllBosonWeight_AlphaUp","_ZllBosonWeight_AlphaDown",
    ]

WBosonSystNames = [
    
     "_WBosonWeight_EW2Up","_WBosonWeight_EW2Down",
     "_WBosonWeight_EW3Up","_WBosonWeight_EW3Down",
     "_WBosonWeight_MixedUp","_WBosonWeight_MixedDown",
     "_WBosonWeight_AlphaUp","_WBosonWeight_AlphaDown",
    ]

ZvvBosonWeights=[
    
       "dummyWeight_ZvvBoson_EW2Up:="+common_weight+"*internalBosonWeight_EW2Up/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       "dummyWeight_ZvvBoson_EW2Down:="+common_weight+"*internalBosonWeight_EW2Down/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       "dummyWeight_ZvvBoson_EW3Up:="+common_weight+"*internalBosonWeight_EW3Up/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       "dummyWeight_ZvvBoson_EW3Down:="+common_weight+"*internalBosonWeight_EW3Down/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       "dummyWeight_ZvvBoson_MixedUp:="+common_weight+"*internalBosonWeight_MixedUp/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       "dummyWeight_ZvvBoson_MixedDown:="+common_weight+"*internalBosonWeight_MixedDown/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       "dummyWeight_ZvvBoson_AlphaUp:="+common_weight+"*internalBosonWeight_AlphaUp/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       "dummyWeight_ZvvBoson_AlphaDown:="+common_weight+"*internalBosonWeight_AlphaDown/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
    
    ]

ZllBosonWeights=[
    
       "dummyWeight_ZllBoson_EW2Up:="+common_weight+"*internalBosonWeight_EW2Up/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       "dummyWeight_ZllBoson_EW2Down:="+common_weight+"*internalBosonWeight_EW2Down/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       "dummyWeight_ZllBoson_EW3Up:="+common_weight+"*internalBosonWeight_EW3Up/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       "dummyWeight_ZllBoson_EW3Down:="+common_weight+"*internalBosonWeight_EW3Down/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       "dummyWeight_ZllBoson_MixedUp:="+common_weight+"*internalBosonWeight_MixedUp/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       "dummyWeight_ZllBoson_MixedDown:="+common_weight+"*internalBosonWeight_MixedDown/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       "dummyWeight_ZllBoson_AlphaUp:="+common_weight+"*internalBosonWeight_AlphaUp/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       "dummyWeight_ZllBoson_AlphaDown:="+common_weight+"*internalBosonWeight_AlphaDown/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
    
    ]

WBosonWeights=[
    
       "dummyWeight_WBoson_EW2Up:="+common_weight+"*internalBosonWeight_EW2Up/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       "dummyWeight_WBoson_EW2Down:="+common_weight+"*internalBosonWeight_EW2Down/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       "dummyWeight_WBoson_EW3Up:="+common_weight+"*internalBosonWeight_EW3Up/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       "dummyWeight_WBoson_EW3Down:="+common_weight+"*internalBosonWeight_EW3Down/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       "dummyWeight_WBoson_MixedUp:="+common_weight+"*internalBosonWeight_MixedUp/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       "dummyWeight_WBoson_MixedDown:="+common_weight+"*internalBosonWeight_MixedDown/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",       
       "dummyWeight_WBoson_AlphaUp:="+common_weight+"*internalBosonWeight_AlphaUp/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
       "dummyWeight_WBoson_AlphaDown:="+common_weight+"*internalBosonWeight_AlphaDown/internalBosonWeight_nominal*(DoWeights==1)+(DoWeights==0)*1.0",
    
    ]


MCWeight='35.91823'

path_ntuples = "/nfs/dust/cms/user/mwassmer/DarkMatter/ntuples_controlregion"
# path_ntuples = "/nfs/dust/cms/user/swieland/Darkmatter/ntuples"

sampleDict=SampleDictionary()
sampleDict.doPrintout()

#sel_MET="*((Triggered_HLT_PFMET170_X==1)||(Triggered_HLT_PFMETNoMu100_PFMHTNoMu100_IDTight_X==1)||(Triggered_HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_X==1)||(Triggered_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_X==1)||(Triggered_HLT_PFMETNoMu90_PFMHTNoMu90_IDTight_X==1))*(N_LooseMuons==2)*(N_LooseElectrons==0)*(N_LooseTaus==0)*(N_TightMuons>0)*(Zmumu_Mass>60)*(Zmumu_Mass<120)*(Muon_Charge[0]!=Muon_Charge[1])"
#sel_MET="*(Triggered_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_X==1)*(N_LooseMuons==2)*(N_LooseElectrons==0)*(N_LooseTaus==0)*(N_TightMuons>0)*(Zmumu_Mass>60)*(Zmumu_Mass<120)*(Muon_Charge[0]!=Muon_Charge[1])"
sel_MET="*((Triggered_HLT_IsoMu24_vX==1)||(Triggered_HLT_IsoTkMu24_vX==1))*(N_LooseMuons==2)*(N_LooseElectrons==0)*(N_LooseTaus==0)*(N_TightMuons>0)*(Zmumu_Mass>60)*(Zmumu_Mass<120)*(Muon_Charge[0]!=Muon_Charge[1])*((DoWeights==1)*(Weight_MuonSFID>0.)+(DoWeights==0)*1.0)"
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
                        Sample('Z(ll)+jets',ROOT.kViolet-7,path_ntuples+'/DYJetsToLL*amc*/*nominal*.root',"1.*0.971"+"*"+MCWeight+sel_MET,'z_ll_jets',weightSystNames+BosonSystNames+ZllBosonSystNames+otherSystNames,samDict=sampleDict),
                        Sample('Diboson',ROOT.kViolet,path_ntuples+'/??_TuneCUETP8M1_13TeV-pythia8/*nominal*.root',"1."+"*"+MCWeight+sel_MET,'diboson',weightSystNames[:-6]+otherSystNames,samDict=sampleDict),                        
                        #Sample('t#bar{t}',ROOT.kViolet-2,path_ntuples+'/TT_Tune*/*nominal*.root',"1."+"*"+MCWeight+sel_MET,'ttbar',weightSystNames[:-2]+otherSystNames,samDict=sampleDict),
                        Sample('Top',ROOT.kViolet-1,path_ntuples+'/?T*/*nominal*.root',"1."+"*"+MCWeight+sel_MET,'top',weightSystNames[:-2]+otherSystNames,samDict=sampleDict),
                        Sample('W(l#nu)+jets',ROOT.kGreen,path_ntuples+'/WJetsToLNu*To*/*nominal*.root',"1.*"+MCWeight+sel_MET,'w_lnu_jets',weightSystNames+BosonSystNames+WBosonSystNames+otherSystNames,samDict=sampleDict),
                        Sample('QCD',ROOT.kViolet+3,path_ntuples+'/QCD*/*nominal*.root',"1."+"*"+MCWeight+sel_MET,'qcd',weightSystNames[:-2]+otherSystNames,samDict=sampleDict),
                        Sample('#gamma +jets',ROOT.kViolet+7,path_ntuples+'/GJets*/*nominal*.root',"1."+"*"+MCWeight+sel_MET,'gamma_jets',weightSystNames[:-2]+otherSystNames,samDict=sampleDict)
                        #Sample('Z(#nu#nu)+jets',ROOT.kBlue,path_ntuples+'/DYJetsToNuNu*To*amc*/*nominal*.root',"1.*3*0.971"+"*"+MCWeight+sel_MET,'z_nunu_jets',weightSystNames+BosonSystNames+ZvvBosonSystNames+otherSystNames,samDict=sampleDict),
                        ]
"""
samples_signal = [
                        Sample('AV|M1000|m300',ROOT.kRed,path_ntuples+'/DMV_NNPDF30_Axial_Mphi-1000_Mchi-300_gSM-0p25_gDM-1p0_v2_13TeV-powheg/*nominal*.root',"1."+"*"+MCWeight+sel_MET,'SIG_AV_M1000_m300',weightSystNames,samDict=sampleDict),
                 ]
"""

samples_signal = [
                        Sample('AV|M1000|m300',ROOT.kRed,path_ntuples+'/Axial_MonoJ_NLO_Mphi-1000_Mchi-300_gSM-0p25_gDM-1p0_13TeV-madgraph/*nominal*.root',"1."+"*"+MCWeight+sel_MET,'SIG_AV_M1000_m300',weightSystNames[:-2],samDict=sampleDict),

                 ]

"""
signal_samples_paths = glob.glob(path_ntuples+'/'+'*MonoJ*NLO*')
signal_samples_names = []
for i in range(len(signal_samples_paths)):
    signal_samples_paths[i]=signal_samples_paths[i]+'/'+'*nominal*.root'
    #signal_samples_names.append(signal_samples_paths[i].replace(path_ntuples+"/","").replace("/*nominal*.root","").replace("DMV_NNPDF30_","").replace("DMS_NNPDF30_","").replace("_v2_13TeV-powheg","").replace("-","_"))
    signal_samples_names.append(signal_samples_paths[i].replace(path_ntuples+"/","").replace("/*nominal*.root","").replace("_13TeV-madgraph","").replace("-","_"))

samples_signal = []
for i in range(len(signal_samples_names)):
    samples_signal.append(Sample(signal_samples_names[i],ROOT.kRed,signal_samples_paths[i],"1."+"*"+MCWeight+sel_MET,signal_samples_names[i],[""],samDict=sampleDict))
    
print samples_signal
print signal_samples_names
"""
