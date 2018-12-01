import ROOT
import math
from itertools import product
import subprocess
import os
import sys
import re
from string import join

ROOT.gStyle.SetPaintTextFormat("4.2f");
ROOT.gROOT.SetBatch(True)

# local imports
filedir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(filedir+"/tools")
import CMS_lumi
import plotClasses

class Config:
    def __init__(self, name, index):
        self.name = name
        self.index = index

class List:
    def __init__(self, genPlots, samples, listName, catNames = [""], doTwoDim = False):
        self.catNames = catNames
        self.plots = genPlots.plots
        self.rebin = genPlots.rebin
        self.doTwoDim = doTwoDim

        self.name = listName
        self.samples = samples

        rootFile = ROOT.TFile(genPlots.outPath, "readonly")
        keyList = rootFile.GetKeyNames()
        print("generating new list with name "+str(listName))
        print("category names:")
        print(catNames)

        dataT = []
        # generate hist list per sample
        print("looping over samples ...")
        for sample in samples:
            print("at sample "+str(sample))
            histList = self.fillHistList(rootFile, sample, keyList)
            print("histList: "+str(histList))
            dataT.append(histList)
            print("dataT: "+str(dataT))
            print("-"*10)
        # generate transposed list
        self.data = transposeLOL( dataT )
        self.T = transposeLOL( self.data )
        print("list:")
        print(self.data)
        print("list.T:")
        print(self.T)
        print("-"*30)

    def fillHistList(self, rootFile, sample, keyList):
        histList = []
        ROOT.gDirectory.cd("PyROOT:/")
        for cat in self.catNames:
            for plot in self.plots:
                print("="*10)
                print("creating histogram")
                print("cat: "+str(cat))
                print("plot: "+str(plot))
                print("sample: "+str(sample))
                key = sample.nick+"_"+cat+plot.name
                print("key: "+str(key))
                if key not in keyList:
                    print("this key is not in key list")
                rootHist = rootFile.Get(key)
                print("type of hist is:")
                print( type( rootHist ))
                if isinstance(rootHist, ROOT.TH1) and not isinstance(rootHist, ROOT.TH2):
                    print("is TH1")
                    rootHist.Rebin(self.rebin)
                    histList.append( rootHist.Clone() )
                if self.doTwoDim and isinstance(rootHist, ROOT.TH2):
                    print("is TH2")
                    histList.append( rootHist.Clone() )
        return histList

