import sys
import os
sys.path.insert(0, '../')
from scriptgenerator import *
from plotutils import *

mcweight='2.0*2.61*(Evt_Odd==0)*(N_Jets>=4 && N_BTagsM>=2)'
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


path_excl4252='/nfs/dust/cms/user/hmildner/merged_trees/output/'
path_incl4252='/nfs/dust/cms/user/hmildner/merged_trees/output*/'
path_swold='/nfs/dust/cms/user/shwillia/BoostedTrees/Setup_160127/'
path_76x='/nfs/dust/cms/user/kelmorab/Samples76x21022016'

# names of the systematics (proper names needed e.g. for combination)
weightsystnames=["",
                 "_CMS_ttH_CSVLFUp","_CMS_ttH_CSVLFDown","_CMS_ttH_CSVHFUp","_CMS_ttH_CSVHFDown",
                 "_CMS_ttH_CSVHFStats1Up","_CMS_ttH_CSVHFStats1Down","_CMS_ttH_CSVLFStats1Up","_CMS_ttH_CSVLFStats1Down",
                 "_CMS_ttH_CSVHFStats2Up","_CMS_ttH_CSVHFStats2Down","_CMS_ttH_CSVLFStats2Up","_CMS_ttH_CSVLFStats2Down",
                 "_CMS_ttH_CSVCErr1Up","_CMS_ttH_CSVCErr1Down","_CMS_ttH_CSVCErr2Up","_CMS_ttH_CSVCErr2Down",
                 #"_CMS_ttH_TopPtUp","_CMS_ttH_TopPtDown",
                 "_CMS_ttH_PUUp","_CMS_ttH_PUDown",
                 "_CMS_ttH_Q2scale_ttbarOtherUp","_CMS_ttH_Q2scale_ttbarOtherDown",
                 "_CMS_ttH_Q2scale_ttbarPlusBUp","_CMS_ttH_Q2scale_ttbarPlusBDown",
                 "_CMS_ttH_Q2scale_ttbarPlus2BUp","_CMS_ttH_Q2scale_ttbarPlus2BDown",
                 "_CMS_ttH_Q2scale_ttbarPlusBBbarUp","_CMS_ttH_Q2scale_ttbarPlusBBbarDown",
                 "_CMS_ttH_Q2scale_ttbarPlusCCbarUp","_CMS_ttH_Q2scale_ttbarPlusCCbarDown",
                 "_CMS_ttH_NNPDFUp","_CMS_ttH_NNPDFDown",
                 #"_CMS_ttH_MuonIDUp","_CMS_ttH_MuonIDDown",
                 #"_CMS_ttH_MuonIsoUp","_CMS_ttH_MuonIsoDown",
                 #"_CMS_ttH_MuonTriggerUp","_CMS_ttH_MuonTriggerDown",                 
           ]

systs_all_samples=["",
                  "_CMS_ttH_CSVLFUp","_CMS_ttH_CSVLFDown","_CMS_ttH_CSVHFUp","_CMS_ttH_CSVHFDown",
                  "_CMS_ttH_CSVHFStats1Up","_CMS_ttH_CSVHFStats1Down","_CMS_ttH_CSVLFStats1Up","_CMS_ttH_CSVLFStats1Down",
                  "_CMS_ttH_CSVHFStats2Up","_CMS_ttH_CSVHFStats2Down","_CMS_ttH_CSVLFStats2Up","_CMS_ttH_CSVLFStats2Down",
                  "_CMS_ttH_CSVCErr1Up","_CMS_ttH_CSVCErr1Down","_CMS_ttH_CSVCErr2Up","_CMS_ttH_CSVCErr2Down",
                   "_CMS_ttH_PUUp","_CMS_ttH_PUDown",
                   "_CMS_scale_jUp","_CMS_scale_jDown",
                  #"_CMS_ttH_MuonIDUp","_CMS_ttH_MuonIDDown",
                  #"_CMS_ttH_MuonIsoUp","_CMS_ttH_MuonIsoDown",
                  #"_CMS_ttH_MuonTriggerUp","_CMS_ttH_MuonTriggerDown",
                   ]

systs_ttbar= [
	      "_CMS_ttH_NNPDFUp","_CMS_ttH_NNPDFDown",
	      "_CMS_ttH_PSscaleUp","_CMS_ttH_PSscaleDown",
	      ]
