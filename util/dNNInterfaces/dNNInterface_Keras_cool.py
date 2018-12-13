import tensorflow
import csv
import os
from distutils.dir_util import copy_tree

class theInterface:
  def __init__(self, workdir, cpLocation):
    self.workdir = workdir
    self.includeString = "-I/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/tensorflow-cc/1.3.0-elfike/tensorflow_cc/include -I/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/eigen/c7dc0a897676/include/eigen3 -I/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/protobuf/3.4.0-fmblme/include"
    #self.libraryString="-L/nfs/dust/cms/user/kelmorab/CMSSW_Moriond2017/cardsCMSSWTF/CMSSW_8_0_26_patch2/lib/slc6_amd64_gcc530 -lDNNBase -lDNNTensorflow -lTTHCommonClassifier"
    self.libraryString = "-L/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/tensorflow-cc/1.3.0-elfike/tensorflow_cc/lib -ltensorflow_cc -L/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/protobuf/3.4.0-fmblme/lib -lprotobuf -lrt"
    self.usesPythonLibraries = True
    self.DNNCheckpointLocation = cpLocation
    self.copyCheckpoints()
    self._get_variables_from_csv()

  def copyCheckpoints(self):
    self.localCheckpointPath = self.workdir + "/DNNCheckpoints/"
    if not os.path.exists(self.localCheckpointPath):
        os.makedirs(self.localCheckpointPath)
    copy_tree(self.DNNCheckpointLocation, self.localCheckpointPath)
    print("copied DNN checkpoint files to "+str(self.localCheckpointPath))
    print("checking structure of checkpoint files...")
    categories = ["4j_ge3t", "5j_ge3t", "ge6j_ge3t"]
    files = ["trained_model.meta", "trained_model.index", "trained_model.data-00000-of-00001", "variable_norm.csv", "checkpoint"]
    errors = False
    for cat in categories:
        cat_path = self.localCheckpointPath+"/"+cat
        if not os.path.exists(cat_path):
            print("directory "+cat_path+" missing.")
            errors = True
        else:
            for f in files:
                file_path = cat_path + "/" + f
                if not os.path.exists(file_path):
                    print("file "+str(file_path)+" missing.")
                    errors = True
    if errors:
        print("... not all neccesary files found for dnn loading")
        exit()
    else:
        print("... all files found.")

            

  def getExternalyCallableVariables(self):
    return [
        "DNN_Out_4j_ge3t_ttbar2B",
        "DNN_Out_4j_ge3t_ttbarB",
        "DNN_Out_4j_ge3t_ttbarBB",
        "DNN_Out_4j_ge3t_ttbarCC",
        "DNN_Out_4j_ge3t_ttbarlf",
        "DNN_Out_4j_ge3t_ttH",
        "DNN_4j_ge3t_pred_class",

        "DNN_Out_5j_ge3t_ttbar2B",
        "DNN_Out_5j_ge3t_ttbarB",
        "DNN_Out_5j_ge3t_ttbarBB",
        "DNN_Out_5j_ge3t_ttbarCC",
        "DNN_Out_5j_ge3t_ttbarlf",
        "DNN_Out_5j_ge3t_ttH",
        "DNN_5j_ge3t_pred_class",

        "DNN_Out_ge6j_ge3t_ttbar2B",
        "DNN_Out_ge6j_ge3t_ttbarB",
        "DNN_Out_ge6j_ge3t_ttbarBB",
        "DNN_Out_ge6j_ge3t_ttbarCC",
        "DNN_Out_ge6j_ge3t_ttbarlf",
        "DNN_Out_ge6j_ge3t_ttH",
        "DNN_ge6j_ge3t_pred_class",
        ]
    
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

    //ge6j_ge3t cat
    const string pathToGraph_ge6j_ge3t =\""""+str(self.localCheckpointPath)+"""/ge6j_ge3t/trained_model.meta";
    const string checkpointPath_ge6j_ge3t =\""""+str(self.localCheckpointPath)+"""/ge6j_ge3t/trained_model";

    auto session_ge6j_ge3t = NewSession(SessionOptions());
    if (session_ge6j_ge3t == nullptr) {
        throw runtime_error("Could not create Tensorflow session.");
    }

    Status status_ge6j_ge3t;

    // Read in the protobuf graph we exported
    MetaGraphDef graph_def_ge6j_ge3t;
    status_ge6j_ge3t = ReadBinaryProto(Env::Default(), pathToGraph_ge6j_ge3t, &graph_def_ge6j_ge3t);
    if (!status_ge6j_ge3t.ok()) {
        throw runtime_error("Error reading graph definition from " + pathToGraph_ge6j_ge3t + ": " + status_ge6j_ge3t.ToString());
    }

    // Add the graph to the session
    status_ge6j_ge3t = session_ge6j_ge3t->Create(graph_def_ge6j_ge3t.graph_def());
    if (!status_ge6j_ge3t.ok()) {
        throw runtime_error("Error creating graph: " + status_ge6j_ge3t.ToString());
    }


    // Read weights from the saved checkpoint
    Tensor checkpointPathTensor_ge6j_ge3t(DT_STRING, TensorShape());
    checkpointPathTensor_ge6j_ge3t.scalar<std::string>()() = checkpointPath_ge6j_ge3t;
    status_ge6j_ge3t = session_ge6j_ge3t->Run(
            {{ graph_def_ge6j_ge3t.saver_def().filename_tensor_name(), checkpointPathTensor_ge6j_ge3t },},
            {},
      {graph_def_ge6j_ge3t.saver_def().restore_op_name()},
            nullptr);
    if (!status_ge6j_ge3t.ok()) {
        throw runtime_error("Error loading checkpoint from " + checkpointPath_ge6j_ge3t + ": " + status_ge6j_ge3t.ToString());
    } 




    //5j_ge3t cat
    const string pathToGraph_5j_ge3t =\""""+str(self.localCheckpointPath)+"""/5j_ge3t/trained_model.meta";
    const string checkpointPath_5j_ge3t =\""""+str(self.localCheckpointPath)+"""/5j_ge3t/trained_model";

    auto session_5j_ge3t = NewSession(SessionOptions());
    if (session_5j_ge3t == nullptr) {
        throw runtime_error("Could not create Tensorflow session.");
    }

    Status status_5j_ge3t;

    // Read in the protobuf graph we exported
    MetaGraphDef graph_def_5j_ge3t;
    status_5j_ge3t = ReadBinaryProto(Env::Default(), pathToGraph_5j_ge3t, &graph_def_5j_ge3t);
    if (!status_5j_ge3t.ok()) {
        throw runtime_error("Error reading graph definition from " + pathToGraph_5j_ge3t + ": " + status_5j_ge3t.ToString());
    }

    // Add the graph to the session
    status_5j_ge3t = session_5j_ge3t->Create(graph_def_5j_ge3t.graph_def());
    if (!status_5j_ge3t.ok()) {
        throw runtime_error("Error creating graph: " + status_5j_ge3t.ToString());
    }


    // Read weights from the saved checkpoint
    Tensor checkpointPathTensor_5j_ge3t(DT_STRING, TensorShape());
    checkpointPathTensor_5j_ge3t.scalar<std::string>()() = checkpointPath_5j_ge3t;
    status_5j_ge3t = session_5j_ge3t->Run(
            {{ graph_def_5j_ge3t.saver_def().filename_tensor_name(), checkpointPathTensor_5j_ge3t },},
            {},
      {graph_def_5j_ge3t.saver_def().restore_op_name()},
            nullptr);
    if (!status_5j_ge3t.ok()) {
        throw runtime_error("Error loading checkpoint from " + checkpointPath_5j_ge3t + ": " + status_5j_ge3t.ToString());
    } 


    //4j_ge3t cat
    const string pathToGraph_4j_ge3t = \""""+str(self.localCheckpointPath)+"""/4j_ge3t/trained_model.meta";
    const string checkpointPath_4j_ge3t =\""""+str(self.localCheckpointPath)+"""/4j_ge3t/trained_model";

    auto session_4j_ge3t = NewSession(SessionOptions());
    if (session_4j_ge3t == nullptr) {
        throw runtime_error("Could not create Tensorflow session.");
    }

    Status status_4j_ge3t;

    // Read in the protobuf graph we exported
    MetaGraphDef graph_def_4j_ge3t;
    status_4j_ge3t = ReadBinaryProto(Env::Default(), pathToGraph_4j_ge3t, &graph_def_4j_ge3t);
    if (!status_4j_ge3t.ok()) {
        throw runtime_error("Error reading graph definition from " + pathToGraph_4j_ge3t + ": " + status_4j_ge3t.ToString());
    }

    // Add the graph to the session
    status_4j_ge3t = session_4j_ge3t->Create(graph_def_4j_ge3t.graph_def());
    if (!status_4j_ge3t.ok()) {
        throw runtime_error("Error creating graph: " + status_4j_ge3t.ToString());
    }


    // Read weights from the saved checkpoint
    Tensor checkpointPathTensor_4j_ge3t(DT_STRING, TensorShape());
    checkpointPathTensor_4j_ge3t.scalar<std::string>()() = checkpointPath_4j_ge3t;
    status_4j_ge3t = session_4j_ge3t->Run(
            {{ graph_def_4j_ge3t.saver_def().filename_tensor_name(), checkpointPathTensor_4j_ge3t },},
            {},
      {graph_def_4j_ge3t.saver_def().restore_op_name()},
            nullptr);
    if (!status_4j_ge3t.ok()) {
        throw runtime_error("Error loading checkpoint from " + checkpointPath_4j_ge3t + ": " + status_4j_ge3t.ToString());
    } 




