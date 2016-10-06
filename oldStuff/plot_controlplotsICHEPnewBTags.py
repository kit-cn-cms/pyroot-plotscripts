#############
# plot general control distributions 
##############

from plotconfigICHEPnewBTags import *
sys.path.insert(0, 'limittools')
from limittools import renameHistos

name='controlplotsICHEPnewBTagsV2'

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

categoriesJTB=[
              ("((N_Jets>=6&&N_BTagsM==2)&&!"+boosted+")","6j2t",""),
              ("((N_Jets==4&&N_BTagsM==3)&&!"+boosted+")","4j3t","0.2"),
              ("((N_Jets==5&&N_BTagsM==3)&&!"+boosted+")","5j3t","0.1"),
              ("((N_Jets>=6&&N_BTagsM==3)&&!"+boosted+")","6j3t","0.1"),
              ("((N_Jets==4&&N_BTagsM>=4)&&!"+boosted+")","4j4t","0.2"),
              ("((N_Jets==5&&N_BTagsM>=4)&&!"+boosted+")","5j4t","0.2"),             
              ("((N_Jets>=6&&N_BTagsM>=4)&&!"+boosted+")","6j4t","0.1"),
              ("((N_Jets>=4&&N_BTagsM>=2)&&"+boosted+")","boosted","")
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
samples=samplesControlPlots
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

        Plot(ROOT.TH1F("N_Jets","Number of ak4 jets",7,3.5,10.5),"N_Jets",plotselection,plotlabel),
        Plot(ROOT.TH1F("N_BTagsM","Number of b-tags",4,1.5,5.5),"N_BTagsM",plotselection,plotlabel),
        Plot(ROOT.TH1F("CSV0","B-tag of leading jet",22,-.1,1),"Jet_CSV[0]",plotselection,plotlabel),
        Plot(ROOT.TH1F("CSV1","B-tag of second jet",22,-.1,1),"Jet_CSV[1]",plotselection,plotlabel),
        Plot(ROOT.TH1F("CSV","B-tag of all jets",22,-.1,1),"Jet_CSV",plotselection,plotlabel),
        
        Plot(ROOT.TH1F("CSV0NPVgeq20","B-tag of leading jet (NPV#geq20)",22,-.1,1),"Jet_CSV[0]",plotselection+"*(N_PrimaryVertices>=20)",plotlabel),
        Plot(ROOT.TH1F("CSV1NPVgeq20","B-tag of second jet (NPV#geq20)",22,-.1,1),"Jet_CSV[1]",plotselection+"*(N_PrimaryVertices>=20)",plotlabel),
        Plot(ROOT.TH1F("CSVNPVgeq20","B-tag of all jets (NPV#geq20)",22,-.1,1),"Jet_CSV",plotselection+"*(N_PrimaryVertices>=20)",plotlabel),
	
	Plot(ROOT.TH1F("CSV0NPV15to20","B-tag of leading jet (15#leqNPV#leq20)",22,-.1,1),"Jet_CSV[0]",plotselection+"*(N_PrimaryVertices<=20 && N_PrimaryVertices>=15)",plotlabel),
        Plot(ROOT.TH1F("CSV1NPV15to20","B-tag of second jet (15#leqNPV#leq20)",22,-.1,1),"Jet_CSV[1]",plotselection+"*(N_PrimaryVertices<=20 && N_PrimaryVertices>=15)",plotlabel),
        Plot(ROOT.TH1F("CSVNPV15to20","B-tag of all jets (15#leqNPV#leq20)",22,-.1,1),"Jet_CSV",plotselection+"*(N_PrimaryVertices<=20 && N_PrimaryVertices>=15)",plotlabel),
	
	Plot(ROOT.TH1F("CSV0NPV10to15","B-tag of leading jet (10#leqNPV#leq15)",22,-.1,1),"Jet_CSV[0]",plotselection+"*(N_PrimaryVertices<=15 && N_PrimaryVertices>=10)",plotlabel),
        Plot(ROOT.TH1F("CSV1NPV10to15","B-tag of second jet (10#leqNPV#leq15)",22,-.1,1),"Jet_CSV[1]",plotselection+"*(N_PrimaryVertices<=15 && N_PrimaryVertices>=10)",plotlabel),
        Plot(ROOT.TH1F("CSVNPV10to15","B-tag of all jets (10#leqNPV#leq15)",22,-.1,1),"Jet_CSV",plotselection+"*(N_PrimaryVertices<=15 && N_PrimaryVertices>=10)",plotlabel),

	Plot(ROOT.TH1F("CSV0NPV0to10","B-tag of leading jet (0#leqNPV#leq10)",22,-.1,1),"Jet_CSV[0]",plotselection+"*(N_PrimaryVertices<=10 && N_PrimaryVertices>=0)",plotlabel),
        Plot(ROOT.TH1F("CSV1NPV0to10","B-tag of second jet (0#leqNPV#leq10)",22,-.1,1),"Jet_CSV[1]",plotselection+"*(N_PrimaryVertices<=10 && N_PrimaryVertices>=0)",plotlabel),
        Plot(ROOT.TH1F("CSVNPV0to10","B-tag of all jets (0#leqNPV#leq10)",22,-.1,1),"Jet_CSV",plotselection+"*(N_PrimaryVertices<=10 && N_PrimaryVertices>=0)",plotlabel),


        Plot(ROOT.TH1F("pt1","p_{T} of leading jet",50,0,500),"Jet_Pt[0]",plotselection,plotlabel),
        Plot(ROOT.TH1F("pt2","p_{T} of second jet",50,0,500),"Jet_Pt[1]",plotselection,plotlabel),
        Plot(ROOT.TH1F("pt3","p_{T} of third jet",40,0,400),"Jet_Pt[2]",plotselection,plotlabel),
        Plot(ROOT.TH1F("pt4","p_{T} of fourth jet",60,0,300),"Jet_Pt[3]",plotselection,plotlabel),
        Plot(ROOT.TH1F("pt5","p_{T} of fifth jet",40,0,200),"Jet_Pt[4]",plotselection,plotlabel),
        Plot(ROOT.TH1F("pt6","p_{T} of sixth jet",40,0,200),"Jet_Pt[5]",plotselection,plotlabel),
        Plot(ROOT.TH1F("pt1tagged","p_{T} of leading tagged jet",50,0,500),"TaggedJet_Pt[0]",plotselection,plotlabel),
        Plot(ROOT.TH1F("pt2tagged","p_{T} of second tagged jet",50,0,500),"TaggedJet_Pt[1]",plotselection,plotlabel),
        Plot(ROOT.TH1F("pt3tagged","p_{T} of third tagged jet",40,0,400),"TaggedJet_Pt[2]",plotselection,plotlabel),
        Plot(ROOT.TH1F("pt4tagged","p_{T} of fourth tagged jet",60,0,300),"TaggedJet_Pt[3]",plotselection,plotlabel),


        Plot(ROOT.TH1F("eta1","#eta of leading jet",50,-2.5,2.5),"Jet_Eta[0]",plotselection,plotlabel),
        Plot(ROOT.TH1F("eta2","#eta of second jet",50,-2.5,2.5),"Jet_Eta[1]",plotselection,plotlabel),
        Plot(ROOT.TH1F("phij1","#phi of leading jet",64,-3.2,3.2),"Jet_Phi[0]",plotselection,plotlabel),
        Plot(ROOT.TH1F("phij2","#phi of second jet",64,-3.2,3.2),"Jet_Phi[1]",plotselection,plotlabel),
        Plot(ROOT.TH1F("Evt_HT_Jets","Sum p_{T} jets",75,0,1500),"Evt_HT_Jets",plotselection,plotlabel),
        Plot(ROOT.TH1F("ptalljets","p_{T} of all jets",60,0,300),"Jet_Pt",plotselection,plotlabel),
        Plot(ROOT.TH1F("csvalljets","csv of all jets",44,-.1,1),"Jet_CSV",plotselection,plotlabel),
        Plot(ROOT.TH1F("leppt","lepton p_{T}",50,0,200),"LooseLepton_Pt[0]",plotselection,plotlabel),
        Plot(ROOT.TH1F("lepeta","lepton #eta",50,-2.5,2.5),"LooseLepton_Eta[0]",plotselection,plotlabel),
        Plot(ROOT.TH1F("elleppt","electron p_{T}",50,0,200),"Electron_Pt[0]",'Electron_Pt[0]>10',plotlabel),
        Plot(ROOT.TH1F("ellepeta","electron #eta",50,-2.5,2.5),"Electron_Eta[0]",'Electron_Pt[0]>10',plotlabel),
        Plot(ROOT.TH1F("muleppt","muon p_{T}",50,0,200),"Muon_Pt[0]",'Muon_Pt[0]>10',plotlabel),
        Plot(ROOT.TH1F("mulepeta","muon #eta",50,-2.5,2.5),"Muon_Eta[0]",'Muon_Pt[0]>10',plotlabel),

        #Plot(ROOT.TH1F("Prescale_HLT_Ele27_eta2p1_WPTight_Gsf_vX","Prescale_HLT_Ele27_eta2p1_WPTight_Gsf_vX",50,0,2.0),"Prescale_HLT_Ele27_eta2p1_WPTight_Gsf_vX",plotselection,plotlabel),
        #Plot(ROOT.TH1F("Prescale_HLT_IsoMu22_vX","Prescale_HLT_IsoMu22_vX",50,0,2.0),"Prescale_HLT_IsoMu22_vX",plotselection,plotlabel),
        #Plot(ROOT.TH1F("Prescale_HLT_IsoTkMu22_vX","Prescale_HLT_IsoTkMu22_vX",50,0,2.0),"Prescale_HLT_IsoTkMu22_vX",plotselection,plotlabel),

        Plot(ROOT.TH1F("eliso","electron relative isolation",50,0,0.15),"Electron_RelIso[0]",plotselection,plotlabel),
        Plot(ROOT.TH1F("muiso","muon relative isolation",50,0,0.15),"Muon_RelIso[0]",plotselection,plotlabel),
        Plot(ROOT.TH1F("MET","missing transverse energy",50,0,200),"Evt_Pt_MET",plotselection,plotlabel),
        Plot(ROOT.TH1F("METphi","MET #phi",64,-3.2,3.2),"Evt_Phi_MET",plotselection,plotlabel),
        Plot(ROOT.TH1F("N_PrimaryVertices","Reconstructed primary vertices",26,-.5,25.5),"N_PrimaryVertices",plotselection,plotlabel),
#        Plot(ROOT.TH1F("CSVpt1","B-tag of jets with p_{T} between 30 and 40 GeV",44,-.1,1),"Jet_CSV",'Jet_Pt>30&&Jet_Pt<40',plotlabel),
#        Plot(ROOT.TH1F("CSVpt2","B-tag of jets with p_{T} between 40 and 60 GeV",44,-.1,1),"Jet_CSV",'Jet_Pt>40&&Jet_Pt<60',plotlabel),
#        Plot(ROOT.TH1F("CSVpt3","B-tag of jets with p_{T} between 60 and 100 GeV",44,-.1,1),"Jet_CSV",'Jet_Pt>60&&Jet_Pt<100',plotlabel),
#        Plot(ROOT.TH1F("CSVpt4","B-tag of jets with p_{T} over 100 GeV",44,-.1,1),"Jet_CSV",'Jet_Pt>100',plotlabel),
#        Plot(ROOT.TH1F("CSVeta1","B-tag of jets with abs(#eta) between 0 and 0.4",44,-.1,1),"Jet_CSV",'fabs(Jet_Eta)<0.4',plotlabel),
#        Plot(ROOT.TH1F("CSVeta2","B-tag of jets with abs(#eta) between 0.4 and 0.8",44,-.1,1),"Jet_CSV",'fabs(Jet_Eta)>0.4&&fabs(Jet_Eta)<0.8',plotlabel),
#        Plot(ROOT.TH1F("CSVeta3","B-tag of jets with abs(#eta) between 0.8 and 1.6",44,-.1,1),"Jet_CSV",'fabs(Jet_Eta)>0.8&&fabs(Jet_Eta)<1.6',plotlabel),
#        Plot(ROOT.TH1F("CSVeta4","B-tag of jets with abs(#eta) between 0.8 and 1.6",44,-.1,1),"Jet_CSV",'fabs(Jet_Eta)>1.6',plotlabel),
        #Plot(ROOT.TH1F("MEM","MEM discriminator for events with #geq 3 b-tags",22,0,1),"(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)",'(N_BTagsM>=3)',plotlabel),
        Plot(ROOT.TH1F("blrHighTag","B-tagging likelihood ratio for events with #geq 3 b-tags",44,-4,10),"TMath::Log(Evt_blr_ETH/(1-Evt_blr_ETH))",'(N_BTagsM>=3)',plotlabel),
        Plot(ROOT.TH1F("blrAll","B-tagging likelihood ratio",44,-6,10),"TMath::Log(Evt_blr_ETH/(1-Evt_blr_ETH))",plotselection,plotlabel),

       Plot(ROOT.TH1F("BJN_N_Leptons","Number of soft leptons",6,-.5,5.5),"BJN_N_Leptons",plotselection,plotlabel),
       #Plot(ROOT.TH1F("BJN_N_TracksNoPV","Number of tracks not from the PV",13,-.5,12.5),"BJN_N_TracksNoPV",plotselection,plotlabel),
       Plot(ROOT.TH1F("BJN_N_PVtrackOvCollTrk","Number PV tracks over all tracks",25,0.2,1.2),"BJN_N_PVtrackOvCollTrk",plotselection,plotlabel),
       Plot(ROOT.TH1F("BJN_N_AvgIp3D","Avg 3D IP",40,0,0.2),"BJN_N_AvgIp3D",plotselection,plotlabel),
       Plot(ROOT.TH1F("BJN_N_AvgIp3Dsig","Avg 3D IP significance",30,0,30),"BJN_N_AvgIp3Dsig",plotselection,plotlabel),
       Plot(ROOT.TH1F("BJN_N_AvgSip3Dsig","Avg 3D signed IP significance",30,-15,15),"BJN_N_AvgSip3Dsig",plotselection,plotlabel),
       Plot(ROOT.TH1F("BJN_N_AvgIp1Dsig","Avg 1D IP significance",25,0,25),"BJN_N_AvgIp1Dsig",plotselection,plotlabel),

#        Plot(ROOT.TH1F("commonBDT43","BDT w/o MEM in training",10,-1,1),"BDT_common5_output",'N_BTagsM==3&&N_Jets==4','4 jets, 3 b-tags'),
#        Plot(ROOT.TH1F("MEM43","MEM discriminator",10,0,1),"(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)",'(N_BTagsM==3&&N_Jets==4)',""),
       
        Plot(ROOT.TH1F("N_BoostedJets","Number of fat jets",5,0,5),"N_BoostedJets",plotselection,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_Pt","p_{T} of fat jet",40,200,600),"BoostedJet_Pt[0]",plotselection,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_Eta","#eta of fat jet",40,-2.5,2.5),"BoostedJet_Eta[0]",plotselection,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_M","invariant mass of fat jet",40,0,1000),"BoostedJet_M[0]",plotselection,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_Bbtag_Pt","p_{T} of B subjet",40,0,400),"BoostedJet_B_Pt[0]",plotselection+"&&"+toptaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_W1btag_Pt","p_{T} of W1 subjet",40,0,400),"BoostedJet_W1_Pt[0]",plotselection+"&&"+toptaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_W2btag_Pt","p_{T} of W2 subjet",40,0,200),"BoostedJet_W2_Pt[0]",plotselection+"&&"+toptaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_Bbtag_Eta","#eta of B subjet",40,-2.5,2.5),"BoostedJet_B_Eta[0]",plotselection+"&&"+toptaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_W1btag_Eta","#eta of W1 subjet",40,-2.5,2.5),"BoostedJet_W1_Eta[0]",plotselection+"&&"+toptaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_W2btag_Eta","#eta of W2 subjet",40,-2.5,2.5),"BoostedJet_W2_Eta[0]",plotselection+"&&"+toptaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_Top_Pt","p_{T} of boosted top",40,100,500),"BoostedJet_Top_Pt[0]",plotselection+"&&"+toptaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_Top_Eta","#eta of boosted top",40,-2.5,2.5),"BoostedJet_Top_Eta[0]",plotselection+"&&"+toptaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_Wbtag_Pt","p_{T} of W",40,0,500),"BoostedJet_Wbtag_Pt[0]",plotselection+"&&"+toptaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_Wbtag_Eta","#eta of W",40,-2.5,2.5),"BoostedJet_Wbtag_Eta[0]",plotselection+"&&"+toptaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_PrunedMass","pruned mass of hardest fat jet",40,0,400),"BoostedJet_PrunedMass[0]",plotselection+"&&"+toptaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_Top_M","invariant mass of top",40,0,300),"BoostedJet_Top_M[0]",plotselection+"&&"+toptaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_Wbtag_M","invariant mass of W",40,0,200),"BoostedJet_Wbtag_M[0]",plotselection+"&&"+toptaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_BW1btag_M","invariant mass of B and W1",40,0,250),"BoostedJet_BW1btag_M[0]",plotselection+"&&"+toptaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_BW2btag_M","invariant mass of B and W2",40,0,250),"BoostedJet_BW2btag_M[0]",plotselection+"&&"+toptaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_MRatio_Wbtag_Top","W and top mass ratio",40,0.,1.),"BoostedJet_Wbtag_M[0]/BoostedJet_Top_M[0]",plotselection+"&&"+toptaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_fRec","Difference to true W top mass ratio",40,0.,.6),"BoostedJet_fRec[0]",plotselection+"&&"+toptaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_Bbtag_CSV","CSV output of B",40,-0.1,1.),"BoostedJet_Bbtag_CSV[0]",plotselection+"&&"+toptaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_W1btag_CSV","CSV output of W1",40,-0.1,1.),"BoostedJet_W1btag_CSV[0]",plotselection+"&&"+toptaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_W2btag_CSV","CSV output of W2",40,-0.1,1.),"BoostedJet_W2btag_CSV[0]",plotselection+"&&"+toptaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_Tau21Filtered","#tau_2/#tau_1",40,0.,1.),"BoostedJet_Tau2Filtered[0]/BoostedJet_Tau1Filtered[0]",plotselection+"&&"+toptaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_Tau32Filtered","#tau_3/#tau_2",40,0.,1.),"BoostedJet_Tau3Filtered[0]/BoostedJet_Tau2Filtered[0]",plotselection+"&&"+toptaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_DRoptRoptCalc","D_{opt}-D_{opt}^{calc}",40,-2.,1.),"BoostedJet_Ropt-BoostedJet_RoptCalc",plotselection+"&&"+toptaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_TopTag_BDT_Std","BDT top tagger output of hardest fat jet",40,-1.,1.),"BoostedJet_TopTag_BDT_Std[0]",plotselection+"&&"+toptaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_Filterjet1_Pt","p_{T} of hardest filterjet",40,0,400),"BoostedJet_Filterjet1_Pt[0]",plotselection+"&&"+higgstaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_Filterjet2_Pt","p_{T} of second hardest filterjet",40,0,300),"BoostedJet_Filterjet2_Pt[0]",plotselection+"&&"+higgstaggersel,plotlabelboosted),
       Plot(ROOT.TH1F("BoostedJet_Filterjet3_Pt","p_{T} of third hardest filterjet",40,0,200),"BoostedJet_Filterjet3_Pt[0]",plotselection+"&&"+higgstaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_Filterjet1_Eta","#eta of hardest filterjet",40,-2.5,2.5),"BoostedJet_Filterjet1_Eta[0]",plotselection+"&&"+higgstaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_Filterjet2_Eta","#eta of second hardest filterjet",40,-2.5,2.5),"BoostedJet_Filterjet2_Eta[0]",plotselection+"&&"+higgstaggersel,plotlabelboosted),
       Plot(ROOT.TH1F("BoostedJet_Filterjet3_Eta","#eta of third hardest filterjet",40,-2.5,2.5),"BoostedJet_Filterjet3_Eta[0]",plotselection+"&&"+higgstaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_Filterjet1_CSV","CSV output of hardest filterjet",40,-0.1,1.0),"BoostedJet_Filterjet1_CSV[0]",plotselection+"&&"+higgstaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_Filterjet2_CSV","CSV output of second hardest filterjet",40,-0.1,1.0),"BoostedJet_Filterjet2_CSV[0]",plotselection+"&&"+higgstaggersel,plotlabelboosted),
       Plot(ROOT.TH1F("BoostedJet_Filterjet3_CSV","CSV output of third hardest filterjet",40,-0.1,1.0),"BoostedJet_Filterjet3_CSV[0]",plotselection+"&&"+higgstaggersel,plotlabelboosted),
        #Plot(ROOT.TH1F("BoostedJet_Mbb","invariant mass of Higgs candidate",40,0,300),"BoostedJet_Mbb[0]",plotselection+"&&"+higgstaggersel,plotlabelboosted),
        Plot(ROOT.TH1F("BoostedJet_HiggsTag_SecondCSV","second highest filterjet CSV output",40,-.1,1.),"BoostedJet_HiggsTag_SecondCSV[0]",plotselection+"&&"+higgstaggersel,plotlabelboosted),

