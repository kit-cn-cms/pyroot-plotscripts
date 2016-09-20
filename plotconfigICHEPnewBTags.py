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
#                    "_CMS_ttH_eff_leptonUp","_CMS_ttH_eff_leptonDown",  
#                    "_CMS_ttH_eff_elUp","_CMS_ttH_eff_elDown",
#                    "_CMS_res_jUp","_CMS_res_jDown"         
#                    "_CMS_ttH_ljets_Trig_muUp","_CMS_ttH_ljets_Trig_muDown",  
#                    "_CMS_ttH_ljets_Trig_elUp","_CMS_ttH_ljets_Trig_elDown",
#                    "_CMS_ttH_eff_muUp","_CMS_ttH_eff_muDown",  
#                    "_CMS_ttH_eff_elUp","_CMS_ttH_eff_elDown",
#                    "_CMS_res_jUp","_CMS_res_jDown"
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
#                    "_CMS_ttH_eff_muUp","_CMS_ttH_eff_muDown",  
#                    "_CMS_ttH_eff_elUp","_CMS_ttH_eff_elDown",
#                    "_CMS_ttH_ljets_TrigUp","_CMS_ttH_ljets_TrigDown",  
#                    "_CMS_ttH_ljets_Trig_elUp","_CMS_ttH_Trig_elDown",
#                    "_CMS_ttH_eff_leptonUp","_CMS_ttH_eff_leptonDown",  
#                    "_CMS_ttH_eff_elUp","_CMS_ttH_eff_elDown",
#                    "_CMS_res_jUp","_CMS_res_jDown",
                    #"_CMS_scale_jUp","_CMS_scale_jDown",
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
#                    "_CMS_ttH_eff_muUp","_CMS_ttH_eff_muDown",  
#                    "_CMS_ttH_eff_leptonUp","_CMS_ttH_eff_leptonDown",
#                    "_CMS_res_jUp","_CMS_res_jDown",
                    #"_CMS_scale_jUp","_CMS_scale_jDown",
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
#                    "_CMS_res_jUp","_CMS_res_jDown",
                    #"_CMS_scale_jUp","_CMS_scale_jDown",
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
                    ####"rwtptup:=(2.0*(Weight_TopPt - 1.0)+1.0):=1*Weight_pu69p2*Weight_CSV","rwtptdown:=Weight_TopPt:=1*Weight_pu69p2*Weight_CSV",
                    #"dummyWeight_pu69p2up:=(((Weight>0)-(Weight<0))*Weight_pu69p2up)*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_pu69p2down:=(((Weight>0)-(Weight<0))*Weight_pu69p2down)*(DoWeights==1)+(DoWeights==0)*1.0",
                    ##"QScaleTTLFUp:=((1.01414811611*(N_Jets==4))+(0.991304934025*(N_Jets==5))+(0.963434636593*(N_Jets==6))+(0.939875721931*(N_Jets==7))+(0.917543113232*(N_Jets==8))+(0.8953820467*(N_Jets==9))+(0.873915433884*(N_Jets>=10)))*"+usualweights+"/"+str(mu_up_sf),
                    ##"QScaleTTLFDown:=((0.980245113373*(N_Jets==4))+(1.01328265667*(N_Jets==5))+(1.05405771732*(N_Jets==6))+(1.08945119381*(N_Jets==7))+(1.12380123138*(N_Jets==8))+(1.1570687294*(N_Jets==9))+(1.19215357304*(N_Jets>=10)))*"+usualweights+"/"+str(mu_down_sf),
                    #"QScaleTTBUp:=((1.00080752373*(N_Jets==4))+(0.98769146204*(N_Jets==5))+(0.959815919399*(N_Jets==6))+(0.937435746193*(N_Jets==7))+(0.916143894196*(N_Jets==8))+(0.894755899906*(N_Jets==9))+(0.868403971195*(N_Jets>=10)))*"+usualweights+"/"+str(mu_up_sf),
                    #"QScaleTTBDown:=((1.00243294239*(N_Jets==4))+(1.0206540823*(N_Jets==5))+(1.06033742428*(N_Jets==6))+(1.0929582119*(N_Jets==7))+(1.12642657757*(N_Jets==8))+(1.15794050694*(N_Jets==9))+(1.19969570637*(N_Jets>=10)))*"+usualweights+"/"+str(mu_down_sf),
                    #"QScaleTTtwoBUp:=((0.975281894207*(N_Jets==4))+(0.953413248062*(N_Jets==5))+(0.932874321938*(N_Jets==6))+(0.912691235542*(N_Jets==7))+(0.893474340439*(N_Jets==8))+(0.866630315781*(N_Jets==9))+(0.858419597149*(N_Jets>=10)))*"+usualweights+"/"+str(mu_up_sf),
                    #"QScaleTTtwoBDown:=((1.03818035126*(N_Jets==4))+(1.06860983372*(N_Jets==5))+(1.10030317307*(N_Jets==6))+(1.13194000721*(N_Jets==7))+(1.16208589077*(N_Jets==8))+(1.20127081871*(N_Jets==9))+(1.21736299992*(N_Jets>=10)))*"+usualweights+"/"+str(mu_down_sf),
                    #"QScaleTTBBUp:=((0.98314666748*(N_Jets==4))+(0.968169569969*(N_Jets==5))+(0.948311269283*(N_Jets==6))+(0.928028643131*(N_Jets==7))+(0.908719837666*(N_Jets==8))+(0.887089312077*(N_Jets==9))+(0.860499441624*(N_Jets>=10)))*"+usualweights+"/"+str(mu_up_sf),
                    #"QScaleTTBBDown:=((1.02689313889*(N_Jets==4))+(1.04824054241*(N_Jets==5))+(1.07803595066*(N_Jets==6))+(1.10838377476*(N_Jets==7))+(1.1380418539*(N_Jets==8))+(1.17105853558*(N_Jets==9))+(1.21034097672*(N_Jets>=10)))*"+usualweights+"/"+str(mu_down_sf),
                    #"QScaleTTCCUp:=((0.998227715492*(N_Jets==4))+(0.978507816792*(N_Jets==5))+(0.955599665642*(N_Jets==6))+(0.932279765606*(N_Jets==7))+(0.909580647945*(N_Jets==8))+(0.888812601566*(N_Jets==9))+(0.868953943253*(N_Jets>=10)))*"+usualweights+"/"+str(mu_up_sf),
                    #"QScaleTTCCDown:=((1.00395655632*(N_Jets==4))+(1.03199350834*(N_Jets==5))+(1.06639623642*(N_Jets==6))+(1.10069298744*(N_Jets==7))+(1.13542354107*(N_Jets==8))+(1.16670846939*(N_Jets==9))+(1.19929921627*(N_Jets>=10)))*"+usualweights+"/"+str(mu_down_sf),
