import plotClasses

class samplesData:
    def __init__(self, pltcfg):
        self.pltcfg = pltcfg
        self.samples = self.pltcfg.samplesLimits
        self.controlSamples  = self.pltcfg.samplesDataControlPlots

        self.systSamples = []
        self.systNames = []

    def addSystSamples(self, systNames, systfileNames,
                        pathReplace = ["''","''"],
                        selReplace = ["''","''"],
                        selReplace2 = ["''","''"],
                        filternicks = None,
                        filtername = None ):
        self.systNames += systNames

        for sample in self.samples:
            if filternicks:
                if sample.nick not in filternicks:
                    continue
            if filtername:
                if not sample.name == filtername:      
                    continue
            for name, filename in zip(systNames, systfileNames):
                selection = sample.selection.replace( eval(selReplace[0]), eval(selReplace[1]) )
                selection = selection.replace( eval(selReplace2[0]), eval(selReplace2[1]) )
                path = sample.path.replace( eval(pathReplace[0]), eval(pathReplace[1]) )
                
                self.systSamples.append(
                    plotClasses.Sample(
                        sample.name + name, 
                        sample.color,
                        path,
                        selection,
                        sample.nick + name,
                        samDict=self.pltcfg.sampleDict) )
                        
    def addAllSamples(self, addNames):
        self.allNames = addNames + self.systNames
        self.allSamples = self.samples + self.controlSamples + self.systSamples 
        self.allSystSamples = self.samples + self.systSamples

