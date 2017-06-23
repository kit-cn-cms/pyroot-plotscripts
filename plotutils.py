import ROOT
import math
from itertools import product
from collections import namedtuple
import glob
import subprocess
import os
import scriptgenerator
import re
import xml.etree.ElementTree as ET
import CMS_lumi
import copy
from ROOT import TMinuit
from ROOT import TVirtualFitter
from ROOT import TMath
from ROOT import TF1
# from ROOT import gStyle
import array

ROOT.gStyle.SetPaintTextFormat("4.2f");
ROOT.gStyle.SetOptFit(1111);
ROOT.gStyle.SetOptStat(0000);
ROOT.gROOT.SetBatch(False)

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
    def __init__(self,name, color=ROOT.kBlack, path='', selection='',nick='',listOfShapes=[],up=0,down=None,samDict="",checknevents=-1,treename='MVATree'):
        self.name=name
        self.color=color
        self.path=path
        self.selection=selection
        self.files=[]
        subpaths=path.split(";")
        # allow globbing samples from different paths
        if samDict!="":
	  if not samDict.hasKey(self.path):  
	    print "globbing files for", name, self.path
	    for sp in subpaths:
	      self.files+=glob.glob(sp)
	      if sp!='' and len(self.files)==0:
		print name
		print 'no files found at',sp
	    samDict.addToMap(path,self.files)
	  else:
	    print "map already knows this sample", self.path
	    self.files=samDict.getFiles(path)
	else:
          print "empty map: globbing files for", name, self.path
	  for sp in subpaths:
	      self.files+=glob.glob(sp)
	      if sp!='' and len(self.files)==0:
		print name
		print 'no files found at',sp
	  
        if nick=='':
            self.nick=name
        else:
            self.nick=nick
        self.shape_unc=listOfShapes
        self.unc_up=up
        self.unc_down=up
        if down!=None:
            self.unc_down=down



    def checkNevents():
        if checknevents>0:
            nevents=0
            for fn in self.files:
                f=ROOT.TFile(fn)
                t=f.Get('MVATree')
                nevents+=t.GetEntries()
            if nevents != checknevents:
                print 'wrong number of events in',self.name,':',nevents,'!=',checknevents
                if not askYesNoQuestion('cancel?'): sys.exit()



    def GetTree(self,treename='MVATree'):
        chain=ROOT.TChain(treename)
        for f in self.files:
            chain.Add(f)
        return chain


class Plot:
    def __init__(self,histo, variable='', selection='',label=''):
        if isinstance(histo,ROOT.TH1):
            self.histo=histo
            self.name=histo.GetName()
        else:
            self.name=histo
        if variable=='':
            if isinstance(histo,ROOT.TH1):
                self.variable=histo.GetName()
        else:
            self.variable=variable
        self.selection=selection
        self.label=label

class TwoDimPlot:
    def __init__(self,histo, variable1='', variable2='', selection='',label=''):
        if isinstance(histo,ROOT.TH2):
            self.histo=histo
            self.name=histo.GetName()
        else:
            self.name=histo
        #if variable=='':
            #if isinstance(histo,ROOT.TH1):
                #self.variable=histo.GetName()
        #else:
        self.variable1=variable1
        self.variable2=variable2
        self.selection=selection
        self.label=label


class MVAPlot:
    def __init__(self,histo, weightfile, selection='',label=''):
        self.histo=histo
        self.weightfile=weightfile
        self.selection=selection
        if selection =='':
            self.selection='1'
        self.name=histo.GetName()
        self.parseWeights(weightfile)
        self.label=label
    def parseWeights(self,weightfile):
        root = ET.parse(weightfile).getroot()
        exprs=[]
        names=[]
        mins=[]
        maxs=[]
        types=[]
        for var in root.iter('Variable'):
            exprs.append(var.get('Expression'))
            names.append(var.get('Internal'))
            mins.append(var.get('Min'))
            maxs.append(var.get('Max'))
            types.append(var.get('Type'))
        self.input_exprs=exprs
        self.input_names=names
        self.input_mins=mins
        self.input_maxs=maxs
        self.input_types=types

class Cateogry:
    def __init__(self,name,title,selection):
        self.name=name
        self.title=title
        self.selection=selection
    


# sets up the style of a histo and its axes
def setupHisto(histo,color,yTitle=None,filled=False):
    if isinstance(histo,ROOT.TH1):
        histo.SetStats(False)
    print histo.GetTitle()
    if not isinstance(histo,ROOT.TH2):   
      if histo.GetYaxis().GetTitle()=="":
	#print "setting up title"
	if histo.GetTitle()!='':
	    histo.GetXaxis().SetTitle(histo.GetTitle())
	    histo.SetTitle('')
	if yTitle!=None:
	    histo.GetYaxis().SetTitle(yTitle)
    if isinstance(histo,ROOT.TH2):
      if histo.GetXaxis().GetTitle()=="" and "VS" in histo.GetTitle() :
	histo.GetXaxis().SetTitle(histo.GetTitle().split("VS",1)[0])
      if histo.GetYaxis().GetTitle()=="" and "VS" in histo.GetTitle() :
	histo.GetYaxis().SetTitle(histo.GetTitle().split("VS",1)[1])
      histo.SetTitle('')
    histo.GetYaxis().SetTitleOffset(1.3)
    histo.GetXaxis().SetTitleOffset(1.2)
    histo.GetYaxis().SetTitleSize(0.05)
    histo.GetXaxis().SetTitleSize(0.05)
    histo.GetYaxis().SetLabelSize(0.05)
    histo.GetXaxis().SetLabelSize(0.05)
    histo.SetMarkerColor(color)
    if filled:
        histo.SetLineColor( ROOT.kBlack )
        histo.SetFillColor( color )
        histo.SetLineWidth(2)
    else:
        histo.SetLineColor(color)
        histo.SetLineWidth(2)

# creates a canvas either with or without ratiopad
def getCanvas(name,ratiopad=False, colz=False):
    if ratiopad:
        c=ROOT.TCanvas(name,name,1024,1024)
        c.Divide(1,2)
        c.cd(1).SetPad(0.,0.3,1.0,1.0);
        c.cd(1).SetBottomMargin(0.0);
        c.cd(2).SetPad(0.,0.0,1.0,0.3);
        c.cd(2).SetTopMargin(0.0);
        c.cd(1).SetTopMargin(0.07);
        c.cd(2).SetBottomMargin(0.4);
        c.cd(1).SetRightMargin(0.05);
        c.cd(1).SetLeftMargin(0.15);
        c.cd(2).SetRightMargin(0.05);
        c.cd(2).SetLeftMargin(0.15);
        c.cd(2).SetTicks(1,1)
        c.cd(1).SetTicks(1,1)
    else:
        c=ROOT.TCanvas(name,name,1024,768)
        c.SetRightMargin(0.05)
        c.SetTopMargin(0.07)
        c.SetLeftMargin(0.15)
        c.SetBottomMargin(0.15)
        c.SetTicks(1,1)
	if colz:
		c.SetRightMargin(0.2)

    return c

def getCanvasLowRes(name,ratiopad=False):
    if ratiopad:
        c=ROOT.TCanvas(name,name,800,600)
        c.Divide(1,2)
        c.cd(1).SetPad(0.,0.3,1.0,1.0);
        c.cd(1).SetBottomMargin(0.0);
        c.cd(2).SetPad(0.,0.0,1.0,0.3);
        c.cd(2).SetTopMargin(0.0);
        c.cd(1).SetTopMargin(0.05);
        c.cd(2).SetBottomMargin(0.4);
        c.cd(1).SetRightMargin(0.05);
        c.cd(1).SetLeftMargin(0.15);
        c.cd(2).SetRightMargin(0.05);
        c.cd(2).SetLeftMargin(0.15);
    else:
        c=ROOT.TCanvas(name,name,800,600)
        c.SetRightMargin(0.05)
        c.SetTopMargin(0.05)
        c.SetLeftMargin(0.15)
        c.SetBottomMargin(0.15)

    return c

# creates legend
def getLegend(): 
    legend=ROOT.TLegend()
    legend.SetX1NDC(0.85)
    legend.SetX2NDC(0.95)
    legend.SetY1NDC(0.92)
    legend.SetY2NDC(0.93)
    legend.SetBorderSize(0);
    legend.SetLineStyle(0);
    legend.SetTextFont(42);
    legend.SetTextSize(0.02);
    #legend.SetTextSize(0.05);
    legend.SetFillStyle(0);
    return legend

def getLegendL(): 
    legend=ROOT.TLegend()
    legend.SetX1NDC(0.6)
    legend.SetX2NDC(0.76)
    legend.SetY1NDC(0.9)
    legend.SetY2NDC(0.91)
    legend.SetBorderSize(0);
    legend.SetLineStyle(0);
    legend.SetTextFont(42);
    legend.SetTextSize(0.04);
    legend.SetFillStyle(0);
    return legend

def getLegendR(): 
    legend=ROOT.TLegend()
    legend.SetX1NDC(0.76)
    legend.SetX2NDC(0.93)
    legend.SetY1NDC(0.9)
    legend.SetY2NDC(0.91)
    legend.SetBorderSize(0);
    legend.SetLineStyle(0);
    legend.SetTextFont(42);
    legend.SetTextSize(0.04);
    legend.SetFillStyle(0);
    return legend


def getLegend2(): 
    legend=ROOT.TLegend()
    legend.SetX1NDC(0.85)
    legend.SetX2NDC(0.99)
    legend.SetY1NDC(0.92)
    legend.SetY2NDC(0.93)
    legend.SetBorderSize(0);
    legend.SetLineStyle(0);
    legend.SetTextFont(42);
    legend.SetTextSize(0.04);
    legend.SetFillStyle(0);
    return legend

# returns tlatex item with results of chi2 and KS test between two histograms
def getStatTests(h1,h2,option="WW"):
    ksprob = h1.KolmogorovTest(h2)
    chi2prob = h1.Chi2Test(h2,option)
    tests = ROOT.TLatex(0.2, 0.8, '#splitline{p(KS): '+str(round(ksprob,3))+'}{p(chi2): '+str(round(chi2prob,3))+'}'  );
    tests.SetTextFont(42);
    tests.SetTextSize(0.03);
    tests.SetNDC()
    return tests

def getStatTestsList(h1,lh2,option="WW"):
    mystrng=''
    ss=[]
    for h2 in lh2:      
      ksprob = h1.KolmogorovTest(h2)
      chi2prob = h1.Chi2Test(h2,option)
      #mystrng+='#splitline{p(KS): '+str(round(ksprob,3))+'}{p(chi2): '+str(round(chi2prob,3))+'}'
      ss.append('p(KS): '+str(round(ksprob,3))+'   p(chi2): '+str(round(chi2prob,3)))
    if len(ss)==1:
      mystrng=ss[0]
    else:
      mystrng='#splitline{'+ss[0]+'}{secline}'
      for isss, sss in enumerate(ss[1:]):
	submystrng='#splitline{'+sss+'}{secline}'
	if isss==(len(ss[1:])-1):
	  mystrng=mystrng.replace('secline',sss)
	else:
	  mystrng=mystrng.replace('secline',submystrng)
    tests = ROOT.TLatex(0.2, 0.8, mystrng  );
    tests.SetTextFont(42);
    tests.SetTextSize(0.04);
    tests.SetNDC()
    return tests

# calculates separation of two histogram (using the ROC integral of)
def getSepaTests(h1,h2):
#    pair=getSuperHistoPair([h1],[h2],'tmp')
    pair=h1,h2
    roc=getROC(*pair)
    rocint=roc.Integral()+0.5
    tests = ROOT.TLatex(0.2, 0.9, 'ROC integral: '+str(round(rocint,3)));
    tests.SetTextFont(42);
    tests.SetTextSize(0.05);
    tests.SetNDC()
    return tests

def getSepaTests2(hs,h1):
    y=0
    tests=[]
    for h in hs:
        pair=getSuperHistoPair([h1],[h],'tmp')
        roc=getROC(*pair)
        rocint=roc.Integral()+0.5
        test = ROOT.TLatex(0.2, 0.9-y, 'ROC integral: '+str(round(rocint,3)));
        y+=0.05
        test.SetTextFont(42);
        test.SetTextSize(0.04);
        test.SetNDC()
        tests.append(test)
        
    return tests


# draws a list of histos on a canvas and returns canvas
def drawHistosOnCanvas(listOfHistos_,normalize=True,stack=False,logscale=False,options_='histo',ratio=False,DoProfile=False):
    listOfHistos=[h.Clone(h.GetName()+'_drawclone') for h in listOfHistos_]
    canvas=getCanvas(listOfHistos[0].GetName(),ratio)        
    #prepare drawing

    # mover over/underflow
    for h in listOfHistos:
        h.SetBinContent(1,h.GetBinContent(0)+h.GetBinContent(1));
        h.SetBinContent(h.GetNbinsX(),h.GetBinContent(h.GetNbinsX()+1)+h.GetBinContent(h.GetNbinsX()));
        h.SetBinError(1,ROOT.TMath.Sqrt(ROOT.TMath.Power(h.GetBinError(0),2)+ROOT.TMath.Power(h.GetBinError(1),2)));
        h.SetBinError(h.GetNbinsX(),ROOT.TMath.Sqrt(ROOT.TMath.Power(h.GetBinError(h.GetNbinsX()+1),2)+ROOT.TMath.Power(h.GetBinError(h.GetNbinsX()),2)));

    if normalize and not stack:
        for h in listOfHistos:
            if h.Integral()>0.:
                h.Scale(1./h.Integral())

    if stack:
        for i in range(len(listOfHistos)-1,0,-1):
            listOfHistos[i-1].Add(listOfHistos[i])
        if normalize:
            integral0=listOfHistos[0].Integral()
            for h in listOfHistos:
                h.Scale(1./integral0)

            
    canvas.cd(1)
    yMax=1e-9
    yMinMax=1000.
    for h in listOfHistos:
        yMax=max(h.GetBinContent(h.GetMaximumBin()),yMax)
        if h.GetBinContent(h.GetMaximumBin())>0:
            yMinMax=min(h.GetBinContent(h.GetMaximumBin()),yMinMax)
    #draw first
    h=listOfHistos[0]
    if logscale:
        h.GetYaxis().SetRangeUser(yMinMax/10000,yMax*10)
        canvas.SetLogy()
    else:
        h.GetYaxis().SetRangeUser(0,yMax*1.5)
    option='histo'
    option+=options_
    h.DrawCopy(option)
    #draw remaining
    for h in listOfHistos[1:]:
        h.DrawCopy(option+'same')
    h.DrawCopy('axissame')
    
    #h.DrawCopy('axissame')
    if ratio:
        canvas.cd(2)
        line=listOfHistos[0].Clone()
        line.Divide(listOfHistos[0])
        line.GetYaxis().SetRangeUser(0.5,1.5)
        line.GetYaxis().SetTitle('#frac{Data}{MC Sample}')
        line.GetXaxis().SetLabelSize(line.GetXaxis().GetLabelSize()*2.4)
        line.GetYaxis().SetLabelSize(line.GetYaxis().GetLabelSize()*2.4)
        line.GetXaxis().SetTitleSize(line.GetXaxis().GetTitleSize()*3)
        line.GetYaxis().SetTitleSize(line.GetYaxis().GetTitleSize()*1.5)
        line.GetYaxis().SetTitleOffset(0.9)
        line.GetYaxis().SetNdivisions(505)
        for i in range(line.GetNbinsX()+1):
            line.SetBinContent(i,1)
            line.SetBinError(i,0)
        line.SetLineWidth(1)
        line.DrawCopy('histo')
        for hist in listOfHistos[1:]:
            ratio=hist.Clone()
            ratio.Divide(listOfHistos[0])
            ratio.DrawCopy('sameP')
        canvas.cd(1)
    return canvas

def drawHistosOnCanvas2D(listOfHistos_,normalize=True,stack=False,logscale=False,options_='',ratio=False,DoProfile=False,statTest=False, samples=None):
    # print 'drawing 2d'
 #   raw_input()
 
    listOfHistos=[h.Clone(h.GetName()+'_drawclone') for h in listOfHistos_]
    canvas = []
    if options_ == "colz":
        for h, sample in zip(listOfHistos, samples):
            canvas_tmp = getCanvas(h.GetName(),False, True)
            #canvas_tmp.SetLogz() #Uncomment for logarithmic z Axis
            h.SetTitle(sample.name)
            ROOT.gStyle.SetTitleFontSize(0.03)
            h.DrawCopy(options_)
            canvas.append(canvas_tmp)

    
    else:
        canvas_tmp = getCanvas(listOfHistos[0].GetName(),False) #from here: Fix canvas as list, not element!      
        print 'canvas name',canvas_tmp.GetName()
        #raw_input()

        #prepare drawing

        # mover over/underflow
        for h in listOfHistos:
            nBinsX=h.GetNbinsX()
            nBinsY=h.GetNbinsY()
            allbins=[]
            edgebins=[]
            for ibx in range(1,nBinsX+1):
                for iby in range(1,nBinsY+1):
                    allbins.append((ibx,iby))
            for b in allbins:
                if b[0]==1 or b[0]==nBinsX or b[1]==1 or b[1]==nBinsY:
                    edgebins.append(b)
            
            surrounding=[-1,0,1]
            for b in edgebins:
                binsToAdd=[b]
                    #for sx in surrounding:
                        #for sy in surrounding:
                            #touchingbin=(b[0]+sx,b[1]+sy)
                            #if touchingbin not in allbins:
                                #binsToAdd.append(touchingbin)
            if b[0]==1:
                binsToAdd.append((b[0]-1,b[1]))
            if b[0]==nBinsX:
                binsToAdd.append((b[0]+1,b[1]))
            if b[1]==1:
                binsToAdd.append((b[0],b[1]-1))
            if b[1]==nBinsY:
                binsToAdd.append((b[0],b[1]+1))
            if b[0]==1 and b[1]==1:
                binsToAdd.append((b[0]-1,b[1]-1))
            if b[0]==1 and b[1]==nBinsY:
                binsToAdd.append((b[0]-1,b[1]+1))
            if b[0]==nBinsX and b[1]==1:
                binsToAdd.append((b[0]+1,b[1]-1))
            if b[0]==nBinsX and b[1]==nBinsY:
                binsToAdd.append((b[0]+1,b[1]+1))

            #print "adding bins ", binsToAdd
            addedContents=0.0
            addedSquaredError=0.0
            for addb in binsToAdd:
                addedContents+=h.GetBinContent(addb[0],addb[1])
                addedSquaredError+=ROOT.TMath.Power(h.GetBinError(addb[0],addb[1]),2)
            h.SetBinContent(b[0],b[1],addedContents)
            h.SetBinError(b[0],b[1],ROOT.TMath.Sqrt(addedSquaredError));
                
        if normalize and not stack:
            for h in listOfHistos:
                if h.Integral()>0.:
                    h.Scale(1./h.Integral())

        if stack:
            for i in range(len(listOfHistos)-1,0,-1):
                listOfHistos[i-1].Add(listOfHistos[i])
            if normalize:
                integral0=listOfHistos[0].Integral()
                for h in listOfHistos:
                    h.Scale(1./integral0)

                    
        canvas_tmp.cd(1)
        #yMax=1e-9
        #yMinMax=1000.
        #for h in listOfHistos:
            #yMax=max(h.GetBinContent(h.GetMaximumBin()),yMax)
            #if h.GetBinContent(h.GetMaximumBin())>0:
                #yMinMax=min(h.GetBinContent(h.GetMaximumBin()),yMinMax)
        #draw first
        h=listOfHistos[0]
        #if logscale:
            #h.GetYaxis().SetRangeUser(yMinMax/10000,yMax*10)
            #canvas.SetLogy()
        #else:
            #h.GetYaxis().SetRangeUser(0,yMax*1.5)
        option=''
        option+=options_
        if option=='':
            option='scat=5000.0'
        h.DrawCopy(option)
        #draw remaining
        for h in listOfHistos[1:]:
            h.DrawCopy(option+'same')
        h.DrawCopy('axissame')
        canvas.append(canvas_tmp)
    
    tests=None
    if DoProfile:
        profilesx=[]
        canvas_tmp = getCanvas(listOfHistos[0].GetName()+"_XProfile", False)
        max_y = 0
        #leg = getLegend()
        for h, sample in zip(listOfHistos, samples):
            #Find maimum of TPfofile Yaxis
            max_tmp = h.GetYaxis().GetBinUpEdge( h.GetNbinsY() )
            if max_tmp > max_y:
                max_y = max_tmp
            profilesx.append(h.ProfileX("profx_"+h.GetName(),1,h.GetNbinsX(),""))
            profilesx[-1].SetLineColor(h.GetLineColor())
            profilesx[-1].SetLineWidth(2)
            profilesx[-1].SetTitle(listOfHistos[0].GetName()+"_XProfile")
            profilesx[-1].GetYaxis().SetRangeUser(0. ,max_y)
            profilesx[-1].Draw("same")
            
        #for px,sample in zip(profilesx,samples):    
            #leg.AddEntry4545( "profx_"+h.GetName(), sample.name , "L")
        #leg.Draw("same")
        canvas.append(canvas_tmp)
        
        profilesy = []
        canvas_tmp = getCanvas(listOfHistos[0].GetName()+"_YProfile", False)
        max_x = 0
        for h, sample in zip(listOfHistos, samples):
            #Find maimum of TPfofile Yaxis
            max_tmp = h.GetXaxis().GetBinUpEdge( h.GetNbinsX() )
            if max_tmp > max_x:
                max_x = max_tmp
            profilesy.append(h.ProfileY("profy_"+h.GetName(),1,h.GetNbinsY(),""))
            profilesy[-1].SetLineColor(h.GetLineColor())
            profilesy[-1].SetLineWidth(2)
            profilesy[-1].SetTitle(listOfHistos[0].GetName()+"_YProfile")
            profilesy[-1].GetYaxis().SetRangeUser(0.,max_x)
            profilesy[-1].Draw("same")
        canvas.append(canvas_tmp)
        
        
    if statTest:
    #print "doing 2D stat test"
        tests=getStatTestsList(profiles[0],profiles[1:],"WW") #profiles has been renamed
            #print tests
            #tests.Draw()
            #objects.append(tests)
        #h.DrawCopy('axissame')
    
    #if ratio:
        #canvas.cd(2)
        #line=listOfHistos[0].Clone()
        #line.Divide(listOfHistos[0])
        #line.GetYaxis().SetRangeUser(0.5,1.5)
        #line.GetYaxis().SetTitle('#frac{Sample}{Nominal Sample}')
        #line.GetXaxis().SetLabelSize(line.GetXaxis().GetLabelSize()*2.4)
        #line.GetYaxis().SetLabelSize(line.GetYaxis().GetLabelSize()*2.4)
        #line.GetXaxis().SetTitleSize(line.GetXaxis().GetTitleSize()*3)
        #line.GetYaxis().SetTitleSize(line.GetYaxis().GetTitleSize()*1.5)
        #line.GetYaxis().SetTitleOffset(0.9)
        #line.GetYaxis().SetNdivisions(505)
        #for i in range(line.GetNbinsX()+1):
            #line.SetBinContent(i,1)
            #line.SetBinError(i,0)
        #line.SetLineWidth(1)
        #line.DrawCopy('histo')
        #for hist in listOfHistos[1:]:
            #ratio=hist.Clone()
            #ratio.Divide(listOfHistos[0])
            #ratio.DrawCopy('sameP')
        #canvas.cd(1)      
    # print 'name2', canvas.GetName()
# raw_input()
    if not DoProfile:
        return canvas, tests
    else:
        return canvas, tests, profilesx, profilesy

def drawHistosOnCanvasAN(listOfHistos_,normalize=True,stack=False,logscale=False,options_='histo',ratio=False):
    listOfHistos=[h.Clone(h.GetName()+'_drawclone') for h in listOfHistos_]
    canvas=getCanvas(listOfHistos[0].GetName(),ratio)        
    #prepare drawing

    # mover over/underflow
    for h in listOfHistos:
        h.SetBinContent(1,h.GetBinContent(0)+h.GetBinContent(1));
        h.SetBinContent(h.GetNbinsX(),h.GetBinContent(h.GetNbinsX()+1)+h.GetBinContent(h.GetNbinsX()));
        h.SetBinError(1,ROOT.TMath.Sqrt(ROOT.TMath.Power(h.GetBinError(0),2)+ROOT.TMath.Power(h.GetBinError(1),2)));
        h.SetBinError(h.GetNbinsX(),ROOT.TMath.Sqrt(ROOT.TMath.Power(h.GetBinError(h.GetNbinsX()+1),2)+ROOT.TMath.Power(h.GetBinError(h.GetNbinsX()),2)));

    if normalize and not stack:
        for h in listOfHistos:
            if h.Integral()>0.:
                h.Scale(1./h.Integral())

    if stack:
        for i in range(len(listOfHistos)-1,0,-1):
            listOfHistos[i-1].Add(listOfHistos[i])
        if normalize:
            integral0=listOfHistos[0].Integral()
            for h in listOfHistos:
                h.Scale(1./integral0)

            
    canvas.cd(1)
    yMax=1e-9
    yMinMax=1000.
    for h in listOfHistos:
        yMax=max(h.GetBinContent(h.GetMaximumBin()),yMax)
        if h.GetBinContent(h.GetMaximumBin())>0:
            yMinMax=min(h.GetBinContent(h.GetMaximumBin()),yMinMax)
    #draw first
    h=listOfHistos[0]
    if logscale:
        h.GetYaxis().SetRangeUser(yMinMax/10000,yMax*10)
        canvas.SetLogy()
    else:
        h.GetYaxis().SetRangeUser(0,yMax*1.5)
    option='histo'
    option+=options_
    h.DrawCopy(option)
    #draw remaining
    for h in listOfHistos[1:]:
        h.DrawCopy(option+'same')
    h.DrawCopy('axissame')
    if ratio:
        canvas.cd(2)
        line=listOfHistos[0].Clone()
        line.Divide(listOfHistos[0])
        line.GetYaxis().SetRangeUser(0.5,1.5)
        line.GetYaxis().SetTitle('#frac{Sample}{Nominal Sample}')
        line.GetXaxis().SetLabelSize(line.GetXaxis().GetLabelSize()*2.4)
        line.GetYaxis().SetLabelSize(line.GetYaxis().GetLabelSize()*2.4)
        line.GetXaxis().SetTitleSize(line.GetXaxis().GetTitleSize()*3)
        line.GetYaxis().SetTitleSize(line.GetYaxis().GetTitleSize()*1.5)
        line.GetYaxis().SetTitleOffset(0.9)
        line.GetYaxis().SetNdivisions(505)
        for i in range(line.GetNbinsX()+1):
            line.SetBinContent(i,1)
            line.SetBinError(i,0)
        line.SetLineWidth(1)
        line.DrawCopy('histo')
        for hist in listOfHistos[1:]:
            ratio=hist.Clone()
            ratio.Divide(listOfHistos[0])
            ratio.DrawCopy('sameP')
        canvas.cd(1)
    return canvas


# writes canvases to pdf 
def printCanvases(canvases,name):

    print 'printing canvases!'
    print canvases,name
    canvas=canvases[0]
    canvas.Print(name+'.pdf[')
    for c in canvases:
        canvas=c
        canvas.Print(name+'.pdf')
        #canvas.SaveAs(name+"/"+c.GetName()+'.png')
        
    canvas.Print(name+'.pdf]')
    if not os.path.exists(name):
        os.makedirs(name)
    for c in canvases:
        c.Print(name+'/'+("_".join(((c.GetName()).split('_'))[1:]))+".pdf")
        c.SaveAs(name+'/'+("_".join(((c.GetName()).split('_'))[1:]))+".png")


def printCanvasesPNG(canvases,name):

    if not os.path.exists(name):
        os.makedirs(name)
    for c in canvases:
        c.Print(name+'/'+("_".join(((c.GetName()).split('_'))[2:]))+".png")


# writes canvases to root file 
def writeObjects(objects,name):
    outfile=ROOT.TFile(name+'.root','recreate')
    for o in objects:
        o.Write()
    outfile.Close()

# returns the next decent round number (like 2, 2.5, 5, 10)
def roundNumber(x):
    loga = int(math.floor(math.log10(x)))
    x_=x/(10**loga)
    y=10
    if x_ < 5:
        y=5
    if x_ < 2.5:
        y=2.5
    if x_ < 2:
        y=2
    y*=(10**loga)
    return y

# changes range of histos in plot to reasonable values, returns plot
def setPlotRangeAuto(plots,samples,treename='MVATree',weightexpression='Weight',maxentries=100000):
    newplots=[]
    trees=[s.GetTree(treename) for s in samples]
    ROOT.gDirectory.cd('PyROOT:/')
    for plot in plots:
        total_xmin=float('inf')
        total_xmax=float('-inf')
        for sample,tree in zip(samples,trees):
            h=plot.histo
            name=h.GetName()
            title=h.GetTitle()
            nbins=h.GetNbinsX()
            project_name=name+'_temp'
            project_var=plot.variable
            ss='('+sample.selection+')'
            if sample.selection == '':
                ss='1'
                ps='('+plot.selection+')'
            if plot.selection == '':
                ps='1'
            project_sel='('+ps+'*'+ss+')*('+weightexpression+')'
            tree.Draw(project_var+">>"+project_name+'('+str(nbins)+')',project_sel,"",maxentries)
            project_histo=ROOT.gDirectory.Get(project_name)
            xmax=project_histo.GetXaxis().GetXmax()
            xmin=project_histo.GetXaxis().GetXmin()
            ymax=project_histo.GetMaximum()
            ycutoff=ymax/50
        
            overflow=0
            nclip=0
            for i in range(nbins,-1,-1):
                xmax=project_histo.GetBinLowEdge(i+1)
                nclip+=1
                overflow+=project_histo.GetBinContent(i)
                if (project_histo.GetBinContent(i)>ycutoff and project_histo.GetBinContent(i-1)>ycutoff and project_histo.GetBinContent(i)>2*h.GetBinError(i) and nclip>3 and nclip>nbins/6) or overflow>ymax:
                    break

            underflow=0
            for i in range(nbins+1):
                xmin=project_histo.GetBinLowEdge(i)
                underflow+=project_histo.GetBinContent(i)
                underflow+=project_histo.GetBinContent(i)
                if (project_histo.GetBinContent(i)>ycutoff and project_histo.GetBinContent(i+1)>ycutoff and project_histo.GetBinContent(i)>2*h.GetBinError(i) and nclip>3 and nclip>nbins/6) or underflow>ymax:
                    break
            if xmin>0 and xmin<xmax/4:
                xmin=0
            total_xmin=min(xmin,total_xmin)
            total_xmax=max(xmax,total_xmax)

        xrange=total_xmax-total_xmin
        binwidth=xrange/nbins
        newbinwidth=roundNumber(binwidth)
        nbins=int(nbins*binwidth/newbinwidth+1)
        total_xmin=int(math.floor(total_xmin/newbinwidth))*newbinwidth
        total_xmax=total_xmin+newbinwidth*nbins
                      
        h.SetDirectory(0)
        newhisto=ROOT.TH1F(name,title,nbins,total_xmin,total_xmax)
        newplots.append(Plot(newhisto,project_var,plot.selection))

    for f in files:
        f.Close()
    return newplots
        
