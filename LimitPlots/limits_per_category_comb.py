import numpy as np
from ROOT import TH2F, TCanvas, gStyle, TLatex, TAxis, TLine, TGraphErrors, TGraphAsymmErrors, TLegend, kGreen, kYellow, gPad, gROOT
gROOT.SetBatch(True)

lumi = "11.4-12.9" # in 1/fb
fontsize = 0.04

def limits_ljets():

    nchannels = 13
    
    #['ttH_hbb_13TeV_dl_3j3t', 'ttH_hbb_13TeV_dl_ge4j3t_low', 'ttH_hbb_13TeV_dl_ge4j3t_high', 'ttH_hbb_13TeV_dl_ge4jge4t_low', 'ttH_hbb_13TeV_dl_ge4jge4t_high', 'inputs2DV12_datacard_ljets_jge6_t3_low_hdecay', 'inputs2DV12_datacard_ljets_jge6_t3_high_hdecay', 'inputs2DV12_datacard_ljets_j4_t4_low_hdecay', 'inputs2DV12_datacard_ljets_j4_t4_high_hdecay', 'inputs2DV12_datacard_ljets_j5_tge4_low_hdecay', 'inputs2DV12_datacard_ljets_j5_tge4_high_hdecay', 'inputs2DV12_datacard_ljets_jge6_tge4_low_hdecay', 'inputs2DV12_datacard_ljets_jge6_tge4_high_hdecay', 'all']

    myn= ['DL 3 jets, 3 b-tags','DL #geq 4 jets, 3 b-tags low BDT','DL #geq 4 jets, 3 b-tags high BDT','DL #geq 4 jets, #geq 4 b-tags low BDT','DL #geq 4 jets, #geq 4 b-tags high BDT','L+J #geq 6 jets, 3 b-tags low BDT','L+J #geq 6 jets, 3 b-tags high BDT','L+J 4 jets, #geq 4 b-tags low BDT','L+J 4 jets, #geq 4 b-tags high BDT', 'L+J 5 jets, #geq 4 b-tags low BDT','L+J 5 jets, #geq 4 b-tags high BDT', 'L+J #geq 6 jets, #geq 4 b-tags low BDT','L+J #geq 6 jets, #geq 4 b-tags high BDT', 'all combined']
    

    nchannels=len(myn)



    #cat_names    = np.array( ['4 jets, 2 b-tags','5 jets, 2 b-tags', '#geq 6 jets, 2 b-tags', '4 jets, 3 b-tags','4 jets, 3 b-tags', '4 jets, #geq 4 b-tags', '4 jets, #geq 4 b-tags', '5 jets, 3 b-tags','5 jets, 3 b-tags', '5 jets, #geq 4 b-tags', '5 jets, #geq 4 b-tags', '#geq 6 jets, 3 b-tags', '#geq 6 jets, 3 b-tags', '#geq 6 jets, #geq 4 b-tags', '#geq 6 jets, #geq 4 b-tags', 'lepton+jets combined'] )
    #['sl2DBDTMEMsplitTTH_datacard_ljets_j4_t2_hdecay', 'sl2DBDTMEMsplitTTH_datacard_ljets_j5_t2_hdecay', 'sl2DBDTMEMsplitTTH_datacard_ljets_jge6_t2_hdecay', 'sl2DBDTMEMsplitTTH_datacard_ljets_j4_t3_low_hdecay', 'sl2DBDTMEMsplitTTH_datacard_ljets_j4_t3_high_hdecay', 'sl2DBDTMEMsplitTTH_datacard_ljets_j5_t3_low_hdecay', 'sl2DBDTMEMsplitTTH_datacard_ljets_j5_t3_high_hdecay', 'sl2DBDTMEMsplitTTH_datacard_ljets_jge6_t3_low_hdecay', 'sl2DBDTMEMsplitTTH_datacard_ljets_jge6_t3_high_hdecay', 'sl2DBDTMEMsplitTTH_datacard_ljets_j4_t4_low_hdecay', 'sl2DBDTMEMsplitTTH_datacard_ljets_j4_t4_high_hdecay', 'sl2DBDTMEMsplitTTH_datacard_ljets_j5_tge4_low_hdecay', 'sl2DBDTMEMsplitTTH_datacard_ljets_j5_tge4_high_hdecay', 'sl2DBDTMEMsplitTTH_datacard_ljets_jge6_tge4_low_hdecay', 'sl2DBDTMEMsplitTTH_datacard_ljets_jge6_tge4_high_hdecay', 'sl2DBDTMEMsplitTTH_datacard_hdecay']

    
    cat_names    = np.array( ['DL 3 jets, 3 b-tags','DL #geq 4 jets, 3 b-tags low BDT','DL #geq 4 jets, 3 b-tags high BDT','DL #geq 4 jets, #geq 4 b-tags low BDT','DL #geq 4 jets, #geq 4 b-tags high BDT','L+J #geq 6 jets, 3 b-tags low BDT','L+J #geq 6 jets, 3 b-tags high BDT','L+J 4 jets, #geq 4 b-tags low BDT','L+J 4 jets, #geq 4 b-tags high BDT', 'L+J 5 jets, #geq 4 b-tags low BDT','L+J 5 jets, #geq 4 b-tags high BDT', 'L+J #geq 6 jets, #geq 4 b-tags low BDT','L+J #geq 6 jets, #geq 4 b-tags high BDT', 'all combined'] )
    
    
    obs    = np.array( [0.0]*nchannels )
    expect    = np.array( [25.8125, 19.3125, 7.28125, 13.3125, 5.046875, 19.6875, 8.25, 47.625, 13.6875, 16.5625, 6.046875, 9.65625, 4.203125, 1.6953125])
    upper1sig    = np.array( [13.0669975281, 8.54483032227, 3.33768844604, 7.48205184937, 2.83650541306, 8.86770057678, 3.58444881439, 22.2107315063, 6.49251556396, 7.59216690063, 2.91647529602, 4.73429775238, 2.11098337173, 0.763607501984] )
    lower1sig    = np.array([8.08511543274, 5.88987636566, 2.2131729126, 4.38715744019, 1.66320610046, 5.7795381546, 2.4066696167, 14.2698402405, 4.03475952148, 4.92242622375, 1.85689353943, 3.07202148438, 1.28554582596, 0.510189771652])
    upper2sig    = np.array( [31.171169281, 19.7590179443, 7.70355224609, 18.4020824432, 6.97637653351, 20.2426223755, 8.39886856079, 52.6733627319, 15.2869510651, 17.9326248169, 7.00279903412, 11.1093921661, 5.01607227325, 1.78524398804])
    lower2sig    = np.array([12.8558349609, 9.54309082031, 3.54107666016, 6.89025878906, 2.61215209961, 9.30541992188, 3.8994140625, 22.9753417969, 6.49621582031, 7.92541503906, 2.95257568359, 4.88470458984, 2.04409790039, 0.811233520508])


    xmin = 0.9
    xmax = 200

    c,h = draw_canvas_histo( nchannels, xmin, xmax, "95% CL limit on #mu = #sigma/#sigma_{SM} at m_{H} = 125 GeV", cat_names )
    c.SetLogx()
    
    go,ge1,ge2,l = draw_limits_per_category( nchannels, xmin, xmax, obs, expect, upper1sig, lower1sig, upper2sig, lower2sig )

    #draw_disclaimer()

    c.RedrawAxis()    
    c.Modified()
    c.Update()
    c.SaveAs( "lj/2D_limits_per_category_ljets.pdf" )



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
    leg = TLegend( 0.32, 0.73, 0.55, 0.9 )
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
    t.DrawLatex( 0.40, 0.91, "CMS preliminary, " + lumi + " fb^{-1}, #sqrt{s} = 13 TeV"  )

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

