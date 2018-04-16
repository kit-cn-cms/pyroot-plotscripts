import sys
import os
sys.path.append('pyroot-plotscripts-base')
sys.path.append('pyroot-plotscripts-base/limittools')

from scriptgenerator import *
from plotutils import *

btagString='N_BTagsM'

sel_singleel="(N_LooseMuons==0 && N_TightElectrons==1 )*(1.0)" # need to veto muon events in electron dataset to avoid double countung
sel_singlemu="(N_LooseElectrons==0 && (N_TightMuons==1))*(1.0)" # and vice versa...
#sel_MET="*(Evt_Pt_MET>20.)"
sel_MET="*(Evt_Pt_MET>20.)"

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
weightSystNames=[
                    "",
                   #"_CMS_btag_lfUp","_CMS_btag_lfDown","_CMS_btag_hfUp","_CMS_btag_hfDown",
                   #"_CMS_btag_hfstats1Up","_CMS_btag_hfstats1Down","_CMS_btag_lfstats1Up","_CMS_btag_lfstats1Down",
                   #"_CMS_btag_hfstats2Up","_CMS_btag_hfstats2Down","_CMS_btag_lfstats2Up","_CMS_btag_lfstats2Down",
                   #"_CMS_btag_cferr1Up","_CMS_btag_cferr1Down","_CMS_btag_cferr2Up","_CMS_btag_cferr2Down",
]

systsAllSamples=[
                    "",
                   #"_CMS_btag_lfUp","_CMS_btag_lfDown","_CMS_btag_hfUp","_CMS_btag_hfDown",
                   #"_CMS_btag_hfstats1Up","_CMS_btag_hfstats1Down","_CMS_btag_lfstats1Up","_CMS_btag_lfstats1Down",
                   #"_CMS_btag_hfstats2Up","_CMS_btag_hfstats2Down","_CMS_btag_lfstats2Up","_CMS_btag_lfstats2Down",
                   #"_CMS_btag_cferr1Up","_CMS_btag_cferr1Down","_CMS_btag_cferr2Up","_CMS_btag_cferr2Down",
]

systsTtbar= [

]

systs_tt_lf=[]
systs_tt_b=[]
systs_tt_2b=[]
systs_tt_bb=[]
systs_tt_cc=[]



mcWeightAll='41.0'
mcWeight='41.0*2.0'


#mcTriggerWeight='((1.0)*(internalEleTriggerWeight*internalMuTriggerWeight)*((N_TightElectrons==1 && Triggered_HLT_Ele27_eta2p1_WPTight_Gsf_vX==1)||(N_TightMuons==1 && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))))'
mcTriggerWeight='1.0'
#sfs="internalEleIDWeight*internalMuIDWeight*internalMuIsoWeight*internalEleGFSWeight*internalMuHIPWeight"
sfs="1.0"
#usualWeights="(1*Weight_pu69p2*((Weight>0)-(Weight<0)))"+"*"+sfs
usualWeights="(1*((Weight>0)-(Weight<0)))"+"*"+sfs

evenSel="*(Evt_Odd==0)"


#ttbarMCWeight='*((N_BTagsM>=4)*((0.000919641*(N_GenTopHad==1 && N_GenTopLep==1)+0.0009753747*(N_GenTopLep==2 && N_GenTopHad==0)+0.0084896859*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS)+(0.0084896859/Weight_XS)*(N_BTagsM<4))'
#ttbarMCWeight='*0.0084896859/Weight_XS'

systWeights=[
                    #"NomWeight:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*(DoWeights==1)+(DoWeights==0)*1.0",
                    "NomWeight:="+usualWeights+"*"+mcTriggerWeight+"*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVLFup:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVLFUp*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVLFdown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVLFDown*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVHFup:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVHFUp*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVHFdown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVHFDown*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVHFStats1up:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVHFStats1Up*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVHFStats1down:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVHFStats1Down*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVLFStats1up:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVLFStats1Up*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVLFStats1down:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVLFStats1Down*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVHFStats2up:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVHFStats2Up*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVHFStats2down:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVHFStats2Down*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVLFStats2up:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVLFStats2Up*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVLFStats2down:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVLFStats2Down*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVCErr1up:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVCErr1Up*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVCErr1down:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVCErr1Down*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVCErr2up:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVCErr2Up*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVCErr2down:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVCErr2Down*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                  
]



Q2SystWeights= [
]

