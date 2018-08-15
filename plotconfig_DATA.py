import sys
import os
from scriptgenerator import *
from plotutils import *
from plot_cuts_DATA import *

    
if WWP=='medium':
  weightsystnamesABCD=[
                    #"_" + ABCDversion + "_ABCD_rateUp",
                    #"_" + ABCDversion + "_ABCD_rateDown",
                    #"_" + ABCDversion + "_ABCD_shapeUp",
                    #"_" + ABCDversion + "_ABCD_shapeDown",
                ]

 
    
if WWP=='medium':
    systweightsABCD=[
                    
                    #"" + ABCDversion + "_ABCD_rateUp:=ABCD_rate_systUp*(DoABCDsyst==1)+MCSF_Weight_" + ABCDversion +"*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"" + ABCDversion + "_ABCD_rateDown:=ABCD_rate_systDown*(DoABCDsyst==1)+MCSF_Weight_" + ABCDversion +"*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"" + ABCDversion + "_ABCD_shapeUp:=ABCD_shape_systUp*(DoABCDsyst==1)+MCSF_Weight_" + ABCDversion +"*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"" + ABCDversion + "_ABCD_shapeDown:=ABCD_shape_systDown*(DoABCDsyst==1)+MCSF_Weight_" + ABCDversion +"*(DoMCDataWeights==1)*(DoABCDsyst==0)",
            
    ]
                    #"nom:=1",r

        
        
else:
    print "Wrong WPs"
    raw_input()

weigthsystnamesMCSFs=[
                    #"_CSV_nominal",
                    #"_CSV_MCSF_systUp",
                    #"_CSV_MCSF_systDown",
                    #"_CSV_nominal",
                    
                    "",
                    
                    "_" + ABCDversion + "_nominal",
                    
                    
    ]
        
murmufttbar=[
1.14398309396,0.880338673747,1.11578278373,0.897477695732,1.01990637208,0.975146721204
]        
        
        
murmufGstars=[#muR20muF20,muR05muF05,muR20muF10,muR05muF10,muR10muF20,muR10muF05
[0.902298845069,1.07357151428,0.793411397192,1.12920371887,0.844779183017,1.06331345473],    #1500
[0.913541564396,1.07114310217,0.788859891827,1.11569334394,0.847201881135,1.06331345473],    #1750
[0.923842764153,1.06855988154,0.785227925426,1.10349024658,0.849681375230,1.08020214758],    #2000
[0.933137438387,1.06592639902,0.781691305888,1.09273276844,0.851738871894,1.08020214758],    #2250
[0.941522478977,1.06328174834,0.777840522115,1.08333081305,0.853184006575,1.09440158723],    #2500  
[0.949449385820,1.06058432115,0.774780218314,1.07448235922,0.854855062329,1.09440158723],    #2750  
[0.956902394754,1.05792270536,0.770967744269,1.06648128262,0.855854021111,1.09440158723],    #3000  
[0.970622717239,1.05270948818,0.764547328234,1.05195774915,0.857959613747,1.09440158723],    #3500  
[0.982975177373,1.04780254477,0.758514448366,1.03929120896,0.859612665386,1.09440158723],    #4000  
]

PDFs=[#up,nom,down
[1.0288470061,0.999995245877,0.971444146978], #ttbar
[1.02618668223,1.01276267314,0.998067037169], #ST_tW
[1.04814946491,1.00197069002,0.955144380386], #ST_tchan
[1.03544739238,0.997517372968,0.960994153179], #ST_schan
]

murmufs_top=[#muR20muF20,muR05muF05,muR20muF10,muR05muF10,muR10muF20,muR10muF05
[0.874574174107,1.1388502408,0.896019776743,1.11628283834,0.980364592389,1.02627873744], #ttbar
[1.0,1.0,1.0,1.0,1.0,1.0], #ST_tW
[0.938219368911,1.07628580446,0.938669629912,1.06973536078,1.00220725786,1.00267219394], #ST_tchan
[0.970196290724,1.03718157851,0.94667594817,1.06582801936,1.0246660911,0.973056764591], #ST_schan
]

