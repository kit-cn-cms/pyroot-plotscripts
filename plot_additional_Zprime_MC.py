from plot_cuts_Zprime import *


additionalfunctions=[
                        #'float temp=1',
                        #for(int i; i<N_Sideband_top_withbtag_anti_Topfirst_Bottoms;i++){temp*=(Sideband_top_withbtag_anti_Topfirst_Bottoms_CSVv2[i]<0.46);};',
                        ##"float anti_loose_btag(const float* bottomCSVs, int sizeofarray){"+"\n"+"   float anti_tag=1;"+"\n"+"      for (int i=0;  i<sizeofarray;i++){"+"\n"+"        if (bottomCSVs[i]>0.46){"+"\n"+"        anti_tag=0;"+"\n"+"      }"+"\n"+"      }"+"\n"+"    return anti_tag;"+"}",
"""
float anti_loose_btag(float const* bottomCSVs, int sizeofarray){
    float anti_tag=1;
    for (int i=0; i<sizeofarray; i++){
        if(bottomCSVs[i]>0.46){
            //std::cout<<"bottomcsv"<<bottomCSVs[i]<<endl;
            //anti_tag=0;
        }
    }
            //std::cout<<"anti_tag"<<anti_tag<<endl;
    return anti_tag;
}
""",

"""

#include "TGraph.h"
#include "TGraphErrors.h"




std::vector<float> interpolateSFandSFerrors(TGraphErrors const& SF_Function, float x_value, bool x_value_filled){
    float deltax_min=9999999999;
    float res_y=0.0;
    float res_deltayup=0.0;
    float res_deltaydown=0.0;
    int i_x=0; 
    std::vector<float> res;
    if (x_value<0.001 || x_value_filled==false)
    {
        res.push_back(0.0);
        res.push_back(0.0);
        res.push_back(0.0);
        return res;
    } else
    {
        for(int i=0; i<SF_Function.GetN();i++){
            float deltax_temp=abs(x_value-SF_Function.GetX()[i]);
            if(deltax_min>deltax_temp){
                deltax_min=deltax_temp;
                i_x=i;
            }
        }
        std::cout<<"i_x=  "<<i_x<<endl;
        //if(i_x==0 || i_x==SF_Function.GetN() || (SF_Function.GetX()[i_x]-x_value)==0){
            //res.push_back(SF_Function.GetY()[i_x]);
            //res.push_back(SF_Function.GetErrorYhigh(i_x));
            //res.push_back(SF_Function.GetErrorYlow(i_x));
        //}else if(!(i_x==0 || i_x==SF_Function.GetN()) && (SF_Function.GetX()[i_x]-x_value)>0){
            //res.push_back((SF_Function.GetY()[i_x]-SF_Function.GetY()[i_x-1])/(SF_Function.GetX()[i_x]-SF_Function.GetX()[i_x-1])*(x_value-SF_Function.GetX()[i_x-1])+SF_Function.GetY()[i_x-1]);
            //res.push_back((SF_Function.GetErrorYhigh(i_x)-SF_Function.GetErrorYhigh(i_x-1))/(SF_Function.GetX()[i_x]-SF_Function.GetX()[i_x-1])*(x_value-SF_Function.GetX()[i_x-1])+SF_Function.GetErrorYhigh(i_x-1));
            //res.push_back((SF_Function.GetErrorYlow(i_x)-SF_Function.GetErrorYlow(i_x-1))/(SF_Function.GetX()[i_x]-SF_Function.GetX()[i_x-1])*(x_value-SF_Function.GetX()[i_x-1])+SF_Function.GetErrorYlow(i_x-1));
        //}else if(!(i_x==0 || i_x==SF_Function.GetN()) && (SF_Function.GetX()[i_x]-x_value)<0){
            //res.push_back((SF_Function.GetY()[i_x+1]-SF_Function.GetY()[i_x])/(SF_Function.GetX()[i_x+1]-SF_Function.GetX()[i_x])*(x_value-SF_Function.GetX()[i_x])+SF_Function.GetY()[i_x]);
            //res.push_back((SF_Function.GetErrorYhigh(i_x+1)-SF_Function.GetErrorYhigh(i_x))/(SF_Function.GetX()[i_x+1]-SF_Function.GetX()[i_x])*(x_value-SF_Function.GetX()[i_x])+SF_Function.GetErrorYhigh(i_x));
            //res.push_back((SF_Function.GetErrorYlow(i_x+1)-SF_Function.GetErrorYlow(i_x))/(SF_Function.GetX()[i_x+1]-SF_Function.GetX()[i_x])*(x_value-SF_Function.GetX()[i_x])+SF_Function.GetErrorYlow(i_x));
        //}
        res.push_back(SF_Function.GetY()[i_x]);
        res.push_back(SF_Function.GetErrorYhigh(i_x));
        res.push_back(SF_Function.GetErrorYlow(i_x));
    
    
        return res;    
    }
    std::cout<<"xvalue: "<<x_value<<"  SF"<<res[0]<<endl;
}
""",
     """
std::vector<float> bbarportionweight(int const N){
    std::vector<float> res;
    
    if(N>0){
        res.push_back(1.0);
        res.push_back(1.5);
        res.push_back(0.5);
        res.push_back(0.0);
    } else {
        res.push_back(1.0);
        res.push_back(1.0);
        res.push_back(1.0);
        res.push_back(1.0);
    };
    return res;
}
  
    """,
"""
bool IsnoSignal_notopbtag(float const* Zprimes_ABCD_M, float const* Tprimes_ABCD_M, float const* Tops_ABCD_maxsubjetCSVv2, float const* Ws_ABCD_MSD, float const* Tops_ABCD_MSD, float const* Tops_ABCD_t32, float const* Bottoms_ABCD_CSV, float const* Ws_ABCD_t21,int N_Zprime_ABCD){
    bool res=true;
    for (int i=0; i<N_Zprime_ABCD; i++){
        if (Zprimes_ABCD_M[i]>0 && Tprimes_ABCD_M[i]>500 && Tops_ABCD_maxsubjetCSVv2[i]<0.8 && 70<Ws_ABCD_MSD[i] && Ws_ABCD_MSD[i]<100 && Ws_ABCD_t21[i]<0.6 && 105<Tops_ABCD_MSD[i] && Tops_ABCD_MSD[i]<220 && Tops_ABCD_t32[i]<0.86 && Bottoms_ABCD_CSV[i]>0.8){
            res=false;
            break;
        }
    }
    return res;
}
""",
"""
bool IsnoSignal_withtopbtag(float const* Zprimes_ABCD_M, float const* Tprimes_ABCD_M, float const* Tops_ABCD_maxsubjetCSVv2, float const* Ws_ABCD_MSD, float const* Tops_ABCD_MSD, float const* Tops_ABCD_t32, float const* Bottoms_ABCD_CSV, float const* Ws_ABCD_t21,int N_Zprime_ABCD){
    bool res=true;
    for (int i=0; i<N_Zprime_ABCD; i++){
        if (Zprimes_ABCD_M[i]>0 && Tprimes_ABCD_M[i]>500 && Tops_ABCD_maxsubjetCSVv2[i]>0.8 && 70<Ws_ABCD_MSD[i] && Ws_ABCD_MSD[i]<100 && Ws_ABCD_t21[i]<0.6 && 105<Tops_ABCD_MSD[i] && Tops_ABCD_MSD[i]<220 && Tops_ABCD_t32[i]<0.86 && Bottoms_ABCD_CSV[i]>0.8){
            res=false;
            break;
        }
    }
    return res;
}
""",
"""
bool IsnoSignal_inclusive(float const* Zprimes_ABCD_M, float const* Tprimes_ABCD_M, float const* Ws_ABCD_MSD, float const* Tops_ABCD_MSD, float const* Tops_ABCD_t32, float const* Bottoms_ABCD_CSV, float const* Ws_ABCD_t21,int N_Zprime_ABCD){
    bool res=true;
    for (int i=0; i<N_Zprime_ABCD; i++){
        if (Zprimes_ABCD_M[i]>0 && Tprimes_ABCD_M[i]>500 && 70<Ws_ABCD_MSD[i] && Ws_ABCD_MSD[i]<100 && Ws_ABCD_t21[i]<0.6 && 105<Tops_ABCD_MSD[i] && Tops_ABCD_MSD[i]<220 && Tops_ABCD_t32[i]<0.86 && Bottoms_ABCD_CSV[i]>0.8){
            res=false;
            break;
        }
    }
    return res;
}
""" 




    ]




