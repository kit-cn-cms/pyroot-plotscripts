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
    # Deactivate checkBins in renameHistos if additionalPlotVariables are used
    self.checkBins = True
    
    # Choose if one would like to activate an optimizing binning algorithm
    self.optimizedRebinning = ''
    
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
        print '[scriptname].py -p <plotnumber> --doPlotParallel= --doDrawParallel= --plotBlinded= --makeEventYields= --makeDataCards= --makeSimplePlots= --makeMCControlPlots= --additionalPlotVariables= --optimizedRebinning='
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
      elif opt in ("--optimizedRebinning"):
        self.setOptimizedRebinning(arg)
        print "Set optimizedRebinning option to: ", arg  
      
      
        
      return opts


  # Helper functions
  
  
  ## Getter functions
  def getAdditionalPlotVariables(self, discriminators, preselections, binLabels, alwaysExecute=False):
    """Function creates plot list for additional (input) variables
    Function checks if additionalPlotVariablesMap.py file exists. 
    If yes, then it will try to use it for determination of the amount of bins and the bin range of the plots. In case some variable cannot be mapped, the variable will be added to existing file and user will get warned.
    If no, then it will construct such a dict and stop the further execution.
    
    mapFile is a dict with additionalPlotVariable as key and numberOfBins, binLowerEdge, binUpperEdge as values contained in list
    """
    
    # Create dictionary for discriminators and preselections using additionalPlotVariables
    # Dictionary contains  additionalPlotVariable, numberOfBins, binLowerEdge, binUpperEdge ,discr, preselection, binLabel,       
    additionalPlotVariablesDictFromClass = {}
    for discr, preselection, binLabel in zip(discriminators, preselections, binLabels):
      for additionalPlotVariable in self.additionalPlotVariables:
        # Use fullVarName as key in class dict while additionalPlotVariable is key in map file
        fullVarName = discr + '_' + binLabel + '_' + additionalPlotVariable
        additionalPlotVariablesDictFromClass[fullVarName] = [additionalPlotVariable, 10, 0, 150, discr, preselection, binLabel]
    
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
      print 'Did not found additionalPlotVariablesMap.py file. Will create one and stop further execution.'
      stopFurtherExecution = True
      
      
    # Compare internal map with map from file and add additional keys if necessary
    print "Comparing map from additionalPlotVariablesMap.py file (or empty dict) with internal map of additional plot variables.\n If necessary, adding keys from internal map to map file."
    missingKeysInFile = set()
    for classKey in additionalPlotVariablesDictFromClass.keys():
      # Check for missing additionalPlotVariable description in map file
      # In map file additionalPlotVariable is the key while in class fullVarName
      mapFileKey = additionalPlotVariablesDictFromClass[classKey][0]
      if not mapFileKey in additionalPlotVariablesDictFromFile:
        missingKeysInFile.add(mapFileKey)
      # otherwise replace internal key/value pair with external one
      else:
        # retrieve full value list
        tmpList = additionalPlotVariablesDictFromClass[classKey]
        # and replace content with stored content
        # numberOfBins replacement
        tmpList[1] = additionalPlotVariablesDictFromFile[mapFileKey][0]
        # binLowerEdge replacement
        tmpList[2] = additionalPlotVariablesDictFromFile[mapFileKey][1]
        # binUpperEdge replacement
        tmpList[3] = additionalPlotVariablesDictFromFile[mapFileKey][2]
        additionalPlotVariablesDictFromClass[classKey] = tmpList
    if missingKeysInFile:
      print "Found keys missing in map from file and required for plotting additional variables:\n", missingKeysInFile, "\n Will add keys to map file using default values.\n Afterwards will stop further execution."
      # Add missing keys to mapFile dictionary
      for missingKey in missingKeysInFile:
        additionalPlotVariablesDictFromFile[missingKey] = [10,0,150]
      stopFurtherExecution = True
    
          
    # Dedicated sort function, so that writen out dict is sorted  
    def sortByUsingLastPart(elem):
      return elem.rsplit('_')[-1]
      
    # Write dictionary to file
    with open('additionalPlotVariablesMap.py', 'w') as mapFile:
      mapFile.write('{\n')
      # sort dict and write entry for each additionalPlotVariable in file
      for mapFileKey in sorted(additionalPlotVariablesDictFromFile.iterkeys(), key=sortByUsingLastPart):
        # list contains numberOfBins, binLowerEdge, binUpperEdge
        tmpList = additionalPlotVariablesDictFromFile[mapFileKey]
        mapFile.write("""'""" + mapFileKey + """': [ """ + str(tmpList[0]) + ', ' + str(tmpList[1]) + ', ' + str(tmpList[2])  + """ ],\n""")
      mapFile.write('}')
    
    if stopFurtherExecution and not alwaysExecute:
      sys.exit('Stopping execution since mapping for additional variable plotting was not successful.\n Check the file additionalPlotVariablesMap.py and adjust it accordingly.')
    
    # construct list containing all additionalPlotVariables
    returnList = []
    for classKey in additionalPlotVariablesDictFromClass.keys():
      currList = additionalPlotVariablesDictFromClass[classKey]
      # Construct full var name, currList: additionalPlotVariable, numberOfBins, binLowerEdge, binUpperEdge, discr, preselection, binLabel
      fullVarName = currList[4] + '_' + currList[6] + '_' + currList[0]
      plotString = '''Plot(ROOT.TH1F("''' + fullVarName + '''", "add. var. (''' + fullVarName +  ''')",''' + str(currList[1]) + ',' + str(currList[2]) + ',' + str(currList[3]) + '''),"''' + currList[0] + '''","''' + currList[5] + '''","''' + currList[6] + '''")'''
      returnList.append(plotString)
      
    # Set variable to deactivate checkBins functionality in renameHistos, because otherwise it will take a long time.
    self.checkBins = False
    print "Set checkBins variable to false. Make sure, this variable is used in renameHistos."
      
    return returnList
      
  
  def getCheckBins(self):
    """ Return value of checkBins variable
    Variable can be used in renameHistos function of limittools.py to reduce time for renaming histograms.
    """
    return self.checkBins
  
  def getActivatedOptimizedRebinning(self):
    """Return true if optimized rebinning was activated """
    if self.optimizedRebinning:
      print "optimizedRebinning is activated."
      return true
    else:
      print "optimizedRebinning is deactivated."
      return false
    
  def getOptimzedRebinning(self):
    """Return which rebinning algorithm was activated """
    if self.optimizedRebinning:
      print "optimizedRebinning set to: ", self.optimizedRebinning
      return self.optimizedRebinning
    else:
      sys.exit('Stopping execution since no optimizedRebinning algorithm was chosen, but it was activated.')
  
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
      
  def setOptimizedRebinning(self,arg):
    self.optimizedRebinning = arg