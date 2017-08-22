import sys
import getopt
import os


class Analysis:
  """A simple class splitting the analysis in parallel and non-parallel parts"""
    
  def __init__(self):
    """Default constructor"""
    return self.__init__(self,"defaultanalysisname")
  
  def __init__(self, name,argv=list(),rootFilePath=''):
    self.name = str(name)
    if not os.path.exists(name):
      print "Making dir."
      os.makedirs(name)
    self.rootFilePath=str(rootFilePath)
    if self.rootFilePath == '':
      self.rootFilePath = name+'/'+name+'_limitInput.root'
    
    # Default settings
    #doPlotParallel or otherwise use old root file
    self.doPlotParallel=False
        
    # Use parallel script for plots
    self.doDrawParallel=True
    # Set plotnumber to none
    self.plotNumber=None

    # if one wants to plot blinded: True (default: False)
    self.plotBlinded = False

    # if one wants to get event yields table: True
    self.makeEventYields = True
    
    # if one wants to create data cards: true
    self.makeDataCards = True
    
    # if one wants to make simple plots
    self.makeSimplePlots = True

    # if one wants to make MC control plots
    self.makeMCControlPlots = True
    
    # list containing additional (input) variables which one would likes to plot in addition to discriminator variables
    self.additionalPlotVariables = []
    
    # Overwrite default settings from commandline
    self.opts = None
    self.opts = self.evaluateCommandlineArgs(argv)
    
  
  
  def evaluateCommandlineArgs(self,argv=list()):
    """Evaluate any commandline arguments"""
    try:
      opts, args = getopt.getopt(argv,"hp:",["plot=","doPlotParallel=","doDrawParallel=","plotBlinded=","makeEventYields=","makeDataCards=","makeSimplePlots=","makeMCControlPlots="])
    except getopt.GetoptError:
      print '[scriptname].py -p  <plotnumber> --doPlotParallel= --doDrawParallel= --plotBlinded= --makeEventYields= --makeDataCards= --makeSimplePlots= --makeMCControlPlots='
      sys.exit(2)
    for opt, arg in opts:
      print 'opt: ', opt, ' arg: ', arg, ' found.'
      if opt in ('-h', '--help'):
        print '[scriptname].py -p <plotnumber> --doPlotParallel= --doDrawParallel= --plotBlinded= --makeEventYields= --makeDataCards= --makeSimplePlots= --makeMCControlPlots= --additionalPlotVariables='
        sys.exit()
      elif opt in ("-p","--plotNumber"):
        self.setPlotNumber(arg)
        print "Set plotNumber option to: ", arg
      elif opt in ("--doPlotParallel"):
        self.setDoPlotParallel(arg)
        print "Set doPlotParallel option to: ", arg
      elif opt in ("--doDrawParallel"):
        self.setDoDrawParallel(arg)
        print "Set doDrawParallel option to: ", arg
      elif opt in ("--plotBlinded"):
        self.setPlotBlinded(arg)
        print "Set plotBlinded option to: ", arg
      elif opt in ("--makeEventYields"):
        self.setMakeEventYields(arg)
        print "Set makeEventYields option to: ", arg
      elif opt in ("--makeDataCards"):
        self.setMakeDataCards(arg)
        print "Set makeDataCards option to: ", arg
      elif opt in ("--makeSimplePlots"):
        self.setMakeSimplePlots(arg)
        print "Set makeSimplePlots option to: ", arg
      elif opt in ("--makeMCControlPlots"):
        self.setMakeMCControlPlots(arg)
        print "Set makeMCControlPlots option to: ", arg
      elif opt in ("--additionalPlotVariables"):
        self.setAdditionalPlotVariables(arg)
        print "Set additionalPlotVariables option to: ", arg
      
        
      return opts


  # Helper functions
  
  
  ## Getter functions
  def getAdditionalPlotVariables(self, discriminators, preselections, binLabels, alwaysExecute=False):
    """Function creates plot list for additional (input) variables
    Function checks if additionalPlotVariablesMap.py file exists. 
    If yes, then it will try to use it for determination of the amount of bins and the bin range of the plots. In case some variable cannot be mapped, the variable will be added to existing file and user will get warned.
    If no, then it will construct such a dict and stop the further execution.
    """
    
    # Create dictionary for discriminators and preselections using additionalPlotVariables
    additionalPlotVariablesDictFromClass = {}
    for discr, preselection, binLabel in zip(discriminators, preselections, binLabels):
      for additionalPlotVariable in self.additionalPlotVariables:
        tmpVarName = discr + '_' + additionalPlotVariable
        additionalPlotVariablesDictFromClass[tmpVarName] = '''Plot(ROOT.TH1F("''' + tmpVarName + '''", "add. var. (''' + tmpVarName +  ''')", 10, 0, 150),"''' + additionalPlotVariable + '''","''' + preselection + '''","''' + binLabel + '''"))'''
    
    # Stop further execution if dict file did not exist, map could not be read or variable could not be mapped.
    stopFurtherExecution = False
    
    # Try to open map (dict) file and read dict
    additionalPlotVariablesDictFromFile = {}
    if os.path.isfile('additionalPlotVariablesMap.py'):
      print 'Found additionalPlotVariablesMap.py file. Will try to open it now.'
      with open('additionalPlotVariablesMap.py') as mapFile:
        additionalPlotVariablesDictFromFile = eval(mapFile.read())
      if not additionalPlotVariablesDictFromFile:
        print "Could not read map from additionalPlotVariablesMap.py file or file is empty.\n Will update existing one and stop further execution."
        stopFurtherExecution = True
      else:
        print "Comparing map from additionalPlotVariablesMap.py file with internal map of additional plot variables.\n Checking if keys from internal map contained in map from file."
        missingKeysInFile = []
        for key in additionalPlotVariablesDictFromClass.keys():
          # Check for missing key
          if not key in additionalPlotVariablesDictFromFile:
            missingKeysInFile.append(key)
          # otherwise replace internal key/value pair with external one
          else:
            additionalPlotVariablesDictFromClass[key] = additionalPlotVariablesDictFromFile[key]
        if differenceInKeys:
          print "Found keys missing in map from file and required for plotting additional variables:\n", differenceInKeys, "\n Will stop further execution."
          stopFurtherExecution = True
      
    else:
      print 'Did not found additionalPlotVariablesMap.py file. Will create one and stop further execution.'
      stopFurtherExecution = True
      
    # Dedicated sort function, so that writen out dict is sorted  
    def sortByUsingLastPart(elem):
      return elem.rsplit('_')[-1]
      
    # Write dictionary to file
    with open('additionalPlotVariablesMap.py', 'w') as mapFile:
      mapFile.write('{\n')
      # sort dict
      for variableKey in sorted(additionalPlotVariablesDictFromClass.iterkeys(), key=sortByUsingLastPart):
        mapFile.write("""'""" + variableKey + """': '""" + additionalPlotVariablesDictFromClass[variableKey] + """',\n""")
      mapFile.write('}')
    
    if stopFurtherExecution and not alwaysExecute:
      sys.exit('Stopping execution since mapping for additional variable plotting was not successful.\n Check the file additionalPlotVariablesMap.py and adjust it accordingly.')
    
    return additionalPlotVariablesDictFromClass
      
    

  
  ## Setter functions
  def setPlotNumber(self,arg):
    self.plotNumber = int(arg)
  
  def setDoPlotParallel(self,arg):
    self.doPlotParallel = arg
      
  def setDoDrawParallel(self,arg):
    self.doDrawParallel = arg
      
  def setPlotBlinded(self,arg):
    self.plotBlinded = arg
      
  def setMakeEventYields(self,arg):
    self.makeEventYields = arg
      
  def setMakeDataCards(self,arg):
    self.makeDatacards = arg
      
  def setMakeSimplePlots(self,arg):
    self.makeSimplePlots = arg
      
  def setMakeMCControlPlots(self,arg):
    self.makeMCControlPlots = arg

  def setAdditionalPlotVariables(self,arg):
    if arg and type(arg) is list:
      print "Activated additional plot variables.\n"
      self.additionalPlotVariables = arg
      print self.additionalPlotVariables
    else:
      print "Could not activate additional plot variables since argument is not a list."