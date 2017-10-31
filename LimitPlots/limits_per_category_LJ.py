import numpy as np
import json
import sys
from ROOT import TH2F, TCanvas, gStyle, TLatex, TAxis, TLine, TGraphErrors, TGraphAsymmErrors, TLegend, kGreen, kYellow, gPad, gROOT
gROOT.SetBatch(True)

lumi = "35.9" # in 1/fb
fontsize = 0.04

injsonfilenameLJ=sys.argv[1]
injsonfileLJ=open(injsonfilenameLJ,"r")
linesLJ=[]
for line in injsonfileLJ:
  linesLJ.append(line)
jsonLJ=json.loads(linesLJ[0])

def limits_ljets():
    
    nchannels = int(jsonLJ["nchannels"])
    cat_namesBuffer=jsonLJ["cat_names"]
    obsbuffer=jsonLJ["obs"]
    expectbuffer=jsonLJ["expected"]
    u1buffer=jsonLJ["upper1sig"]
    u2buffer=jsonLJ["upper2sig"]
    d1buffer=jsonLJ["lower1sig"]
    d2buffer=jsonLJ["lower2sig"]
    obs=np.array(obsbuffer)
    expect=np.array(expectbuffer)
    cat_names=np.array(cat_namesBuffer)
    upper1sig=np.array(u1buffer)
    upper2sig=np.array(u2buffer)
    lower1sig=np.array(d1buffer)
    lower2sig=np.array(d2buffer)
    

    xmin = 0.9
    xmax = 300

    c,h = draw_canvas_histo( nchannels, xmin, xmax, "95% CL limit on #mu = #sigma/#sigma_{SM} at m_{H} = 125 GeV", cat_names )
    c.SetLogx()
    
    go,ge1,ge2,l = draw_limits_per_category( nchannels, xmin, xmax, obs, expect, upper1sig, lower1sig, upper2sig, lower2sig )

    #draw_disclaimer()

    c.RedrawAxis()    
    c.Modified()
    c.Update()
    c.SaveAs( "lj/bdt_limits_per_category_ljets.pdf" )



def limits_dil():

    nchannels = 6
    
    cat_names    = np.array( ['3 jets, 2 b-tags', '3 jets, 3 b-tags', '#geq 4 jets, 2 b-tags', '#geq 4 jets, 3 b-tags', '#geq 4 jets, #geq 4 b-tags', 'dilepton combined'] )
    obs    = np.array( [185.9888, 104.9094, 32.4241, 7.3565, 9.1324, 5.2371] )
    expect    = np.array( [114.8125, 48.625, 40.125, 10.75, 12.2188, 7.6562] )
    upper1sig    = np.array( [52.62950000000001, 26.165899999999993, 16.7937, 5.184799999999999, 7.500400000000001, 3.6317000000000004] )
    lower1sig    = np.array( [34.122600000000006, 15.903500000000001, 11.2698, 3.3143000000000002, 4.2607, 2.3311] )
    upper2sig    = np.array( [122.89089999999999, 64.1284, 37.8989, 12.1876, 19.0792, 8.457299999999998] )
    lower2sig    = np.array( [54.9396, 24.9773, 18.26, 5.27, 6.6106, 3.7533000000000003] )
    
    xmin = 0.9
    xmax = 200

    c,h = draw_canvas_histo( nchannels, xmin, xmax, "95% CL limit on #mu = #sigma/#sigma_{SM} at m_{H} = 125 GeV", cat_names )
    c.SetLogx()
    
    go,ge1,ge2,l = draw_limits_per_category( nchannels, xmin, xmax, obs, expect, upper1sig, lower1sig, upper2sig, lower2sig )

    #draw_disclaimer()
    c.RedrawAxis()    
    c.Modified()
    c.Update()
    #h.Draw("SAMEAXIS")
    #c.Update()
    c.SaveAs( "dil/limits_per_category_dil.pdf" )
    