# creates list of histolist from plots and samples -- draws every histogram after another, slow
def createHistoLists_fromTree(plots,samples,treename='MVATree',weightexpression='Weight'):    
    listOfHistoLists=[]
    for plot in plots:
        histoList=[]           
        for sample in samples:
            h=plot.histo.Clone()
            h.Sumw2()
            h.SetName(h.GetName()+'_'+sample.name)
#            setupHisto(h,sample.color)
            histoList.append(h)
        listOfHistoLists.append(histoList)

    for sample in samples:
        tree = sample.GetTree(treename)
        ROOT.gDirectory.cd('PyROOT:/')
        for plot in plots:
            ss='('+sample.selection+')'
            if sample.selection == '':
                ss='1'
            ps='('+plot.selection+')'
            if plot.selection == '':
                ps='1'
            project_name=plot.histo.GetName()+'_'+sample.name
            project_var=plot.variable
            project_sel='('+ps+'*'+ss+')*('+weightexpression+')'
            print "projecting",project_name,"--",project_var,"--",project_sel
            tree.Project(project_name,project_var,project_sel)

    return listOfHistoLists
# transpose list of list
def transposeLOL(lol):
    return [list(x) for x  in zip(*lol)]

# get keynames from rootfile
def GetKeyNames( self, dir = "" ):
    self.cd(dir)
    return [key.GetName() for key in ROOT.gDirectory.GetListOfKeys()]
ROOT.TFile.GetKeyNames = GetKeyNames

# add entry to legend while adapting lenged size
def AddEntry2( self, histo, label, option='L'):
    self.SetY1NDC(self.GetY1NDC()-0.045)
    width=self.GetX2NDC()-self.GetX1NDC()
    ts=self.GetTextSize()
    neglen = 0
    sscripts = re.findall("_{.+?}|\^{.+?}",label)
    for s in sscripts:
	neglen = neglen + 3
    symbols = re.findall("#[a-zA-Z]+",label)
    for symbol in symbols:
	neglen = neglen + len(symbol)-1
    newwidth=max((len(label)-neglen)*0.015*0.05/ts+0.1,width)
    self.SetX1NDC(self.GetX2NDC()-newwidth)
    self.AddEntry(histo, label, option)
ROOT.TLegend.AddEntry2 = AddEntry2

def AddEntryZprime( self, histo, label, option='L'):
    self.SetY1NDC(self.GetY1NDC()-0.05)
    width=self.GetX2NDC()-self.GetX1NDC()
    ts=self.GetTextSize()
    neglen = 0
    sscripts = re.findall("_{.+?}|\^{.+?}",label)
    for s in sscripts:
	neglen = neglen + 3
    symbols = re.findall("#[a-zA-Z]+",label)
    for symbol in symbols:
	neglen = neglen + len(symbol)-1
	#print neglen
    #newwidth=max((len(label)-neglen)*0.015*0.05/ts+0.1,width)
    newwidth=max((len(label)-neglen)*0.35*ts+0.1,width)
    #print 'old width ',width
    self.SetX1NDC(self.GetX2NDC()-newwidth)
    self.AddEntry(histo, label, option)
ROOT.TLegend.AddEntryZprime = AddEntryZprime

def AddEntry22( self, histo, label, option='L'):
    self.SetY1NDC(self.GetY1NDC()-0.045)
    width=self.GetX2NDC()-self.GetX1NDC()
    ts=self.GetTextSize()
    neglen = 0
    sscripts = re.findall("_{.+?}|\^{.+?}",label)
    for s in sscripts:
	neglen = neglen + 3
    symbols = re.findall("#[a-zA-Z]+",label)
    for symbol in symbols:
	neglen = neglen + len(symbol)-1
    newwidth=max((len(label)-neglen)*0.015*0.05/ts+0.1,width)
    #self.SetX1NDC(self.GetX2NDC()-newwidth)

    
    self.AddEntry(histo, label, option)
ROOT.TLegend.AddEntry22 = AddEntry22


def AddEntry4545( self, histo, label, option='L'):
    self.SetY1NDC(self.GetY1NDC()-0.045)
    width=self.GetX2NDC()-self.GetX1NDC()
    ts=self.GetTextSize()
    neglen = 0
    sscripts = re.findall("_{.+?}|\^{.+?}",label)
    for s in sscripts:
	neglen = neglen + 3
    print sscripts, neglen
    symbols = re.findall("#[a-zA-Z]+",label)
    for symbol in symbols:
	neglen = neglen + len(symbol)-1
    print symbols, neglen
    newwidth=max((len(label)-neglen)*0.015*0.04/ts+0.1,width)
    print newwidth
    self.SetX1NDC(self.GetX2NDC()-newwidth)
    
    self.AddEntry(histo, label, option)
ROOT.TLegend.AddEntry4545 = AddEntry4545


def AddEntry3( self, histo, label, option='L'):
    self.SetY1NDC(self.GetY1NDC()-0.045)
    width=self.GetX2NDC()-self.GetX1NDC()
    ts=self.GetTextSize()
    neglen = 0
    sscripts = re.findall("_{.+?}|\^{.+?}",label)
    for s in sscripts:
	neglen = neglen + 3
    symbols = re.findall("#[a-zA-Z]+",label)
    for symbol in symbols:
	neglen = neglen + len(symbol)-1
    label+=' ('+str(round(10*histo.Integral())/10.)+')'
    newwidth=max((len(label)-neglen)*0.015*0.05/ts+0.1,width)
    self.SetX1NDC(self.GetX2NDC()-newwidth)

    
    self.AddEntry(histo, label, option)
ROOT.TLegend.AddEntry3 = AddEntry3

def AddEntry4( self, histo, label, option='L'):
    self.SetY1NDC(self.GetY1NDC()-0.045)
    width=self.GetX2NDC()-self.GetX1NDC()
    ts=self.GetTextSize()
    neglen = 0
    sscripts = re.findall("_{.+?}|\^{.+?}",label)
    for s in sscripts:
	neglen = neglen + 3
    symbols = re.findall("#[a-zA-Z]+",label)
    for symbol in symbols:
	neglen = neglen + len(symbol)-1
    label+=' ('+str(round(10*histo.Integral())/10.)+')'
    newwidth=max((len(label)-neglen)*0.015*0.05/ts+0.1,width)
    self.SetX1NDC(self.GetX2NDC()-newwidth)

    
    self.AddEntry(histo, label, option)
ROOT.TLegend.AddEntry4 = AddEntry4

# get histolist from file
def createHistoLists_fromHistoFile(samples,rebin=1):
    listOfHistoListsT=[]
    listLength=-1
    for sample in samples:
        f=ROOT.TFile(sample.path, "readonly")       
        keyList = f.GetKeyNames()
        ROOT.gDirectory.cd('PyROOT:/')
        if listLength>0:
            assert len(keyList) == listLength
        listLength=len(keyList)
        histoList = []
        for key in keyList:
            o=f.Get(key)
            if isinstance(o,ROOT.TH1) and not isinstance(o,ROOT.TH2): 
                o.Rebin(rebin)
                histoList.append(o.Clone())
                histoList[-1].SetName(o.GetName()+'_'+sample.name)
        listOfHistoListsT.append(histoList)
    listOfHistoLists=transposeLOL(listOfHistoListsT)
    return listOfHistoLists
  
def createHistoLists_fromFiles(files,rebin=1):
    listOfHistoListsT=[]
    listLength=-1
    for hfile in files:
        f=ROOT.TFile(hfile, "readonly")       
        keyList = f.GetKeyNames()
        ROOT.gDirectory.cd('PyROOT:/')
        if listLength>0:
            assert len(keyList) == listLength
        listLength=len(keyList)
        histoList = []
        for key in keyList:
            o=f.Get(key)
            if isinstance(o,ROOT.TH1) and not isinstance(o,ROOT.TH2): 
                o.Rebin(rebin)
                histoList.append(o.Clone())
                #histoList[-1].SetName(o.GetName()+'_'+sample.name)
        listOfHistoListsT.append(histoList)
    listOfHistoLists=transposeLOL(listOfHistoListsT)
    return listOfHistoLists

def createHistoLists_fromSuperHistoFile(path,samples,plots,rebin=1,catnames=[""],DoTwoDim=False):
    listOfHistoListsT=[]
    f=ROOT.TFile(path, "readonly")
    keyList = f.GetKeyNames()
    print keyList
    for sample in samples:
        
        histoList=[]
        ROOT.gDirectory.cd('PyROOT:/')
        print catnames
        for c in catnames:
            for plot in plots:
                key=sample.nick+'_'+c+plot.name
                print key
                print key, sample.nick, c, plot.name
                o=f.Get(key)
                print o
                if isinstance(o,ROOT.TH1) and not isinstance(o,ROOT.TH2): 
                    o.Rebin(rebin)
                    histoList.append(o.Clone())
                    print "ok", histoList[-1], len(histoList)
                if DoTwoDim and isinstance(o,ROOT.TH2):
		    print "2D"
		    histoList.append(o.Clone())
	#raw_input()

        listOfHistoListsT.append(histoList)
    listOfHistoLists=transposeLOL(listOfHistoListsT)
    return listOfHistoLists

def createLLL_fromSuperHistoFileSyst(path,samples,plots,systnames=[""]):
    f=ROOT.TFile(path, "readonly")
#    print path
    keyList = f.GetKeyNames()    
    lll=[]
    for plot in plots:
        ll=[]
        for sample in samples:
            nominal_key=sample.nick+'_'+plot.name+systnames[0]
            nominal=f.Get(nominal_key)
#            print sample.name
#            print sample.shape_unc
            l=[]
            for syst in systnames:
                ROOT.gDirectory.cd('PyROOT:/')               
                key=sample.nick+'_'+plot.name+syst
                print key
                if not syst in sample.shape_unc: 
#		    print "using nominal for ", key
                    l.append(nominal.Clone(key))
                    continue
                o=f.Get(key)
                if isinstance(o,ROOT.TH1) and not isinstance(o,ROOT.TH2): 
#		    print "using right one for", key
                    l.append(o.Clone())
 #               else:
  #                  print syst,'not used for',sample.name
            ll.append(l)
        lll.append(ll)
    return lll

def createErrorbands(lll,samples,DoRateSysts=True):
    print "creating errorbands"
    if DoRateSysts:
      print "using ratesysts"
    #print lll
    graphs=[]
    print ' '
    print ' lll :',lll
    print ' '
    for ll in lll: #for all plots
        llT=transposeLOL(ll)
        print ' '   
        print 'llT : ',llT
        print ' '   
        nominal=llT[0][0].Clone()
        print "addresses ", llT[0][0], nominal
        print llT
        for h in llT[0][1:]:
            nominal.Add(h)
            print h
        print "integrals ", llT[0][0].Integral(), nominal.Integral()
        systs=[]
        print ' '   
        print 'llT[1:] : ',llT[1:]
        print ' '         
        for l in llT[1:]: #for all systematics
            syst=l[0].Clone()
            for h in l[1:]:
                syst.Add(h)
                print h
            systs.append(syst)
        print len(samples), '   ',len(llT[0])
        assert len(samples)==len(llT[0])
        for isample,sample in enumerate(samples): # for all normalization unc
	      ls=[]
	      for ihisto,h in enumerate(llT[0]):
		  ls.append(h.Clone())
		  if ihisto==isample:
		    if DoRateSysts:
		      ls[-1].Scale(1+sample.unc_up)
	      syst=ls[0].Clone()
	      #print syst.GetName()
	      for h in ls[1:]:
		  syst.Add(h)
		  #print h.GetName()
	      #print "rates ", sample.nick, syst.Integral()
	      systs.append(syst)

	      ls=[]
	      for ihisto,h in enumerate(llT[0]):
		  ls.append(h.Clone())
		  if ihisto==isample:
		    if DoRateSysts:
		      ls[-1].Scale(1-sample.unc_down)
	      syst=ls[0].Clone()
	      for h in ls[1:]:
		  syst.Add(h)
	      #print "rates ", sample.nick, syst.Integral()
	      systs.append(syst)
	      
        uperrors=[0]*ll[0][0].GetNbinsX()
        downerrors=[0]*ll[0][0].GetNbinsX()
        
        #for sys in systs:
	  #print sys, sys.Integral()
        for ibin in range(0,nominal.GetNbinsX()):
            nerr=nominal.GetBinError(ibin+1)
            print "Bin, name, content ",ibin, nominal.GetName(), nominal.GetBinContent(ibin+1)
            uperrors[ibin]=ROOT.TMath.Sqrt(uperrors[ibin]*uperrors[ibin]+nerr*nerr)
            downerrors[ibin]=ROOT.TMath.Sqrt(downerrors[ibin]*downerrors[ibin]+nerr*nerr)
            n=nominal.GetBinContent(ibin+1)
            ups=systs[0::2]
            downs=systs[1::2]
            for up,down in zip(ups,downs):
	        print "up/down name ", up.GetName(), down.GetName()
	        print "up/down diff ",  up.GetBinContent(ibin+1)-n, down.GetBinContent(ibin+1)-n
                u_=up.GetBinContent(ibin+1)-n
                d_=down.GetBinContent(ibin+1)-n
                #print u_,d_
                if u_ >= 0 and u_ >= d_:
                    u=u_
                    if d_<0:
                        d=d_
                    else:
                        d=0
                elif u_ >= 0 and u_ <= d_:
                    u=d_
                    d=0
                elif u_ < 0 and d_ <= u_:
                    d=d_
                    u=0
                elif u_ < 0 and u_ < d_:
                    d=u_
                    if d_>=0:
		      u=d_
		    else:
                      u=0
                
                uperrors[ibin]=ROOT.TMath.Sqrt(uperrors[ibin]*uperrors[ibin]+u*u)
                downerrors[ibin]=ROOT.TMath.Sqrt(downerrors[ibin]*downerrors[ibin]+d*d)
                #print u,d
                print "up/down errors ", uperrors[ibin],downerrors[ibin]
                
        graph=ROOT.TGraphAsymmErrors(nominal)
        for i in range(len(uperrors)):
            graph.SetPointEYlow(i,downerrors[i])
            graph.SetPointEYhigh(i,uperrors[i])
            graph.SetPointEXlow(i,nominal.GetBinWidth(i+1)/2.)
            graph.SetPointEXhigh(i,nominal.GetBinWidth(i+1)/2.)
            
        graphs.append(graph)
    return graphs
    
    
# for a list of selections (and a list of their names) and a list of histos (and the variable expressions to fill them) the cartesian product is created and plots are booked
def plotsForSelections_cross_Histos(selections,selectionnames,histos,variables):
    selection_histos=product(zip(selections,selectionnames),zip(histos,variables))
    plots=[]
    for selectionpair,histopair in selection_histos:
        histopair=(histopair[0].Clone(),histopair[1])
        histopair[0].SetName(histopair[0].GetName()+'_'+selectionpair[1])
        histopair[0].SetTitle(histopair[0].GetTitle()+' '+selectionpair[1])
        plots.append(Plot(histopair[0],histopair[1],selectionpair[0]))
    return plots


# gets a list of histogramlist and creates a plot for every list
def writeListOfHistoLists(listOfHistoLists,samples, label,name,normalize=True,stack=False,logscale=False,options='histo',statTest=False, sepaTest=False,ratio=False,DoProfile=False):
    #if DoProfile and not isinstance(listOfHistoLists[0][0], ROOT.TH2):
      #print "need 2D plots for Profile Histograms"
      #DoProfile=False
    listofallstattests=[]
    if isinstance(label, basestring):
        labeltexts=len(listOfHistoLists)*[label]
#        print "bla"
    else:
        labeltexts=label
    canvases=[]
    objects=[]   
    i=0
    print labeltexts
    for listOfHistos, labeltext in zip(listOfHistoLists, labeltexts):
        listofthisstattests=[listOfHistos[0].GetTitle()]
        i+=1
        for histo,sample in zip(listOfHistos,samples):
            print labeltext
            yTitle='Events'
            if normalize:
                yTitle='normalized'
            setupHisto(histo,sample.color,yTitle,stack)        
        stattests2D=None
        if isinstance(listOfHistos[0], ROOT.TH2):
            print "drawing 2D"
            if not (options=='COLZ' or options=='colz' or options=='box' or options==''):
                currentoption=''
            else:
                currentoption=options
            if not DoProfile:    
                c, stattests2D=drawHistosOnCanvas2D(listOfHistos,normalize,stack,logscale,currentoption,ratio,DoProfile,statTest, samples)
            else:
                c, stattests2D, profilesx, profilesy = drawHistosOnCanvas2D(listOfHistos,normalize,stack,logscale,currentoption,ratio,DoProfile,statTest, samples)
        else:
            c=drawHistosOnCanvas(listOfHistos,normalize,stack,logscale,options,ratio,DoProfile)

        if not isinstance(c, list):
            c.SetName('c_'+listOfHistos[0].GetName())
            l=getLegend2()
            for h,sample in zip(listOfHistos,samples):
                loption='L'
                if stack:
                    loption='F'            
                l.AddEntry4545(h,sample.name,loption)
            canvases.append(c)
            l.Draw('same')
            objects.append(l)
        elif options == "colz":
            for i in range(len(listOfHistos)):
                c[i].SetName('c_'+listOfHistos[i].GetName()) #wrong! What name should be set?

            if DoProfile:
                c[-2].SetName('c_'+c[-2].GetName())
                lx = getLegend2()
                for px,  sample in zip(profilesx,  samples):
                    lx.AddEntry4545( px.GetName() , sample.name, "L" )
                lx.Draw("same")
                objects.append(lx)
                
                c[-1].SetName('c_'+c[-1].GetName())
                ly = getLegend2()
                for  py, sample in zip( profilesy, samples):
                    ly.AddEntry4545( py.GetName() , sample.name, "L" )
                ly.Draw("same")
                objects.append(ly)
            canvases+=c
        else:
            canvases+=c
        
        if statTest:
            if not isinstance(listOfHistos[0],ROOT.TH2):
                tests=getStatTestsList(listOfHistos[0],listOfHistos[1:],"UW")
                tests.Draw()
                listofthisstattests.append(tests.GetTitle())
                objects.append(tests)
        if sepaTest:
            stests=getSepaTests(listOfHistos[0],listOfHistos[1])
            stests.Draw()
            objects.append(stests)
        if stattests2D!=None:
            # stattests2D.Draw()
            objects.append(stattests2D)
            listofthisstattests.append(stattests2D.GetTitle())
        # cms = ROOT.TLatex(0.2, 0.96, 'CMS private work'  );
        # cms.SetTextFont(42)
        # cms.SetTextSize(0.05)
        # cms.SetNDC()
        # cms.Draw()
        # print cms
        # objects.append(cms)

        if not isinstance(c, list):
            cms = ROOT.TLatex(0.2, 0.96, 'CMS preliminary,  37.8 fb^{-1},  #sqrt{s} = 13 TeV'  );
            cms.SetTextFont(42)
            cms.SetTextSize(0.05)
            cms.SetNDC()
            cms.Draw()
            objects.append(cms)

            label = ROOT.TLatex(0.2, 0.9, labeltext);
            label.SetTextFont(42)
            label.SetTextSize(0.04)
            label.SetNDC()
            label.Draw()
            objects.append(label)
            listofallstattests.append(listofthisstattests)
        # else:
        #     for can, sam in zip(c,samples):
        #         labeltext = sam.name
        #         label = ROOT.TLatex(0.2, 0.96, labeltext);
        #         label.SetTextFont(42)
        #         label.SetTextSize(0.04)
        #         label.SetNDC()
        #         label.Draw()
        #         objects.append(label)
        #     listofallstattests.append(listofthisstattests)

        
    printCanvases(canvases,name)
    writeObjects(canvases,name)
    stattestoutfile=open("stattests_"+name+".txt","w")
    for stst in listofallstattests:
      stattestoutfile.write(' '.join(stst)+'\n')
    stattestoutfile.close()  
      
    
def writeListOfHistoListsAN(listOfHistoLists,samples, label,name,normalize=True,stack=False,logscale=False,options='histo',statTest=False, sepaTest=False,ratio=False):
    if isinstance(label, basestring):
        labeltexts=len(listOfHistoLists)*[label]
#        print "bla"
    else:
        labeltexts=label
    canvases=[]
    objects=[]   
    i=0
#    print labeltexts
    for listOfHistos, labeltext in zip(listOfHistoLists, labeltexts):
        i+=1
        for histo,sample in zip(listOfHistos,samples):
#            print labeltext
            yTitle='Events'
            if normalize:
                yTitle='normalized'
            setupHisto(histo,sample.color,yTitle,stack)        
        c=drawHistosOnCanvas(listOfHistos,normalize,stack,logscale,options,ratio)
        c.SetName('c_'+listOfHistos[0].GetName())        
        l=getLegend()
        for h,sample in zip(listOfHistos,samples):
            loption='L'
            if stack:
                loption='F'            
            l.AddEntry2(h,sample.name,loption)
        canvases.append(c)
        l.Draw('same')
        objects.append(l)
        if statTest:
            tests=getStatTests(listOfHistos[0],listOfHistos[1])
            tests.Draw()
            objects.append(tests)
        if sepaTest:
            stests=getSepaTests(listOfHistos[0],listOfHistos[1])
            stests.Draw()
            objects.append(stests)
#        cms = ROOT.TLatex(0.2, 0.96, 'CMS private work'  );
#        cms.SetTextFont(42)
#        cms.SetTextSize(0.05)
#        cms.SetNDC()
#        cms.Draw()
#        print cms
#        objects.append(cms)

        cms = ROOT.TLatex(0.2, 0.96, 'CMS preliminary,  12.9 fb^{-1},  #sqrt{s} = 13 TeV'  );
        cms.SetTextFont(42)
        cms.SetTextSize(0.05)
        cms.SetNDC()
        cms.Draw()
        objects.append(cms)

        label = ROOT.TLatex(0.2, 0.86, labeltext);
        label.SetTextFont(42)
        label.SetTextSize(0.05)
        label.SetNDC()
        label.Draw()
        objects.append(label)



    printCanvases(canvases,name)
    writeObjects(canvases,name)


def writeListOfROCs(graphs,names,colors,filename,logscale=False,rej=True):
    c=getCanvas('ROC')
    if logscale:
        c.SetLogy()
    l=getLegend()
    first=True
    for graph,name,color in zip(graphs,names,colors):
        l.AddEntry2(graph,name)
        if first:
            graph.Draw('AL')
            first=False
        else:
            graph.Draw('L')
        setupHisto(graph,color)
        graph.GetXaxis().SetTitle('Signal efficiency')
        if rej:
             graph.GetYaxis().SetTitle('Background rejection')
        else:
            graph.GetYaxis().SetTitle('Background efficiency')
        graph.SetMarkerStyle(20)
    l.Draw('same')
    printCanvases([c],filename)
    writeObjects([c],filename)


#from lists of background and signalhistos one signal and one background histo are created
def getSuperHistoPair(histosS,histosB,name):
    superbins=[]
    for hs,hb in zip(histosS,histosB):
        nBins=hs.GetNbinsX()
        for i in range(1,nBins+1):
            s=hs.GetBinContent(i)
            b=hb.GetBinContent(i)
            if(b!=0):
                superbins.append( (s/b,s,b) )
            elif(s!=0):
                superbins.append( (float("inf"),s,b) )
    superbins_sorted=sorted(superbins,key=lambda b: b[0])
    superhistoS=ROOT.TH1F('superhistoS_'+name,'superhistoS_'+name,len(superbins_sorted),-0.5,len(superbins_sorted)-0.5)
    superhistoB=ROOT.TH1F('superhistoB_'+name,'superhistoB_'+name,len(superbins_sorted),-0.5,len(superbins_sorted)-0.5)
    for i in range(len(superbins)):
        superhistoS.SetBinContent(i+1,superbins_sorted[i][1])
        superhistoB.SetBinContent(i+1,superbins_sorted[i][2])
    return (superhistoS,superhistoB)

# calculate significance for cuts at bins in signal and background histogram
# histogram bins are expected to be sorted by increasing S/B (e.g. BDT output)
def getSignifCurve(histoS,histoB):
    nBins=histoS.GetNbinsX()
    nonZeroBins=[]
    for i in range(nBins):
        if histoS.GetBinContent(i)>0. or histoB.GetBinContent(i)>0.:
            nonZeroBins.append(i)     
    sigs=ROOT.TGraphAsymmErrors(len(nonZeroBins))
    point=0
    for i in nonZeroBins:
        intS=histoS.Integral(i,nBins)
        intB=histoB.Integral(i,nBins)#*6000000./61974084.
        sigs.SetPoint(point,intS/histoS.Integral(0,nBins),intS/math.sqrt(intS+intB))
        point+=1
    return sigs

# calculate ROC for signal(1) and bkg(2) histo
def getROC(histo1,histo2,rej=True):
    nBins=histo1.GetNbinsX()
    nBins2=histo2.GetNbinsX()
    integral1=histo1.Integral(0,nBins+1)
    integral2=histo2.Integral(0,nBins2+1)

    nonZeroBins=[]
    for i in range(nBins,-1,-1):
        if histo1.GetBinContent(i)>0. or histo2.GetBinContent(i)>0.:
            nonZeroBins.append(i)           

    roc = ROOT.TGraphAsymmErrors(len(nonZeroBins)+1)
    if rej:
        roc.SetPoint(0,0,1)
    else:
        roc.SetPoint(0,0,0)
    point=1
    for i in nonZeroBins:
        eff1=0
        eff2=0
        if integral1 > 0:
            eff1=histo1.Integral(i,nBins+1)/integral1
        if integral2 > 0:
            eff2=histo2.Integral(i,nBins+1)/integral2
        if rej:
            roc.SetPoint(point,eff1,1-eff2)
        else:
            roc.SetPoint(point,eff1,eff2)
        point+=1
    
    return roc

def getEff(histo1):
    nBins=histo1.GetNbinsX()
    integral1=histo1.Integral(0,nBins+1)

    nonZeroBins=[]
    for i in range(nBins+2):
        if histo1.GetBinContent(i)>0.:
            nonZeroBins.append(i)
    eff = ROOT.TGraphAsymmErrors(len(nonZeroBins)+1)
    point=0
    for i in nonZeroBins:
        eff1=0
        if integral1 > 0:
            eff1=histo1.Integral(i,nBins+1)/integral1
#        print i, histo1.GetBinLowEdge(i), eff1
        eff.SetPoint(point,histo1.GetBinLowEdge(i),eff1)
        point+=1
#    print "###"
    return eff



def writeSyst(f,values):
    for val in values[:-1]:
        f.write(val+" &")
    f.write(values[-1])
    f.write('\\\\ \n')

def writeFoot(f):
    f.write('\\hline\n')
    f.write('\end{tabular}\n')
    f.write('\\end{center}\n')

def writeHead(f,columns):
    #print columns
    f.write('\\begin{center}\n')
    f.write('\\begin{tabular}{l')
    for entry in columns[1:]:
        f.write('c')
    f.write('}\n')
    f.write('\\hline\n')
    for entry in columns[:-1]:
        f.write(entry+' &')
    f.write(columns[-1]+' \\\\ \n')
    f.write('\\hline\n')



def root2latex(s,mth=True):
    ns=""
    if mth:
        ns+="$"
    ns+=s.replace('#','\\')
    if mth:
        ns+="$"
    return ns

def turn1dHistoToRow(h,witherror=True,rounding="3dig"):
    s=""
    for i in range(1,h.GetNbinsX()+1):
        if rounding=="3dig":
          s+="%.3f" % h.GetBinContent(i)
        else:
	  s+="%.1f" % h.GetBinContent(i)
        if witherror:
            s+=" $\pm$ "
            if rounding=="3dig":
              s+="%.3f" % h.GetBinError(i)
            else:
	      s+="%.1f" % h.GetBinError(i)
        if i==h.GetNbinsX():
            s+="\\\\"
        else:
            s+="&"
    return s
    

def turn1dHistosToTable(histos,samples,outfile,witherror=True):
    out=open(outfile+".tex","w")
    out.write( '\\documentclass[landscape]{article}\n')
    out.write( '\\usepackage[landscape]{geometry}\n')
    out.write( '\\begin{document}\n')
    out.write( '\\thispagestyle{empty}\n')
    out.write( '\\footnotesize\n')
    cls=['Process']
    for i in range(1,histos[0].GetNbinsX()+1):
        cls.append(histos[0].GetXaxis().GetBinLabel(i))
    writeHead(out,cls)
    for h,s in zip(histos,samples):
        rounding="1dig"
        if s.name=="S/B":
	  rounding="3dig"
        out.write(root2latex(s.name) + " & " + turn1dHistoToRow(h,witherror,rounding)+ "\\\\ \n")       
    writeFoot(out)
    out.write( '\\end{document}\n')


def write2dHistoToTable(histo,outfile):
    out=open(outfile+".tex","w")
    out.write( '\\documentclass{article}\n')
    out.write( '\\begin{document}\n')
    out.write( '\\thispagestyle{empty}\n')
    nx=histo.GetNbinsX()
    ny=histo.GetNbinsY()
    xtitle=[""]
    for i in range(1,nx+1):
        xtitle.append(histo.GetXaxis().GetBinLabel(i))
    ytitle=[]
    for i in range(1,ny+1):
        ytitle.append(histo.GetYaxis().GetBinLabel(i))

    writeHead(out,xtitle)
    for y in range(1,ny+1):
        contents=[ytitle[y-1]]
        for x in range(1,nx+1):
            contents.append("%.1f"%(histo.GetBinContent(x,y)))
        writeSyst(out,contents)
    writeFoot(out)
    out.write("\\end{document}")
    out.close()

def writeHistoListToTable(histos,names,outfile):
    names=["$"+n.replace("#","\\")+"$" for n in names]
    out=open(outfile+".tex","w")
    out.write( '\\documentclass{article}\n')
    out.write( '\\begin{document}\n')
    out.write( '\\thispagestyle{empty}\n')
    nx=histos[0].GetNbinsX()
    ny=histos[0].GetNbinsY()
    xtitle1=[""]
    xtitle2=[""]
    for i in range(1,nx+1):
        xtitle1.append(histos[0].GetXaxis().GetBinLabel(i))
        xtitle2.append(names[0])
        for i in range(1,len(histos)):
            xtitle1.append("")
            xtitle2.append(names[i])
    ytitle=[]
    for i in range(1,ny+1):
        ytitle.append(histos[0].GetYaxis().GetBinLabel(i))

    writeHead(out,xtitle1)
    writeSyst(out,xtitle2)
    for y in range(1,ny+1):
        contents=[ytitle[y-1]]
        for x in range(1,nx+1):
            for histo in histos:
                contents.append("%.1f"%(histo.GetBinContent(x,y)))
        writeSyst(out,contents)
    writeFoot(out)
    out.write("\\end{document}")
    out.close()


def writeListOfHistoListsToFile(listOfHistoLists,samples,name):
    hs=[]
    for hl in listOfHistoLists:
        for h,s in zip(hl,samples):
            h.SetLineColor(s.color)
            hs.append(h)
    l=getLegend()
    for h in listOfHistoLists[0]:
        l.AddEntry(h)
    hs.append(l)
    writeObjects(hs,name)

