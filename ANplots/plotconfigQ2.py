import sys
import os
sys.path.insert(0, '../')
from scriptgenerator import *
from plotutils import *

mcweight='2.0*2.67*(Evt_Odd==0)*(N_Jets>=4 && N_BTagsM>=2)*((N_Jets==4 && N_BTagsM==3)||(N_Jets==4&&N_BTagsM==4)||(N_Jets==5&&N_BTagsM==3)||(N_Jets==5&&N_BTagsM>=4)||(N_Jets>=6&&N_BTagsM==2)||(N_Jets>=6&&N_BTagsM==3)||(N_Jets>=6&&N_BTagsM>=4)||(BoostedTopHiggs_TopHadCandidate_TopMVAOutput >= -0.485 && BoostedTopHiggs_HiggsCandidate_HiggsTag >= 0.8925))'
mcweightAll='2.67*(N_Jets>=4 && N_BTagsM>=2)*((N_Jets==4 && N_BTagsM==3)||(N_Jets==4&&N_BTagsM==4)||(N_Jets==5&&N_BTagsM==3)||(N_Jets==5&&N_BTagsM>=4)||(N_Jets>=6&&N_BTagsM==2)||(N_Jets>=6&&N_BTagsM==3)||(N_Jets>=6&&N_BTagsM>=4)||(BoostedTopHiggs_TopHadCandidate_TopMVAOutput >= -0.485 && BoostedTopHiggs_HiggsCandidate_HiggsTag >= 0.8925))'
#mcweightAll='2.67'
#mcweight='2.0*2.67'

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



path_76x="/nfs/dust/cms/user/kelmorab/Samples76x21022016"

# names of the systematics (proper names needed e.g. for combination)
weightsystnames=["",
                 "_CMS_ttH_Q2scale_ttbarOtherUp","_CMS_ttH_Q2scale_ttbarOtherDown",
                 "_CMS_ttH_Q2scale_ttbarPlusBUp","_CMS_ttH_Q2scale_ttbarPlusBDown",
                 "_CMS_ttH_Q2scale_ttbarPlus2BUp","_CMS_ttH_Q2scale_ttbarPlus2BDown",
                 "_CMS_ttH_Q2scale_ttbarPlusBBbarUp","_CMS_ttH_Q2scale_ttbarPlusBBbarDown",
                 "_CMS_ttH_Q2scale_ttbarPlusCCbarUp","_CMS_ttH_Q2scale_ttbarPlusCCbarDown",
           ]

systs_all_samples=["",
                   ]

systs_ttbar= []
systs_tt_lf=["_CMS_ttH_Q2scale_ttbarOtherUp","_CMS_ttH_Q2scale_ttbarOtherDown",]
systs_tt_b=["_CMS_ttH_Q2scale_ttbarPlusBUp","_CMS_ttH_Q2scale_ttbarPlusBDown"]
systs_tt_2b=[ "_CMS_ttH_Q2scale_ttbarPlus2BUp","_CMS_ttH_Q2scale_ttbarPlus2BDown"]
systs_tt_bb=[ "_CMS_ttH_Q2scale_ttbarPlusBBbarUp","_CMS_ttH_Q2scale_ttbarPlusBBbarDown"]
systs_tt_cc=[ "_CMS_ttH_Q2scale_ttbarPlusCCbarUp","_CMS_ttH_Q2scale_ttbarPlusCCbarDown"]



PSSystnames=[   "",
		            "","",
		            "","",
		            "","",
		            "","",
		            "","",
            ]

errorSystnames=[  "",
                  "_CMS_ttH_Q2scale_ttbarOtherUp","_CMS_ttH_Q2scale_ttbarOtherDown",
                  "_CMS_ttH_Q2scale_ttbarPlusBUp","_CMS_ttH_Q2scale_ttbarPlusBDown",
                  "_CMS_ttH_Q2scale_ttbarPlus2BUp","_CMS_ttH_Q2scale_ttbarPlus2BDown",
                  "_CMS_ttH_Q2scale_ttbarPlusBBbarUp","_CMS_ttH_Q2scale_ttbarPlusBBbarDown",
                  "_CMS_ttH_Q2scale_ttbarPlusCCbarUp","_CMS_ttH_Q2scale_ttbarPlusCCbarDown",
               ]


# corresponding weight names
mu_down_sf=1.1402
mu_up_sf=0.8727
pdf_05_sf=0.950964383883
pdf_67_sf=1.04093344845


## in future use Muon SF
muSF="muonIDHelper.GetSF(muonPt,muonEta,0)*muonIsoHelper.GetSF(muonPt,muonEta,0)*muonTriggerHelper.GetSF(muonPt,muonEta,0)"
#muSF="1.0"
#usualweights="(1*Weight_PU*TMath::Sign(1.0,Weight)*"+muSF+"*Weight_CSV)"
usualweights="(1*Weight_PU*TMath::Sign(1.0,Weight)*"+muSF+"*Weight_CSV)"


systweights=["NomWeight:="+usualweights+"*(DoWeights==1)+(DoWeights==0)*1.0",
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
             ]

assert len(systweights)==len(weightsystnames)

othersystnames=[]

othersystfilenames=[]

# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)

samples_data_controlplots=[Sample('SingleMu',ROOT.kBlack,path_76x+'/mu_*/*nominal*.root',sel_singlemu,'SingleMu'),
                           Sample('SingleEl',ROOT.kBlack,path_76x+'/el_*/*nominal*.root',sel_singleel,'SingleEl')
                       ]
                       
ttbarMCweight='*(0.000919641*(N_GenTopHad==1 && N_GenTopLep==1)+0.000707116*(N_GenTopLep==2 && N_GenTopHad==0)+0.0084896859*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS'
#ttbarMCweight='*0.0084896859/Weight_XS'

samplesControlPlots=[Sample('t#bar{t}H',ROOT.kBlue+1,path_76x+'/ttH*/*nominal*.root',mcweight,'ttH',systs_all_samples) ,     
                     Sample('t#bar{t}+lf',ROOT.kRed-7,path_76x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)'+ttbarMCweight,'ttbarOther',systs_all_samples+systs_ttbar+systs_tt_lf,0.05),
                     Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,path_76x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==1)'+ttbarMCweight,'ttbarPlusCCbar',systs_all_samples+systs_ttbar+systs_tt_cc,0.5),
                     Sample('t#bar{t}+b',ROOT.kRed-2,path_76x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==1)'+ttbarMCweight,'ttbarPlusB',systs_all_samples+systs_ttbar+systs_tt_b,0.5),
                     Sample('t#bar{t}+2b',ROOT.kRed+2,path_76x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==2)'+ttbarMCweight,'ttbarPlus2B',systs_all_samples+systs_ttbar+systs_tt_2b,0.5),
                     Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,path_76x+'/ttbar_????_*/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==3)'+ttbarMCweight,'ttbarPlusBBbar',systs_all_samples+systs_ttbar+systs_tt_bb,0.5),  
]
