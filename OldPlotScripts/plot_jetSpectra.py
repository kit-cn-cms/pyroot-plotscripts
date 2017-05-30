#############
# plot general control distributions
##############

from plotconfigjetSpectra import *
sys.path.insert(0, 'limittools')
from limittools import renameHistos

name='jetSpectra'

# if one wants to plot blinded: True (default: False)
plotBlinded = False

bdtset="V4"
additionalvariables=[
                    "Muon_Pt","Electron_Pt","Muon_Eta","Electron_Eta","Jet_Pt","Jet_Eta","Jet_CSV","Jet_Flav","N_Jets","Weight_CSV","Weight_CSVLFup","Weight_CSVLFdown","Weight_CSVHFup","Weight_CSVHFdown","Weight_CSVHFStats1up","Weight_CSVHFStats1down","Weight_CSVLFStats1up","Weight_CSVLFStats1down","Weight_CSVHFStats2up","Weight_CSVHFStats2down","Weight_CSVLFStats2up","Weight_CSVLFStats2down","Weight_CSVCErr1up","Weight_CSVCErr1down","Weight_CSVCErr2up","Weight_CSVCErr2down",
]

# selections
boosted="(BoostedTopHiggs_TopHadCandidate_TopMVAOutput>=-0.485&&BoostedTopHiggs_HiggsCandidate_HiggsTag>=0.8925)"
toptaggersel="(BoostedJet_Top_Pt[0]>=0)"
higgstaggersel="(BoostedJet_Filterjet2_Pt[0]>=0)"

# definition of categories
categoriesJT=[
              ("(N_Jets>=6&&N_BTagsM==2)","6j2t",""),
              ("(N_Jets==4&&N_BTagsM==3)","4j3t",""),
              ("(N_Jets==5&&N_BTagsM==3)","5j3t",""),
              ("(N_Jets>=6&&N_BTagsM==3)","6j3t",""),
              ("(N_Jets==4&&N_BTagsM>=4)","4j4t",""),
              ("(N_Jets==5&&N_BTagsM>=4)","5j4t",""),
              ("(N_Jets>=6&&N_BTagsM>=4)","6j4t","")
]


# selections for categories
categoriesJTsel="("+categoriesJT[0][0]
for cat in categoriesJT[1:]:
  categoriesJTsel+="||"+cat[0]
categoriesJTsel+=")"


# category strings
catstringJT="0"
for i,cat in enumerate(categoriesJT):
    catstringJT+=("+"+str(i+1)+"*"+cat[0])
#catstringJTB="0"
#for i,cat in enumerate(categoriesJTB):
    #catstringJTB+=("+"+str(i+1)+"*"+cat[0])

# samples
samples=samplesControlPlots
samples_data=samples_data_controlplots
systsamples=[]
for sample in samples:
  for sysname,sysfilename in zip(othersystnames,othersystfilenames):
    thisnewsel=sample.selection
    systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),thisnewsel,sample.nick+sysname))

allsamples=samples+systsamples
allsystnames=weightsystnames+othersystnames

# book plots
plotlabel="1 lepton, #geq 4 jets, #geq 2 b-tags"
plotselection="(N_Jets>=4&&N_BTagsM>=2)"
plots=[
    Plot(ROOT.TH1F("JetFlavPt20to30" ,"JetFlavPt20to30",10,-1,9),"Jet_Flav",plotselection+"*(Jet_Pt>=20&&Jet_Pt<30)","1 lepton, #geq 4 jets, #geq 2 b-tags"),
    Plot(ROOT.TH1F("JetFlavPt30to40" ,"JetFlavPt30to40",10,-1,9),"Jet_Flav",plotselection+"*(Jet_Pt>=30&&Jet_Pt<40)","1 lepton, #geq 4 jets, #geq 2 b-tags"),    
    Plot(ROOT.TH1F("JetFlavPt40to60" ,"JetFlavPt40to60",10,-1,9),"Jet_Flav",plotselection+"*(Jet_Pt>=40&&Jet_Pt<60)","1 lepton, #geq 4 jets, #geq 2 b-tags"),    
    Plot(ROOT.TH1F("JetFlavPt60to100" ,"JetFlavPt60to100",10,-1,9),"Jet_Flav",plotselection+"*(Jet_Pt>=60&&Jet_Pt<100)","1 lepton, #geq 4 jets, #geq 2 b-tags"),    
    Plot(ROOT.TH1F("JetFlavPt100to1000" ,"JetFlavPt100to1000",10,-1,9),"Jet_Flav",plotselection+"*(Jet_Pt>=100&&Jet_Pt<1000)","1 lepton, #geq 4 jets, #geq 2 b-tags"), 
    Plot(ROOT.TH1F("JetFlavPt30to50" ,"JetFlavPt30to50",10,-1,9),"Jet_Flav",plotselection+"*(Jet_Pt>=30&&Jet_Pt<50)","1 lepton, #geq 4 jets, #geq 2 b-tags"),
    Plot(ROOT.TH1F("JetFlavPt50to70" ,"JetFlavPt50to70",10,-1,9),"Jet_Flav",plotselection+"*(Jet_Pt>=50&&Jet_Pt<70)","1 lepton, #geq 4 jets, #geq 2 b-tags"),    
    Plot(ROOT.TH1F("JetFlavPt70to100" ,"JetFlavPt70to100",10,-1,9),"Jet_Flav",plotselection+"*(Jet_Pt>=70&&Jet_Pt<100)","1 lepton, #geq 4 jets, #geq 2 b-tags"),    
]




print name,2000000,plots,samples+samples_data,[''],['1.'],weightsystnames, systweights
outputpath=plotParallel(name,2000000,plots,samples,[''],['1.'],weightsystnames, systweights,additionalvariables,[],"/nfs/dust/cms/user/kelmorab/plotscriptsSpring17/pyroot-plotscripts/treejson_Spring117v2p1_ttbarincl.json")

# plot dataMC comparison
listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
#listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots,1)
#if not os.path.exists(outputpath[:-4]+'_syst.root') or not askYesNo('reuse systematic histofile?'):
    #renameHistos(outputpath,outputpath[:-4]+'_syst.root',allsystnames,False)
#lll=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots,errorSystnames)


#labels=[plot.label for plot in plots]
##lolT=transposeLOL(listOfHistoLists)
#plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],-1,name,[[lll,3354,ROOT.kBlack,True]],False,labels,True,plotBlinded)

exit(0)

