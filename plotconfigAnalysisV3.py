import sys
import os
from scriptgenerator import *
from plotutils import *

sel_singleel="(N_LooseMuons==0)*(N_Jets>=4 && N_BTagsM>=2)" # need to veto muon events in electron dataset to avoid double countung
sel_singlemu="(N_LooseElectrons==0)*(N_Jets>=4 && N_BTagsM>=2)" # and vice versa...

# hcc is uu dd ss cc with ids 1 2 3 4
hccSel='*((abs(GenHiggs_DecProd1_PDGID)==1 && abs(GenHiggs_DecProd2_PDGID)==1) || (abs(GenHiggs_DecProd1_PDGID)==2 && abs(GenHiggs_DecProd2_PDGID)==2) || (abs(GenHiggs_DecProd1_PDGID)==3 && abs(GenHiggs_DecProd2_PDGID)==3) || (abs(GenHiggs_DecProd1_PDGID)==4 && abs(GenHiggs_DecProd2_PDGID)==4) )'
# htt is mumu tautau with ids 13 15
httSel='*((abs(GenHiggs_DecProd1_PDGID)==13 && abs(GenHiggs_DecProd2_PDGID)==13) || (abs(GenHiggs_DecProd1_PDGID)==15 && abs(GenHiggs_DecProd2_PDGID)==15))'
# hgg is gammagamma with id 22
hggSel='*((abs(GenHiggs_DecProd1_PDGID)==22 && abs(GenHiggs_DecProd2_PDGID)==22))'
# hgluglu with id 21
hglugluSel='*((abs(GenHiggs_DecProd1_PDGID)==21 && abs(GenHiggs_DecProd2_PDGID)==21))'
# hww with id 24
hwwSel='*((abs(GenHiggs_DecProd1_PDGID)==24 && abs(GenHiggs_DecProd2_PDGID)==24))'
# hzz with id 23
hzzSel='*((abs(GenHiggs_DecProd1_PDGID)==23 && abs(GenHiggs_DecProd2_PDGID)==23))'
# hzg with id 23 and id 22
hzgSel='*((abs(GenHiggs_DecProd1_PDGID)==23 && abs(GenHiggs_DecProd2_PDGID)==22) || (abs(GenHiggs_DecProd1_PDGID)==22 && abs(GenHiggs_DecProd2_PDGID)==23))'

# names of the systematics (proper names needed e.g. for combination)
weightsystnames=[
                    "",
                   "_CMS_ttH_CSVLFUp","_CMS_ttH_CSVLFDown","_CMS_ttH_CSVHFUp","_CMS_ttH_CSVHFDown",
                   "_CMS_ttH_CSVHFStats1Up","_CMS_ttH_CSVHFStats1Down","_CMS_ttH_CSVLFStats1Up","_CMS_ttH_CSVLFStats1Down",
                   "_CMS_ttH_CSVHFStats2Up","_CMS_ttH_CSVHFStats2Down","_CMS_ttH_CSVLFStats2Up","_CMS_ttH_CSVLFStats2Down",
                   "_CMS_ttH_CSVCErr1Up","_CMS_ttH_CSVCErr1Down","_CMS_ttH_CSVCErr2Up","_CMS_ttH_CSVCErr2Down",
#                    "_CMS_ttH_TopPtUp","_CMS_ttH_TopPtDown",
                    #"_CMS_ttH_PUUp","_CMS_ttH_PUDown",
                    #"_CMS_ttH_Q2scale_ttbarOtherUp","_CMS_ttH_Q2scale_ttbarOtherDown",
                    #"_CMS_ttH_Q2scale_ttbarPlusBUp","_CMS_ttH_Q2scale_ttbarPlusBDown",
                    #"_CMS_ttH_Q2scale_ttbarPlus2BUp","_CMS_ttH_Q2scale_ttbarPlus2BDown",
                    #"_CMS_ttH_Q2scale_ttbarPlusBBbarUp","_CMS_ttH_Q2scale_ttbarPlusBBbarDown",
                    #"_CMS_ttH_Q2scale_ttbarPlusCCbarUp","_CMS_ttH_Q2scale_ttbarPlusCCbarDown",
#                    "_CMS_ttH_NNPDFUp","_CMS_ttH_NNPDFDown",
#                    "_CMS_ttH_ljets_TrigUp","_CMS_ttH_ljets_TrigDown",  
#                    "_CMS_ttH_ljets_Trig_elUp","_CMS_ttH_ljets_Trig_elDown",
                   #"_CMS_ttH_eff_leptonUp","_CMS_ttH_eff_leptonDown",  
#                    "_CMS_ttH_ljets_Trig_muUp","_CMS_ttH_ljets_Trig_muDown",  
#                    "_CMS_ttH_ljets_Trig_elUp","_CMS_ttH_ljets_Trig_elDown",
                   #"_CMS_ttH_eff_muUp","_CMS_ttH_eff_muDown",  
                   #"_CMS_ttH_eff_elUp","_CMS_ttH_eff_elDown",
                   #"_CMS_res_jUp","_CMS_res_jDown"
                    #"_CMS_scale_jUp","_CMS_scale_jDown",
]

