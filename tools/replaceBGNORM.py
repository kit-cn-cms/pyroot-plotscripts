import sys

files=sys.argv[1:]

listOfUncertaintiesToToggle=["bgnorm"]

for f in files:
  theFile=open(f,"r")
  inlist=list(theFile)
  theFile.close()
  outlist=[]
  for line in inlist:
    newline=line
    if "number of nuisance parameters" in line:
      newline="kmax * #number of nuisance parameters\n"
    lineContainsUncToRemove=False
    for unc in listOfUncertaintiesToToggle:
      if unc in line:
        if "1.35" in line:
          newline=line.replace("1.35","1.5")
        elif "1.5" in line:
          newline=line.replace("1.5","1.35")
    outlist.append(newline)
  theFile=open(f,"w")
  for line in outlist:
    theFile.write(line)
  theFile.close()

