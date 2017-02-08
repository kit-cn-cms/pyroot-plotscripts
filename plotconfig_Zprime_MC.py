import sys
import os
from scriptgenerator import *
from plotutils import *


# names of the systematics (proper names needed e.g. for combination)
mcweight='27.3'

sfs="Weight_ElectronSFID*Weight_ElectronSFTrigger*Weight_ElectronSFIso*Weight_MuonSFID*Weight_MuonSFTrigger*Weight_MuonSFIso"
usualweights="(1*Weight_PU*((Weight>0)-(Weight<0)))*Weight_ElectronSFID*Weight_ElectronSFTrigger*Weight_ElectronSFIso*Weight_MuonSFID*Weight_MuonSFTrigger*Weight_MuonSFIso"


# samples
# input path 
path_80x="/nfs/dust/cms/user/skudella/processed_MC/flat_trees/"

# MC samples (name, color, path to files,weight,nickname_without_special_characters,systematics)                       
samples=[ 
                    #Sample('Z->tWb, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=700',ROOT.kMagenta,path_80x+'ZPrime/Zprime_1500_700_nominal_Tree.root',mcweight,'Zprime1500700') ,
                    Sample('Z->tWb, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=900',ROOT.kMagenta+2,path_80x+'Zprime/Zprime_1500_900_nominal_Tree.root',mcweight,'Zprime1500900') ,
                    #Sample('Z->tWb, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=1200',ROOT.kMagenta-9,path_80x+'ZPrime/Zprime_1500_1200_nominal_Tree.root',mcweight,'Zprime15001200') ,

                    #Sample('Z->tWb, MZp2000Nar_MTp900Nar_LH',ROOT.kCyan,path_80x+'ZPrime/Zprime_2000_900_nominal_Tree.root',mcweight,'Zprime2000900') ,
                    Sample('Z->tWb, m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1200',ROOT.kCyan,path_80x+'Zprime/Zprime_2000_1200_LH_nominal_Tree.root',mcweight,'Zprime20001200') ,
                    #Sample('Z->tWb, MZp2000Nar_MTp1200Nar_RH',ROOT.kCyan,path_80x+'ZPrime/Zprime_2000_1200_RH_nominal_Tree.root',mcweight,'Zprime20001200RH') ,
                    #Sample('Z->tWb, MZp2000Wid_MTp1200Nar_LH',ROOT.kCyan+1,path_80x+'ZPrime/Zprime_2000Wid_1200_nominal_Tree.root',mcweight,'Zprime2000W1200') ,
                    #Sample('Z->tWb, MZp2000nar_MTp1200Wid_LH',ROOT.kCyan+1,path_80x+'ZPrime/Zprime_2000_1200Wid_nominal_Tree.root',mcweight,'Zprime20001200W') ,
                    #Sample('Z->tWb, MZp2000Nar_MTp1500Nar_LH',ROOT.kCyan+3,path_80x+'ZPrime/Zprime_2000_1500_nominal_Tree.root',mcweight,'Zprime200015000') , 
                    
                    Sample('Z->tWb, m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1200',ROOT.kRed,path_80x+'Zprime/Zprime_2500_1200_nominal_Tree.root',mcweight,'Zprime25001200') ,     
                    #Sample('Z->tWb, MZp2500Nar_MTp1500Nar_LH',ROOT.kRed+2,path_80x+'ZPrime/Zprime_2500_1500_nominal_Tree.root',mcweight,'Zprime25001500') ,     
                    

                    #Sample('QCD_comb',ROOT.kYellow,path_80x+'QCD/MC_QCD_*nominal*Tree*.root',mcweight,'QCD_comb') ,     
                    Sample('QCD_Pt',ROOT.kOrange,path_80x+'QCD/MC_QCD_P*nominal*Tree*.root',mcweight+'/2','QCD_PT') ,     
                    Sample('QCD_HT',ROOT.kYellow,path_80x+'QCD/MC_QCD_H*nominal*Tree*.root',mcweight+'/2','QCD_HT') ,     
  

                    #Sample('t#bar{t} + jets',ROOT.kBlue,path_80x+'TTbar/MC_TTbar_nominal_Tree_1.root',mcweight,'ttbar') ,     
                    #Sample('t#bar{t} + jets',ROOT.kBlue,path_80x+'TTbar/*nominal*.root',mcweight,'ttbar') ,     

                    #Sample('Single Top',ROOT.kMagenta,path_80x+'/st*/*nominal*.root',mcweightAll,'SingleTop',systs_all_samples) , 
                    #Sample('V+jets',ROOT.kGreen-3,path_80x+'/??ets*/*nominal*.root',mcweightAll,'Vjets',systs_all_samples) , 
                    #Sample('t#bar{t}+V',ROOT.kBlue-10,path_80x+'/tt?_*/*nominal*.root',mcweightAll,'ttV',systs_all_samples),         
                    ##Sample('Diboson',ROOT.kAzure+2,path_80x+'/??/*nominal*.root',mcweightAll,'Diboson',systs_all_samples) , 
#                    Sample('QCD',ROOT.kYellow ,path_80x+'/QCD*/*nominal*root',mcweight,'QCD') , 
                    #Sample('C_BKG_DATA',ROOT.kBlue,path_80x+'TT*/*nominal*.root+QCD/*nominal*.root',mcweight,'MC_BKG_DATA') ,     
                    #Sample('C_BKG_DATA',ROOT.kBlue,path_80x+'QCD/*nominal*.root',mcweight,'MC_QCD_BKG_DATA') ,     

]


samples_data=[]
