import sys
import os
from scriptgenerator_minimal import *
from plotutils import *


# names of the systematics (proper names needed e.g. for combination)
mcweight='35.9'


ttbarXS_MCgen='730.0'
ttbarXS_NLO='831.76' 

# samples
# input path
path_80x="/nfs/dust/cms/user/skudella/processed_MC/flat_trees_new/"
path="/pnfs/desy.de/cms/tier2/store/user/skudella/*/MC_minimal_minimal_*/*/*/*minimal*"

# MC samples (name, color, path to files,weight,nickname_without_special_characters,systematics)

SignalSamples=[
                    Sample('ttbar',ROOT.kBlue-4,path+'MC_Ttbar*nominal*.root',mcweight+'/'+ttbarXS_MCgen+'*'+ttbarXS_NLO,'ttbar') ,
                    #Sample('Top background',ROOT.kBlue-4,path_80x_MC+'BKG_TTbar/*nominal*.root',mcweight+'/'+ttbarXS_MCgen+'*'+ttbarXS_NLO,'ttbar',allweightsystnames) ,
                    Sample('single top (tW-channel)',ROOT.kBlue+2,path+'*MC_st*tWchan*nominal*.root',mcweight,'ST_tW') ,
                    Sample('single top (t-channel)',ROOT.kBlue-9,path+'*MC_st*tchan*nominal*.root',mcweight,'ST_t') ,
                    Sample('single top (s-channel)',ROOT.kBlue-7,path+'*MC_st*schan*nominal*.root',mcweight,'ST_s') ,
]

    
    
    

SignalSampleNames=[]
for i in SignalSamples:
    SignalSampleNames.append(i.nick)
