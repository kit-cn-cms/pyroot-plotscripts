import sys
import os
import optparse
import ROOT
from array import array
import numpy
from math import sqrt


def get_roc_point(threshold, h_sig, h_bkg, from_right = False):
    x_axis_sig = h_sig.GetXaxis()
    x_axis_bkg = h_bkg.GetXaxis()
    nbins = x_axis_sig.GetNbins()
    true_sig = 0.0
    true_bkg = 0.0
    all_sig = 0.0
    all_bkg = 0.0
    for i in range(1, nbins + 1):
        if x_axis_sig.GetBinLowEdge(i) >= threshold:
            true_sig += h_sig.GetBinContent(i)
        elif x_axis_bkg.GetBinLowEdge(i) < threshold:
            true_bkg += h_bkg.GetBinContent(i)
        all_sig += h_sig.GetBinContent(i)
        all_bkg += h_bkg.GetBinContent(i)
    if from_right:
        true_sig = all_sig - true_sig
        true_bkg = all_bkg - true_bkg
    print "true sig: ",true_sig
    print "true bkg: ",true_bkg
    print "false bkg: ",all_bkg - true_bkg
    if all_sig != 0:
        sig_efficiency = true_sig / all_sig
    else:
        sig_efficiency = 0
    if all_bkg != 0:
        bkg_efficiency = true_bkg / all_bkg
    else:
        bkg_efficiency = 0
    s_b = None
    try:
        s_b = true_sig / sqrt(all_bkg - true_bkg)
    except ZeroDivisionError:
        s_b = None
    print (
        "WP:",
        round(threshold, 3),
        "sig eff:",
        round(sig_efficiency, 3),
        "bkg rej",
        round((bkg_efficiency), 3),
        "S/sqrt(B):",
        s_b,
    )
    return sig_efficiency, 1 - bkg_efficiency, s_b


def get_graphs(h_sig, h_bkg, min, max, from_right = False):
    x_roc_points = array("f")
    y_roc_points = array("f")
    x_sb_points = array("f")
    y_sb_points = array("f")
    # add (0,0) point for calculation of correct integral
    x_roc_points.append(0.0)
    y_roc_points.append(0.0)
    for threshold in numpy.linspace(min, max, 40):
        sig_eff, bkg_eff, s_b = get_roc_point(threshold, h_sig, h_bkg, from_right)
        x_roc_points.append(1 - bkg_eff)
        y_roc_points.append(sig_eff)
        if s_b!=None:
            x_sb_points.append(threshold)
            y_sb_points.append(s_b) 
    roc_graph = ROOT.TGraph(len(x_roc_points), x_roc_points, y_roc_points)
    sb_graph = ROOT.TGraph(len(x_sb_points), x_sb_points, y_sb_points)
    return roc_graph,sb_graph


def drawROC(roc, signal_label, background_label, discr_label, cat_label):
    c = ROOT.TCanvas("ROC" + "_" + signal_label, "ROC", 1200, 1200)
    c.cd()
    c.SetGrid()
    # calculate integral with (0,0) included to get correct result
    integral = round(roc.Integral(), 3)
    # then remove the (0,0) point for plotting purposes
    roc.RemovePoint(0)
    roc.Draw("ALP")
    roc.SetTitle("")
    roc.GetXaxis().SetTitle("background rejection")
    roc.GetYaxis().SetTitle("signal efficiency")
    roc.SetLineColor(ROOT.kRed)
    roc.SetLineWidth(2)
    roc.SetMarkerStyle(20)
    roc.SetMarkerColor(ROOT.kBlack)
    print ("ROCAUC: {integral}".format(integral=integral))

    text_cms = ROOT.TLatex(0.2, 0.94, "CMS #scale[0.8]{simulation}")
    text_cms.SetNDC(ROOT.kTRUE)
    text_cms.SetTextSize(0.035)
    text_cms.Draw()

    text_wip = ROOT.TLatex(0.2, 0.91, "work in progress")
    text_wip.SetNDC(ROOT.kTRUE)
    text_wip.SetTextSize(0.025)
    text_wip.Draw()

    text_auc = ROOT.TLatex(0.70, 0.85, "ROCAUC: {integral}".format(integral=integral))
    text_auc.SetNDC(ROOT.kTRUE)
    text_auc.SetTextSize(0.025)
    text_auc.Draw()

    text_signal = ROOT.TLatex(0.15, 0.4, "Signal: {signal}".format(signal=signal_label))
    text_signal.SetNDC(ROOT.kTRUE)
    text_signal.SetTextSize(0.025)
    text_signal.Draw()

    text_bkg = ROOT.TLatex(
        0.15, 0.35, "Background: {background}".format(background=background_label)
    )
    text_bkg.SetNDC(ROOT.kTRUE)
    text_bkg.SetTextSize(0.025)
    text_bkg.Draw()

    text_discr = ROOT.TLatex(
        0.15, 0.3, "Discriminator: {discr}".format(discr=discr_label)
    )
    text_discr.SetNDC(ROOT.kTRUE)
    text_discr.SetTextSize(0.025)
    text_discr.Draw()

    text_cat = ROOT.TLatex(0.15, 0.25, "Category: {cat}".format(cat=cat_label))
    text_cat.SetNDC(ROOT.kTRUE)
    text_cat.SetTextSize(0.025)
    text_cat.Draw()

    c.SaveAs("roc_" + discr_label + "_" + signal_label + ".png")
    c.SaveAs("roc_" + discr_label + "_" + signal_label + ".pdf")