def draw_limits_per_category( nchannels, xmin, xmax, obs, expect, upper1sig, lower1sig, upper2sig, lower2sig ):

    channel = np.array( [ nchannels - 1.5 - float(i) for i in range( 0, nchannels ) ] )
    ey      = np.array( [0.494]*nchannels )
    zero    = np.zeros( nchannels )

    gexpect1sig = TGraphAsymmErrors( nchannels, expect, channel, lower1sig, upper1sig, ey, ey )
    gexpect1sig.SetFillColor( kGreen )
    gexpect1sig.SetLineWidth( 2 )
    gexpect1sig.SetLineStyle( 2 )
    
    gexpect2sig = TGraphAsymmErrors( nchannels, expect, channel, lower2sig, upper2sig, ey, ey )
    gexpect2sig.SetFillColor( kYellow )
    gexpect2sig.SetLineWidth( 2 )
    gexpect2sig.SetLineStyle( 2 )

    gexpect2sig.Draw("2")
    gexpect1sig.Draw("2")

    gobs = TGraphErrors( nchannels, obs, channel, zero, ey )
    gobs.SetMarkerStyle( 21 )
    gobs.SetMarkerSize( 1.5 )
    gobs.SetLineWidth( 2 )
    #gobs.Draw("pz")

    # dashed line at median expected limits
    l = TLine()
    l.SetLineStyle( 2 )
    l.SetLineWidth( 2 )
    for bin in range( nchannels ):
        l.DrawLine( expect[bin], channel[bin]-ey[bin], expect[bin], channel[bin]+ey[bin] )

    # line to separate individual and combined limits
    l.SetLineStyle( 1 )
    l.SetLineWidth( 1 )
    l.DrawLine( xmin, 0, xmax, 0 )

    # legend
    leg = TLegend(0.75, 0.75, 0.95, 0.9 )
    leg.SetFillColor( 4000 )
    leg.AddEntry( gexpect1sig, "Expected #pm1#sigma", "FL" )
    leg.AddEntry( gexpect2sig, "Expected #pm2#sigma", "FL" )
    #leg.AddEntry( gobs,        "Observed", "pl" )
    leg.Draw()

    return gobs, gexpect1sig, gexpect2sig, leg


def draw_canvas_histo( nchannels, xmin, xmax, title, cat_names ):
    c = TCanvas( "c", "Canvas", 800, 600 )
    c.Draw()
    
    h = TH2F( "h", "", 10, xmin, xmax, nchannels, -1, nchannels-1 )
    h.Draw()
    h.SetStats( 0 )
    h.SetXTitle( title )

    yaxis = h.GetYaxis()
    yaxis.SetLabelSize( fontsize )

    for ibin in range( 0, nchannels ):
        yaxis.SetBinLabel( nchannels-ibin, cat_names[ibin] )


    t = TLatex();
    t.SetNDC()
    t.SetTextFont( 42 )
    t.SetTextSize( fontsize )
    t.SetTextAlign( 11 )
    t.DrawLatex( 0.40, 0.91, "CMS preliminary, " + lumi + " fb^{-1}, #sqrt{s} = 13 TeV" )

    return c,h

def draw_disclaimer():
    # disclaimer
    t = TLatex();
    t.SetNDC()
    t.SetTextSize( 0.1 )
    t.SetTextAlign( 22 )
    t.SetTextAngle( 45 )
    t.DrawText( 0.5, 0.5, "FAKE VALUES" )
    
def my_style():
    
    gStyle.SetLabelSize( fontsize, "x" );
    gStyle.SetLabelSize( fontsize, "y" );
    gStyle.SetLabelSize( fontsize, "z" );

    gStyle.SetTitleFontSize( 1.5*fontsize );
    gStyle.SetTitleSize( fontsize, "x" );
    gStyle.SetTitleSize( fontsize, "y" );
    gStyle.SetTitleSize( fontsize, "z" );


    gStyle.SetTitleOffset( 1.5, "xy" );
    gStyle.SetTitleFont( 62, "bla" );

    gStyle.SetPadBottomMargin(0.15);
    gStyle.SetPadTopMargin(0.10);
    gStyle.SetPadLeftMargin(0.30);
    gStyle.SetPadRightMargin(0.05);

    gStyle.SetStatX( 0.88 );
    gStyle.SetStatY( 0.87 );
    gStyle.SetNdivisions( 505 );

    gStyle.SetCanvasColor(-1); 
    gStyle.SetPadColor(-1); 
    gStyle.SetFrameFillColor(-1); 
    gStyle.SetTitleFillColor(-1); 
    gStyle.SetFillColor(-1); 
    gStyle.SetFillStyle(4000); 
    gStyle.SetStatStyle(0); 
    gStyle.SetTitleStyle(0); 
    gStyle.SetCanvasBorderSize(0); 
    gStyle.SetFrameBorderSize(0); 
    gStyle.SetLegendBorderSize(0); 
    gStyle.SetStatBorderSize(0); 
    gStyle.SetTitleBorderSize(0); 
    
if __name__ == '__main__':
    my_style()
    limits_ljets()
    #limits_dil()

