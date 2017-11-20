import numpy as np
from ROOT import TH2F, TCanvas, gStyle, TLatex, TAxis, TLine, TGraphErrors, TGraphAsymmErrors, TLegend, kGreen, kYellow

nchannels = 3
fontsize = 0.04

#def limits():

    ## put real limits here: lepton+jets, dilepton, combined
    #obs       = np.array( [3.1800042632, 1.83107995924, 1.51963270303] )

    #upper2sig = np.array( [3.67880916595, 2.29233074188, 1.70253658295]   )
    #upper1sig = np.array( [1.53992033005, 0.970508098602, 0.736265659332] )
    #expect    = np.array( [3.359375, 2.1171875, 1.6640625]                )
    #lower1sig = np.array( [1.0274810791, 0.629234552383, 0.480370521545]  )
    #lower2sig = np.array( [1.63375854492, 1.0131072998, 0.783279418945]   )

    #sig_inj   = np.array( [ 4.5, 2.9, 2.4] ) 

    #channels = np.array( [ 7.5, 4.5, 1.5 ] )
    #ey      = np.array( [ 0.7, 0.7, 0.7 ] )
    #zero    = np.zeros( nchannels )

    #xmin = 0.7
    #xmax = 35

    #c,h = draw_canvas_histo( xmin, xmax, "95% CL limit on #mu = #sigma/#sigma_{SM} at m_{H} = 125 GeV" )
    #c.SetLogx()

    #gexpect1sig = TGraphAsymmErrors( nchannels, expect, channels, lower1sig, upper1sig, ey, ey )
    #gexpect1sig.SetFillColor( kGreen )
    #gexpect1sig.SetLineWidth( 2 )
    #gexpect1sig.SetLineStyle( 2 )
    
    #gexpect2sig = TGraphAsymmErrors( nchannels, expect, channels, lower2sig, upper2sig, ey, ey )
    #gexpect2sig.SetFillColor( kYellow )
    #gexpect2sig.SetLineWidth( 2 )
    #gexpect2sig.SetLineStyle( 2 )

    #gexpect2sig.Draw("2")
    #gexpect1sig.Draw("2")

    #gobs = TGraphErrors( nchannels, obs, channels, zero, ey )
    #gobs.SetMarkerStyle( 21 )
    #gobs.SetMarkerSize( 1.5 )
    #gobs.SetLineWidth( 2 )
    #gobs.Draw("pz")

    #gsinj = TGraphErrors( nchannels, sig_inj, channels, zero, ey )
    #gsinj.SetLineWidth( 2 )
    #gsinj.SetLineColor( 2 )
    #gsinj.SetLineStyle( 2 )
    #gsinj.Draw("z")

    ## dashed line at median expected limits
    #l = TLine()
    #l.SetLineStyle( 2 )
    #l.SetLineWidth( 2 )
    #for bin in range( nchannels ):
        #l.DrawLine( expect[bin], channels[bin]-ey[bin], expect[bin], channels[bin]+ey[bin] )

    ## legend
    #x2 = 1-gStyle.GetPadRightMargin()
    #y1 = gStyle.GetPadBottomMargin()+gStyle.GetTickLength()+0.02
    #y2 = 1-gStyle.GetPadTopMargin()
    ##leg = TLegend( x2-0.3, y2-0.21, x2, y2 )
    #leg = TLegend( x2-0.34, y1, x2-0.002, y1+0.18 )
    #leg.SetFillColor( 10 )
    #leg.SetFillStyle(1000)
    #leg.AddEntry( gexpect1sig, "Expected #pm1#sigma", "FL" )
    #leg.AddEntry( gexpect2sig, "Expected #pm2#sigma", "FL" )
    #leg.AddEntry( gsinj,       "t#bar{t}H(#mu=1) injected", "L" )
    #leg.AddEntry( gobs,        "Observed", "pl" )
    #leg.Draw()

    ##draw_disclaimer()

    #c.RedrawAxis()    
    #c.Modified()
    #c.Update()
    #c.SaveAs( "HIG-16-038_limits.pdf" )


