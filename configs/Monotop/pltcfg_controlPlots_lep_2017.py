import sys
import os
import ROOT
import pandas
import Systematics

filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = os.path.dirname(os.path.dirname(filedir))

sys.path.append(pyrootdir)
import util.tools.plotClasses as plotClasses

def find_masses(dataset_name):
    dataset_name = dataset_name.replace("-","_")
    dataset_name = dataset_name.lower()
    index_1 = dataset_name.find("mphi_")
    index_2 = dataset_name.find("mchi_")
    #print(index_1,index_2)
    number_1 = ""
    number_2 = ""
    for char in dataset_name[index_1+5:]:
        #print(char)
        if not char.isdigit(): break
        number_1+=char
    for char in dataset_name[index_2+5:]:
        #print(char)
        if not char.isdigit(): break
        number_2+=char
    print("Mphi="+number_1+" Mchi="+number_2)
    return number_1,number_2

# samples
# input path
path_mwassmer = "/nfs/dust/cms/user/swieland/monotop/ntuples/2017"

# ======= #
# WEIGHTS #
# ======= #

# generator weight
defaultWeight = "Weight_GEN_nom"


# csv weights
# csvWeightNom = "Weight_CSV"
#csvWeightNom = "1."
csvWeightNom = "("
csvWeightNom += " ((internalCSVweight_medium_0B_final)*(N_BTagsM==0))" #W region
csvWeightNom += "+((internalCSVweight_medium_1B_final)*(N_BTagsM==1))" #SR
csvWeightNom += "+((internalCSVweight_medium_ge2B_final)*(N_BTagsM>=2))" #ttbar region
csvWeightNom += ")"

csvWeightLF_Up = "("
csvWeightLF_Up += " ((internalCSVweight_medium_LFUP_0B_final)*(N_BTagsM==0))" #W region
csvWeightLF_Up += "+((internalCSVweight_medium_LFUP_1B_final)*(N_BTagsM==1))" #SR
csvWeightLF_Up += "+((internalCSVweight_medium_LFUP_ge2B_final)*(N_BTagsM>=2))" #ttbar region
csvWeightLF_Up += ")"

csvWeightLF_Down = "("
csvWeightLF_Down += " ((internalCSVweight_medium_LFDOWN_0B_final)*(N_BTagsM==0))" #W region
csvWeightLF_Down += "+((internalCSVweight_medium_LFDOWN_1B_final)*(N_BTagsM==1))" #SR
csvWeightLF_Down += "+((internalCSVweight_medium_LFDOWN_ge2B_final)*(N_BTagsM>=2))" #ttbar region
csvWeightLF_Down += ")"

csvWeightHF_Up = "("
csvWeightHF_Up += " ((internalCSVweight_medium_HFUP_0B_final)*(N_BTagsM==0))" #W region
csvWeightHF_Up += "+((internalCSVweight_medium_HFUP_1B_final)*(N_BTagsM==1))" #SR
csvWeightHF_Up += "+((internalCSVweight_medium_HFUP_ge2B_final)*(N_BTagsM>=2))" #ttbar region
csvWeightHF_Up += ")"

csvWeightHF_Down = "("
csvWeightHF_Down += " ((internalCSVweight_medium_HFDOWN_0B_final)*(N_BTagsM==0))" #W region
csvWeightHF_Down += "+((internalCSVweight_medium_HFDOWN_1B_final)*(N_BTagsM==1))" #SR
csvWeightHF_Down += "+((internalCSVweight_medium_HFDOWN_ge2B_final)*(N_BTagsM>=2))" #ttbar region
csvWeightHF_Down += ")"

# pile up weights
pileupWeightNom = "internalPUWeight"
pileupWeightUp = "internalPUWeight_Up"
pileupWeightDown = "internalPUWeight_Down"


# lepton and photon scalefactors

electronRecoSFs = "((N_LooseElectrons==2)*LooseElectron_ReconstructionSF[0]*LooseElectron_ReconstructionSF[1]+(N_TightElectrons==1 && N_LooseElectrons==1)*Electron_ReconstructionSF[0]+(N_TightElectrons==0 && N_LooseElectrons==1)*LooseElectron_ReconstructionSF[0]+(N_LooseElectrons==0)*1.)"

