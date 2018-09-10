import sys
import subprocess

newROOTName=sys.argv[1]
files=sys.argv[2:]

#cmd="cp -v "+OldString+" "+newString
#subprocess.call(cmd,shell=True)
oldrootpath=""
for f in files:
  theFile=open(f,"r")
  inlist=list(theFile)
  theFile.close()
  outlist=[]
  for line in inlist:
    if ".root" in line:
      sl=line.split()
      for ss in sl:
        if ".root" in ss:
          oldrootpath=ss
      line=line.replace(oldrootpath,newROOTName)
    outlist.append(line)
  theFile=open(f,"w")
  for line in outlist:
    theFile.write(line)
  theFile.close()
  cmd="cp -v "+oldrootpath+" "+newROOTName.replace(".root","___"+oldrootpath.split("/")[-1])
  print cmd
  subprocess.call(cmd,shell=True)

