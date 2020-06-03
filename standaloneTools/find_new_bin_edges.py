import os
import sys
from optparse import OptionParser
import ROOT


def split_comma_list(tosplit):
    returnlist = []
    print("Input to split:")
    print(tosplit)
    for c in tosplit:
        returnlist += c.split(",")
    print(returnlist)
    return returnlist

def do_rebinning(combinedHist, threshold):
    squaredError = 0.
    binContent = 0.
    bin_edges = []
    last_added_edge = 0
    nbins = combinedHist.GetNbinsX()
    for i in range(nbins, 0, -1):
        if i == nbins:
            last_added_edge = combinedHist.GetBinLowEdge(nbins+1)
            bin_edges.append(last_added_edge)

        # add together squared bin errors and bin contents
        squaredError += combinedHist.GetBinError(i)**2
        binContent += combinedHist.GetBinContent(i)
        # print("bin (low edge): {} ({})".format(i, combinedHist.GetBinLowEdge(i)))
        # print("bkg stack: {}".format(combinedHist.GetBinContent(i)))
        # print("sum: {}".format(binContent))

        # calculate relative error
        relerror = squaredError**0.5/binContent if not binContent == 0 else squaredError**0.5
        
        if binContent == 0: continue
        if threshold > 1:
            # do rebinning based on the population of the bins enterly
            # bins are ok if the bin content is larger than the threshold
            if binContent >= threshold:
                # if relative error is smaller than threshold, start new bin
                last_added_edge = combinedHist.GetBinLowEdge(i)
                bin_edges.append(last_added_edge)
                squaredError = 0.
                binContent = 0.
        else:
            # if relative error is smaller than threshold, start new bin
            if relerror <= threshold:
                last_added_edge = combinedHist.GetBinLowEdge(i)
                bin_edges.append(last_added_edge)
                squaredError = 0.
                binContent = 0.
    
    
    # underflow_edge = combinedHist.GetBinLowEdge(1)
    # if not underflow_edge in bin_edges:
    #     # if underflow_edge is not in bin_edges list the relative
    #     # error of the last bin is too small, so just merge the
    #     # first two bins by replacing the last_added_edge with
    #     # the underflow_edge 
    #     bin_edges[-1] = underflow_edge

    print("\tnew bin edges: [{}]".format(",".join([str(round(b,4)) for b in bin_edges])))
    return sorted(bin_edges)


def prepare_rebinning(rootfile, histolist, threshold = 0.1):
    print("\tWill rebin with these histograms:")
    for h in histolist:
        print("\t{}".format(h))
    h_added = None
    for h in histolist:
        h_tmp = rootfile.Get(h)
        if h_added is None:
            h_added = h_tmp.Clone("h_added")
            h_added.Reset()
        h_added.Add(h_tmp)
    if not h_added is None:
        print("\toriginal lower bin edges:")
        for i in range(1, h_added.GetNbinsX()+1):
            print("\t{}\t{}".format(i, h_added.GetBinLowEdge(i)))
        do_rebinning(combinedHist = h_added, threshold = threshold)
    else:
        print("ERROR: could not add any histograms!")


def rebin_histos_in_rootfile(inputfile, options):
    
    cats = split_comma_list(options.channels)
    
    procs = split_comma_list(options.processes)
    inputfile = os.path.abspath(inputfile)
    print(inputfile)
    print("ITS HAPPENING NOW")
    rfile = None
    rfile = ROOT.TFile.Open(inputfile)
    if not isinstance(rfile, ROOT.TFile):
        print("{} is not a TFile!".format(inputfile))
        return
    print("opened root file")

    keylist = [x.GetName() for x in rfile.GetListOfKeys()]
    # key = "$PROCESS_$CHANNEL"
    key = options.nomkey
    for cat in cats:
        print("Doing channel '{}'".format(cat))
        consider_for_rebinning = []
        for p in procs:
            tmp = key.replace("$PROCESS", p).replace("$CHANNEL", cat)
            print(tmp)
            if tmp in keylist:
                consider_for_rebinning.append(tmp)
            else:
                print("ERROR: Could not find histogram with name {} in inputfile {}".format(tmp, inputfile))
                continue
        if len(consider_for_rebinning) > 0:
            prepare_rebinning(rootfile = rfile, histolist = consider_for_rebinning, threshold = options.threshold)
        else:
            print("ERROR: Could not find any histograms to rebin in inputfile {}".format(inputfile))



def main(options, histofiles):
    for hfile in histofiles:
        rebin_histos_in_rootfile(inputfile = hfile, options = options)

def parse_arguments():
    parser = OptionParser()

    parser.add_option("-k", "--nomkey",
                        help = "use this string to select histogram keys, e.g. '$PROCESS__$CHANNEL' (this is the default)",
                        dest = "nomkey",
                        type = "str",
                        default = '$PROCESS__$CHANNEL'
                    )
    parser.add_option( "-c", "--channel",
                        help = """Do rebinning for this channel, e.g. 'ljets_ge4j_ge4t_ttH_node'.
                        Can be comma-separated list or called multiple times.
                        """,
                        action = "append",
                        dest = "channels",
                        type = "str"
            )
    parser.add_option( "-p", "--processes",
                        help = """Consider these processes for the rebinning.
                        Can be comma-separated list or called multiple times.
                        (default = 'ttbarPlusB_BBbar,ttbarPlusCCbar,ttbarOther,ttbarPlus2B')
                        """,
                        action = "append",
                        dest = "processes",
                        type = "str",
        )
    parser.add_option( "-t", "--threshold",
                        help = "threshold to use when bin uncertainties are used to decide on binning (default = 0.1)",
                        dest = "threshold",
                        default = 0.1,
                        type = "float"
                )

    options, args = parser.parse_args()
    if len(options.channels) == 0:
        parser.error("ERROR: You need to provide at least one category for rebinning")
    if options.processes is None:
        options.processes = ["ttbarOther,ttbarPlusB,ttbarPlus2B,ttbarPlusBBbar,ttbarPlusCCbar"]
    return options, args

if __name__ == '__main__':
    options, histofiles = parse_arguments()
    main(options = options, histofiles = histofiles)
