from plotconfig import *
sys.path.insert(0, '../limittools')
from limittools import renameHistos

name='AN_controlplots_plusBoosted'

# selections for categories
sel1="((N_TightLeptons==1)*(N_LooseLeptons==1)*(N_BTagsM>=2)*(N_Jets>=4))" # l+jets channel
name1="1lge4ge2"

toptaggersel="(BoostedJet_Top_Pt[0]>=0)"
higgstaggersel="(BoostedJet_Filterjet2_Pt[0]>=0)"
samples=samplesControlPlots
samples_data=samples_data_controlplots
systsamples=[]
for sample in samples:
  for sysname,sysfilename in zip(othersystnames,othersystfilenames):
    systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),sample.selection,sample.nick+sysname))
  
allsamples=samples+systsamples
allsystnames=weightsystnames+othersystnames

#                                                 B C D
boosted="(BoostedTopHiggs_TopHadCandidate_TopMVAOutput>=-0.575&&BoostedTopHiggs_HiggsCandidate_HiggsTag>=0.9075)"                        
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

plots=[Plot(ROOT.TH1F("JT" ,"jet-tag categories",len(categoriesJT),0.5,0.5+len(categoriesJT)),catstringJT,"(((N_BTagsM>=2&&N_Jets>=6||N_BTagsM>=3&&N_Jets>=4)&&!"+categoriesJT[-1][0]+")||"+categoriesJT[-1][0]+")",label),
       Plot(ROOT.TH1F("JTsplitByBDToptB" ,"2D analysis B + boosted categories",len(categoriesSplitBDT),0.5,0.5+len(categoriesSplitBDT)),catstringSplitByBDT,"(((N_BTagsM>=2&&N_Jets>=6||N_BTagsM>=3&&N_Jets>=4)&&!"+categoriesJT[-1][0]+")||"+categoriesJT[-1][0]+")"),
       Plot(ROOT.TH1F("JTByBDToptC" ,"analysis C + boosted categories",len(categoriesBDT),0.5,0.5+len(categoriesBDT)),catstringBDT,"(((N_BTagsM>=2&&N_Jets>=6||N_BTagsM>=3&&N_Jets>=4)&&!"+categoriesJT[-1][0]+")||"+categoriesJT[-1][0]+")"),
       Plot(ROOT.TH1F("JTsplitByBDToptD" ,"2D analysis D + boosted categories",len(categoriesSplitByBDToptD),0.5,0.5+len(categoriesSplitByBDToptD)),catstringSplitByBDToptD,"(((N_BTagsM>=2&&N_Jets>=6||N_BTagsM>=3&&N_Jets>=4)&&!"+categoriesJT[-1][0]+")||"+categoriesJT[-1][0]+")"),

       Plot(ROOT.TH1F("N_Jets","Number of ak4 jets",7,3.5,10.5),"N_Jets",'',label),
       Plot(ROOT.TH1F("N_BTagsM","Number of b-tags",4,1.5,5.5),"N_BTagsM",'',label),
       Plot(ROOT.TH1F("CSV0","B-tag of leading jet",22,-.1,1),"Jet_CSV[0]",'',label),
       Plot(ROOT.TH1F("CSV1","B-tag of second jet",22,-.1,1),"Jet_CSV[1]",'',label),
       Plot(ROOT.TH1F("CSV","B-tag of all jets",22,-.1,1),"Jet_CSV",'',label),
       
       Plot(ROOT.TH1F("pt1","p_{T} of leading jet",50,0,500),"Jet_Pt[0]",'',label),
       Plot(ROOT.TH1F("pt2","p_{T} of second jet",50,0,500),"Jet_Pt[1]",'',label),
       Plot(ROOT.TH1F("pt3","p_{T} of third jet",40,0,400),"Jet_Pt[2]",'',label),
       Plot(ROOT.TH1F("pt4","p_{T} of fourth jet",60,0,300),"Jet_Pt[3]",'',label),
       Plot(ROOT.TH1F("pt5","p_{T} of fifth jet",40,0,200),"Jet_Pt[4]",'',label),
       Plot(ROOT.TH1F("pt6","p_{T} of sixth jet",40,0,200),"Jet_Pt[5]",'',label),
       Plot(ROOT.TH1F("pt7","p_{T} of seventh jet",40,0,100),"Jet_Pt[6]",'',label),

       Plot(ROOT.TH1F("eta1","#eta of leading jet",50,-2.5,2.5),"Jet_Eta[0]",'',label),
       Plot(ROOT.TH1F("eta2","#eta of second jet",50,-2.5,2.5),"Jet_Eta[1]",'',label),
       Plot(ROOT.TH1F("phij1","#phi of leading jet",64,-3.2,3.2),"Jet_Phi[0]",'',label),
       Plot(ROOT.TH1F("phij2","#phi of second jet",64,-3.2,3.2),"Jet_Phi[1]",'',label),
       Plot(ROOT.TH1F("Evt_HT_Jets","Sum p_{T} jets",75,0,1500),"Evt_HT_Jets",'',label),
       Plot(ROOT.TH1F("ptalljets","p_{T} of all jets",60,0,300),"Jet_Pt",'',label),
       Plot(ROOT.TH1F("csvalljets","csv of all jets",44,-.1,1),"Jet_CSV",'',label),
       Plot(ROOT.TH1F("leppt","lepton p_{T}",50,0,200),"LooseLepton_Pt[0]",'',label),
       Plot(ROOT.TH1F("lepeta","lepton #eta",50,-2.5,2.5),"LooseLepton_Eta[0]",'',label),
       Plot(ROOT.TH1F("eliso","electron relative isolation",50,0,0.15),"Electron_RelIso[0]",'',label),
       Plot(ROOT.TH1F("muiso","muon relative isolation",50,0,0.15),"Muon_RelIso[0]",'',label),
       Plot(ROOT.TH1F("MET","missing transverse energy",50,0,200),"Evt_Pt_MET",'',label),
       Plot(ROOT.TH1F("METphi","MET #phi",64,-3.2,3.2),"Evt_Phi_MET",'',label),
       Plot(ROOT.TH1F("N_PrimaryVertices","Reconstructed primary vertices",26,-.5,25.5),"N_PrimaryVertices",'',label),
       Plot(ROOT.TH1F("CSVpt1","B-tag of jets with p_{T} between 30 and 40 GeV",44,-.1,1),"Jet_CSV",'Jet_Pt>30&&Jet_Pt<40',label),
       Plot(ROOT.TH1F("CSVpt2","B-tag of jets with p_{T} between 40 and 60 GeV",44,-.1,1),"Jet_CSV",'Jet_Pt>40&&Jet_Pt<60',label),
       Plot(ROOT.TH1F("CSVpt3","B-tag of jets with p_{T} between 60 and 100 GeV",44,-.1,1),"Jet_CSV",'Jet_Pt>60&&Jet_Pt<100',label),
       Plot(ROOT.TH1F("CSVpt4","B-tag of jets with p_{T} over 100 GeV",44,-.1,1),"Jet_CSV",'Jet_Pt>100',label),
       Plot(ROOT.TH1F("CSVeta1","B-tag of jets with abs(#eta) between 0 and 0.4",44,-.1,1),"Jet_CSV",'fabs(Jet_Eta)<0.4',label),
       Plot(ROOT.TH1F("CSVeta2","B-tag of jets with abs(#eta) between 0.4 and 0.8",44,-.1,1),"Jet_CSV",'fabs(Jet_Eta)>0.4&&fabs(Jet_Eta)<0.8',label),
       Plot(ROOT.TH1F("CSVeta3","B-tag of jets with abs(#eta) between 0.8 and 1.6",44,-.1,1),"Jet_CSV",'fabs(Jet_Eta)>0.8&&fabs(Jet_Eta)<1.6',label),
       Plot(ROOT.TH1F("CSVeta4","B-tag of jets with abs(#eta) between 0.8 and 1.6",44,-.1,1),"Jet_CSV",'fabs(Jet_Eta)>1.6',label),
       Plot(ROOT.TH1F("MEM","MEM discriminator for events with #geq 3 b-tags",22,0,1),"(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)",'(N_BTagsM>=3)',label),
       Plot(ROOT.TH1F("blrHighTag","B-tagging likelihood ratio for events with #geq 3 b-tags",44,-4,10),"TMath::Log(Evt_blr_ETH/(1-Evt_blr_ETH))",'(N_BTagsM>=3)',label),
       Plot(ROOT.TH1F("blrAll","B-tagging likelihood ratio",44,-6,10),"TMath::Log(Evt_blr_ETH/(1-Evt_blr_ETH))",'',label),

       Plot(ROOT.TH1F("BJN_N_Leptons","Number of soft leptons",6,-.5,5.5),"BJN_N_Leptons",'',label),
       Plot(ROOT.TH1F("BJN_N_TracksNoPV","Number of tracks not from the PV",13,-.5,12.5),"BJN_N_TracksNoPV",'',label),
       Plot(ROOT.TH1F("BJN_N_PVtrackOvCollTrk","Number PV tracks over all tracks",25,0.2,1.2),"BJN_N_PVtrackOvCollTrk",'',label),
       Plot(ROOT.TH1F("BJN_N_AvgIp3D","Avg 3D IP",40,0,0.08),"BJN_N_AvgIp3D",'',label),
       Plot(ROOT.TH1F("BJN_N_AvgIp3Dsig","Avg 3D IP significance",30,0,15),"BJN_N_AvgIp3Dsig",'',label),
       Plot(ROOT.TH1F("BJN_N_AvgSip3Dsig","Avg 3D signed IP significance",30,-15,15),"BJN_N_AvgSip3Dsig",'',label),
       Plot(ROOT.TH1F("BJN_N_AvgIp1Dsig","Avg 1D IP significance",25,0,25),"BJN_N_AvgIp1Dsig",'',label),

       Plot(ROOT.TH1F("commonBDT43","BDT w/o MEM in training",10,-1,1),"BDT_common5_output",'N_BTagsM==3&&N_Jets==4','4 jets, 3 b-tags'),
       Plot(ROOT.TH1F("MEM43","MEM discriminator",10,0,1),"(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)",'(N_BTagsM==3&&N_Jets==4)',""),
       
#       Plot(ROOT.TH1F("N_BoostedJets","Number of fat jets",5,0,5),"N_BoostedJets",'',label),
#       Plot(ROOT.TH1F("BoostedJet_Pt","transverse momentum of fat jet",40,200,600),"BoostedJet_Pt[0]",'',label)
#       
#       Plot(ROOT.TH1F("BoostedJet_PrunedMass","pruned mass of hardest fat jet",40,0,400),"BoostedJet_PrunedMass[0]",toptaggersel,label),
#       Plot(ROOT.TH1F("BoostedJet_Top_M","invariant mass of top",40,0,300),"BoostedJet_Top_M[0]",toptaggersel,label),
#       Plot(ROOT.TH1F("BoostedJet_Wbtag_M","invariant mass of W",40,0,200),"BoostedJet_Wbtag_M[0]",toptaggersel,label),
#       Plot(ROOT.TH1F("BoostedJet_BW1btag_M","invariant mass of B and W1",40,0,250),"BoostedJet_BW1btag_M[0]",toptaggersel,label),
#       Plot(ROOT.TH1F("BoostedJet_BW2btag_M","invariant mass of B and W2",40,0,250),"BoostedJet_BW2btag_M[0]",toptaggersel,label),
#       Plot(ROOT.TH1F("BoostedJet_Bbtag_CSV","CSV output of B",40,-0.1,1.),"BoostedJet_Bbtag_CSV[0]",toptaggersel,label),
#       Plot(ROOT.TH1F("BoostedJet_W1btag_CSV","CSV output of W1",40,-0.1,1.),"BoostedJet_W1btag_CSV[0]",toptaggersel,label),
#       Plot(ROOT.TH1F("BoostedJet_W2btag_CSV","CSV output of W2",40,-0.1,1.),"BoostedJet_W2btag_CSV[0]",toptaggersel,label),
#       Plot(ROOT.TH1F("BoostedJet_Tau21Filtered","#tau_2/#tau_1",40,0.,1.),"BoostedJet_Tau2Filtered[0]/BoostedJet_Tau1Filtered[0]",toptaggersel,label),
#       Plot(ROOT.TH1F("BoostedJet_Tau32Filtered","#tau_3/#tau_2",40,0.,1.),"BoostedJet_Tau3Filtered[0]/BoostedJet_Tau2Filtered[0]",toptaggersel,label),
#       Plot(ROOT.TH1F("BoostedJet_fRec","Difference to true W top mass ratio",40,0.,.6),"BoostedJet_fRec[0]",toptaggersel,label),
#       Plot(ROOT.TH1F("BoostedJet_DRoptRoptCalc","D_{opt}-D_{opt}^{calc}",40,-2.,1.),"BoostedJet_Ropt[0]-BoostedJet_RoptCalc[0]",toptaggersel,label),
#       
#       Plot(ROOT.TH1F("BoostedJet_TopTag_BDT_Std","BDT top tagger output of hardest fat jet",40,-1.,1.),"BoostedJet_TopTag_BDT_Std[0]",toptaggersel,label)
#       
#       Plot(ROOT.TH1F("BoostedJet_HiggsTag_SecondCSV","b-tagging output of subjet B2 of hardest fat jet",40,-.1,1.),"BoostedJet_HiggsTag_SecondCSV[0]",higgstaggersel,label)
       ]