#                    "PDFweightUp:=Weight_NNPDFid260067*"+usualweights+"/"+str(pdf_67_sf),
#                    "PDFWeightDown:=Weight_NNPDFid260005*"+usualweights+"/"+str(pdf_05_sf),
#                    "dummyCMS_ttH_ljets_TrigUp:="+"(1*Weight_pu69p2*TMath::Sign(1.0,Weight)*"+"muonIDHelper.GetSF(muonPt,muonEta,0)*muonIsoHelper.GetSF(muonPt,muonEta,0)*muonTriggerHelper.GetSF(muonPt,muonEta,1)"+"*"+"electronIDHelper.GetSF(electronPt,electronEta,0)*electronIsoHelper.GetSF(electronPt,electronEta,0)*electronTriggerHelper.GetSF(electronPt,electronEta,1)"+"*Weight_CSV)"+"*(DoWeights==1)*(1.0*(N_TightMuons==1 && N_TightElectrons==0)+1.04*(N_TightMuons==0 && N_TightElectrons==1))+(DoWeights==0)*1.0",
#                    "dummyCMS_ttH_ljets_TrigDown:="+"(1*Weight_pu69p2*TMath::Sign(1.0,Weight)*"+"muonIDHelper.GetSF(muonPt,muonEta,0)*muonIsoHelper.GetSF(muonPt,muonEta,0)*muonTriggerHelper.GetSF(muonPt,muonEta,-1)"+"*"+"electronIDHelper.GetSF(electronPt,electronEta,0)*electronIsoHelper.GetSF(electronPt,electronEta,0)*electronTriggerHelper.GetSF(electronPt,electronEta,-1)"+"*Weight_CSV)"+"*(DoWeights==1)*(1.0*(N_TightMuons==1 && N_TightElectrons==0)+0.96*(N_TightMuons==0 && N_TightElectrons==1))+(DoWeights==0)*1.0",
#                    "dummyCMS_ttH_ljets_Trig_elUp:="+"(1*Weight_pu69p2*TMath::Sign(1.0,Weight)*"+muSF+"*"+"electronIDHelper.GetSF(electronPt,electronEta,0)*electronIsoHelper.GetSF(electronPt,electronEta,0)*electronTriggerHelper.GetSF(electronPt,electronEta,1)"+"*Weight_CSV)"+"*(DoWeights==1)*(1.01*(N_TightElectrons==1)+1.0*(N_TightElectrons==0))+(DoWeights==0)*1.0",
#                    "dummyCMS_ttH_ljets_Trig_elDown:="+"(1*Weight_pu69p2*TMath::Sign(1.0,Weight)*"+muSF+"*"+"electronIDHelper.GetSF(electronPt,electronEta,0)*electronIsoHelper.GetSF(electronPt,electronEta,0)*electronTriggerHelper.GetSF(electronPt,electronEta,-1)"+"*Weight_CSV)"+"*(DoWeights==1)*(0.99*(N_TightElectrons==1)+1.0*(N_TightElectrons==0))+(DoWeights==0)*1.0",
#                    "dummyCMS_ttH_eff_leptonUp:="+"(1*Weight_pu69p2*TMath::Sign(1.0,Weight)*"+"muonIDHelper.GetSF(muonPt,muonEta,1)*muonIsoHelper.GetSF(muonPt,muonEta,1)*muonTriggerHelper.GetSF(muonPt,muonEta,0)"+"*"+"electronIDHelper.GetSF(electronPt,electronEta,1)*electronIsoHelper.GetSF(electronPt,electronEta,1)*electronTriggerHelper.GetSF(electronPt,electronEta,0)"+"*Weight_CSV)"+"*(DoWeights==1)*(1.0*(N_TightMuons==1 && N_TightElectrons==0)+1.04*(N_TightMuons==0 && N_TightElectrons==1))+(DoWeights==0)*1.0",
#                    "dummyCMS_ttH_eff_leptonDown:="+"(1*Weight_pu69p2*TMath::Sign(1.0,Weight)*"+"muonIDHelper.GetSF(muonPt,muonEta,-1)*muonIsoHelper.GetSF(muonPt,muonEta,-1)*muonTriggerHelper.GetSF(muonPt,muonEta,0)"+"*"+"electronIDHelper.GetSF(electronPt,electronEta,-1)*electronIsoHelper.GetSF(electronPt,electronEta,-1)*electronTriggerHelper.GetSF(electronPt,electronEta,0)"+"*Weight_CSV)"+"*(DoWeights==1)*(1.0*(N_TightMuons==1 && N_TightElectrons==0)+0.96*(N_TightMuons==0 && N_TightElectrons==1))+(DoWeights==0)*1.0",
#                    "dummyCMS_ttH_eff_elUp:="+"(1*Weight_pu69p2*TMath::Sign(1.0,Weight)*"+muSF+"*"+"electronIDHelper.GetSF(electronPt,electronEta,1)*electronIsoHelper.GetSF(electronPt,electronEta,1)*electronTriggerHelper.GetSF(electronPt,electronEta,0)"+"*Weight_CSV)"+"*(DoWeights==1)*(1.01*(N_TightElectrons==1)+1.0*(N_TightElectrons==0))+(DoWeights==0)*1.0",
#                    "dummyCMS_ttH_eff_elDown:="+"(1*Weight_pu69p2*TMath::Sign(1.0,Weight)*"+muSF+"*"+"electronIDHelper.GetSF(electronPt,electronEta,1)*electronIsoHelper.GetSF(electronPt,electronEta,1)*electronTriggerHelper.GetSF(electronPt,electronEta,0)"+"*Weight_CSV)"+"*(DoWeights==1)*(0.99*(N_TightElectrons==1)+1.0*(N_TightElectrons==0))+(DoWeights==0)*1.0",
#                    "MuonIDUp:=(1*Weight_pu69p2*muonIDHelper.GetSF(muonPt,muonEta,1)*muonIsoHelper.GetSF(muonPt,muonEta,0)*muonTriggerHelper.GetSF(muonPt,muonEta,0)*Weight_CSV)*(DoWeights==1)+(DoWeights==0)*1.0",
#                    "MuonIDDown:=(1*Weight_pu69p2*muonIDHelper.GetSF(muonPt,muonEta,-1)*muonIsoHelper.GetSF(muonPt,muonEta,0)*muonTriggerHelper.GetSF(muonPt,muonEta,0)*Weight_CSV)*(DoWeights==1)+(DoWeights==0)*1.0",
#                    "MuonIsoUp:=(1*Weight_pu69p2*muonIDHelper.GetSF(muonPt,muonEta,0)*muonIsoHelper.GetSF(muonPt,muonEta,1)*muonTriggerHelper.GetSF(muonPt,muonEta,0)*Weight_CSV)*(DoWeights==1)+(DoWeights==0)*1.0",
#                    "MuonIsoDown:=(1*Weight_pu69p2*muonIDHelper.GetSF(muonPt,muonEta,0)*muonIsoHelper.GetSF(muonPt,muonEta,-1)*muonTriggerHelper.GetSF(muonPt,muonEta,0)*Weight_CSV)*(DoWeights==1)+(DoWeights==0)*1.0",
#                    "MuonTriggerUp:=(1*Weight_pu69p2*muonIDHelper.GetSF(muonPt,muonEta,0)*muonIsoHelper.GetSF(muonPt,muonEta,0)*muonTriggerHelper.GetSF(muonPt,muonEta,1)*Weight_CSV)*(DoWeights==1)+(DoWeights==0)*1.0",
#                    "MuonTriggerDown:=(1*Weight_pu69p2*muonIDHelper.GetSF(muonPt,muonEta,0)*muonIsoHelper.GetSF(muonPt,muonEta,0)*muonTriggerHelper.GetSF(muonPt,muonEta,-1)*Weight_CSV)*(DoWeights==1)+(DoWeights==0)*1.0",
#                    "dummyWeight_CMS_res_jUp:=JERUpWeight*"+usualweights+"*(DoWeights==1)+(DoWeights==0)*1.0",
#                    "dummyWeight_CMS_res_jDown:=JERDownWeight*"+usualweights+"*(DoWeights==1)+(DoWeights==0)*1.0"
]

