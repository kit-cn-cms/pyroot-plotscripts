import numpy as np
from ROOT import TH2F, TCanvas, gStyle, TLatex, TAxis, TLine, TGraphErrors, TGraphAsymmErrors, TLegend, kGreen, kYellow, gPad

lumi = "2.7" # in 1/fb
fontsize = 0.04

def limits_ljets():

    nchannels = 13

    cat_names    = np.array( ['4 jets, 2 b-tags','5 jets, 2 b-tags','4 jets, 3 b-tags low BDT output','4 jets, 3 b-tags high BDT output', '4 jets, #geq 4 b-tags low BDT output', '4 jets, #geq 4 b-tags high BDT output', '5 jets, 3 b-tags low BDT output','5 jets, 3 b-tags high BDT output', '5 jets, #geq 4 b-tags low BDT output', '5 jets, #geq 4 b-tags high BDT output', '#geq 6 jets, 2 b-tags', '#geq 6 jets, 3 b-tags low BDT output', '#geq 6 jets, 3 b-tags high BDT output', '#geq 6 jets, #geq 4 b-tags low BDT output', '#geq 6 jets, #geq 4 b-tags high BDT output', 'lepton+jets combined'] )
    obs    = np.array( [0.0]*nchannels )
    expect    = np.array( [65.25, 44.312, 120.25, 49.625, 42.125, 11.968, 
			   41.125, 1, 1, 1, 1, 1] )
    upper1sig    = np.array( [8.213000000000001, 13.380600000000001, 41.3064, 5.461499999999999, 5.6485, 16.136000000000003, 21.146500000000003, 3.2993000000000006, 4.423299999999999, 9.5623, 5.853299999999999, 1.8319999999999999] )
    lower1sig    = np.array( [5.4718, 8.126100000000001, 25.768300000000004, 3.5929, 3.3830999999999998, 9.9057, 13.062999999999999, 2.1878, 2.6673, 5.825900000000001, 3.5324, 1.2306] )
    upper2sig    = np.array( [18.9917, 33.2948, 102.0315, 12.6291, 13.983300000000002, 39.6387, 50.331, 7.635400000000001, 10.905800000000001, 23.359099999999998, 14.1773, 4.236400000000001] )
    lower2sig    = np.array( [8.8099, 12.7625, 40.9731, 5.8585, 5.3133, 15.750699999999998, 20.6428, 3.5447999999999995, 4.1891, 9.2635, 5.5478, 1.9813] )


    xmin = 0.9
    xmax = 110

    c,h = draw_canvas_histo( nchannels, xmin, xmax, "95% CL limit on #mu = #sigma/#sigma_{SM} at m_{H} = 125 GeV", cat_names )
    c.SetLogx()
    
    go,ge1,ge2,l = draw_limits_per_category( nchannels, xmin, xmax, obs, expect, upper1sig, lower1sig, upper2sig, lower2sig )

    #draw_disclaimer()

    c.RedrawAxis()    
    c.Modified()
    c.Update()
    c.SaveAs( "lj/limits_per_category_ljets.pdf" )



def limits_dil():

    nchannels = 6
    
    cat_names    = np.array( ['3 jets, 2 b-tags', '3 jets, 3 b-tags', '#geq 4 jets, 2 b-tags', '#geq 4 jets, 3 b-tags', '#geq 4 jets, #geq 4 b-tags', 'dilepton combined'] )
    obs    = np.array( [1, 1, 1,1,1, 1] )
    expect    = np.array( [1, 1, 1, 1, 1, 1] )
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
    ey      = np.full( nchannels, 0.494 )
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
    gobs.Draw("pz")

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
    leg = TLegend( 0.32, 0.73, 0.55, 0.9 )
    leg.SetFillColor( 4000 )
    leg.AddEntry( gexpect1sig, "Expected #pm1#sigma", "FL" )
    leg.AddEntry( gexpect2sig, "Expected #pm2#sigma", "FL" )
    leg.AddEntry( gobs,        "Observed", "pl" )
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
    limits_dil()

