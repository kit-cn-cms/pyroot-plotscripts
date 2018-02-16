import sys
import os
sys.path.append('pyroot-plotscripts-base')
sys.path.append('pyroot-plotscripts-base/limittools')

from scriptgenerator import *
from plotutils import *

# names of the systematics (proper names needed e.g. for combination)
weightSystNames=[
                    "",
]

systsAllSamples=[
                    "",
]

mcWeightAll='35.91823'
mcWeight='35.91823*2.0'

systWeights=[
                    #"NomWeight:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*(DoWeights==1)+(DoWeights==0)*1.0",
                    "NomWeight:=1.0",
                   
]

assert len(systWeights)==len(weightSystNames)

otherSystNames=[
  
]

otherSystFileNames=[
 

]

# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
sampleDict=SampleDictionary()
sampleDict.doPrintout()


print "controlsamples"
samplesControlPlots=[
                    Sample('t#bar{t}H',ROOT.kBlue+1,"/nfs/dust/cms/user/areitter/output/ttHbb3/ttHbb_*_nominal_Tree.root",mcWeightAll,'ttH',systsAllSamples,samDict=sampleDict) ,     
#                    Sample('t#bar{t}',ROOT.kRed+1,path_80x+'/ttbar/*nominal*.root',mcWeight,'ttbar',systsAllSamples) ,     
                    Sample('t#bar{t}',ROOT.kRed-7,"/nfs/dust/cms/user/areitter/output/ttbar3/ttbar_incl_*_nominal_Tree.root",mcWeightAll,'ttbarOther',systsAllSamples,samDict=sampleDict),
]