Q2SystNames= [

]

PDFSystWeights= [
]

PDFSystNames= [
]

systs_tt_all=[]
systs_tt_all_weights=[
                    ]



systs_tt_lf=[]
systs_tt_lf_weights=[
                    ]
systs_tt_b=[]
systs_tt_b_weights=[
                    ]
systs_tt_2b=[]
systs_tt_2b_weights=[
                ]
systs_tt_bb=[]
systs_tt_bb_weights=[
                ]
systs_tt_cc=[]
systs_tt_cc_weights=[
                    ]

systWeights+=Q2SystWeights+PDFSystWeights+systs_tt_all_weights+systs_tt_lf_weights+systs_tt_b_weights+systs_tt_2b_weights+systs_tt_bb_weights+systs_tt_cc_weights
weightSystNames+=Q2SystNames+PDFSystNames+systs_tt_all+systs_tt_lf+systs_tt_b+systs_tt_2b+systs_tt_bb+systs_tt_cc


assert len(systWeights)==len(weightSystNames)

otherSystNames=[
]

otherSystFileNames=[
]

PSSystNames=[
]
PSSystFileNames=[
]

QCDSystNames=[
  ]
QCDSystReplacementStrings=[
  ]

errorSystNamesNoPS=[
                    "",
                   #"_CMS_btag_lfUp","_CMS_btag_lfDown","_CMS_btag_hfUp","_CMS_btag_hfDown",
                   #"_CMS_btag_hfstats1Up","_CMS_btag_hfstats1Down","_CMS_btag_lfstats1Up","_CMS_btag_lfstats1Down",
                   #"_CMS_btag_hfstats2Up","_CMS_btag_hfstats2Down","_CMS_btag_lfstats2Up","_CMS_btag_lfstats2Down",
                   #"_CMS_btag_cferr1Up","_CMS_btag_cferr1Down","_CMS_btag_cferr2Up","_CMS_btag_cferr2Down",
]+systs_tt_all


#assert len(errorSystNames)==len(weightSystNames+otherSystNames+PSSystNames+QCDSystNames)

# samples
# input path 
path_lea="/nfs/dust/cms/user/lreuter/ntuples/BDTnewntuples"

doReadInTrees=True
# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
sampleDict=SampleDictionary()
sampleDict.doPrintout()

# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
samplesDataControlPlots=[
                    Sample('SingleMu',ROOT.kBlack,path_lea+'/SingleMuon*/*nominal*.root',sel_singlemu+sel_MET,'SingleMu',samDict=sampleDict, readTrees=doReadInTrees),
                    Sample('SingleEl',ROOT.kBlack,path_lea+'/SingleElectron*/*nominal*.root',sel_singleel+sel_MET,'SingleEl',samDict=sampleDict, readTrees=doReadInTrees)
]

## DANGERZONE 
# Recheck these numbers !!!
# Use incl and SL samples together
# SL sample has nominally 152720952  events
# After skims but before ntupling at least 4 SL files are missing with events 235523/58319342 = 0.004038506 -> 0.995961494
# incl sample has 77229341 events
# branching for Single lepton = 43.8 (pdg) -> nSL = 77229341*0.438 + 152720952*0.995961494
# the total number of SL events in both samples is 185930638.8770223 . This also included the fact that 3 MiniAOD files are missing
# the ttbar DL sample has a total of 79092400 events
# branching dfraction is 10.5% 
# ttbarDL + BF*ttbar_incl = 79092400 + 0.105*77229341 = 87201480.805
# Now Calculate new XS weights to mix the samples together
# incl ttbar XS = 831.76
# SL ttbar XS = 831.76*0.438 = 364.31088
# => weight had  831.76*1000/77229341 = 0.01077
# => weight DL 831.76*0.105*1000/87201480.805 = 0.001001529
# => weight SL = 364.31088*1000/185930638.8770223 = 0.00195939

#ttbarMCWeight='*((0.001958064*(N_GenTopHad==1 && N_GenTopLep==1)+0.001001529*(N_GenTopLep==2 && N_GenTopHad==0)+0.01077*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS)'