class genPlots:
    def __init__(self, outPath, plots, plotdir, rebin):
        self.outPath = outPath
        self.plots = plots
        self.plotdir = plotdir
        self.rebin = 1

        self.lists = {}
        self.samples = {}
        self.nestedHistLists = {}


    # -- functions for setting up lists -----------------------------------------------------------
    # old def createHistoLists_fromSuperHistoFile
    def genList(self, samples, listName, catNames = [""], doTwoDim = False):
        newList = List(self, samples, listName, catNames, doTwoDim)
    
        self.lists[newList.name] = newList
        return newList.name


    # -- loading options for simple control/shape plots -------------------------------------------
    def loadOptions(self, options):
        defaultOptions = {
            "factor":           -1,
            "logscale":         False,
            "canvasOptions":    "histo",
            "normalize":        False,
            "stack":            False,
            "ratio":            False,
            "doProfile":        False,
            "statTest":         False,
            "sepaTest":         False,
            "blinded":          True}

        # set options
        for opt in defaultOptions:
            if opt in options:
                defaultOptions[opt] = options[opt]
                print(str(opt)+" set to "+str(options[opt]))

        return defaultOptions
    # ---------------------------------------------------------------------------------------------



    # -- making simple control/shape plots --------------------------------------------------------
    # old def writeLOLAndOneOnTop
    def makeSimpleControlPlots(self, dataConfig, options = {}):
        print("\n"+"="*30)
        print("making simple control plots ...")
        # load options
        print("-"*10)
        print("loading options:")
        plotOptions = self.loadOptions(options)
        listName = dataConfig.name
        listIndex = dataConfig.index
        print("-"*10)

        # load transposed list#
        transposedList = self.lists[listName].T
        samples = self.lists[listName].samples
        print("transposedList")
        print(transposedList)

        # generate stuff for control plots
        plotPath = self.plotdir + "/simpleControlPlots/"
        if not os.path.exists(plotPath):
            os.makedirs(plotPath)
        print("plots output: "+str(plotPath+"plots.pdf"))

        controlList = transposeLOL( transposedList[listIndex:] )
        headList = transposedList[0]
        controlSamples = samples[listIndex:]
        headSamples = samples[0]
        # starting draw control plots
        canvases = []
        objects = []
        index = 0
        
        # start loop over used list
        print("looping over used histolist ...")
        for listOfHists, headHist in zip(controlList, headList):
            print("listOfHists:" +str(listOfHists))
            print("headHist: "+str(headHist))
            print

            index += 1
            integralFactor = 0

            # start loop over histos in listofhists
            for hist, sample in zip(listOfHists, controlSamples):
                yTitle = 'Events expected for 41.5 fb^{-1} @ 13 TeV'

                # stup histogram
                setupHist( hist, sample.color, yTitle, plotOptions["stack"] )
                
                if plotOptions["factor"] < 0:
                    integralFactor += hist.Integral()

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
            setupHist(headCanvas, headSamples.color, yTitle = "")

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
                legend2.addEntryLRLegend(headCanvas, headSamples.name+" x "+str(plotOptions["factor"]), "L")
            else:
                legend2.addEntryLRLegend(headCanvas, headSamples.name+(' x {:4.0f}').format(integralFactor), "L")
            
            index = 0
            for hist, sample in zip(listOfHists, controlSamples):
                index += 1
                if index%2 == 1:
                    legend1.addEntryLRLegend(hist, sample.name, "F")
                if index%2 == 0:
                    legend2.addEntryLRLegend(hist, sample.name, "F")
            
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
            if plotOptions["sepaTest"]:
                sepTests = getSepaTests2(listOfHists, headHist)
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
        print("done with loop")
        print("printing canvases")
        printCanvases(canvases, plotPath)
        
        # write all objects
        print("writing objects")
        writeObjects(canvases, plotPath)


    # old def writeListOfHistoListsAN
    def makeSimpleShapePlots(self, dataConfig, label = "", options = {}):
        print("\n"+"="*30)
        print("making simple shape plots ...")
        # load options
        print("loading options:")
        plotOptions = self.loadOptions(options)
        listName = dataConfig.name
        listIndex = dataConfig.index

        # load transposed list
        transposedList = self.lists[listName].T
        samples = self.lists[listName].samples
        print("transposedList")
        print(transposedList)

        # generate stuff for shape plots    
        plotPath = self.plotdir + "/simpleShapePlots/"
        if not os.path.exists(plotPath):
            os.makedirs(plotPath)
        print("plots output: "+str(plotPath+"plots.pdf"))

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
        print("looping over used histolist ...")
        for listOfHists, labelText in zip( shapeList, labelTexts):
            print("listOfHists: "+str(listOfHists))
            print("labelText: "+str(labelText))
            print
         
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
                legend.AddEntryLegend( hist, sample.name, legendOpt )

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
            cms = ROOT.TLatex(0.2, 0.96, "CMS preliminary,  41.5 fb^{-1},  #sqrt{s} = 13 TeV" );
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

        print("done with loop")
        print("printing canvases")
        printCanvases(canvases, plotPath)

        # write all objects
        print("writing objects")
        writeObjects(canvases, plotPath)
    # ---------------------------------------------------------------------------------------------





    # -- making control plots ---------------------------------------------------------------------
    # old def createLLL_fromSuperHistoFileSyst
    def genNestedHistList(self, dataConfig, systNames, outName):
        rootFile = ROOT.TFile(self.outPath, "readonly")
        listName = dataConfig.name
        listIndex = dataConfig.index

        objects = []
        keyList = rootFile.GetKeyNames()
        outList = []

        controlSamples = self.lists[listName].samples[listIndex:]
        
        # looping over discr plots
        for plot in self.plots:
            nestedList = []
            print("creating nested list for plot " + str(plot.name))
            for sample in controlSamples:
                nominalKey = sample.nick+"_"+plot.name+systNames[0]
                nominal = rootFile.Get(nominalKey)

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
        print("location: self.nestedHistList["+str(outName)+"]")
        print
        self.nestedHistLists[outName] = outList


    # old def plotDataMCanWsyst
    # def makeControlPlots(self, listName, listIndex, dataName, nestedHistsConfig, options):
    def makeControlPlots(self, dataConfig, controlConfig, sampleConfig, headHist, headSample, nestedHistsConfig, options = {}, outName = "controlPlots"):
        print("\n"+"="*30)
        print("making control plots ...")
        # load options
        print("loading options:")
        plotOptions = self.loadOptions(options)

        # set the used lists
        # dataList was listOfHistoListsData
        dataList = self.lists[ dataConfig.name ].data
        
        # controlList was listOfHistoLists
        transposedList = self.lists[ controlConfig.name ].T
        controlList = transposeLOL( transposedList[controlConfig.index:] )

        # controlSamples was samples
        samples = self.lists[ sampleConfig.name ].samples
        controlSamples = samples[sampleConfig.index:]

        # headList was listOfhistosOnTop
        transposedList = self.lists[headHist].T
        headList = transposedList[0]

        # headSamples was sampleOnTop
        samples = self.lists[headSample].samples
        headSamples = samples[0]

        # generate stuff for control plots
        plotPath = self.plotdir + "/"+str(outName)+"/"
        if not os.path.exists(plotPath):
            os.makedirs(plotPath)
        print("plots output: "+str(plotPath+"plots.pdf"))

        # get labels and label texts
        labels = [plot.label for plot in self.plots]
        if isinstance(labels, basestring):
            labelTexts = len(dataList)*[labels]
        else:
            labelTexts = labels

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
                setupHist( hist, sample.color, yTitle, True )

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
                        ROOT.TMath.Power( headHistClone.GetBinError( headHistClone.GetNbinsX() ), 2) ));
            headHistClone.SetLineWidth(2)   

            if plotOptions["factor"] >= 0.:
                headHistClone.Scale(plotOptions["factor"])
            else:
                headHistClone.Scale(integralFactor)

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
                    errorGraph.GetPoint( igCount, x, ROOT.Double(1.0) )
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
                    
                errorGraph.SetFillStyle( fillStyle )
                errorGraph.SetLineColor( fillColor )
                errorGraph.SetFillColor( fillColor )
                ratioErrorGraph.SetFillStyle( fillStyle )
                ratioErrorGraph.SetLineColor( fillColor )
                ratioErrorGraph.SetFillColor( fillColor )
   
                #if gCounter == 0:
                    #errorGraph.Draw("2")
                #else:
                errorGraph.Draw("same2")
                gCounter += 1

                objects.append(errorGraph)
                objects.append(ratioErrorGraph)
                ratioErrorGraphs.append(ratioErrorGraph)
                
            # writing legends
            legend1 = getLegendL()
            legend2 = getLegendR()
            
            legend1.addEntryLRLegend(data, "data", "P")
            if plotOptions["factor"] >= 0.:
                legend2.addEntryLRLegend( headHistClone, headSamples.name+" x "+str(plotOptions["factor"]), "L")
            else:
                legend2.addEntryLRLegend( headHistClone, headSamples.name+(" x {:4.0f}").format(integralFactor), "L")
            
            ilc = 0
            for hist, sample in zip( stackedListOfHists, controlSamples ):
                ilc += 1
                if ilc%2 == 1:
                    legend1.addEntryLRLegend(hist, sample.name, "F")
                if ilc%2 == 0:
                    legend2.addEntryLRLegend(hist, sample.name, "F")

            print("appending canvas "+str(canvas))
            canvases.append(canvas)
            legend1.Draw("same")
            legend2.Draw("same")

            objects.append(data)
            objects.append(legend1)
            objects.append(legend2)
            objects.append(headHistClone)

            # draw lumi text on canvas
            CMS_lumi.lumi_13TeV = "41.5 fb^{-1}"
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
        
        print("done with loop")
        print("printing canvases")
        printCanvases(canvases, plotPath)

        # write all objects
        print("writing objects")
        writeObjects(canvases, plotPath)


    def makeEventYields(self, categories, listName, dataName, nameRequirements = []):
        histoList = self.lists[listName].data  
        dataList = self.lists[dataName].data
        samples = self.lists[listName].samples

        path = self.plotdir+"/eventYields"
        if not os.path.exists( path ):
            os.makedirs(path)
        print("looping over data and histoLists:")
        for data, hist in zip(dataList, histoList):
            print("-"*10)
            print("now at dataList entry:")
            print(data)
            print("-"*10)

            # check if name requirement is met
            req_met = False
            if nameRequirements == []:
                req_met = True
            for req in nameRequirements:
                if req in data[0].GetName():
                    req_met = True
            if not req_met:
                continue

            name = data[0].GetName()
            for h in data+hist:
                for iCat, cat in enumerate(categories):
                    h.GetXaxis().SetBinLabel(iCat+1, cat[1])

            eventYields( data, hist, samples, path, name ) 




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
# old def setupHisto
def setupHist(histo, color, yTitle = None, filled = False):
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
# old def drawHistosOnCanvas
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

