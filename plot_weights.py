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


def getweightpdfset(string):
    retlist = []
    endpos = 0
    return re.findall('[0-9]+(?!\.)|[0-9]\.[0-9]',string)
    #return list = [weight_id, pdf_set] for pdf-variation
    #or list = [weight_id, mu_R, mu_F] for scale-variation



filename = "/pnfs/desy.de/cms/tier2/store/user/hmildner/ttHTobb_M125_13TeV_powheg_pythia8/Boostedv2MiniAOD/151017_154254/0000/BoostedTTH_MiniAOD_13.root"
#filename = "/pnfs/desy.de/cms/tier2//store/user/hmildner/ttHToNonbb_M125_13TeV_powheg_pythia8/Boostedv2MiniAOD/151017_154312/0000/BoostedTTH_MiniAOD_1.root" 
#filename = "/pnfs/desy.de/cms/tier2/store/mc/RunIISpring15MiniAODv2/ttHToNonbb_M125_13TeV_powheg_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/02FE2DB6-D06D-E511-8BC7-0025905C431C.root"
#filename = "/pnfs/desy.de/cms/tier2/store/user/hmildner/TT_TuneCUETP8M1_13TeV-powheg-pythia8/Boostedv2MiniAOD/151017_154450/0000/BoostedTTH_MiniAOD_101.root" 
#filename = "/pnfs/desy.de/cms/tier2//store/user/hmildner/TT_TuneCUETP8M1_13TeV-powheg-pythia8/Boostedv2MiniAOD/151017_154450/0000/BoostedTTH_MiniAOD_204.root"


outputname = "scales_BoostedTTH_MiniAOD_13_2.root"
#outputname = "scales_BoostedTTH_MiniAOD_1.root"
#outputname = "scales_BoostedTTH_MiniAOD_101.root"
#outputname = "scales_BoostedTTbar_MiniAOD_204.root"

events = Events(filename)
runs = Runs(filename)





#Getting weight number for PDF:
weightnum = True

if (weightnum):
    for ir, run in enumerate(runs):
	if ir > 10: break
        run.getByLabel(LHEProductLabel, LHEProduct)


##############################
	
	#read header and print the part about the weights
	var = LHEProduct.product()

	test = var.headers_begin()

	weightlist = []
	weightlist2 = []
	scalevarlist = []
	pdfvarlist = []
	while(test != var.headers_end()):
            wnum = 0
            for line in range(test.lines().size()):
                if (test.lines().at(1)[0:5] == '<weig'):
                    print test.lines().at(line)[0:-1]
                    if (test.lines().at(line)[0:8] == '<weight '):
                        weightlist2.append(getweightpdfset(test.lines().at(line)[0:-1]))
                        weightlist2[wnum].append(wnum)
                        wnum = wnum + 1
            test = test + 1
	
	#some cosmetic stuff. Only works right, if there are no weights for hdamp variation. With hdamp variation
	#the plot titles are wrong, while the weight numbers are still right
	#scalevarlist: [weight_id, mu_R, mu_F, file_weight_number]
	#pdfvarlist: [weight_id, pdf_set, file_weight_number]
	for i in range(len(weightlist2)):
            if len(weightlist2[i]) != 4:
                scalevarlist = weightlist2[:i]
                pdfvarlist = weightlist2[i:]
                break
	
	#log
	with open('BoostedTTH_MiniAOD_13.root_'+str(ir)+'.txt', 'w') as f:
	#with open('BoostedTTH_MiniAOD_101.root_'+str(ir)+'.txt', 'w') as f:
            for scalevar in scalevarlist:
                f.write(str(scalevar)+"\n")
            for pdfvar in pdfvarlist:
                f.write(str(pdfvar)+"\n")
	f.closed
############################

#Plot weights for all events
outputfile = ROOT.TFile(outputname,"RECREATE")

ROOT.TH1F
scalevarhistos = []
pdfvarhistos = []
#scalevariations
for variation in scalevarlist:
    scalevarhistos.append(ROOT.TH1F("Scale variations - Weightnum: "+str(variation[-1])+" mu_F: "+str(variation[1])+" mu_R: "+str(variation[2]),"Scale variations "+"Weightnum: "+str(variation[-1])+" mu_F: "+str(variation[1])+" mu_R: "+str(variation[2]),80,0,2))
for variation in pdfvarlist:
    pdfvarhistos.append(ROOT.TH1F("PDF variation - Weightnum: "+str(variation[-1])+" PDF set: "+str(variation[1]),"PDF variation - Weightnum: "+str(variation[-1])+" PDF set: "+str(variation[1]),80,0,2))
    

for iev,event in enumerate(events): 
    #if iev > 1000: break
    event.getByLabel(GenEvtInfoLabel, GenEvtInfo)
    event.getByLabel(LHEEvtHandleLabel, LHEEvtHandle)
    
    #for i in range(222): 
    #print  LHEEvtHandle.product().weights().size()
	
    #raw_input("press key")
    for i,scale in enumerate(scalevarlist):
       	scalevarhistos[i].Fill(LHEEvtHandle.product().weights()[scale[-1]].wgt/LHEEvtHandle.product().originalXWGTUP())
    for i,scale in enumerate(pdfvarlist):
        pdfvarhistos[i].Fill(LHEEvtHandle.product().weights()[scale[-1]].wgt/LHEEvtHandle.product().originalXWGTUP())
        


for histo in scalevarhistos:
    outputfile.WriteTObject(histo)

for histo in pdfvarhistos:
    outputfile.WriteTObject(histo)

