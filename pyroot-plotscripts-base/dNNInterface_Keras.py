
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
  return max_pos;
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
       int num_classes_4j3t = 6;
    """
    
    rstr+="int num_features_4j3t = "+str(len(self._variable_helper_function("4j3t")))+";\n"
    #rstr+="cout<<"+str(len(self._variable_helper_function("4j3t")))+"<<std::endl;\n"
    
       
    rstr+="""
       double DNN_Out_4j3t_ttbar2B  = -6;
       double DNN_Out_4j3t_ttbarB  = -6;
       double DNN_Out_4j3t_ttbarBB  = -6;
       double DNN_Out_4j3t_ttbarCC  = -6;
       double DNN_Out_4j3t_ttbarlf = -6;
       double DNN_Out_4j3t_ttH  = -6;
       int DNN_4j3t_pred_class  = -6;

       int num_classes_5j3t = 6;
    """
    
    rstr+="int num_features_5j3t = "+str(len(self._variable_helper_function("5j3t")))+";\n"
       
    rstr+="""
       double DNN_Out_5j3t_ttbar2B  = -6;
       double DNN_Out_5j3t_ttbarB  = -6;
       double DNN_Out_5j3t_ttbarBB  = -6;
       double DNN_Out_5j3t_ttbarCC  = -6;
       double DNN_Out_5j3t_ttbarlf = -6;
       double DNN_Out_5j3t_ttH  = -6;
       int DNN_5j3t_pred_class  = -6;

       int num_classes_6j3t = 6;
    """
    
    rstr+="int num_features_6j3t = "+str(len(self._variable_helper_function("6j3t")))+";\n"
       
    rstr+="""
        double DNN_Out_6j3t_ttbar2B  = -6;
       double DNN_Out_6j3t_ttbarB  = -6;
       double DNN_Out_6j3t_ttbarBB  = -6;
       double DNN_Out_6j3t_ttbarCC  = -6;
       double DNN_Out_6j3t_ttbarlf  = -6;
       double DNN_Out_6j3t_ttH  = -6;
       int DNN_6j3t_pred_class= -6;

       Tensor tensor_4j3t (DT_FLOAT, TensorShape({1,num_features_4j3t}));
       Tensor tensor_5j3t (DT_FLOAT, TensorShape({1,num_features_5j3t}));
       Tensor tensor_6j3t (DT_FLOAT, TensorShape({1,num_features_6j3t}));

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
  //std::cout<<N_Jets<<" "<<N_BTagsM<<std::endl;
  if (N_Jets == 4 and N_BTagsM >= 3){
    //Load Data
    """
    rstr+=str(self._fill_vector('4j3t'))
    rstr+="""

    //Run graph
    vector<pair<string,Tensor>> input2 = {{"input",tensor_4j3t}};
    status_4j3t = session_4j3t->Run(input2, {"output/Softmax"},  {}, &outputTensors);
    //if (!status_4j3t.ok()) 
    //{
    //  std::cout << status_4j3t.ToString() << std::endl;
    //}
    //else
    //{
    //  std::cout << "Success load graph !! " << std::endl;
    //}

    //Feed output into right variables

    DNN_Out_4j3t_ttbar2B  = outputTensors.at(0).tensor<float,2>()(0,2);
    DNN_Out_4j3t_ttbarB  = outputTensors.at(0).tensor<float,2>()(0,3);
    DNN_Out_4j3t_ttbarBB  = outputTensors.at(0).tensor<float,2>()(0,1);
    DNN_Out_4j3t_ttbarCC  = outputTensors.at(0).tensor<float,2>()(0,4);
    DNN_Out_4j3t_ttbarlf  = outputTensors.at(0).tensor<float,2>()(0,5);
    DNN_Out_4j3t_ttH  = outputTensors.at(0).tensor<float,2>()(0,0);
    DNN_4j3t_pred_class  = getMaxPosition(outputTensors,num_classes_4j3t);

    bool printstuff=0;
    if(iEntry<200){printstuff=1;}
    if(printstuff){
      cout<<"-----DNN-----"<<std::endl;
      std::cout<<"jt="<<N_Jets<<" "<<N_BTagsM<< "event "<<Evt_Run<<" "<<Evt_Lumi<<" "<<Evt_ID<<std::endl;
      cout<<"mem "<<memDBp<<std::endl;
for(int ifeat=0; ifeat<num_features_4j3t;ifeat++){
        cout<<tensor_4j3t.tensor<float,2>()(0,ifeat)<<std::endl;
        }
      
      cout<<"ttH node "<<DNN_Out_4j3t_ttH<<std::endl;
      cout<<"ttbarBB node "<<DNN_Out_4j3t_ttbarBB<<std::endl;
      cout<<"ttbar2B node "<<DNN_Out_4j3t_ttbar2B<<std::endl;
      cout<<"ttbarB node "<<DNN_Out_4j3t_ttbarB<<std::endl;
      cout<<"ttbarCC node "<<DNN_Out_4j3t_ttbarCC<<std::endl;
      cout<<"ttbarOther node "<<DNN_Out_4j3t_ttbarlf<<std::endl;
      
      cout<<"predicted class "<< DNN_4j3t_pred_class<<std::endl;
     }
  }
  else if (N_Jets == 5 and N_BTagsM >= 3){
    """
    rstr+=str(self._fill_vector('5j3t'))
    rstr+="""

    //Run graph
    vector<pair<string,Tensor>> input2 = {{"input",tensor_5j3t}};
    status_5j3t = session_5j3t->Run(input2, {"output/Softmax"},  {}, &outputTensors);
    //if (!status_5j3t.ok()) 
    //{
    //  std::cout << status_5j3t.ToString() << std::endl;
    //}
    //else
    //{
    //  std::cout << "Success load graph !! " << std::endl;
    //}

    //Feed output into right variables

    DNN_Out_5j3t_ttbar2B  = outputTensors.at(0).tensor<float,2>()(0,2);
    DNN_Out_5j3t_ttbarB  = outputTensors.at(0).tensor<float,2>()(0,3);
    DNN_Out_5j3t_ttbarBB  = outputTensors.at(0).tensor<float,2>()(0,1);
    DNN_Out_5j3t_ttbarCC  = outputTensors.at(0).tensor<float,2>()(0,4);
    DNN_Out_5j3t_ttbarlf  = outputTensors.at(0).tensor<float,2>()(0,5);
    DNN_Out_5j3t_ttH  = outputTensors.at(0).tensor<float,2>()(0,0);
    DNN_5j3t_pred_class  = getMaxPosition(outputTensors,num_classes_4j3t);

    bool printstuff=0;
    if(iEntry<200){printstuff=1;}
    if(printstuff){
      cout<<"-----DNN-----"<<std::endl;
      std::cout<<"jt="<<N_Jets<<" "<<N_BTagsM<< "event "<<Evt_Run<<" "<<Evt_Lumi<<" "<<Evt_ID<<std::endl;
      cout<<"mem "<<memDBp<<std::endl;
for(int ifeat=0; ifeat<num_features_5j3t;ifeat++){
        cout<<tensor_5j3t.tensor<float,2>()(0,ifeat)<<std::endl;
        }
      
      cout<<"ttH node "<<DNN_Out_5j3t_ttH<<std::endl;
      cout<<"ttbarBB node "<<DNN_Out_5j3t_ttbarBB<<std::endl;
      cout<<"ttbar2B node "<<DNN_Out_5j3t_ttbar2B<<std::endl;
      cout<<"ttbarB node "<<DNN_Out_5j3t_ttbarB<<std::endl;
      cout<<"ttbarCC node "<<DNN_Out_5j3t_ttbarCC<<std::endl;
      cout<<"ttbarOther node "<<DNN_Out_5j3t_ttbarlf<<std::endl;
      cout<<"predicted class "<< DNN_5j3t_pred_class<<std::endl;
     }

  }
  else if(N_Jets >= 6 and N_BTagsM >= 3){
      """
    rstr+=str(self._fill_vector('6j3t'))
    rstr+="""

    //Run graph
    vector<pair<string,Tensor>> input2 = {{"input",tensor_6j3t}};
    status_6j3t = session_6j3t->Run(input2, {"output/Softmax"},  {}, &outputTensors);
    //if (!status_6j3t.ok()) 
    //{
    //  std::cout << status_6j3t.ToString() << std::endl;
    //}
    //else
    //{
    //  std::cout << "Success load graph !! " << std::endl;
    //}

    //Feed output into right variables

    DNN_Out_6j3t_ttbar2B  = outputTensors.at(0).tensor<float,2>()(0,2);
    DNN_Out_6j3t_ttbarB  = outputTensors.at(0).tensor<float,2>()(0,3);
    DNN_Out_6j3t_ttbarBB  = outputTensors.at(0).tensor<float,2>()(0,1);
    DNN_Out_6j3t_ttbarCC  = outputTensors.at(0).tensor<float,2>()(0,4);
    DNN_Out_6j3t_ttbarlf  = outputTensors.at(0).tensor<float,2>()(0,5);
    DNN_Out_6j3t_ttH  = outputTensors.at(0).tensor<float,2>()(0,0);
    DNN_6j3t_pred_class  = getMaxPosition(outputTensors,num_classes_6j3t);

    bool printstuff=0;
    if(iEntry<200){printstuff=1;}
    if(printstuff){
      std::cout<<"-----DNN-----"<<std::endl;
      std::cout<<"jt="<<N_Jets<<" "<<N_BTagsM<< "event "<<Evt_Run<<" "<<Evt_Lumi<<" "<<Evt_ID<<std::endl;
      cout<<"mem "<<memDBp<<std::endl;
      for(int ifeat=0; ifeat<num_features_6j3t;ifeat++){
        cout<<tensor_6j3t.tensor<float,2>()(0,ifeat)<<std::endl;
        }
      
      cout<<"ttH node "<<DNN_Out_6j3t_ttH<<std::endl;
      cout<<"ttbarBB node "<<DNN_Out_6j3t_ttbarBB<<std::endl;
      cout<<"ttbar2B node "<<DNN_Out_6j3t_ttbar2B<<std::endl;
      cout<<"ttbarB node "<<DNN_Out_6j3t_ttbarB<<std::endl;
      cout<<"ttbarCC node "<<DNN_Out_6j3t_ttbarCC<<std::endl;
      cout<<"ttbarOther node "<<DNN_Out_6j3t_ttbarlf<<std::endl;
      std::cout<<"predicted class "<< DNN_6j3t_pred_class<<std::endl;
     }
  }
 

  // classes are 
  // 0 = ttH 
  // 1 = ttbb 
  // 2 = tt2b 
  // 3 = ttb 
  // 4 = ttcc 
  // 5 = ttlf

  