#        Plot(ROOT.TH1F("Evt_Deta_JetsAverage","avg #Delta #eta (jet,jet)", 60,0.0,3),"",plotselection,plotlabel),
        Plot(ROOT.TH1F("Evt_Deta_UntaggedJetsAverage","avg #Delta #eta (untagged,untagged)",45,0.,4.5),"Evt_Deta_UntaggedJetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1F("Evt_Deta_TaggedJetsAverage","avg #Delta #eta (tag,tag)",45,0.,4.5),"Evt_Deta_TaggedJetsAverage",plotselection,plotlabel),
#        Plot(ROOT.TH1F("Evt_Dr_JetsAverage","avg #Delta R (jet,jet)",35,0.5,4.),"Evt_Dr_JetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1F("Evt_Dr_TaggedJetsAverage","avg #Delta R (tag,tag)",45,0.4,4.9),"Evt_Dr_TaggedJetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1F("Evt_Dr_UntaggedJetsAverage","avg #Delta R (untagged,untagged)",50,0.,5),"Evt_Dr_UntaggedJetsAverage",plotselection,plotlabel),
#        Plot(ROOT.TH1F("Evt_M2_JetsAverage","",50,0,250),"Evt_M2_JetsAverage",plotselection,plotlabel),
#        Plot(ROOT.TH1F("Evt_M2_UntaggedJetsAverage","",50,0.,250),"Evt_M2_UntaggedJetsAverage",plotselection,plotlabel),
#        Plot(ROOT.TH1F("Evt_M2_TaggedJetsAverage","",50,0.,250),"Evt_M2_TaggedJetsAverage",plotselection,plotlabel),

#        Plot(ROOT.TH1F("Evt_M_MinDeltaRJets","",30,0.,150),"Evt_M_MinDeltaRJets",plotselection,plotlabel),
        Plot(ROOT.TH1F("Evt_M_MinDeltaRTaggedJets","mass of closest tagged jets",45,0.,450),"Evt_M_MinDeltaRTaggedJets",plotselection,plotlabel),
        Plot(ROOT.TH1F("Evt_M_MinDeltaRUntaggedJets","mass of closest untagged jets",45,0.,450),"Evt_M_MinDeltaRUntaggedJets",plotselection,plotlabel),
#        Plot(ROOT.TH1F("Evt_M_MinDeltaRLeptonJet","",60,0.4,3.4),"Evt_M_MinDeltaRLeptonJet",plotselection,plotlabel),
       Plot(ROOT.TH1F("Evt_Dr_MinDeltaRJets","",50,0.,5.0),"Evt_Dr_MinDeltaRJets",plotselection,plotlabel),
#        Plot(ROOT.TH1F("Evt_Dr_MinDeltaRTaggedJets","",50,0.,5.0),"Evt_Dr_MinDeltaRTaggedJets",plotselection,plotlabel),
#        Plot(ROOT.TH1F("Evt_Dr_MinDeltaRUntaggedJets","",50,0.,5.0),"Evt_Dr_MinDeltaRUntaggedJets",plotselection,plotlabel),
#        Plot(ROOT.TH1F("Evt_Dr_MinDeltaRLeptonJet","",60,0.4,3.4),"Evt_Dr_MinDeltaRLeptonJet",plotselection,plotlabel),

        Plot(ROOT.TH1F("Evt_Jet_MaxDeta_Jets","max #Delta #eta (jet,jet)",50,0.,5.0),"Evt_Jet_MaxDeta_Jets",plotselection,plotlabel),
        Plot(ROOT.TH1F("Evt_TaggedJet_MaxDeta_Jets","max #Delta #eta (tag,jet)",50,0.,5.0),"Evt_TaggedJet_MaxDeta_Jets",plotselection,plotlabel),
        Plot(ROOT.TH1F("Evt_TaggedJet_MaxDeta_TaggedJets","max #Delta #eta (tag,tag)",60,0.,6.0),"Evt_TaggedJet_MaxDeta_TaggedJets",plotselection,plotlabel),

#        Plot(ROOT.TH1F("Evt_M_Total","",40,0.,4000),"Evt_M_Total",plotselection,plotlabel),

       Plot(ROOT.TH1F("H0","",40,0.5,4.5),"Evt_H0",plotselection,plotlabel),
        Plot(ROOT.TH1F("H1","",60,-0.2,0.4),"Evt_H1",plotselection,plotlabel),
        Plot(ROOT.TH1F("H2","",60,-0.2,0.4),"Evt_H2",plotselection,plotlabel),
        Plot(ROOT.TH1F("H3","",50,-0.05,1.05),"Evt_H3",plotselection,plotlabel),
        Plot(ROOT.TH1F("H4","",50,-0.15,0.35),"Evt_H4",plotselection,plotlabel),

        Plot(ROOT.TH1F("Sphericity","",50,0,1),"Evt_Sphericity",plotselection,plotlabel),
        Plot(ROOT.TH1F("Aplanarity","",50,0,0.5),"Evt_Aplanarity",plotselection,plotlabel),
]