'''
def getCanvasLowRes(name, ratiopad = False):
    if ratiopad:
        c = ROOT.TCanvas(name, name, 800, 600)
        c.Divide(1, 2)
        c.cd(1).SetPad(0., 0.3, 1.0, 1.0);
        c.cd(1).SetBottomMargin(0.0);
        c.cd(2).SetPad(0., 0.0, 1.0, 0.3);
        c.cd(2).SetTopMargin(0.0);
        c.cd(1).SetTopMargin(0.05);
        c.cd(2).SetBottomMargin(0.4);
        c.cd(1).SetRightMargin(0.05);
        c.cd(1).SetLeftMargin(0.15);
        c.cd(2).SetRightMargin(0.05);
        c.cd(2).SetLeftMargin(0.15);
    else:
        c = ROOT.TCanvas(name, name, 800, 600)
        c.SetRightMargin(0.05)
        c.SetTopMargin(0.05)
        c.SetLeftMargin(0.15)
        c.SetBottomMargin(0.15)
    return c
'''


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
def AddEntryLegend( self, histo, label, option = 'L'):
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
ROOT.TLegend.AddEntryLegend = AddEntryLegend


def addEntryLRLegend( self, histo, label, option = 'L'):
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
ROOT.TLegend.addEntryLRLegend = addEntryLRLegend


# deleted versions: 
# def AddEntry4545
# def AddEntry3
# def AddEntry4
# renamed def AddEntry22 -> AddEntryLRLegend
# renamed def AddEntry2  -> addEntryLegend


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


def getSepaTests(hist1,hist2):
    pair = hist1, hist2
    roc = getROC(*pair)
    rocint = roc.Integral()+0.5

    tests = ROOT.TLatex(0.2, 0.9, 'ROC integral: '+str(round(rocint,3)));
    tests.SetTextFont(42);
    tests.SetTextSize(0.05);
    tests.SetNDC()
    return tests


def getStatTests(hist1, hist2, option = "WW"):
    ksprob = hist1.KolmogorovTest(hist2)
    chi2prob = hist1.Chi2Test(hist2, option)

    tests = ROOT.TLatex(0.2, 0.8, 
            '#splitline{p(KS): '+str(round(ksprob,3))+'}{p(chi2): '+str(round(chi2prob,3))+'}'  );
    tests.SetTextFont(42);
    tests.SetTextSize(0.03);
    tests.SetNDC()
    return tests


'''
def getStatTestsList(h1, lh2, option = "WW"):
    mystrng = ''
    ss = []
    for h2 in lh2:
        ksprob = h1.KolmogorovTest(h2)
        chi2prob = h1.Chi2Test(h2,option)
        string = 'p(KS): '+str(round(ksprob,3))+'   p(chi2): '+str(round(chi2prob,3))
        ss.append( string )
    if len(ss) == 1:
        mystrng = ss[0]
    else:
        mystrng = '#splitline{'+ss[0]+'}{secline}'
        for isss, sss in enumerate(ss[1:]):
          submystrng = '#splitline{'+sss+'}{secline}'
          if isss == (len(ss[1:])-1):
              mystrng = mystrng.replace('secline',sss)
          else:
            mystrng = mystrng.replace('secline',submystrng)
    tests = ROOT.TLatex(0.2, 0.8, mystrng  );
    tests.SetTextFont(42);
    tests.SetTextSize(0.04);
    tests.SetNDC()
    return tests
'''


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
    print("canvases:")
    print(canvases)
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

'''
def printCanvasesPNG(canvases,name):

    name = name.replace("/","")
    if not os.path.exists(name):
        os.makedirs(name)
    for c in canvases:
        c.Print(name+'/'+("_".join(((c.GetName()).split('_'))[2:]))+".png")
'''


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
		#print("adding to errorband (h, int, nominal.int)")
		#print hist, hist.Integral(), nominal.Integral()
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
	        #print "up/down name ", up.GetName(), down.GetName()
	        #print "up/down diff ",  up.GetBinContent(ibin+1)-n, down.GetBinContent(ibin+1)-n
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
                #print u, d
                #print "up/down errors ", uperrors[ibin],downerrors[ibin]

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