# Now for the ttbb sherpa sample:
# the weighted number of events here is 20.924893208852154 with >=4j >=2t und ttbb definition without the GenValue
# the weighted number of events here is 3675937.4093933105 with >=4j >=2t und ttbb definition with the GenValue
# the number in powheg = 10897.337975859642 for 35.918 fb
# to get the same yield we have to multiply the ttbb sherpa weights with 10897.337975859642/35.918/20.924893208852154 = 14.499232841620643
# and 
# 10897.337975859642/35.918/3675937.4093933105 = 8.253538214386172e-05
#specialSherpaWeight='*14.49923'
#specialSherpaWeightWithGenValue='*0.000082535*abs(Weight_GenValue)'

#DANGERZONE
# need also to correct for the pos/neg fraction of ttH
# ttHbb:
# nGen=3845992
# xs=0.2953
# weight_noposneg = xs*1000/nGen = 7.67812309542e-05
# Having negative and positive events changes the weight calculation to
# weight_posneg = (xs*1000/nGen = 7.67812309542e-05)/((pos-neg)/total)
# But we only have the ratio of r=neg/pos at this moment
# => corrFactor=1.0/((pos-r*pos)/total)
# and with total=pos+neg = pos+r*pos 
# follows corrFactor =1.0/( (1+r)/(1-r) )
# => weight_new=corrFactor*weight_old
# With a r=neg/pos=0.010039594265217715
#corrFactor_posneg_ttHbb = "*((abs(GenHiggs_DecProd1_PDGID)==5 && abs(GenHiggs_DecProd2_PDGID)==5)*1.02028 + 1.0*(!(abs(GenHiggs_DecProd1_PDGID)==5 && abs(GenHiggs_DecProd2_PDGID)==5)))"

# and for ttHnonbb
#corrFactor_posneg_ttHnonbb ="*((abs(GenHiggs_DecProd1_PDGID)==5 && abs(GenHiggs_DecProd2_PDGID)==5)*1.0 + 1.02166*(!(abs(GenHiggs_DecProd1_PDGID)==5 && abs(GenHiggs_DecProd2_PDGID)==5)))"

