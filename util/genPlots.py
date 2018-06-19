import ROOT
import math
import numpy as np
from itertools import product
import glob
import subprocess
import os
import re
import xml.etree.ElementTree as ET
import CMS_lumi
from copy import deepcopy
import array
from string import join

ROOT.gStyle.SetPaintTextFormat("4.2f");
ROOT.gROOT.SetBatch(True)


class genPlots:
    def __init__(self, outPath, plots, workdir, samplesData, rebin):
        self.outPath = outPath
        self.plots = plots
        self.workdir = workdir
        self.rebin = 1
        self.samplesData = samplesData

        self.lists = {}
        self.samples = {}
        self.nestedHistLists = {}


    # -- functions for setting up lists -----------------------------------------------------------
    def genList(self, samples, listName, catNames = [""], doTwoDim = False):
        newList = []
        rootFile = ROOT.TFile(self.outPath, "readonly")
        keyList = rootFile.GetKeyNames()

        # generate hist lists per sample
        for sample in samples:
            histList = []
            ROOT.gDirectory.cd("PyROOT:/")
            print("category names:")
            print catNames
            for cat in catNames:
                for plot in self.plots:
                    key = sample.nick+"_"+cat+plot.name
                    rootHist = f.Get(key)
                    if isinstance(rootHist, ROOT.TH1) and not isinstance(rootHist, ROOT.TH2):
                        rootHist.Rebin(self.rebin)
                        histList.append( rootHist.Clone() )
                    if doTwoDim and isinstance(rootHist, ROOT.TH2):
                        histList.append( rootHist.Clone() )
            newList.append(histList)

        # transpose the new list
        newList = transposeLOL(newList)
        print("-"*30)
        print("generated new list with name "+str(listName))
        print(newList)
        print("-"*30)
        self.lists[listName] = newList
        self.samples[listName] = samples
        return

    def genTranspose(self, listName):
        transposedList = transposeLOL( self.lists[listName] )
        self.lists[listName+".T"] = transposedList
        print("-"*30)
        print("generated transposed list with name "+str(listName+".T"))
        print(transposedList)
        print("-"*30)
        return
    # ---------------------------------------------------------------------------------------------



    # -- loading options for simple control/shape plots -------------------------------------------
    def loadOptions(self, options):
        defaultOptions = {"factor": -1,
                "logscale": False,
                "canvasOptions": "histo",
                "normalize": False,
                "stack": False,
                "ratio": False,
                "doProfile": False,
                "statTest": False,
                "sepaTest": False,
                "blinded": True}

        # set options
        for opt in defaultOptions:
            if opt in options:
                defaultOptions[opt] = options[opt]
                print(str(opt)+" set to "+str(options[opt]))

        return defaultOptions
    # ---------------------------------------------------------------------------------------------



    # -- making simple control/shape plots --------------------------------------------------------
    def makeSimpleControlPlots(self, listName, listIndex, options = {}):

        # load options
        print("loading options for making simple control plots")
        plotOptions = self.loadOptions(options)
        
        # load transposed list
        transposedList = self.lists[listName+".T"]
        samples = self.samples[listName]

        # generate stuff for control plots
        plotPath = self.workdir + "/controlPlots/"
        if not os.path.exists(plotPath):
            os.makedirs(plotPath)

        controlList = transposeLOL( transposedList[listIndex:] )
        headList = transposedList[0]
        controlSamples = samples[listIndex:]
        headSamples = samples[0]

        # starting draw control plots
        canvases = []
        objects = []
        index = 0
        
        # start loop over used list
        for listOfHists, headHist in zip(controlList, headList):
            index += 1
            integralFactor = 0

            # start loop over histos in listofhists
            for hist, sample in zip(listOfHists, controlSamples):
                yTitle = 'Events expected for 12.9 fb^{-1} @ 13 TeV'

                # stup histogram
                setupHist( hist, sample.color, yTitle, plotOptions["stack"] )
                
                if plotOptions["factor"] < 0:
                    integralFactor += histo.Integral()

            # getting integralfactor
            if plotOptions["factor"] < 0:
                if headHist.Integral() != 0:
                    integralFactor = integralFactor/headHist.Integral()
                else:
                    print("WARNING")
                    print("head histo "+str(headHist.GetName)+ "has integral 0")
                    print("this would lead to zero division error")
            
            # drawing hists on canvas
            canvas = drawHistOnCanvas(listOfHists, plotOptions)
            canvas.cd()

            # setting up head canvas
            headCanvas = headHist.Clone()
            setupHist(headCanvas, headSample.color, yTitle = "")

            headCanvas.SetBinContent(1, 
                        headCanvas.GetBinContent(0)+headCanvas.GetBinContent(1));
            headCanvas.SetBinContent(headCanvas.GetNbinsX(),
                        headCanvas.GetBinContent(headCanvas.GetNbinsX()+1) + \
                            headCanvas.GetBinContent(headCanvas.GetNbinsX()));
            headCanvas.SetBinError(1,
                        ROOT.TMath.Sqrt(
                            ROOT.TMath.Power(headCanvas.GetBinError(0),2) + \
                                ROOT.TMath.Power(headCanvas.GetBinError(1),2)));
            headCanvas.SetBinError(headCanvas.GetNbinsX(),
                        ROOT.TMath.Sqrt(
                            ROOT.TMath.Power(headCanvas.GetBinError(headCanvas.GetNbinsX()+1),2) + \
                                ROOT.TMath.Power(headCanvas.GetBinError(headCanvas.GetNbinsX()),2)));
            headCanvas.SetLineWidth(3)

            # setting up legends
            legend1 = getLegendL()
            legend2 = getLegendR()

            if plotOptions["factor"] >= 0:
                legend2.AddEntry22(headCanvas, headSample.name+" x "+str(plotOptions["factor"]), "L")
            else:
                legend2.AddEntry22(headCanvas, headSample.name+(' x {:4.0f}').format(integralFactor), "L")
            
            index = 0
            for hist, sample in zip(listOfHistos, controlSamples):
                index += 1
                if index%2 == 1:
                    legend1.AddEntry22(hist, sample.name, "F")
                if index%2 == 0:
                    legend2.AddEntry22(hist, sample.name, "F")
            
            # add generated canvas to canvas list
            canvases.append(canvas)
            
            if plotOptions["factor"] >= 0.:
                headCanvas.Scale( plotOptions["factor"] )
            else:
                headCanvas.Scale( integralFactor )

            # add legend and headcanvas to objects
            headCanvas.DrawCopy( "samehisto" )
            legend1.Draw("same")
            legend2.Draw("same")
            objects.append(legend1)
            objects.append(legend2)
            objects.append(headCanvas)

            # do separation tests
            if sepaTest:
                sepTests = getSepaTests2(listOfHistos, headHist)
                for sepTest in sepTests:
                    sepTest.Draw()
                    objects.append(sepTest)
        
            #cms = ROOT.TLatex(0.2, 0.96, "CMS private work");
            #cms = ROOT.TLatex(0.18, 0.85, "#splitline{CMS simulation}{WORK IN PROGRESS}" );
            #cms.SetTextFont(42)
            #cms.SetTextSize(0.065)
            #cms.SetNDC()
            #cms.Draw()
            #objects.append(cms)
        
        # print all canvases
        printCanvases(canvases, plotPath)
        
        # write all objects
        writeObjects(canvases, plotPath)


    def makeSimpleShapePlots(self, listName, listIndex, label = "", options = {}):
        # load options
        print("loading options for making simple shape plots")
        plotOptions = self.loadOptions(options)

        # load transposed list
        transposedList = self.lists[listName+".T"]
        samples = self.samples[listName]

        # generate stuff for shape plots    
        plotPath = self.workdir + "/shapePlots/"
        if not os.path.exists(plotPath):
            os.makedirs(plotPath)

        shapeList = transposeLOL( [transposedList[0]] + transposedList[listIndex:] )
        shapeSamples = [samples[0]] + samples[listIndex:]

        # get label texts
        if isinstance(label, basestring):
            labelTexts = len(shapeList)*[label]
        else:
            labelTexts = label

        # starting shape plots
        canvases = []
        objects = []
        index = 0

        # starting loop over list of hists
        for listOfHists, labelText in zip( shapeList, labelTexts):
            index += 1

            # starting loop over hists in list of hists
            for hist, sample in zip(listOfHists, shapeSamples):

                # setting y title
                yTitle = "Events"
                if plotOptions["normalize"]:
                    yTitle = "normalized"

                # setting up histogram
                setupHist( hist, sample.color, yTitle, plotOptions["stack"] )

            # drawing canvas
            canvas = drawHistOnCanvas( listOfHists, plotOptions )
            canvas.SetName( listOfHists[0].GetName() )

            # setting up legend
            legend = getLegend()
            for hist, sample in zip(listOfHists, shapeSamples):
                legendOpt = "F" if plotOptions["stack"] else "L"
                legend.AddEntry2( hist, sample.name, legendOpt )

            # adding canvas to list
            canvases.append( canvas )
            legend.Draw("same")
            objects.append( legend )

            # doint stat and sepa tests
            if plotOptions["statTest"]:
                statTests = getStatTests( listOfHists[0], listOfHists[1] )
                statTests.Draw()
                objects.append( statTests )
            if plotOptions["sepaTest"]:
                sepTests = getSepaTests( listOfHists[0], listOfHists[1] )
                sepTests.Draw()
                objects.append( sepTests )


            #cms = ROOT.TLatex( 0.2, 0.96, "CMS private work" );
            cms = ROOT.TLatex(0.2, 0.96, "CMS preliminary,  36.0 fb^{-1},  #sqrt{s} = 13 TeV" );
            cms.SetTextFont(42)
            cms.SetTextSize(0.05)
            cms.SetNDC()
            cms.Draw()
            objects.append(cms)

            label = ROOT.TLatex(0.2, 0.86, labelText);
            label.SetTextFont(42)
            label.SetTextSize(0.05)
            label.SetNDC()
            label.Draw()
            objects.append(label)

        # print all canvases
        printCanvases( canvases, plotPath )

        # write all objects
        writeObjects( canvases, plotPath )
    # ---------------------------------------------------------------------------------------------





    # -- making control plots ---------------------------------------------------------------------
    def genNestedHistList(self, controlSamples, systNames, name):
        rootFile = ROOT.TFile(self.outPath, "readonly")

        objects = []
        keyList = rootFile.GetKeyNames()
        outList = []

        # looping over discr plots
        for plot in self.plots:
            nestedList = []
            print("creating nested list for plot " + str(plot.name))
            for sample in controlSamples:
                nominalKey = sample.nick+"_"+plot.name+systNames[0]
                nominal = f.Get(nominalKey)

                baseList = []
                for syst in systNames:
                    ROOT.gDirectory.cd("PyROOT:/")
                    key = sample.nick+"_"+plot.name+syst

                    if not syst in sample.shape_unc:
                        print("using nominal key for " + str(key))
                        baseList.append( nominal.Clone(key) )
                        continue

                    outHist = rootFile.Get(key)
                    if isinstance(outHist, ROOT.TH1) and not isinstance(outHist, ROOT.TH2):
                        baseList.append( outHist.Clone() )
                    else:
                        print(str(syst)+" not used for "+str(sample.name))
                nestedList.append(baseList)
            outList.append(nestedList)

        print("generated list of histograms for making control plots")
        print("location: self.nestedHistList[name]")
        self.nestedHistLists[name] = outList


    def makeControlPlots(self, listName, listIndex, dataName, nestedHistsConfig, options):
        # load options
        print("loading options for making simple shape plots")
        plotOptions = self.loadOptions(options)

        # load transposed list
        transposedList = self.lists[listName+".T"]
        samples = self.samples[listName]

        # generate stuff for control plots
        plotPath = self.workdir + "/controlPlots/"
        if not os.path.exists(plotPath):
            os.makedirs(plotPath)

        controlList = transposeLOL( transposedList[listIndex:] )
        headList = transposedList[0]
        dataList = self.lists[dataName]
        controlSamples = samples[listIndex:]
        headSamples = samples[0]

        # get labels and label texts
        labels = [plot.label for plot in self.plots]
        if isinstance(label, basestring):
            labelTexts = len(dataList)*[label]
        else:
            labelTexts = label

        # init lists
        canvases = []
        objects = []
        index = 0

        errorGraphs = []
        errorStyles = []
        errorColors = []
        
        errorBands = []
    
        # [ [ lll, fillstyle, fillcolor, doratesysts ] ]
        #lllll = [ [ lll, 3354, ROOT.kBlack, True] ]
        # loop at all samples for every plot
        for nestedName in nestedHistsConfig:
            histConfig = nestedHistsConfig[nestedName]
            nestedHistList = self.nestedHistLists[nestedName]

            errorBands.append( createErrorbands(nestedHistList, controlSamples, histConfig["doRateSysts"]) )
            errorStyles.append( histConfig["style"] )
            errorColors.append( histConfig["color"] )
            print("errorband created: "+str(errorBands[-1]))
            
        for iGraph in range(len(errorBands[0])):
            graphs = []
            for iBand in range(len(errorBands)):
                graph = [errorBands[iBand][iGraph], errorStyles[iBand], errorColors[iBand]]
                graphs.append( graph ) 
            errorGraphs.append(graphs)

        for headHist, listOfHists, listOfData, labelText, errorGraphList in zip( 
                headList, controlList, dataList, labelTexts, errorGraphs ):
            index += 1
            integralFactor = 0
            for hist, sample in zip( listOfHists, controlSamples ):
                yTitle = "Events"
                setupHist( hist, sample.color, yTitle, stack = True )

                if plotOptions["factor"] < -1 and headHist.GetName() == hist.GetName():
                    # if you stack the headHist (ontoph) to stackplot
                    # but dont want it in the integral
                    continue
                if plotOptions["factor"] < 0:
                    integralFactor += hist.Integral()

            if plotOptions["factor"] < 0:
                # check if headhist (ontoph) integral not zero
                # otherwise will give zero div. error
                if headHist.Integral() != 0:
                    integralFactor = integralFactor/headHist.Integral()
                else:
                    print( "WARNING")
                    print( "head hist (ontoph) "+str(headHist.GetName())+" has integral zero")
                    print( "this would lead to zero div. error")

            # move over/underflow
            for hist in listOfHists:
                moveOverFlow( hist )
            
            # stack
            stackedListOfHists = stackHistoList( listOfHists )
            objects.append( stackedListOfHists )

            # find maximum
            yMax = 1e-9
            for hist in stackedListOfHists:
                yMax = max( hist.GetBinContent( hist.GetMaximumBin() ), yMax )

            # init canvas
            canvas = getCanvas( stackedListOfHists[0].GetName(), plotOptions["ratio"] )
            canvas.cd(1)
        
            # draw first hist
            hist = stackedListOfHists[0]
            if plotOptions["logscale"]:
                hist.GetYaxis().SetRangeUser( yMax/10000, yMax*10 )
                canvas.cd(1).SetLogy()
            else:
                hist.GetYaxis().SetRangeUser(0, yMax*1.8)
            option = "histo"
            option+= plotOptions["canvasOptions"]
            hist.DrawCopy( option )

            for hist in stackedListOfHists[1:]:
                hist.DrawCopy(option+"same")
            hist.DrawCopy( "axissame" )

            
            # making error bars
            headHistClone = headHist.Clone()
            nok = 99999
            if plotOptions["blinded"]:
                for iBin in range(stackedListOfHists[0].GetNbinsX()):
                    if headHistClone.GetBinContent(iBin) > 0 and \
                            stackedListOfHists[0].GetBinContent(iBin)/headHistClone.GetBinContent(iBin) < 100:
                        nok = iBin - 1
                        break

            data, blind = getDataGraphBlind( listOfData, nok )

            # setup hists
            setupHist( headHistClone, headSamples.color, yTitle = "")

            headHistClone.SetBinContent(1, headHistClone.GetBinContent(0)+headHistClone.GetBinContent(1));
            headHistClone.SetBinContent(headHistClone.GetNbinsX(),
                    headHistClone.GetBinContent( headHistClone.GetNbinsX()+1 ) + \
                        headHistClone.GetBinContent( headHistClone.GetNbinsX() ));

            headHistClone.SetBinError(1, ROOT.TMath.Sqrt(
                    ROOT.TMath.Power( headHistClone.GetBinError(0), 2) + \
                        ROOT.TMath.Power( headHistClone.GetBinError(1), 2) ));
            headHistClone.SetBinError( headHistClone.GetNbinsX(), ROOT.TMath.Sqrt(
                    ROOT.TMath.Power( headHistClone.GetBinError( headHistClone.GetNbinsX()+1 ), 2) + \
                        ROOT.TMath.Power( headHistClone.GetBinError( headHistClone.GetNbinX() ), 2) ));
            headHistClone.SetLineWidth(2)   

            if plotOptions["factor"] >= 0.:
                headHistClone.Scale(plotOptions["factor"])
            else:
                headHistClone.Scape(integralFactor)

            headHistClone.Draw("histosame")
            data.Draw("samePE1")
            blind.SetFillStyle(3665)
            blind.SetLineColor(ROOT.kGray)
            blind.SetFillColor(ROOT.kGray)

            #if plotOptions["blinded"]:
                #blind.Draw("same2")
            #objects.append(blind)
   
            ratioErrorGraphs = []
            gCounter = 0
            print("doing ratio error graph")
            for errorGraph, fillStyle, fillColor in errorGraphList:
                ratioErrorGraph = ROOT.TGraphAsymmErrors( errorGraph.GetN() )
                x, y = ROOT.Double(0), ROOT.Double(0)
                for igCount in range( errorGraph.GetN() ):
                    errorGraph.GetPoint( igCount, x, 1.0 )
                    relErrUp = 0.0
                    relErrDown = 0.0
                    # check if bincontent error becomes negative
                    if (y - abs(errorGraph.GetErrorYlow(igCount))) < 0:
                        print("WARNING")
                        print("stack - error is negative in "+str(headHist.GetName())+" "+str(igCount))
                        print("with valies "+str(y)+" "+str(errorGraph.GetErrorYlow(igCount))+" \n")
                    
                    if y > 0.0:
                        relErrUp = errorGraph.GetErrorYhigh(igCount)/y
                        relErrDown = errorGraph.GetErrorYlow(igCount)/y
                        print "errUp/Down: ", relErrUp, relErrDown
                    
                    ratioErrorGraph.SetPointError(igCount, 
                            errorGraph.GetErrorXlow(igCount),
                            errorGraph.GetErrorXhigh(igCount),
                            relErrDown, relErrUp)
                    
                errorGraph.SetFillStype( fillStyle )
                errorGraph.SetLineColor( fillColor )
                errorGraph.SetFillColor( fillColor )
                ratioErrorGraph.SetFillStyle( fillStyle )
                ratioErrorGraph.SetLineColor( fillColor )
                ratioErrorGraph.SetFillColor( fillColor )
   
                #if gCounter == 0:
                    #errorGraph.Draw("2")
                #else:
                errorGraph.Draw("same2")
                graphCounter += 1

                objects.append(errorGraph)
                objects.append(ratioErrorGraph)
                ratioErrorGraphs.append(ratioErrorGraph)
                
            # writing legends
            legend1 = getLegendL()
            legend2 = getLegendR()
            
            legend1.AddEntry22(data, "data", "P")
            if plotOptions["factor"] >= 0.:
                legend2.AddEntry22( headHistClone, headSample.name+" x "+str(plotOptions["factor"]), "L")
            else:
                legend2.AddEntry22( headHistClone, headSample.name+(" x {:4.0f}").format(integralFactor), "L")
            
            ilc = 0
            for hist, sample in zip( stackedListOfHists, controlSamples ):
                ilc += 1
                if ilc%2 == 1:
                    legend1.AddEntry22(hist, sample.name, "F")
                if ilc%2 == 0:
                    legend2.AddEntry22(hist, sample.name, "F")

            canvases.append(canvas)
            legend1.Draw("same")
            legend2.Draw("same")

            objects.append(data)
            objects.append(legend1)
            objects.append(legend2)
            objects.append(headHistClone)

            # draw lumi text on canvas
            CMS_lumi.lumi_13TeV = "35.9 fb^{-1}"
            CMS_lumi.writeExtraText = 1   
            #CMS_lumi.extraText = "Preliminary"
            CMS_lumi.extraText = ""
            CMS_lumi.cmsText="CMS"
            CMS_lumi.lumi_sqrtS = "13 TeV"
            CMS_lumi.cmsTextSize = 0.55
            CMS_lumi.cmsTextOffset = 0.49
            CMS_lumi.lumiTextSize = 0.43
            CMS_lumi.lumiTextOffset = 0.61
            CMS_lumi.relPosX = 0.15
            CMS_lumi.hOffset = 0.05

            iPeriod = 4
            iPos = 0

            CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)

            label = ROOT.TLatex(0.18, 0.89, labelText);
            label.SetTextFont(42)
            label.SetTextSize(0.035)
            label.SetNDC()
            label.Draw()
            objects.append(label)

            ratioGraph, ratioMin, ratioMax = getRatioGraph( data, stackedListOfHists[0] )
            canvas.cd(2)
            line = listOfHists[0].Clone()
            line.SetFillStyle(0)
            line.Divide(listOfHists[0])

            emptyHist = listOfHists[0].Clone()
            print("empty hist name: "+str(emptyHist.GetName()))
            emptyHist.SetFillStyle(0)
            # line.GetYaxis().SetRangeUser(0.5, 1.6)
            ## with this line you can let the ratiograph scale yaxis automatically
            # line.GetYaxis().SetRangeUser(ratioMin - 0.2, ratioMax + 0.2)
            line.GetYaxis().SetRangeUser(0.4, 1.65)
            line.GetXaxis().SetRangeUser(
                listOfHists[0].GetXaxis().GetXmin(),
                    listOfHists[0].GetXaxis().GetXmax())
            for inBin in range(line.GetNbinsX()+2):
                line.SetBinContent(inBin, 1)
                line.SetBinError(inBin, 0)

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

            if "N_BTagsM" in headHistClone.GetName():
                line.GetXaxis().SetNdivisions( 505 );
            line.GetXaxis().SetTickLength( line.GetXaxis().GetTickLength() * 2.0 );
            line.GetYaxis().SetTickLength( line.GetYaxis().GetTickLength() * 1.65 );

            line.Draw("histo")
            objects.append(ratioGraph)
            for ratioErrorGraph in ratioErrorGraphs:
                ratioErrorGraph.Draw("same2")
                #objects.append(ratioErrorGraph)
            ratioGraph.Draw("sameP0")
            line.SetLineWidth(1)
            line.Draw("histosame")
            #emptyHist.GetYaxis().SetTitle("data/MC");
            line.Draw("axissame")
            #emptyhist.Draw("axissame")
            #objects.append(emptyHist)
            objects.append(line)
        
        printCanvases( canvases, plotPath )
        
        writeObjects( canvases, plotPath )    