def printPlots(plots):
    for plot in plots:
        print 'TH1F("'+plot.histo.GetName()+'","'+plot.histo.GetTitle()+'",'+str(plot.histo.GetNbinsX())+','+str(plot.histo.GetXaxis().GetXmin())+','+str(plot.histo.GetXaxis().GetXmax())+')'


def moveOverFlow(h):
    h.SetBinContent(1,h.GetBinContent(0)+h.GetBinContent(1));
    h.SetBinContent(h.GetNbinsX(),h.GetBinContent(h.GetNbinsX()+1)+h.GetBinContent(h.GetNbinsX()));
    h.SetBinError(1,ROOT.TMath.Sqrt(ROOT.TMath.Power(h.GetBinError(0),2)+ROOT.TMath.Power(h.GetBinError(1),2)));
    h.SetBinError(h.GetNbinsX(),ROOT.TMath.Sqrt(ROOT.TMath.Power(h.GetBinError(h.GetNbinsX()+1),2)+ROOT.TMath.Power(h.GetBinError(h.GetNbinsX()),2)));

# stack histo list 
def stackHistoList(listOfHistos_,normalize=False):
    listOfHistos=[]
    for h in listOfHistos_:
        listOfHistos.append(h.Clone(h.GetName()+"_stack"))
    for i in range(len(listOfHistos)-1,0,-1):
        listOfHistos[i-1].Add(listOfHistos[i])
    if normalize:
        integral0=listOfHistos[0].Integral()
        for h in listOfHistos:
            h.Scale(1./integral0)
    return listOfHistos

    

def getDataGraph(listOfHistosData,nunblinded):
    if len(listOfHistosData)>0:
        datahisto=listOfHistosData[0]
    for d in listOfHistosData[1:]:
        datahisto.Add(d)
    moveOverFlow(datahisto)
    data=ROOT.TGraphAsymmErrors(datahisto)
    alpha = 1 - 0.6827
    for i in range(0,data.GetN()):
    
      N = data.GetY()[i];
      
      L = 0
      if N != 0:
        L = ROOT.Math.gamma_quantile(alpha/2,N,1.)

      U =  ROOT.Math.gamma_quantile_c(alpha/2,N+1,1)
      
      data.SetPointEYlow(i, N-L);
      data.SetPointEYhigh(i, U-N);

    data.SetMarkerStyle(20)
    data.SetMarkerColor(ROOT.kBlack)
    data.SetLineColor(ROOT.kBlack)
    blind_band=ROOT.TGraphAsymmErrors(datahisto)
    j=0
    x, y = ROOT.Double(0), ROOT.Double(0)
    for i in range(0,data.GetN()):
        data.GetPoint(i,x,y)
        data.SetPointEXlow(i,0)
        data.SetPointEXhigh(i,0)
           
        if i>nunblinded:
            blind_band.SetPoint(j,x,0)
            blind_band.SetPointEYlow(j,0)
            blind_band.SetPointEYhigh(j,20000)
            blind_band.SetPointEXlow(j,datahisto.GetBinWidth(1))
            blind_band.SetPointEXhigh(j,datahisto.GetBinWidth(1))

            data.RemovePoint(nunblinded)


    return data
    # TODO: proper y-errors

def getDataGraphBlind(listOfHistosData,nunblinded, MCData=False):
    if len(listOfHistosData)>0:
        datahisto=listOfHistosData[0]
    for d in listOfHistosData[1:]:
        datahisto.Add(d)
    moveOverFlow(datahisto)
    data=ROOT.TGraphAsymmErrors(datahisto)
    alpha = 1 - 0.6827
      
    if not MCData:
      for i in range(0,data.GetN()):
    
        N = data.GetY()[i];
      
        L = 0
        if N != 0:
          L = ROOT.Math.gamma_quantile(alpha/2,N,1.)

        U =  ROOT.Math.gamma_quantile_c(alpha/2,N+1,1)
      
        data.SetPointEYlow(i, N-L);
        data.SetPointEYhigh(i, U-N);
    
    data.SetMarkerStyle(20)
    data.SetMarkerSize(1.3)
    data.SetLineWidth(3)
    data.SetMarkerColor(ROOT.kBlack)
    data.SetLineColor(ROOT.kBlack)
    blind_band=ROOT.TGraphAsymmErrors(datahisto.GetNbinsX()-nunblinded)
    j=0
    x, y = ROOT.Double(0), ROOT.Double(0)
    for i in range(0,data.GetN()+1):
        data.SetPointEXlow(i,0)
        data.SetPointEXhigh(i,0)          
        if i>nunblinded:
            data.GetPoint(nunblinded,x,y)
            blind_band.SetPoint(j,x,0)
            blind_band.SetPointEYlow(j,0)
            blind_band.SetPointEYhigh(j,200000)
            blind_band.SetPointEXlow(j,datahisto.GetBinWidth(1)/2)
            blind_band.SetPointEXhigh(j,datahisto.GetBinWidth(1)/2)
            data.RemovePoint(nunblinded)
            j+=1


    return data,blind_band
    # TODO: proper y-errors


def getRatioGraph(data,mchisto):
    ratio=data.Clone()
    x, y = ROOT.Double(0), ROOT.Double(0)
    minimum = 9999.
    maximum = -9999.
    for i in range(0,data.GetN()):
        data.GetPoint(i,x,y)
        if mchisto.GetBinContent(i+1)>0:
            ratioval=y/mchisto.GetBinContent(i+1)
            ratio.SetPoint(i,x,ratioval)
            if ratioval>maximum and ratioval>0:
              maximum=round(ratioval,1);
            if ratioval<minimum and ratioval>0:
              minimum=round(ratioval,1);
        else:
            ratio.SetPoint(i,x,-999)
        
        if y>0:
            ratio.SetPointEYlow(i,1-(y-data.GetErrorYlow(i))/y)
            ratio.SetPointEYhigh(i,(y+data.GetErrorYhigh(i))/y-1)
        else:
            ratio.SetPointEYlow(i,0)
            ratio.SetPointEYhigh(i,0)
#    moveOverFlow(datahisto)
#    datahisto.Divide(mchisto)
#    return datahisto
#    data=ROOT.TGraphAsymmErrors(datahisto)
#    data.SetMarkerStyle(20)
#    data.SetMarkerColor(ROOT.kBlack)
#    data.SetLineColor(ROOT.kBlack)
#    for i in range(0,data.GetN()):
#        data.SetPointEXlow(i,0)
#        data.SetPointEXhigh(i,0)
    return ratio,minimum,maximum

def getDiffGraph(data,mchisto):
    diff=data.Clone()
    x, y = ROOT.Double(0), ROOT.Double(0)
    minimum = 9999.
    maximum = -9999.
    for i in range(0,data.GetN()):
        data.GetPoint(i,x,y)
        if mchisto.GetBinContent(i+1)>0:
            diffval=y-mchisto.GetBinContent(i+1)
            diff.SetPoint(i,x,diffval)
            if diffval>maximum and ratioval>0:
              maximum=round(diffval,1);
            if diffval<minimum and diffval>0:
              minimum=round(diffval,1);
        else:
            diff.SetPoint(i,x,-999)
        
        if y>0:
            diff.SetPointEYlow(i,1-(y-data.GetErrorYlow(i))/y)
            diff.SetPointEYhigh(i,(y+data.GetErrorYhigh(i))/y-1)
        else:
            diff.SetPointEYlow(i,0)
            diff.SetPointEYhigh(i,0)
#    moveOverFlow(datahisto)
#    datahisto.Divide(mchisto)
#    return datahisto
#    data=ROOT.TGraphAsymmErrors(datahisto)
#    data.SetMarkerStyle(20)
#    data.SetMarkerColor(ROOT.kBlack)
#    data.SetLineColor(ROOT.kBlack)
#    for i in range(0,data.GetN()):
#        data.SetPointEXlow(i,0)
#        data.SetPointEXhigh(i,0)
    return diff,minimum,maximum




def plotDataMC(listOfHistoListsData,listOfHistoLists,samples,name,logscale=False,label='',ratio=True,options='histo'):    
    if isinstance(label, basestring):
        labeltexts=len(listOfHistoListsData)*[label]
    else:
        labeltexts=label
    canvases=[]
    objects=[]   
    i=0
#    print len(listOfHistoLists)
    # for every plot, look at all samples
    for listOfHistos,listOfHistosData,labeltext in zip(listOfHistoLists,listOfHistoListsData,labeltexts):
        i+=1
#        print i
        # setup histo style
        for histo,sample in zip(listOfHistos,samples):
            yTitle='Events'
            setupHisto(histo,sample.color,yTitle,True) 
        # 
        # mover over/underflow
        for h in listOfHistos:
            moveOverFlow(h)
        #stack
        stackedListOfHistos=stackHistoList(listOfHistos)
        objects.append(stackedListOfHistos)
        # find maximum
        yMax=1e-9
        for h in stackedListOfHistos:
            yMax=max(h.GetBinContent(h.GetMaximumBin()),yMax)
        canvas=getCanvas(stackedListOfHistos[0].GetName(),ratio)        
        canvas.cd(1)
        #draw first histo
        h=stackedListOfHistos[0]
        if logscale:
            h.GetYaxis().SetRangeUser(yMax/10000,yMax*10)
            canvas.cd(1).SetLogy()
        else:
            h.GetYaxis().SetRangeUser(0,yMax*1.5)
        option='histo'
        option+=options
        h.DrawCopy(option)
        #draw remaining
        for h in stackedListOfHistos[1:]:
            h.DrawCopy(option+'same')
        h.DrawCopy('axissame')
        #draw data
        data=getDataGraph(listOfHistosData)
        data.Draw('samePE1')
        l=getLegend()
        l.AddEntry2(data,'data','P')
        for h,sample in zip(stackedListOfHistos,samples):
            l.AddEntry2(h,sample.name,'F')

        canvases.append(canvas)
        l.Draw('same')
        objects.append(data)
        objects.append(l)

#        cms = ROOT.TLatex(0.2, 0.96, 'CMS private work'  );
#        cms.SetTextFont(42)
#        cms.SetTextSize(0.05)
#        cms.SetNDC()
#        cms.Draw()
#        objects.append(cms)

        lumi = ROOT.TLatex(0.2, 0.89, '2.46 fb^{-1} @ 13 TeV'  );
        lumi.SetTextFont(42)
        lumi.SetTextSize(0.06)
        lumi.SetNDC()
#        lumi.Draw()
        objects.append(lumi)

        label = ROOT.TLatex(0.2, 0.83, labeltext);
        label.SetTextFont(42)
        label.SetTextSize(0.06)
        label.SetNDC()
        label.Draw()
        objects.append(label)


        ratiograph,ratiominimum,ratiomaximum=getRatioGraph(data,stackedListOfHistos[0])
        canvas.cd(2)
        line=listOfHistos[0].Clone()
        line.SetFillStyle(0)
        line.Divide(listOfHistos[0])
        #line.GetYaxis().SetRangeUser(0.5,1.6)
        line.GetYaxis().SetRangeUser(ratiominimum-0.2,ratiomaximum+0.2)
        
        line.GetXaxis().SetRangeUser(listOfHistos[0].GetXaxis().GetXmin(),listOfHistos[0].GetXaxis().GetXmax())
        for i in range(line.GetNbinsX()+1):
            line.SetBinContent(i,1)
            line.SetBinError(i,0)
        line.GetXaxis().SetLabelSize(line.GetXaxis().GetLabelSize()*2.4)
        line.GetYaxis().SetLabelSize(line.GetYaxis().GetLabelSize()*2.4)
        line.GetXaxis().SetTitleSize(line.GetXaxis().GetTitleSize()*3)
        line.GetYaxis().SetTitleSize(line.GetYaxis().GetTitleSize()*2.4)
        line.GetYaxis().SetTitleSize(line.GetYaxis().GetTitleSize()*2.4)
        line.GetYaxis().CenterTitle(1);
        line.GetYaxis().SetTitle('data/MC');
        line.GetYaxis().SetNdivisions( 503 );
#        line.GetXaxis().SetLabelOffset( 0.006 );
        line.GetXaxis().SetNdivisions( 510 );
        line.GetXaxis().SetTickLength( line.GetXaxis().GetTickLength() * 2.0 );
        line.GetYaxis().SetTickLength( line.GetYaxis().GetTickLength() * 1.65 );

        line.Draw('histo')
        line.SetLineWidth(1)
        objects.append(line)
        objects.append(ratiograph)
        ratiograph.Draw('sameP')



#    print len(canvases)
    printCanvases(canvases,name)
    writeObjects(canvases,name)


##WIP
def plotDataMCwSysts(listOfHistoListsData,listOfHistoLists,ListSysHistosUp,ListSysHistosDown,samples,name,logscale=False,label='',ratio=True,options='histo'):    
    if isinstance(label, basestring):
        labeltexts=len(listOfHistoListsData)*[label]
    else:
        labeltexts=label
    canvases=[]
    objects=[]   
    i=0
    print "listOfHistoLists", len(listOfHistoLists)
    # for every plot, look at all samples
    for listOfHistos,listOfHistosData,labeltext in zip(listOfHistoLists,listOfHistoListsData,labeltexts):
        print "listOfHistos", len(listOfHistos), listOfHistos
        i+=1
        # setup histo style
        for histo,sample in zip(listOfHistos,samples):
            yTitle='Events'
            setupHisto(histo,sample.color,yTitle,True) 
        # 
        # mover over/underflow
        for h in listOfHistos:
            moveOverFlow(h)
       # print i, "bla", len(ListSysHistosUp), len(ListSysHistosUp[0])
        for w in ListSysHistosUp:
#          print len(w)
#          print i, len(w[i-1])
          for h in w[i-1]:
            moveOverFlow(h)
        for w in ListSysHistosDown:
          for h in w[i-1]:
            moveOverFlow(h)
        #stack
        stackedListOfHistos=stackHistoList(listOfHistos)
        objects.append(stackedListOfHistos)
        # find maximum
        yMax=1e-9
        for h in stackedListOfHistos:
            yMax=max(h.GetBinContent(h.GetMaximumBin()),yMax)

        # error bars
        nbins=stackedListOfHistos[0].GetNbinsX()
        errorgraph=ROOT.TGraphAsymmErrors(nbins)
        ratioerrorgraph=ROOT.TGraphAsymmErrors(nbins)
        errorsup=[]
        errorsdown=[]
        for ibin in range(nbins):
          thisbinErrorUp=0.0
          thisbinErrorDown=0.0
          thisbin=ibin+1
          thisbinwidth=stackedListOfHistos[0].GetBinWidth(thisbin)
          centralY=stackedListOfHistos[0].GetBinContent(thisbin)
          centralX=stackedListOfHistos[0].GetBinCenter(thisbin)
          thisStatUp=stackedListOfHistos[0].GetBinError(thisbin)
          thisStatDown=stackedListOfHistos[0].GetBinError(thisbin)
          for wup, wdown in zip(ListSysHistosUp, ListSysHistosDown):
            stackedUp=stackHistoList(wup[i-1])[0]
            stackedDown=stackHistoList(wdown[i-1])[0]
            diffUp=stackedUp.GetBinContent(thisbin)-centralY
            diffDown=stackedDown.GetBinContent(thisbin)-centralY
            if stackedUp.GetBinContent(thisbin) > centralY:
              thisbinErrorUp+=diffUp*diffUp
            else:
              thisbinErrorUp+=diffDown*diffDown
            if stackedDown.GetBinContent(thisbin) > centralY:
              thisbinErrorDown+=diffUp*diffUp
            else:
              thisbinErrorDown+=diffDown*diffDown
            print stackedUp.GetName(), centralX, stackedDown.GetBinContent(thisbin), centralY, stackedUp.GetBinContent(thisbin), diffUp, diffDown
          errorgraph.SetPoint(ibin, centralX,centralY)
          thisbinErrorUp+=thisStatUp*thisStatUp
          thisbinErrorDown+=thisStatDown*thisStatDown
          print "stat error", thisStatDown, centralY, thisStatUp
          print ROOT.TMath.Sqrt(thisbinErrorDown), ROOT.TMath.Sqrt(thisbinErrorUp)
          errorgraph.SetPointError(ibin, thisbinwidth/2.0,thisbinwidth/2.0,ROOT.TMath.Sqrt(thisbinErrorDown), ROOT.TMath.Sqrt(thisbinErrorUp))
          ratioerrorgraph.SetPoint(ibin,centralX, 1.0)
          relErrUp=0.0
          relErrDown=0.0
          if centralY>0.0:
            relErrUp=ROOT.TMath.Sqrt(thisbinErrorUp)/centralY
            relErrDown=ROOT.TMath.Sqrt(thisbinErrorDown)/centralY
          ratioerrorgraph.SetPointError(ibin, thisbinwidth/2.0,thisbinwidth/2.0, relErrUp, relErrDown)
	  print 


        errorgraph.SetFillStyle(3154)
        errorgraph.SetLineColor(ROOT.kBlack)
        errorgraph.SetFillColor(ROOT.kBlack)
#        ratioerrorgraph.SetFillStyle(3154)
        ratioerrorgraph.SetFillStyle(1001)
        ratioerrorgraph.SetLineColor(ROOT.kBlack)
        ratioerrorgraph.SetFillColor(ROOT.kGreen)

        canvas=getCanvas(stackedListOfHistos[0].GetName(),ratio)        
        canvas.cd(1)
        #draw first histo
        h=stackedListOfHistos[0]
        if logscale:
            h.GetYaxis().SetRangeUser(yMax/1000000,yMax*10)
            canvas.cd(1).SetLogy()
        else:
            h.GetYaxis().SetRangeUser(0,yMax*1.5)
        option='histo'
        option+=options
        h.DrawCopy(option)
        #draw remaining
        for h in stackedListOfHistos[1:]:
            h.DrawCopy(option+'same')
        h.DrawCopy('axissame')
        #draw data
        data=getDataGraph(listOfHistosData)
        data.Draw('samePE1')
        
        errorgraph.Draw("2")
        l=getLegend()
        l.AddEntry2(data,'data','P')
        for h,sample in zip(stackedListOfHistos,samples):
            l.AddEntry2(h,sample.name,'F')

        canvases.append(canvas)
        l.Draw('same')
        objects.append(data)
        objects.append(l)
        objects.append(errorgraph)

#        cms = ROOT.TLatex(0.2, 0.96, 'CMS private work'  );
#        cms.SetTextFont(42)
#        cms.SetTextSize(0.05)
#        cms.SetNDC()
#        cms.Draw()
#        objects.append(cms)

        lumi = ROOT.TLatex(0.2, 0.89, '2.46 fb^{-1} @ 13 TeV'  );
        lumi.SetTextFont(42)
        lumi.SetTextSize(0.06)
        lumi.SetNDC()
#        lumi.Draw()
        objects.append(lumi)

        label = ROOT.TLatex(0.2, 0.83, labeltext);
        label.SetTextFont(42)
        label.SetTextSize(0.06)
        label.SetNDC()
        label.Draw()
        objects.append(label)


        ratiograph,ratiominimum,ratiomaximum=getRatioGraph(data,stackedListOfHistos[0])
        canvas.cd(2)
        line=listOfHistos[0].Clone()
        line.SetFillStyle(0)
        line.Divide(listOfHistos[0])
        #line.GetYaxis().SetRangeUser(0.5,1.6)
        line.GetYaxis().SetRangeUser(ratiominimum-0.2,ratiomaximum+0.2)

        line.GetXaxis().SetRangeUser(listOfHistos[0].GetXaxis().GetXmin(),listOfHistos[0].GetXaxis().GetXmax())
        for kbin in range(line.GetNbinsX()+1):
            line.SetBinContent(kbin,1)
            line.SetBinError(kbin,0)
        line.GetXaxis().SetLabelSize(line.GetXaxis().GetLabelSize()*2.4)
        line.GetYaxis().SetLabelSize(line.GetYaxis().GetLabelSize()*2.4)
        line.GetXaxis().SetTitleSize(line.GetXaxis().GetTitleSize()*3)
        line.GetYaxis().SetTitleSize(line.GetYaxis().GetTitleSize()*2.4)
        line.GetYaxis().SetTitleSize(line.GetYaxis().GetTitleSize()*2.4)
        line.GetYaxis().CenterTitle(1);
        line.GetYaxis().SetTitle('data/MC');
        line.GetYaxis().SetNdivisions( 503 );
#        line.GetXaxis().SetLabelOffset( 0.006 );
        line.GetXaxis().SetNdivisions( 510 );
        line.GetXaxis().SetTickLength( line.GetXaxis().GetTickLength() * 2.0 );
        line.GetYaxis().SetTickLength( line.GetYaxis().GetTickLength() * 1.65 );

        line.Draw('histo')
        line.SetLineWidth(1)
        ratioerrorgraph.Draw("2")
        objects.append(ratioerrorgraph)
        objects.append(line)
        objects.append(ratiograph)
        ratiograph.Draw('sameP')




    printCanvases(canvases,name)
    writeObjects(canvases,name)


def writeLOLAndOneOnTop(listOfHistoLists,samples,listOfhistosOnTop,sampleOnTop,factor,name,logscale=False,options='histo',ontopoptions='samehisto',sepaTest=False):
    normalize=False
    stack=True,
    canvases=[]
    objects=[]   
    i=0
    print "ok"
    
    for listOfHistos,ot in zip(listOfHistoLists,listOfhistosOnTop):
        print i
        i+=1
        
        integralfactor=0
        for histo,sample in zip(listOfHistos,samples):

            yTitle='Events expected for 12.9 fb^{-1} @ 13 TeV'
#            yTitle='Events'
            setupHisto(histo,sample.color,yTitle,stack) 
            
            if factor < 0:
              integralfactor+=histo.Integral()
        
        if factor < 0:    
          integralfactor=integralfactor/ot.Integral()
            
        c=drawHistosOnCanvas(listOfHistos,normalize,stack,logscale,options)       
        #c.SetName('c'+str(i))
        c.cd()
        otc=ot.Clone()
        setupHisto(otc,sampleOnTop.color,'',False)
        otc.SetBinContent(1,otc.GetBinContent(0)+otc.GetBinContent(1));
        otc.SetBinContent(otc.GetNbinsX(),otc.GetBinContent(otc.GetNbinsX()+1)+otc.GetBinContent(otc.GetNbinsX()));
        otc.SetBinError(1,ROOT.TMath.Sqrt(ROOT.TMath.Power(otc.GetBinError(0),2)+ROOT.TMath.Power(otc.GetBinError(1),2)));
        otc.SetBinError(otc.GetNbinsX(),ROOT.TMath.Sqrt(ROOT.TMath.Power(otc.GetBinError(otc.GetNbinsX()+1),2)+ROOT.TMath.Power(otc.GetBinError(otc.GetNbinsX()),2)));
        otc.SetLineWidth(3)
        l=getLegend()
        if factor >= 0.: 
          l.AddEntry2(otc,sampleOnTop.name+' x '+str(factor),'L')
        else:
          l.AddEntry2(otc,sampleOnTop.name+(' x {:4.0f}').format(integralfactor),'L')
          
        for h,sample in zip(listOfHistos,samples):
            loption='L'
            if stack:
                loption='F'
            l.AddEntry2(h,sample.name,loption)
        canvases.append(c)
        if factor >= 0.:
          otc.Scale(factor)
        else:
          otc.Scale(integralfactor)
        otc.DrawCopy(ontopoptions)
        l.Draw('same')
        objects.append(l)
        objects.append(otc)
        if sepaTest:
            stestss=getSepaTests2(listOfHistos,ot)
            for stests in stestss:
                stests.Draw()
                objects.append(stests)
#        cms = ROOT.TLatex(0.2, 0.96, 'CMS private work'  );
#        cms = ROOT.TLatex(0.18, 0.85, '#splitline{CMS simulation}{WORK IN PROGRESS}'  );
#        cms.SetTextFont(42)
#        cms.SetTextSize(0.065)
#        cms.SetNDC()
#        cms.Draw()
#        objects.append(cms)


    printCanvases(canvases,name)
    writeObjects(canvases,name)




def writeLOLSeveralOnTop(listOfHistoLists,samples,listOfHistoListsOnTop,samplesOnTop,factor,name,logscale=False,options='histo',ontopoptions=['samehisto'],sepaTest=False):
    normalize=False
    stack=True,
    canvases=[]
    objects=[]   
    i=0
    print "ok"
    print 'histofhistolists', listOfHistoLists
    print 'histofhistolistsontop', listOfHistoListsOnTop
    print 'samples', samples
    print 'samplesontop', samplesOnTop
    
        
    for listOfHistos,listOfHistosOnTop in zip(listOfHistoLists,listOfHistoListsOnTop):
        print i
        i+=1
        
        integralfactor=0
        for histo,sample in zip(listOfHistos,samples):

            yTitle='Events expected for 37.8 fb^{-1} @ 13 TeV'
#            yTitle='Events'
#            print histo
            setupHisto(histo,sample.color,yTitle,stack) 
            
            if factor < 0:
              integralfactor+=histo.Integral()
              print 'INTEGRALFACTOR',integralfactor
        c=drawHistosOnCanvas(listOfHistos,normalize,stack,logscale,options)       
        #c.SetName('c'+str(i))
        c.cd()
        otcs=[]
        l=getLegend()
        for ot, sampleOnTop in zip(listOfHistosOnTop, samplesOnTop):
            #if factor < 0:    
                #integralfactor=integralfactor/ot.Integral()

            otc=ot.Clone()
            otcs.append(otc)
            setupHisto(otc,sampleOnTop.color,'',False)
            otc.SetBinContent(1,otc.GetBinContent(0)+otc.GetBinContent(1));
            otc.SetBinContent(otc.GetNbinsX(),otc.GetBinContent(otc.GetNbinsX()+1)+otc.GetBinContent(otc.GetNbinsX()));
            otc.SetBinError(1,ROOT.TMath.Sqrt(ROOT.TMath.Power(otc.GetBinError(0),2)+ROOT.TMath.Power(otc.GetBinError(1),2)));
            otc.SetBinError(otc.GetNbinsX(),ROOT.TMath.Sqrt(ROOT.TMath.Power(otc.GetBinError(otc.GetNbinsX()+1),2)+ROOT.TMath.Power(otc.GetBinError(otc.GetNbinsX()),2)));
            otc.SetLineWidth(3)
            if factor >= 0.: 
                l.AddEntryZprime(otc,sampleOnTop.name+' x '+str(factor)[:4],'L')
            else:
                l.AddEntryZprime(otc,sampleOnTop.name+(' x ')+str(integralfactor/otc.Integral()*abs(factor))[:4],'L')
                #l.AddEntryZprime(otc,sampleOnTop.name+(' x {:4.0f}').format(integralfactor/otc.Integral()*abs(factor)),'L')
          
        for h,sample in zip(listOfHistos,samples):
            loption='L'
            if stack:
                loption='F'
            l.AddEntryZprime(h,sample.name,loption)
        canvases.append(c)
        for otc, ontopoption in zip(otcs,ontopoptions):
            if factor >= 0.:
                otc.Scale(factor)
            else:
                otc.Scale(integralfactor/otc.Integral()*abs(factor))
            otc.DrawCopy(ontopoption)
            l.Draw('same')
            objects.append(l)
            objects.append(otc)
        if sepaTest:
            stestss=getSepaTests2(listOfHistos,listOfHistosOnTop)
            for stests in stestss:
                stests.Draw()
                objects.append(stests)
#        cms = ROOT.TLatex(0.2, 0.96, 'CMS private work'  );
#        cms = ROOT.TLatex(0.18, 0.85, '#splitline{CMS simulation}{WORK IN PROGRESS}'  );
#        cms.SetTextFont(42)
#        cms.SetTextSize(0.065)
#        cms.SetNDC()
#        cms.Draw()
#        objects.append(cms)


    printCanvases(canvases,name)
    writeObjects(canvases,name)

def eventYields(hl_data,hl_mc,samples,tablename,witherror=True,makeRatios=True):
    h_data=hl_data[0].Clone()
    for h in hl_data[1:]:
        h_data.Add(h)
    s_data=Sample('data')
    s_bkg=Sample('sum of backgrounds')
    h_bkg=hl_mc[1].Clone()
    for h in hl_mc[2:]:
        h_bkg.Add(h.Clone())
    hratio=None
    if makeRatios:
      hratio=hl_mc[0].Clone()
      hratio.Divide(h_bkg)
      s_ratio=Sample('S/B')
      hratioData=h_data.Clone()
      hratioData.Divide(h_bkg)
      s_ratioData=Sample('data/B')
      turn1dHistosToTable(hl_mc[1:]+[h_bkg]+[hl_mc[0]]+[h_data]+[hratio,hratioData],samples[1:]+[s_bkg]+[samples[0]]+[s_data]+[s_ratio,s_ratioData],tablename,witherror)
    else:
      turn1dHistosToTable(hl_mc[1:]+[h_bkg]+[hl_mc[0]]+[h_data],samples[1:]+[s_bkg]+[samples[0]]+[s_data],tablename,witherror)
    command=['pdflatex',tablename+'.tex']
    subprocess.call(command)

def plotDataMCan(listOfHistoListsData,listOfHistoLists,samples,listOfhistosOnTop,sampleOnTop,factor,name,logscale=False,label='',ratio=True,blind=False,options='histo'):    
    if isinstance(label, basestring):
        labeltexts=len(listOfHistoListsData)*[label]
    else:
        labeltexts=label
    canvases=[]
    objects=[]   
    i=0
#    print len(listOfHistoLists)
    # for every plot, look at all samples
    for ot,listOfHistos,listOfHistosData,labeltext in zip(listOfhistosOnTop,listOfHistoLists,listOfHistoListsData,labeltexts):
        i+=1
