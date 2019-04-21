import tensorflow as tf
import csv
import json
import os
import sys
from distutils.dir_util import copy_tree
import glob

includeString = "-I/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/tensorflow-cc/1.3.0-elfike/tensorflow_cc/include -I/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/eigen/c7dc0a897676/include/eigen3 -I/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/protobuf/3.4.0-fmblme/include"
libraryString = "-L/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/tensorflow-cc/1.3.0-elfike/tensorflow_cc/lib -ltensorflow_cc -L/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/protobuf/3.4.0-fmblme/lib -lprotobuf -lrt"

class DNN:
    def __init__(self, cpPath):
        self.path = cpPath

        self.configFile = self.path+"/net_config.json"
        with open(self.configFile) as f:
            self.config = json.loads(f.read())

        self.category = self.config["JetTagCategory"]
        self.selection = self.config["Selection"]
        self.inputLayer = self.config["inputName"]
        self.outputLayer = self.config["outputName"]
        print("category: {}".format(self.category))
        print("selection: {}".format(self.selection))
        print("inputName: {}".format(self.inputLayer))
        print("outputName: {}".format(self.outputLayer))
        
        # collecting variables
        self.variables = []
        self.var_means = []
        self.var_stds  = []
        with open(self.path+"/variable_norm.csv", "r") as cf:
            csv_reader = csv.reader(cf, delimiter = ",")
            for i, row in enumerate(csv_reader):
                if i == 0: continue
                self.variables.append(row[0])
                self.var_means.append(row[1])
                self.var_stds.append( row[2])

        # collection event classes
        classes = self.config["eventClasses"]
        self.out_nodes = []
        for cls in classes:
            self.out_nodes.append(cls["sampleLabel"])

        # generate discriminator names
        self.discrNames = [
            "DNNOutput_{}_node_{}".format(self.category, node)
            for node in self.out_nodes]
        # generate class prediction variable
        self.predictionVariable = "DNNPredictedClass_{}".format(self.category)

    def getBeforeLoopLines(self):
        return """
    // category {cat}
    const string pathToGraph_{cat} = "{path}/trained_model.meta";
    const string checkpointPath_{cat} = "{path}/trained_model";

    auto session_{cat} = NewSession( SessionOptions() );
    if( session_{cat} == nullptr ) {{
        throw runtime_error("Could not create Tensorflow session.");
        }}
    
    Status status_{cat};

    // Read in protobuf we exported
    MetaGraphDef graph_def_{cat};
    status_{cat} = ReadBinaryProto( Env::Default(), pathToGraph_{cat}, &graph_def_{cat});
    if( !status_{cat}.ok() ) {{
        throw runtime_error("Status could not be read");
        }}

    // Add the graph to the session
    status_{cat} = session_{cat}->Create( graph_def_{cat}.graph_def() );
    if( !status_{cat}.ok() ) {{
        throw runtime_error("Error creating graph: "+status_{cat}.ToString());
        }}

    // Read weights from the saved checkpoint
    Tensor checkpointPathTensor_{cat}( DT_STRING, TensorShape() );
    checkpointPathTensor_{cat}.scalar<std::string>()() = checkpointPath_{cat};

    status_{cat} = session_{cat}->Run(
        {{ {{graph_def_{cat}.saver_def().filename_tensor_name(), checkpointPathTensor_{cat} }} }}, 
        {{}}, 
        {{ graph_def_{cat}.saver_def().restore_op_name() }},
        nullptr);

    if( !status_{cat}.ok() ) {{
        throw runtime_error("Error loading checkpoint from "+checkpointPath_{cat}+": "+status_{cat}.ToString());
        }}
    """.format( cat = self.category, path = self.path )

    def getVariableInitInsideEventLoopLines(self):
        string = """
        int num_classes_{cat} = {ncls};
        int num_features_{cat} = {nvars};\n""".format(
            cat = self.category, ncls = len(self.out_nodes), nvars = len(self.variables))
        for discr in self.discrNames:
            string += "        double {} = -6;\n".format(discr)
        string += """
        int {pred_var} = -6;
        Tensor tensor_{cat} (DT_FLOAT, TensorShape( {{1, num_features_{cat}}}));
        """.format(pred_var = self.predictionVariable, cat = self.category)
        return string

    def getEventLoopCodeLines(self, testPrint = False):

        string = """
        if( {selection} ) {{
            // loading data\n""".format(selection = self.selection)

        # fill vector
        for i, var in enumerate(self.variables):
            string += """
            tensor_{cat}.tensor<float,2>()(0,{i}) = float( (({var})-({mean}))/({std}) );""".format(
            cat = self.category, i = i, var = var, mean = self.var_means[i], std = self.var_stds[i])

        # run graph
        string += """
            // run graph
            feed_dict.push_back(std::make_pair("{input}", tensor_{cat}));\n""".format(
            input = self.inputLayer, cat = self.category)
    
        # set dropouts to zero
        string += self.__fixDropout()

        # run graph
        string += """
            status_{cat} = session_{cat}->Run(feed_dict, {{"{output}"}}, {{}}, &outputTensors);
            if( !status_{cat}.ok() ) {{
                std::cout << status_{cat}.ToString() << std::endl; 
                }}

            // feed output into right variables""".format(
            cat = self.category, output = self.outputLayer)
        
        # get outputs
        for i, discr in enumerate(self.discrNames):
            string += """
            {discr} = outputTensors.at(0).tensor<float,2>()(0,{i});""".format(
            discr = discr, i = i)

        # get prediction
        string += """
            {pred_var} = getMaxPosition(outputTensors, {ncls});""".format(
            pred_var = self.predictionVariable, ncls = len(self.out_nodes))

        if testPrint:
            # add test print lines        
            string += """
            if(iEntry < 100) {{
                std::cout << "=========== DNN output ============" << std::endl;
                std::cout << "JT = "<<N_Jets<<" "<<N_BTagsM<< std::endl;
                std::cout << "Event: "<<Evt_Run<<" "<<Evt_Lumi<<" "<<Evt_ID<< std::endl;
                std::cout << "MEM: "<<memDBp<< std::endl;
                for( int ifeat=0; ifeat<num_features_{cat}; ifeat++) {{
                    std::cout << tensor_{cat}.tensor<float,2>()(0,ifeat)<<std::endl;
                    }}

                std::cout << "-----------------------------------" << std::endl;""".format(
                cat = self.category)
            for i, discr in enumerate(self.discrNames):
                string += """
                std::cout << "{discr} " <<{discr}<<std::endl;""".format(
                discr = discr)
            string += """
                std::cout << "predicted class "<<{pred_var}<<std::endl;
                std::cout << "-----------------------------------" << std::endl;
                }}\n""".format(pred_var = self.predictionVariable)

        string += "            }\n"
        return string


    def __fixDropout(self):
        tf.reset_default_graph()
        string = ""
        self.sess = tf.Session()
        self.saver = tf.train.import_meta_graph( self.path+"/trained_model.meta" )
        self.saver.restore( self.sess, self.path+"/trained_model" )
        self.graph = tf.get_default_graph()
        for op in self.graph.get_operations():
            if op.name.find("dropout/keep_prob") != -1:
                string += "            feed_dict.push_back( std::make_pair(\"{name}\", dropout_disable));\n".format(name = op.name)
        return string

