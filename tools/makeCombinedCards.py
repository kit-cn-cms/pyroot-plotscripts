import subprocess 
import sys
from namingMaps import *

inprefix=sys.argv[1]


# figure out stuff

outcards={}
for incard in inputCards:
  for combCard in inputCards[incard]:
    if combCard in outcards:
      outcards[combCard].append(inprefix+incard+".txt")
    else:
      outcards[combCard]=[inprefix+incard+".txt"]

for combination in outcards:
  print "----------------------------------"
  print "creating ", combination
  print "with "
  for incard in outcards[combination]:
    print incard
  cmd="combineCards.py "+" ".join(outcards[combination])+" > "+combination+".txt"
  print cmd
  subprocess.call(cmd, shell=True)