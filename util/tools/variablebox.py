import os
import re
import ROOT
import xml.etree.ElementTree as ET
import collections

class Variable:
  def __init__(self, name, expression='', vartype='F', arraylength=None):
    self.name = name
    self.vartype = vartype
    self.arraylength = arraylength
    self.expression = expression
    if expression is '':
      self.expression = name
    self.intree = False
    self.mvavar = False
    self.exprvariables = []


  ## functions for initializing variables ##
  def initVar(self,tree,variables):
    if hasattr(tree, self.name):
      self.intree = True
      branch = tree.GetBranch(self.name)
      branchtitle = branch.GetTitle()
      self.setupVarType(branchtitle)
      self.setupVarArray(tree, variables, branchtitle)
      return

    print(str(self.name)+' does not exist in tree!')
    self.intree = False
    self.vartype = 'F'
    # setting up MVA variable
    self.setupMVAVar(tree,variables)

  def setupVarType(self,branchtitle):
    self.vartype = branchtitle.split('/')[1]

  def setupVarArray(self, tree, variables, branchtitle):
    isArray = branchtitle.split('/')[0][-1] == ']'

    if not isArray:
      self.arraylength = None
      return

    # variable is array
    self.arraylength = re.findall(r"\[(.*?)\]",branchtitle.split('/')[0])[0]
    # call initSingeVar with vartype I
    variables.initSingleVar(tree,self.arraylength,self.arraylength,'I')


  def setupMVAVar(self,tree,variables):
    if not '.xml' in self.expression:
      self.mvavar = False
      return

    self.mvavar = True

    root = ET.parse(self.expression).getroot()
    for var in root.iter('Variable'):
      exprname = var.get('Internal')
      exprexpr = var.get('Expression')
      exprtype = var.get('Type')

      self.exprvariables.append(exprname)

      # calling initSingleVar
      variables.initSingleVar(tree, exprname, exprexpr, exprtype)




  ## function for initializing variable and writing cc code ##
  def initVarProgram(self):
    var = self.name
    vartype = self.vartype
    isArray = self.arraylength != None
    castText = ""
    if isArray:
      if vartype == 'F':
        text = '  float* '+var+' = new float[100];'
        for i in range(0,100):
          text += '\nfloatMap["' + var + '_' + str(i+1) + '"] = &' + var + '[' + str(i) + ']' + ';'
      elif vartype == 'I':
        text = '  Long64_t* '+var+' = new Long64_t[100];'
        for i in range(0,100):
          text += '\nintMap["' + var + '_' + str(i+1) + '"] = &' + var + '[' + str(i) + ']' + ';'
      elif vartype == 'L':
        text='  Long64_t* '+var+' = new Long64_t[100];'
        for i in range(0,100):
          text += '\nlongMap["' + var + '_' + str(i+1) + '"] = &' + var + '[' + str(i) + ']' + ';'    
      else: "UNKNOWN TYPE", vartype
    else:
      if vartype =='F':
        text = '\nfloat '+var+' = -999;\nfloatMap["' + var + '"] = &' + var + ';'
      #DANGERZONE
      # Needed hack because of mixing of Int and Long ntuples
      # Avoid in the future
      # Not working for array ints. But i dont think that there are any anywhere
      elif (vartype == 'I' or vartype == 'L'):
        text = '\nLong64_t '+var+'LONGDUMMY = -999;\nlongMap["' + var + 'LONGDUMMY"] = &' + var + 'LONGDUMMY;'
        text += '\nInt_t '+var+' = -999;\nintMap["' + var + '"] = &' + var + ';'        
        castText = '\n'+var+' = Int_t('+var + 'LONGDUMMY);'
      #elif vartype =='L':
        #text='\nLong64_t '+var+' = -999;\nlongMap["' + var + '"] = &' + var + ';'
      else: "UNKNOWN TYPE", vartype
    return text, castText




  ## init branch adress for CC programm and write code ##
  def initBranchAddressProgram(self):
    isArray = self.arraylength != None
    text = ''
    if isArray:
      text += '  chain->SetBranchAddress("'+self.name+'",'+self.name+');\n'
    else:
      if self.vartype == 'I' or self.vartype == 'L':
        text += '  chain->SetBranchAddress("'+self.name+'",&'+self.name+'LONGDUMMY);\n'
      else:
        text += '  chain->SetBranchAddress("'+self.name+'",&'+self.name+');\n'
    return text




  ## functions for MVA reader ##
  def setupTMVAReaderProgram(self,variables):
    if not self.mvavar:
      print 'Error! Trying to setup TMVA Reader for non MVA variable ',self.name,'!'
      return None
    text = ''
    text += self.initReaderProgram()
    text += self.addVariablesToReaderProgram(variables)
    text += self.bookMVAProgram()
    text += '\n'
    return text

  def initReaderProgram(self):
    text = ''
    text += '  TMVA::Reader *r_'+self.name+' = new TMVA::Reader("Silent");\n'
    return text

  def addVariablesToReaderProgram(self,variables):
    text = ''
    for varname in self.exprvariables:
      if not varname in variables.variables:
        print 'Error! Input variable ',varname,' does not exist in expr collection!'
        return None

      var = variables.variables[varname]
      text += '  r_'+self.name+'->AddVariable("'+var.expression+'", &'+var.name+');\n'
    return text

  def bookMVAProgram(self):
    text = '  r_'+self.name+'->BookMVA("BDT","'+self.expression+'");\n'
    return text



  # setup branch adress for CC code ##
  def calculateVarProgram(self):
    text=''

    if not self.intree:
      if not self.mvavar:
        text+='    '+self.name+' = '+self.expression+';\n'
      else:
        text+='    '+self.name+' = r_'+self.name+'->EvaluateMVA("BDT");\n'

    return text










