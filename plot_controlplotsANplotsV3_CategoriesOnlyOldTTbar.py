#############
# plot general control distributions
##############

from plotconfigAnalysisV3csvForPSscale import *
sys.path.insert(0, 'limittools')
from limittools import renameHistos

name='controlplotsV12OnlyCategoriesOldTTBar'

# if one wants to plot blinded: True (default: False)
plotBlinded = False

# selections
boosted="(BoostedTopHiggs_TopHadCandidate_TopMVAOutput>=-0.485&&BoostedTopHiggs_HiggsCandidate_HiggsTag>=0.8925)"
toptaggersel="(BoostedJet_Top_Pt[0]>=0)"
higgstaggersel="(BoostedJet_Filterjet2_Pt[0]>=0)"

# definition of categories
categoriesJT=[
              ("(N_Jets==4&&N_BTagsM==2)","4j2t",""),
              ("(N_Jets==5&&N_BTagsM==2)","5j2t",""),
              ("(N_Jets>=6&&N_BTagsM==2)","6j2t",""),
              ("(N_Jets==4&&N_BTagsM==3)","4j3t",""),
              ("(N_Jets==5&&N_BTagsM==3)","5j3t",""),
              ("(N_Jets>=6&&N_BTagsM==3)","6j3t",""),
              ("(N_Jets==4&&N_BTagsM>=4)","4j4t",""),
              ("(N_Jets==5&&N_BTagsM>=4)","5j4t",""),
              ("(N_Jets>=6&&N_BTagsM>=4)","6j4t","")
]

categoriesJTB=[
              ("((N_Jets>=4&&N_BTagsM==2)&&!"+boosted+")","4j2t",""),
              ("((N_Jets>=5&&N_BTagsM==2)&&!"+boosted+")","5j2t",""),
              ("((N_Jets>=6&&N_BTagsM==2)&&!"+boosted+")","6j2t",""),
              ("((N_Jets==4&&N_BTagsM==3)&&!"+boosted+")","4j3t","0.2"),
              ("((N_Jets==5&&N_BTagsM==3)&&!"+boosted+")","5j3t","0.1"),
              ("((N_Jets>=6&&N_BTagsM==3)&&!"+boosted+")","6j3t","0.1"),
              ("((N_Jets==4&&N_BTagsM>=4)&&!"+boosted+")","4j4t","0.2"),
              ("((N_Jets==5&&N_BTagsM>=4)&&!"+boosted+")","5j4t","0.2"),
              ("((N_Jets>=6&&N_BTagsM>=4)&&!"+boosted+")","6j4t","0.1"),
              ("((N_Jets>=4&&N_BTagsM>=2)&&"+boosted+")","boosted","")
]

additionalvariables=[
                      #'finalbdt_ljets_boosted:='+bdtweightpath+'/weights_Final_DB_boosted_76xmem.xml',
                      "Jet_Pt","Jet_Eta","Jet_CSV","Jet_Flav","N_Jets","Weight_CSV","Weight_CSVLFup","Weight_CSVLFdown","Weight_CSVHFup","Weight_CSVHFdown","Weight_CSVHFStats1up","Weight_CSVHFStats1down","Weight_CSVLFStats1up","Weight_CSVLFStats1down","Weight_CSVHFStats2up","Weight_CSVHFStats2down","Weight_CSVLFStats2up","Weight_CSVLFStats2down","Weight_CSVCErr1up","Weight_CSVCErr1down","Weight_CSVCErr2up","Weight_CSVCErr2down",
]

#
#categoriesSplitByBDToptD=[]
#for cat in categoriesJTB:
    #if cat[1] in ["4j4t","5j4t","6j4t"]:
      #categoriesSplitByBDToptD.append(('('+cat[0]+"*(BDT_common5_output<"+cat[2]+"))",cat[1]+"l"))
      #categoriesSplitByBDToptD.append(('('+cat[0]+"*(BDT_common5_output>="+cat[2]+"))",cat[1]+"h"))
    #else:
      #categoriesSplitByBDToptD.append(cat)

# selections for categories
categoriesJTsel="("+categoriesJT[0][0]
for cat in categoriesJT[1:]:
  categoriesJTsel+="||"+cat[0]
