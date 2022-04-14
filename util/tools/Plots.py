import ROOT
ROOT.gROOT.SetBatch(True)
import re
import numpy as np
from array import array
import sys
debug=10
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
        if debug > 5:
            print("input hist in Plot class: ")
            print(hist)
        self.hist=hist
        self.name=name
        self.label=label
        if not label:
            self.label=name
        if not color:
            self.GetPlotColor()
        else:
            self.color=color
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
        
            "sig":          601,
            "total_signal": 601,
            "bkg":          ROOT.kOrange,
            }
        cls = self.name
        if "ttZ" in cls: cls = "ttZ"
        if "ttH" in cls: cls = "ttH"
        self.color = color_dict[cls]

    # moves underflow in first histogram bin and overflow in last bin
    def handleOverUnderFlow(self):
        moveOverUnderFlow(self.hist)
        # set flag that over and underflow werde merged into the histogram
        self.OverUnderFlowInc=True

    # sets the Style for the Histogram and errorband
    def setStyle(self, typ=None):
        if not typ:
            typ = self.typ
        self.hist.SetStats(False)
        #Sets style for Histogram, filled for background, line for signal
        if typ=="bkg":
            self.hist.SetLineColor(ROOT.kBlack )
            self.hist.SetFillColor(self.color)

            self.hist.SetLineWidth(2)
        elif typ=="signal":

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
            for n,seb in enumerate(self.specificerrorband):
                seb.SetFillStyle(3004)
                seb.SetLineColor(self.sebColor[n])
                seb.SetFillColor(self.sebColor[n])

    def __str__(self):
        indent = " "*4
        s = ""
        for key in self.__dict__.keys():
            s += "{}{}: {}\n".format(indent, key, self.__dict__[key])
        return s

# ===============================================
# GET HISTOGRAMS AND ERROR BANDS
# ===============================================