electronRecoSFs_up = "((N_LooseElectrons==2)*LooseElectron_ReconstructionSFUp[0]*LooseElectron_ReconstructionSFUp[1]+(N_TightElectrons==1 && N_LooseElectrons==1)*Electron_ReconstructionSFUp[0]+(N_TightElectrons==0 && N_LooseElectrons==1)*LooseElectron_ReconstructionSFUp[0]+(N_LooseElectrons==0)*1.)"

electronRecoSFs_down = "((N_LooseElectrons==2)*LooseElectron_ReconstructionSFDown[0]*LooseElectron_ReconstructionSFDown[1]+(N_TightElectrons==1 && N_LooseElectrons==1)*Electron_ReconstructionSFDown[0]+(N_TightElectrons==0 && N_LooseElectrons==1)*LooseElectron_ReconstructionSFDown[0]+(N_LooseElectrons==0)*1.)"


electronIDSFs = "((N_LooseElectrons==2)*LooseElectron_IdentificationSF[0]*LooseElectron_IdentificationSF[1]+(N_TightElectrons==1 && N_LooseElectrons==1)*Electron_IdentificationSF[0]+(N_TightElectrons==0 && N_LooseElectrons==1)*LooseElectron_IdentificationSF[0]+(N_LooseElectrons==0)*1.)"

electronIDSFs_up = "((N_LooseElectrons==2)*LooseElectron_IdentificationSFUp[0]*LooseElectron_IdentificationSFUp[1]+(N_TightElectrons==1 && N_LooseElectrons==1)*Electron_IdentificationSFUp[0]+(N_TightElectrons==0 && N_LooseElectrons==1)*LooseElectron_IdentificationSFUp[0]+(N_LooseElectrons==0)*1.)"

electronIDSFs_down = "((N_LooseElectrons==2)*LooseElectron_IdentificationSFDown[0]*LooseElectron_IdentificationSFDown[1]+(N_TightElectrons==1 && N_LooseElectrons==1)*Electron_IdentificationSFDown[0]+(N_TightElectrons==0 && N_LooseElectrons==1)*LooseElectron_IdentificationSFDown[0]+(N_LooseElectrons==0)*1.)"


muonIsoSFs = "((N_LooseMuons==2)*LooseMuon_IsolationSF[0]*LooseMuon_IsolationSF[1]+(N_TightMuons==1 && N_LooseMuons==1)*Muon_IsolationSF[0]+(N_TightMuons==0 && N_LooseMuons==1)*LooseMuon_IsolationSF[0]+(N_LooseMuons==0)*1.)"

muonIsoSFs_up = "((N_LooseMuons==2)*LooseMuon_IsolationSFUp[0]*LooseMuon_IsolationSFUp[1]+(N_TightMuons==1 && N_LooseMuons==1)*Muon_IsolationSFUp[0]+(N_TightMuons==0 && N_LooseMuons==1)*LooseMuon_IsolationSFUp[0]+(N_LooseMuons==0)*1.)"

muonIsoSFs_down = "((N_LooseMuons==2)*LooseMuon_IsolationSFDown[0]*LooseMuon_IsolationSFDown[1]+(N_TightMuons==1 && N_LooseMuons==1)*Muon_IsolationSFDown[0]+(N_TightMuons==0 && N_LooseMuons==1)*LooseMuon_IsolationSFDown[0]+(N_LooseMuons==0)*1.)"


muonIDSFs = "((N_LooseMuons==2)*LooseMuon_IdentificationSF[0]*LooseMuon_IdentificationSF[1]+(N_TightMuons==1 && N_LooseMuons==1)*Muon_IdentificationSF[0]+(N_TightMuons==0 && N_LooseMuons==1)*LooseMuon_IdentificationSF[0]+(N_LooseMuons==0)*1.)"

muonIDSFs_up = "((N_LooseMuons==2)*LooseMuon_IdentificationSFUp[0]*LooseMuon_IdentificationSFUp[1]+(N_TightMuons==1 && N_LooseMuons==1)*Muon_IdentificationSFUp[0]+(N_TightMuons==0 && N_LooseMuons==1)*LooseMuon_IdentificationSFUp[0]+(N_LooseMuons==0)*1.)"