class Variables:
    def __init__(self,veto=[]):
        self.variables = {}
        self.vetolist = veto

    ## functions for initializing variables ## 
    def initVars(self, expr, tree):
        if type(expr) == list:
            for expression in expr:
                self.initVars(expression, tree)
        elif type(expr) == str:
            if ":=" in expr:
                name, expr = expr.split(":=")
                if not ".xml" in expr:
                    self.initVars(expr, tree)
                self.initSingleVar(tree, name, expr, "F")
            else:
                varNames = self.getVarNames(expr)
                for name in varNames:
                    self.initSingleVar(tree, name, name, "F")
        else:
            print("input for initVars should either be a list of expressions or an expression (str)")
        
    def getVarNames(self,expr):
        # find all words not followed by ( (these are functions)
        candidates = re.findall(r"\w+\b(?!\()", expr)
        variables = []
        for var in candidates:
            if var[0].isalpha() or var[0] == '_':
                variables.append(var)
        return variables

    def initSingleVar(self, tree, name, expression = '', vartype = 'F', arraylength=None):
        if name in self.variables or name in self.vetolist:
            # dont use variables in vetolist or already used
            return

        # if variable fulfils any of these conditions init the variable
        if ".xml" in expression or hasattr(tree, expression) or "Weight_" in name:
            print("creating variable "+str(expression)+" with name "+str(name))
            self.variables[name] = Variable(name, expression, vartype, arraylength)
            self.variables[name].initVar(tree, self) 
            return

        # check if other variables are vector sub variables?
        if "_" in expression:
            exprHead, exprTail = expression.rsplit("_", 1)
            if hasattr(tree, exprHead) and exprTail.isdigit():
                print("found vector like variable: "+str(expression)+" which was converted to: "+str(exprHead))
                self.initSingleVar(tree, exprHead, exprHead, vartype, arraylength)
                return
        
        # handle formular expression by recursive function
        # splits formular based on bracets
        print("init vars for "+str(expression))
        self.initVars(expression, tree)
        
        print("creating variable "+str(expression)+" with name "+str(name))
        self.variables[name] = Variable(name, expression, vartype, arraylength)
        self.variables[name].initVar(tree, self)
        return
    ## -----------------------------------------------


    
    ## init variables for CC program and write code ##
    def initVarsProgram(self):
        castText = ""
        text = "std::map<std::string, float*> floatMap;\n"
        text+= "std::map<std::string, Int_t*> intMap;\n"
        text+= "std::map<std::string, Long64_t*> longMap;\n\n"
        
        # loop over all variables
        for name, var in self.variables.iteritems():
            stubInit, stubCast = var.initVarProgram()
            text += stubInit
            castText += stubCast
        text += '\n'
        castText += '\n'
        return text, castText



    ## init branch adresses for CC programm and write code ##
    def initBranchAddressesProgram(self):
        text = ""
        # loop over variables
        for name, var in self.variables.iteritems():
            if var.intree:
                text += var.initBranchAddressProgram()
        text += '\n'
        return text



    ## setup all TMVA readers and write code ##
    def setupTMVAReadersProgram(self):
        text = ""
        for name, var in self.variables.iteritems():
            if var.mvavar:
                text += var.setupTMVAReaderProgram(self)
        return text



    ## get array lenghts for writing CC code ##
    def checkArrayLengths(self,expr):
        maxidxs = self.varsWithMaxIndex(expr)
        arrayselection = "1"
        for v in maxidxs.keys():
            arrayselection += '&&'+v+'>'+str(maxidxs[v])
        return arrayselection




    # setup branch adresses for CC code ##
    def calculateVarsProgram(self):
        text = ""
        
        # get list of sorted variables
        sortedVariableList = self.sortVariables()
        
        conditionVariableList = []        
        for name,var in sortedVariableList:
            if "conditionFor" in name:
                conditionVariableList.append([name,var])
        
        # now write the code for each variable
        for name,var in sortedVariableList:
            print "writing code for ", var.name
            # check for conditional evaluation
            hasCondition = False
            for condname, condvar in conditionVariableList:
                if name in condname:
                    hasCondition = True
                    text += 'if('+condvar.expression+'){\n'
            text += var.calculateVarProgram()
            if hasCondition:
                text += '}\n'
        text += '\n'
        return text

    def sortVariables(self):
        # figure out the dependencies between the variables so that they can be calculated in the proper order
        print "print figuring out variable dependencies"
        rawVariableList = []
        sortedVariableList = []
        for name,var in self.variables.iteritems():
            rawVariableList.append([name,var])

        allVariablesHandled = False
        nVariables = len(rawVariableList)
        
        variableCounter =- 1
        while allVariablesHandled == False:
            variableCounter+=1
            if len(sortedVariableList) > len(rawVariableList):
                print "PROBLEM: sorted list longer than raw list?"
                print rawVariableList
                print sortedVariableList
                exit(0)

            name, var = rawVariableList[variableCounter]
            
            if variableCounter == nVariables-1:
                #starting loop from the beginning
                variableCounter=-1

            if len(sortedVariableList) > 0:
                if collections.Counter(zip(*sortedVariableList)[0]) == collections.Counter(zip(*rawVariableList)[0]):
                    # list should be finished here - check lists
                    if len(rawVariableList) != len(sortedVariableList):
                        print "PROBLEM: lists have different lengths"
                        print rawVariableList
                        print sortedVariableList
                        exit(0)

                    # this will get the element with the most entries in the list and also how often it appears.
                    MaxOcc, numMaxOcc = collections.Counter(zip(*sortedVariableList)[0]).most_common(1)[0]
                    if numMaxOcc != 1:
                        print "PROBLEM: sorted list contains the same entry multiple times"
                        print MaxOcc, numMaxOcc
                        exit(0)

                    allVariablesHandled = True
                    continue

                if name in zip(*sortedVariableList)[0]:
                    ##already have this variable
                    continue

            # consider the variable
            print "considering ", name, var
            if var.name == var.expression:
                sortedVariableList.append([name,var])
                continue
            if var.mvavar == True:
                sortedVariableList.append([name,var])
                continue
            if var.intree == True:
                sortedVariableList.append([name,var])
                continue
            alldependenciesresovled = True
            for dvar in zip(*rawVariableList)[0]:
                if dvar in var.expression:
                    if len(sortedVariableList) == 0:
                        alldependenciesresovled = False
                        continue
                    if dvar not in zip(*sortedVariableList)[0]:
                        # the needed variable was not added to the sorted list yet
                        alldependenciesresovled = False
            if alldependenciesresovled==True:
                sortedVariableList.append([name,var])
        
        # all variables have been sorted now
        return sortedVariableList    
    ## --------------------------------------------------------------------------------------------




    ## returns all variables of an expression that are not followed by '[' ##
    def varsNoIndex(self,expr):
        # find all words not followed by [
        candidates = re.findall(r"\w+\b(?!\[)", expr)
        variables = []
        for var in candidates:
            if var[0].isalpha() or var[0] == '_':
                variables.append(var)
        return variables



    ## replaces all occurances of array variables with an instance i of that variable ( e.g. Jet_Pt -> Jet_Pt[3] ) ##
    def getArrayEntries(self,expr,i):
        print "getArrayEntries ", expr
        newexpr = expr
        variables = self.varsNoIndex(expr)
        for var in variables:
            print "search ", var
            if var in self.variables:
                print "found"
                if self.variables[var].arraylength == None:
                    print "no array"
                    continue
                # substitute v by v[i]
                rexp = (var.encode('string-escape')+r"+\b(?!\[)")
                newexpr = re.sub(rexp,var+'['+str(i)+']',newexpr)
                print "after subst ", newexpr
        return newexpr







    # returns map of maximum array indices of variables in an expression
    def varsWithMaxIndex(self,expr):
        # find all words followed by [
        variablescandidates = re.findall(r"\w+\b(?=\[)", expr)
        variables=[]
        maxidxs=[]
        for v in variablescandidates:
            if v[0].isalpha() or v[0]=='_':
                variables.append(v)
        variables=list(set(variables))
        arraylength={}
        for name,v in self.variables.iteritems():
            if v.arraylength == None:
                continue
            arraylength[name]=v.arraylength
        maxmap={}
        for v in variables:
            maxidx=-1
            lower=0
            while True:
                varstart=expr.find(v+'[',lower)
                if varstart>-1:
                    lower=varstart+len(v)+1
                else:
                    break
                upper=expr.find(']',lower)
                if lower > 0 and upper>0 and (varstart==0    or ( not expr[varstart-1].isalpha() and not expr[varstart-1] == '_' ) ):
                    idx=int(expr[lower:upper])
                    if idx>maxidx: maxidx=idx
            if arraylength[v] not in maxmap.keys() or maxmap[arraylength[v]]<maxidx:
                maxmap[arraylength[v]]=maxidx
        return maxmap













