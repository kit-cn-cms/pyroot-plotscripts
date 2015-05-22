import ROOT
import math
from itertools import product
from collections import namedtuple

Sample = namedtuple("Sample", "name color path selection")
Plot = namedtuple("Plot", "histo variable selection")

# sets up the style of a histo and its axes. options for data and stackplots will follow.
def setupHisto(histo,color):
    if isinstance(histo,ROOT.TH1):
        histo.SetStats(False)
    histo.GetXaxis().SetTitle(histo.GetTitle())
    histo.SetTitle('')
    histo.GetYaxis().SetTitle('normalized')
    histo.GetYaxis().SetTitleOffset(1.3)
    histo.GetYaxis().SetTitleSize(0.05)
    histo.GetXaxis().SetTitleSize(0.05)
    histo.GetYaxis().SetLabelSize(0.05)
    histo.GetXaxis().SetLabelSize(0.05)
    histo.SetLineColor(color)
    histo.SetLineWidth(3)

# creates canvas. option to add ratiopad will follow
def getCanvas(name):
    c=ROOT.TCanvas(name,name,1000,800)
    c.SetRightMargin(0.05)
    c.SetTopMargin(0.05)
    c.SetLeftMargin(0.15)
    c.SetBottomMargin(0.12)
    return c

# creates legend
def getLegend(): 
    legend=ROOT.TLegend()
    legend.SetX1NDC(0.65)
    legend.SetX2NDC(0.93)
    legend.SetY1NDC(0.75)
    legend.SetY2NDC(0.93)
    legend.SetBorderSize(0);
    legend.SetLineStyle(0);
    legend.SetTextFont(42);
    legend.SetTextSize(0.05);
    legend.SetFillStyle(0);
    return legend

def getStatTests(h1,h2):
    ksprob = h1.KolmogorovTest(h2)
    chi2prob = h1.Chi2Test(h2)
    print ksprob,chi2prob
    tests = ROOT.TLatex(0.2, 0.9, 'p(KS): '+str(round(ksprob,3))+', p(chi2): '+str(round(chi2prob,3))  );
    tests.SetTextFont(42);
    tests.SetTextSize(0.05);
    tests.SetNDC()
    return tests


# draws a list of histos on a canvas and returns canvas. options for stackplots, ratioplot, etc will be implemented soon
def drawHistosOnCanvas(listOfHistos_,normalize=True,options_='histo'):
    listOfHistos=[h.Clone(h.GetName()+'_drawclone') for h in listOfHistos_]
    canvas=getCanvas(listOfHistos[0].GetName())        
    #prepare drawing
    if normalize:
        for h in listOfHistos:
            if h.Integral()>0.:
                h.Scale(1./h.Integral())
    yMax=1e-9
    for h in listOfHistos:
        h.SetBinContent(1,h.GetBinContent(0)+h.GetBinContent(1));
        h.SetBinContent(h.GetNbinsX(),h.GetBinContent(h.GetNbinsX()+1)+h.GetBinContent(h.GetNbinsX()));
        h.SetBinError(1,ROOT.TMath.Sqrt(ROOT.TMath.Power(h.GetBinError(0),2)+ROOT.TMath.Power(h.GetBinError(1),2)));
        h.SetBinError(h.GetNbinsX(),ROOT.TMath.Sqrt(ROOT.TMath.Power(h.GetBinError(h.GetNbinsX()+1),2)+ROOT.TMath.Power(h.GetBinError(h.GetNbinsX()),2)));
        yMax=max(h.GetBinContent(h.GetMaximumBin()),yMax)

    #draw first
    h=listOfHistos[0]
    h.GetYaxis().SetRangeUser(0,yMax*1.3)
    option='histo'
    option+=options_
    h.DrawCopy(option)
    #draw remaining
    for h in listOfHistos[1:]:
        h.DrawCopy(option+'same')
    h.DrawCopy('axissame')
    return canvas

# writes canvases to pdf 
def printCanvases(canvases,name):
    canvas=getCanvas('canvas')
    canvas.Print(name+'.pdf[')
    for c in canvases:
        canvas=c
        canvas.Print(name+'.pdf')
        
    canvas.Print(name+'.pdf]')