systs_all_samples=[
                    "",
                   "_CMS_ttH_CSVLFUp","_CMS_ttH_CSVLFDown","_CMS_ttH_CSVHFUp","_CMS_ttH_CSVHFDown",
                   "_CMS_ttH_CSVHFStats1Up","_CMS_ttH_CSVHFStats1Down","_CMS_ttH_CSVLFStats1Up","_CMS_ttH_CSVLFStats1Down",
                   "_CMS_ttH_CSVHFStats2Up","_CMS_ttH_CSVHFStats2Down","_CMS_ttH_CSVLFStats2Up","_CMS_ttH_CSVLFStats2Down",
                   "_CMS_ttH_CSVCErr1Up","_CMS_ttH_CSVCErr1Down","_CMS_ttH_CSVCErr2Up","_CMS_ttH_CSVCErr2Down",
                    #"_CMS_ttH_PUUp","_CMS_ttH_PUDown",
#                    "_CMS_ttH_ljets_Trig_muUp","_CMS_ttH_ljets_Trig_muDown",  
#                    "_CMS_ttH_ljets_Trig_elUp","_CMS_ttH_Trig_elDown",
                   #"_CMS_ttH_eff_muUp","_CMS_ttH_eff_muDown",  
                   #"_CMS_ttH_eff_elUp","_CMS_ttH_eff_elDown",
#                    "_CMS_ttH_ljets_TrigUp","_CMS_ttH_ljets_TrigDown",  
#                    "_CMS_ttH_ljets_Trig_elUp","_CMS_ttH_Trig_elDown",
                   #"_CMS_ttH_eff_leptonUp","_CMS_ttH_eff_leptonDown",  
                   "_CMS_res_jUp","_CMS_res_jDown",
                    "_CMS_scale_jUp","_CMS_scale_jDown",
]

systs_ttbar= [
#                    "_CMS_ttH_NNPDFUp","_CMS_ttH_NNPDFDown",
                    #"_CMS_ttH_PSscaleUp","_CMS_ttH_PSscaleDown",
]

#systs_tt_lf=["_CMS_ttH_Q2scale_ttbarOtherUp","_CMS_ttH_Q2scale_ttbarOtherDown"]
#systs_tt_b=["_CMS_ttH_Q2scale_ttbarPlusBUp","_CMS_ttH_Q2scale_ttbarPlusBDown"]
#systs_tt_2b=[ "_CMS_ttH_Q2scale_ttbarPlus2BUp","_CMS_ttH_Q2scale_ttbarPlus2BDown"]
#systs_tt_bb=[ "_CMS_ttH_Q2scale_ttbarPlusBBbarUp","_CMS_ttH_Q2scale_ttbarPlusBBbarDown"]
#systs_tt_cc=[ "_CMS_ttH_Q2scale_ttbarPlusCCbarUp","_CMS_ttH_Q2scale_ttbarPlusCCbarDown"]

systs_tt_lf=[]
systs_tt_b=[]
systs_tt_2b=[]
systs_tt_bb=[]
systs_tt_cc=[]