additionalobjectsfromaddtionalrootfile=[
    
"""



  TFile* SFfile = new TFile("/nfs/dust/cms/user/skudella/pyroot-plotscripts/Zprime_SBSSSFs_Graphs.root","READONLY");
  TGraphErrors* QCDMadgraph_Graph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M=(TGraphErrors*)SFfile->Get("Graph_QCDMadgraph_SB_SF_bottom_anti_Zprime_M");
  TGraphErrors* QCDMadgraph_Graph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt=(TGraphErrors*)SFfile->Get("Graph_QCDMadgraph_SB_SF_bottom_anti_Tops_Pt");
  TGraphErrors* QCDMadgraph_Graph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt=(TGraphErrors*)SFfile->Get("Graph_QCDMadgraph_SB_SF_top_anti_Tops_Pt");
  TGraphErrors* QCDMadgraph_Graph_SF_SB_top_anti_Signal_Topfirst_Ws_Pt=(TGraphErrors*)SFfile->Get("Graph_QCDMadgraph_SB_SF_top_anti_Ws_Pt");
  TGraphErrors* QCDPythia8_Graph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M=(TGraphErrors*)SFfile->Get("Graph_QCDPythia8_SB_SF_bottom_anti_Zprime_M");
  TGraphErrors* QCDPythia8_Graph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt=(TGraphErrors*)SFfile->Get("Graph_QCDPythia8_SB_SF_bottom_anti_Tops_Pt");
  TGraphErrors* QCDPythia8_Graph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt=(TGraphErrors*)SFfile->Get("Graph_QCDPythia8_SB_SF_top_anti_Tops_Pt");
  TGraphErrors* QCDPythia8_Graph_SF_SB_top_anti_Signal_Topfirst_Ws_Pt=(TGraphErrors*)SFfile->Get("Graph_QCDPythia8_SB_SF_top_anti_Ws_Pt");
  
  TGraphErrors* QCDMadgraph_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M=(TGraphErrors*)SFfile->Get("Graph_QCDMadgraph_SB_SF_withtopbtag_bottom_anti_Zprime_M");
  TGraphErrors* QCDMadgraph_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt=(TGraphErrors*)SFfile->Get("Graph_QCDMadgraph_SB_SF_withtopbtag_bottom_anti_Tops_Pt");
  TGraphErrors* QCDMadgraph_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt=(TGraphErrors*)SFfile->Get("Graph_QCDMadgraph_SB_SF_withtopbtag_top_anti_Tops_Pt");
  TGraphErrors* QCDMadgraph_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt=(TGraphErrors*)SFfile->Get("Graph_QCDMadgraph_SB_SF_withtopbtag_top_anti_Ws_Pt");
  TGraphErrors* QCDPythia8_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M=(TGraphErrors*)SFfile->Get("Graph_QCDPythia8_SB_SF_withtopbtag_bottom_anti_Zprime_M");
  TGraphErrors* QCDPythia8_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt=(TGraphErrors*)SFfile->Get("Graph_QCDPythia8_SB_SF_withtopbtag_bottom_anti_Tops_Pt");
  TGraphErrors* QCDPythia8_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt=(TGraphErrors*)SFfile->Get("Graph_QCDPythia8_SB_SF_withtopbtag_top_anti_Tops_Pt");
  TGraphErrors* QCDPythia8_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt=(TGraphErrors*)SFfile->Get("Graph_QCDPythia8_SB_SF_withtopbtag_top_anti_Ws_Pt");
  
  
  SFfile->cd();
  
"""
    
    ]


