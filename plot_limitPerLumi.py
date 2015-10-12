from plotutils import *
g=ROOT.TGraph()
e1=ROOT.TGraphAsymmErrors()
e2=ROOT.TGraphAsymmErrors()
xs=[10,20,40,60,80,100,200]
limit=[2.48,1.85,1.34,1.11,0.97,0.88,0.63]
down1=[1.73,1.30,0.95,0.78,0.68,0.62,0.32]
down2=[1.28,0.96,0.7,0.58,0.5,0.45,0.44]
up1=[3.59,2.67,1.93,1.61,1.41,1.27,0.91]
up2=[5.08,3.75,2.71,2.24,1.96,1.78,1.28]

for i,x,y,u1,u2,d1,d2 in zip(range(len(xs)),xs,limit,up1,up2,down1,down2)[:-1]:
    g.SetPoint(i,x,y)
    e1.SetPoint(i,x,y)
    e2.SetPoint(i,x,y)
    e1.SetPointError(i,0,0,y-d1,u1-y)
    print d1,u1
    e2.SetPointError(i,0,0,y-d2,u2-y)
c=getCanvas('limit')
g.Draw('ALP')
setupHisto(g,ROOT.kBlack)
g.GetYaxis().SetTitle('95% CL #sigma/#sigma_{SM}')
g.GetXaxis().SetTitle('Integrated luminosity [fb^{-1}]')
g.GetYaxis().SetRangeUser(0,5.5)
g.GetXaxis().SetRangeUser(0,105)

e1.SetFillColor(ROOT.kGreen)
e2.SetFillColor(ROOT.kYellow)
e2.Draw('E3same')
e1.Draw('E3same')
g.Draw('LPsame')
legend=ROOT.TLegend()
legend.SetX1NDC(0.65)
legend.SetX2NDC(1.0)
legend.SetY1NDC(0.72)
legend.SetY2NDC(0.96)
legend.SetBorderSize(0);
legend.SetLineStyle(0);
legend.SetTextFont(42);
legend.SetTextSize(0.06);
legend.SetFillStyle(0);
legend.AddEntry(g,'Expected','L')
legend.AddEntry(e1,'#pm 1 #sigma','F')
legend.AddEntry(e2,'#pm 2 #sigma','F')
legend.Draw()
cms = ROOT.TLatex(0.2, 0.92, 'CMS private work'  );
cms.SetTextFont(42)
cms.SetNDC()
cms.Draw()
l=ROOT.TLine(0,1,105,1)
l.Draw()

printCanvases([c],'limit')

