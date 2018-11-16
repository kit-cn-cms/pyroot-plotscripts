
class theInterface:
  
  def __init__(self):

    self.includeString="-I/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/tensorflow-cc/1.3.0-elfike/tensorflow_cc/include -I/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/eigen/c7dc0a897676/include/eigen3 -I/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/protobuf/3.4.0-fmblme/include"
    #self.libraryString="-L/nfs/dust/cms/user/kelmorab/CMSSW_Moriond2017/cardsCMSSWTF/CMSSW_8_0_26_patch2/lib/slc6_amd64_gcc530 -lDNNBase -lDNNTensorflow -lTTHCommonClassifier"
    self.libraryString="-L/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/tensorflow-cc/1.3.0-elfike/tensorflow_cc/lib -ltensorflow_cc -L/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/protobuf/3.4.0-fmblme/lib -lprotobuf -lrt"
    self.usesPythonLibraries=True

  def getExternalyCallableVariables(self):
    return [
	    "DNN_Out_4j3t_ttbar2B",
	    "DNN_Out_4j3t_ttbarB",
	    "DNN_Out_4j3t_ttbarBB",
	    "DNN_Out_4j3t_ttbarCC",
	    "DNN_Out_4j3t_ttbarlf",
	    "DNN_Out_4j3t_ttH",
	    "DNN_4j3t_pred_class",
      "DNN_Out_5j3t_ttbar2B",
      "DNN_Out_5j3t_ttbarB",
      "DNN_Out_5j3t_ttbarBB",
      "DNN_Out_5j3t_ttbarCC",
      "DNN_Out_5j3t_ttbarlf",
      "DNN_Out_5j3t_ttH",
      "DNN_5j3t_pred_class",
      "DNN_Out_6j3t_ttbar2B",
      "DNN_Out_6j3t_ttbarB",
      "DNN_Out_6j3t_ttbarBB",
      "DNN_Out_6j3t_ttbarCC",
      "DNN_Out_6j3t_ttbarlf",
      "DNN_Out_6j3t_ttH",
      "DNN_6j3t_pred_class",]
    
  def getIncludeLines(self):
    retstr="""
#include <tensorflow/core/protobuf/meta_graph.pb.h>
#include "tensorflow/core/public/session.h"
#include "tensorflow/cc/framework/ops.h"
#include "tensorflow/core/framework/tensor.h"

// Should be removed for future work
using namespace tensorflow;
"""
    return retstr
  
  def getAdditionalFunctionDefinitionLines(self):
    retstr="""



int getMaxPosition(std::vector<tensorflow::Tensor> &output, int nClasses)
{
  double max_value = -5;
  int max_pos = -1;
  for(int idim =0; idim<nClasses; idim++)
  {
    if (output.at(0).tensor<float,2>()(0,idim)> max_value)
    {
      max_value = output.at(0).tensor<float,2>()(0,idim);
      max_pos = idim;
    }
  }
  return idim;
}


"""
    return retstr
  
  
  def getBeforeLoopLines(self):
    rstr="""

    //6j3t cat
    const string pathToGraph_6j3t = "/nfs/dust/cms/user/jschindl/DNN_checkpoints/V1/6j3t/trained_main_net.meta";
    const string checkpointPath_6j3t = "/nfs/dust/cms/user/jschindl/DNN_checkpoints/V1/6j3t/trained_main_net";

    auto session_6j3t = NewSession(SessionOptions());
    if (session_6j3t == nullptr) {
        throw runtime_error("Could not create Tensorflow session.");
    }

    Status status_6j3t;

    // Read in the protobuf graph we exported
    MetaGraphDef graph_def_6j3t;
    status_6j3t = ReadBinaryProto(Env::Default(), pathToGraph_6j3t, &graph_def_6j3t);
    if (!status_6j3t.ok()) {
        throw runtime_error("Error reading graph definition from " + pathToGraph_6j3t + ": " + status_6j3t.ToString());
    }

    // Add the graph to the session
    status_6j3t = session_6j3t->Create(graph_def_6j3t.graph_def());
    if (!status_6j3t.ok()) {
        throw runtime_error("Error creating graph: " + status_6j3t.ToString());
    }


    // Read weights from the saved checkpoint
    Tensor checkpointPathTensor_6j3t(DT_STRING, TensorShape());
    checkpointPathTensor_6j3t.scalar<std::string>()() = checkpointPath_6j3t;
    status_6j3t = session_6j3t->Run(
            {{ graph_def_6j3t.saver_def().filename_tensor_name(), checkpointPathTensor_6j3t },},
            {},
      {graph_def_6j3t.saver_def().restore_op_name()},
            nullptr);
    if (!status_6j3t.ok()) {
        throw runtime_error("Error loading checkpoint from " + checkpointPath_6j3t + ": " + status_6j3t.ToString());
    } 




    //5j3t cat
    const string pathToGraph_5j3t = "/nfs/dust/cms/user/jschindl/DNN_checkpoints/V1/5j3t/trained_main_net.meta";
    const string checkpointPath_5j3t = "/nfs/dust/cms/user/jschindl/DNN_checkpoints/V1/5j3t/trained_main_net";

    auto session_5j3t = NewSession(SessionOptions());
    if (session_5j3t == nullptr) {
        throw runtime_error("Could not create Tensorflow session.");
    }

    Status status_5j3t;

    // Read in the protobuf graph we exported
    MetaGraphDef graph_def_5j3t;
    status_5j3t = ReadBinaryProto(Env::Default(), pathToGraph_5j3t, &graph_def_5j3t);
    if (!status_5j3t.ok()) {
        throw runtime_error("Error reading graph definition from " + pathToGraph_5j3t + ": " + status_5j3t.ToString());
    }

    // Add the graph to the session
    status_5j3t = session_5j3t->Create(graph_def_5j3t.graph_def());
    if (!status_5j3t.ok()) {
        throw runtime_error("Error creating graph: " + status_5j3t.ToString());
    }


    // Read weights from the saved checkpoint
    Tensor checkpointPathTensor_5j3t(DT_STRING, TensorShape());
    checkpointPathTensor_5j3t.scalar<std::string>()() = checkpointPath_5j3t;
    status_5j3t = session_5j3t->Run(
            {{ graph_def_5j3t.saver_def().filename_tensor_name(), checkpointPathTensor_5j3t },},
            {},
      {graph_def_5j3t.saver_def().restore_op_name()},
            nullptr);
    if (!status_5j3t.ok()) {
        throw runtime_error("Error loading checkpoint from " + checkpointPath_5j3t + ": " + status_5j3t.ToString());
    } 


    //4j3t cat
    const string pathToGraph_4j3t = "/nfs/dust/cms/user/jschindl/DNN_checkpoints/V1/4j3t/trained_main_net.meta";
    const string checkpointPath_4j3t = "/nfs/dust/cms/user/jschindl/DNN_checkpoints/V1/4j3t/trained_main_net";

    auto session_4j3t = NewSession(SessionOptions());
    if (session_4j3t == nullptr) {
        throw runtime_error("Could not create Tensorflow session.");
    }

    Status status_4j3t;

    // Read in the protobuf graph we exported
    MetaGraphDef graph_def_4j3t;
    status_4j3t = ReadBinaryProto(Env::Default(), pathToGraph_4j3t, &graph_def_4j3t);
    if (!status_4j3t.ok()) {
        throw runtime_error("Error reading graph definition from " + pathToGraph_4j3t + ": " + status_4j3t.ToString());
    }

    // Add the graph to the session
    status_4j3t = session_4j3t->Create(graph_def_4j3t.graph_def());
    if (!status_4j3t.ok()) {
        throw runtime_error("Error creating graph: " + status_4j3t.ToString());
    }


    // Read weights from the saved checkpoint
    Tensor checkpointPathTensor_4j3t(DT_STRING, TensorShape());
    checkpointPathTensor_4j3t.scalar<std::string>()() = checkpointPath_4j3t;
    status_4j3t = session_4j3t->Run(
            {{ graph_def_4j3t.saver_def().filename_tensor_name(), checkpointPathTensor_4j3t },},
            {},
      {graph_def_4j3t.saver_def().restore_op_name()},
            nullptr);
    if (!status_4j3t.ok()) {
        throw runtime_error("Error loading checkpoint from " + checkpointPath_4j3t + ": " + status_4j3t.ToString());
    } 




"""
    return rstr

  def getVariableInitInsideEventLoopLines(self):
    rstr="""
    // variables for DNNs
       int 4j3t_num_classes = 34;
       double DNN_Out_4j3t_ttbar2B  = -6;
       double DNN_Out_4j3t_ttbarB  = -6;
       double DNN_Out_4j3t_ttbarBB  = -6;
       double DNN_Out_4j3t_ttbarCC  = -6;
       double DNN_Out_4j3t_ttbarlf = -6;
       double DNN_Out_4j3t_ttH  = -6;
       int DNN_4j3t_pred_class  = -6;

       int 5j3t_num_classes = 42;
       double DNN_Out_5j3t_ttbar2B  = -6;
       double DNN_Out_5j3t_ttbarB  = -6;
       double DNN_Out_5j3t_ttbarBB  = -6;
       double DNN_Out_5j3t_ttbarCC  = -6;
       double DNN_Out_5j3t_ttbarlf = -6;
       double DNN_Out_5j3t_ttH  = -6;
       int DNN_5j3t_pred_class  = -6;

       int 6j3t_num_classes = 41;
       double DNN_Out_6j3t_ttbar2B  = -6;
       double DNN_Out_6j3t_ttbarB  = -6;
       double DNN_Out_6j3t_ttbarBB  = -6;
       double DNN_Out_6j3t_ttbarCC  = -6;
       double DNN_Out_6j3t_ttbarlf  = -6;
       double DNN_Out_6j3t_ttH  = -6;
       int DNN_6j3t_pred_class= -6;

       Tensor tensor_4j3t (DT_FLOAT, TensorShape({1,4j3t_num_classes}));
       Tensor tensor_5j3t (DT_FLOAT, TensorShape({1,5j3t_num_classes}));
       Tensor tensor_6j3t (DT_FLOAT, TensorShape({1,6j3t_num_classes}));

       std::vector<tensorflow::Tensor> outputTensors;
 """
    return rstr
  
  def getEventLoopCodeLines(self):
    rstr="""
  // classes are 
  // 0 = ttH 
  // 1 = ttbb 
  // 2 = tt2b 
  // 3 = ttb 
  // 4 = ttcc 
  // 5 = ttlf
  if (N_Jets == 4 and N_BTagsM >= 3){
    //Load Data
    """
    +str(self._fill_vector('4j3t'))"""

    //Run graph
    vector<pair<string,Tensor>> input2 = { {"input",tensor_4j3t}};
    status_4j3t = session_4j3t->Run(input2, {"dense_2/Softmax"},  {}, &outputTensors);
    if (!status_4j3t.ok()) 
    {
      cout << status_4j3t.ToString() << "\n";
      return 1;
    }
    else
    {
      cout << "Success load graph !! " << "\n";
    }

    //Feed output into right variables

    double DNN_Out_4j3t_ttbar2B  = outputTensors.at(0).tensor<float,2>()(0,2);
    double DNN_Out_4j3t_ttbarB  = outputTensors.at(0).tensor<float,2>()(0,3);
    double DNN_Out_4j3t_ttbarBB  = outputTensors.at(0).tensor<float,2>()(0,1);
    double DNN_Out_4j3t_ttbarCC  = outputTensors.at(0).tensor<float,2>()(0,4);
    double DNN_Out_4j3t_ttbarlf  = outputTensors.at(0).tensor<float,2>()(0,5);
    double DNN_Out_4j3t_ttH  = outputTensors.at(0).tensor<float,2>()(0,0);
    int DNN_4j3t_pred_class  = int getMaxPosition(outputTensors,4j3t_num_classes);

    bool printstuff=0;
    if(printstuff){
      cout<<"-----DNN-----"<<std::endl;
      cout<<"ttH node "<<DNN_Out_4j3t_ttH<<std::endl;
      cout<<"ttbarCC node "<<DNN_Out_4j3t_ttbarCC<<std::endl;
      cout<<"ttbarBB node "<<DNN_Out_4j3t_ttbarBB<<std::endl;
      cout<<"ttbarB node "<<DNN_Out_4j3t_ttbarB<<std::endl;
      cout<<"ttbar2B node "<<DNN_Out_4j3t_ttbar2B<<std::endl;
      cout<<"predicted class "<< DNN_Out_4j3t_class<<std::endl;
     }

  }
  else if (N_Jets == 5 and N_BTagsM >= 3){
    """
    +str(self._fill_vector('5j3t'))"""

    //Run graph
    vector<pair<string,Tensor>> input2 = { {"input",tensor_5j3t}};
    status_5j3t = session_5j3t->Run(input2, {"dense_2/Softmax"},  {}, &outputTensors);
    if (!status_5j3t.ok()) 
    {
      cout << status_5j3t.ToString() << "\n";
      return 1;
    }
    else
    {
      cout << "Success load graph !! " << "\n";
    }

    //Feed output into right variables

    double DNN_Out_5j3t_ttbar2B  = outputTensors.at(0).tensor<float,2>()(0,2);
    double DNN_Out_5j3t_ttbarB  = outputTensors.at(0).tensor<float,2>()(0,3);
    double DNN_Out_5j3t_ttbarBB  = outputTensors.at(0).tensor<float,2>()(0,1);
    double DNN_Out_5j3t_ttbarCC  = outputTensors.at(0).tensor<float,2>()(0,4);
    double DNN_Out_5j3t_ttbarlf  = outputTensors.at(0).tensor<float,2>()(0,5);
    double DNN_Out_5j3t_ttH  = outputTensors.at(0).tensor<float,2>()(0,0);
    int DNN_5j3t_pred_class  = int getMaxPosition(outputTensors,4j3t_num_classes);

    bool printstuff=0;
    if(printstuff){
      cout<<"-----DNN-----"<<std::endl;
      cout<<"ttH node "<<DNN_Out_5j3t_ttH<<std::endl;
      cout<<"ttbarCC node "<<DNN_Out_5j3t_ttbarCC<<std::endl;
      cout<<"ttbarBB node "<<DNN_Out_5j3t_ttbarBB<<std::endl;
      cout<<"ttbarB node "<<DNN_Out_5j3t_ttbarB<<std::endl;
      cout<<"ttbar2B node "<<DNN_Out_5j3t_ttbar2B<<std::endl;
      cout<<"predicted class "<< DNN_Out_5j3t_class<<std::endl;
     }

  }
  else (N_Jets == 6 and N_BTagsM >= 3){
      """
    +str(self._fill_vector('6j3t'))"""

    //Run graph
    vector<pair<string,Tensor>> input2 = { {"input",tensor_6j3t}};
    status_6j3t = session_6j3t->Run(input2, {"dense_2/Softmax"},  {}, &outputTensors);
    if (!status_6j3t.ok()) 
    {
      cout << status_6j3t.ToString() << "\n";
      return 1;
    }
    else
    {
      cout << "Success load graph !! " << "\n";
    }

    //Feed output into right variables

    double DNN_Out_6j3t_ttbar2B  = outputTensors.at(0).tensor<float,2>()(0,2);
    double DNN_Out_6j3t_ttbarB  = outputTensors.at(0).tensor<float,2>()(0,3);
    double DNN_Out_6j3t_ttbarBB  = outputTensors.at(0).tensor<float,2>()(0,1);
    double DNN_Out_6j3t_ttbarCC  = outputTensors.at(0).tensor<float,2>()(0,4);
    double DNN_Out_6j3t_ttbarlf  = outputTensors.at(0).tensor<float,2>()(0,5);
    double DNN_Out_6j3t_ttH  = outputTensors.at(0).tensor<float,2>()(0,0);
    int DNN_6j3t_pred_class  = int getMaxPosition(outputTensors,6j3t_num_classes);

    bool printstuff=0;
    if(printstuff){
      cout<<"-----DNN-----"<<std::endl;
      cout<<"ttH node "<<DNN_Out_6j3t_ttH<<std::endl;
      cout<<"ttbarCC node "<<DNN_Out_6j3t_ttbarCC<<std::endl;
      cout<<"ttbarBB node "<<DNN_Out_6j3t_ttbarBB<<std::endl;
      cout<<"ttbarB node "<<DNN_Out_6j3t_ttbarB<<std::endl;
      cout<<"ttbar2B node "<<DNN_Out_6j3t_ttbar2B<<std::endl;
      cout<<"predicted class "<< DNN_Out_6j3t_class<<std::endl;
     }
  }

  }
 

  // classes are 
  // 0 = ttH 
  // 1 = ttbb 
  // 2 = tt2b 
  // 3 = ttb 
  // 4 = ttcc 
  // 5 = ttlf

  }
  
"""

    return rstr

  def getTestCallLines(self):
    rstr="""
  //TODO: Change TestCallLines
  std::vector<TLorentzVector> testdnnjets = {
        makeVectorE(561.853400685, -1.687604070, 1.248519063, 48.315901270),
        makeVectorE(317.050318074, -0.592420697, -1.641329408, 41.454653026),
        makeVectorE(130.993330071, -0.257405132, -2.218888283, 15.829634094),
        makeVectorE(90.088794331, -0.758062780, -1.199205875, 11.687776745),
        makeVectorE(57.793076163, 0.163249642, 2.988173246, 9.959981641),
        makeVectorE(45.080527604, -1.838460445, 1.761856556, 7.07615728)
    };
    std::vector<double> testdnnjetCSVs = {
        0.592329562, 0.156740859, 0.998748481, 0.944896400, 0.268956393, 0.109731160
    };

    TLorentzVector testdnnlepton = makeVectorM(45.567291260, -1.122234225, 2.685425282, 0.105700001);
    TLorentzVector testdnnmet = makeVectorM(70.089050293, 0.0, -2.230507374, 0.0); 
    std::vector<double> testdnnAddFeatures;
    testdnnAddFeatures.push_back(1.); // blr
    testdnnAddFeatures.push_back(1.); // blr_transformed
    testdnnAddFeatures.push_back(1.); // MEM
    
    // evaluate
    DNNOutput aachentestdnnoutput = dnn.evaluate(testdnnjets, testdnnjetCSVs, testdnnlepton, testdnnmet, testdnnAddFeatures);
    std::vector<double> targetOutputsfordnntest = { 0.51680371, 0.25959021, 0.07142095, 0.07112622, 0.05624627, 0.02481263, 0.0};
    std::cout<<"doing DNN unit test"<<std::endl;
    std::cout<<"No error printout means it worked"<<std::endl;
    for (size_t i = 0; i < targetOutputsfordnntest.size(); ++i)
    {
        //assert(fabs(targetOutputsfordnntest[i] - aachentestdnnoutput.values[i]) < 0.000001 && "The DNN output for 6 jet events is incorrect");
    }
"""
    return rstr
  
  def getCleanUpLines(self):
    rstr="""

   """
    return rstr
  

  def _variable_helper_function(self,region):
    all_variables = {
    "pT_j1":                    "Jet_Pt[0]",
    "eta_j1":                   "Jet_Eta[0]",
    "CSV_j1":                   "Jet_CSV[0]",

    "pT_j2":                    "Jet_Pt[1]",
    "eta_j2":                   "Jet_Eta[1]",
    "CSV_j2":                   "Jet_CSV[1]",

    "pT_j3":                    "Jet_Pt[2]",
    "eta_j3":                   "Jet_Eta[2]",
    "CSV_j3":                   "Jet_CSV[2]",

    "pT_j4":                    "Jet_Pt[3]",
    "eta_j4":                   "Jet_Eta[3]",
    "CSV_j4":                   "Jet_CSV[3]",

    "pT_lep1":                  "LooseLepton_Pt[0]" ,
    "eta_lep1":                 "LooseLepton_Eta[0]",

    "HT":                       "Evt_HT",
    "HT_tag":                   "BDT_common5_input_HT_tag",

    "min_dR_jj":                "Evt_Dr_MinDeltaRJets",
    "min_dR_bb":                "Evt_Dr_MinDeltaRTaggedJets",

    "max_dR_jj":                "BDT_common5_input_max_dR_jj", 
    "max_dR_bb":                "BDT_common5_input_max_dR_bb",

    "aplanarity_jets":          "BDT_common5_input_aplanarity_jets",
    "aplanarity_tags":          "BDT_common5_input_aplanarity_tags",

    "centrality_jets":          "Evt_JetPtOverJetE",
    "centrality_tags":          "BDT_common5_input_pt_all_jets_over_E_all_jets_tags",

    "sphericity_jets":          "BDT_common5_input_sphericity_jets",
    "sphericity_tags":          "BDT_common5_input_sphericity_tags",

    # transverse sphericities
    "sphericityT_jets":         "BDT_common5_input_transverse_sphericity_jets",
    "sphericityT_tags":         "BDT_common5_input_transverse_sphericity_tags",

    "avg_CSV_jets":             "Evt_CSV_Average",
    "avg_CSV_tags":             "Evt_CSV_Average_Tagged",

    "max_CSV_jets":             "CSV[0]",
    "max_CSV_tags":             "CSV[0]",

    "min_CSV_jets":             "Evt_CSV_Min",
    "min_CSV_tags":             "Evt_CSV_Min_Tagged",

    "min_dR_lep_jet":           "Evt_Dr_MinDeltaRLeptonJet",
    "min_dR_lep_tag":           "Evt_Dr_MinDeltaRLeptonTaggedJet",

    # fox wolframs
    "H_2":                      "BDT_common5_input_h1",
    "H_3":                      "BDT_common5_input_h2",
    "H_4":                      "BDT_common5_input_h3",

    "M_lep_closest_tag":        "Evt_M_MinDeltaRLeptonTaggedJet",

    "avg_deta_bb":              "Evt_Deta_TaggedJetsAverage",
    "avg_dR_bb":                "Evt_Dr_TaggedJetsAverage",

    "M2_of_min_dR_bb":          "BDT_common5_input_closest_tagged_dijet_mass",
    "2nd_moment_tagged_jets_CSVs":      "BDT_common5_input_dev_from_avg_disc_btags",

    "avg_M_jets":               "Evt_M_JetsAverage",
    "avg_M2_tags":              "Evt_M2_TaggedJetsAverage",

    "N_tags_tight":             "N_BTagsT",

    "M2_bb_closest_to_125":     "BDT_common5_input_tagged_dijet_mass_closest_to_125",

    "2nd_highest_CSV":          "CSV[1]",

    "blr":                      "Evt_blr_ETH",
    "blr_transformed":          "Evt_blr_ETH_transformed",
    "dank_MEM":                 None,
    }

    # categories
    # SL 4j,>=3b
    variables_4j_3b = [
        "pT_j1",
        "CSV_j1",

        "eta_j2",
        "CSV_j2",

        "eta_j3",
        "CSV_j3",

        "pT_j4",
        "eta_j4",
        "CSV_j4",

        "eta_lep1",

        "HT_tag",

        "min_dR_jj",
        "min_dR_bb",

        "aplanarity_tags",
        "sphericity_jets",

        "sphericityT_jets",
        "sphericityT_tags",

        "avg_CSV_jets",
        "avg_CSV_tags",
        "max_CSV_jets",
        "max_CSV_tags",
        "min_CSV_jets",
        "min_CSV_tags",

        "min_dR_lep_jet",

        "H_3",
        "H_4",

        "M_lep_closest_tag",
        "M2_of_min_dR_bb",
        "2nd_moment_tagged_jets_CSVs",

        "avg_M_jets",
        "avg_M2_tags",

        "N_tags_tight",

        "2nd_highest_CSV",

        "blr",
        "blr_transformed",
        "dank_MEM",
        ]

    # SL 5j,>=3b
    variables_5j_3b = [
        "pT_j1",
        "eta_j1",
        "CSV_j1",

        "pT_j2",
        "eta_j2",
        "CSV_j2",

        "pT_j3",
        "eta_j3",
        "CSV_j3",

        "pT_j4",
        "eta_j4",

        "pT_lep1",

        "HT",
        "HT_tag",

        "min_dR_jj",
        "min_dR_bb",

        "max_dR_jj",

        "aplanarity_jets",
        "aplanarity_tags",

        "sphericity_jets",
        "sphericity_tags",

        "sphericityT_jets",
        "sphericityT_tags",

        "avg_CSV_jets",
        "avg_CSV_tags",

        "max_CSV_jets",
        "max_CSV_tags",

        "min_CSV_jets",
        "min_CSV_tags",

        "min_dR_lep_jet",
        "min_dR_lep_tag",

        "H_2",
        "H_3",

        "M_lep_closest_tag",

        "avg_dR_bb",

        "M2_of_min_dR_bb",
        "2nd_moment_tagged_jets_CSVs",

        "avg_M_jets",

        "N_tags_tight",

        "M2_bb_closest_to_125",

        "2nd_highest_CSV",

        "blr",
        "blr_transformed",
        "dank_MEM",
        ]



    # SL >=6j, >=3b
    variables_6j_3b = [
        "eta_j1",
        "CSV_j1",

        "eta_j2",
        "CSV_j2",

        "eta_j3",
        "CSV_j3",

        "eta_j4",
        "CSV_j4",

        "pT_lep1",
        "eta_lep1",

        "HT_tag",

        "min_dR_jj",
        "min_dR_bb",

        "max_dR_bb",

        "aplanarity_jets",
        "aplanarity_tags",

        "centrality_jets",
        "centrality_tags",

        "sphericity_jets",
        "sphericity_tags",

        "sphericityT_jets",
        "sphericityT_tags",

        "avg_CSV_jets",
        "avg_CSV_tags",

        "max_CSV_jets",
        "max_CSV_tags",

        "min_CSV_jets",
        "min_CSV_tags",

        "min_dR_lep_tag",

        "H_4",

        "M_lep_closest_tag",

        "avg_deta_bb",
        "avg_dR_bb",

        "M2_of_min_dR_bb",
        "2nd_moment_tagged_jets_CSVs",

        "avg_M_jets",
        "avg_M2_tags",

        "N_tags_tight",

        "M2_bb_closest_to_125",

        "2nd_highest_CSV",

        "blr",
        "blr_transformed",
        "dank_MEM",
        ]
    if region=='4j3t':
      return variables_4j_3b = [all_variables[var] for var in variables_4j_3b if not var in undefined_variables]
    elif region=='5j3t':
      return variables_5j_3b = [all_variables[var] for var in variables_5j_3b if not var in undefined_variables]
    elif region=='6j3t'
      return variables_6j_3b = [all_variables[var] for var in variables_6j_3b if not var in undefined_variables]
      
  def _fill_vector(self,cat):

    master_string= ""
    if cat == '4j3t': 
      for i,value in enumerate(self._variable_helper_function('4j3t')):

        master_string+="tensor_4j3t.tensor<float,2>()(0,"+str(i)") = float("+str(value)"); \n"
      return master_string
    elif cat == '5j3t':
       for i,value in enumerate(self._variable_helper_function('5j3t')):

        master_string+="tensor_5j3t.tensor<float,2>()(0,"+str(i)") = float("+str(value)"); \n"
      return master_string
    elif cat == 'j3t':
       for i,value in enumerate(self._variable_helper_function('6j3t')):

        master_string+="tensor_6j3t.tensor<float,2>()(0,"+str(i)") = float("+str(value)"); \n"
      return master_string
