import sys
import os

filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = "/".join(filedir.split("/")[:-1])

sys.path.append(pyrootdir)
import util.tools.plotClasses as plotClasses
import ROOT


categoriesJT = [
	("(N_Jets>=6&&N_BTagsM==2)","6j2t",""),
    ("(N_Jets==4&&N_BTagsM==3)","4j3t",""),
    ("(N_Jets==5&&N_BTagsM==3)","5j3t",""),
    ("(N_Jets>=6&&N_BTagsM==3)","6j3t",""),
    ("(N_Jets==4&&N_BTagsM>=4)","4j4t",""),
    ("(N_Jets==5&&N_BTagsM>=4)","5j4t",""),
    ("(N_Jets>=6&&N_BTagsM>=4)","6j4t","")
	]

# define event yield categories
def evtYieldCategories():
	return categoriesJT

# selection for categories
categoriesJTsel="("+categoriesJT[0][0]
for cat in categoriesJT[1:]:
	categoriesJTsel+="||"+cat[0]
categoriesJTsel+=")"

# category strings 
catstringJT="0"
for i,cat in enumerate(categoriesJT):
	catstringJT+=("+"+str(i+1)+"*"+cat[0])

def add_plots():
	# book plots
	plotlabel="t#bar{t}+b-jets, semileptonic top decays"
	#plotlabelboosted="#splitline{1 lepton, #geq 4 jets, #geq 2 b-tags}{#geq 1 C/A 1.5 jet p_{T} > 200 GeV}"
	plotselection="(1.0)"
	plots=[
		# ~ plotClasses.Plot(ROOT.TH1D("AdditionalBHadrons_Dr" ,"additional b-hadron #Delta{R}",1200,0.0,12.0),"AdditionalBHadrons_Dr",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("AdditionalBHadrons_GenJet_Dr" ,"additional b-hadron-jet #Delta{R}",1200,0.0,12.0),"AdditionalBHadrons_GenJet_Dr",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("AdditionalBHadrons_GenJet_M" ,"additional b-hadron-jet M [GeV]",200,0.0,2000.0),"AdditionalBHadrons_GenJet_M",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("AdditionalBHadrons_M" ,"additional b-hadron M [GeV]",200,0.0,2000.0),"AdditionalBHadrons_M",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("Weight" ,"Weight",1000,0.0,1.0),"Weight",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("Weight_GEN_nom" ,"Weight_GEN_nom",2600,-3000.0,10000.0),"Weight_GEN_nom",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("Weight_GenValue" ,"Weight_GenValue",2600,-3000.0,10000.0),"Weight_GenValue",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("Weight_XS" ,"Weight_XS",1000,0.0,1.0),"Weight_XS",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("N_AdditionalBHadrons" ,"additional b-hadron multiplicity",41,-0.5,40.5),"N_AdditionalBHadrons",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("N_AdditionalGenBJets" ,"additional b-jet multiplicity",41,-0.5,40.5),"N_AdditionalGenBJets",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("N_AdditionalLightGenJets" ,"additional light flavor jet multiplicity",41,-0.5,40.5),"N_AdditionalLightGenJets",plotselection,plotlabel),
		plotClasses.Plot(ROOT.TH1D("N_GenJets" ,"jet multiplicity",41,-0.5,40.5),"N_GenJets",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("N_GenTopHad" ," multiplicity from top quark",41,-0.5,40.5),"N_GenTopHad",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("N_GenTopLep" ," multiplicity from top quark",41,-0.5,40.5),"N_GenTopLep",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("AdditionalBHadron_E" ,"additional b-hadron E [GeV]",420,0.0,4200.0),"AdditionalBHadron_E",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("AdditionalBHadron_Eta" ,"additional b-hadron #eta",1600,-8.0,8.0),"AdditionalBHadron_Eta",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("AdditionalBHadron_Phi" ,"additional b-hadron #Phi",700,-3.5,3.5),"AdditionalBHadron_Phi",plotselection,plotlabel),
		plotClasses.Plot(ROOT.TH1D("AdditionalBHadron_Pt" ,"additional b-hadron p_{T} [GeV]",25,0.0,1000.0),"AdditionalBHadron_Pt",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("AdditionalGenBJet_E" ,"additional b-jet E [GeV]",420,0.0,4200.0),"AdditionalGenBJet_E",plotselection,plotlabel),
		plotClasses.Plot(ROOT.TH1D("AdditionalGenBJet_Eta" ,"additional b-jet #eta",30,-3.0,3.0),"AdditionalGenBJet_Eta",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("AdditionalGenBJet_HadronPt" ,"additional b-hadron p_{T} [GeV]",250,0.0,2500.0),"AdditionalGenBJet_HadronPt",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("AdditionalGenBJet_NHadrons" ,"additional b-hadron multiplicity",41,-0.5,40.5),"AdditionalGenBJet_NHadrons",plotselection,plotlabel),
		plotClasses.Plot(ROOT.TH1D("AdditionalGenBJet_Phi" ,"additional b-jet #varphi",28,-3.5,3.5),"AdditionalGenBJet_Phi",plotselection,plotlabel),
		plotClasses.Plot(ROOT.TH1D("AdditionalGenBJet_Pt" ,"additional b-jet p_{T} [GeV]",25,0.0,1000.0),"AdditionalGenBJet_Pt",plotselection,plotlabel),
		plotClasses.Plot(ROOT.TH1D("AdditionalGenBJet_1st_Pt" ,"additional b-jet p_{T} [GeV] of leading jet",25,0.0,1000.0),"AdditionalGenBJet_Pt[0]",plotselection,plotlabel),
		plotClasses.Plot(ROOT.TH1D("AdditionalGenBJet_2nd_Pt" ,"additional b-jet p_{T} [GeV] of second jet",25,0.0,1000.0),"AdditionalGenBJet_Pt[1]",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("AdditionalLightGenJet_E" ,"additional light flavor jet E [GeV]",420,0.0,4200.0),"AdditionalLightGenJet_E",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("AdditionalLightGenJet_Eta" ,"additional light flavor jet #eta",600,-3.0,3.0),"AdditionalLightGenJet_Eta",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("AdditionalLightGenJet_Phi" ,"additional light flavor jet #Phi",700,-3.5,3.5),"AdditionalLightGenJet_Phi",plotselection,plotlabel),
		plotClasses.Plot(ROOT.TH1D("AdditionalLightGenJet_Pt" ,"additional light flavor jet p_{T} [GeV]",25,0.0,1000.0),"AdditionalLightGenJet_Pt",plotselection,plotlabel),
		plotClasses.Plot(ROOT.TH1D("AdditionalLightGenJet_1st_Pt" ,"additional light flavor jet p_{T} [GeV] of leading jet",25,0.0,1000.0),"AdditionalLightGenJet_Pt[0]",plotselection,plotlabel),
		plotClasses.Plot(ROOT.TH1D("AdditionalLightGenJet_2nd_Pt" ,"additional light flavor jet p_{T} [GeV] of second jet",25,0.0,1000.0),"AdditionalLightGenJet_Pt[1]",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenJet_E" ,"jet E [GeV]",420,0.0,4200.0),"GenJet_E",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenJet_Eta" ,"jet #eta",600,-3.0,3.0),"GenJet_Eta",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenJet_Jet_DeltaR" ,"jet #Delta{R}",1200,0.0,12.0),"GenJet_Jet_DeltaR",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenJet_Jet_E" ,"jet E [GeV]",420,0.0,4200.0),"GenJet_Jet_E",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenJet_Jet_Eta" ,"jet #eta",600,-3.0,3.0),"GenJet_Jet_Eta",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenJet_Jet_Phi" ,"jet #Phi",700,-3.5,3.5),"GenJet_Jet_Phi",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenJet_Jet_Pt" ,"jet p_{T} [GeV]",250,0.0,2500.0),"GenJet_Jet_Pt",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenJet_Phi" ,"jet #Phi",700,-3.5,3.5),"GenJet_Phi",plotselection,plotlabel),
		plotClasses.Plot(ROOT.TH1D("GenJet_Pt" ,"jet p_{T} [GeV]",25,0.0,1000.0),"GenJet_Pt",plotselection,plotlabel),
		plotClasses.Plot(ROOT.TH1D("GenJet_1st_Pt" ,"jet p_{T} [GeV] of leading jet",25,0.0,1000.0),"GenJet_Pt[0]",plotselection,plotlabel),
		plotClasses.Plot(ROOT.TH1D("GenJet_2nd_Pt" ,"jet p_{T} [GeV] of second jet",25,0.0,1000.0),"GenJet_Pt[1]",plotselection,plotlabel),
		plotClasses.Plot(ROOT.TH1D("GenJet_3rd_Pt" ,"jet p_{T} [GeV] of third jet",25,0.0,1000.0),"GenJet_Pt[2]",plotselection,plotlabel),
		plotClasses.Plot(ROOT.TH1D("GenJet_4th_Pt" ,"jet p_{T} [GeV] of fourth jet",25,0.0,1000.0),"GenJet_Pt[3]",plotselection,plotlabel),
		plotClasses.Plot(ROOT.TH1D("GenJet_5th_Pt" ,"jet p_{T} [GeV] of fifth jet",25,0.0,1000.0),"GenJet_Pt[4]",plotselection,plotlabel),
		plotClasses.Plot(ROOT.TH1D("GenJet_6th_Pt" ,"jet p_{T} [GeV] of sixth jet",25,0.0,1000.0),"GenJet_Pt[5]",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopHad_B_E" ,"b- E [GeV] from top quark",420,0.0,4200.0),"GenTopHad_B_E",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopHad_B_Eta" ,"b- #eta from top quark",800,-4.0,4.0),"GenTopHad_B_Eta",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopHad_B_GenJet_E" ,"b-jet E [GeV] from top quark",420,0.0,4200.0),"GenTopHad_B_GenJet_E",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopHad_B_GenJet_Eta" ,"b-jet #eta from top quark",600,-3.0,3.0),"GenTopHad_B_GenJet_Eta",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopHad_B_GenJet_Phi" ,"b-jet #Phi from top quark",700,-3.5,3.5),"GenTopHad_B_GenJet_Phi",plotselection,plotlabel),
		plotClasses.Plot(ROOT.TH1D("GenTopHad_B_GenJet_Pt" ,"b-jet p_{T} [GeV] from top quark",25,0.0,1000.0),"GenTopHad_B_GenJet_Pt",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopHad_B_Hadron_E" ,"b-hadron E [GeV] from top quark",420,0.0,4200.0),"GenTopHad_B_Hadron_E",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopHad_B_Hadron_Eta" ,"b-hadron #eta from top quark",1600,-8.0,8.0),"GenTopHad_B_Hadron_Eta",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopHad_B_Hadron_Phi" ,"b-hadron #Phi from top quark",700,-3.5,3.5),"GenTopHad_B_Hadron_Phi",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopHad_B_Hadron_Pt" ,"b-hadron p_{T} [GeV] from top quark",250,0.0,2500.0),"GenTopHad_B_Hadron_Pt",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopHad_B_Phi" ,"b- #Phi from top quark",700,-3.5,3.5),"GenTopHad_B_Phi",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopHad_B_Pt" ,"b- p_{T} [GeV] from top quark",250,0.0,2500.0),"GenTopHad_B_Pt",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopHad_E" ," E [GeV] from top quark",420,0.0,4200.0),"GenTopHad_E",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopHad_Eta" ," #eta from top quark",800,-4.0,4.0),"GenTopHad_Eta",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopHad_Phi" ," #Phi from top quark",700,-3.5,3.5),"GenTopHad_Phi",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopHad_Pt" ," p_{T} [GeV] from top quark",250,0.0,2500.0),"GenTopHad_Pt",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopLep_B_E" ,"b- E [GeV] from top quark",420,0.0,4200.0),"GenTopLep_B_E",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopLep_B_Eta" ,"b- #eta from top quark",800,-4.0,4.0),"GenTopLep_B_Eta",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopLep_B_GenJet_E" ,"b-jet E [GeV] from top quark",420,0.0,4200.0),"GenTopLep_B_GenJet_E",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopLep_B_GenJet_Eta" ,"b-jet #eta from top quark",600,-3.0,3.0),"GenTopLep_B_GenJet_Eta",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopLep_B_GenJet_Phi" ,"b-jet #Phi from top quark",700,-3.5,3.5),"GenTopLep_B_GenJet_Phi",plotselection,plotlabel),
		plotClasses.Plot(ROOT.TH1D("GenTopLep_B_GenJet_Pt" ,"b-jet p_{T} [GeV] from top quark",25,0.0,1000.0),"GenTopLep_B_GenJet_Pt",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopLep_B_Hadron_E" ,"b-hadron E [GeV] from top quark",420,0.0,4200.0),"GenTopLep_B_Hadron_E",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopLep_B_Hadron_Eta" ,"b-hadron #eta from top quark",1600,-8.0,8.0),"GenTopLep_B_Hadron_Eta",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopLep_B_Hadron_Phi" ,"b-hadron #Phi from top quark",700,-3.5,3.5),"GenTopLep_B_Hadron_Phi",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopLep_B_Hadron_Pt" ,"b-hadron p_{T} [GeV] from top quark",250,0.0,2500.0),"GenTopLep_B_Hadron_Pt",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopLep_B_Phi" ,"b- #Phi from top quark",700,-3.5,3.5),"GenTopLep_B_Phi",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopLep_B_Pt" ,"b- p_{T} [GeV] from top quark",250,0.0,2500.0),"GenTopLep_B_Pt",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopLep_E" ," E [GeV] from top quark",420,0.0,4200.0),"GenTopLep_E",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopLep_Eta" ," #eta from top quark",800,-4.0,4.0),"GenTopLep_Eta",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopLep_Phi" ," #Phi from top quark",700,-3.5,3.5),"GenTopLep_Phi",plotselection,plotlabel),
		# ~ plotClasses.Plot(ROOT.TH1D("GenTopLep_Pt" ," p_{T} [GeV] from top quark",250,0.0,2500.0),"GenTopLep_Pt",plotselection,plotlabel),
	]




	plotsAdditional=[
		
	]

	return plots + plotsAdditional


