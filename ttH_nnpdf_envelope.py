from plotutils import *

pdflist = []
id = 260001
colorlist = [ROOT.kRed,ROOT.kBlue,ROOT.kGreen+2,ROOT.kYellow+1,ROOT.kMagenta,ROOT.kAzure+4,ROOT.kCyan,ROOT.kSpring+10,ROOT.kOrange-3,ROOT.kRed-6]

samples=[]
samples.append(Sample('t#bar{t}Hbb',ROOT.kBlack,'/nfs/dust/cms/user/kschweig/ttHbb_nominal_Tree.root',""))
plots=[]
plots.append(Plot(ROOT.TH1F("N_Jets_"+str(id-1),"N_{Jets} ID"+str(id-1),11,-0.5,10.5),"N_Jets",""))
for i in range(100):
    plots.append(Plot(ROOT.TH1F("N_Jets_"+str(id+i),"N_{Jets} ID:"+str(id+i),11,-0.5,10.5),"N_Jets","Weight_NNPDFid"+str(id+i)))
listOfhistoLists=createHistoLists_fromTree(plots,samples,'MVATree')
nominal = []
for bin in range(listOfhistoLists[0][0].GetNbinsX()):
    nominal.append(listOfhistoLists[0][0].GetBinContent(bin))
#maximum = {0:1,1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1}
abwdic = {}
abwlist = []
for i in range(len(listOfhistoLists)-1):
    Abw = 0
    for ibin in range(listOfhistoLists[i+1][0].GetNbinsX()):
        if nominal[ibin] != 0:
            Abw = Abw + ((listOfhistoLists[i+1][0].GetBinContent(ibin)-nominal[ibin])/nominal[ibin])
    abwlist.append(Abw)
    abwdic[i+1] = Abw

print max(abwlist),min(abwlist)
maxhisto = 0
minhisto = 0
for key in abwdic:
    if abwdic[key] == max(abwlist):
        maxhisto = key
    if abwdic[key] == min(abwlist):
        minhisto = key

print maxhisto,minhisto


del samples
del plots
del listOfhistoLists

samples=[]
samples.append(Sample('t#bar{t}Hbb',ROOT.kBlack,'/nfs/dust/cms/user/kschweig/ttHbb_nominal_Tree.root',""))
samples.append(Sample('t#bar{t}Hbb NNPDF '+str(260000+maxhisto),ROOT.kRed,'/nfs/dust/cms/user/kschweig/ttHbb_nominal_Tree.root',"Weight_NNPDFid"+str(260000+maxhisto)))
samples.append(Sample('t#bar{t}Hbb NNPDF '+str(260000+minhisto),ROOT.kBlue,'/nfs/dust/cms/user/kschweig/ttHbb_nominal_Tree.root',"Weight_NNPDFid"+str(260000+minhisto)))

plots=[]
plots.append(Plot(ROOT.TH1F("N_Jets","N_{Jets}",11,-0.5,10.5),"N_Jets",""))
listOfhistoLists=createHistoLists_fromTree(plots,samples,'MVATree')
writeListOfHistoLists(listOfhistoLists,samples,"comp_nnpdf_ttHbb_env",False,False,False,'histoe',False,False,False)



#print listOfhistoLists



#    writeListOfHistoLists(listOfhistoLists,samples,"comp_nnpdf_ttHbb_"+str(id-10)+"-"+str(id-1),False,False,False,'histoe',False,False,False)
    
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