muonIDSFs_down = "((N_LooseMuons==2)*LooseMuon_IdentificationSFDown[0]*LooseMuon_IdentificationSFDown[1]+(N_TightMuons==1 && N_LooseMuons==1)*Muon_IdentificationSFDown[0]+(N_TightMuons==0 && N_LooseMuons==1)*LooseMuon_IdentificationSFDown[0]+(N_LooseMuons==0)*1.)"


photonSFs = "((N_LoosePhotons==1 && N_TightPhotons==1)*Photon_IdentificationSF[0]+(N_LoosePhotons==0)*1.)"

photonSFs_up = "((N_LoosePhotons==1 && N_TightPhotons==1)*Photon_IdentificationSFUp[0]+(N_LoosePhotons==0)*1.)"

photonSFs_down = "((N_LoosePhotons==1 && N_TightPhotons==1)*Photon_IdentificationSFDown[0]+(N_LoosePhotons==0)*1.)"


#tauVetoSFs = "internalTauVetoWeight"
#tauVetoSFs_up = "internalTauVetoWeightUp"
#tauVetoSFs_down = "internalTauVetoWeightDown"


# trigger scale factors

triggerSFs = "((N_LooseElectrons>0 && N_LooseMuons==0 && N_LoosePhotons==0)*TriggerSF_SingleElectron+(N_LooseMuons>=0 && N_LooseElectrons==0 && N_LoosePhotons==0)*TriggerSF_SingleMuon+(N_LoosePhotons>0 && N_LooseElectrons==0 && N_LooseMuons==0)*TriggerSF_SinglePhoton)"


electronTriggerSFs_up = "((N_LooseElectrons>0 && N_LooseMuons==0 && N_LoosePhotons==0)*TriggerSF_SingleElectron_Up+(N_LooseMuons>=0 && N_LooseElectrons==0 && N_LoosePhotons==0)*TriggerSF_SingleMuon+(N_LoosePhotons>0 && N_LooseElectrons==0 && N_LooseMuons==0)*TriggerSF_SinglePhoton)"

electronTriggerSFs_down = "((N_LooseElectrons>0 && N_LooseMuons==0 && N_LoosePhotons==0)*TriggerSF_SingleElectron_Down+(N_LooseMuons>=0 && N_LooseElectrons==0 && N_LoosePhotons==0)*TriggerSF_SingleMuon+(N_LoosePhotons>0 && N_LooseElectrons==0 && N_LooseMuons==0)*TriggerSF_SinglePhoton)"


metTriggerSFs_up = "((N_LooseElectrons>0 && N_LooseMuons==0 && N_LoosePhotons==0)*TriggerSF_SingleElectron+(N_LooseMuons>=0 && N_LooseElectrons==0 && N_LoosePhotons==0)*TriggerSF_MET_Up+(N_LoosePhotons>0 && N_LooseElectrons==0 && N_LooseMuons==0)*TriggerSF_SinglePhoton)"

metTriggerSFs_down = "((N_LooseElectrons>0 && N_LooseMuons==0 && N_LoosePhotons==0)*TriggerSF_SingleElectron+(N_LooseMuons>=0 && N_LooseElectrons==0 && N_LoosePhotons==0)*TriggerSF_MET_Down+(N_LoosePhotons>0 && N_LooseElectrons==0 && N_LooseMuons==0)*TriggerSF_SinglePhoton)"


photonTriggerSFs_up = "((N_LooseElectrons>0 && N_LooseMuons==0 && N_LoosePhotons==0)*TriggerSF_SingleElectron+(N_LooseMuons>=0 && N_LooseElectrons==0 && N_LoosePhotons==0)*TriggerSF_MET+(N_LoosePhotons>0 && N_LooseElectrons==0 && N_LooseMuons==0)*TriggerSF_SinglePhoton_Up)"

