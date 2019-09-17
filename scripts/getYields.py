import ROOT
import sys

processes = [
    "ttZbb",
    "ttZqq",
    "ttZll",
    "ttlf",
    "ttbb",
    "ttcc",
    "singlet",
    "wjets",
    "zjets",
    "ttH",
    "ttW",
    "diboson",
    "data_obs",
    "SingleEl",
    "SingleMu",
    ]

f = ROOT.TFile(sys.argv[1], "READ")
histName = "_inclusive_eventYields"

bins = [
    "4j",
    "5j",
    "6j",
    ]

for i, b in enumerate(bins):
    print("\n"+b+"\n")
    for p in processes:
        h = f.Get(p+histName)
        integral = h.GetBinContent(i+1)+h.GetBinContent(i+4)
        error = (h.GetBinError(i+1)**2+h.GetBinError(i+4)**2)**(1./2.)
        #entries = h.GetEntries(i+1)
        print("{} | {} +- {} | {}".format(p, integral, error, "*"))
 
print("\ntotal yield\n")
for p in processes:
    h = f.Get(p+histName)
    integral = 0
    squerr = 0
    for i in range(6):
        integral += h.GetBinContent(i+1)
        squerr += h.GetBinError(i+1)**2

    print("{} | {} +- {} | {}".format(p, integral, squerr**0.5, "*"))
