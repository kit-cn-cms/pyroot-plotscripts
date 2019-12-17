import ROOT
import sys
f = ROOT.TFile(sys.argv[1])
d = f.Get("Nominal")
procs = ["ttH", "Others", "ttbarOther", "ttbarPlus2B", "ttbarPlusB", "ttbarPlusBBbar", "ttbarPlusCCbar"]
for p in procs:
    h = d.Get(p)

    s = "    \"weight_CSVSF_SF_{}:=(".format(p)
    for i in range(2,10):
        iBin = h.FindBin(i)
        val = h.GetBinContent(iBin)
        if i == 9:
            s+="((N_Jets>={})*{})".format(i, val)
        else:
            s+="((N_Jets=={})*{})+".format(i, val)
    s+=")\","
    print(s)
