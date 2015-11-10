import ROOT
import re
ROOT.gROOT.SetBatch(True)


ROOT.gSystem.Load("libFWCoreFWLite.so");
ROOT.gSystem.Load("libDataFormatsFWLite.so");
ROOT.AutoLibraryLoader.enable()

from DataFormats.FWLite import Handle, Events, Runs


#Get LHERunInfo from MiniAOD File
def getHeader(filename, weightsonly=True):
	LHEProduct, LHEProductLabel = Handle("LHERunInfoProduct"), "externalLHEProducer"
	runs = Runs(filename)
	for ir, run in enumerate(runs):
        	run.getByLabel(LHEProductLabel, LHEProduct)
		var = LHEProduct.product()
		test = var.headers_begin()

		header = []
		while(test != var.headers_end()):
            		for line in range(test.lines().size()):
            			header.append(test.lines().at(line)[0:-1])
            		test = test + 1
	if weightsonly == True:
		return getonlyweights(header)
	else:
		return header

#Get weights in run
def getonlyweights(header):
	weightheader = []
	for line in header:
		if line[0:5] == '<weig':
			weightheader.append(line)
	return weightheader

#Get total number of weights
def getnumofweights(weightheader):
	num = 0
	for line in weightheader:
		if (line[0:8] == '<weight '):
			num = num + 1
	return num

#Get Weightgroups and weightnumber range
def getweightgroupnames(weightheader):
	names = []
	#Code to read the weightheader with more details 
	return names
