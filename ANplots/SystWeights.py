import ROOT

# Put Plotsscript output here
inputpath='/nfs/dust/cms/user/shwillia/BoostedTTHScripts/LimitCalculation/Setup_160222/pyroot-plotscripts/ANplots/workdir/76controlplotsPlusBoosted_JER/output.root'

# Histogram used for reweighting
histname='JT'

# Start with number binbias (e.g. 4 for N_Jets)
binbias=0

# Bin Selections
binSelections=[ "N_Jets==4&&N_BTagsM==2",
                "N_Jets==5&&N_BTagsM==2",
                "N_Jets>=6&&N_BTagsM==2",
                "N_Jets==4&&N_BTagsM==3",
                "N_Jets==5&&N_BTagsM==3",
                "N_Jets>=6&&N_BTagsM==3",
                "N_Jets==4&&N_BTagsM>=4",
                "N_Jets==5&&N_BTagsM>=4",             
                "N_Jets>=6&&N_BTagsM>=4"
]

# name of wsystematic
systname='CMS_res_j'

# Get weights for the following processes
processes=[ 'ttH',
            'ttH_hbb',
            'ttH_hcc',
            'ttH_htt',
            'ttH_hgg',
            'ttH_hgluglu',
            'ttH_hww',
            'ttH_hzz',
            'ttH_hzg',
            'ttbarOther',
            'ttbarPlusCCbar',
            'ttbarPlusB',
            'ttbarPlus2B',
            'ttbarPlusBBbar',
            'singlet',
            'zjets',
            'wjets',
            'ttbarW',
            'ttbarZ',
            'diboson'
]

# Get file
infile = ROOT.TFile(inputpath)
keys = infile.GetListOfKeys()

hists=[[ROOT.TH1F(),ROOT.TH1F(),ROOT.TH1F()] for proc in processes]

for key in keys:
  keyname = key.GetName()
 
  if not histname in keyname:
    continue
  
  procindex=-1
  systtype=-1
  
  for iproc,proc in enumerate(processes):
    
    if proc == keyname.split('_')[0] or proc == keyname.split('_')[0]+'_'+keyname.split('_')[1] :
      
      print proc,proc == "ttH",keyname, keyname.split('_')[1][0], keyname.split('_')[1][0] == "h"
      if proc == "ttH" and keyname.split('_')[1][0] == "h":
        continue
      print proc,keyname
      procindex=iproc
    else:
      continue
    
    if systname in keyname:
      if systname+'Up' in keyname:
        systtype=1
      if systname+'Down' in keyname:
        systtype=2
    else:
      systtype=0
        
  if procindex<0 or systtype<0:
    continue
  
  hists[procindex][systtype]=infile.Get(keyname)

weights=[]
for hists in hists:
  upRatio   =hists[1]
  downRatio =hists[2]
  
  upRatio.Divide(hists[0])
  downRatio.Divide(hists[0])
  
  weights.append([])
  
  nbins=hists[0].GetNbinsX()
  
  print nbins
  
  for bin in range(nbins):
    bincontentup=upRatio.GetBinContent(bin+1)
    bincontentdown=downRatio.GetBinContent(bin+1)
    
    if bincontentup<=0.:
      bincontentup=1.
    if bincontentdown<=0.:
      bincontentdown=1.
      
    weights[-1].append([bincontentup,bincontentdown])

upstrings=[]
downstrings=[]

upstringall='('
downstringall='('

for iproc,proc in enumerate(weights):
  
  upstring='('
  downstring='('
  
  upstringall  +='((processname==\''+processes[iproc]+'\')*('
  downstringall+='((processname==\''+processes[iproc]+'\')*('
  
  print len(proc)
  
  for ibin,jetbin in enumerate(proc):
    
    upstring      +='('+str(jetbin[0])+'*('+binSelections[ibin]+'))'
    upstringall   +='('+str(jetbin[0])+'*('+binSelections[ibin]+'))'
    downstring    +='('+str(jetbin[1])+'*('+binSelections[ibin]+'))'
    downstringall +='('+str(jetbin[1])+'*('+binSelections[ibin]+'))'
    
    if ibin < len(proc)-1:
      upstring+='+'
      upstringall+='+'
      downstring+='+'
      downstringall+='+'
    else:
      upstring+=')'
      upstringall+=')'
      downstring+=')'
      downstringall+=')'
  
  upstrings.append(upstring)
  downstrings.append(downstring)
  
  upstringall+=')'
  downstringall+=')'
  
  if iproc < len(weights)-1:
    upstringall   +='\\n +'
    downstringall +='\\n +'
  else:
    upstringall+=')'
    downstringall+=')'
  
print upstrings
print downstrings

outfile = open(systname+'_weights.txt', 'w')
outfile.write(systname+'Up Weights:\n')
for iproc,proc in enumerate(upstrings):
  outfile.write(processes[iproc]+':   '+proc+'\n')
outfile.write('\n')  
outfile.write('All '+systname+'Up Weights:\n')
outfile.write(upstringall+'\n')
outfile.write('\n')
outfile.write(systname+'Down Weights:\n')
for iproc,proc in enumerate(downstrings):
  outfile.write(processes[iproc]+':   '+proc+'\n')
outfile.write('\n')
outfile.write('All '+systname+'Down Weights:\n')
outfile.write(downstringall+'\n')

outfile.close()


