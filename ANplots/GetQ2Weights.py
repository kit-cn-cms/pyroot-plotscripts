import ROOT

inputpath="/nfs/dust/cms/user/shwillia/BoostedTTHScripts/LimitCalculation/Setup_160222/pyroot-plotscripts/ANplots/workdir/76controlplotsPlusBoosted/output.root"


infile = ROOT.TFile(inputpath)
keys = infile.GetListOfKeys()

histname="N_Jets"

ttbarProcesses=[  "ttbarOther",
                  "ttbarPlusCCbar",
                  "ttbarPlusB",
                  "ttbarPlus2B",
                  "ttbarPlusBBbar"
]

ttbarHists=[[ROOT.TH1F(),ROOT.TH1F(),ROOT.TH1F()] for proc in ttbarProcesses]

for key in keys:
  keyname = key.GetName()
 
  if not histname in keyname:
    continue
  
  procindex=-1
  systtype=-1
  
  for iproc,proc in enumerate(ttbarProcesses):
    
    if proc == keyname.split('_')[0]:
      procindex=iproc
    else:
      continue
    
    if 'CMS_ttH_Q2scale' in keyname:
      if '_'+proc+'Up' in keyname:
        systtype=1
      if '_'+proc+'Down' in keyname:
        systtype=2
    else:
      systtype=0
        
  if procindex<0 or systtype<0:
    continue
  
  ttbarHists[procindex][systtype]=infile.Get(keyname)

Q2weights=[]
for hists in ttbarHists:
  upRatio   =hists[1]
  downRatio =hists[2]
  
  upRatio.Divide(hists[0])
  downRatio.Divide(hists[0])
  
  Q2weights.append([])
  
  nbins=hists[0].GetNbinsX()
  
  for bin in range(nbins):
    Q2weights[-1].append([upRatio.GetBinContent(bin+1),downRatio.GetBinContent(bin+1)])

upstrings=[]
downstrings=[]

binbias=4

for proc in Q2weights:
  
  upstring="("
  downstring="("
  
  for ibin,jetbin in enumerate(proc):
  
    if ibin < len(proc)-1:
      upstring+="("+str(jetbin[0])+"*("+histname+"=="+str(ibin+binbias)+"))+"
      downstring+="("+str(jetbin[1])+"*("+histname+"=="+str(ibin+binbias)+"))+"
    else:
      upstring+="("+str(jetbin[0])+"*("+histname+">="+str(ibin+binbias)+")))"
      downstring+="("+str(jetbin[1])+"*("+histname+">="+str(ibin+binbias)+")))"
    
  upstrings.append(upstring)
  downstrings.append(downstring)
  
print upstrings
print downstrings

outfile = open('Q2weights.txt', 'w')
outfile.write('Q2 Up Weights:\n')
for iproc,proc in enumerate(upstrings):
  outfile.write(ttbarProcesses[iproc]+':   '+proc+'\n')
outfile.write('\n')
outfile.write('Q2 Down Weights:\n')
for iproc,proc in enumerate(downstrings):
  outfile.write(ttbarProcesses[iproc]+':   '+proc+'\n')
outfile.close()
