from plotutils import *

pdflist = []
id = 260001
colorlist = [ROOT.kRed,ROOT.kBlue,ROOT.kGreen+2,ROOT.kYellow+1,ROOT.kMagenta,ROOT.kAzure+4,ROOT.kCyan,ROOT.kSpring+10,ROOT.kOrange-3,ROOT.kRed-6]
for i in range(10):
    samples=[]
    for j in range(10):
        samples.append(Sample('t#bar{t}Hbb NNPDF '+str(id),colorlist[j],'/nfs/dust/cms/user/kschweig/ttHbb_nominal_Tree.root',"Weight_NNPDFid"+str(id)))
        id = id+1
    samples.append(Sample('t#bar{t}Hbb NNPDF 260000',ROOT.kBlack,'/nfs/dust/cms/user/kschweig/ttHbb_nominal_Tree.root',""))
    plots=[
        Plot(ROOT.TH1F("N_Jets","N_{Jets}",15,-0.5,14.5),"N_Jets",""),
        ]
    listOfhistoLists=createHistoLists_fromTree(plots,samples,'MVATree')
    writeListOfHistoLists(listOfhistoLists,samples,"comp_nnpdf_ttHbb_"+str(id-10)+"-"+str(id-1),False,False,False,'histoe',False,False,False)
    del samples
    del plots
    del listOfhistoLists

    
"""
aslist = ["asdown265000", "asup266000"]
for a in aslist:
    samples=[
        Sample('t#bar{t}Hbb NNPDF Central Value',ROOT.kBlack,'/nfs/dust/cms/user/kschweig/ttHbb_nominal_T\
ree.root',"") ,
        Sample('t#bar{t}Hbb NNPDF '+a[-6:],ROOT.kRed,'/nfs/dust/cms/user/kschweig/ttHbb_nominal_Tree.root',"Weight_NNPDF"+a)
        ]

    plots=[
        Plot(ROOT.TH1F("N_Jets","N_{Jets}",11,-0.5,10.5),"N_Jets",""),
        ]

    listOfhistoLists=createHistoLists_fromTree(plots,samples,'MVATree')
    writeListOfHistoLists(listOfhistoLists,samples,"comp_nnpdf_ttHbb_"+a,False,False,False,'histoe',False,False,False)
    del samples
    del plots
    del listOfhistoLists
"""
