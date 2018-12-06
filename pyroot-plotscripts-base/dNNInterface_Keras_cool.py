import tensorflow
import csv
import os
import uuid
from distutils.dir_util import copy_tree

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
    
    self.unique_id = uuid.uuid4()
    self.path_to_chekpoitns =os.getcwd()+"/workdir/checkpoints_"+str(self.unique_id)
    if not os.path.isdir("workdir"):
		os.mkdir("workdir")
		os.mkdir(self.path_to_chekpoitns)
    # location of plain DNNs (no prenet)
    copy_tree('/nfs/dust/cms/user/vdlinden/DNN_checkpoints/',self.path_to_chekpoitns)
    self._get_variables_from_csv()

    rstr="""

    //6j3t cat
    const string pathToGraph_6j3t =\""""+str(self.path_to_chekpoitns)+"""/6j3t/trained_model.meta";
    const string checkpointPath_6j3t =\""""+str(self.path_to_chekpoitns)+"""/6j3t/trained_model";

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
    const string pathToGraph_5j3t =\""""+str(self.path_to_chekpoitns)+"""/5j3t/trained_model.meta";
    const string checkpointPath_5j3t =\""""+str(self.path_to_chekpoitns)+"""/5j3t/trained_model";

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
    const string pathToGraph_4j3t = \""""+str(self.path_to_chekpoitns)+"""/4j3t/trained_model.meta";
    const string checkpointPath_4j3t =\""""+str(self.path_to_chekpoitns)+"""/4j3t/trained_model";

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
    
    rstr+="int num_features_4j3t = "+str(len(self.variables_4j_3t))+";\n"
    
       
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
    
    rstr+="int num_features_5j3t = "+str(len(self.variables_5j_3t))+";\n"
       
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
    
    rstr+="int num_features_6j3t = "+str(len(self.variables_6j_3t))+";\n"
       
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

       std::vector<std::pair<std::string, tensorflow::Tensor>> feed_dict;
       std::vector<tensorflow::Tensor> outputTensors;
       Tensor drop_1 (DT_FLOAT, TensorShape({ 1}));

      drop_1.tensor<float,1>()(0) = 1.0;


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
    feed_dict.push_back(std::make_pair("dense_1_input",tensor_4j3t));"""
    rstr+= self._fix_dropout('4j3t')
    rstr+="""


    status_4j3t = session_4j3t->Run(feed_dict, {"dense_4/Softmax"},  {}, &outputTensors);
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
    // fish for fishy outputs
//    for(int jclass=0; jclass<num_classes_4j3t; jclass++){
//      if(outputTensors.at(0).tensor<float,2>()(0,jclass)>0.95 or outputTensors.at(0).tensor<float,2>()(0,jclass)<0.05 or DNN_4j3t_pred_class<0 or DNN_4j3t_pred_class>5 ){
//      printstuff=1;
//      std::cout<<std::endl<<"Something is fishy here "<<Evt_ID<<std::endl;
//      }
//    }
    // take close look at 4j4t events
    if(N_Jets==4 && N_BTagsM==4){
      printstuff=1; 
      std::cout<<std::endl<<"4j4t event"<<std::endl;
    }
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
    feed_dict.push_back(std::make_pair("dense_1_input",tensor_5j3t));"""
    rstr+= self._fix_dropout('5j3t')
    rstr+="""

    status_5j3t = session_5j3t->Run(feed_dict, {"dense_4/Softmax"},  {}, &outputTensors);
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
    DNN_5j3t_pred_class  = getMaxPosition(outputTensors,num_classes_5j3t);

    bool printstuff=0;
    // fish for fishy outputs
//    for(int jclass=0; jclass<num_classes_5j3t; jclass++){
//      if(outputTensors.at(0).tensor<float,2>()(0,jclass)>0.95 or outputTensors.at(0).tensor<float,2>()(0,jclass)<0.05 or DNN_5j3t_pred_class<0 or DNN_5j3t_pred_class>5 ){
//      //printstuff=1;
//      std::cout<<std::endl<<"Something is fishy here "<<Evt_ID<<std::endl;
//      }
//    }
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
    feed_dict.push_back(std::make_pair("dense_1_input",tensor_6j3t));"""

    rstr+= self._fix_dropout('6j3t')

    rstr+="""status_6j3t = session_6j3t->Run(feed_dict, {"dense_4/Softmax"},  {}, &outputTensors);
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
        // fish for fishy outputs
//    for(int jclass=0; jclass<num_classes_6j3t; jclass++){
//      if(outputTensors.at(0).tensor<float,2>()(0,jclass)>0.95 or outputTensors.at(0).tensor<float,2>()(0,jclass)<0.05 or DNN_6j3t_pred_class<0 or DNN_6j3t_pred_class>5 ){
//      printstuff=1;
//      std::cout<<std::endl<<"Something is fishy here "<<Evt_ID<<std::endl;
//      }
//    }
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
  
  def _get_variables_from_csv(self):
  	# Read variables from cvs files. The order of the variables is important for the DNN
  	self.variables_4j_3t = []
  	self.means_4j3t = []
  	self.stddev_4j3t = []
  	self.variables_5j_3t = []
  	self.means_5j3t = []
  	self.stddev_5j3t = []
  	self.variables_6j_3t = []
  	self.means_6j3t = []
  	self.stddev_6j3t = []

  	with open(self.path_to_chekpoitns+"/4j3t/variable_norm.csv") as csv_file:
  		csv_reader = csv.reader(csv_file,delimiter=',')
  		for i, row in enumerate(csv_reader):
  			if i != 0:
  				# MEM is not named right in CSV, workaround. TODO: Fix name in preprocessing
  				if row[0]=="MEM":
  					self.variables_4j_3t.append('memDBp')
  				else:
  					self.variables_4j_3t.append(row[0])
  				self.means_4j3t.append(row[1])
  				self.stddev_4j3t.append(row[2])

  	with open(self.path_to_chekpoitns+"/5j3t/variable_norm.csv") as csv_file:
  		csv_reader = csv.reader(csv_file,delimiter=',')
  		for i, row in enumerate(csv_reader):
  			if i != 0:
  				if row[0]=="MEM":
  					self.variables_5j_3t.append('memDBp')
  				else:
  					self.variables_5j_3t.append(row[0])
  				self.means_5j3t.append(row[1])
  				self.stddev_5j3t.append(row[2])

  	with open(self.path_to_chekpoitns+"/6j3t/variable_norm.csv") as csv_file:
  		csv_reader = csv.reader(csv_file,delimiter=',')
  		for i, row in enumerate(csv_reader):
  			if i != 0:
  				if row[0]=="MEM":
  					self.variables_6j_3t.append('memDBp')
  				else:
  					self.variables_6j_3t.append(row[0])
  				self.means_6j3t.append(row[1])
  				self.stddev_6j3t.append(row[2])

      
  def _fill_vector(self,cat):
   
  	# Helper function to fill inputtensors for tensorflow
    master_string= ""
    if cat == '4j3t': 
        for i,value in enumerate(self.variables_4j_3t):
            master_string+="tensor_4j3t.tensor<float,2>()(0,"+str(i)+") = float(("+str(value)+"-("+str(self.means_4j3t[i])+"))/"+str(self.stddev_4j3t[i])+"); \n"
        return master_string
    elif cat == '5j3t':
        for i,value in enumerate(self.variables_5j_3t):
            master_string+="tensor_5j3t.tensor<float,2>()(0,"+str(i)+") = float(("+str(value)+"-("+str(self.means_5j3t[i])+"))/"+str(self.stddev_5j3t[i])+"); \n"
        return master_string
    elif cat == '6j3t':
        for i,value in enumerate(self.variables_6j_3t):
            master_string+="tensor_6j3t.tensor<float,2>()(0,"+str(i)+") = float(("+str(value)+"-("+str(self.means_6j3t[i])+"))/"+str(self.stddev_6j3t[i])+"); \n"
            master_string+="//cout<<float(("+str(value)+"-("+str(self.means_6j3t[i])+"))/"+str(self.stddev_6j3t[i])+")<<std::endl; \n"
            
        return master_string

  def _fix_dropout(self,cat):
  	# Check how many dropout layers are in a model and feed the kepp_pro of 1 -> deactivates dropout

  	# Clear default graph, otherwise old stuff still in the graph
    tensorflow.reset_default_graph()
    master_string = ""
    if cat == '4j3t':
	  sess_1=tensorflow.Session()
	  saver_1= tensorflow.train.import_meta_graph(self.path_to_chekpoitns+'/4j3t/trained_model.meta')
	  saver_1.restore(sess_1,self.path_to_chekpoitns+'/4j3t/trained_model')
	  graph = tensorflow.get_default_graph()

    elif cat == '5j3t':

	  sess_2=tensorflow.Session()
	  saver_2 = tensorflow.train.import_meta_graph(self.path_to_chekpoitns+'/5j3t/trained_model.meta')
	  saver_2.restore(sess_2,self.path_to_chekpoitns+'/5j3t/trained_model')
	  graph = tensorflow.get_default_graph()

    elif cat == '6j3t':

	  sess_1=tensorflow.Session()
	  saver_1 = tensorflow.train.import_meta_graph(self.path_to_chekpoitns+'/6j3t/trained_model.meta')
	  saver_1.restore(sess_1,self.path_to_chekpoitns+'/6j3t/trained_model')
	  graph = tensorflow.get_default_graph()

    graph = tensorflow.get_default_graph()
    for op in graph.get_operations():
	  if op.name.find("dropout/keep_prob")!=-1:
	    master_string+="feed_dict.push_back(std::make_pair(\""+op.name + "\", drop_1)); \n"

    return master_string