plotlabel="1 lepton, 4 jets, 2 b-tags"
plotselection="((N_Jets==4&&N_BTagsM==2)&&!"+boosted+")"
plotprefix="4j2t"
plots42=[
       Plot(ROOT.TH1F(plotprefix+"Evt_Deta_JetsAverage","Evt_Deta_JetsAverage", 60,0.0,3),"Evt_Deta_JetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Deta_2JetsAverage","Evt_Deta_2JetsAverage", 60,0.0,3),"Evt_Deta_2JetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Deta_3JetsAverage","Evt_Deta_3JetsAverage", 60,0.0,3),"Evt_Deta_3JetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Deta_4JetsAverage","Evt_Deta_4JetsAverage", 60,0.0,3),"Evt_Deta_4JetsAverage",plotselection,plotlabel),

       Plot(ROOT.TH1F(plotprefix+"Evt_Deta_UntaggedJetsAverage","Evt_Deta_UntaggedJetsAverage",45,0.,4.5),"Evt_Deta_UntaggedJetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",45,0.,4.5),"Evt_Deta_TaggedJetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Deta_2TaggedJetsAverage","Evt_Deta_2TaggedJetsAverage", 60,0.0,3),"Evt_Deta_2TaggedJetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Deta_3TaggedJetsAverage","Evt_Deta_3TaggedJetsAverage", 60,0.0,3),"Evt_Deta_3TaggedJetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Deta_4TaggedJetsAverage","Evt_Deta_4TaggedJetsAverage", 60,0.0,3),"Evt_Deta_4TaggedJetsAverage",plotselection,plotlabel),

       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",35,0.5,4.),"Evt_Dr_JetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_TaggedJetsAverage","Evt_Dr_TaggedJetsAverage",45,0.4,4.9),"Evt_Dr_TaggedJetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_2JetsAverage","Evt_Dr_2JetsAverage",35,0.5,4.),"Evt_Dr_2JetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_2TaggedJetsAverage","Evt_Dr_2TaggedJetsAverage",45,0.4,4.9),"Evt_Dr_2TaggedJetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_3JetsAverage","Evt_Dr_3JetsAverage",35,0.5,4.),"Evt_Dr_3JetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_3TaggedJetsAverage","Evt_Dr_3TaggedJetsAverage",45,0.4,4.9),"Evt_Dr_3TaggedJetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_4JetsAverage","Evt_Dr_4JetsAverage",35,0.5,4.),"Evt_Dr_4JetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_4TaggedJetsAverage","Evt_Dr_4TaggedJetsAverage",45,0.4,4.9),"Evt_Dr_4TaggedJetsAverage",plotselection,plotlabel),

       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_UntaggedJetsAverage","Evt_Dr_UntaggedJetsAverage",50,0.,5),"Evt_Dr_UntaggedJetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_M2_JetsAverage","Evt_M2_JetsAverage",50,0,250),"Evt_M2_JetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_M2_UntaggedJetsAverage","Evt_M2_UntaggedJetsAverage",50,0.,250),"Evt_M2_UntaggedJetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",50,0.,250),"Evt_M2_TaggedJetsAverage",plotselection,plotlabel),

       Plot(ROOT.TH1F(plotprefix+"Evt_M2_2JetsAverage","Evt_M2_2JetsAverage",50,0,250),"Evt_M2_2JetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_M2_2TaggedJetsAverage","Evt_M2_2TaggedJetsAverage",50,0.,250),"Evt_M2_2TaggedJetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_M2_3JetsAverage","Evt_M2_3JetsAverage",50,0,250),"Evt_M2_3JetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_M2_3TaggedJetsAverage","Evt_M2_3TaggedJetsAverage",50,0.,250),"Evt_M2_3TaggedJetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_M2_4JetsAverage","Evt_M2_4JetsAverage",50,0,250),"Evt_M2_4JetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_M2_4TaggedJetsAverage","Evt_M2_4TaggedJetsAverage",50,0.,250),"Evt_M2_4TaggedJetsAverage",plotselection,plotlabel),

       Plot(ROOT.TH1F(plotprefix+"Evt_M_MinDeltaRJets","Evt_M_MinDeltaRJets",30,0.,150),"Evt_M_MinDeltaRJets",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",45,0.,450),"Evt_M_MinDeltaRTaggedJets",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_M_MinDeltaRUntaggedJets","Evt_M_MinDeltaRUntaggedJets",45,0.,450),"Evt_M_MinDeltaRUntaggedJets",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_M_MinDeltaRLeptonJet","Evt_M_MinDeltaRLeptonJet",60,0.4,3.4),"Evt_M_MinDeltaRLeptonJet",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRJets","Evt_Dr_MinDeltaRJets",50,0.,5.0),"Evt_Dr_MinDeltaRJets",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRTaggedJets","Evt_Dr_MinDeltaRTaggedJets",50,0.,5.0),"Evt_Dr_MinDeltaRTaggedJets",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRUntaggedJets","Evt_Dr_MinDeltaRUntaggedJets",50,0.,5.0),"Evt_Dr_MinDeltaRUntaggedJets",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRLeptonJet","Evt_Dr_MinDeltaRLeptonJet",60,0.4,3.4),"Evt_Dr_MinDeltaRLeptonJet",plotselection,plotlabel),

       Plot(ROOT.TH1F(plotprefix+"Evt_Jet_MaxDeta_Jets","Evt_Jet_MaxDeta_Jets",50,0.,5.0),"Evt_Jet_MaxDeta_Jets",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_TaggedJet_MaxDeta_Jets","Evt_TaggedJet_MaxDeta_Jets",50,0.,5.0),"Evt_TaggedJet_MaxDeta_Jets",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_TaggedJet_MaxDeta_TaggedJets","Evt_TaggedJet_MaxDeta_TaggedJets",60,0.,6.0),"Evt_TaggedJet_MaxDeta_TaggedJets",plotselection,plotlabel),

       Plot(ROOT.TH1F(plotprefix+"Evt_M_Total","Evt_M_Total",40,0.,4000),"Evt_M_Total",plotselection,plotlabel),

       Plot(ROOT.TH1F(plotprefix+"Evt_H0","Evt_H0",40,0.5,4.5),"Evt_H0",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_H1","Evt_H1",60,-0.2,0.4),"Evt_H1",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_H2","Evt_H2",60,-0.2,0.4),"Evt_H2",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_H3","Evt_H3",50,-0.05,1.05),"Evt_H3",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_H4","Evt_H4",50,-0.15,0.35),"Evt_H4",plotselection,plotlabel),

       Plot(ROOT.TH1F(plotprefix+"Sphericity","Sphericity",50,0,1),"Evt_Sphericity",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Aplanarity","Aplanarity",50,0,0.5),"Evt_Aplanarity",plotselection,plotlabel),
]

