#OPEN: what does this script do?
import sys

inf=sys.argv[1]
outf=sys.argv[2]

outfile=open(outf,"w")
infile=open(inf,"r")

lines=list(infile)

for line in lines:
  template="    Plot(ROOT.TH1F(plotprefix+\"NAME\",\"NAME\",30,0.0,10.0),\"NAME\",plotselection,plotlabel),"
  newline=template.replace("NAME",line.replace("\n",""))
  outfile.write(newline+"\n")
  
outfile.close()
