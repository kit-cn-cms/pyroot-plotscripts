import ROOT
import math
from itertools import product
from collections import namedtuple
import glob
import subprocess
import os
import scriptgenerator
import re


ROOT.gStyle.SetPaintTextFormat("4.2f");
ROOT.gROOT.SetBatch(True)

class Sample:
    def __init__(self,name, color=ROOT.kBlack, path='', selection='',nick='',checknevents=-1,treename='MVATree'):
        self.name=name
        self.color=color
        self.path=path
        self.selection=selection
        self.files=glob.glob(path)
        if path!='' and len(self.files)==0:
            print 'no files found at',path    
        if nick=='':
            self.nick=name
        else:
            self.nick=nick
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
    def __init__(self,histo, variable='', selection=''):
        self.histo=histo
        if variable=='':
            self.variable=histo.GetName()
        else:
            self.variable=variable
        self.selection=selection
        self.name=histo.GetName()

class MVAPlot:
    def __init__(self,histo, weightfile, selection=''):
        self.histo=histo
        self.weightfile=weightfile
        self.selection=selection
        self.name=histo.GetName()
    def parseWeights(weightfile):
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


# sets up the style of a histo and its axes
def setupHisto(histo,color,yTitle=None,filled=False):
    if isinstance(histo,ROOT.TH1):
        histo.SetStats(False)
    if histo.GetTitle()!='':
        histo.GetXaxis().SetTitle(histo.GetTitle())
        histo.SetTitle('')
    if yTitle!=None:
        histo.GetYaxis().SetTitle(yTitle)
    histo.GetYaxis().SetTitleOffset(1.3)
    histo.GetXaxis().SetTitleOffset(1.2)
    histo.GetYaxis().SetTitleSize(0.05)
    histo.GetXaxis().SetTitleSize(0.05)
    histo.GetYaxis().SetLabelSize(0.05)
    histo.GetXaxis().SetLabelSize(0.05)
    if filled:
        histo.SetLineColor( ROOT.kBlack )
        histo.SetFillColor( color )
        histo.SetLineWidth(2)
    else:
        histo.SetLineColor(color)
        histo.SetLineWidth(2)

# creates a canvas either with or without ratiopad
def getCanvas(name,ratiopad=False):
    if ratiopad:
        c=ROOT.TCanvas(name,name,1024,1024)
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
        c=ROOT.TCanvas(name,name,1024,768)
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
    legend.SetTextSize(0.05);
    legend.SetFillStyle(0);
    return legend

# returns tlatex item with results of chi2 and KS test between two histograms
def getStatTests(h1,h2,option="WW"):
    ksprob = h1.KolmogorovTest(h2)
    chi2prob = h1.Chi2Test(h2,option)
    tests = ROOT.TLatex(0.2, 0.85, '#splitline{p(KS): '+str(round(ksprob,3))+'}{p(chi2): '+str(round(chi2prob,3))+'}'  );
    tests.SetTextFont(42);
    tests.SetTextSize(0.05);
    tests.SetNDC()
    return tests

# calculates separation of two histogram (using the ROC integral of)
def getSepaTests(h1,h2):
    pair=getSuperHistoPair([h1],[h2],'tmp')
    roc=getROC(*pair)
    rocint=roc.Integral()+0.5
    tests = ROOT.TLatex(0.2, 0.9, 'ROC integral: '+str(round(rocint,3)));
    tests.SetTextFont(42);
    tests.SetTextSize(0.05);
    tests.SetNDC()
    return tests


# draws a list of histos on a canvas and returns canvas
def drawHistosOnCanvas(listOfHistos_,normalize=True,stack=False,logscale=False,options_='histo',ratio=False):
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
        h.GetYaxis().SetRangeUser(0,yMax*1.3)
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
    canvas=canvases[0]
    canvas.Print(name+'.pdf[')
    for c in canvases:
        canvas=c
        canvas.Print(name+'.pdf')
        
    canvas.Print(name+'.pdf]')

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