#        print i
        # setup histo style
        integralfactor=0
        for histo,sample in zip(listOfHistos,samples):
            yTitle='Events'
            setupHisto(histo,sample.color,yTitle,True)
            
            if factor < 0:
              integralfactor+=histo.Integral()
        
        if factor < 0:    
          integralfactor=integralfactor/ot.Integral()
          
        # 
        # mover over/underflow
        for h in listOfHistos:
            moveOverFlow(h)
        #stack
        stackedListOfHistos=stackHistoList(listOfHistos)
        objects.append(stackedListOfHistos)
        # find maximum
        yMax=1e-9
        for h in stackedListOfHistos:
            yMax=max(h.GetBinContent(h.GetMaximumBin()),yMax)
        canvas=getCanvas(stackedListOfHistos[0].GetName(),ratio)        
        canvas.cd(1)
        #draw first histo
        h=stackedListOfHistos[0]
        if logscale:
            h.GetYaxis().SetRangeUser(yMax/10000,yMax*10)
            canvas.cd(1).SetLogy()
        else:
            h.GetYaxis().SetRangeUser(0,yMax*1.5)
        option='histo'
        option+=options
        h.DrawCopy(option)
        #draw remaining
        for h in stackedListOfHistos[1:]:
            h.DrawCopy(option+'same')
        h.DrawCopy('axissame')
        #draw data
        otc=ot.Clone()
        nok=99999
        if blind:
            for ibin in range(stackedListOfHistos[0].GetNbinsX()):
                if otc.GetBinContent(ibin)>0 and stackedListOfHistos[0].GetBinContent(ibin)/otc.GetBinContent(ibin)<100:
                    nok=ibin-1
                    break
        data=getDataGraph(listOfHistosData,nok)
        setupHisto(otc,sampleOnTop.color,'',False)
        otc.SetBinContent(1,otc.GetBinContent(0)+otc.GetBinContent(1));
        otc.SetBinContent(otc.GetNbinsX(),otc.GetBinContent(otc.GetNbinsX()+1)+otc.GetBinContent(otc.GetNbinsX()));
        otc.SetBinError(1,ROOT.TMath.Sqrt(ROOT.TMath.Power(otc.GetBinError(0),2)+ROOT.TMath.Power(otc.GetBinError(1),2)));
        otc.SetBinError(otc.GetNbinsX(),ROOT.TMath.Sqrt(ROOT.TMath.Power(otc.GetBinError(otc.GetNbinsX()+1),2)+ROOT.TMath.Power(otc.GetBinError(otc.GetNbinsX()),2)));
        otc.SetLineWidth(3)
        if factor >= 0.:
          otc.Scale(factor)
        else:
          otc.Scale(integralfactor)
        otc.Draw('histosame')
        data.Draw('samePE1')
        l=getLegend()
        l.AddEntry2(data,'data','P')
        if factor >= 0.: 
          l.AddEntry2(otc,sampleOnTop.name+' x '+str(factor),'L')
        else:
          l.AddEntry2(otc,sampleOnTop.name+(' x {:4.0f}').format(integralfactor),'L')
        for h,sample in zip(stackedListOfHistos,samples):
            l.AddEntry2(h,sample.name,'F')

        canvases.append(canvas)
        l.Draw('same')
        objects.append(data)
        objects.append(l)
        objects.append(otc)

        #draw the lumi text on the canvas
        CMS_lumi.lumi_13TeV = "12.9 fb^{-1}"
        CMS_lumi.writeExtraText = 1
        CMS_lumi.extraText = "Preliminary"
        CMS_lumi.lumi_sqrtS = "13 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

        CMS_lumi.cmsTextSize = 0.55
        CMS_lumi.cmsTextOffset = 0.49
        CMS_lumi.lumiTextSize = 0.43
        CMS_lumi.lumiTextOffset = 0.61
        
        CMS_lumi.relPosX = 0.15
        
        CMS_lumi.hOffset = 0.05
        
        iPeriod=4   # 13TeV
        iPos=0     # CMS inside frame
        
        CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)

        label = ROOT.TLatex(0.2, 0.89, labeltext);
        label.SetTextFont(42)
        label.SetTextSize(0.05)
        label.SetNDC()
        label.Draw()
        objects.append(label)


        ratiograph,ratiominimum,ratiomaximum=getRatioGraph(data,stackedListOfHistos[0])
        canvas.cd(2)
        line=listOfHistos[0].Clone()
        line.SetFillStyle(0)
        line.Divide(listOfHistos[0])
            
        #line.GetYaxis().SetRangeUser(0.5,1.6)
        line.GetYaxis().SetRangeUser(ratiominimum-0.2,ratiomaximum+0.2)
        line.GetXaxis().SetRangeUser(listOfHistos[0].GetXaxis().GetXmin(),listOfHistos[0].GetXaxis().GetXmax())
        for i in range(line.GetNbinsX()+2):
            line.SetBinContent(i,1)
            line.SetBinError(i,0)
        line.GetXaxis().SetLabelSize(line.GetXaxis().GetLabelSize()*2.4)
        line.GetYaxis().SetLabelSize(line.GetYaxis().GetLabelSize()*2.4)
        line.GetXaxis().SetTitleSize(line.GetXaxis().GetTitleSize()*3)
        line.GetYaxis().SetTitleSize(line.GetYaxis().GetTitleSize()*2.4)
        line.GetYaxis().SetTitleSize(line.GetYaxis().GetTitleSize()*2.4)
        line.GetYaxis().CenterTitle(1);
        line.GetYaxis().SetTitle('data/MC');
        line.GetYaxis().SetNdivisions( 503 );
#        line.GetXaxis().SetLabelOffset( 0.006 );
        line.GetXaxis().SetNdivisions( 510 );
        line.GetXaxis().SetTickLength( line.GetXaxis().GetTickLength() * 2.0 );
        line.GetYaxis().SetTickLength( line.GetYaxis().GetTickLength() * 1.65 );

        line.Draw('histo')
        line.SetLineWidth(1)
        objects.append(line)
        objects.append(ratiograph)
        ratiograph.Draw('sameP')



#    print len(canvases)
    printCanvases(canvases,name)
    writeObjects(canvases,name)


def plotDataMCanWsyst(listOfHistoListsData,listOfHistoLists,samples,listOfhistosOnTop,sampleOnTop,factor,name,listOflll,logscale=False,label='',ratio=True,blinded=False, diff=False, MCData=False, autoscaleRatioYAxis=False):    
################################################




################################################
    options='histo'
    
    if isinstance(label, basestring):
        labeltexts=len(listOfHistoListsData)*[label]
    else:
        labeltexts=label
    canvases=[]
    objects=[]   
    histosforcombine=[]
    i=0
#    print len(listOfHistoLists)
    # for every plot, look at all samples
    listOfErrorGraphs=[]
    listOfErrorGraphStyles=[]
    listOfErrorGraphColors=[]
    
    listOfErrorGraphLists=[]
    #lll=[listOflistOflist of histograms, FillStyle, FillColor, DoRateSysts]
    for lll in listOflll:
      listOfErrorGraphLists.append(createErrorbands(lll[0],samples,lll[3]))
      #print listOfErrorGraphLists[-1]
      #raw_input()
      listOfErrorGraphStyles.append(lll[1])
      listOfErrorGraphColors.append(lll[2])
      print ''
      print 'listOfErrorGraphLists[0]  ',listOfErrorGraphLists[0]
      
    for ll in lll[0]:
      for l in ll:
          for hl in l:
            histosforcombine.append(hl)
      
    for igraph in range(len(listOfErrorGraphLists[0])):
      thisgraphs=[]
      for iband in range(len(listOfErrorGraphLists)):
	thisgraphs.append([listOfErrorGraphLists[iband][igraph],listOfErrorGraphStyles[iband],listOfErrorGraphColors[iband]])
      listOfErrorGraphs.append(thisgraphs)
    #for g in listOfErrorGraphs:
      #print g
    print len(listOfhistosOnTop),len(listOfHistoLists),len(listOfHistoListsData),len(labeltexts),len(listOfErrorGraphs)
    #raw_input()
    for ot,listOfHistos,listOfHistosData,labeltext,errorgraphList in zip(listOfhistosOnTop,listOfHistoLists,listOfHistoListsData,labeltexts,listOfErrorGraphs):
        print 'histoOnTop',ot,'ListofHistos',listOfHistos
        i+=1
#        print i
        # setup histo style
        integralfactor=0
        for histo,sample in zip(listOfHistos,samples):
            yTitle='Events'
            setupHisto(histo,sample.color,yTitle,True)
            
            if factor < 0:
              integralfactor+=histo.Integral()
        
        if factor < 0:    
          integralfactor=integralfactor/ot.Integral()
      
        # 
        # mover over/underflow
        for h in listOfHistos:
            if not MCData:
                alpha = 1 - 0.6827
                for i in range(0,h.GetNbinsX()):
                    N = h.GetBinContent(i);
                    L=0
                    if N!=0:
                        L=ROOT.Math.gamma_quantile(alpha/2,N,1.)
                    U =  ROOT.Math.gamma_quantile_c(alpha/2,N+1,1)
                    #h.SetBinError(i, N-L);
                    h.SetBinError(i, U-N);
                    #h.SetPointEYhigh(i, U-N);

            moveOverFlow(h)
            histosforcombine.append(h)
            
        for hdata in listOfHistosData:
            histosforcombine.append(hdata)
        #stack
        stackedListOfHistos=stackHistoList(listOfHistos)
        objects.append(stackedListOfHistos)
        # find maximum
        yMax=1e-9
        for h in stackedListOfHistos:
            yMax=max(h.GetBinContent(h.GetMaximumBin()),yMax)
        canvas=getCanvas(stackedListOfHistos[0].GetName(),ratio)        
        canvas.cd(1)
        #draw first histo
        h=stackedListOfHistos[0]
        if logscale:
            h.GetYaxis().SetRangeUser(yMax/10000,yMax*10)
            canvas.cd(1).SetLogy()
        else:
            h.GetYaxis().SetRangeUser(0,yMax*1.8)
        option='histo'
        option+=options
        h.DrawCopy(option)
        print h.GetName()
        #h.GetXaxis().SetBinLabel(1,"test")
        #draw remaining
        for h in stackedListOfHistos[1:]:
            h.DrawCopy(option+'same')
        h.DrawCopy('axissame')
#make error bars ##########
###

        otc=ot.Clone()
        nok=99999
        if blinded:
            for ibin in range(stackedListOfHistos[0].GetNbinsX()):
                if otc.GetBinContent(ibin)>0 and stackedListOfHistos[0].GetBinContent(ibin)/otc.GetBinContent(ibin)<100:
                    nok=ibin-1
                    break
        data,blind=getDataGraphBlind(listOfHistosData,nok, MCData)
        setupHisto(otc,sampleOnTop.color,'',False)
        otc.SetBinContent(1,otc.GetBinContent(0)+otc.GetBinContent(1));
        otc.SetBinContent(otc.GetNbinsX(),otc.GetBinContent(otc.GetNbinsX()+1)+otc.GetBinContent(otc.GetNbinsX()));
        otc.SetBinError(1,ROOT.TMath.Sqrt(ROOT.TMath.Power(otc.GetBinError(0),2)+ROOT.TMath.Power(otc.GetBinError(1),2)));
        otc.SetBinError(otc.GetNbinsX(),ROOT.TMath.Sqrt(ROOT.TMath.Power(otc.GetBinError(otc.GetNbinsX()+1),2)+ROOT.TMath.Power(otc.GetBinError(otc.GetNbinsX()),2)));
        otc.SetLineWidth(2)
        if factor >= 0.:
          otc.Scale(factor)
        else:
          otc.Scale(integralfactor)
        otc.Draw('histosame')
        if MCData:
            data.SetMarkerStyle(ROOT.kOpenCircle)
            data.SetMarkerColor(ROOT.kGray+2)

        data.Draw('samePE1')
        blind.SetFillStyle(3665)
        #blind.SetFillStyle(1001)
        blind.SetLineColor(ROOT.kGray)
        blind.SetFillColor(ROOT.kGray)
        if blinded:
            blind.Draw('same2')
        objects.append(blind)
        #objects.append(data)
        
        
        listOfRatioErrorGraphs=[]
        graphcounter=0
        for errorgraph,thisFillStyle,ThisFillColor in errorgraphList:
	  ratioerrorgraph=ROOT.TGraphAsymmErrors(errorgraph.GetN())
	  #print ratioerrorgraph
	  #raw_input()
	  x, y = ROOT.Double(0), ROOT.Double(0)
	  for i in range(errorgraph.GetN()):
	      errorgraph.GetPoint(i,x,y)
	      ratioerrorgraph.SetPoint(i,x, 1.0)
	      relErrUp=0.0
	      relErrDown=0.0
	      if y>0.0:
		  relErrUp=errorgraph.GetErrorYhigh(i)/y
		  relErrDown=errorgraph.GetErrorYlow(i)/y
	      ratioerrorgraph.SetPointError(i, errorgraph.GetErrorXlow(i),errorgraph.GetErrorXhigh(i), relErrUp, relErrDown)

  
	  errorgraph.SetFillStyle(thisFillStyle)
	  errorgraph.SetLineColor(ThisFillColor)
	  errorgraph.SetFillColor(ThisFillColor)
	  ratioerrorgraph.SetFillStyle(thisFillStyle)
	  ratioerrorgraph.SetLineColor(ThisFillColor)
	  ratioerrorgraph.SetFillColor(ThisFillColor)
  #        ratioerrorgraph.SetFillStyle(1001)
  #        ratioerrorgraph.SetLineColor(ROOT.kBlack)
  #        ratioerrorgraph.SetFillColor(ROOT.kGreen)

	  #if graphcounter==0:
	    #errorgraph.Draw("2")
	  #else:
	  errorgraph.Draw("same2")  
	  graphcounter+=1

	  objects.append(errorgraph)
	  objects.append(ratioerrorgraph)
	  listOfRatioErrorGraphs.append(ratioerrorgraph)
	  #print objects
	  #raw_input()
        
        l1=getLegendL()
        l2=getLegendR()
        if MCData:
            l1.AddEntry22(data,'MCData','P')
        else:
            l1.AddEntry22(data,'data','P')
        if factor >= 0.: 
          l2.AddEntry22(otc,sampleOnTop.name+' x '+str(factor),'L')
        else:
          l2.AddEntry22(otc,sampleOnTop.name+(' x {:4.0f}').format(integralfactor),'L')
        i=0
        for h,sample in zip(stackedListOfHistos,samples):
            i+=1
            if i%2==1:
                l1.AddEntry22(h,sample.name,'F')
            if i%2==0:
                l2.AddEntry22(h,sample.name,'F')

        canvases.append(canvas)
        l1.Draw('same')
        l2.Draw('same')
        objects.append(data)
        objects.append(l1)
        objects.append(l2)
        objects.append(otc)
        
        #draw the lumi text on the canvas
        CMS_lumi.lumi_13TeV = "37.8 fb^{-1}"
        CMS_lumi.writeExtraText = 1
        CMS_lumi.extraText = "Preliminary"
        CMS_lumi.lumi_sqrtS = "13 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

        CMS_lumi.cmsTextSize = 0.55
        CMS_lumi.cmsTextOffset = 0.49
        CMS_lumi.lumiTextSize = 0.43
        CMS_lumi.lumiTextOffset = 0.61
        
        CMS_lumi.relPosX = 0.15
        
        CMS_lumi.hOffset = 0.05
        
        iPeriod=4   # 13TeV
        iPos=0     # CMS inside frame
        
        CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)
        
        labelobj=label
        labelobj = ROOT.TLatex(0.18, 0.89, labeltext);
        labelobj.SetTextFont(42)
        labelobj.SetTextSize(0.035)
        labelobj.SetNDC()
        labelobj.Draw()
        objects.append(labelobj)


        ratiograph,ratiominimum,ratiomaximum=getRatioGraph(data,stackedListOfHistos[0])
        canvas.cd(2)
        line=listOfHistos[0].Clone()
        line.SetFillStyle(0)
        line.Divide(listOfHistos[0])
        
        emptyHisto=listOfHistos[0].Clone()
        print emptyHisto.GetName()
        emptyHisto.SetFillStyle(0)
        #line.GetYaxis().SetRangeUser(0.5,1.6)
        line.GetYaxis().SetRangeUser(0.0,2.0)
        if autoscaleRatioYAxis:
            line.GetYaxis().SetRangeUser(ratiominimum-0.2,ratiomaximum+0.2)
        line.GetXaxis().SetRangeUser(listOfHistos[0].GetXaxis().GetXmin(),listOfHistos[0].GetXaxis().GetXmax())
        for i in range(line.GetNbinsX()+2):
            line.SetBinContent(i,1)
            line.SetBinError(i,0)
        #print listOfHistos[0].GetXaxis().GetXmin(),listOfHistos[0].GetXaxis().GetXmax(),listOfHistos[0].GetXaxis().GetBinLabel(1)
        #print line.GetXaxis().GetXmin(),line.GetXaxis().GetXmax(),line.GetXaxis().GetBinLabel(1)
        #raw_input()
        line.GetXaxis().SetLabelSize(line.GetXaxis().GetLabelSize()*2.4)
        line.GetYaxis().SetLabelSize(line.GetYaxis().GetLabelSize()*2.4)
        line.GetXaxis().SetTitleSize(line.GetXaxis().GetTitleSize()*3)
        #line.GetYaxis().SetTitleSize(line.GetYaxis().GetTitleSize()*2.4)
        line.GetYaxis().SetTitleSize(line.GetYaxis().GetTitleSize()*2.4)
        line.GetYaxis().CenterTitle(1);
        line.GetYaxis().SetTitle('Data/MC');
        if MCData:
            line.GetYaxis().SetTitle('MCData/MC');
        line.GetYaxis().SetNdivisions( 503 );
        line.GetYaxis().SetTitleOffset( 0.5 );
        line.GetXaxis().SetNdivisions( 510 );
        line.GetXaxis().SetTickLength( line.GetXaxis().GetTickLength() * 2.0 );
        line.GetYaxis().SetTickLength( line.GetYaxis().GetTickLength() * 1.65 );

        #line.GetXaxis().SetBinLabel(4,"bla")
        line.Draw('histo')
        objects.append(ratiograph)
        #print len(listOfRatioErrorGraphs)
        for ratioerrorgraph in listOfRatioErrorGraphs:
          ratioerrorgraph.Draw("same2")
#        objects.append(ratioerrorgraph)
        if MCData:
            ratiograph.SetMarkerStyle(ROOT.kOpenCircle)
            ratiograph.SetMarkerColor(ROOT.kGray+2)
        ratiograph.Draw('sameP')
        line.SetLineWidth(1)
        line.Draw('histosame')
        #emptyHisto.GetYaxis().SetTitle('data/MC');
        #print "title? ", emptyHisto.GetYaxis().GetTitle()
        #print "title? ", line.GetYaxis().GetTitle()
        line.Draw('axissame')
        #emptyHisto.Draw("axissame")
        #objects.append(emptyHisto)
        objects.append(line)
        #print labeltext
        #raw_input()

        #print labeltext
        #raw_input()

    
    print histosforcombine
#    print len(canvases)
    printCanvases(canvases,name)
    writeObjects(canvases,name)
    writeObjects(histosforcombine,name+'_'+label+'_combinehistos')
###################################################    


#def plotDataMCanWsystdiff(listOfHistoListsData,listOfHistoLists,samples,listOfhistosOnTop,sampleOnTop,factor,name,listOflll,logscale=False,label='',ratio=True,blinded=False, diff=False):    

    #options='histo'
    #if isinstance(label, basestring):
        #labeltexts=len(listOfHistoListsData)*[label]
    #else:
        #labeltexts=label
    #canvases=[]
    #objects=[]   
    #i=0
##    print len(listOfHistoLists)
    ## for every plot, look at all samples
    #listOfErrorGraphs=[]
    #listOfErrorGraphStyles=[]
    #listOfErrorGraphColors=[]
    
    #listOfErrorGraphLists=[]
    ##lll=[listOflistOflist of histograms, FillStyle, FillColor, DoRateSysts]
    #for lll in listOflll:
      #listOfErrorGraphLists.append(createErrorbands(lll[0],samples,lll[3]))
      ##print listOfErrorGraphLists[-1]
      ##raw_input()
      #listOfErrorGraphStyles.append(lll[1])
      #listOfErrorGraphColors.append(lll[2])
      #print ''
      #print 'listOfErrorGraphLists[0]  ',listOfErrorGraphLists[0]
    #for igraph in range(len(listOfErrorGraphLists[0])):
      #thisgraphs=[]
      #for iband in range(len(listOfErrorGraphLists)):
	#thisgraphs.append([listOfErrorGraphLists[iband][igraph],listOfErrorGraphStyles[iband],listOfErrorGraphColors[iband]])
      #listOfErrorGraphs.append(thisgraphs)
    ##for g in listOfErrorGraphs:
      ##print g
    #print len(listOfhistosOnTop),len(listOfHistoLists),len(listOfHistoListsData),len(labeltexts),len(listOfErrorGraphs)
    ##raw_input()
    #for ot,listOfHistos,listOfHistosData,labeltext,errorgraphList in zip(listOfhistosOnTop,listOfHistoLists,listOfHistoListsData,labeltexts,listOfErrorGraphs):
        #print 'histoOnTop',ot,'ListofHistos',listOfHistos
        #i+=1
##        print i
        ## setup histo style
        #integralfactor=0
        #for histo,sample in zip(listOfHistos,samples):
            #yTitle='Events'
            #setupHisto(histo,sample.color,yTitle,True)
            
            #if factor < 0:
              #integralfactor+=histo.Integral()
        
        #if factor < 0:    
          #integralfactor=integralfactor/ot.Integral()
            
        ## 
        ## mover over/underflow
        #for h in listOfHistos:
            #moveOverFlow(h)
        ##stack
        #stackedListOfHistos=stackHistoList(listOfHistos)
        #objects.append(stackedListOfHistos)
        ## find maximum
        #yMax=1e-9
        #for h in stackedListOfHistos:
            #yMax=max(h.GetBinContent(h.GetMaximumBin()),yMax)
        #canvas=getCanvas(stackedListOfHistos[0].GetName(),ratio or diff)        
        #canvas.cd(1)
        ##draw first histo
        #h=stackedListOfHistos[0]
        #if logscale:
            #h.GetYaxis().SetRangeUser(yMax/10000,yMax*10)
            #canvas.cd(1).SetLogy()
        #else:
            #h.GetYaxis().SetRangeUser(0,yMax*1.8)
        #option='histo'
        #option+=options
        #h.DrawCopy(option)
        #print h.GetName()
        ##h.GetXaxis().SetBinLabel(1,"test")
        ##draw remaining
        #for h in stackedListOfHistos[1:]:
            #h.DrawCopy(option+'same')
        #h.DrawCopy('axissame')
##make error bars ##########
####

        #otc=ot.Clone()
        #nok=99999
        #if blinded:
            #for ibin in range(stackedListOfHistos[0].GetNbinsX()):
                #if otc.GetBinContent(ibin)>0 and stackedListOfHistos[0].GetBinContent(ibin)/otc.GetBinContent(ibin)<100:
                    #nok=ibin-1
                    #break
        #data,blind=getDataGraphBlind(listOfHistosData,nok)
        #setupHisto(otc,sampleOnTop.color,'',False)
        #otc.SetBinContent(1,otc.GetBinContent(0)+otc.GetBinContent(1));
        #otc.SetBinContent(otc.GetNbinsX(),otc.GetBinContent(otc.GetNbinsX()+1)+otc.GetBinContent(otc.GetNbinsX()));
        #otc.SetBinError(1,ROOT.TMath.Sqrt(ROOT.TMath.Power(otc.GetBinError(0),2)+ROOT.TMath.Power(otc.GetBinError(1),2)));
        #otc.SetBinError(otc.GetNbinsX(),ROOT.TMath.Sqrt(ROOT.TMath.Power(otc.GetBinError(otc.GetNbinsX()+1),2)+ROOT.TMath.Power(otc.GetBinError(otc.GetNbinsX()),2)));
        #otc.SetLineWidth(2)
        #if factor >= 0.:
          #otc.Scale(factor)
        #else:
          #otc.Scale(integralfactor)
        #otc.Draw('histosame')
        #data.Draw('samePE1')
        #blind.SetFillStyle(3665)
        ##blind.SetFillStyle(1001)
        #blind.SetLineColor(ROOT.kGray)
        #blind.SetFillColor(ROOT.kGray)
        #if blinded:
            #blind.Draw('same2')
        #objects.append(blind)
        
        
        #listOfRatioErrorGraphs=[]
        #graphcounter=0
        #if ratio:
            #for errorgraph,thisFillStyle,ThisFillColor in errorgraphList:
                #ratioerrorgraph=ROOT.TGraphAsymmErrors(errorgraph.GetN())
                ##print ratioerrorgraph
                ##raw_input()
                #x, y = ROOT.Double(0), ROOT.Double(0)
            #for i in range(errorgraph.GetN()):
                #errorgraph.GetPoint(i,x,y)
                #ratioerrorgraph.SetPoint(i,x, 1.0)
                #relErrUp=0.0
                #relErrDown=0.0
                #if y>0.0:
                    #relErrUp=errorgraph.GetErrorYhigh(i)/y
                    #relErrDown=errorgraph.GetErrorYlow(i)/y
                #ratioerrorgraph.SetPointError(i, errorgraph.GetErrorXlow(i),errorgraph.GetErrorXhigh(i), relErrUp, relErrDown)

  
            #errorgraph.SetFillStyle(thisFillStyle)
            #errorgraph.SetLineColor(ThisFillColor)
            #errorgraph.SetFillColor(ThisFillColor)
            #ratioerrorgraph.SetFillStyle(thisFillStyle)
            #ratioerrorgraph.SetLineColor(ThisFillColor)
            #ratioerrorgraph.SetFillColor(ThisFillColor)
  ##          ratioerrorgraph.SetFillStyle(1001)
  ##            ratioerrorgraph.SetLineColor(ROOT.kBlack)
  ##         ratioerrorgraph.SetFillColor(ROOT.kGreen)

            ##if graphcounter==0:
                ##errorgraph.Draw("2")
            ##else:
            #errorgraph.Draw("same2")  
            #graphcounter+=1

            #objects.append(errorgraph)
            #objects.append(ratioerrorgraph)
            #listOfRatioErrorGraphs.append(ratioerrorgraph)
            ##print objects
            ##raw_input()
        
          #else if diff:
            #for errorgraph,thisFillStyle,ThisFillColor in errorgraphList:
                #ratioerrorgraph=ROOT.TGraphAsymmErrors(errorgraph.GetN())
                ##print ratioerrorgraph
                ##raw_input()
                #x, y = ROOT.Double(0), ROOT.Double(0)
            #for i in range(errorgraph.GetN()):
                #errorgraph.GetPoint(i,x,y)
                #ratioerrorgraph.SetPoint(i,x, 0.0)
                #relErrUp=0.0
                #relErrDown=0.0
                #if y>0.0:
                    #relErrUp=(errorgraph.GetErrorYhigh(i)-y)/sqrt.(y)
                    #relErrDown=(errorgraph.GetErrorYlow(i)-y)/sqrt.(y)
                #ratioerrorgraph.SetPointError(i, errorgraph.GetErrorXlow(i),errorgraph.GetErrorXhigh(i), relErrUp, relErrDown)

  
            #errorgraph.SetFillStyle(thisFillStyle)
            #errorgraph.SetLineColor(ThisFillColor)
            #errorgraph.SetFillColor(ThisFillColor)
            #ratioerrorgraph.SetFillStyle(thisFillStyle)
            #ratioerrorgraph.SetLineColor(ThisFillColor)
            #ratioerrorgraph.SetFillColor(ThisFillColor)
  ##          ratioerrorgraph.SetFillStyle(1001)
  ##            ratioerrorgraph.SetLineColor(ROOT.kBlack)
  ##         ratioerrorgraph.SetFillColor(ROOT.kGreen)

            ##if graphcounter==0:
                ##errorgraph.Draw("2")
            ##else:
            #errorgraph.Draw("same2")  
            #graphcounter+=1

            #objects.append(errorgraph)
            #objects.append(ratioerrorgraph)
            #listOfRatioErrorGraphs.append(ratioerrorgraph)
            ##print objects
            ##raw_input()
                        
        
        
        
        #l1=getLegendL()
        #l2=getLegendR()
        #l1.AddEntry22(data,'data','P')
        #if factor >= 0.: 
          #l2.AddEntry22(otc,sampleOnTop.name+' x '+str(factor),'L')
        #else:
          #l2.AddEntry22(otc,sampleOnTop.name+(' x {:4.0f}').format(integralfactor),'L')
        #i=0
        #for h,sample in zip(stackedListOfHistos,samples):
            #i+=1
            #if i%2==1:
                #l1.AddEntry22(h,sample.name,'F')
            #if i%2==0:
                #l2.AddEntry22(h,sample.name,'F')

        #canvases.append(canvas)
        #l1.Draw('same')
        #l2.Draw('same')
        #objects.append(data)
        #objects.append(l1)
        #objects.append(l2)
        #objects.append(otc)
        
        ##draw the lumi text on the canvas
        #CMS_lumi.lumi_13TeV = "12.9 fb^{-1}"
        #CMS_lumi.writeExtraText = 1
        #CMS_lumi.extraText = "Preliminary"
        #CMS_lumi.lumi_sqrtS = "13 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

        #CMS_lumi.cmsTextSize = 0.55
        #CMS_lumi.cmsTextOffset = 0.49
        #CMS_lumi.lumiTextSize = 0.43
        #CMS_lumi.lumiTextOffset = 0.61
        
        #CMS_lumi.relPosX = 0.15
        
        #CMS_lumi.hOffset = 0.05
        
        #iPeriod=4   # 13TeV
        #iPos=0     # CMS inside frame
        
        #CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)
        
        #label = ROOT.TLatex(0.18, 0.89, labeltext);
        #label.SetTextFont(42)
        #label.SetTextSize(0.035)
        #label.SetNDC()
        #label.Draw()
        #objects.append(label)


        #ratiograph,ratiominimum,ratiomaximum=getRatioGraph(data,stackedListOfHistos[0])
        #canvas.cd(2)
        #line=listOfHistos[0].Clone()
        #line.SetFillStyle(0)
        #line.Divide(listOfHistos[0])
        
        #emptyHisto=listOfHistos[0].Clone()
        #print emptyHisto.GetName()
        #emptyHisto.SetFillStyle(0)
        ##line.GetYaxis().SetRangeUser(0.5,1.6)
        #line.GetYaxis().SetRangeUser(ratiominimum-0.2,ratiomaximum+0.2)
        #line.GetXaxis().SetRangeUser(listOfHistos[0].GetXaxis().GetXmin(),listOfHistos[0].GetXaxis().GetXmax())
        #for i in range(line.GetNbinsX()+2):
            #line.SetBinContent(i,1)
            #line.SetBinError(i,0)
        ##print listOfHistos[0].GetXaxis().GetXmin(),listOfHistos[0].GetXaxis().GetXmax(),listOfHistos[0].GetXaxis().GetBinLabel(1)
        ##print line.GetXaxis().GetXmin(),line.GetXaxis().GetXmax(),line.GetXaxis().GetBinLabel(1)
        ##raw_input()
        #line.GetXaxis().SetLabelSize(line.GetXaxis().GetLabelSize()*2.4)
        #line.GetYaxis().SetLabelSize(line.GetYaxis().GetLabelSize()*2.4)
        #line.GetXaxis().SetTitleSize(line.GetXaxis().GetTitleSize()*3)
        ##line.GetYaxis().SetTitleSize(line.GetYaxis().GetTitleSize()*2.4)
        #line.GetYaxis().SetTitleSize(line.GetYaxis().GetTitleSize()*2.4)
        #line.GetYaxis().CenterTitle(1);
        #line.GetYaxis().SetTitle('data/MC');
        #line.GetYaxis().SetNdivisions( 503 );
        #line.GetYaxis().SetTitleOffset( 0.5 );
        #line.GetXaxis().SetNdivisions( 510 );
        #line.GetXaxis().SetTickLength( line.GetXaxis().GetTickLength() * 2.0 );
        #line.GetYaxis().SetTickLength( line.GetYaxis().GetTickLength() * 1.65 );

        ##line.GetXaxis().SetBinLabel(4,"bla")
        #line.Draw('histo')
        #objects.append(ratiograph)
        ##print len(listOfRatioErrorGraphs)
        #for ratioerrorgraph in listOfRatioErrorGraphs:
          #ratioerrorgraph.Draw("same2")
