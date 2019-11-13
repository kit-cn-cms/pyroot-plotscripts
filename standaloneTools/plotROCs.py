import sys
import os
import optparse
import ROOT
from array import array
import numpy

def get_roc_point(threshold,h_sig,h_bkg):
    x_axis_sig = h_sig.GetXaxis()
    x_axis_bkg = h_bkg.GetXaxis()
    nbins = x_axis_sig.GetNbins()
    true_sig = 0.
    true_bkg = 0.
    all_sig = 0.
    all_bkg = 0.
    for i in range(nbins + 2):
        if x_axis_sig.GetBinLowEdge(i) >= threshold:
            true_sig += h_sig.GetBinContent(i)
        elif x_axis_bkg.GetBinLowEdge(i) < threshold:
            true_bkg += h_bkg.GetBinContent(i)
        all_sig += h_sig.GetBinContent(i)
        all_bkg += h_bkg.GetBinContent(i)
    if all_sig != 0:
        sig_efficiency = true_sig / float(all_sig)
    else:
        sig_efficiency = 0
    if all_bkg != 0:
        bkg_efficiency = true_bkg / float(all_bkg)
    else:
        bkg_efficiency = 0
    return sig_efficiency, 1-bkg_efficiency

def get_roc_graph(h_sig, h_bkg):
    x_points = array('f')
    y_points = array('f')
    for threshold in numpy.linspace(0., 1., 50):
        sig_eff, bkg_eff = get_roc_point(threshold, h_sig, h_bkg)
        x_points.append(1 - bkg_eff)
        y_points.append(sig_eff)
    roc_graph = ROOT.TGraph(len(x_points), x_points, y_points)
    return roc_graph

def drawROC(roc,label):
    c = ROOT.TCanvas(label,label,1000,1000)
    c.cd()
    roc.Draw("AC*")
    roc.GetXaxis().SetTitle("background rejection")
    roc.GetYaxis().SetTitle("signal efficiency")
    integral = 1-roc.Integral()
    print("{0}: ROCAUC: {1}".format(label,integral))

    text = ROOT.TLatex(0.11,0.8,"{0}: ROCAUC: {1}".format(label,integral))
    text.SetNDC(ROOT.kTRUE)
    text.SetTextSize(0.025)
    text.Draw()
    c.SaveAs("roc_"+label+".png")
    c.SaveAs("roc_"+label+".pdf")

def addHistos(lHistos):
    h_added=lHistos[0].Clone()
    h_added.Reset()
    for h in lHistos:
        h_added.Add(h)
    return h_added

"""
python plotROCs.py -f ../workdir/Monotop_controlplots_had/output_limitInput.root -s VectorMonotop_Mphi_2000_Mchi_500 -b bkg -d AK15Jet_TopTagger_SR_had,AK15Jet_DeepAK15_probQCD_SR_had,AK15Jet_DeepAK15_probQCDbb_SR_had,AK15Jet_DeepAK15_probQCDc_SR_had,AK15Jet_DeepAK15_probQCDcc_SR_had,AK15Jet_DeepAK15_probQCDothers_SR_had,AK15Jet_DeepAK15_probT_SR_had,AK15Jet_DeepAK15_probTbc_SR_had,AK15Jet_DeepAK15_probTbcq_SR_had,AK15Jet_DeepAK15_probTbcq_Tbc_SR_had,AK15Jet_DeepAK15_probTbq_SR_had,AK15Jet_DeepAK15_probTbq_Tbc_SR_had,AK15Jet_DeepAK15_probTbq_Tbcq_SR_had,AK15Jet_DeepAK15_probTbq_Tbcq_Tbc_SR_had,AK15Jet_DeepAK15_probTbq_Tbqq_SR_had,AK15Jet_DeepAK15_probTbq_Tbqq_Tbc_SR_had,AK15Jet_DeepAK15_probTbq_Tbqq_Tbcq_SR_had,AK15Jet_DeepAK15_probTbq_Tbqq_Tbcq_Tbc_SR_had,AK15Jet_DeepAK15_probTbqq_SR_had,AK15Jet_DeepAK15_probTbqq_Tbc_SR_had,AK15Jet_DeepAK15_probTbqq_Tbcq_SR_had,AK15Jet_DeepAK15_probTbqq_Tbcq_Tbc_SR_had,AK15Jet_DeepAK15_probWZ_SR_had,AK15Jet_DeepAK15_probW_SR_had,AK15Jet_DeepAK15_probWcq_SR_had,AK15Jet_DeepAK15_probWqq_SR_had,AK15Jet_DeepAK15_probZ_SR_had,AK15Jet_DeepAK15_probZbb_SR_had,AK15Jet_DeepAK15_probZcc_SR_had,AK15Jet_DeepAK15_probZqq_SR_had -l znunujets
"""
parser = optparse.OptionParser("usage: %prog [options]")

parser.add_option("-f", "--file", dest="file", type="string",help="Specify the output_limitInput.root file")
parser.add_option("-s", "--signal", dest="signal", type="string",help="Specify the name of the signal process , or a list of processes to be considered")
parser.add_option("-b", "--bkg", dest="bkg", type="string",help="Specify the name of the bkq process, or a list of processes to be considered")
parser.add_option("-d", "--discr", dest="discr",help="Specify a list of discriminators to plot the ROCs for")
parser.add_option("-l", "--label", dest="label",help="Specify an additional label to find bkg hists")

(opts, args) = parser.parse_args()

rFile = ROOT.TFile(opts.file, "READ")


for discr in opts.discr.split(","):
    print("\n\n"+"="*50)
    print("Doing ROC curve for  {}".format(discr))
    print("Checking Discrimination of {0} (sig) vs {1} (bkg)".format(opts.signal,opts.bkg))
    lBKGS = []
    for bkg in opts.bkg.split(","):
        lBKGS.append(rFile.Get(bkg+"_"+discr))
    h_bkg = addHistos(lBKGS)

    lSigs = []
    for sig in opts.signal.split(","):
        lSigs.append(rFile.Get(bkg+"_"+discr))
    h_sig = addHistos(lSigs)

    roc = get_roc_graph(h_sig, h_bkg)
    drawROC(roc, discr+"_"+opts.signal+"_vs_"+opts.bkg.replace(",","_"))

print("="*50)

