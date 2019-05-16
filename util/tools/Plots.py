import ROOT
ROOT.gROOT.SetBatch(True)
import re
import numpy as np

class Plot:
	def __init__(self, histo, variable, label = '', color= '', typ=''):
		self.histo=histo
		self.variable=variable
		self.label=label
		self.color=color
		self.typ=typ


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
ROOT.TMath.Power(hist.GetBinError(hist.GetNbinsX()),2) + ROOT.TMath.Power(hist.GetBinError(hist.GetNbinsX()+1),2) ))


# dictionary for colors
def GetPlotColor( cls ):
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

    if "ttZ" in cls: cls = "ttZ"
    if "ttH" in cls: cls = "ttH"
    return color_dict[cls]

def GetyTitle(privateWork = False):
    # if privateWork flag is enabled, normalize plots to unit area
    if privateWork:
        return "normalized to unit area"
    return "Events expected"


# ===============================================
# DRAW HISTOGRAMS ON CANVAS
# ===============================================

def drawHistsOnCanvas(sigHists, bkgHists, canvasName,ratio=False, errorband=None, displayname=None, logoption=False):
    if not displayname: 
        displayname=canvasName
    if not isinstance(sigHists, list):
        sigHists = [sigHists]
    if not isinstance(bkgHists, list):
        bkgHists = [bkgHists]
    
    canvas = getCanvas(canvasName, ratio)

    # # move over/underflow bins into plotrange
    # for h in bkgHists:
    #     moveOverUnderFlow(h)
    # for h in sigHists:
    #     moveOverUnderFlow(h)
    
    # stack Histograms
    bkgHists = [bkgHists[len(bkgHists)-1-i] for i in range(len(bkgHists))]
    for i in range(len(bkgHists)-1, 0, -1):
        bkgHists[i-1].Add(bkgHists[i])

    # figure out plotrange
    canvas.cd(1)
    yMax = 1e-9
    yMinMax = 1000.
    for h in bkgHists:
        yMax = max(h.GetBinContent(h.GetMaximumBin()), yMax)
        if h.GetBinContent(h.GetMaximumBin()) > 0:
            yMinMax = min(h.GetBinContent(h.GetMaximumBin()), yMinMax)
    
    # draw the first histogram
    if len(bkgHists) == 0:
        firstHist = sigHists[0]
    else:
        firstHist = bkgHists[0]
    if logoption:
        firstHist.GetYaxis().SetRangeUser(yMinMax/10000, yMax*10)
        canvas.SetLogy()
    else:
        firstHist.GetYaxis().SetRangeUser(0, yMax*1.5)
    firstHist.GetXaxis().SetTitle(displayname)

    option = "histo"
    firstHist.DrawCopy(option+"E0")

    # draw the other histograms
    for h in bkgHists[1:]:
        h.DrawCopy(option+"same")

    if errorband:
    	errorband.Draw("same2")

    canvas.cd(1)
    # redraw axis
    firstHist.DrawCopy("axissame")

    
    # draw signal histograms
    for sH in sigHists:
        # draw signal histogram
        sH.DrawCopy(option+" E0 same")
    

    if ratio:
        canvas.cd(2)
        line = sigHists[0].Clone()
        line.Divide(sigHists[0])
        line.GetYaxis().SetRangeUser(0.5,1.5)
        line.GetYaxis().SetTitle(ratio)

        line.GetXaxis().SetLabelSize(line.GetXaxis().GetLabelSize()*2.4)
        line.GetYaxis().SetLabelSize(line.GetYaxis().GetLabelSize()*2.2)
        line.GetXaxis().SetTitle(displayname)

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
        # ratio plots
        for sigHist in sigHists:
            ratioPlot = sigHist.Clone()
            ratioPlot.Divide(bkgHists[0])
            ratioPlot.SetTitle(displayname)
            ratioPlot.SetLineColor(sigHist.GetLineColor())
            ratioPlot.SetLineWidth(1)
            ratioPlot.SetMarkerStyle(20)
            ratioPlot.SetMarkerColor(sigHist.GetMarkerColor())
            ROOT.gStyle.SetErrorX(0)
            ratioPlot.DrawCopy("sameP")
        canvas.cd(1)
    return canvas
    


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
    legend.SetTextSize(0.05);
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
