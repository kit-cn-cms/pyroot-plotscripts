import ROOT
ROOT.gROOT.SetBatch(True)
import re
import numpy as np
debug=0
"""
===============================================
Class handling the Plotting
Contains the Name and the Histogram
label is for the legend naming
if color is not set uses dictionary defined here
OverUnderFlowInc as flag if Overflow and Underflow were already merged in the hist
Errorband should be all uncertainties
TODO: specific error band as list of error bands
===============================================
"""
class Plot:
    def __init__(self, hist, name, label = None, 
                    color=None, typ='bkg', OverUnderFlowInc=False, 
                    errorband=None, specificerrorband=None):
        self.hist=hist
        self.name=name
        self.label=label
        if not label:
            self.label=name
        self.color=color
        if not color:
            self.GetPlotColor
        self.typ=typ
        self.OverUnderFlowInc=OverUnderFlowInc
        self.errorband=errorband
        self.specificerrorband=specificerrorband
        if specificerrorband:
            if not isinstance(specificerrorband, list):
                self.specificerrorband=[specificerrorband]
            self.sebColor=[ROOT.kCyan,ROOT.kYellow, 
                                    ROOT.kMagenta,ROOT.kOrange,
                                    ROOT.kPink, ROOT.kViolet]
    # dictionary for colors
    def GetPlotColor(self ):
        color_dict = {
            "ttZ":          ROOT.kCyan,
            "ttH":          ROOT.kBlue+1,
            "ttlf":         ROOT.kRed-7,
            "ttcc":         ROOT.kRed+1,
            "ttbb":         ROOT.kRed+3,
            "tt2b":         ROOT.kRed+2,
            "ttb":          ROOT.kRed-2,
            "tthf":         ROOT.kRed-3,
            "ttbar":        ROOT.kOrange,
            "ttmergedb":    ROOT.kRed-1,
        
            "sig":   ROOT.kCyan,
            "bkg":   ROOT.kOrange,
            }
        cls=self.name
        if "ttZ" in cls: cls = "ttZ"
        if "ttH" in cls: cls = "ttH"
        self.color=color_dict[cls]

    # moves underflow in first histogram bin and overflow in last bin
    def handleOverUnderFlow(self):
        moveOverUnderFlow(self.hist)
        # set flag that over and underflow werde merged into the histogram
        self.OverUnderFlowInc=True

    # sets the Style for the Histogram and errorband
    def setStyle(self):
        self.hist.SetStats(False)
        #Sets style for Histogram, filled for background, line for signal
        if self.typ=="bkg":
            self.hist.SetLineColor(ROOT.kBlack )
            self.hist.SetFillColor(self.color)
            self.hist.SetLineWidth(1)
        elif self.typ=="signal":
            self.hist.SetLineColor(self.color )
            self.hist.SetFillColor(0)
            self.hist.SetLineWidth(3)
        else:
            print("ERROR! Type wrong!")
        #sets style for error band
        if self.errorband:
            self.errorband.SetFillStyle(3004)
            self.errorband.SetLineColor(ROOT.kBlack)
            self.errorband.SetFillColor(ROOT.kBlack)
        #sets style for error band
        if self.specificerrorband:
            for n,seb in enumerate(specificerrorband):
                seb.SetFillStyle(3004)
                seb.SetLineColor(self.sebColor[n])
                seb.SetFillColor(self.sebColor[n])

# moves underflow in first histogram bin and overflow in last bin
def moveOverUnderFlow(hist):
    # move underflow
    hist.SetBinContent(1, hist.GetBinContent(0)+hist.GetBinContent(1))
    # move overflow
    hist.SetBinContent(hist.GetNbinsX(), hist.GetBinContent(hist.GetNbinsX()+1)+hist.GetBinContent(hist.GetNbinsX()))

    # set underflow error
    hist.SetBinError(1, ROOT.TMath.Sqrt(
        ROOT.TMath.Power(hist.GetBinError(0),2) + ROOT.TMath.Power(hist.GetBinError(1),2) ))
    # set overflow error
    hist.SetBinError(hist.GetNbinsX(), ROOT.TMath.Sqrt(
        ROOT.TMath.Power(hist.GetBinError(hist.GetNbinsX()),2) + 
        ROOT.TMath.Power(hist.GetBinError(hist.GetNbinsX()+1),2) ))

