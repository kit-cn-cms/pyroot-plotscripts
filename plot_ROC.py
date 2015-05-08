from plotutils import *
# samples
samples=[Sample('t#bar{t}H',ROOT.kBlue,'/nfs/dust/cms/user/hmildner/trees/tth.root','') , Sample('t#bar{t}',ROOT.kRed+1,'/nfs/dust/cms/user/hmildner/trees/ttbar.root','')]

# selecion for categories
s4j3t="(N_Jets==4&&N_BTagsM==3)"
s4j4t="(N_Jets==4&&N_BTagsM>=4)"
s5j3t="(N_Jets==5&&N_BTagsM==3)"
s5j4t="(N_Jets==5&&N_BTagsM>=4)"
s6j2t="(N_Jets>=6&&N_BTagsM==2)"
s6j3t="(N_Jets>=6&&N_BTagsM==3)"
s6j4t="(N_Jets>=6&&N_BTagsM>=4)"

plots=[
    Plot(ROOT.TH1F("BDToutput_6j2t","BDT output (6j2t)",20,-1,1),"BDTOhio_v1_output",s6j2t),
    Plot(ROOT.TH1F("BDToutput_4j3t","BDT output (4j3t)",20,-1,1),"BDTOhio_v1_output",s4j3t),
    Plot(ROOT.TH1F("BDToutput_5j3t","BDT output (5j3t)",20,-1,1),"BDTOhio_v1_output",s5j3t),
    Plot(ROOT.TH1F("BDToutput_6j3t","BDT output (6j3t)",20,-1,1),"BDTOhio_v1_output",s6j3t),
    Plot(ROOT.TH1F("BDToutput_4j4t","BDT output (4j4t)",20,-1,1),"BDTOhio_v1_output",s4j4t),
    Plot(ROOT.TH1F("BDToutput_5j4t","BDT output (5j4t)",20,-1,1),"BDTOhio_v1_output",s5j4t),
    Plot(ROOT.TH1F("BDToutput_6j4t","BDT output (6j4t)",20,-1,1),"BDTOhio_v1_output",s6j4t),
]
listOfhistoLists=createHistoLists_fromTree(plots,samples,'MVATree')
writeListOfhistoLists(listOfhistoLists,samples,"bdts")
listOfhistoListsT=transposeLOL(listOfhistoLists)
superPair=getSuperHistoPair(listOfhistoListsT[0],listOfhistoListsT[1],'BDTOhio_v1')
superPair[0].SetTitle('histogram of all BDT bins')
writeListOfhistoLists([list(superPair)],samples,'superhistos')
roc=getROC(superPair[0],superPair[1])
writeListOfROCs([roc],['Ohio BDT v1'],[ROOT.kRed],'roc')