errorSystnames=[
                    "",
                   "_CMS_ttH_CSVLFUp","_CMS_ttH_CSVLFDown","_CMS_ttH_CSVHFUp","_CMS_ttH_CSVHFDown",
                   "_CMS_ttH_CSVHFStats1Up","_CMS_ttH_CSVHFStats1Down","_CMS_ttH_CSVLFStats1Up","_CMS_ttH_CSVLFStats1Down",
                   "_CMS_ttH_CSVHFStats2Up","_CMS_ttH_CSVHFStats2Down","_CMS_ttH_CSVLFStats2Up","_CMS_ttH_CSVLFStats2Down",
                   "_CMS_ttH_CSVCErr1Up","_CMS_ttH_CSVCErr1Down","_CMS_ttH_CSVCErr2Up","_CMS_ttH_CSVCErr2Down",
#                    "_CMS_ttH_TopPtUp","_CMS_ttH_TopPtDown",
                    #"_CMS_ttH_PUUp","_CMS_ttH_PUDown",
                    #"_CMS_ttH_Q2scale_ttbarOtherUp","_CMS_ttH_Q2scale_ttbarOtherDown",
                    #"_CMS_ttH_Q2scale_ttbarPlusBUp","_CMS_ttH_Q2scale_ttbarPlusBDown",
                    #"_CMS_ttH_Q2scale_ttbarPlus2BUp","_CMS_ttH_Q2scale_ttbarPlus2BDown",
                    #"_CMS_ttH_Q2scale_ttbarPlusBBbarUp","_CMS_ttH_Q2scale_ttbarPlusBBbarDown",
                    #"_CMS_ttH_Q2scale_ttbarPlusCCbarUp","_CMS_ttH_Q2scale_ttbarPlusCCbarDown",
#                    "_CMS_ttH_NNPDFUp","_CMS_ttH_NNPDFDown",
#                    "_CMS_ttH_ljets_Trig_muUp","_CMS_ttH_ljets_Trig_muDown",  
#                     "_CMS_ttH_ljets_TrigUp","_CMS_ttH_ljets_TrigDown",
                   #"_CMS_ttH_eff_muUp","_CMS_ttH_eff_muDown",  
                   #"_CMS_ttH_eff_elUp","_CMS_ttH_eff_elDown", 
                   #"_CMS_ttH_eff_leptonUp","_CMS_ttH_eff_leptonDown",
                   "_CMS_res_jUp","_CMS_res_jDown",
                    "_CMS_scale_jUp","_CMS_scale_jDown",
                    #"_CMS_ttH_PSscaleUp","_CMS_ttH_PSscaleDown",
]

CSVSystnames=[
                    "",
                   "_CMS_ttH_CSVLFUp","_CMS_ttH_CSVLFDown","_CMS_ttH_CSVHFUp","_CMS_ttH_CSVHFDown",
                   "_CMS_ttH_CSVHFStats1Up","_CMS_ttH_CSVHFStats1Down","_CMS_ttH_CSVLFStats1Up","_CMS_ttH_CSVLFStats1Down",
                   "_CMS_ttH_CSVHFStats2Up","_CMS_ttH_CSVHFStats2Down","_CMS_ttH_CSVLFStats2Up","_CMS_ttH_CSVLFStats2Down",
                   "_CMS_ttH_CSVCErr1Up","_CMS_ttH_CSVCErr1Down","_CMS_ttH_CSVCErr2Up","_CMS_ttH_CSVCErr2Down",
#                    "_CMS_ttH_TopPtUp","_CMS_ttH_TopPtDown",
                    #"_CMS_ttH_PUUp","_CMS_ttH_PUDown",
                    #"_CMS_ttH_Q2scale_ttbarOtherUp","_CMS_ttH_Q2scale_ttbarOtherDown",
                    #"_CMS_ttH_Q2scale_ttbarPlusBUp","_CMS_ttH_Q2scale_ttbarPlusBDown",
                    #"_CMS_ttH_Q2scale_ttbarPlus2BUp","_CMS_ttH_Q2scale_ttbarPlus2BDown",
                    #"_CMS_ttH_Q2scale_ttbarPlusBBbarUp","_CMS_ttH_Q2scale_ttbarPlusBBbarDown",
                    #"_CMS_ttH_Q2scale_ttbarPlusCCbarUp","_CMS_ttH_Q2scale_ttbarPlusCCbarDown",
#                    "_CMS_ttH_NNPDFUp","_CMS_ttH_NNPDFDown",
#                    "_CMS_ttH_ljets_Trig_muUp","_CMS_ttH_ljets_Trig_muDown",  
#                     "_CMS_ttH_ljets_TrigUp","_CMS_ttH_ljets_TrigDown",
#                    "_CMS_ttH_eff_muUp","_CMS_ttH_eff_muDown",  
#                    "_CMS_ttH_eff_leptonUp","_CMS_ttH_eff_leptonDown",
                   #"","",
                    #"","",
                    #"_CMS_ttH_PSscaleUp","_CMS_ttH_PSscaleDown",
]