# ===============================================
# GET HISTOGRAMS AND ERROR BANDS
# ===============================================

def buildHistogramAndErrorBand(rootFile,sample,color,typ,label,systematics,nominalKey,procIden,systematicKey,sysIden):
    print("new sample: "+str(sample))
    # replace keys to get histogram key
    if procIden in nominalKey:
        sampleKey = nominalKey.replace(procIden, sample)
    else:
        sampleKey=nominalKey
    rootHist = rootFile.Get(sampleKey)
    print("    type of hist is: "+str(type(rootHist)) )
    if not isinstance(rootHist, ROOT.TH1):
        return "ERROR"
    #moves underflow in the first and overflow in the last bin
    moveOverUnderFlow(rootHist)
    # replace keys to get systematic key
    print("    starting with systematics - building Errorband")
    if procIden in systematicKey:
        sampleSystKey = systematicKey.replace(procIden, sample)
    else:
        sampleSystKey = systematicKey
    #Lists for error band values
    upErrors=None
    downErrors=None
    """
    Loop over systematics to get Error band for sample
    """
    for systematic in systematics:
        """
        create empty Error Band for sample to fill 
        """
        if not upErrors and not downErrors:
            upErrors=[0]*rootHist.GetNbinsX()
            downErrors=[0]*rootHist.GetNbinsX()
        """
        Get Key for Sytematic (up and down variation)
        """
        if sysIden in sampleSystKey:
            sampleHistKey = sampleSystKey.replace(sysIden, systematic)
        else:
            sampleHistKey = sampleSystKey
        upname=sampleHistKey+"Up"
        up= rootFile.Get(upname)
        downname=sampleHistKey+"Down"
        down= rootFile.Get(downname)
        
        """
        check if histogram is TH1 type, else skip uncertainty
        """

        if isinstance(up, ROOT.TH1) and isinstance(down, ROOT.TH1):
            print  "    adding systematic ",systematic
            moveOverUnderFlow(up)
            moveOverUnderFlow(down)

            for ibin in range(0, rootHist.GetNbinsX()):
                # get up down variations
                u_=up[ibin+1]-rootHist[ibin+1]
                d_=down[ibin+1]-rootHist[ibin+1]
                 # set max as up and min as down
                u = max(u_,d_)
                d = min(u_,d_)
                # only consider positive up and negative down variations
                u = max(0.,u)
                d = min(0.,d)
                upErrors[ibin]=ROOT.TMath.Sqrt( upErrors[ibin]*upErrors[ibin] + u*u )
                downErrors[ibin] = ROOT.TMath.Sqrt( downErrors[ibin]*downErrors[ibin] + d*d)
            
            if debug>99:
                print "adding up/down ", u, d
                print "total up/down now: ", upErrors[ibin], downErrors[ibin]
                print "-"*50
        else:
            if debug>9:
                print("ERROR! can not use: "+str(systematic) )
                print("->type of up shape hist is: "+str(type(up)) )
                print("->type of down shape is: "+str(type(down)) )
            else:
                continue

    if upErrors:
        errorband = ROOT.TGraphAsymmErrors(rootHist)
        for i in range(len(upErrors)):
            errorband.SetPointEYlow(i, downErrors[i])
            errorband.SetPointEYhigh(i, upErrors[i])
            errorband.SetPointEXlow(i, rootHist.GetBinWidth(i+1)/2.)
            errorband.SetPointEXhigh(i, rootHist.GetBinWidth(i+1)/2.)
        PlotObject=Plot(rootHist,sample,label=label,
                                    color=color,typ=typ,
                                    errorband=errorband,OverUnderFlowInc=True)
    else:
        PlotObject=Plot(rootHist,sample,label=label,
                                    color=color,typ=typ,
                                    OverUnderFlowInc=True)
    return PlotObject