"""
    return rstr

  def getVariableInitInsideEventLoopLines(self):
    rstr="""
    // variables for DNNs
       int num_classes_4j_ge3t = 6;
    """
    
    rstr+="int num_features_4j_ge3t = "+str(len(self.variables_4j_ge3t))+";\n"
    
       
    rstr+="""
       double DNN_Out_4j_ge3t_ttbar2B  = -6;
       double DNN_Out_4j_ge3t_ttbarB  = -6;
       double DNN_Out_4j_ge3t_ttbarBB  = -6;
       double DNN_Out_4j_ge3t_ttbarCC  = -6;
       double DNN_Out_4j_ge3t_ttbarlf = -6;
       double DNN_Out_4j_ge3t_ttH  = -6;
       int DNN_4j_ge3t_pred_class  = -6;

       int num_classes_5j_ge3t = 6;
    """
    
    rstr+="int num_features_5j_ge3t = "+str(len(self.variables_5j_ge3t))+";\n"
       
    rstr+="""
       double DNN_Out_5j_ge3t_ttbar2B  = -6;
       double DNN_Out_5j_ge3t_ttbarB  = -6;
       double DNN_Out_5j_ge3t_ttbarBB  = -6;
       double DNN_Out_5j_ge3t_ttbarCC  = -6;
       double DNN_Out_5j_ge3t_ttbarlf = -6;
       double DNN_Out_5j_ge3t_ttH  = -6;
       int DNN_5j_ge3t_pred_class  = -6;

       int num_classes_ge6j_ge3t = 6;
    """
    
    rstr+="int num_features_ge6j_ge3t = "+str(len(self.variables_ge6j_ge3t))+";\n"
       
    rstr+="""
        double DNN_Out_ge6j_ge3t_ttbar2B  = -6;
       double DNN_Out_ge6j_ge3t_ttbarB  = -6;
       double DNN_Out_ge6j_ge3t_ttbarBB  = -6;
       double DNN_Out_ge6j_ge3t_ttbarCC  = -6;
       double DNN_Out_ge6j_ge3t_ttbarlf  = -6;
       double DNN_Out_ge6j_ge3t_ttH  = -6;
       int DNN_ge6j_ge3t_pred_class= -6;

       Tensor tensor_4j_ge3t (DT_FLOAT, TensorShape({1,num_features_4j_ge3t}));
       Tensor tensor_5j_ge3t (DT_FLOAT, TensorShape({1,num_features_5j_ge3t}));
       Tensor tensor_ge6j_ge3t (DT_FLOAT, TensorShape({1,num_features_ge6j_ge3t}));

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
    rstr+=str(self._fill_vector('4j_ge3t'))
    rstr+="""

    //Run graph
    feed_dict.push_back(std::make_pair("dense_1_input",tensor_4j_ge3t));"""
    rstr+= self._fix_dropout('4j_ge3t')
    rstr+="""


    status_4j_ge3t = session_4j_ge3t->Run(feed_dict, {"dense_3/Softmax"},  {}, &outputTensors);
    //if (!status_4j_ge3t.ok()) 
    //{
    //  std::cout << status_4j_ge3t.ToString() << std::endl;
    //}
    //else
    //{
    //  std::cout << "Success load graph !! " << std::endl;
    //}

    //Feed output into right variables

    DNN_Out_4j_ge3t_ttbar2B  = outputTensors.at(0).tensor<float,2>()(0,2);
    DNN_Out_4j_ge3t_ttbarB  = outputTensors.at(0).tensor<float,2>()(0,3);
    DNN_Out_4j_ge3t_ttbarBB  = outputTensors.at(0).tensor<float,2>()(0,1);
    DNN_Out_4j_ge3t_ttbarCC  = outputTensors.at(0).tensor<float,2>()(0,4);
    DNN_Out_4j_ge3t_ttbarlf  = outputTensors.at(0).tensor<float,2>()(0,5);
    DNN_Out_4j_ge3t_ttH  = outputTensors.at(0).tensor<float,2>()(0,0);
    DNN_4j_ge3t_pred_class  = getMaxPosition(outputTensors,num_classes_4j_ge3t);
    
    bool printstuff=0;
    if(iEntry<200){printstuff=1;}
    if(printstuff){
      cout<<"-----DNN-----"<<std::endl;
      std::cout<<"jt="<<N_Jets<<" "<<N_BTagsM<< "event "<<Evt_Run<<" "<<Evt_Lumi<<" "<<Evt_ID<<std::endl;
      cout<<"mem "<<memDBp<<std::endl;
for(int ifeat=0; ifeat<num_features_4j_ge3t;ifeat++){
        cout<<tensor_4j_ge3t.tensor<float,2>()(0,ifeat)<<std::endl;
        }
      
      cout<<"ttH node "<<DNN_Out_4j_ge3t_ttH<<std::endl;
      cout<<"ttbarBB node "<<DNN_Out_4j_ge3t_ttbarBB<<std::endl;
      cout<<"ttbar2B node "<<DNN_Out_4j_ge3t_ttbar2B<<std::endl;
      cout<<"ttbarB node "<<DNN_Out_4j_ge3t_ttbarB<<std::endl;
      cout<<"ttbarCC node "<<DNN_Out_4j_ge3t_ttbarCC<<std::endl;
      cout<<"ttbarOther node "<<DNN_Out_4j_ge3t_ttbarlf<<std::endl;
      
      cout<<"predicted class "<< DNN_4j_ge3t_pred_class<<std::endl;
     }
  }
  else if (N_Jets == 5 and N_BTagsM >= 3){
    """
    rstr+=str(self._fill_vector('5j_ge3t'))
    rstr+="""

    //Run graph
    feed_dict.push_back(std::make_pair("dense_1_input",tensor_5j_ge3t));"""
    rstr+= self._fix_dropout('5j_ge3t')
    rstr+="""

    status_5j_ge3t = session_5j_ge3t->Run(feed_dict, {"dense_3/Softmax"},  {}, &outputTensors);
    //if (!status_5j_ge3t.ok()) 
    //{
    //  std::cout << status_5j_ge3t.ToString() << std::endl;
    //}
    //else
    //{
    //  std::cout << "Success load graph !! " << std::endl;
    //}

    //Feed output into right variables

    DNN_Out_5j_ge3t_ttbar2B  = outputTensors.at(0).tensor<float,2>()(0,2);
    DNN_Out_5j_ge3t_ttbarB  = outputTensors.at(0).tensor<float,2>()(0,3);
    DNN_Out_5j_ge3t_ttbarBB  = outputTensors.at(0).tensor<float,2>()(0,1);
    DNN_Out_5j_ge3t_ttbarCC  = outputTensors.at(0).tensor<float,2>()(0,4);
    DNN_Out_5j_ge3t_ttbarlf  = outputTensors.at(0).tensor<float,2>()(0,5);
    DNN_Out_5j_ge3t_ttH  = outputTensors.at(0).tensor<float,2>()(0,0);
    DNN_5j_ge3t_pred_class  = getMaxPosition(outputTensors,num_classes_5j_ge3t);

    bool printstuff=0;
    if(iEntry<200){printstuff=1;}
    if(printstuff){
      cout<<"-----DNN-----"<<std::endl;
      std::cout<<"jt="<<N_Jets<<" "<<N_BTagsM<< "event "<<Evt_Run<<" "<<Evt_Lumi<<" "<<Evt_ID<<std::endl;
      cout<<"mem "<<memDBp<<std::endl;
for(int ifeat=0; ifeat<num_features_5j_ge3t;ifeat++){
        cout<<tensor_5j_ge3t.tensor<float,2>()(0,ifeat)<<std::endl;
        }
     
      cout<<"ttH node "<<DNN_Out_5j_ge3t_ttH<<std::endl;
      cout<<"ttbarBB node "<<DNN_Out_5j_ge3t_ttbarBB<<std::endl;
      cout<<"ttbar2B node "<<DNN_Out_5j_ge3t_ttbar2B<<std::endl;
      cout<<"ttbarB node "<<DNN_Out_5j_ge3t_ttbarB<<std::endl;
      cout<<"ttbarCC node "<<DNN_Out_5j_ge3t_ttbarCC<<std::endl;
      cout<<"ttbarOther node "<<DNN_Out_5j_ge3t_ttbarlf<<std::endl;
      cout<<"predicted class "<< DNN_5j_ge3t_pred_class<<std::endl;
     }

  }
  else if(N_Jets >= 6 and N_BTagsM >= 3){
      """
    rstr+=str(self._fill_vector('ge6j_ge3t'))
    rstr+="""

    //Run graph
    feed_dict.push_back(std::make_pair("dense_1_input",tensor_ge6j_ge3t));"""

    rstr+= self._fix_dropout('ge6j_ge3t')

    rstr+="""status_ge6j_ge3t = session_ge6j_ge3t->Run(feed_dict, {"dense_3/Softmax"},  {}, &outputTensors);
    //if (!status_ge6j_ge3t.ok()) 
    //{
    //  std::cout << status_ge6j_ge3t.ToString() << std::endl;
    //}
    //else
    //{
    //  std::cout << "Success load graph !! " << std::endl;
    //}

    //Feed output into right variables

    DNN_Out_ge6j_ge3t_ttbar2B  = outputTensors.at(0).tensor<float,2>()(0,2);
    DNN_Out_ge6j_ge3t_ttbarB  = outputTensors.at(0).tensor<float,2>()(0,3);
    DNN_Out_ge6j_ge3t_ttbarBB  = outputTensors.at(0).tensor<float,2>()(0,1);
    DNN_Out_ge6j_ge3t_ttbarCC  = outputTensors.at(0).tensor<float,2>()(0,4);
    DNN_Out_ge6j_ge3t_ttbarlf  = outputTensors.at(0).tensor<float,2>()(0,5);
    DNN_Out_ge6j_ge3t_ttH  = outputTensors.at(0).tensor<float,2>()(0,0);
    DNN_ge6j_ge3t_pred_class  = getMaxPosition(outputTensors,num_classes_ge6j_ge3t);

    bool printstuff=0;
    if(iEntry<200){printstuff=1;}
    if(printstuff){
      std::cout<<"-----DNN-----"<<std::endl;
      std::cout<<"jt="<<N_Jets<<" "<<N_BTagsM<< "event "<<Evt_Run<<" "<<Evt_Lumi<<" "<<Evt_ID<<std::endl;
      cout<<"mem "<<memDBp<<std::endl;
     for(int ifeat=0; ifeat<num_features_ge6j_ge3t;ifeat++){
       cout<<tensor_ge6j_ge3t.tensor<float,2>()(0,ifeat)<<std::endl;
       }
      
      cout<<"ttH node "<<DNN_Out_ge6j_ge3t_ttH<<std::endl;
      cout<<"ttbarBB node "<<DNN_Out_ge6j_ge3t_ttbarBB<<std::endl;
      cout<<"ttbar2B node "<<DNN_Out_ge6j_ge3t_ttbar2B<<std::endl;
      cout<<"ttbarB node "<<DNN_Out_ge6j_ge3t_ttbarB<<std::endl;
      cout<<"ttbarCC node "<<DNN_Out_ge6j_ge3t_ttbarCC<<std::endl;
      cout<<"ttbarOther node "<<DNN_Out_ge6j_ge3t_ttbarlf<<std::endl;
      std::cout<<"predicted class "<< DNN_ge6j_ge3t_pred_class<<std::endl;
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
    return rstr
  
  def getCleanUpLines(self):
    rstr=""
    return rstr
  
  def _get_variables_from_csv(self):
  	# Read variables from cvs files. The order of the variables is important for the DNN
  	self.variables_4j_ge3t = []
  	self.means_4j_ge3t = []
  	self.stddev_4j_ge3t = []
  	self.variables_5j_ge3t = []
  	self.means_5j_ge3t = []
  	self.stddev_5j_ge3t = []
  	self.variables_ge6j_ge3t = []
  	self.means_ge6j_ge3t = []
  	self.stddev_ge6j_ge3t = []

  	with open(self.localCheckpointPath+"/4j_ge3t/variable_norm.csv") as csv_file:
  		csv_reader = csv.reader(csv_file,delimiter=',')
  		for i, row in enumerate(csv_reader):
  			if i != 0:
  				# MEM is not named right in CSV, workaround. TODO: Fix name in preprocessing
  				if row[0]=="MEM":
  					self.variables_4j_ge3t.append('memDBp')
  				else:
  					self.variables_4j_ge3t.append(row[0])
  				self.means_4j_ge3t.append(row[1])
  				self.stddev_4j_ge3t.append(row[2])

  	with open(self.localCheckpointPath+"/5j_ge3t/variable_norm.csv") as csv_file:
  		csv_reader = csv.reader(csv_file,delimiter=',')
  		for i, row in enumerate(csv_reader):
  			if i != 0:
  				if row[0]=="MEM":
  					self.variables_5j_ge3t.append('memDBp')
  				else:
  					self.variables_5j_ge3t.append(row[0])
  				self.means_5j_ge3t.append(row[1])
  				self.stddev_5j_ge3t.append(row[2])

  	with open(self.localCheckpointPath+"/ge6j_ge3t/variable_norm.csv") as csv_file:
  		csv_reader = csv.reader(csv_file,delimiter=',')
  		for i, row in enumerate(csv_reader):
  			if i != 0:
  				if row[0]=="MEM":
  					self.variables_ge6j_ge3t.append('memDBp')
  				else:
  					self.variables_ge6j_ge3t.append(row[0])
  				self.means_ge6j_ge3t.append(row[1])
  				self.stddev_ge6j_ge3t.append(row[2])

      
  def _fill_vector(self,cat):
  	# Helper function to fill inputtensors for tensorflow
    master_string= ""
    if cat == '4j_ge3t': 
        for i,value in enumerate(self.variables_4j_ge3t):
            master_string+="tensor_4j_ge3t.tensor<float,2>()(0,"+str(i)+") = float(("+str(value)+"-("+str(self.means_4j_ge3t[i])+"))/"+str(self.stddev_4j_ge3t[i])+"); \n"
        return master_string
    elif cat == '5j_ge3t':
        for i,value in enumerate(self.variables_5j_ge3t):
            master_string+="tensor_5j_ge3t.tensor<float,2>()(0,"+str(i)+") = float(("+str(value)+"-("+str(self.means_5j_ge3t[i])+"))/"+str(self.stddev_5j_ge3t[i])+"); \n"
        return master_string
    elif cat == 'ge6j_ge3t':
        for i,value in enumerate(self.variables_ge6j_ge3t):
            master_string+="tensor_ge6j_ge3t.tensor<float,2>()(0,"+str(i)+") = float(("+str(value)+"-("+str(self.means_ge6j_ge3t[i])+"))/"+str(self.stddev_ge6j_ge3t[i])+"); \n"
            master_string+="//cout<<float(("+str(value)+"-("+str(self.means_ge6j_ge3t[i])+"))/"+str(self.stddev_ge6j_ge3t[i])+")<<std::endl; \n"
            
        return master_string


  def _fix_dropout(self,cat):
  	# Check how many dropout layers are in a model and feed the kepp_pro of 1 -> deactivates dropout

  	# Clear default graph, otherwise old stuff still in the graph
    tensorflow.reset_default_graph()
    master_string = ""
    if cat == '4j_ge3t':
	  sess_1    = tensorflow.Session()
	  saver_1   = tensorflow.train.import_meta_graph(self.localCheckpointPath+'/4j_ge3t/trained_model.meta')
	  saver_1.restore(sess_1, self.localCheckpointPath+'/4j_ge3t/trained_model')
	  graph     = tensorflow.get_default_graph()

    elif cat == '5j_ge3t':
	  sess_2    = tensorflow.Session()
	  saver_2   = tensorflow.train.import_meta_graph(self.localCheckpointPath+'/5j_ge3t/trained_model.meta')
	  saver_2.restore(sess_2, self.localCheckpointPath+'/5j_ge3t/trained_model')
	  graph     = tensorflow.get_default_graph()

    elif cat == 'ge6j_ge3t':
	  sess_1    = tensorflow.Session()
	  saver_1   = tensorflow.train.import_meta_graph(self.localCheckpointPath+'/ge6j_ge3t/trained_model.meta')
	  saver_1.restore(sess_1, self.localCheckpointPath+'/ge6j_ge3t/trained_model')
	  graph     = tensorflow.get_default_graph()

    graph = tensorflow.get_default_graph()
    for op in graph.get_operations():
	  if op.name.find("dropout/keep_prob")!=-1:
	    master_string+="feed_dict.push_back(std::make_pair(\""+op.name + "\", drop_1)); \n"

    return master_string