# ---------------------
# stuff for eventYields
# ---------------------
def eventYields(data, hists, samples, path, name, withError = True, makeRatios = True):
    tablePath = path + "/"+name+"_yields"
    histData = data[0].Clone()
    for h in data[1:]:
        histData.Add(h)
    
    sampleData = plotClasses.Sample("data")
    bkgSample = plotClasses.Sample("Total bkg")
    bkgHist = hists[1].Clone()
    for h in hists[2:]:
        bkgHist.Add( h.Clone() )

    histsForTable = hists[1:]+[bkgHist]+[hists[0]]+[histData]
    samplesForTable = samples[1:]+[bkgSample]+[samples[0]]+[sampleData]

    # alternative from eventYieldsNew
    #bkgSample = samples[-1]
    #bkgHist = hists[-1]
    #histsForTable = hists[1:]+[hists[0]]+[histData]
    #samplesForTable = samples[1:]+[samples[0]]+[samplesData]

    histRatio = None
    if makeRatios:
        histRatio = hists[0].Clone()
        histRatio.Divide( bkgHist )
        sRatio = plotClasses.Sample( "S/B" )
        
        hRatioData = histData.Clone()
        hRatioData.Divide( bkgHist )

        sRatioData = plotClasses.Sample("data/B")

        histsForTable += [histRatio, hRatioData]
        samplesForTable += [sRatio, sRatioData]

    turn1DHistsToTable(
        hists = histsForTable,
        samples = samplesForTable,
        outFile = tablePath,
        withError = withError)

    cmd = ["pdflatex", "-output-directory", path, tablePath+".tex"]
    print("calling pdflatex...")
    print( " ".join(cmd) )
    subprocess.call(cmd)


def turn1DHistsToTable(hists, samples, outFile, withError = True):
    with open( outFile+".tex", "w") as out:
        out.write('\\documentclass{article}\n')
        
        paperWidth = hists[0].GetNbinsX()*2.2 + 10
        out.write('\\usepackage[paperwidth=' + str(paperWidth) + 'cm, paperheight=23cm, top=2.5cm, bottom=2.5cm, left=2.5cm, right=2.5cm]{geometry}\n')

        out.write('\\begin{document}\n')
        out.write('\\thispagestyle{empty}\n')
        out.write('\\footnotesize\n')

        cls = ["Process"]
        for i in range(1, hists[0].GetNbinsX()+1):
            cls.append( hists[0].GetXaxis().GetBinLabel(i) )

        writeHead(out, cls)

        for hist, sample in zip(hists, samples):
            rounding = "1dig"
            if sample.name == "S/B":
                rounding = "3dig"
            out.write( root2latex(sample.name) + " & " + turn1DHistToRow(hist, withError, rounding+ "\\\\ \n") )
        
        writeFoot(out)
        out.write("\\end{document}\n")


def turn1DHistToRow(hist, withError = True, rounding = "3dig"):
    string = ""
    for i in range(1, hist.GetNbinsX()+1):
        if rounding == "3dig":
            string += "%.3f" % hist.GetBinContent(i)
        else:
            string += "%.1f" % hist.GetBinContent(i)

        if withError:
            string += " $\pm$ "
            if rounding == "3dig":
                string += "%.3f" % hist.GetBinError(i)
            else:
                string += "%.1f" % hist.GetBinError(i)

        if i == hist.GetNbinsX():
            string += "\\\\"
        else:
            string += "&"

    return string

def root2latex(string, mth = True):
    new = ""
    if mth:
        new += "$"
    new += string.replace("#", "\\")
    if mth:
        new += "$"
    return new
# -------------------------------------------------------------------------------------------------































## TODO ##
## this is random and unused stuff - not sure if it still needed

def drawHistosOnCanvas2D(listOfHistos_,normalize=True,stack=False,logscale=False,options_='',ratio=False,DoProfile=False,statTest=False):
    print 'drawing 2d'
 #   raw_input()
    listOfHistos=[h.Clone(h.GetName()+'_drawclone') for h in listOfHistos_]
    canvas=getCanvas(listOfHistos[0].GetName(),False)
    print 'canvas name',canvas.GetName()
#    raw_input()

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
              # Check if integral is not null, since it will give a zero division error
              if integral0 != 0:
                h.Scale(1./integral0)
              else:
                h.Scale(1.)
                print "Warning: integral0  variable of histogram ", listOfHistos[0].GetName() ," has value 0 which would lead to zero division error."



    canvas.cd(1)
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

    #tests=None
    if DoProfile:
      profiles=[]
      for h in listOfHistos:
        profiles.append(h.ProfileX("prof_"+h.GetName(),1,h.GetNbinsX(),"o"))
        profiles[-1].SetLineColor(h.GetLineColor())
        profiles[-1].SetLineWidth(2)
        profiles[-1].Draw("SAME")
      if statTest:
        #print "doing 2D stat test"
        tests=getStatTestsList(profiles[0],profiles[1:],"WW")
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
#    print 'name2', canvas.GetName()
#    raw_input()
    return canvas, tests


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
              # Check if integral is not null, since it will give a zero division error
              if integral0 != 0:
                h.Scale(1./integral0)
              else:
                h.Scale(1.)
                print "Warning: integral0  variable of histogram ", listOfHistos[0].GetName() ," has value 0 which would lead to zero division error."


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






# ---------------------------------------------------
# alternatives to createHistoLists_fromSuperHistoFile
# (now self.genList)
# ---------------------------------------------------
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
# -------------------------------------------------------------------------------------------------







# ---------------------------------
# alternatives to plotDataMCanWsyst
# (now self.makeControlPlots)
# ---------------------------------
#def plotDataMCan(listOfHistoListsData,listOfHistoLists,samples,listOfhistosOnTop,sampleOnTop,factor,name,logscale=False,label='',ratio=True,blind=False,options='histo'):
    #if isinstance(label, basestring):
        #labeltexts=len(listOfHistoListsData)*[label]
    #else:
        #labeltexts=label
    #canvases=[]
    #objects=[]
    #i=0
