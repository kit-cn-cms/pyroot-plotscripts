from plotutils import *

#samples
samples=[Sample('t#bar{t}',ROOT.kRed+1,'ttbar_test.root',''),Sample('t#bar{t}H',ROOT.kBlue,'tth_test.root','') ]

listOfhistoLists=createHistoLists_fromHistoFile(samples)
writeListOfhistoLists(listOfhistoLists,samples,'plots')