assert len(systweights)==len(weightsystnames)

othersystnames=[
                    #"_CMS_scale_jUp",
                    #"_CMS_scale_jDown",
#                    "_CMS_res_jUp",
#                    "_CMS_res_jDown"
                    #"_CMS_ttH_PSscaleUp",
                    #"_CMS_ttH_PSscaleDown"
]

othersystfilenames=[
                    #"JESUP",
                    #"JESDOWN",
#                    "JERUP",
#                    "JERDOWN"
                    #"scaleup",
                    #"scaledown"
]

assert len(errorSystnames)==len(weightsystnames+othersystnames)

# samples
# input path 
path_80x="/nfs/dust/cms/user/kelmorab/samples8019_newBTags"

# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
samples_data_controlplots=[
                    Sample('SingleMu',ROOT.kBlack,path_80x+'/mu_*/*nominal*.root',sel_singlemu,'SingleMu'),
                    Sample('SingleEl',ROOT.kBlack,path_80x+'/el_*/*nominal*.root',sel_singleel,'SingleEl')
]

# MC samples (name, color, path to files,weight,nickname_without_special_characters,systematics)                       
samplesControlPlots=[
                    Sample('t#bar{t}H',ROOT.kBlue+1,path_80x+'/ttH*/*nominal*.root',mcweight,'ttH',systs_all_samples) ,     
#                    Sample('t#bar{t}',ROOT.kRed+1,path_80x+'/ttbar/*nominal*.root',mcweight,'ttbar',systs_all_samples) ,     
                    Sample('t#bar{t}+lf',ROOT.kRed-7,path_80x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)','ttbarOther',systs_all_samples+systs_ttbar+systs_tt_lf,0.05),
                    Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,path_80x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==1)','ttbarPlusCCbar',systs_all_samples+systs_ttbar+systs_tt_cc,0.5),
                    Sample('t#bar{t}+b',ROOT.kRed-2,path_80x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==1)','ttbarPlusB',systs_all_samples+systs_ttbar+systs_tt_b,0.5),
                    Sample('t#bar{t}+2b',ROOT.kRed+2,path_80x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==2)','ttbarPlus2B',systs_all_samples+systs_ttbar+systs_tt_2b,0.5),
                    Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,path_80x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==3)','ttbarPlusBBbar',systs_all_samples+systs_ttbar+systs_tt_bb,0.5),  
                    Sample('Single Top',ROOT.kMagenta,path_80x+'/st*/*nominal*.root',mcweightAll,'SingleTop',systs_all_samples) , 
                    Sample('V+jets',ROOT.kGreen-3,path_80x+'/??ets*/*nominal*.root',mcweightAll,'Vjets',systs_all_samples) , 
                    #Sample('t#bar{t}+V',ROOT.kBlue-10,path_80x+'/tt?_*/*nominal*.root',mcweightAll,'ttV',systs_all_samples),         
                    ##Sample('Diboson',ROOT.kAzure+2,path_80x+'/??/*nominal*.root',mcweightAll,'Diboson',systs_all_samples) , 