#######################
# more util functions #
#######################


# -- misc -----------------------------------------------------------------------------------------
# get key names from root file
def GetKeyNames(self, dir = ""):
    self.cd(dir)
    return [key.GetName() for key in ROOT.gDirectory.GetListOfKeys()]
ROOT.TFile.GetKeyNames = GetKeyNames


# transpose a list of lists
def transposeLOL(lol):
    return [list(x) for x in zip(*lol)]


# -- set style of hist and its axes ---------------------------------------------------------------
def setupHist(hist, color, yTitle = None, filled = False):
    if isinstance(histo, ROOT.TH1):
        histo.SetStats(False)

    if not isinstance(histo, ROOT.TH2):
        if histo.GetYaxis().GetTitle() == "":
            if histo.GetTitle() != '':
                histo.GetXaxis().SetTitle( histo.GetTitle() )
                histo.SetTitle( '' )
            if yTitle != None:
                histo.GetYaxis().SetTitle( yTitle )

    if isinstance(histo,ROOT.TH2):
        if histo.GetXaxis().GetTitle() == "" and "VS" in histo.GetTitle():
            histo.GetXaxis().SetTitle(histo.GetTitle().split("VS",1)[0])
        if histo.GetYaxis().GetTitle() == "" and "VS" in histo.GetTitle():
            histo.GetYaxis().SetTitle(histo.GetTitle().split("VS",1)[1])
        histo.SetTitle( '' )

    histo.GetYaxis().SetTitleOffset(1.4)
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
        histo.SetFillColor(0)
        histo.SetLineWidth(2)


