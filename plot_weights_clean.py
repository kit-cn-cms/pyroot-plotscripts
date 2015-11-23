import sys
oldargv = sys.argv[:]
sys.argv = ['-b-']
import ROOT
import re
ROOT.gROOT.SetBatch(True)
sys.argv = oldargv

ROOT.gSystem.Load("libFWCoreFWLite.so");
ROOT.gSystem.Load("libDataFormatsFWLite.so");
ROOT.AutoLibraryLoader.enable()

from DataFormats.FWLite import Handle, Events, Runs

GenEvtInfo, GenEvtInfoLabel = Handle("GenEventInfoProduct") , "generator"
LHEEvtHandle, LHEEvtHandleLabel = Handle("LHEEventProduct"), "externalLHEProducer"
LHEProduct, LHEProductLabel = Handle("LHERunInfoProduct"), "externalLHEProducer"


###############################################
#Set inputfilename and outputfilename
filename = "/pnfs/desy.de/cms/tier2/store/mc/RunIISpring15MiniAODv2/TT_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/F6AB6CE6-A46F-E511-B103-44A842CFD633.root"

outputname ="ttbar.root"
##############################################

events = Events(filename)
runs = Runs(filename)





#Getting weight number for PDF:
weightnum = True

if (weightnum):
    for ir, run in enumerate(runs):
	if ir > 10: break
        run.getByLabel(LHEProductLabel, LHEProduct)


##################################################
#read header and print the part about the weights
	var = LHEProduct.product()

	test = var.headers_begin()

	weightlist = []
	weightlist2 = []
	scalevarlist = []
	pdfvarlist = []
        wnum = 0
	while(test != var.headers_end()):
            for line in range(test.lines().size()):
                if (test.lines().at(line).strip().startswith('<weig')):
                    print test.lines().at(line).strip()
                    tmpstring=test.lines().at(line).strip()
                    if (tmpstring.startswith('<weight id=')):
                        #if tmpstring.endswith('"hdamp_variation">'):
                        #    break
                        #else:
                        wnum = wnum + 1
            test = test + 1

#print wnum
##################################################
#Plot weights for all events
outputfile = ROOT.TFile(outputname,"RECREATE")
print "\nSample has",wnum,"weights stored\n"

histos = []
for i in range(wnum):
    histos.append(ROOT.TH1F("Weights"+str(i),"Weights"+str(i),800,-10,10))
histos.append(ROOT.TH1F("originalXWGTUP","originalXWGTUP",800,-10,10))


for iev,event in enumerate(events): 
    if iev > 1000: break
    event.getByLabel(GenEvtInfoLabel, GenEvtInfo)
    event.getByLabel(LHEEvtHandleLabel, LHEEvtHandle)
    

    for i,histo in enumerate(histos):
        if i != len(histos)-1:
            histo.Fill(LHEEvtHandle.product().weights()[i].wgt)
    
    histos[-1].Fill(LHEEvtHandle.product().originalXWGTUP())

for histo in histos:
    outputfile.WriteTObject(histo)

