import sys
import os
from scriptgenerator import *
from plotutils import *

weigthsystnamesMCSFs=[
                    '',
                    '_ABCD1_nominal',
                    '_ABCD2_nominal',
                    '_ABCD3_nominal',
                    '_ABCD4_nominal',
                    '_ABCD5_nominal',
                    '_ABCD6_nominal',
                    '_ABCD7_nominal',
                    '_ABCD8_nominal',
                    '_ABCD9_nominal',
                    '_ABCD10_nominal',
                    
    ]

systweightnamesMCSFs=[
                    "_nom:=triggered",
                    "_ABCD1_nominal:=(MCSF_Weight_ABCD1)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "_ABCD2_nominal:=(MCSF_Weight_ABCD2)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "_ABCD3_nominal:=(MCSF_Weight_ABCD3)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "_ABCD4_nominal:=(MCSF_Weight_ABCD4)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "_ABCD5_nominal:=(MCSF_Weight_ABCD5)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "_ABCD6_nominal:=(MCSF_Weight_ABCD6)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "_ABCD7_nominal:=(MCSF_Weight_ABCD7)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "_ABCD8_nominal:=(MCSF_Weight_ABCD8)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "_ABCD9_nominal:=(MCSF_Weight_ABCD9)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "_ABCD10_nominal:=(MCSF_Weight_ABCD10)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
    ]


# names of the systematics (proper names needed e.g. for combination)
mcweight='35.9'

ttbarXS_MCgen='730.0'
ttbarXS_NLO='831.76*(0.7985390843)' 

sfs="Weight_ElectronSFID*Weight_ElectronSFTrigger*Weight_ElectronSFIso*Weight_MuonSFID*Weight_MuonSFTrigger*Weight_MuonSFIso"
usualweights="(1*Weight_PU*((Weight>0)-(Weight<0)))*Weight_ElectronSFID*Weight_ElectronSFTrigger*Weight_ElectronSFIso*Weight_MuonSFID*Weight_MuonSFTrigger*Weight_MuonSFIso"


# samples
# input paths
path_80x_MC="/nfs/dust/cms/user/skudella/processed_MC/flat_trees_new/"
path_80x_DATA="/nfs/dust/cms/user/skudella/processed_DATA/flat_trees/"

