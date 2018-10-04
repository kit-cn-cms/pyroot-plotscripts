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

name='mus_Sig'

plots=[

    Plot(ROOT.TH1F("Weight_scale_variation_muR0p5_muF0p5" ,"Weight_scale_variation_muR0p5_muF0p5" ,80,0.7,1.5),"Weight_scale_variation_muR0p5_muF0p5", "Weight_scale_variation_muR0p5_muF0p5>0", ""),
    Plot(ROOT.TH1F("Weight_scale_variation_muR0p5_muF1p0" ,"Weight_scale_variation_muR0p5_muF1p0" ,80,0.7,1.5),"Weight_scale_variation_muR0p5_muF1p0", "Weight_scale_variation_muR0p5_muF1p0>0", ""),
    Plot(ROOT.TH1F("Weight_scale_variation_muR0p5_muF2p0" ,"Weight_scale_variation_muR0p5_muF2p0" ,80,0.7,1.5),"Weight_scale_variation_muR0p5_muF2p0", "Weight_scale_variation_muR0p5_muF2p0>0", ""),
    Plot(ROOT.TH1F("Weight_scale_variation_muR1p0_muF0p5" ,"Weight_scale_variation_muR1p0_muF0p5" ,80,0.7,1.5),"Weight_scale_variation_muR1p0_muF0p5", "Weight_scale_variation_muR1p0_muF0p5>0", ""),
    Plot(ROOT.TH1F("Weight_scale_variation_muR1p0_muF1p0" ,"Weight_scale_variation_muR1p0_muF1p0" ,80,0.7,1.5),"Weight_scale_variation_muR1p0_muF1p0", "Weight_scale_variation_muR1p0_muF1p0>0", ""),
    Plot(ROOT.TH1F("Weight_scale_variation_muR1p0_muF2p0" ,"Weight_scale_variation_muR1p0_muF2p0" ,80,0.7,1.5),"Weight_scale_variation_muR1p0_muF2p0", "Weight_scale_variation_muR1p0_muF2p0>0", ""),
    Plot(ROOT.TH1F("Weight_scale_variation_muR2p0_muF0p5" ,"Weight_scale_variation_muR2p0_muF0p5" ,80,0.7,1.5),"Weight_scale_variation_muR2p0_muF0p5", "Weight_scale_variation_muR2p0_muF0p5>0", ""),
    Plot(ROOT.TH1F("Weight_scale_variation_muR2p0_muF1p0" ,"Weight_scale_variation_muR2p0_muF1p0" ,80,0.7,1.5),"Weight_scale_variation_muR2p0_muF1p0", "Weight_scale_variation_muR2p0_muF1p0>0", ""),
    Plot(ROOT.TH1F("Weight_scale_variation_muR2p0_muF2p0" ,"Weight_scale_variation_muR2p0_muF2p0" ,80,0.7,1.5),"Weight_scale_variation_muR2p0_muF2p0", "Weight_scale_variation_muR2p0_muF2p0>0", ""),

    
    
    Plot(ROOT.TH1F("Weight_LHA_NNPDF30_nlo_as_0118_nominal" ,"Weight_LHA_NNPDF30_nlo_as_0118_nominal" ,100,0.0,2.0),"Weight_LHA_NNPDF30_nlo_as_0118_nominal", "Weight_LHA_NNPDF30_nlo_as_0118_nominal>0", ""),
    Plot(ROOT.TH1F("Weight_LHA_NNPDF30_nlo_as_0118_up" ,"Weight_LHA_NNPDF30_nlo_as_0118_up" ,100,0.0,2.0),"Weight_LHA_NNPDF30_nlo_as_0118_up", "Weight_LHA_NNPDF30_nlo_as_0118_up>0", ""),
    Plot(ROOT.TH1F("Weight_LHA_NNPDF30_nlo_as_0118_down" ,"Weight_LHA_NNPDF30_nlo_as_0118_down" ,100,0.0,2.0),"Weight_LHA_NNPDF30_nlo_as_0118_down", "Weight_LHA_NNPDF30_nlo_as_0118_down>0", ""),
    
        

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
listOfHistoListsSignal=createHistoLists_fromSuperHistoFile(outputpath,SignalSamples ,plots,1.0, [""], True )
#print "hell yeah", listOfHistoListsSignal


#writeListOfHistoLists(transposeLOL(transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime1500700_tWb'):SignalSampleNames.index('Zprime25001500_tWb')+1])[plotnames.index('Weight_scale_variation_muR0p5_muF0p5'):plotnames.index('Weight_scale_variation_muR2p0_muF2p0')+1],SignalSamples[SignalSampleNames.index('Zprime1500700_tWb'):SignalSampleNames.index('Zprime25001500_tWb')+1],"","mus",True,False,False,"",False,False,False)

#writeListOfHistoLists(transposeLOL(transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime1500700_ttZ'):SignalSampleNames.index('Zprime25001500_ttZ')+1])[plotnames.index('Weight_scale_variation_muR0p5_muF0p5'):plotnames.index('Weight_scale_variation_muR2p0_muF2p0')+1],SignalSamples[SignalSampleNames.index('Zprime1500700_ttZ'):SignalSampleNames.index('Zprime25001500_ttZ')+1],"","mus",True,False,False,"",False,False,False)

#writeListOfHistoLists(transposeLOL(transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime1500700_ttH'):SignalSampleNames.index('Zprime25001500_ttH')+1])[plotnames.index('Weight_scale_variation_muR0p5_muF0p5'):plotnames.index('Weight_scale_variation_muR2p0_muF2p0')+1],SignalSamples[SignalSampleNames.index('Zprime1500700_ttH'):SignalSampleNames.index('Zprime25001500_ttH')+1],"","mus",True,False,False,"",False,False,False)
               
               
#writeListOfHistoLists(listOfHistoListsSignal,SignalSamples,"","mus_Sig",True,False,False,"",False,False,False)
    
               
               
#print            listOfHistoListsSignal[0]
#raw_input()
print plotnames
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
    
    print "Zprime ", plot,"   1500:",av1500/float(n1500),"  2000:",av2000/float(n2000),"  2500:",av2500/float(n2500)
    raw_input()
    
    
#writeListOfHistoLists(transposeLOL(transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Gprime1500800_tWb'):SignalSampleNames.index('Gprime20001500_tWb')+1])[plotnames.index('Weight_scale_variation_muR0p5_muF0p5'):plotnames.index('Weight_scale_variation_muR2p0_muF2p0')+1],SignalSamples[SignalSampleNames.index('Gprime1500800_tWb'):SignalSampleNames.index('Gprime20001500_tWb')+1],"","mus",True,False,False,"",False,False,False)
#writeListOfHistoLists(transposeLOL(transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Gprime22501300_tWb'):SignalSampleNames.index('Gprime25001800_tWb')+1])[plotnames.index('Weight_scale_variation_muR0p5_muF0p5'):plotnames.index('Weight_scale_variation_muR2p0_muF2p0')+1],SignalSamples[SignalSampleNames.index('Gprime22501300_tWb'):SignalSampleNames.index('Gprime25001800_tWb')+1],"","mus",True,False,False,"",False,False,False)
##writeListOfHistoLists(transposeLOL(transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Gprime1500800_tWb'):SignalSampleNames.index('Gprime25001800_tWb')+1])[plotnames.index('Weight_scale_variation_muR0p5_muF0p5'):plotnames.index('Weight_scale_variation_muR2p0_muF2p0')+1],SignalSamples[SignalSampleNames.index('Gprime1500800_tWb'):SignalSampleNames.index('Gprime25001800_tWb')+1],"","mus",True,False,False,"",False,False,False)
##writeListOfHistoLists(transposeLOL(transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Gprime1500800_tWb'):SignalSampleNames.index('Gprime25001800_tWb')+1])[plotnames.index('Weight_scale_variation_muR0p5_muF0p5'):plotnames.index('Weight_scale_variation_muR2p0_muF2p0')+1],SignalSamples[SignalSampleNames.index('Gprime1500800_tWb'):SignalSampleNames.index('Gprime25001800_tWb')+1],"","mus",True,False,False,"",False,False,False)
##writeListOfHistoLists(transposeLOL(transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Gprime1500800_tWb'):SignalSampleNames.index('Gprime25001800_tWb')+1])[plotnames.index('Weight_scale_variation_muR0p5_muF0p5'):plotnames.index('Weight_scale_variation_muR2p0_muF2p0')+1],SignalSamples[SignalSampleNames.index('Gprime1500800_tWb'):SignalSampleNames.index('Gprime25001800_tWb')+1],"","mus",True,False,False,"",False,False,False)

##writeListOfHistoLists(transposeLOL(transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Gprime1500800_ttZ'):SignalSampleNames.index('Gprime40003000_ttZ')+1])[plotnames.index('Weight_scale_variation_muR0p5_muF0p5'):plotnames.index('Weight_scale_variation_muR2p0_muF2p0')+1],SignalSamples[SignalSampleNames.index('Gprime1500800_ttZ'):SignalSampleNames.index('Gprime40003000_ttZ')+1],"","mus",True,False,False,"",False,False,False)

#writeListOfHistoLists(transposeLOL(transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Gprime1500800_ttH'):SignalSampleNames.index('Gprime20001500_ttH')+1])[plotnames.index('Weight_scale_variation_muR0p5_muF0p5'):plotnames.index('Weight_scale_variation_muR2p0_muF2p0')+1],SignalSamples[SignalSampleNames.index('Gprime1500800_ttH'):SignalSampleNames.index('Gprime20001500_ttH')+1],"","mus",True,False,False,"",False,False,False)
#writeListOfHistoLists(transposeLOL(transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Gprime22501300_ttH'):SignalSampleNames.index('Gprime27501500_ttH')+1])[plotnames.index('Weight_scale_variation_muR0p5_muF0p5'):plotnames.index('Weight_scale_variation_muR2p0_muF2p0')+1],SignalSamples[SignalSampleNames.index('Gprime22501300_ttH'):SignalSampleNames.index('Gprime27501500_ttH')+1],"","mus",True,False,False,"",False,False,False)
#writeListOfHistoLists(transposeLOL(transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Gprime30001500_ttH'):SignalSampleNames.index('Gprime40003000_ttH')+1])[plotnames.index('Weight_scale_variation_muR0p5_muF0p5'):plotnames.index('Weight_scale_variation_muR2p0_muF2p0')+1],SignalSamples[SignalSampleNames.index('Gprime30001500_ttH'):SignalSampleNames.index('Gprime40003000_ttH')+1],"","mus",True,False,False,"",False,False,False)


#writeListOfHistoLists(listOfHistoListsSignal,SignalSamples,"","mus",True,False,False,"",False,False,False)

              
for l,plot in zip(listOfHistoListsSignal,plotnames):
    av1500=0
    av1750=0
    av2000=0
    av2250=0
    av2500=0
    av2750=0
    av3000=0
    av3500=0
    av4000=0
    
    n1500=0
    n1750=0
    n2000=0
    n2250=0
    n2500=0
    n2750=0
    n3000=0
    n3500=0
    n4000=0
    for h in l:
        if "Gprime1500" in h.GetName():
            av1500+=h.GetMean()
            n1500+=1
        elif "Gprime1750" in h.GetName():
            av1750+=h.GetMean()
            n1750+=1
        elif "Gprime2000" in h.GetName():
            av2000+=h.GetMean()
            n2000+=1
        elif "Gprime2250" in h.GetName():
            av2250+=h.GetMean()
            n2250+=1
        elif "Gprime2500" in h.GetName():
            av2500+=h.GetMean()
            n2500+=1
        elif "Gprime2750" in h.GetName():
            av2750+=h.GetMean()
            n2750+=1            
        elif "Gprime3000" in h.GetName():
            av3000+=h.GetMean()
            n3000+=1 
        elif "Gprime3500" in h.GetName():
            av3500+=h.GetMean()
            n3500+=1 
        elif "Gprime4000" in h.GetName():
            av4000+=h.GetMean()
            n4000+=1 
            
    #av=av/float(len(l))
    
    print "Gstar ",plot,"   1500:",av1500/float(n1500),"  1750:",av1750/float(n1750),"  2000:",av2000/float(n2000),"  2250:",av2250/float(n2250),"  2500:",av2500/float(n2500),"  2750:",av2750/float(n2750),"  3000:",av3000/float(n3000),"  3500:",av3500/float(n3500),"  4000:",av4000/float(n4000)
    
   
   
   

    
for l,plot in zip(listOfHistoListsSignal,plotnames):
    print "####################",plot,"#####################"
    for h in l:
        print plot, "   ", h.GetName(),"  ", h.GetMean() 