import tensorflow
import csv
import json
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
    
    # define categories
    self.categories = ["4j_ge3t", "5j_ge3t", "ge6j_ge3t"]
    self.categorySelection = {
        "4j_ge3t":      "N_Jets == 4 and N_BTagsM >= 3",
        "5j_ge3t":      "N_Jets == 5 and N_BTagsM >= 3",
        "ge6j_ge3t":    "N_Jets >= 6 and N_BTagsM >= 3"}

    self.__loadCheckpoints()
    self.__getVariables()

  def __loadCheckpoints(self):
    # generate directory
    self.localCheckpointPath = self.workdir + "/DNNCheckpoints/"
    if not os.path.exists(self.localCheckpointPath):
        os.makedirs(self.localCheckpointPath)

    # copy directory with checkpoint files
    copy_tree(self.DNNCheckpointLocation, self.localCheckpointPath)
    print("copied DNN checkpoint files to "+str(self.localCheckpointPath))

    # check if all files are present
    print("checking structure of checkpoint files...")
    files = ["trained_model.meta", "trained_model.index", "trained_model.data-00000-of-00001", 
            "variable_norm.csv", "checkpoint", "net_config.json"
            ]
    errors = False
    for cat in self.categories:
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

    if errors:  exit("... not all neccesary files found for dnn loading")
    else:       print("... all files found.")

    # get input and output layer names from config files
    self.inputLayers = {}
    self.outputLayers = {}
    for cat in self.categories:
        config_file = self.localCheckpointPath+"/"+cat+"/net_config.json"
        with open(config_file, "r") as jf:
            configs = json.load(jf)

        self.inputLayers[cat] = configs["inputName"]
        self.outputLayers[cat] = configs["outputName"]
        print("set inputLayer name for "+cat+" to "+configs["inputName"])
        print("set outputLayer name for "+cat+" to "+configs["outputName"])


  def __getVariables(self):
  	# Read variables from cvs files. The order of the variables is important for the DNN
    self.variables = {}
    self.variable_means = {}
    self.variable_stds = {}
    for cat in self.categories:
        variables = []
        means = []
        stds = []
        with open(self.localCheckpointPath+"/"+cat+"/variable_norm.csv", "r") as cf:
            csv_reader = csv.reader(cf, delimiter = ",")
            for i, row in enumerate(csv_reader):
                if i == 0: continue
                # rename mem (called 'MEM' in file, should be called 'memDBp'
                if row[0] == "MEM": variables.append("memDBp")
                else:               variables.append(row[0])
                means.append(row[1])
                stds.append( row[2])
        self.variables[cat] = variables
        self.variable_means[cat] = means
        self.variable_stds[cat] = stds




  def getExternalyCallableVariables(self):
    variables = []
    for cat in self.categories:
        variables += [
            "DNN_Out_"+cat+"_ttbar2B",
            "DNN_Out_"+cat+"_ttbarB",
            "DNN_Out_"+cat+"_ttbarBB",
            "DNN_Out_"+cat+"_ttbarCC",
            "DNN_Out_"+cat+"_ttbarlf",
            "DNN_Out_"+cat+"_ttH",
            "DNN_"+cat+"_pred_class",
            ]
    return variables 

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

    rstr = ""
    for cat in self.categories:
        rstr += "    //"+cat+" category\n"
        rstr += "    const string pathToGraph_"+cat+" = \""+str(self.localCheckpointPath)+"/"+cat+"/trained_model.meta\";\n"
        rstr += "    const string checkpointPath_"+cat+" = \""+str(self.localCheckpointPath)+"/"+cat+"/trained_model\";\n\n"

        rstr += "    auto session_"+cat+" = NewSession(SessionOptions());\n"
        rstr += "    if (session_"+cat+" == nullptr) {throw runtime_error(\"Could not create Tensorflow session.\");}\n"
        rstr += "    Status status_"+cat+";\n"

        rstr += "    // Read in the protobuf graph we exported\n"
        rstr += "    MetaGraphDef graph_def_"+cat+";\n"
        rstr += "    status_"+cat+" = ReadBinaryProto(Env::Default(), pathToGraph_"+cat+", &graph_def_"+cat+");\n"
        rstr += "    if (!status_"+cat+".ok()) {throw runtime_error(\"status could not be read\");}\n"

        rstr += "    // Add the graph to the session\n"
        rstr += "    status_"+cat+" = session_"+cat+"->Create(graph_def_"+cat+".graph_def());\n"
        rstr += "    if (!status_"+cat+".ok()) {throw runtime_error(\"Error creating graph: \" + status_"+cat+".ToString());}\n"

        rstr += "    // Read weights from the saved checkpoint\n"
        rstr += "    Tensor checkpointPathTensor_"+cat+"(DT_STRING, TensorShape());\n"
        rstr += "    checkpointPathTensor_"+cat+".scalar<std::string>()() = checkpointPath_"+cat+";\n"
        rstr += "    status_"+cat+" = session_"+cat+"->Run(\n"
        rstr += "        {{graph_def_"+cat+".saver_def().filename_tensor_name(), checkpointPathTensor_"+cat+" },},{},\n"
        rstr += "        {graph_def_"+cat+".saver_def().restore_op_name()}, nullptr);\n"
        rstr += "    if (!status_"+cat+".ok()) {throw runtime_error(\"Error loading checkpoint from \" + checkpointPath_"+cat+" +\": \"+ status_"+cat+".ToString());}\n" 

    return rstr

  def getVariableInitInsideEventLoopLines(self):
    rstr = "       // variables for DNNs\n"
    for cat in self.categories:
        rstr += "        int num_classes_"+cat+" = 6;\n"
        rstr += "        int num_features_"+cat+" = "+str(len(self.variables[cat]))+";\n"
        rstr += "        double DNN_Out_"+cat+"_ttbar2B = -6;\n"
        rstr += "        double DNN_Out_"+cat+"_ttbarB  = -6;\n"
        rstr += "        double DNN_Out_"+cat+"_ttbarBB = -6;\n"
        rstr += "        double DNN_Out_"+cat+"_ttbarCC = -6;\n"
        rstr += "        double DNN_Out_"+cat+"_ttbarlf = -6;\n"
        rstr += "        double DNN_Out_"+cat+"_ttH     = -6;\n"
        rstr += "        int DNN_"+cat+"_pred_class     = -6;\n\n"
        rstr += "        Tensor tensor_"+cat+" (DT_FLOAT, TensorShape({1, num_features_"+cat+"}));\n\n"
    
    rstr += "        std::vector<std::pair<std::string, tensorflow::Tensor>> feed_dict;\n"
    rstr += "        std::vector<tensorflow::Tensor> outputTensors;\n"
    rstr += "        Tensor drop_1 (DT_FLOAT, TensorShape({1}));\n"
    rstr += "        drop_1.tensor<float, 1>()(0) = 1.0;\n"       
    return rstr
  
  def getEventLoopCodeLines(self):
    rstr = """ 
        // classes are 
        // 0 = ttH 
        // 1 = ttbb 
        // 2 = tt2b 
        // 3 = ttb 
        // 4 = ttcc 
        // 5 = ttlf
        //std::cout<<N_Jets<<" "<<N_BTagsM<<std::endl;
    """
    for i, cat in enumerate(self.categories):
        if i == 0:
            rstr += "        if( "+self.categorySelection[cat]+" ){\n"
        else:
            rstr += "        else if( "+self.categorySelection[cat]+" ){\n"
            
        rstr += "        // Loading Data\n"
        rstr += self.__fillVector(cat)
        rstr += "        // Run graph\n"
        rstr += "        feed_dict.push_back(std::make_pair(\""+self.inputLayers[cat]+"\", tensor_"+cat+"));\n"
        rstr += self.__fixDropout(cat)
        rstr += "        status_"+cat+" = session_"+cat+"->Run(feed_dict, {\""+self.outputLayers[cat]+"\"}, {}, &outputTensors);\n\n"
        rstr += "        if( !status_"+cat+".ok()){ std::cout << status_"+cat+".ToString() << std::endl; }\n"
        rstr += "        //else { std::cout << \"Graph loaded\" << std::endl; }\n\n"
        rstr += "        // Feed output into right variables\n"
        rstr += "        DNN_Out_"+cat+"_ttH     = outputTensors.at(0).tensor<float,2>()(0,0);\n"
        rstr += "        DNN_Out_"+cat+"_ttbarBB = outputTensors.at(0).tensor<float,2>()(0,1);\n"
        rstr += "        DNN_Out_"+cat+"_ttbar2B = outputTensors.at(0).tensor<float,2>()(0,2);\n"
        rstr += "        DNN_Out_"+cat+"_ttbarB  = outputTensors.at(0).tensor<float,2>()(0,3);\n"
        rstr += "        DNN_Out_"+cat+"_ttbarCC = outputTensors.at(0).tensor<float,2>()(0,4);\n"
        rstr += "        DNN_Out_"+cat+"_ttbarlf = outputTensors.at(0).tensor<float,2>()(0,5);\n"
        rstr += "        DNN_"+cat+"_pred_class  = getMaxPosition(outputTensors, num_classes_"+cat+");\n\n"
        rstr += "        bool printstuff = 0;\n"
        rstr += "        if(iEntry < 100){ printstuff = 1; }\n"
        rstr += "        if( printstuff ){\n"
        rstr += "            std::cout << \"========== DNN output ==========\" << std::endl;\n"
        rstr += "            std::cout << \"JT  = \"<<N_Jets<<\" \"<<N_BTagsM<<\"; Event: \"<<Evt_Run<<\" \"<<Evt_Lumi<<\" \"<<Evt_ID<<std::endl;\n"
        rstr += "            std::cout << \"MEM = \"<<memDBp<<std::endl;\n\n"
        rstr += "            for( int ifeat=0; ifeat<num_features_"+cat+"; ifeat++){\n"
        rstr += "                std::cout << tensor_"+cat+".tensor<float,2>()(0,ifeat)<<std::endl;}\n"
        rstr += "            std::cout << \"-------------------->\"<<std::endl;\n"
        rstr += "            std::cout << \"ttH node        \"<<DNN_Out_"+cat+"_ttH<<std::endl;\n"      
        rstr += "            std::cout << \"ttbarBB node    \"<<DNN_Out_"+cat+"_ttbarBB<<std::endl;\n"      
        rstr += "            std::cout << \"ttbar2B node    \"<<DNN_Out_"+cat+"_ttbar2B<<std::endl;\n"      
        rstr += "            std::cout << \"ttbarB node     \"<<DNN_Out_"+cat+"_ttbarB<<std::endl;\n"      
        rstr += "            std::cout << \"ttbarCC node    \"<<DNN_Out_"+cat+"_ttbarCC<<std::endl;\n"      
        rstr += "            std::cout << \"ttbarOther node \"<<DNN_Out_"+cat+"_ttbarlf<<std::endl;\n\n"
        rstr += "            std::cout << \"predicted class \"<<DNN_"+cat+"_pred_class<<std::endl;\n"
        rstr += "            std::cout << \"-------------------->\"<<std::endl;\n"
        rstr += "            }\n"
        rstr += "        }\n"      

    return rstr

  def getTestCallLines(self):
    rstr=""  
    return rstr
  
  def getCleanUpLines(self):
    rstr=""
    return rstr
  
      
  def __fillVector(self, cat):
  	# Helper function to fill inputtensors for tensorflow
    rstr = ""
    for i, var in enumerate(self.variables[cat]):
        rstr += "        tensor_"+cat+".tensor<float,2>()(0,"+str(i)+") = "
        rstr += "float( (("+var+")-("+str(self.variable_means[cat][i])+"))/("+str(self.variable_stds[cat][i])+") );\n"
    return rstr


  def __fixDropout(self, cat):
  	# Check how many dropout layers are in a model 
    # and feed them a keep probability of 1 -> deactivates dropout

  	# Clear default graph, otherwise old stuff still in the graph
    tensorflow.reset_default_graph()
    rstr = ""
    session = {}
    saver = {}

    session[cat] = tensorflow.Session()
    saver[cat] = tensorflow.train.import_meta_graph( self.localCheckpointPath+"/"+cat+"/trained_model.meta" )
    saver[cat].restore( session[cat], self.localCheckpointPath+"/"+cat+"/trained_model" )
    graph = tensorflow.get_default_graph()
    for op in graph.get_operations():
	    if op.name.find("dropout/keep_prob") != -1:
	      rstr += "        feed_dict.push_back(std::make_pair(\""+op.name+"\", drop_1));\n"

    return rstr

