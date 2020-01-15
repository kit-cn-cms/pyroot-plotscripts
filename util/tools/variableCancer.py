import sys
import re
import collections
import xml.etree.ElementTree as ET
import ROOT

class VariableManager:
    '''
    replacement of 'Variables' Class
    add lists of variables/single variables with .add
    run the initialization program with .run
    '''
    def __init__(self, tree, vetolist = [], verbose = 0):
        # all initialized Variables
        self.variables          = {}
        # all Variables that are not initialized yet
        self.variablesToInit    = {}
        # list of variables to be ignored when initializing
        self.vetolist           = vetolist
        # tree to get variable information from
        self.tree               = tree
        # list of expressions to search for variables
        self.expressionsToInit  = []
        # verbosity setting
        self.verbose            = verbose
        
    # functions for variable setup
    # =============================================================================================
    def add(self, expressionList):
        '''
        add lists of expressions/expressions to be searched for variables
        '''
        if isinstance(expressionList, basestring):
            expressionList = [expressionList]

        if not isinstance(expressionList, list):
            print("VariableManager.add needs a list of variables or a single variable as argument")
            exit()

        # adding expression to list
        self.expressionsToInit = list(set(self.expressionsToInit+expressionList))
        self.expressionsToInit = sorted(self.expressionsToInit)

    def run(self):
        '''
        run the variable search and initialization program
        '''
        print("initializing all {} expressions.".format(len(self.expressionsToInit)))
        if self.verbose > 1:
            print("------- expressions -------")
            for v in self.expressionsToInit:
                print(v)
            print("---------------------------")

        # looping over all expressions in list and search them for variables
        for expr in self.expressionsToInit:
            if self.verbose > 10:
                print("+"*20)
                print("initializing "+str(expr))
            self.searchVariables( expr )

        # after all expressions have been found, initialize them
        print("initializing all variables...")
        self.initializeAllVariables()



    def searchVariables(self, expression):
        '''
        search for variables in a given expression
        '''
        if self.verbose > 5: print("\ncalling searchVariables with expression "+str(expression))

        # search for variable definitions in expression of form varName:=expression
        if ":=" in expression:
            varName, expression = expression.split(":=")
            self.addVariable(varName, expression, "F")

            # if expression is not a .xml-path (i.e. is not a BDT weight file), search for other variables
            if not expression.endswith(".xml"):
                if self.verbose > 5: print("searching for other variables in expression "+str(expression))
                self.searchVariables(expression)

        else:
            # search for other variables in expression
            variableNames = self.getVariableNames( expression )
            for varName in variableNames: 
                self.addVariable(varName, varName, "F")

    def getVariableNames(self, expression):
        '''
        split stuff like '(N_Jets==6&&N_BTagsM>=2)' into 
           ['N_Jets','6','N_BTagsM','2']
        and filter out variables
        '''
        candidates = re.findall( r"\w+\b(?!\()", expression )
        variables = []
        for var in candidates:
            if var[0].isalpha() or var[0] == "_":
                variables.append(var)
        return list(set(variables))


    def addVariable(self, varName, expression = "", varType = "F", indexVariable = None):
        '''
        add variable to dictionary if conditions are fullfiiled
        '''
        # dont add variables that are in the vetolist
        if varName in self.vetolist:
            if self.verbose > 20: print("variable is in vetolist not adding it.")
            return
        
        # dont add variables that already exist
        if varName in self.variables:
            if self.verbose > 20: print("variable already in variableList")
            return

        if varName in self.variablesToInit:
            # check if expressions match
            initExpr = self.variablesToInit[varName].expression
            if initExpr == expression:
                if self.verbose > 20: print("variable expressions match - skip.")
                return
            elif initExpr != varName:
                if self.verbose > 20: print("variable already has an expression string")
                return
            else:
                if self.verbose > 20: print("adding variable again with new expression")

        # adding variables that 
        #   are BDT weight files (.xml)
        #   are in the tree
        #   are Weights
        if ".xml" in expression or hasattr(self.tree, expression) or "Weight_" in varName:
            if self.verbose > 5: print("adding variable "+str(expression)+" with name "+str(varName))
            self.variablesToInit[varName] = Variable(varName, expression, varType, indexVariable)
            return

        # check remaining variables, whether they are vector variables
        if "_" in expression:
            expressionHead, expressionTail = expression.rsplit("_",1)
            if hasattr(self.tree, expressionHead) and expressionTail.isdigit():
                if self.verbose > 20: print("found vectorlike variable: "+str(expression)+" converted to "+str(expressionHead))
                self.addVariable(expressionHead, expressionHead, varType, indexVariable)
                return

        # everything remaining is added to the variable list
        if self.verbose > 5: print("adding variable "+str(expression)+" with name "+str(varName))
        self.variablesToInit[varName] = Variable(varName, expression, varType, indexVariable)

        # search expression for further variables
        if self.verbose > 20: print("searching for further variables in expression "+str(expression))
        self.searchVariables(expression)

        return


    def initializeAllVariables(self):
        '''
        initialize all variables found in expressions
        call the .initializeVariable function for each variable
        some variables (e.g. arrayVariables or BDTWeights) need additional variables to be initialized.
        those are gathered in a new .variablesToInit dictionary which is checked for remaining variables
        '''
        # add variables to variables dictionary
        for v in self.variablesToInit:
            self.variables[v] = self.variablesToInit[v]

        # empty out variablesToInit dictionary
        self.variablesToInit = {}

        # loop over all variables and initialize them
        for var in sorted(self.variables):
            if self.variables[var].isInitialized: continue
            self.variables[var].setupVariable(self.tree, self.verbose, self)
        print("total: {} variables initialized".format(len(self.variables)))

        # check if new variables need to be initialized
        if len(self.variablesToInit)>0:
            print("during the initialization of variables, {} other variables were added".format(len(self.variablesToInit)))
            if self.verbose > 1:
                print("\tvariables:")
                for var in self.variablesToInit:
                    print("\t"+str(var))
            print("initializing them now...")
            self.initializeAllVariables()
            return

        print("all variables were initialized successfully.")
        
        # get variableIndexMap
        self.indexMap = {}
        for varName, var in self.variables.iteritems():
            if var.indexVariable == None: continue
            self.indexMap[varName] = var.indexVariable
    # =============================================================================================


    # functions for writing CPP code
    # =============================================================================================



    # ---------------------------------------------------------------------------------------------
    # functions for writing code of variable initialization

    ## initialization of variables in cpp ##
    def writeVariableInitialization(self):
        castText = ""
        text = ""
        #text+= "std::map<std::string, float*> floatMap;\n"
        #text+= "std::map<std::string, Int_t*> intMap;\n"
        #text+= "std::map<std::string, Long64_t*> longMap;\n\n"

        # loop over all variables
        for name in sorted(self.variables):
            var = self.variables[name]
            stubInit, stubCast = var.writeVariableInitialization()
            text+= stubInit
            castText+= stubCast
        if self.verbose > 20: print("\n\nvariable Init:\n"+text)
        return text, castText
    
    def resetVariableInitialization(self):
        code = ""
        
        # loop over all variables
        for name in sorted(self.variables):
            var = self.variables[name]
            code += var.resetInitializedVariables()
        return code

    ## write branch adresseses to cpp file ##
    def writeBranchAdresses(self):
        text = ""
        # loop over all variables
        for name in sorted(self.variables):
            var = self.variables[name]
            if var.inTree:
                text += var.writeBranchAdress()
        text += "\n"
        if self.verbose > 20: print("\n\nbranch adresses:\n"+text)
        return text

    ## write TMVA reader for BDT variables ##
    def writeTMVAReader(self):
        text = ""
        # loop over all variables
        for name in sorted(self.variables):
            var = self.variables[name]
            if var.isBDTVar:
                text += var.writeTMVAReader(self)
        text += "\n"
        if self.verbose > 20: print("\n\ntmva reader:\n"+text)
        return text
    
    # ---------------------------------------------------------------------------------------------
    # functions for writing code of sample selections

    ## get lengths of array variables ##
    def checkArrayLengths(self, selection):
        maxIndexMap = self.getMaxIndices(selection)
        arraySelection = "1"
        for var in maxIndexMap.keys():
            arraySelection += "&&"+str(var)+">"+str(maxIndexMap[var])
        if self.verbose > 20: print("arraySelection: "+str(arraySelection))
        return arraySelection

    # get map of indices for variables in selection ##
    def getMaxIndices(self, selection):
        # find all variables in selection
        candidates = re.findall(r"\w+\b(?=\[)", selection)
        variables = []
        for var in candidates:
            if var[0].isalpha() or var[0]=="_":
                variables.append(var)
        variables = list(set(variables))

        # generate map
        # search selection string for varName[index]
        # look for maximum index occuring and write to maxIndexMap
        maxIndexMap = {}
        for var in variables:
            maxIndex = -1
            lowerBound = 0
            while True:
                variableStart = selection.find(var+"[",lowerBound)
                if variableStart > -1:  lowerBound = variableStart+len(var)+1
                else:                   break
                
                upperBound = selection.find("]", lowerBound)
                if lowerBound > 0 and upperBound > 0:
                    if variableStart == 0 or (not selection[variableStart-1].isalpha() and not selection[variableStart-1] == "_"):
                        index = int(selection[lowerBound:upperBound])
                        maxIndex = max(index, maxIndex)
            if self.indexMap[var] not in maxIndexMap.keys() or maxIndexMap[self.indexMap[var]] < maxIndex:
                maxIndexMap[self.indexMap[var]] = maxIndex

        return maxIndexMap


    # ---------------------------------------------------------------------------------------------
    # functions to write code of variable calculations

    def calculateVariables(self):
        '''
        write variable calculation lines for all variables that have expressions
        first sort variables such that dependencies are resolved
        '''
        text = ""
        
        # generate list of sorted variables
        self.generateSortedVariables()

        # generate condition variable list
        self.conditionVariables = []
        for var in self.sortedVariables:
            if "conditionFor" in var.varName:
                if self.verbose >= 1: print("adding variable to conditionVariables: "+str(var.varName))
                conditionVariables.append(var)

        # now loop over all variables in sorted list and write code
        for var in self.sortedVariables:
            if self.verbose >= 1: print("writing code for variable "+str(var.varName))
            
            # check for condition
            hasCondition = False
            for condVar in self.conditionVariables:
                if var.varName in conVar.varName:
                    hasCondition = True
                    text += "    if("+str(condVar.expression)+")\n    {\n"

            # write code for variable
            text += var.writeVariableCalculation(hasCondition)
            if hasCondition: text += "    }\n"
        text+="\n"
        if self.verbose > 20: print("\n\ncaluclate Variables:\n"+str(text))
        return text

    def generateSortedVariables(self):
        '''
        take all variables in self.variables and sort them depending on their dependencies
        if a variable is calculated from another variable, the other variable has to be calculated first
        '''

        print("figuring out variable dependencies")
        rawVariableList = [self.variables[var] for var in self.variables]
        sortedVariables = []

        allHandled = False
        nVariables = len(rawVariableList)
        print("number of variables: "+str(nVariables))

        counter = -1
        iterations = 0
        while not allHandled:
            counter += 1
            var = rawVariableList[counter]

            # if the last element is reached
            # start the loop from the beginning
            if counter == nVariables-1: 
                iterations += 1
                counter = -1
                print("resetting counter, iteration "+str(iterations))
            
            if len(sortedVariables) > 0:
                # check if all variables are in sorted list
                if collections.Counter(sortedVariables) == collections.Counter(rawVariableList):
                    # here the list should be finished
                    allHandled = True
                    continue
                
                if var in sortedVariables: continue

            # consider the variable
            if self.verbose > 5: print("considering variable "+str(var.varName))
            if var.varName == var.expression:
                # no problem here, just add variable
                sortedVariables.append( var )
                if self.verbose >= 1: print("adding variable to list: "+str(var.varName))
                continue
            if var.isBDTVar:
                # no problem here, just BDT variable without dependencies
                sortedVariables.append( var )
                if self.verbose >= 1: print("adding variable to list: "+str(var.varName))
                continue
            if var.inTree:
                # no problem here, variable is in tree without dependencies
                sortedVariables.append( var )
                if self.verbose >= 1: print("adding variable to list: "+str(var.varName))
                continue    
        
            # check for dependencies in remaining variables
            dependenciesResolved = True
            
            # loop over variables and check for dependencies
            for dependentVariable in rawVariableList:
                if dependentVariable.varName in var.expression:
                    # if a variable is in expression, check if it already in sorted list
                    # as the expression is dependent on this variable, the variable needs to be initialized first
                    if dependentVariable not in sortedVariables:
                        # variable is not in sorted list yet
                        if self.verbose > 5: print("variable {} dependent on {}".format(var.varName, dependentVariable.varName))
                        dependenciesResolved = False

            # only if no more dependencies open, add the variable to list
            if dependenciesResolved:
                sortedVariables.append( var )
                if self.verbose >= 1: print("adding variable to list: "+str(var.varName))
                continue

        print("all variable dependencies resolved and variable list sorted")
        self.sortedVariables = sortedVariables                    
            
    # ---------------------------------------------------------------------------------------------
    # functions for writing code in plot loops

    ## get all variables from expression not followed by [ ##
    def getVariablesNoIndex(self, expression):
        candidates = re.findall(r"\w+\b(?!\[)", expression)
        variables = []
        for var in candidates:
            if var[0].isalpha() or var[0] == "_":
                variables.append(var)
        return variables
    

    ## replace all occurences of array variables with indexed variable (Jet_Pt -> Jet_Pt[3]) ##
    def getArrayEntries(self, expression, index):
        newExpression = expression
        variables = self.getVariablesNoIndex(expression)
        
        for var in variables:
            if var in self.variables:
                if self.variables[var].indexVariable == None:
                    #not an array
                    continue
    
                # write regular expression to replace var -> var[index]
                regex = (var.encode("string-escape")+r'+\b(?!\[)')
                newExpression = re.sub(regex, var+"["+str(index)+"]", newExpression)

        print("returning newExpression: "+str(newExpression))
        return newExpression
                
        
    def checkVariableInitialization(self):
        for var in self.variables:
            if self.variables[var].initError:
                sys.exit("error during variable initialisation")