#mcweight='2.0*2.67*(Evt_Odd==0)*(N_Jets>=4 && N_BTagsM>=2)*((N_Jets==4 && N_BTagsM==3)||(N_Jets==4&&N_BTagsM==4)||(N_Jets==5&&N_BTagsM==3)||(N_Jets==5&&N_BTagsM>=4)||(N_Jets>=6&&N_BTagsM==2)||(N_Jets>=6&&N_BTagsM==3)||(N_Jets>=6&&N_BTagsM>=4)||(BoostedTopHiggs_TopHadCandidate_TopMVAOutput >= -0.485 && BoostedTopHiggs_HiggsCandidate_HiggsTag >= 0.8925))'
#mcweightAll='2.67*(N_Jets>=4 && N_BTagsM>=2)*((N_Jets==4 && N_BTagsM==3)||(N_Jets==4&&N_BTagsM==4)||(N_Jets==5&&N_BTagsM==3)||(N_Jets==5&&N_BTagsM>=4)||(N_Jets>=6&&N_BTagsM==2)||(N_Jets>=6&&N_BTagsM==3)||(N_Jets>=6&&N_BTagsM>=4)||(BoostedTopHiggs_TopHadCandidate_TopMVAOutput >= -0.485 && BoostedTopHiggs_HiggsCandidate_HiggsTag >= 0.8925))'
mcweightAll='12.9'
mcweight='12.9'

sfs="Weight_ElectronSFID*Weight_MuonSFID*Weight_MuonSFIso*Weight_ElectronSFGFS*Weight_MuonSFHIP"
usualweights="(1*Weight_pu69p2*((Weight>0)-(Weight<0)))"+"*"+sfs

#ttbarMCweight='*((N_BTagsM>=4)*((0.000919641*(N_GenTopHad==1 && N_GenTopLep==1)+0.0009753747*(N_GenTopLep==2 && N_GenTopHad==0)+0.0084896859*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS)+(0.0084896859/Weight_XS)*(N_BTagsM<4))'
#ttbarMCweight='*0.0084896859/Weight_XS'

# generator rate normalization weights
#mu_down_sf=1.1402
#mu_up_sf=0.8727
mu_down_sf=1.0
mu_up_sf=1.0
pdf_05_sf=0.950964383883
pdf_67_sf=1.04093344845

systweights=[
                    "NomWeight:="+usualweights+"*Weight_CSV*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVLFup:=("+usualweights+"*Weight_CSVLFup*Weight_CSV)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVLFdown:=("+usualweights+"*Weight_CSVLFdown*Weight_CSV)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVHFup:=("+usualweights+"*Weight_CSVHFup*Weight_CSV)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVHFdown:=("+usualweights+"*Weight_CSVHFdown*Weight_CSV)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVHFStats1up:=("+usualweights+"*Weight_CSVHFStats1up*Weight_CSV)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVHFStats1down:=("+usualweights+"*Weight_CSVHFStats1down*Weight_CSV)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVLFStats1up:=("+usualweights+"*Weight_CSVLFStats1up*Weight_CSV)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVLFStats1down:=("+usualweights+"*Weight_CSVLFStats1down*Weight_CSV)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVHFStats2up:=("+usualweights+"*Weight_CSVHFStats2up*Weight_CSV)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVHFStats2down:=("+usualweights+"*Weight_CSVHFStats2down*Weight_CSV)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVLFStats2up:=("+usualweights+"*Weight_CSVLFStats2up*Weight_CSV)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVLFStats2down:=("+usualweights+"*Weight_CSVLFStats2down*Weight_CSV)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVCErr1up:=("+usualweights+"*Weight_CSVCErr1up*Weight_CSV)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVCErr1down:=("+usualweights+"*Weight_CSVCErr1down*Weight_CSV)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVCErr2up:=("+usualweights+"*Weight_CSVCErr2up*Weight_CSV)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVCErr2down:=("+usualweights+"*Weight_CSVCErr2down*Weight_CSV)*(DoWeights==1)+(DoWeights==0)*1.0",
                   
                   #"dummyWeight_CSVCErr2down:=("+usualweights+"*Weight_CSVCErr2down*Weight_CSV)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVCErr2down:=("+usualweights+"*Weight_CSVCErr2down*Weight_CSV)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVCErr2down:=("+usualweights+"*Weight_CSVCErr2down*Weight_CSV)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVCErr2down:=("+usualweights+"*Weight_CSVCErr2down*Weight_CSV)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVCErr2down:=("+usualweights+"*Weight_CSVCErr2down*Weight_CSV)*(DoWeights==1)+(DoWeights==0)*1.0",

                   
                  
]