"""

    return rstr

  def getTestCallLines(self):
    rstr=""  
    #rstr="""
  #//TODO: Change TestCallLines
  #std::vector<TLorentzVector> testdnnjets = {
        #makeVectorE(561.853400685, -1.687604070, 1.248519063, 48.315901270),
        #makeVectorE(317.050318074, -0.592420697, -1.641329408, 41.454653026),
        #makeVectorE(130.993330071, -0.257405132, -2.218888283, 15.829634094),
        #makeVectorE(90.088794331, -0.758062780, -1.199205875, 11.687776745),
        #makeVectorE(57.793076163, 0.163249642, 2.988173246, 9.959981641),
        #makeVectorE(45.080527604, -1.838460445, 1.761856556, 7.07615728)
    #};
    #std::vector<double> testdnnjetCSVs = {
        #0.592329562, 0.156740859, 0.998748481, 0.944896400, 0.268956393, 0.109731160
    #};

    #TLorentzVector testdnnlepton = makeVectorM(45.567291260, -1.122234225, 2.685425282, 0.105700001);
    #TLorentzVector testdnnmet = makeVectorM(70.089050293, 0.0, -2.230507374, 0.0); 
    #std::vector<double> testdnnAddFeatures;
    #testdnnAddFeatures.push_back(1.); // blr
    #testdnnAddFeatures.push_back(1.); // blr_transformed
    #testdnnAddFeatures.push_back(1.); // MEM
    
    #// evaluate
    #DNNOutput aachentestdnnoutput = dnn.evaluate(testdnnjets, testdnnjetCSVs, testdnnlepton, testdnnmet, testdnnAddFeatures);
    #std::vector<double> targetOutputsfordnntest = { 0.51680371, 0.25959021, 0.07142095, 0.07112622, 0.05624627, 0.02481263, 0.0};
    #std::cout<<"doing DNN unit test"<<std::endl;
    #std::cout<<"No error printout means it worked"<<std::endl;
    #for (size_t i = 0; i < targetOutputsfordnntest.size(); ++i)
    #{
        #//assert(fabs(targetOutputsfordnntest[i] - aachentestdnnoutput.values[i]) < 0.000001 && "The DNN output for 6 jet events is incorrect");
    #}