photonTriggerSFs_down = "((N_LooseElectrons>0 && N_LooseMuons==0 && N_LoosePhotons==0)*TriggerSF_SingleElectron+(N_LooseMuons>=0 && N_LooseElectrons==0 && N_LoosePhotons==0)*TriggerSF_MET+(N_LoosePhotons>0 && N_LooseElectrons==0 && N_LooseMuons==0)*TriggerSF_SinglePhoton_Down)"


muonTriggerSFs_up = "((N_LooseElectrons>0 && N_LooseMuons==0 && N_LoosePhotons==0)*TriggerSF_SingleElectron+(N_LooseMuons>=0 && N_LooseElectrons==0 && N_LoosePhotons==0)*TriggerSF_SingleMuon_Up+(N_LoosePhotons>0 && N_LooseElectrons==0 && N_LooseMuons==0)*TriggerSF_SinglePhoton)"

muonTriggerSFs_down = "((N_LooseElectrons>0 && N_LooseMuons==0 && N_LoosePhotons==0)*TriggerSF_SingleElectron+(N_LooseMuons>=0 && N_LooseElectrons==0 && N_LoosePhotons==0)*TriggerSF_SingleMuon_Down+(N_LoosePhotons>0 && N_LooseElectrons==0 && N_LooseMuons==0)*TriggerSF_SinglePhoton)"


# top pt weight
topptWeightNom = "1."


# higher-order v+jets theory reweighting weight
#bosonWeightNom = "internalBosonWeight"
bosonWeightNom = "internalBosonWeight_monojet"


#deepakMistagSF = "((AK15Jet_TopMatched[0]<0.5)*1.0+(AK15Jet_TopMatched[0]>0.5)*1.)"
#deepakMistagSF_low_up = "((AK15Jet_TopMatched[0]<0.5 && AK15Jet_Pt[0]<400.)*1.5+(AK15Jet_TopMatched[0]>0.5 && AK15Jet_Pt[0]<400.)*1.+(AK15Jet_Pt[0]>=400.)*1.)"
#deepakMistagSF_low_down = "((AK15Jet_TopMatched[0]<0.5 && AK15Jet_Pt[0]<400.)*0.5+(AK15Jet_TopMatched[0]>0.5 && AK15Jet_Pt[0]<400.)*1.+(AK15Jet_Pt[0]>=400.)*1.)"
#deepakMistagSF_high_up = "((AK15Jet_TopMatched[0]<0.5 && AK15Jet_Pt[0]>=400.)*1.5+(AK15Jet_TopMatched[0]>0.5 && AK15Jet_Pt[0]>=400.)*1.+(AK15Jet_Pt[0]<400.)*1.)"
#deepakMistagSF_high_down = "((AK15Jet_TopMatched[0]<0.5 && AK15Jet_Pt[0]>=400.)*0.5+(AK15Jet_TopMatched[0]>0.5 && AK15Jet_Pt[0]>=400.)*1.+(AK15Jet_Pt[0]<400.)*1.)"

#deepakEfficiencySF = "((AK15Jet_TopMatched[0]>0.5)*1.0+(AK15Jet_TopMatched[0]<0.5)*1.)"
#deepakEfficiencySF_low_up = "((AK15Jet_TopMatched[0]>0.5 && AK15Jet_Pt[0]<400.)*1.5+(AK15Jet_TopMatched[0]<0.5 && AK15Jet_Pt[0]<400.)*1.+(AK15Jet_Pt[0]>=400.)*1.)"
#deepakEfficiencySF_low_down = "((AK15Jet_TopMatched[0]>0.5 && AK15Jet_Pt[0]<400.)*0.5+(AK15Jet_TopMatched[0]<0.5 && AK15Jet_Pt[0]<400.)*1.+(AK15Jet_Pt[0]>=400.)*1.)"
#deepakEfficiencySF_high_up = "((AK15Jet_TopMatched[0]>0.5 && AK15Jet_Pt[0]>=400.)*1.5+(AK15Jet_TopMatched[0]<0.5 && AK15Jet_Pt[0]>=400.)*1.+(AK15Jet_Pt[0]<400.)*1.)"
#deepakEfficiencySF_high_down = "((AK15Jet_TopMatched[0]>0.5 && AK15Jet_Pt[0]>=400.)*0.5+(AK15Jet_TopMatched[0]<0.5 && AK15Jet_Pt[0]>=400.)*1.+(AK15Jet_Pt[0]<400.)*1.)"