##        objects.append(ratioerrorgraph)
        #ratiograph.Draw('sameP')
        #line.SetLineWidth(1)
        #line.Draw('histosame')
        ##emptyHisto.GetYaxis().SetTitle('data/MC');
        ##print "title? ", emptyHisto.GetYaxis().GetTitle()
        ##print "title? ", line.GetYaxis().GetTitle()
        #line.Draw('axissame')
        ##emptyHisto.Draw("axissame")
        ##objects.append(emptyHisto)
        #objects.append(line)
        ##print labeltext
        ##raw_input()

        ##print labeltext
        ##raw_input()

    
    
##    print len(canvases)
    #printCanvases(canvases,name)
    #writeObjects(canvases,name)
    



###################################################

def plotDataMCanWsystCustomBinLabels(listOfHistoListsData,listOfHistoLists,samples,listOfhistosOnTop,sampleOnTop,factor,name,listOflll,listOfmyCustomBinLabels,logscale=False,label='',ratio=True,blinded=False):    

    options='histo'
    if isinstance(label, basestring):
        labeltexts=len(listOfHistoListsData)*[label]
    else:
        labeltexts=label
    canvases=[]
    objects=[]   
    i=0
#    print len(listOfHistoLists)
    # for every plot, look at all samples
    listOfErrorGraphs=[]
    listOfErrorGraphStyles=[]
    listOfErrorGraphColors=[]
    
    listOfErrorGraphLists=[]
    #lll=[listOflistOflist of histograms, FillStyle, FillColor, DoRateSysts]
    for lll in listOflll:
      listOfErrorGraphLists.append(createErrorbands(lll[0],samples,lll[3]))
      #print listOfErrorGraphLists[-1]
      #raw_input()
      listOfErrorGraphStyles.append(lll[1])
      listOfErrorGraphColors.append(lll[2])
    for igraph in range(len(listOfErrorGraphLists[0])):
      thisgraphs=[]
      for iband in range(len(listOfErrorGraphLists)):
	thisgraphs.append([listOfErrorGraphLists[iband][igraph],listOfErrorGraphStyles[iband],listOfErrorGraphColors[iband]])
      listOfErrorGraphs.append(thisgraphs)
    #for g in listOfErrorGraphs:
      #print g
    print len(listOfhistosOnTop),len(listOfHistoLists),len(listOfHistoListsData),len(labeltexts),len(listOfErrorGraphs)
    #raw_input()
    for ot,listOfHistos,listOfHistosData,labeltext,errorgraphList, myCustomBinLabels in zip(listOfhistosOnTop,listOfHistoLists,listOfHistoListsData,labeltexts,listOfErrorGraphs,listOfmyCustomBinLabels):
        i+=1
#        print i
        # setup histo style
        integralfactor=0
        for histo,sample in zip(listOfHistos,samples):
            yTitle='Events'
            setupHisto(histo,sample.color,yTitle,True) 
            
            if factor < 0:
              integralfactor+=histo.Integral()
        
        if factor < 0:    
          integralfactor=integralfactor/ot.Integral()
        
        # 
        # mover over/underflow
        for h in listOfHistos:
            moveOverFlow(h)
        #stack
        stackedListOfHistos=stackHistoList(listOfHistos)
        objects.append(stackedListOfHistos)
        # find maximum
        yMax=1e-9
        for h in stackedListOfHistos:
            yMax=max(h.GetBinContent(h.GetMaximumBin()),yMax)
        canvas=getCanvas(stackedListOfHistos[0].GetName(),ratio)        
        canvas.cd(1)
        #draw first histo
        h=stackedListOfHistos[0]
        if logscale:
            h.GetYaxis().SetRangeUser(yMax/10000,yMax*10)
            canvas.cd(1).SetLogy()
        else:
            h.GetYaxis().SetRangeUser(0,yMax*1.8)
        option='histo'
        option+=options
        h.DrawCopy(option)
        print h.GetName()
        #h.GetXaxis().SetBinLabel(1,"test")
        #draw remaining
        for h in stackedListOfHistos[1:]:
            h.DrawCopy(option+'same')
        h.DrawCopy('axissame')
#make error bars ##########
###

        otc=ot.Clone()
        nok=99999
        if blinded:
            for ibin in range(stackedListOfHistos[0].GetNbinsX()):
                if otc.GetBinContent(ibin)>0 and stackedListOfHistos[0].GetBinContent(ibin)/otc.GetBinContent(ibin)<100:
                    nok=ibin-1
                    break
        data,blind=getDataGraphBlind(listOfHistosData,nok)
        setupHisto(otc,sampleOnTop.color,'',False)
        otc.SetBinContent(1,otc.GetBinContent(0)+otc.GetBinContent(1));
        otc.SetBinContent(otc.GetNbinsX(),otc.GetBinContent(otc.GetNbinsX()+1)+otc.GetBinContent(otc.GetNbinsX()));
        otc.SetBinError(1,ROOT.TMath.Sqrt(ROOT.TMath.Power(otc.GetBinError(0),2)+ROOT.TMath.Power(otc.GetBinError(1),2)));
        otc.SetBinError(otc.GetNbinsX(),ROOT.TMath.Sqrt(ROOT.TMath.Power(otc.GetBinError(otc.GetNbinsX()+1),2)+ROOT.TMath.Power(otc.GetBinError(otc.GetNbinsX()),2)));
        otc.SetLineWidth(2)
        if factor >= 0.:
          otc.Scale(factor)
        else:
          otc.Scale(integralfactor)
        otc.Draw('histosame')
        data.Draw('samePE1')
        blind.SetFillStyle(3665)
        #blind.SetFillStyle(1001)
        blind.SetLineColor(ROOT.kGray)
        blind.SetFillColor(ROOT.kGray)
        if blinded:
            blind.Draw('same2')
        objects.append(blind)
        
        
        listOfRatioErrorGraphs=[]
        graphcounter=0
        for errorgraph,thisFillStyle,ThisFillColor in errorgraphList:
	  ratioerrorgraph=ROOT.TGraphAsymmErrors(errorgraph.GetN())
	  #print ratioerrorgraph
	  #raw_input()
	  x, y = ROOT.Double(0), ROOT.Double(0)
	  for i in range(errorgraph.GetN()):
	      errorgraph.GetPoint(i,x,y)
	      ratioerrorgraph.SetPoint(i,x, 1.0)
	      relErrUp=0.0
	      relErrDown=0.0
	      if y>0.0:
		  relErrUp=errorgraph.GetErrorYhigh(i)/y
		  relErrDown=errorgraph.GetErrorYlow(i)/y
	      ratioerrorgraph.SetPointError(i, errorgraph.GetErrorXlow(i),errorgraph.GetErrorXhigh(i), relErrUp, relErrDown)

  
	  errorgraph.SetFillStyle(thisFillStyle)
	  errorgraph.SetLineColor(ThisFillColor)
	  errorgraph.SetFillColor(ThisFillColor)
	  ratioerrorgraph.SetFillStyle(thisFillStyle)
	  ratioerrorgraph.SetLineColor(ThisFillColor)
	  ratioerrorgraph.SetFillColor(ThisFillColor)
  #        ratioerrorgraph.SetFillStyle(1001)
  #        ratioerrorgraph.SetLineColor(ROOT.kBlack)
  #        ratioerrorgraph.SetFillColor(ROOT.kGreen)

	  #if graphcounter==0:
	    #errorgraph.Draw("2")
	  #else:
	  errorgraph.Draw("same2")  
	  graphcounter+=1

	  objects.append(errorgraph)
	  objects.append(ratioerrorgraph)
	  listOfRatioErrorGraphs.append(ratioerrorgraph)
	  #print objects
	  #raw_input()
          l1=getLegendL()
          l2=getLegendR()
          l1.AddEntry22(data,'data','P')
          if factor >= 0.: 
              l2.AddEntry22(otc,sampleOnTop.name+' x '+str(factor),'L')
          else:
              l2.AddEntry22(otc,sampleOnTop.name+(' x {:4.0f}').format(integralfactor),'L')
              i=0
              for h,sample in zip(stackedListOfHistos,samples):
                  i+=1
                  if i%2==1:
                      l1.AddEntry22(h,sample.name,'F')
                  if i%2==0:
                      l2.AddEntry22(h,sample.name,'F')

        canvases.append(canvas)
        l1.Draw('same')
        l2.Draw('same')
        objects.append(data)
        objects.append(l1)
        objects.append(l2)
        objects.append(otc)

        #draw the lumi text on the canvas
        CMS_lumi.lumi_13TeV = "12.9 fb^{-1}"
        CMS_lumi.writeExtraText = 1
        CMS_lumi.extraText = "Preliminary"
        CMS_lumi.lumi_sqrtS = "13 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

        CMS_lumi.cmsTextSize = 0.55
        CMS_lumi.cmsTextOffset = 0.49
        CMS_lumi.lumiTextSize = 0.43
        CMS_lumi.lumiTextOffset = 0.61
        
        CMS_lumi.relPosX = 0.15
        
        CMS_lumi.hOffset = 0.05
        
        iPeriod=4   # 13TeV
        iPos=0     # CMS inside frame
        
        CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)

        label = ROOT.TLatex(0.18, 0.89, labeltext);
        label.SetTextFont(42)
        label.SetTextSize(0.035)
        label.SetNDC()
        label.Draw()
        objects.append(label)


        ratiograph,ratiominimum,ratiomaximum=getRatioGraph(data,stackedListOfHistos[0])
        canvas.cd(2)
        line=listOfHistos[0].Clone()
        line.SetFillStyle(0)
        line.Divide(listOfHistos[0])
        
        emptyHisto=listOfHistos[0].Clone()
        print emptyHisto.GetName()
        emptyHisto.SetFillStyle(0)
            
        #line.GetYaxis().SetRangeUser(0.5,1.6)
        line.GetYaxis().SetRangeUser(ratiominimum-0.2,ratiomaximum+0.2)
        line.GetXaxis().SetRangeUser(listOfHistos[0].GetXaxis().GetXmin(),listOfHistos[0].GetXaxis().GetXmax())
        for i in range(line.GetNbinsX()+2):
            line.SetBinContent(i,1)
            line.SetBinError(i,0)
        #print listOfHistos[0].GetXaxis().GetXmin(),listOfHistos[0].GetXaxis().GetXmax(),listOfHistos[0].GetXaxis().GetBinLabel(1)
        #print line.GetXaxis().GetXmin(),line.GetXaxis().GetXmax(),line.GetXaxis().GetBinLabel(1)
        #raw_input()
        line.GetXaxis().SetLabelSize(line.GetXaxis().GetLabelSize()*2.4)
        line.GetYaxis().SetLabelSize(line.GetYaxis().GetLabelSize()*2.4)
        line.GetXaxis().SetTitleSize(line.GetXaxis().GetTitleSize()*3)
        #line.GetYaxis().SetTitleSize(line.GetYaxis().GetTitleSize()*2.4)
        line.GetYaxis().SetTitleSize(line.GetYaxis().GetTitleSize()*2.4)
        line.GetYaxis().CenterTitle(1);
        line.GetYaxis().SetTitle('data/MC');
        line.GetYaxis().SetNdivisions( 503 );
        line.GetYaxis().SetTitleOffset( 0.5 );
        line.GetXaxis().SetNdivisions( 510 );
        line.GetXaxis().SetTickLength( line.GetXaxis().GetTickLength() * 2.0 );
        line.GetYaxis().SetTickLength( line.GetYaxis().GetTickLength() * 1.65 );

        for icbl, cbl in enumerate(myCustomBinLabels):
	  line.GetXaxis().SetBinLabel(icbl+1,cbl)
        #line.GetXaxis().SetBinLabel(4,"bla")
        line.Draw('histo')
        objects.append(ratiograph)
        #print len(listOfRatioErrorGraphs)
        for ratioerrorgraph in listOfRatioErrorGraphs:
          ratioerrorgraph.Draw("same2")
#        objects.append(ratioerrorgraph)
        ratiograph.Draw('sameP')
        line.SetLineWidth(1)
        line.Draw('histosame')
        #emptyHisto.GetYaxis().SetTitle('data/MC');
        #print "title? ", emptyHisto.GetYaxis().GetTitle()
        #print "title? ", line.GetYaxis().GetTitle()
        line.Draw('axissame')
        #emptyHisto.Draw("axissame")
        #objects.append(emptyHisto)
        objects.append(line)
        #print labeltext
        #raw_input()


#    print len(canvases)
    printCanvases(canvases,name)
    writeObjects(canvases,name)
    writeObjects(objects,name)

def divideHistos(listOfHistoLists, numeratorPlot, denumeratorPlot, normalizefirst=False,rebin=1,option=''):
    dividedHistoList=[]
    print 'numerator ',numeratorPlot
    print 'denumerator ',denumeratorPlot
    print 'lol[numerator] ',listOfHistoLists[numeratorPlot]
    print 'lol[denumerator] ',listOfHistoLists[denumeratorPlot]
    #print len(listOfHistoLists[numeratorPlot])
    listofratios=[]
    if len(listOfHistoLists[numeratorPlot])==1:
        numerator=listOfHistoLists[numeratorPlot][0].Clone()
        denumerator=listOfHistoLists[denumeratorPlot][0].Clone()
        if (listOfHistoLists[numeratorPlot][0].Integral()>0) and (listOfHistoLists[denumeratorPlot][0].Integral()>0):
                listofratios.append((listOfHistoLists[numeratorPlot][0].Integral())/(listOfHistoLists[denumeratorPlot][0].Integral()))
        else :
                listofratios.append(0)
        numerator.Rebin(rebin)
        denumerator.Rebin(rebin)
        if normalizefirst: 
            print 'numerator before divide ',numerator, '     numerator Integral= ', numerator.Integral()
            print 'denumerator before divide ',denumerator, '      denumerator Integral= ',denumerator.Integral() 
            print 'Ratio of ', numerator,'  over  ', denumerator,'  =  ',(numerator.Integral())/(denumerator.Integral() )
            numerator.Scale(1./numerator.Integral())
            denumerator.Scale(1./denumerator.Integral())
        #x=numerator.Clone()
        #print 'numerator before divide ',numerator, '     numerator Integral= ', numerator.Integral()
        #print 'denumerator before divide ',denumerator, '      denumerator Integral= ',denumerator.Integral()
        numerator.Divide(numerator,denumerator,1.0,1.0,option)
        listOfHistoLists[numeratorPlot][0]=numerator
        #print 'numerator after divide temp ',numerator, '     numerator Integral= ', numerator.Integral()
        #print 'numerator after divide ', listOfHistoLists[numeratorPlot][0]   
        #print 'denumerator after divide ', listOfHistoLists[denumeratorPlot][0]
        
    if len(listOfHistoLists[numeratorPlot])>1:
        for i in range(len(listOfHistoLists[numeratorPlot])):
            numerator=listOfHistoLists[numeratorPlot][i].Clone()
            denumerator=listOfHistoLists[denumeratorPlot][i].Clone()
            if (listOfHistoLists[numeratorPlot][i].Integral()>0) and (listOfHistoLists[denumeratorPlot][i].Integral()>0):
                listofratios.append((listOfHistoLists[numeratorPlot][i].Integral())/(listOfHistoLists[denumeratorPlot][i].Integral()))
            else :
                listofratios.append(0)
            numerator.Rebin(rebin)
            denumerator.Rebin(rebin)
            if normalizefirst: #######check if integral>0
                print 'Ratio of ', numerator,'  over  ', denumerator,'  =  ',(numerator.Integral())/(denumerator.Integral() )
                numerator.Scale(1./numerator.Integral())
                denumerator.Scale(1./denumerator.Integral())
            #x=numerator.Clone()
            
            #print 'numerator before divide ',numerator, '     numerator Integral= ', numerator.Integral(), '    bing contents'
            #for ibin in range (numerator.GetNbinsX()+1):
                #print 'bincontent before', numerator.GetBinContent(ibin), denumerator.GetBinContent(ibin)
            #print 'denumerator before divide ',denumerator, '      denumerator Integral= ',denumerator.Integral()
            #numerator.Divide(numerator, denumerator,1.0,1.0,option)
            numerator.Divide(denumerator)
            #print 'numerator after divide temp1',numerator, '     numerator Integral= ', numerator.Integral()
            #print 'denumerator after divide temp1',denumerator, '     denumerator Integral= ', denumerator.Integral()
            #for ibin in range (numerator.GetNbinsX()+1):
                #print 'bincontent after', numerator.GetBinContent(ibin), denumerator.GetBinContent(ibin)
            listOfHistoLists[numeratorPlot][i]=numerator   
            #print 'numerator after divide temp2',numerator, '     numerator Integral= ', numerator.Integral()
            #print 'denumerator after divide temp2',denumerator, '     denumerator Integral= ', denumerator.Integral()
            #print 'x after divide ahhhh',x, '     x Integral= ', x.Integral()
            #print 'numerator after divide ', listOfHistoLists[numeratorPlot][i], '     numerator Integral= ', listOfHistoLists[numeratorPlot][i].Integral()
            #print 'denumerator after divide ', listOfHistoLists[denumeratorPlot][i], '      denumerator Integral= ',listOfHistoLists[denumeratorPlot][i].Integral()
        #print 'divide? ', listofHistoLists
        #self.append(x)
    #self.append(dividedHistoList)
    #print len(self)
    return listofratios





def multiplyHistos(listOfHistoLists, Factor1Plot, Factor2Plot, normalizefirst=False,rebin=1,option=''):
    multipliedHistoList=[]
    print 'First Factor ', Factor1Plot
    print 'Second Factor ',Factor2Plot
    print 'lol[First Factor] ',listOfHistoLists[Factor1Plot]
    print len(listOfHistoLists[Factor1Plot])
    
    if len(listOfHistoLists[Factor1Plot])==1:
        Factor1 = listOfHistoLists[Factor1Plot][0].Clone()
        Factor2 = listOfHistoLists[Factor2Plot][0].Clone()
        Factor1.Rebin(rebin)
        Factor2.Rebin(rebin)
        if normalizefirst: 
            print 'Factor1 before divide ',Factor1
            Factor1.Scale(1./Factor1.Integral())
            Factor2.Scale(1./Factor2.Integral())
        x=Factor1.Clone()
        Factor1.Multiply(Factor1,Factor2,1.0,1.0,option)
        listOfHistoLists[Factor1Plot][0]=Factor1   
        print 'First Factor after divide ', listOfHistoLists[Factor1Plot][0]   
        
    if len(listOfHistoLists[Factor1Plot])>1:
        for i in range(len(listOfHistoLists[Factor1Plot])):
            Factor1=listOfHistoLists[Factor1Plot][i].Clone()
            Factor2=listOfHistoLists[Factor2Plot][i].Clone()
            Factor1.Rebin(rebin)
            Factor2.Rebin(rebin)
            if normalizefirst: 
                print 'First Factor before divide ',Factor1
                Factor1.Scale(1./Factor1.Integral())
                Factor2.Scale(1./Factor2.Integral())
            x=Factor1.Clone()
            Factor1.Multiply(Factor1,Factor2,1.0,1.0,option)
            listOfHistoLists[Factor1Plot][i]=Factor1   
            print 'First Factor after divide ', listOfHistoLists[Factor1Plot][i]
        #print 'divide? ', listofHistoLists
        #self.append(x)
    #self.append(dividedHistoList)
    #print len(self)
    #return listofHistoLists



    
#def LOLSumw2(listOfHistoLists):
    #for listOfHisto in listOfHistoLists:
        #for h in listOfHisto:
            #h.Sumw2()
    
  
def writeHistoListwithXYErrors(listOfHistoListsToPlot, sampleListToPlot, name='define name', rebin=1, fitoption='pol2', labels=None, autoXrange=False):
    if labels==None:
        labels = len(listOfHistoListsToPlot)*['Singal-BKG-Shape-Ratio']
    canvases=[]
    ratio=False
    objects=[] 
    logscale=False
    ListofTgraphsforFile=[]
    #ListofTgraphNamsforFile=[]
    #ROOT.gStyle.SetOptFit()
    for listOfHistos, label in zip(listOfHistoListsToPlot, labels):                 
        for histo,sample in zip(listOfHistos, sampleListToPlot):
            yTitle='Ratio'
            histo.Rebin(rebin)
            error = ROOT.Double(0)
            nonemptybins=0
            for i in range(histo.GetNbinsX()+1):
                #print i
                #print histo.GetBinContent(i)
                if histo.GetBinContent(i)>0:
                    nonemptybins+=1
            #print histo.GetName(), ' Integral=', histo.IntegralAndError(0,histo.GetNbinsX(),error,""),'+-',error, '  Nbins=', histo.GetNbinsX(), '  nonemptybins=', nonemptybins, ' Int/nonemtybins=',  (histo.IntegralAndError(0,histo.GetNbinsX(),error,""))/float(nonemptybins),'+-',error/float(nonemptybins)
             
            data=ROOT.TGraphAsymmErrors(histo)
            fit=fitFunctionToHistogrammwitherrorband(histo,fitoption, autoXrange)   
            #fit=fitFunctionToHistogrammwitherrorband(histo,"[0]+([1]*log(x-[3])+[2]*log(x-[4])*log(x-[4]))")
            #fit=fitFunctionToHistogrammwitherrorband(histo,"[0]+([1]*log(x)+[2]*log(x)*log(x))*erf(x-[3]/[4])")
            canvas=getCanvas(data.GetName(),ratio)
        
            if logscale:
                canvas.SetLogy()
                canvas.SetLogx()
            fit[0].SetFillColor(ROOT.kRed)
            fit[0].SetLineColor(ROOT.kBlue)
            fit[0].SetName('Graph_'+histo.GetName())
            #fit[0].ConfidenceIntervals()
            ROOT.gStyle.SetOptFit(1111)
            data.GetYaxis().SetRangeUser(0,2)
            fit[0].GetYaxis().SetRangeUser(0,2)
            #data.GetYaxis().SetRangeUser(0,2)
            #data.SetOptFit(1111)
            #canvas.Update()
            fit[0].Draw('A3')
            #canvas.Update()

            fit[0].Draw('sameLXZ')
            #canvas.Update()
            data.Draw('sameP')
            #histo.GetFunction("fit").Draw("sameL")
            #canvas.Update()
            
            l=getLegend()
            l.AddEntryZprime(data,label ,'P') 
            #l.AddEntryZprime(data,'Singal-BKG-Shape-Ratio','P')
            l.AddEntryZprime(fit[0],"fit",'L')
            l.Draw('same')
            
            #canvas.Update()
            canvases.append(canvas)
            objects.append(data)
            objects.append(fit[0])
            objects.append(l)
            #objects.append(graph)
            ListofTgraphsforFile.append(fit[0])
            #ListofTgraphNamsforFile.append()
            print 'here its ok'
            
    printCanvases(canvases,name)
    writeObjects(canvases,name)
    writeObjects(ListofTgraphsforFile,name+'_Graphs')
    #writeTGraphstoextraFile(ListofTgraphsforFile,ListofTgraphNamsforFile,'SB_transferfunctions')

    
def fitFunctionToHistogrammwitherrorband(histo, fitoption="[0]+[1]*log(x)+[2]*log(x)*log(x)",autoXrange=False):
    xmax=histo.GetNbinsX()*histo.GetBinWidth(histo.GetNbinsX())
    xmin=0.0
    ROOT.gStyle.SetOptFit(1111)
    if autoXrange:
        for ibin in range(0,histo.GetNbinsX()):
            if histo.GetBinContent(ibin)==0 and histo.GetBinContent(ibin-1)!=0:
                xmax=histo.GetBinCenter(ibin-1)
            #print ibin,' of ',histo.GetNbinsX(),' binwidth: ',histo.GetBinWidth(ibin),' of ',xmax
        for ibin in range(histo.GetNbinsX(),0,-1):
            if histo.GetBinContent(ibin)==0 and histo.GetBinContent(ibin+1)!=0:
                xmin=histo.GetBinCenter(ibin+1)
            #print ibin,' of ',histo.GetNbinsX(),' xmin ',xmin
        
    print 'xmin=',xmin,'   xmax=',xmax
    fitfunction=ROOT.TF1("fit",fitoption,xmin,xmax)
    print 'here its ok aswell1'
    if(fitoption=="[0]+([1]*log(x-[3])+[2]*log(x-[3])*log(x-[3]))"):
        fitfunction.SetParameter(0,-1.0)
        fitfunction.SetParameter(1,1.0)
        fitfunction.SetParameter(2,0.0)
        fitfunction.SetParameter(3,600.0)
        
    if(fitoption=="[0]+([1]*log(x*x-[3])+[2]*log(x*x-[3])*log(x*x-[3]))"):
        fitfunction.SetParameter(0,-1.0)
        fitfunction.SetParameter(1,1.0)
        fitfunction.SetParameter(2,0.0)
        fitfunction.SetParameter(3,600.0)
        
    if(fitoption=="[0]+([1]*log([4]*x-[3])+[2]*log([4]*x-[3])*log([4]*x-[3]))"):
        fitfunction.SetParameter(0,-1.0)
        fitfunction.SetParameter(1,1.0)
        fitfunction.SetParameter(2,0.0)
        fitfunction.SetParameter(3,400.0)
        fitfunction.SetParameter(4,1.0)
        
    if(fitoption=="[0]+([1]*log(x-[4])+[2]*log(x-[4])*log(x-[4])+[3]*log(x-[4])*log(x-[4])*log(x-[4]))/x"):
        fitfunction.SetParameter(0,-1.0)
        fitfunction.SetParameter(1,1.0)
        fitfunction.SetParameter(2,0.0)
        fitfunction.SetParameter(3,1.0)
        fitfunction.SetParameter(4,400.0)
        
    if(fitoption=="[0]+([1]*log(x-[3])+[2]*log(x-[3])*log(x-[3]))/x"):
        fitfunction.SetParameter(0,-1.0)
        fitfunction.SetParameter(1,1.0)
        fitfunction.SetParameter(2,0.0)
        fitfunction.SetParameter(3,400.0)
        
    if(fitoption=="[0]+([1]*log(x-[3])+[2]*log(x-[3])*log(x-[3]))*x"):
        fitfunction.SetParameter(0,-1.0)
        fitfunction.SetParameter(1,1.0)
        fitfunction.SetParameter(2,0.0)
        fitfunction.SetParameter(3,400.0)        
        
    if(fitoption=="[0]+[1]*log(x-[3])+[2]*log(x-[3])*log(x-[3])+[4]*log(x-[3])*log(x-[3])*log(x-[3])"):
        fitfunction.SetParameter(0,-1.0)
        fitfunction.SetParameter(1,1.0)
        fitfunction.SetParameter(2,0.0)
        fitfunction.SetParameter(3,400.0)           
        fitfunction.SetParameter(4,0.0)           
        
    if(fitoption=="[0]+([1]*x*(1/(exp([2]*x)-1)))"):
        fitfunction.SetParameter(0,-1.0)
        fitfunction.SetParameter(1,1.0)
        fitfunction.SetParameter(2,0.0)
        #fitfunction.SetParameter(3,400.0)        
        #fitfunction.SetParameter(4,400.0)        
        #fitfunction.SetParameter(5,400.0)        
        
        
        
    if(fitoption=="pol2"):
        fitfunction.SetParameter(0,1.0)
        fitfunction.SetParameter(1,0.0)
        fitfunction.SetParameter(2,0.0)
    #fitfunction.SetParameter(4,400.0)
    
    #fitfunction.SetParameter(3,100.0)
    #fitfunction.SetParameter(4,1.0)


    fitgraphwitherrorband=ROOT.TGraphErrors(1000)
    for ibingraph in range(1000):
        #print(ibingraph*xmax/1000.0)
        fitgraphwitherrorband.SetPoint(ibingraph,xmin+(ibingraph+1)*(xmax-xmin)/1000.0,fitfunction.Eval(xmin+(ibingraph+1)*(xmax-xmin)/1000.0))
        fitgraphwitherrorband.SetPointError(ibingraph,0.5,0.5)    
    
    #res=histo.Fit(fitfunction,'S0M')
    res=histo.Fit(fitfunction,'S0M')
    fit=histo.GetFunction("fit")
    if int(res)>=0:
    #if not res.IsEmpty():
        print 'Successfully fitted to histogramm ', histo.GetName()
        #res.Dump()
        res.Print('V')
        print 'Fit propability:  ',res.Prob()
        print ' '
        print ' '
        print ' '

    
    
        cov=res.GetCovarianceMatrix()
        #x=array.array("d",[])

        #print 'n: ',ibingraph,'  x: ',xmin+(ibingraph+1)*(xmax-xmin)/1000.0,'  y: ',fitfunction.Eval(xmin+(ibingraph+1)*(xmax-xmin)/1000.0)
        ROOT.TVirtualFitter.GetFitter().GetConfidenceIntervals(fitgraphwitherrorband)
        #for l in fitgraphwitherrorband.GetX():
            #print l
        #print fitgraphwitherrorband.GetY()
        #print res.GetConfidenceIntervals(fitgraphwitherrorband,0.66)
        #dy=res.GetConfidenceIntervals(0.68)
        #ROOT.Fit.FitResult.GetConfidenceIntervals(fitgraphwitherrorband,0.66)
        #fitgraphwitherrorband.GetConfidenceIntervals(res,0.66)
        #fitgraphwitherrorband=makefunctionerrorbands(fit,cov,1000,0.0,xmax*1.1)
    else:
        print 'No fit for ', histo.GetName(),'. Check if histogramm is filled'    
    
    return [fitgraphwitherrorband,res]

#def makefunctionerrorbands(fitfunction, covariancematrix, npoints=1000,xmin=0.0,xmax=6000.0):
    #xbin=(xmax-xmin)/float(npoints)
    #y=array.array("d",[])
    #deltax=array.array("d",[])
    #deltay=array.array("d",[])
    #mu=array.array("d",[])
    #fitfunctiontemp=fitfunction
    #for i in range(fitfunction.GetNumberFreeParameters()):
        #mu=append(fitfunction.GetParameter(i))
    
    #for i in range(npoints):
        ##print i
        ##print orderofpolynom
        #xi=xmin+i*xbin
        #x.append(xi)
        #yi=fitfunction.Eval(xi)
        #y.append(yi)
        #deltax.append(xbin/2.0)
        #deltay2=0.0
        
        #k=array.array("d",[])
        #z=array.array("d",[])
        #dyi=array.array("d",[])
        
        #for i in range(1000):
            #for j in range(fitfunction.GetNumberFreeParameters()):
                #z.append(random.normalvariate(0,fitfunction.GetParError(j))
                
                #fitfunctiontemp.SetParameter(j,mu[j]+A*z)
                
            #dyi.append(fitfunctiontemp.Eval(xi))
        
        #deltay.append(variance(dyi,yi))
                     
        ##for j in range(0,(orderofpolynom+1)):
            ##for k in range(0,(orderofpolynom+1)):
                ##deltay2=deltay2+pow(xi,j)*pow(xi,k)*covariancematrix(j,k)
        ##deltay.append(math.sqrt(deltay2))
        
    #graph=ROOT.TGraphAsymmErrors(int(npoints),x,y,deltax,deltax,deltay,deltay)
    #return graph    

#def variance(my_list, average):
    #variance = 0
    #for i in my_list:
        #variance += (average - my_list[i]) ** 2
    #return variance / len(my_list)

#def writeTGraphstoextraFile(ListofTgraphs,ListofTgraphNames,filename='TGraphs',)
#    print "writing Graphs into file"
#    f=ROOT.TFile(filename+'.root','recreate')
#    t=ROOT.TTree('MVATree','MVATree')
#    zipi=zip(ListofTgraphs,ListofTgraphNames)
#    for graph,graphname in zipi:
#        t.Branch(graphnames,graph)
#        t.Fill()
#        
#    f.Write()
#    f.Close()