"""
Combine Output Style where Errorbands already exist
"""
def getHistogramAndErrorband(rootFile,sample,color,typ,label,nominalKey,procIden):
    print("new sample: "+str(sample))
    # replace keys to get histogram key
    if procIden in nominalKey:
        sampleKey = nominalKey.replace(procIden, sample)
    else:
        sampleKey=nominalKey
        print sample.Key
    rootHist = rootFile.Get(sampleKey)
    print("    type of hist is: "+str(type(rootHist)) )
    if not isinstance(rootHist, ROOT.TH1):
        return "ERROR"
    PlotObject=Plot(rootHist,sample,label=label,
                                    color=color,typ=typ,
                                    OverUnderFlowInc=True)

    return PlotObject

def GetErrorGraph(histo):
    error_graph = ROOT.TGraphAsymmErrors(histo)
    error_graph.SetFillStyle(3005)
    error_graph.SetFillColor(ROOT.kBlack)
    return error_graph

# combines other samples as it is defined in the input "sample"
# to create an clearer plot
# combines Histogram and Errorband and deletes other samples
def addSamples(sample,color,typ,label,addsamples,PlotList):
    combinedErrorbands=[]
    combinedHist = None
    print("Adding samples for summarized process %s" % sample)
    for sample in addsamples:
        print "    "+sample
        if combinedHist:
            combinedHist.Add(PlotList[sample].hist)
            combinedErrorbands.append(PlotList[sample].errorband)
            del PlotList[sample]
        else:
            combinedHist    = PlotList[sample].hist 
            combinedErrorbands.append(PlotList[sample].errorband)
            del PlotList[sample]
    # add all Errorbands together
    errorband=addErrorbands(combinedErrorbands,combinedHist)
    # add the new combined sample
    PlotList[sample]=Plot(combinedHist, sample, color=color, typ=typ, label=label, errorband=errorband)
    
    # return the altered PlotList
    return PlotList

# adding Errorbands with correlated option
def addErrorbands(combinedErrorbands,combinedHist,correlated=False):
    newErrorband = ROOT.TGraphAsymmErrors(combinedHist)
    for i in range (newErrorband.GetN()):
        up=0
        down=0
        for errorband in combinedErrorbands:
                if correlated:
                   up=up+errorband.GetErrorYhigh(i)
                   down=down+errorband.GetErrorYlow(i)
                else:
                    up=ROOT.TMath.Sqrt(up*up+errorband.GetErrorYhigh(i)*errorband.GetErrorYhigh(i))
                    down=ROOT.TMath.Sqrt(down*down+errorband.GetErrorYlow(i)*errorband.GetErrorYlow(i))
        newErrorband.SetPointEYlow(i, down)
        newErrorband.SetPointEYhigh(i, up)
        newErrorband.SetPointEXlow(i, combinedHist.GetBinWidth(i+1)/2.)
        newErrorband.SetPointEXhigh(i, combinedHist.GetBinWidth(i+1)/2.)
    return newErrorband


def moveOverUnderFlow(hist):
    # move underflow
    hist.SetBinContent(1, hist.GetBinContent(0)+hist.GetBinContent(1))
    # move overflow
    hist.SetBinContent(hist.GetNbinsX(), hist.GetBinContent(hist.GetNbinsX()+1)+hist.GetBinContent(hist.GetNbinsX()))

    # set underflow error
    hist.SetBinError(1, ROOT.TMath.Sqrt(
        ROOT.TMath.Power(hist.GetBinError(0),2) + ROOT.TMath.Power(hist.GetBinError(1),2) ))
    # set overflow error
    hist.SetBinError(hist.GetNbinsX(), ROOT.TMath.Sqrt(
        ROOT.TMath.Power(hist.GetBinError(hist.GetNbinsX()),2) + 
        ROOT.TMath.Power(hist.GetBinError(hist.GetNbinsX()+1),2) ))
    #delete overflow and underflow after moving
    hist.SetBinContent(0,0)
    hist.SetBinError(0,0)
    hist.SetBinContent(hist.GetNbinsX()+1,0)
    hist.SetBinError(hist.GetNbinsX()+1,0)