def drawSoverB(sb_graph, signal_label, background_label, discr_label, cat_label):
    c = ROOT.TCanvas("S_B" + "_" + signal_label, "S/sqrt(B)", 1300, 1000)
    pad = c.cd()
    pad.SetLeftMargin(0.12)
    c.SetGrid()
    sb_graph.Draw("ALP")
    sb_graph.SetTitle("")
    sb_graph.GetXaxis().SetTitle("working point")
    sb_graph.GetYaxis().SetTitle("s/#sqrt{b}")
    sb_graph.SetLineColor(ROOT.kRed)
    sb_graph.SetLineWidth(2)
    sb_graph.SetMarkerStyle(20)
    sb_graph.SetMarkerColor(ROOT.kBlack)

    text_cms = ROOT.TLatex(0.20, 0.94, "CMS #scale[0.8]{simulation}")
    text_cms.SetNDC(ROOT.kTRUE)
    text_cms.SetTextSize(0.035)
    text_cms.Draw()

    text_wip = ROOT.TLatex(0.20, 0.91, "work in progress")
    text_wip.SetNDC(ROOT.kTRUE)
    text_wip.SetTextSize(0.025)
    text_wip.Draw()

    text_signal = ROOT.TLatex(0.15, 0.8, "Signal: {signal}".format(signal=signal_label))
    text_signal.SetNDC(ROOT.kTRUE)
    text_signal.SetTextSize(0.025)
    text_signal.Draw()

    text_bkg = ROOT.TLatex(
        0.15, 0.75, "Background: {background}".format(background=background_label)
    )
    text_bkg.SetNDC(ROOT.kTRUE)
    text_bkg.SetTextSize(0.025)
    text_bkg.Draw()

    text_discr = ROOT.TLatex(
        0.15, 0.7, "Discriminator: {discr}".format(discr=discr_label)
    )
    text_discr.SetNDC(ROOT.kTRUE)
    text_discr.SetTextSize(0.025)
    text_discr.Draw()

    text_cat = ROOT.TLatex(0.15, 0.65, "Category: {cat}".format(cat=cat_label))
    text_cat.SetNDC(ROOT.kTRUE)
    text_cat.SetTextSize(0.025)
    text_cat.Draw()

    c.SaveAs("sb_" + discr_label + "_" + signal_label + ".png")
    c.SaveAs("sb_" + discr_label + "_" + signal_label + ".pdf")

def addHistos(lHistos):
    h_added = lHistos[0].Clone()
    h_added.Reset()
    for h in lHistos:
        h_added.Add(h)
    return h_added


