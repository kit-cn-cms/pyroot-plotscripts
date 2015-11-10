#Test, if all events have the right amount of weights
import sys
oldargv = sys.argv[:]
sys.argv = ['-b-']
import ROOT
import miniAODheader
import glob
ROOT.gROOT.SetBatch(True)
sys.argv = oldargv

ROOT.gSystem.Load("libFWCoreFWLite.so");
ROOT.gSystem.Load("libDataFormatsFWLite.so");
ROOT.AutoLibraryLoader.enable()

from DataFormats.FWLite import Handle, Events, Runs

GenEvtInfo, GenEvtInfoLabel = Handle("GenEventInfoProduct") , "generator"
LHEEvtHandle, LHEEvtHandleLabel = Handle("LHEEventProduct"), "externalLHEProducer"

############################################################################
# Set folder containing Root Files to be tested and set name of the log file
folder = "/pnfs/desy.de/cms/tier2//store/user/hmildner/ttHToNonbb_M125_13TeV_powheg_pythia8/Boostedv2MiniAOD/151017_154312/0000/"
logfilename = 'BoostedTTHnonbb_weightsize_test.txt'
############################################################################

setlist = sorted(glob.glob(folder+"*.root"))

#Get header from MiniAOD File and extract number of weights, that are given in the header
weightheader = miniAODheader.getHeader(setlist[0])
num_of_weights = miniAODheader.getnumofweights(weightheader)

print "Expected number of weights from header: "+str(num_of_weights)
print "Testing "+str(len(setlist))+" files...."


#Loop over all files in Folder und compare the lengths of the weights vector from each event 
#to the expected lenghts (== number expected weights)
with open(logfilename, 'w') as f:
	for line in weightheader:
		f.write(line+"\n")
	num_ges=0
	num_per_set_list=[]
	for sets in setlist:
		print sets
		events = Events(sets)
		f.write(sets+"\n")
		num_per_set = 0
		for iev,event in enumerate(events): 
			event.getByLabel(GenEvtInfoLabel, GenEvtInfo)
			event.getByLabel(LHEEvtHandleLabel, LHEEvtHandle)
			#print "Event Nr. :",iev
			if LHEEvtHandle.product().weights().size() != num_of_weights:
				#print LHEEvtHandle.product().weights().size()
				f.write("Event Nr. : "+str(iev)+" with: "+str(LHEEvtHandle.product().weights().size())+"\n")
				num_ges = num_ges + 1
				num_per_set = num_per_set + 1
		if num_per_set != 0:		
			num_per_set_list.append([sets,num_per_set])
			#raw_input("press key")
	f.write("\n"+"\n"+"\n")
	print "Differences were found in the folling files:"
	f.write("Differences were found in the folling files:\n")
	for el in num_per_set_list:
		print str(el[0]).split('/')[-1]+" | "+str(el[1])
		f.write(str(el[0])+" | "+str(el[1])+"\n")
	f.write("Total number of differences in all Samples: "+str(num_ges))
	print "Total number of differences in all Samples: "+str(num_ges)
f.close
print "Logfile saved: "+logfilename


