# this class describes the interface to the DNN interface to be used in the scriptgenerator
# This class can be used to load a Tensorflow model obtained by making use of the NNFlow framework

# There are several methods which you will need to update for your own classifier 
# Then use the interface by passing THIS file path to the plotparallel function

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
    if self.debugOutput:
      print "Update function: Start reading input variables list file: ", inputVariablesListLoc
    self.inputVariablesList = self.readListFromFile(inputVariablesListLoc)
    
    # Update / read output labels list, the assumption is that the file is located under self.modelFolderPath/model_properties/outputLabels.txt
    outputLabelsListLoc = self.modelFolderPath + '/model_properties/outputLabels.txt'
    if self.debugOutput:
      print "Update function: Start reading output labels list file: ", outputLabelsListLoc
    self.outputLabelsList = self.readListFromFile(outputLabelsListLoc)
    # Add tf in front of output label list entries 
    for outputLabelNumber, outputLabel in enumerate(self.outputLabelsList):
      if (not outputLabel.startswith('tf_')):
        self.outputLabelsList[outputLabelNumber] = 'tf_' + self.outputLabelsList[outputLabelNumber]
    if self.debugOutput:
      print "Update function: Output labels list: ", self.outputLabelsList
    
    # Add tf_class variable to list
    self.outputLabelsList.append('tf_class')
  
    # Update / read preselection list, the assumption is that the file is located under self.modelFolderPath/model_properties/preselection.txt
    preselectionListLoc = self.modelFolderPath + '/model_properties/preselection.txt'
    if self.debugOutput:
      print "Update function: Start reading preselection list file: ", preselectionListLoc
    self.preselectionList = self.readListFromFile(preselectionListLoc)
  
    # Update / read unitTest input values list, the assumption is that the file is located under self.modelFolderPath/model_properties/unitTestInputValues.txt
    unitTestInputValuesListLoc = self.modelFolderPath + '/model_properties/unitTestInputValues.txt'
    if self.debugOutput:
      print "Update function: Start reading unitTest input values list file: ", unitTestInputValuesListLoc
    self.unitTestInputValuesList = self.readListFromFile(unitTestInputValuesListLoc)
  
    # Update / read unitTest output values list, the assumption is that the file is located under self.modelFolderPath/model_properties/unitTestOutputValues.txt
    unitTestOutputValuesListLoc = self.modelFolderPath + '/model_properties/unitTestOutputValues.txt'
    if self.debugOutput:
      print "Update function: Start reading unitTest output values list file: ", unitTestOutputValuesListLoc
    self.unitTestOutputValuesList = self.readListFromFile(unitTestOutputValuesListLoc)
  
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
      raise
  
    for singleContent in fileContent:
      # Make sure that lines does not only consists of whitespace or line break characters
      if(not bool(not singleContent or singleContent.isspace())):
        tempList.append(singleContent)
    
    if self.debugOutput:
      print "\n readListFromFile function read file: ", fileLocation
      print "List obtained from file:\n", tempList
    
    return tempList
  

  ## Getter function
  def getAdditionalVariablesList(self):
    """Function returns list with all input variables which have to be defined in main analysis script as additional variables
    Returns: String list 
    """
  
    if(not self.updateFunctionCalled):
      self.update()
      
    return self.inputVariablesList
  
  
  ## Interface functions
 
  def getExternalyCallableVariables(self):
    """This is a list of variables which should be visible for the plotscript.
    You also need to define them in the getVariableInitLines method
    """
    
    if(not self.updateFunctionCalled):
      self.update()
    
    print "Get external callable variables: ", self.outputLabelsList
    return self.outputLabelsList
    
  
  def getIncludeLines(self):
    """Write here the code with the include statements
    DNN header is relative to CMSSW BASE
    """
    
    if(not self.updateFunctionCalled):
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
    
    if(not self.updateFunctionCalled):
      self.update()
    
    # NNFlowInterface does not need any additional functions :-)
    retstr=''
    return retstr
  
  
  def getBeforeLoopLines(self):
    """ Here you write the code which shgould be inserted before the main event loop"""
    
    if(not self.updateFunctionCalled):
      self.update()
    
    rstr='''
    
    std::string dataDir = "''' + self.modelFolderPath + '''";\n'''
    
    rstr += '''
    std::string modelLoc = dataDir + "/''' + self.modelName + '''";\n'''
    
    rstr += """
    std::cout << "Will use the tfModelUser model: " << modelLoc << std::endl;

    // Number of input variables and output labels\n
    """
    
    rstr += '''int numberOfInputVariables = ''' + str(int(len(self.inputVariablesList))) + ''';'''
    rstr += '''int numberOfOutputLabels = ''' + str(int(len(self.outputLabelsList))) + ''';'''
    
    rstr += '''
    std::cout << "Number of input variables: " << numberOfInputVariables << std::endl;
    std::cout << "Number of output labels: " << numberOfOutputLabels << std::endl;
    
    // load and initialize the model
    dnn::tf::tfModelUser modelUser(modelLoc, numberOfInputVariables, numberOfOutputLabels);
    '''
    
    return rstr

  
  def getVariableInitInsideEventLoopLines(self):
    """ Initialize variables INSIDE event loop"""
    
    if(not self.updateFunctionCalled):
      self.update()
    
    rstr='''
    // output node variables\n
    '''
    
    for outputLabel in self.outputLabelsList:
      # Handle tf_class variable which is an integer
      if(outputLabel == 'tf_class'):
        rstr += '''int tf_class = -2;\n'''
      else:
        rstr += '''double ''' + outputLabel + ''';\n'''
 
    # Add preselection string to speed up plotting
    if(len(self.preselectionList) > 0):
      rstr += '''\nNNFlowInterface preselection\n'''
      for preselection in preselectionList:
        rstr += '''\nif(!''' + preselection + ''') continue;\n'''
 
    return rstr
  
  
  def getEventLoopCodeLines(self):
    """ Code that call the Classifier and fills the needed variables
    This is also inside of the event loop
    """
    
    if(not self.updateFunctionCalled):
      self.update()
    
    rstr='''

    // String vector contains names of all input variables pushed into input values vector
    std::vector<std::string> inputNames = {
    '''
  
    for inputVariable in self.inputVariablesList:
      rstr += '''"''' + inputVariable + '''",\n'''
  
    rstr += '''
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
    
    '''
    
    # Add tf output label variables handling and handling of tf_class
    for outputLabelNumber, outputLabel in enumerate(self.outputLabelsList):
      if(outputLabel == 'tf_class'):
        rstr += '''
        // Check which class has largest outputValue and set tf_class variable accordingly
        int currentIndexOfOutputValuesReturnVec = 0;
        float tempLargestOutputValue = -2.0;
        for (auto outputValue: outputValuesReturnVec) {
          currentIndexOfOutputValuesReturnVec++;
          if(outputValue > tempLargestOutputValue) {
            tempLargestOutputValue = outputValue;
            tf_class = currentIndexOfOutputValuesReturnVec;
          }
        }
        
        '''
      else:
        rstr += outputLabel + ''' =  outputValuesReturnVec[''' + outputLabelNumber + '''];\n'''
  
       
    if self.debugOutput:
      rstr += '''
      std::cout << "-----NNFlowInterface debug output-----" << std::endl;
      std::cout <<"Input values " << std::endl;
      for (auto inputValue: inputValues) {
        std::cout << inputValue << ", " ;
      }
      
      '''
      
      for outputLabel in self.outputLabelsList:
        rstr += '''std::cout << "''' + outputLabel +  '''" << ''' + outputLabel + '''<< std::endl;\n'''

    return rstr

  
  def getTestCallLines(self):
    """ Here is code calling a test function to see wether the calling works as it should"""
    
    if(not self.updateFunctionCalled):
      self.update()
    
    
    rstr = '''
    // NNFlowInterface unit test
    // Vector containing input variables values
    std::vector<float> eventVec = {
    '''
    
    for inputValue in self.unitTestInputValuesList:
      rstr += ''' ''' + inputValue + ''',\n'''
    
    rstr += '''
    };

    // Vector containing output labels values
    std::vector<float> outputValuesVec = {
    '''
    
    for outputValue in self.unitTestOutputValuesList:
      rstr += ''' ''' + outputValue + ''',\n'''
    
    rstr += '''
    };
    
    // Evaluate unit test event for given model
    std::vector<float> outputValuesReturnVec = modelUser.evalModel(eventVec);

    // compare vectors for unit test
    std::cout << "Compare NNFlowInterface unit test result with known output" << std::endl;
    std::cout << "No error printout means unit test succeeded." << std::endl;
    for (unsigned int i = 0; i < outputValuesReturnVec.size(); i++)
    {
        std::cout << "Calculated output Value: " << outputValuesReturnVec[i] << ", known output value: " << outputValuesVec[i]  << std::endl;
        assert(fabs(outputValuesReturnVec[i] - outputValuesVec[i]) < 0.00001 && "The unit test for the NNFlowInterface did not succeed.");
    }
    '''
    
    return rstr
  
  
  def getCleanUpLines(self):
    """ Call need desctructors here and other cleanup things
    
    Will be run after event loop
    """
    
    if(not self.updateFunctionCalled):
      self.update()
    
    rstr='''
    '''
    
    return rstr
  
  
  