#############
# plot general control distributions
##############

from plotconfig_Zprime_MC_minimal import *
#from plot_additional_Zprime_MC_Lena import *
#from plot_cuts_ZPrime_MC_Lena import *
sys.path.insert(0, 'limittools')
from limittools import renameHistos
import copy



#ABCDeventhandling='oncefirst'
##ABCDeventhandling='reweight'

#name='Zprime_MC_ABCD'+radi+'_'+ABCDeventhandling+'_'+WPs
##SampleNames=['ttbar' , 'QCD_HT', 'QCD_Pt' ]
##SignalSampleNames=['Zprime1500900',  'Zprime20001200',  'Zprime25001200']

name='mus'

plots=[

    Plot(ROOT.TH1F("Weight_scale_variation_muR0p5_muF0p5" ,"Weight_scale_variation_muR0p5_muF0p5" ,40,0.8,1.2),"Weight_scale_variation_muR0p5_muF0p5", "Weight_scale_variation_muR0p5_muF0p5>0", ""),
    Plot(ROOT.TH1F("Weight_scale_variation_muR0p5_muF1p0" ,"Weight_scale_variation_muR0p5_muF1p0" ,40,0.8,1.2),"Weight_scale_variation_muR0p5_muF1p0", "Weight_scale_variation_muR0p5_muF1p0>0", ""),
    Plot(ROOT.TH1F("Weight_scale_variation_muR0p5_muF2p0" ,"Weight_scale_variation_muR0p5_muF2p0" ,40,0.8,1.2),"Weight_scale_variation_muR0p5_muF2p0", "Weight_scale_variation_muR0p5_muF2p0>0", ""),
    Plot(ROOT.TH1F("Weight_scale_variation_muR1p0_muF0p5" ,"Weight_scale_variation_muR1p0_muF0p5" ,40,0.8,1.2),"Weight_scale_variation_muR1p0_muF0p5", "Weight_scale_variation_muR1p0_muF0p5>0", ""),
    Plot(ROOT.TH1F("Weight_scale_variation_muR1p0_muF2p0" ,"Weight_scale_variation_muR1p0_muF2p0" ,40,0.8,1.2),"Weight_scale_variation_muR1p0_muF2p0", "Weight_scale_variation_muR1p0_muF2p0>0", ""),
    Plot(ROOT.TH1F("Weight_scale_variation_muR2p0_muF0p5" ,"Weight_scale_variation_muR2p0_muF0p5" ,40,0.8,1.2),"Weight_scale_variation_muR2p0_muF0p5", "Weight_scale_variation_muR2p0_muF0p5>0", ""),
    Plot(ROOT.TH1F("Weight_scale_variation_muR2p0_muF1p0" ,"Weight_scale_variation_muR2p0_muF1p0" ,40,0.8,1.2),"Weight_scale_variation_muR2p0_muF1p0", "Weight_scale_variation_muR2p0_muF1p0>0", ""),
    Plot(ROOT.TH1F("Weight_scale_variation_muR2p0_muF2p0" ,"Weight_scale_variation_muR2p0_muF2p0" ,40,0.8,1.2),"Weight_scale_variation_muR2p0_muF2p0", "Weight_scale_variation_muR2p0_muF2p0>0", ""),

]




plotnames=[]
for i in plots:
    plotnames.append(i.name)




#print name,2000000,plots,SignalSamples+,[''],['1.']
#outputpath=plotParallel(name,4000000,plots,samples)
outputpath=plotParallel(name,1500000,plots,SignalSamples, [''], ['1'] , [''], ['1'],[""],[""],[""])
#outputpath=plotParallel(name,2000000,plots,SignalSamples, [''], ['1'] , [''], ['1'],additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile,OnlyFirstList)
#outputpath=plotParallel(name,3000000,plots,SignalSamples+BackgroundSamples+CombinedSamples, [''], ['1'] , [''], ['1'], [],  OnlyFirstList)
#outputpathBackground=plotParallel(name,4000000,plots,BackgroundSamples)
#outputpathData=plotParallel(name,4000000,plots,DataSamples)

# plot dataMC comparison
#listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
#listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
#print outputpath, SignalSamples, plots
listOfHistoListsSignal=createHistoLists_fromSuperHistoFile(outputpath,SignalSamples ,plots,1, [""], True )
#print "hell yeah", listOfHistoListsSignal


writeListOfHistoLists(transposeLOL(transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime1500700_tWb'):SignalSampleNames.index('Zprime25001500_tWb')+1])[plotnames.index('Weight_scale_variation_muR0p5_muF0p5'):plotnames.index('Weight_scale_variation_muR2p0_muF2p0')+1],SignalSamples[SignalSampleNames.index('Zprime1500700_tWb'):SignalSampleNames.index('Zprime25001500_tWb')+1],"","mus",True,False,False,"",False,False,False)

writeListOfHistoLists(transposeLOL(transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime1500700_ttZ'):SignalSampleNames.index('Zprime25001500_ttZ')+1])[plotnames.index('Weight_scale_variation_muR0p5_muF0p5'):plotnames.index('Weight_scale_variation_muR2p0_muF2p0')+1],SignalSamples[SignalSampleNames.index('Zprime1500700_ttZ'):SignalSampleNames.index('Zprime25001500_ttZ')+1],"","mus",True,False,False,"",False,False,False)

writeListOfHistoLists(transposeLOL(transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime1500700_ttH'):SignalSampleNames.index('Zprime25001500_ttH')+1])[plotnames.index('Weight_scale_variation_muR0p5_muF0p5'):plotnames.index('Weight_scale_variation_muR2p0_muF2p0')+1],SignalSamples[SignalSampleNames.index('Zprime1500700_ttH'):SignalSampleNames.index('Zprime25001500_ttH')+1],"","mus",True,False,False,"",False,False,False)
                   
print            listOfHistoListsSignal[0]
raw_input()
for l,plot in zip(listOfHistoListsSignal,plotnames):
    av1500=0
    av2000=0
    av2500=0
    n1500=0
    n2000=0
    n2500=0
    for h in l:
        if "Zprime1500" in h.GetName():
            av1500+=h.GetMean()
            n1500+=1
        elif "Zprime2000" in h.GetName():
            av2000+=h.GetMean()
            n2000+=1
        elif "Zprime2500" in h.GetName():
            av2500+=h.GetMean()
            n2500+=1
    #av=av/float(len(l))
    
    print plot,"   1500:",av1500/float(n1500),"  2000:",av2000/float(n2000),"  2500:",av2500/float(n2500)