# converts the TGraphAsymmError data object in the mlfit file to a histogram (therby dropping bins again) and in addition sets asymmetric errors***
def GetHistoFromTGraphAE(tgraph,category,nbins_new):
    nbins_old = tgraph.GetN()
    # add category to name of histogram so each histogram has a different name to avoid problems with ROOT
    histo = ROOT.TH1F(process+category,process,nbins_new,0,nbins_new)
    # set this flag for asymmetric errors in data histogram
    histo.Sumw2(ROOT.kFALSE)
    # loop has to go from 0..nbins_new-1 for a tgraphasymmerror with nbins_new points
    for i in range(0,nbins_new,1):
        # first point (point 0) in tgraphae corresponds to first bin (bin 1 (0..1)) in histogram
        entries = tgraph.GetY()[i]
        for k in range(int(round(entries))):# rounding necessary if used with asimov dataset because entries can be non-integer in this case
            histo.Fill(i+0.5)
    # set this flag for calculation of asymmetric errors in data histogram
    histo.SetBinErrorOption(ROOT.TH1.kPoisson)
    return histo

#starting from the rigth side of the histogram, finds the bin number where the first time the bin content is smaller than 0.1*** 
def FindNewBinNumber(histo):
    nbins_old = histo.GetNbinsX()
    nbins_new = 0
    # loop starting from nbins_old to 1 with stepsize -1, so starting from the right side of a histogram
    for i in range(nbins_old,0,-1):
        # if the first bin with bin content > 0.1 is found, set this value as the new maximum bin number
        if histo.GetBinContent(i)>0.1:
            nbins_new = i
            break
    return nbins_new