# plot parallel -- alternatively there are also options to plot more traditional that also return lists of histo lists
outputpath=plotParallel(name,2000000,plots,samples+samples_data+systsamples,[''],['1.'],weightsystnames, systweights)

listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots,1)
if not os.path.exists(outputpath[:-4]+'_syst.root') or not askYesNo('reuse systematic histofile?'):
    renameHistos(outputpath,outputpath[:-4]+'_syst.root',allsystnames)
print othersystnames
lll=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots,allsystnames)
ntables=0
# do some post processing
#for hld,hl in zip(listOfHistoListsData,listOfHistoLists):
#    if "JT" in hld[0].GetName() and not "JTsplitByBDToptB" in hld[0].GetName() and not "JTByBDToptC" in hld[0].GetName() and not "JTsplitByBDToptD" in hld[0].GetName() :
#        for h in hld+hl:
#            h.GetXaxis().SetBinLabel(1,'4j2t')
#            h.GetXaxis().SetBinLabel(2,'5j2t')
#            h.GetXaxis().SetBinLabel(3,'6j2t')
#            h.GetXaxis().SetBinLabel(4,'4j3t')
#            h.GetXaxis().SetBinLabel(5,'5j3t')
#            h.GetXaxis().SetBinLabel(6,'6j3t')
#            h.GetXaxis().SetBinLabel(7,'4j4t')
#            h.GetXaxis().SetBinLabel(8,'5j4t')
#            h.GetXaxis().SetBinLabel(9,'6j4t')
#            h.GetXaxis().SetBinLabel(10,'boosted')
#        tablepath=("/".join((outputpath.split('/'))[:-1]))+"/"+name+"_yields"
#        ntables+=1
#        # make an event yield table
#        eventYields(hld,hl,samples,tablepath)