def bestfit():
    
    xmin = -0.5
    xmax = 6

    c,h = draw_canvas_histo( xmin, xmax, "Best fit #mu = #sigma/#sigma_{SM} at m_{H} = 125 GeV" )

    # line at SM expectation of mu = 1
    l = TLine()
    l.SetLineStyle( 2 )
    l.DrawLine( 1.0, 0, 1.0, 3*nchannels+0.5 )


    # DL, SL, comb
    mu    = np.array( [ 1.0, 1.0, 1.0 ] )
    upper = np.array( [ 1.06, 0.61, 0.53 ] )
    lower = np.array( [ 0.97, 0.57, 0.5 ] )
    upper_stat = np.array( [ 0.63, 0.27, 0.25 ] )
    lower_stat = np.array( [ 0.61, 0.27, 0.25 ] )
    upper_syst = np.array( [ 0.85, 0.54, 0.46 ] )
    lower_syst = np.array( [ 0.76, 0.51, 0.43 ] )
    channels = np.array( [ 7.5, 4.5, 1.5 ] )
    zero    = np.zeros( nchannels )

    gmu_tot = TGraphAsymmErrors( nchannels, mu, channels, lower, upper, zero, zero )
    gmu_tot.SetMarkerStyle( 1 )
    gmu_tot.SetMarkerSize( 1 )
    gmu_tot.SetMarkerColor( 4 )
    gmu_tot.SetLineColor( 4 )
    gmu_tot.SetLineWidth( 2 )
    gmu_tot.Draw( "p" )

    gmu = TGraphAsymmErrors( nchannels, mu, channels, lower_stat, upper_stat, zero, zero )
    gmu.SetMarkerStyle( 21 )
    gmu.SetMarkerSize( 1.5 )
    gmu.SetMarkerColor( 1 )
    gmu.SetLineColor( 2 )
    gmu.SetLineWidth( 2 )
    gmu.Draw( "pe1same" )


    leg = TLatex();
    leg.SetTextFont( 42 )
    leg.SetTextSize( 0.035 )
    leg.SetTextAlign( 11 )
    leg.DrawLatex( 2.6, 3*nchannels, "#mu       #color[4]{tot.}    #color[2]{stat.}    syst." )

    for ich,channel in enumerate(channels):
        res = TLatex();
        res.SetTextFont( 42 )
        res.SetTextSize( 0.045 )
        res.SetTextAlign( 11 )
        res.DrawLatex( 2.4, channel-0.2,
                       ("%.2f #color[4]{{}^{+%.2f}_{ -%.2f}} #color[2]{{}^{+%.2f}_{ -%.2f}} {}^{+%.2f}_{ -%.2f}"
                        %
                        (mu[ich],upper[ich],lower[ich],
                         upper_stat[ich],lower_stat[ich],
                         upper_syst[ich],lower_syst[ich])) )

  
    
    #draw_disclaimer()

    c.RedrawAxis()    
    c.Modified()
    c.Update()
    c.SaveAs( "HIG-17-026_bestfit.pdf" )
    c.SaveAs( "HIG-17-026_bestfit.png" ) 

def draw_canvas_histo( xmin, xmax, title ):
    c = TCanvas( "c", "Canvas", 600, 600 )
    c.Draw()
    
    h = TH2F( "h", "", 10, xmin, xmax, 3*nchannels+2, 0, 3*nchannels+2 )
    h.Draw()
    h.SetStats( 0 )
    h.SetXTitle( title )

    yaxis = h.GetYaxis()
    yaxis.SetLabelSize( 1.5*fontsize )
    yaxis.SetBinLabel( 8, "Dilepton" )
    yaxis.SetBinLabel( 5, "Lepton+jets" )
    yaxis.SetBinLabel( 2, "Combined" )

    # separating combined result
    l = TLine()
    l.SetLineStyle( 1 )
    l.DrawLine( xmin, 3, xmax, 3 )

    pub = TLatex();
    pub.SetNDC()
    pub.SetTextFont( 42 )
    pub.SetTextSize( 0.045 )
    pub.SetTextAlign( 11 )
    #pub.DrawLatex( gStyle.GetPadLeftMargin()+0.02, 0.84, "#scale[1.2]{#bf{CMS}} #it{Preliminary}" )
    pub.DrawLatex( gStyle.GetPadLeftMargin()+0.02, 0.84, "#scale[1.2]{#bf{CMS}}" )

    lumi = TLatex();
    lumi.SetNDC()
    lumi.SetTextFont( 42 )
    lumi.SetTextSize( 0.035 )
    lumi.SetTextAlign( 31 )
    lumi.DrawLatex( 1-gStyle.GetPadRightMargin(), 0.92, "35.9 fb^{-1} (13 TeV)" )


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
    gStyle.SetTickLength(0,"Y");
    gStyle.SetEndErrorSize(6)

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
    #limits()
    bestfit()
