import numpy as np
from array import array
import ROOT
import sys
import json
filedir = os.path.dirname(__file__)
sys.path.append('../pyroot-plotscripts-base')
import CMS_lumi

ROOT.gROOT.SetBatch(True)


injsonfilenameLJ=sys.argv[1]
injsonfileLJ=open(injsonfilenameLJ,"r")
linesLJ=[]
for line in injsonfileLJ:
  linesLJ.append(line)
jsonLJ=json.loads(linesLJ[0])
outname=sys.argv[2]
print jsonLJ
inchan=sys.argv[3]
if inchan=="lj" or inchan=="LJ":
  channel="lj"
if inchan=="dl" or inchan=="DL":
  channel="dil"
  

#nchannels = 3
lumi = "35.9" # in 1/fb
fontsize = 0.06

def categories():
    yields={}
    for cat in jsonLJ:
      processes = [str(p) for p in jsonLJ[cat]["processes"]]
      colors = [int(c) for c in jsonLJ[cat]["colors"]]
      yields[cat]=[float(y) for y in jsonLJ[cat]["yields"]]
    ncats=len(yields)
    pads = [i+1 for i in range(ncats)]

    plot_pies( channel, processes, yields, colors, pads, doLegend=False )
    
    return

def plot_pies( channel, processes, yields, colors, pads, doLegend=False ):
    if doLegend:
      pads+=[len(pads)+1]
      print "legend pad ", pads
    nrows = len(pads)/4
    if len(pads)%4!=0:
      nrows+=1
    print nrows
    canvas = ROOT.TCanvas( "c", "Canvas", 1200, 300*nrows+80 )
    #canvas.Divide( 4, nrows ) #easier divide function
    totalHeight=300*nrows+80
    topFraction=80/float(300*nrows+80)
    remFraction=1.0-topFraction
    print totalHeight, topFraction, remFraction
    padlist=[]
    for irow in range(nrows):
      for ip in range(4):
	print irow, ip
	xlow=1.0/float(4)+1.0/float(4)*ip-1.0/float(4)
	xhigh=1.0/float(4)+1.0/float(4)*(ip+1)-1.0/float(4)
	yhigh=1.0 - (remFraction/float(nrows)+remFraction/float(nrows)*irow + topFraction -remFraction/float(nrows))
	ylow=1.0 - (remFraction/float(nrows)+remFraction/float(nrows)*(irow+1) + topFraction -remFraction/float(nrows))
	print xlow, xhigh, ylow, yhigh
	thispad=ROOT.TPad("p_"+str(irow)+"_"+str(ip),"p_"+str(irow)+"_"+str(ip),xlow,ylow,xhigh,yhigh)
	padlist.append(thispad)
    print "pl, ", len(padlist)
    print "p, ", len(pads)
    canvas.Draw()
    
    channel_text = ROOT.TLatex()
    channel_text.SetTextSize(0.06)
    channel_text.DrawLatex(0.4,0.9,"Dilepton Channel" if channel=="dil" else "Lepton+Jets Channel")
    
    pies = {}
    print processes
    names = [ array( 'c', name + '\0' ) for name in processes ]
    labels = array( 'l', map( lambda x: x.buffer_info()[0], names ) )
    ipad = 0
    
    legend=None
    for cat in sorted(yields):
        print ""
        print ipad
        print cat
        print pads[ipad]
        #canvas.cd( pads[ipad] )#easier divide function
        print padlist
        padlist[pads[ipad]-1].cd()
        pname = 'pie%d' % ipad
        pies[cat] = ROOT.TPie( pname, cat, len(colors), np.asarray(yields[cat],dtype=np.float64), np.asarray(colors,dtype=np.int32) )
        pies[cat].SetLabels( labels )
        pies[cat].SetRadius( 0.33 )
        pies[cat].SetTextFont( 42 )
        #pies[cat].SetLabelFormat("#splitline{%val (%perc)}{%txt}")
        pies[cat].Draw( "nol " )
        #if doLegend and ipad==0:
	  #legend=pies[cat].MakeLegend(0,0,1,1)
        
        sigID=0
        for icy, cy in enumerate(processes):
          if cy=="ttH":
            sigID=icy
        # print S/B, S/sqrt(B)
        S = yields[cat][sigID]
        B = 0
        for i in range( len(processes) ):
          if i==sigID:
            print "skipping this ", processes[i], yields[cat][i]
            continue
          else:
            B += yields[cat][i]
            print "added", yields[cat][i]
        #print S, B, S/B, S/np.sqrt(B)
        print S, B, S/float(B), S/np.sqrt(B)

        t = ROOT.TLatex()
        t.SetTextFont( 42 )
        print "size ", t.SetTextSize(0.067)
        
        t.SetTextAlign( 22 )
        t.DrawLatex( 0.5, 0.07, "S/B=%5.3f, S/#sqrt{B}=%5.3f" % ( S/B, S/np.sqrt(B) ) )
        canvas.cd()#complicated divide function
        padlist[pads[ipad]-1].Draw()#complicated divide function
        
        ipad += 1
     
    if doLegend:
      emptyhists=[]
      legend=ROOT.TLegend(0.3,0.1,0.9,0.9)
      for p,c in zip(processes,colors):
	emptyhists.append(ROOT.TH1D(p,p,10,0,1))
	emptyhists[-1].SetLineColor(c)
	emptyhists[-1].SetFillColor(c)
	emptyhists[-1].SetMarkerColor(c)
	legend.AddEntry(emptyhists[-1],p,"f")
      print pads[-1]
      #print padlist[6]
      print padlist[pads[-1] - 1]
      padlist[pads[-1] - 1].cd()#complicated divide function
      
      legend.SetBorderSize(0)
      legend.SetFillStyle(0)
      legend.Draw()
      canvas.cd()
      padlist[pads[-1] - 1].Draw()

    canvas.cd()
    CMS_lumi.lumi_13TeV = ""
    CMS_lumi.writeExtraText = 1
    CMS_lumi.extraText = "Simulation"
    CMS_lumi.lumi_sqrtS = "" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

    CMS_lumi.cmsTextSize = 0.8
    CMS_lumi.cmsTextOffset = 0.1
    CMS_lumi.lumiTextSize = 0.7
    CMS_lumi.lumiTextOffset = 0.1
    
    CMS_lumi.relPosX = 0.12
    
    CMS_lumi.hOffset = -0.0
    
    iPeriod=0   # 13TeV
    iPos=0     # CMS inside frame
    
    CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)
      
    canvas.Modified()
    canvas.Update()
    canvas.SaveAs( outname+"_" + channel + ".pdf" )
    canvas.SaveAs( outname+"_" + channel + ".png" )

    return

    