def buildHistogramAndErrorBand(rootFile,sample,color,typ,label,systematics,nominalKey,procIden,systematicKey,sysIden,systClass=None,addStatErrorband=False):
    print("new sample: "+str(sample))
    # replace keys to get histogram key
    if procIden in nominalKey:
        sampleKey = nominalKey.replace(procIden, sample)
    else:
        sampleKey=nominalKey
    print(sampleKey)
    rootHist = rootFile.Get(sampleKey)
    print("    loading key '{}'".format(sampleKey))
    print("    type of hist is: "+str(type(rootHist)) )
    if not isinstance(rootHist, ROOT.TH1):
        return "ERROR"
    if rootHist.Integral() <= 0:
        print("integral zero")
        return "ERROR"

    #moves underflow in the first and overflow in the last bin
    moveOverUnderFlow(rootHist)
    # replace keys to get systematic key
    print("    starting with systematics - building Errorband")
    if procIden in systematicKey:
        sampleSystKey = systematicKey.replace(procIden, sample)
    else:
        sampleSystKey = systematicKey

    """
    check if systematic should be added when systClass is given
    """
    if not systClass is None:
        systClass.getSystematicsForProcesses([sample])
        systs = systClass.get_weight_systs(sample)
        systs+= systClass.get_variation_systs(sample)
        systs+= systClass.get_shape_systs(sample)

        systematicsForProcess = []
        for s in systs:
            if      s.endswith("Down"): systematicsForProcess.append(s[:-4])
            elif    s.endswith("Up"):   systematicsForProcess.append(s[:-2])
            else:                       systematicsForProcess.append(s)
        systematicsForProcess = list(set(systematicsForProcess))
        print(systematicsForProcess)
    else:
        systematicsForProcess = None


    #Lists for error band values
    upErrors=None
    downErrors=None
    """
    Loop over systematics to get Error band for sample
    """
    for systematic in systematics:
        """
        check if systematic is in systForProcess list if option is activated
        """
        if not systematicsForProcess is None:
            if not systematic in systematicsForProcess:
                if debug>9: print("    systematic {} not in list for this process. skipping.".format(systematic))
                continue

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
        check if histogram is TH1 type and integrals>0, else skip uncertainty
        """

        if isinstance(up, ROOT.TH1) and isinstance(down, ROOT.TH1):
            if up.Integral() < 0 or down.Integral() < 0:
                print("    variation Integrals of systematic {} smaller zero. skipping.".format(systematic))
                continue
            print  "    adding systematic ",systematic
            moveOverUnderFlow(up)
            moveOverUnderFlow(down)

            if debug>9:
                print("        integral up   {}".format(up.Integral()))
                print("        integral nom  {}".format(rootHist.Integral()))
                print("        integral down {}".format(down.Integral()))
                upRate      = (up.Integral()-rootHist.Integral())/rootHist.Integral()*100.
                downRate    = (down.Integral()-rootHist.Integral())/rootHist.Integral()*100
                cmd         = "        shift rate: {:.2f}% / {:.2f}%".format(upRate, downRate)
                if abs(upRate)>10. or abs(downRate)>10.:
                    print("\033[1;31m{}\033[0m".format(cmd))
                else:
                    print(cmd)

            for ibin in range(0, rootHist.GetNbinsX()):
                # get up down variations
                u_= up[ibin+1]-rootHist[ibin+1]
                d_= down[ibin+1]-rootHist[ibin+1]
                 # set max as up and min as down
                u = max(u_,d_)
                d = min(u_,d_)
                # only consider positive up and negative down variations
                u = max(0.,u)
                d = min(0.,d)
                upErrors[ibin]=ROOT.TMath.Sqrt( upErrors[ibin]*upErrors[ibin] + u*u )
                downErrors[ibin] = ROOT.TMath.Sqrt( downErrors[ibin]*downErrors[ibin] + d*d)
            
                if debug>99:
                    print("        adding up/down {}/{}".format(u,d))
                    print("             total {} +{}/-{}".format(rootHist[ibin+1], upErrors[ibin], downErrors[ibin]))
                    #print "-"*50
        else:
            if debug>9:
                print("ERROR! can not use: "+str(systematic) )
                print("->type of up shape hist is: "+str(type(up)) )
                print("->type of down shape is: "+str(type(down)) )
            else:
                continue

    errorband = None
    statErrorband = None
    if upErrors:
        errorband = ROOT.TGraphAsymmErrors(rootHist)
        for i in range(len(upErrors)):
            errorband.SetPointEYlow(i, downErrors[i])
            errorband.SetPointEYhigh(i, upErrors[i])
            errorband.SetPointEXlow(i, rootHist.GetBinWidth(i+1)/2.)
            errorband.SetPointEXhigh(i, rootHist.GetBinWidth(i+1)/2.)

    if addStatErrorband:
        statErrorband = ROOT.TGraphAsymmErrors(rootHist)
        for i in range(rootHist.GetNbinsX()):
            statErrorband.SetPointEYlow(i, rootHist.GetBinError(i+1))
            statErrorband.SetPointEYhigh(i, rootHist.GetBinError(i+1))
            statErrorband.SetPointEXlow(i, rootHist.GetBinWidth(i+1)/2.)
            statErrorband.SetPointEXhigh(i, rootHist.GetBinWidth(i+1)/2.)
            
    PlotObject=Plot(rootHist, sample, 
                    label = label,
                    color = color,  
                    typ = typ,
                    errorband = errorband, 
                    specificerrorband = statErrorband,
                    OverUnderFlowInc=True)

    return PlotObject


def updateBinEdges(hist, edges):
    newHist = ROOT.TH1F(hist.GetName(), hist.GetTitle(), len(edges)-1, array("f", edges))
    for i in range(len(edges)+1):
        newHist.SetBinContent(i, hist.GetBinContent(i))
        newHist.SetBinError(i, hist.GetBinError(i))
    
    return newHist


"""
Combine Output Style where Errorbands already exist
"""
def getHistogramAndErrorband(rootFile,sample,color,typ,label,nominalKey,procIden,binEdges=None,newTitle=""):
    print("new sample: "+str(sample))
    # replace keys to get histogram key
    if procIden in nominalKey:
        sampleKey = nominalKey.replace(procIden, sample)
    else:
        sampleKey=nominalKey
    print("    loading key '{}'".format(sampleKey))
    rootHist = rootFile.Get(sampleKey)
    print("    type of hist is: "+str(type(rootHist)) )
    if not isinstance(rootHist, ROOT.TH1):
        return "ERROR"

    if not binEdges is None:
        rootHist = updateBinEdges(rootHist, binEdges)
        rootHist.SetTitle(newTitle)
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
def addSamples(sample,color,typ,label,addsamples,PlotList,combineflag=None):
    combinedErrorbands=[]
    combinedHist = None
    print("Adding samples for summarized process %s" % sample)
    for addsample in addsamples:
        entry = PlotList.get(addsample, "ERROR")
        if entry == "ERROR": continue
        print "    "+addsample
        if combinedHist:
            combinedHist.Add(PlotList[addsample].hist)
            if not combineflag:
                combinedErrorbands.append(PlotList[addsample].errorband)
            del PlotList[addsample]
        else:
            combinedHist    = PlotList[addsample].hist
            if not combineflag: 
                combinedErrorbands.append(PlotList[addsample].errorband)
            del PlotList[addsample]
    if not combinedHist:
        print "WARNING: Could not load any histograms for sample '{}'".format(sample)
    # add all Errorbands together
    elif not combineflag:
        errorband=addErrorbands(combinedErrorbands,combinedHist)
        # add the new combined sample
        PlotList[sample]=Plot(combinedHist, sample, color=color, typ=typ, label=label, errorband=errorband)
    else:
        PlotList[sample]=Plot(combinedHist, sample, color=color, typ=typ, label=label)
    
    # return the altered PlotList
    return PlotList

# adding Errorbands with correlated option
def addErrorbands(combinedErrorbands,combinedHist,correlated=False):
    newErrorband = ROOT.TGraphAsymmErrors(combinedHist)
    for i in range (newErrorband.GetN()):
        up=0
        down=0
        for errorband in combinedErrorbands:
            if errorband is None: continue
            
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
    print("zeroth bin: {}".format(hist.GetBinContent(0)))
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
def GetHistoFromTGraphAE(tgraph,process,nbins_new,binEdges=None):
    nbins_old = tgraph.GetN()
    # add category to name of histogram so each histogram has a different name to avoid problems with ROOT
    histo = ROOT.TH1F(process,process,nbins_new,0,nbins_new)
    if not binEdges is None:
        histo = updateBinEdges(histo, binEdges)
    # set this flag for asymmetric errors in data histogram
    histo.Sumw2(ROOT.kFALSE)
    # loop has to go from 0..nbins_new-1 for a tgraphasymmerror with nbins_new points
    for i in range(0,nbins_new,1):
        # first point (point 0) in tgraphae corresponds to first bin (bin 1 (0..1)) in histogram
        entries = tgraph.GetY()[i]
        for k in range(int(round(entries))):# rounding necessary if used with asimov dataset because entries can be non-integer in this case
            histo.Fill(histo.GetBinCenter(i+1))
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
                    errorband=None, background=None, displayname=None, logoption=False, shape=False,
                    normalize=False, combineflag=False, splitlegend=False, datalabel="data",
                    sortedProcesses=False, yLabel="Events expected", xLabel = None):
        self.PlotList       = PlotList
        self.canvasName     = canvasName
        self.data           = data 
        self.datalabel      = datalabel
        if self.data:
            self.ratio      = ratio 
        else:
            self.ratio      = False
        self.signalscaling  = signalscaling
        self.errorband      = errorband 
        self.background     = background
        self.displayname    = displayname 
        if not self.displayname:
            self.displayname = canvasName
        self.logoption      = logoption 
        self.normalize      = normalize 
        self.combineflag    = combineflag
        self.splitlegend    = splitlegend
        self.shape          = shape
        self.sortedProcesses = sortedProcesses
        if self.combineflag and not self.sortedProcesses:
            self.sortedProcesses = ["total_signal"]

        self.yLabel          = yLabel
        self.xLabel          = xLabel
    # ===============================================
    # DRAW HISTOGRAMS ON CANVAS
    # ===============================================

    def drawHistsOnCanvas(self):
        """
        set the Style for the Signal and Background Plots
        get the integral of the hists to sort it by event yield for plotting
        sort it by Event Yield, lowest to highest
        """
        #c = ROOT.TCanvas()
        #self.data.Draw()
        #c.SaveAs("test.pdf")
        #c.Clear()        


        self.sortPlots()

        """
        stack background Histograms
        add errorbands of background histograms to a list
        to combine them for the errorband of all backgrounds
        """
        self.stackPlots(self.sortedStacks)

        """
        sort signal Histograms by Event Yield
        """
        self.shapePlots(self.sortedShapes)

        """
        figure out plotrange
        yMax is the maximum bin value of all background histograms
        yMinMax is the minimal bin value of all background histograms, 
        needed for logarithmic plotting (need to set lowest value)
        """
        self.PlotRange()
        
        """
        get the first histogram to draw,
        use the first background histogram,
        else use an signal histogram
        and do shape Plots
        """
        if len(self.stackPlots) == 0:
            firstHist       = self.shapePlots[0]
            self.ratio      = False
            self.data       = False
            self.normalize  = True
        else:
            firstHist = self.stackPlots[0]


        firstHist.SetStats(False)
        """
        get the total background event yield
        to scale the signal
        and normalize the Plot 
        """
        firstHistIntegral=firstHist.Integral()
        if self.shape:
            firstHist.Scale(1./firstHistIntegral)
        elif self.normalize:
            self.normalizePlot(PlotHist=firstHist)

        """
        create Canvas split in two if ratio is activated
        """
        self.canvas = getCanvas(self.displayname,self.ratio)
        self.canvas.cd(1)

        """
        consider logoption and set the user range accordingly
        scaling maximal and minimal y value for better readability
        """
        if self.logoption:
            firstHist.GetYaxis().SetRangeUser(self.yMinMax/10000, self.yMax*1000)
            ROOT.gPad.SetLogy(1)
        else:
            firstHist.GetYaxis().SetRangeUser(0.01, self.yMax*1.6)
        
        """
        Handle titles
        """
        firstHist.GetYaxis().SetTitle(self.GetyTitle())
        firstHist.GetYaxis().SetTitleSize(firstHist.GetYaxis().GetTitleSize()*1.2)
        canvaslabel=firstHist.GetTitle() if self.xLabel == None else self.xLabel


        if self.ratio:
            firstHist.GetXaxis().SetTitle("")
            firstHist.SetTitle("")
        else:
            firstHist.GetXaxis().SetTitle(canvaslabel)
            firstHist.SetTitle("")

        """
        Draws first hist
        """
        option = "histo"
        if self.stackPlots:
            firstHist.DrawCopy(option+"")
        else:
            firstHist.DrawCopy(option)

        """
        draw the other histograms and the errorband
        """
        for h in self.stackPlots[1:]:
            if self.normalize:
                h.Scale(self.normalizefactor)
            h.DrawCopy(option+"same")

        if self.errorband:
            self.errorband.SetFillStyle(1001)
            self.errorband.SetLineColorAlpha(ROOT.kBlack, 0.3)
            self.errorband.SetFillColorAlpha(ROOT.kBlack, 0.3)
            self.errorband.Draw("same2")
        elif self.combinederrorbands:
            for ceb in self.combinederrorbands:
                ceb.SetFillStyle(1001)
                ceb.SetLineColorAlpha(ROOT.kBlack,0.1)
                ceb.SetFillColorAlpha(ROOT.kBlack,0.1)
                ceb.Draw("same2")





        self.canvas.cd(1)
        # redraw axis
        firstHist.DrawCopy("axissame")
        
        # draw signal histograms
        for n,shape in enumerate(self.shapePlots):
            # scale signal
            if self.normalize or self.shape:
                scalefactor=1/shape.Integral()
            elif self.signalscaling==-1:
                scalefactor=firstHistIntegral/shape.Integral()
            else:
                scalefactor=self.signalscaling
            shape.Scale(scalefactor)
            if scalefactor != 1 and not self.normalize and not self.shape:
                self.PlotList[self.sortedShapes[n]].label += " x "+str(int(scalefactor))
            # draw signal histogram
            shape.DrawCopy(option+" same")

        # draw data
        if self.data:
            self.data.SetLineColor(ROOT.kBlack)
            self.data.SetMarkerStyle(20)
            self.data.SetFillStyle(0)
            self.data.SetMarkerSize(1.5)
            self.data.SetLineWidth(1)
            #self.data.Draw("same1")
            self.data.Draw("histPEX0same")

        """
        Draws the ratio plot, scales the background, signal and errorband to the background
        """
        if self.ratio:
            self.canvas.cd(2)
            if self.errorband:
                self.drawRatioCombine(title = "", canvaslabel=canvaslabel)
            else:
                self.drawRatio(stackhist = firstHist, canvaslabel = canvaslabel)

    
    def sortPlots(self):
        """
        set the Style for the Signal and Background Plots
        get the integral of the hists to sort it by event yield for plotting
        """
        Shapes      = {}
        Stacks      = {}
        for sample in self.PlotList:
            PlotObject = self.PlotList[sample]
            if PlotObject == "ERROR": continue
            if self.shape:
                PlotObject.setStyle("signal")
                Shapes[PlotObject.name] = PlotObject.hist.Integral()
            else:
                PlotObject.setStyle()
                if PlotObject.typ == "signal":
                    Shapes[PlotObject.name] = PlotObject.hist.Integral()
                elif PlotObject.typ == "bkg":
                    Stacks[PlotObject.name] = PlotObject.hist.Integral()
        """
        sort it by Event Yield, lowest to highest
        """
        self.sortedShapes      = sorted(Shapes, key=Shapes.get, reverse=True)
        self.sortedStacks      = sorted(Stacks, key=Stacks.get,reverse=True)

        if self.sortedProcesses:
            sortedShapes        = self.sortedShapes
            self.sortedShapes   = []
            sortedStacks        = self.sortedStacks
            self.sortedStacks   = []
            for process in self.sortedProcesses:
                if process in sortedShapes:
                    self.sortedShapes.append(process)
                elif process in sortedStacks:
                    self.sortedStacks.append(process)
            for shape in sortedShapes:
                if shape not in self.sortedShapes:
                    self.sortedShapes.append(shape)
            for stack in sortedStacks:
                if stack not in self.sortedStacks:
                    self.sortedStacks.append(stack)

    def stackPlots(self, sortedPlots):
        """
        stack background Histograms
        if not combine style of rootfile
        add errorbands of background histograms to a list
        to combine them for the errorband of all backgrounds
        """
        # figure out number of errorbands:
        errorbands = []
    
        if len(sortedPlots) >= 1:
            PlotObject = self.PlotList[sortedPlots[0]]
            if not PlotObject.errorband is None:
                print("default errorband found")
                errorbands.append( [] )
            if not PlotObject.specificerrorband is None:
                for seb in PlotObject.specificerrorband:
                    print("specific errorband found")
                    errorbands.append( [] )

        self.stackPlots         = []
        self.combinederrorbands = None
        for i in range(len(sortedPlots),0,-1):
            Plot        = sortedPlots[i-1]
            PlotObject  = self.PlotList[Plot]
            if len(self.stackPlots)==0:
                self.stackPlots.append(PlotObject.hist.Clone())
                if not self.combineflag:
                    idx = 0
                    if not PlotObject.errorband is None:
                        errorbands[idx].append(PlotObject.errorband.Clone())
                        idx += 1
                    if not PlotObject.specificerrorband is None:
                        for seb in PlotObject.specificerrorband:
                            errorbands[idx].append(seb.Clone())
                            idx += 1
            else:
                hist = PlotObject.hist.Clone()
                hist.Add(self.stackPlots[0])
                self.stackPlots.insert(0, hist)
                if not self.combineflag:
                    idx = 0
                    if not PlotObject.errorband is None:
                        errorbands[idx].append(PlotObject.errorband.Clone())
                        idx += 1
                    if not PlotObject.specificerrorband is None:
                        for seb in PlotObject.specificerrorband:
                            errorbands[idx].append(seb.Clone())
                            idx += 1

        if not len(self.stackPlots) == 0 and not self.combineflag:
            self.combinederrorbands = []
            for eb in errorbands:
                self.combinederrorbands.append(addErrorbands(eb,self.stackPlots[0]))


    def shapePlots(self,sortedPlots):
        """
        get Shape Histograms in a List
        with combine flag activated only get total signal
        """
        self.shapePlots=[]
        for signal in sortedPlots:
            PlotObject = self.PlotList[signal]
            self.shapePlots.append(PlotObject.hist.Clone())

    def PlotRange(self):
        """
        figure out plotrange
        yMax is the maximum bin value of all background histograms
        yMinMax is the minimal bin value of all background histograms, 
        needed for logarithmic plotting (need to set lowest value)
        """
        self.yMax = 1e-9
        self.yMinMax = 1000.
        for hist in self.stackPlots:#+self.shapePlots:
            if self.shape and hist.Integral()!=0:
                self.yMax = max(hist.GetBinContent(hist.GetMaximumBin())/hist.Integral(), self.yMax)
            else:
                self.yMax = max(hist.GetBinContent(hist.GetMaximumBin()), self.yMax)
            if hist.GetBinContent(hist.GetMaximumBin()) > 0:
                if self.shape and hist.Integral()!=0:
                    self.yMinMax = min(hist.GetBinContent(hist.GetMaximumBin())/hist.Integral(), self.yMinMax)
                else:
                    self.yMinMax = min(hist.GetBinContent(hist.GetMaximumBin()), self.yMinMax)

    def normalizePlot(self, PlotHist):

        """
        to normalize the Plot 
        """
        self.normalizefactor=1/PlotHist.Integral()
        PlotHist.Scale(self.normalizefactor)
        self.yMax    = self.yMax*self.normalizefactor
        self.yMinMax = self.yMinMax*self.normalizefactor

        print self.yMax
        print self.yMinMax


    def drawRatioLine(self, canvaslabel):
        """
        Draws the ratio plot, scales the background, signal and errorband to the background
        """
        
        line = self.data.Clone()
        line.Divide(self.data)
        #line.GetYaxis().SetRangeUser(0.5,1.5)
        line.GetYaxis().SetRangeUser(0.3,1.7)
        line.GetYaxis().SetTitle(self.ratio)

        line.SetTitle("")

        line.GetXaxis().SetLabelSize(line.GetXaxis().GetLabelSize()*2.4)
        line.GetYaxis().SetLabelSize(line.GetYaxis().GetLabelSize()*2.2)
        line.GetXaxis().SetTitle(canvaslabel)

        line.GetXaxis().SetTitleSize(line.GetXaxis().GetTitleSize()*3)
        line.GetYaxis().SetTitleSize(line.GetYaxis().GetTitleSize()*2.5)

        line.GetYaxis().SetTitleOffset(0.5)
        line.GetYaxis().SetNdivisions(505)
        line.GetYaxis().CenterTitle()
        for i in range(line.GetNbinsX()+1):
            line.SetBinContent(i, 1)
            line.SetBinError(i, 1)
        line.SetLineWidth(1)
        line.SetLineColor(ROOT.kBlack)
        line.DrawCopy("histo")

    def drawRatio(self,stackhist,canvaslabel=""):
        self.drawRatioLine(canvaslabel)

        # ratio plot
        ratioPlot = self.data.Clone()
        ratioPlot.Divide(stackhist)
        ratioPlot.SetTitle(stackhist.GetTitle())
        ratioPlot.SetLineColor(ROOT.kBlack)
        ratioPlot.SetLineWidth(1)
        ratioPlot.SetMarkerStyle(20)
        ROOT.gStyle.SetErrorX(0)
        ratioPlot.DrawCopy("sameP")

        self.generateRatioErrorband()
        self.canvas.cd(1)

    def drawRatioCombine(self,title="",canvaslabel = ""):
        self.drawRatioLine(canvaslabel)    
        self.ratio_error_graph = self.errorband.Clone()
        for i in range(0,self.errorband.GetN(),1):
            self.ratio_error_graph.SetPoint(i,self.errorband.GetX()[i],1)
            self.ratio_error_graph.SetPointEYhigh(i,self.errorband.GetErrorYhigh(i)/self.errorband.GetY()[i])
            self.ratio_error_graph.SetPointEYlow(i,self.errorband.GetErrorYlow(i)/self.errorband.GetY()[i])
        self.ratio_error_graph.Draw("same2")

        self.ratioPlot = ROOT.TGraphAsymmErrors(self.data.Clone())
        for i in range(1,self.data.GetNbinsX()+1,1):
            self.ratioPlot.SetPoint(i-1,self.errorband.GetX()[i-1],self.data.GetBinContent(i)/self.background.GetBinContent(i))
            self.ratioPlot.SetPointError(i-1,0.,0.,
                (self.data.GetBinErrorLow(i))/self.background.GetBinContent(i),(self.data.GetBinErrorUp(i))/self.background.GetBinContent(i))
        self.ratioPlot.SetMarkerStyle(20)
        self.ratioPlot.Draw("P2 same")
        self.canvas.cd(1)

    # scales the Errorband for the ratio plot
    def generateRatioErrorband(self):
        self.ratioerrorbands = []
        if self.combinederrorbands:
            for ceb in self.combinederrorbands:
                self.ratioerrorbands.append( ceb.Clone() )
        elif self.errorband:
            self.ratioerrorbands.append(self.errorband.Clone())
        else: return 

        for reb in self.ratioerrorbands:
            for i in range(reb.GetN()):
                x=ROOT.Double()
                y=ROOT.Double()
                reb.GetPoint(i,x,y)
                reb.SetPoint(i,x,1)
                if y>0.:
                    reb.SetPointEYlow(i,reb.GetErrorYlow(i)/y)
                    reb.SetPointEYhigh(i,reb.GetErrorYhigh(i)/y)
                else:
                    reb.SetPointEYlow(i,0)
                    reb.SetPointEYhigh(i,0)

            reb.Draw("same2")
        
    def GetyTitle(self):
        # normalize plots to unit area
        if self.normalize:
            return "normalized to unit area"
        return self.yLabel

    def builtLegend(self):
        # drawing the legend
        # split legend:

        if self.splitlegend:
            self.legend1 = getLegend1()
            self.legend2 = getLegend2()
            n = 0
            if self.data:
                self.legend1.AddEntry(self.data,self.datalabel,"P")
                n+=1

            legendentries = len(self.sortedShapes)+len(self.sortedStacks)
            for i,shape in enumerate(self.sortedShapes):
                if not n%2:
                    self.legend1.AddEntry(self.shapePlots[i], self.PlotList[shape].label, "L")
                else:
                    self.legend2.AddEntry(self.shapePlots[i], self.PlotList[shape].label, "L")
                n+=1
            for i,stack in enumerate(self.sortedStacks):
                if not n%2:
                    self.legend1.AddEntry(self.stackPlots[i], self.PlotList[stack].label, "F")
                else:
                    self.legend2.AddEntry(self.stackPlots[i], self.PlotList[stack].label, "F")
                n+=1
            self.legend1.Draw("same")
            self.legend2.Draw("same")
        else:
            self.legend = getLegend()
            if self.data:
                self.legend.AddEntry(self.data,self.datalabel,"P")

            for i,shape in enumerate(self.sortedShapes):
                self.legend.AddEntry(self.shapePlots[i], self.PlotList[shape].label, "L")
            for i,stack in enumerate(self.sortedStacks):
                self.legend.AddEntry(self.stackPlots[i], self.PlotList[stack].label, "F")
            self.legend.Draw("same")

    # ===============================================
    # PRINT STUFF ON CANVAS
    # ===============================================
    def printLumi(self, lumi):
        if lumi == 0.: return

        lumi_text = str(lumi)+" fb^{-1} (13 TeV)"

        self.canvas.cd(1)
        l = self.canvas.GetLeftMargin()
        t = self.canvas.GetTopMargin()
        r = self.canvas.GetRightMargin()
        b = self.canvas.GetBottomMargin()

        latex = ROOT.TLatex()
        latex.SetNDC()
        latex.SetTextColor(ROOT.kBlack)
        
        if self.ratio:  latex.DrawLatex(l+0.60,1.-t+0.04,lumi_text)
        else:           latex.DrawLatex(l+0.53,1.-t+0.02,lumi_text)

    def printChannelLabel(self, channelLabel):
        self.canvas.cd(1)
        l = self.canvas.GetLeftMargin()
        t = self.canvas.GetTopMargin()
        r = self.canvas.GetRightMargin()
        b = self.canvas.GetBottomMargin()

        latex = ROOT.TLatex()
        latex.SetNDC()
        latex.SetTextColor(ROOT.kBlack)

        if self.ratio:  latex.DrawLatex(l+0.09,1.-t-0.06, channelLabel)
        else:           latex.DrawLatex(l+0.02,1.-t-0.06, channelLabel)

    def printCMSLabel(self, cmslabel):
        self.canvas.cd(1) 
        l = self.canvas.GetLeftMargin() 
        t = self.canvas.GetTopMargin() 
        r = self.canvas.GetRightMargin() 
        b = self.canvas.GetBottomMargin() 
     
        latex = ROOT.TLatex() 
        latex.SetNDC() 
        latex.SetTextColor(ROOT.kBlack) 
        latex.SetTextSize(0.04)

        text = "CMS #bf{#it{"+cmslabel+"}}"

        if self.ratio:      latex.DrawLatex(l+0.05,1.-t+0.04, text) 
        else:               latex.DrawLatex(l,1.-t+0.01, text)

    def saveCanvas(self, path):
        self.canvas.SaveAs(path)
        self.canvas.SaveAs(path.replace(".pdf",".png"))
        self.canvas.Clear()


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
    legend=ROOT.TLegend(0.65,0.7,0.95,0.9)
    legend.SetBorderSize(0)
    legend.SetLineStyle(0)
    legend.SetTextFont(42)
    legend.SetTextSize(0.03)
    legend.SetFillStyle(0)
    return legend

def getLegend1():
    legend=ROOT.TLegend(0.65,0.7,0.8,0.9)
    legend.SetBorderSize(0)
    legend.SetLineStyle(0)
    legend.SetTextFont(42)
    legend.SetTextSize(0.03)
    legend.SetFillStyle(0)
    return legend

def getLegend2():
    legend=ROOT.TLegend(0.8,0.7,0.95,0.9)
    legend.SetBorderSize(0)
    legend.SetLineStyle(0)
    legend.SetTextFont(42)
    legend.SetTextSize(0.03)
    legend.SetFillStyle(0)
    return legend



def createExamplePlotconfig(outputpath):
    outputpath=outputpath+'/ExamplePlotconfig.py'
    code = """# samples named in the rootfile