systweightnamesMCSFs=[
                    #"CSV_nominal:=(1)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"CSV_MCSF_systUp:=(1*(1+1.15))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"CSV_MCSF_systDown:=(1*(1-1.15))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0", 
                    
                    "nom:=1.0",
                    
                    "" + ABCDversion + "_nominal:=(DoWeights*DoMCDataWeights==0)*triggered",
                    
                    
                    

    ]
    

print weigthsystnamesMCSFs
print systweightnamesMCSFs

assert len(weigthsystnamesMCSFs)==len(systweightnamesMCSFs)


otherSystNames=[
    "_JERUp","_JERDown",
    "_JESUp","_JESDown",



]

otherSystFileNames=[
    "JERup","JERdown",
    "JESup","JESdown",
]

JECsystnames=[
    "_" + ABCDversion + "_nominal_JERUp","_" + ABCDversion + "_nominal_JERDown",
    "_" + ABCDversion + "_nominal_JESUp","_" + ABCDversion + "_nominal_JESDown",

]

assert len(otherSystNames)==len(JECsystnames)

#allweightsystnames=weigthsystnamesbasic+weightsystnamesMadgraphbantiZprimeM+weightsystnamesPythia8bantiZprimeM+weightsystnamesMadgraphtantiTopPt+weightsystnamesPythia8tantiTopPt+weightsystnamesGeneratorDiffMadgraphbantiZprimeM+weightsystnamesGeneratorDiffPythia8bantiZprimeM+weightsystnamesGeneratorDiffMadgraphtantiTopPt+weightsystnamesGeneratorDiffPythia8tantiTopPt+weightsystnamesMadgraphbantiZprimeMWithtopbtag+weightsystnamesPythia8bantiZprimeMWithtopbtag+weightsystnamesGeneratorDiffMadgraphbantiZprimeMWithtopbtag+weightsystnamesGeneratorDiffPythia8bantiZprimeMWithtopbtag+weightsystnamesMadgraphtantiTopPtWithtopbtag+weightsystnamesPythia8tantiTopPtWithtopbtag+weightsystnamesGeneratorDiffMadgraphtantiTopPtWithtopbtag+weightsystnamesGeneratorDiffPythia8tantiTopPtWithtopbtag+weightsystnamesABCD+weigthsystnamesMCSFs
##allweightsystnames=weightsystnamesABCD

#allsystweights=systweightsbasic+systweightsMadgraphbantiZprimeM+systweightsPythia8bantiZprimeM+systweightsMadgraphtantiTopPt+systweightsPythia8tantiTopPt+systweightsGeneartorDiffMadgraphbantiZprimeM+systweightsGeneartorDiffPythia8bantiZprimeM+systweightsGeneartorDiffMadgraphtantiTopPt+systweightsGeneartorDiffPythia8tantiTopPt+systweightsMadgraphbantiZprimeMWithtopbtag+systweightsPythia8bantiZprimeMWithtopbtag+systweightsGeneartorDiffMadgraphbantiZprimeMWithtopbtag+systweightsGeneartorDiffPythia8bantiZprimeMWithtopbtag+systweightsMadgraphtantiTopPtWithtopbtag+systweightsPythia8tantiTopPtWithtopbtag+systweightsGeneartorDiffMadgraphtantiTopPtWithtopbtag+systweightsGeneartorDiffPythia8tantiTopPtWithtopbtag+systweightsABCD+systweightnamesMCSFs
##allsystweights=systweightsABCD

#ABweightsystnames=weigthsystnamesbasic+weightsystnamesMadgraphbantiZprimeM+weightsystnamesPythia8bantiZprimeM+weightsystnamesMadgraphtantiTopPt+weightsystnamesPythia8tantiTopPt+weightsystnamesGeneratorDiffMadgraphbantiZprimeM+weightsystnamesGeneratorDiffPythia8bantiZprimeM+weightsystnamesGeneratorDiffMadgraphtantiTopPt+weightsystnamesGeneratorDiffPythia8tantiTopPt+weightsystnamesMadgraphbantiZprimeMWithtopbtag+weightsystnamesPythia8bantiZprimeMWithtopbtag+weightsystnamesGeneratorDiffMadgraphbantiZprimeMWithtopbtag+weightsystnamesGeneratorDiffPythia8bantiZprimeMWithtopbtag+weightsystnamesMadgraphtantiTopPtWithtopbtag+weightsystnamesPythia8tantiTopPtWithtopbtag+weightsystnamesGeneratorDiffMadgraphtantiTopPtWithtopbtag+weightsystnamesGeneratorDiffPythia8tantiTopPtWithtopbtag+weigthsystnamesMCSFs