# MC samples (name, color, path to files,weight,nickname_without_special_characters,systematics)
samples=[
                    #Sample('Z->tWb, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=700',ROOT.kMagenta,path_80x_MC+'ZPrime/Zprime_1500_700_nominal_Tree.root',mcweight,'Zprime1500700') ,
                    #Sample('Z->tWb, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=900',ROOT.kMagenta+2,path_80x_MC+'Signal_Zprime/Zprime_1500_900_nominal_Tree.root',mcweight,'Zprime1500900') ,
                    #Sample('Z->tWb, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=1200',ROOT.kMagenta-9,path_80x_MC+'ZPrime/Zprime_1500_1200_nominal_Tree.root',mcweight,'Zprime15001200') ,

                    #Sample('Z->tWb, MZp2000Nar_MTp900Nar_LH',ROOT.kCyan,path_80x_MC+'ZPrime/Zprime_2000_900_nominal_Tree.root',mcweight,'Zprime2000900') ,
                    #Sample('Z->tWb, m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1200',ROOT.kCyan,path_80x_MC+'Signal_Zprime/Zprime_2000_1200_LH_nominal_Tree.root',mcweight,'Zprime20001200') ,
                    #Sample('Z->tWb, MZp2000Nar_MTp1200Nar_RH',ROOT.kCyan,path_80x_MC+'ZPrime/Zprime_2000_1200_RH_nominal_Tree.root',mcweight,'Zprime20001200RH') ,
                    #Sample('Z->tWb, MZp2000Wid_MTp1200Nar_LH',ROOT.kCyan+1,path_80x_MC+'ZPrime/Zprime_2000Wid_1200_nominal_Tree.root',mcweight,'Zprime2000W1200') ,
                    #Sample('Z->tWb, MZp2000nar_MTp1200Wid_LH',ROOT.kCyan+1,path_80x_MC+'ZPrime/Zprime_2000_1200Wid_nominal_Tree.root',mcweight,'Zprime20001200W') ,
                    #Sample('Z->tWb, MZp2000Nar_MTp1500Nar_LH',ROOT.kCyan+3,path_80x_MC+'ZPrime/Zprime_2000_1500_nominal_Tree.root',mcweight,'Zprime200015000') ,

                    #Sample('Z->tWb, m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1200',ROOT.kRed,path_80x_MC+'Signal_Zprime/Zprime_2500_1200_nominal_Tree.root',mcweight,'Zprime25001200') ,
                    #Sample('Z->tWb, MZp2500Nar_MTp1500Nar_LH',ROOT.kRed+2,path_80x_MC+'ZPrime/Zprime_2500_1500_nominal_Tree.root',mcweight,'Zprime25001500') ,


                    #Sample('QCD_comb',ROOT.kYellow,path_80x_MC+'QCD/MC_QCD_*nominal*Tree*.root',mcweight,'QCD_comb') ,
                    #Sample('QCD_HT',ROOT.kYellow,path_80x_MC+'BKG_QCD/MC_QCD_H*nominal*Tree*.root',mcweight,'QCD_HT') ,
                    #Sample('QCD_Pt',ROOT.kGreen,path_80x_MC+'BKG_QCD/MC_QCD_P*nominal*Tree*.root',mcweight,'QCD_PT') ,

                    #Sample('t#bar{t} + jets',ROOT.kBlue,path_80x_MC+'BKG_TTbar/MC_TTbar_nominal_Tree_1.root',mcweight,'ttbar') ,
                    #Sample('t#bar{t} + jets',ROOT.kBlue,path_80x_MC+'BKG_TTbar/*nominal*.root',mcweight,'ttbar') ,
                    #Sample('Single Top',ROOT.kMagenta,path_80x_MC+'/st*/*nominal*.root',mcweightAll,'SingleTop',systs_all_samples) ,
                    #Sample('V+jets',ROOT.kGreen-3,path_80x_MC+'/??ets*/*nominal*.root',mcweightAll,'Vjets',systs_all_samples) ,
                    #Sample('t#bar{t}+V',ROOT.kBlue-10,path_80x_MC+'/tt?_*/*nominal*.root',mcweightAll,'ttV',systs_all_samples),
                    #Sample('Diboson',ROOT.kAzure+2,path_80x_MC+'/??/*nominal*.root',mcweightAll,'Diboson',systs_all_samples) ,
                    #Sample('QCD',ROOT.kYellow ,path_80x_MC+'/QCD*/*nominal*root',mcweight,'QCD') ,
                    #Sample('MC_BKG_DATA',ROOT.kAzure,path_80x_MC+'BKG*/*nominal*.root',mcweight,'MC_BKG_DATA') ,
                    #Sample('C_BKG_DATA',ROOT.kAzure,path_80x_MC+'QCD*/*nominal*.root',mcweight,'MC_BKG_DATA') ,

]



SignalSamples=[
                    #Sample('Z->tWb, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=700',ROOT.kMagenta,path_80x_MC+'Signal_Zprime/Zprime_1500_700_nominal_Tree.root',mcweight,'Zprime1500700') ,
                    #Sample('Z->tWb, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=900',ROOT.kMagenta+2,path_80x_MC+'Signal_Zprime/Zprime_1500_900_nominal_Tree.root',mcweight,'Zprime1500900'),
                    #Sample('Z->tWb, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=1200',ROOT.kMagenta-9,path_80x_MC+'Signal_Zprime/Zprime_1500_1200_nominal_Tree.root',mcweight,'Zprime15001200') ,
                    #Sample('Z->tWb, m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1200',ROOT.kCyan,path_80x_MC+'Signal_Zprime/Zprime_2000_1200_LH_nominal_Tree.root',mcweight,'Zprime20001200'),
                    #Sample('Z->tWb, m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1500',ROOT.kCyan+3,path_80x_MC+'Signal_Zprime/Zprime_2000_1500_nominal_Tree.root',mcweight,'Zprime20001500') ,
                    #Sample('Z->tWb, m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1200',ROOT.kRed,path_80x_MC+'Signal_Zprime/Zprime_2500_1200_nominal_Tree.root',mcweight ,'Zprime25001200') ,


]

