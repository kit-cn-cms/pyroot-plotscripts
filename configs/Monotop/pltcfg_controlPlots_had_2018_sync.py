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
    #dataset_name = dataset_name.replace("-","_")
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
path_mwassmer = "/nfs/dust/cms/user/mwassmer/MonoTop/ntuples_2018_PuppiMET"

# ======= #
# WEIGHTS #
# ======= #

# generator weight
defaultWeight = "Weight_GEN_nom"


# csv weight
csvWeightNom = "1."#"internalCSVweight_loose"


# pile up weights
pileupWeightNom = "internalPUWeight_2018"
pileupWeightUp = "internalPUWeight_2018_Up"
pileupWeightDown = "internalPUWeight_2018_Down"


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


# trigger scale factors

triggerSFs = "((N_LooseElectrons>0 && N_LooseMuons==0 && N_LoosePhotons==0)*TriggerSF_SingleElectron+(N_LooseMuons>=0 && N_LooseElectrons==0 && N_LoosePhotons==0)*TriggerSF_MET+(N_LoosePhotons>0 && N_LooseElectrons==0 && N_LooseMuons==0)*TriggerSF_SinglePhoton)"


electronTriggerSFs_up = "((N_LooseElectrons>0 && N_LooseMuons==0 && N_LoosePhotons==0)*TriggerSF_SingleElectron_Up+(N_LooseMuons>=0 && N_LooseElectrons==0 && N_LoosePhotons==0)*TriggerSF_MET+(N_LoosePhotons>0 && N_LooseElectrons==0 && N_LooseMuons==0)*TriggerSF_SinglePhoton)"

electronTriggerSFs_down = "((N_LooseElectrons>0 && N_LooseMuons==0 && N_LoosePhotons==0)*TriggerSF_SingleElectron_Down+(N_LooseMuons>=0 && N_LooseElectrons==0 && N_LoosePhotons==0)*TriggerSF_MET+(N_LoosePhotons>0 && N_LooseElectrons==0 && N_LooseMuons==0)*TriggerSF_SinglePhoton)"


metTriggerSFs_up = "((N_LooseElectrons>0 && N_LooseMuons==0 && N_LoosePhotons==0)*TriggerSF_SingleElectron+(N_LooseMuons>=0 && N_LooseElectrons==0 && N_LoosePhotons==0)*TriggerSF_MET_Up+(N_LoosePhotons>0 && N_LooseElectrons==0 && N_LooseMuons==0)*TriggerSF_SinglePhoton)"

metTriggerSFs_down = "((N_LooseElectrons>0 && N_LooseMuons==0 && N_LoosePhotons==0)*TriggerSF_SingleElectron+(N_LooseMuons>=0 && N_LooseElectrons==0 && N_LoosePhotons==0)*TriggerSF_MET_Down+(N_LoosePhotons>0 && N_LooseElectrons==0 && N_LooseMuons==0)*TriggerSF_SinglePhoton)"


photonTriggerSFs_up = "((N_LooseElectrons>0 && N_LooseMuons==0 && N_LoosePhotons==0)*TriggerSF_SingleElectron+(N_LooseMuons>=0 && N_LooseElectrons==0 && N_LoosePhotons==0)*TriggerSF_MET+(N_LoosePhotons>0 && N_LooseElectrons==0 && N_LooseMuons==0)*TriggerSF_SinglePhoton_Up)"

photonTriggerSFs_down = "((N_LooseElectrons>0 && N_LooseMuons==0 && N_LoosePhotons==0)*TriggerSF_SingleElectron+(N_LooseMuons>=0 && N_LooseElectrons==0 && N_LoosePhotons==0)*TriggerSF_MET+(N_LoosePhotons>0 && N_LooseElectrons==0 && N_LooseMuons==0)*TriggerSF_SinglePhoton_Down)"


#muonTriggerSFs_up = "((N_TightElectrons>0 && N_LooseMuons==0 && N_LoosePhotons==0)*TriggerSF_SingleElectron+(N_TightMuons>=0 && N_LooseElectrons==0 && N_LoosePhotons==0)*TriggerSF_MET+(N_LoosePhotons>0 && N_LooseElectrons==0 && N_LooseMuons==0)*TriggerSF_SinglePhoton)"

#muonTriggerSFs_down = "((N_TightElectrons>0 && N_LooseMuons==0 && N_LoosePhotons==0)*TriggerSF_SingleElectron+(N_TightMuons>=0 && N_LooseElectrons==0 && N_LoosePhotons==0)*TriggerSF_MET+(N_LoosePhotons>0 && N_LooseElectrons==0 && N_LooseMuons==0)*TriggerSF_SinglePhoton)"


# top pt weight
topptWeightNom = "Weight_TopPt"


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
    
    # higher-order v+jets theory reweighting weight
    "BOSONWEIGHTNOM": bosonWeightNom,
    
    # trigger scale factors
    "TRIGGERSFNOM" : triggerSFs,
    "ELTRIGGERSFUP" : electronTriggerSFs_up,
    "ELTRIGGERSFDOWN" : electronTriggerSFs_down,
    
    #"MUTRIGGERSFUP" : muonTriggerSFs_up,
    #"MUTRIGGERSFDOWN" : muonTriggerSFs_down,
    
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
    + muonIsoSFs
    + "*"
    + muonIDSFs
    + "*"
    + electronRecoSFs
    + "*"
    + electronIDSFs
    + "*"
    + photonSFs
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
        #"#splitline{VectorMonotop}{M_{#phi}=2000 M_{#chi}=500}",
        #ROOT.kCyan,
        #path_mwassmer + "/VectorMonotop_Mphi_2000_Mchi_500/*nominal*.root",
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
        #lumi,
        lumi + "*1.094*1.084",
        "znunujets",
        samDict=sampleDict,
        readTrees=doReadTrees,
        typ="bkg",
    ),
    plotClasses.Sample(
        "Z(ll)+jets",
        ROOT.kOrange + 1,
        path_mwassmer + "/DYJetsToLL_M-50_HT*/*nominal*.root",
        #lumi,
        lumi + "*1.132*1.043",
        "zlljets",
        samDict=sampleDict,
        readTrees=doReadTrees,
        typ="bkg",
    ),
    plotClasses.Sample(
        "W(l#nu)+jets",
        ROOT.kOrange,
        path_mwassmer + "/WJetsToLNu_HT*/*nominal*.root",
        #lumi,
        lumi + "*1.014*1.034",
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
    if "VectorMonotop" in sample_folder:
        sample_name = sample_folder
        mphi,mchi = find_masses(sample_name)
        sample_label = "#splitline{Vector Monotop}{M_{#phi}="+mphi+" GeV, "+"M_{#chi}="+mchi+" GeV}"
        print sample_label
        samples += [plotClasses.Sample(sample_label,ROOT.kCyan,path_mwassmer+"/"+sample_folder+"/*nominal*.root",lumi,sample_name.lower(),samDict=sampleDict,readTrees=doReadTrees,typ="signal")]

processes = []
for sample in samples:
    processes.append(sample.nick)
list_of_processes = processes
datacard_processes = processes


plottingsamples = []

# sort subset of processes in plots. descending order
sortedProcesses = []