##    print len(listOfHistoLists)
    ## for every plot, look at all samples
    #for ot,listOfHistos,listOfHistosData,labeltext in zip(listOfhistosOnTop,listOfHistoLists,listOfHistoListsData,labeltexts):
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
          ## Check if on top histogram integral is not null, since it will give a zero division error
          #if ot.Integral() != 0:
            #integralfactor=integralfactor/ot.Integral()
          #else:
            #integralfactor=integralfactor
            #print "Warning: On top histogram ", ot.GetName(), " has integral 0 which would lead to zero division error."

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
        #canvas=getCanvas(stackedListOfHistos[0].GetName(),ratio)
        #canvas.cd(1)
        ##draw first histo
        #h=stackedListOfHistos[0]
        #if logscale:
            #h.GetYaxis().SetRangeUser(yMax/10000,yMax*10)
            #canvas.cd(1).SetLogy()
        #else:
            #h.GetYaxis().SetRangeUser(0,yMax*1.5)
        #option='histo'
        #option+=options
        #h.DrawCopy(option)
        ##draw remaining
        #for h in stackedListOfHistos[1:]:
            #h.DrawCopy(option+'same')
        #h.DrawCopy('axissame')
        ##draw data
        #otc=ot.Clone()
        #nok=99999
        #if blind:
            #for ibin in range(stackedListOfHistos[0].GetNbinsX()):
                #if otc.GetBinContent(ibin)>0 and stackedListOfHistos[0].GetBinContent(ibin)/otc.GetBinContent(ibin)<100:
                    #nok=ibin-1
                    #break
        #data=getDataGraph(listOfHistosData,nok)
        #setupHisto(otc,sampleOnTop.color,'',False)
        #otc.SetBinContent(1,otc.GetBinContent(0)+otc.GetBinContent(1));
        #otc.SetBinContent(otc.GetNbinsX(),otc.GetBinContent(otc.GetNbinsX()+1)+otc.GetBinContent(otc.GetNbinsX()));
        #otc.SetBinError(1,ROOT.TMath.Sqrt(ROOT.TMath.Power(otc.GetBinError(0),2)+ROOT.TMath.Power(otc.GetBinError(1),2)));
        #otc.SetBinError(otc.GetNbinsX(),ROOT.TMath.Sqrt(ROOT.TMath.Power(otc.GetBinError(otc.GetNbinsX()+1),2)+ROOT.TMath.Power(otc.GetBinError(otc.GetNbinsX()),2)));
        #otc.SetLineWidth(3)
        #if factor >= 0.:
          #otc.Scale(factor)
        #else:
          #otc.Scale(integralfactor)
        #otc.Draw('histosame')
        #data.Draw('samePE1')
        #l=getLegend()
        #l.AddEntry2(data,'data','P')
        #if factor >= 0.:
          #l.AddEntry2(otc,sampleOnTop.name+' x '+str(factor),'L')
        #else:
          #l.AddEntry2(otc,sampleOnTop.name+(' x {:4.0f}').format(integralfactor),'L')
        #for h,sample in zip(stackedListOfHistos,samples):
            #l.AddEntry2(h,sample.name,'F')





        #canvases.append(canvas)
        #l.Draw('same')
        #objects.append(data)
        #objects.append(l)
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

        #label = ROOT.TLatex(0.2, 0.89, labeltext);
        #label.SetTextFont(42)
        #label.SetTextSize(0.05)
        #label.SetNDC()
        #label.Draw()
        #objects.append(label)


        #ratiograph,ratiominimum,ratiomaximum=getRatioGraph(data,stackedListOfHistos[0])
        #canvas.cd(2)
        #line=listOfHistos[0].Clone()
        #line.SetFillStyle(0)
        #line.Divide(listOfHistos[0])

        ##line.GetYaxis().SetRangeUser(0.5,1.6)
        #line.GetYaxis().SetRangeUser(ratiominimum-0.2,ratiomaximum+0.2)
        #line.GetXaxis().SetRangeUser(listOfHistos[0].GetXaxis().GetXmin(),listOfHistos[0].GetXaxis().GetXmax())
        #for i in range(line.GetNbinsX()+2):
            #line.SetBinContent(i,1)
            #line.SetBinError(i,0)
        #line.GetXaxis().SetLabelSize(line.GetXaxis().GetLabelSize()*2.4)
        #line.GetYaxis().SetLabelSize(line.GetYaxis().GetLabelSize()*2.4)
        #line.GetXaxis().SetTitleSize(line.GetXaxis().GetTitleSize()*3)
        #line.GetYaxis().SetTitleSize(line.GetYaxis().GetTitleSize()*2.4)
        #line.GetYaxis().SetTitleSize(line.GetYaxis().GetTitleSize()*2.4)
        #line.GetYaxis().CenterTitle(1);
        #line.GetYaxis().SetTitle('data/MC');
        #line.GetYaxis().SetNdivisions( 503 );
##        line.GetXaxis().SetLabelOffset( 0.006 );
        #line.GetXaxis().SetNdivisions( 510 );
        #line.GetXaxis().SetTickLength( line.GetXaxis().GetTickLength() * 2.0 );
        #line.GetYaxis().SetTickLength( line.GetYaxis().GetTickLength() * 1.65 );

        #line.Draw('histo')
        #line.SetLineWidth(1)
        #objects.append(line)
        #objects.append(ratiograph)
        #ratiograph.Draw('sameP')



##    print len(canvases)
    #printCanvases(canvases,name)
    #writeObjects(canvases,name





def plotDataMCanWsystCustomBinLabels(listOfHistoListsData,listOfHistoLists,samples,listOfhistosOnTop,sampleOnTop,factor,name,listOflll,listOfmyCustomBinLabels,logscale=False,label='',ratio=True,blinded=False,verbosity=0):
################################################
################################################
    options='histo'
    if isinstance(label, basestring):
        labeltexts=len(listOfHistoListsData)*[label]
    else:
        labeltexts=label
    canvases=[]
    objects=[]
    iplot=0