plotlabel="1 lepton, 5 jets, 2 b-tags"
plotselection="((N_Jets==5&&N_BTagsM==2)&&!"+boosted+")"
plotprefix="s52_"
plots52=[
       Plot(ROOT.TH1F(plotprefix+"Evt_Deta_JetsAverage","Evt_Deta_JetsAverage", 60,0.0,3),"Evt_Deta_JetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Deta_2JetsAverage","Evt_Deta_2JetsAverage", 60,0.0,3),"Evt_Deta_2JetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Deta_3JetsAverage","Evt_Deta_3JetsAverage", 60,0.0,3),"Evt_Deta_3JetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Deta_4JetsAverage","Evt_Deta_4JetsAverage", 60,0.0,3),"Evt_Deta_4JetsAverage",plotselection,plotlabel),


       Plot(ROOT.TH1F(plotprefix+"Evt_Deta_UntaggedJetsAverage","Evt_Deta_UntaggedJetsAverage",45,0.,4.5),"Evt_Deta_UntaggedJetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",45,0.,4.5),"Evt_Deta_TaggedJetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Deta_2TaggedJetsAverage","Evt_Deta_2TaggedJetsAverage", 60,0.0,3),"Evt_Deta_2TaggedJetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Deta_3TaggedJetsAverage","Evt_Deta_3TaggedJetsAverage", 60,0.0,3),"Evt_Deta_3TaggedJetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Deta_4TaggedJetsAverage","Evt_Deta_4TaggedJetsAverage", 60,0.0,3),"Evt_Deta_4TaggedJetsAverage",plotselection,plotlabel),

       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",35,0.5,4.),"Evt_Dr_JetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_TaggedJetsAverage","Evt_Dr_TaggedJetsAverage",45,0.4,4.9),"Evt_Dr_TaggedJetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_2JetsAverage","Evt_Dr_2JetsAverage",35,0.5,4.),"Evt_Dr_2JetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_2TaggedJetsAverage","Evt_Dr_2TaggedJetsAverage",45,0.4,4.9),"Evt_Dr_2TaggedJetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_3JetsAverage","Evt_Dr_3JetsAverage",35,0.5,4.),"Evt_Dr_3JetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_3TaggedJetsAverage","Evt_Dr_3TaggedJetsAverage",45,0.4,4.9),"Evt_Dr_3TaggedJetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_4JetsAverage","Evt_Dr_4JetsAverage",35,0.5,4.),"Evt_Dr_4JetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_4TaggedJetsAverage","Evt_Dr_4TaggedJetsAverage",45,0.4,4.9),"Evt_Dr_4TaggedJetsAverage",plotselection,plotlabel),

       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_UntaggedJetsAverage","Evt_Dr_UntaggedJetsAverage",50,0.,5),"Evt_Dr_UntaggedJetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_M2_JetsAverage","Evt_M2_JetsAverage",50,0,250),"Evt_M2_JetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_M2_UntaggedJetsAverage","Evt_M2_UntaggedJetsAverage",50,0.,250),"Evt_M2_UntaggedJetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",50,0.,250),"Evt_M2_TaggedJetsAverage",plotselection,plotlabel),

       Plot(ROOT.TH1F(plotprefix+"Evt_M2_2JetsAverage","Evt_M2_2JetsAverage",50,0,250),"Evt_M2_2JetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_M2_2TaggedJetsAverage","Evt_M2_2TaggedJetsAverage",50,0.,250),"Evt_M2_2TaggedJetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_M2_3JetsAverage","Evt_M2_3JetsAverage",50,0,250),"Evt_M2_3JetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_M2_3TaggedJetsAverage","Evt_M2_3TaggedJetsAverage",50,0.,250),"Evt_M2_3TaggedJetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_M2_4JetsAverage","Evt_M2_4JetsAverage",50,0,250),"Evt_M2_4JetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_M2_4TaggedJetsAverage","Evt_M2_4TaggedJetsAverage",50,0.,250),"Evt_M2_4TaggedJetsAverage",plotselection,plotlabel),

       Plot(ROOT.TH1F(plotprefix+"Evt_M_MinDeltaRJets","Evt_M_MinDeltaRJets",30,0.,150),"Evt_M_MinDeltaRJets",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",45,0.,450),"Evt_M_MinDeltaRTaggedJets",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_M_MinDeltaRUntaggedJets","Evt_M_MinDeltaRUntaggedJets",45,0.,450),"Evt_M_MinDeltaRUntaggedJets",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_M_MinDeltaRLeptonJet","Evt_M_MinDeltaRLeptonJet",60,0.4,3.4),"Evt_M_MinDeltaRLeptonJet",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRJets","Evt_Dr_MinDeltaRJets",50,0.,5.0),"Evt_Dr_MinDeltaRJets",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRTaggedJets","Evt_Dr_MinDeltaRTaggedJets",50,0.,5.0),"Evt_Dr_MinDeltaRTaggedJets",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRUntaggedJets","Evt_Dr_MinDeltaRUntaggedJets",50,0.,5.0),"Evt_Dr_MinDeltaRUntaggedJets",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRLeptonJet","Evt_Dr_MinDeltaRLeptonJet",60,0.4,3.4),"Evt_Dr_MinDeltaRLeptonJet",plotselection,plotlabel),

       Plot(ROOT.TH1F(plotprefix+"Evt_Jet_MaxDeta_Jets","Evt_Jet_MaxDeta_Jets",50,0.,5.0),"Evt_Jet_MaxDeta_Jets",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_TaggedJet_MaxDeta_Jets","Evt_TaggedJet_MaxDeta_Jets",50,0.,5.0),"Evt_TaggedJet_MaxDeta_Jets",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_TaggedJet_MaxDeta_TaggedJets","Evt_TaggedJet_MaxDeta_TaggedJets",60,0.,6.0),"Evt_TaggedJet_MaxDeta_TaggedJets",plotselection,plotlabel),

       Plot(ROOT.TH1F(plotprefix+"Evt_M_Total","Evt_M_Total",40,0.,4000),"Evt_M_Total",plotselection,plotlabel),

       Plot(ROOT.TH1F(plotprefix+"Evt_H0","Evt_H0",40,0.5,4.5),"Evt_H0",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_H1","Evt_H1",60,-0.2,0.4),"Evt_H1",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_H2","Evt_H2",60,-0.2,0.4),"Evt_H2",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_H3","Evt_H3",50,-0.05,1.05),"Evt_H3",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_H4","Evt_H4",50,-0.15,0.35),"Evt_H4",plotselection,plotlabel),

       Plot(ROOT.TH1F(plotprefix+"Sphericity","Sphericity",50,0,1),"Evt_Sphericity",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Aplanarity","Aplanarity",50,0,0.5),"Evt_Aplanarity",plotselection,plotlabel),
]

