#############
# plot general control distributions 
##############

from plotconfig_generator import *
from plot_additional_Zprime_MC import *
from plot_cuts_ZPrime_MC import *

sys.path.insert(0, 'limittools')
from limittools import renameHistos
import copy



name='generatorplots'




plots=[
    Plot(ROOT.TH1F( "Gen_ZPrime_M" ,"m(Z') in GeV" ,300,0,3000),"Gen_ZPrime_M", "Gen_ZPrime_M>0", ""),
    Plot(ROOT.TH1F( "Gen_TPrimeandTPrimebar_M" ,"m(T) in GeV" ,35,0,1400),"Gen_TPrimeandTPrimebar_M", "Gen_TPrimeandTPrimebar_M>0", ""),
    Plot(ROOT.TH1F( "Gen_TPrimeandTPrimebar_Pt" ,"p_{T}(T) in GeV" ,35,0,1400),"Gen_TPrimeandTPrimebar_Pt", "Gen_TPrimeandTPrimebar_Pt>0", ""),
    Plot(ROOT.TH1F( "Gen_TopandTopbar_Pt" ,"p_{T}(t) in GeV" ,35,0,1400),"Gen_TopandTopbar_Pt", "Gen_TopandTopbar_Pt>0", ""),
    Plot(ROOT.TH1F( "Gen_WfromTPrimeandTPrimebar_Pt" ,"p_{T}(W from T) in GeV" ,35,0,1400),"Gen_WfromTPrimeandTPrimebar_Pt", "Gen_WfromTPrimeandTPrimebar_Pt>0", ""),
    Plot(ROOT.TH1F( "Gen_BottomfromTPrimeandTPrimebar_Pt" ,"p_{T}(b from T) in GeV" ,35,0,1400),"Gen_BottomfromTPrimeandTPrimebar_Pt", "Gen_BottomfromTPrimeandTPrimebar_Pt>0", ""),
    
    Plot(ROOT.TH1F( "Gen_Top_TPrime_DeltaR" ,"#Delta R(t,T)" ,35,0,7),"Gen_Top_TPrime_DeltaR", "Gen_Top_TPrime_DeltaR>0", ""),
    Plot(ROOT.TH1F( "Gen_Top_WfromTPrime_DeltaR" ,"#Delta R(t,W from T)" ,35,0,7),"Gen_Top_WfromTPrime_DeltaR", "Gen_Top_WfromTPrime_DeltaR>0", ""),
    Plot(ROOT.TH1F( "Gen_Top_BottomfromTPrime_DeltaR" ,"#Delta R(t,b from T)" ,35,0,7),"Gen_Top_BottomfromTPrime_DeltaR", "Gen_Top_BottomfromTPrime_DeltaR>0", ""),
    Plot(ROOT.TH1F( "Gen_WfromTPrime_BottomfromTPrime_DeltaR" ,"#Delta R(W from T,b from b)" ,35,0,7),"Gen_WfromTPrime_BottomfromTPrime_DeltaR", "Gen_WfromTPrime_BottomfromTPrime_DeltaR>0", ""),
]





plotnames=[]
for i in plots:
    plotnames.append(i.name)

#OnlyFirstList=len(plots)*[False]
#OnlyFirstList[plotnames.index("ABCD1_notopbtag_CatA_Zprime_M"):plotnames.index('ABCD2_inclusive_CatH_Tprime_M') +1 ] = len(OnlyFirstList[plotnames.index("ABCD1_notopbtag_CatA_Zprime_M"):plotnames.index('ABCD2_inclusive_CatH_Tprime_M') + 1 ] ) * [True]
#OnlyFirstList[plotnames.index(ABCDversion + "_notopbtag_CatA_Zprime_M"):plotnames.index(ABCDversion + "_notopbtag_CatA_Zprime_eff") +1 ] = len(OnlyFirstList[plotnames.index(ABCDversion + "_notopbtag_CatA_Zprime_M"):plotnames.index(ABCDversion + "_notopbtag_CatA_Zprime_eff") + 1 ] ) * [True]

#print OnlyFirstList, 'This is the boolean List for only first elements'


outputpath=plotParallel(name,2000000,plots,SignalSamples)


SignalLOL=createHistoLists_fromSuperHistoFile(outputpath,SignalSamples,plots)

writeListOfHistoLists(SignalLOL,SignalSamples, "",name,True,False,False,'C',False, False,False,False,False)