additionalvariables=[
			'anti_btag_withtopbtag:=anti_loose_btag(Sideband_withtopbtag_bottom_anti_Topfirst_Bottoms_CSVv2,N_Sideband_withtopbtag_bottom_anti_Topfirst_Bottoms)',
			'anti_btag:=anti_loose_btag(Sideband_bottom_anti_Topfirst_Bottoms_CSVv2,N_Sideband_bottom_anti_Topfirst_Bottoms)',
                        #'testea:=anti_btag + 2',
                        'QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M, Sideband_bottom_anti_Topfirst_Zprime_M ,true))[0]',
                        'QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt,Sideband_bottom_anti_Topfirst_Tops_Pt[0],N_Sideband_bottom_anti_Topfirst_Tops>0))[0]',
                        'QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt,Sideband_top_anti_Topfirst_Tops_Pt[0],N_Sideband_top_anti_Topfirst_Tops>0))[0]',
                        'QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Ws_Pt:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_top_anti_Signal_Topfirst_Ws_Pt,Sideband_top_anti_Topfirst_Ws_Pt[0],N_Sideband_top_anti_Topfirst_Ws>0))[0]',
                        'QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M, Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M,true))[0]',
                        'QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt,Sideband_withtopbtag_bottom_anti_Topfirst_Tops_Pt[0],N_Sideband_withtopbtag_bottom_anti_Topfirst_Tops>0))[0]',
                        'QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt,Sideband_top_withbtag_anti_Topfirst_Tops_Pt[0],N_Sideband_top_withbtag_anti_Topfirst_Tops>0))[0]',
                        'QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt,Sideband_top_withbtag_anti_Topfirst_Ws_Pt[0],N_Sideband_top_withbtag_anti_Topfirst_Ws>0))[0]',
			
                        'QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M, Sideband_bottom_anti_Topfirst_Zprime_M,true))[0]',
                        'QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt,Sideband_bottom_anti_Topfirst_Tops_Pt[0],N_Sideband_bottom_anti_Topfirst_Tops>0))[0]',
                        'QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt,Sideband_top_anti_Topfirst_Tops_Pt[0],N_Sideband_top_anti_Topfirst_Tops>0))[0]',
                        'QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Ws_Pt:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_top_anti_Signal_Topfirst_Ws_Pt,Sideband_top_anti_Topfirst_Ws_Pt[0],N_Sideband_top_anti_Topfirst_Ws>0))[0]',
                        'QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M, Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M,true))[0]',
                        'QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt,Sideband_withtopbtag_bottom_anti_Topfirst_Tops_Pt[0],N_Sideband_withtopbtag_bottom_anti_Topfirst_Tops>0))[0]',
                        'QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt,Sideband_top_withbtag_anti_Topfirst_Tops_Pt[0],N_Sideband_top_withbtag_anti_Topfirst_Tops>0))[0]',
                        'QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt,Sideband_top_withbtag_anti_Topfirst_Ws_Pt[0],N_Sideband_top_withbtag_anti_Topfirst_Ws>0))[0]',
                        
                        
                        
                        'QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M_systup:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M, Sideband_bottom_anti_Topfirst_Zprime_M ,true))[1]',
                        'QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt_systup:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt,Sideband_bottom_anti_Topfirst_Tops_Pt[0],N_Sideband_bottom_anti_Topfirst_Tops>0))[1]',
                        'QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt_systup:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt,Sideband_top_anti_Topfirst_Tops_Pt[0],N_Sideband_top_anti_Topfirst_Tops>0))[1]',
                        'QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Ws_Pt_systup:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_top_anti_Signal_Topfirst_Ws_Pt,Sideband_top_anti_Topfirst_Ws_Pt[0],N_Sideband_top_anti_Topfirst_Ws>0))[1]',
                        'QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M_systup:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M, Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M,true))[1]',
                        'QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt_systup:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt,Sideband_withtopbtag_bottom_anti_Topfirst_Tops_Pt[0],N_Sideband_withtopbtag_bottom_anti_Topfirst_Tops>0))[1]',
                        'QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt_systup:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt,Sideband_top_withbtag_anti_Topfirst_Tops_Pt[0],N_Sideband_top_withbtag_anti_Topfirst_Tops>0))[1]',
                        'QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt_systup:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt,Sideband_top_withbtag_anti_Topfirst_Ws_Pt[0],N_Sideband_top_withbtag_anti_Topfirst_Ws>0))[1]',
			
                        'QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M_systup:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M, Sideband_bottom_anti_Topfirst_Zprime_M,true))[1]',
                        'QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt_systup:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt,Sideband_bottom_anti_Topfirst_Tops_Pt[0],N_Sideband_bottom_anti_Topfirst_Tops>0))[1]',
                        'QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt_systup:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt,Sideband_top_anti_Topfirst_Tops_Pt[0],N_Sideband_top_anti_Topfirst_Tops>0))[1]',
                        'QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Ws_Pt_systup:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_top_anti_Signal_Topfirst_Ws_Pt,Sideband_top_anti_Topfirst_Ws_Pt[0],N_Sideband_top_anti_Topfirst_Ws>0))[1]',
                        'QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M_systup:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M, Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M,true))[1]',
                        'QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt_systup:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt,Sideband_withtopbtag_bottom_anti_Topfirst_Tops_Pt[0],N_Sideband_withtopbtag_bottom_anti_Topfirst_Tops>0))[1]',
                        'QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt_systup:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt,Sideband_top_withbtag_anti_Topfirst_Tops_Pt[0],N_Sideband_top_withbtag_anti_Topfirst_Tops>0))[1]',
                        'QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt_systup:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt,Sideband_top_withbtag_anti_Topfirst_Ws_Pt[0],N_Sideband_top_withbtag_anti_Topfirst_Ws>0))[1]',                        
                        
                        
                        'QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M_systdown:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M, Sideband_bottom_anti_Topfirst_Zprime_M ,true))[2]',
                        'QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt_systdown:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt,Sideband_bottom_anti_Topfirst_Tops_Pt[0],N_Sideband_bottom_anti_Topfirst_Tops>0))[2]',
                        'QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt_systdown:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt,Sideband_top_anti_Topfirst_Tops_Pt[0],N_Sideband_top_anti_Topfirst_Tops>0))[2]',
                        'QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Ws_Pt_systdown:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_top_anti_Signal_Topfirst_Ws_Pt,Sideband_top_anti_Topfirst_Ws_Pt[0],N_Sideband_top_anti_Topfirst_Ws>0))[2]',
                        'QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M_systdown:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M, Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M,true))[2]',
                        'QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt_systdown:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt,Sideband_withtopbtag_bottom_anti_Topfirst_Tops_Pt[0],N_Sideband_withtopbtag_bottom_anti_Topfirst_Tops>0))[2]',
                        'QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt_systdown:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt,Sideband_top_withbtag_anti_Topfirst_Tops_Pt[0],N_Sideband_top_withbtag_anti_Topfirst_Tops>0))[2]',
                        'QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt_systdown:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt,Sideband_top_withbtag_anti_Topfirst_Ws_Pt[0],N_Sideband_top_withbtag_anti_Topfirst_Ws>0))[2]',
			
                        'QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M_systdown:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M, Sideband_bottom_anti_Topfirst_Zprime_M,true))[2]',
                        'QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt_systdown:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt,Sideband_bottom_anti_Topfirst_Tops_Pt[0],N_Sideband_bottom_anti_Topfirst_Tops>0))[2]',
                        'QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt_systdown:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt,Sideband_top_anti_Topfirst_Tops_Pt[0],N_Sideband_top_anti_Topfirst_Tops>0))[2]',
                        'QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Ws_Pt_systdown:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_top_anti_Signal_Topfirst_Ws_Pt,Sideband_top_anti_Topfirst_Ws_Pt[0],N_Sideband_top_anti_Topfirst_Ws>0))[2]',
                        'QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M_systdown:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M, Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M,true))[2]',
                        'QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt_systdown:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt,Sideband_withtopbtag_bottom_anti_Topfirst_Tops_Pt[0],N_Sideband_withtopbtag_bottom_anti_Topfirst_Tops>0))[2]',
                        'QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt_systdown:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt,Sideband_top_withbtag_anti_Topfirst_Tops_Pt[0],N_Sideband_top_withbtag_anti_Topfirst_Tops>0))[2]',
                        'QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt_systdown:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt,Sideband_top_withbtag_anti_Topfirst_Ws_Pt[0],N_Sideband_top_withbtag_anti_Topfirst_Ws>0))[2]',
                        
                        
                        
                        
                        
                        
                        
			"Sideband_withtopbtag_bottom_anti_Topfirst_Bottoms_CSVv2", "N_Sideband_withtopbtag_bottom_anti_Topfirst_Bottoms",
                        "Sideband_bottom_anti_Topfirst_Bottoms_CSVv2","N_Sideband_bottom_anti_Topfirst_Bottoms",
                        "Sideband_bottom_anti_Topfirst_Zprime_M","true",
                        "Sideband_bottom_anti_Topfirst_Tops_Pt","N_Sideband_bottom_anti_Topfirst_Tops",
                        "Sideband_top_anti_Topfirst_Tops_Pt","N_Sideband_top_anti_Topfirst_Tops",
                        "Sideband_top_anti_Topfirst_Ws_Pt","N_Sideband_top_anti_Topfirst_Ws",
                        "Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M","true",
                        "Sideband_withtopbtag_bottom_anti_Topfirst_Tops_Pt","N_Sideband_withtopbtag_bottom_anti_Topfirst_Tops",
                        "Sideband_top_withbtag_anti_Topfirst_Tops_Pt","N_Sideband_top_withbtag_anti_Topfirst_Tops",
                        "Sideband_top_withbtag_anti_Topfirst_Ws_Pt","N_Sideband_top_withbtag_anti_Topfirst_Ws",
                        
                        
                        'bportionup:=(bbarportionweight(N_AK4_bottom_tag_candidates))[1]',
			'bportiondown:=(bbarportionweight(N_AK4_bottom_tag_candidates))[2]',
			'bportionno:=(bbarportionweight(N_AK4_bottom_tag_candidates))[3]',
			'bportionnorm:=(bbarportionweight(N_AK4_bottom_tag_candidates))[0]',
			"N_AK4_bottom_tag_candidates",
			'IsnoSignalnotopbtag:=IsnoSignal_notopbtag(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD)',
			'IsnoSignalwithtopbtag:=IsnoSignal_withtopbtag(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD)',
			'IsnoSignalinclusive:=IsnoSignal_inclusive(Zprimes_ABCD_M, Tprimes_ABCD_M, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD)',
                        "N_Zprime_ABCD","Zprimes_ABCD_M","Tprimes_ABCD_M","Tops_ABCD_maxsubjetCSVv2","Ws_ABCD_MSD","Tops_ABCD_MSD","Tops_ABCD_t32","Bottoms_ABCD_CSV","Ws_ABCD_t21",                        

]