plotlabel="1 lepton, 4 jets, 3 b-tags"
plotselection=categoriesJT[1][0]
plotprefix="s43_"
plots43=[
          Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_avg_btag_disc_btags","avg CSV (tags)",30,0.8,1.05),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_HT","HT",20,0,1000),"BDT_common5_input_HT",plotselection,plotlabel),
          #Plot(ROOT.TH1F(plotprefix+"s43_MEM_transformed","MEM discriminator",24,0,1.2),"(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_sphericity","sphericity",20,0,1),"BDT_common5_input_sphericity",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_third_highest_btag","third highest btag",22,0.79,1),"BDT_common5_input_third_highest_btag",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"s43_Evt_CSV_Average","avg CSV (jets)",20,0.6,1),"Evt_CSV_Average",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_M3","M3",30,0,600),"BDT_common5_input_M3",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_all_sum_pt_with_met","#sum p_{T} (lepton,jet,met)",20,0,1000),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_h1","H_{1}",30,-0.2,0.4),"BDT_common5_input_h1",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_pt_all_jets_over_E_all_jets","(#sum jet p_{T})/(#sum jet E))",20,0.2,1.2),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_dr_between_lep_and_closest_jet","#Delta R (lepton,jet)",35,0,3.5),"BDT_common5_input_dr_between_lep_and_closest_jet",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_first_jet_pt","jet 1 p_{T}",50,0,500),"BDT_common5_input_first_jet_pt",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_closest_tagged_dijet_mass","closest tagged dijet mass",20,0,400),"BDT_common5_input_closest_tagged_dijet_mass",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"s43_blr","B-tagging likelihood ratio",30,-3,8),"Evt_blr_ETH_transformed",'(N_Jets==4&&N_BTagsM==3)',plotlabel),
	         Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",20,0,4),"BDT_common5_input_avg_dr_tagged_jets",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_dev_from_avg_disc_btags","dev from avg CSV (tags)",25,0,0.008),"BDT_common5_input_dev_from_avg_disc_btags",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_min_dr_tagged_jets","min #Delta R(tag,tag)",30,0.3,3.5),"BDT_common5_input_min_dr_tagged_jets",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_h3","H_{3}",30,-0.2,0.9),"BDT_common5_input_h3",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_second_jet_pt","jet 2 p_{T}",40,0,300),"BDT_common5_input_second_jet_pt",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_fourth_jet_pt","jet 4 p_{T}",32,0,160),"BDT_common5_input_fourth_jet_pt",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_maxeta_tag_tag","max #Delta #eta(tag,tag)",20,0.,1.6),"BDT_common5_input_maxeta_tag_tag",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_maxeta_jet_tag","max #Delta #eta(jet,tag)",20,0.,1.6),"BDT_common5_input_maxeta_jet_tag",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"s43_Evt_Deta_JetsAverage","avg #Delta #eta (jet,jet)",20,0,3),"Evt_Deta_JetsAverage",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_third_jet_pt","jet 1 p_{T}",40,0,500),"BDT_common5_input_third_jet_pt",plotselection,plotlabel),
]

        
plotlabel="1 lepton, 4 jets, 4 b-tags"
plotselection=categoriesJT[4][0]
plotprefix="s44_"
# weights_Final_44_MEMBDTv2.xml
plots44=[
          #Plot(ROOT.TH1F(plotprefix+"s44_MEM_transformed","MEM discriminator",6,0,1.2),"(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)","(N_Jets==4&&N_BTagsM>=4)",plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_btag_disc_btags","avg CSV tagged",6,0.8,1.05),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fourth_jet_pt","jet 4 p_{T}",7,30,100),"BDT_common5_input_fourth_jet_pt",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_first_jet_pt","jet 1 p_{T}",15,0,400),"BDT_common5_input_first_jet_pt",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"Evt_Deta_JetsAverage","avg #Delta #eta (jet,jet)",15,0,3),"Evt_Deta_JetsAverage",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","#Delta R (lepton,jet)",16,0,3.2),"BDT_common5_input_dr_between_lep_and_closest_jet",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fourth_highest_btag","fourth-highest CSV",11,0.8,1),"BDT_common5_input_fourth_highest_btag",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_aplanarity","aplanarity",9,0,0.3),"BDT_common5_input_aplanarity",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_invariant_mass_of_everything","mass(jets,lepton,MET)",15,0,1500),"BDT_common5_input_invariant_mass_of_everything",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_M3","M3",15,0,800),"BDT_common5_input_M3",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"blr","B-tagging likelihood ratio",12,0,12),"Evt_blr_ETH_transformed",'(N_Jets==4&&N_BTagsM>=4)',plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",10,1.6,3.6),"BDT_common5_input_avg_dr_tagged_jets",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","closest tagged dijet mass",10,0,200),"BDT_common5_input_closest_tagged_dijet_mass",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_min_dr_tagged_jets","min #Delta R (tag,tag)",12,0,2.4),"BDT_common5_input_min_dr_tagged_jets",plotselection,plotlabel),
 	       Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_tag_tag","max #Delta #eta (tag,tag)",15,0,1.5),"BDT_common5_input_maxeta_tag_tag",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_all_sum_pt_with_met","#sum p_{T} (lepton,jet,met)",10,0,1000),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_HT","HT",15,0,1000),"BDT_common5_input_HT",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h1","H_{1}",15,-0.2,0.4),"BDT_common5_input_h1",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_third_highest_btag","third-highest CSV",11,0.8,1),"BDT_common5_input_third_highest_btag",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h3","H_{3}",15,-0.2,1.0),"BDT_common5_input_h3",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_Mlb","mass(lepton,closest tag)",15,0,250),"BDT_common5_input_Mlb",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_second_highest_btag","second-highest CSV",11,0.8,1),"BDT_common5_input_second_highest_btag",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_jet_jet","max #Delta #eta(jet,jet)",14,0.2,1.6),"BDT_common5_input_maxeta_jet_jet",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_jet_tag","max #Delta #eta(jet,tag)",14,0.2,1.6),"BDT_common5_input_maxeta_jet_tag",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","(#sum jet p_{T})/(#sum jet E))",20,0.2,1.2),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h0","H_{0}",15,0.2,0.4),"BDT_common5_input_h0",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_second_jet_pt","jet 2 p_{T}",20,0,250),"BDT_common5_input_second_jet_pt",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","dev from avg CSV (tags)",15,0,0.008),"BDT_common5_input_dev_from_avg_disc_btags",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h2","H_{2}",15,-0.2,0.4),"BDT_common5_input_h2",plotselection,plotlabel),
]