def createHistoLists_fromSuperHistoFile(path,samples,plots,rebin=1,catnames=[""]):
    listOfHistoListsT=[]
    f=ROOT.TFile(path, "readonly")
    keyList = f.GetKeyNames()
    for sample in samples:
        histoList=[]
        ROOT.gDirectory.cd('PyROOT:/')
        for c in catnames:
            for plot in plots:
                key=sample.nick+'_'+c+plot.name
                print key, sample.nick, c, plot.name
                o=f.Get(key)
                print o
                if isinstance(o,ROOT.TH1) and not isinstance(o,ROOT.TH2): 
                    o.Rebin(rebin)
                    histoList.append(o.Clone())
                    print "ok", histoList[-1], len(histoList)
        listOfHistoListsT.append(histoList)
    listOfHistoLists=transposeLOL(listOfHistoListsT)
    return listOfHistoLists

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
def writeListOfHistoLists(listOfHistoLists,samples, label,name,normalize=True,stack=False,logscale=False,options='histo',statTest=False, sepaTest=False,ratio=False):
    if isinstance(label, basestring):
        labeltexts=len(listOfHistoLists)*[label]
        print "bla"
    else:
        labeltexts=label
    canvases=[]
    objects=[]   
    i=0
    print labeltexts
    for listOfHistos, labeltext in zip(listOfHistoLists, labeltexts):
        i+=1
        for histo,sample in zip(listOfHistos,samples):
            print labeltext
            yTitle='Events'
            if normalize:
                yTitle='normalized'
            setupHisto(histo,sample.color,yTitle,stack)        
        c=drawHistosOnCanvas(listOfHistos,normalize,stack,logscale,options,ratio)
        c.SetName('c'+str(i))
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

        lumi = ROOT.TLatex(0.2, 0.89, '2.46 fb^{-1} @ 13 TeV'  );
        lumi.SetTextFont(42)
        lumi.SetTextSize(0.06)
        lumi.SetNDC()
        lumi.Draw()
        objects.append(lumi)

        label = ROOT.TLatex(0.2, 0.83, labeltext);
        label.SetTextFont(42)
        label.SetTextSize(0.06)
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
            graph.Draw('ALP')
            first=False
        else:
            graph.Draw('LP')
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
        print i, histo1.GetBinLowEdge(i), eff1
        eff.SetPoint(point,histo1.GetBinLowEdge(i),eff1)
        point+=1
    print "###"
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

def turn1dHistoToRow(h,witherror=True):
    s=""
    for i in range(1,h.GetNbinsX()+1):
        s+="%.2f" % h.GetBinContent(i)
        if witherror:
            s+=" $\pm$ "
            s+="%.2f" % h.GetBinError(i)
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
        out.write(root2latex(s.name) + " & " + turn1dHistoToRow(h)+ "\\\\ \n") 
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

    

def getDataGraph(listOfHistosData):
    if len(listOfHistosData)>0:
        datahisto=listOfHistosData[0]
    for d in listOfHistosData[1:]:
        datahisto.Add(d)
    moveOverFlow(datahisto)
    data=ROOT.TGraphAsymmErrors(datahisto)
    data.SetMarkerStyle(20)
    data.SetMarkerColor(ROOT.kBlack)
    data.SetLineColor(ROOT.kBlack)
    for i in range(0,data.GetN()):
        data.SetPointEXlow(i,0)
        data.SetPointEXhigh(i,0)
    return data
    # TODO: proper y-errors

def getRatioGraph(data,mchisto):
    ratio=data.Clone()
    x, y = ROOT.Double(0), ROOT.Double(0)
    for i in range(0,data.GetN()):
        data.GetPoint(i,x,y)
        if mchisto.GetBinContent(i+1)>0:
            ratio.SetPoint(i,x,y/mchisto.GetBinContent(i+1))
        else:
            ratio.SetPoint(i,x,0)
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
    return ratio