systs_tt_lf=["_CMS_ttH_Q2scale_ttbarOtherUp","_CMS_ttH_Q2scale_ttbarOtherDown",]
systs_tt_b=["_CMS_ttH_Q2scale_ttbarPlusBUp","_CMS_ttH_Q2scale_ttbarPlusBDown"]
systs_tt_2b=[ "_CMS_ttH_Q2scale_ttbarPlus2BUp","_CMS_ttH_Q2scale_ttbarPlus2BDown"]
systs_tt_bb=[ "_CMS_ttH_Q2scale_ttbarPlusBBbarUp","_CMS_ttH_Q2scale_ttbarPlusBBbarDown"]
systs_tt_cc=[ "_CMS_ttH_Q2scale_ttbarPlusCCbarUp","_CMS_ttH_Q2scale_ttbarPlusCCbarDown"]



PSSystnames=["",
		 "","","","",
		 "","","","",
		 "","","","",
		 "","","","",
		 #"_CMS_ttH_TopPtUp","_CMS_ttH_TopPtDown",
		 "","",
		 "","",
		 "","",
		 "","",
		 "","",
		 "","",
		 "","",
		 "","",
                 "_CMS_ttH_PSscaleUp","_CMS_ttH_PSscaleDown",
                 #"","",
		 #"","",
		 #"","",
                 ]

errorSystnames=["",
		 "_CMS_ttH_CSVLFUp","_CMS_ttH_CSVLFDown","_CMS_ttH_CSVHFUp","_CMS_ttH_CSVHFDown",
                 "_CMS_ttH_CSVHFStats1Up","_CMS_ttH_CSVHFStats1Down","_CMS_ttH_CSVLFStats1Up","_CMS_ttH_CSVLFStats1Down",
                 "_CMS_ttH_CSVHFStats2Up","_CMS_ttH_CSVHFStats2Down","_CMS_ttH_CSVLFStats2Up","_CMS_ttH_CSVLFStats2Down",
                 "_CMS_ttH_CSVCErr1Up","_CMS_ttH_CSVCErr1Down","_CMS_ttH_CSVCErr2Up","_CMS_ttH_CSVCErr2Down",
		 #"_CMS_ttH_TopPtUp","_CMS_ttH_TopPtDown",
                 "_CMS_ttH_PUUp","_CMS_ttH_PUDown",
		 "_CMS_ttH_Q2scale_ttbarOtherUp","_CMS_ttH_Q2scale_ttbarOtherDown",
                 "_CMS_ttH_Q2scale_ttbarPlusBUp","_CMS_ttH_Q2scale_ttbarPlusBDown",
                 "_CMS_ttH_Q2scale_ttbarPlus2BUp","_CMS_ttH_Q2scale_ttbarPlus2BDown",
                 "_CMS_ttH_Q2scale_ttbarPlusBBbarUp","_CMS_ttH_Q2scale_ttbarPlusBBbarDown",
                 "_CMS_ttH_Q2scale_ttbarPlusCCbarUp","_CMS_ttH_Q2scale_ttbarPlusCCbarDown",
                 "_CMS_ttH_NNPDFUp","_CMS_ttH_NNPDFDown",
                 "_CMS_scale_jUp","_CMS_scale_jDown",
                 "_CMS_ttH_PSscaleUp","_CMS_ttH_PSscaleDown",
                 #"","",
		 #"","",
		 #"","",
                 ]


# corresponding weight names
mu_down_sf=1.1402
mu_up_sf=0.8727
pdf_05_sf=0.950964383883
pdf_67_sf=1.04093344845


#systweightsold=["1",
             #"Weight_CSVLFup","Weight_CSVLFdown","Weight_CSVHFup","Weight_CSVHFdown",
             #"Weight_CSVHFStats1up","Weight_CSVHFStats1down","Weight_CSVLFStats1up","Weight_CSVLFStats1down",
             #"Weight_CSVHFStats2up","Weight_CSVHFStats2down","Weight_CSVLFStats2up","Weight_CSVLFStats2down",
             #"Weight_CSVCErr1up","Weight_CSVCErr1down","Weight_CSVCErr2up","Weight_CSVCErr2down",
             ##"rwtptup:=(2.0*(Weight_TopPt - 1.0)+1.0)","rwtptdown:=Weight_TopPt",
             #"Weight_PUup","Weight_PUdown",
             #"QScaleTTLFUp:=Weight_muRupmuFup/"+str(mu_up_sf),"QScaleTTLFDown:=Weight_muRdownmuFdown/"+str(mu_down_sf),
             #"QScaleTTBUp:=Weight_muRupmuFup/"+str(mu_up_sf),"QScaleTTBDown:=Weight_muRdownmuFdown/"+str(mu_down_sf),
             #"QScaleTTtwoBUp:=Weight_muRupmuFup/"+str(mu_up_sf),"QScaleTTtwoBDown:=Weight_muRdownmuFdown/"+str(mu_down_sf),
             #"QScaleTTBBUp:=Weight_muRupmuFup/"+str(mu_up_sf),"QScaleTTBBDown:=Weight_muRdownmuFdown/"+str(mu_down_sf),
             #"QScaleTTCCUp:=Weight_muRupmuFup/"+str(mu_up_sf),"QScaleTTCCDown:=Weight_muRdownmuFdown/"+str(mu_down_sf),
             #"PDFweightUp:=Weight_NNPDFid260067/"+str(pdf_67_sf),"PDFWeightDown:=Weight_NNPDFid260005/"+str(pdf_05_sf),
             #]