categoriesJTsel+=")"

categoriesJTBsel="("+categoriesJTB[0][0]
for cat in categoriesJTB[1:]:
  categoriesJTBsel+="||"+cat[0]
categoriesJTBsel+=")"

# category strings
catstringJT="0"
for i,cat in enumerate(categoriesJT):
    catstringJT+=("+"+str(i+1)+"*"+cat[0])
catstringJTB="0"
for i,cat in enumerate(categoriesJTB):
    catstringJTB+=("+"+str(i+1)+"*"+cat[0])
#catstringSplitByBDToptD="0"
#for i,cat in enumerate(categoriesSplitByBDToptD):
    #catstringSplitByBDToptD+=("+"+str(i+1)+"*"+cat[0])

# samples
samples=samplesControlplotsOLD
samples_data=samples_data_controlplots
systsamples=[]
for sample in samples:
  for sysname,sysfilename in zip(othersystnames,othersystfilenames):
    thisnewsel=sample.selection
    #if sysname=="_CMS_ttH_PSscaleUp":
      #thisnewsel=thisnewsel.replace('*((N_BTagsM>=4)*((0.000919641*(N_GenTopHad==1 && N_GenTopLep==1)+0.0009753747*(N_GenTopLep==2 && N_GenTopHad==0)+0.0084896859*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS)+(0.0084896859/Weight_XS)*(N_BTagsM<4))',
				    #'*((N_BTagsM>=4)*((0.0033838531*(N_GenTopHad==1 && N_GenTopLep==1)+0.0027473283*(N_GenTopLep==2 && N_GenTopHad==0)+0.017175278*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS)+(0.017175278/Weight_XS)*(N_BTagsM<4))')
      #print "weights for scaleUp sample", thisnewsel

    #if sysname=="_CMS_ttH_PSscaleDown":
      #thisnewsel=thisnewsel.replace('*((N_BTagsM>=4)*((0.000919641*(N_GenTopHad==1 && N_GenTopLep==1)+0.0009753747*(N_GenTopLep==2 && N_GenTopHad==0)+0.0084896859*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS)+(0.0084896859/Weight_XS)*(N_BTagsM<4))',
				    #'*((N_BTagsM>=4)*((0.003070913*(N_GenTopHad==1 && N_GenTopLep==1)+0.0027532915*(N_GenTopLep==2 && N_GenTopHad==0)+0.016839284*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS)+(0.016839284/Weight_XS)*(N_BTagsM<4))')
      #print "weights for scaleDown sample", thisnewsel

    #if sysname=="_CMS_scale_jUp":
      #thisnewsel=thisnewsel.replace('*((N_BTagsM>=4)*((0.000919641*(N_GenTopHad==1 && N_GenTopLep==1)+0.0009753747*(N_GenTopLep==2 && N_GenTopHad==0)+0.0084896859*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS)+(0.0084896859/Weight_XS)*(N_BTagsM<4))',
				    #'*((N_BTagsM>=4)*((0.0011192298*(N_GenTopHad==1 && N_GenTopLep==1)+0.0007071164*(N_GenTopLep==2 && N_GenTopHad==0)+0.0084896859*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS)+(0.0084896859/Weight_XS)*(N_BTagsM<4))')
      #print "weights for scaleUp sample", thisnewsel

    #if sysname=="_CMS_scale_jDown":
      #thisnewsel=thisnewsel.replace('*((N_BTagsM>=4)*((0.000919641*(N_GenTopHad==1 && N_GenTopLep==1)+0.0009753747*(N_GenTopLep==2 && N_GenTopHad==0)+0.0084896859*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS)+(0.0084896859/Weight_XS)*(N_BTagsM<4))',
				    #'*((N_BTagsM>=4)*((0.0010096664*(N_GenTopHad==1 && N_GenTopLep==1)+0.0008658787*(N_GenTopLep==2 && N_GenTopHad==0)+0.0084896859*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS)+(0.0084896859/Weight_XS)*(N_BTagsM<4))')

    systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),thisnewsel,sample.nick+sysname))

allsamples=samples+systsamples
allsystnames=weightsystnames+othersystnames

