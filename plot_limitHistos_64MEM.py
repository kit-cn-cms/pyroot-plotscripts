from scriptgenerator import *
from plotutils import *
import sys

path='/nfs/dust/cms/user/kelmorab/treesMEM/'
pathDB='/nfs/dust/cms/user/kelmorab/trees0108/'
name='bdtplots_parrallel'

#mcweight='(2.54*Weight_TopPt)*(N_LooseElectrons==0||N_LooseMuons==0)' 
mcweight='2.0*2.54*(Evt_Odd==0)'
mcweightSBKG='2.54'

samples=[Sample('ttH125',ROOT.kBlue+1,path+'/ttH*/*nominal*.root',mcweight,'ttH125') ,     
         Sample('ttbarOther',ROOT.kRed+1,path+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)','ttbarOther') ,     
         Sample('ttbarPlusCCbar',ROOT.kRed+2,path+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==1)','ttbarPlusCCbar') ,     
         Sample('ttbarPlusBBbar',ROOT.kRed+3,path+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==3)','ttbarPlusBBbar') ,     
         Sample('ttbarPlusB',ROOT.kRed+4,path+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==1)','ttbarPlusB') ,     
         Sample('ttbarPlus2B',ROOT.kRed+5,path+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==2)','ttbarPlus2B') ,
#         Sample('singlet',ROOT.kMagenta,path+'/st*/*nominal*.root',mcweightSBKG,'singlet') ,
#         Sample('wjets',ROOT.kGreen-3,path+'/WJets*/*nominal*.root',mcweightSBKG,'wjets') ,
#         Sample('zjets',ROOT.kAzure-3,path+'/Zjets*/*nominal*.root',mcweightSBKG,'zjets') ,
#         Sample('ttbarZ',ROOT.kGray,path+'/ttZ*/*nominal*.root',mcweightSBKG,'ttbarZ') ,
#         Sample('ttbarW',ROOT.kGray+5,path+'/ttW*/*nominal*.root',mcweightSBKG,'ttbarW') ,
#         Sample('diboson',ROOT.kBlue-2,pathDB+'/DiBoson*/*nominal*.root',mcweightSBKG,'diboson') ,
]

# names of the systematics (proper names needed e.g. for combination)
weightsystnames=["",
           "_CMS_ttH_CSVLFUp","_CMS_ttH_CSVLFDown","_CMS_ttH_CSVHFUp","_CMS_ttH_CSVHFDown",
           "_CMS_ttH_CSVHFStats1Up","_CMS_ttH_CSVHFStats1Down","_CMS_ttH_CSVLFStats1Up","_CMS_ttH_CSVLFStats1Down",
           "_CMS_ttH_CSVHFStats2Up","_CMS_ttH_CSVHFStats2Down","_CMS_ttH_CSVLFStats2Up","_CMS_ttH_CSVLFStats2Down",
           "_CMS_ttH_CSVCErr1Up","_CMS_ttH_CSVCErr1Down","_CMS_ttH_CSVCErr2Up","_CMS_ttH_CSVCErr2Down"]

# corresponding weight names
systweights=["1",
             "Weight_CSVLFup","Weight_CSVLFdown","Weight_CSVHFup","Weight_CSVHFdown",
             "Weight_CSVHFStats1up","Weight_CSVHFStats1down","Weight_CSVLFStats1up","Weight_CSVLFStats1down",
             "Weight_CSVHFStats2up","Weight_CSVHFStats2down","Weight_CSVLFStats2up","Weight_CSVLFStats2down",
             "Weight_CSVCErr1up","Weight_CSVCErr1down","Weight_CSVCErr2up","Weight_CSVCErr2down"]

# create extra samples with special weights
samples_syst=[]
for sn,sw in zip(weightsystnames,systweights):
    for sample in samples:
        ss=sw
        if sample.selection != '':
            ss='('+sample.selection+')*'+ss
        samples_syst.append(Sample(sample.name+sn,sample.color,sample.path,ss,sample.nick+sn))

samples_jesup=[]
for sample in samples:
  samples_jesup.append(Sample(sample.name+'_CMS_scale_jUp',sample.color,sample.path.replace("nominal","JESUP"),sample.selection,sample.nick+"_CMS_scale_jUp"))

samples_jesdown=[]
for sample in samples:
  samples_jesdown.append(Sample(sample.name+'_CMS_scale_jDown',sample.color,sample.path.replace("nominal","JESDOWN"),sample.selection,sample.nick+"_CMS_scale_jDown"))

#samples_jerdown=[]
#for sample in samples:
  #samples_jerdown.append(Sample(sample.name+'_CMS_res_jDown',sample.color,sample.path.replace("nominal","JERDOWN"),sample.selection,sample.nick+"_CMS_res_jDown"))
  
#samples_jerup=[]
#for sample in samples:
  #samples_jerup.append(Sample(sample.name+'_CMS_res_jUp',sample.color,sample.path.replace("nominal","JERUP"),sample.selection,sample.nick+"_CMS_res_jUp"))  

#plots=[Plot(ROOT.TH1F("BDTcommon5xc","BDTcommon5xc",20,-1,1),"BDT_common5_output"),
       #]

#allsamples=samples_syst+samples_jerdown+samples_jerup+samples_jesdown+samples_jesup
allsamples=samples_syst+samples_jesdown+samples_jesup

# definition of analysis bins
s4j3t="(N_Jets==4&&N_BTagsM==3)"
s4j4t="(N_Jets==4&&N_BTagsM>=4)"
s5j3t="(N_Jets==5&&N_BTagsM==3)"
s5j4t="(N_Jets==5&&N_BTagsM>=4)"
s6j2t="(N_Jets>=6&&N_BTagsM==2)"
s6j3t="(N_Jets>=6&&N_BTagsM==3)"
s6j4t="(N_Jets>=6&&N_BTagsM>=4)"
bins=     [s6j4t]
# corresponding labels
binlabels=["jge6_tge4"]
# number of bins in each category
nhistobins=    [10]
minxvals= [0.0]
maxxvals= [1.0]

#minxvals= [-1, -1, -1, -1, -1, -1, -1 ]
#maxxvals= [ 1,  1,  1,  1,  1,  1,  1 ]

bdts=[]
for b,bl,nb,minx,maxx in zip(bins,binlabels,nhistobins,minxvals,maxxvals):
    bdts.append(Plot(ROOT.TH1F("BDT_ljets"+"_"+bl,"BDT_ljets"+" ("+bl+")",nb,minx,maxx),"MEM_p",b))


outputpath=plotParallel(name,2000000,bdts,allsamples)
listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,allsamples,bdts)
writeListOfHistoLists(listOfHistoLists,allsamples,name,'')