# -- draw list of hsts on canvas and return canvas ------------------------------------------------
def drawHistOnCanvas(listOfHistos, plotOptions):
    listOfHistos = [hist.Clone( hist.GetName()+'_drawclone' ) for hist in listOfHistos]

    # init canvas
    canvas = getCanvas(listOfHistos[0].GetName(), plotOptions["ratio"])

    # mover over/underflow
    for hist in listOfHistos:
        hist.SetBinContent(1, 
            hist.GetBinContent(0)+hist.GetBinContent(1));

        hist.SetBinContent(hist.GetNbinsX(), 
            hist.GetBinContent(hist.GetNbinsX()+1)+hist.GetBinContent(hist.GetNbinsX()));

        hist.SetBinError(1,
            ROOT.TMath.Sqrt(
                ROOT.TMath.Power( hist.GetBinError(0),2) + \
                    ROOT.TMath.Power( hist.GetBinError(1),2)));

        hist.SetBinError(hist.GetNbinsX(),
            ROOT.TMath.Sqrt(
                ROOT.TMath.Power( hist.GetBinError(hist.GetNbinsX()+1),2) + \
                        ROOT.TMath.Power( hist.GetBinError(hist.GetNbinsX()),2)));

    # scale hist
    if plotOptions["normalize"] and not plotOptions["stack"]:
        for hist in listOfHistos:
            if hist.Integral() > 0.:
                hist.Scale(1./hist.Integral())

    if plotOptions["stack"]:
        for i in range( len(listOfHistos)-1, 0, -1 ):
            listOfHistos[i-1].Add(listOfHistos[i])
        if plotOptions["normalize"]:
            integral0 = listOfHistos[0].Integral()
            for hist in listOfHistos:
                # Check if integral is not zero, since it will give a zero division error
                if integral0 != 0:
                    hist.Scale(1./integral0)
                else:
                    hist.Scale(1.)
                    print("WARNING")
                    print("integral0 variable of histogram "+str(listOfHistos[0].GetName())+" has value zero")
                    print("this would lead to zero division error")
                
    canvas.cd(1)
    yMax = 1e-9
    yMinMax = 1000.
    for hist in listOfHistos:
        yMax = max( hist.GetBinContent(hist.GetMaximumBin()), yMax)
        if hist.GetBinContent(hist.GetMaximumBin()) > 0:
            yMinMax = min(hist.GetBinContent(hist.GetMaximumBin()), yMinMax)

    #draw first
    hist0 = listOfHistos[0]
    if plotOptions["logscale"]:
        hist0.GetYaxis().SetRangeUser(yMinMax/10000,yMax*10)
        canvas.SetLogy()
    else:
        hist0.GetYaxis().SetRangeUser(0, yMax*1.5)
    option = 'histo'
    option += plotOptions["canvasOptions"]
    hist0.DrawCopy(option)

    #draw remaining
    for hist in listOfHistos[1:]:
        hist.DrawCopy(option+'same')
    hist0.DrawCopy('axissame')

    #h.DrawCopy('axissame')
    if plotOptions["ratio"]:
        canvas.cd(2)
        line = listOfHistos[0].Clone()
        line.Divide(listOfHistos[0])
        line.GetYaxis().SetRangeUser(0.5, 1.5)
        line.GetYaxis().SetTitle('#frac{Data}{MC Sample}')
        line.GetXaxis().SetLabelSize(line.GetXaxis().GetLabelSize()*2.4)
        line.GetYaxis().SetLabelSize(line.GetYaxis().GetLabelSize()*2.4)
        line.GetXaxis().SetTitleSize(line.GetXaxis().GetTitleSize()*3)
        line.GetYaxis().SetTitleSize(line.GetYaxis().GetTitleSize()*1.5)
        line.GetYaxis().SetTitleOffset(0.9)
        line.GetYaxis().SetNdivisions(505)
        for i in range(line.GetNbinsX()+1):
            line.SetBinContent(i, 1)
            line.SetBinError(i, 0)
        line.SetLineWidth(1)
        line.DrawCopy('histo')
        for hist in listOfHistos[1:]:
            ratioPlot = hist.Clone()
            ratioPlot.Divide(listOfHistos[0])
            ratioPlot.DrawCopy('sameP')
        canvas.cd(1)
    return canvas