#    print len(listOfHistoLists)
    # for every plot, look at all samples
    listOfErrorGraphs=[]
    listOfErrorGraphStyles=[]
    listOfErrorGraphColors=[]

    listOfErrorGraphLists=[]
    #lll=[listOflistOflist of histograms, FillStyle, FillColor, DoRateSysts]
    for lll in listOflll:
      listOfErrorGraphLists.append(createErrorbands(lll[0],samples,lll[3]))
      #print listOfErrorGraphLists[-1stName, listIndex, dataName, nestedHistsConfig, options]
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
    #print len(listOfhistosOnTop),len(listOfHistoLists),len(listOfHistoListsData),len(labeltexts),len(listOfErrorGraphs)
    #raw_input()
    for ot,listOfHistos,listOfHistosData,labeltext,errorgraphList in zip(listOfhistosOnTop,listOfHistoLists,listOfHistoListsData,labeltexts,listOfErrorGraphs):
        iplot+=1
        integralfactor=0
        for histo,sample in zip(listOfHistos,samples):
            yTitle='Events'
            setupHisto(histo,sample.color,yTitle,True)

            if factor<-1 and ot.GetName()==histo.GetName(): ## case if you stack the ontop histogram to the stackplot but do not want it in the integral
              continue
            if factor < 0:
              integralfactor+=histo.Integral()

        if factor < 0:
          # Check if on top histogram integral is not null, since it will give a zero division error
          if ot.Integral() != 0:
            integralfactor=integralfactor/ot.Integral()
          else:
            integralfactor=integralfactor
            print "Warning: On top histogram ", ot.GetName(), " has integral 0 which would lead to zero division error."

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
        #print h.GetName()
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
        #if blinded:
            #blind.Draw('same2')
        #objects.append(blind)

        #BinningErrorFile=open(name+"/binningWarnings_"+ot.GetName()+".txt","w")
        listOfRatioErrorGraphs=[]
        graphcounter=0
        if verbosity>=2:
          print "doing ratio error graph"
        for errorgraph,thisFillStyle,ThisFillColor in errorgraphList:
          ratioerrorgraph=ROOT.TGraphAsymmErrors(errorgraph.GetN())
          #print ratioerrorgraph
          #raw_input()
          x, y = ROOT.Double(0), ROOT.Double(0)
          for igc in range(errorgraph.GetN()):
              errorgraph.GetPoint(igc,x,y)
              ratioerrorgraph.SetPoint(igc,x, 1.0)
              relErrUp=0.0
              relErrDown=0.0
              #check if bincontent-error becomes negative and if that is the case print it to the log file
              if (y-abs(errorgraph.GetErrorYlow(igc)))<0:
                print "WARNING: Stack - Error is negative in "+ot.GetName()+" "+str(igc)+" with values "+str(y)+" "+str(errorgraph.GetErrorYlow(igc))+" \n"
                #BinningErrorFile.write("WARNING: Stack - Error is negative in "+ot.GetName()+" "+str(igc)+" with values "+str(y)+" "+str(errorgraph.GetErrorYlow(igc))+" \n")
              if verbosity>=2:
                print x,y,errorgraph.GetErrorYhigh(igc),errorgraph.GetErrorYlow(igc)

              if y>0.0:
                  relErrUp=errorgraph.GetErrorYhigh(igc)/y
                  relErrDown=errorgraph.GetErrorYlow(igc)/y
                  if verbosity>=2:
                    print relErrUp,relErrDown
              ratioerrorgraph.SetPointError(igc, errorgraph.GetErrorXlow(igc),errorgraph.GetErrorXhigh(igc), relErrDown, relErrUp)


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
        ilc=0
        for h,sample in zip(stackedListOfHistos,samples):
            ilc+=1
            if ilc%2==1:
                l1.AddEntry22(h,sample.name,'F')
            if ilc%2==0:
                l2.AddEntry22(h,sample.name,'F')

        canvases.append(canvas)
        l1.Draw('same')
        l2.Draw('same')
        objects.append(data)
        objects.append(l1)
        objects.append(l2)
        objects.append(otc)

        #draw the lumi text on the canvas
        CMS_lumi.lumi_13TeV = "41.5 fb^{-1}"
        CMS_lumi.writeExtraText = 1
        #CMS_lumi.extraText = "Preliminary"
        CMS_lumi.extraText = ""
        CMS_lumi.cmsText="CMS"

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
        ## with this line you can let the ratio graph scale the y axis automatically
        #line.GetYaxis().SetRangeUser(ratiominimum-0.2,ratiomaximum+0.2)
        line.GetYaxis().SetRangeUser(0.4,1.65)

        line.GetXaxis().SetRangeUser(listOfHistos[0].GetXaxis().GetXmin(),listOfHistos[0].GetXaxis().GetXmax())
        for inb in range(line.GetNbinsX()+2):
            line.SetBinContent(inb,1)
            line.SetBinError(inb,0)
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

        #line.GetXaxis().SetBinLabel(4,"bla")
        line.Draw('histo')
        objects.append(ratiograph)
        #print len(listOfRatioErrorGraphs)
        for ratioerrorgraph in listOfRatioErrorGraphs:
          ratioerrorgraph.Draw("same2")
#        objects.append(ratioerrorgraph)
        ratiograph.Draw('sameP0')
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
        #BinningErrorFile.close()



#    print len(canvases)
    printCanvases(canvases,name)
    writeObjects(canvases,name)






