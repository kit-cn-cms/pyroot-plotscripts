from plotutils import *

samples=[Sample('t#bar{t} spring15 powheg',ROOT.kBlue,'/nfs/dust/cms/user/kelmorab/Spring15_Base16thJuly/forTraining/ttbar/ttbar_nominal.root','') ,
         Sample('t#bar{t} spring15 amcNLO',ROOT.kRed,'/nfs/dust/cms/user/kelmorab/Spring15_Base16thJuly/forLimit/ttbar/ttbar_nominal.root',''), 
         Sample('t#bar{t} phys14 madgraph',ROOT.kGreen-3,'/nfs/dust/cms/user/hmildner/trees0717/ttbar.root',''), 
         ]


plots=[
    Plot(ROOT.TH1F("Jet_CSVb" ,"CSVv2 IVF b-jets",40,0,1),"Jet_CSV","abs(Jet_Flav)>4.5&&abs(Jet_Flav)<5.5"),
    Plot(ROOT.TH1F("Jet_CSVl" ,"CSVv2 IVF l-jets",40,0,1),"Jet_CSV","abs(Jet_Flav)<3.5||abs(Jet_Flav)>5.5"),
]



listOfhistoLists=createHistoLists_fromTree(plots,samples,'MVATree')

writeListOfhistoLists(listOfhistoLists,samples,'btag_plots')

roc_p=getROC(listOfhistoLists[0][0],listOfhistoLists[1][0],False)
roc_a=getROC(listOfhistoLists[0][1],listOfhistoLists[1][1],False)
writeListOfROCs([roc_p,roc_a],['powheg', 'amcnlo'],[ROOT.kBlue,ROOT.kRed],'btag_roc_pa',True,False)

eff_p=getEff(listOfhistoLists[0][0])
eff_a=getEff(listOfhistoLists[0][1])
writeListOfROCs([eff_p,eff_a],['powheg', 'amcnlo'],[ROOT.kBlue,ROOT.kRed],'btag_eff_pa',False,True)

roc_s15=getROC(listOfhistoLists[0][0],listOfhistoLists[1][0],False)
roc_p14=getROC(listOfhistoLists[0][2],listOfhistoLists[1][2],False)
writeListOfROCs([roc_s15,roc_p14],['spring15','phys14'],[ROOT.kBlue,ROOT.kRed],'btag_roc_sp',True,False)

eff_s15=getEff(listOfhistoLists[0][0])
eff_p14=getEff(listOfhistoLists[0][2])
writeListOfROCs([eff_s15,eff_p14],['spring15','phys14'],[ROOT.kBlue,ROOT.kRed],'btag_eff_sp',False,True)