def add_ak8():

	plotlabel="1 lepton, #geq 4 jets, #geq 2 b-tags"
	plotselection="(N_Jets>=4&&N_BTagsM>=2)"
	plotlabelboosted="#splitline{1 lepton, #geq 4 jets, #geq 2 b-tags}{#geq 1 Ak8 jet p_{T} > 200 GeV}"
	plotselectionboosted="(N_Jets>=4&&N_BTagsM>=2&&N_AK8Jets>=1)*(AK8Jet_Pt>200)"
	plotsAK8jets=[
	]

	return plotsAK8jets

# def add_sl4j2t():
# 	plotlabel="1 lepton, 4 jets, 2 b-tags"
# 	plotselection="((N_Jets==4&&N_BTagsM==2))"
# 	#plotselection="((N_Jets==4&&N_BTagsM==2)&&!"+boosted+")"

# 	plotprefix="4j2t"
# 	plots42=[
# 	]

# 	return plots42


# def add_sl5j2t():
# 	plotlabel="1 lepton, 5 jets, 2 b-tags"
# 	plotselection="((N_Jets==5&&N_BTagsM==2))"
# 	#plotselection="((N_Jets==5&&N_BTagsM==2)&&!"+boosted+")"

# 	plotprefix="s52_"
# 	plots52=[
# 	]

