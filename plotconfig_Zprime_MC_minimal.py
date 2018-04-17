import sys
import os
from scriptgenerator_minimal import *
from plotutils import *


# names of the systematics (proper names needed e.g. for combination)
mcweight='35.9'



# samples
# input path
path_80x="/nfs/dust/cms/user/skudella/processed_MC/flat_trees_new/"
path="/pnfs/desy.de/cms/tier2/store/user/skudella/*/MC_minimal_minimal_*/*/*/*minimal*"

# MC samples (name, color, path to files,weight,nickname_without_special_characters,systematics)

SignalSamples=[
                    #Sample("m(Z')=1500, m(T)=700",ROOT.kMagenta,'/pnfs/desy.de/cms/tier2/store/user/skudella/ZprimeToTprimeT_TprimeToWB_MZp-1500Nar_MTp-900Nar_LH_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MC_minimal_minimal_ZprimeToTprimeT_TprimeToWB_Mzp-1500Nar_Mtp-900Nar_LH/180416_115738/0000/minimal*Zprime*ToWB*1500*700*nominal*Tree*.root',mcweight+'/95.06*0.80','Zprime1500700_tWb') ,
                    
                    Sample("m(Z')=1500, m(T)=700",ROOT.kMagenta,path+'Zprime*ToWB*1500*Nar*700*Nar*nominal*Tree*.root',mcweight+'/95.06*0.80','Zprime1500700_tWb') ,
                    Sample("m(Z')=1500, m(T)=900",ROOT.kMagenta-9,path+'Zprime*ToWB*1500*Nar*900*Nar*nominal*Tree*.root',mcweight+'/138.07*1.5','Zprime1500900_tWb'),
                    Sample("m(Z')=1500, m(T)=1200",ROOT.kMagenta+2,path+'Zprime*ToWB*1500*Nar*1200*Nar*nominal*Tree*.root',mcweight+'/99.03*8.6','Zprime15001200_tWb') ,
                    Sample("m(Z')=2000, m(T)=900",ROOT.kCyan,path+'Zprime*ToWB*2000*Nar*900*Nar*LH*nominal*Tree*.root',mcweight+'/86.28*0.27','Zprime20001200_tWb'),
                    Sample("m(Z')=2000, m(T)=1200",ROOT.kCyan-9,path+'Zprime*ToWB*2000*Nar*1200*Nar*LH*nominal*Tree*.root',mcweight+'/86.28*0.27','Zprime20001200_tWb'),
                    Sample("m(Z')=2000, m(T)=1500",ROOT.kCyan+2,path+'Zprime*ToWB*2000*Nar*1500*Nar*nominal*Tree*.root',mcweight+'/83.47*0.90','Zprime20001500_tWb') ,
                    Sample("m(Z')=2500, m(T)=1200",ROOT.kRed,path+'Zprime*ToWB*2500*Nar*1200*Nar*nominal*Tree*.root',mcweight+'/37.6*0.33' ,'Zprime25001200_tWb') ,
                    Sample("m(Z')=2500, m(T)=1500",ROOT.kRed-9,path+'Zprime*ToWB*2500*Nar*1500*Nar*nominal*Tree*.root',mcweight+'/37.6*0.33' ,'Zprime25001500_tWb') ,

                    Sample('Z->ttZ, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=700',ROOT.kMagenta,path+'Zprime*ToZT*1500*Nar*700*Nar*nominal*Tree*.root',mcweight+'/186.7*3.1','Zprime1500700_ttZ') ,
                    Sample('Z->ttZ, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=900',ROOT.kMagenta+2,path+'Zprime*ToZT*1500*Nar*900*Nar*nominal*Tree*.root',mcweight+'/320.4*2.4','Zprime1500900_ttZ'),
                    Sample('Z->ttZ, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=1200',ROOT.kMagenta-9,path+'Zprime*ToZT*1500*Nar*1200*Nar*nominal*Tree*.root',mcweight+'/285.1*3.1','Zprime15001200_ttZ') ,
                    Sample('Z->ttZ, m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=900',ROOT.kCyan,path+'Zprime*ToZT*2000*Nar*900*Nar*nominal*Tree*.root',mcweight+'/205.6*0.29','Zprime2000900_ttZ'),
                    Sample('Z->ttZ, m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1200',ROOT.kCyan-9,path+'Zprime*ToZT*2000*Nar*1200*Nar*LH*nominal*Tree*.root',mcweight+'/205.6*0.29','Zprime20001200_ttZ'),
                    Sample('Z->ttZ, m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1500',ROOT.kCyan+3,path+'Zprime*ToZT*2000*Nar*1500*Nar*nominal*Tree*.root',mcweight+'/214.1*0.33','Zprime20001500_ttZ') ,
                    Sample('Z->ttZ, m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1200',ROOT.kRed,path+'Zprime*ToZT*2500*Nar*1200*Nar*nominal*Tree*.root',mcweight+'/83.5*0.18' ,'Zprime25001200_ttZ') ,
                    Sample('Z->ttZ, m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1500',ROOT.kRed-9,path+'Zprime*ToZT*2500*Nar*1500*Nar*nominal*Tree*.root',mcweight+'/83.5*0.18' ,'Zprime25001500_ttZ') ,

                    Sample('Z->ttH, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=700',ROOT.kMagenta,path+'Zprime*ToHT*1500*Nar*700*Nar*nominal*Tree*.root',mcweight+'/3.62*3.5','Zprime1500700_ttH') ,
                    Sample('Z->ttH, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=900',ROOT.kMagenta+2,path+'Zprime*ToHT*1500*Nar*900*Nar*nominal*Tree*.root',mcweight+'/3.571*2.6','Zprime1500900_ttH'),
                    Sample('Z->ttH, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=1200',ROOT.kPink-9,path+'Zprime*ToHT*1500*Nar*1200*Nar*nominal*Tree*.root',mcweight+'/1.731*11.0','Zprime15001200_ttH') ,
                    Sample('Z->ttH, m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=900',ROOT.kCyan,path+'Zprime*ToHT*2000*Nar*900*Nar*LH*nominal*Tree*.root',mcweight+'/1.251*0.54','Zprime2000900_ttH'),
                    Sample('Z->ttH, m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1200',ROOT.kCyan-9,path+'Zprime*ToHT*2000*Nar*1200*Nar*LH*nominal*Tree*.root',mcweight+'/1.251*0.54','Zprime20001200_ttH'),
                    Sample('Z->ttH, m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1500',ROOT.kCyan+3,path+'Zprime*ToHT*2000*Nar*1500*Nar*nominal*Tree*.root',mcweight+'/0.8246*0.59','Zprime20001500_ttH') ,
                    Sample('Z->ttH, m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1200',ROOT.kGreen+1,path+'Zprime*ToHT*2500*Nar*1200*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Zprime25001200_ttH') ,
                    Sample('Z->ttH, m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1500',ROOT.kGreen+1,path+'Zprime*ToHT*2500*Nar*1500*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Zprime25001500_ttH') ,
                    
                    
                    
                    #Sample('Signal',ROOT.kGreen+1,path+'Zprime*ToWB*2000*1200*LH*nominal*Tree*.root',mcweight ,'ZprimeAll') ,


]




SignalSampleNames=[]
for i in SignalSamples:
    SignalSampleNames.append(i.nick)