class theInterface:
    def __init__(self, workdir = None, dnnSet = None):
        # compile stuff
        self.includeString = includeString
        self.libraryString = libraryString
        self.usesPythonLibraries = True

        if workdir:
            copy_tree(dnnSet, workdir+"/DNNCheckpoints/")
            dnnSet = workdir+"/DNNCheckpoints/"

        self.dnnSet = dnnSet
        if not os.path.exists(self.dnnSet):
            sys.exit("path to DNN set does not exist!")

        # searching for DNN checkpoints in dnnset
        dnnDirs = glob.glob(self.dnnSet+"/*")

        # checking required files
        requirements = ["trained_model.meta", "trained_model.index", 
            "trained_model.data-00000-of-00001", "variable_norm.csv", 
            "checkpoint", "net_config.json"]

        self.DNNs = []
        for dnnDir in dnnDirs:
            errors = False
            for req in requirements:
                if not os.path.exists(dnnDir+"/"+req):
                    errors = True
                    print("file {}/{} missing.".format(dnnDir,req))
            if not errors:
                print("\tAdding DNN {}".format(dnnDir))
                self.DNNs.append(DNN(dnnDir))
        if len(self.DNNs) == 0:
            sys.exit("no suitable DNN checkpoints found")

    def getVariables(self):
        variables = []
        for dnn in self.DNNs:
            variables += dnn.variables
        variables = list(set(variables))
        variables = [v for v in variables if not v == "memDBp"]
        return variables

    def getExternalyCallableVariables(self):
        variables = []
        for dnn in self.DNNs:
            variables += dnn.discrNames
            variables += [dnn.predictionVariable]
        return variables    

    def getBeforeLoopLines(self):
        string = ""
        for dnn in self.DNNs:
            string += dnn.getBeforeLoopLines()
            string += "\n"
        return string

    def getVariableInitInsideEventLoopLines(self):
        string = ""
        for dnn in self.DNNs:
            string += dnn.getVariableInitInsideEventLoopLines()
            string += "\n"
        string += """
            
        std::vector<std::pair<std::string, tensorflow::Tensor>> feed_dict;
        std::vector<tensorflow::Tensor> outputTensors;
        Tensor dropout_disable (DT_FLOAT, TensorShape({1}));
        dropout_disable.tensor<float, 1>()(0) = 1.0;
        """
        return string

    def getEventLoopCodeLines(self):
        string = ""
        for dnn in self.DNNs:
            string += dnn.getEventLoopCodeLines(testPrint = True)
            string += "\n"
        return string


    # setting up C code
    def getIncludeLines(self):
        return """
#include <tensorflow/core/protobuf/meta_graph.pb.h>
#include "tensorflow/core/public/session.h"
#include "tensorflow/cc/framework/ops.h"
#include "tensorflow/core/framework/tensor.h"

// Should be removed for future work
using namespace tensorflow;
"""

    def getAdditionalFunctionDefinitionLines(self):
        return """
int getMaxPosition(std::vector<tensorflow::Tensor> &output, int nClasses) {
    double max_value = -5;
    int max_pos = -1;
    for( int idim=0; idim<nClasses; idim++ ) {
        if( output.at(0).tensor<float,2>()(0,idim)> max_value ) {
            max_value = output.at(0).tensor<float,2>()(0,idim);
            max_pos = idim;
            }
        }
    return max_pos;
    }
"""

    def getTestCallLines(self):
        return ""

    def getCleanUpLines(self):
        return ""

