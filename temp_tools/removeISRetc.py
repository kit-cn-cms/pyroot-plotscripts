#OPEN: what does this script do?
import sys

files=sys.argv[1:]

for f in files:
  theFile=open(f,"r")
  inlist=list(theFile)
  theFile.close()
  outlist=[]
  for line in inlist:
    if "number of nuisance parameters" in line:
      line="kmax * #number of nuisance parameters\n"
    if "CMS_ttH_FSR" in line or "CMS_ttH_ISR" in line or "CMS_ttH_ue" in line or "CMS_ttH_hdamp" in line:
      continue
    outlist.append(line)
  theFile=open(f,"w")
  for line in outlist:
    theFile.write(line)
  theFile.close()