vvj_sample_renorm_factor = "0.89"
evj_sample_renorm_factor = "0.92"
eej_sample_renorm_factor = "0.92"

prefireWeightNom = "Weight_L1_Prefire"
prefireWeightUp = "Weight_L1_Prefire_Up"
prefireWeightDown = "Weight_L1_Prefire_Down"

# dictionary of expressions to replace in systematics csv
weightReplacements = {
    # default weight
    "DEFAULTWEIGHT": defaultWeight,
    
    # pileup weights
    "PUWEIGHTNOM": pileupWeightNom,
    "PUWEIGHTUP": pileupWeightUp,
    "PUWEIGHTDOWN": pileupWeightDown,
    
    # csv weight
    "CSVWEIGHTNOM": csvWeightNom,
    "CSVWEIGHTLFUP": csvWeightLF_Up,
    "CSVWEIGHTLFDOWN": csvWeightLF_Down,
    "CSVWEIGHTHFUP": csvWeightHF_Up,
    "CSVWEIGHTHFDOWN": csvWeightHF_Down,
    
    # top pt weight
    "TOPPTWEIGHTNOM": topptWeightNom,
    
    # lepton and photon scale factors
    "ELERECOSFNOM": electronRecoSFs,
    "ELERECOSFUP": electronRecoSFs_up,
    "ELERECOSFDOWN": electronRecoSFs_down,
    
    "ELEIDSFNOM": electronIDSFs,
    "ELEIDSFUP": electronIDSFs_up,
    "ELEIDSFDOWN": electronIDSFs_down,
    
    "MUISOSFNOM": muonIsoSFs,
    "MUISOSFUP": muonIsoSFs_up,
    "MUISOSFDOWN": muonIsoSFs_down,
    
    "MUIDSFNOM": muonIDSFs,
    "MUIDSFUP": muonIDSFs_up,
    "MUIDSFDOWN": muonIDSFs_down,
    
    "PHSFNOM": photonSFs,
    "PHSFUP": photonSFs_up,
    "PHSFDOWN": photonSFs_down,
    
    #"TAUVETOSFNOM": tauVetoSFs,
    #"TAUVETOSFUP": tauVetoSFs_up,
    #"TAUVETOSFDOWN": tauVetoSFs_down,
    
    # higher-order v+jets theory reweighting weight
    "BOSONWEIGHTNOM": bosonWeightNom,
    
    "VVJSAMPLERENORMUP" : vvj_sample_renorm_factor,
    "VVJSAMPLERENORMDOWN" : "1.01",
    "EVJSAMPLERENORMUP" : evj_sample_renorm_factor,
    "EVJSAMPLERENORMDOWN" : "1.01",
    "EEJSAMPLERENORMUP" : eej_sample_renorm_factor,
    "EEJSAMPLERENORMDOWN" : "1.01",
    
    # trigger scale factors
    "TRIGGERSFNOM" : triggerSFs,
    "ELTRIGGERSFUP" : electronTriggerSFs_up,
    "ELTRIGGERSFDOWN" : electronTriggerSFs_down,
    
    "MUTRIGGERSFUP" : muonTriggerSFs_up,
    "MUTRIGGERSFDOWN" : muonTriggerSFs_down,
    
    "METTRIGGERSFUP" : metTriggerSFs_up,
    "METTRIGGERSFDOWN" : metTriggerSFs_down,
    
    "PHOTONTRIGGERSFUP" : photonTriggerSFs_up,
    "PHOTONTRIGGERSFDOWN" : photonTriggerSFs_down,
    
    "DEEPAKMISTAGNOM" : "1.",
    #"DEEPAKMISTAGLOWUP" : deepakMistagSF_low_up,
    #"DEEPAKMISTAGLOWDOWN" : deepakMistagSF_low_down,
    #"DEEPAKMISTAGHIGHUP" : deepakMistagSF_high_up,
    #"DEEPAKMISTAGHIGHDOWN" : deepakMistagSF_high_down,
    "DEEPAKEFFICIENCYNOM" : "1.",
    #"DEEPAKEFFICIENCYLOWUP" : deepakEfficiencySF_low_up,
    #"DEEPAKEFFICIENCYLOWDOWN" : deepakEfficiencySF_low_down,
    #"DEEPAKEFFICIENCYHIGHUP" : deepakEfficiencySF_high_up,
    #"DEEPAKEFFICIENCYHIGHDOWN" : deepakEfficiencySF_high_down,
    
    # prefire weights
    "PREFIREWEIGHTNOM": prefireWeightNom,
    "PREFIREWEIGHTUP": prefireWeightUp,
    "PREFIREWEIGHTDOWN": prefireWeightDown,
   
    ## do weights for data
    "DOWEIGHTS": "(DoWeights==1)+(DoWeights==0)*1.0",
}

