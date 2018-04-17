import sys
import os
from scriptgenerator import *
from plotutils import *


# names of the systematics (proper names needed e.g. for combination)
mcweight='35.9'

sfs="Weight_ElectronSFID*Weight_ElectronSFTrigger*Weight_ElectronSFIso*Weight_MuonSFID*Weight_MuonSFTrigger*Weight_MuonSFIso"
usualweights="(1*Weight_PU*((Weight>0)-(Weight<0)))*Weight_ElectronSFID*Weight_ElectronSFTrigger*Weight_ElectronSFIso*Weight_MuonSFID*Weight_MuonSFTrigger*Weight_MuonSFIso"


# samples
# input path
path_80x="/nfs/dust/cms/user/skudella/processed_MC/flat_trees_new/"

# MC samples (name, color, path to files,weight,nickname_without_special_characters,systematics)
samples=[
                    #Sample('Z->tWb, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=700',ROOT.kMagenta,path_80x+'ZPrime/Zprime_1500_700_nominal_Tree.root',mcweight,'Zprime1500700') ,
                    Sample('Z->tWb, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=900',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Zprime_1500_900_nominal_Tree.root',mcweight,'Zprime1500900') ,
                    Sample('Z->tWb, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=1200',ROOT.kMagenta-9,path_80x+'ZPrime/Zprime_1500_1200_nominal_Tree.root',mcweight,'Zprime15001200') ,

                    #Sample('Z->tWb, MZp2000Nar_MTp900Nar_LH',ROOT.kCyan,path_80x+'ZPrime/Zprime_2000_900_nominal_Tree.root',mcweight,'Zprime2000900') ,
                    Sample('Z->tWb, m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1200',ROOT.kCyan,path_80x+'Signal_Zprime/Zprime_2000_1200_LH_nominal_Tree.root',mcweight,'Zprime20001200') ,
                    #Sample('Z->tWb, MZp2000Nar_MTp1200Nar_RH',ROOT.kCyan,path_80x+'ZPrime/Zprime_2000_1200_RH_nominal_Tree.root',mcweight,'Zprime20001200RH') ,
                    #Sample('Z->tWb, MZp2000Wid_MTp1200Nar_LH',ROOT.kCyan+1,path_80x+'ZPrime/Zprime_2000Wid_1200_nominal_Tree.root',mcweight,'Zprime2000W1200') ,
                    #Sample('Z->tWb, MZp2000nar_MTp1200Wid_LH',ROOT.kCyan+1,path_80x+'ZPrime/Zprime_2000_1200Wid_nominal_Tree.root',mcweight,'Zprime20001200W') ,
                    #Sample('Z->tWb, MZp2000Nar_MTp1500Nar_LH',ROOT.kCyan+3,path_80x+'ZPrime/Zprime_2000_1500_nominal_Tree.root',mcweight,'Zprime200015000') ,

                    Sample('Z->tWb, m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1200',ROOT.kRed,path_80x+'Signal_Zprime/Zprime_2500_1200_nominal_Tree.root',mcweight,'Zprime25001200') ,
                    #Sample('Z->tWb, MZp2500Nar_MTp1500Nar_LH',ROOT.kRed+2,path_80x+'ZPrime/Zprime_2500_1500_nominal_Tree.root',mcweight,'Zprime25001500') ,


                    #Sample('QCD_comb',ROOT.kYellow,path_80x+'QCD/MC_QCD_*nominal*Tree*.root',mcweight,'QCD_comb') ,
                    Sample('QCD_HT',ROOT.kYellow,path_80x+'BKG_QCD/MC_QCD_H*nominal*Tree*.root',mcweight,'QCD_HT') ,
                    Sample('QCD_Pt',ROOT.kGreen,path_80x+'BKG_QCD/MC_QCD_P*nominal*Tree*.root',mcweight,'QCD_PT') ,

                    #Sample('t#bar{t} + jets',ROOT.kBlue,path_80x+'BKG_TTbar/MC_TTbar_nominal_Tree_1.root',mcweight,'ttbar') ,
                    Sample('t#bar{t} + jets',ROOT.kBlue,path_80x+'BKG_TTbar/*nominal*.root',mcweight,'ttbar') ,
                    #Sample('Single Top',ROOT.kMagenta,path_80x+'/st*/*nominal*.root',mcweightAll,'SingleTop',systs_all_samples) ,
                    #Sample('V+jets',ROOT.kGreen-3,path_80x+'/??ets*/*nominal*.root',mcweightAll,'Vjets',systs_all_samples) ,
                    #Sample('t#bar{t}+V',ROOT.kBlue-10,path_80x+'/tt?_*/*nominal*.root',mcweightAll,'ttV',systs_all_samples),
                    #Sample('Diboson',ROOT.kAzure+2,path_80x+'/??/*nominal*.root',mcweightAll,'Diboson',systs_all_samples) ,
                    #Sample('QCD',ROOT.kYellow ,path_80x+'/QCD*/*nominal*root',mcweight,'QCD') ,
                    #Sample('MC_BKG_DATA',ROOT.kAzure,path_80x+'BKG*/*nominal*.root',mcweight,'MC_BKG_DATA') ,
                    #Sample('C_BKG_DATA',ROOT.kAzure,path_80x+'QCD*/*nominal*.root',mcweight,'MC_BKG_DATA') ,

]



SignalSamples=[
                    Sample("m(Z')=1500, m(T)=700",ROOT.kMagenta,path_80x+'Signal_Zprime/Zprime*ToWB*1500*700*nominal*Tree.root',mcweight+'/95.06*0.80','Zprime1500700_tWb') ,
                    Sample("m(Z')=1500, m(T)=900",ROOT.kMagenta-9,path_80x+'Signal_Zprime/Zprime*ToWB*1500*900*nominal*Tree.root',mcweight+'/138.07*1.5','Zprime1500900_tWb'),
                    Sample("m(Z')=1500, m(T)=1200",ROOT.kMagenta+2,path_80x+'Signal_Zprime/Zprime*ToWB*1500*1200*nominal*Tree.root',mcweight+'/99.03*8.6','Zprime15001200_tWb') ,
                    Sample("m(Z')=2000, m(T)=900",ROOT.kCyan,path_80x+'Signal_Zprime/Zprime*ToWB*2000*900*LH*nominal*Tree.root',mcweight+'/86.28*0.27','Zprime20001200_tWb'),
                    Sample("m(Z')=2000, m(T)=1200",ROOT.kCyan-9,path_80x+'Signal_Zprime/Zprime*ToWB*2000*1200*LH*nominal*Tree.root',mcweight+'/86.28*0.27','Zprime20001200_tWb'),
                    Sample("m(Z')=2000, m(T)=1500",ROOT.kCyan+2,path_80x+'Signal_Zprime/Zprime*ToWB*2000*1500*nominal*Tree.root',mcweight+'/83.47*0.90','Zprime20001500_tWb') ,
                    Sample("m(Z')=2500, m(T)=1200",ROOT.kRed,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1200*nominal*Tree.root',mcweight+'/37.6*0.33' ,'Zprime25001200_tWb') ,
                    Sample("m(Z')=2500, m(T)=1500",ROOT.kRed-9,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1500*nominal*Tree.root',mcweight+'/37.6*0.33' ,'Zprime25001500_tWb') ,

                    Sample('Z->ttZ, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=700',ROOT.kMagenta,path_80x+'Signal_Zprime/Zprime*ToZT*1500*700*nominal*Tree.root',mcweight+'/186.7*3.1','Zprime1500700_ttZ') ,
                    Sample('Z->ttZ, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=900',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Zprime*ToZT*1500*900*nominal*Tree.root',mcweight+'/320.4*2.4','Zprime1500900_ttZ'),
                    Sample('Z->ttZ, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=1200',ROOT.kMagenta-9,path_80x+'Signal_Zprime/Zprime*ToZT*1500*1200*nominal*Tree.root',mcweight+'/285.1*3.1','Zprime15001200_ttZ') ,
                    Sample('Z->ttZ, m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1200',ROOT.kCyan,path_80x+'Signal_Zprime/Zprime*ToZT*2000*1200*LH*nominal*Tree.root',mcweight+'/205.6*0.29','Zprime20001200_ttZ'),
                    Sample('Z->ttZ, m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1500',ROOT.kCyan+3,path_80x+'Signal_Zprime/Zprime*ToZT*2000*1500*nominal*Tree.root',mcweight+'/214.1*0.33','Zprime20001500_ttZ') ,
                    Sample('Z->ttZ, m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1200',ROOT.kRed,path_80x+'Signal_Zprime/Zprime*ToZT*2500*1200*nominal*Tree.root',mcweight+'/83.5*0.18' ,'Zprime25001200_ttZ') ,

                    Sample('Z->ttH, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=700',ROOT.kMagenta,path_80x+'Signal_Zprime/Zprime*ToHT*1500*700*nominal*Tree.root',mcweight+'/3.62*3.5','Zprime1500700_ttH') ,
                    Sample('Z->ttH, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=900',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Zprime*ToHT*1500*900*nominal*Tree.root',mcweight+'/3.571*2.6','Zprime1500900_ttH'),
                    Sample('Z->ttH, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=1200',ROOT.kPink-9,path_80x+'Signal_Zprime/Zprime*ToHT*1500*1200*nominal*Tree.root',mcweight+'/1.731*11.0','Zprime15001200_ttH') ,
                    Sample('Z->ttH, m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1200',ROOT.kCyan,path_80x+'Signal_Zprime/Zprime*ToHT*2000*1200*LH*nominal*Tree.root',mcweight+'/1.251*0.54','Zprime20001200_ttH'),
                    Sample('Z->ttH, m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1500',ROOT.kCyan+3,path_80x+'Signal_Zprime/Zprime*ToHT*2000*1500*nominal*Tree.root',mcweight+'/0.8246*0.59','Zprime20001500_ttH') ,
                    Sample('Z->ttH, m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1200',ROOT.kGreen+1,path_80x+'Signal_Zprime/Zprime*ToHT*2500*1200*nominal*Tree.root',mcweight+'/0.511*0.26' ,'Zprime25001200_ttH') ,
                    Sample('Signal',ROOT.kGreen+1,path_80x+'Signal_Zprime/Zprime*ToWB*2000*1200*LH*nominal*Tree.root',mcweight ,'ZprimeAll') ,


]

BackgroundSamples=[
                    Sample('Top background',ROOT.kBlue,path_80x+'BKG_TTbar/*nominal*.root',mcweight,'ttbar') ,
                    Sample('single top (tW-channel)',ROOT.kBlue+2,path_80x+'BKG_ST/*ST*tW*nominal*.root',mcweight,'ST_tW') ,
                    Sample('single top (t-channel)',ROOT.kBlue-9,path_80x+'BKG_ST/*ST*t-channel*nominal*.root',mcweight,'ST_t') ,
                    Sample('single top (s-channel)',ROOT.kBlue-7,path_80x+'BKG_ST/*ST*s-channel*nominal*.root',mcweight,'ST_s') ,
                    
                    Sample('QCD from MC',ROOT.kOrange-3,path_80x+'BKG_QCD/*QCD_H*nominal*Tree*.root',mcweight,'QCD_HT'),
                    #Sample('QCD_Pt',ROOT.kGreen,path_80x+'BKG_QCD/MC_QCD_P*nominal*Tree*.root',mcweight,'QCD_PT'),
                    #Sample('QCD_comb',ROOT.kGreen,path_80x+'BKG_QCD/MC_QCD*nominal*Tree*.root',mcweight,'QCD_comb'),
]


DataSamples=[
                    #Sample('DATA_2016',ROOT.kBlack,path_80x+'DATA*/*nominal*.root',mcweight,'MC_BKG_DATA'),

]

CombinedSamples=[
                    #Sample('Zprime15001200_and_QCD_HT',ROOT.kRed, [path_80x+'BKG_QCD/MC_QCD_P*nominal*Tree*.root', path_80x+'Signal_Zprime/Zprime_1500_900_nominal_Tree.root'],mcweight,'Zprime15001200_and_QCD_HT'),
                    #Sample('Zprime20001200_and_QCD_HT',ROOT.kRed, [path_80x+'BKG_QCD/MC_QCD_P*nominal*Tree*.root', path_80x+'Signal_Zprime/Zprime_2000_1200_nominal_Tree.root'],mcweight,'Zprime20001200_and_QCD_HT'),
                    #Sample('Zprime25001200_and_QCD_HT',ROOT.kRed, [path_80x+'BKG_QCD/MC_QCD_P*nominal*Tree*.root', path_80x+'Signal_Zprime/Zprime_2500_1200_nominal_Tree.root'],mcweight,'Zprime25001200_and_QCD_HT'),

                    #Sample('Zprime15001200_and_QCD_PT',ROOT.kRed, [path_80x+'BKG_QCD/MC_QCD_P*nominal*Tree*.root', path_80x+'Signal_Zprime/Zprime_1500_900_nominal_Tree.root'],mcweight,'Zprime15001200_and_QCD_PT'),
                    #Sample('Zprime20001200_and_QCD_PT',ROOT.kRed, [path_80x+'BKG_QCD/MC_QCD_P*nominal*Tree*.root', path_80x+'Signal_Zprime/Zprime_2000_1200_nominal_Tree.root'],mcweight,'Zprime20001200_and_QCD_PT'),
                    #Sample('Zprime25001200_and_QCD_PT',ROOT.kRed, [path_80x+'BKG_QCD/MC_QCD_P*nominal*Tree*.root', path_80x+'Signal_Zprime/Zprime_2500_1200_nominal_Tree.root'],mcweight,'Zprime25001200_and_QCD_PT'),

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
print "ladida ", SignalSampleNames