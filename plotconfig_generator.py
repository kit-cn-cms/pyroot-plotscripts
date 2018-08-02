import sys
import os
from scriptgenerator import *
from plotutils import *
from plot_cuts_ZPrime_MC import *

   
# names of the systematics (proper names needed e.g. for combination)
mcweight='35.9'

ttbarXS_MCgen='730.0'
ttbarXS_NLO='831.76' 
rateunc_ttbarXS_Up=math.sqrt(19.77*19.77 + 35.06*35.06)
rateunc_ttbarXS_Down=math.sqrt(29.20*29.20 + 35.06*35.06)

doBR=True

if doBR:
    BR_name="BR05_025_025"

if BR_name is "BR05_025_025":
    BR=[0.5,0.25,0.25]



sfs="Weight_ElectronSFID*Weight_ElectronSFTrigger*Weight_ElectronSFIso*Weight_MuonSFID*Weight_MuonSFTrigger*Weight_MuonSFIso"
usualweights="(1*Weight_PU*((Weight>0)-(Weight<0)))*Weight_ElectronSFID*Weight_ElectronSFTrigger*Weight_ElectronSFIso*Weight_MuonSFID*Weight_MuonSFTrigger*Weight_MuonSFIso"


# samples
# input path 
path_80x="/nfs/dust/cms/user/skudella/processed_MC/flat_trees_new/"
#path_80x="/nfs/dust/cms/user/skudella/processed_MC/flat_trees_old/"

#DATA_MC_rate_scalefactor_QCD='0.506626268137'
#DATA_MC_rate_scalefactor_QCD='0.681942750822'
#DATA_MC_rate_scalefactor_QCD='0.761444753045'

SignalSamples=[
                    
                    Sample('m_{Z\'}=1.5 TeV, m_{T}=0.7 TeV',ROOT.kMagenta,path_80x+'Signal_Zprime/Zprime*ToWB*1500*700*nominal*Tree.root',mcweight+'/95.06*0.80','SigZprime1500700_tWb'),
                    Sample('m_{Z\'}=1.5 TeV, m_{T}=0.9 TeV',ROOT.kMagenta-9,path_80x+'Signal_Zprime/Zprime*ToWB*1500*900*nominal*Tree.root',mcweight+'/138.07*1.5','SigZprime1500900_tWb'),
                    Sample('m_{Z\'}=1.5 TeV, m_{T}=1.2 TeV',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Zprime*ToWB*1500*1200*nominal*Tree.root',mcweight+'/99.03*8.6','SigZprime15001200_tWb'),
                    Sample('m_{Z\'}=2.0 TeV, m_{T}=0.9 TeV',ROOT.kCyan,path_80x+'Signal_Zprime/Zprime*ToWB*2000*900*nominal*Tree.root',mcweight+'/55.83*0.21','SigZprime2000900_tWb'),
                    Sample('m_{Z\'}=2.0 TeV, m_{T}=1.2 TeV',ROOT.kCyan-9,path_80x+'Signal_Zprime/Zprime*ToWB*2000*1200*LH*nominal*Tree.root',mcweight+'/86.28*0.27','SigZprime20001200_tWb'),
                    Sample('m_{Z\'}=2.0 TeV, m_{T}=1.5 TeV',ROOT.kCyan+2,path_80x+'Signal_Zprime/Zprime*ToWB*2000*1500*nominal*Tree.root',mcweight+'/83.47*0.90','SigZprime20001500_tWb'),
                    Sample('m_{Z\'}=2.5 TeV, m_{T}=1.2 TeV',ROOT.kRed,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1200*nominal*Tree.root',mcweight+'/37.6*0.33','SigZprime25001200_tWb'),
                    Sample('m_{Z\'}=2.5 TeV, m_{T}=1.5 TeV',ROOT.kRed-9,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1500*nominal*Tree.root',mcweight+'/53.9*0.29','SigZprime25001500_tWb'),
                    ]



#samplenames=[]
#for i in samples:
    #samplenames.append(i.nick)
SignalSampleNames=[]
for i in SignalSamples:
    SignalSampleNames.append(i.nick)
#BackgroundSampleNames=[]
#for i in BackgroundSamples:
    #BackgroundSampleNames.append(i.nick)
#DataSampleNames=[]
#for i in DataSamples:
    #DataSampleNames.append(i.nick)
  
#samples=SignalSamples+BackgroundSamples+DataSamples

#samplenames=SignalSampleNames+BackgroundSampleNames+DataSampleNames




#systsamples=[]
#for sample,samplename in zip(samples,samplenames):
 #if (( 'QCDMadgraph' not in samplename ) and ( 'QCDPythia8' not in samplename ) and ( 'BKG' not in samplename ) and ( 'DATA' not in samplename ) ):   
  #for sysname,sysfilename in zip(otherSystNames,otherSystFileNames):
    #thisnewsel=sample.selection
    #systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),thisnewsel,sample.nick+sysname))
    ##DataSampleNames.append(sample.nick+sysname)
    #print 'with JEC ', sample.path

 #else:
  #for sysname,sysfilename in zip(otherSystNames,otherSystFileNames):
    #thisnewsel=sample.selection
    #systsamples.append(Sample(sample.name+sysname,sample.color,sample.path,thisnewsel,sample.nick+sysname))
    ##DataSampleNames.append(sample.nick+sysname)  
    #print 'no JEC ', sample.path