# -- create canvas with or without ratiopad -------------------------------------------------------
def getCanvas(name, ratiopad=False):
    if ratiopad:
        canvas = ROOT.TCanvas(name, name, 1024, 1024)
        canvas.Divide(1,2)
        canvas.cd(1).SetPad(0.,0.3,1.0,1.0);
        canvas.cd(1).SetTopMargin(0.07);
        canvas.cd(1).SetBottomMargin(0.0);

        canvas.cd(2).SetPad(0.,0.0,1.0,0.3);
        canvas.cd(2).SetTopMargin(0.0);
        canvas.cd(2).SetBottomMargin(0.4);

        canvas.cd(1).SetRightMargin(0.05);
        canvas.cd(1).SetLeftMargin(0.15);
        canvas.cd(1).SetTicks(1,1)

        canvas.cd(2).SetRightMargin(0.05);
        canvas.cd(2).SetLeftMargin(0.15);
        canvas.cd(2).SetTicks(1,1)
    else:
        canvas = ROOT.TCanvas(name, name, 1024, 768)
        canvas.SetTopMargin(0.07)
        canvas.SetBottomMargin(0.15)
        canvas.SetRightMargin(0.05)
        canvas.SetLeftMargin(0.15)
        canvas.SetTicks(1,1)
    return canvas





