# this class describes the interface to the DNN interface to be used in the scriptgenerator
# This class can be used to load a Tensorflow model obtained by making use of the NNFlow framework

# There are several methods which you will need to update for your own classifier 
# Then use the interface by passing THIS file path to the plotparallel function


class theInterface:
  
  def __init__(self):
    # path to include in the search for header files. This is probably the src CMSSW directory where you installed the CommonClassifier
    self.includeString="-I/nfs/dust/cms/user/mharrend/gitlab-ci/CMSSW_8_0_26_patch2/src"
    # precompiled library path and libraries to be included
    self.libraryString="-L/nfs/dust/cms/user/mharrend/gitlab-ci/CMSSW_8_0_26_patch2/lib/slc6_amd64_gcc530 -lDNNBase -lDNNTensorflow"
    # if the following is true, the g++ compiler will also link the python libraries. You probably need this if you use Tensorflow
    self.usesPythonLibraries=True

  # This is a list of variables which should be visible for the plotscript.
  # You also need to define them in the getVariableInitLines method
  def getExternalyCallableVariables(self):
    return ["tf_ttlight",
	    "tf_ttcc",
	    "tf_ttb",
	    "tf_tt2b",
	    "tf_ttbb",
	    "tf_ttH"
	    ]
    
  # Write here the code with the include statements
  # DNN header is relative to CMSSW BASE
  def getIncludeLines(self):
    retstr="""
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <exception> 

#include "DNN/Tensorflow/interface/tfModelUser.h"
"""
    return retstr
  
  # Here you define any additional functions you will need
  def getAdditionalFunctionDefinitionLines(self):
    retstr="""

// Function opens file with variable list and returns std::vector<std::string> of variables
std::vector<std::string> readinNumberOfVariables(std::string variableListLocation)
{
    // Define string vector
    std::vector<std::string> variableList;
    
    // Reading in variables
    std::string tempVariable;
    std::ifstream variableListFile;
    variableListFile.exceptions ( std::ifstream::failbit | std::ifstream::badbit );
    try {
        variableListFile.open(variableListLocation);
        while (!variableListFile.eof()) {
            getline(variableListFile,tempVariable);
            // Only save variable if it is not an empty line or whitespace line
            if (!tempVariable.empty() and tempVariable.find_first_not_of(" \t\n\v\f\r") != std::string::npos)
                variableList.push_back(tempVariable);
        }
        variableListFile.close();
    }
    catch (std::ifstream::failure e) {
        std::cerr << "Exception opening/reading/closing file: " << variableListLocation << std::endl << "Error message was: " << std::endl <<  e.what() << std::endl;
    }
    variableListFile.close();
    
    for(const auto &i: variableList)
	std::cout << "VariableList: " << i << std::endl;
    std::cout << "Variable list contains " << variableList.size() << " entries." << std::endl;

    return variableList;
}

"""
    return retstr
  
  # here you write the code which shgould be inserted before the main event loop
  def getBeforeLoopLines(self):
    rstr="""
    
    std::string dataDir = "/nfs/dust/cms/user/mharrend/doktorarbeit/tensorflowModels/multiclass_ttlight_ttcc_ttb_tt2b_ttbb_ttH";
    std::string modelLoc = dataDir + "/model/multiclass_ttlight_ttcc_ttb_tt2b_ttbb_ttH.ckpt";
    std::cout << "Will use the tfModelUser model: " << modelLoc << std::endl;

    // Read in input variable list
    std::string inputvariableListLoc = dataDir + "/inputVariables.txt";
    std::cout << "Will use the tfModelUser input variable list: " << inputvariableListLoc << std::endl;
    std::vector<std::string> inputvariableList = readinNumberOfVariables(inputvariableListLoc);
    
    // Read in output label list
    std::string outputLabelListLoc = dataDir + "/outputLabels.txt";
    std::cout << "Will use the tfModelUser output label list: " << outputLabelListLoc << std::endl;
    std::vector<std::string> outputLabelList = readinNumberOfVariables(outputLabelListLoc);
    
    // load and initialize the model
    dnn::tf::tfModelUser modelUser(modelLoc, inputvariableList, outputLabelList);

    

"""
    return rstr

  # initialize variables INSIDE event loop
  def getVariableInitInsideEventLoopLines(self):
    rstr="""
    // output node variables
 double tf_ttlight=-2.0;
 double tf_ttcc=-2.0;
 double tf_ttb=-2.0;
 double tf_tt2b=-2.0;
 double tf_ttbb=-2.0;
 double tf_ttH=-2.0;
 """
    return rstr
  
  # Code that call the Classifier and fills the needed variables
  # This is also inside of the event loop
  def getEventLoopCodeLines(self):
    rstr="""

  // String vector contains names of all input variables pushed into input values vector
  std::vector<std::string> inputNames = {  
    "BDT_common5_input_Mlb",
    "BDT_common5_input_all_sum_pt_with_met",
    "BDT_common5_input_aplanarity",
    "BDT_common5_input_avg_dr_tagged_jets",
    "BDT_common5_input_best_higgs_mass",
    "BDT_common5_input_closest_tagged_dijet_mass",
    "BDT_common5_input_cos_theta_blep_bhad",
    "BDT_common5_input_cos_theta_l_bhad",
    "BDT_common5_input_dEta_fn",
    "BDT_common5_input_delta_eta_blep_bhad",
    "BDT_common5_input_delta_eta_l_bhad",
    "BDT_common5_input_delta_phi_blep_bhad",
    "BDT_common5_input_delta_phi_l_bhad",
    "BDT_common5_input_dr_between_lep_and_closest_jet",
    "BDT_common5_input_h0",
    "BDT_common5_input_h1",
    "BDT_common5_input_h2",
    "BDT_common5_input_h3",
    "BDT_common5_input_invariant_mass_of_everything",
    "BDT_common5_input_lowest_btag",
    "BDT_common5_input_pt_all_jets_over_E_all_jets",
    "BDT_common5_input_sphericity",
    "BDT_common5_input_tagged_dijet_mass_closest_to_125",
    "Evt_CSV_Average",
    "Evt_CSV_Average_Tagged",
    "Evt_CSV_Dev",
    "Evt_CSV_Dev_Tagged",
    "Evt_CSV_Min",
    "Evt_CSV_Min_Tagged",
    "Evt_Deta_JetsAverage",
    "Evt_Deta_TaggedJetsAverage",
    "Evt_Deta_UntaggedJetsAverage",
    "Evt_Dr_JetsAverage",
    "Evt_Dr_MinDeltaRJets",
    "Evt_Dr_MinDeltaRLeptonJet",
    "Evt_Dr_MinDeltaRLeptonTaggedJet",
    "Evt_Dr_MinDeltaRTaggedJets",
    "Evt_Dr_MinDeltaRUntaggedJets",
    "Evt_Dr_UntaggedJetsAverage",
    "Evt_E_PrimaryLepton",
    "Evt_Eta_JetsAverage",
    "Evt_Eta_PrimaryLepton",
    "Evt_Eta_TaggedJetsAverage",
    "Evt_Eta_UntaggedJetsAverage",
    "Evt_HT",
    "Evt_HT_Jets",
    "Evt_JetPtOverJetE",
    "Evt_Jet_MaxDeta_Jets",
    "Evt_M2_JetsAverage",
    "Evt_M2_TaggedJetsAverage",
    "Evt_M2_UntaggedJetsAverage",
    "Evt_M3",
    "Evt_MHT",
    "Evt_M_JetsAverage",
    "Evt_M_MedianTaggedJets",
    "Evt_M_MinDeltaRJets",
    "Evt_M_MinDeltaRLeptonJet",
    "Evt_M_MinDeltaRLeptonTaggedJet",
    "Evt_M_MinDeltaRTaggedJets",
    "Evt_M_MinDeltaRUntaggedJets",
    "Evt_M_PrimaryLepton",
    "Evt_M_TaggedJetsAverage",
    "Evt_M_TaggedJetsClosestTo125",
    "Evt_M_Total",
    "Evt_M_UntaggedJetsAverage",
    "Evt_Phi_MET",
    "Evt_Phi_PrimaryLepton",
    "Evt_Pt_MET",
    "Evt_Pt_MinDeltaRJets",
    "Evt_Pt_MinDeltaRTaggedJets",
    "Evt_Pt_MinDeltaRUntaggedJets",
    "Evt_Pt_PrimaryLepton",
    "Evt_TaggedJet_MaxDeta_Jets",
    "Evt_TaggedJet_MaxDeta_TaggedJets",
    "Evt_blr_ETH",
    "Evt_blr_ETH_transformed",
    "HadTop_B_LepTop_B_DR",
    "HadTop_B_LepTop_DR",
    "HadTop_B_LepTop_W1_DR",
    "HadTop_B_LepTop_W2_DR",
    "HadTop_B_LepTop_W_DR",
    "HadTop_LepTop_B_DR",
    "HadTop_LepTop_DR",
    "HadTop_LepTop_W1_DR",
    "HadTop_LepTop_W2_DR",
    "HadTop_LepTop_W_DR",
    "HadTop_W1_LepTop_B_DR",
    "HadTop_W1_LepTop_DR",
    "HadTop_W1_LepTop_W1_DR",
    "HadTop_W1_LepTop_W2_DR",
    "HadTop_W1_LepTop_W_DR",
    "HadTop_W2_LepTop_B_DR",
    "HadTop_W2_LepTop_DR",
    "HadTop_W2_LepTop_W1_DR",
    "HadTop_W2_LepTop_W2_DR",
    "HadTop_W2_LepTop_W_DR",
    "HadTop_W_LepTop_B_DR",
    "HadTop_W_LepTop_DR",
    "HadTop_W_LepTop_W1_DR",
    "HadTop_W_LepTop_W2_DR",
    "HadTop_W_LepTop_W_DR",
    "Reco_Deta_Fn_best_TTBBLikelihood",
    "Reco_Deta_Fn_best_TTBBLikelihoodTimesME",
    "Reco_Deta_TopHad_BB_best_TTBBLikelihood",
    "Reco_Deta_TopHad_BB_best_TTBBLikelihoodTimesME",
    "Reco_Deta_TopLep_BB_best_TTBBLikelihood",
    "Reco_Deta_TopLep_BB_best_TTBBLikelihoodTimesME",
    "Reco_Dr_BB_best_TTLikelihood",
    "Reco_Dr_BB_best_TTLikelihood_comb",
    "Reco_Higgs_M_best_TTLikelihood",
    "Reco_Higgs_M_best_TTLikelihood_comb",
    "Reco_LikelihoodRatio_best_Likelihood",
    "Reco_LikelihoodRatio_best_LikelihoodTimesME",
    "Reco_LikelihoodRatio_best_TTLikelihood",
    "Reco_LikelihoodRatio_best_TTLikelihood_comb",
    "Reco_LikelihoodTimesMERatio_best_Likelihood",
    "Reco_LikelihoodTimesMERatio_best_LikelihoodTimesME",
    "Reco_LikelihoodTimesMERatio_best_TTLikelihood",
    "Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",
    "Reco_LikelihoodTimesMERatio_off_best_Likelihood",
    "Reco_LikelihoodTimesMERatio_off_best_LikelihoodTimesME",
    "Reco_LikelihoodTimesMERatio_off_best_TTLikelihood",
    "Reco_LikelihoodTimesMERatio_off_best_TTLikelihood_comb",
    "Reco_MERatio_best_Likelihood",
    "Reco_MERatio_best_LikelihoodTimesME",
    "Reco_MERatio_best_TTLikelihood",
    "Reco_MERatio_best_TTLikelihood_comb",
    "Reco_MERatio_off_best_Likelihood",
    "Reco_MERatio_off_best_LikelihoodTimesME",
    "Reco_MERatio_off_best_TTLikelihood",
    "Reco_MERatio_off_best_TTLikelihood_comb",
    "Reco_Sum_LikelihoodRatio",
    "Reco_Sum_LikelihoodTimesMERatio",
    "Reco_Sum_MERatio",
    "Reco_Sum_TTBBLikelihood",
    "Reco_Sum_TTBBLikelihoodTimesME",
    "Reco_Sum_TTBBME",
    "Reco_Sum_TTHBBME",
    "Reco_Sum_TTHLikelihood",
    "Reco_Sum_TTHLikelihoodTimesME",
    "Reco_TTBBLikelihoodTimesME_best_TTBBLikelihood",
    "Reco_TTBBLikelihoodTimesME_best_TTBBLikelihoodTimesME",
    "Reco_TTBBLikelihoodTimesME_best_TTLikelihood",
    "Reco_TTBBLikelihoodTimesME_best_TTLikelihood_comb",
    "Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihood",
    "Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",
    "Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood",
    "Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",
    "Reco_TTBBLikelihood_best_TTBBLikelihood",
    "Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",
    "Reco_TTBBLikelihood_best_TTLikelihood",
    "Reco_TTBBLikelihood_best_TTLikelihood_comb",
    "Reco_TTBBME_best_TTBBLikelihood",
    "Reco_TTBBME_best_TTBBLikelihoodTimesME",
    "Reco_TTBBME_best_TTLikelihood",
    "Reco_TTBBME_best_TTLikelihood_comb",
    "Reco_TTBBME_off_best_TTBBLikelihood",
    "Reco_TTBBME_off_best_TTBBLikelihoodTimesME",
    "Reco_TTBBME_off_best_TTLikelihood",
    "Reco_TTBBME_off_best_TTLikelihood_comb",
    "Reco_TTHBBME_best_TTHLikelihood",
    "Reco_TTHBBME_best_TTHLikelihoodTimesME",
    "Reco_TTHBBME_best_TTLikelihood",
    "Reco_TTHBBME_best_TTLikelihood_comb",
    "Reco_TTHLikelihoodTimesME_best_TTHLikelihood",
    "Reco_TTHLikelihoodTimesME_best_TTHLikelihoodTimesME",
    "Reco_TTHLikelihoodTimesME_best_TTLikelihood",
    "Reco_TTHLikelihoodTimesME_best_TTLikelihood_comb",
    "Reco_TTHLikelihood_best_TTHLikelihood",
    "Reco_TTHLikelihood_best_TTHLikelihoodTimesME",
    "Reco_TTHLikelihood_best_TTLikelihood",
    "Reco_TTHLikelihood_best_TTLikelihood_comb",
    "N_BTagsL",
    "N_BTagsM",
    "N_BTagsT",
    "N_Jets",
    "N_LooseElectrons",
    "N_LooseJets",
    "N_LooseMuons",
    "N_PrimaryVertices",
    "N_TightElectrons",
    "N_TightMuons",
    "N_additionalTaggedJets",
    "N_additionalUntaggedJets",
    "LooseLepton_E_1",
    "LooseLepton_Eta_1",
    "LooseLepton_M_1",
    "LooseLepton_Phi_1",
    "LooseLepton_Pt_1",
    "CSV_1",
    "CSV_2",
    "CSV_3",
    "CSV_4",
    "CSV_5",
    "CSV_6",
    "Jet_CSV_1",
    "Jet_CSV_2",
    "Jet_CSV_3",
    "Jet_CSV_4",
    "Jet_CSV_5",
    "Jet_CSV_6",
    "Jet_Charge_1",
    "Jet_Charge_2",
    "Jet_Charge_3",
    "Jet_Charge_4",
    "Jet_Charge_5",
    "Jet_Charge_6",
    "Jet_E_1",
    "Jet_E_2",
    "Jet_E_3",
    "Jet_E_4",
    "Jet_E_5",
    "Jet_E_6",
    "Jet_Eta_1",
    "Jet_Eta_2",
    "Jet_Eta_3",
    "Jet_Eta_4",
    "Jet_Eta_5",
    "Jet_Eta_6",
    "Jet_M_1",
    "Jet_M_2",
    "Jet_M_3",
    "Jet_M_4",
    "Jet_M_5",
    "Jet_M_6",
    "Jet_Phi_1",
    "Jet_Phi_2",
    "Jet_Phi_3",
    "Jet_Phi_4",
    "Jet_Phi_5",
    "Jet_Phi_6",
    "Jet_Pt_1",
    "Jet_Pt_2",
    "Jet_Pt_3",
    "Jet_Pt_4",
    "Jet_Pt_5",
    "Jet_Pt_6",
    "Jet_PileUpMVA_1",
    "Jet_PileUpMVA_2",
    "Jet_PileUpMVA_3",
    "Jet_PileUpMVA_4",
    "Jet_PileUpMVA_5",
    "Jet_PileUpMVA_6"
  };

  // Construct float vector containing input values of a single event
  std::vector<float> inputValues;
  for(auto variableName: inputNames) {
    if(floatMap.find(variableName) != floatMap.end()) {
      inputValues.push_back(floatMap[variableName]);
    }
    else if(intMap.find(variableName) != intMap.end()) {
      inputValues.push_back(intMap[variableName]);
    }
    else {
      std::cerr << "NNFlowInterface: Inputvariable was not found in maps." << std::endl;
    }
  }  
  
  // Evaluate the output for an event
  std::vector<float> outputValuesReturnVec;
  outputValuesReturnVec = modelUser.evalModel(inputValues);
  tf_ttlight=outputValuesReturnVec[0];
  tf_ttcc=outputValuesReturnVec[1];
  tf_ttb=outputValuesReturnVec[2];
  tf_tt2b=outputValuesReturnVec[3];
  tf_ttbb=outputValuesReturnVec[4];
  tf_ttH=outputValuesReturnVec[5];
  
  bool printstuff=1;
  if(printstuff){
    std::cout << "-----NNFlowInterface-----" << std::endl;
    std::cout <<"tf ttlight node " << tf_ttlight << std::endl;
    std::cout <<"tf ttcc node " << tf_ttcc << std::endl;
    std::cout <<"tf ttb node " << tf_ttb << std::endl;
    std::cout <<"tf tt2b node " << tf_tt2b << std::endl;
    std::cout <<"tf ttbb node " << tf_ttbb << std::endl;
    std::cout <<"tf ttH node " << tf_ttH << std::endl;
    }
  
"""

    return rstr

  # Here is code calling a test function to see wether the calling works as it should
  def getTestCallLines(self):
    rstr="""
    std::vector<float> eventVec = {
  75.3191833496, 449.89855957, 0.0750138610601, 3.22019815445,
  0.0, 217.826843262, -0.700150609016, -0.794458508492,
  0.0, 3.18069839478, 2.90678453445, 0.502826452255,
  1.75928318501, 0.99976426363, 0.398145616055, -0.0298533830792,
  0.16509616375, 0.0580038204789, 866.979003906, 0.878696382046,
  0.401795059443, 0.406872868538, 217.826843262, 0.489256113768,
  0.895407497883, 0.113197058439, 0.000279261381365, 0.0824939981103,
  0.878696382046, 1.96167123318, 3.18069839478, 2.04820561409,
  2.80315327644, 0.976631700993, 0.99976426363, 2.27863311768,
  3.22019815445, 1.35024535656, 3.0377805233, 75.1506958008,
  0.234085097909, -1.10028648376, 0.216148853302, 0.243053168058,
  449.898529053, 269.498138428, 0.40179502964, 3.28364706039,
  143.182815552, 217.826843262, 143.743743896, 307.974884033,
  95.3141174316, 3.02768826485, 217.826843262, 36.9866218567,
  43.5902404785, 75.3191833496, 217.826843262, 64.619102478,
  -0.0148671893403, 8.54773235321, 217.826843262, 866.979003906,
  7.07996463776, -0.0760409533978, 0.80216896534, 135.370361328,
  64.2974319458, 91.3021011353, 85.4920501709, 45.0300445557,
  2.66747665405, 4.55489873886, 0.419706910849, -0.323976635933,
  0.0, 2.99721050262, 3.21775770187, 2.97493648529,
  2.97493648529, 0.69654083252, 2.94123387337, 3.3925049305,
  2.86213493347, 2.86213493347, 0.976631700993, 2.66130447388,
  3.2393848896, 2.59573721886, 2.59573721886, 0.976631700993,
  2.66130447388, 3.2393848896, 2.59573721886, 2.59573721886,
  0.976631700993, 2.66130447388, 3.2393848896, 2.59573721886,
  2.59573721886, 1.04637384415, 1.68253695965, 3.85681200027,
  0.730289399624, 0.283886820078, 3.87645053864, 3.57489085197,
  2.94803261757, 162.348922729, 204.765716553, 0.506848037243,
  0.517021179199, 0.176898449659, 0.0618144534528, 0.542471766472,
  0.437094211578, 0.221899345517, 0.0443901047111, 0.0520681291819,
  0.212498500943, 0.336108744144, 0.110937654972, 0.535665273666,
  0.42041388154, 0.570250093937, 0.413498193026, 0.0507325269282,
  0.201323732734, 0.701995849609, 0.654439508915, 0.306296408176,
  0.292550832033, 0.460287541151, 9.75731018116e-05, 1.01019764998e-07,
  0.228382438421, 0.194773316383, 4.30822183262e-05, 4.17746157666e-08,
  4.12119316451e-09, 6.29278495978e-09, 7.43852313079e-10, 3.84066167758e-10,
  8.89584867991e-08, 1.81083024131e-08, 4.19009715813e-10, 1.42976547268e-10,
  3.15395573125e-06, 3.02811440633e-06, 1.18623836443e-06, 6.69018390909e-07,
  0.00130667432677, 0.00207811989821, 0.00062706816243, 0.000574074161705,
  0.0282053686678, 0.00598005903885, 0.00035322556505, 0.000213710940443,
  0.00150740402751, 0.00150740402751, 0.000832078629173, 0.000404736376368,
  4.88632379003e-09, 4.88632379003e-09, 2.12132381106e-10, 1.78406872609e-11,
  3.24154871123e-06, 3.24154871123e-06, 2.54942705169e-07, 4.40797727208e-08,
  3.0, 2.0, 0.0, 6.0,
  1.0, 7.0, 0.0, 18.0,
  1.0, 0.0, 1.0, 3.0,
  75.1506958008, -1.10028648376, -0.0148671893403, 0.80216896534,
  45.0300445557, 0.91211861372, 0.878696382046, 0.637541413307,
  0.275193244219, 0.149492889643, 0.0824939981103, 0.0824939981103,
  0.91211861372, 0.149492889643, 0.878696382046, 0.637541413307,
  0.275193244219, -0.147270709276, 0.490214288235, 0.44051322341,
  0.148862197995, -0.862654268742, 0.269968181849, 164.798751831,
  179.662216187, 37.6692733765, 77.646736145, 89.7762527466,
  121.182106018, 1.49528670311, 1.80649805069, -0.105236373842,
  -1.37420034409, 1.57253301144, -1.99037063122, 9.01439476013,
  8.91282653809, 5.50948381424, 8.18263816833, 6.94388914108,
  6.85209083557, -2.54293274879, 2.56145215034, 0.705195367336,
  3.0642786026, -1.19489884377, -2.46118402481, 70.2493286133,
  57.3906860352, 37.0587921143, 36.725402832, 35.6151771545,
  32.4587554932, 0.995814323425, 0.977832615376, 0.968445897102,
  0.804459810257, -0.163851693273, 0.965455949306
  };

    std::vector<float> outputValuesVec = { 0.26361305, 0.25014877, 0.24499501, 0.11612786, 0.10633284, 0.01878254 };
    
    // evaluate event for given model
    std::vector<float> outputValuesReturnVec = modelUser.evalModel(eventVec);

    // compare vectors for unit test
    std::cout << "Doing NNFlowInterface unit test" << std::endl;
    std::cout << "No error printout means unit test succeeded." << std::endl;
    for (int i = 0; i < outputValuesReturnVec.size(); i++)
    {
        std::cout << "Output Value: " << outputValuesReturnVec[i] << std::endl;
        assert(fabs(outputValuesReturnVec[i] - outputValuesVec[i]) < 0.00001 && "The unit test for the NNFlowInterface did not succeed.");
    }
"""
    return rstr
  
  # call need desctructors here and other cleanup things
  # Will be run after event loop
  def getCleanUpLines(self):
    rstr="""
   """
    return rstr
  
  
  