#ABsystweights=systweightsbasic+systweightsMadgraphbantiZprimeM+systweightsPythia8bantiZprimeM+systweightsMadgraphtantiTopPt+systweightsPythia8tantiTopPt+systweightsGeneartorDiffMadgraphbantiZprimeM+systweightsGeneartorDiffPythia8bantiZprimeM+systweightsGeneartorDiffMadgraphtantiTopPt+systweightsGeneartorDiffPythia8tantiTopPt+systweightsMadgraphbantiZprimeMWithtopbtag+systweightsPythia8bantiZprimeMWithtopbtag+systweightsGeneartorDiffMadgraphbantiZprimeMWithtopbtag+systweightsGeneartorDiffPythia8bantiZprimeMWithtopbtag+systweightsMadgraphtantiTopPtWithtopbtag+systweightsPythia8tantiTopPtWithtopbtag+systweightsGeneartorDiffMadgraphtantiTopPtWithtopbtag+systweightsGeneartorDiffPythia8tantiTopPtWithtopbtag+systweightnamesMCSFs
     
#allweightsystnames=weigthsystnamesMCSFs+weightsystnamesABCD+JECsystnames
allweightsystnames=weigthsystnamesMCSFs

allsystweights=systweightnamesMCSFs

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
path_80x_MC="/nfs/dust/cms/user/skudella/processed_MC/flat_trees_new/"
path_80x_DATA="/nfs/dust/cms/user/skudella/processed_DATA/flat_trees/"


#DATA_MC_rate_scalefactor_QCD='0.506626268137'
#DATA_MC_rate_scalefactor_QCD='0.681942750822'
DATA_MC_rate_scalefactor_QCD='0.761444753045'


#BackgroundSamples=[
                    #Sample('ttbar',ROOT.kBlue-4,path_80x_MC+'BKG_TTbar/*nominal*.root',mcweight+'/'+ttbarXS_MCgen+'*'+ttbarXS_NLO,'ttbar',allweightsystnames) ,
                    ##Sample('Top background',ROOT.kBlue-4,path_80x_MC+'BKG_TTbar/*nominal*.root',mcweight+'/'+ttbarXS_MCgen+'*'+ttbarXS_NLO,'ttbar',allweightsystnames) ,
                    #Sample('single top (tW-channel)',ROOT.kBlue+2,path_80x_MC+'BKG_ST/*ST*tW*nominal*.root',mcweight,'ST_tW',allweightsystnames) ,
                    #Sample('single top (t-channel)',ROOT.kBlue-9,path_80x_MC+'BKG_ST/*ST*t-channel*nominal*.root',mcweight,'ST_t',allweightsystnames) ,
                    #Sample('single top (s-channel)',ROOT.kBlue-7,path_80x_MC+'BKG_ST/*ST*s-channel*nominal*.root',mcweight,'ST_s',allweightsystnames) ,
                    ##Sample('QCD from MC',ROOT.kOrange-3,path_80x_MC+'BKG_QCD/*QCD_H*nominal*Tree*.root',mcweight,'QCDMadgraph',allweightsystnames),
#]


DataSamples=[
                    Sample('data',ROOT.kBlack,path_80x_DATA+'*nominal*.root','1.0','DATA_2016'),
]




#samplenames=[]
#for i in samples:
    #samplenames.append(i.nick)
#SignalSampleNames=[]
#for i in SignalSamples:
    #SignalSampleNames.append(i.nick)
#BackgroundSampleNames=[]
#for i in BackgroundSamples:
    #BackgroundSampleNames.append(i.nick)
DataSampleNames=[]
for i in DataSamples:
    DataSampleNames.append(i.nick)
  
#samples=BackgroundSamples+DataSamples

#samplenames=BackgroundSampleNames+DataSampleNames

  
samples=DataSamples

samplenames=DataSampleNames




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