assert len(systweights)==len(weightsystnames)

othersystnames=[
                    "_CMS_scale_jUp",
                    "_CMS_scale_jDown",
                   "_CMS_res_jUp",
                   "_CMS_res_jDown"
                    #"_CMS_ttH_PSscaleUp",
                    #"_CMS_ttH_PSscaleDown"
]

othersystfilenames=[
                    "JESUP",
                    "JESDOWN",
                   "JERUP",
                   "JERDOWN"
                    #"scaleup",
                    #"scaledown"
]

assert len(errorSystnames)==len(weightsystnames+othersystnames)

# samples
# input path 
path_80x="/nfs/dust/cms/user/kelmorab/samples8019_ICHEP_V3"

# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
samples_data_controlplots=[
                    Sample('SingleMu',ROOT.kBlack,path_80x+'/mu_*/*nominal*.root',sel_singlemu,'SingleMu'),
                    Sample('SingleEl',ROOT.kBlack,path_80x+'/el_*/*nominal*.root',sel_singleel,'SingleEl')
]

# MC samples (name, color, path to files,weight,nickname_without_special_characters,systematics)                       
samplesControlPlots=[
                    Sample('t#bar{t}H',ROOT.kBlue+1,path_80x+'/Tranche3_ttH*/*nominal*.root',mcweight,'ttH',systs_all_samples) ,     
#                    Sample('t#bar{t}',ROOT.kRed+1,path_80x+'/ttbar/*nominal*.root',mcweight,'ttbar',systs_all_samples) ,     
                    Sample('t#bar{t}+lf',ROOT.kRed-7,path_80x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)','ttbarOther',systs_all_samples+systs_ttbar+systs_tt_lf,0.05),
                    Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,path_80x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==1)','ttbarPlusCCbar',systs_all_samples+systs_ttbar+systs_tt_cc,0.5),
                    Sample('t#bar{t}+b',ROOT.kRed-2,path_80x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==1)','ttbarPlusB',systs_all_samples+systs_ttbar+systs_tt_b,0.5),
                    Sample('t#bar{t}+2b',ROOT.kRed+2,path_80x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==2)','ttbarPlus2B',systs_all_samples+systs_ttbar+systs_tt_2b,0.5),
                    Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,path_80x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==3)','ttbarPlusBBbar',systs_all_samples+systs_ttbar+systs_tt_bb,0.5),  
                    Sample('Single Top',ROOT.kMagenta,path_80x+'/st*/*nominal*.root',mcweightAll,'SingleTop',systs_all_samples) , 
                    Sample('V+jets',ROOT.kGreen-3,path_80x+'/??ets*/*nominal*.root',mcweightAll,'Vjets',systs_all_samples) , 
                    Sample('t#bar{t}+V',ROOT.kBlue-10,path_80x+'/tt?_*/*nominal*.root',mcweightAll,'ttV',systs_all_samples),         
                    Sample('Diboson',ROOT.kAzure+2,path_80x+'/??/*nominal*.root',mcweightAll,'Diboson',systs_all_samples) , 
#                    Sample('QCD',ROOT.kYellow ,path_80x+'/QCD*/*nominal*root',mcweight,'QCD') , 
]

