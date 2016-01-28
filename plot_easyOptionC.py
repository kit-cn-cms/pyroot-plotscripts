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
name='easyOptionC'
mcweight='2.0*2.5*(Evt_Odd==0)'
nhistobins_=      [ 20,       10,     20,       10,   20,   20,  10    ]
minxvals_=        [-0.9,   -0.35,  -0.8, -0.75,   -0.80,  -0.8, -0.6]
maxxvals_=        [0.8,     0.5,  0.8,    0.75,    0.76,   0.8,   0.7]
discrs =          ['/nfs/dust/cms/user/kelmorab/MEMstudies/3makeHistosAndCards/weights/weights_Final_43_MEMBDTv2.xml', '/nfs/dust/cms/user/kelmorab/MEMstudies/3makeHistosAndCards/weights/weights_Final_44_MEMBDTv2.xml', '/nfs/dust/cms/user/kelmorab/MEMstudies/3makeHistosAndCards/weights/weights_Final_53_MEMBDTv2.xml', '/nfs/dust/cms/user/kelmorab/MEMstudies/3makeHistosAndCards/weights/weights_Final_54_MEMBDTv2.xml' , 'BDT_common5_output','/nfs/dust/cms/user/kelmorab/MEMstudies/3makeHistosAndCards/weights/weights_Final_63_MEMBDTv2.xml','/nfs/dust/cms/user/kelmorab/MEMstudies/3makeHistosAndCards/weights/weights_Final_64_MEMBDTv2.xml']

nhistobins=[]
minxvals=[]
maxxvals=[]
for n in nhistobins_:
  nhistobins.append(n)
for x in minxvals_:
  minxvals.append(x)
#  minxvals.append(x)
for x in maxxvals_:
  maxxvals.append(x)
#  maxxvals.append(x)

categories_=[("(N_Jets==4&&N_BTagsM==3)","ljets_j4_t3"),
            ("(N_Jets==4&&N_BTagsM>=4)","ljets_j4_t4"),
            ("(N_Jets==5&&N_BTagsM==3)","ljets_j5_t3"),
            ("(N_Jets==5&&N_BTagsM>=4)","ljets_j5_tge4"),
            ("(N_Jets>=6&&N_BTagsM==2)","ljets_jge6_t2"),
            ("(N_Jets>=6&&N_BTagsM==3)","ljets_jge6_t3"),
            ("(N_Jets>=6&&N_BTagsM>=4)","ljets_jge6_tge4")]
categories=[]
#blrcuts=[1.34,6.56,2.39,
#         6.86,-0.552,3.21,7.06]
blrcuts=[2.14,7.55,3.12,7.63,0.19,3.91,7.67]
bdtcuts=[0.199,0.217,0.129,0.217,0.091,0.108,0.121]
#j4_t3 BDT_blr_ -0.290966014877
#j4_t3 BLR_ 1.37683990748
#j4_t4 BDT_blr_ -0.160885207987
#j4_t4 BLR_ 6.5647594931
#j5_t3 BDT_blr_ -0.241945770323
#j5_t3 BLR_ 2.385700423
#j5_tge4 BDT_blr_ -0.170663547327
#j5_tge4 BLR_ 6.86461242473
#jge6_t2 BDT_blr_ -0.243206660866
#jge6_t2 BLR_ -0.551654104151
#jge6_t3 BDT_blr_ -0.207576303689
#jge6_t3 BLR_ 3.20986324993
#jge6_tge4 BDT_blr_ -0.143261847899
#jge6_tge4 BLR_ 7.05715952903 

for cat,bdt in zip(categories_,bdtcuts):
  #if cat[1] in ["ljets_jge6_tge4","ljets_j5_tge4","ljets_j4_t4"]:
    #categories.append(('('+cat[0]+')*(BDT_common5_output>'+str(bdt)+')',cat[1]+'_high') )
    #categories.append(('('+cat[0]+')*(BDT_common5_output<='+str(bdt)+')',cat[1]+'_low') )
  #else:
    categories.append(cat )
print categories


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
print len(discrs),len(bins),len(binlabels),len(nhistobins),len(minxvals),len(maxxvals),
print len(zip(discrs,bins,binlabels,nhistobins,minxvals,maxxvals))
for discr,b,bl,nb,minx,maxx in zip(discrs,bins,binlabels,nhistobins,minxvals,maxxvals):
  if '.xml' in discr:
    bdts.append(MVAPlot(ROOT.TH1F(discrname+"_"+bl,"final dicsriminator ("+bl+")",nb,minx,maxx),discr,b))
  else:
    bdts.append(Plot(ROOT.TH1F(discrname+"_"+bl,"final dicsriminator ("+bl+")",nb,minx,maxx),discr,b))
  print discr,b,bl,nb,minx,maxx

print "if cateries are correct press the \"any\" key"
raw_input()

outputpath=plotParallel(name,1000000,bdts,allsamples,[''],['1.'],weightsystnames, systweights)
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
  
