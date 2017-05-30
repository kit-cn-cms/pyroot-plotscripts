import sys

infile=open("systematicVariations.txt","r")
lines=list(infile)

for l in lines:
  #print l
  if "#" in l:
    continue
  name=l.replace("\n","")
  print "    \""+name+"up\",\""+name+"down\","
  #print name