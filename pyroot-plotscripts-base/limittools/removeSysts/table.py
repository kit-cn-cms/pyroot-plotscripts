infile=open("results.txt","r")
inlist=list(infile)

for line in reversed(inlist):
#  print line
  splitline=line.split(" ")
#  print splitline
  name=splitline[0]
  value=splitline[1]
  improv=splitline[2].replace("\n","")
  nimp=float(improv)
  pimp=abs(100.0*nimp)
  rimp=round(pimp,2)
  print name.replace("_","\_")+" & "+str(rimp)+" \\ "
