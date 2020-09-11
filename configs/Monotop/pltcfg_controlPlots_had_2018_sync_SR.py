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
path_mwassmer = "/nfs/dust/cms/user/mwassmer/MonoTop/ntuples_2018"

# ======= #
# WEIGHTS #
# ======= #

# generator weight
defaultWeight = "Weight_GEN_nom"


# csv weight
# csvWeightNom = "1."
csvWeightNom = "(internalCSVweight_loose_outside_0B_final)"

csvWeightLF_Up = "(internalCSVweight_loose_outside_LFUP_0B_final)"
csvWeightLF_Down = "(internalCSVweight_loose_outside_LFDOWN_0B_final)"

csvWeightHF_Up = "(internalCSVweight_loose_outside_HFUP_0B_final)"
csvWeightHF_Down = "(internalCSVweight_loose_outside_HFDOWN_0B_final)"

# pile up weights
pileupWeightNom = "internalPUWeight_2018"
pileupWeightUp = "internalPUWeight_2018_Up"
pileupWeightDown = "internalPUWeight_2018_Down"



# trigger scale factors

# triggerSFs = "((N_LooseElectrons>0 && N_LooseMuons==0 && N_LoosePhotons==0)*TriggerSF_SingleElectron+(N_LooseMuons>=0 && N_LooseElectrons==0 && N_LoosePhotons==0)*TriggerSF_MET+(N_LoosePhotons>0 && N_LooseElectrons==0 && N_LooseMuons==0)*TriggerSF_SinglePhoton)"
triggerSFs = "(TriggerSF_MET)"

metTriggerSFs_up = "(TriggerSF_MET_Up)"
metTriggerSFs_down = "(TriggerSF_MET_Down)"

# top pt weight
topptWeightNom = "1."


# higher-order v+jets theory reweighting weight
bosonWeightNom = "internalBosonWeight"


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

vvj_sample_renorm_factor = "1.1"
evj_sample_renorm_factor = "1.07"
eej_sample_renorm_factor = "1.1"

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
    "ELEVETOSFNOM" : "EleVetoWeight",
    
    # "ELERECOSFNOM": "1.",
    "ELERECOSFUP": "EleVetoWeightRecoUp",
    "ELERECOSFDOWN": "EleVetoWeightRecoDown",
    
    # "ELEIDSFNOM": "1.",
    "ELEIDSFUP": "EleVetoWeightIDUp",
    "ELEIDSFDOWN": "EleVetoWeightIDDown",
    
    # "MUISOSFNOM": "1.",
    "MUVETOSFNOM" : "MuonVetoWeight",

    "MUISOSFUP": "MuonVetoWeightIsoUp",
    "MUISOSFDOWN": "MuonVetoWeightIsoDown",
    
    # "MUIDSFNOM": "1.",
    "MUIDSFUP": "MuonVetoWeightIDUp",
    "MUIDSFDOWN": "MuonVetoWeightIDDown",
    
    "PHSFNOM": "PhotonVetoWeight",
    "PHSFUP": "PhotonVetoWeightIDUp",
    "PHSFDOWN": "PhotonVetoWeightIDDown",
    
    # higher-order v+jets theory reweighting weight
    "BOSONWEIGHTNOM": bosonWeightNom,
    
    "VVJSAMPLERENORMUP" : vvj_sample_renorm_factor,
    "VVJSAMPLERENORMDOWN" : "0.99",
    "EVJSAMPLERENORMUP" : evj_sample_renorm_factor,
    "EVJSAMPLERENORMDOWN" : "0.99",
    "EEJSAMPLERENORMUP" : eej_sample_renorm_factor,
    "EEJSAMPLERENORMDOWN" : "0.99",
    
    # trigger scale factors
    "TRIGGERSFNOM" : triggerSFs,
    # "ELTRIGGERSFUP" : electronTriggerSFs_up,
    # "ELTRIGGERSFDOWN" : electronTriggerSFs_down,
    
    # "MUTRIGGERSFUP" : muonTriggerSFs_up,
    # "MUTRIGGERSFDOWN" : muonTriggerSFs_down,
    
    "METTRIGGERSFUP" : metTriggerSFs_up,
    "METTRIGGERSFDOWN" : metTriggerSFs_down,
    
    # "PHOTONTRIGGERSFUP" : photonTriggerSFs_up,
    # "PHOTONTRIGGERSFDOWN" : photonTriggerSFs_down,
    
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
   
    ## do weights for data
    "DOWEIGHTS": "(DoWeights==1)+(DoWeights==0)*1.0",
}

# Lumi weight
lumi = "59.7"

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
    + "MuonVetoWeight"
    # + muonIsoSFs
    # + "*"
    # + muonIDSFs
    + "*"
    + "EleVetoWeight"
    # + electronRecoSFs
    # + "*"
    # + electronIDSFs
    + "*"
    # + photonSFs
    + "PhotonVetoWeight"
    + "*"
    + bosonWeightNom
    + "*"
    + triggerSFs
    #+ "*"
    #+ deepakMistagSF
    #+ "*"
    #+ deepakEfficiencySF
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
        path_mwassmer + "/EGamma*/*nominal*.root",
        "((N_LooseElectrons>0) || (N_LoosePhotons>0)) && (N_LooseMuons==0)",
        "SingleEl",
        samDict=sampleDict,
        readTrees=doReadTrees,
    )
]
samplesDataControlPlots += [
    plotClasses.Sample(
        "MET",
        ROOT.kBlack,
        path_mwassmer + "/MET*/*nominal*.root",
        "(N_LooseElectrons==0) && (N_LooseMuons>=0) && (N_LoosePhotons==0)",
        "MET",
        samDict=sampleDict,
        readTrees=doReadTrees,
    )
]

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
        #lumi + "*1.094*1.084",
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
        #lumi + "*1.132*1.043",
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
        #lumi + "*1.036*1.034",
        "wlnujets",
        samDict=sampleDict,
        readTrees=doReadTrees,
        typ="bkg",
    ),
    plotClasses.Sample(
        "#gamma+jets",
        ROOT.kOrange - 4,
        path_mwassmer + "/GJets_HT*/*nominal*.root",
        lumi,
        # first factor removes yield change due to reweighting, second factor is k factor for total cross section multiplied by fraction of isolated photons in analysis phase-space
        #lumi + "*0.710*1.105/0.830
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


plottingsamples = []

# sort subset of processes in plots. descending order
sortedProcesses = []