#"""
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
    "dank_MEM":                 "memDBp",
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
        #"max_CSV_tags",
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
        #"max_CSV_tags",

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
        #"max_CSV_tags",

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
      return  [all_variables[var] for var in variables_4j_3b ]
    elif region=='5j3t':
      return  [all_variables[var] for var in variables_5j_3b ]
    elif region=='6j3t':
      return  [all_variables[var] for var in variables_6j_3b ]
      
  def _fill_vector(self,cat):
    
    means_4j3t = [137.42442321777344, 0.7040854692459106, -0.002667010063305497, 0.706744372844696, -0.0029508802108466625, 0.6589658260345459, 44.81528091430664, -0.005932101514190435, 0.6004650592803955, -0.001963152550160885, 265.8736877441406, 1.0248833894729614, 1.3533670902252197, 0.037160590291023254, 0.3212321102619171, 0.3685488700866699, 0.3482910394668579, 0.6682165861129761, 0.8427796959877014, 0.9680687785148621, 0.12919066846370697, 0.6893522143363953, 1.2168452739715576, 0.029151437804102898, -0.00427990173920989, 91.96558380126953, 104.1175537109375, 0.018611226230859756, 8.265861511230469, 160.66160583496094, 2.015070642093216, 0.8731255531311035, 0.4207630753517151, -0.08600679785013199,0.0434101040506144]
    
    stddev_4j3t = [75.24872589111328, 0.32950106263160706, 1.071563482284546, 0.3353903591632843, 1.1041667461395264, 0.36023637652397156, 15.387630462646484, 1.1405773162841797, 0.3784834146499634, 1.0388246774673462, 117.03247833251953, 0.3717459440231323, 0.5251893997192383, 0.04789897799491882, 0.18624438345432281, 0.22396820783615112, 0.2246055006980896, 0.09083244949579239, 0.08815127611160278, 0.05874808132648468, 0.19366784393787384, 0.14462552964687347, 0.46422579884529114, 0.08465658128261566, 0.06357312947511673, 42.57014083862305, 52.89622116088867, 0.014765373431146145, 2.8693623542785645, 74.20048522949219, 0.8281713935766097, 0.12357530742883682, 0.3543999195098877, 3.0725975036621094,0.16827486722246718]
    
    means_5j3t = [156.375732421875, -0.00032880803337320685, 0.6131682991981506, 105.55225372314453, -0.004987628664821386, 0.6288220286369324, 75.91429901123047, -0.003388760844245553, 0.5913440585136414, 56.25959777832031, -0.0018144077621400356, 75.46308898925781, 597.2225341796875, 283.2565002441406, 0.833136260509491, 1.298830509185791, 3.3669307231903076, 0.07262205332517624, 0.039233606308698654, 0.34573566913604736, 0.29650983214378357, 0.38770490884780884, 0.35514912009239197, 0.5750634670257568, 0.8545134663581848, 0.9723204374313354, 0.04474116489291191, 0.7062298059463501, 1.0992268323898315, 1.2617878913879395, 0.03608007729053497, 0.03382204473018646, 91.98273468017578, 2.1716742515563965, 104.11076354980469, 0.01721077226102352, 6.3061418533325195, 2.1743043582276704, 126.14007568359375, 0.889057993888855, 0.6431511044502258, 1.8492393493652344,0.09970538353532113]
    
    stddev_5j3t = [88.20352172851562, 1.0197919607162476, 0.379265695810318, 51.25883483886719, 1.0398567914962769, 0.38030382990837097, 30.92882537841797, 1.0721449851989746, 0.3952060639858246, 20.394432067871094, 1.1045029163360596, 46.308982849121094, 209.8328857421875, 124.52266693115234, 0.27812954783439636, 0.524810254573822, 0.44963932037353516, 0.061429448425769806, 0.04927894100546837, 0.1887226551771164, 0.182241752743721, 0.22402966022491455, 0.22506974637508392, 0.08860533684492111, 0.0877293199300766, 0.054021451622247696, 0.08164707571268082, 0.1492588371038437, 0.4125250577926636, 0.5172849297523499, 0.11800339072942734, 0.07911771535873413, 44.468082427978516, 0.41986992955207825, 54.75101089477539, 0.01454669889062643, 2.022589921951294, 0.8710606106845818, 32.66651153564453, 0.11747807264328003, 0.3359447419643402, 3.4670112133026123,0.25546956531646264]

    means_6j3t = [-0.0008877884829416871, 0.4935821294784546, -0.0025072903372347355, 0.5363996028900146, -0.003351669292896986, 0.5134074687957764, -0.0020857935305684805, 0.4836447238922119, 79.5152587890625, -0.0029293408151715994, 306.08428955078125, 0.6799668073654175, 1.2340381145477295, 2.9112722873687744, 0.08225125074386597, 0.04102278873324394, 0.6223732829093933, 0.6703897714614868, 0.35639750957489014, 0.29853734374046326, 0.3923519551753998, 0.35610607266426086, 0.47097671031951904, 0.8573898673057556, 0.9742678999900818, 0.017539111897349358, 0.7076912522315979, 1.2088245153427124, -0.0018109147204086185, 92.76698303222656, 0.9589356780052185, 2.1291556358337402, 104.26104736328125, 0.016947662457823753, 4.670713901519775, 166.32098388671875, 2.2768849141199157, 126.27725219726562, 0.8968206644058228, 0.7888676524162292, 3.2685322761535645,0.49101815172037266]

    stddev_6j3t = [1.0285539627075195, 0.40034034848213196, 1.0304632186889648, 0.4029228091239929, 1.0525333881378174, 0.4097650349140167, 1.0795516967773438, 0.4120606780052185, 50.92250442504883, 0.9998945593833923, 138.02743530273438, 0.19679751992225647, 0.5196573734283447, 0.587063729763031, 0.06376378983259201, 0.05062000826001167, 0.14537474513053894, 0.17313380539417267, 0.18998992443084717, 0.1838066577911377, 0.2232932299375534, 0.2260759472846985, 0.08877662569284439, 0.0869012251496315, 0.052015211433172226, 0.0422247052192688, 0.1498209834098816, 0.5142785310745239, 0.05038578808307648, 46.50405502319336, 0.4855087399482727, 0.4360775351524353, 58.25953674316406, 0.014364002272486687, 1.5304850339889526, 78.13500213623047, 0.90994039173215, 33.320430755615234, 0.11385979503393173, 0.2697998881340027, 3.5215914249420166,0.3414608286386706]



    master_string= ""
    if cat == '4j3t': 
        for i,value in enumerate(self._variable_helper_function('4j3t')):
            master_string+="tensor_4j3t.tensor<float,2>()(0,"+str(i)+") = float(("+str(value)+"-("+str(means_4j3t[i])+"))/"+str(stddev_4j3t[i])+"); \n"
        return master_string
    elif cat == '5j3t':
        for i,value in enumerate(self._variable_helper_function('5j3t')):
            master_string+="tensor_5j3t.tensor<float,2>()(0,"+str(i)+") = float(("+str(value)+"-("+str(means_5j3t[i])+"))/"+str(stddev_5j3t[i])+"); \n"
        return master_string
    elif cat == '6j3t':
        for i,value in enumerate(self._variable_helper_function('6j3t')):
            master_string+="tensor_6j3t.tensor<float,2>()(0,"+str(i)+") = float(("+str(value)+"-("+str(means_6j3t[i])+"))/"+str(stddev_6j3t[i])+"); \n"
            master_string+="//cout<<float(("+str(value)+"-("+str(means_6j3t[i])+"))/"+str(stddev_6j3t[i])+")<<std::endl; \n"
            
        return master_string