# writes canvases to root file 
def writeCanvases(canvases,name):
    outfile=ROOT.TFile(name+'.root','recreate')
    for c in canvases:
        c.Write()

# for a list of booked plots trees are opened and the histograms are filled using the TTree::Project function
def createHistoLists_fromTree(plots,samples,treename):    
    listOfhistoLists=[]
    for plot in plots:
        histoList=[]
        for sample in samples:
            h=plot.histo.Clone()
            h.Sumw2()
            h.SetName(h.GetName()+'_'+sample.name)
#            setupHisto(h,sample.color)
            histoList.append(h)
        listOfhistoLists.append(histoList)

    for sample in samples:
        f=ROOT.TFile(sample.path, "readonly")
        tree = f.Get(treename)
        ROOT.gDirectory.cd('PyROOT:/')
        for plot in plots:
            ss='('+sample.selection+')'
            if sample.selection == '':
                ss='1'
            ps='('+plot.selection+')'
            if plot.selection == '':
                ps='1'
            tree.Project(plot.histo.GetName()+'_'+sample.name,plot.variable,ps+'&&'+ss)

    return listOfhistoLists

def transposeLOL(lol):
    return [list(x) for x  in zip(*lol)]

def GetKeyNames( self, dir = "" ):
        self.cd(dir)
        return [key.GetName() for key in ROOT.gDirectory.GetListOfKeys()]
ROOT.TFile.GetKeyNames = GetKeyNames


def createHistoLists_fromHistoFile(samples):
    listOfhistoListsT=[]
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
            if isinstance(o,ROOT.TH1):                
                histoList.append(o.Clone())
                histoList[-1].SetName(o.GetName()+'_'+sample.name)
        listOfhistoListsT.append(histoList)
    listOfhistoLists=transposeLOL(listOfhistoListsT)
    return listOfhistoLists

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
def writeListOfhistoLists(listOfhistoLists,samples,name,normalize=True,options='histo',statTest=False):
    canvases=[]
    objects=[]   
    i=0
    for listOfHistos in listOfhistoLists:
        i+=1
        for histo,sample in zip(listOfHistos,samples):
            setupHisto(histo,sample.color)        
        c=drawHistosOnCanvas(listOfHistos,normalize,options)
        c.SetName('c'+str(i))
        l=getLegend()
        for h,sample in zip(listOfHistos,samples):
            l.AddEntry(h,sample.name,'l')
        canvases.append(c)
        l.Draw('same')
        objects.append(l)
        if statTest:
            tests=getStatTests(listOfHistos[0],listOfHistos[1])
            tests.Draw()
            objects.append(tests)


    printCanvases(canvases,name)
    writeCanvases(canvases,name)

def writeListOfROCs(graphs,names,colors,filename):
    c=getCanvas('ROC')
    l=getLegend()
    first=True
    for graph,name,color in zip(graphs,names,colors):
        l.AddEntry(graph,name,'l')
        if first:
            graph.Draw('ALP')
            first=False
        else:
            graph.Draw('LP')
        setupHisto(graph,color)
        graph.GetXaxis().SetTitle('Signal efficiency')
        graph.GetYaxis().SetTitle('Background rejection')
        graph.SetMarkerStyle(20)
    l.Draw('same')
    printCanvases([c],filename)
    writeCanvases([c],filename)


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
def getROC(histo1,histo2):
    nBins=histo1.GetNbinsX()
    nBins2=histo2.GetNbinsX()
    integral1=histo1.Integral(0,nBins+1)
    integral2=histo2.Integral(0,nBins2+1)

    nonZeroBins=[]
    for i in range(nBins,-1,-1):
        if histo1.GetBinContent(i)>0. or histo1.GetBinContent(i)>0.:
            nonZeroBins.append(i)           

    roc = ROOT.TGraphAsymmErrors(len(nonZeroBins)+1)
    roc.SetPoint(0,0,1)
    point=1
    for i in nonZeroBins:
        eff1=histo1.Integral(i,nBins)/integral1
        eff2=histo2.Integral(i,nBins)/integral2
        roc.SetPoint(point,eff1,1-eff2)
        point+=1
    
    return roc