plotlabel="1 lepton, 5 jets, 3 b-tags"
plotselection=categoriesJT[2][0]
plotprefix="s53_"
plots53=[
          #Plot(ROOT.TH1F(plotprefix+"MEM_transformed","MEM discriminator",20,0,1),"(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","(#sum jet p_{T})/(#sum jet E))",20,0.2,1.2),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_all_sum_pt_with_met","#sum p_{T} (lepton,jet,met)",30,0,1500),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_third_highest_btag","third highest CSV",22,.8,1),"BDT_common5_input_third_highest_btag",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fourth_highest_btag","fourth highest CSV",22,-.1,1),"BDT_common5_input_fourth_highest_btag",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"Evt_Deta_JetsAverage","avg #Delta #eta jets",25,0,2.5),"Evt_Deta_JetsAverage",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"Evt_CSV_Average","avg CSV",25,0.5,0.9),"Evt_CSV_Average",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"blr","B-tagging likelihood ratio",20,-2,10),"Evt_blr_ETH_transformed",'(N_Jets==5&&N_BTagsM==3)',plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h1","H_{1}",27,-.2,.34),"BDT_common5_input_h1",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",30,0.5,3.5),"BDT_common5_input_avg_dr_tagged_jets",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_sphericity","sphericity",25,0,1),"BDT_common5_input_sphericity",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h3","H_{3}",20,0,1),"BDT_common5_input_h3",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_HT","HT",25,0,1000),"BDT_common5_input_HT",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","dev from ave CSV (tags)",25,0,0.008),"BDT_common5_input_dev_from_avg_disc_btags",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_min_dr_tagged_jets","min #Delta R (tag,tag)",25,0,2.4),"BDT_common5_input_min_dr_tagged_jets",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_btag_disc_btags","avg CSV tagged",25,0.8,1.05),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","#Delta R (lepton,jet)",25,0,3.2),"BDT_common5_input_dr_between_lep_and_closest_jet",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_jet_tag","max #Delta #eta(tag,avg jet #eta)",25,0.2,1.6),"BDT_common5_input_maxeta_jet_tag",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_tag_tag","max #Delta #eta (tag,avg tag #eta)",25,0,1.5),"BDT_common5_input_maxeta_tag_tag",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_second_jet_pt","jet 2 p_{T}",20,0,300),"BDT_common5_input_second_jet_pt",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_third_jet_pt","jet 3 p_{T}",20,0,250),"BDT_common5_input_third_jet_pt",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h2","H_{2}",20,0,0.3),"BDT_common5_input_h2",plotselection,plotlabel),
]


plotlabel="1 lepton, 5 jets, #geq4 b-tags"
plotselection=categoriesJT[5][0]
plotprefix="s54_"
plots54=[
          #Plot(ROOT.TH1F(plotprefix+"MEM_transformed","MEM discriminator",10,0,1),"(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_btag_disc_btags","avg CSV (tags)",7,.8,1.04),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"Evt_Deta_JetsAverage","avg #Delta #eta jets",10,0,2.5),"Evt_Deta_JetsAverage",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fourth_jet_pt","jet 4 p_{T}",15,0,150),"BDT_common5_input_fourth_jet_pt",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_M3","M3",20,0,1000),"BDT_common5_input_M3",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_all_sum_pt_with_met","#sum (lepton pt,jet pt,met)",12,0,1200),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h2","H_{2}",15,-.15,0.3),"BDT_common5_input_h2",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",10,1,4),"BDT_common5_input_avg_dr_tagged_jets",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"blr","B-tagging likelihood ratio",10,-2,12),"Evt_blr_ETH_transformed",'(N_Jets==5&&N_BTagsM>=4)',plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","(#sum jet p_{T})/(#sum jet E))",10,0.2,1.2),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","closest tagged dijet mass",10,0,200),"BDT_common5_input_closest_tagged_dijet_mass",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","tagged dijet mass closest to 125",10,80,180),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_HT","HT",10,0,1000),"BDT_common5_input_HT",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h1","H_{1}",10,-.2,.34),"BDT_common5_input_h1",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_best_higgs_mass","best higgs mass",10,0,400),"BDT_common5_input_best_higgs_mass",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_third_highest_btag","third highest CSV",10,.8,1),"BDT_common5_input_third_highest_btag",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_sphericity","sphericity",10,0,1),"BDT_common5_input_sphericity",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h3","H_{3}",10,0,1),"BDT_common5_input_h3",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fourth_highest_btag","fourth highest CSV",10,0.79,1),"BDT_common5_input_fourth_highest_btag",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fifth_highest_CSV","fifth highest CSV",10,-.1,.91),"BDT_common5_input_fifth_highest_CSV",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_jet_tag","max #Delta #eta(jet,tag)",14,0.2,1.6),"BDT_common5_input_maxeta_jet_tag",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_tag_tag","max #Delta #eta (tag,tag)",15,0,1.5),"BDT_common5_input_maxeta_tag_tag",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_jet_jet","max #Delta #eta (jet,jet)",15,0,1.5),"BDT_common5_input_maxeta_jet_jet",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","#Delta R (lepton,jet)",16,0,3.2),"BDT_common5_input_dr_between_lep_and_closest_jet",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_aplanarity","aplanarity",9,0,0.3),"BDT_common5_input_aplanarity",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_invariant_mass_of_everything","mass(jets,lepton,MET)",15,0,1500),"BDT_common5_input_invariant_mass_of_everything",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_min_dr_tagged_jets","min #Delta R (tag,tag)",12,0,2.4),"BDT_common5_input_min_dr_tagged_jets",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_second_highest_btag","second highest btag",10,.8,1),"BDT_common5_input_second_highest_btag",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h0","H_{0}",10,0.2,1.0),"BDT_common5_input_h0",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"Evt_CSV_Average","avg CSV",10,0.5,1),"Evt_CSV_Average",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_third_jet_pt","jet 3 p_{T}",15,0,200),"BDT_common5_input_third_jet_pt",plotselection,plotlabel),
]


plotlabel="1 lepton, #geq6 jets, 2 b-tags"
plotselection=categoriesJT[0][0]
plotprefix="s62_"
plots62=[
       Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_second_jet_pt","jet 2 p_{T}",20,0,300),"BDT_common5_input_second_jet_pt",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fourth_jet_pt","jet 4 p_{T}",20,0,160),"BDT_common5_input_fourth_jet_pt",plotselection,plotlabel),
	       Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h1","H_{1}",27,-0.2,.34),"BDT_common5_input_h1",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",25,0,5),"BDT_common5_input_avg_dr_tagged_jets",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_sphericity","sphericity",20,0,1),"BDT_common5_input_sphericity",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_third_highest_btag","third highest CSV",22,0,1.1),"BDT_common5_input_third_highest_btag",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h3","H_{3}",20,0,1),"BDT_common5_input_h3",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_HT","HT",20,0,1400),"BDT_common5_input_HT",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_Mlb","mass(lepton,closest tag)",20,0,250),"BDT_common5_input_Mlb",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fifth_highest_CSV","fifth highest CSV",20,-.1,.91),"BDT_common5_input_fifth_highest_CSV",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fourth_highest_btag","fourth highest CSV",20,-.1,.9),"BDT_common5_input_fourth_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"blr","B-tagging likelihood ratio",20,-5,3),"Evt_blr_ETH_transformed",'(N_Jets>=6&&N_BTagsM==2)',plotlabel),
	      Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_min_dr_tagged_jets","min #Delta R (tag,tag)",30,0.5,3.4),"BDT_common5_input_min_dr_tagged_jets",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_btag_disc_btags","avg CSV (tags)",30,.8,1.04),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Deta_JetsAverage","avg #Delta #eta jets",30,0,2.5),"Evt_Deta_JetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_jet_tag","max #Delta #eta(tag, avg jet #eta)",30,0.2,1.6),"BDT_common5_input_maxeta_jet_tag",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_tag_tag","max #Delta #eta (tag,avg tag #eta)",30,0,1.5),"BDT_common5_input_maxeta_tag_tag",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_jet_jet","max #Delta #eta (jet,jet)",30,0,1.5),"BDT_common5_input_maxeta_jet_jet",plotselection,plotlabel),
	       Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","(#sum jet p_{T})/(#sum jet E))",30,0.2,1.1),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_all_sum_pt_with_met","#sum (lepton pt,jet pt,met)",30,200,1300),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h2","H_{2}",30,-.15,0.3),"BDT_common5_input_h2",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_aplanarity","aplanarity",30,0,0.3),"BDT_common5_input_aplanarity",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_CSV_Average","avg CSV",25,0.2,0.65),"Evt_CSV_Average",plotselection,plotlabel),
        
       Plot(ROOT.TH1F(plotprefix+"Evt_Deta_2JetsAverage","Evt_Deta_2JetsAverage", 60,0.0,3),"Evt_Deta_2JetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Deta_3JetsAverage","Evt_Deta_3JetsAverage", 60,0.0,3),"Evt_Deta_3JetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Deta_4JetsAverage","Evt_Deta_4JetsAverage", 60,0.0,3),"Evt_Deta_4JetsAverage",plotselection,plotlabel),


       Plot(ROOT.TH1F(plotprefix+"Evt_Deta_UntaggedJetsAverage","Evt_Deta_UntaggedJetsAverage",45,0.,4.5),"Evt_Deta_UntaggedJetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"Evt_Deta_TaggedJetsAverage","avg #Delta #eta (tag,tag)",45,0.,4.5),"Evt_Deta_TaggedJetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Deta_2TaggedJetsAverage","Evt_Deta_2TaggedJetsAverage", 60,0.0,3),"Evt_Deta_2TaggedJetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Deta_3TaggedJetsAverage","Evt_Deta_3TaggedJetsAverage", 60,0.0,3),"Evt_Deta_3TaggedJetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Deta_4TaggedJetsAverage","Evt_Deta_4TaggedJetsAverage", 60,0.0,3),"Evt_Deta_4TaggedJetsAverage",plotselection,plotlabel),

       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",35,0.5,4.),"Evt_Dr_JetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1F(plotprefix+"Evt_Dr_2JetsAverage","#Delta R (jet 1, jet 2)",35,0.5,4.),"Evt_Dr_2JetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_2TaggedJetsAverage","Evt_Dr_2TaggedJetsAverage",45,0.4,4.9),"Evt_Dr_2TaggedJetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_3JetsAverage","Evt_Dr_3JetsAverage",35,0.5,4.),"Evt_Dr_3JetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_3TaggedJetsAverage","Evt_Dr_3TaggedJetsAverage",45,0.4,4.9),"Evt_Dr_3TaggedJetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_4JetsAverage","Evt_Dr_4JetsAverage",35,0.5,4.),"Evt_Dr_4JetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_4TaggedJetsAverage","Evt_Dr_4TaggedJetsAverage",45,0.4,4.9),"Evt_Dr_4TaggedJetsAverage",plotselection,plotlabel),

       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_UntaggedJetsAverage","Evt_Dr_UntaggedJetsAverage",50,0.,5),"Evt_Dr_UntaggedJetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_M2_JetsAverage","Evt_M2_JetsAverage",50,0,250),"Evt_M2_JetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_M2_UntaggedJetsAverage","Evt_M2_UntaggedJetsAverage",50,0.,250),"Evt_M2_UntaggedJetsAverage",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",50,0.,250),"Evt_M2_TaggedJetsAverage",plotselection,plotlabel),

       #Plot(ROOT.TH1F(plotprefix+"Evt_M2_2JetsAverage","Evt_M2_2JetsAverage",50,0,250),"Evt_M2_2JetsAverage",plotselection,plotlabel),
       #Plot(ROOT.TH1F(plotprefix+"Evt_M2_2TaggedJetsAverage","Evt_M2_2TaggedJetsAverage",50,0.,250),"Evt_M2_2TaggedJetsAverage",plotselection,plotlabel),
       #Plot(ROOT.TH1F(plotprefix+"Evt_M2_3JetsAverage","Evt_M2_3JetsAverage",50,0,250),"Evt_M2_3JetsAverage",plotselection,plotlabel),
       #Plot(ROOT.TH1F(plotprefix+"Evt_M2_3TaggedJetsAverage","Evt_M2_3TaggedJetsAverage",50,0.,250),"Evt_M2_3TaggedJetsAverage",plotselection,plotlabel),
       #Plot(ROOT.TH1F(plotprefix+"Evt_M2_4JetsAverage","Evt_M2_4JetsAverage",50,0,250),"Evt_M2_4JetsAverage",plotselection,plotlabel),
       #Plot(ROOT.TH1F(plotprefix+"Evt_M2_4TaggedJetsAverage","Evt_M2_4TaggedJetsAverage",50,0.,250),"Evt_M2_4TaggedJetsAverage",plotselection,plotlabel),

       Plot(ROOT.TH1F(plotprefix+"Evt_M_MinDeltaRJets","Evt_M_MinDeltaRJets",30,0.,150),"Evt_M_MinDeltaRJets",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",45,0.,450),"Evt_M_MinDeltaRTaggedJets",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_M_MinDeltaRUntaggedJets","Evt_M_MinDeltaRUntaggedJets",45,0.,450),"Evt_M_MinDeltaRUntaggedJets",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_M_MinDeltaRLeptonJet","Evt_M_MinDeltaRLeptonJet",60,0.4,3.4),"Evt_M_MinDeltaRLeptonJet",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRJets","Evt_Dr_MinDeltaRJets",50,0.,5.0),"Evt_Dr_MinDeltaRJets",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRTaggedJets","Evt_Dr_MinDeltaRTaggedJets",50,0.,5.0),"Evt_Dr_MinDeltaRTaggedJets",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRUntaggedJets","Evt_Dr_MinDeltaRUntaggedJets",50,0.,5.0),"Evt_Dr_MinDeltaRUntaggedJets",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRLeptonJet","Evt_Dr_MinDeltaRLeptonJet",60,0.4,3.4),"Evt_Dr_MinDeltaRLeptonJet",plotselection,plotlabel),

       Plot(ROOT.TH1F(plotprefix+"Evt_Jet_MaxDeta_Jets","Evt_Jet_MaxDeta_Jets",50,0.,5.0),"Evt_Jet_MaxDeta_Jets",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_TaggedJet_MaxDeta_Jets","Evt_TaggedJet_MaxDeta_Jets",50,0.,5.0),"Evt_TaggedJet_MaxDeta_Jets",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_TaggedJet_MaxDeta_TaggedJets","Evt_TaggedJet_MaxDeta_TaggedJets",60,0.,6.0),"Evt_TaggedJet_MaxDeta_TaggedJets",plotselection,plotlabel),

       Plot(ROOT.TH1F(plotprefix+"Evt_M_Total","Evt_M_Total",40,0.,4000),"Evt_M_Total",plotselection,plotlabel),

       Plot(ROOT.TH1F(plotprefix+"Evt_H0","Evt_H0",40,0.5,4.5),"Evt_H0",plotselection,plotlabel),
       Plot(ROOT.TH1F(plotprefix+"Evt_H4","Evt_H4",50,-0.15,0.35),"Evt_H4",plotselection,plotlabel),
]