"""
===============================================
Class handling the Drawing of the Histograms
===============================================
"""
class DrawHistograms:
    def __init__(self, PlotList, canvasName, data=None, ratio=False, signalscaling=1, 
                    errorband=None, displayname=None, logoption=False, 
                    normalize=False, combineflag=False):
        self.PlotList       = PlotList
        self.canvasName     = canvasName
        self.data           = data 
        self.ratio          = ratio 
        self.signalscaling  = signalscaling
        self.errorband      = errorband 
        self.displayname    = displayname 
        if not self.displayname:
            self.displayname = canvasName
        self.logoption      = logoption 
        self.normalize      = normalize 
        self.combineflag    = combineflag


    # ===============================================
    # DRAW HISTOGRAMS ON CANVAS
    # ===============================================

    def drawHistsOnCanvas(self):
        """
        set the Style for the Signal and Background Plots
        get the integral of the hists to sort it by event yield for plotting
        sort it by Event Yield, lowest to highest
        """
        sortPlots()

        """
        stack background Histograms
        add errorbands of background histograms to a list
        to combine them for the errorband of all backgrounds
        """
        stackPlots()

        """
        sort signal Histograms by Event Yield
        """
       
        sigHists = SortedShapeHistList(PlotList=PlotList,sortedPlots=sortedSignal)

        """
        figure out plotrange
        yMax is the maximum bin value of all background histograms
        yMinMax is the minimal bin value of all background histograms, 
        needed for logarithmic plotting (need to set lowest value)
        """
        yMax,yMinMax = PlotRange(sigHists,bkgHists)
        
        """
        get the first histogram to draw,
        use the first background histogram,
        else use an signal histogram
        """
        if len(bkgHists) == 0:
            firstHist = PlotList[sortedSignal[0]].hist
            ratio=False
            data=False
        else:
            firstHist = bkgHists[0]
        """
        create Canvas split in two if ratio is activated
        """
        canvas = getCanvas(canvasName, ratio)
        canvas.cd(1)


        """
        get the total background event yield
        to scale the signal
        and normalize the Plot 
        """
        firstHistIntegral=firstHist.Integral()
        if normalize:
            normalizefactor=1/firstHist.Integral()
            firstHist.Scale(normalizefactor)
            yMax    = yMax*normalizefactor
            yMinMax = yMinMax*normalizefactor

        """
        consider logoption and set the user range accordingly
        scaling maximal and minimal y value for better readability
        """
        if logoption:
            firstHist.GetYaxis().SetRangeUser(yMinMax/10000, yMax*1000)
            ROOT.gPad.SetLogy(1)
        else:
            firstHist.GetYaxis().SetRangeUser(0, yMax*1.5)
        
        
        firstHist.GetYaxis().SetTitle(GetyTitle(normalize))
        firstHist.GetYaxis().SetTitleSize(firstHist.GetYaxis().GetTitleSize()*1.2)
        #firstHist.GetYaxis().SetTitleOffset(0.5)
        canvaslabel=firstHist.GetTitle()
        if ratio:
            firstHist.GetXaxis().SetTitle("")
            firstHist.SetTitle("")
        else:
            firstHist.GetXaxis().SetTitle(canvaslabel)
            firstHist.SetTitle("")

        option = "histo"
        if bkgHists:
            firstHist.DrawCopy(option+"E0")
        else:
            firstHist.DrawCopy(option)
        """
        draw the other histograms and the errorband
        """
        for h in bkgHists[1:]:
            if normalize:
                h.Scale(normalizefactor)
            h.DrawCopy(option+"same")

        if errorband and combinederrorband:
            combinederrorband.SetFillStyle(3004)
            combinederrorband.SetLineColor(ROOT.kBlack)
            combinederrorband.SetFillColor(ROOT.kBlack)
            combinederrorband.Draw("same2")

        # draw data
        if data:
            data.SetLineColor(ROOT.kBlack)
            data.SetMarkerStyle(20)
            data.Draw("same2")

        canvas.cd(1)
        # redraw axis
        firstHist.DrawCopy("axissame")
        
        # draw signal histograms
        for n,signal in enumerate(sigHists):
            print sortedSignal[n]
            # scale signal
            if normalize:
                scalefactor=1/signal.Integral()
            elif signalscaling==-1:
                scalefactor=firstHistIntegral/signal.Integral()
            else:
                scalefactor=signalscaling
            signal.Scale(scalefactor)
            if scalefactor != 1 and not normalize:
                PlotList[sortedSignal[n]].label += " x "+str(int(scalefactor))
            # draw signal histogram
            signal.DrawCopy(option+" same")

        if ratio:
            canvas.cd(2)
            ratio(data=data, stackhist=firstHist,canvaslabel=canvaslabel)

        """
        return everything ROOT related,
        as well as the signal and background histogram list
        for labels
        """
        if ratio:
            return canvas, combinederrorband, ratioerrorband, sortedSignal, sigHists, sortedBackground, bkgHists, data, ratio
        else:
            return canvas, combinederrorband, False, sortedSignal, sigHists, sortedBackground, bkgHists, data, ratio

    def drawCombineHistsOnCanvas(self, PlotList, canvasName, data=None, ratio=False, 
                    signalscaling=1, errorband=None, displayname=None, logoption=False, normalize=False):
        if not displayname: 
            displayname = canvasName
            
        """
        set the Style for the Signal and Background Plots
        get the integral of the hists to sort it by event yield for plotting
        sort it by Event Yield, lowest to highest
        """
        sortedSignal, sortedBackground = sortPlots(PlotList=PlotList)

        """
        stack background Histograms
        add errorbands of background histograms to a list
        to combine them for the errorband of all backgrounds
        """
        
        bkgHists, combinederrorband = stackPlots(PlotList=PlotList,sortedPlots=sortedBackground,combineflag=True)

        """
        sort signal Histograms by Event Yield
        """
        sigHists = SortedShapeHistList(PlotList=PlotList,sortedPlots=sortedSignal,combineflag=True)

        """
        figure out plotrange
        yMax is the maximum bin value of all background histograms
        yMinMax is the minimal bin value of all background histograms, 
        needed for logarithmic plotting (need to set lowest value)
        """
        yMax,yMinMax = PlotRange(sigHists,bkgHists)

        """
        get the first histogram to draw,
        use the first background histogram,
        else use an signal histogram
        """
        firstHist = bkgHists[0]
        """
        create Canvas split in two if ratio is activated
        """
        canvas = getCanvas(canvasName, ratio)
        canvas.cd(1)

        """
        get the total background event yield
        to scale the signal
        and normalize the Plot 
        """
        firstHistIntegral=firstHist.Integral()
        if normalize:
            normalizefactor, yMax, yMinMax = normalizePlot(PlotHist=firstHist,yMax=yMax,yMinMax=yMinMax)

        """
        consider logoption and set the user range accordingly
        scaling maximal and minimal y value for better readability
        """
        if logoption:
            firstHist.GetYaxis().SetRangeUser(yMinMax/10000, yMax*1000)
            ROOT.gPad.SetLogy(1)
        else:
            firstHist.GetYaxis().SetRangeUser(0, yMax*1.5)
        
        
        firstHist.GetYaxis().SetTitle(GetyTitle(normalize))
        firstHist.GetYaxis().SetTitleSize(firstHist.GetYaxis().GetTitleSize()*1.2)
        #firstHist.GetYaxis().SetTitleOffset(0.5)
        canvaslabel=firstHist.GetTitle()
        if ratio:
            firstHist.GetXaxis().SetTitle("")
            firstHist.SetTitle("")
        else:
            firstHist.GetXaxis().SetTitle(canvaslabel)
            firstHist.SetTitle("")

        option = "histo"
        if bkgHists:
            firstHist.DrawCopy(option+"E0")
        else:
            firstHist.DrawCopy(option)
        """
        draw the other histograms and the errorband
        """
        for h in bkgHists[1:]:
            if normalize:
                h.Scale(normalizefactor)
            h.DrawCopy(option+"same")

        if errorband:
            combinederrorband.SetFillStyle(3004)
            combinederrorband.SetLineColor(ROOT.kBlack)
            combinederrorband.SetFillColor(ROOT.kBlack)
            combinederrorband.Draw("same2")

        # draw data
        if data:
            data.SetLineColor(ROOT.kBlack)
            data.SetMarkerStyle(20)
            data.Draw("same2")

        canvas.cd(1)
        # redraw axis
        firstHist.DrawCopy("axissame")

        if ratio:
            canvas.cd(2)
            ratio(data=data, stackhist=firstHist,canvaslabel=canvaslabel)

        """
        return everything ROOT related,
        as well as the signal and background histogram list
        for labels
        """
        if ratio:
            return canvas, combinederrorband, ratioerrorband, sortedSignal, sigHists, sortedBackground, bkgHists, data, ratio
        else:
            return canvas, combinederrorband, False, sortedSignal, sigHists, sortedBackground, bkgHists, data, ratio

    def sortPlots(self):
          """
        set the Style for the Signal and Background Plots
        get the integral of the hists to sort it by event yield for plotting
        """
        Signal      = {}
        Background  = {}
        for sample in self.PlotList:
            PlotObject=self.PlotList[sample]
            PlotObject.setStyle()
            if PlotObject.typ == "signal":
                Signal[PlotObject.name] = PlotObject.hist.Integral()
            elif PlotObject.typ == "bkg":
                Background[PlotObject.name] = PlotObject.hist.Integral()
        """
        sort it by Event Yield, lowest to highest
        """
        self.sortedSignal        = sorted(Signal, key=Signal.get, reverse=True)
        self.sortedBackground    = sorted(Background, key=Background.get,reverse=True)

    def stackPlots(self):
        """
        stack background Histograms
        if not combine style of rootfile
        add errorbands of background histograms to a list
        to combine them for the errorband of all backgrounds
        """
        self.errorbands         = []
        self.stackPlots         = []
        self.combinederrorband  = None
        for i in range(len(self.sortedPlots),0,-1):
            Plot        = self.sortedPlots[i-1]
            PlotObject  = self.PlotList[Plot]
            if len(stackPlots)==0:
                self.stackPlots.append(PlotObject.hist.Clone())
                if not self.combineflag:
                    self.errorbands.append(PlotObject.errorband.Clone())
            else:
                hist = PlotObject.hist.Clone()
                hist.Add(stackPlots[0])
                self.stackPlots.insert(0, hist)
                if not self.combineflag:
                    self.errorbands.append(PlotObject.errorband.Clone())
        if stackPlots and not combineflag:
            self.combinederrorband=addErrorbands(errorbands,stackPlots[0])

    def SortedShapeHistList(self):
        """
        sort Shape Histograms by Event Yield
        """
        sigHists=[]
        if len(self.sortedSignal)==1 and self.combineflag:
            PlotObject = self.PlotList["total_signal"]
            sigHists.append(PlotObject.hist.Clone())
        else:
            for signal in self.sortedSignal:
                PlotObject = self.PlotList[signal]
                sigHists.append(PlotObject.hist.Clone())

    def PlotRange(sigHists,bkgHists):
        """
        figure out plotrange
        yMax is the maximum bin value of all background histograms
        yMinMax is the minimal bin value of all background histograms, 
        needed for logarithmic plotting (need to set lowest value)
        """
        yMax = 1e-9
        yMinMax = 1000.
        for hist in bkgHists:
            yMax = max(hist.GetBinContent(h.GetMaximumBin()), yMax)
            if hist.GetBinContent(hist.GetMaximumBin()) > 0:
                yMinMax = min(hist.GetBinContent(h.GetMaximumBin()), yMinMax)
        for hist in sigHists:
            yMax = max(hist.GetBinContent(h.GetMaximumBin()), yMax)
            if hist.GetBinContent(hist.GetMaximumBin()) > 0:
                yMinMax = min(hist.GetBinContent(h.GetMaximumBin()), yMinMax)

        return yMax,yMinMax

    def normalizePlot(PlotHist,yMax,yMinMax):

        """
        to normalize the Plot 
        """
        normalizefactor=1/PlotHist.Integral()
        PlotHist.Scale(normalizefactor)
        yMax    = yMax*normalizefactor
        yMinMax = yMinMax*normalizefactor

        return normalizefactor, yMax, yMinMax


    def ratio(data,stackhist,canvaslabel=None):
        """
        Draws the ratio plot, scales the background, signal and errorband to the background
        """
        
        line = data.Clone()
        line.Divide(data)
        line.GetYaxis().SetRangeUser(0.5,1.5)
        line.GetYaxis().SetTitle(ratio)

        line.SetTitle("")

        line.GetXaxis().SetLabelSize(line.GetXaxis().GetLabelSize()*2.4)
        line.GetYaxis().SetLabelSize(line.GetYaxis().GetLabelSize()*2.2)
        line.GetXaxis().SetTitle(canvaslabel)

        line.GetXaxis().SetTitleSize(line.GetXaxis().GetTitleSize()*3)
        line.GetYaxis().SetTitleSize(line.GetYaxis().GetTitleSize()*2.5)

        line.GetYaxis().SetTitleOffset(0.5)
        line.GetYaxis().SetNdivisions(505)
        for i in range(line.GetNbinsX()+1):
            line.SetBinContent(i, 1)
            line.SetBinError(i, 1)
        line.SetLineWidth(1)
        line.SetLineColor(ROOT.kBlack)
        line.DrawCopy("histo")
        # ratio plot
        ratioPlot = data.Clone()
        ratioPlot.Divide(stackhist)
        ratioPlot.SetTitle(stackhist.GetTitle())
        ratioPlot.SetLineColor(ROOT.kBlack)
        ratioPlot.SetLineWidth(1)
        ratioPlot.SetMarkerStyle(20)
        ROOT.gStyle.SetErrorX(0)
        ratioPlot.DrawCopy("sameP")

        ratioerrorband=generateRatioErrorband(combinederrorband)
        ratioerrorband.Draw("same2")
        canvas.cd(1)

    # scales the Errorband for the ratio plot
    def generateRatioErrorband(errorband):
        ratioerrorband=errorband.Clone()
        for i in range(ratioerrorband.GetN()):
            x=ROOT.Double()
            y=ROOT.Double()
            ratioerrorband.GetPoint(i,x,y)
            ratioerrorband.SetPoint(i,x,1)
            if y>0.:
                ratioerrorband.SetPointEYlow(i,ratioerrorband.GetErrorYlow(i)/y)
                ratioerrorband.SetPointEYhigh(i,ratioerrorband.GetErrorYhigh(i)/y)
            else:
                ratioerrorband.SetPointEYlow(i,0)
                ratioerrorband.SetPointEYhigh(i,0)

        return ratioerrorband
        
    def GetyTitle(normalize = False):
        # if privateWork flag is enabled, normalize plots to unit area
        if normalize:
            return "normalized to unit area"
        return "Events expected"