#                    Sample('QCD',ROOT.kYellow ,path_80x+'/QCD*/*nominal*root',mcweight,'QCD') , 
]

samplesLimits=[
                    Sample('t#bar{t}H',ROOT.kBlue+1,path_80x+'/ttH*/*nominal*.root',mcweight,'ttH',systs_all_samples) ,     
#                    Sample('t#bar{t}',ROOT.kRed+1,path_80x+'/ttbar/*nominal*.root',mcweight,'ttbar') ,     
                    Sample('t#bar{t}H, H to b#bar{b}',ROOT.kBlue+1,path_80x+'/ttHbb*/*nominal*.root','1.009359*'+mcweight,'ttH_hbb',systs_all_samples) ,  
                    Sample('t#bar{t}H, H to c#bar{c}',ROOT.kBlue+1,path_80x+'/ttHnonbb*/*nominal*.root','0.987234*'+mcweight+hccSel,'ttH_hcc',systs_all_samples) ,  
                    Sample('t#bar{t}H, H to #tau#tau',ROOT.kBlue+1,path_80x+'/ttHnonbb*/*nominal*.root','0.987234*'+mcweight+httSel,'ttH_htt',systs_all_samples) ,  
                    Sample('t#bar{t}H, H to #gamma#gamma',ROOT.kBlue+1,path_80x+'/ttHnonbb*/*nominal*.root','0.987234*'+mcweight+hggSel,'ttH_hgg',systs_all_samples) ,  
                    Sample('t#bar{t}H, H to gluglu',ROOT.kBlue+1,path_80x+'/ttHnonbb*/*nominal*.root','0.987234*'+mcweight+hglugluSel,'ttH_hgluglu',systs_all_samples) ,  
                    Sample('t#bar{t}H, H to WW',ROOT.kBlue+1,path_80x+'/ttHnonbb*/*nominal*.root','0.987234*'+mcweight+hwwSel,'ttH_hww',systs_all_samples) ,  
                    Sample('t#bar{t}H, H to ZZ',ROOT.kBlue+1,path_80x+'/ttHnonbb*/*nominal*.root','0.987234*'+mcweight+hzzSel,'ttH_hzz',systs_all_samples) ,  
                    Sample('t#bar{t}H, H to #gamma Z',ROOT.kBlue+1,path_80x+'/ttHnonbb*/*nominal*.root','0.987234*'+mcweight+hzgSel,'ttH_hzg',systs_all_samples) ,
                    Sample('t#bar{t}+lf',ROOT.kRed-7,path_80x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)','ttbarOther',systs_all_samples+systs_ttbar+systs_tt_lf,0.05),
                    Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,path_80x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==1)','ttbarPlusCCbar',systs_all_samples+systs_ttbar+systs_tt_cc,0.5),
                    Sample('t#bar{t}+b',ROOT.kRed-2,path_80x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==1)','ttbarPlusB',systs_all_samples+systs_ttbar+systs_tt_b,0.5),
                    Sample('t#bar{t}+2b',ROOT.kRed+2,path_80x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==2)','ttbarPlus2B',systs_all_samples+systs_ttbar+systs_tt_2b,0.5),
                    Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,path_80x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==3)','ttbarPlusBBbar',systs_all_samples+systs_ttbar+systs_tt_bb,0.5),
                    Sample('Single Top',ROOT.kMagenta,path_80x+'/st*/*nominal*.root',mcweightAll,'singlet',systs_all_samples) , 
                    #Sample('Z+jets',ROOT.kGreen-3,path_80x+'/Zjets*/*nominal*.root',mcweightAll,'zjets',systs_all_samples) , 
                    #Sample('W+jets',ROOT.kGreen-7,path_80x+'/WJets*/*nominal*.root',mcweightAll,'wjets',systs_all_samples) , 
                    #Sample('t#bar{t}+W',ROOT.kBlue-10,path_80x+'/ttW_*/*nominal*.root',mcweightAll,'ttbarW',systs_all_samples),
                    #Sample('t#bar{t}+Z',ROOT.kBlue-6,path_80x+'/ttZ_*/*nominal*.root',mcweightAll,'ttbarZ',systs_all_samples),
                    #Sample('Diboson',ROOT.kAzure+2,path_80x+'/??/*nominal*.root',mcweightAll,'diboson',systs_all_samples) , 
#                    Sample('QCD',ROOT.kYellow ,path_80x+'/QCD*/*nominal*root',mcweightAll,'QCD') , 
]