#def plotDataMCanWsystCustomBinLabels(listOfHistoListsData,listOfHistoLists,samples,listOfhistosOnTop,sampleOnTop,factor,name,listOflll,listOfmyCustomBinLabels,logscale=False,label='',ratio=True,blinded=False):

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
    #for igraph in range(len(listOfErrorGraphLists[0])):
      #thisgraphs=[]
      #for iband in range(len(listOfErrorGraphLists)):
        #thisgraphs.append([listOfErrorGraphLists[iband][igraph],listOfErrorGraphStyles[iband],listOfErrorGraphColors[iband]])
      #listOfErrorGraphs.append(thisgraphs)
    ##for g in listOfErrorGraphs:
      ##print g
    #print len(listOfhistosOnTop),len(listOfHistoLists),len(listOfHistoListsData),len(labeltexts),len(listOfErrorGraphs)
    ##raw_input()
    #for ot,listOfHistos,listOfHistosData,labeltext,errorgraphList, myCustomBinLabels in zip(listOfhistosOnTop,listOfHistoLists,listOfHistoListsData,labeltexts,listOfErrorGraphs,listOfmyCustomBinLabels):
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
          ## Check if on top histogram integral is not null, since it will give a zero division error
          #if ot.Integral() != 0:
            #integralfactor=integralfactor/ot.Integral()
          #else:
            #integralfactor=integralfactor
            #print "Warning: On top histogram ", ot.GetName(), " has integral 0 which would lead to zero division error."

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
        #canvas=getCanvas(stackedListOfHistos[0].GetName(),ratio)
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
        ##if blinded:
            ##blind.Draw('same2')
        ##objects.append(blind)


        #listOfRatioErrorGraphs=[]
        #graphcounter=0
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
              #ratioerrorgraph.SetPointError(i, errorgraph.GetErrorXlow(i),errorgraph.GetErrorXhigh(i), relErrDown, relErrUp)


          #errorgraph.SetFillStyle(thisFillStyle)
          #errorgraph.SetLineColor(ThisFillColor)
          #errorgraph.SetFillColor(ThisFillColor)
          #ratioerrorgraph.SetFillStyle(thisFillStyle)
          #ratioerrorgraph.SetLineColor(ThisFillColor)
          #ratioerrorgraph.SetFillColor(ThisFillColor)
  ##        ratioerrorgraph.SetFillStyle(1001)
  ##        ratioerrorgraph.SetLineColor(ROOT.kBlack)
  ##        ratioerrorgraph.SetFillColor(ROOT.kGreen)

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
        #CMS_lumi.lumi_13TeV = "41.5 fb^{-1}"
        #CMS_lumi.writeExtraText = 1
        ##CMS_lumi.extraText = "Preliminary"
        #CMS_lumi.extraText = ""
        #CMS_lumi.cmsText=""
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

        #line.GetYaxis().SetRangeUser(0.5,1.6)
        ##line.GetYaxis().SetRangeUser(ratiominimum-0.2,ratiomaximum+0.2)
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


        #for icbl, cbl in enumerate(myCustomBinLabels):
          #line.GetXaxis().SetBinLabel(icbl+1,cbl)
        ##line.GetXaxis().SetBinLabel(4,"bla")
        #line.Draw('histo')
        #objects.append(ratiograph)
        ##print len(listOfRatioErrorGraphs)
        #for ratioerrorgraph in listOfRatioErrorGraphs:
          #ratioerrorgraph.Draw("same2")
##        objects.append(ratioerrorgraph)
        #ratiograph.Draw('sameP0')
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


##    print len(canvases)
    #printCanvases(canvases,name)
    #writeObjects(canvases,name)




def plotRefWsystandOthers(listOfHistoLists,samples,listOfhistosOnTop,sampleOnTop,name,listOflll,logscale=False,label='',ratio=True,blinded=False):
################################################
    listOfhistosOnTop_=[listOfhistosOnTop[i][0] for i in range(len(listOfhistosOnTop))]
    listOfRatioHistoLists=[]
    for ot,listOfHistos in zip(listOfhistosOnTop_,listOfHistoLists):
        RatioHistoLists=[]
        for histo in listOfHistos:
            histo_tmp=histo.Clone()
            histo_tmp.Divide(ot)
            RatioHistoLists.append(histo_tmp)
        listOfRatioHistoLists.append(RatioHistoLists)
################################################
    options=''
    if isinstance(label, basestring):
        labeltexts=len(listOfhistosOnTop)*[label]
    else:
        labeltexts=label
    canvases=[]
    objects=[]
