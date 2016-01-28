from scriptgenerator import *
from plotutils import *
import sys
import os
sys.path.insert(0, 'limittools')
from limittools import renameHistos
from limittools import addPseudoData
from limittools import makeDatacards
from limittools import calcLimits

path='/nfs/dust/cms/user/hmildner/treesMEM0126/'
name='bdtwithmem'
mcweight='2.0*2.5*(Evt_Odd==0)'
nhistobins=      [ 20,          10,         20,         10,       20,    20,  10     ]
minxvals=        [-1]*7
maxxvals=        [1.]*7
discrs =          ["BDT_common5_output"]*7



categories=[("(N_Jets==4&&N_BTagsM==3)","ljets_j4_t3"),
            ("(N_Jets==4&&N_BTagsM>=4)","ljets_j4_t4"),
            ("(N_Jets==5&&N_BTagsM==3)","ljets_j5_t3"),
            ("(N_Jets==5&&N_BTagsM>=4)","ljets_j5_tge4"),
            ("(N_Jets>=6&&N_BTagsM==2)","ljets_jge6_t2"),
            ("(N_Jets>=6&&N_BTagsM==3)","ljets_jge6_t3"),
            ("(N_Jets>=6&&N_BTagsM>=4)","ljets_jge6_tge4")]


discrname='BDT'

bins= [c[0] for c in categories]
binlabels= [c[1] for c in categories]

samples=[Sample('t#bar{t}H',ROOT.kBlue+1,path+'/ttHbb/*nominal*.root',mcweight,'ttH125') ,     
         Sample('t#bar{t}+l',ROOT.kRed-7,path+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)','ttbarOther') ,     
         Sample('t#bar{t}+c#bar{c}',ROOT.kRed,path+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==1)','ttbarPlusCCbar') ,     
         Sample('t#bar{t}+b',ROOT.kRed+2,path+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==1)','ttbarPlusB') ,     
         Sample('t#bar{t}+2b',ROOT.kRed+3,path+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==2)','ttbarPlus2B') ,
         Sample('t#bar{t}+b#bar{b}',ROOT.kRed+4,path+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==3)','ttbarPlusBBbar') ,     
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

bdts=[]
for discr,b,bl,nb,minx,maxx in zip(discrs,bins,binlabels,nhistobins,minxvals,maxxvals):
  if bl=="ljets_jge6_tge4":
    bdts.append(MVAPlot(ROOT.TH1F("BDT"+"_"+bl,"BDT"+" ("+bl+")",nb,minx,maxx),"/nfs/dust/cms/user/kelmorab/weights0116/weights_Final_64_64MEMBDTRecoVars.xml",b))
  elif bl=="ljets_j5_tge4":
    bdts.append(MVAPlot(ROOT.TH1F("BDT"+"_"+bl,"BDT"+" ("+bl+")",nb,minx,maxx),"/nfs/dust/cms/user/kelmorab/weights0116/weights_Final_54_54MEMBDToldVars.xml",b))
  elif bl=="ljets_j4_t4":
    bdts.append(MVAPlot(ROOT.TH1F("BDT"+"_"+bl,"BDT"+" ("+bl+")",nb,minx,maxx),"/nfs/dust/cms/user/kelmorab/weights0116/weights_Final_44_44MEMBDToldVars.xml",b))
  else:
    bdts.append(Plot(ROOT.TH1F(discrname+"_"+bl,"BDT ("+bl+")",nb,minx,maxx),discr,b))

outputpath=plotParallel(name,200000,bdts,allsamples,[''],['1.'],weightsystnames, systweights)
if not os.path.exists(name):
  os.makedirs(name)

renameHistos(outputpath,name+'/'+name+'_limitInput.root',allsystnames)
addPseudoData(name+'/'+name+'_limitInput.root',[s.nick for s in samples[1:]],binlabels,allsystnames,discrname)

listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,bdts)
lolT=transposeLOL(listOfHistoLists)
writeLOLAndOneOnTop(transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],20,name+'/'+name+'_controlplots')
makeDatacards(name+'/'+name+'_limitInput.root',name+'/'+name+'_datacard',binlabels)

#if askYesNo('Calculate limits?'):
calcLimits(name+'/'+name+'_datacard',binlabels)
  