# ===============================================
# GENERATE CANVAS AND LEGENDS
# ===============================================
def getCanvas(name, ratiopad = False):
    if ratiopad:
        canvas = ROOT.TCanvas(name, name, 1024, 1024)
        canvas.Divide(1,2)
        canvas.cd(1).SetPad(0.,0.3,1.0,1.0)
        canvas.cd(1).SetTopMargin(0.07)
        canvas.cd(1).SetBottomMargin(0.0)

        canvas.cd(2).SetPad(0.,0.0,1.0,0.3)
        canvas.cd(2).SetTopMargin(0.0)
        canvas.cd(2).SetBottomMargin(0.4)

        canvas.cd(1).SetRightMargin(0.05)
        canvas.cd(1).SetLeftMargin(0.15)
        canvas.cd(1).SetTicks(1,1)

        canvas.cd(2).SetRightMargin(0.05)
        canvas.cd(2).SetLeftMargin(0.15)
        canvas.cd(2).SetTicks(1,1)
    else:
        canvas = ROOT.TCanvas(name, name, 1024, 768)
        canvas.SetTopMargin(0.07)
        canvas.SetBottomMargin(0.15)
        canvas.SetRightMargin(0.05)
        canvas.SetLeftMargin(0.15)
        canvas.SetTicks(1,1)

    return canvas