for hld,hl in zip(listOfHistoListsData,listOfHistoLists):
    if "JT" in hld[0].GetName() and not "JTsplitByBDToptB" in hld[0].GetName() and not "JTByBDToptC" in hld[0].GetName() and not "JTsplitByBDToptD" in hld[0].GetName() :
        for h in hld+hl:
            for i,cat in enumerate(categoriesJT):
                h.GetXaxis().SetBinLabel(i+1,cat[1])
                print cat[1]
        tablepath=("/".join((outputpath.split('/'))[:-1]))+"/"+name+"_yields"
        ntables+=1
        # make an event yield table
        eventYields(hld,hl,samples,tablepath)
    if "JTsplitByBDToptB" in hld[0].GetName():       
        for h in hld+hl:
            for i,cat in enumerate(categoriesSplitBDT):
                h.GetXaxis().SetBinLabel(i+1,cat[1])
                print cat[1]
        tablepath=("/".join((outputpath.split('/'))[:-1]))+"/"+name+"_yieldsB"
        # make an event yield table
        eventYields(hld,hl,samples,tablepath)
    if "JTByBDToptC" in hld[0].GetName():       
        for h in hld+hl:
            for i,cat in enumerate(categoriesBDT):
                h.GetXaxis().SetBinLabel(i+1,cat[1])
                print cat[1]
        tablepath=("/".join((outputpath.split('/'))[:-1]))+"/"+name+"_yieldsC"
        # make an event yield table
        eventYields(hld,hl,samples,tablepath)
    if "JTsplitByBDToptD" in hld[0].GetName():       
        for h in hld+hl:
            for i,cat in enumerate(categoriesSplitByBDToptD):
                h.GetXaxis().SetBinLabel(i+1,cat[1])
                print cat[1]
        tablepath=("/".join((outputpath.split('/'))[:-1]))+"/"+name+"_yieldsD"
        # make an event yield table
        eventYields(hld,hl,samples,tablepath)