#    print len(listOfHistoLists)
    # for every plot, look at all samples
    listOfErrorGraphs=[]
    listOfErrorGraphStyles=[]
    listOfErrorGraphColors=[]

    listOfErrorGraphLists=[]
    #lll=[listOflistOflist of histograms, FillStyle, FillColor, DoRateSysts]
    for lll in listOflll:
      listOfErrorGraphLists.append(createErrorbands(lll[0],[sampleOnTop],lll[3]))
      #print listOfErrorGraphLists[-1]
      #raw_input()
      listOfErrorGraphStyles.append(lll[1])
      listOfErrorGraphColors.append(lll[2])
    for igraph in range(len(listOfErrorGraphLists[0])):
      thisgraphs=[]
      for iband in range(len(listOfErrorGraphLists)):
        thisgraphs.append([listOfErrorGraphLists[iband][igraph],listOfErrorGraphStyles[iband],listOfErrorGraphColors[iband]])
      listOfErrorGraphs.append(thisgraphs)


    iplot=0
    # loop over the variables wh are supposed to be plotted (jet 1 pt, Njets , lep1 eta , ... )
    for ot,listOfHistos,labeltext,errorgraphList,listOfRatioHistos in zip(listOfhistosOnTop_,listOfHistoLists,labeltexts,listOfErrorGraphs,listOfRatioHistoLists):
        iplot+=1

        # setup histo style
        # loop over samples and the histograms of the plotted variable for each sample
        for histo,histo_ratio,sample in zip(listOfHistos,listOfRatioHistos,samples):
            yTitle='Events'
            setupHisto(histo,sample.color,yTitle,False)
            setupHisto(histo_ratio,sample.color,"x/nom.",False)
            histo_ratio.GetYaxis().SetTitleFont(42)
            histo_ratio.GetYaxis().CenterTitle()
            histo_ratio.GetYaxis().SetTitleOffset(0.5)
            histo_ratio.GetYaxis().SetTitleSize(0.1)
            histo_ratio.GetYaxis().SetLabelSize(0.08)
            histo_ratio.GetXaxis().SetTitleFont(42)
            histo_ratio.GetXaxis().SetTitleOffset(1.0)
            histo_ratio.GetXaxis().SetTitleSize(0.1)
            histo_ratio.GetXaxis().SetLabelSize(0.1)

        # mover over/underflow
        for h in listOfHistos:
            moveOverFlow(h)

        # find maximum bin value of all samples for the considered variable to know how large the y axis scale has to be
        yMax=1e-9
        yMax_=1e-9
        for h,h_ in zip(listOfHistos,listOfRatioHistos):
            yMax=max(h.GetBinContent(h.GetMaximumBin()),yMax)
            yMax_=max(h_.GetBinContent(h_.GetMaximumBin()),yMax_)

        #create first canvas: if ratio true then a canvas with ratio pad, if false then without
        canvas=getCanvas(listOfHistos[0].GetName(),ratio)
        canvas.cd(1)

        #set y-scale on first histo / ratiohisto for later
        h=listOfHistos[0]
        h_=listOfRatioHistos[0]
        if logscale:
            h.GetYaxis().SetRangeUser(yMax/10000,yMax*10)
            canvas.cd(1).SetLogy()
        else:
            h.GetYaxis().SetRangeUser(0,yMax*1.8)
            h_.GetYaxis().SetRangeUser(0.5,yMax_*1.2)
        option='histo'
        option+=options
        #print h.GetName()
        #h.GetXaxis().SetBinLabel(1,"test")
        #draw remaining
        for h,h_,isc in zip(listOfHistos,listOfRatioHistos,range(len(listOfHistos))):
            if isc==0:
                canvas.cd(1)
                h.DrawCopy(option)
                canvas.cd(2)
                h_.DrawCopy()
            else:
                canvas.cd(1)
                h.DrawCopy(option+'same')
                canvas.cd(2)
                h_.DrawCopy('same')
        line = ot.Clone()
        line.Divide(ot)
        for icb in range(line.GetNbinsX()+2):
            line.SetBinContent(icb,1)
            line.SetBinError(icb,0)

        line.SetLineColor(ROOT.kBlack)
        line.DrawCopy('same')
        canvas.cd(1)
        h.DrawCopy('axissame')
        canvas.cd(2)
        h_.DrawCopy('axissame')

        # plot sample on top
        canvas.cd(1)
        otc=ot.Clone()
        setupHisto(otc,sampleOnTop.color,'',False)
        otc.SetBinContent(1,otc.GetBinContent(0)+otc.GetBinContent(1));
        otc.SetBinContent(otc.GetNbinsX(),otc.GetBinContent(otc.GetNbinsX()+1)+otc.GetBinContent(otc.GetNbinsX()));
        otc.SetBinError(1,ROOT.TMath.Sqrt(ROOT.TMath.Power(otc.GetBinError(0),2)+ROOT.TMath.Power(otc.GetBinError(1),2)));
        otc.SetBinError(otc.GetNbinsX(),ROOT.TMath.Sqrt(ROOT.TMath.Power(otc.GetBinError(otc.GetNbinsX()+1),2)+ROOT.TMath.Power(otc.GetBinError(otc.GetNbinsX()),2)));
        otc.SetLineWidth(2)

        otc.Draw('histosame')


        # from error graphs calculate ratio error graphs
        listOfRatioErrorGraphs=[]
        #graphcounter=0
        print "doing ratio error graph"
        for errorgraph,thisFillStyle,ThisFillColor in errorgraphList:
          ratioerrorgraph=ROOT.TGraphAsymmErrors(errorgraph.GetN())
          #print ratioerrorgraph
          #raw_input()
          x, y = ROOT.Double(0), ROOT.Double(0)
          for igc in range(errorgraph.GetN()):
              errorgraph.GetPoint(igc,x,y)
              ratioerrorgraph.SetPoint(igc,x, 1.0)
              relErrUp=0.0
              relErrDown=0.0
              print x,y,errorgraph.GetErrorYhigh(igc),errorgraph.GetErrorYlow(igc)
              if y>0.0:
                  relErrUp=errorgraph.GetErrorYhigh(igc)/y
                  relErrDown=errorgraph.GetErrorYlow(igc)/y
                  print relErrUp,relErrDown
              ratioerrorgraph.SetPointError(igc, errorgraph.GetErrorXlow(igc),errorgraph.GetErrorXhigh(igc), relErrDown, relErrUp)

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
          #graphcounter+=1

          objects.append(errorgraph)
          objects.append(ratioerrorgraph)
          listOfRatioErrorGraphs.append(ratioerrorgraph)
          #print objects
          #raw_input()

        l1=getLegendL()
        l2=getLegendR()
        ilc=0
        for h,sample in zip(listOfHistos,samples):
            ilc+=1
            if ilc%2==1:
                l1.AddEntry22(h,sample.name,'L')
            if ilc%2==0:

                l2.AddEntry22(h,sample.name,'L')
        l2.AddEntry22(otc,sampleOnTop.name,'L')

        l1.Draw('same')
        l2.Draw('same')
        objects.append(l1)
        objects.append(l2)
        objects.append(otc)

        #draw the lumi text on the canvas
        CMS_lumi.lumi_13TeV = "41.5 fb^{-1}"
        CMS_lumi.writeExtraText = 1
        #CMS_lumi.extraText = "Preliminary"
        CMS_lumi.extraText = ""
        CMS_lumi.cmsText=""

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

        canvas.cd(2)

        for ratioerrorgraph in listOfRatioErrorGraphs:
          ratioerrorgraph.Draw("same2")

#       
        canvases.append(canvas)

    printCanvases(canvases,name)
    writeObjects(canvases,name)
# -------------------------------------------------------------------------------------------------






# -------------------------------
# write functions that are unused
# -------------------------------
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
    for entryNumber, entry in enumerate(columns):
        if entryNumber == 0:
          f.write('Sample &')
        # Check if last entry and add line endings  
        elif entryNumber +1 == len(columns):
          f.write('Bin' + str(entryNumber) + ' \\\\ \n')
        else:
          f.write('Bin' + str(entryNumber) + ' &')
    f.write('\\hline\n')
# -------------------------------------------------------------------------------------------------











# completely random stuff

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


def writeListOfROCs(graphs,names,colors,filename,printInts=True,logscale=False,rej=True):
    c=getCanvas('ROC')
    if logscale:
        c.SetLogy()
    l=getLegend()
    first=True
    for graph,name,color in zip(graphs,names,colors):
        integral=graph.Integral()+0.5
        if printInts:
          l.AddEntry2(graph,name+" ("+str(round(integral,2))+")")
        else:
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

def printPlots(plots):
    for plot in plots:
        print 'TH1F("'+plot.histo.GetName()+'","'+plot.histo.GetTitle()+'",'+str(plot.histo.GetNbinsX())+','+str(plot.histo.GetXaxis().GetXmin())+','+str(plot.histo.GetXaxis().GetXmax())+')'


