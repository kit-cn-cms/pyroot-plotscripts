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
mcweight='2.0*2.5*(Evt_Odd==0)'
mcweightSBKG='2.5'

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
nhistobins=    [1, 1, 1000,1000,1000,1000,1000,1000,1000]
#old minxvals= [0., 0., -0.87, -0.89, -0.94, -0.7, -0.84, -0.87, -0.58 ]
#old maxxvals= [5000., 5000., 0.88, 0.9, 0.9, 0.72, 0.87, 0.87, 0.8]
minxvals= [0., 0.,      -0.88, -0.9, -0.94, -0.7, -0.84, -0.87, -0.6 ]
maxxvals= [5000., 5000., 0.89,  0.5,  0.9,   0.3,  0.87,  0.87,  0.15]
#minxvals= [0., 0., -1,-1,-1,-1,-1,-1,-1]
#maxxvals= [5000., 5000., 1,1,1,1,1,1,1]


bdts=[]
for b,bl,nb,minx,maxx in zip(bins,binlabels,nhistobins,minxvals,maxxvals):
  if bl=="jge6_tge4":
    bdts.append(MVAPlot(ROOT.TH1F("BDT_ljets"+"_"+bl,"BDT_ljets"+" ("+bl+")",nb,minx,maxx),"/nfs/dust/cms/user/kelmorab/weights0116/weights_Final_64_64MEMBDTRecoVars.xml",b))
  elif bl=="j5_tge4":
    bdts.append(MVAPlot(ROOT.TH1F("BDT_ljets"+"_"+bl,"BDT_ljets"+" ("+bl+")",nb,minx,maxx),"/nfs/dust/cms/user/kelmorab/weights0116/weights_Final_54_54MEMBDToldVars.xml",b))
  elif bl=="j4_t4":
    bdts.append(MVAPlot(ROOT.TH1F("BDT_ljets"+"_"+bl,"BDT_ljets"+" ("+bl+")",nb,minx,maxx),"/nfs/dust/cms/user/kelmorab/weights0116/weights_Final_44_44MEMBDToldVars.xml",b))
  elif bl=="j4_t2" or bl=="j5_t2":
    bdts.append(Plot(ROOT.TH1F("BDT_ljets"+"_"+bl,"BDT_ljets"+" ("+bl+")",nb,minx,maxx),"Evt_HT",b))  
  else:    
    bdts.append(Plot(ROOT.TH1F("BDT_ljets"+"_"+bl,"BDT_ljets"+" ("+bl+")",nb,minx,maxx),"BDT_common5_output",b))

outputpath=plotParallel(name,1000000,bdts,allsamples,[''],['1.'],weightsystnames, systweights)
renameHistos(outputpath,name+'_limitInput.root',allsystnames)
addPseudoData(name+'_limitInput.root',[s.name for s in samples[1:]],binlabels,allsystnames)

listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,bdts)
writeListOfHistoLists(listOfHistoLists,allsamples,'',name,False)
