import sys
import ROOT
ROOT.gDirectory.cd('PyROOT:/')
ROOT.gROOT.SetBatch(True)

infiles=sys.argv[1:]

toRemove=['singlet', 'wjets', 'zjets', 'ttbarW', 'ttbarZ', 'diboson']

for inf in infiles:
  infl=open(inf,"r")
  outf=open("removed_"+inf,"w")
  inlist=list(infl)
  infprocs=[]
  for line in inlist:
    if "process " in line and infprocs==[]:
      print "found process line"
      sl=line.replace("\n","").replace("\t","").replace("  "," ").split(" ")
      print sl
      for pl in sl[1:]:
	infprocs.append(pl)
      print infprocs
  for line in inlist:
    sl=line.replace("\n","").replace("\t","").replace("  "," ").split(" ")
    print sl
    if len(sl)<len(infprocs):
      outf.write(line)
    else:
      if ("bin" in line or "process" in line or "rate" in line) and not ( "shape" in line or "Combin" in line):
	newline=sl[0]
	for im,m in enumerate(sl[1:]):
	  print im, m
	  if infprocs[im] in toRemove:
	    print "remove ", infprocs[im], " in ", sl[0]
	    newline+=""
	  else:
	    newline+=" "+m
	newline+="\n"
      elif "lnN" in line or "shape " in line:
	newline=sl[0]+" "+sl[1]
	for im,m in enumerate(sl[2:]):
	  if infprocs[im] in toRemove:
	    print "remove ", infprocs[im], " in ", sl[0]
	    newline+=""
	  else:
	    newline+=" "+m
	newline+="\n"
      else:
	newline=line
      outf.write(newline)
  outf.close()