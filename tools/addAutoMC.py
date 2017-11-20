import os
import sys
import glob

datacards = sys.argv[1:]

for datacard in datacards:
	for d in glob.glob(datacard):
		newlines = []
		with open(d, "r+") as infile:
			lines = infile.read().splitlines()
			categories = []
			for n, line in enumerate(lines):
				if n != len(lines) and line.startswith("bin") and lines[n+1].startswith("observation"):
					categories = line.split()[1:]
					print "found categories:\n", categories
				if not "BDTbin" in line:
					if line.startswith("kmax"):
						entries = line.split()
						entries[1] = "*"
						line = " ".join(entries)
					newlines.append(line)
				else:
					print "skipping", line
			for cat in categories:
				automc = cat + " autoMCStats 0 0 1"
				if automc in lines:
					continue
				print "writing line", automc
				newlines.append(automc)
		with open(d,"w") as newfile:
			newfile.write("\n".join(newlines))
			