def getLegend():
    legend=ROOT.TLegend(0.70,0.6,0.95,0.9)
    legend.SetBorderSize(0);
    legend.SetLineStyle(0);
    legend.SetTextFont(42);
    legend.SetTextSize(0.03);
    legend.SetFillStyle(0);
    return legend

def getLegend1():
    legend=ROOT.TLegend(0.65,0.7,0.8,0.9)
    legend.SetBorderSize(0);
    legend.SetLineStyle(0);
    legend.SetTextFont(42);
    legend.SetTextSize(0.03);
    legend.SetFillStyle(0);
    return legend

def getLegend2():
    legend=ROOT.TLegend(0.8,0.7,0.95,0.9)
    legend.SetBorderSize(0);
    legend.SetLineStyle(0);
    legend.SetTextFont(42);
    legend.SetTextSize(0.03);
    legend.SetFillStyle(0);
    return legend

def saveCanvas(canvas, path):
    canvas.SaveAs(path)
    canvas.SaveAs(path.replace(".pdf",".png"))
    canvas.Clear()


# ===============================================
# PRINT STUFF ON CANVAS
# ===============================================
def printLumi(pad, lumi = 41.5, ratio = False, twoDim = False):
    if lumi == 0.: return

    lumi_text = str(lumi)+" fb^{-1} (13 TeV)"

    pad.cd(1)
    l = pad.GetLeftMargin()
    t = pad.GetTopMargin()
    r = pad.GetRightMargin()
    b = pad.GetBottomMargin()

    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextColor(ROOT.kBlack)
    
    if twoDim:  latex.DrawLatex(l+0.40,1.-t+0.01,lumi_text)
    elif ratio: latex.DrawLatex(l+0.60,1.-t+0.04,lumi_text)
    else:       latex.DrawLatex(l+0.53,1.-t+0.02,lumi_text)