# correction factors to take even/odd splitting into account 
#evenWeight_ttH = "*((N_Jets>=6&&N_BTagsM==2)*1.00259034198 + (N_Jets==4&&N_BTagsM==3)*0.993218447691 + (N_Jets==5&&N_BTagsM==3)*1.00531861013 + (N_Jets>=6&&N_BTagsM==3)*0.99788182971 + (N_Jets==4&&N_BTagsM>=4)*0.995369893223 + (N_Jets==5&&N_BTagsM>=4)*0.996719815245 + (N_Jets>=6&&N_BTagsM>=4)*1.00269083017 + 1.0*(N_Jets==4 && N_BTagsM==2) + 1.0*(N_Jets==5 && N_BTagsM==2))"
#evenWeight_ttH_hbb = "*((N_Jets>=6&&N_BTagsM==2)*1.00401305677 + (N_Jets==4&&N_BTagsM==3)*0.992461831261 + (N_Jets==5&&N_BTagsM==3)*1.00665379522 + (N_Jets>=6&&N_BTagsM==3)*0.999294824768 + (N_Jets==4&&N_BTagsM>=4)*0.994934728544 + (N_Jets==5&&N_BTagsM>=4)*0.995972029483 + (N_Jets>=6&&N_BTagsM>=4)*1.00386335248 + 1.0*(N_Jets==4 && N_BTagsM==2) + 1.0*(N_Jets==5 && N_BTagsM==2))"
#evenWeight_ttH_hcc = "*((N_Jets>=6&&N_BTagsM==2)*1.02933684902 + (N_Jets==4&&N_BTagsM==3)*0.969233705254 + (N_Jets==5&&N_BTagsM==3)*1.07442421713 + (N_Jets>=6&&N_BTagsM==3)*0.939579319546 + (N_Jets==4&&N_BTagsM>=4)*1.44559873446 + (N_Jets==5&&N_BTagsM>=4)*0.93259195499 + (N_Jets>=6&&N_BTagsM>=4)*0.988910117375 + 1.0*(N_Jets==4 && N_BTagsM==2) + 1.0*(N_Jets==5 && N_BTagsM==2))"
#evenWeight_ttH_hww = "*((N_Jets>=6&&N_BTagsM==2)*1.0072749693 + (N_Jets==4&&N_BTagsM==3)*1.01913462971 + (N_Jets==5&&N_BTagsM==3)*1.00246353815 + (N_Jets>=6&&N_BTagsM==3)*0.995483524925 + (N_Jets==4&&N_BTagsM>=4)*1.13175517892 + (N_Jets==5&&N_BTagsM>=4)*1.05318209121 + (N_Jets>=6&&N_BTagsM>=4)*0.976690141824 + 1.0*(N_Jets==4 && N_BTagsM==2) + 1.0*(N_Jets==5 && N_BTagsM==2))"
#evenWeight_ttH_hzz = "*((N_Jets>=6&&N_BTagsM==2)*0.96154443077 + (N_Jets==4&&N_BTagsM==3)*0.979948488426 + (N_Jets==5&&N_BTagsM==3)*0.918107925149 + (N_Jets>=6&&N_BTagsM==3)*1.00294817123 + (N_Jets==4&&N_BTagsM>=4)*1.18893936333 + (N_Jets==5&&N_BTagsM>=4)*0.971677675169 + (N_Jets>=6&&N_BTagsM>=4)*1.11350611091 + 1.0*(N_Jets==4 && N_BTagsM==2) + 1.0*(N_Jets==5 && N_BTagsM==2))"
#evenWeight_ttH_htt = "*((N_Jets>=6&&N_BTagsM==2)*0.98931520386 + (N_Jets==4&&N_BTagsM==3)*1.04376582688 + (N_Jets==5&&N_BTagsM==3)*0.967505946821 + (N_Jets>=6&&N_BTagsM==3)*0.982411625155 + (N_Jets==4&&N_BTagsM>=4)*0.692924564086 + (N_Jets==5&&N_BTagsM>=4)*1.18728634504 + (N_Jets>=6&&N_BTagsM>=4)*0.84891962106 + 1.0*(N_Jets==4 && N_BTagsM==2) + 1.0*(N_Jets==5 && N_BTagsM==2))"
#evenWeight_ttH_hgg = "*((N_Jets>=6&&N_BTagsM==2)*0.977549831446 + (N_Jets==4&&N_BTagsM==3)*1.38639077739 + (N_Jets==5&&N_BTagsM==3)*1.17250328444 + (N_Jets>=6&&N_BTagsM==3)*1.90302173909 + (N_Jets>=6&&N_BTagsM>=4)*0.501357836064 + 1.0*(N_Jets==4 && N_BTagsM==2) + 1.0*(N_Jets==5 && N_BTagsM==2))"
#evenWeight_ttH_hgluglu = "*((N_Jets>=6&&N_BTagsM==2)*0.995675201646 + (N_Jets==4&&N_BTagsM==3)*0.932422744087 + (N_Jets==5&&N_BTagsM==3)*0.984314909964 + (N_Jets>=6&&N_BTagsM==3)*0.999811574701 + (N_Jets==4&&N_BTagsM>=4)*0.759757163734 + (N_Jets==5&&N_BTagsM>=4)*1.0767902998 + (N_Jets>=6&&N_BTagsM>=4)*1.06001906365 + 1.0*(N_Jets==4 && N_BTagsM==2) + 1.0*(N_Jets==5 && N_BTagsM==2))"
#evenWeight_ttH_hzg = "*((N_Jets>=6&&N_BTagsM==2)*0.955776288592 + (N_Jets==4&&N_BTagsM==3)*1.28839073053 + (N_Jets==5&&N_BTagsM==3)*1.15772752057 + (N_Jets>=6&&N_BTagsM==3)*0.911383632984 + (N_Jets==4&&N_BTagsM>=4)*0.767450585102 + (N_Jets>=6&&N_BTagsM>=4)*0.914383605909 + 1.0*(N_Jets==4 && N_BTagsM==2) + 1.0*(N_Jets==5 && N_BTagsM==2))"
#evenWeight_ttbarOther = "*((N_Jets>=6&&N_BTagsM==2)*1.00034485799 + (N_Jets==4&&N_BTagsM==3)*0.999721880196 + (N_Jets==5&&N_BTagsM==3)*1.00245164082 + (N_Jets>=6&&N_BTagsM==3)*0.992863302453 + (N_Jets==4&&N_BTagsM>=4)*0.980003485631 + (N_Jets==5&&N_BTagsM>=4)*1.02109352629 + (N_Jets>=6&&N_BTagsM>=4)*0.980264790403 + 1.0*(N_Jets==4 && N_BTagsM==2) + 1.0*(N_Jets==5 && N_BTagsM==2))"
#evenWeight_ttbarPlusB = "*((N_Jets>=6&&N_BTagsM==2)*0.998657571164 + (N_Jets==4&&N_BTagsM==3)*1.00234957317 + (N_Jets==5&&N_BTagsM==3)*1.01189419133 + (N_Jets>=6&&N_BTagsM==3)*0.990403631007 + (N_Jets==4&&N_BTagsM>=4)*1.03391421004 + (N_Jets==5&&N_BTagsM>=4)*0.988297188392 + (N_Jets>=6&&N_BTagsM>=4)*1.02629639163 + 1.0*(N_Jets==4 && N_BTagsM==2) + 1.0*(N_Jets==5 && N_BTagsM==2))"
#evenWeight_ttbarPlus2B = "*((N_Jets>=6&&N_BTagsM==2)*1.0011011967 + (N_Jets==4&&N_BTagsM==3)*0.998672303154 + (N_Jets==5&&N_BTagsM==3)*1.00005381083 + (N_Jets>=6&&N_BTagsM==3)*1.00790722387 + (N_Jets==4&&N_BTagsM>=4)*1.05014046552 + (N_Jets==5&&N_BTagsM>=4)*1.00503439176 + (N_Jets>=6&&N_BTagsM>=4)*1.02482458405 + 1.0*(N_Jets==4 && N_BTagsM==2) + 1.0*(N_Jets==5 && N_BTagsM==2))"
#evenWeight_ttbarPlusBBbar = "*((N_Jets>=6&&N_BTagsM==2)*0.997740414419 + (N_Jets==4&&N_BTagsM==3)*0.996447054425 + (N_Jets==5&&N_BTagsM==3)*0.999155544707 + (N_Jets>=6&&N_BTagsM==3)*0.998067271837 + (N_Jets==4&&N_BTagsM>=4)*1.01253849135 + (N_Jets==5&&N_BTagsM>=4)*0.991172816531 + (N_Jets>=6&&N_BTagsM>=4)*1.00226402447 + 1.0*(N_Jets==4 && N_BTagsM==2) + 1.0*(N_Jets==5 && N_BTagsM==2))"
#evenWeight_ttbarPlusCCbar = "*((N_Jets>=6&&N_BTagsM==2)*1.00111281833 + (N_Jets==4&&N_BTagsM==3)*1.00212184704 + (N_Jets==5&&N_BTagsM==3)*0.999470938958 + (N_Jets>=6&&N_BTagsM==3)*1.00454308971 + (N_Jets==4&&N_BTagsM>=4)*1.01824667 + (N_Jets==5&&N_BTagsM>=4)*1.02429204075 + (N_Jets>=6&&N_BTagsM>=4)*0.992977729595 + 1.0*(N_Jets==4 && N_BTagsM==2) + 1.0*(N_Jets==5 && N_BTagsM==2))"


