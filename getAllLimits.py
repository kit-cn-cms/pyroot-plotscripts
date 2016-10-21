import sys
import ROOT
from subprocess import call


def readLimit(fn='higgsCombineTest.Asymptotic.mH125.root'):
  f=ROOT.TFile(fn)
  t=f.Get('limit')
  up=-1.
  down=-1.
  upTwo=-1.
  downTwo=-1.
  limit=-1.
  for e in t:
    if e.quantileExpected>0.1 and e.quantileExpected<0.2: 
      down = e.limit
    elif e.quantileExpected==0.5: 
      limit= e.limit
    elif e.quantileExpected>0.8 and e.quantileExpected<0.9: 
      up = e.limit
    elif e.quantileExpected>0.0 and e.quantileExpected<0.1: 
      downTwo= e.limit
    elif e.quantileExpected>0.1 and e.quantileExpected<1.0: 
      upTwo = e.limit


  f.Close()
  return downTwo, down,limit,up, upTwo

resfile=open("results.txt","w")
limit_cats=[]
infilenames=sys.argv[1:]
for card in infilenames:
  cmd='combine -M Asymptotic --minosAlgo stepping -m 125 --run="blind" '+card
  call(cmd,shell=True) 
  d2, d1, m, u1, u2 = readLimit('higgsCombineTest.Asymptotic.mH125.root')
  err2Up=u2-m
  err1Up=u1-m
  err2Down=m-d2
  err1Down=m-d1
  texString="$%.1f^{+%.1f}_{-%.1f}$" % ( m, err1Up, err1Down)
  
  lims=[d2, d1, m , u1, u2, err2Up, err1Up, m , err1Down, err2Down]
  limstrings=[]
  for i in lims:
    limstrings.append(str(i))
  limstrings.append(texString)
  print limstrings
  outstr=card.replace(".txt","")+" "+" ".join(limstrings)
  print outstr
  resfile.write(outstr+"\n")
  #limit_cats.append([card.replace(".txt",""),readLimit('higgsCombineTest.Asymptotic.mH125.root')])
  #print limit_cats

resfile.close()