plotlabel="1 lepton, #geq6 jets, 3 b-tags"
plotselection=categoriesJT[3][0]
plotprefix="s63_"
plots63=[
          #Plot(ROOT.TH1F(plotprefix+"MEM_transformed","MEM discriminator",20,0.,1),"(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_jet_tag","max #Delta #eta(tag,avg jet #eta)",14,0.2,1.6),"BDT_common5_input_maxeta_jet_tag",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_tag_tag","max #Delta #eta (tag,tag)",15,0,1.5),"BDT_common5_input_maxeta_tag_tag",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_jet_jet","max #Delta #eta (jet,jet)",15,0,1.5),"BDT_common5_input_maxeta_jet_jet",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","#Delta R (lepton,jet)",16,0,3.2),"BDT_common5_input_dr_between_lep_and_closest_jet",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","dev from ave CSV (tags)",25,0,0.008),"BDT_common5_input_dev_from_avg_disc_btags",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"Evt_Deta_JetsAverage","avg #Delta #eta jets",25,0,2.5),"Evt_Deta_JetsAverage",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_all_sum_pt_with_met","#sum (lepton pt,jet pt,met)",25,0,2000),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fourth_highest_btag","fourth-highest b-tag",18,0,0.9),"BDT_common5_input_fourth_highest_btag",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_aplanarity","aplanarity",20,0,0.4),"BDT_common5_input_aplanarity",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_btag_disc_btags","avg CSV (tags)",30,.8,1.05),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",28,0.5,3.9),"BDT_common5_input_avg_dr_tagged_jets",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fourth_jet_pt","jet 4 p_{T}",20,0,160),"BDT_common5_input_fourth_jet_pt",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","tagged dijet mass closest to 125",30,0,300),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h2","H_{2}",20,-.1,.3),"BDT_common5_input_h2",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fifth_highest_CSV","fifth-highest CSV",20,-.1,.8),"BDT_common5_input_fifth_highest_CSV",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"blr","B-tagging likelihood ratio",20,-2,8),"Evt_blr_ETH_transformed",'(N_Jets>=6&&N_BTagsM==3)',plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_min_dr_tagged_jets","min #Delta R (tag,tag)",17,0,3.4),"BDT_common5_input_min_dr_tagged_jets",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dEta_fn","#sqrt{#Delta #eta(t^{lep}, bb) #times #Delta #eta(t^{had}, bb)}",20,0,5),"BDT_common5_input_dEta_fn",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h1","H_{1}",27,-.2,.34),"BDT_common5_input_h1",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_sphericity","sphericity",20,0,1),"BDT_common5_input_sphericity",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_third_highest_btag","third highest CSV",21,0.79,1),"BDT_common5_input_third_highest_btag",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h3","H_{3}",20,0,1),"BDT_common5_input_h3",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","(#sum jet p_{T})/(#sum jet E))",10,0.2,1.1),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_HT","HT",10,0,2000),"BDT_common5_input_HT",plotselection,plotlabel),
]
   
plotlabel="1 lepton, #geq6 jets, #geq4 b-tags"
plotselection=categoriesJT[6][0]
plotprefix="s64"
plots64=[
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_third_highest_btag","third-highest CSV",16,.8,1.05),"BDT_common5_input_third_highest_btag",plotselection,plotlabel),
          #Plot(ROOT.TH1F(plotprefix+"MEM_transformed","MEM discriminator",10,0,1),"(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"Evt_Deta_JetsAverage","avg #Delta #eta (jet,jet)",14,0,2.8),"Evt_Deta_JetsAverage",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_sphericity","sphericity",20,0,1),"BDT_common5_input_sphericity",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fourth_jet_pt","jet 4 p_{T}",20,0,200),"BDT_common5_input_fourth_jet_pt",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_aplanarity","aplanarity",20,0,0.4),"BDT_common5_input_aplanarity",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_M3","M3",20,0,1000),"BDT_common5_input_M3",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_third_jet_pt","jet 3 p_{T}",20,0,250),"BDT_common5_input_third_jet_pt",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"blr","B-tagging likelihood ratio",14,0,12),"Evt_blr_ETH_transformed",'(N_Jets>=6&&N_BTagsM>=4)',plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",25,1,3.5),"BDT_common5_input_avg_dr_tagged_jets",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_best_higgs_mass","best higgs mass",30,0,600),"BDT_common5_input_best_higgs_mass",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","tagged dijet mass closest to 125",17,40,210),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fourth_highest_btag","fourth highest btag",22,.8,1),"BDT_common5_input_fourth_highest_btag",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","closest tagged dijet mass",25,0,250),"BDT_common5_input_closest_tagged_dijet_mass",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fifth_highest_CSV","fifth highest CSV",22,-.1,1),"BDT_common5_input_fifth_highest_CSV",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_second_highest_btag","second highest btag",22,.8,1),"BDT_common5_input_second_highest_btag",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","min #Delta R (lepton,jet)",25,0,2.5),"BDT_common5_input_dr_between_lep_and_closest_jet",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h3","H_{3}",20,0,1),"BDT_common5_input_h3",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_HT","HT",10,0,2000),"BDT_common5_input_HT",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_all_sum_pt_with_met","#sum (lepton pt,jet pt,met)",10,200,2000),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","(#sum jet p_{T})/(#sum jet E))",10,0.2,1.2),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_invariant_mass_of_everything","mass(jets,lepton,MET)",10,400,1600),"BDT_common5_input_invariant_mass_of_everything",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_jet_tag","max #Delta #eta(jet,tag)",14,0.2,1.6),"BDT_common5_input_maxeta_jet_tag",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_tag_tag","max #Delta #eta (tag,avg tag #eta)",15,0,1.5),"BDT_common5_input_maxeta_tag_tag",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_jet_jet","max #Delta #eta (jet,jet)",15,0,1.5),"BDT_common5_input_maxeta_jet_jet",plotselection,plotlabel),
]