## in future use Muon SF
#muSF="muonIDHelper.GetSF(muonPt,muonEta,0)*muonIsoHelper.GetSF(muonPt,muonEta,0)*muonTriggerHelper.GetSF(muonPt,muonEta,0)"
muSF="1.0"
usualweights="(1*Weight_PU*"+muSF+"*csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,internalSystName,csvWgtHF,csvWgtLF,csvWgtCF))"


systweights=["NomWeight:="+usualweights+"*(DoWeights==1)+(DoWeights==0)*1.0",
             "dummyWeight_CSVLFup:=(1*Weight_PU*"+muSF+"*csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,9,csvWgtHF,csvWgtLF,csvWgtCF))*(DoWeights==1)+(DoWeights==0)*1.0",
             "dummyWeight_CSVLFdown:=(1*Weight_PU*"+muSF+"*csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,10,csvWgtHF,csvWgtLF,csvWgtCF))*(DoWeights==1)+(DoWeights==0)*1.0",
             "dummyWeight_CSVHFup:=(1*Weight_PU*"+muSF+"*csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,11,csvWgtHF,csvWgtLF,csvWgtCF))*(DoWeights==1)+(DoWeights==0)*1.0",
             "dummyWeight_CSVHFdown:=(1*Weight_PU*"+muSF+"*csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,12,csvWgtHF,csvWgtLF,csvWgtCF))*(DoWeights==1)+(DoWeights==0)*1.0",
             "dummyWeight_CSVHFStats1up:=(1*Weight_PU*"+muSF+"*csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,13,csvWgtHF,csvWgtLF,csvWgtCF))*(DoWeights==1)+(DoWeights==0)*1.0",
             "dummyWeight_CSVHFStats1down:=(1*Weight_PU*"+muSF+"*csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,14,csvWgtHF,csvWgtLF,csvWgtCF))*(DoWeights==1)+(DoWeights==0)*1.0",
             "dummyWeight_CSVLFStats1up:=(1*Weight_PU*"+muSF+"*csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,17,csvWgtHF,csvWgtLF,csvWgtCF))*(DoWeights==1)+(DoWeights==0)*1.0",
             "dummyWeight_CSVLFStats1down:=(1*Weight_PU*"+muSF+"*csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,18,csvWgtHF,csvWgtLF,csvWgtCF))*(DoWeights==1)+(DoWeights==0)*1.0",
             "dummyWeight_CSVHFStats2up:=(1*Weight_PU*"+muSF+"*csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,15,csvWgtHF,csvWgtLF,csvWgtCF))*(DoWeights==1)+(DoWeights==0)*1.0",
             "dummyWeight_CSVHFStats2down:=(1*Weight_PU*"+muSF+"*csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,16,csvWgtHF,csvWgtLF,csvWgtCF))*(DoWeights==1)+(DoWeights==0)*1.0",
             "dummyWeight_CSVLFStats2up:=(1*Weight_PU*"+muSF+"*csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,19,csvWgtHF,csvWgtLF,csvWgtCF))*(DoWeights==1)+(DoWeights==0)*1.0",
             "dummyWeight_CSVLFStats2down:=(1*Weight_PU*"+muSF+"*csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,20,csvWgtHF,csvWgtLF,csvWgtCF))*(DoWeights==1)+(DoWeights==0)*1.0",
             "dummyWeight_CSVCErr1up:=(1*Weight_PU*"+muSF+"*csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,21,csvWgtHF,csvWgtLF,csvWgtCF))*(DoWeights==1)+(DoWeights==0)*1.0",
             "dummyWeight_CSVCErr1down:=(1*Weight_PU*"+muSF+"*csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,22,csvWgtHF,csvWgtLF,csvWgtCF))*(DoWeights==1)+(DoWeights==0)*1.0",
             "dummyWeight_CSVCErr2up:=(1*Weight_PU*"+muSF+"*csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,23,csvWgtHF,csvWgtLF,csvWgtCF))*(DoWeights==1)+(DoWeights==0)*1.0",
             "dummyWeight_CSVCErr2down:=(1*Weight_PU*"+muSF+"*csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,24,csvWgtHF,csvWgtLF,csvWgtCF))*(DoWeights==1)+(DoWeights==0)*1.0",
            ####"rwtptup:=(2.0*(Weight_TopPt - 1.0)+1.0):=1*Weight_PU*csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,internalSystName,csvWgtHF,csvWgtLF,csvWgtCF)","rwtptdown:=Weight_TopPt:=1*Weight_PU*csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,internalSystName,csvWgtHF,csvWgtLF,csvWgtCF)",
             "dummyWeight_PUup:=(Weight_PUup*"+muSF+"*csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,internalSystName,csvWgtHF,csvWgtLF,csvWgtCF))*(DoWeights==1)+(DoWeights==0)*1.0",
             "dummyWeight_PUdown:=(Weight_PUdown*"+muSF+"*csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,internalSystName,csvWgtHF,csvWgtLF,csvWgtCF))*(DoWeights==1)+(DoWeights==0)*1.0",
             "QScaleTTLFUp:=Weight_muRupmuFup*"+usualweights+"/"+str(mu_up_sf),
             "QScaleTTLFDown:=Weight_muRdownmuFdown*"+usualweights+"/"+str(mu_down_sf),
             "QScaleTTBUp:=Weight_muRupmuFup*"+usualweights+"/"+str(mu_up_sf),
             "QScaleTTBDown:=Weight_muRdownmuFdown*"+usualweights+"/"+str(mu_down_sf),
             "QScaleTTtwoBUp:=Weight_muRupmuFup*"+usualweights+"/"+str(mu_up_sf),
             "QScaleTTtwoBDown:=Weight_muRdownmuFdown*"+usualweights+"/"+str(mu_down_sf),
             "QScaleTTBBUp:=Weight_muRupmuFup*"+usualweights+"/"+str(mu_up_sf),
             "QScaleTTBBDown:=Weight_muRdownmuFdown*"+usualweights+"/"+str(mu_down_sf),
             "QScaleTTCCUp:=Weight_muRupmuFup*"+usualweights+"/"+str(mu_up_sf),
             "QScaleTTCCDown:=Weight_muRdownmuFdown*"+usualweights+"/"+str(mu_down_sf),
             "PDFweightUp:=Weight_NNPDFid260067*"+usualweights+"/"+str(pdf_67_sf),
             "PDFWeightDown:=Weight_NNPDFid260005*"+usualweights+"/"+str(pdf_05_sf),
             #"MuonIDUp:=(1*Weight_PU*muonIDHelper.GetSF(muonPt,muonEta,1)*muonIsoHelper.GetSF(muonPt,muonEta,0)*muonTriggerHelper.GetSF(muonPt,muonEta,0)*csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,internalSystName,csvWgtHF,csvWgtLF,csvWgtCF))",
             #"MuonIDDown:=(1*Weight_PU*muonIDHelper.GetSF(muonPt,muonEta,-1)*muonIsoHelper.GetSF(muonPt,muonEta,0)*muonTriggerHelper.GetSF(muonPt,muonEta,0)*csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,internalSystName,csvWgtHF,csvWgtLF,csvWgtCF))",
             #"MuonIsoUp:=(1*Weight_PU*muonIDHelper.GetSF(muonPt,muonEta,0)*muonIsoHelper.GetSF(muonPt,muonEta,1)*muonTriggerHelper.GetSF(muonPt,muonEta,0)*csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,internalSystName,csvWgtHF,csvWgtLF,csvWgtCF))",
             #"MuonIsoDown:=(1*Weight_PU*muonIDHelper.GetSF(muonPt,muonEta,0)*muonIsoHelper.GetSF(muonPt,muonEta,-1)*muonTriggerHelper.GetSF(muonPt,muonEta,0)*csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,internalSystName,csvWgtHF,csvWgtLF,csvWgtCF))",
             #"MuonTriggerUp:=(1*Weight_PU*muonIDHelper.GetSF(muonPt,muonEta,0)*muonIsoHelper.GetSF(muonPt,muonEta,0)*muonTriggerHelper.GetSF(muonPt,muonEta,1)*csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,internalSystName,csvWgtHF,csvWgtLF,csvWgtCF))",
             #"MuonTriggerDown:=(1*Weight_PU*muonIDHelper.GetSF(muonPt,muonEta,0)*muonIsoHelper.GetSF(muonPt,muonEta,0)*muonTriggerHelper.GetSF(muonPt,muonEta,-1)*csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,internalSystName,csvWgtHF,csvWgtLF,csvWgtCF))",
             ]


