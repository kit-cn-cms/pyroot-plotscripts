

#############
# plot general control distributions 
##############


from plotconfig import *
sys.path.insert(0, '../limittools')
from limittools import renameHistos

name='76controlplotsPlusBoostedOnlyCats'

# selections for categories
sel1="((N_TightLeptons==1)*(N_LooseLeptons==1)*(N_BTagsM>=2)*(N_Jets>=4))" # l+jets channel
sl42sel="((N_TightLeptons==1)*(N_LooseLeptons==1)*(N_BTagsM>=2)*(N_Jets>=4))" # l+jets channel

name1="1lge4ge2"

toptaggersel="(BoostedJet_Top_Pt[0]>=0)"
higgstaggersel="(BoostedJet_Filterjet2_Pt[0]>=0)"
samples=samplesControlPlots
samples_data=samples_data_controlplots
systsamples=[]
for sample in samples:
  for sysname,sysfilename in zip(othersystnames,othersystfilenames):
    thisnewsel=sample.selection
    if sysname=="_CMS_ttH_PSscaleUp":
      thisnewsel=thisnewsel.replace('*(0.000919641*(N_GenTopHad==1 && N_GenTopLep==1)+0.000707116*(N_GenTopLep==2 && N_GenTopHad==0)+0.0084896859*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS','*(0.003106675*(N_GenTopHad==1 && N_GenTopLep==1)+0.00251279*(N_GenTopLep==2 && N_GenTopHad==0)+0.017175278*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS')
      print "weights for scaleUp sample ", thisnewsel
    if sysname=="_CMS_ttH_PSscaleDown":
      thisnewsel=thisnewsel.replace('*(0.000919641*(N_GenTopHad==1 && N_GenTopLep==1)+0.000707116*(N_GenTopLep==2 && N_GenTopHad==0)+0.0084896859*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS','*(0.003070913*(N_GenTopHad==1 && N_GenTopLep==1)+0.002519151*(N_GenTopLep==2 && N_GenTopHad==0)+0.016839284*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS')
      print "weights for scaleDown sample ", thisnewsel
    systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),thisnewsel,sample.nick+sysname))

systsamples=[]
othersystnames=[]

allsamples=samples+systsamples
allsystnames=weightsystnames+othersystnames

# Categorization Options
boosted="(BoostedTopHiggs_TopHadCandidate_TopMVAOutput>=-0.485&&BoostedTopHiggs_HiggsCandidate_HiggsTag>=0.8925)"                        
categoriesBasic=[ ("((N_Jets>=6&&N_BTagsM==2)&&!"+boosted+")","6j2t","","",""),
                  ("((N_Jets==4&&N_BTagsM==3)&&!"+boosted+")","4j3t","0.2","0.2","0.2"),
                  ("((N_Jets==5&&N_BTagsM==3)&&!"+boosted+")","5j3t","0.15","0.15","0.15"),
                  ("((N_Jets>=6&&N_BTagsM==3)&&!"+boosted+")","6j3t","0.1","0.1","0.1"),
                  ("((N_Jets==4&&N_BTagsM>=4)&&!"+boosted+")","4j4t","0.2","0.2","0.2"),
                  ("((N_Jets==5&&N_BTagsM>=4)&&!"+boosted+")","5j4t","0.2","0.2","0.2"),             
                  ("((N_Jets>=6&&N_BTagsM>=4)&&!"+boosted+")","6j4t","0.1","0.1","0.1"),
                  ("((N_Jets>=4&&N_BTagsM>=2)&&"+boosted+")","boosted","0.1","0.1","0.1")]

allcategoriessel="("+categoriesBasic[0][0]
for cat in categoriesBasic[1:]:
  allcategoriessel+="||"+cat[0]
allcategoriessel+=")"

print allcategoriessel

categoriesJT=[]
for cat in categoriesBasic[:-1]:
    categoriesJT.append(cat)
    
categoriesSplitBDT=[]
categoriesSplitBDT.append(categoriesBasic[0])
for cat in categoriesBasic[1:]:
    categoriesSplitBDT.append(('('+cat[0]+"*(BDT_common5_output<"+cat[2]+"))",cat[1]+"l"))
    categoriesSplitBDT.append(('('+cat[0]+"*(BDT_common5_output>="+cat[2]+"))",cat[1]+"h"))
    
categoriesBDT=[]
categoriesBDT.append(categoriesBasic[0])
for cat in categoriesBasic[1:]:
    categoriesBDT.append(cat)

categoriesSplitByBDToptD=[]
categoriesSplitByBDToptD.append(categoriesBasic[0])
for cat in categoriesBasic[1:]:
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
catstringBasic="0"
for i,cat in enumerate(categoriesBasic):
    catstringBasic+=("+"+str(i+1)+"*"+cat[0])