# -- legend functions -----------------------------------------------------------------------------
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





# -- addEntry functions ---------------------------------------------------------------------------
def AddEntry2( self, histo, label, option = 'L'):
    self.SetY1NDC( self.GetY1NDC()-0.045 )
    width = self.GetX2NDC() - self.GetX1NDC()
    ts = self.GetTextSize()
    neglen = 0
    sscripts = re.findall("_{.+?}|\^{.+?}", label)

    for s in sscripts:
	neglen = neglen + 3
    symbols = re.findall("#[a-zA-Z]+", label)
    for symbol in symbols:
	neglen = neglen + len(symbol)-1

    newwidth = max( (len(label) - neglen) * 0.015 * 0.05 / ts + 0.1, width )
    self.SetX1NDC(self.GetX2NDC() - newwidth)

    self.AddEntry(histo, label, option)
ROOT.TLegend.AddEntry2 = AddEntry2


def AddEntry22( self, histo, label, option = 'L'):
    self.SetY1NDC( self.GetY1NDC()-0.045 )
    width = self.GetX2NDC() - self.GetX1NDC()
    ts = self.GetTextSize()
    neglen = 0
    sscripts = re.findall("_{.+?}|\^{.+?}", label)

    for s in sscripts:
	neglen = neglen + 3
    symbols = re.findall("#[a-zA-Z]+", label)
    for symbol in symbols:
	neglen = neglen + len(symbol)-1

    newwidth = max( (len(label) - neglen) * 0.015 * 0.05 / ts + 0.1, width )

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






