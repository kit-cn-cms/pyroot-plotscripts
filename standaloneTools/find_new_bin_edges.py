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
    return returnlist

def do_rebinning(histo, threshold):
    errorsqared = 0.
    val = 0.
    bin_edges = []
    last_added_edge = 0
    for i in range(1, histo.GetNbinsX()+1):
        if i == 1:
            last_added_edge = histo.GetBinLowEdge(i)
            bin_edges.append(last_added_edge)

        errorsqared += histo.GetBinError(i)**2
        val += histo.GetBinContent(i)
        relerror = errorsqared**0.5/val if not val == 0 else errorsqared**0.5
        print("Rel. Error: {}".format(relerror))
        if relerror <= threshold:
            last_added_edge = histo.GetBinLowEdge(i+1)
            bin_edges.append(last_added_edge)
            # last_added_edge = histo.GetBinLowEdge(i+1)
            errorsqared = 0.
            val = 0
    overflow_edge = histo.GetBinLowEdge(histo.GetNbinsX()+2)
    if not overflow_edge in bin_edges: bin_edges.append(overflow_edge)
    print("\tNew Edges:[{}]".format(",".join([str(round(b,4)) for b in bin_edges])))


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
        do_rebinning(histo = h_added, threshold = threshold)
    else:
        print("ERROR: could not add any histograms!")


def rebin_histos_in_rootfile(inputfile, options):
    key = options.key
    cats = split_comma_list(options.channels)
    
    procs = split_comma_list(options.processes)

    rfile = ROOT.TFile.Open(inputfile)
    keylist = [x.GetName() for x in rfile.GetListOfKeys()]
    for cat in cats:
        print("Doing channel '{}'".format(cat))
        consider_for_rebinning = []
        for p in procs:
            tmp = key.replace("$PROCESS", p).replace("$CHANNEL", cat)
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

    parser.add_option("-k", "--key",
                        help = "use this string to select histogram keys, e.g. '$PROCESS_finaldiscr_$CHANNEL' (this is the default)",
                        dest = "key",
                        type = "str",
                        default = "$PROCESS_finaldiscr_$CHANNEL"
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
                        default = ["ttbarOther,ttbarPlusB,ttbarPlus2B,ttbarPlusBBbar,ttbarPlusCCbar"]
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
    return options, args

if __name__ == '__main__':
    options, histofiles = parse_arguments()
    main(options = options, histofiles = histofiles)