#"Weight_pileupup:=((Weight_PU!=0.0) ? Weight_PUup/Weight_PU : Weight_PUup)","Weight_pileupdown:=((Weight_PU!=0.0) ? Weight_PUdown/Weight_PU : Weight_PUdown)",


assert len(systweights)==len(weightsystnames)

othersystnames=[
		"_CMS_scale_jUp",
                "_CMS_scale_jDown",
               #"_CMS_res_jUp",
               #"_CMS_res_jDown"
               "_CMS_ttH_PSscaleUp",
               "_CMS_ttH_PSscaleDown"
                ]

othersystfilenames=[
		    "JESUP",
                    "JESDOWN",
                   #"JERUP",
                   #"JERDOWN"
                   "scaleup",
                   "scaledown"
                   ]

samplesLimits=[Sample('t#bar{t}H',ROOT.kBlue+1,path_excl4252+'/ttH*/*nominal*.root',mcweight,'ttH') ,  
                     Sample('t#bar{t}H, H to b#bar{b}',ROOT.kBlue+1,path_excl4252+'/ttHbb*/*nominal*.root',mcweight,'ttH_hbb') ,  
                     Sample('t#bar{t}H, H to c#bar{c}',ROOT.kBlue+1,path_excl4252+'/ttHnonbb*/*nominal*.root',mcweight+hccSel,'ttH_hcc') ,  
                     Sample('t#bar{t}H, H to #tau#tau',ROOT.kBlue+1,path_excl4252+'/ttHnonbb*/*nominal*.root',mcweight+httSel,'ttH_htt') ,  
                     Sample('t#bar{t}H, H to #gamma#gamma',ROOT.kBlue+1,path_excl4252+'/ttHnonbb*/*nominal*.root',mcweight+hggSel,'ttH_hgg') ,  
                     Sample('t#bar{t}H, H to gluglu',ROOT.kBlue+1,path_excl4252+'/ttHnonbb*/*nominal*.root',mcweight+hglugluSel,'ttH_hgluglu') ,  
                     Sample('t#bar{t}H, H to WW',ROOT.kBlue+1,path_excl4252+'/ttHnonbb*/*nominal*.root',mcweight+hwwSel,'ttH_hww') ,  
                     Sample('t#bar{t}H, H to ZZ',ROOT.kBlue+1,path_excl4252+'/ttHnonbb*/*nominal*.root',mcweight+hzzSel,'ttH_hzz') ,  
                     Sample('t#bar{t}H, H to #gamma Z',ROOT.kBlue+1,path_excl4252+'/ttHnonbb*/*nominal*.root',mcweight+hzgSel,'ttH_hzg') ,
  	 
                     Sample('t#bar{t}+lf',ROOT.kRed-7,path_excl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)','ttbarOther'),
                     Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,path_excl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==1)','ttbarPlusCCbar'),
                     Sample('t#bar{t}+b',ROOT.kRed-2,path_excl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==1)','ttbarPlusB'),
                     Sample('t#bar{t}+2b',ROOT.kRed+2,path_excl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==2)','ttbarPlus2B'),
                     Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,path_excl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==3)','ttbarPlusBBbar'),  
                     Sample('Single Top',ROOT.kMagenta,path_excl4252+'/st*/*nominal*.root',mcweight,'singlet') , 
                     Sample('Z+jets',ROOT.kGreen-3,path_excl4252+'/Zjets*/*nominal*.root',mcweight,'zjets') , 
                     Sample('W+jets',ROOT.kGreen-7,path_excl4252+'/WJets*/*nominal*.root',mcweight,'wjets') , 
                     Sample('t#bar{t}+W',ROOT.kBlue-10,path_excl4252+'/ttW_*/*nominal*.root',mcweight,'ttbarW'),
                     Sample('t#bar{t}+Z',ROOT.kBlue-6,path_excl4252+'/ttZ_*/*nominal*.root',mcweight,'ttbarZ'),
                     Sample('Diboson',ROOT.kAzure+2,path_excl4252+'/??/*nominal*.root',mcweight,'diboson') , 
                     #Sample('QCD',ROOT.kYellow ,path_excl4252+'/QCD*/*nominal*root',mcweight,'QCD') , 
]