plottingsamples = {
    "ttH_hbb" : {
        "info" : {
            "label" : "t#bar{t}H, H to b#bar{b}",   # text that will be displayed in the plot legend for this process 
            "color": ROOT.kCyan,    # color of the process in the plot. You can use both kCOLOR or the number attributed to the enum keyword
            "typ": "signal"     # defines type of process. Signal are not part of the stack and are drawn as lines
            },
        "plot" : True   # decides is process is drawn in the first place or not
    },
    "ttH_hgg" : {
        "info" : {
            "label" : "t#bar{t}H, H to #gamma#gamma",   # text that will be displayed in the plot legend for this process 
            "color": ROOT.kCyan,    # color of the process in the plot. You can use both kCOLOR or the number attributed to the enum keyword
            "typ": "signal"     # defines type of process. Signal are not part of the stack and are drawn as lines
            },
        "plot" : True   # decides is process is drawn in the first place or not
    },
    "ttbb" : {
        "info" : {
            "label" : "t#bar{t}+b#bar{b}",
            "color": ROOT.kRed+3,
            "typ": "bkg"
            },
        "plot" : True
    },
    "ttbarZ" : {
        "info" : {
            "label" : 't#bar{t}+Z',
            "color": 432,
            "typ": "bkg"
            },
        "plot" : False
    }
}