"""
python plotROCs.py -f ../workdir/Monotop_controlplots_had/output_limitInput.root -s VectorMonotop_Mphi_2000_Mchi_500 -b bkg -d AK15Jet_TopTagger_SR_had,AK15Jet_DeepAK15_probQCD_SR_had,AK15Jet_DeepAK15_probQCDbb_SR_had,AK15Jet_DeepAK15_probQCDc_SR_had,AK15Jet_DeepAK15_probQCDcc_SR_had,AK15Jet_DeepAK15_probQCDothers_SR_had,AK15Jet_DeepAK15_probT_SR_had,AK15Jet_DeepAK15_probTbc_SR_had,AK15Jet_DeepAK15_probTbcq_SR_had,AK15Jet_DeepAK15_probTbcq_Tbc_SR_had,AK15Jet_DeepAK15_probTbq_SR_had,AK15Jet_DeepAK15_probTbq_Tbc_SR_had,AK15Jet_DeepAK15_probTbq_Tbcq_SR_had,AK15Jet_DeepAK15_probTbq_Tbcq_Tbc_SR_had,AK15Jet_DeepAK15_probTbq_Tbqq_SR_had,AK15Jet_DeepAK15_probTbq_Tbqq_Tbc_SR_had,AK15Jet_DeepAK15_probTbq_Tbqq_Tbcq_SR_had,AK15Jet_DeepAK15_probTbq_Tbqq_Tbcq_Tbc_SR_had,AK15Jet_DeepAK15_probTbqq_SR_had,AK15Jet_DeepAK15_probTbqq_Tbc_SR_had,AK15Jet_DeepAK15_probTbqq_Tbcq_SR_had,AK15Jet_DeepAK15_probTbqq_Tbcq_Tbc_SR_had,AK15Jet_DeepAK15_probWZ_SR_had,AK15Jet_DeepAK15_probW_SR_had,AK15Jet_DeepAK15_probWcq_SR_had,AK15Jet_DeepAK15_probWqq_SR_had,AK15Jet_DeepAK15_probZ_SR_had,AK15Jet_DeepAK15_probZbb_SR_had,AK15Jet_DeepAK15_probZcc_SR_had,AK15Jet_DeepAK15_probZqq_SR_had -l znunujets
"""
parser = optparse.OptionParser("usage: %prog [options]")

parser.add_option(
    "-f",
    "--file",
    dest="file",
    type="string",
    help="Specify the output_limitInput.root file",
)
parser.add_option(
    "-s",
    "--signal",
    dest="signal",
    type="string",
    help="Specify the name of the signal process , or a list of processes to be considered",
)
parser.add_option(
    "-b",
    "--bkg",
    dest="bkg",
    type="string",
    help="Specify the name of the bkq process, or a list of processes to be considered",
)
parser.add_option(
    "-d",
    "--discr",
    dest="discr",
    help="Specify a list of discriminators to plot the ROCs for",
)
parser.add_option(
    "--discr_min",
    dest="discr_min",
    type="string",
    default="0.0",
    help="minimum value of discriminator range",
)
parser.add_option(
    "--discr_max",
    dest="discr_max",
    type="string",
    default="1.0",
    help="maximum value of discriminator range",
)
parser.add_option(
    "-l", "--label", dest="label", help="Specify an additional label to find bkg hists"
)
parser.add_option(
    "--from_right", dest="from_right", action = "store_true", default=False, help = "set this flag if you want to start from the right side of the histogram"
)
parser.add_option(
    "--add_sigs", dest="add_sigs", action = "store_true", default=False, help = "set this flag if you want to add the signal histograms"
)


(opts, args) = parser.parse_args()

rFile = ROOT.TFile(opts.file, "READ")


for discr in opts.discr.split(","):
    print ("\n\n" + "=" * 50)
    print ("Doing ROC curve for  {}".format(discr))
    print (
        "Checking Discrimination of {0} (sig) vs {1} (bkg)".format(
            opts.signal, opts.bkg
        )
    )
    backgrounds = opts.bkg.split(",")
    lBkgs = []
    for bkg in backgrounds:
        print(bkg + "_" + discr + "_" + opts.label)
        bkg_hist = rFile.Get(bkg + "_" + discr + "_" + opts.label)
        if bkg_hist.Integral() == 0:
            continue
        lBkgs.append(bkg_hist)
    h_bkg = addHistos(lBkgs)
    h_bkg.Print()

    signals = opts.signal.split(",")
    lSigs = []
    for sig in signals:
        sig_hist = rFile.Get(sig + "_" + discr + "_" + opts.label)
        # sig_hist = rFile.Get(sig + "_" + discr)
        # print(sig_hist.Integral())
        if sig_hist.Integral() == 0:
            continue
        sig_hist.Print()
        if not opts.add_sigs:
            sig_hist.Scale(h_bkg.Integral()/sig_hist.Integral())
        lSigs.append(sig_hist)
    if opts.add_sigs:
        h_sigs = addHistos(lSigs)
        h_sigs.Scale(h_bkg.Integral()/h_sigs.Integral())
        l_sigs = [h_sigs]
    else:
        l_sigs = lSigs
    print(l_sigs)

    for i, sig in enumerate(l_sigs):
        h_sig = sig
        roc,sb = get_graphs(h_sig, h_bkg, float(opts.discr_min), float(opts.discr_max), opts.from_right)
        drawROC(roc, signals[i], opts.bkg.replace(",", "_"), discr, opts.label)
        drawSoverB(sb, signals[i], opts.bkg.replace(",", "_"), discr, opts.label)

print ("=" * 50)
