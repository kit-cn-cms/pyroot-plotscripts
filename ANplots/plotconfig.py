import sys
import os
sys.path.insert(0, '../')
from scriptgenerator import *
from plotutils import *

mcweight='2.0*2.61*(Evt_Odd==0)'
sel_singleel="(N_LooseMuons==0)" # need to veto muon events in electron dataset to avoid double countung
sel_singlemu="(N_LooseElectrons==0)" # and vice versa...

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

samplesLimits=[       Sample('t#bar{t}H',ROOT.kBlue+1,path_excl4252+'/ttH*/*nominal*.root',mcweight,'ttH') ,  
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
samples_data_controlplots=[Sample('SingleMu',ROOT.kBlack,path_incl4252+'/mu_*/*nominal*.root',sel_singlemu,'SingleMu'),
                           Sample('SingleEl',ROOT.kBlack,path_incl4252+'/el_*/*nominal*.root',sel_singleel,'SingleEl')
                       ]
samples_data_bdtplots=[Sample('SingleMu',ROOT.kBlack,path_incl4252+'/mu_*/*nominal*.root',sel_singlemu,'SingleMu'),
                           Sample('SingleEl',ROOT.kBlack,path_incl4252+'/el_*/*nominal*.root',sel_singleel,'SingleEl')
                       ]
# mc samples
samplesControlPlots=[Sample('t#bar{t}H',ROOT.kBlue+1,path_incl4252+'/ttH*/*nominal*.root',mcweight,'ttH') ,     
#         Sample('t#bar{t}',ROOT.kRed+1,path_incl4252+'/ttbar/*nominal*.root',mcweight,'ttbar') ,     
         Sample('t#bar{t}+lf',ROOT.kRed-7,path_incl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)','ttl'),
         Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,path_incl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==1)','ttcc'),
         Sample('t#bar{t}+b',ROOT.kRed-2,path_incl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==1)','tt1b'),
         Sample('t#bar{t}+2b',ROOT.kRed+2,path_incl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==2)','tt2b'),
         Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,path_incl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==3)','ttbb'),  
         Sample('Single Top',ROOT.kMagenta,path_incl4252+'/st*/*nominal*.root',mcweight,'SingleTop') , 
         Sample('V+jets',ROOT.kGreen-3,path_incl4252+'/??ets*/*nominal*.root',mcweight,'Vjets') , 
         Sample('t#bar{t}+V',ROOT.kBlue-10,path_incl4252+'/tt?_*/*nominal*.root',mcweight,'ttV'),         
         Sample('Diboson',ROOT.kAzure+2,path_incl4252+'/??/*nominal*.root',mcweight,'Diboson') , 
#         Sample('QCD',ROOT.kYellow ,path_incl4252+'/QCD*/*nominal*root',mcweight,'QCD') , 
]

samplesBDTplots=[Sample('t#bar{t}H',ROOT.kBlue+1,path_excl4252+'/ttH*/*nominal*.root',mcweight,'ttH') ,     
#         Sample('t#bar{t}',ROOT.kRed+1,path_excl4252+'/ttbar/*nominal*.root',mcweight,'ttbar') ,     
         Sample('t#bar{t}+lf',ROOT.kRed-7,path_excl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)','ttl'),
         Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,path_excl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==1)','ttcc'),
         Sample('t#bar{t}+b',ROOT.kRed-2,path_excl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==1)','tt1b'),
         Sample('t#bar{t}+2b',ROOT.kRed+2,path_excl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==2)','tt2b'),
         Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,path_excl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==3)','ttbb'),  
         Sample('Single Top',ROOT.kMagenta,path_excl4252+'/st*/*nominal*.root',mcweight,'SingleTop') , 
         Sample('V+jets',ROOT.kGreen-3,path_excl4252+'/??ets*/*nominal*.root',mcweight,'Vjets') , 
         Sample('t#bar{t}+V',ROOT.kBlue-10,path_excl4252+'/tt?_*/*nominal*.root',mcweight,'ttV'),         
         Sample('Diboson',ROOT.kAzure+2,path_excl4252+'/??/*nominal*.root',mcweight,'Diboson') , 
#         Sample('QCD',ROOT.kYellow ,path_excl4252+'/QCD*/*nominal*root',mcweight,'QCD') , 
]