def plotDataMC(listOfHistoListsData,listOfHistoLists,samples,name,logscale=False,label='',ratio=True,options='histo'):    
    if isinstance(label, basestring):
        labeltexts=len(listOfHistoListsData)*[label]
    else:
        labeltexts=label
    canvases=[]
    objects=[]   
    i=0
    print len(listOfHistoLists)
    # for every plot, look at all samples
    for listOfHistos,listOfHistosData,labeltext in zip(listOfHistoLists,listOfHistoListsData,labeltexts):
        i+=1
        print i
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
        lumi.Draw()
        objects.append(lumi)

        label = ROOT.TLatex(0.2, 0.83, labeltext);
        label.SetTextFont(42)
        label.SetTextSize(0.06)
        label.SetNDC()
        label.Draw()
        objects.append(label)


        ratiograph=getRatioGraph(data,stackedListOfHistos[0])
        canvas.cd(2)
        line=listOfHistos[0].Clone()
        line.SetFillStyle(0)
        line.Divide(listOfHistos[0])
        line.GetYaxis().SetRangeUser(0.5,1.6)
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



    print len(canvases)
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
          print len(w)
          print i, len(w[i-1])
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
        ratioerrorgraph.SetFillStyle(3154)
        ratioerrorgraph.SetLineColor(ROOT.kBlack)
        ratioerrorgraph.SetFillColor(ROOT.kBlack)

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
        lumi.Draw()
        objects.append(lumi)

        label = ROOT.TLatex(0.2, 0.83, labeltext);
        label.SetTextFont(42)
        label.SetTextSize(0.06)
        label.SetNDC()
        label.Draw()
        objects.append(label)


        ratiograph=getRatioGraph(data,stackedListOfHistos[0])
        canvas.cd(2)
        line=listOfHistos[0].Clone()
        line.SetFillStyle(0)
        line.Divide(listOfHistos[0])
        line.GetYaxis().SetRangeUser(0.5,1.6)
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



def writeLOLAndOneOnTop(listOfHistoLists,samples,listOfhistosOnTop,sampleOnTop,factor,name,logscale=False,options='histo'):
    normalize=False
    stack=True,
    canvases=[]
    objects=[]   
    i=0
    for listOfHistos,ot in zip(listOfHistoLists,listOfhistosOnTop):
        i+=1
        for histo,sample in zip(listOfHistos,samples):
            yTitle='Events expected for 2.46 fb^{-1} @ 13 TeV'
            setupHisto(histo,sample.color,yTitle,stack)        
        c=drawHistosOnCanvas(listOfHistos,normalize,stack,logscale,options)       
        c.SetName('c'+str(i))
        c.cd()
        otc=ot.Clone()
        otc.Scale(factor)
        setupHisto(otc,sampleOnTop.color,'',False)
        otc.DrawCopy("samehisto")
        l=getLegend()
        l.AddEntry2(otc,sampleOnTop.name+' x '+str(factor),'L')
        for h,sample in zip(listOfHistos,samples):
            loption='L'
            if stack:
                loption='F'
            l.AddEntry2(h,sample.name,loption)
        canvases.append(c)
        l.Draw('same')
        objects.append(l)
        objects.append(otc)
#        cms = ROOT.TLatex(0.2, 0.96, 'CMS private work'  );
#        cms = ROOT.TLatex(0.18, 0.85, '#splitline{CMS simulation}{WORK IN PROGRESS}'  );
#        cms.SetTextFont(42)
#        cms.SetTextSize(0.065)
#        cms.SetNDC()
#        cms.Draw()
#        objects.append(cms)


    printCanvases(canvases,name)
    writeObjects(canvases,name)

def eventYields(hl_data,hl_mc,samples,tablename):
    h_data=hl_data[0].Clone()
    for h in hl_data[1:]:
        h_data.Add(h)
    s_data=Sample('data')
    turn1dHistosToTable(hl_mc+[h_data],samples+[s_data],tablename)
    command=['pdflatex',tablename+'.tex']
    subprocess.call(command)
