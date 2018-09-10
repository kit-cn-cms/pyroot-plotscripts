import sys
import subprocess

OldString=sys.argv[1]
newString=sys.argv[2]
files=sys.argv[3:]

cmd="cp -v "+OldString+" "+newString
subprocess.call(cmd,shell=True)

for f in files:
  theFile=open(f,"r")
  inlist=list(theFile)
  theFile.close()
  outlist=[]
  for line in inlist:
    line=line.replace(OldString,newString)
    outlist.append(line)
  theFile=open(f,"w")
  for line in outlist:
    theFile.write(line)
  theFile.close()