# 	return plots52


# def add_sl4j3t():
# 	plotlabel="1 lepton, 4 jets, 3 b-tags"
# 	plotselection=categoriesJT[1][0]
# 	plotprefix="s43_"
# 	plots43=[
# 	]

# 	return plots43



# def add_sl4j4t():
# 	plotlabel="1 lepton, 4 jets, 4 b-tags"
# 	plotselection=categoriesJT[4][0]
# 	plotprefix="s44_"
# 	# weights_Final_44_MEMBDTv2.xml
# 	plots44=[
# 	]

# 	return plots44



# def add_sl5j3t():
# 	plotlabel="1 lepton, 5 jets, 3 b-tags"
# 	plotselection=categoriesJT[2][0]
# 	plotprefix="s53_"
# 	plots53=[
# 	]
	
# 	return plots53


# def add_sl5j4t():
# 	plotlabel="1 lepton, 5 jets, #geq4 b-tags"
# 	plotselection=categoriesJT[5][0]
# 	plotprefix="s54_"
# 	plots54=[
# 	]

# 	return plots54


# def add_sl6j2t():
# 	plotlabel="1 lepton, #geq6 jets, 2 b-tags"
# 	plotselection=categoriesJT[0][0]
# 	plotprefix="s62_"
# 	plots62=[
# 	]
	