plotlabel="boosted"
plotselection=categoriesJTB[7][0]
plotprefix="sboosted_"
plotsBoosted=[
          Plot(ROOT.TH1F(plotprefix+"BoostedTopHiggs_HiggsCandidate_M2","Di-filterjet mass of Higgs candidate",25,0,250),"BoostedTopHiggs_HiggsCandidate_M2",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BoostedTopHiggs_HiggsCandidate_Pt2","BoostedTopHiggs_HiggsCandidate_Pt2",20,30,600),"BoostedTopHiggs_HiggsCandidate_Pt2",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"blr","B-tagging likelihood ratio",15,-5,10),"Evt_blr_ETH_transformed",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BoostedTopHiggs_HiggsCandidate_Subjetiness21","2-subjettiness / 1-subjettiness of Higgs candidate",20,0,1),"BoostedTopHiggs_HiggsCandidate_Subjetiness2/BoostedTopHiggs_HiggsCandidate_Subjetiness1",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BoostedTopHiggs_HiggsCandidate_Dr_Lepton","BoostedTopHiggs_HiggsCandidate_Dr_Lepton",20,0,4),"BoostedTopHiggs_HiggsCandidate_Dr_Lepton",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"BoostedTopHiggs_HiggsCandidate_Deta_TopHadCandidate","#Delta #eta (boosted Higgs cand., boosted top cand.)",20,0,4),"BoostedTopHiggs_HiggsCandidate_Deta_TopHadCandidate",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"Evt_HT","Evt_HT",20,200,2000),"Evt_HT",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRTaggedJets","min #Delta R (tag,tag)",20,0,4),"Evt_Dr_MinDeltaRTaggedJets",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",20,0,600),"Evt_M_MinDeltaRTaggedJets",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"Evt_Dr_TaggedJetsAverage","avg #Delta R (tag,tag)",20,0,4),"Evt_Dr_TaggedJetsAverage",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"Evt_Sphericity","Evt_Sphericity",20,0,1),"Evt_Sphericity",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BoostedTopHiggs_TopHadCandidate_Top_M","BoostedTopHiggs_TopHadCandidate_Top_M",20,29,300),"BoostedTopHiggs_TopHadCandidate_Top_M",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BoostedTopHiggs_TopHadCandidate_B_CSV","BoostedTopHiggs_TopHadCandidate_B_CSV",20,-0.1,1),"BoostedTopHiggs_TopHadCandidate_B_CSV",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BoostedTopHiggs_TopHadCandidate_W1_CSV","BoostedTopHiggs_TopHadCandidate_W1_CSV",20,-0.1,1),"BoostedTopHiggs_TopHadCandidate_W1_CSV",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BoostedTopHiggs_TopHadCandidate_W2_CSV","BoostedTopHiggs_TopHadCandidate_W2_CSV",20,-0.1,1),"BoostedTopHiggs_TopHadCandidate_W2_CSV",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"Evt_H0","Evt_H0",20,0.2,0.5),"Evt_H0",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"Evt_H3","Evt_H3",20,0,1),"Evt_H3",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"Evt_JetPtOverJetE","Evt_JetPtOverJetE",20,0,1),"Evt_JetPtOverJetE",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"Evt_Deta_JetsAverage","Evt_Deta_JetsAverage",20,0,2.5),"Evt_Deta_JetsAverage",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"CSV2","third highest b-tag",20,-0.1,1),"CSV[2]",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"CSV3","fourth highest b-tag",20,-0.1,1),"CSV[3]",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"CSV4","CSV4",20,-0.1,1),"CSV[4]",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"Evt_CSV_Average","average b-tag",17,0.3,1),"Evt_CSV_Average",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"Evt_TaggedJet_MaxDeta_TaggedJets","Evt_TaggedJet_MaxDeta_TaggedJets",20,0,4),"Evt_TaggedJet_MaxDeta_TaggedJets",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"Evt_M_MedianTaggedJets","Evt_M_MedianTaggedJets",20,0,800),"Evt_M_MedianTaggedJets",plotselection,plotlabel),
#          Plot(ROOT.TH1F(plotprefix+"Evt_Deta_2TaggedJetsAverage","Evt_Deta_2TaggedJetsAverage",20,0,4),"Evt_Deta_2TaggedJetsAverage",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"Evt_Aplanarity","Aplanarity",17,0,0.34),"Evt_Aplanarity",plotselection,plotlabel),
          Plot(ROOT.TH1F(plotprefix+"MEM","MEM discriminator (using subjets)",22,0,1),"(BoostedTopHiggs_MEM_p>=0.0)*(BoostedTopHiggs_MEM_p_sig/(BoostedTopHiggs_MEM_p_sig+0.15*BoostedTopHiggs_MEM_p_bkg))+(BoostedTopHiggs_MEM_p<0.0)*(0.01)",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dEta_fn","#sqrt{#Delta #eta(t^{lep}, bb) #times #Delta #eta(t^{had}, bb)}",20,0,5),"BDT_common5_input_dEta_fn",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_invariant_mass_of_everything","BDT_common5_input_invariant_mass_of_everything",20,0,3000),"BDT_common5_input_invariant_mass_of_everything",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","BDT_common5_input_dev_from_avg_disc_btags",20,0,0.006),"BDT_common5_input_dev_from_avg_disc_btags",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_Mlb","BDT_common5_input_Mlb",20,0,200),"BDT_common5_input_Mlb",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"Evt_M_Total","Evt_M_Total",20,400,4000),"Evt_M_Total",plotselection,plotlabel),
         Plot(ROOT.TH1F(plotprefix+"Evt_CSV_Dev","Evt_CSV_Dev",20,0,0.25),"Evt_CSV_Dev",plotselection,plotlabel),
]

bdtplots=plots64+plots63+plots62+plots54+plots53+plots44+plots43+plotsBoosted
#plots+=bdtplots
#plots+=plots62+plots63

print name,2000000,plots,samples+samples_data,[''],['1.'],weightsystnames, systweights
outputpath=plotParallel(name,2000000,plots,samples+samples_data+systsamples,[''],['1.'],weightsystnames, systweights)

# plot dataMC comparison
listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots,1)
if not os.path.exists(outputpath[:-4]+'_syst.root') or not askYesNo('reuse systematic histofile?'):
    renameHistos(outputpath,outputpath[:-4]+'_syst.root',allsystnames,False)
lll=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots,errorSystnames)
#lllcsv=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots,CSVSystnames)

for hld,hl in zip(listOfHistoListsData,listOfHistoLists):
    
  makeEventyields=False

  if "optD" in hld[0].GetName():
    makeEventyields=True
    for h in hld+hl:
      for i,cat in enumerate(categoriesSplitByBDToptD):
        h.GetXaxis().SetBinLabel(i+1,cat[1])
    tablepath=("/".join((outputpath.split('/'))[:-1]))+"/"+name+"_yieldsD"
  #elif "JTB" in hld[0].GetName():
    #makeEventyields=True
    #for h in hld+hl:
      #for i,cat in enumerate(categoriesJTB):
        #h.GetXaxis().SetBinLabel(i+1,cat[1])
    #tablepath=("/".join((outputpath.split('/'))[:-1]))+"/"+name+"_yieldsJTB"
  elif "JT" in hld[0].GetName():
    makeEventyields=True
    for h in hld+hl:
      for i,cat in enumerate(categoriesJT):
        h.GetXaxis().SetBinLabel(i+1,cat[1])
    tablepath=("/".join((outputpath.split('/'))[:-1]))+"/"+name+"_yieldsJT"
  
  # make an event yield table
  if makeEventyields:
    eventYields(hld,hl,samples,tablepath)

labels=[plot.label for plot in plots]
lolT=transposeLOL(listOfHistoLists)
plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],-1,name,[[lll,3354,ROOT.kBlack,True]],False,labels)

#exit(0)

# make log plots
listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots,1)
lll=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots,errorSystnames)
#lllcsv=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots,CSVSystnames)
labels=[plot.label for plot in plots]
lolT=transposeLOL(listOfHistoLists)
plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],-1,name+'_log',[[lll,3354,ROOT.kBlack,True]],True,labels)

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
plotDataMCanWsystCustomBinLabels(listOfHistoListsDataForCategories,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],-1,name+'Categories_log',[[lllForCategories,3354,ROOT.kBlack,True]],listOfcustomBinLabels,True,labels,True)



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
plotDataMCanWsystCustomBinLabels(listOfHistoListsDataForCategoriesNL,transposeLOL(lolTNL[1:]),samples[1:],lolTNL[0],samples[0],-1,name+'Categories_nolog',[[lllForCategoriesNL,3354,ROOT.kBlack,True]],listOfcustomBinLabels,False,labels,True)

