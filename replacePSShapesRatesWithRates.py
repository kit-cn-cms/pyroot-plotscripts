import sys
import ROOT
from math import *

rootfile=sys.argv[1]
incards=sys.argv[2:]

discrname="finaldiscr"
nuisanceStringsToFind=["CMS_ttHbb_ISR","CMS_ttHbb_FSR","CMS_ttHbb_HDAMP","CMS_ttHbb_UE"]
f=ROOT.TFile(rootfile,"READ")

def round_to_sign(x):
  x=float(x)
  strx=str(x)
  afterDecimal=float("0."+strx.split(".")[1])
  if afterDecimal==0.0:
    return x
  minNDigs=3
  actualNDigs=-int(floor(log10(abs(afterDecimal))))
  nDigs=max(actualNDigs,minNDigs)
  #print nDigs, actualNDigs
  return round(x, nDigs)

def replaceShapeWithRate(rootfile,card,nuisanceStringsToFind):
  
  binlist=[]
  processlist=[]
  infile=open(card,"r")
  inlist=list(infile)
  infile.close()
  outfile=open(card,"w")
  newlist=[]
  afterHeader=False
  afterNuisStart=False
  for line in inlist:
    newline=line
    print line
    if "observation" in line:
      afterHeader=True
    if afterHeader:
      if "bin" in line:
        binlist=line.replace("  "," ").replace("\n","").replace("\t"," ").split(" ")
        print binlist
      if "process" in line and "tt" in line:
        processlist=line.replace("  "," ").replace("\n","").replace("\t"," ").split(" ")
        afterNuisStart=True
        print processlist
    if afterNuisStart:
      for nuis in nuisanceStringsToFind:
        if nuis in line:
          splitline=line.replace("shape","lnN").replace("  "," ").replace("\n","").replace("\t"," ").split(" ")
          actualNuisName=splitline[0]
          #print splitline
          newlinelist=splitline[:2]
          #print newlinelist
          for icol, col in enumerate(splitline[2:]):
            procname=processlist[1:][icol]
            histprefix=binlist[1:][icol]
            #print icol, col,histprefix, procname
            if col!="-":
              # need to replace this
              print "replacing", icol, col, procname+"_"+discrname+"_"+histprefix
              print "loading ", procname+"_"+discrname+"_"+histprefix+"_"+actualNuisName.replace("#","")+"Up"
              print "loading ", procname+"_"+discrname+"_"+histprefix+"_"+actualNuisName.replace("#","")+"Down"
              hnom=f.Get(procname+"_"+discrname+"_"+histprefix)
              hup=f.Get(procname+"_"+discrname+"_"+histprefix+"_"+actualNuisName.replace("#","")+"Up")
              hdown=f.Get(procname+"_"+discrname+"_"+histprefix+"_"+actualNuisName.replace("#","")+"Down")
              if hnom==None or hup==None or hdown==None:
                print "ERROR did not find histos", procname+"_"+discrname+"_"+histprefix
                exit(1)
              nomInt=hnom.Integral()
              upInt=hup.Integral()
              downInt=hdown.Integral()
              if nomInt==0:
                nomInt=0.001
              upRatio=upInt/nomInt
              downRatio=downInt/nomInt
              print nomInt, upInt, downInt, upRatio, downRatio
              downRatio=round_to_sign(downRatio)
              upRatio=round_to_sign(upRatio)
              print nomInt, upInt, downInt, upRatio, downRatio
              newcol=str(downRatio)+"/"+str(upRatio)
              newlinelist.append(newcol)
            else:
              newlinelist.append(col)
          newline=" ".join(newlinelist)+"\n"
          print newline
    outfile.write(newline)
  
  outfile.close()
              
              
            
            
      

for card in incards:
  replaceShapeWithRate(rootfile,card,nuisanceStringsToFind)