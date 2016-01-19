from scriptgenerator import *
from plotutils import *
import sys
sys.path.insert(0, 'limittools')
from limittools import renameHistos
from limittools import addPseudoData

path='/nfs/dust/cms/user/hmildner/trees0108/'
pathDB='/nfs/dust/cms/user/kelmorab/trees0108/'
name='bdtplots_parrallel_test'

#mcweight='(2.54*Weight_TopPt)*(N_LooseElectrons==0||N_LooseMuons==0)' 
mcweight='2.0*2.61*(Evt_Odd==0)'
mcweightSBKG='2.54'

samples=[Sample('t#bar{t}H',ROOT.kBlue+1,path+'/ttH*/*nominal*.root',mcweight,'ttH125') ,     
         Sample('t#bar{t}+l',ROOT.kRed-7,path+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)','ttbarOther') ,     
         Sample('t#bar{t}+c#bar{c}',ROOT.kRed,path+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==1)','ttbarPlusCCbar') ,     
         Sample('t#bar{t}+b',ROOT.kRed+2,path+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==1)','ttbarPlusB') ,     
         Sample('t#bar{t}+2b',ROOT.kRed+3,path+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==2)','ttbarPlus2B') ,
         Sample('t#bar{t}+b#bar{b}',ROOT.kRed+4,path+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==3)','ttbarPlusBBbar') ,     
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

othersystnames=["_CMS_scale_jUp",
                "_CMS_scale_jDown",
#                "_CMS_res_jUp",
#                "_CMS_res_jDown"
                ]
allsystnames=weightsystnames+othersystnames

othersystfilenames=["JESUP",
                    "JESDOWN",
#                    "JERUP",
#                    "JERDOWN"
                    ]

# corresponding weight names
systweights=["1",
             "Weight_CSVLFup","Weight_CSVLFdown","Weight_CSVHFup","Weight_CSVHFdown",
             "Weight_CSVHFStats1up","Weight_CSVHFStats1down","Weight_CSVLFStats1up","Weight_CSVLFStats1down",
             "Weight_CSVHFStats2up","Weight_CSVHFStats2down","Weight_CSVLFStats2up","Weight_CSVLFStats2down",
             "Weight_CSVCErr1up","Weight_CSVCErr1down","Weight_CSVCErr2up","Weight_CSVCErr2down"]


systsamples=[]
for sample in samples:
  for sysname,sysfilename in zip(othersystnames,othersystfilenames):
    systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),sample.selection,sample.nick+sysname))
  
allsamples=samples+systsamples

# definition of analysis bins
s4j2t="(N_Jets==4&&N_BTagsM==2)"
s5j2t="(N_Jets==5&&N_BTagsM==2)"
s4j3t="(N_Jets==4&&N_BTagsM==3)"
s4j4t="(N_Jets==4&&N_BTagsM>=4)"
s5j3t="(N_Jets==5&&N_BTagsM==3)"
s5j4t="(N_Jets==5&&N_BTagsM>=4)"
s6j2t="(N_Jets>=6&&N_BTagsM==2)"
s6j3t="(N_Jets>=6&&N_BTagsM==3)"
s6j4t="(N_Jets>=6&&N_BTagsM>=4)"
bins=     [s4j2t,s5j2t,s4j3t,s4j4t,s5j3t,s5j4t,s6j2t,s6j3t,s6j4t]
# corresponding labels
binlabels=["j4_t2","j5_t2","j4_t3","j4_t4","j5_t3","j5_tge4","jge6_t2","jge6_t3","jge6_tge4"]
# number of bins in each category
nhistobins=    [1, 1, 20,    10,    20,    10      ,20,   20,    10]
minxvals= [0., 0., -0.87, -0.8, -0.94, -0.86, -0.84, -0.87, -0.71 ]
maxxvals= [5000., 5000., 0.88, 0.82, 0.9, 0.9, 0.87, 0.87, 0.65]

bdts=[]
for b,bl,nb,minx,maxx in zip(bins,binlabels,nhistobins,minxvals,maxxvals):
  if bl=="j4_t2" or bl=="j5_t2":
    bdts.append(Plot(ROOT.TH1F("BDT_ljets"+"_"+bl,"BDT_ljets"+" ("+bl+")",nb,minx,maxx),"Evt_HT",b))  
  else:    
    bdts.append(Plot(ROOT.TH1F("BDT_ljets"+"_"+bl,"BDT_ljets"+" ("+bl+")",nb,minx,maxx),"BDT_common5_output",b))

outputpath=plotParallel(name,1000000,bdts,allsamples,[''],['1.'],weightsystnames, systweights)
renameHistos(outputpath,name+'_limitInput.root',allsystnames)
addPseudoData(name+'_limitInput.root',[s.nick for s in samples[1:]],binlabels,allsystnames)

listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,bdts)
#writeListOfHistoLists(listOfHistoLists,allsamples,'',name,False)
lolT=transposeLOL(listOfHistoLists)
writeLOLAndOneOnTop(transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],20,name)