# book plots
plotlabel="1 lepton, #geq 4 jets, #geq 2 b-tags"
plotlabelboosted="#splitline{1 lepton, #geq 4 jets, #geq 2 b-tags}{#geq 1 C/A 1.5 jet p_{T} > 200 GeV}"
plotselection="(N_Jets>=4&&N_BTagsM>=2)"
plots=[
    Plot(ROOT.TH1F("JT" ,"jet-tag categories",len(categoriesJT),0.5,0.5+len(categoriesJT)),catstringJT,categoriesJTsel,"1 lepton"),
    Plot(ROOT.TH1F("BCAT" ,"jet-tag + boosted categories",len(categoriesJTB),0.5,0.5+len(categoriesJTB)),catstringJTB,categoriesJTBsel,"1 lepton"),
    #Plot(ROOT.TH1F("JTsplitByBDToptD" ,"2D analysis D + boosted categories",len(categoriesSplitByBDToptD),0.5,0.5+len(categoriesSplitByBDToptD)),catstringSplitByBDToptD,categoriesJTBsel,"1 lepton"),



]


plotlabel="1 lepton, 4 jets, 2 b-tags"
plotselection="((N_Jets==4&&N_BTagsM==2))"
#plotselection="((N_Jets==4&&N_BTagsM==2)&&!"+boosted+")"

plotprefix="4j2t"
plots42=[

]

plotlabel="1 lepton, 5 jets, 2 b-tags"
plotselection="((N_Jets==5&&N_BTagsM==2))"
#plotselection="((N_Jets==5&&N_BTagsM==2)&&!"+boosted+")"

plotprefix="s52_"
plots52=[

]

plotlabel="1 lepton, 4 jets, 3 b-tags"
plotselection=categoriesJT[1][0]
plotprefix="s43_"
plots43=[

]


plotlabel="1 lepton, 4 jets, 4 b-tags"
plotselection=categoriesJT[4][0]
plotprefix="s44_"
# weights_Final_44_MEMBDTv2.xml
plots44=[

]


plotlabel="1 lepton, 5 jets, 3 b-tags"
plotselection=categoriesJT[2][0]
plotprefix="s53_"
plots53=[

]


plotlabel="1 lepton, 5 jets, #geq4 b-tags"
plotselection=categoriesJT[5][0]
plotprefix="s54_"
plots54=[

]


plotlabel="1 lepton, #geq6 jets, 2 b-tags"
plotselection=categoriesJT[0][0]
plotprefix="s62_"
plots62=[

]


plotlabel="1 lepton, #geq6 jets, 3 b-tags"
plotselection=categoriesJT[3][0]
plotprefix="s63_"
plots63=[

]

plotlabel="1 lepton, #geq6 jets, #geq4 b-tags"
plotselection=categoriesJT[6][0]
plotprefix="s64"
plots64=[

]

plotlabel="boosted"
plotselection=categoriesJTB[7][0]
plotprefix="sboosted_"
plotsBoosted=[

]

#bdtplots=plots64+plots63+plots62+plots54+plots53+plots44+plots43+plotsBoosted+plots42+plots52
#plots+=bdtplots
#plots+=plots62+plots63

print name,500000,plots,samples+samples_data,[''],['1.'],weightsystnames, systweights
outputpath=plotParallel(name,500000,plots,samples+samples_data+systsamples,[''],['1.'],weightsystnames, systweights,additionalvariables,[],"")

# plot dataMC comparison
listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots,1)
if not os.path.exists(outputpath[:-4]+'_syst.root') or not askYesNo('reuse systematic histofile?'):
    renameHistos(outputpath,outputpath[:-4]+'_syst.root',allsystnames,False)