samplesLimits=[
                    Sample('t#bar{t}H',ROOT.kBlue+1,path_80x+'/Tranche3_ttH*/*nominal*.root',mcweight,'ttH',systs_all_samples) ,     
#                    Sample('t#bar{t}',ROOT.kRed+1,path_80x+'/ttbar/*nominal*.root',mcweight,'ttbar') ,     
                    Sample('t#bar{t}H, H to b#bar{b}',ROOT.kBlue+1,path_80x+'/Tranche3_ttHbb/*nominal*.root','1.009359*'+mcweight,'ttH_hbb',systs_all_samples) ,  
                    Sample('t#bar{t}H, H to c#bar{c}',ROOT.kBlue+1,path_80x+'/Tranche3_ttHnonbb/*nominal*.root','0.987234*'+mcweight+hccSel,'ttH_hcc',systs_all_samples) ,  
                    Sample('t#bar{t}H, H to #tau#tau',ROOT.kBlue+1,path_80x+'/Tranche3_ttHnonbb/*nominal*.root','0.987234*'+mcweight+httSel,'ttH_htt',systs_all_samples) ,  
                    Sample('t#bar{t}H, H to #gamma#gamma',ROOT.kBlue+1,path_80x+'/Tranche3_ttHnonbb/*nominal*.root','0.987234*'+mcweight+hggSel,'ttH_hgg',systs_all_samples) ,  
                    Sample('t#bar{t}H, H to gluglu',ROOT.kBlue+1,path_80x+'/Tranche3_ttHnonbb/*nominal*.root','0.987234*'+mcweight+hglugluSel,'ttH_hgluglu',systs_all_samples) ,  
                    Sample('t#bar{t}H, H to WW',ROOT.kBlue+1,path_80x+'/Tranche3_ttHnonbb/*nominal*.root','0.987234*'+mcweight+hwwSel,'ttH_hww',systs_all_samples) ,  
                    Sample('t#bar{t}H, H to ZZ',ROOT.kBlue+1,path_80x+'/Tranche3_ttHnonbb/*nominal*.root','0.987234*'+mcweight+hzzSel,'ttH_hzz',systs_all_samples) ,  
                    Sample('t#bar{t}H, H to #gamma Z',ROOT.kBlue+1,path_80x+'/Tranche3_ttHnonbb/*nominal*.root','0.987234*'+mcweight+hzgSel,'ttH_hzg',systs_all_samples) ,
                    Sample('t#bar{t}+lf',ROOT.kRed-7,path_80x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)','ttbarOther',systs_all_samples+systs_ttbar+systs_tt_lf,0.05),
                    Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,path_80x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==1)','ttbarPlusCCbar',systs_all_samples+systs_ttbar+systs_tt_cc,0.5),
                    Sample('t#bar{t}+b',ROOT.kRed-2,path_80x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==1)','ttbarPlusB',systs_all_samples+systs_ttbar+systs_tt_b,0.5),
                    Sample('t#bar{t}+2b',ROOT.kRed+2,path_80x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==2)','ttbarPlus2B',systs_all_samples+systs_ttbar+systs_tt_2b,0.5),
                    Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,path_80x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==3)','ttbarPlusBBbar',systs_all_samples+systs_ttbar+systs_tt_bb,0.5),
                    Sample('Single Top',ROOT.kMagenta,path_80x+'/st*/*nominal*.root',mcweightAll,'singlet',systs_all_samples) , 
                    Sample('Z+jets',ROOT.kGreen-3,path_80x+'/Zjets*/*nominal*.root',mcweightAll,'zjets',systs_all_samples) , 
                    Sample('W+jets',ROOT.kGreen-7,path_80x+'/WJets*/*nominal*.root',mcweightAll,'wjets',systs_all_samples) , 
                    Sample('t#bar{t}+W',ROOT.kBlue-10,path_80x+'/ttW_*/*nominal*.root',mcweightAll,'ttbarW',systs_all_samples),
                    Sample('t#bar{t}+Z',ROOT.kBlue-6,path_80x+'/ttZ_*/*nominal*.root',mcweightAll,'ttbarZ',systs_all_samples),
                    Sample('Diboson',ROOT.kAzure+2,path_80x+'/??/*nominal*.root',mcweightAll,'diboson',systs_all_samples) , 
#                    Sample('QCD',ROOT.kYellow ,path_80x+'/QCD*/*nominal*root',mcweightAll,'QCD') , 
]