print "controlsamples"
samplesControlPlots=[
                    Sample('t#bar{t}H',ROOT.kBlue+1,path_lea+'/ttH*/*nominal*.root',mcWeightAll+sel_MET,'ttH',systsAllSamples,samDict=sampleDict, readTrees=doReadInTrees) ,     
#                    Sample('t#bar{t}',ROOT.kRed+1,path_80x+'/ttbar/*nominal*.root',mcWeight,'ttbar',systsAllSamples) ,     
                    Sample('t#bar{t}+lf',ROOT.kRed-7,path_lea+'/TTTo*/*nominal*.root',mcWeightAll+sel_MET+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)','ttbarOther',systsAllSamples+systsTtbar+systs_tt_lf,samDict=sampleDict, readTrees=doReadInTrees),
                    Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,path_lea+'/TTTo*/*nominal*.root',mcWeightAll+sel_MET+'*(GenEvt_I_TTPlusCC==1)','ttbarPlusCCbar',systsAllSamples+systsTtbar+systs_tt_cc,samDict=sampleDict, readTrees=doReadInTrees),
                    Sample('t#bar{t}+b',ROOT.kRed-2,path_lea+'/TTTo*/*nominal*.root',mcWeightAll+sel_MET+'*(GenEvt_I_TTPlusBB==1)','ttbarPlusB',systsAllSamples+systsTtbar+systs_tt_b,samDict=sampleDict, readTrees=doReadInTrees),
                    Sample('t#bar{t}+2b',ROOT.kRed+2,path_lea+'/TTTo*/*nominal*.root',mcWeightAll+sel_MET+'*(GenEvt_I_TTPlusBB==2)','ttbarPlus2B',systsAllSamples+systsTtbar+systs_tt_2b,samDict=sampleDict, readTrees=doReadInTrees),
                    Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,path_lea+'/TTTo*/*nominal*.root',mcWeightAll+sel_MET+'*(GenEvt_I_TTPlusBB==3)','ttbarPlusBBbar',systsAllSamples+systsTtbar+systs_tt_bb,samDict=sampleDict, readTrees=doReadInTrees),  
                    #Sample('Single Top',ROOT.kMagenta,path_lea+'/st*/*nominal*.root',mcWeightAll+sel_MET,'SingleTop',systsAllSamples,samDict=sampleDict, readTrees=doReadInTrees) , 
                    #Sample('V+jets',ROOT.kGreen-3,path_lea+'/*ets*/*nominal*.root',mcWeightAll+sel_MET,'Vjets',systsAllSamples,samDict=sampleDict, readTrees=doReadInTrees) , 
                    #Sample('t#bar{t}+V',ROOT.kBlue-10,path_lea+'/tt?_*/*nominal*.root',mcWeightAll+sel_MET,'ttV',systsAllSamples,samDict=sampleDict, readTrees=doReadInTrees),         
                    #Sample('Diboson',ROOT.kAzure+2,path_lea+'/??_pythia_*/*nominal*.root',mcWeightAll+sel_MET,'diboson',systsAllSamples,samDict=sampleDict, readTrees=doReadInTrees) , 
                    #Sample('QCD',ROOT.kYellow,iso_inverted_paths,'1.'+sel_MET+'*internalQCDweight'+'*(((Weight_XS==1.0)*1.0*((electron_data*'+sel_singleel+')+(muon_data*'+sel_singlemu+')))+((Weight_XS!=1.0)*(-1.0)*35.91823))','QCD',[systsAllSamples[0]]+QCDSystNames,samDict=sampleDict, readTrees=doReadInTrees),  
]

