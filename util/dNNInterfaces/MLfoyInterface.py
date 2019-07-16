import tensorflow as tf
import csv
import json
import os
import sys
from distutils.dir_util import copy_tree
import glob
import pandas as pd
import numpy as np
import ROOT

includeString = "-I/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/tensorflow-cc/1.3.0-elfike/tensorflow_cc/include -I/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/eigen/c7dc0a897676/include/eigen3 -I/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/protobuf/3.4.0-fmblme/include"
libraryString = "-L/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/tensorflow-cc/1.3.0-elfike/tensorflow_cc/lib -ltensorflow_cc -L/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/protobuf/3.4.0-fmblme/lib -lprotobuf -lrt"


def doRebinning(rootfile, histolist, threshold):
    combinedHist = None

    # loop over hists and add them to a combined histogram
    for h in histolist:
        h_tmp = rootfile.Get(h)
        if combinedHist is None:
            combinedHist = h_tmp.Clone("combinedHist")
            combinedHist.Reset()
        combinedHist.Add(h_tmp)

    if combinedHist is None:
        print("ERROR: could not add any histograms!")
        return []

    squaredError = 0.
    binContent = 0.
    bin_edges = []
    last_added_edge = 0
    for i in range(1, combinedHist.GetNbinsX()+1):
        if i == 1:
            last_added_edge = combinedHist.GetBinLowEdge(i)
            bin_edges.append(last_added_edge)

        # add together squared bin errors and bin contents
        squaredError += combinedHist.GetBinError(i)**2
        binContent += combinedHist.GetBinContent(i)

        # calculate relative error
        relerror = squaredError**0.5/binContent if not binContent == 0 else squaredError**0.5
        
        # if relative error is smaller than threshold, start new bin
        if relerror <= threshold and not binContent == 0:
            last_added_edge = combinedHist.GetBinLowEdge(i+1)
            bin_edges.append(last_added_edge)
            squaredError = 0.
            binContent = 0.
    
    
    overflow_edge = combinedHist.GetBinLowEdge(combinedHist.GetNbinsX()+1)
    if not overflow_edge in bin_edges:
        # if overflow_edge is not in bin_edges list the relative
        # error of the last bin is too small, so just merge the
        # last two bins by replacing the last_added_edge with
        # the overflow_edge 
        bin_edges[-1] = overflow_edge

    print("\tnew bin edges: [{}]".format(",".join([str(round(b,4)) for b in bin_edges])))
    return bin_edges


def getOptimizedBinEdges(label, opts):
    channel = opts.discrname+"_"+label

    # open rootfile
    rfile = ROOT.TFile.Open(opts.histogram_file)
    keylist = [x.GetName() for x in rfile.GetListOfKeys()]
    print("\noptimizing bin edges for channel {}".format(channel))

    # collect keys to conider for rebinning
    consider_for_rebinning = []
    for p in opts.considered_processes.split(","):
        branch = p+"_"+channel
        if branch in keylist:
            consider_for_rebinning.append(branch)
        else:
            print("ERROR: Could not find histogram with name {} in inputfile {}".format(
                branch, opts.histogram_file))

    # do the rebinning
    if len(consider_for_rebinning) > 0:
        return doRebinning(
            rootfile  = rfile,
            histolist = consider_for_rebinning,
            threshold = float(opts.threshold))
    else:
        return []