samplesLimitsBoosted=[Sample('t#bar{t}H',ROOT.kBlue+1,path_incl4252+'/ttH*/*nominal*.root',mcweight,'ttH') ,  
                      Sample('t#bar{t}H, H to b#bar{b}',ROOT.kBlue+1,path_incl4252+'/ttHbb*/*nominal*.root',mcweight,'ttH_hbb') ,  
                      Sample('t#bar{t}H, H to c#bar{c}',ROOT.kBlue+1,path_incl4252+'/ttHnonbb*/*nominal*.root',mcweight+hccSel,'ttH_hcc') ,  
                      Sample('t#bar{t}H, H to #tau#tau',ROOT.kBlue+1,path_incl4252+'/ttHnonbb*/*nominal*.root',mcweight+httSel,'ttH_htt') ,  
                      Sample('t#bar{t}H, H to #gamma#gamma',ROOT.kBlue+1,path_incl4252+'/ttHnonbb*/*nominal*.root',mcweight+hggSel,'ttH_hgg') ,  
                      Sample('t#bar{t}H, H to gluglu',ROOT.kBlue+1,path_incl4252+'/ttHnonbb*/*nominal*.root',mcweight+hglugluSel,'ttH_hgluglu') ,  
                      Sample('t#bar{t}H, H to WW',ROOT.kBlue+1,path_incl4252+'/ttHnonbb*/*nominal*.root',mcweight+hwwSel,'ttH_hww') ,  
                      Sample('t#bar{t}H, H to ZZ',ROOT.kBlue+1,path_incl4252+'/ttHnonbb*/*nominal*.root',mcweight+hzzSel,'ttH_hzz') ,  
                      Sample('t#bar{t}H, H to #gamma Z',ROOT.kBlue+1,path_incl4252+'/ttHnonbb*/*nominal*.root',mcweight+hzgSel,'ttH_hzg') ,

                      Sample('t#bar{t}+lf',ROOT.kRed-7,path_incl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)','ttbarOther'),
                      Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,path_incl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==1)','ttbarPlusCCbar'),
                      Sample('t#bar{t}+b',ROOT.kRed-2,path_incl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==1)','ttbarPlusB'),
                      Sample('t#bar{t}+2b',ROOT.kRed+2,path_incl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==2)','ttbarPlus2B'),
                      Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,path_incl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==3)','ttbarPlusBBbar'),  
                      Sample('Single Top',ROOT.kMagenta,path_incl4252+'/st*/*nominal*.root',mcweight,'singlet') , 
                      Sample('Z+jets',ROOT.kGreen-3,path_incl4252+'/Zjets*/*nominal*.root',mcweight,'zjets') , 
                      Sample('W+jets',ROOT.kGreen-7,path_incl4252+'/WJets*/*nominal*.root',mcweight,'wjets') , 
                      Sample('t#bar{t}+W',ROOT.kBlue-10,path_incl4252+'/ttW_*/*nominal*.root',mcweight,'ttbarW'),
                      Sample('t#bar{t}+Z',ROOT.kBlue-6,path_incl4252+'/ttZ_*/*nominal*.root',mcweight,'ttbarZ'),
                      Sample('Diboson',ROOT.kAzure+2,path_incl4252+'/??/*nominal*.root',mcweight,'diboson') , 
                      #Sample('QCD',ROOT.kYellow ,path_incl4252+'/QCD*/*nominal*root',mcweight,'QCD') , 
]

# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)

samples_data_controlplots=[Sample('SingleMu',ROOT.kBlack,path_76x+'/mu_*/*nominal*.root',sel_singlemu,'SingleMu'),
                           Sample('SingleEl',ROOT.kBlack,path_76x+'/el_*/*nominal*.root',sel_singleel,'SingleEl')
                       ]
                       
samples_data_controlplots_swold=[Sample('SingleMu',ROOT.kBlack,path_swold+'/mu_*/*nominal*.root',sel_singlemu,'SingleMu'),
                           Sample('SingleEl',ROOT.kBlack,path_swold+'/el_*/*nominal*.root',sel_singleel,'SingleEl')
                       ]
                       
samples_data_bdtplots=[Sample('SingleMu',ROOT.kBlack,path_incl4252+'/mu_*/*nominal*.root',sel_singlemu,'SingleMu'),
                           Sample('SingleEl',ROOT.kBlack,path_incl4252+'/el_*/*nominal*.root',sel_singleel,'SingleEl')
                       ]

ttbarMCweight='*(0.000919641*(N_GenTopHad==1 && N_GenTopLep==1)+0.000707116*(N_GenTopLep==2 && N_GenTopHad==0)+0.0084896859*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS'
samplesControlPlots=[Sample('t#bar{t}H',ROOT.kBlue+1,path_76x+'/ttH*/*nominal*.root',mcweight,'ttH',systs_all_samples) ,     
#         Sample('t#bar{t}',ROOT.kRed+1,path_76x+'/ttbar/*nominal*.root',mcweight,'ttbar') ,     
         Sample('t#bar{t}+lf',ROOT.kRed-7,path_76x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)'+ttbarMCweight,'ttbarOther',systs_all_samples+systs_ttbar+systs_tt_lf,0.05),
         Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,path_76x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==1)'+ttbarMCweight,'ttbarPlusCCbar',systs_all_samples+systs_ttbar+systs_tt_cc,0.5),
         Sample('t#bar{t}+b',ROOT.kRed-2,path_76x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==1)'+ttbarMCweight,'ttbarPlusB',systs_all_samples+systs_ttbar+systs_tt_b,0.5),
         Sample('t#bar{t}+2b',ROOT.kRed+2,path_76x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==2)'+ttbarMCweight,'ttbarPlus2B',systs_all_samples+systs_ttbar+systs_tt_2b,0.5),
         Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,path_76x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==3)'+ttbarMCweight,'ttbarPlusBBbar',systs_all_samples+systs_ttbar+systs_tt_bb,0.5),  
         Sample('Single Top',ROOT.kMagenta,path_76x+'/st*/*nominal*.root',mcweight,'SingleTop',systs_all_samples) , 
         Sample('V+jets',ROOT.kGreen-3,path_76x+'/??ets*/*nominal*.root',mcweight,'Vjets',systs_all_samples) , 
         Sample('t#bar{t}+V',ROOT.kBlue-10,path_76x+'/tt?_*/*nominal*.root',mcweight,'ttV',systs_all_samples),         
         Sample('Diboson',ROOT.kAzure+2,path_76x+'/??/*nominal*.root',mcweight,'Diboson',systs_all_samples) , 
