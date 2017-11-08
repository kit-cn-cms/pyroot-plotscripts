import numpy as np
from ROOT import TH2F, TCanvas, gStyle, TLatex, TAxis, TLine, TGraphErrors, TGraphAsymmErrors, TLegend, kGreen, kYellow

nchannels = 3
lumi = "12.9" # in 1/fb
fontsize = 0.04

def limits():

    # put real limits here: lepton+jets, dilepton, combined
    obs    = np.array( [  0.0,0.0, 0.0 ] )
    
    expect = np.array( [  1,1, 1 ] )
    upper1sig = np.array( [ 1.179, 0.827, 0.736] )
    lower1sig = np.array( [ 0.824, 0.578, 0.501 ] )
    upper2sig = np.array( [ 2.661, 1.892, 1.662 ] )
    lower2sig = np.array( [ 1.344, 0.9303, 0.806 ] )
    
    channel = np.array( [ 1.5, 0.5, -0.5 ] )
    ey      = np.array( [ 0.495, 0.495, 0.495 ] )
    zero    = np.zeros( nchannels )

    xmin = 0.9
    xmax = 20

    c,h = draw_canvas_histo( xmin, xmax, "95% CL limit on #mu = #sigma/#sigma_{SM} at m_{H} = 125 GeV" )
    c.SetLogx()

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
    leg = TLegend( 0.67, 0.75, 0.95, 0.9 )
    leg.SetFillColor( 4000 )
    leg.AddEntry( gexpect1sig, "Expected #pm1#sigma", "FL" )
    leg.AddEntry( gexpect2sig, "Expected #pm2#sigma", "FL" )
    #leg.AddEntry( gobs,        "Observed", "pl" )
    leg.Draw()

    #draw_disclaimer()

    c.RedrawAxis()    
    c.Modified()
    c.Update()
    c.SaveAs( "limits.pdf" )


def bestfit():
    
    xmin = -10
    xmax = 6

    c,h = draw_canvas_histo( xmin, xmax, "Best fit #mu = #sigma/#sigma_{SM} at m_{H} = 125 GeV" )

    # line at SM expectation of mu = 1
    l = TLine()
    l.SetLineStyle( 2 )
    l.DrawLine( 1.0, -1.0, 1.0, -1.0+nchannels )
    
    mu    = np.array( [ -0.4, -4.734, -2.014 ] )
    upper = np.array( [ 2.12, 3.688, 1.80 ] )
    lower = np.array( [ 2.08, 3.754, 1.8224 ] )

    channel = np.array( [ 1.5, 0.5, -0.5 ] )
    zero    = np.zeros( nchannels )

    gmu = TGraphAsymmErrors( nchannels, mu, channel, lower, upper, zero, zero )
    gmu.SetMarkerStyle( 21 )
    gmu.SetMarkerSize( 1.5 )
    gmu.SetLineColor( 2 )
    gmu.SetLineWidth( 2 )
    gmu.Draw( "pz" )


    
    #draw_disclaimer()

    c.RedrawAxis()    
    c.Modified()
    c.Update()
    c.SaveAs( "bestfit.pdf" )

def draw_canvas_histo( xmin, xmax, title ):
    c = TCanvas( "c", "Canvas", 600, 600 )
    c.Draw()
    
    h = TH2F( "h", "", 10, xmin, xmax, nchannels, -1, nchannels-1+0.001 )
    h.Draw()
    h.SetStats( 0 )
    h.SetXTitle( title )

    yaxis = h.GetYaxis()
    yaxis.SetLabelSize( 1.5*fontsize )
    yaxis.SetBinLabel( 3, "SL(BDT)" )
    yaxis.SetBinLabel( 2, "SL(MEM)" )
    yaxis.SetBinLabel( 1, "SL(2D)" )

    t = TLatex();
    t.SetNDC()
    t.SetTextFont( 42 )
    t.SetTextSize( fontsize )
    t.SetTextAlign( 11 )
    t.DrawLatex( 0.22, 0.91, "CMS preliminary, " + lumi + " fb^{-1}, #sqrt{s} = 13 TeV" )

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
    gStyle.SetPadLeftMargin(0.22);
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
    limits()
    #bestfit()