class DNN:
    def __init__(self, cpPath, suffix = "", xEval = True):
        # if dictionary of paths is given initialize multiple DNNs here
        if type(cpPath) == dict:
            self.DNNs       = [DNN(
                    cpPath  = cpPath[key], 
                    suffix  = "_"+key, 
                    xEval   = xEval) 
                    for key in cpPath]
            self.multiDNN   = True
            self.xEval      = xEval
            return

        # structural options
        self.multiDNN   = False
        self.xEval      = xEval
        self.suffix     = suffix
        self.path       = cpPath

        # set evaluation suffix when cross evaluation is 
        # activated and remove the usual suffix
        self.evalSuffix = ""
        if self.xEval:
            self.evalSuffix = self.suffix
            self.suffix = ""

        self.configFile = self.path+"/net_config.json"
        with open(self.configFile) as f:
            self.config = json.loads(f.read())

        if "binaryConfig" in self.config:
            print("    BINARY DNN")

        self.category       = self.config["JetTagCategory"]+self.suffix
        self.label          = self.config["categoryLabel"]
        self.selection      = self.config["Selection"]
        self.evalSelection  = "&&("+self.config["evalSelection"]+")"
        self.inputLayer     = self.config["inputName"]
        self.outputLayer    = self.config["outputName"]
        print("    category: {}".format(self.category))
        print("    selection: {}{}".format(self.selection, self.evalSelection))
        print("    inputName: {}".format(self.inputLayer))
        print("    outputName: {}".format(self.outputLayer))
        
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

        if not "binaryConfig" in self.config:
            # collecting event classes
            classes = self.config["eventClasses"]
            self.out_nodes = []
            self.node_mins = []
            self.node_maxs = []
            for cls in classes:

                # save names of output nodes
                self.out_nodes.append(cls["sampleLabel"])

                # save min and max values of output nodes
                if "min" in cls and "max" in cls:
                    self.node_mins.append(cls["min"])
                    self.node_maxs.append(cls["max"])
                else:
                    print("\tdid not find plotrange for discriminator {} - setting it to [0.,1.]".format(cls["sampleLabel"]))
                    self.node_mins.append(0.)
                    self.node_maxs.append(1.)

            # generate discriminator names
            self.discrNames = [
                "DNNOutput_{}_node_{}".format(self.category, node)
                for node in self.out_nodes]
            # generate class prediction variable
            self.predictionVariable = "DNNPredictedClass_{}".format(self.category)
        else:
            self.out_nodes = ["binary"]
            self.node_mins = [self.config["binaryConfig"]["minValue"]]
            self.node_maxs = [self.config["binaryConfig"]["maxValue"]]
            self.discrNames = ["DNNOutput_{}".format(self.category)]
            self.predictionVariable = "DNNPredictedClass_{}".format(self.category)

    def getVariables(self):
        if self.multiDNN:
            variables = []
            for dnn in self.DNNs:
                variables += dnn.getVariables()
            variables = list(set(variables))
            return variables

        return self.variables

    def getExternalVariables(self):
        if self.multiDNN:
            variables = []
            for dnn in self.DNNs:
                variables += dnn.getExternalVariables()
            variables = list(set(variables))
            return variables

        return self.discrNames + [self.predictionVariable]


    def getBeforeLoopLines(self):
        if self.multiDNN:
            string = ""
            for dnn in self.DNNs:
                string += dnn.getBeforeLoopLines()
                string += "\n"
            return string

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
        """.format( cat = self.category+self.evalSuffix, path = self.path )
        

    def getVariableInitInsideEventLoopLines(self):
        if self.multiDNN:
            string = ""
            for dnn in self.DNNs:
                string += dnn.getVariableInitInsideEventLoopLines()
                string += "\n"
                if self.xEval: break
            return string

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
        if self.multiDNN:
            string = ""
            for dnn in self.DNNs:
                string += dnn.getEventLoopCodeLines(testPrint)
            return string

        string = """
        if( {selection} ) {{
            // initialize tensors 
            std::vector<std::pair<std::string, tensorflow::Tensor>> feed_dict;
            std::vector<tensorflow::Tensor> outputTensors;

            // loading data\n""".format(selection = self.selection.replace(" and ","&&")+self.evalSelection)

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
            cat = self.category+self.evalSuffix, output = self.outputLayer)
        
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
            if(iEntry < 100) {
                std::cout << "=========== DNN output ============" << std::endl;
                std::cout << "JT = "<<N_Jets<<" "<<N_BTagsM<< std::endl;
                std::cout << "Event: "<<Evt_Run<<" "<<Evt_Lumi<<" "<<Evt_ID<< std::endl;"""
            if "memDBp" in self.variables:
                string+="\n                std::cout << \"MEM: \"<<memDBp<< std::endl;\n"
            string += """
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


    def generateInputPlots(self):
        if self.multiDNN:
            string = ""
            for dnn in self.DNNs:
                string += dnn.generateInputPlots()
                string += "\n"
                # only read one set of input plots if cross evaluation activated
                if self.xEval: break
            return string

        # loading plot config csv
        csv_path = self.path+"/plot_config.csv"
        if not os.path.exists(csv_path):
            print("no plot config for DNN {}\n\tnot adding any input plots.".format(self.path))
            return "    plots = []\n"
        
        # read variable set
        variables = pd.read_csv(csv_path, sep = ",").set_index("variablename", drop = True)

        # generate header
        string = "def plots_{}(data = None):\n".format(self.category)
        string+= "    label = \"{}\"\n".format(self.label)
        if self.xEval:
            string+= "    selection = \"{}\"\n\n".format(self.selection.replace(" ","").replace("and","&&"))
        else:
            string+= "    selection = \"{}\"\n\n".format(self.selection.replace(" ","").replace("and","&&")+self.evalSelection)
        string+= "    plots = ["

        for var in list(variables.index):
            # generate dictionary
            plotConfig = {
                "histname":     "\""+self.category+"_"+var+"\"", 
                "plotname":     "\""+variables.loc[var, "displayname"]+"\"",
                "nbins":        variables.loc[var, "numberofbins"],
                "minval":       variables.loc[var, "minvalue"],
                "maxval":       variables.loc[var, "maxvalue"],
                "expression":   "\""+var+"\""}
            
            # var[1]->var_1 renaming
            plotConfig["histname"] = plotConfig["histname"].replace("[","_").replace("]","")

            # special case: MEM
            if var == "memDBp": plotConfig["expression"] = "memexp"

            # generate the plot string
            string += """
        plotClasses.Plot(ROOT.TH1D({histname},{plotname},{nbins},{minval},{maxval}),{expression},selection,label),""".format(**plotConfig)

        string += "\n        ]\n\n"
        string += "    if data:\n"
        string += "        add_data_plots(plots=plots,data=data)\n"
        string += "    return plots\n\n\n\n"
        return string
    
    def generatePlotCall(self, opts):
        if self.multiDNN:
            string = ""
            for dnn in self.DNNs:
                string += dnn.generatePlotCall(opts)
                if self.xEval: break
            return string

        string = "    "
        if not opts.input_plots:
            string+= "#"
        string += "discriminatorPlots += plots_{}(data)\n".format(self.category)
        return string
   

    def generateOutputPlots(self, opts):
        if self.multiDNN:
            string = ""
            for dnn in self.DNNs:
                string += dnn.generateOutputPlots(opts)
                if self.xEval: break
            return string

        # generate categoires list
        string = "\n\n\n    # plots for {}\n".format(self.category)
        template ="""
    category_dict["category"] = ("{PRESELECTION}","{LABEL}","")
    category_dict["discr"] = "{DISCR_NAME}"
    category_dict["catlabel"] = "{CATLABEL}"
    category_dict["nhistobins"] = ndefaultbins\n"""



        for i, node in enumerate(self.out_nodes):
            label = "ljets_{cat}_{node}_node".format(cat = self.category, node = node)

            if self.xEval:
                preselection = "({sel}&&({pred_var}=={i}))".format(
                    sel         = self.selection.replace(" ","").replace("and","&&"), 
                    pred_var    = self.predictionVariable, 
                    i           = i)
            else:
                preselection = "({sel}&&({pred_var}=={i}))".format(
                    sel         = self.selection.replace(" ","").replace("and","&&")+self.evalSelection, 
                    pred_var    = self.predictionVariable, 
                    i           = i)
                

            string += template.format(  
                PRESELECTION    = preselection,
                LABEL           = label,
                CATLABEL        = self.label,
                DISCR_NAME      = self.discrNames[i])

            if opts.variable_binning or opts.optimize_binning:
                if opts.optimize_binning:
                    # generate optimized bin edges
                    bin_edges = getOptimizedBinEdges(label, opts)
                elif not opts.ndefaultbins is None:
                    # generate default bin edges
                    bin_edges = np.linspace(self.node_mins[i], self.node_maxs[i], opts.ndefaultbins, dtype = float)
                    delta = (bin_edges[1] - bin_edges[0])/2.
                    nextval = bin_edges[-1] + delta
                    bin_edges = np.concatenate([bin_edges, [nextval]])
                    #shift values to get lower edges
                    bin_edges -= delta
                else:
                    print("WARNING: variable binning is required, but there is no information about the binning!")
                    bin_edges = []

                # write bin edges to file
                indents = "\t\t\t\t"
                separator = ",\n"+indents
                string += '    category_dict["bin_edges"] = [ \n{}{}\n{}]'.format(
                    indents,
                    separator.join([str(round(x,4)) for x in bin_edges]),
                    indents
                    )
                
            else:
                # fill binranges
                string += '    category_dict["minxval"] = {}\n'.format(self.node_mins[i])
                string += '    category_dict["maxxval"] = {}\n'.format(self.node_maxs[i])
                # string += "\n\n"

            string += """
    this_dict["{LABEL}"] = deepcopy(category_dict)
    category_dict.clear()
    """.format(LABEL=label)
        return string




class theInterface:
    def __init__(self, workdir = None, dnnSet = None, crossEvaluation = True):
        # compile stuff
        self.includeString = includeString
        self.libraryString = libraryString
        self.usesPythonLibraries = True
        self.xEval = crossEvaluation

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
            dnnDict = {}
            # check if there are subdirectories 
            subDirs = glob.glob(dnnDir+"/*")
            for subDir in subDirs:
                if not os.path.isdir(subDir): continue
                # append subdir to dnnDict
                dnnDict[os.path.basename(subDir)] = subDir

            # if no subdirectories were found there is 
            # only one DNN to be evaluated, so add it 
            # to the dnnDict 
            if len(dnnDict) == 0:
                dnnDict[os.path.basename(dnnDir)] = dnnDir

            # now loop over all dnnDicts and find files
            errors = False
            for key in dnnDict:
                for req in requirements:
                    if not os.path.exists(dnnDict[key]+"/"+req):
                        errors = True
                        print("file {}/{} missing.".format(dnnDict[key],req))

            if not errors:
                if len(dnnDict) == 1:
                    self.DNNs.append(DNN(dnnDict[dnnDict.keys()[0]], xEval = self.xEval))
                else:
                    self.DNNs.append(DNN(dnnDict, xEval = self.xEval))
            if len(self.DNNs) == 0:
                sys.exit("no suitable DNN checkpoints found")

    def getVariables(self):
        variables = []
        for dnn in self.DNNs:
            variables += dnn.getVariables()
        variables = list(set(variables))
        variables = [v for v in variables if not v == "memDBp"]
        return variables

    def getExternalyCallableVariables(self):
        variables = []
        for dnn in self.DNNs:
            variables += dnn.getExternalVariables()
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

    def generatePlotConfig(self, opts):
        '''
        generate plot config from variables and plots in checkpoint files
        '''

        # header
        string = """
import sys
import os
filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = os.path.dirname(filedir)
basedir = os.path.dirname(pyrootdir)
sys.path.append(pyrootdir)
sys.path.append(basedir)

import util.tools.plotClasses as plotClasses
import ROOT
from array import array
from copy import deepcopy\n\n\n"""

        # get event yield categories
        string += """
def evtYieldCategories():
    return [
    ("(N_Jets>=6&&N_BTagsM==2)","6j2t",""),
    ("(N_Jets==4&&N_BTagsM==3)","4j3t",""),
    ("(N_Jets==5&&N_BTagsM==3)","5j3t",""),
    ("(N_Jets>=6&&N_BTagsM==3)","6j3t",""),
    ("(N_Jets==4&&N_BTagsM>=4)","4j4t",""),
    ("(N_Jets==5&&N_BTagsM>=4)","5j4t",""),
    ("(N_Jets>=6&&N_BTagsM>=4)","6j4t","")
    ]

memexp = ""\n\n\n"""

        # header for discr plots function
        funcstring = "def getDiscriminatorPlots(data = None, discrname = ''):\n"
        funcstring +="    discriminatorPlots = []\n"

        # loop over dnns writing code for plots
        for dnn in self.DNNs:
            string += dnn.generateInputPlots()
            funcstring += dnn.generatePlotCall(opts)


        # writing code for dnn output plots
        string += """
def plots_dnn(data, discrname):

    ndefaultbins = {}
    category_dict = {{}}
    this_dict = {{}}\n\n""".format(opts.ndefaultbins)


        # loop over dnns witing code for DNN discr plots
        for dnn in self.DNNs:
            string += dnn.generateOutputPlots(opts)

        # generating plot classes for DNN plots and adding info to data class
        string += """

    for l in this_dict:
        this_dict[l]["histoname"] = discrname+"_"+l
        this_dict[l]["histotitle"] = "final discriminator ({})".format(l)
        this_dict[l]["plotPreselections"] = this_dict[l]["category"][0]

    DNNPlots = init_plots(dictionary = this_dict, data = data)
    return DNNPlots\n\n\n"""

        string += funcstring
        string += "    discriminatorPlots += plots_dnn(data, discrname)\n\n"
        string += "    return discriminatorPlots\n\n"
        string += self.generateInitPlotsFunc()

        return string

    def generateInitPlotsFunc(self):
        code ="""
def init_plots(dictionary, data = None):
    plots = [] #init list of plotClasses objects to return
    for label in dictionary:
        subdict     = dictionary[label] #for easy access
        discr       = subdict["discr"] # load discriminator name
        sel         = subdict["plotPreselections"] # load selection
        histoname   = subdict["histoname"] # load histogram name
        histotitle  = subdict["histotitle"] # load histogram title
        catlabel    = subdict["catlabel"] # category label

        # check if initialization uses bin edges or min/max vals
        # if 'subdict' contains the keyword 'bin_edges', an array
        # of type float is created from the corresponding python list.
        # Else, the min/maxvals are used 
        if "bin_edges" in subdict:
            bins  = array("f", subdict["bin_edges"])
            nbins = len(bins)-1 # last bin edge in array is overflow bin => subtract for nbins
            subdict["nhistobins"] = nbins # update number of bins
            plots.append(
                plotClasses.Plot(
                    ROOT.TH1F(histoname,histotitle,nbins,bins),
                    discr,sel,catlabel))

        elif "minxval" in subdict and "maxxval" in subdict:
            nbins = subdict["nhistobins"]
            xmax  = subdict["maxxval"]
            xmin  = subdict["minxval"]
            plots.append(
                plotClasses.Plot(
                    ROOT.TH1F(histoname, histotitle,nbins,xmin, xmax),
                    discr,sel,catlabel))

    if not data is None:
        data.categories.update(dictionary)

    return plots

def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
    """
        return code


if __name__ == "__main__":
    import optparse
    parser = optparse.OptionParser()
    
    
    parser.add_option("-c","--checkpoints",dest="checkpoints",default=None,metavar="CHECKPOINTS",
        help = "path to DNN checkpoints")
    parser.add_option("-o","--output",dest="output",default="autogenerated_plotconfig.py",metavar="OUTPUT",
        help = "output file")
    parser.add_option("--disableplots", dest="input_plots",default=True,action="store_false",metavar="DISABLEPLOTS",
        help = "disable plotting of input features as default setting")
    parser.add_option("-n", "--ndefaultbins", dest="ndefaultbins",default=15,metavar="NDEFAULTBINS",
        help = "number of default bins per discriminator")
    parser.add_option("-v", "--variableBinning", dest = "variable_binning", action = "store_true", default = False,
        help = """enable variable binning (currently only for discriminator distributions. 
The config will contain lists of bin edges which are equally spaced by default.""")
    parser.add_option("-x", "--crossEvaluation", dest = "crossEvaluation", action = "store_true", default = False,
        help = """enable cross evaluation of multi DNN structures.
The usual structure of DNN checkpoint files is a folder containing
one subfolder per evaluated DNN containing the corresponding checkpoint files.
If this subfolder again contains multiple subfolders with checkpoint files these
are evaluated as separate DNNs. If the crossEvaluation flag is activated
no separate plots and no separate discriminators are produced""")

    binningOptions = optparse.OptionGroup(parser, "binning Options", description = 
        "settings concerning the variable binning of discriminator plots")
    binningOptions.add_option("--optimizeBinning",dest="optimize_binning",default=False,action="store_true",metavar="OPTBINNING",
        help = "enable optimization of binning. Requires some additional input information from already produced output plots")
    binningOptions.add_option("-f",dest="histogram_file",default="output_limitInput.root",metavar="HISTFILE",
        help = "root file with histograms for binning optimization")
    binningOptions.add_option("-p",dest="considered_processes",default="ttbarOther,ttbarPlusB,ttbarPlus2B,ttbarPlusBBbar,ttbarPlusCCbar",metavar="PROCESSES",
        help = "comma separated list of processes to be considered during at the binning optimization")
    binningOptions.add_option("-t",dest="threshold",default=0.1,metavar="THRESHOLD",
        help = "relative stat uncertainty threshold for binning optimization")
    binningOptions.add_option("-d",dest="discrname",default="finaldiscr",
        help = "name of discriminator in histogram file for binning optimization")

    parser.add_option_group(binningOptions)
    (opts, args) = parser.parse_args()

    if not opts.checkpoints:
        parser.error("need to specify path to checkpoints")


    interface = theInterface(dnnSet = opts.checkpoints, crossEvaluation = opts.crossEvaluation)
    cfg_string = interface.generatePlotConfig(opts)
    with open(opts.output, "w") as f:
        f.write(cfg_string)
    print("\n\nwrite new plot config to {}".format(opts.output))    







