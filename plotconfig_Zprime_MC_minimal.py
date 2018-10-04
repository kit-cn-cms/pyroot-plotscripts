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
                    
                    Sample("m(Z')=1500, m(T)=700",ROOT.kMagenta,path+'Zprime*ToWB*-1500*Nar*700*Nar*nominal*Tree*.root',mcweight+'/95.06*0.80','Zprime1500700_tWb') ,
                    Sample("m(Z')=1500, m(T)=900",ROOT.kMagenta-9,path+'Zprime*ToWB*-1500*Nar*900*Nar*nominal*Tree*.root',mcweight+'/138.07*1.5','Zprime1500900_tWb'),
                    Sample("m(Z')=1500, m(T)=1200",ROOT.kMagenta+2,path+'Zprime*ToWB*-1500*Nar*1200*Nar*nominal*Tree*.root',mcweight+'/99.03*8.6','Zprime15001200_tWb') ,
                    Sample("m(Z')=2000, m(T)=900",ROOT.kCyan,path+'Zprime*ToWB*-2000*Nar*900*Nar*LH*nominal*Tree*.root',mcweight+'/86.28*0.27','Zprime20001200_tWb'),
                    Sample("m(Z')=2000, m(T)=1200",ROOT.kCyan-9,path+'Zprime*ToWB*-2000*Nar*1200*Nar*LH*nominal*Tree*.root',mcweight+'/86.28*0.27','Zprime20001200_tWb'),
                    Sample("m(Z')=2000, m(T)=1500",ROOT.kCyan+2,path+'Zprime*ToWB*-2000*Nar*1500*Nar*nominal*Tree*.root',mcweight+'/83.47*0.90','Zprime20001500_tWb') ,
                    Sample("m(Z')=2500, m(T)=1200",ROOT.kRed,path+'Zprime*ToWB*-2500*Nar*1200*Nar*nominal*Tree*.root',mcweight+'/37.6*0.33' ,'Zprime25001200_tWb') ,
                    Sample("m(Z')=2500, m(T)=1500",ROOT.kRed-9,path+'Zprime*ToWB*-2500*Nar*1500*Nar*nominal*Tree*.root',mcweight+'/37.6*0.33' ,'Zprime25001500_tWb') ,

                    Sample('Z->ttZ, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=700',ROOT.kMagenta,path+'Zprime*ToZT*-1500*Nar*700*Nar*nominal*Tree*.root',mcweight+'/186.7*3.1','Zprime1500700_ttZ') ,
                    Sample('Z->ttZ, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=900',ROOT.kMagenta+2,path+'Zprime*ToZT*-1500*Nar*900*Nar*nominal*Tree*.root',mcweight+'/320.4*2.4','Zprime1500900_ttZ'),
                    Sample('Z->ttZ, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=1200',ROOT.kMagenta-9,path+'Zprime*ToZT*-1500*Nar*1200*Nar*nominal*Tree*.root',mcweight+'/285.1*3.1','Zprime15001200_ttZ') ,
                    Sample('Z->ttZ, m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=900',ROOT.kCyan,path+'Zprime*ToZT*-2000*Nar*900*Nar*nominal*Tree*.root',mcweight+'/205.6*0.29','Zprime2000900_ttZ'),
                    Sample('Z->ttZ, m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1200',ROOT.kCyan-9,path+'Zprime*ToZT*-2000*Nar*1200*Nar*LH*nominal*Tree*.root',mcweight+'/205.6*0.29','Zprime20001200_ttZ'),
                    Sample('Z->ttZ, m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1500',ROOT.kCyan+3,path+'Zprime*ToZT*-2000*Nar*1500*Nar*nominal*Tree*.root',mcweight+'/214.1*0.33','Zprime20001500_ttZ') ,
                    Sample('Z->ttZ, m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1200',ROOT.kRed,path+'Zprime*ToZT*-2500*Nar*1200*Nar*nominal*Tree*.root',mcweight+'/83.5*0.18' ,'Zprime25001200_ttZ') ,
                    Sample('Z->ttZ, m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1500',ROOT.kRed-9,path+'Zprime*ToZT*-2500*Nar*1500*Nar*nominal*Tree*.root',mcweight+'/83.5*0.18' ,'Zprime25001500_ttZ') ,

                    Sample('Z->ttH, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=700',ROOT.kMagenta,path+'Zprime*ToHT*-1500*Nar*700*Nar*nominal*Tree*.root',mcweight+'/3.62*3.5','Zprime1500700_ttH') ,
                    Sample('Z->ttH, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=900',ROOT.kMagenta+2,path+'Zprime*ToHT*-1500*Nar*900*Nar*nominal*Tree*.root',mcweight+'/3.571*2.6','Zprime1500900_ttH'),
                    Sample('Z->ttH, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=1200',ROOT.kPink-9,path+'Zprime*ToHT*-1500*Nar*1200*Nar*nominal*Tree*.root',mcweight+'/1.731*11.0','Zprime15001200_ttH') ,
                    Sample('Z->ttH, m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=900',ROOT.kCyan,path+'Zprime*ToHT*-2000*Nar*900*Nar*LH*nominal*Tree*.root',mcweight+'/1.251*0.54','Zprime2000900_ttH'),
                    Sample('Z->ttH, m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1200',ROOT.kCyan-9,path+'Zprime*ToHT*-2000*Nar*1200*Nar*LH*nominal*Tree*.root',mcweight+'/1.251*0.54','Zprime20001200_ttH'),
                    Sample('Z->ttH, m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1500',ROOT.kCyan+3,path+'Zprime*ToHT*-2000*Nar*1500*Nar*nominal*Tree*.root',mcweight+'/0.8246*0.59','Zprime20001500_ttH') ,
                    Sample('Z->ttH, m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1200',ROOT.kGreen+1,path+'Zprime*ToHT*-2500*Nar*1200*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Zprime25001200_ttH') ,
                    Sample('Z->ttH, m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1500',ROOT.kGreen+1,path+'Zprime*ToHT*-2500*Nar*1500*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Zprime25001500_ttH') ,
                    
                    
                    
                    

                    Sample('G->tWb, m(Gp_{Nar})=1500, m(Tp_{Nar,LH})=800',ROOT.kMagenta,path+'Zprime*ToWB*Zp1500*Nar*800*Nar*nominal*Tree*.root',mcweight+'/3.62*3.5','Gprime1500800_tWb') ,
                    Sample('G->tWb, m(Gp_{Nar})=1500, m(Tp_{Nar,LH})=1000',ROOT.kMagenta+2,path+'Zprime*ToWB*Zp1500*Nar*1000*Nar*nominal*Tree*.root',mcweight+'/3.571*2.6','Gprime15001000_tWb'),
                    Sample('G->tWb, m(Gp_{Nar})=1500, m(Tp_{Nar,LH})=1300',ROOT.kMagenta-7,path+'Zprime*ToWB*Zp1500*Nar*1300*Nar*nominal*Tree*.root',mcweight+'/1.731*11.0','Gprime15001300_tWb') ,
                    
                    Sample('G->tWb, m(Gp_{Nar})=1750, m(Tp_{Nar,LH})=1300',ROOT.kYellow-3,path+'Zprime*ToWB*Zp1750*Nar*1300*Nar*nominal*Tree*.root',mcweight+'/1.731*11.0','Gprime17501300_tWb') ,
                    
                    Sample('G->tWb, m(Gp_{Nar})=2000, m(Tp_{Nar,LH})=1000',ROOT.kOrange-5,path+'Zprime*ToWB*Zp2000*Nar*1000*Nar*LH*nominal*Tree*.root',mcweight+'/1.251*0.54','Gprime20001000_tWb'),
                    Sample('G->tWb, m(Gp_{Nar})=2000, m(Tp_{Nar,LH})=1300',ROOT.kOrange-9,path+'Zprime*ToWB*Zp2000*Nar*1300*Nar*LH*nominal*Tree*.root',mcweight+'/1.251*0.54','Gprime20001300_tWb'),
                    Sample('G->tWb, m(Gp_{Nar})=2000, m(Tp_{Nar,LH})=1500',ROOT.kOrange+3,path+'Zprime*ToWB*Zp2000*Nar*1500*Nar*nominal*Tree*.root',mcweight+'/0.8246*0.59','Gprime20001500_tWb') ,
                    
                    Sample('G->tWb, m(Gp_{Nar})=2250, m(Tp_{Nar,LH})=1300',ROOT.kSpring,path+'Zprime*ToWB*Zp2250*Nar*1300*Nar*nominal*Tree*.root',mcweight+'/0.8246*0.59','Gprime22501300_tWb') ,
                    Sample('G->tWb, m(Gp_{Nar})=2250, m(Tp_{Nar,LH})=1500',ROOT.kSpring+2,path+'Zprime*ToWB*Zp2250*Nar*1500*Nar*nominal*Tree*.root',mcweight+'/0.8246*0.59','Gprime22501500_tWb') ,
                    
                    Sample('G->tWb, m(Gp_{Nar})=2500, m(Tp_{Nar,LH})=1200',ROOT.kCyan,path+'Zprime*ToWB*Zp2500*Nar*1300*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime25001200_tWb') ,
                    Sample('G->tWb, m(Gp_{Nar})=2500, m(Tp_{Nar,LH})=1500',ROOT.kCyan-3,path+'Zprime*ToWB*Zp2500*Nar*1500*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime25001500_tWb') ,                 
                    Sample('G->tWb, m(Gp_{Nar})=2500, m(Tp_{Nar,LH})=1800',ROOT.kCyan-7,path+'Zprime*ToWB*Zp2500*Nar*1800*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime25001800_tWb') ,                 
                 
                    Sample('G->tWb, m(Gp_{Nar})=2750, m(Tp_{Nar,LH})=1500',ROOT.kPink,path+'Zprime*ToWB*Zp2750*Nar*1500*Nar*nominal*Tree*.root',mcweight+'/1.731*11.0','Gprime27501500_tWb') ,

                    Sample('G->tWb, m(Gp_{Nar})=3000, m(Tp_{Nar,LH})=1500',ROOT.kRed+2,path+'Zprime*ToWB*Zp3000*Nar*1500*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime30001500_tWb') ,
                    Sample('G->tWb, m(Gp_{Nar})=3000, m(Tp_{Nar,LH})=1800',ROOT.kRed-7,path+'Zprime*ToWB*Zp3000*Nar*1800*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime30001800_tWb') ,                 
                    Sample('G->tWb, m(Gp_{Nar})=3000, m(Tp_{Nar,LH})=2100',ROOT.kRed-3,path+'Zprime*ToWB*Zp3000*Nar*2100*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime30002100_tWb') , 

                    Sample('G->tWb, m(Gp_{Nar})=3500, m(Tp_{Nar,LH})=1800',ROOT.kGreen,path+'Zprime*ToWB*Zp3500*Nar*1800*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime35001800_tWb') ,
                    Sample('G->tWb, m(Gp_{Nar})=3500, m(Tp_{Nar,LH})=2100',ROOT.kGreen+2,path+'Zprime*ToWB*Zp3500*Nar*2100*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime35002100_tWb') ,                 
                    Sample('G->tWb, m(Gp_{Nar})=3500, m(Tp_{Nar,LH})=2500',ROOT.kGreen-7,path+'Zprime*ToWB*Zp3500*Nar*2500*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime35002500_tWb') , 

                    Sample('G->tWb, m(Gp_{Nar})=4000, m(Tp_{Nar,LH})=2100',ROOT.kBlue-3,path+'Zprime*ToWB*Zp4000*Nar*2100*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime40002100_tWb') ,
                    Sample('G->tWb, m(Gp_{Nar})=4000, m(Tp_{Nar,LH})=2500',ROOT.kBlue-5,path+'Zprime*ToWB*Zp4000*Nar*2500*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime40002500_tWb') ,                 
                    Sample('G->tWb, m(Gp_{Nar})=4000, m(Tp_{Nar,LH})=3000',ROOT.kBlue-9,path+'Zprime*ToWB*Zp4000*Nar*3000*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime40003000_tWb') , 
                    
         

                    Sample('G->ttZ, m(Gp_{Nar})=1500, m(Tp_{Nar,LH})=800',ROOT.kMagenta,path+'Zprime*ToZT*Zp1500*Nar*800*Nar*nominal*Tree*.root',mcweight+'/3.62*3.5','Gprime1500800_ttZ') ,
                    Sample('G->ttZ, m(Gp_{Nar})=1500, m(Tp_{Nar,LH})=1000',ROOT.kMagenta+2,path+'Zprime*ToZT*Zp1500*Nar*1000*Nar*nominal*Tree*.root',mcweight+'/3.571*2.6','Gprime15001000_ttZ'),
                    Sample('G->ttZ, m(Gp_{Nar})=1500, m(Tp_{Nar,LH})=1300',ROOT.kMagenta-7,path+'Zprime*ToZT*Zp1500*Nar*1300*Nar*nominal*Tree*.root',mcweight+'/1.731*11.0','Gprime15001300_ttZ') ,
                    
                    Sample('G->ttZ, m(Gp_{Nar})=1750, m(Tp_{Nar,LH})=1300',ROOT.kYellow-3,path+'Zprime*ToZT*Zp1750*Nar*1300*Nar*nominal*Tree*.root',mcweight+'/1.731*11.0','Gprime17501300_ttZ') ,
                    
                    Sample('G->ttZ, m(Gp_{Nar})=2000, m(Tp_{Nar,LH})=1000',ROOT.kOrange-5,path+'Zprime*ToZT*Zp2000*Nar*1000*Nar*LH*nominal*Tree*.root',mcweight+'/1.251*0.54','Gprime20001000_ttZ'),
                    Sample('G->ttZ, m(Gp_{Nar})=2000, m(Tp_{Nar,LH})=1300',ROOT.kOrange-9,path+'Zprime*ToZT*Zp2000*Nar*1300*Nar*LH*nominal*Tree*.root',mcweight+'/1.251*0.54','Gprime20001300_ttZ'),
                    Sample('G->ttZ, m(Gp_{Nar})=2000, m(Tp_{Nar,LH})=1500',ROOT.kOrange+3,path+'Zprime*ToZT*Zp2000*Nar*1500*Nar*nominal*Tree*.root',mcweight+'/0.8246*0.59','Gprime20001500_ttZ') ,
                    
                    Sample('G->ttZ, m(Gp_{Nar})=2250, m(Tp_{Nar,LH})=1300',ROOT.kSpring,path+'Zprime*ToZT*Zp2250*Nar*1300*Nar*nominal*Tree*.root',mcweight+'/0.8246*0.59','Gprime22501300_ttZ') ,
                    Sample('G->ttZ, m(Gp_{Nar})=2250, m(Tp_{Nar,LH})=1500',ROOT.kSpring+2,path+'Zprime*ToZT*Zp2250*Nar*1500*Nar*nominal*Tree*.root',mcweight+'/0.8246*0.59','Gprime22501500_ttZ') ,
                    
                    Sample('G->ttZ, m(Gp_{Nar})=2500, m(Tp_{Nar,LH})=1200',ROOT.kCyan,path+'Zprime*ToZT*Zp2500*Nar*1300*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime25001200_ttZ') ,
                    Sample('G->ttZ, m(Gp_{Nar})=2500, m(Tp_{Nar,LH})=1500',ROOT.kCyan-3,path+'Zprime*ToZT*Zp2500*Nar*1500*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime25001500_ttZ') ,                 
                    Sample('G->ttZ, m(Gp_{Nar})=2500, m(Tp_{Nar,LH})=1800',ROOT.kCyan-7,path+'Zprime*ToZT*Zp2500*Nar*1800*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime25001800_ttZ') ,                 
                 
                    Sample('G->ttZ, m(Gp_{Nar})=2750, m(Tp_{Nar,LH})=1500',ROOT.kPink,path+'Zprime*ToZT*Zp2750*Nar*1500*Nar*nominal*Tree*.root',mcweight+'/1.731*11.0','Gprime27501500_ttZ') ,

                    Sample('G->ttZ, m(Gp_{Nar})=3000, m(Tp_{Nar,LH})=1500',ROOT.kRed+2,path+'Zprime*ToZT*Zp3000*Nar*1500*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime30001500_ttZ') ,
                    Sample('G->ttZ, m(Gp_{Nar})=3000, m(Tp_{Nar,LH})=1800',ROOT.kRed-7,path+'Zprime*ToZT*Zp3000*Nar*1800*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime30001800_ttZ') ,                 
                    Sample('G->ttZ, m(Gp_{Nar})=3000, m(Tp_{Nar,LH})=2100',ROOT.kRed-3,path+'Zprime*ToZT*Zp3000*Nar*2100*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime30002100_ttZ') , 

                    Sample('G->ttZ, m(Gp_{Nar})=3500, m(Tp_{Nar,LH})=1800',ROOT.kGreen,path+'Zprime*ToZT*Zp3500*Nar*1800*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime35001800_ttZ') ,
                    Sample('G->ttZ, m(Gp_{Nar})=3500, m(Tp_{Nar,LH})=2100',ROOT.kGreen+2,path+'Zprime*ToZT*Zp3500*Nar*2100*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime35002100_ttZ') ,                 
                    Sample('G->ttZ, m(Gp_{Nar})=3500, m(Tp_{Nar,LH})=2500',ROOT.kGreen-7,path+'Zprime*ToZT*Zp3500*Nar*2500*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime35002500_ttZ') , 

                    Sample('G->ttZ, m(Gp_{Nar})=4000, m(Tp_{Nar,LH})=2100',ROOT.kBlue-3,path+'Zprime*ToZT*Zp4000*Nar*2100*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime40002100_ttZ') ,
                    Sample('G->ttZ, m(Gp_{Nar})=4000, m(Tp_{Nar,LH})=2500',ROOT.kBlue-5,path+'Zprime*ToZT*Zp4000*Nar*2500*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime40002500_ttZ') ,                 
                    Sample('G->ttZ, m(Gp_{Nar})=4000, m(Tp_{Nar,LH})=3000',ROOT.kBlue-9,path+'Zprime*ToZT*Zp4000*Nar*3000*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime40003000_ttZ') , 
                    
                    
                    
         



                    Sample('G->ttH, m(Gp_{Nar})=1500, m(Tp_{Nar,LH})=800',ROOT.kMagenta,path+'Zprime*ToHT*Zp1500*Nar*800*Nar*nominal*Tree*.root',mcweight+'/3.62*3.5','Gprime1500800_ttH') ,
                    Sample('G->ttH, m(Gp_{Nar})=1500, m(Tp_{Nar,LH})=1000',ROOT.kMagenta+2,path+'Zprime*ToHT*Zp1500*Nar*1000*Nar*nominal*Tree*.root',mcweight+'/3.571*2.6','Gprime15001000_ttH'),
                    Sample('G->ttH, m(Gp_{Nar})=1500, m(Tp_{Nar,LH})=1300',ROOT.kMagenta-7,path+'Zprime*ToHT*Zp1500*Nar*1300*Nar*nominal*Tree*.root',mcweight+'/1.731*11.0','Gprime15001300_ttH') ,
                    
                    Sample('G->ttH, m(Gp_{Nar})=1750, m(Tp_{Nar,LH})=1300',ROOT.kYellow-3,path+'Zprime*ToHT*Zp1750*Nar*1300*Nar*nominal*Tree*.root',mcweight+'/1.731*11.0','Gprime17501300_ttH') ,
                    
                    Sample('G->ttH, m(Gp_{Nar})=2000, m(Tp_{Nar,LH})=1000',ROOT.kOrange-5,path+'Zprime*ToHT*Zp2000*Nar*1000*Nar*LH*nominal*Tree*.root',mcweight+'/1.251*0.54','Gprime20001000_ttH'),
                    #Sample('G->ttH, m(Gp_{Nar})=2000, m(Tp_{Nar,LH})=1300',ROOT.kOrange-9,path+'Zprime*ToHT*Zp2000*Nar*1300*Nar*LH*nominal*Tree*.root',mcweight+'/1.251*0.54','Gprime20001300_ttH'),
                    Sample('G->ttH, m(Gp_{Nar})=2000, m(Tp_{Nar,LH})=1500',ROOT.kOrange+3,path+'Zprime*ToHT*Zp2000*Nar*1500*Nar*nominal*Tree*.root',mcweight+'/0.8246*0.59','Gprime20001500_ttH') ,
                    
                    Sample('G->ttH, m(Gp_{Nar})=2250, m(Tp_{Nar,LH})=1300',ROOT.kSpring,path+'Zprime*ToHT*Zp2250*Nar*1300*Nar*nominal*Tree*.root',mcweight+'/0.8246*0.59','Gprime22501300_ttH') ,
                    Sample('G->ttH, m(Gp_{Nar})=2250, m(Tp_{Nar,LH})=1500',ROOT.kSpring+2,path+'Zprime*ToHT*Zp2250*Nar*1500*Nar*nominal*Tree*.root',mcweight+'/0.8246*0.59','Gprime22501500_ttH') ,
                    
                    Sample('G->ttH, m(Gp_{Nar})=2500, m(Tp_{Nar,LH})=1200',ROOT.kCyan,path+'Zprime*ToHT*Zp2500*Nar*1300*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime25001200_ttH') ,
                    Sample('G->ttH, m(Gp_{Nar})=2500, m(Tp_{Nar,LH})=1500',ROOT.kCyan-3,path+'Zprime*ToHT*Zp2500*Nar*1500*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime25001500_ttH') ,                 
                    Sample('G->ttH, m(Gp_{Nar})=2500, m(Tp_{Nar,LH})=1800',ROOT.kCyan-7,path+'Zprime*ToHT*Zp2500*Nar*1800*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime25001800_ttH') ,                 
                 
                    Sample('G->ttH, m(Gp_{Nar})=2750, m(Tp_{Nar,LH})=1500',ROOT.kPink,path+'Zprime*ToHT*Zp2750*Nar*1500*Nar*nominal*Tree*.root',mcweight+'/1.731*11.0','Gprime27501500_ttH') ,

                    Sample('G->ttH, m(Gp_{Nar})=3000, m(Tp_{Nar,LH})=1500',ROOT.kRed+2,path+'Zprime*ToHT*Zp3000*Nar*1500*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime30001500_ttH') ,
                    Sample('G->ttH, m(Gp_{Nar})=3000, m(Tp_{Nar,LH})=1800',ROOT.kRed-7,path+'Zprime*ToHT*Zp3000*Nar*1800*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime30001800_ttH') ,                 
                    Sample('G->ttH, m(Gp_{Nar})=3000, m(Tp_{Nar,LH})=2100',ROOT.kRed-3,path+'Zprime*ToHT*Zp3000*Nar*2100*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime30002100_ttH') , 

                    Sample('G->ttH, m(Gp_{Nar})=3500, m(Tp_{Nar,LH})=1800',ROOT.kGreen,path+'Zprime*ToHT*Zp3500*Nar*1800*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime35001800_ttH') ,
                    Sample('G->ttH, m(Gp_{Nar})=3500, m(Tp_{Nar,LH})=2100',ROOT.kGreen+2,path+'Zprime*ToHT*Zp3500*Nar*2100*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime35002100_ttH') ,                 
                    Sample('G->ttH, m(Gp_{Nar})=3500, m(Tp_{Nar,LH})=2500',ROOT.kGreen-7,path+'Zprime*ToHT*Zp3500*Nar*2500*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime35002500_ttH') , 

                    Sample('G->ttH, m(Gp_{Nar})=4000, m(Tp_{Nar,LH})=2100',ROOT.kBlue-3,path+'Zprime*ToHT*Zp4000*Nar*2100*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime40002100_ttH') ,
                    Sample('G->ttH, m(Gp_{Nar})=4000, m(Tp_{Nar,LH})=2500',ROOT.kBlue-5,path+'Zprime*ToHT*Zp4000*Nar*2500*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime40002500_ttH') ,                 
                    Sample('G->ttH, m(Gp_{Nar})=4000, m(Tp_{Nar,LH})=3000',ROOT.kBlue-9,path+'Zprime*ToHT*Zp4000*Nar*3000*Nar*nominal*Tree*.root',mcweight+'/0.511*0.26' ,'Gprime40003000_ttH') , 
                                        
                    #Sample("m(Z')=1500, m(T)=700",ROOT.kMagenta,path+'Zprime*ToWB*1500*Nar*700*Nar*nominal*Tree*.root',mcweight+'/95.06*0.80','Zprime1500700_tWb') ,


]

    
    
    

SignalSampleNames=[]
for i in SignalSamples:
    SignalSampleNames.append(i.nick)
