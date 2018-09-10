import ROOT
import sys

infile=sys.argv[1]

f=ROOT.TFile(infile,"READ")

frs=[]
frB=f.Get("fit_b")
frS=f.Get("fit_s")
frlist=[["s+b",frS],["b-only",frB]]

print frlist
bothGood=0
for fr in frlist:
  quality=-1
  quality=fr[1].covQual()
  print quality
  if quality==-1:
    print fr[0], "Unknown, matrix was externally provided"
  elif quality==0:
    print fr[0], "Not calculated at all"
  elif quality==1:
    print fr[0], "Approximation only, not accurate"  
  elif quality==2:
    print fr[0], "Full matrix, but forced positive-definite"
  elif quality==3:
    print fr[0], "Full, accurate covariance matrix"
    bothGood+=1

if bothGood==2:
  print "Both matrices were Full, accurate covariance matrices"