# -- get sepa and stat tests ----------------------------------------------------------------------
def getSepaTests2(histos, head):
    y = 0
    tests = []
    for hist in histos:
        pair = getSuperHistoPair( [head], [hist], 'tmp')
        roc = getROC(*pair)
        rocint = roc.Integral()+0.5
        test = ROOT.TLatex(0.2, 0.9-y, 'ROC integral: '+str(round(rocint, 3)) );
        y += 0.05
        test.SetTextFont(42);
        test.SetTextSize(0.04);
        test.SetNDC()
        tests.append(test)
    return tests


def getStatTests(hist1, hist2, option = "WW"):
    ksprob = h1.KolmogorovTest(hist2)
    chi2prob = h1.Chi2Test(hist2, option)

    tests = ROOT.TLatex(0.2, 0.8, 
            '#splitline{p(KS): '+str(round(ksprob,3))+'}{p(chi2): '+str(round(chi2prob,3))+'}'  );
    tests.SetTextFont(42);
    tests.SetTextSize(0.03);
    tests.SetNDC()
    return tests

def getSepaTests(hist1,hist2):
    pair = hist1, hist2
    roc = getROC(*pair)
    rocint = roc.Integral()+0.5

    tests = ROOT.TLatex(0.2, 0.9, 'ROC integral: '+str(round(rocint,3)));
    tests.SetTextFont(42);
    tests.SetTextSize(0.05);
    tests.SetNDC()
    return tests


# -- create one sig and bkg sample from all sig and bkg hists -------------------------------------
def getSuperHistoPair(histosS, histosB, name):
    superbins = []
    for histS, histB in zip(histosS,histosB):
        nBins = histS.GetNbinsX()
        for i in range(1, nBins+1):
            s = histS.GetBinContent(i)
            b = histB.GetBinContent(i)
            if (b != 0):
                superbins.append( (s/b, s, b) )
            elif (s != 0):
                superbins.append( (float("inf"), s, b) )

    superbins_sorted = sorted(superbins, key = lambda b: b[0])

    superhistoS = ROOT.TH1F(
            'superhistoS_'+name, 
            'superhistoS_'+name,
            len(superbins_sorted),
            -0.5,
            len(superbins_sorted) - 0.5)
    superhistoB = ROOT.TH1F(
            'superhistoB_'+name,
            'superhistoB_'+name,
            len(superbins_sorted),
            -0.5,
            len(superbins_sorted) - 0.5)

    for i in range(len(superbins)):
        superhistoS.SetBinContent(i+1, superbins_sorted[i][1])
        superhistoB.SetBinContent(i+1, superbins_sorted[i][2])
    return (superhistoS,superhistoB)