def DrawErrorBand(graph):
    isErrorBand = (graph.GetErrorYhigh(0)!=-1) and (graph.GetErrorYlow(0) != -1)
    npoints     = graph.GetN()
    
    if not isErrorBand:
        graph.Draw("l same")
        return
 
    # Declare individual TGraph objects used in drawing error band
    central, min, max = ROOT.TGraph(), ROOT.TGraph(), ROOT.TGraph()
    shapes = []
    for i in range((npoints-1)*4):
        shapes.append(ROOT.TGraph())
 
    # Set ownership of TGraph objects
    ROOT.SetOwnership(central, False)
    ROOT.SetOwnership(    min, False)
    ROOT.SetOwnership(    max, False)
    for shape in shapes:
        ROOT.SetOwnership(shape, False)
 
    # Get data points from TGraphAsymmErrors
    x, y, ymin, ymax = [], [], [], []
    for i in range(npoints):
        tmpX, tmpY = ROOT.Double(0), ROOT.Double(0)
        graph.GetPoint(i, tmpX, tmpY)
        x.append(tmpX)
        y.append(tmpY)
        ymin.append(tmpY - graph.GetErrorYlow(i))
        ymax.append(tmpY + graph.GetErrorYhigh(i))
 
    # Fill central, min and max graphs
    for i in range(npoints):
        central.SetPoint(i, x[i], y[i])
    min.SetPoint(i, x[i], ymin[i])
    max.SetPoint(i, x[i], ymax[i])
 
    # Fill shapes which will be shaded to create the error band
    for i in range(npoints-1):
        for version in range(4):
            shapes[i+(npoints-1)*version].SetPoint((version+0)%4, x[i],   ymax[i])
            shapes[i+(npoints-1)*version].SetPoint((version+1)%4, x[i+1], ymax[i+1])
            shapes[i+(npoints-1)*version].SetPoint((version+2)%4, x[i+1], ymin[i+1])
            shapes[i+(npoints-1)*version].SetPoint((version+3)%4, x[i],   ymin[i])
 
    # Set attributes to those of input graph
    central.SetLineColor(graph.GetLineColor())
    central.SetLineStyle(graph.GetLineStyle())
    central.SetLineWidth(graph.GetLineWidth())
    min.SetLineColor(graph.GetLineColor())
    min.SetLineStyle(graph.GetLineStyle())
    max.SetLineColor(graph.GetLineColor())
    max.SetLineStyle(graph.GetLineStyle())
    for shape in shapes:
        shape.SetFillColor(graph.GetFillColor())
        shape.SetFillStyle(graph.GetFillStyle())
 
    # Draw
    for shape in shapes:
        shape.Draw("f same")
    min.Draw("l same")
    max.Draw("l same")
    central.Draw("l same")
    ROOT.gPad.RedrawAxis()
    
def SchmonCorrelation(listOfHistoListsX,listOfHistoListsY,name='define_name', rebin=1):
    canvases=[]
    ratio=False
    objects=[]
    #print 'listOfHistoListsX ', listOfHistoListsX
    #print 'listOfHistoListsY ', listOfHistoListsY
    #for listOfHistosX in listOfHistoListsX:
        #print 'listOfHistosX ',listOfHistosX
        #for listOfHistosY in listOfHistoListsY:
            #print 'listOfHistosY ', listOfHistosY
            #for histoX in listOfHistosX:
                #for histoY in listOfHistosY:
    for histoX in listOfHistoListsX:
        for histoY in listOfHistoListsY:
                    canvas=getCanvas(histoX.GetName()+'_vs_'+histoY.GetName(),ratio)
                    canvas.Divide(2,1)
                    
                    hX=histoX.Clone()
                    hY=histoY.Clone()
                    hX.Rebin(rebin)
                    hY.Rebin(rebin)
                    
                    hX.Scale(1./hX.Integral())
                    hY.Scale(1./hY.Integral())

                    #meanY1=0
                    #meanY2=0
                    #trace=0
                    #x,y,ex,ey=[],[],[],[]
                    x=array.array("d",[])
                    y=array.array("d",[])
                    ex=array.array("d",[])
                    ey=array.array("d",[])
                    
                    corr2D=ROOT.TH2F("SchmonCorrelation","",20,0.0,0.05,20,0.0,0.05)
                    #for i in range(hX.GetNbinsX()):
                        #print i, ' in ', hX.GetNbinsX()
                        #meanY1=meanY1+hX.GetBinContent(i)
                    #meanY1=meanY1/float(hX.GetNbinsX())
                    #print 'meanY1 ',meanY1
                    #for j in range(hY.GetNbinsX()):
                        #meanY2=meanY2+hY.GetBinContent(j)
                    #meanY2=meanY2/float(hY.GetNbinsX())
                    #print 'meanY2 ',meanY2
                    for i in range(hX.GetNbinsX()):
                        #for j in range(hY.GetNbinsX()):
                            #if hX.GetBinCenter(i)>0 and hX.GetBinCenter(j)>0 and hX.GetBinError(i)>0 and hY.GetBinError(j)>0:
                               #corr2D.Fill(hX.GetBinCenter(i),hX.GetBinCenter(j),(hX.GetBinContent(i)-meanY1)*(hY.GetBinContent(j)-meanY2)/(hX.GetBinError(i)*hY.GetBinError(j)))
                               #if i is j:
                                   #trace=trace+(hX.GetBinContent(i)-meanY1)*(hY.GetBinContent(j)-meanY2)
                    #print 'trace ', trace
                        if hX.GetBinContent(i) and hY.GetBinContent(i):
                            corr2D.Fill(hX.GetBinContent(i),hY.GetBinContent(i),1.0/(hX.GetBinError(i)*hY.GetBinError(i)))
                            x.append(hX.GetBinContent(i))
                            y.append(hY.GetBinContent(i))
                            ex.append(hX.GetBinError(i))
                            ey.append(hY.GetBinError(i))
                    canvas.cd(1)      
                    corr2Dgraph=ROOT.TGraphErrors(len(x),x,y,ex,ey)
                    corr2Dgraph.GetXaxis().SetTitle(hX.GetName())
                    corr2Dgraph.GetYaxis().SetTitle(hY.GetName())
                    corr2Dgraph.Draw('ap')
                    canvas.cd(2)
                    corr2D.GetXaxis().SetTitle(hX.GetName())
                    corr2D.GetYaxis().SetTitle(hY.GetName())
                    corr2D.SetStats(False)
                    corr2D.Draw('colz')
                    print 'histoX ',histoX
                    print 'histoY ',histoY
                    print 'Correlation Factor TGraph: ',corr2Dgraph.GetCorrelationFactor()
                    print 'Covariance Factor TGraph: ',corr2Dgraph.GetCovariance()
                    print 'Correlation Factor TH2: ',corr2D.GetCorrelationFactor()
                    print 'Covariance Factor TH2: ',corr2D.GetCovariance()

                    canvases.append(canvas)
                    objects.append(corr2D)
                    objects.append(corr2Dgraph)
                    
    printCanvases(canvases,name)
    writeObjects(canvases,name)    



def GetListOfCorrelationLists(listOfHistoLists, DoSpear):
    ListOfCorrelationLists = []
    ListOfSpearCorrelationLists = []
    ListOfPValueLists = []
    ListOfPlotNameLists=[]
    ListOfNDFs=[]
    for HistoList in listOfHistoLists:
        CorrelationList = []
        SpearCorrelationList = []
        PlotNameList=[]
        PValueList =[]
        NDFs=[]
        # print "iterate over LOL"
        for Histo in HistoList:
            # print "iterate over L"
            a = Histo.GetCorrelationFactor()
            b = Histo.GetName()
            if DoSpear:
                c=  GetSpearCorrelationFactor(Histo)
            else: c="Spear Correlation Coefficient not activated."
            d, df= GetPValueHisto(Histo)
            CorrelationList.append(a)
            PlotNameList.append(b)
            SpearCorrelationList.append(c)
            PValueList.append(d)
            NDFs.append(df)
            # print "Correlation of Histogram: " , a
        ListOfCorrelationLists.append(CorrelationList)
        ListOfPlotNameLists.append(PlotNameList)
        ListOfSpearCorrelationLists.append(SpearCorrelationList)
        ListOfPValueLists.append(PValueList)
        ListOfNDFs.append(NDFs)
    return ListOfCorrelationLists, ListOfPlotNameLists, ListOfSpearCorrelationLists, ListOfPValueLists, ListOfNDFs


#Write CorrelationFactors of ListOfHistoLists to Textfile
def writeCorrLOL(listOfHistoLists, FileName="Correlationfactors.txt", PlotNames="", SampleNames = None, DoSpear=False ):
    with open(FileName, "w") as corrFile:
        CorrLOL, PlotNamesLOL, SpearLOL, PValueLOL, NDFLOL = GetListOfCorrelationLists(listOfHistoLists, DoSpear)
        print PValueLOL
        # print CorrLOL, PlotNamesLOL
        if PlotNames != "":
            if SampleNames == None:
                SampleNames = len(listOfHistoLists[0])*[""]
                
            for CorrL, PlotName, SpearL, PValueL, NDFs in zip(CorrLOL, PlotNames, SpearLOL, PValueLOL, NDFLOL):
                corrFile.write("----------------------------\n")
                corrFile.write(PlotName+"\n")
                for Corr, SampleName, Spear, PValue, NDF in zip(CorrL, SampleNames, SpearL, PValueL, NDFs):
                    corrFile.write(str(Corr)+"\t"+SampleName + "\tPearson \n")
                    corrFile.write(str(PValue)+"\t"+SampleName + "\tPValue \n")
                    corrFile.write(str(NDF) +"\t"+ SampleName+ "\t Number of Degrees of Freedom\n")
                    if DoSpear:
                        corrFile.write(str(Spear) + "\t"+SampleName + "\tSpearman \n")

                    
        else:
            for CorrL,NameL, SpearL, PValueL in zip( CorrLOL, PlotNamesLOL, SpearLOL, PValueLOL ):
                corrFile.write("----------------------------------------\n")
                for Corr, Name, Spear, PValue in zip(CorrL, NameL, SpearL, PValueL):
                    corrFile.write(str(Corr)+"\t\t"+Name + "\tPearson \n")
                    corrFile.write(str(PValue)+"\t\t"+Name + "\tPearson \n")
                    if DoSpear:
                        corrFile.write(str(Spear)+"\t\t"+Name + "\tSpearman \n")









#Functions to get the Spearman CorrelationFactor


#Get Temporary List of X an Y that can be ranked afterwards
def GetXYBins(Histo2D):
    X=[]
    Y=[]
    nx = Histo2D.GetNbinsX()
    ny = Histo2D.GetNbinsY()
    print "Entries of the Histogram", Histo2D.GetEntries()

    for x in range(nx+2):
        x_tmp = 0
        for y in range(ny+2):
            x_tmp += int(Histo2D.GetBinContent(x,y))
        # print "x_tmp", x_tmp
        for i in range(x_tmp):
            X.append(x)

            
    #Sort y, so that x-Entry at position i belongs to y-Entry at position i
    Y = []
    x_tmp = -1
    for x in X:
        if x == x_tmp:
            continue
        x_tmp = x
        for y in range(ny+2):
            
            Y += int(Histo2D.GetBinContent(x,y) ) * [y]
        
    
    # print "unranked", X, Y    
    return X,Y



#return to old sortation (as X was sorted before)
def unsorted(X_modified_sorted, X_):
    X = X_
    X_modified_unsorted= len(X)*['not changed yet']
    
    for i in range( len(X) ):
        index_tmp = X.index(  min( X ) )
        X_modified_unsorted[index_tmp] = X_modified_sorted[i]
        X[index_tmp] = max(X)+1
    return X_modified_unsorted
    


#Rank a given array
def RankArray(X_):
    X=X_
    X_sorted = sorted(X)
    X_ranked = []
    last = X_sorted[0]
    X_Bool_MoreThanLast = []
    
    for element in X_sorted[1:]:
        if element > last:
            X_Bool_MoreThanLast.append(True)
        else:
            X_Bool_MoreThanLast.append(False)
        last = element

    size = 1
    i = 1
    for MoreThanLast in X_Bool_MoreThanLast:
        if MoreThanLast:
            X_ranked += size*[i - (size - 1)/2. ]
            size = 1
        else:
            size += 1
        i += 1
        
    X_ranked += size*[ i- (size-1)/ 2. ]
    X_ranked = unsorted(X_ranked, X) #return to old sortation
    return X_ranked




def GetSpearCorrelationFactor(Histo_, Smaller=True):

    Histo = Histo_.Clone()
    if Smaller:
        Histo.Scale(200/Histo.Integral())
    
    X_tmp, Y_tmp = GetXYBins(Histo)
    X_ranked=RankArray(X_tmp)
    Y_ranked=RankArray(Y_tmp)

    
    histo_rank = ROOT.TH2F("histo_rank", "Histogram of ranked variables", 15 , 0.95*min(X_ranked), 1.05*max(X_ranked), 15 , 0.95*min(Y_ranked), 1.05*max(Y_ranked) )
    for i in range(len( X_ranked ) ):
        histo_rank.Fill( X_ranked[i], Y_ranked[i] )
        
    mycanv = ROOT.TCanvas("mycanv", "mycanv", 800, 600)
    histo_rank.Draw("colz")
    mycanv.SaveAs("ABCD/"+Histo.GetName()+"_ranked.png")
    SpearCorr = histo_rank.GetCorrelationFactor()
    return SpearCorr



#def closuretest(listOfHistos, listOfHistosPrediction, listOfHistosPrediction_systup, listOfHistosPrediction_systdown,samples, label,name,normalize=True,stack=False,logscale=False,options='histo',statTest=False, sepaTest=False,ratio=False):
    ##if DoProfile and not isinstance(listOfHistoLists[0][0], ROOT.TH2):
      ##print "need 2D plots for Profile Histograms"
      ##DoProfile=False
    #listofallstattests=[]
    #if isinstance(label, basestring):
        #labeltexts=len(listOfHistoLists)*[label]
##        print "bla"
    #else:
        #labeltexts=label
    #canvases=[]
    #objects=[]   
    #i=0
    #print labeltexts
        #listofthisstattests=[listOfHistos[0].GetTitle()]
        #i+=1
        #for histo, histoPrediction,histoPrediction_systup,histoPrediction_systdown,sample in zip(listOfHistos,listOfHistosPrediction,listOfHistosPrediction_systup,listOfHistosPrediction_systdown,samples):
            #print labeltext
            #yTitle='Events'
            #if normalize:
                #yTitle='normalized'
            #setupHisto(histo,sample.color,yTitle,stack)        
        #stattests2D=None
        #c=drawHistosOnCanvas([histoPrediction]+[histoPrediction_systup]+[histoPrediction_systdown]+[histo],normalize,stack,logscale,options,ratio,DoProfile)

        #if not isinstance(c, list):
            #c.SetName('c_'+listOfHistos[0].GetName())
            #l=getLegend2()
            #for h,sample in zip(listOfHistos,samples):
                #loption='L'
                #if stack:
                    #loption='F'            
                #l.AddEntry4545(h,sample.name,loption)
            #canvases.append(c)
            #l.Draw('same')
            #objects.append(l)
        #elif options == "colz":
            #for i in range(len(listOfHistos)):
                #c[i].SetName('c_'+listOfHistos[i].GetName()) #wrong! What name should be set?

            #if DoProfile:
                #c[-2].SetName('c_'+c[-2].GetName())
                #lx = getLegend2()
                #for px,  sample in zip(profilesx,  samples):
                    #lx.AddEntry4545( px.GetName() , sample.name, "L" )
                #lx.Draw("same")
                #objects.append(lx)
                
                #c[-1].SetName('c_'+c[-1].GetName())
                #ly = getLegend2()
                #for  py, sample in zip( profilesy, samples):
                    #ly.AddEntry4545( py.GetName() , sample.name, "L" )
                #ly.Draw("same")
                #objects.append(ly)
            #canvases+=c
        #else:
            #canvases+=c
        
        #if statTest:
            #if not isinstance(listOfHistos[0],ROOT.TH2):
                #tests=getStatTestsList(listOfHistos[0],listOfHistos[1:],"UW")
                #tests.Draw()
                #listofthisstattests.append(tests.GetTitle())
                #objects.append(tests)
        #if sepaTest:
            #stests=getSepaTests(listOfHistos[0],listOfHistos[1])
            #stests.Draw()
            #objects.append(stests)
        #if stattests2D!=None:
            ## stattests2D.Draw()
            #objects.append(stattests2D)
            #listofthisstattests.append(stattests2D.GetTitle())
        ## cms = ROOT.TLatex(0.2, 0.96, 'CMS private work'  );
        ## cms.SetTextFont(42)
        ## cms.SetTextSize(0.05)
        ## cms.SetNDC()
        ## cms.Draw()
        ## print cms
        ## objects.append(cms)

        #if not isinstance(c, list):
            #cms = ROOT.TLatex(0.2, 0.96, 'CMS preliminary,  37.8 fb^{-1},  #sqrt{s} = 13 TeV'  );
            #cms.SetTextFont(42)
            #cms.SetTextSize(0.05)
            #cms.SetNDC()
            #cms.Draw()
            #objects.append(cms)

            #label = ROOT.TLatex(0.2, 0.9, labeltext);
            #label.SetTextFont(42)
            #label.SetTextSize(0.04)
            #label.SetNDC()
            #label.Draw()
            #objects.append(label)
            #listofallstattests.append(listofthisstattests)
        ## else:
        ##     for can, sam in zip(c,samples):
        ##         labeltext = sam.name
        ##         label = ROOT.TLatex(0.2, 0.96, labeltext);
        ##         label.SetTextFont(42)
        ##         label.SetTextSize(0.04)
        ##         label.SetNDC()
        ##         label.Draw()
        ##         objects.append(label)
        ##     listofallstattests.append(listofthisstattests)

        
    #printCanvases(canvases,name)
    #writeObjects(canvases,name)
    #stattestoutfile=open("stattests_"+name+".txt","w")
    #for stst in listofallstattests:
      #stattestoutfile.write(' '.join(stst)+'\n')
    #stattestoutfile.close()  











#Is Correlation smaller than rho 0 -- probability Hypothesis is _what_ ?
#r CorrelationCoefficient, p, probability hypothesis is true, rho0 - hyothesis
def GetPValue(r, df, rho0=0):
    #Get t Wert
    T =abs( (math.atanh(r) - math.atanh(rho0) - r/df )/(1/math.sqrt(df)) )
    #Get Propability, rho0 is true
    return 2*(1 - ROOT.TMath.StudentI(T , df) )

def GetPValueHisto(Histo, rho0 = 0):
    r = Histo.GetCorrelationFactor()
    df = Histo.GetEntries()
    return GetPValue(r, df , rho0), df

def addLOLtoLOL(ListOfHistoLists1,ListOfHistoLists2, c1=1.0, c2=1.0):
    #print ListOfHistoLists1
    #print ListOfHistoLists2
    for HistoList1, HistoList2 in zip(ListOfHistoLists1,ListOfHistoLists2):
        for Histo1 in HistoList1:
            for  Histo2 in HistoList2:
                #print Histo1, ' zip ', Histo2
                Histo1.Add(Histo2,c2)
      
def addLLLtoLLL(lll1,lll2, c1=1.0, c2=1.0):
    #print ListOfHistoLists1
    #print ListOfHistoLists2
    for HistoList1, HistoList2 in zip(lll1,lll2):
        for Histosystlist1 in HistoList1:
            for  Histosystlist2 in HistoList2:
                #print Histo1, ' zip ', Histo2
                for Histo1, Histo2 in zip(Histosystlist1,Histosystlist2):
                    #print Histo1, ' zip ', Histo2
                    Histo1.Add(Histo2,c2)
                      
def signal_sideband_integralratio(signalhisto,sidebandhisto):
    print signalhisto
    print sidebandhisto
    ratio=(signalhisto.Integral())/(sidebandhisto.Integral())
    print 'Ratio of ', signalhisto.GetName(), ' over ', sidebandhisto.GetName(), '=  ' , ratio
    return ratio


#def signal_sideband_integralratio(listOfHistoLists1,listOfHistoLists2):
    #for listOfHistos,listOfHistosOnTop in zip(listOfHistoLists1,listOfHistoLists2):
        #for 
        
def multiplyListofHistoswithfactors(listofHistos,factorlist):
    if (len(listofHistos)!=len(factorlist)):
        print 'len(listofHistos)!=len(factorlist)'
    if (len(listofHistos)==len(factorlist)):    
        for histo, factor in zip(listofHistos,factorlist):
            histo.Scale(factor)
            print 'multiplied ',histo, ' with ', factor
            
  
  
  
  
  
  
  
def normalizeBKGtoData(listofHistoBackground,listofHistoBackgroundincludingsysts ,HistoData):
    #print listofHistoBackground
    #print HistoData
    IntegralBKG=0
    ratio=1
    for histoBKG in listofHistoBackground:
        IntegralBKG+=histoBKG.Integral()
    ratio=HistoData.Integral()/IntegralBKG
    #print 'ratio ',ratio
    for histoBKGsystlist in listofHistoBackgroundincludingsysts:
        for histoBKGsyst in histoBKGsystlist:
            #print histoBKGsyst,'  bevor ratio applied', histoBKGsyst.Integral()
            histoBKGsyst.Scale(ratio)
            #print  histoBKGsyst,'  after ratio applied', histoBKGsyst.Integral()
    
def subtract_histos(histo1,histo2):
    histo1.Add(histo2,-1.0)


def subtract_llls(lll1,lll2):
    for ll1,ll2 in zip(lll1,lll2):
        for l1, l2 in zip(ll1,ll2):
            for histo1, histo2 in zip(l1,l2):
                histo1.Add(histo2,-1.0)


    
    
def add_histos(histo1,histo2):
    histo1.Add(histo2,1)
    


def ABBackgroundEstimationCalculationAndPlotsWithSystematics(loldata,llldata,lolBackground,lllBackgroundWithweightsys,lllBackgroundNoweightsys,lolSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames, SignalSampleNames, plotnames,weightsystnames,DatasampleNick,SCNick,SignalsampleNick,SBSSF_nick,PlotNameSignal,PlotNameSideband,QCDSample, name, useGeneratorDiff=False):

    loldataT=transposeLOL(loldata)
    lolBackgroundT=transposeLOL(lolBackground)
    lolSignalT=transposeLOL(lolSignal)

    loldatacopy=copy.deepcopy(loldata)
    llldatacopy=copy.deepcopy(llldata)
    lolBackgroundcopy=copy.deepcopy(lolBackground)
    lllBackgroundWithweightsyscopy=copy.deepcopy(lllBackgroundWithweightsys)

    subtract_histos(llldatacopy[plotnames.index(PlotNameSideband)][DataSampleNames.index(DatasampleNick)][weightsystnames.index(SBSSF_nick+'_nominal')],lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)][BackgroundSampleNames.index('ttbar')][weightsystnames.index(SBSSF_nick+'_nominal')])
    subtract_histos(loldatacopy[plotnames.index(PlotNameSignal)][DataSampleNames.index(DatasampleNick)],lolBackgroundcopy[plotnames.index(PlotNameSignal)][BackgroundSampleNames.index('ttbar')])   
    
    normalizeBKGtoData([llldatacopy[plotnames.index(PlotNameSideband)][DataSampleNames.index(DatasampleNick)][weightsystnames.index(SBSSF_nick+'_nominal')]],transposeLOL(lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)]),loldatacopy[plotnames.index(PlotNameSignal)][DataSampleNames.index(DatasampleNick)])
    
    #print lolBackgroundcopy[plotnames.index(PlotNameSignal)][BackgroundSampleNames.index('ttbar')].Integral(), ' of ', lolBackgroundcopy[plotnames.index(PlotNameSignal)][BackgroundSampleNames.index('ttbar')]
    
    #print loldatacopy[plotnames.index(PlotNameSignal)][DataSampleNames.index(DatasampleNick)].Integral(), ' of copy ', loldatacopy[plotnames.index(PlotNameSignal)][DataSampleNames.index(DatasampleNick)]
    #print loldata[plotnames.index(PlotNameSignal)][DataSampleNames.index(DatasampleNick)].Integral(), ' of originial ', loldata[plotnames.index(PlotNameSignal)][DataSampleNames.index(DatasampleNick)]

  
    print lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)][BackgroundSampleNames.index(QCDSample)][weightsystnames.index(SBSSF_nick+'_nominal')].Integral()
    
    #QCDlist=[transposeLOL(transposeLOL(lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)])[weightsystnames.index(SBSSF_nick+'_nominal'):weightsystnames.index(SBSSF_nick+'_systdown')+1])[BackgroundSampleNames.index(QCDSample)]+transposeLOL(transposeLOL(lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)])[weightsystnames.index(SBSSF_nick+'GeneratorDiff_systup'):weightsystnames.index(SBSSF_nick+'GeneratorDiff_systdown')+1])[BackgroundSampleNames.index(QCDSample)]]
    
    #ttbarlist=[transposeLOL(transposeLOL(lllBackgroundNoweightsys[plotnames.index(PlotNameSignal)])[weightsystnames.index('_no'+'_nominal'):weightsystnames.index('_no'+'_systdown')+1])[BackgroundSampleNames.index('ttbar')]+transposeLOL(transposeLOL(lllBackgroundNoweightsys[plotnames.index(PlotNameSignal)])[weightsystnames.index('_no'+'_systup'):weightsystnames.index('_no'+'_systdown')+1])[BackgroundSampleNames.index('ttbar')]]
    
    #SClist=[transposeLOL(transposeLOL(lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)])[weightsystnames.index(SBSSF_nick+'_nominal'):weightsystnames.index(SBSSF_nick+'_systdown')+1])[BackgroundSampleNames.index(SCNick)]+transposeLOL(transposeLOL(lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)])[weightsystnames.index(SBSSF_nick+'GeneratorDiff_systup'):weightsystnames.index(SBSSF_nick+'GeneratorDiff_systdown')+1])[BackgroundSampleNames.index(SCNick)]]


    if(useGeneratorDiff):
        
        QCDlist=[transposeLOL(transposeLOL(lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)])[weightsystnames.index(SBSSF_nick+'_nominal'):weightsystnames.index(SBSSF_nick+'_systdown')+1])[BackgroundSampleNames.index(QCDSample)]+transposeLOL(transposeLOL(lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)])[weightsystnames.index(SBSSF_nick+'GeneratorDiff_systup'):weightsystnames.index(SBSSF_nick+'GeneratorDiff_systdown')+1])[BackgroundSampleNames.index(QCDSample)]]
    
        ttbarlist=[transposeLOL(transposeLOL(lllBackgroundNoweightsys[plotnames.index(PlotNameSignal)])[weightsystnames.index('_no'+'_nominal'):weightsystnames.index('_no'+'_systdown')+1])[BackgroundSampleNames.index('ttbar')]+transposeLOL(transposeLOL(lllBackgroundNoweightsys[plotnames.index(PlotNameSignal)])[weightsystnames.index('_no'+'_systup'):weightsystnames.index('_no'+'_systdown')+1])[BackgroundSampleNames.index('ttbar')]]
    
        SClist=[transposeLOL(transposeLOL(lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)])[weightsystnames.index(SBSSF_nick+'_nominal'):weightsystnames.index(SBSSF_nick+'_systdown')+1])[BackgroundSampleNames.index(SCNick)]+transposeLOL(transposeLOL(lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)])[weightsystnames.index(SBSSF_nick+'GeneratorDiff_systup'):weightsystnames.index(SBSSF_nick+'GeneratorDiff_systdown')+1])[BackgroundSampleNames.index(SCNick)]]
    
        plotDataMCanWsyst([transposeLOL([loldataT[DataSampleNames.index(DatasampleNick)]])[plotnames.index(PlotNameSignal)]],transposeLOL([[lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)][BackgroundSampleNames.index(SCNick)][weightsystnames.index(SBSSF_nick+'_nominal')]]]+[[lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)][BackgroundSampleNames.index(QCDSample)][weightsystnames.index(SBSSF_nick+'_nominal')]]]+[transposeLOL([lolBackgroundT[BackgroundSampleNames.index("ttbar")]])[plotnames.index(PlotNameSignal)]]),[BackgroundSamples[BackgroundSampleNames.index(SCNick)]]+[BackgroundSamples[BackgroundSampleNames.index(QCDSample)]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]],transposeLOL([lolSignalT[SignalSampleNames.index(SignalsampleNick)]])[plotnames.index(PlotNameSignal)],SignalSamples[SignalSampleNames.index(SignalsampleNick)],1,name+DatasampleNick+QCDSample,[[[SClist+QCDlist+ttbarlist],3354,ROOT.kBlack,True]],False,SBSSF_nick+'+GeneratorDiff',True,False, False, True)
        print 'used generator differences'
        
    else:
        
        QCDlist=[transposeLOL(transposeLOL(lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)])[weightsystnames.index(SBSSF_nick+'_nominal'):weightsystnames.index(SBSSF_nick+'_systdown')+1])[BackgroundSampleNames.index(QCDSample)]]
    
        ttbarlist=[transposeLOL(transposeLOL(lllBackgroundNoweightsys[plotnames.index(PlotNameSignal)])[weightsystnames.index('_no'+'_nominal'):weightsystnames.index('_no'+'_systdown')+1])[BackgroundSampleNames.index('ttbar')]]
    
        SClist=[transposeLOL(transposeLOL(lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)])[weightsystnames.index(SBSSF_nick+'_nominal'):weightsystnames.index(SBSSF_nick+'_systdown')+1])[BackgroundSampleNames.index(SCNick)]]  
        
        plotDataMCanWsyst([transposeLOL([loldataT[DataSampleNames.index(DatasampleNick)]])[plotnames.index(PlotNameSignal)]],transposeLOL([[lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)][BackgroundSampleNames.index(SCNick)][weightsystnames.index(SBSSF_nick+'_nominal')]]]+[[lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)][BackgroundSampleNames.index(QCDSample)][weightsystnames.index(SBSSF_nick+'_nominal')]]]+[transposeLOL([lolBackgroundT[BackgroundSampleNames.index("ttbar")]])[plotnames.index(PlotNameSignal)]]),[BackgroundSamples[BackgroundSampleNames.index(SCNick)]]+[BackgroundSamples[BackgroundSampleNames.index(QCDSample)]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]],transposeLOL([lolSignalT[SignalSampleNames.index(SignalsampleNick)]])[plotnames.index(PlotNameSignal)],SignalSamples[SignalSampleNames.index(SignalsampleNick)],1,name+DatasampleNick+QCDSample,[[[SClist+QCDlist+ttbarlist],3354,ROOT.kBlack,True]],False,SBSSF_nick,True,False, False, True)
        
    print loldataT[0][0].Integral()
    print llldatacopy[0][0][0].Integral()

def ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(loldata,llldata,lolBackground,lllBackgroundWithweightsys,lllBackgroundNoweightsys,lolSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames, SignalSampleNames, plotnames,weightsystnames,DatasampleNick,SCNick,SignalsampleNick,SBSSF_nick,PlotNameSignal,PlotNameSideband, CatB_sideband, CatC_sideband, CatD_sideband,QCDSample, name, useGeneratorDiff=False):

    category='_notopbtag'
    if 'with' in PlotNameSignal:
        category='_withtopbtag'
        
    loldataT=transposeLOL(loldata)
    lolBackgroundT=transposeLOL(lolBackground) 
    lolSignalT=transposeLOL(lolSignal)

    llldatacopy=copy.deepcopy(llldata)
    llldatacopyABCD=copy.deepcopy(llldata)
    lllBackgroundWithweightsyscopy=copy.deepcopy(lllBackgroundWithweightsys)
    lllBackgroundWithweightsyscopyABCD=copy.deepcopy(lllBackgroundWithweightsys)
    
    subtract_llls(transposeLOL([transposeLOL(llldatacopyABCD)[DataSampleNames.index(DatasampleNick)]]),transposeLOL([transposeLOL(lllBackgroundWithweightsyscopyABCD)[BackgroundSampleNames.index('ttbar')]]))   
    
    rebintoonebinllls(llldatacopyABCD)

    dividellls(llldatacopyABCD, plotnames.index(CatB_sideband), plotnames.index(CatD_sideband),False)
    multiplyllls(llldatacopyABCD, plotnames.index(CatB_sideband),plotnames.index(CatC_sideband),False)
    #dividellls(lllBackgroundWithweightsyscopyABCD, weightsystnames.index(CatB_sideband), weightsystnames.index(CatD_sideband),False,lllBackgroundWithweightsyscopyABCD[plotnames.index(CatD_sideband)][DataSampleNames.index(DatasampleNick)][weightsystnames.index(SBSSF_nick+'_nominal')].GetNbinsX())
    #multiplyllls(lllBackgroundWithweightsyscopyABCD, weightsystnames.index(CatB_sideband),weightsystnames.index(CatC_sideband),False,lllBackgroundWithweightsyscopyABCD[plotnames.index(CatC_sideband)][DataSampleNames.index(DatasampleNick)][weightsystnames.index(SBSSF_nick+'_nominal')].GetNbinsX())
    
    #dividellls(lllBackgroundWithweightsyscopyABCD, weightsystnames.index(CatB_sideband), weightsystnames.index(CatD_sideband),False)
    #multiplyllls(lllBackgroundWithweightsyscopyABCD, weightsystnames.index(CatB_sideband),weightsystnames.index(CatC_sideband),False)  
    subtract_histos(llldatacopy[plotnames.index(PlotNameSideband)][DataSampleNames.index(DatasampleNick)][weightsystnames.index(SBSSF_nick+'_nominal')],lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)][BackgroundSampleNames.index('ttbar')][weightsystnames.index(SBSSF_nick+'_nominal')])
    
    #divideHistos(loldatacopyABCD, plotnames.index(CatB_sideband), plotnames.index(CatD_sideband),False,loldatacopy[plotnames.index(CatB_sideband)][DataSampleNames.index(DatasampleNick)].GetNbinsX())
    #multiplyHistos(loldatacopyABCD, plotnames.index(CatB_sideband),plotnames.index(CatC_sideband),False,loldatacopy[plotnames.index(CatC_sideband)][DataSampleNames.index(DatasampleNick)].GetNbinsX())
    
    
    #subtract_histos(loldatacopy[plotnames.index(PlotNameSignal)][DataSampleNames.index(DatasampleNick)],lolBackgroundcopy[plotnames.index(PlotNameSignal)][BackgroundSampleNames.index('ttbar')])   
    print llldatacopy[plotnames.index(PlotNameSideband)][DataSampleNames.index(DatasampleNick)][weightsystnames.index(SBSSF_nick+'_nominal')], 'Integral ', llldatacopy[plotnames.index(PlotNameSideband)][DataSampleNames.index(DatasampleNick)][weightsystnames.index(SBSSF_nick+'_nominal')].Integral()
    print lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)][BackgroundSampleNames.index(QCDSample)][weightsystnames.index(SBSSF_nick+'_nominal')], ' Integral ', lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)][BackgroundSampleNames.index(QCDSample)][weightsystnames.index(SBSSF_nick+'_nominal')].Integral()
    
    print llldatacopyABCD[plotnames.index(CatB_sideband)][DataSampleNames.index(DatasampleNick)][weightsystnames.index('_ABCD_nominal')], 'Integral ', llldatacopyABCD[plotnames.index(CatB_sideband)][DataSampleNames.index(DatasampleNick)][weightsystnames.index('_ABCD_nominal')].Integral()
    
    
    
    normalizeBKGtoData([llldatacopy[plotnames.index(PlotNameSideband)][DataSampleNames.index(DatasampleNick)][weightsystnames.index(SBSSF_nick+'_nominal')]],transposeLOL(lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)]),llldatacopyABCD[plotnames.index(CatB_sideband)][DataSampleNames.index(DatasampleNick)][weightsystnames.index('_ABCD_nominal')])
    
    print lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)][BackgroundSampleNames.index(QCDSample)][weightsystnames.index(SBSSF_nick+'_nominal')], ' Integral ', lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)][BackgroundSampleNames.index(QCDSample)][weightsystnames.index(SBSSF_nick+'_nominal')].Integral()
     
    QCDlist=[transposeLOL(transposeLOL(lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)])[weightsystnames.index(SBSSF_nick+'_nominal'):weightsystnames.index(SBSSF_nick+'_systdown')+1])[BackgroundSampleNames.index(QCDSample)]+transposeLOL(transposeLOL(lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)])[weightsystnames.index(SBSSF_nick+'GeneratorDiff_systup'):weightsystnames.index(SBSSF_nick+'GeneratorDiff_systdown')+1])[BackgroundSampleNames.index(QCDSample)]]
    
    ttbarlist=[transposeLOL(transposeLOL(lllBackgroundNoweightsys[plotnames.index(PlotNameSignal)])[weightsystnames.index('_no'+'_nominal'):weightsystnames.index('_no'+'_systdown')+1])[BackgroundSampleNames.index('ttbar')]+transposeLOL(transposeLOL(lllBackgroundNoweightsys[plotnames.index(PlotNameSignal)])[weightsystnames.index('_no'+'_systup'):weightsystnames.index('_no'+'_systdown')+1])[BackgroundSampleNames.index('ttbar')]]
    
    SClist=[transposeLOL(transposeLOL(lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)])[weightsystnames.index(SBSSF_nick+'_nominal'):weightsystnames.index(SBSSF_nick+'_systdown')+1])[BackgroundSampleNames.index(SCNick)]+transposeLOL(transposeLOL(lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)])[weightsystnames.index(SBSSF_nick+'GeneratorDiff_systup'):weightsystnames.index(SBSSF_nick+'GeneratorDiff_systdown')+1])[BackgroundSampleNames.index(SCNick)]]


    if(useGeneratorDiff):
        
        QCDlist=[transposeLOL(transposeLOL(lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)])[weightsystnames.index(SBSSF_nick+'_nominal'):weightsystnames.index(SBSSF_nick+'_systdown')+1])[BackgroundSampleNames.index(QCDSample)]+transposeLOL(transposeLOL(lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)])[weightsystnames.index(SBSSF_nick+'GeneratorDiff_systup'):weightsystnames.index(SBSSF_nick+'GeneratorDiff_systdown')+1])[BackgroundSampleNames.index(QCDSample)]+transposeLOL(transposeLOL(lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)])[weightsystnames.index('_ABCD'+category+'_ZprimeM'+'_systup'):weightsystnames.index('_ABCD'+category+'_ZprimeM'+'_systdown')+1])[BackgroundSampleNames.index(QCDSample)]]
    
        ttbarlist=[transposeLOL(transposeLOL(lllBackgroundNoweightsys[plotnames.index(PlotNameSignal)])[weightsystnames.index('_no'+'_nominal'):weightsystnames.index('_no'+'_systdown')+1])[BackgroundSampleNames.index('ttbar')]+transposeLOL(transposeLOL(lllBackgroundNoweightsys[plotnames.index(PlotNameSignal)])[weightsystnames.index('_no'+'_systup'):weightsystnames.index('_no'+'_systdown')+1])[BackgroundSampleNames.index('ttbar')]]
    
        SClist=[transposeLOL(transposeLOL(lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)])[weightsystnames.index(SBSSF_nick+'_nominal'):weightsystnames.index(SBSSF_nick+'_systdown')+1])[BackgroundSampleNames.index(SCNick)]+transposeLOL(transposeLOL(lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)])[weightsystnames.index(SBSSF_nick+'GeneratorDiff_systup'):weightsystnames.index(SBSSF_nick+'GeneratorDiff_systdown')+1])[BackgroundSampleNames.index(SCNick)]+transposeLOL(transposeLOL(lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)])[weightsystnames.index('_ABCD'+category+'_ZprimeM'+'_systup'):weightsystnames.index('_ABCD'+category+'_ZprimeM'+'_systdown')+1])[BackgroundSampleNames.index(SCNick)]]
    
        plotDataMCanWsyst([transposeLOL([loldataT[DataSampleNames.index(DatasampleNick)]])[plotnames.index(PlotNameSignal)]],transposeLOL([[lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)][BackgroundSampleNames.index(SCNick)][weightsystnames.index(SBSSF_nick+'_nominal')]]]+[[lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)][BackgroundSampleNames.index(QCDSample)][weightsystnames.index(SBSSF_nick+'_nominal')]]]+[transposeLOL([lolBackgroundT[BackgroundSampleNames.index("ttbar")]])[plotnames.index(PlotNameSignal)]]),[BackgroundSamples[BackgroundSampleNames.index(SCNick)]]+[BackgroundSamples[BackgroundSampleNames.index(QCDSample)]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]],transposeLOL([lolSignalT[SignalSampleNames.index(SignalsampleNick)]])[plotnames.index(PlotNameSignal)],SignalSamples[SignalSampleNames.index(SignalsampleNick)],1,name+DatasampleNick+QCDSample,[[[SClist+QCDlist+ttbarlist],3354,ROOT.kBlack,True]],False,SBSSF_nick+'+GeneratorDiff',True,False, False, True)
        print 'used generator differences'
        
    else:
        
        QCDlist=[transposeLOL(transposeLOL(lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)])[weightsystnames.index(SBSSF_nick+'_nominal'):weightsystnames.index(SBSSF_nick+'_systdown')+1])[BackgroundSampleNames.index(QCDSample)]+transposeLOL(transposeLOL(lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)])[weightsystnames.index('_ABCD'+category+'_ZprimeM'+'_systup'):weightsystnames.index('_ABCD'+category+'_ZprimeM'+'_systdown')+1])[BackgroundSampleNames.index(QCDSample)]]
    
        ttbarlist=[transposeLOL(transposeLOL(lllBackgroundNoweightsys[plotnames.index(PlotNameSignal)])[weightsystnames.index('_no'+'_nominal'):weightsystnames.index('_no'+'_systdown')+1])[BackgroundSampleNames.index('ttbar')]]
    
        SClist=[transposeLOL(transposeLOL(lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)])[weightsystnames.index(SBSSF_nick+'_nominal'):weightsystnames.index(SBSSF_nick+'_systdown')+1])[BackgroundSampleNames.index(SCNick)]+transposeLOL(transposeLOL(lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)])[weightsystnames.index('_ABCD'+category+'_ZprimeM'+'_systup'):weightsystnames.index('_ABCD'+category+'_ZprimeM'+'_systdown')+1])[BackgroundSampleNames.index(SCNick)]]
        
        plotDataMCanWsyst([transposeLOL([loldataT[DataSampleNames.index(DatasampleNick)]])[plotnames.index(PlotNameSignal)]],transposeLOL([[lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)][BackgroundSampleNames.index(SCNick)][weightsystnames.index(SBSSF_nick+'_nominal')]]]+[[lllBackgroundWithweightsyscopy[plotnames.index(PlotNameSideband)][BackgroundSampleNames.index(QCDSample)][weightsystnames.index(SBSSF_nick+'_nominal')]]]+[transposeLOL([lolBackgroundT[BackgroundSampleNames.index("ttbar")]])[plotnames.index(PlotNameSignal)]]),[BackgroundSamples[BackgroundSampleNames.index(SCNick)]]+[BackgroundSamples[BackgroundSampleNames.index(QCDSample)]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]],transposeLOL([lolSignalT[SignalSampleNames.index(SignalsampleNick)]])[plotnames.index(PlotNameSignal)],SignalSamples[SignalSampleNames.index(SignalsampleNick)],1,name+DatasampleNick+QCDSample,[[[SClist+QCDlist+ttbarlist],3354,ROOT.kBlack,True]],False,SBSSF_nick,True,False, False, True)




def ABCDBackgroundEstimationCalculationAndPlotsWithSystematics(loldata,llldata,lolBackground,lllBackgroundWithweightsys,lllBackgroundNoweightsys,lolSignal,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames, SignalSampleNames, plotnames,weightsystnames,DatasampleNick,SCNick,SignalsampleNick,CatA_sideband, CatB_sideband, CatC_sideband, CatD_sideband,QCDSample, name):
    category='_notopbtag'
    if 'with' in CatA_sideband:
        category='_withtopbtag'
    if 'inclusive' in CatA_sideband:
        category='_inclusive'

    loldataT=transposeLOL(loldata)
    lolBackgroundT=transposeLOL(lolBackground) 
    lolSignalT=transposeLOL(lolSignal)


    llldatacopyABCD=copy.deepcopy(llldata)

    lllBackgroundWithweightsyscopyABCD=copy.deepcopy(lllBackgroundWithweightsys)
    
    
    subtract_llls(transposeLOL([transposeLOL(llldatacopyABCD)[DataSampleNames.index(DatasampleNick)]]),transposeLOL([transposeLOL(lllBackgroundWithweightsyscopyABCD)[BackgroundSampleNames.index('ttbar')]]))   
    
    
    dividellls(llldatacopyABCD, plotnames.index(CatB_sideband+'_Zprime_M'), plotnames.index(CatD_sideband+'_Zprime_M'),False)
    multiplyllls(llldatacopyABCD, plotnames.index(CatB_sideband+'_Zprime_M'),plotnames.index(CatC_sideband+'_Zprime_M'),False)
    dividellls(lllBackgroundWithweightsyscopyABCD, plotnames.index(CatB_sideband+'_Zprime_M'), plotnames.index(CatD_sideband+'_Zprime_M'),False)
    multiplyllls(lllBackgroundWithweightsyscopyABCD, plotnames.index(CatB_sideband+'_Zprime_M'),plotnames.index(CatC_sideband+'_Zprime_M'),False)    
    
    llldatacopyABCD_SConly=copy.deepcopy(llldatacopyABCD)
    subtract_llls(transposeLOL([transposeLOL(llldatacopyABCD_SConly)[DataSampleNames.index(DatasampleNick)]]),transposeLOL([transposeLOL(lllBackgroundWithweightsyscopyABCD)[BackgroundSampleNames.index(QCDSample)]]))
    
    Data=[transposeLOL([loldataT[DataSampleNames.index(DatasampleNick)]])[plotnames.index(CatA_sideband+'_Zprime_M')]]
   
    Backgrounds=transposeLOL([[llldatacopyABCD_SConly[plotnames.index(CatB_sideband+'_Zprime_M')][DataSampleNames.index(DatasampleNick)][weightsystnames.index('_ABCD_nominal')]]]+[[lllBackgroundWithweightsyscopyABCD[plotnames.index(CatB_sideband+'_Zprime_M')][BackgroundSampleNames.index(QCDSample)][weightsystnames.index('_ABCD_nominal')]]]+[transposeLOL([lolBackgroundT[BackgroundSampleNames.index("ttbar")]])[plotnames.index(CatA_sideband+'_Zprime_M')]])
    
    Backgroundsamples=[BackgroundSamples[BackgroundSampleNames.index(SCNick)]]+[BackgroundSamples[BackgroundSampleNames.index(QCDSample)]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]]
    OTSignal=transposeLOL([lolSignalT[SignalSampleNames.index(SignalsampleNick)]])[plotnames.index(CatA_sideband+'_Zprime_M')]
    SignalSamples=SignalSamples[SignalSampleNames.index(SignalsampleNick)]


    QCDlist=[transposeLOL([transposeLOL(lllBackgroundWithweightsyscopyABCD[plotnames.index(CatB_sideband+'_Zprime_M')])[weightsystnames.index('_ABCD_nominal')]]+transposeLOL(lllBackgroundWithweightsyscopyABCD[plotnames.index(CatB_sideband+'_Zprime_M')])[weightsystnames.index('_ABCD'+category+'_ZprimeM'+'_systup'):weightsystnames.index('_ABCD'+category+'_ZprimeM'+'_systdown')+1])[BackgroundSampleNames.index(QCDSample)]]
    
    ttbarlist=[transposeLOL(transposeLOL(lllBackgroundNoweightsys[plotnames.index(CatA_sideband+'_Zprime_M')])[weightsystnames.index('_no'+'_nominal'):weightsystnames.index('_no'+'_systdown')+1])[BackgroundSampleNames.index('ttbar')]]
    
    SClist=[transposeLOL([transposeLOL(llldatacopyABCD_SConly[plotnames.index(CatB_sideband+'_Zprime_M')])[weightsystnames.index('_ABCD_nominal')]]+transposeLOL(llldatacopyABCD_SConly[plotnames.index(CatB_sideband+'_Zprime_M')])[weightsystnames.index('_ABCD'+category+'_ZprimeM'+'_systup'):weightsystnames.index('_ABCD'+category+'_ZprimeM'+'_systdown')+1])[DataSampleNames.index(DatasampleNick)]]  

    
    plotDataMCanWsyst(Data,Backgrounds,Backgroundsamples,OTSignal,SignalSamples,1,name+category+'_'+DatasampleNick+QCDSample,[[[SClist+QCDlist+ttbarlist],3354,ROOT.kBlack,True]],False,'ABCD'+category+'_ZprimeM',True,False, False, True)
    
    
    
    dividellls(llldatacopyABCD, plotnames.index(CatB_sideband+'_Tprime_M'), plotnames.index(CatD_sideband+'_Tprime_M'),False)
    multiplyllls(llldatacopyABCD, plotnames.index(CatB_sideband+'_Tprime_M'),plotnames.index(CatC_sideband+'_Tprime_M'),False)
    dividellls(lllBackgroundWithweightsyscopyABCD, plotnames.index(CatB_sideband+'_Tprime_M'), plotnames.index(CatD_sideband+'_Tprime_M'),False)
    multiplyllls(lllBackgroundWithweightsyscopyABCD, plotnames.index(CatB_sideband+'_Tprime_M'),plotnames.index(CatC_sideband+'_Tprime_M'),False)    
    
    llldatacopyABCD_SConly=copy.deepcopy(llldatacopyABCD)
    subtract_llls(transposeLOL([transposeLOL(llldatacopyABCD_SConly)[DataSampleNames.index(DatasampleNick)]]),transposeLOL([transposeLOL(lllBackgroundWithweightsyscopyABCD)[BackgroundSampleNames.index(QCDSample)]]))
    
    Data=[transposeLOL([loldataT[DataSampleNames.index(DatasampleNick)]])[plotnames.index(CatA_sideband+'_Tprime_M')]]
   
    Backgrounds=transposeLOL([[llldatacopyABCD_SConly[plotnames.index(CatB_sideband+'_Tprime_M')][DataSampleNames.index(DatasampleNick)][weightsystnames.index('_ABCD_nominal')]]]+[[lllBackgroundWithweightsyscopyABCD[plotnames.index(CatB_sideband+'_Tprime_M')][BackgroundSampleNames.index(QCDSample)][weightsystnames.index('_ABCD_nominal')]]]+[transposeLOL([lolBackgroundT[BackgroundSampleNames.index("ttbar")]])[plotnames.index(CatA_sideband+'_Tprime_M')]])
    
    #Backgroundsamples=[BackgroundSamples[BackgroundSampleNames.index(SCNick)]]+[BackgroundSamples[BackgroundSampleNames.index(QCDSample)]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]]
    OTSignal=transposeLOL([lolSignalT[SignalSampleNames.index(SignalsampleNick)]])[plotnames.index(CatA_sideband+'_Tprime_M')]
    #SignalSamples=SignalSamples[SignalSampleNames.index(SignalsampleNick)]


    QCDlist=[transposeLOL([transposeLOL(lllBackgroundWithweightsyscopyABCD[plotnames.index(CatB_sideband+'_Tprime_M')])[weightsystnames.index('_ABCD_nominal')]]+transposeLOL(lllBackgroundWithweightsyscopyABCD[plotnames.index(CatB_sideband+'_Tprime_M')])[weightsystnames.index('_ABCD'+category+'_TprimeM'+'_systup'):weightsystnames.index('_ABCD'+category+'_TprimeM'+'_systdown')+1])[BackgroundSampleNames.index(QCDSample)]]
    ttbarlist=[transposeLOL(transposeLOL(lllBackgroundNoweightsys[plotnames.index(CatA_sideband+'_Tprime_M')])[weightsystnames.index('_no'+'_nominal'):weightsystnames.index('_no'+'_systdown')+1])[BackgroundSampleNames.index('ttbar')]]
    SClist=[transposeLOL([transposeLOL(llldatacopyABCD_SConly[plotnames.index(CatB_sideband+'_Tprime_M')])[weightsystnames.index('_ABCD_nominal')]]+transposeLOL(llldatacopyABCD_SConly[plotnames.index(CatB_sideband+'_Tprime_M')])[weightsystnames.index('_ABCD'+category+'_TprimeM'+'_systup'):weightsystnames.index('_ABCD'+category+'_TprimeM'+'_systdown')+1])[DataSampleNames.index(DatasampleNick)]]  

    
    plotDataMCanWsyst(Data,Backgrounds,Backgroundsamples,OTSignal,SignalSamples,1,name+category+'_'+DatasampleNick+QCDSample,[[[SClist+QCDlist+ttbarlist],3354,ROOT.kBlack,True]],False,'ABCD'+category+'_TprimeM',True,False, False, True)    
    print category
    print QCDlist
    print ttbarlist
    print SClist
    #raw_input()



def ABCDcorrEBackgroundEstimationCalculationAndPlotsWithSystematics(loldata,llldata,lolBackground,lllBackgroundWithweightsys,lllBackgroundNoweightsys,lolSignal,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames, SignalSampleNames, plotnames,weightsystnames,DatasampleNick,SCNick,SignalsampleNick,CatA_sideband, CatB_sideband, CatC_sideband, CatD_sideband,CatE_sideband, CatF_sideband, CatG_sideband, CatH_sideband,QCDSample, name):
    
    ABCDversion=''
    if 'ABCD' in name:
        ABCDversion='ABCD'
    if 'ABCD2' in name:
        ABCDversion='ABCD2'
        
    category='_notopbtag'
    if 'with' in CatA_sideband:
        category='_withtopbtag'
    if 'inclusive' in CatA_sideband:
        category='_inclusive'
        
        

    loldataT=transposeLOL(loldata)
    lolBackgroundT=transposeLOL(lolBackground) 
    lolSignalT=transposeLOL(lolSignal)


    llldatacopyABCD=copy.deepcopy(llldata)

    lllBackgroundWithweightsyscopyABCD=copy.deepcopy(lllBackgroundWithweightsys)
    
    
    subtract_llls(transposeLOL([transposeLOL(llldatacopyABCD)[DataSampleNames.index(DatasampleNick)]]),transposeLOL([transposeLOL(lllBackgroundWithweightsyscopyABCD)[BackgroundSampleNames.index('ttbar')]]))   
    
    
    dividellls(llldatacopyABCD, plotnames.index(CatB_sideband+'_Zprime_M'), plotnames.index(CatD_sideband+'_Zprime_M'),False)
    multiplyllls(llldatacopyABCD, plotnames.index(CatB_sideband+'_Zprime_M'),plotnames.index(CatC_sideband+'_Zprime_M'),False)
    dividellls(llldatacopyABCD, plotnames.index(CatF_sideband+'_Zprime_M'), plotnames.index(CatH_sideband+'_Zprime_M'),False)
    multiplyllls(llldatacopyABCD, plotnames.index(CatF_sideband+'_Zprime_M'),plotnames.index(CatG_sideband+'_Zprime_M'),False)
    dividellls(llldatacopyABCD, plotnames.index(CatE_sideband+'_Zprime_M'), plotnames.index(CatF_sideband+'_Zprime_M'),False)
    multiplyllls(llldatacopyABCD, plotnames.index(CatB_sideband+'_Zprime_M'), plotnames.index(CatE_sideband+'_Zprime_M'),False)
    
    dividellls(lllBackgroundWithweightsyscopyABCD, plotnames.index(CatB_sideband+'_Zprime_M'), plotnames.index(CatD_sideband+'_Zprime_M'),False)
    multiplyllls(lllBackgroundWithweightsyscopyABCD, plotnames.index(CatB_sideband+'_Zprime_M'),plotnames.index(CatC_sideband+'_Zprime_M'),False)   
    dividellls(lllBackgroundWithweightsyscopyABCD, plotnames.index(CatF_sideband+'_Zprime_M'), plotnames.index(CatH_sideband+'_Zprime_M'),False)
    multiplyllls(lllBackgroundWithweightsyscopyABCD, plotnames.index(CatF_sideband+'_Zprime_M'),plotnames.index(CatG_sideband+'_Zprime_M'),False)    
    dividellls(lllBackgroundWithweightsyscopyABCD, plotnames.index(CatE_sideband+'_Zprime_M'), plotnames.index(CatF_sideband+'_Zprime_M'),False)
    multiplyllls(lllBackgroundWithweightsyscopyABCD, plotnames.index(CatB_sideband+'_Zprime_M'), plotnames.index(CatE_sideband+'_Zprime_M'),False)

    
    llldatacopyABCD_SConly=copy.deepcopy(llldatacopyABCD)
    subtract_llls(transposeLOL([transposeLOL(llldatacopyABCD_SConly)[DataSampleNames.index(DatasampleNick)]]),transposeLOL([transposeLOL(lllBackgroundWithweightsyscopyABCD)[BackgroundSampleNames.index(QCDSample)]]))
    
    Data=[transposeLOL([loldataT[DataSampleNames.index(DatasampleNick)]])[plotnames.index(CatA_sideband+'_Zprime_M')]]
   
    Backgrounds=transposeLOL([[llldatacopyABCD_SConly[plotnames.index(CatB_sideband+'_Zprime_M')][DataSampleNames.index(DatasampleNick)][weightsystnames.index('_ABCD_nominal')]]]+[[lllBackgroundWithweightsyscopyABCD[plotnames.index(CatB_sideband+'_Zprime_M')][BackgroundSampleNames.index(QCDSample)][weightsystnames.index('_ABCD_nominal')]]]+[transposeLOL([lolBackgroundT[BackgroundSampleNames.index("ttbar")]])[plotnames.index(CatA_sideband+'_Zprime_M')]])
    
    Backgroundsamples=[BackgroundSamples[BackgroundSampleNames.index(SCNick)]]+[BackgroundSamples[BackgroundSampleNames.index(QCDSample)]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]]
    OTSignalZprime=transposeLOL([lolSignalT[SignalSampleNames.index(SignalsampleNick)]])[plotnames.index(CatA_sideband+'_Zprime_M')]
    SignalSamples=SignalSamples[SignalSampleNames.index(SignalsampleNick)]


    QCDlist=[transposeLOL([transposeLOL(lllBackgroundWithweightsyscopyABCD[plotnames.index(CatB_sideband+'_Zprime_M')])[weightsystnames.index('_ABCD_nominal')]]+transposeLOL(lllBackgroundWithweightsyscopyABCD[plotnames.index(CatB_sideband+'_Zprime_M')])[weightsystnames.index('_'+ABCDversion+'corrE'+category+'_ZprimeM'+'_systup'):weightsystnames.index('_'+ABCDversion+'corrE'+category+'_ZprimeM'+'_systdown')+1])[BackgroundSampleNames.index(QCDSample)]]
    ttbarlist=[transposeLOL(transposeLOL(lllBackgroundNoweightsys[plotnames.index(CatA_sideband+'_Zprime_M')])[weightsystnames.index('_no'+'_nominal'):weightsystnames.index('_no'+'_systdown')+1])[BackgroundSampleNames.index('ttbar')]]
    SClist=[transposeLOL([transposeLOL(llldatacopyABCD_SConly[plotnames.index(CatB_sideband+'_Zprime_M')])[weightsystnames.index('_ABCD_nominal')]]+transposeLOL(llldatacopyABCD_SConly[plotnames.index(CatB_sideband+'_Zprime_M')])[weightsystnames.index('_'+ABCDversion+'corrE'+category+'_ZprimeM'+'_systup'):weightsystnames.index('_'+ABCDversion+'corrE'+category+'_ZprimeM'+'_systdown')+1])[DataSampleNames.index(DatasampleNick)]]  

    
    plotDataMCanWsyst(Data,Backgrounds,Backgroundsamples,OTSignalZprime,SignalSamples,1,name+category+DatasampleNick+QCDSample,[[[SClist+QCDlist+ttbarlist],3354,ROOT.kBlack,True]],False,ABCDversion+'corrE'+category+'_ZprimeM',True,False, False, True)
    
    
    
    
    dividellls(llldatacopyABCD, plotnames.index(CatB_sideband+'_Tprime_M'), plotnames.index(CatD_sideband+'_Tprime_M'),False)
    multiplyllls(llldatacopyABCD, plotnames.index(CatB_sideband+'_Tprime_M'),plotnames.index(CatC_sideband+'_Tprime_M'),False)
    dividellls(llldatacopyABCD, plotnames.index(CatF_sideband+'_Tprime_M'), plotnames.index(CatH_sideband+'_Tprime_M'),False)
    multiplyllls(llldatacopyABCD, plotnames.index(CatF_sideband+'_Tprime_M'),plotnames.index(CatG_sideband+'_Tprime_M'),False)
    dividellls(llldatacopyABCD, plotnames.index(CatE_sideband+'_Tprime_M'), plotnames.index(CatF_sideband+'_Tprime_M'),False)
    multiplyllls(llldatacopyABCD, plotnames.index(CatB_sideband+'_Tprime_M'), plotnames.index(CatE_sideband+'_Tprime_M'),False)
    
    dividellls(lllBackgroundWithweightsyscopyABCD, plotnames.index(CatB_sideband+'_Tprime_M'), plotnames.index(CatD_sideband+'_Tprime_M'),False)
    multiplyllls(lllBackgroundWithweightsyscopyABCD, plotnames.index(CatB_sideband+'_Tprime_M'),plotnames.index(CatC_sideband+'_Tprime_M'),False)   
    dividellls(lllBackgroundWithweightsyscopyABCD, plotnames.index(CatF_sideband+'_Tprime_M'), plotnames.index(CatH_sideband+'_Tprime_M'),False)
    multiplyllls(lllBackgroundWithweightsyscopyABCD, plotnames.index(CatF_sideband+'_Tprime_M'),plotnames.index(CatG_sideband+'_Tprime_M'),False)    
    dividellls(lllBackgroundWithweightsyscopyABCD, plotnames.index(CatE_sideband+'_Tprime_M'), plotnames.index(CatF_sideband+'_Tprime_M'),False)
    multiplyllls(lllBackgroundWithweightsyscopyABCD, plotnames.index(CatB_sideband+'_Tprime_M'), plotnames.index(CatE_sideband+'_Tprime_M'),False)

 
 
    llldatacopyABCD_SConly=copy.deepcopy(llldatacopyABCD)
    subtract_llls(transposeLOL([transposeLOL(llldatacopyABCD_SConly)[DataSampleNames.index(DatasampleNick)]]),transposeLOL([transposeLOL(lllBackgroundWithweightsyscopyABCD)[BackgroundSampleNames.index(QCDSample)]]))
    
    Data=[transposeLOL([loldataT[DataSampleNames.index(DatasampleNick)]])[plotnames.index(CatA_sideband+'_Tprime_M')]]
   
    Backgrounds=transposeLOL([[llldatacopyABCD_SConly[plotnames.index(CatB_sideband+'_Tprime_M')][DataSampleNames.index(DatasampleNick)][weightsystnames.index('_ABCD_nominal')]]]+[[lllBackgroundWithweightsyscopyABCD[plotnames.index(CatB_sideband+'_Tprime_M')][BackgroundSampleNames.index(QCDSample)][weightsystnames.index('_ABCD_nominal')]]]+[transposeLOL([lolBackgroundT[BackgroundSampleNames.index("ttbar")]])[plotnames.index(CatA_sideband+'_Tprime_M')]])
    
    #Backgroundsamples=[BackgroundSamples[BackgroundSampleNames.index(SCNick)]]+[BackgroundSamples[BackgroundSampleNames.index(QCDSample)]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]]
    OTSignalTprime=transposeLOL([lolSignalT[SignalSampleNames.index(SignalsampleNick)]])[plotnames.index(CatA_sideband+'_Tprime_M')]
    #SignalSamples=SignalSamples[SignalSampleNames.index(SignalsampleNick)]


    QCDlist=[transposeLOL([transposeLOL(lllBackgroundWithweightsyscopyABCD[plotnames.index(CatB_sideband+'_Tprime_M')])[weightsystnames.index('_ABCD_nominal')]]+transposeLOL(lllBackgroundWithweightsyscopyABCD[plotnames.index(CatB_sideband+'_Tprime_M')])[weightsystnames.index('_'+ABCDversion+'corrE'+category+'_TprimeM'+'_systup'):weightsystnames.index('_'+ABCDversion+'corrE'+category+'_TprimeM'+'_systdown')+1])[BackgroundSampleNames.index(QCDSample)]]
    ttbarlist=[transposeLOL(transposeLOL(lllBackgroundNoweightsys[plotnames.index(CatA_sideband+'_Tprime_M')])[weightsystnames.index('_no'+'_nominal'):weightsystnames.index('_no'+'_systdown')+1])[BackgroundSampleNames.index('ttbar')]]
    SClist=[transposeLOL([transposeLOL(llldatacopyABCD_SConly[plotnames.index(CatB_sideband+'_Tprime_M')])[weightsystnames.index('_ABCD_nominal')]]+transposeLOL(llldatacopyABCD_SConly[plotnames.index(CatB_sideband+'_Tprime_M')])[weightsystnames.index('_'+ABCDversion+'corrE'+category+'_TprimeM'+'_systup'):weightsystnames.index('_'+ABCDversion+'corrE'+category+'_TprimeM'+'_systdown')+1])[DataSampleNames.index(DatasampleNick)]]  

    
    plotDataMCanWsyst(Data,Backgrounds,Backgroundsamples,OTSignalTprime,SignalSamples,1,name+category+DatasampleNick+QCDSample,[[[SClist+QCDlist+ttbarlist],3354,ROOT.kBlack,True]],False,ABCDversion+'corrE'+category+'_TprimeM',True,False, False, True)    
    print category
    print QCDlist
    print ttbarlist
    print SClist
    #raw_input()


