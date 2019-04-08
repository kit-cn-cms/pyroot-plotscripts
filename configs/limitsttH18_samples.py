import os
import sys
filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = "/".join(filedir.split("/")[:-1])

sys.path.append(pyrootdir)
import util.tools.plotClasses as plotClasses

def getSamples( pltcfg ):
    return pltcfg.samples
    
def getSystSamples(systematics, analysis, samples):
    systSamples = []

    # adding other samples
    for sample in samples:
        variationsysts=systematics.get_variation_systs(sample.name)
        for sysName in variationsysts:
            newSel = sample.selection
            fileName=systematics[sample.name][sysName].expression
            if "/" in fileName:
                newpath=fileName
            else:
                newpath=sample.path.replace("nominal",fileName)
            #not enough samples ind hdamp up
            if "HDAMP" in sysName and sysName.endswith("Up"):
                newSel += "*((N_GenTopHad==1 && N_GenTopLep==1)* %s + !(N_GenTopHad==1 && N_GenTopLep ==1)*1)" %str(round(1.0399, 2))

            systSamples.append( 
                plotClasses.Sample( 
                    sample.name+sysName, 
                    sample.color, 
                    sample.path.replace("nominal", sysFileName), 
                    newSel, 
                    sample.nick+sysName, 
                    samDict = pltcfg.sampleDict ))

    return systSamples

def getAllSamples( pltcfg, systematics, analysis, samples):
    return getSamples(pltcfg) + getSystSamples(systematics, analysis, samples)