catstringSplitByBDT="0"
for i,cat in enumerate(categoriesSplitBDT):
    catstringSplitByBDT+=("+"+str(i+1)+"*"+cat[0])
catstringBDT="0"
for i,cat in enumerate(categoriesBDT):
    catstringBDT+=("+"+str(i+1)+"*"+cat[0])
catstringSplitByBDToptD="0"
for i,cat in enumerate(categoriesSplitByBDToptD):
    catstringSplitByBDToptD+=("+"+str(i+1)+"*"+cat[0])

plots=[Plot(ROOT.TH1F("JT" ,"jet-tag categories",len(categoriesJT),0.5,0.5+len(categoriesJT)),catstringJT,allcategoriessel,label),
       Plot(ROOT.TH1F("Basic" ,"categories",len(categoriesBasic),0.5,0.5+len(categoriesBasic)),catstringBasic,allcategoriessel,label),
       #Plot(ROOT.TH1F("JTsplitByBDToptB" ,"2D analysis B + boosted categories",len(categoriesSplitBDT),0.5,0.5+len(categoriesSplitBDT)),catstringSplitByBDT,"",label),
       #Plot(ROOT.TH1F("JTByBDToptC" ,"analysis C + boosted categories",len(categoriesBDT),0.5,0.5+len(categoriesBDT)),catstringBDT,"",label),
       Plot(ROOT.TH1F("JTsplitByBDToptD" ,"2D analysis D + boosted categories",len(categoriesSplitByBDToptD),0.5,0.5+len(categoriesSplitByBDToptD)),catstringSplitByBDToptD,allcategoriessel,label),
]

# plot parallel -- alternatively there are also options to plot more traditional that also return lists of histo lists
outputpath=plotParallel(name,2000000,plots,samples+samples_data,[''],['1.'],weightsystnames, systweights)

############
# make category plots
listOfHistoListsForCategories=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
listOfHistoListsDataForCategories=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots,1)
if not os.path.exists(outputpath[:-4]+'_syst.root') or not askYesNo('reuse systematic histofile?'):
  renameHistos(outputpath,outputpath[:-4]+'_syst.root',allsystnames)
lllForCategories=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots,[''])

for hld,hl in zip(listOfHistoListsDataForCategories,listOfHistoListsForCategories):
  
  if "JT" in hld[0].GetName() and not "JTsplitByBDToptB" in hld[0].GetName() and not "JTByBDToptC" in hld[0].GetName() and not "JTsplitByBDToptD" in hld[0].GetName() :
    tablepath=("/".join((outputpath.split('/'))[:-1]))+"/"+name+"_yieldsJT"
  elif "Basic" in hld[0].GetName():       
    tablepath=("/".join((outputpath.split('/'))[:-1]))+"/"+name+"_yieldsBasic"
  elif "JTsplitByBDToptB" in hld[0].GetName():       
    tablepath=("/".join((outputpath.split('/'))[:-1]))+"/"+name+"_yieldsB"
  elif "JTByBDToptC" in hld[0].GetName():       
    tablepath=("/".join((outputpath.split('/'))[:-1]))+"/"+name+"_yieldsC"
  elif "JTsplitByBDToptD" in hld[0].GetName():       
    tablepath=("/".join((outputpath.split('/'))[:-1]))+"/"+name+"_yieldsD"

  # make an event yield table
  eventYields(hld,hl,samples,tablepath)
    

listOfcustomBinLabels=[]

categoriesJTlist=[]
for i,cat in enumerate(categoriesJT):
  categoriesJTlist.append(cat[1])             
categoriesBasiclist=[]
for i,cat in enumerate(categoriesBasic):
  categoriesBasiclist.append(cat[1])             
categoriesSplitBDTlist=[]
for i,cat in enumerate(categoriesSplitBDT):
  categoriesSplitBDTlist.append(cat[1])             
categoriesBDTlist=[]
for i,cat in enumerate(categoriesBDT):
  categoriesBDTlist.append(cat[1])
categoriesSplitByBDToptDlist=[]
for i,cat in enumerate(categoriesSplitByBDToptD):
  categoriesSplitByBDToptDlist.append(cat[1])

listOfcustomBinLabels=[categoriesJTlist,categoriesBasiclist,categoriesSplitByBDToptDlist]               
labels=[plot.label for plot in plots]
lolT=transposeLOL(listOfHistoListsForCategories)
plotDataMCanWsystCustomBinLabels(listOfHistoListsDataForCategories,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],20,name+'Categories_log',[[lllForCategories,3354,ROOT.kGray+1,True]],listOfcustomBinLabels,True,labels,True)