# combined samples. This allows to merge process for a plot
plottingsamples = {
    "ttH" : {
        "color": ROOT.kCyan, 
        "addSamples": ["ttH_hbb", "ttH_hgg"], 
        "typ": "signal", 
        "label": "t#bar{t}H"
    }
}

# systematics to be plotted. Uncertainties will be used for the uncertainty band in the plot, i.e. merged
systematics = [
    "CMS_ttHbb_PU",
    "CMS_eff_e_2018",
    "CMS_scale_j_2018"
]

# order of the stack processes, descending from top to bottom
sortedprocesses=["ttH","ttbb"]

# options for the plotting style
plotinfo = {
    "signalScaling"     : -1,   # factor with which the signal processes will be scaled. Choose -1 to normalize signal processes to background stack
    "datalabel"         : "data", # name of data displayed in legend
    "data"              : "data_obs", # name of data in the input root file
    "lumiLabel"         : "41.5",     # string in upper right corner next to '(13 TeV)'
    
    "cmslabel"          : "private Work",   # text in cursive in upper left corner next to 'CMS'
    "normalize"         : False,    # normalize all processes to unity
    "ratio"             : '#frac{data}{MC Background}', # label for y axis of ratio plot
    "logarithmic"       : False,    # draw y axis logarithmic
    "splitLegend"       : True,     # split the legend into two columns
    "shape"             : False,    # normalize to first histogram
    
    "statErrorband"     : True,     # draw statistical uncertainty band in a separate error band (additional to systematics)
    "nominalKey"        : "$PROCESS__$CHANNEL", # name template for histograms in .root file. Keywords will be replaced
    "systematicKey"     : "$PROCESS__$CHANNEL__$SYSTEMATIC",  # name template for systematic variations in .root file. Keywords will be replaced

    # use for combine plots, use 'shapes_prefit' for prefit OR 'shapes_fit_s' for post fit
    # only uses total signal and does not split signal processes
    # 
    # "combineflag"     : "shapes_prefit"/"shapes_fit_s",
    # "signallabel"     : "Signal"  # label in legend for signal
}
    """
    with open(outputpath,'w') as outfile:
        outfile.write(code)

    print("saved Example Plotconfig at {}".format(outputpath))