def rebintoonebinllls(lll):
    for ll in lll:
        for l in ll:
            for histo in l:
                histo.Rebin(histo.GetNbinsX())
            
            
            
def dividellls(lll, numeratorPlot, denumeratorPlot, normalizefirst=False,rebin=1,option=''):
    for i in range(len(lll[numeratorPlot])):
        for j in range(len(lll[numeratorPlot][i])):
            numerator=lll[numeratorPlot][i][j].Clone()
            denumerator=lll[denumeratorPlot][i][j].Clone()
            
            numerator.Rebin(rebin)
            denumerator.Rebin(rebin)
            if normalizefirst: #######check if integral>0
                print 'Ratio of ', numerator,'  over  ', denumerator,'  =  ',(numerator.Integral())/(denumerator.Integral() )
                numerator.Scale(1./numerator.Integral())
                denumerator.Scale(1./denumerator.Integral())

            numerator.Divide(denumerator)
            lll[numeratorPlot][i][j]=numerator   

def multiplyllls(lll, ProduktPlot1, ProduktPlot2, normalizefirst=False,rebin=1,option=''):
    for i in range(len(lll[ProduktPlot1])):
        for j in range(len(lll[ProduktPlot1][i])):
            produkt1=lll[ProduktPlot1][i][j].Clone()
            produkt2=lll[ProduktPlot2][i][j].Clone()
            
            produkt1.Rebin(rebin)
            produkt2.Rebin(rebin)
            if normalizefirst: #######check if integral>0
                print 'Ratio of ', produkt1,'  over  ', produkt2,'  =  ',(produkt1.Integral())/(produkt2.Integral() )
                produkt1.Scale(1./produkt1.Integral())
                produkt2.Scale(1./produkt2.Integral())

            produkt1.Multiply(produkt2)
            lll[ProduktPlot1][i][j]=produkt1   


def rebintovarbinsLL(lll):
    lllreturn=[]
    #raw_input
    for ll in lll:
        llreturn=[]
        for l in ll:
            lreturn=[]
            for histo in l:
                #print histo.GetName()
                binwidth=histo.GetBinWidth(0)
                if (('Tprime_M' in histo.GetName()) and (not (isinstance(histo,ROOT.TH2)))):
                    #print 'Nbins histo before TprimeM ', histo.GetNbinsX()
                    xbins= array.array('d',[0,500,550,600,650,700,750,800,850,900,950,1000,1100,1200,1300,1400,1500,1650,1800,1950,2100,2300,2500])
                    historeturn=histo.Rebin(len(xbins)-1,histo.GetName(),xbins)
                    for i in range(historeturn.GetNbinsX()):
                        historeturn.SetBinContent(i,(historeturn.GetBinContent(i)*binwidth/(historeturn.GetBinWidth(i))))
                        historeturn.SetBinError(i,(historeturn.GetBinError(i)*binwidth/(historeturn.GetBinWidth(i))))
                    #print 'Nbins histo after TprimeM ', historeturn.GetNbinsX()
                    lreturn.append(historeturn)
                elif (('Zprime_M' in histo.GetName()) and (not (isinstance(histo,ROOT.TH2)))):
                    #print 'Nbins histo before ZprimeM ', histo.GetNbinsX()
                    xbins= array.array('d',[0,1000,1100,1200,1300,1400,1500,1650,1800,1950,2100,2300,2500,2750,3000,3250,3500,3750,4000,4500,5000])
                    historeturn=histo.Rebin(len(xbins)-1,histo.GetName(),xbins)
                    for i in range(historeturn.GetNbinsX()):
                        historeturn.SetBinContent(i,(historeturn.GetBinContent(i)*binwidth/(historeturn.GetBinWidth(i))))
                        historeturn.SetBinError(i,(historeturn.GetBinError(i)*binwidth/(historeturn.GetBinWidth(i))))
                        #print 'Nbins histo after ZprimeM ', historeturn.GetNbinsX()
                    lreturn.append(historeturn)
                else:
                    lreturn.append(histo)
            llreturn.append(lreturn)
        lllreturn.append(llreturn)
    #raw_input
    return lllreturn

def rebintovarbinsLOL(lol):
    lolreturn=[]
    #raw_input
    for l in lol:
        lreturn=[]
        for histo in l:
            #print histo.GetName()
            if (('Tprime_M' in histo.GetName()) and (not (isinstance(histo,ROOT.TH2)))):
                #print 'Nbins histo before TprimeM ', histo.GetNbinsX(),'  ' ,histo
                binwidth=histo.GetBinWidth(0)
                #print binwidth
                xbins= array.array('d',[0,500,550,600,650,700,750,800,850,900,950,1000,1100,1200,1300,1400,1500,1650,1800,1950,2100,2300,2500])
                historeturn=histo.Rebin(len(xbins)-1,histo.GetName(),xbins)
                for i in range(0,historeturn.GetNbinsX()):
                    historeturn.SetBinContent(i,(historeturn.GetBinContent(i)*binwidth/(historeturn.GetBinWidth(i))))
                    historeturn.SetBinError(i,(historeturn.GetBinError(i)*binwidth/(historeturn.GetBinWidth(i))))
                print 'Nbins histo after TprimeM ', historeturn.GetNbinsX(), ' ',historeturn,'  Integral:', historeturn.Integral()
                lreturn.append(historeturn)
            elif (('Zprime_M' in histo.GetName()) and (not (isinstance(histo,ROOT.TH2)))):
                #print isinstance(histo,ROOT.TH1)
            
                #print 'Nbins histo before ZprimeM ', histo.GetNbinsX(),'  ' ,histo
                binwidth=histo.GetBinWidth(0)
                #print binwidth
                xbins= array.array('d',[0,1000,1100,1200,1300,1400,1500,1650,1800,1950,2100,2300,2500,2750,3000,3250,3500,3750,4000,4500,5000])
                historeturn=histo.Rebin(len(xbins)-1,histo.GetName(),xbins)
                for i in range(0,historeturn.GetNbinsX()):
                    historeturn.SetBinContent(i,(historeturn.GetBinContent(i)*binwidth/(historeturn.GetBinWidth(i))))
                    historeturn.SetBinError(i,(historeturn.GetBinError(i)*binwidth/(historeturn.GetBinWidth(i))))
                print 'Nbins histo after ZprimeM ', historeturn.GetNbinsX(), ' ',historeturn,'  Integral:', historeturn.Integral()
                lreturn.append(historeturn)
            else:
                lreturn.append(histo)
        lolreturn.append(lreturn)
    raw_input
    return lolreturn

def chekcNbins(lol):
    for l in lol:
        for histo in l:
            if (('Tprime_M' in histo.GetName()) and (not (isinstance(histo,ROOT.TH1)))):
                print 'Nbins histo after TprimeM ', histo.GetNbinsX(),'  ', histo
            if (('Zprime_M' in histo.GetName()) and (not (isinstance(histo,ROOT.TH1)))):
                print 'Nbins histo after ZprimeM ', histo.GetNbinsX(),'  ', histo
    #raw_input()



#def ABCDclosure1D(lol,plotnames,samples,CatA,CatB,CatC,CatD, CatE,CatF,CatG,CatH,normalizefirst=False,rebin=1,option='',fit='pol1'):
    #divideHistos(lol), plotnames.index(CatA), plotnames.index(CatB), normalizefirst,rebin,option)
    #divideHistos(lol), plotnames.index(CatC), plotnames.index(CatD), normalizefirst,rebin,option)
    #divideHistos(lol), CatA, plotnames.index(CatC), False,1,option)

    #divideHistos(lol), plotnames.index(CatE), plotnames.index(CatF), normalizefirst=False,rebin=1,option)
    #divideHistos(lol), plotnames.index(CatG), plotnames.index(CatH), normalizefirst=False,rebin=1,option)
    #divideHistos(lol), plotnames.index(CatE), plotnames.index(CatG), False,1,option)


    #writeHistoListwithXYErrors(lol)[plotnames.index(CatA)]], samples, name="check0forABCD_"+topWP+"WP_ratioABoverCD_"+fit, rebin=1, fitoption=fit, labels=None, autoXrange=True)
    #writeHistoListwithXYErrors([lol)[plotnames.index(CatE)]], samples, name="check0forABCD_"+topWP+"WP_ratioEFoverGH_"+fit, rebin=1, fitoption=fit, labels=None, autoXrange=True)
    #divideHistos(lol), CatA, plotnames.index(CatE), False,1,option)



def GetListOfCorrelationLists(listOfHistoLists, DoSpear):
    ListOfCorrelationLists = []
    ListOfSpearCorrelationLists = []
    ListOfPValueLists = []
    ListOfPlotNameLists=[]
    ListOfNDFs=[]
    for HistoList in listOfHistoLists:
        CorrelationList = []
        SpearCorrelationList = []
        PlotNameList=[]
        PValueList =[]
        NDFs=[]
        # print "iterate over LOL"
        for Histo in HistoList:
            # print "iterate over L"
            a = Histo.GetCorrelationFactor()
            b = Histo.GetName()
            if DoSpear:
                c=  GetSpearCorrelationFactor(Histo)
            else: c="Spear Correlation Coefficient not activated."
            d, df= GetPValueHisto(Histo)
            CorrelationList.append(a)
            PlotNameList.append(b)
            SpearCorrelationList.append(c)
            PValueList.append(d)
            NDFs.append(df)
            # print "Correlation of Histogram: " , a
        ListOfCorrelationLists.append(CorrelationList)
        ListOfPlotNameLists.append(PlotNameList)
        ListOfSpearCorrelationLists.append(SpearCorrelationList)
        ListOfPValueLists.append(PValueList)
        ListOfNDFs.append(NDFs)
    return ListOfCorrelationLists, ListOfPlotNameLists, ListOfSpearCorrelationLists, ListOfPValueLists, ListOfNDFs


#Write CorrelationFactors of ListOfHistoLists to Textfile
def writeCorrLOL(listOfHistoLists, FileName="Correlationfactors.txt", PlotNames="", SampleNames = None, DoSpear=False ):
    with open(FileName, "w") as corrFile:
        CorrLOL, PlotNamesLOL, SpearLOL, PValueLOL, NDFLOL = GetListOfCorrelationLists(listOfHistoLists, DoSpear)
        print PValueLOL
        # print CorrLOL, PlotNamesLOL
        if PlotNames != "":
            if SampleNames == None:
                SampleNames = len(listOfHistoLists[0])*[""]
                
            for CorrL, PlotName, SpearL, PValueL, NDFs in zip(CorrLOL, PlotNames, SpearLOL, PValueLOL, NDFLOL):
                corrFile.write("----------------------------\n")
                corrFile.write(PlotName+"\n")
                for Corr, SampleName, Spear, PValue, NDF in zip(CorrL, SampleNames, SpearL, PValueL, NDFs):
                    corrFile.write(str(Corr)+"\t"+SampleName + "\tPearson \n")
                    corrFile.write(str(PValue)+"\t"+SampleName + "\tPValue \n")
                    corrFile.write(str(NDF) +"\t"+ SampleName+ "\t Number of Degrees of Freedom\n")
                    if DoSpear:
                        corrFile.write(str(Spear) + "\t"+SampleName + "\tSpearman \n")

                    
        else:
            for CorrL,NameL, SpearL, PValueL in zip( CorrLOL, PlotNamesLOL, SpearLOL, PValueLOL ):
                corrFile.write("----------------------------------------\n")
                for Corr, Name, Spear, PValue in zip(CorrL, NameL, SpearL, PValueL):
                    corrFile.write(str(Corr)+"\t\t"+Name + "\tPearson \n")
                    corrFile.write(str(PValue)+"\t\t"+Name + "\tPearson \n")
                    if DoSpear:
                        corrFile.write(str(Spear)+"\t\t"+Name + "\tSpearman \n")









#Functions to get the Spearman CorrelationFactor


#Get Temporary List of X an Y that can be ranked afterwards
def GetXYBins(Histo2D):
    X=[]
    Y=[]
    nx = Histo2D.GetNbinsX()
    ny = Histo2D.GetNbinsY()
    print "Entries of the Histogram", Histo2D.GetEntries()

    for x in range(nx+2):
        x_tmp = 0
        for y in range(ny+2):
            x_tmp += int(Histo2D.GetBinContent(x,y))
        # print "x_tmp", x_tmp
        for i in range(x_tmp):
            X.append(x)

            
    #Sort y, so that x-Entry at position i belongs to y-Entry at position i
    Y = []
    x_tmp = -1
    for x in X:
        if x == x_tmp:
            continue
        x_tmp = x
        for y in range(ny+2):
            
            Y += int(Histo2D.GetBinContent(x,y) ) * [y]
        
    
    # print "unranked", X, Y    
    return X,Y



#return to old sortation (as X was sorted before)
def unsorted(X_modified_sorted, X_):
    X = X_
    X_modified_unsorted= len(X)*['not changed yet']
    
    for i in range( len(X) ):
        index_tmp = X.index(  min( X ) )
        X_modified_unsorted[index_tmp] = X_modified_sorted[i]
        X[index_tmp] = max(X)+1
    return X_modified_unsorted
    


#Rank a given array
def RankArray(X_):
    X=X_
    X_sorted = sorted(X)
    X_ranked = []
    last = X_sorted[0]
    X_Bool_MoreThanLast = []
    
    for element in X_sorted[1:]:
        if element > last:
            X_Bool_MoreThanLast.append(True)
        else:
            X_Bool_MoreThanLast.append(False)
        last = element

    size = 1
    i = 1
    for MoreThanLast in X_Bool_MoreThanLast:
        if MoreThanLast:
            X_ranked += size*[i - (size - 1)/2. ]
            size = 1
        else:
            size += 1
        i += 1
        
    X_ranked += size*[ i- (size-1)/ 2. ]
    X_ranked = unsorted(X_ranked, X) #return to old sortation
    return X_ranked




def GetSpearCorrelationFactor(Histo_, Smaller=True):

    Histo = Histo_.Clone()
    if Smaller:
        Histo.Scale(200/Histo.Integral())
    
    X_tmp, Y_tmp = GetXYBins(Histo)
    X_ranked=RankArray(X_tmp)
    Y_ranked=RankArray(Y_tmp)

    
    histo_rank = ROOT.TH2F("histo_rank", "Histogram of ranked variables", 15 , 0.95*min(X_ranked), 1.05*max(X_ranked), 15 , 0.95*min(Y_ranked), 1.05*max(Y_ranked) )
    for i in range(len( X_ranked ) ):
        histo_rank.Fill( X_ranked[i], Y_ranked[i] )
        
    mycanv = ROOT.TCanvas("mycanv", "mycanv", 800, 600)
    histo_rank.Draw("colz")
    mycanv.SaveAs("ABCD/"+Histo.GetName()+"_ranked.png")
    SpearCorr = histo_rank.GetCorrelationFactor()
    return SpearCorr



#def closuretest(listOfHistos, listOfHistosPrediction, listOfHistosPrediction_systup, listOfHistosPrediction_systdown,samples, label,name,normalize=True,stack=False,logscale=False,options='histo',statTest=False, sepaTest=False,ratio=False):
    ##if DoProfile and not isinstance(listOfHistoLists[0][0], ROOT.TH2):
      ##print "need 2D plots for Profile Histograms"
      ##DoProfile=False
    #listofallstattests=[]
    #if isinstance(label, basestring):
        #labeltexts=len(listOfHistoLists)*[label]
##        print "bla"
    #else:
        #labeltexts=label
    #canvases=[]
    #objects=[]   
    #i=0
    #print labeltexts
        #listofthisstattests=[listOfHistos[0].GetTitle()]
        #i+=1
        #for histo, histoPrediction,histoPrediction_systup,histoPrediction_systdown,sample in zip(listOfHistos,listOfHistosPrediction,listOfHistosPrediction_systup,listOfHistosPrediction_systdown,samples):
            #print labeltext
            #yTitle='Events'
            #if normalize:
                #yTitle='normalized'
            #setupHisto(histo,sample.color,yTitle,stack)        
        #stattests2D=None
        #c=drawHistosOnCanvas([histoPrediction]+[histoPrediction_systup]+[histoPrediction_systdown]+[histo],normalize,stack,logscale,options,ratio,DoProfile)

        #if not isinstance(c, list):
            #c.SetName('c_'+listOfHistos[0].GetName())
            #l=getLegend2()
            #for h,sample in zip(listOfHistos,samples):
                #loption='L'
                #if stack:
                    #loption='F'            
                #l.AddEntry4545(h,sample.name,loption)
            #canvases.append(c)
            #l.Draw('same')
            #objects.append(l)
        #elif options == "colz":
            #for i in range(len(listOfHistos)):
                #c[i].SetName('c_'+listOfHistos[i].GetName()) #wrong! What name should be set?

            #if DoProfile:
                #c[-2].SetName('c_'+c[-2].GetName())
                #lx = getLegend2()
                #for px,  sample in zip(profilesx,  samples):
                    #lx.AddEntry4545( px.GetName() , sample.name, "L" )
                #lx.Draw("same")
                #objects.append(lx)
                
                #c[-1].SetName('c_'+c[-1].GetName())
                #ly = getLegend2()
                #for  py, sample in zip( profilesy, samples):
                    #ly.AddEntry4545( py.GetName() , sample.name, "L" )
                #ly.Draw("same")
                #objects.append(ly)
            #canvases+=c
        #else:
            #canvases+=c
        
        #if statTest:
            #if not isinstance(listOfHistos[0],ROOT.TH2):
                #tests=getStatTestsList(listOfHistos[0],listOfHistos[1:],"UW")
                #tests.Draw()
                #listofthisstattests.append(tests.GetTitle())
                #objects.append(tests)
        #if sepaTest:
            #stests=getSepaTests(listOfHistos[0],listOfHistos[1])
            #stests.Draw()
            #objects.append(stests)
        #if stattests2D!=None:
            ## stattests2D.Draw()
            #objects.append(stattests2D)
            #listofthisstattests.append(stattests2D.GetTitle())
        ## cms = ROOT.TLatex(0.2, 0.96, 'CMS private work'  );
        ## cms.SetTextFont(42)
        ## cms.SetTextSize(0.05)
        ## cms.SetNDC()
        ## cms.Draw()
        ## print cms
        ## objects.append(cms)

        #if not isinstance(c, list):
            #cms = ROOT.TLatex(0.2, 0.96, 'CMS preliminary,  37.8 fb^{-1},  #sqrt{s} = 13 TeV'  );
            #cms.SetTextFont(42)
            #cms.SetTextSize(0.05)
            #cms.SetNDC()
            #cms.Draw()
            #objects.append(cms)

            #label = ROOT.TLatex(0.2, 0.9, labeltext);
            #label.SetTextFont(42)
            #label.SetTextSize(0.04)
            #label.SetNDC()
            #label.Draw()
            #objects.append(label)
            #listofallstattests.append(listofthisstattests)
        ## else:
        ##     for can, sam in zip(c,samples):
        ##         labeltext = sam.name
        ##         label = ROOT.TLatex(0.2, 0.96, labeltext);
        ##         label.SetTextFont(42)
        ##         label.SetTextSize(0.04)
        ##         label.SetNDC()
        ##         label.Draw()
        ##         objects.append(label)
        ##     listofallstattests.append(listofthisstattests)

        
    #printCanvases(canvases,name)
    #writeObjects(canvases,name)
    #stattestoutfile=open("stattests_"+name+".txt","w")
    #for stst in listofallstattests:
      #stattestoutfile.write(' '.join(stst)+'\n')
    #stattestoutfile.close()  











#Is Correlation smaller than rho 0 -- probability Hypothesis is _what_ ?
#r CorrelationCoefficient, p, probability hypothesis is true, rho0 - hyothesis
def GetPValue(r, df, rho0=0):
    #Get t Wert
    T =abs( (math.atanh(r) - math.atanh(rho0) - r/df )/(1/math.sqrt(df)) )
    #Get Propability, rho0 is true
    return 2*(1 - ROOT.TMath.StudentI(T , df) )

def GetPValueHisto(Histo, rho0 = 0):
    r = Histo.GetCorrelationFactor()
    df = Histo.GetEntries()
    return GetPValue(r, df , rho0), df





def GetIntegralLOL( ListOfHistoLists ):
    print ListOfHistoLists
    ListOfIntegralLists = []
    for HistoList in ListOfHistoLists:
        IntegralList = []
        for Histo in HistoList:
            #IntegralList.append( Histo.IntegralAndError() )
            IntegralList.append( Histo.Integral() )
            error = ROOT.Double(0)
            if not isinstance(Histo,ROOT.TH2):
                #print error
                #print Histo, '  ', Histo.IntegralAndError(0,Histo.GetNbinsX(),error,"",)
                print Histo, ' Integral=', Histo.IntegralAndError(0,Histo.GetNbinsX(),error,""),'+-',error
        ListOfIntegralLists.append( IntegralList )
    return ListOfIntegralLists




def writeIntegralLOLinTEX( ListOfHistoLists, filename = "IntegralList.tex", samplenames_ = None ):

    if samplenames_ == None:
        samplenames = len(ListOfHistoLists[0])*[""]
    else:
        samplenames = samplenames_


    with open( filename , "w") as IntFile:
        IntFile.write( " %% List of Integrals of Histograms created in plotutils.py \n \\begin{tabular}{cc} \n \\toprule \n \\textbf{Integral} & \\textbf{Sample} \\\\ \n" )
        for HistoList in ListOfHistoLists:
            IntFile.write( "\\midrule \n " + str( HistoList[0].GetName()  )+ " & \\\\ \n " )
            for Histo, sample in zip( HistoList, samplenames ):
                IntFile.write( "\\tablenum{" +  str( Histo.Integral() ) + "}  & " + sample + "  \\\\ \n " )
                #IntFile.write( "\\tablenum{" +  str( Histo.IntegralAndError(0,GetNbinsX()-1) ) + "}  & " + sample + "  \\\\ \n " )
        IntFile.write( "\\bottomrule \n \\end{tabular} " )





#Transposes specific Indices Example: transposeLOLextended( list,  [ [1, 3], [2, 4] ] ) converts     list = [ [a1, a2], [b1, b2], [c1, c2], [d1, d2] ]     to      [ [a1, c1] , [a2, c2], [b1, d1], [b2, d2] ]
def transposeLOLextended( ListOfHistoList,  IndexListOfLists ):
    Transposed = []

    for IndexList in IndexListOfLists:
        tmpList=[]
        for Index in IndexList:
            tmpList.append( ListOfHistoList[Index] )
        Transposed += transposeLOL( tmpList )
        print "Warning in Function transposeLOLextended(): If used with writeListOfHistoLists, not all elements are appended to pdf file. Spepearate PDF and JPG are created."
    return Transposed




def ReconstructWithABCD(ListOfHistoLists, PlotnameCatA, plotnames):
    if(PlotnameCatA[8] != "A" ):
        print "Error in Function ReconstructWithABCD(): This Plot is not Category A"
        return

    stringlist=list(PlotnameCatA)
    stringlist[8]="B"
    PlotnameCatB="".join(stringlist)
    stringlist[8]="C"
    PlotnameCatC="".join(stringlist)
    stringlist[8]="D"
    PlotnameCatD="".join(stringlist)
    stringlist[8]="E"
    PlotnameCatE="".join(stringlist)
    stringlist[8]="F"
    PlotnameCatF="".join(stringlist)
    stringlist[8]="G"
    PlotnameCatG="".join(stringlist)
    stringlist[8]="H"
    PlotnameCatH="".join(stringlist)

    multiplyHistos(ListOfHistoLists, plotnames.index(PlotnameCatB) , plotnames.index(PlotnameCatC))
    divideHistos(ListOfHistoLists, plotnames.index(PlotnameCatB), plotnames.index(PlotnameCatD) )

    multiplyHistos(ListOfHistoLists, plotnames.index(PlotnameCatF) , plotnames.index(PlotnameCatG))
    divideHistos(ListOfHistoLists, plotnames.index(PlotnameCatF), plotnames.index(PlotnameCatH) )


def CloneListOfHistoLists(ListOfHistoLists):
    ClonedListOfHistoLists=[]
    for HistoList in ListOfHistoLists:
        ClonedHistoList=[]
        for Histo in HistoList:
            ClonedHistoList.append( Histo.Clone() )
        ClonedListOfHistoLists.append(ClonedHistoList)
    return ClonedListOfHistoLists


#Function designed to compare Entrys in Signal and BackgroundRegion, Only Use with transposed ListOfHistoLists
def compareEntriesInBackgroundAndSignalRegion( TransposedListsOfHistoLists, filename="set_filename.txt"):
    with open(filename, "w") as filecontent:
        filecontent.write("#List of Integrals in Signal and Background, constructed with function compareEntriesInBackgroundAndSignalRegion() in plotutils.py \n #NameOfHistogram;\tIntegral in Signalregion;\tIntegral in BackgroundRegion;\tRatio\n")


        #Loop over ListOfHistoLists and calculation of Integrals (Only for ABCD)
        for HistoList in TransposedListsOfHistoLists:
            for CurrentIndex,Histo in enumerate(HistoList):
                # filecontent.write("BUGFIX" + str(Histo.GetName()[8]) + "    " +str(Histo.GetName() + "\n") )
                if Histo.GetName()[22] == "A" or Histo.GetName()[23] == "A":
                    IntegralInSignalRegion=Histo.Integral()
                    IntegralInBackgroundRegion=0
                    for i in range(CurrentIndex+1,CurrentIndex+4):
                        IntegralInBackgroundRegion += HistoList[i].Integral()
                    filecontent.write(str(Histo.GetName()) + ";\t" + str(IntegralInSignalRegion) + ";\t" + str(IntegralInBackgroundRegion) + ";\t" + str( IntegralInSignalRegion / IntegralInBackgroundRegion)+ "\n" )

#InputHistoList should contain all Histograms that shold be in the same stack Plot
def stackPlotABCD(ListOfHistoList, name, optionlist=None , stacklist=None, colorlist=None, labellist=None, titlelist=None, Fill=True):

    if optionlist==None:
        optionlist = len(ListOfHistoList)*["histo"]
    if stacklist==None:
        stacklist = len(ListOfHistoList)*[True]
    if colorlist == None:
        colorlist = len(ListOfHistoList)*[kBlack]
        Fill=False
    if labellist == None:
        labellist = len(ListOfHistoList)*[" "]
    if titlelist == None:
        titlelist = len(ListOfHistoList)*[" "]
    # yTitle = "Not Set Yet"

    canvases=[]
    objects = []


    for HistoList,  yTitle in zip(ListOfHistoList, titlelist):
        for Histo, color, option, stack in zip(HistoList, colorlist, optionlist, stacklist):
            setupHisto(Histo,color,yTitle, stack)

        c=drawHistosOnCanvas(HistoList, normalize=True, stack=True, options_=option)
        c.cd(1)
        l=getLegend()
        for Histo, label in zip(HistoList, labellist):
            l.AddEntryZprime(Histo, label, 'L') #For Filld, Option propably "F"
            l.Draw("same")
        canvases.append(c)

    printCanvases(canvases,name)
    writeObjects(canvases,name)

def addLOLTtoLOLT(ListOfHistoLists1,ListOfHistoLists2, c1=1.0, c2=1.0):
    for HistoList1 in ListOfHistoLists1:
      for  HistoList2 in ListOfHistoLists2:
        for Histo1, Histo2, in zip(HistoList1,HistoList2):
            Histo1.Add(Histo2,c2)


def scalCatAclosurewithCatEclosure(histo1, histo2):
    #histo1.Scale(histo2.Integral()/(histo1.Integral()))
    histo1.Scale(histo2.Integral())
    

