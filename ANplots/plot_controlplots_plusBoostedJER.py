#############
# plot general control distributions 
##############


from plotconfigJER import *
sys.path.insert(0, '../limittools')
from limittools import renameHistos

name='76controlplotsPlusBoosted_JER'

samples=samplesControlPlots
samples_data=samples_data_controlplots
systsamples=[]
for sample in samples:
  for sysname,sysfilename in zip(othersystnames,othersystfilenames):
    thisnewsel=sample.selection
    systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),thisnewsel,sample.nick+sysname))

allsamples=samples
allsystnames=weightsystnames

#                                                 B C D
boosted="(BoostedTopHiggs_TopHadCandidate_TopMVAOutput>=-0.485&&BoostedTopHiggs_HiggsCandidate_HiggsTag>=0.8925)"                        
categoriesJT=[("((N_Jets>=6&&N_BTagsM==2)&&!"+boosted+")","6j2t","","",""),
              ("((N_Jets==4&&N_BTagsM==3)&&!"+boosted+")","4j3t","0.2","0.2","0.2"),
              ("((N_Jets==5&&N_BTagsM==3)&&!"+boosted+")","5j3t","0.15","0.15","0.15"),
              ("((N_Jets>=6&&N_BTagsM==3)&&!"+boosted+")","6j3t","0.1","0.1","0.1"),
              ("((N_Jets==4&&N_BTagsM>=4)&&!"+boosted+")","4j4t","0.2","0.2","0.2"),
              ("((N_Jets==5&&N_BTagsM>=4)&&!"+boosted+")","5j4t","0.2","0.2","0.2"),             
              ("((N_Jets>=6&&N_BTagsM>=4)&&!"+boosted+")","6j4t","0.1","0.1","0.1"),
              ("((N_Jets>=4&&N_BTagsM>=2)&&"+boosted+")","boosted","0.1","0.1","0.1")]

categoriesSplitBDT=[]
categoriesSplitBDT.append(categoriesJT[0])
for cat in categoriesJT[1:]:
    categoriesSplitBDT.append(('('+cat[0]+"*(BDT_common5_output<"+cat[2]+"))",cat[1]+"l"))
    categoriesSplitBDT.append(('('+cat[0]+"*(BDT_common5_output>="+cat[2]+"))",cat[1]+"h"))

categoriesBDT=[]
categoriesBDT.append(categoriesJT[0])
for cat in categoriesJT[1:]:
    categoriesBDT.append(cat)

categoriesSplitByBDToptD=[]
categoriesSplitByBDToptD.append(categoriesJT[0])
for cat in categoriesJT[1:]:
    if cat[1] in ["4j4t","5j4t","6j4t"]:
      categoriesSplitByBDToptD.append(('('+cat[0]+"*(BDT_common5_output<"+cat[2]+"))",cat[1]+"l"))
      categoriesSplitByBDToptD.append(('('+cat[0]+"*(BDT_common5_output>="+cat[2]+"))",cat[1]+"h"))
    else:
      categoriesSplitByBDToptD.append(cat)

    
# book plots
label="1 lepton, #geq 4 jets, #geq 2 b-tags"
catstringJT="0"
for i,cat in enumerate(categoriesJT):
    catstringJT+=("+"+str(i+1)+"*"+cat[0])
catstringSplitByBDT="0"
for i,cat in enumerate(categoriesSplitBDT):
    catstringSplitByBDT+=("+"+str(i+1)+"*"+cat[0])
catstringBDT="0"
for i,cat in enumerate(categoriesBDT):
    catstringBDT+=("+"+str(i+1)+"*"+cat[0])
catstringSplitByBDToptD="0"
for i,cat in enumerate(categoriesSplitByBDToptD):
    catstringSplitByBDToptD+=("+"+str(i+1)+"*"+cat[0])

plots=[
       Plot(ROOT.TH1F("JT" ,"jet-tag categories",9,-0.5,8.5),"3*max(min(N_BTagsM-2,2),0)+max(min(N_Jets-4,2),0)","(N_BTagsM>=2&&N_Jets>=4)",label),
       Plot(ROOT.TH1F("JTByBDToptC" ,"analysis C + boosted categories",len(categoriesBDT),0.5,0.5+len(categoriesBDT)),catstringBDT,"(((N_BTagsM>=2&&N_Jets>=6||N_BTagsM>=3&&N_Jets>=4)&&!"+categoriesJT[-1][0]+")||"+categoriesJT[-1][0]+")"),
       Plot(ROOT.TH1F("N_Jets","Number of ak4 jets",7,3.5,10.5),"N_Jets",'',label),
       Plot(ROOT.TH1F("N_BTagsM","Number of b-tags",4,1.5,5.5),"N_BTagsM",'',label),
]

# plot parallel -- alternatively there are also options to plot more traditional that also return lists of histo lists
outputpath=plotParallel(name,2000000,plots,samples+samples_data+systsamples,[''],['1.'],weightsystnames, systweights)

listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots,1)
if not os.path.exists(outputpath[:-4]+'_syst.root') or not askYesNo('reuse systematic histofile?'):
    renameHistos(outputpath,outputpath[:-4]+'_syst.root',allsystnames)
print othersystnames
lll=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots,errorSystnames)

# plot dataMC comparison
labels=[plot.label for plot in plots]

lolT=transposeLOL(listOfHistoLists)
plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],20,name,[[lll,3354,ROOT.kGray+1,True]],False,labels)