# -- calc ROC values ------------------------------------------------------------------------------
def getROC(histo1, histo2, rej = True):
    nBins = histo1.GetNbinsX()
    nBins2 = histo2.GetNbinsX()
    integral1 = histo1.Integral(0,nBins+1)
    integral2 = histo2.Integral(0,nBins2+1)

    nonZeroBins = []
    for i in range(nBins, -1, -1):
        if histo1.GetBinContent(i) > 0. or histo2.GetBinContent(i) > 0.:
            nonZeroBins.append(i)

    roc = ROOT.TGraphAsymmErrors( len(nonZeroBins)+1 )
    if rej:
        roc.SetPoint(0,0,1)
    else:
        roc.SetPoint(0,0,0)
    point = 1
    for i in nonZeroBins:
        eff1 = 0
        eff2 = 0
        if integral1 > 0:
            eff1 = histo1.Integral(i, nBins+1)/integral1
        if integral2 > 0:
            eff2 = histo2.Integral(i, nBins+1)/integral2
        if rej:
            roc.SetPoint(point, eff1, 1-eff2)
        else:
            roc.SetPoint(point, eff1, eff2)
        point += 1

    return roc





# -- write canvases to pdf and root ---------------------------------------------------------------
def printCanvases(canvases, plotPath):
    plotPath += "/plots"
    canvas = canvases[0]
    canvas.Print( plotPath+'.pdf[')
    for c in canvases:
        canvas = c
        canvas.Print( plotPath+'.pdf')
        #canvas.SaveAs(name+"/"+c.GetName()+'.png')

    canvas.Print( plotPath+'.pdf]')
    if not os.path.exists( plotPath ):
        os.makedirs( plotPath )
    for c in canvases:
        c.Print( plotPath +'/'+("_".join(((c.GetName()).split('_'))[1:]))+".pdf")
        c.SaveAs( plotPath +'/'+("_".join(((c.GetName()).split('_'))[1:]))+".png")

def writeObjects(objects, plotPath):
    plotPath += "/rootfiles/"
    if not os.path.exists(plotPath):
        os.makedirs(plotPath)
    for o in objects:
        outfile = ROOT.TFile(plotPath + o.GetName() + '.root','recreate')
        o.Write()
        outfile.Close()




# -- creating errorbands --------------------------------------------------------------------------
def createErrorbands(nestedHistList, samples, doRateSysts = True):
    print "creating errorbands"
    if doRateSysts:
        print "using ratesysts"
    errorBand = []
    for ll in nestedHistList: #for all plots
        llT = transposeLOL(ll)
        nominal = llT[0][0].Clone()
        print("Creating error band for "+str(nominal.GetName()))
        for hist in llT[0][1:]:
            nominal.Add(hist)
        systs = []
        for l in llT[1:]: #for all systematics
            syst = l[0].Clone()
            for hist in l[1:]:
                syst.Add(hist)
		print("adding to errorband (h, int, nominal.int)")
		print hist, hist.Integral(), nominal.Integral()
            systs.append(syst)
        assert len(samples) == len(llT[0])
        for isample, sample in enumerate(samples): # for all normalization unc
	    ls = []
	    for ihisto, hist in enumerate(llT[0]):
		ls.append(hist.Clone())
		if ihisto == isample:
		    if doRateSysts:
		        ls[-1].Scale(1 + sample.unc_up)
	    syst = ls[0].Clone()
	    for hist in ls[1:]:
		syst.Add(hist)
	    systs.append(syst)

	    ls = []
	    for ihisto, hist in enumerate(llT[0]):
		ls.append(hist.Clone())
		if ihisto==isample:
		    if doRateSysts:
		        ls[-1].Scale(1 - sample.unc_down)
	    syst = ls[0].Clone()
	    for hist in ls[1:]:
		syst.Add(hist)
	    #print "rates ", sample.nick, syst.Integral()
	    systs.append(syst)

        uperrors = [0]*ll[0][0].GetNbinsX()
        downerrors = [0]*ll[0][0].GetNbinsX()

        for ibin in range(0, nominal.GetNbinsX()):
            nerr = nominal.GetBinError(ibin+1)
            uperrors[ibin] = ROOT.TMath.Sqrt( uperrors[ibin]*uperrors[ibin] + nerr*nerr )
            downerrors[ibin] = ROOT.TMath.Sqrt( downerrors[ibin]*downerrors[ibin] + nerr*nerr )
            n = nominal.GetBinContent(ibin+1)
            ups = systs[0::2]
            downs = systs[1::2]
            for up, down in zip(ups, downs):
	        print "up/down name ", up.GetName(), down.GetName()
	        print "up/down diff ",  up.GetBinContent(ibin+1)-n, down.GetBinContent(ibin+1)-n
                u_ = up.GetBinContent(ibin+1)-n
                d_ = down.GetBinContent(ibin+1)-n
                #print u_,d_
                # TODO that shit sucks
                if u_ >= 0 and u_ >= d_:
                    u = u_
                    if d_ < 0:
                        d = d_
                    else:
                        d = 0
                elif u_ >= 0 and u_ <= d_:
                    u = d_
                    d = 0
                elif u_ < 0 and d_ <= u_:
                    d = d_
                    u = 0
                elif u_ < 0 and u_ < d_:
                    d = u_
                    if d_ >= 0:
		        u = d_
		    else:
                        u = 0

                uperrors[ibin] = ROOT.TMath.Sqrt( uperrors[ibin]*uperrors[ibin] + u*u )
                downerrors[ibin] = ROOT.TMath.Sqrt( downerrors[ibin]*downerrors[ibin] + d*d)
                print u, d
                print "up/down errors ", uperrors[ibin],downerrors[ibin]

        graph = ROOT.TGraphAsymmErrors(nominal)
        for i in range(len(uperrors)):
            graph.SetPointEYlow(i, downerrors[i])
            graph.SetPointEYhigh(i, uperrors[i])
            graph.SetPointEXlow(i, nominal.GetBinWidth(i+1)/2.)
            graph.SetPointEXhigh(i, nominal.GetBinWidth(i+1)/2.)

        errorBand.append(graph)
    return errorBand