#         Sample('QCD',ROOT.kYellow ,path_76x+'/QCD*/*nominal*root',mcweight,'QCD') , 
]

#samplesControlPlots_swold=[Sample('t#bar{t}H',ROOT.kBlue+1,path_swold+'/ttH*/*nominal*.root',mcweight,'ttH') ,     
##         Sample('t#bar{t}',ROOT.kRed+1,path_swold+'/ttbar/*nominal*.root',mcweight,'ttbar') ,     
         #Sample('t#bar{t}+lf',ROOT.kRed-7,path_swold+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)','ttl'),
         #Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,path_swold+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==1)','ttcc'),
         #Sample('t#bar{t}+b',ROOT.kRed-2,path_swold+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==1)','tt1b'),
         #Sample('t#bar{t}+2b',ROOT.kRed+2,path_swold+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==2)','tt2b'),
         #Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,path_swold+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==3)','ttbb'),  
         #Sample('Single Top',ROOT.kMagenta,path_swold+'/st*/*nominal*.root',mcweight,'SingleTop') , 
         #Sample('V+jets',ROOT.kGreen-3,path_swold+'/??ets*/*nominal*.root',mcweight,'Vjets') , 
         #Sample('t#bar{t}+V',ROOT.kBlue-10,path_swold+'/tt?_*/*nominal*.root',mcweight,'ttV'),         
         #Sample('Diboson',ROOT.kAzure+2,path_swold+'/??/*nominal*.root',mcweight,'Diboson') , 
##         Sample('QCD',ROOT.kYellow ,path_swold+'/QCD*/*nominal*root',mcweight,'QCD') , 
#]
samplesBDTplots=[Sample('t#bar{t}H',ROOT.kBlue+1,path_excl4252+'/ttH*/*nominal*.root',mcweight,'ttH',systs_all_samples) ,     
#         Sample('t#bar{t}',ROOT.kRed+1,path_excl4252+'/ttbar/*nominal*.root',mcweight,'ttbar') ,     
         Sample('t#bar{t}+lf',ROOT.kRed-7,path_excl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)','ttbarOther',systs_all_samples+systs_ttbar+systs_tt_lf),
         Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,path_excl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==1)','ttbarPlusCCbar',systs_all_samples+systs_ttbar+systs_tt_cc),
         Sample('t#bar{t}+b',ROOT.kRed-2,path_excl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==1)','ttbarPlusB',systs_all_samples+systs_ttbar+systs_tt_b),
         Sample('t#bar{t}+2b',ROOT.kRed+2,path_excl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==2)','ttbarPlus2B',systs_all_samples+systs_ttbar+systs_tt_2b),
         Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,path_excl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==3)','ttbarPlusBBbar',systs_all_samples+systs_ttbar+systs_tt_bb),  
         Sample('Single Top',ROOT.kMagenta,path_excl4252+'/st*/*nominal*.root',mcweight,'SingleTop',systs_all_samples) , 
         Sample('V+jets',ROOT.kGreen-3,path_excl4252+'/??ets*/*nominal*.root',mcweight,'Vjets',systs_all_samples) , 
         Sample('t#bar{t}+V',ROOT.kBlue-10,path_excl4252+'/tt?_*/*nominal*.root',mcweight,'ttV',systs_all_samples),         
         Sample('Diboson',ROOT.kAzure+2,path_excl4252+'/??/*nominal*.root',mcweight,'Diboson',systs_all_samples) , 
#         Sample('QCD',ROOT.kYellow ,path_excl4252+'/QCD*/*nominal*root',mcweight,'QCD') , 
]

