import ROOT
import glob
import optparse
import os

ROOT.gROOT.SetBatch(True)
#ROOT.gStyle.SetOptTitle(0)




"""
USE: python corrMat.py --path=DIR --fit=TYPE OF FIT
"""
usage="usage=%prog [options] \n"
usage+="USE: python corrMat.py --path=ROOTFILE --fit=TYPE OF FIT"
usage+="OR: USE: python corrMat.py -p ROOTFILE -f=TYPE OF FIT"

parser = optparse.OptionParser(usage=usage)

parser.add_option("-p", "--path", dest="path",default="workdir/*/datacards/",
        help="root file with fitresults, wildcard possible", metavar="path")

parser.add_option("-f", "--fit", dest="fit",default="fit_s",
        help="TYPE of the used fit (fit_s, fit_b, fit_mdf)", metavar="fit")

parser.add_option("-o","--outPath", dest="outPath",
        help="saves copy of Correlation Matrix to given path", metavar="outPath")

(options, args) = parser.parse_args()


#path_to_file = '/nfs/dust/cms/user/jschindl/combine/Masterarbeit/*/*/powheg_vs_OL*/sig*/PseudoExperiment1/fitDiagnostics.root'
print options.path
list_of = glob.glob(options.path+"*.root")
list_of_paths = []
for path in list_of:
    print path
    if options.fit=="fit_mdf":
        print "fit_mdf"
        if "multidimfit" in path:
            list_of_paths.append(path)
            print path.split("/")
for diagnostics_file in list_of_paths:
    print diagnostics_file
    ROOT_file = ROOT.TFile(diagnostics_file)

    name=""
    for n in diagnostics_file.split("/"):
        if "workdir" not in n and "datacards" not in n:
            if ".root" in n:
                n=n.split(".")[0]
            name+=n+"_"
    name+="corMat"

    fit_s = ROOT_file.Get(options.fit)
    params = fit_s.floatParsFinal().contentsString().split(",")
    params = [a for a in params if 'prop_bin' not in a]
    sigparams = fit_s.floatParsFinal().contentsString().split(",")
    sigparams = [a for a in params if ('prop_bin' not in a and a.startswith("r_"))]

    corr_mat = ROOT.TH2F("Corr_mat","",len(params),0,len(params),len(params),0,len(params))
    corr_mat.SetStats(0)
    corr_mat.GetXaxis().SetLabelSize(0.02)
    corr_mat.GetYaxis().SetLabelSize(0.02)

    corrMat = ROOT.TH2F("CorrMat","",len(sigparams),0,len(sigparams),len(sigparams),0,len(sigparams))
    corrMat.SetStats(0)
    corrMat.GetXaxis().SetLabelSize(0.02)
    corrMat.GetYaxis().SetLabelSize(0.02)


    for i,p1 in enumerate(params):

        corr_mat.GetXaxis().SetBinLabel(i+1,p1)
        corr_mat.GetXaxis().LabelsOption("v")
        for j,p2 in enumerate(params):
            corr_mat.GetYaxis().SetBinLabel(j+1,p2)
            corr_mat.SetBinContent(i+1,j+1,fit_s.correlation(p1, p2))

    for i,p1 in enumerate(sigparams):

        corrMat.GetXaxis().SetBinLabel(i+1,p1)
        corrMat.GetXaxis().LabelsOption("v")
        for j,p2 in enumerate(sigparams):
            corrMat.GetYaxis().SetBinLabel(j+1,p2)
            corrMat.SetBinContent(i+1,j+1,fit_s.correlation(p1, p2))

    canvas = ROOT.TCanvas(diagnostics_file, name, 2524, 2524)

    canvas.SetRightMargin(.15)
    canvas.SetLeftMargin(0.28)
    canvas.SetBottomMargin(0.28)


    ROOT.gStyle.SetPaintTextFormat(".3f")
    corr_mat.SetMarkerColor(ROOT.kWhite)
    corr_mat.GetZaxis().SetRangeUser(-1,1)
    corr_mat.SetTitle(name)
    if len(params)<10:
        corr_mat.Draw("colz text1")
    else:
        corr_mat.Draw("colz")
    canvas.SaveAs(os.path.dirname(diagnostics_file)+"/"+name+".png")
    if options.outPath:
        canvas.SaveAs(options.outPath+"/"+name+".png")
    
    can = ROOT.TCanvas("can_"+diagnostics_file, name+"sig", 2524, 2524)

    can.SetRightMargin(.15)
    can.SetLeftMargin(0.28)
    can.SetBottomMargin(0.28)

    corrMat.SetMarkerColor(ROOT.kWhite)
    corrMat.GetZaxis().SetRangeUser(-1,1)
    corrMat.SetTitle(name+"sig")
    if len(sigparams)<10:
        corrMat.Draw("colz text1")
    else:
        corrMat.Draw("colz")
    can.SaveAs(os.path.dirname(diagnostics_file)+"/"+name+"_Sig.png")
    can.SaveAs(os.path.dirname(diagnostics_file)+"/"+name+"_Sig.pdf")
    if options.outPath:
        can.SaveAs(options.outPath+"/"+name+"_Sig.png")
        can.SaveAs(options.outPath+"/"+name+"_Sig.pdf")