def my_style():
    
    ROOT.gStyle.SetLabelSize( fontsize, "x" );
    ROOT.gStyle.SetLabelSize( fontsize, "y" );
    ROOT.gStyle.SetLabelSize( fontsize, "z" );

    ROOT.gStyle.SetTitleFontSize( 1.5*fontsize );
    ROOT.gStyle.SetTitleSize( fontsize, "x" );
    ROOT.gStyle.SetTitleSize( fontsize, "y" );
    ROOT.gStyle.SetTitleSize( fontsize, "z" );


    ROOT.gStyle.SetTitleOffset( 1.4, "xy" );
    ROOT.gStyle.SetTitleFont( 62, "bla" );

    ROOT.gStyle.SetPadBottomMargin(0.15);
    ROOT.gStyle.SetPadTopMargin(5.50);
    ROOT.gStyle.SetPadLeftMargin(0.03);
    ROOT.gStyle.SetPadRightMargin(0.03);

    ROOT.gStyle.SetStatX( 0.88 );
    ROOT.gStyle.SetStatY( 0.87 );
    ROOT.gStyle.SetNdivisions( 505 );

    ROOT.gStyle.SetCanvasColor(-1); 
    ROOT.gStyle.SetPadColor(-1); 
    ROOT.gStyle.SetFrameFillColor(-1); 
    ROOT.gStyle.SetTitleFillColor(-1); 
    ROOT.gStyle.SetFillColor(-1); 
    ROOT.gStyle.SetFillStyle(4000); 
    ROOT.gStyle.SetStatStyle(0); 
    ROOT.gStyle.SetTitleStyle(0); 
    ROOT.gStyle.SetCanvasBorderSize(0); 
    ROOT.gStyle.SetFrameBorderSize(0); 
    ROOT.gStyle.SetLegendBorderSize(0); 
    ROOT.gStyle.SetStatBorderSize(0); 
    ROOT.gStyle.SetTitleBorderSize(0); 
    
if __name__ == '__main__':
    my_style()
    categories()
    #extendedcategories_lj()
    
    #categories_dil()
