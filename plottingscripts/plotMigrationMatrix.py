import ROOT
ROOT.gStyle.SetPalette(ROOT.kCool)
ROOT.gStyle.SetPaintTextFormat(".0f")
ROOT.gROOT.SetBatch(True)

import sys
f = ROOT.TFile(sys.argv[1]+"/output_limitInput.root")


def printCMSLabel(pad, privateWork = True):
    pad.cd(1)
    l = pad.GetLeftMargin()
    t = pad.GetTopMargin()
    r = pad.GetRightMargin()
    b = pad.GetBottomMargin()

    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextColor(ROOT.kBlack)
    latex.SetTextSize(0.04)

    text = "CMS"
    if privateWork: text += " #bf{#it{private work}}"

    latex.DrawLatex(l+0.01,1.-t+0.01, text)

def printLumiLabel(pad, lumi):
    pad.cd(1)
    l = pad.GetLeftMargin()
    t = pad.GetTopMargin()
    r = pad.GetRightMargin()
    b = pad.GetBottomMargin()

    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextColor(ROOT.kBlack)
    latex.SetTextSize(0.04)
    text = "#bf{"+str(lumi)+" fb^{-1} (13 TeV)}"
    latex.DrawLatex(1.-r-0.24,1.-t+0.01, text)



matrixName = "ttbb__migrationMatrix_dRbb"
m = f.Get(matrixName)
print(m)
m.GetXaxis().SetTitle("reco. level #DeltaR(bb)")
m.GetYaxis().SetTitle("gen. level #DeltaR(bb)")
m.SetTitle("")
m.SetLineWidth(2)
m.SetLineStyle(1)
m.SetStats(False)
name = "migrationMatrix"
canvas = ROOT.TCanvas(name, name, 1024, 1024)
canvas.SetBottomMargin(0.1)
canvas.SetLeftMargin(0.1)
canvas.SetTopMargin(0.12)
canvas.SetRightMargin(0.12)
m.Draw("colz text1")
m.Draw("axis same")
canvas.SetTicks(1,1)
canvas.RedrawAxis()
printCMSLabel(canvas)
printLumiLabel(canvas, "59.7")
canvas.SaveAs(sys.argv[1]+"/migrationMatrix.pdf")