# -- functions for creating control plots ---------------------------------------------------------
def moveOverFlow(hist):
    #h.SetBinContent(1,h.GetBinContent(0)+h.GetBinContent(1));
    hist.SetBinContent(hist.GetNbinsX(), 
        hist.GetBinContent( hist.GetNbinsX()+1 ) + hist.GetBinContent( hist.GetNbinsX() ) );
    #h.SetBinError(1,ROOT.TMath.Sqrt(ROOT.TMath.Power(h.GetBinError(0),2)+ROOT.TMath.Power(h.GetBinError(1),2)));
    hist.SetBinError( hist.GetNbinsX(), 
        ROOT.TMath.Sqrt( 
            ROOT.TMath.Power( hist.GetBinError( hist.GetNbinsX()+1 ), 2) + \
                ROOT.TMath.Power( hist.GetBinError( hist.GetNbinsX() ), 2) ));


def stackHistoList(listOfHistos_, normalize = False):
    listOfHistos=[]
    for hist in listOfHistos_:
        listOfHistos.append( hist.Clone(hist.GetName()+"_stack") )
    for i in range(len(listOfHistos)-1, 0, -1):
        listOfHistos[i-1].Add(listOfHistos[i])
    if normalize:
        integral0 = listOfHistos[0].Integral()
        for hist in listOfHistos:
            # Check if integral is not null, since it will give a zero division error
            if integral0 != 0:
                hist.Scale(1./integral0)
            else:
                hist.Scale(1.)
                print("WARNING")
                print("integral0 variable of hist "+str(listOfHistos[0].GetName())+" has value zero")
                print("this would lead to zero div. error")
    return listOfHistos


def getDataGraphBlind(listOfHistosData, nunblinded, verbosity=0):
    print "blind after point ", nunblinded
    if len(listOfHistosData) > 0:
        datahisto = listOfHistosData[0].Clone()
    for d in listOfHistosData[1:]:
        datahisto.Add(d)
    moveOverFlow(datahisto)
    data = ROOT.TGraphAsymmErrors(datahisto)
    alpha = 1 - 0.6827
    for i in range(0, data.GetN()):
        N = data.GetY()[i];
        L = 0
        if N != 0:
            L = ROOT.Math.gamma_quantile(alpha/2, N, 1.)

        U =  ROOT.Math.gamma_quantile_c(alpha/2, N+1, 1)
        data.SetPointEYlow(i, N-L);
        data.SetPointEYhigh(i, U-N);
        if verbosity >= 2:
            print i, N-L, U-N

    data.SetMarkerStyle(20)
    data.SetMarkerSize(1.3)
    data.SetLineWidth(3)
    data.SetMarkerColor(ROOT.kBlack)
    data.SetLineColor(ROOT.kBlack)
    blind_band = ROOT.TGraphAsymmErrors( datahisto.GetNbinsX()-nunblinded )
    j = 0
    x, y = ROOT.Double(0), ROOT.Double(0)
    for i in range(data.GetN()):
        data.GetPoint(i, x, y)
        if verbosity >= 2:
            print datahisto, x, y
    if verbosity >= 2:
        print data.GetN()
        print datahisto.GetNbinsX()
    x, y = ROOT.Double(0), ROOT.Double(0)
    for i in range(data.GetN()):
        #data.SetPointEXlow(i,0)
        #data.SetPointEXhigh(i,0)
        if i >= nunblinded:
            data.GetPoint(nunblinded, x, y)
            print i, datahisto, x, y
            blind_band.SetPoint(j, x, 0)
            blind_band.SetPointEYlow(j, 0)
            blind_band.SetPointEYhigh(j, 200000)
            blind_band.SetPointEXlow(j, datahisto.GetBinWidth(1)/2)
            blind_band.SetPointEXhigh(j,datahisto.GetBinWidth(1)/2)
            print "remove ", data.RemovePoint(nunblinded), data.GetN()
            j += 1
    x, y = ROOT.Double(0), ROOT.Double(0)
    if verbosity >= 2:
        print "done removing"
    for i in range(data.GetN()):
        data.GetPoint(i, x, y)
        if verbosity >= 2:
            print datahisto, x, y
        data.SetPointEXlow(i, 0)
        data.SetPointEXhigh(i, 0)
    if verbosity >= 2:
        print data.GetN()
    return data, blind_band
    # TODO: proper y-errors


def getRatioGraph(data, mchisto):
    print "creating ratio ", mchisto
    ratio = data.Clone()
    x, y = ROOT.Double(0), ROOT.Double(0)
    minimum = 9999.
    maximum = -9999.
    for i in range(0, data.GetN()):
        data.GetPoint(i, x, y)
        currentBin = mchisto.FindBin(x)
        currentBinContent = mchisto.GetBinContent(currentBin)
        #if mchisto.GetBinContent(i+1) > 0:
            #ratioval = y/mchisto.GetBinContent(i+1)
        if currentBinContent > 0:
            ratioval = y/currentBinContent
            ratio.SetPoint(i, x, ratioval)
            if ratioval > maximum and ratioval > 0:
              maximum = round(ratioval, 1);
            if ratioval < minimum and ratioval > 0:
              minimum = round(ratioval, 1);
        else:
            ratio.SetPoint(i, x, -999)

        if y > 0:
            #ratio.SetPointEYlow( i, 1 - (y-data.GetErrorYlow(i)) / y )
            #ratio.SetPointEYhigh( i, (y+data.GetErrorYhigh(i)) / y - 1 )
            if currentBinContent > 0:
              ratio.SetPointEYlow(i, data.GetErrorYlow(i)/currentBinContent)
              ratio.SetPointEYhigh(i, data.GetErrorYhigh(i)/currentBinContent)
            else:
	      ratio.SetPointEYlow( i, 1 - (y-data.GetErrorYlow(i)) / y )
              ratio.SetPointEYhigh( i, (y + data.GetErrorYhigh(i)) / y - 1 )
            
        else:
            ratio.SetPointEYlow(i, 0)
            ratio.SetPointEYhigh(i, 0)
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
    return ratio, minimum, maximum
# -------------------------------------------------------------------------------------------------