# Lumi weight
lumi = "41.5"

# nominal weight
nominalweight = (
    "NomWeight:=("
    + defaultWeight
    + "*"
    + pileupWeightNom
    + "*"
    + csvWeightNom
    + "*"
    + topptWeightNom
    + "*"
    + muonIsoSFs
    + "*"
    + muonIDSFs
    + "*"
    + electronRecoSFs
    + "*"
    + electronIDSFs
    + "*"
    + photonSFs
    #+ "*"
    #+ tauVetoSFs
    + "*"
    + bosonWeightNom
    + "*"
    + triggerSFs
    #+ "*"
    #+ deepakMistagSF
    #+ "*"
    #+ deepakEfficiencySF
    + "*"
    + prefireWeightNom
    + ")"
    + "*(DoWeights==1)+(DoWeights==0)*1.0"
)


sampleDict = plotClasses.SampleDictionary()
sampleDict.doPrintout()
doReadTrees = True

# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
samplesDataControlPlots = []
samplesDataControlPlots += [
    plotClasses.Sample(
        "SingleEl",
        ROOT.kBlack,
        path_mwassmer + "/SingleElectron*/*nominal*.root",
        "(N_LooseElectrons>0) && (N_LooseMuons==0) && (N_LoosePhotons==0)",
        "SingleEl",
        samDict=sampleDict,
        readTrees=doReadTrees,
    )
]
samplesDataControlPlots += [
    plotClasses.Sample(
        "SingleMu",
        ROOT.kBlack,
        path_mwassmer + "/SingleMuon*/*nominal*.root",
        "(N_LooseMuons>0) && (N_LooseElectrons==0) && (N_LoosePhotons==0)",
        "SingleMu",
        samDict=sampleDict,
        readTrees=doReadTrees,
    )
]