samplesBDTplotsBoosted=[Sample('t#bar{t}H',ROOT.kBlue+1,path_incl4252+'/ttH*/*nominal*.root',mcweight,'ttH') ,     
#         Sample('t#bar{t}',ROOT.kRed+1,path_incl4252+'/ttbar/*nominal*.root',mcweight,'ttbar') ,     
         Sample('t#bar{t}+lf',ROOT.kRed-7,path_incl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)','ttbarOther'),
         Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,path_incl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==1)','ttbarPlusCCbar'),
         Sample('t#bar{t}+b',ROOT.kRed-2,path_incl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==1)','ttbarPlusB'),
         Sample('t#bar{t}+2b',ROOT.kRed+2,path_incl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==2)','ttbarPlus2B'),
         Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,path_incl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==3)','ttbarPlusBBbar'),  
         Sample('Single Top',ROOT.kMagenta,path_incl4252+'/st*/*nominal*.root',mcweight,'SingleTop') , 
         Sample('V+jets',ROOT.kGreen-3,path_incl4252+'/??ets*/*nominal*.root',mcweight,'Vjets') , 
         Sample('t#bar{t}+V',ROOT.kBlue-10,path_incl4252+'/tt?_*/*nominal*.root',mcweight,'ttV'),         
         Sample('Diboson',ROOT.kAzure+2,path_incl4252+'/??/*nominal*.root',mcweight,'Diboson') , 
#         Sample('QCD',ROOT.kYellow ,path_incl4252+'/QCD*/*nominal*root',mcweight,'QCD') , 
]

#systweightsForSysTest=["1",
             #"Weight_CSVLFup","Weight_CSVLFdown","Weight_CSVHFup","Weight_CSVHFdown",
             #"Weight_CSVHFStats1up","Weight_CSVHFStats1down","Weight_CSVLFStats1up","Weight_CSVLFStats1down",
             #"Weight_CSVHFStats2up","Weight_CSVHFStats2down","Weight_CSVLFStats2up","Weight_CSVLFStats2down",
             #"Weight_CSVCErr1up","Weight_CSVCErr1down","Weight_CSVCErr2up","Weight_CSVCErr2down",
             #"rwtptup:=(2.0*(Weight_TopPt - 1.0)+1.0)","rwtptdown:=Weight_TopPt",
             #"Weight_pileupup:=((Weight_PU!=0.0) ? Weight_PUup/Weight_PU : Weight_PUup)","Weight_pileupdown:=((Weight_PU!=0.0) ? Weight_PUdown/Weight_PU : Weight_PUdown)",
             #"QScaleTTLFUp:=(Weight_muRupmuFup/"+str(mu_up_sf)+"*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)+1.0*(GenEvt_I_TTPlusCC!=0||GenEvt_I_TTPlusBB!=0))",
             #"QScaleTTLFDown:=(Weight_muRdownmuFdown/"+str(mu_down_sf)+"*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)+1.0*(GenEvt_I_TTPlusCC!=0||GenEvt_I_TTPlusBB!=0))",
             #"QScaleTTBUp:=(Weight_muRupmuFup/"+str(mu_up_sf)+"*(GenEvt_I_TTPlusBB==1)+1.0*(GenEvt_I_TTPlusBB!=1))",
             #"QScaleTTBDown:=(Weight_muRdownmuFdown/"+str(mu_down_sf)+"*(GenEvt_I_TTPlusBB==1)+1.0*(GenEvt_I_TTPlusBB!=1))",
             #"QScaleTTtwoBUp:=(Weight_muRupmuFup/"+str(mu_up_sf)+"*(GenEvt_I_TTPlusBB==2)+1.0*(GenEvt_I_TTPlusBB!=2))",
             #"QScaleTTtwoBDown:=(Weight_muRdownmuFdown/"+str(mu_down_sf)+"*(GenEvt_I_TTPlusBB==2)+1.0*(GenEvt_I_TTPlusBB!=2))",
             #"QScaleTTBBUp:=(Weight_muRupmuFup/"+str(mu_up_sf)+"*(GenEvt_I_TTPlusBB==3)+1.0*(GenEvt_I_TTPlusBB!=3))",
             #"QScaleTTBBDown:=(Weight_muRdownmuFdown/"+str(mu_down_sf)+"*(GenEvt_I_TTPlusBB==3)+1.0*(GenEvt_I_TTPlusBB!=3))",
             #"QScaleTTCCUp:=(Weight_muRupmuFup/"+str(mu_up_sf)+"*(GenEvt_I_TTPlusCC==1)+1.0*(GenEvt_I_TTPlusCC!=1))",
             #"QScaleTTCCDown:=(Weight_muRdownmuFdown/"+str(mu_down_sf)+"*(GenEvt_I_TTPlusCC==1)+1.0*(GenEvt_I_TTPlusCC!=1))",
             #"PDFweightUp:=Weight_NNPDFid260067/"+str(pdf_67_sf),"PDFWeightDown:=Weight_NNPDFid260005/"+str(pdf_05_sf),
             #]