class Variable:
    def __init__(self, varName, expression = "", varType = "F", indexVariable = None):
        self.varName                = varName
        self.varType                = varType
        self.isArray                = False
        self.indexVariable          = indexVariable
        self.expression             = expression
        if expression == "":
            self.expression         = varName
        self.inTree                 = False
        self.isBDTVar               = False
        self.isInitialized          = False
        self.expressionVariables    = []
    
        self.initError              = False

    def setupVariable(self, tree, verbose, variableManager):
        '''
        program to setup variable
        '''
        if verbose > 10: print("initializing variable: "+str(self.varName))

        # check if variable is in tree
        if self.varName == "GenEvt_I_TTZ":
            self.inTree = True
            alt_file = ROOT.TFile("/nfs/dust/cms/user/vdlinden/legacyTTH/ntuples/legacy_2018_ttZ_v2/TTZToBB_TuneCP5_13TeV-amcatnlo-pythia8/TTZToBB_TuneCP5_13TeV-amcatnlo-pythia8_31_nominal_Tree.root")
            alt_tree = alt_file.Get("MVATree")
            branch = alt_tree.GetBranch(self.varName)
            branchTitle = branch.GetTitle()
            self.setupVariableType(branchTitle, verbose)
            self.isArray = branchTitle.split("/")[0][-1] == "]"
            alt_file.Close()
        if "Weight_LHA_320900" in self.varName :
            self.inTree = True
            alt_file = ROOT.TFile("/nfs/dust/cms/user/swieland/ttH_legacy/ntupleHadded_2017/TTbb_Powheg_Openloops_new_pmx/TTbb_Powheg_Openloops_new_pmx_1_nominal_Tree.root")
            alt_tree = alt_file.Get("MVATree")
            branch = alt_tree.GetBranch(self.varName)
            branchTitle = branch.GetTitle()
            self.setupVariableType(branchTitle, verbose)
            self.isArray = branchTitle.split("/")[0][-1] == "]"
            alt_file.Close()
        elif self.varName.startswith("Weight_rwgt") :
            self.inTree = True
            alt_file = ROOT.TFile("/nfs/dust/cms/user/swieland/ttH_legacy/ntupleHadded_2017/THQ_ctcvcp_4f_Hincl_13TeV_madgraph_pythia8/THQ_ctcvcp_4f_Hincl_13TeV_madgraph_pythia8_1_nominal_Tree.root")
            alt_tree = alt_file.Get("MVATree")
            branch = alt_tree.GetBranch(self.varName)
            branchTitle = branch.GetTitle()
            self.setupVariableType(branchTitle, verbose)
            self.isArray = branchTitle.split("/")[0][-1] == "]"
            alt_file.Close()
        elif hasattr(tree, self.varName):
            if verbose > 20: print("variable is in tree")
            self.inTree = True
            branch = tree.GetBranch(self.varName)
            branchTitle = branch.GetTitle()
            if verbose > 20: print("branchTitle is "+str(branchTitle))

            # get variable type from branch title
            # branch title is formatted as 'variableName/variableType'
            self.setupVariableType(branchTitle, verbose)

            # check if variable is an array variable
            # then branch title is formatted as 'variableName[indexVariable]/variableType'
            self.isArray = branchTitle.split("/")[0][-1] == "]"
            if self.isArray:
                if verbose > 20: print("variable is an array variable")
                self.setupVariableArray(tree, variableManager, branchTitle, verbose)
        else:
            # variable is not in tree
            if verbose > 20: print(self.varName +" does not exist in tree")
            self.inTree = False
            self.varType = "F"
            
            # check if veriable is BDT variable
            if self.expression.endswith(".xml"):
                if verbose > 20: print("variable is BDT variable")
                self.setupBDTVariable(tree, variableManager, verbose)

        self.isInitialized = True
    

    # setup functions =========================================================
    def setupVariableType(self, branchTitle, verbose):
        self.varType = branchTitle.split("/")[1]
        if verbose > 30: print("set varType to "+str(self.varType))

    def setupVariableArray(self, tree, variableManager, branchTitle, verbose):
        # search for indexVariable in 'variableName[indexVariable]/variableType'
        self.indexVariable = re.findall(r"\[(.*?)\]", branchTitle.split("/")[0])[0]
        if verbose > 20: print("indexVariable is "+str(self.indexVariable))

        # adding indexVariable to list of variables to be initialized in variableManager
        if verbose > 20: print("adding indexVariable "+str(self.indexVariable)+" to variableManager")
        variableManager.addVariable( self.indexVariable, self.indexVariable, "I")


    def setupBDTVariable(self, tree, variableManager, verbose):
        self.isBDTVar = True

        # parse xml file var variables
        root = ET.parse(self.expression).getroot()
        for var in root.iter("Variable"):
            expressionName  = var.get("Internal")
            expression      = var.get("Expression")
            expressionType  = var.get("Type")

            # add expression to expressionVariables list
            self.expressionVariables.append(expressionName)

            # for every newly found variable call variableManager to initialize this variable
            if verbose > 20: print("adding "+str(expressionName)+" to variableManager")
            variableManager.addVariable(expressionName, expression, expressionType)






    def writeVariableInitialization(self):
        '''
        write initialization of variable to CC file
        '''
        varName = self.varName
        varType = self.varType
        
        castText = ""

        # manage array variables
        if self.isArray:
            if varType == "F":
                text = "    std::unique_ptr<float[]> "+varName+" ( new float[20] );\n"
                text+= "    std::fill_n ("+varName+".get(), 20, -999);\n"
            elif varType == "I":
                text = "    std::unique_ptr<Long64_t[]> "+varName+" ( new Long64_t[20] );\n"
                text+= "    std::fill_n ("+varName+".get(), 20, -999);\n"
            elif varType == "L":
                text = "    std::unique_ptr<Long64_t[]> "+varName+" ( new Long64_t[20] );\n"
                text+= "    std::fill_n ("+varName+".get(),20,-999);\n"
            else: print("UNKNOWN TYPE: "+str(varType))

        else:
            if varType == "F":
                text = "    float "+varName+" = -999;\n"
            elif varType == "I" or varType == "L":
                text = "    Long64_t "+varName+"LONGDUMMY = -999;\n"
                text+= "    Int_t "+varName+" = -999;\n"
                castText = "    "+varName+" = Int_t("+varName+"LONGDUMMY);\n"
            else: print("UNKNOWN TYPE: "+str(varType))
        return text, castText
    
    def resetInitializedVariables(self):
        varName = self.varName
        code =""
        if self.isArray:
            code+="    std::fill_n ("+varName+".get(), 20, -999);\n"
        else:
            code+="    "+varName+" = -999;\n"
        return code
        
    def writeBranchAdress(self):
        '''
        write chain for branch adress to CC file
        '''
        text = ""

        if self.isArray:
            text += "    chain->SetBranchAddress(\""+self.varName+"\", "+self.varName+".get());\n"
        else:
            if self.varType == "I" or self.varType == "L":
                text += "    chain->SetBranchAddress(\""+self.varName+"\", &"+self.varName+"LONGDUMMY);\n"
            else:
                text += "    chain->SetBranchAddress(\""+self.varName+"\", &"+self.varName+");\n"
        return text

    def writeTMVAReader(self, variableManager):
        '''
        write TMVA reader to CC file
        '''
        text = ""
        text += "   TMVA::Reader *r_"+self.varName+" = new TMVA:Reader('Silent');\n"
        
        # add variables to reader program
        for expr in self.expressionVariables:
            if not expr in variableManager.variables:
                print("ERROR - variable not found")
                return None

            var = variableManager.variables[expr]
            text += "   r_"+self.varName+"->AddVariable('"+var.expression+"', &"+var.varName+");\n"
        
        # book MVA
        text += "   r_"+self.varName+"->BookMVA('BDT','"+self.expression+"');\n"
        return text



    def writeVariableCalculation(self, hasCondition):
        '''
        write lines for calculation of varibales if they have an expression or are BDT variables
        '''
        indent = ""
        if hasCondition: indent+= "    "
        if self.inTree:     return ""
        elif self.isBDTVar: return "    "+indent+self.varName+" = r_"+self.varName+"->EvaluateMVA('BDT'):\n"
        else:               
            if self.varName == self.expression:
                self.initError = True
                print("trying to initialize variable '{}' with itself (var = var) - this does not work".format(self.varName))
            return "    "+indent+self.varName+" = "+self.expression+";\n"