# plot dataMC comparison
labels=[plot.label for plot in plots]

lolT=transposeLOL(listOfHistoLists)
plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],20,name,lll,False,labels)


listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots,1)
lll=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots,allsystnames)
ntables=0
# do some post processing
for hld,hl in zip(listOfHistoListsData,listOfHistoLists):
    if "JT" in hld[0].GetName() and not "JTsplitByBDToptB" in hld[0].GetName() and not "JTByBDToptC" in hld[0].GetName() and not "JTsplitByBDToptD" in hld[0].GetName() :
        for h in hld+hl:
            h.GetXaxis().SetBinLabel(1,'4j2t')
            h.GetXaxis().SetBinLabel(2,'5j2t')
            h.GetXaxis().SetBinLabel(3,'6j2t')
            h.GetXaxis().SetBinLabel(4,'4j3t')
            h.GetXaxis().SetBinLabel(5,'5j3t')
            h.GetXaxis().SetBinLabel(6,'6j3t')
            h.GetXaxis().SetBinLabel(7,'4j4t')
            h.GetXaxis().SetBinLabel(8,'5j4t')
            h.GetXaxis().SetBinLabel(9,'6j4t')
            h.GetXaxis().SetBinLabel(10,'boosted')
for hld,hl in zip(listOfHistoListsData,listOfHistoLists):
    if "JTsplitByBDToptB" in hld[0].GetName():       
        for h in hld+hl:
            for i,cat in enumerate(categoriesSplitBDT):
                h.GetXaxis().SetBinLabel(i+1,cat[1])
    if "JTByBDToptC" in hld[0].GetName():       
        for h in hld+hl:
            for i,cat in enumerate(categoriesBDT):
                h.GetXaxis().SetBinLabel(i+1,cat[1])
    if "JTsplitByBDToptD" in hld[0].GetName():       
        for h in hld+hl:
            for i,cat in enumerate(categoriesSplitByBDToptD):
                h.GetXaxis().SetBinLabel(i+1,cat[1])


# plot dataMC comparison
labels=[plot.label for plot in plots]

lolT=transposeLOL(listOfHistoLists)
plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],20,name+'_log',lll,True,labels)
