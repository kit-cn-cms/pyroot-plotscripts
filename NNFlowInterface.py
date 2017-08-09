# this class describes the interface to the DNN interface to be used in the scriptgenerator
# This class can be used to load a Tensorflow model obtained by making use of the NNFlow framework

# There are several methods which you will need to update for your own classifier 
# Then use the interface by passing THIS file path to the plotparallel function

import sys

class theInterface:
  
  def __init__(self):
    """Init function sets same default path and variables, which can modified by setter functions"""
    
    # path to include in the search for header files. This is probably the src CMSSW directory where you installed the CommonClassifier
    self.includeString="-I/nfs/dust/cms/user/mharrend/gitlab-ci/CMSSW_8_0_26_patch2/src"
    # precompiled library path and libraries to be included
    self.libraryString="-L/nfs/dust/cms/user/mharrend/gitlab-ci/CMSSW_8_0_26_patch2/lib/slc6_amd64_gcc530 -lDNNBase -lDNNTensorflow"
    # if the following is true, the g++ compiler will also link the python libraries. You probably need this if you use Tensorflow
    self.usesPythonLibraries=True
    
    # Full path to the folder containing the  Tensorflow model, the code assumes that the inputVariables.txt and the outputLables.txt file are in the subfolder model_properties.
    self.modelFolderPath = "/nfs/dust/cms/user/mharrend/doktorarbeit/tensorflowModels/multiclass_ttlight_ttcc_ttb_tt2b_ttbb_ttH/model"
    # Name of the Tensorflow model
    self.modelName = "multiclass_ttlight_ttcc_ttb_tt2b_ttbb_ttH.ckpt"
   
    # Print out debug output if true
    self.debugOutput = False
   
    ## internal variables
    # List contains input variables
    self.inputVariablesList = []
    # List contains output labels names and additional tf_class variable
    self.outputLabelsList = []
    
    # List contains information about preselection
    self.preselectionList = []
    
    # Lists contain information for unit test
    self.unitTestInputValuesList = []
    self.unitTestOutputValuesList = []
    
    
    # Make sure, update function gets called before interface is used by using a dedicated bool variable
    self.updateFunctionCalled = False
    
    
  def update(self):
    """ Function updates class object, necessary to update e.g. self.inputvariablesList list """
    self.updateFunctionCalled = True
    
    # Update / read input variable list, the assumption is that the file is located under self.modelFolderPath/model_properties/inputVariables.txt
    inputVariablesListLoc = self.modelFolderPath + '/model_properties/inputVariables.txt'
    if(self.debugOutput)
      print "Update function: Start reading input variables list file: ", inputVariablesListLoc
    self.inputVariablesList = readListFromFile(inputVariablesListLoc)
    
    # Update / read output labels list, the assumption is that the file is located under self.modelFolderPath/model_properties/outputLabels.txt
    outputLabelsListLoc = self.modelFolderPath + '/model_properties/outputLabels.txt'
    if(self.debugOutput)
      print "Update function: Start reading output labels list file: ", outputLabelsListLoc
    self.outputLabelList = readListFromFile(outputLabelsListLoc)
    # Add tf_class variable to list
    self.outputLabelList.append('tf_class')
  
    # Update / read preselection list, the assumption is that the file is located under self.modelFolderPath/model_properties/preselection.txt
    preselectionListLoc = self.modelFolderPath + '/model_properties/preselection.txt'
    if(self.debugOutput)
      print "Update function: Start reading preselection list file: ", preselectionListLoc
    self.preselectionList = readListFromFile(preselectionListLoc)
  
    # Update / read unitTest input values list, the assumption is that the file is located under self.modelFolderPath/model_properties/unitTestInputValues.txt
    unitTestInputValuesListLoc = self.modelFolderPath + '/model_properties/unitTestInputValues.txt'
    if(self.debugOutput)
      print "Update function: Start reading unitTest input values list file: ", unitTestInputValuesListLoc
    self.unitTestInputValuesList = readListFromFile(unitTestInputValuesListLoc)
  
    # Update / read unitTest output values list, the assumption is that the file is located under self.modelFolderPath/model_properties/unitTestOutputValues.txt
    unitTestOutputValuesListLoc = self.modelFolderPath + '/model_properties/unitTestOutputValues.txt'
    if(self.debugOutput)
      print "Update function: Start reading unitTest output values list file: ", unitTestOutputValuesListLoc
    self.unitTestOutputValuesList = readListFromFile(unitTestOutputValuesListLoc)
  
  ## Setter functions
  
  def setModelFolderPath(self, folderString):
    self.modelFolderPath = str(folderString)
    print "Set model folder path to: ", self.modelFolderPath

  def setModelName(self, nameString):
    self.modelName = str(nameString)
    print "Set model name to: ", self.modelName
    
  def setIncludeString(self, includeString):
    self.includeString = str(includeString)
    print "Set include string to: ", self.includeString
    
  def setLibraryString(self, libraryString):
    self.libraryString = str(libraryString)
    print "Set library string to: ", self.libraryString

  def setDebugOutput(self, activateDebugOutput):
    self.debugOutput = bool(activateDebugOutput)
    print "Set debug output to: ", self.debugOutput


  ## Helper functions

  def readListFromFile(self, fileLocation):
    """Helper function reads a list with e.g. input variable names or output node name from a file
    Returns: String list
    """
    tempList = []
    
    try:
      with open(fileLocation, 'r') as file:
        fileContent = file.read().splitlines()
        
    except IOError:
      print "Could not read file:", fileLocation
      sys.exit()
  
    for singleContent in fileContent:
      # Make sure that lines does not only consists of whitespace or line break characters
      if(not bool(not singleContent or singleContent.isspace())):
        tempList.append(singleContent)
    
    if(self.debugOutput):
      print "\n readListFromFile function read file: ", fileLocation
      print "List obtained from file:\n", tempList
    
    return tempList
  

  
  
  ## Interface functions
 
  def getExternalyCallableVariables(self):
    """This is a list of variables which should be visible for the plotscript.
    You also need to define them in the getVariableInitLines method
    """
    
    if(!self.updateFunctionCalled)
      self.update()
    
    return self.outputLabelsList
    
  
  def getIncludeLines(self):
    """Write here the code with the include statements
    DNN header is relative to CMSSW BASE
    """
    
    if(!self.updateFunctionCalled)
      self.update()
    
    retstr="""
    #include <iostream>
    #include <fstream>
    #include <string>
    #include <vector>
    #include <exception> 

    #include "DNN/Tensorflow/interface/tfModelUser.h"
    """
    
    return retstr
  
  
  def getAdditionalFunctionDefinitionLines(self):
    """ Here you define any additional functions you will need"""
    
    if(!self.updateFunctionCalled)
      self.update()
    
    # NNFlowInterface does not need any additional functions :-)
    retstr=''
    return retstr
  
  
  def getBeforeLoopLines(self):
    """ Here you write the code which shgould be inserted before the main event loop"""
    
    if(!self.updateFunctionCalled)
      self.update()
    
    rstr='''
    
    std::string dataDir = "''' + self.modelFolderPath + '''";\n'''
    
    rstr += '''
    std::string modelLoc = dataDir + "/''' + self.modelName + '''";\n'''
    
    rstr += """
    std::cout << "Will use the tfModelUser model: " << modelLoc << std::endl;

    // Number of input variables and output labels\n
    """
    
    rstr += '''int numberOfInputVariables = ''' + int(len(self.inputVariablesList)) + ''';'''
    rstr += '''int numberOfOutputLabels = ''' + int(len(self.outputLabelsList)) + ''';'''
    
    rstr += '''
    std::cout << "Number of input variables: " << numberOfInputVariables << std::endl;
    std::cout << "Number of output labels: " << numberOfOutputLabels << std::endl;
    
    // load and initialize the model
    dnn::tf::tfModelUser modelUser(modelLoc, numberOfInputVariables, numberOfOutputLabels);
    '''
    
    return rstr

  
  def getVariableInitInsideEventLoopLines(self):
    """ Initialize variables INSIDE event loop"""
    
    if(!self.updateFunctionCalled)
      self.update()
    
    rstr='''
    // output node variables\n
    '''
    
    for(outputLabel in outputLabelList):
      # Handle tf_class variable which is an integer
      if(outputLabel == 'tf_class'):
        rstr += '''int tf_class = -2;\n'''
      else:
        rstr += '''double ''' + outputLabel + ''';\n'''
 
    # Add preselection string to speed up plotting
    if(len(self.preselectionList) > 0):
      rstr += '''\nNNFlowInterface preselection\n'''
      for(preselection in preselectionList):
        rstr += '''\nif(!''' + preselection + ''') continue;\n'''
 
    return rstr
  
  
  def getEventLoopCodeLines(self):
    """ Code that call the Classifier and fills the needed variables
    This is also inside of the event loop
    """
    
    if(!self.updateFunctionCalled)
      self.update()
    
    rstr='''

    // String vector contains names of all input variables pushed into input values vector
    std::vector<std::string> inputNames = {
    '''
  
    for(inputVariable in self.inputVariablesList):
      rstr += '''"''' + inputVariable + '''",\n'''
  
    rstr= '''
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
        std::cerr << "NNFlowInterface: Inputvariable " << variableName <<  " was not found in maps." << std::endl;
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
  
  '''

    return rstr

  
  def getTestCallLines(self):
    """ Here is code calling a test function to see wether the calling works as it should"""
    
    if(!self.updateFunctionCalled)
      self.update()
    
    
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
    for (unsigned int i = 0; i < outputValuesReturnVec.size(); i++)
    {
        std::cout << "Output Value: " << outputValuesReturnVec[i] << std::endl;
        assert(fabs(outputValuesReturnVec[i] - outputValuesVec[i]) < 0.00001 && "The unit test for the NNFlowInterface did not succeed.");
    }
"""
    return rstr
  
  
  def getCleanUpLines(self):
    """ Call need desctructors here and other cleanup things
    
    Will be run after event loop
    """
    
    if(!self.updateFunctionCalled)
      self.update()
    
    rstr="""
   """
    return rstr
  
  
  