samplesBDTplotsBoosted=[Sample('t#bar{t}H',ROOT.kBlue+1,path_incl4252+'/ttH*/*nominal*.root',mcweight,'ttH') ,     
#         Sample('t#bar{t}',ROOT.kRed+1,path_incl4252+'/ttbar/*nominal*.root',mcweight,'ttbar') ,     
         Sample('t#bar{t}+lf',ROOT.kRed-7,path_incl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)','ttl'),
         Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,path_incl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==1)','ttcc'),
         Sample('t#bar{t}+b',ROOT.kRed-2,path_incl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==1)','tt1b'),
         Sample('t#bar{t}+2b',ROOT.kRed+2,path_incl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==2)','tt2b'),
         Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,path_incl4252+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==3)','ttbb'),  
         Sample('Single Top',ROOT.kMagenta,path_incl4252+'/st*/*nominal*.root',mcweight,'SingleTop') , 
         Sample('V+jets',ROOT.kGreen-3,path_incl4252+'/??ets*/*nominal*.root',mcweight,'Vjets') , 
         Sample('t#bar{t}+V',ROOT.kBlue-10,path_incl4252+'/tt?_*/*nominal*.root',mcweight,'ttV'),         
         Sample('Diboson',ROOT.kAzure+2,path_incl4252+'/??/*nominal*.root',mcweight,'Diboson') , 
#         Sample('QCD',ROOT.kYellow ,path_incl4252+'/QCD*/*nominal*root',mcweight,'QCD') , 
]

# names of the systematics (proper names needed e.g. for combination)
weightsystnames=["",
           "_CMS_ttH_CSVLFUp","_CMS_ttH_CSVLFDown","_CMS_ttH_CSVHFUp","_CMS_ttH_CSVHFDown",
           "_CMS_ttH_CSVHFStats1Up","_CMS_ttH_CSVHFStats1Down","_CMS_ttH_CSVLFStats1Up","_CMS_ttH_CSVLFStats1Down",
           "_CMS_ttH_CSVHFStats2Up","_CMS_ttH_CSVHFStats2Down","_CMS_ttH_CSVLFStats2Up","_CMS_ttH_CSVLFStats2Down",
           "_CMS_ttH_CSVCErr1Up","_CMS_ttH_CSVCErr1Down","_CMS_ttH_CSVCErr2Up","_CMS_ttH_CSVCErr2Down",
           "_CMS_ttH_Q2scale_ttbarOtherUp","_CMS_ttH_Q2scale_ttbarPlusBUp","_CMS_ttH_Q2scale_ttbarPlus2BUp","_CMS_ttH_Q2scale_ttbarPlusBBbarUp","_CMS_ttH_Q2scale_ttbarPlusCCbarUp",
           "_CMS_ttH_Q2scale_ttbarOtherDown","_CMS_ttH_Q2scale_ttbarPlusBDown","_CMS_ttH_Q2scale_ttbarPlus2BDown","_CMS_ttH_Q2scale_ttbarPlusBBbarDown","_CMS_ttH_Q2scale_ttbarPlusCCbarDown",
           "_CMS_ttH_NNPDFUp","_CMS_ttH_NNPDFDown"
           ]

# corresponding weight names
pdfweightscalefactor=1.0


systweights=["1",
             "Weight_CSVLFup","Weight_CSVLFdown","Weight_CSVHFup","Weight_CSVHFdown",
             "Weight_CSVHFStats1up","Weight_CSVHFStats1down","Weight_CSVLFStats1up","Weight_CSVLFStats1down",
             "Weight_CSVHFStats2up","Weight_CSVHFStats2down","Weight_CSVLFStats2up","Weight_CSVLFStats2down",
             "Weight_CSVCErr1up","Weight_CSVCErr1down","Weight_CSVCErr2up","Weight_CSVCErr2down",
             "QScaleTTLFUp:=Weight_muRupmuFup/"+str(pdfweightscalefactor),"QScaleTTBUp:=Weight_muRupmuFup/"+str(pdfweightscalefactor),"QScaleTTtwoBUp:=Weight_muRupmuFup/"+str(pdfweightscalefactor),"QScaleTTBBUp:=Weight_muRupmuFup/"+str(pdfweightscalefactor),"QScaleTTCCUp:=Weight_muRupmuFup/"+str(pdfweightscalefactor),
             "QScaleTTLFDown:=Weight_muRdownmuFdown/"+str(pdfweightscalefactor),"QScaleTTBDown:=Weight_muRdownmuFdown/"+str(pdfweightscalefactor),"QScaleTTtwoBDown:=Weight_muRdownmuFdown/"+str(pdfweightscalefactor),"QScaleTTBBDown:=Weight_muRdownmuFdown/"+str(pdfweightscalefactor),"QScaleTTCCDown:=Weight_muRdownmuFdown/"+str(pdfweightscalefactor),
             "PDFweightUp:=Weight_NNPDFid260067/"+str(pdfweightscalefactor),"PDFWeightDown:=Weight_NNPDFid260005/"+str(pdfweightscalefactor)
             ]

othersystnames=["_CMS_scale_jUp",
                "_CMS_scale_jDown",
#                "_CMS_res_jUp",
#                "_CMS_res_jDown"
                ]

othersystfilenames=["JESUP",
                    "JESDOWN",
#                    "JERUP",
#                    "JERDOWN"
                    ]





