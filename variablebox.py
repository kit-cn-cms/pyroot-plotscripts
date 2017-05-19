import os
import re
import ROOT
import xml.etree.ElementTree as ET
import collections 

class Variable():
  def __init__(self,name,expression='',vartype='F',arraylength=None):
    self.name=name
    self.vartype=vartype
    self.arraylength=arraylength
    if expression is '':
      self.expression=name
    else:
      self.expression=expression
    self.intree=False
    self.mvavar=False
    self.inputvariables=[]

  
  def initVar(self,tree,variables):
    
    if hasattr(tree,self.name):
      self.intree=True
      branch=tree.GetBranch(self.name)  
      branchtitle=branch.GetTitle()
      self.setupVarType(branchtitle)
      self.setupVarArray(tree,variables,branchtitle)
      return
      
    print self.name,'does not exist in tree!'
    
    self.intree=False
    self.vartype='F'
    
    self.setupMVAVar(tree,variables)
  
  def setupVarType(self,branchtitle):
    self.vartype=branchtitle.split('/')[1]
    
  
  def setupVarArray(self,tree,variables,branchtitle):
    varisarray=branchtitle.split('/')[0][-1]==']'
    
    if not varisarray:
      self.arraylength=None
      return
     
    self.arraylength=re.findall(r"\[(.*?)\]",branchtitle.split('/')[0])[0]
    
    variables.initVar(tree,self.arraylength,self.arraylength,'I')

      
  def setupMVAVar(self,tree,variables): 
    if not '.xml' in self.expression:
      self.mvavar=False
      return
    
    self.mvavar=True
  
    root = ET.parse(self.expression).getroot()
    for var in root.iter('Variable'):
      inputname=var.get('Internal')
      inputexpr=var.get('Expression')
      inputtype=var.get('Type')
      
      self.inputvariables.append(inputname)
      
      variables.initVar(tree,inputname,inputexpr,inputtype)

  
  # initialize new variable
  def initVarProgram(self):
    var=self.name
    t=self.vartype
    isarray=self.arraylength!=None
    if isarray:
      if t=='F':
        text='  float* '+var+' = new float[100];\n'
      elif t=='I':
        text='  int* '+var+' = new int[100];\n'
      else: "UNKNOWN TYPE",t
    else:
      if t=='F':
        text='  float '+var+' = -999;\n'
      elif t=='I':
        text='  int '+var+' = -999;\n'
      else: "UNKNOWN TYPE",t
    return text


  # setup branch address
  def initBranchAddressProgram(self):
    isarray=self.arraylength!=None
    text=''
    if isarray:
      text+='  chain->SetBranchAddress("'+self.name+'",'+self.name+');\n'
    else:
      text+='  chain->SetBranchAddress("'+self.name+'",&'+self.name+');\n'
    return text


  # initialize TMVA Reader
  def initReaderProgram(self):
    if not self.mvavar:
      print 'Error! Trying to Initialize TMVA reader for non MVA variable ',self.name,'!'
      return None
    text=''
    text+='  TMVA::Reader *r_'+self.name+' = new TMVA::Reader("Silent");\n'
    return text

  
  # add variables to TMVA Reader
  def addVariablesToReaderProgram(self,variables):
    if not self.mvavar:
      print 'Error! Trying to add input variables to TMVA reader for non MVA variable ',self.name,'!'
      return None
    
    text=''
    for varname in self.inputvariables:
      if not varname in variables.variables:
        print 'Error! Input variable ',varname,' does not exist in input collection!'
        return None
      
      var=variables.variables[varname]
      text+='  r_'+self.name+'->AddVariable("'+var.expression+'", &'+var.name+');\n'
    return text

  
  # book MVA Method
  def bookMVAProgram(self):
    if not self.mvavar:
      print 'Error! Trying to book MVA for non MVA variable ',self.name,'!'
      return None
    text='  r_'+self.name+'->BookMVA("BDT","'+self.expression+'");\n'
    return text

  
  # setup TMVA Reader
  def setupTMVAReaderProgram(self,variables):
    if not self.mvavar:
      print 'Error! Trying to setup TMVA Reader for non MVA variable ',self.name,'!'
      return None
    text=''
    text+=self.initReaderProgram()
    text+=self.addVariablesToReaderProgram(variables)
    text+=self.bookMVAProgram()
    text+='\n'
    return text
  
  
  # calculate variables not in Tree and MVA variables
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
    self.variables={}
    self.vetolist=veto
  
  # returns all variables of an expression
  def varsIn(self,expr):
    # find all words not followed by ( (these are functions)
    variablescandidates = re.findall(r"\w+\b(?!\()", expr)
    variables=[]
    for v in variablescandidates:
      if v[0].isalpha() or v[0]=='_':
        variables.append(v)
    return variables


  # returns all variables of an expression that are not followed by [ (e.g. variable[0])
  def varsNoIndex(self,expr):
    # find all words not followed by [
    variablescandidates = re.findall(r"\w+\b(?!\[)", expr)
    variables=[]
    for v in variablescandidates:
      if v[0].isalpha() or v[0]=='_':
        variables.append(v)
    return variables


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
        if lower > 0 and upper>0 and (varstart==0  or ( not expr[varstart-1].isalpha() and not expr[varstart-1] == '_' ) ):
          idx=int(expr[lower:upper])
          if idx>maxidx: maxidx=idx
      if arraylength[v] not in maxmap.keys() or maxmap[arraylength[v]]<maxidx:
        maxmap[arraylength[v]]=maxidx
    return maxmap


  # returns maximum array indices selection of variables in an expression
  def checkArrayLengths(self,expr):
    maxidxs=self.varsWithMaxIndex(expr)
    arrayselection="1"
    for v in maxidxs.keys():
      arrayselection+='&&'+v+'>'+str(maxidxs[v])
    return arrayselection

  
  # replaces all occurances of array variables with an instance i of that variable ( e.g. Jet_Pt -> Jet_Pt[3] )
  def getArrayEntries(self,expr,i):
    print "getArrayEntries ", expr
    newexpr=expr
    variables=self.varsNoIndex(expr)
    print variables
    print self.variables
    for v in variables:
      print "search ", v
      if v in self.variables:
	print "found"
        if self.variables[v].arraylength==None:
	  print "no array"
          continue
        # substitute v by v[i]
        rexp=(v.encode('string-escape')+r"+\b(?!\[)")
        newexpr=re.sub(rexp,v+'['+str(i)+']',newexpr)
        print "after subst ", newexpr
    return newexpr
  
  
  # initialize variable
  def initVar(self,tree,name,expression='',vartype='F',arraylength=None):
    #print "initVar", tree,name,expression
    if not name in self.variables and not name in self.vetolist:
      
      if not ".xml" in expression and not hasattr(tree,expression):
        self.initVarsFromExpr(expression,tree)
        print expression
        
      self.variables[name]=Variable(name,expression,vartype,arraylength)
      self.variables[name].initVar(tree,self)
  
  
  # initialize variables from expression
  def initVarsFromExpr(self,expr,tree):
    print "initVarsFromExpr",expr,tree
    if ":=" in expr:
      name,expr=expr.split(":=")
      
      if not ".xml" in expr:
        self.initVarsFromExpr(expr,tree)
      
      self.initVar(tree,name,expr,'F')
    
    #else if "function_":
      #name,expr=espr.split("function_")
      #self.
        
    else:
      variablenames=self.varsIn(expr)
      
      for name in variablenames:
	#print name
        self.initVar(tree,name,name,'F')  
  
  # initialize variables from expression list
  def initVarsFromExprList(self,exprlist,tree):
    for expr in exprlist:
      print expr
      self.initVarsFromExpr(expr,tree)
  
  
  # Program: Initialize all variables        
  def initVarsProgram(self):
    text=""
    for name,var in self.variables.iteritems():
      text+=var.initVarProgram()
    text+='\n'
    return text
  
  
  # Program: Setup all branch addresses      
  def initBranchAddressesProgram(self):
    text=""
    for name,var in self.variables.iteritems():
      if var.intree:
        text+=var.initBranchAddressProgram()
    text+='\n'
    return text


  # Program: Setup all TMVA readers
  def setupTMVAReadersProgram(self):
    text=""
    for name,var in self.variables.iteritems():
      if var.mvavar:
        text+=var.setupTMVAReaderProgram(self)
    return text
  
  
   
  ## Program: Setup all branch addresses      
  #def calculateVarsProgram(self):
    #text=""
    #for name,var in self.variables.iteritems():
      #text+=var.calculateVarProgram()
    #text+='\n'
    #return text
  
  # Program: Setup all branch addresses      
  def calculateVarsProgram(self):
    text=""
    rawVariableList=[]
    sortedVariableList=[]
    print "print figuring out variable dependencies"
    for name,var in self.variables.iteritems():
      rawVariableList.append([name,var])
    print'rawVariableList', rawVariableList
    #rawInput()
    allVariablesHandled=False
    nVariables=len(rawVariableList)
    print "nVariables", nVariables
    variableCounter=-1
    iterationcounter=0
    while allVariablesHandled==False:
      #print'rawVariableList', rawVariableList
      print'sortedVariableList', sortedVariableList
      variableCounter+=1
      #print 'index ',variableCounter, ' of ',nVariables
      if len(sortedVariableList)>len(rawVariableList):
	print "PROBLEM: sorted list longer than raw list?"
	print rawVariableList
	print sortedVariableList
	exit(0)
      name, var = rawVariableList[variableCounter]
      # begin from begging of the raw list again
      #print len(sortedVariableList)
      if variableCounter==nVariables-1:
	print "starting loop from the beginning"
	iterationcounter+=1
	#print iterationcounter
        #print'sortedVariableList so far', sortedVariableList
	variableCounter=-1
      if len(sortedVariableList)>0:
	if name in zip(*sortedVariableList)[0]:
	  ##already have this variable
	  #print 'continue0'
	  continue
      print "considering ", name, var
      if var.name==var.expression:
	sortedVariableList.append([name,var])
	#print 'continue1'
	continue
      if var.mvavar==True:
	sortedVariableList.append([name,var])
	#print 'continue2'
	continue
      if var.intree==True:
	sortedVariableList.append([name,var])
	#print 'continue3'
	continue
      alldependenciesresovled=True
      for dvar in zip(*rawVariableList)[0]:
	if dvar in var.expression:
          print 'here', dvar, '   ', var.expression, '   '
	  if dvar not in zip(*sortedVariableList)[0]:
	    # the needed variable was not added to the sorted list yet
	    print 'the needed variable was not added to the sorted list yet',
	    print 'found ', dvar, ' in ', var.expression
	    print 'but could not find',dvar ,' in',  zip(*sortedVariableList)[0]
	    alldependenciesresovled=False
      if alldependenciesresovled==True:
	sortedVariableList.append([name,var])
      if collections.Counter(zip(*sortedVariableList)[0])==collections.Counter(zip(*rawVariableList)[0]):
	if len(rawVariableList)!=len(sortedVariableList):
	  print "PROBLEM: lists have different lengths"
	  print rawVariableList
	  print sortedVariableList
	  exit(0)
	# this will get the element with the most entries in the list and also how often it appears. If there are more than one it does not matter her
	MaxOcc, numMaxOcc=collections.Counter(zip(*sortedVariableList)[0]).most_common(1)[0]
	if numMaxOcc!=1:
	  print "PROBLEM: sorted list contains the same entry multiple times"
	  print MaxOcc, numMaxOcc
	  exit(0)
	allVariablesHandled=True
	
	
    # now write the code for each variable
    for name,var in sortedVariableList:
      print "writing code for ", var.name
      text+=var.calculateVarProgram()
    text+='\n'
    return text