lll=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots,errorSystnames)
#lllcsv=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots,CSVSystnames)
exit(0)
#for hld,hl in zip(listOfHistoListsData,listOfHistoLists):

  #makeEventyields=False

  #if "optD" in hld[0].GetName():
    #makeEventyields=True
    #for h in hld+hl:
      #for i,cat in enumerate(categoriesSplitByBDToptD):
        #h.GetXaxis().SetBinLabel(i+1,cat[1])
    #tablepath=("/".join((outputpath.split('/'))[:-1]))+"/"+name+"_yieldsD"
  ##elif "JTB" in hld[0].GetName():
    ##makeEventyields=True
    ##for h in hld+hl:
      ##for i,cat in enumerate(categoriesJTB):
        ##h.GetXaxis().SetBinLabel(i+1,cat[1])
    ##tablepath=("/".join((outputpath.split('/'))[:-1]))+"/"+name+"_yieldsJTB"
  #elif "JT" in hld[0].GetName():
    #makeEventyields=True
    #for h in hld+hl:
      #for i,cat in enumerate(categoriesJT):
        #h.GetXaxis().SetBinLabel(i+1,cat[1])
    #tablepath=("/".join((outputpath.split('/'))[:-1]))+"/"+name+"_yieldsJT"

  ## make an event yield table
  #if makeEventyields:
    #eventYields(hld,hl,samples,tablepath)

labels=[plot.label for plot in plots]
#lolT=transposeLOL(listOfHistoLists)
#plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],-1,name,[[lll,3354,ROOT.kBlack,False]],False,labels,True,plotBlinded)

#exit(0)

# make log plots
#listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
#listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots,1)
#lll=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots,errorSystnames)
##lllcsv=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots,CSVSystnames)
#labels=[plot.label for plot in plots]
#lolT=transposeLOL(listOfHistoLists)
#plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],-1,name+'_log',[[lll,3354,ROOT.kBlack,False]],True,labels,True,plotBlinded)

# make category plots
categoryplotsindex=3
listOfHistoListsForCategories=createHistoLists_fromSuperHistoFile(outputpath,samples,plots[:categoryplotsindex],1)
listOfHistoListsDataForCategories=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots[:categoryplotsindex],1)
lllForCategories=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots[:categoryplotsindex],errorSystnames)

listOfcustomBinLabels=[]

categoriesJTlist=[]
for i,cat in enumerate(categoriesJT):
  categoriesJTlist.append(cat[1])
#categoriesJTBlist=[]
#for i,cat in enumerate(categoriesJTB):
  #categoriesJTBlist.append(cat[1])
#categoriesSplitByBDToptDlist=[]
#for i,cat in enumerate(categoriesSplitByBDToptD):
  #categoriesSplitByBDToptDlist.append(cat[1])

listOfcustomBinLabels=[categoriesJTlist]
labels=[plot.label for plot in plots[:categoryplotsindex]]
lolT=transposeLOL(listOfHistoListsForCategories)
plotDataMCanWsystCustomBinLabels(listOfHistoListsDataForCategories,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],-1,name+'Categories_log',[[lllForCategories,3354,ROOT.kBlack,True]],listOfcustomBinLabels,True,labels,True,plotBlinded)



# make category plots
# again without log
categoryplotsindex=3
listOfHistoListsForCategoriesNL=createHistoLists_fromSuperHistoFile(outputpath,samples,plots[:categoryplotsindex],1)
listOfHistoListsDataForCategoriesNL=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots[:categoryplotsindex],1)
lllForCategoriesNL=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots[:categoryplotsindex],errorSystnames)

listOfcustomBinLabels=[]

categoriesJTlist=[]
for i,cat in enumerate(categoriesJT):
  categoriesJTlist.append(cat[1])
#categoriesJTBlist=[]
#for i,cat in enumerate(categoriesJTB):
  #categoriesJTBlist.append(cat[1])
#categoriesSplitByBDToptDlist=[]
#for i,cat in enumerate(categoriesSplitByBDToptD):
  #categoriesSplitByBDToptDlist.append(cat[1])

listOfcustomBinLabels=[categoriesJTlist]
labels=[plot.label for plot in plots[:categoryplotsindex]]
lolTNL=transposeLOL(listOfHistoListsForCategoriesNL)
plotDataMCanWsystCustomBinLabels(listOfHistoListsDataForCategoriesNL,transposeLOL(lolTNL[1:]),samples[1:],lolTNL[0],samples[0],-1,name+'Categories_nolog',[[lllForCategoriesNL,3354,ROOT.kBlack,True]],listOfcustomBinLabels,False,labels,True,plotBlinded)