def printCategoryLabel(pad, catLabel, ratio = False):
    pad.cd(1)
    l = pad.GetLeftMargin()
    t = pad.GetTopMargin()
    r = pad.GetRightMargin()
    b = pad.GetBottomMargin()

    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextColor(ROOT.kBlack)

    if ratio:   latex.DrawLatex(l+0.07,1.-t-0.04, catLabel)
    else:       latex.DrawLatex(l+0.02,1.-t-0.06, catLabel)

def printPrivateWork(pad, ratio = False, twoDim = False, nodePlot = False):
    pad.cd(1) 
    l = pad.GetLeftMargin() 
    t = pad.GetTopMargin() 
    r = pad.GetRightMargin() 
    b = pad.GetBottomMargin() 
 
    latex = ROOT.TLatex() 
    latex.SetNDC() 
    latex.SetTextColor(ROOT.kBlack) 
    latex.SetTextSize(0.04)

    text = "CMS private work" 

    if nodePlot:    latex.DrawLatex(l+0.57,1.-t+0.01, text)
    elif twoDim:    latex.DrawLatex(l+0.39,1.-t+0.01, text)
    elif ratio:     latex.DrawLatex(l+0.05,1.-t+0.04, text) 
    else:           latex.DrawLatex(l,1.-t+0.01, text)