BackgroundSamples=[
                    #Sample('t#bar{t} + jets',ROOT.kBlue,path_80x_MC+'BKG_TTbar/*nominal*.root',mcweight+'/'+ttbarXS_MCgen+'*'+ttbarXS_NLO,'ttbar',weigthsystnamesMCSFs),
                    Sample('Top background',ROOT.kBlue,path_80x_MC+'BKG_TTbar/*nominal*.root',mcweight+'/'+ttbarXS_MCgen+'*'+ttbarXS_NLO,'ttbar',weigthsystnamesMCSFs),
                    Sample('single top (tW-channel)',ROOT.kBlue+2,path_80x_MC+'BKG_ST/*ST*tW*nominal*.root',mcweight,'ST_tW',weigthsystnamesMCSFs),
                    Sample('single top (t-channel)',ROOT.kBlue-9,path_80x_MC+'BKG_ST/*ST*t-channel*nominal*.root',mcweight,'ST_t',weigthsystnamesMCSFs) ,
                    Sample('single top (s-channel)',ROOT.kBlue-7,path_80x_MC+'BKG_ST/*ST*s-channel*nominal*.root',mcweight,'ST_s',weigthsystnamesMCSFs) ,
                    
                    Sample('QCD_HT',ROOT.kOrange-3,path_80x_MC+'BKG_QCD/QCD_H*nominal*Tree*.root',mcweight,'QCD_HT',weigthsystnamesMCSFs),
                    #Sample('QCD_Pt',ROOT.kGreen,path_80x_MC+'BKG_QCD/MC_QCD_P*nominal*Tree*.root',mcweight,'QCD_PT'),
                    #Sample('QCD_comb',ROOT.kGreen,path_80x_MC+'BKG_QCD/MC_QCD*nominal*Tree*.root',mcweight,'QCD_comb'),
]


DataSamples=[
                    Sample('DATA 2016 - Top',ROOT.kOrange-3,path_80x_DATA+'*nominal*.root','1.0','DATA_2016'),
                    #Sample('DATA_2016_test',ROOT.kBlack,path_80x_DATA+'*nominal*Tree_.root','1.0','DATA_2016_test'),

]

CombinedSamples=[
                    #Sample('Zprime15001200_and_QCD_HT',ROOT.kRed, [path_80x_MC+'BKG_QCD/MC_QCD_P*nominal*Tree*.root', path_80x_MC+'Signal_Zprime/Zprime_1500_900_nominal_Tree.root'],mcweight,'Zprime15001200_and_QCD_HT'),
                    #Sample('Zprime20001200_and_QCD_HT',ROOT.kRed, [path_80x_MC+'BKG_QCD/MC_QCD_P*nominal*Tree*.root', path_80x_MC+'Signal_Zprime/Zprime_2000_1200_nominal_Tree.root'],mcweight,'Zprime20001200_and_QCD_HT'),
                    #Sample('Zprime25001200_and_QCD_HT',ROOT.kRed, [path_80x_MC+'BKG_QCD/MC_QCD_P*nominal*Tree*.root', path_80x_MC+'Signal_Zprime/Zprime_2500_1200_nominal_Tree.root'],mcweight,'Zprime25001200_and_QCD_HT'),

                    #Sample('Zprime15001200_and_QCD_PT',ROOT.kRed, [path_80x_MC+'BKG_QCD/MC_QCD_P*nominal*Tree*.root', path_80x_MC+'Signal_Zprime/Zprime_1500_900_nominal_Tree.root'],mcweight,'Zprime15001200_and_QCD_PT'),
                    #Sample('Zprime20001200_and_QCD_PT',ROOT.kRed, [path_80x_MC+'BKG_QCD/MC_QCD_P*nominal*Tree*.root', path_80x_MC+'Signal_Zprime/Zprime_2000_1200_nominal_Tree.root'],mcweight,'Zprime20001200_and_QCD_PT'),
                    #Sample('Zprime25001200_and_QCD_PT',ROOT.kRed, [path_80x_MC+'BKG_QCD/MC_QCD_P*nominal*Tree*.root', path_80x_MC+'Signal_Zprime/Zprime_2500_1200_nominal_Tree.root'],mcweight,'Zprime25001200_and_QCD_PT'),

	]


samplenames=[]
for i in samples:
    samplenames.append(i.nick)
SignalSampleNames=[]
for i in SignalSamples:
    SignalSampleNames.append(i.nick)
BackgroundSampleNames=[]
for i in BackgroundSamples:
    BackgroundSampleNames.append(i.nick)
DataSampleNames=[]
for i in DataSamples:
    DataSampleNames.append(i.nick)