#print "limit samples"
samplesLimits=[
                    Sample('t#bar{t}H',ROOT.kBlue+1,path_lea+'/ttH*/*nominal*.root',mcWeight+evenSel+sel_MET,'ttH',systsAllSamples,samDict=sampleDict, readTrees=doReadInTrees) ,     
#                    Sample('t#bar{t}',ROOT.kRed+1,path_80x+'/ttbar/*nominal*.root',mcWeight+evenSel,'ttbar',samDict=sampleDict, readTrees=doReadInTrees) ,     
                    #Sample('t#bar{t}H, H to b#bar{b}',ROOT.kBlue+1,path_lea+'/ttHTobb*/*nominal*.root','1.0*'+mcWeight+evenSel+sel_MET,'ttH_hbb',systsAllSamples,samDict=sampleDict, readTrees=doReadInTrees) ,  
                    #Sample('t#bar{t}H, H to c#bar{c}',ROOT.kBlue+1,path_lea+'/ttHToNonbb*/*nominal*.root','1.0*'+mcWeightAll+hccSel+sel_MET,'ttH_hcc',systsAllSamples,samDict=sampleDict, readTrees=doReadInTrees) ,  
                    #Sample('t#bar{t}H, H to #tau#tau',ROOT.kBlue+1,path_lea+'/ttHToNonbb*/*nominal*.root','1.0*'+mcWeightAll+httSel+sel_MET,'ttH_htt',systsAllSamples,samDict=sampleDict, readTrees=doReadInTrees) ,  
                    #Sample('t#bar{t}H, H to #gamma#gamma',ROOT.kBlue+1,path_lea+'/ttHToNonbb*/*nominal*.root','1.0*'+mcWeightAll+hggSel+sel_MET,'ttH_hgg',systsAllSamples,samDict=sampleDict, readTrees=doReadInTrees) ,  
                    #Sample('t#bar{t}H, H to gluglu',ROOT.kBlue+1,path_lea+'/ttHToNonbb*/*nominal*.root','1.0*'+mcWeightAll+hglugluSel+sel_MET,'ttH_hgluglu',systsAllSamples,samDict=sampleDict, readTrees=doReadInTrees) ,  
                    #Sample('t#bar{t}H, H to WW',ROOT.kBlue+1,path_lea+'/ttHToNonbb*/*nominal*.root','1.0*'+mcWeightAll+hwwSel+sel_MET,'ttH_hww',systsAllSamples,samDict=sampleDict, readTrees=doReadInTrees) ,  
                    #Sample('t#bar{t}H, H to ZZ',ROOT.kBlue+1,path_lea+'/ttHToNonbb*/*nominal*.root','1.0*'+mcWeightAll+hzzSel+sel_MET,'ttH_hzz',systsAllSamples,samDict=sampleDict, readTrees=doReadInTrees) ,  
                    #Sample('t#bar{t}H, H to #gamma Z',ROOT.kBlue+1,path_lea+'/ttHToNonbb*/*nominal*.root','1.0*'+mcWeightAll+hzgSel+sel_MET,'ttH_hzg',systsAllSamples,samDict=sampleDict, readTrees=doReadInTrees) ,
                    
                    Sample('t#bar{t}+lf',ROOT.kRed-7,path_lea+'/TTTo*/*nominal*.root',mcWeight+evenSel+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)'+sel_MET,'ttbarOther',systsAllSamples+systsTtbar+systs_tt_lf,samDict=sampleDict, readTrees=doReadInTrees),
                    Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,path_lea+'/TTTo*/*nominal*.root',mcWeight+evenSel+'*(GenEvt_I_TTPlusCC==1)'+sel_MET,'ttbarPlusCCbar',systsAllSamples+systsTtbar+systs_tt_cc,samDict=sampleDict, readTrees=doReadInTrees),
                    Sample('t#bar{t}+b',ROOT.kRed-2,path_lea+'/TTTo*/*nominal*.root',mcWeight+evenSel+'*(GenEvt_I_TTPlusBB==1)'+sel_MET,'ttbarPlusB',systsAllSamples+systsTtbar+systs_tt_b,samDict=sampleDict, readTrees=doReadInTrees),
                    Sample('t#bar{t}+2b',ROOT.kRed+2,path_lea+'/TTTo*/*nominal*.root',mcWeight+evenSel+'*(GenEvt_I_TTPlusBB==2)'+sel_MET,'ttbarPlus2B',systsAllSamples+systsTtbar+systs_tt_2b,samDict=sampleDict, readTrees=doReadInTrees),
                    Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,path_lea+'/TTTo*/*nominal*.root',mcWeight+evenSel+'*(GenEvt_I_TTPlusBB==3)'+sel_MET,'ttbarPlusBBbar',systsAllSamples+systsTtbar+systs_tt_bb,samDict=sampleDict, readTrees=doReadInTrees), 
                    #Sample('Single Top',ROOT.kMagenta,path_lea+'/st*/*nominal*.root',mcWeightAll+sel_MET,'singlet',systsAllSamples,samDict=sampleDict, readTrees=doReadInTrees) , 
                    #Sample('Z+jets',ROOT.kGreen-3,path_lea+'/Zjets*/*nominal*.root',mcWeightAll+sel_MET,'zjets',systsAllSamples,samDict=sampleDict, readTrees=doReadInTrees) , 
                    #Sample('W+jets',ROOT.kGreen-7,path_lea+'/Wjets*/*nominal*.root',mcWeightAll+sel_MET,'wjets',systsAllSamples,samDict=sampleDict, readTrees=doReadInTrees) , 
                    #Sample('t#bar{t}+W',ROOT.kBlue-10,path_lea+'/ttW_*/*nominal*.root',mcWeightAll+sel_MET,'ttbarW',systsAllSamples,samDict=sampleDict, readTrees=doReadInTrees),
                    #Sample('t#bar{t}+Z',ROOT.kBlue-6,path_lea+'/ttZ_*/*nominal*.root',mcWeightAll+sel_MET,'ttbarZ',systsAllSamples,samDict=sampleDict, readTrees=doReadInTrees),
                    #Sample('Diboson',ROOT.kAzure+2,path_lea+'/??_pythia_*/*nominal*.root',mcWeightAll+sel_MET,'diboson',systsAllSamples,samDict=sampleDict, readTrees=doReadInTrees) , 
                    #Sample('QCD',ROOT.kYellow,iso_inverted_paths,'1.'+sel_MET+'*internalQCDweight'+'*(((Weight_XS==1.0)*1.0*((electron_data*'+sel_singleel+')+(muon_data*'+sel_singlemu+')))+((Weight_XS!=1.0)*(-1.0)*35.91823))','QCD',[systsAllSamples[0]]+QCDSystNames,samDict=sampleDict, readTrees=doReadInTrees),  
]