# 	return plots62



# def add_sl6j3t():
# 	plotlabel="1 lepton, #geq6 jets, 3 b-tags"
# 	plotselection=categoriesJT[3][0]
# 	plotprefix="s63_"
# 	plots63=[
# 	]

# 	return plots63



# def add_sl6j4t():
# 	plotlabel="1 lepton, #geq6 jets, #geq4 b-tags"
# 	plotselection=categoriesJT[6][0]
# 	plotprefix="s64"
# 	plots64=[
# 	]

# 	return plots64





# def add_sl6j3tDNN():
# 	plotlabel="1 lepton, #geq6 jets, #geq3 b-tags"
# 	plotselection="((N_Jets>=6&&N_BTagsM>=3))"
# 	plotprefix="s63DNN_"
# 	plots63DNN = [
# 	]
	
# 	return plots63DNN


# def add_sl5j3tDNN():
# 	plotlabel="1 lepton, 5 jets, #geq3 b-tags"
# 	plotselection="((N_Jets==5&&N_BTagsM>=3))"
# 	plotprefix="s53DNN_"

# 	plots53DNN = [
# 	]
	
# 	return plots53DNN

# def add_sl4j3tDNN():
# 	plotlabel="1 lepton, 4 jets, #geq3 b-tags"
# 	plotselection="((N_Jets==4&&N_BTagsM>=3))"
# 	plotprefix="s43DNN_"

# 	plots43DNN = [
# 	]







def getDiscriminatorPlots(data = None, discrname = None):
	discriminatorPlots = add_plots()
	#discriminatorPlots += add_ak8()
	# discriminatorPlots += add_sl6j4t()
	# discriminatorPlots += add_sl6j3t()
	# discriminatorPlots += add_sl5j4t()
	# discriminatorPlots += add_sl5j3t()
	# discriminatorPlots += add_sl4j4t()
	# discriminatorPlots += add_sl4j3t()
	# discriminatorPlots += add_sl4j3tDNN()
	# discriminatorPlots += add_sl5j3tDNN()
	# discriminatorPlots += add_sl6j3tDNN()


	return discriminatorPlots

