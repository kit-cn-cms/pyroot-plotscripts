import ROOT
import glob
import xml.etree.ElementTree as ET

ROOT.gStyle.SetPaintTextFormat("4.2f");
ROOT.gROOT.SetBatch(True)

class SampleDictionary:
  def __init__(self):
    self.samplemap={}
    
  def addToMap(self,path,files):
    if not self.samplemap.has_key(path):
      self.samplemap[path]=files
    else:
      print "already have this key", path
  
  def hasKey(self,path):
    if self.samplemap.has_key(path):
      return True
  
  def getFiles(self,path):
    if self.samplemap.has_key(path):
      return self.samplemap[path]
    else:
      print "key not in sample dictionary"
      return []
  
  def doPrintout(self):
    print self.samplemap

class Sample:
    def __init__(self, name, color = ROOT.kBlack, path = '', selection = '',
            nick = '', origName = '', up = 0, down = None, samDict = "",
            addsamples = None, plot = True, vetoEventWeights = None,
            readTrees = True, filterFile = "NONE", checknevents = -1, 
            treename = 'MVATree',typ="bkg"):

        self.name = name
        self.color = color
        self.path = path
        self.plot = plot

        self.selection = selection
        self.files = []
        self.filterFile = filterFile
        self.addsamples=addsamples
        subpaths = path.split(";")

        self.vetoEventWeights = vetoEventWeights
        # allow globbing samples from different paths
        if readTrees:
          if samDict != "":
            if not samDict.hasKey(self.path):  
              print("globbing files for "+str(name))#, self.path
              for sp in subpaths:
                self.files += glob.glob(sp)
                if sp != '' and len(self.files) == 0:
                  print name
                  print 'no files found at',sp
              samDict.addToMap(path, self.files)
            else:
              #print("map already knows this sample "+str(self.path))
              self.files = samDict.getFiles(path)
          else:
            print "empty map: globbing files for", name, self.path
            for sp in subpaths:
                self.files += glob.glob(sp)
                if sp!='' and len(self.files)==0:
                  print name
                  print 'no files found at', sp
	  
        if nick == '':
            self.nick = name
        else:
            self.nick = nick
        if origName == '':
            self.origName = self.nick
        else:
            self.origName = origName
        self.typ=typ
        #self.shape_unc = listOfShapes
        self.unc_up = up
        self.unc_down = up
        if down != None:
            self.unc_down = down

    def setShapes(self,listOfShapes):
        self.shape_unc=listOfShapes

    def getShapes(self):
        if self.shape_unc:
            return self.shape_unc
        else:
            return "ERROR: no shapes for this sample"


    def checkNevents():
        if checknevents > 0:
            nevents = 0
            for fn in self.files:
                f = ROOT.TFile(fn)
                t = f.Get('MVATree')
                nevents += t.GetEntries()
            if nevents != checknevents:
                print 'wrong number of events in',self.name,':',nevents,'!=',checknevents
                if not askYesNo('cancel?'): sys.exit()



    def GetTree(self, treename = 'MVATree'):
        chain = ROOT.TChain(treename)
        for f in self.files:
            chain.Add(f)
        return chain

    def addSamples(self):
        if addsamples:
            return self.addsamples 
        else:
            return [self.nick]


class Plot:
    def __init__(self, histo, variable = '', selection = '',label = '', variable_bin_width = False):
        if isinstance(histo,ROOT.TH1):
            self.histo = histo
            self.name = histo.GetName()
        else:
            self.name = histo
        if variable == '':
            if isinstance(histo,ROOT.TH1):
                self.variable = histo.GetName()
        else:
            self.variable = variable
        self.selection = selection
        self.label = label
        self.dim = 1
        self.variable_bin_width = variable_bin_width

class TwoDimPlot:
    def __init__(self, histo, variable1 = '', variable2 = '', selection = '',label = ''):
        if isinstance(histo,ROOT.TH2):
            self.histo = histo
            self.name = histo.GetName()
        else:
            self.name = histo
        #if variable=='':
            #if isinstance(histo,ROOT.TH1):
                #self.variable=histo.GetName()
        #else:
        self.variable1 = variable1
        self.variable2 = variable2
        self.selection = selection
        self.label = label
        self.dim = 2

class MVAPlot:
    def __init__(self,histo, weightfile, selection='',label=''):
        self.histo = histo
        self.weightfile = weightfile
        self.selection = selection
        if selection =='':
            self.selection = '1'
        self.name = histo.GetName()
        self.parseWeights(weightfile)
        self.label = label
    def parseWeights(self,weightfile):
        root = ET.parse(weightfile).getroot()
        exprs = []
        names = []
        mins = []
        maxs = []
        types = []
        for var in root.iter('Variable'):
            exprs.append(var.get('Expression'))
            names.append(var.get('Internal'))
            mins.append(var.get('Min'))
            maxs.append(var.get('Max'))
            types.append(var.get('Type'))
        self.input_exprs = exprs
        self.input_names = names
        self.input_mins = mins
        self.input_maxs = maxs
        self.input_types = types

class Cateogry:
    def __init__(self, name, title, selection):
        self.name = name
        self.title = title
        self.selection = selection