# print("limit samples")
samples = [
    # signal samples
    #plotClasses.Sample(
        #"#splitline{Vector Monotop}{M_{#phi}=2000 GeV M_{#chi}=500 GeV}",
        #ROOT.kCyan,
        #path_mwassmer + "/Vector_MonoTop_NLO_Mphi-2000_Mchi-500*/*nominal*.root",
        # lumi reweighting factor due to stupid cross section calculation
        #lumi,
        #"vectormonotop_mphi_2000_mchi_500",
        #samDict=sampleDict,
        #readTrees=doReadTrees,
        #typ="signal",
    #),
    plotClasses.Sample(
        "t#bar{t}",
        ROOT.kBlue,
        path_mwassmer + "/TTTo*/*nominal*.root",
        lumi,
        "ttbar",
        samDict=sampleDict,
        readTrees=doReadTrees,
        typ="bkg",
    ),
    # minor samples
    plotClasses.Sample(
        "Single Top",
        ROOT.kBlue - 7,
        path_mwassmer + "/ST_*/*nominal*.root",
        lumi,
        "singlet",
        samDict=sampleDict,
        readTrees=doReadTrees,
        typ="bkg",
    ),
    plotClasses.Sample(
        "Z(#nu#nu)+jets",
        ROOT.kOrange + 7,
        path_mwassmer + "/ZJetsToNuNu_HT*/*nominal*.root",
        lumi,
        "znunujets",
        samDict=sampleDict,
        readTrees=doReadTrees,
        typ="bkg",
    ),
    plotClasses.Sample(
        "Z(ll)+jets",
        ROOT.kOrange + 1,
        path_mwassmer + "/DYJetsToLL_M-50_HT*/*nominal*.root",
        lumi,
        "zlljets",
        samDict=sampleDict,
        readTrees=doReadTrees,
        typ="bkg",
    ),
    plotClasses.Sample(
        "W(l#nu)+jets",
        ROOT.kOrange,
        path_mwassmer + "/WJetsToLNu_HT*/*nominal*.root",
        lumi,
        "wlnujets",
        samDict=sampleDict,
        readTrees=doReadTrees,
        typ="bkg",
    ),
    #plotClasses.Sample(
        #"W(l#nu)+jets + HF",
        #ROOT.kOrange - 1,
        #path_mwassmer + "/WJetsToLNu_HT*/*nominal*.root",
        #lumi + "*(isHF==1)",
        #"wlnujets_hf",
        #samDict=sampleDict,
        #readTrees=doReadTrees,
        #typ="bkg",
    #),
    #plotClasses.Sample(
        #"W(l#nu)+jets + LF",
        #ROOT.kOrange - 2,
        #path_mwassmer + "/WJetsToLNu_HT*/*nominal*.root",
        #lumi + "*(isLF==1)",
        #"wlnujets_lf",
        #samDict=sampleDict,
        #readTrees=doReadTrees,
        #typ="bkg",
    #),
    plotClasses.Sample(
        "#gamma+jets",
        ROOT.kOrange - 4,
        path_mwassmer + "/GJets_HT*/*nominal*.root",
        lumi,
        "gammajets",
        samDict=sampleDict,
        readTrees=doReadTrees,
        typ="bkg",
    ),
    plotClasses.Sample(
        "QCD",
        ROOT.kGray,
        path_mwassmer + "/QCD*/*nominal*.root",
        lumi,
        "qcd",
        samDict=sampleDict,
        readTrees=doReadTrees,
        typ="bkg",
    ),
    plotClasses.Sample(
        "Diboson",
        ROOT.kGreen + 2,
        path_mwassmer + "/??_TuneCP5*/*nominal*.root",
        lumi,
        "diboson",
        samDict=sampleDict,
        readTrees=doReadTrees,
        typ="bkg",
    ),
]

sample_folders = os.listdir(path_mwassmer)
#print(sample_folders)
for sample_folder in sample_folders:
    if "Vector_MonoTop" in sample_folder:
        sample_name = sample_folder
        mphi,mchi = find_masses(sample_name)
        sample_label = "#splitline{Vector Monotop}{M_{#phi}="+mphi+" GeV, "+"M_{#chi}="+mchi+" GeV}"
        print sample_label
        sample_name = sample_name.lower()
        sample_name = sample_name.replace("-","_")
        sample_name = sample_name.replace("_nlo_","_")
        sample_name = sample_name.replace("_13tev_tunecp5_mcatnlo_pythia8","")
        sample_name = sample_name.replace("vector_monotop","vectormonotop")
        samples += [plotClasses.Sample(sample_label,ROOT.kCyan,path_mwassmer+"/"+sample_folder+"/*nominal*.root",lumi,sample_name.lower(),samDict=sampleDict,readTrees=doReadTrees,typ="signal")]

processes = []
for sample in samples:
    processes.append(sample.nick)
list_of_processes = processes
datacard_processes = processes


plottingsamples = [
    # plotClasses.Sample("t#bar{t}Z", ROOT.kCyan,
    #    ttZpath,
    #    lumi+sel_MET+sel_MET,
    #    "ttZ", addsamples = ["ttZbb", "ttZqq", "ttZll"],
    #    samDict = sampleDict, readTrees = doReadTrees, typ = "signal"),
    # plotClasses.Sample(
    # "V+jets",
    # ROOT.kGreen - 3,
    # VJetsPathS,
    # lumi + sel_MET ,
    # "Vjets",
    # addsamples=["wjets", "zjets"],
    # samDict=sampleDict,
    # readTrees=doReadTrees,
    # )
]

# sort subset of processes in plots. descending order
sortedProcesses = []
