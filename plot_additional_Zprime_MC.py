from plot_cuts_ZPrime_MC import *



if ABCDversion is 'ABCD1':
    generalselection=plotselection_ABCD1_general
    generalselection_0=plotselection_ABCD1_general_0
    generalselection_i=plotselection_ABCD1_general_i
    cut1=plotselection_W_tau21
    cut1_0=plotselection_W_tau21_0
    cut1_i=plotselection_W_tau21_i
    cut2=plotselection_B_CSV
    cut2_0=plotselection_B_CSV_0
    cut2_i=plotselection_B_CSV_i
    cut3=plotselection_tau32
    cut3_0=plotselection_tau32_0
    cut3_i=plotselection_tau32_i

    cut1_anti=plotselection_W_tau21_anti
    cut1_anti_0=plotselection_W_tau21_anti_0
    cut1_anti_i=plotselection_W_tau21_anti_i
    cut2_anti=plotselection_B_CSV_anti
    cut2_anti_0=plotselection_B_CSV_anti_0
    cut2_anti_i=plotselection_B_CSV_anti_i
    cut3_anti=plotselection_tau32_anti
    cut3_anti_0=plotselection_tau32_anti_0
    cut3_anti_i=plotselection_tau32_anti_i
    
    
    
    
if ABCDversion is 'ABCD2':
    generalselection=plotselection_ABCD2_general
    generalselection_0=plotselection_ABCD2_general_0
    generalselection_i=plotselection_ABCD2_general_i
    cut1=plotselection_W_tau21
    cut1_0=plotselection_W_tau21_0
    cut1_i=plotselection_W_tau21_i
    cut2=plotselection_B_CSV
    cut2_0=plotselection_B_CSV_0
    cut2_i=plotselection_B_CSV_i
    cut3=plotselection_t_MSD
    cut3_0=plotselection_t_MSD_0
    cut3_i=plotselection_t_MSD_i 

    cut1_anti=plotselection_W_tau21_anti
    cut1_anti_0=plotselection_W_tau21_anti_0
    cut1_anti_i=plotselection_W_tau21_anti_i
    cut2_anti=plotselection_B_CSV_anti
    cut2_anti_0=plotselection_B_CSV_anti_0
    cut2_anti_i=plotselection_B_CSV_anti_i
    cut3_anti=plotselection_t_MSD_anti
    cut3_anti_0=plotselection_t_MSD_anti_0
    cut3_anti_i=plotselection_t_MSD_anti_i 
    
    
if ABCDversion is 'ABCD3':
    generalselection=plotselection_ABCD3_general
    generalselection_0=plotselection_ABCD3_general_0
    generalselection_i=plotselection_ABCD3_general_i
    cut1=plotselection_W_tau21
    cut1_0=plotselection_W_tau21_0
    cut1_i=plotselection_W_tau21_i
    cut2=plotselection_B_CSV
    cut2_0=plotselection_B_CSV_0
    cut2_i=plotselection_B_CSV_i
    cut3=plotselection_W_MSD
    cut3_0=plotselection_W_MSD_0
    cut3_i=plotselection_W_MSD_i    

    cut1_anti=plotselection_W_tau21_anti
    cut1_anti_0=plotselection_W_tau21_anti_0
    cut1_anti_i=plotselection_W_tau21_anti_i
    cut2_anti=plotselection_B_CSV_anti
    cut2_anti_0=plotselection_B_CSV_anti_0
    cut2_anti_i=plotselection_B_CSV_anti_i
    cut3_anti=plotselection_W_MSD_anti
    cut3_anti_0=plotselection_W_MSD_anti_0
    cut3_anti_i=plotselection_W_MSD_anti_i
    
if ABCDversion is 'ABCD4':
    generalselection=plotselection_ABCD4_general
    generalselection_0=plotselection_ABCD4_general_0
    generalselection_i=plotselection_ABCD4_general_i
    cut1=plotselection_W_MSD
    cut1_0=plotselection_W_MSD_0
    cut1_i=plotselection_W_MSD_i
    cut2=plotselection_B_CSV
    cut2_0=plotselection_B_CSV_0
    cut2_i=plotselection_B_CSV_i
    cut3=plotselection_TprimeMass
    cut3_0=plotselection_TprimeMass_0
    cut3_i=plotselection_TprimeMass_i
    
    cut1_anti=plotselection_W_MSD_anti
    cut1_anti_0=plotselection_W_MSD_anti_0
    cut1_anti_i=plotselection_W_MSD_anti_i
    cut2_anti=plotselection_B_CSV_anti
    cut2_anti_0=plotselection_B_CSV_anti_0
    cut2_anti_i=plotselection_B_CSV_anti_i
    cut3_anti=plotselection_TprimeMass_anti
    cut3_anti_0=plotselection_TprimeMass_anti_0
    cut3_anti_i=plotselection_TprimeMass_anti_i
    
if ABCDversion is 'ABCD5':
    generalselection=plotselection_ABCD5_general
    generalselection_0=plotselection_ABCD5_general_0
    generalselection_i=plotselection_ABCD5_general_i
    cut1=plotselection_W_MSD
    cut1_0=plotselection_W_MSD_0
    cut1_i=plotselection_W_MSD_i
    cut2=plotselection_B_CSV
    cut2_0=plotselection_B_CSV_0
    cut2_i=plotselection_B_CSV_i
    cut3=plotselection_W_tau21
    cut3_0=plotselection_W_tau21_0
    cut3_i=plotselection_W_tau21_i
   
    cut1_anti=plotselection_W_MSD_anti
    cut1_anti_0=plotselection_W_MSD_anti_0
    cut1_anti_i=plotselection_W_MSD_anti_i
    cut2_anti=plotselection_B_CSV_anti
    cut2_anti_0=plotselection_B_CSV_anti_0
    cut2_anti_i=plotselection_B_CSV_anti_i
    cut3_anti=plotselection_W_tau21_anti
    cut3_anti_0=plotselection_W_tau21_anti_0
    cut3_anti_i=plotselection_W_tau21_anti_i
    
    if radi=='CHSSoftDrop':
        if WZwindow and fullWMSD:
            if old:
                Zprime_withtopbtag_systrate=0.026335429083
                Zprime_withtopbtag_systshape_m=-0.000014237
                Zprime_withtopbtag_systshape_c=1.01372
                Zprime_notopbtag_systrate=0.025035741394
                Zprime_notopbtag_systshape_m=-0.0000563142
                Zprime_notopbtag_systshape_c=1.10324
                            
            else:
                Zprime_withtopbtag_systrate=0.0437729147047
                Zprime_withtopbtag_systshape_m=-0.00000748147
                Zprime_withtopbtag_systshape_c=0.959254
                Zprime_notopbtag_systrate=0.0416820871399
                Zprime_notopbtag_systshape_m=-0.0000748556
                Zprime_notopbtag_systshape_c=1.111
            
    if radi=='CHSPruning':
        if (not WZwindow) and fullWMSD:
            if old:
                Zprime_withtopbtag_systrate=0.0615567929662
                Zprime_withtopbtag_systshape_m=0.0000820445
                Zprime_withtopbtag_systshape_c=0.815448
                Zprime_notopbtag_systrate=0.0237731064005
                Zprime_notopbtag_systshape_m=-0.000079382
                Zprime_notopbtag_systshape_c=1.14017
            else:
                Zprime_withtopbtag_systrate=0.0351573391572
                Zprime_withtopbtag_systshape_m=-6.02946e-05
                Zprime_withtopbtag_systshape_c=1.10373
                Zprime_notopbtag_systrate=0.0349000297823
                Zprime_notopbtag_systshape_m=-6.51334e-05
                Zprime_notopbtag_systshape_c=1.11245
        
if ABCDversion is 'ABCD6':
    generalselection=plotselection_ABCD6_general
    generalselection_0=plotselection_ABCD6_general_0
    generalselection_i=plotselection_ABCD6_general_i
    cut1=plotselection_B_CSV
    cut1_0=plotselection_B_CSV_0
    cut1_i=plotselection_B_CSV_i
    cut2=plotselection_W_tau21
    cut2_0=plotselection_W_tau21_0
    cut2_i=plotselection_W_tau21_i
    cut3=plotselection_t_MSD
    cut3_0=plotselection_t_MSD_0
    cut3_i=plotselection_t_MSD_i
  
    cut1_anti=plotselection_B_CSV_anti
    cut1_anti_0=plotselection_B_CSV_anti_0
    cut1_anti_i=plotselection_B_CSV_anti_i
    cut2_anti=plotselection_W_tau21_anti
    cut2_anti_0=plotselection_W_tau21_anti_0
    cut2_anti_i=plotselection_W_tau21_anti_i
    cut3_anti=plotselection_t_MSD_anti
    cut3_anti_0=plotselection_t_MSD_anti_0
    cut3_anti_i=plotselection_t_MSD_anti_i
    
if ABCDversion is 'ABCD7':
    generalselection=plotselection_ABCD7_general
    generalselection_0=plotselection_ABCD7_general_0
    generalselection_i=plotselection_ABCD7_general_i
    cut1=plotselection_B_CSV
    cut1_0=plotselection_B_CSV_0
    cut1_i=plotselection_B_CSV_i
    cut2=plotselection_t_MSD
    cut2_0=plotselection_t_MSD_0
    cut2_i=plotselection_t_MSD_i
    cut3=plotselection_W_MSD
    cut3_0=plotselection_W_MSD_0
    cut3_i=plotselection_W_MSD_i

    cut1_anti=plotselection_B_CSV_anti
    cut1_anti_0=plotselection_B_CSV_anti_0
    cut1_anti_i=plotselection_B_CSV_anti_i
    cut2_anti=plotselection_t_MSD_anti
    cut2_anti_0=plotselection_t_MSD_anti_0
    cut2_anti_i=plotselection_t_MSD_anti_i
    cut3_anti=plotselection_W_MSD_anti
    cut3_anti_0=plotselection_W_MSD_anti_0
    cut3_anti_i=plotselection_W_MSD_anti_i


#stringforPDFs="float Weight_pdf_variation_260001"
#stringforPDFs1="Weight_pdf_variation_260001"
#stringforPDFs2="""
#PDFweights.push_back(Weight_pdf_variation_260001);
#"""
stringforPDFs="float Weight_pdf_1"
stringforPDFs1="Weight_pdf_1"
stringforPDFs2="""
PDFweights.push_back(Weight_pdf_1);
"""

for i in range(2,100):
    #if i<10:
        #istring="00"+str(i)
    #if i>9 and i<100:
        #istring="0"+str(i)
    #if i>99:
        #istring=""+str(i)
    #stringforPDFs=stringforPDFs+(", float Weight_nnpdf30_lo_as_0130_"+str(i))
    #stringforPDFs1=stringforPDFs1+(", Weight_nnpdf30_lo_as_0130_"+str(i))
    #stringforPDFs2=stringforPDFs2+("PDFweights.push_back(Weight_nnpdf30_lo_as_0130_"+str(i)+");")
    #stringforPDFs=stringforPDFs+(", float Weight_pdf_variation_260"+istring)
    #stringforPDFs1=stringforPDFs1+(", Weight_pdf_variation_260"+istring)
    #stringforPDFs2=stringforPDFs2+("PDFweights.push_back(Weight_pdf_variation_260"+istring+");")
    istring=str(i)
    stringforPDFs=stringforPDFs+(", float Weight_pdf_"+istring)
    stringforPDFs1=stringforPDFs1+(", Weight_pdf_"+istring)
    stringforPDFs2=stringforPDFs2+("PDFweights.push_back(Weight_pdf_"+istring+");")#print stringforPDFs

additionalfunctions=[
                        #'float temp=1',
                        #for(int i; i<N_Sideband_top_withbtag_anti_Topfirst_Bottoms;i++){temp*=(Sideband_top_withbtag_anti_Topfirst_Bottoms_CSVv2[i]<0.46);};',
                        ##"float anti_loose_btag(const float* bottomCSVs, int sizeofarray){"+"\n"+"   float anti_tag=1;"+"\n"+"      for (int i=0;  i<sizeofarray;i++){"+"\n"+"        if (bottomCSVs[i]>0.46){"+"\n"+"        anti_tag=0;"+"\n"+"      }"+"\n"+"      }"+"\n"+"    return anti_tag;"+"}",
                        
                        
"""
std::vector<float> PDF_RMS(""" + stringforPDFs + """){
    std::vector<float> PDFweights;
    std::vector<float> res;
    float RMSmean=0.0;
    float RMSerror=0.0;
   
    """+stringforPDFs2+"""
    for(int i=0; i<PDFweights.size(); i++){
        RMSmean+=PDFweights[i]*PDFweights[i];
    }
    RMSmean=sqrt(RMSmean/float(PDFweights.size()));
    for(int i=0; i<PDFweights.size(); i++){
        RMSerror+=(RMSmean-PDFweights[i])*(RMSmean-PDFweights[i]);      
    }
    RMSerror=sqrt(RMSerror/float(PDFweights.size()));
    res.push_back(RMSmean);
    res.push_back(RMSmean+RMSerror);
    res.push_back(RMSmean-RMSerror);
    
    return res;
}
"""                        
,                        
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
        //std::cout<<"i_x=  "<<i_x<<endl;
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
    //std::cout<<"xvalue: "<<x_value<<"  SF"<<res[0]<<endl;
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
int ABCD_Category(float const* Zprimes_ABCD""" +  radi + """_M, float const* Tprimes_ABCD""" +  radi + """_M, float const* Tops_ABCD""" +  radi + """_maxsubjetCSVv2, float const* Ws_ABCD""" +  radi + """_MSD, float const* Ws_ABCD""" +  radi + """_corrL2L3, float const* Tops_ABCD""" +  radi + """_MSD, float const* Tops_ABCD""" +  radi + """_corrL2L3, float const* Tops_ABCD""" +  radi + """_t32, float const* Bottoms_ABCD""" +  radi + """_CSV, float const* Ws_ABCD""" +  radi + """_t21, float const* Ws_ABCD""" + radi + """_Pt, float const* Tops_ABCD""" + radi + """_Pt, float const* Bottoms_ABCD""" + radi + """_Pt, float Evt_HT_Jets, int N_Zprime_ABCD""" + radi + """, float N_Jets, float N_packedPatJetsAK8PF""" +  radi + """){

    int res=0;
    for (int i=0; i<N_Zprime_ABCD""" +  radi + """; i++){
        if ("""+ generalselection_i +"""){
            if("""+ plotselection_topsubjetCSVv2_i +"""){
                if("""+ cut1_i +"""){
                    if("""+ cut2_i + """){
                        if(""" + cut3_i + """){
                            res=1;
                            break;
                        }
                        if(""" + cut3_anti_i + """){
                            res=2;
                            break;
                        }
                    }
                    if("""+ cut2_anti_i + """){
                        if(""" + cut3_i + """){
                            res=3;
                            break;
                        }
                        if(""" + cut3_anti_i + """){
                            res=4;
                            break;
                        }
                    }                
                }
                if("""+ cut1_anti_i +"""){
                    if("""+ cut2_i + """){
                        if(""" + cut3_i + """){
                            res=5;
                            break;
                        }
                        if(""" + cut3_anti_i + """){
                            res=6;
                            break;
                        }
                    }
        
                    if("""+ cut2_anti_i + """){
                        if(""" + cut3_i + """){
                            res=7;
                            break;
                        }
                        if(""" + cut3_anti_i + """){
                            res=8;
                            break;
                        }
                    }                
                }
            } else {
                if("""+ cut1_i +"""){
                    if("""+ cut2_i + """){
                        if(""" + cut3_i + """){
                            res=9;
                            break;
                        }
                        if(""" + cut3_anti_i + """){
                            res=10;
                            break;
                        }
                    }
                    if("""+ cut2_anti_i + """){
                        if(""" + cut3_i + """){
                            res=11;
                            break;
                        }
                        if(""" + cut3_anti_i + """){
                            res=12;
                            break;
                        }
                    }                
                }
                if("""+ cut1_anti_i +"""){
                    if("""+ cut2_i + """){
                        if(""" + cut3_i + """){
                            res=13;
                            break;
                        }
                        if(""" + cut3_anti_i + """){
                            res=14;
                            break;
                        }
                    }
                    if("""+ cut2_anti_i + """){
                        if(""" + cut3_i + """){
                            res=15;
                            break;
                        }
                        if(""" + cut3_anti_i + """){
                            res=16;
                            break;
                        }
                    }                
                }
            }
        }
    }
    return res;
}
""",



"""
std::vector<float> CSV_weights_""" + ABCDversion + """(float const* Zprimes_ABCD""" + radi + """_M, float const* Tprimes_ABCD""" + radi + """_M, float const* Tops_ABCD""" + radi + """_maxsubjetCSVv2, float const* Ws_ABCD""" + radi + """_MSD, float const* Ws_ABCD""" + radi + """_corrL2L3, float const* Tops_ABCD""" + radi + """_MSD, float const* Tops_ABCD""" + radi + """_corrL2L3, float const* Tops_ABCD""" + radi + """_t32, float const* Bottoms_ABCD""" + radi + """_CSV, float const* Ws_ABCD""" + radi + """_t21, float const* Ws_ABCD""" + radi + """_Pt, float const* Tops_ABCD""" + radi + """_Pt, float const* Bottoms_ABCD""" + radi + """_Pt, float Evt_HT_Jets, int N_Zprime_ABCD""" + radi + """, float N_Jets, float N_packedPatJetsAK8PF""" +  radi + """, float const* Bottoms_ABCD""" + radi + """_WeightCSVnominal, float const* Bottoms_ABCD""" + radi + """_WeightCSVLFup, float const* Bottoms_ABCD""" + radi + """_WeightCSVLFdown, float const* Bottoms_ABCD""" + radi + """_WeightCSVHFup, float const* Bottoms_ABCD""" + radi + """_WeightCSVHFdown, float const* Bottoms_ABCD""" + radi + """_WeightCSVHFStats1up, float const* Bottoms_ABCD""" + radi + """_WeightCSVHFStats1down, float const* Bottoms_ABCD""" + radi + """_WeightCSVLFStats1up, float const* Bottoms_ABCD""" + radi + """_WeightCSVLFStats1down, float const* Bottoms_ABCD""" + radi + """_WeightCSVHFStats2up, float const* Bottoms_ABCD""" + radi + """_WeightCSVHFStats2down, float const* Bottoms_ABCD""" + radi + """_WeightCSVLFStats2up, float const* Bottoms_ABCD""" + radi + """_WeightCSVLFStats2down, float const* Bottoms_ABCD""" + radi + """_WeightCSVCErr1up, float const* Bottoms_ABCD""" + radi + """_WeightCSVCErr1down, float const* Bottoms_ABCD""" + radi + """_WeightCSVCErr2up, float const* Bottoms_ABCD""" + radi + """_WeightCSVCErr2down, float const* Topsubjets_ABCD""" + radi + """_WeightCSVnominal, float const* Topsubjets_ABCD""" + radi + """_WeightCSVLFup, float const* Topsubjets_ABCD""" + radi + """_WeightCSVLFdown, float const* Topsubjets_ABCD""" + radi + """_WeightCSVHFup, float const* Topsubjets_ABCD""" + radi + """_WeightCSVHFdown, float const* Topsubjets_ABCD""" + radi + """_WeightCSVHFStats1up, float const* Topsubjets_ABCD""" + radi + """_WeightCSVHFStats1down, float const* Topsubjets_ABCD""" + radi + """_WeightCSVLFStats1up, float const* Topsubjets_ABCD""" + radi + """_WeightCSVLFStats1down, float const* Topsubjets_ABCD""" + radi + """_WeightCSVHFStats2up, float const* Topsubjets_ABCD""" + radi + """_WeightCSVHFStats2down, float const* Topsubjets_ABCD""" + radi + """_WeightCSVLFStats2up, float const* Topsubjets_ABCD""" + radi + """_WeightCSVLFStats2down, float const* Topsubjets_ABCD""" + radi + """_WeightCSVCErr1up, float const* Topsubjets_ABCD""" + radi + """_WeightCSVCErr1down, float const* Topsubjets_ABCD""" + radi + """_WeightCSVCErr2up, float const* Topsubjets_ABCD""" + radi + """_WeightCSVCErr2down  ){
    std::vector<float> weights;
    
    float CSVnominal=1.0;
    float CSVLFup=1.0;
    float CSVLFdown=1.0;
    float CSVHFup=1.0;
    float CSVHFdown=1.0;
    float CSVHFStats1up=1.0;
    float CSVHFStats1down=1.0;
    float CSVLFStats1up=1.0;
    float CSVLFStats1down=1.0;
    float CSVHFStats2up=1.0;
    float CSVHFStats2down=1.0;
    float CSVLFStats2up=1.0;
    float CSVLFStats2down=1.0;
    float CSVCErr1up=1.0;
    float CSVCErr1down=1.0;
    float CSVCErr2up=1.0;
    float CSVCErr2down=1.0;

    float tpt=0.0;
    float Wpt=0.0;
    float bpt=0.0;

    for (int i=0; i<N_Zprime_ABCD""" + radi + """; i++){
        if ("""+ generalselection_i +""" && Bottoms_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0){   
            if (Bottoms_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVnominal *= Bottoms_ABCD""" + radi + """_WeightCSVnominal[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVLFup[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVLFup[i]<=1000){
                CSVLFup *= Bottoms_ABCD""" + radi + """_WeightCSVLFup[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVLFdown[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVLFdown[i]<=1000){
                CSVLFdown *= Bottoms_ABCD""" + radi + """_WeightCSVLFdown[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVHFup[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVHFup[i]<=1000){
                CSVHFup *= Bottoms_ABCD""" + radi + """_WeightCSVHFup[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVHFdown[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVHFdown[i]<=1000){
                CSVHFdown *= Bottoms_ABCD""" + radi + """_WeightCSVHFdown[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVHFStats1up[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVHFStats1up[i]<=1000){
                CSVHFStats1up *= Bottoms_ABCD""" + radi + """_WeightCSVHFStats1up[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVHFStats1down[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVHFStats1down[i]<=1000){
                CSVHFStats1down *= Bottoms_ABCD""" + radi + """_WeightCSVHFStats1down[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVLFStats1up[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVLFStats1up[i]<=1000){
                CSVLFStats1up *= Bottoms_ABCD""" + radi + """_WeightCSVLFStats1up[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVLFStats1down[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVLFStats1down[i]<=1000){
                CSVLFStats1down *= Bottoms_ABCD""" + radi + """_WeightCSVLFStats1down[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVHFStats2up[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVHFStats2up[i]<=1000){
                CSVHFStats2up *= Bottoms_ABCD""" + radi + """_WeightCSVHFStats2up[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVHFStats2down[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVHFStats2down[i]<=1000){
                CSVHFStats2down *= Bottoms_ABCD""" + radi + """_WeightCSVHFStats2down[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVLFStats2up[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVLFStats2up[i]<=1000){
                CSVLFStats2up *= Bottoms_ABCD""" + radi + """_WeightCSVLFStats2up[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVLFStats2down[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVLFStats2down[i]<=1000){
                CSVLFStats2down *= Bottoms_ABCD""" + radi + """_WeightCSVLFStats2down[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVCErr1up[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVCErr1up[i]<=1000){
                CSVCErr1down *= Bottoms_ABCD""" + radi + """_WeightCSVCErr1up[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVCErr1down[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVCErr1down[i]<=1000){
                CSVCErr1down *= Bottoms_ABCD""" + radi + """_WeightCSVCErr1down[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVCErr2up[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVCErr2up[i]<=1000){
                CSVCErr2up *= Bottoms_ABCD""" + radi + """_WeightCSVCErr2up[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVCErr2down[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVCErr2down[i]<=1000){
                CSVCErr2down *= Bottoms_ABCD""" + radi + """_WeightCSVCErr2down[i];
            }
            
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVnominal *= Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVLFup *= Topsubjets_ABCD""" + radi + """_WeightCSVLFup[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVLFdown *= Topsubjets_ABCD""" + radi + """_WeightCSVLFdown[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVHFup *= Topsubjets_ABCD""" + radi + """_WeightCSVHFup[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVHFdown *= Topsubjets_ABCD""" + radi + """_WeightCSVHFdown[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVHFStats1up *= Topsubjets_ABCD""" + radi + """_WeightCSVHFStats1up[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVHFStats1down *= Topsubjets_ABCD""" + radi + """_WeightCSVHFStats1down[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVLFStats1up *= Topsubjets_ABCD""" + radi + """_WeightCSVLFStats1up[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVLFStats1down *= Topsubjets_ABCD""" + radi + """_WeightCSVLFStats1down[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVHFStats2up *= Topsubjets_ABCD""" + radi + """_WeightCSVHFStats2up[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVHFStats2down *= Topsubjets_ABCD""" + radi + """_WeightCSVHFStats2down[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVLFStats2up *= Topsubjets_ABCD""" + radi + """_WeightCSVLFStats2up[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVLFStats2down *= Topsubjets_ABCD""" + radi + """_WeightCSVLFStats2down[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVCErr1down *= Topsubjets_ABCD""" + radi + """_WeightCSVCErr1up[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVCErr1down *= Topsubjets_ABCD""" + radi + """_WeightCSVCErr1down[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVCErr2up *= Topsubjets_ABCD""" + radi + """_WeightCSVCErr2up[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVCErr2down *= Topsubjets_ABCD""" + radi + """_WeightCSVCErr2down[i];
            }
            break;
        }
    };
    
    weights.push_back(CSVnominal);
    weights.push_back(CSVLFup);
    weights.push_back(CSVLFdown);
    weights.push_back(CSVHFup);
    weights.push_back(CSVHFdown);
    weights.push_back(CSVHFStats1up);
    weights.push_back(CSVHFStats1down);
    weights.push_back(CSVLFStats1up);
    weights.push_back(CSVLFStats1down);
    weights.push_back(CSVHFStats2up);
    weights.push_back(CSVHFStats2down);
    weights.push_back(CSVLFStats2up);
    weights.push_back(CSVLFStats2down);
    weights.push_back(CSVCErr1up);
    weights.push_back(CSVCErr1down);
    weights.push_back(CSVCErr2up);
    weights.push_back(CSVCErr2down);    
    
    return weights;
}

"""
,

"""
std::vector<float> toptag_weights_""" + ABCDversion + """(float const* Zprimes_ABCD""" + radi + """_M, float const* Tprimes_ABCD""" + radi + """_M, float const* Tops_ABCD""" + radi + """_maxsubjetCSVv2, float const* Ws_ABCD""" + radi + """_MSD, float const* Ws_ABCD""" + radi + """_corrL2L3, float const* Tops_ABCD""" + radi + """_MSD, float const* Tops_ABCD""" + radi + """_corrL2L3, float const* Tops_ABCD""" + radi + """_t32, float const* Bottoms_ABCD""" + radi + """_CSV, float const* Ws_ABCD""" + radi + """_t21, float const* Ws_ABCD""" + radi + """_Pt, float const* Tops_ABCD""" + radi + """_Pt, float const* Bottoms_ABCD""" + radi + """_Pt, float Evt_HT_Jets, int N_Zprime_ABCD""" + radi + """, float N_Jets, float N_packedPatJetsAK8PF""" +  radi + """, float const* Tops_ABCD""" + radi + """_real, float const* Tops_ABCD""" + radi + """_matcheddecays){
    std::vector<float> weights;
    
    float toptagnominal=1.0;
    float toptagup=1.0;
    float toptagdown=1.0;
    
    float topmisstagnominal=1.0;
    float topmisstagup=1.0;
    float topmisstagdown=1.0;
    
    float SF_top_tau32_MSD_=""" + MCSF_top_t32_MSD + """;
    float SF_top_tau32_MSD_up=""" + MCSF_top_t32_MSD_up + """;
    float SF_top_tau32_MSD_down=""" + MCSF_top_t32_MSD_down + """;
    float SF_top_tau32_MSDanti_=""" + MCSF_top_t32_MSD_down + """;
    float SF_top_tau32_MSDanti_up=""" + MCSF_top_t32_MSD_up + """;
    float SF_top_tau32_MSDanti_down=""" + MCSF_top_t32_MSD_down + """;
    float SF_top_tau32anti_MSD_=""" + MCSF_top_t32_MSD + """;
    float SF_top_tau32anti_MSD_up=""" + MCSF_top_t32_MSD_up + """;
    float SF_top_tau32anti_MSD_down=""" + MCSF_top_t32_MSD_down + """;
    float SF_top_tau32anti_MSDanti_=""" + MCSF_top_t32_MSD + """;
    float SF_top_tau32anti_MSDanti_up=""" + MCSF_top_t32_MSD_up + """;
    float SF_top_tau32anti_MSDanti_down=""" + MCSF_top_t32_MSD_down + """;
    
    float SF_topmiss_tau32_MSD_=""" + MCSF_topmiss_t32_MSD + """;
    float SF_topmiss_tau32_MSD_up=""" + MCSF_topmiss_t32_MSD_up + """;
    float SF_topmiss_tau32_MSD_down=""" + MCSF_topmiss_t32_MSD_down + """;
    float SF_topmiss_tau32_MSDanti_=""" + MCSF_topmiss_t32_MSDanti + """;
    float SF_topmiss_tau32_MSDanti_up=""" + MCSF_topmiss_t32_MSDanti_up + """;
    float SF_topmiss_tau32_MSDanti_down=""" + MCSF_topmiss_t32_MSDanti_down + """;
    float SF_topmiss_tau32anti_MSD_=""" + MCSF_topmiss_t32anti_MSD + """;
    float SF_topmiss_tau32anti_MSD_up=""" + MCSF_topmiss_t32anti_MSD_up + """;
    float SF_topmiss_tau32anti_MSD_down=""" + MCSF_topmiss_t32anti_MSD_down + """;
    float SF_topmiss_tau32anti_MSDanti_=""" + MCSF_topmiss_t32anti_MSDanti + """;
    float SF_topmiss_tau32anti_MSDanti_up=""" + MCSF_topmiss_t32anti_MSDanti_up + """;
    float SF_topmiss_tau32anti_MSDanti_down=""" + MCSF_topmiss_t32anti_MSDanti_down + """;
    
    
    for (int i=0; i<N_Zprime_ABCD""" + radi + """; i++){
        if (""" + generalselection_i + """){
            if(Tops_ABCD""" + radi + """_real[i]==1 && Tops_ABCD""" + radi + """_matcheddecays[i]>2){
            //if(Tops_ABCD""" + radi + """_real[i]==1){
                if(""" + plotselection_tau32_i + """ && """ + plotselection_t_MSD_i + """){
                    toptagnominal *= SF_top_tau32_MSD_;
                    toptagup *= (SF_top_tau32_MSD_ + SF_top_tau32_MSD_up);
                    toptagdown *= (SF_top_tau32_MSD_ - SF_top_tau32_MSD_down);
                }
                if(""" + plotselection_tau32_anti_i + """ && """ + plotselection_t_MSD_i + """){
                    toptagnominal *= SF_top_tau32anti_MSD_;
                    toptagup *= (SF_top_tau32anti_MSD_ + SF_top_tau32anti_MSD_up);
                    toptagdown *= (SF_top_tau32anti_MSD_ - SF_top_tau32anti_MSD_down);
                }
                if(""" + plotselection_tau32_i + """ && """ + plotselection_t_MSD_anti_i + """){
                    toptagnominal *= SF_top_tau32_MSDanti_;
                    toptagup *= (SF_top_tau32_MSDanti_ + SF_top_tau32_MSDanti_up);
                    toptagdown *= (SF_top_tau32_MSDanti_ - SF_top_tau32_MSDanti_down);
                }
                if(""" + plotselection_tau32_anti_i + """ && """ + plotselection_t_MSD_anti_i + """){
                    toptagnominal *= SF_top_tau32anti_MSDanti_;
                    toptagup *= (SF_top_tau32anti_MSDanti_ + SF_top_tau32anti_MSDanti_up);
                    toptagdown *= (SF_top_tau32anti_MSDanti_ - SF_top_tau32anti_MSDanti_down);
                }
            } else {
                if(""" + plotselection_tau32_i + """ && """ + plotselection_t_MSD_i + """){
                    topmisstagnominal *= SF_topmiss_tau32_MSD_;
                    topmisstagup *= (SF_topmiss_tau32_MSD_ + SF_topmiss_tau32_MSD_up);
                    topmisstagdown *= (SF_topmiss_tau32_MSD_ - SF_topmiss_tau32_MSD_down);
                }
                if(""" + plotselection_tau32_anti_i + """ && """ + plotselection_t_MSD_i + """){
                    topmisstagnominal *= SF_topmiss_tau32anti_MSD_;
                    topmisstagup *= (SF_topmiss_tau32anti_MSD_ + SF_topmiss_tau32anti_MSD_up);
                    topmisstagdown *= (SF_topmiss_tau32anti_MSD_ - SF_topmiss_tau32anti_MSD_down);
                }
                if(""" + plotselection_tau32_i + """ && """ + plotselection_t_MSD_anti_i + """){
                    topmisstagnominal *= SF_topmiss_tau32_MSDanti_;
                    topmisstagup *= (SF_topmiss_tau32_MSDanti_ + SF_topmiss_tau32_MSDanti_up);
                    topmisstagdown *= (SF_topmiss_tau32_MSDanti_ - SF_topmiss_tau32_MSDanti_down);
                }
                if(""" + plotselection_tau32_anti_i + """ && """ + plotselection_t_MSD_anti_i + """){
                    topmisstagnominal *= SF_topmiss_tau32anti_MSDanti_;
                    topmisstagup *= (SF_topmiss_tau32anti_MSDanti_ + SF_topmiss_tau32anti_MSDanti_up);
                    topmisstagdown *= (SF_topmiss_tau32anti_MSDanti_ - SF_topmiss_tau32anti_MSDanti_down);
                }
            }
            break;
        }
    }
    
    weights.push_back(toptagnominal);
    weights.push_back(toptagup);
    weights.push_back(toptagdown);
    weights.push_back(topmisstagnominal);
    weights.push_back(topmisstagup);
    weights.push_back(topmisstagdown);
   
        
    return weights;
}

"""
,
"""
std::vector<float> Wtag_weights_""" + ABCDversion + """(float const* Zprimes_ABCD""" + radi + """_M, float const* Tprimes_ABCD""" + radi + """_M, float const* Tops_ABCD""" + radi + """_maxsubjetCSVv2, float const* Ws_ABCD""" + radi + """_MSD, float const* Ws_ABCD""" + radi + """_corrL2L3, float const* Tops_ABCD""" + radi + """_MSD, float const* Tops_ABCD""" + radi + """_corrL2L3, float const* Tops_ABCD""" + radi + """_t32, float const* Bottoms_ABCD""" + radi + """_CSV, float const* Ws_ABCD""" + radi + """_t21, float const* Ws_ABCD""" + radi + """_Pt, float const* Tops_ABCD""" + radi + """_Pt, float const* Bottoms_ABCD""" + radi + """_Pt, float Evt_HT_Jets, int N_Zprime_ABCD""" + radi + """, float N_Jets, float N_packedPatJetsAK8PF""" +  radi + """, float const* Ws_ABCD""" + radi + """_real, float const* Ws_ABCD""" + radi + """_matcheddecays){
    std::vector<float> weights;
    
    float Wtag_tag_t21_nominal=1.0;
    float Wtag_tag_t21_up=1.0;
    float Wtag_tag_t21_down=1.0;

    
    float SF_W_tau21_MSD=""" + MCSF_W_t21_MSD + """;
    float SF_W_tau21_MSD_up=""" + MCSF_W_t21_MSD_up + """;
    float SF_W_tau21_MSD_down=""" + MCSF_W_t21_MSD_down + """;
    float SF_W_tau21_MSDanti=""" + MCSF_W_t21_MSDanti + """;
    float SF_W_tau21_MSDanti_up=""" + MCSF_W_t21_MSDanti_up + """;
    float SF_W_tau21_MSDanti_down=""" + MCSF_W_t21_MSDanti_down + """;
    float SF_W_tau21anti_MSD=""" + MCSF_W_t21anti_MSD + """;
    float SF_W_tau21anti_MSD_up=""" + MCSF_W_t21anti_MSD_up + """;
    float SF_W_tau21anti_MSD_down=""" + MCSF_W_t21anti_MSD_down + """;
    float SF_W_tau21anti_MSDanti=""" + MCSF_W_t21anti_MSDanti + """;
    float SF_W_tau21anti_MSDanti_up=""" + MCSF_W_t21anti_MSDanti_up + """;
    float SF_W_tau21anti_MSDanti_down=""" + MCSF_W_t21anti_MSDanti_down + """;
    
    float SF_Wmiss_tau21_MSD=""" + MCSF_Wmiss_t21_MSD + """;
    float SF_Wmiss_tau21_MSD_up=""" + MCSF_Wmiss_t21_MSD_up + """;
    float SF_Wmiss_tau21_MSD_down=""" + MCSF_Wmiss_t21_MSD_down + """;
    float SF_Wmiss_tau21_MSDanti=""" + MCSF_Wmiss_t21_MSDanti + """;
    float SF_Wmiss_tau21_MSDanti_up=""" + MCSF_Wmiss_t21_MSDanti_up + """;
    float SF_Wmiss_tau21_MSDanti_down=""" + MCSF_Wmiss_t21_MSDanti_down + """;
    float SF_Wmiss_tau21anti_MSD=""" + MCSF_Wmiss_t21anti_MSD + """;
    float SF_Wmiss_tau21anti_MSD_up=""" + MCSF_Wmiss_t21anti_MSD_up + """;
    float SF_Wmiss_tau21anti_MSD_down=""" + MCSF_Wmiss_t21anti_MSD_down + """;
    float SF_Wmiss_tau21anti_MSDanti=""" + MCSF_Wmiss_t21anti_MSDanti + """;
    float SF_Wmiss_tau21anti_MSDanti_up=""" + MCSF_Wmiss_t21anti_MSDanti_up + """;
    float SF_Wmiss_tau21anti_MSDanti_down=""" + MCSF_Wmiss_t21anti_MSDanti_down + """;    
    

    for (int i=0; i<N_Zprime_ABCD""" + radi + """; i++){
        if ("""+ generalselection_i + """ ){
                if(""" + plotselection_W_tau21_i + """ && """ + plotselection_W_MSD_i + """){
                    Wtag_tag_t21_nominal *= SF_W_tau21_MSD;
                    Wtag_tag_t21_up *= (SF_W_tau21_MSD + SF_W_tau21_MSD_up);
                    Wtag_tag_t21_down *= (SF_W_tau21_MSD - SF_W_tau21_MSD_down);
                }
                if(""" + plotselection_W_tau21_anti_i + """ && """ + plotselection_W_MSD_i + """){
                    Wtag_tag_t21_nominal *= SF_W_tau21anti_MSD;
                    Wtag_tag_t21_up *= (SF_W_tau21anti_MSD + SF_W_tau21anti_MSD_down);
                    Wtag_tag_t21_down *= (SF_W_tau21anti_MSD - SF_W_tau21anti_MSD_up);
                }
                if(""" + plotselection_W_tau21_i + """ && """ + plotselection_W_MSD_anti_i + """){
                    Wtag_tag_t21_nominal *= SF_W_tau21_MSDanti;
                    Wtag_tag_t21_up *= (SF_W_tau21_MSDanti + SF_W_tau21_MSDanti_up);
                    Wtag_tag_t21_down *= (SF_W_tau21_MSDanti - SF_W_tau21_MSDanti_down);
                }
                if(""" + plotselection_W_tau21_anti_i + """ && """ + plotselection_W_MSD_i + """){
                    Wtag_tag_t21_nominal *= SF_W_tau21anti_MSDanti;
                    Wtag_tag_t21_up *= (SF_W_tau21anti_MSDanti + SF_W_tau21anti_MSDanti_down);
                    Wtag_tag_t21_down *= (SF_W_tau21anti_MSDanti - SF_W_tau21anti_MSDanti_up);
                }

            break;
        }
    }
    
    weights.push_back(Wtag_tag_t21_nominal);
    weights.push_back(Wtag_tag_t21_up);
    weights.push_back(Wtag_tag_t21_down);
    
    
    return weights;
}

""",

"""
std::vector<float> RenFacEnv(float muR20_muF20, float muR05_muF05, float muR10_muF20 , float muR10_muF05, float muR20_muF10, float muR05_muF10){
    std::vector<float> res;
    float envUp=1.0;
    float envDown=1.0;
    
        if (muR20_muF20>envUp){
            envUp=muR20_muF20;
        }
        if (muR20_muF20<envDown){
            envDown=muR20_muF20;
        }
        if (muR05_muF05>envUp){
            envUp=muR05_muF05;
        }
        if (muR05_muF05<envDown){
            envDown=muR05_muF05;
        }
        if (muR10_muF20>envUp){
            envUp=muR10_muF20;
        }
        if (muR10_muF20<envDown){
            envDown=muR10_muF20;
        }
        if (muR10_muF05>envUp){
            envUp=muR10_muF05;
        }
        if (muR10_muF05<envDown){
            envDown=muR10_muF05;
        }
        if (muR20_muF10>envUp){
            envUp=muR20_muF10;
        }
        if (muR20_muF10<envDown){
            envDown=muR20_muF10;
        }
        if (muR05_muF10>envUp){
            envUp=muR05_muF10;
        }
        if (muR05_muF10<envDown){
            envDown=muR05_muF10;
        }

    res.push_back(envUp);
    res.push_back(envDown);
    
    return res;
}
"""

"""
std::vector<float> ABCD_syts(float const* Zprimes_ABCD""" +  radi + """_M, float const* Tprimes_ABCD""" +  radi + """_M, float const* Tops_ABCD""" +  radi + """_maxsubjetCSVv2, float const* Ws_ABCD""" +  radi + """_MSD, float const* Ws_ABCD""" +  radi + """_corrL2L3, float const* Tops_ABCD""" +  radi + """_MSD, float const* Tops_ABCD""" +  radi + """_corrL2L3, float const* Tops_ABCD""" +  radi + """_t32, float const* Bottoms_ABCD""" +  radi + """_CSV, float const* Ws_ABCD""" +  radi + """_t21, float const* Ws_ABCD""" + radi + """_Pt, float const* Tops_ABCD""" + radi + """_Pt, float const* Bottoms_ABCD""" + radi + """_Pt, float Evt_HT_Jets, int N_Zprime_ABCD""" + radi + """, float N_Jets, float N_packedPatJetsAK8PF""" +  radi + """){
    std::vector<float> res;
    float ABCD_rateUp=1.0;
    float ABCD_rateDown=1.0;
    float ABCD_shapeUp=1.0;
    float ABCD_shapeDown=1.0;
    
    for (int i=0; i<N_Zprime_ABCD""" + radi + """; i++){
        if ("""+ generalselection_i +"""){
            if("""+ plotselection_topsubjetCSVv2_i +"""){
                ABCD_rateUp=(1.0 + (""" + str(Zprime_withtopbtag_systrate) + """));
                ABCD_rateDown=(1.0 - (""" + str(Zprime_withtopbtag_systrate) + """));
                ABCD_shapeUp=(1.0+(((Zprimes_ABCD""" +  radi + """_M[i]) * (""" + str(Zprime_withtopbtag_systshape_m) + """) + (""" + str(Zprime_withtopbtag_systshape_c) + """))-1.0));
                ABCD_shapeDown=(1.0-(((Zprimes_ABCD""" +  radi + """_M[i]) * (""" + str(Zprime_withtopbtag_systshape_m) + """) + (""" + str(Zprime_withtopbtag_systshape_c) + """))-1.0));
            } else {
                ABCD_rateUp=(1.0 + (""" + str(Zprime_notopbtag_systrate) + """));
                ABCD_rateDown=(1.0 - (""" + str(Zprime_notopbtag_systrate) + """));
                //ABCD_shapeUp=(((Zprimes_ABCD""" +  radi + """_M[i]) * (""" + str(Zprime_notopbtag_systshape_m) + """) + (""" + str(Zprime_notopbtag_systshape_c) + """)));
                //ABCD_shapeDown=(-((Zprimes_ABCD""" +  radi + """_M[i]) * (""" + str(Zprime_notopbtag_systshape_m) + """) + (""" + str(Zprime_notopbtag_systshape_c) + """)));
                ABCD_shapeUp=(1.0+(((Zprimes_ABCD""" +  radi + """_M[i]) * (""" + str(Zprime_notopbtag_systshape_m) + """) + (""" + str(Zprime_notopbtag_systshape_c) + """))-1.0));
                ABCD_shapeDown=(1.0-(((Zprimes_ABCD""" +  radi + """_M[i]) * (""" + str(Zprime_notopbtag_systshape_m) + """) + (""" + str(Zprime_notopbtag_systshape_c) + """))-1.0));
            };
        break;
        };
    }
    res.push_back(ABCD_rateUp);
    res.push_back(ABCD_rateDown);
    res.push_back(ABCD_shapeUp);
    res.push_back(ABCD_shapeDown);
    
    return res;
}
""",


"""
std::vector<float> CSV_weights_all(float const* Zprimes_ABCD""" + radi + """_M, float const* Tprimes_ABCD""" + radi + """_M, float const* Tops_ABCD""" + radi + """_maxsubjetCSVv2, float const* Ws_ABCD""" + radi + """_MSD, float const* Ws_ABCD""" + radi + """_corrL2L3, float const* Tops_ABCD""" + radi + """_MSD, float const* Tops_ABCD""" + radi + """_corrL2L3, float const* Tops_ABCD""" + radi + """_t32, float const* Bottoms_ABCD""" + radi + """_CSV, float const* Ws_ABCD""" + radi + """_t21, float const* Ws_ABCD""" + radi + """_Pt, float const* Tops_ABCD""" + radi + """_Pt, float const* Bottoms_ABCD""" + radi + """_Pt, float Evt_HT_Jets, int N_Zprime_ABCD""" + radi + """, float N_Jets, float N_packedPatJetsAK8PF""" +  radi + """, float const* Bottoms_ABCD""" + radi + """_WeightCSVnominal, float const* Bottoms_ABCD""" + radi + """_WeightCSVLFup, float const* Bottoms_ABCD""" + radi + """_WeightCSVLFdown, float const* Bottoms_ABCD""" + radi + """_WeightCSVHFup, float const* Bottoms_ABCD""" + radi + """_WeightCSVHFdown, float const* Bottoms_ABCD""" + radi + """_WeightCSVHFStats1up, float const* Bottoms_ABCD""" + radi + """_WeightCSVHFStats1down, float const* Bottoms_ABCD""" + radi + """_WeightCSVLFStats1up, float const* Bottoms_ABCD""" + radi + """_WeightCSVLFStats1down, float const* Bottoms_ABCD""" + radi + """_WeightCSVHFStats2up, float const* Bottoms_ABCD""" + radi + """_WeightCSVHFStats2down, float const* Bottoms_ABCD""" + radi + """_WeightCSVLFStats2up, float const* Bottoms_ABCD""" + radi + """_WeightCSVLFStats2down, float const* Bottoms_ABCD""" + radi + """_WeightCSVCErr1up, float const* Bottoms_ABCD""" + radi + """_WeightCSVCErr1down, float const* Bottoms_ABCD""" + radi + """_WeightCSVCErr2up, float const* Bottoms_ABCD""" + radi + """_WeightCSVCErr2down, float const* Topsubjets_ABCD""" + radi + """_WeightCSVnominal, float const* Topsubjets_ABCD""" + radi + """_WeightCSVLFup, float const* Topsubjets_ABCD""" + radi + """_WeightCSVLFdown, float const* Topsubjets_ABCD""" + radi + """_WeightCSVHFup, float const* Topsubjets_ABCD""" + radi + """_WeightCSVHFdown, float const* Topsubjets_ABCD""" + radi + """_WeightCSVHFStats1up, float const* Topsubjets_ABCD""" + radi + """_WeightCSVHFStats1down, float const* Topsubjets_ABCD""" + radi + """_WeightCSVLFStats1up, float const* Topsubjets_ABCD""" + radi + """_WeightCSVLFStats1down, float const* Topsubjets_ABCD""" + radi + """_WeightCSVHFStats2up, float const* Topsubjets_ABCD""" + radi + """_WeightCSVHFStats2down, float const* Topsubjets_ABCD""" + radi + """_WeightCSVLFStats2up, float const* Topsubjets_ABCD""" + radi + """_WeightCSVLFStats2down, float const* Topsubjets_ABCD""" + radi + """_WeightCSVCErr1up, float const* Topsubjets_ABCD""" + radi + """_WeightCSVCErr1down, float const* Topsubjets_ABCD""" + radi + """_WeightCSVCErr2up, float const* Topsubjets_ABCD""" + radi + """_WeightCSVCErr2down  ){
    std::vector<float> weights;
    
    float CSVnominal=1.0;
    float CSVLFup=1.0;
    float CSVLFdown=1.0;
    float CSVHFup=1.0;
    float CSVHFdown=1.0;
    float CSVHFStats1up=1.0;
    float CSVHFStats1down=1.0;
    float CSVLFStats1up=1.0;
    float CSVLFStats1down=1.0;
    float CSVHFStats2up=1.0;
    float CSVHFStats2down=1.0;
    float CSVLFStats2up=1.0;
    float CSVLFStats2down=1.0;
    float CSVCErr1up=1.0;
    float CSVCErr1down=1.0;
    float CSVCErr2up=1.0;
    float CSVCErr2down=1.0;

    float tpt=0.0;
    float Wpt=0.0;
    float bpt=0.0;

    for (int i=0; i<N_Zprime_ABCD""" + radi + """; i++){
        if ( Evt_HT_Jets>1000 && Bottoms_ABCD""" + radi + """_WeightCSVnominal[i]>(-0.5)){         
            CSVnominal *= Bottoms_ABCD""" + radi + """_WeightCSVnominal[i];
            CSVLFup *= Bottoms_ABCD""" + radi + """_WeightCSVLFup[i];
            CSVLFdown *= Bottoms_ABCD""" + radi + """_WeightCSVLFdown[i];
            CSVHFup *= Bottoms_ABCD""" + radi + """_WeightCSVHFup[i];
            CSVHFdown *= Bottoms_ABCD""" + radi + """_WeightCSVHFdown[i];
            CSVHFStats1up *= Bottoms_ABCD""" + radi + """_WeightCSVHFStats1up[i];
            CSVHFStats1down *= Bottoms_ABCD""" + radi + """_WeightCSVHFStats1down[i];
            CSVLFStats1up *= Bottoms_ABCD""" + radi + """_WeightCSVLFStats1up[i];
            CSVLFStats1down *= Bottoms_ABCD""" + radi + """_WeightCSVLFStats1down[i];
            CSVHFStats2up *= Bottoms_ABCD""" + radi + """_WeightCSVHFStats2up[i];
            CSVHFStats2down *= Bottoms_ABCD""" + radi + """_WeightCSVHFStats2down[i];
            CSVLFStats2up *= Bottoms_ABCD""" + radi + """_WeightCSVLFStats2up[i];
            CSVLFStats2down *= Bottoms_ABCD""" + radi + """_WeightCSVLFStats2down[i];
            CSVCErr1down *= Bottoms_ABCD""" + radi + """_WeightCSVCErr1up[i];
            CSVCErr1down *= Bottoms_ABCD""" + radi + """_WeightCSVCErr1down[i];
            CSVCErr2up *= Bottoms_ABCD""" + radi + """_WeightCSVCErr2up[i];
            CSVCErr2down *= Bottoms_ABCD""" + radi + """_WeightCSVCErr2down[i];
            
            CSVnominal *= Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i];
            CSVLFup *= Topsubjets_ABCD""" + radi + """_WeightCSVLFup[i];
            CSVLFdown *= Topsubjets_ABCD""" + radi + """_WeightCSVLFdown[i];
            CSVHFup *= Topsubjets_ABCD""" + radi + """_WeightCSVHFup[i];
            CSVHFdown *= Topsubjets_ABCD""" + radi + """_WeightCSVHFdown[i];
            CSVHFStats1up *= Topsubjets_ABCD""" + radi + """_WeightCSVHFStats1up[i];
            CSVHFStats1down *= Topsubjets_ABCD""" + radi + """_WeightCSVHFStats1down[i];
            CSVLFStats1up *= Topsubjets_ABCD""" + radi + """_WeightCSVLFStats1up[i];
            CSVLFStats1down *= Topsubjets_ABCD""" + radi + """_WeightCSVLFStats1down[i];
            CSVHFStats2up *= Topsubjets_ABCD""" + radi + """_WeightCSVHFStats2up[i];
            CSVHFStats2down *= Topsubjets_ABCD""" + radi + """_WeightCSVHFStats2down[i];
            CSVLFStats2up *= Topsubjets_ABCD""" + radi + """_WeightCSVLFStats2up[i];
            CSVLFStats2down *= Topsubjets_ABCD""" + radi + """_WeightCSVLFStats2down[i];
            CSVCErr1down *= Topsubjets_ABCD""" + radi + """_WeightCSVCErr1up[i];
            CSVCErr1down *= Topsubjets_ABCD""" + radi + """_WeightCSVCErr1down[i];
            CSVCErr2up *= Topsubjets_ABCD""" + radi + """_WeightCSVCErr2up[i];
            CSVCErr2down *= Topsubjets_ABCD""" + radi + """_WeightCSVCErr2down[i];
                        
        }
    };
    
    weights.push_back(CSVnominal);
    weights.push_back(CSVLFup);
    weights.push_back(CSVLFdown);
    weights.push_back(CSVHFup);
    weights.push_back(CSVHFdown);
    weights.push_back(CSVHFStats1up);
    weights.push_back(CSVHFStats1down);
    weights.push_back(CSVLFStats1up);
    weights.push_back(CSVLFStats1down);
    weights.push_back(CSVHFStats2up);
    weights.push_back(CSVHFStats2down);
    weights.push_back(CSVLFStats2up);
    weights.push_back(CSVLFStats2down);
    weights.push_back(CSVCErr1up);
    weights.push_back(CSVCErr1down);
    weights.push_back(CSVCErr2up);
    weights.push_back(CSVCErr2down);    
    
    return weights;
}

"""
,
"""float triggerresult(int Triggered_HLT_PFHT800_vX, int Triggered_HLT_PFHT900_vX, int Triggered_HLT_PFJet450_vX, float Prescale_HLT_PFHT800_vX, float Prescale_HLT_PFHT900_vX,float Prescale_HLT_PFJet450_vX){
    int result=0;
    if(Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFJet450_vX){result=1.0;}; //run H has damaged PFHT900 GeV
    return result;
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
                        
                        
                        
                        'QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M_systUp:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M, Sideband_bottom_anti_Topfirst_Zprime_M ,true))[1]',
                        'QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt_systUp:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt,Sideband_bottom_anti_Topfirst_Tops_Pt[0],N_Sideband_bottom_anti_Topfirst_Tops>0))[1]',
                        'QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt_systUp:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt,Sideband_top_anti_Topfirst_Tops_Pt[0],N_Sideband_top_anti_Topfirst_Tops>0))[1]',
                        'QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Ws_Pt_systUp:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_top_anti_Signal_Topfirst_Ws_Pt,Sideband_top_anti_Topfirst_Ws_Pt[0],N_Sideband_top_anti_Topfirst_Ws>0))[1]',
                        'QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M_systUp:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M, Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M,true))[1]',
                        'QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt_systUp:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt,Sideband_withtopbtag_bottom_anti_Topfirst_Tops_Pt[0],N_Sideband_withtopbtag_bottom_anti_Topfirst_Tops>0))[1]',
                        'QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt_systUp:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt,Sideband_top_withbtag_anti_Topfirst_Tops_Pt[0],N_Sideband_top_withbtag_anti_Topfirst_Tops>0))[1]',
                        'QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt_systUp:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt,Sideband_top_withbtag_anti_Topfirst_Ws_Pt[0],N_Sideband_top_withbtag_anti_Topfirst_Ws>0))[1]',
			
                        'QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M_systUp:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M, Sideband_bottom_anti_Topfirst_Zprime_M,true))[1]',
                        'QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt_systUp:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt,Sideband_bottom_anti_Topfirst_Tops_Pt[0],N_Sideband_bottom_anti_Topfirst_Tops>0))[1]',
                        'QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt_systUp:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt,Sideband_top_anti_Topfirst_Tops_Pt[0],N_Sideband_top_anti_Topfirst_Tops>0))[1]',
                        'QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Ws_Pt_systUp:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_top_anti_Signal_Topfirst_Ws_Pt,Sideband_top_anti_Topfirst_Ws_Pt[0],N_Sideband_top_anti_Topfirst_Ws>0))[1]',
                        'QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M_systUp:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M, Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M,true))[1]',
                        'QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt_systUp:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt,Sideband_withtopbtag_bottom_anti_Topfirst_Tops_Pt[0],N_Sideband_withtopbtag_bottom_anti_Topfirst_Tops>0))[1]',
                        'QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt_systUp:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt,Sideband_top_withbtag_anti_Topfirst_Tops_Pt[0],N_Sideband_top_withbtag_anti_Topfirst_Tops>0))[1]',
                        'QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt_systUp:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt,Sideband_top_withbtag_anti_Topfirst_Ws_Pt[0],N_Sideband_top_withbtag_anti_Topfirst_Ws>0))[1]',                        
                        
                        
                        'QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M_systDown:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M, Sideband_bottom_anti_Topfirst_Zprime_M ,true))[2]',
                        'QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt_systDown:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt,Sideband_bottom_anti_Topfirst_Tops_Pt[0],N_Sideband_bottom_anti_Topfirst_Tops>0))[2]',
                        'QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt_systDown:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt,Sideband_top_anti_Topfirst_Tops_Pt[0],N_Sideband_top_anti_Topfirst_Tops>0))[2]',
                        'QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Ws_Pt_systDown:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_top_anti_Signal_Topfirst_Ws_Pt,Sideband_top_anti_Topfirst_Ws_Pt[0],N_Sideband_top_anti_Topfirst_Ws>0))[2]',
                        'QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M_systDown:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M, Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M,true))[2]',
                        'QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt_systDown:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt,Sideband_withtopbtag_bottom_anti_Topfirst_Tops_Pt[0],N_Sideband_withtopbtag_bottom_anti_Topfirst_Tops>0))[2]',
                        'QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt_systDown:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt,Sideband_top_withbtag_anti_Topfirst_Tops_Pt[0],N_Sideband_top_withbtag_anti_Topfirst_Tops>0))[2]',
                        'QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt_systDown:=(interpolateSFandSFerrors(*QCDMadgraph_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt,Sideband_top_withbtag_anti_Topfirst_Ws_Pt[0],N_Sideband_top_withbtag_anti_Topfirst_Ws>0))[2]',
			
                        'QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M_systDown:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M, Sideband_bottom_anti_Topfirst_Zprime_M,true))[2]',
                        'QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt_systDown:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt,Sideband_bottom_anti_Topfirst_Tops_Pt[0],N_Sideband_bottom_anti_Topfirst_Tops>0))[2]',
                        'QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt_systDown:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt,Sideband_top_anti_Topfirst_Tops_Pt[0],N_Sideband_top_anti_Topfirst_Tops>0))[2]',
                        'QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Ws_Pt_systDown:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_top_anti_Signal_Topfirst_Ws_Pt,Sideband_top_anti_Topfirst_Ws_Pt[0],N_Sideband_top_anti_Topfirst_Ws>0))[2]',
                        'QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M_systDown:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M, Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M,true))[2]',
                        'QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt_systDown:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt,Sideband_withtopbtag_bottom_anti_Topfirst_Tops_Pt[0],N_Sideband_withtopbtag_bottom_anti_Topfirst_Tops>0))[2]',
                        'QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt_systDown:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt,Sideband_top_withbtag_anti_Topfirst_Tops_Pt[0],N_Sideband_top_withbtag_anti_Topfirst_Tops>0))[2]',
                        'QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt_systDown:=(interpolateSFandSFerrors(*QCDPythia8_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt,Sideband_top_withbtag_anti_Topfirst_Ws_Pt[0],N_Sideband_top_withbtag_anti_Topfirst_Ws>0))[2]',
                        
                      
                        
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
                        
			'bportionUp:=(bbarportionweight(N_AK4_bottom_tag_candidates))[1]',
			'bportionDown:=(bbarportionweight(N_AK4_bottom_tag_candidates))[2]',
			'bportionno:=(bbarportionweight(N_AK4_bottom_tag_candidates))[3]',
			'bportionnorm:=(bbarportionweight(N_AK4_bottom_tag_candidates))[0]',
			"N_AK4_bottom_tag_candidates",
                        
                        
                        'ABCD_CatID:=1.0 * ABCD_Category(Zprimes_ABCD' + radi + '_M,   Tprimes_ABCD' + radi + '_M,   Tops_ABCD' + radi + '_maxsubjetCSVv2,   Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3,   Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3,   Tops_ABCD' + radi + '_t32,   Bottoms_ABCD' + radi + '_CSV,   Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ')',
                        
                        'ABCD_rate_systUp:=ABCD_syts( Zprimes_ABCD' +  radi + '_M,  Tprimes_ABCD' +  radi + '_M,  Tops_ABCD' +  radi + '_maxsubjetCSVv2,  Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3,  Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3,  Tops_ABCD' +  radi + '_t32,  Bottoms_ABCD' +  radi + '_CSV,  Ws_ABCD' +  radi + '_t21,  Ws_ABCD' + radi + '_Pt,  Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt,  Evt_HT_Jets,  N_Zprime_ABCD' + radi + ',  N_Jets,  N_packedPatJetsAK8PF' +  radi + ')[0]',
                        'ABCD_rate_systDown:=ABCD_syts( Zprimes_ABCD' +  radi + '_M,  Tprimes_ABCD' +  radi + '_M,  Tops_ABCD' +  radi + '_maxsubjetCSVv2,  Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3,  Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3,  Tops_ABCD' +  radi + '_t32,  Bottoms_ABCD' +  radi + '_CSV,  Ws_ABCD' +  radi + '_t21,  Ws_ABCD' + radi + '_Pt,  Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt,  Evt_HT_Jets,  N_Zprime_ABCD' + radi + ',  N_Jets,  N_packedPatJetsAK8PF' +  radi + ')[1]',
                        
                        'ABCD_shape_systUp:=ABCD_syts( Zprimes_ABCD' +  radi + '_M,  Tprimes_ABCD' +  radi + '_M,  Tops_ABCD' +  radi + '_maxsubjetCSVv2,  Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3,  Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3,  Tops_ABCD' +  radi + '_t32,  Bottoms_ABCD' +  radi + '_CSV,  Ws_ABCD' +  radi + '_t21,  Ws_ABCD' + radi + '_Pt,  Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt,  Evt_HT_Jets,  N_Zprime_ABCD' + radi + ',  N_Jets,  N_packedPatJetsAK8PF' +  radi + ')[2]',
                        'ABCD_shape_systDown:=ABCD_syts( Zprimes_ABCD' +  radi + '_M,  Tprimes_ABCD' +  radi + '_M,  Tops_ABCD' +  radi + '_maxsubjetCSVv2,  Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3,  Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3,  Tops_ABCD' +  radi + '_t32,  Bottoms_ABCD' +  radi + '_CSV,  Ws_ABCD' +  radi + '_t21,  Ws_ABCD' + radi + '_Pt,  Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt,  Evt_HT_Jets,  N_Zprime_ABCD' + radi + ',  N_Jets,  N_packedPatJetsAK8PF' +  radi + ')[3]',                         
                        
                        'ABCD_CatA_withtopbtag:=1',
                        'ABCD_CatB_withtopbtag:=2',
                        'ABCD_CatC_withtopbtag:=3',
                        'ABCD_CatD_withtopbtag:=4',
                        'ABCD_CatE_withtopbtag:=5',
                        'ABCD_CatF_withtopbtag:=6',
                        'ABCD_CatG_withtopbtag:=7',
                        'ABCD_CatH_withtopbtag:=8',
                        
                        'ABCD_CatA_notopbtag:=9',
                        'ABCD_CatB_notopbtag:=10',
                        'ABCD_CatC_notopbtag:=11',
                        'ABCD_CatD_notopbtag:=12',
                        'ABCD_CatE_notopbtag:=13',
                        'ABCD_CatF_notopbtag:=14',
                        'ABCD_CatG_notopbtag:=15',
                        'ABCD_CatH_notopbtag:=16',
                        
                        
             

                        '' + ABCDversion + '_WeightCSVnominal:=(CSV_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ',Bottoms_ABCD' + radi + '_WeightCSVnominal, Bottoms_ABCD' + radi + '_WeightCSVLFup, Bottoms_ABCD' + radi + '_WeightCSVLFdown, Bottoms_ABCD' + radi + '_WeightCSVHFup, Bottoms_ABCD' + radi + '_WeightCSVHFdown, Bottoms_ABCD' + radi + '_WeightCSVHFStats1up, Bottoms_ABCD' + radi + '_WeightCSVHFStats1down, Bottoms_ABCD' + radi + '_WeightCSVLFStats1up, Bottoms_ABCD' + radi + '_WeightCSVLFStats1down, Bottoms_ABCD' + radi + '_WeightCSVHFStats2up, Bottoms_ABCD' + radi + '_WeightCSVHFStats2down, Bottoms_ABCD' + radi + '_WeightCSVLFStats2up, Bottoms_ABCD' + radi + '_WeightCSVLFStats2down, Bottoms_ABCD' + radi + '_WeightCSVCErr1up, Bottoms_ABCD' + radi + '_WeightCSVCErr1down, Bottoms_ABCD' + radi + '_WeightCSVCErr2up, Bottoms_ABCD' + radi + '_WeightCSVCErr2down, Topsubjets_ABCD' + radi + '_WeightCSVnominal, Topsubjets_ABCD' + radi + '_WeightCSVLFup, Topsubjets_ABCD' + radi + '_WeightCSVLFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFup, Topsubjets_ABCD' + radi + '_WeightCSVHFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVCErr1up, Topsubjets_ABCD' + radi + '_WeightCSVCErr1down, Topsubjets_ABCD' + radi + '_WeightCSVCErr2up, Topsubjets_ABCD' + radi + '_WeightCSVCErr2down  ))[0]',

                        '' + ABCDversion + '_WeightCSVLFUp:=(CSV_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ',Bottoms_ABCD' + radi + '_WeightCSVnominal, Bottoms_ABCD' + radi + '_WeightCSVLFup, Bottoms_ABCD' + radi + '_WeightCSVLFdown, Bottoms_ABCD' + radi + '_WeightCSVHFup, Bottoms_ABCD' + radi + '_WeightCSVHFdown, Bottoms_ABCD' + radi + '_WeightCSVHFStats1up, Bottoms_ABCD' + radi + '_WeightCSVHFStats1down, Bottoms_ABCD' + radi + '_WeightCSVLFStats1up, Bottoms_ABCD' + radi + '_WeightCSVLFStats1down, Bottoms_ABCD' + radi + '_WeightCSVHFStats2up, Bottoms_ABCD' + radi + '_WeightCSVHFStats2down, Bottoms_ABCD' + radi + '_WeightCSVLFStats2up, Bottoms_ABCD' + radi + '_WeightCSVLFStats2down, Bottoms_ABCD' + radi + '_WeightCSVCErr1up, Bottoms_ABCD' + radi + '_WeightCSVCErr1down, Bottoms_ABCD' + radi + '_WeightCSVCErr2up, Bottoms_ABCD' + radi + '_WeightCSVCErr2down, Topsubjets_ABCD' + radi + '_WeightCSVnominal, Topsubjets_ABCD' + radi + '_WeightCSVLFup, Topsubjets_ABCD' + radi + '_WeightCSVLFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFup, Topsubjets_ABCD' + radi + '_WeightCSVHFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVCErr1up, Topsubjets_ABCD' + radi + '_WeightCSVCErr1down, Topsubjets_ABCD' + radi + '_WeightCSVCErr2up, Topsubjets_ABCD' + radi + '_WeightCSVCErr2down  ))[1]',
                        '' + ABCDversion + '_WeightCSVLFDown:=(CSV_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ',Bottoms_ABCD' + radi + '_WeightCSVnominal, Bottoms_ABCD' + radi + '_WeightCSVLFup, Bottoms_ABCD' + radi + '_WeightCSVLFdown, Bottoms_ABCD' + radi + '_WeightCSVHFup, Bottoms_ABCD' + radi + '_WeightCSVHFdown, Bottoms_ABCD' + radi + '_WeightCSVHFStats1up, Bottoms_ABCD' + radi + '_WeightCSVHFStats1down, Bottoms_ABCD' + radi + '_WeightCSVLFStats1up, Bottoms_ABCD' + radi + '_WeightCSVLFStats1down, Bottoms_ABCD' + radi + '_WeightCSVHFStats2up, Bottoms_ABCD' + radi + '_WeightCSVHFStats2down, Bottoms_ABCD' + radi + '_WeightCSVLFStats2up, Bottoms_ABCD' + radi + '_WeightCSVLFStats2down, Bottoms_ABCD' + radi + '_WeightCSVCErr1up, Bottoms_ABCD' + radi + '_WeightCSVCErr1down, Bottoms_ABCD' + radi + '_WeightCSVCErr2up, Bottoms_ABCD' + radi + '_WeightCSVCErr2down, Topsubjets_ABCD' + radi + '_WeightCSVnominal, Topsubjets_ABCD' + radi + '_WeightCSVLFup, Topsubjets_ABCD' + radi + '_WeightCSVLFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFup, Topsubjets_ABCD' + radi + '_WeightCSVHFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVCErr1up, Topsubjets_ABCD' + radi + '_WeightCSVCErr1down, Topsubjets_ABCD' + radi + '_WeightCSVCErr2up, Topsubjets_ABCD' + radi + '_WeightCSVCErr2down  ))[2]',
                        '' + ABCDversion + '_WeightCSVHFUp:=(CSV_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ',Bottoms_ABCD' + radi + '_WeightCSVnominal, Bottoms_ABCD' + radi + '_WeightCSVLFup, Bottoms_ABCD' + radi + '_WeightCSVLFdown, Bottoms_ABCD' + radi + '_WeightCSVHFup, Bottoms_ABCD' + radi + '_WeightCSVHFdown, Bottoms_ABCD' + radi + '_WeightCSVHFStats1up, Bottoms_ABCD' + radi + '_WeightCSVHFStats1down, Bottoms_ABCD' + radi + '_WeightCSVLFStats1up, Bottoms_ABCD' + radi + '_WeightCSVLFStats1down, Bottoms_ABCD' + radi + '_WeightCSVHFStats2up, Bottoms_ABCD' + radi + '_WeightCSVHFStats2down, Bottoms_ABCD' + radi + '_WeightCSVLFStats2up, Bottoms_ABCD' + radi + '_WeightCSVLFStats2down, Bottoms_ABCD' + radi + '_WeightCSVCErr1up, Bottoms_ABCD' + radi + '_WeightCSVCErr1down, Bottoms_ABCD' + radi + '_WeightCSVCErr2up, Bottoms_ABCD' + radi + '_WeightCSVCErr2down, Topsubjets_ABCD' + radi + '_WeightCSVnominal, Topsubjets_ABCD' + radi + '_WeightCSVLFup, Topsubjets_ABCD' + radi + '_WeightCSVLFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFup, Topsubjets_ABCD' + radi + '_WeightCSVHFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVCErr1up, Topsubjets_ABCD' + radi + '_WeightCSVCErr1down, Topsubjets_ABCD' + radi + '_WeightCSVCErr2up, Topsubjets_ABCD' + radi + '_WeightCSVCErr2down  ))[3]',
                        '' + ABCDversion + '_WeightCSVHFDown:=(CSV_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ',Bottoms_ABCD' + radi + '_WeightCSVnominal, Bottoms_ABCD' + radi + '_WeightCSVLFup, Bottoms_ABCD' + radi + '_WeightCSVLFdown, Bottoms_ABCD' + radi + '_WeightCSVHFup, Bottoms_ABCD' + radi + '_WeightCSVHFdown, Bottoms_ABCD' + radi + '_WeightCSVHFStats1up, Bottoms_ABCD' + radi + '_WeightCSVHFStats1down, Bottoms_ABCD' + radi + '_WeightCSVLFStats1up, Bottoms_ABCD' + radi + '_WeightCSVLFStats1down, Bottoms_ABCD' + radi + '_WeightCSVHFStats2up, Bottoms_ABCD' + radi + '_WeightCSVHFStats2down, Bottoms_ABCD' + radi + '_WeightCSVLFStats2up, Bottoms_ABCD' + radi + '_WeightCSVLFStats2down, Bottoms_ABCD' + radi + '_WeightCSVCErr1up, Bottoms_ABCD' + radi + '_WeightCSVCErr1down, Bottoms_ABCD' + radi + '_WeightCSVCErr2up, Bottoms_ABCD' + radi + '_WeightCSVCErr2down, Topsubjets_ABCD' + radi + '_WeightCSVnominal, Topsubjets_ABCD' + radi + '_WeightCSVLFup, Topsubjets_ABCD' + radi + '_WeightCSVLFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFup, Topsubjets_ABCD' + radi + '_WeightCSVHFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVCErr1up, Topsubjets_ABCD' + radi + '_WeightCSVCErr1down, Topsubjets_ABCD' + radi + '_WeightCSVCErr2up, Topsubjets_ABCD' + radi + '_WeightCSVCErr2down  ))[4]',
                        '' + ABCDversion + '_WeightCSVHFStats1Up:=(CSV_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ',Bottoms_ABCD' + radi + '_WeightCSVnominal, Bottoms_ABCD' + radi + '_WeightCSVLFup, Bottoms_ABCD' + radi + '_WeightCSVLFdown, Bottoms_ABCD' + radi + '_WeightCSVHFup, Bottoms_ABCD' + radi + '_WeightCSVHFdown, Bottoms_ABCD' + radi + '_WeightCSVHFStats1up, Bottoms_ABCD' + radi + '_WeightCSVHFStats1down, Bottoms_ABCD' + radi + '_WeightCSVLFStats1up, Bottoms_ABCD' + radi + '_WeightCSVLFStats1down, Bottoms_ABCD' + radi + '_WeightCSVHFStats2up, Bottoms_ABCD' + radi + '_WeightCSVHFStats2down, Bottoms_ABCD' + radi + '_WeightCSVLFStats2up, Bottoms_ABCD' + radi + '_WeightCSVLFStats2down, Bottoms_ABCD' + radi + '_WeightCSVCErr1up, Bottoms_ABCD' + radi + '_WeightCSVCErr1down, Bottoms_ABCD' + radi + '_WeightCSVCErr2up, Bottoms_ABCD' + radi + '_WeightCSVCErr2down, Topsubjets_ABCD' + radi + '_WeightCSVnominal, Topsubjets_ABCD' + radi + '_WeightCSVLFup, Topsubjets_ABCD' + radi + '_WeightCSVLFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFup, Topsubjets_ABCD' + radi + '_WeightCSVHFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVCErr1up, Topsubjets_ABCD' + radi + '_WeightCSVCErr1down, Topsubjets_ABCD' + radi + '_WeightCSVCErr2up, Topsubjets_ABCD' + radi + '_WeightCSVCErr2down  ))[5]',
                        '' + ABCDversion + '_WeightCSVHFStats1Down:=(CSV_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ',Bottoms_ABCD' + radi + '_WeightCSVnominal, Bottoms_ABCD' + radi + '_WeightCSVLFup, Bottoms_ABCD' + radi + '_WeightCSVLFdown, Bottoms_ABCD' + radi + '_WeightCSVHFup, Bottoms_ABCD' + radi + '_WeightCSVHFdown, Bottoms_ABCD' + radi + '_WeightCSVHFStats1up, Bottoms_ABCD' + radi + '_WeightCSVHFStats1down, Bottoms_ABCD' + radi + '_WeightCSVLFStats1up, Bottoms_ABCD' + radi + '_WeightCSVLFStats1down, Bottoms_ABCD' + radi + '_WeightCSVHFStats2up, Bottoms_ABCD' + radi + '_WeightCSVHFStats2down, Bottoms_ABCD' + radi + '_WeightCSVLFStats2up, Bottoms_ABCD' + radi + '_WeightCSVLFStats2down, Bottoms_ABCD' + radi + '_WeightCSVCErr1up, Bottoms_ABCD' + radi + '_WeightCSVCErr1down, Bottoms_ABCD' + radi + '_WeightCSVCErr2up, Bottoms_ABCD' + radi + '_WeightCSVCErr2down, Topsubjets_ABCD' + radi + '_WeightCSVnominal, Topsubjets_ABCD' + radi + '_WeightCSVLFup, Topsubjets_ABCD' + radi + '_WeightCSVLFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFup, Topsubjets_ABCD' + radi + '_WeightCSVHFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVCErr1up, Topsubjets_ABCD' + radi + '_WeightCSVCErr1down, Topsubjets_ABCD' + radi + '_WeightCSVCErr2up, Topsubjets_ABCD' + radi + '_WeightCSVCErr2down  ))[6]',
                        '' + ABCDversion + '_WeightCSVLFStats1Up:=(CSV_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ',Bottoms_ABCD' + radi + '_WeightCSVnominal, Bottoms_ABCD' + radi + '_WeightCSVLFup, Bottoms_ABCD' + radi + '_WeightCSVLFdown, Bottoms_ABCD' + radi + '_WeightCSVHFup, Bottoms_ABCD' + radi + '_WeightCSVHFdown, Bottoms_ABCD' + radi + '_WeightCSVHFStats1up, Bottoms_ABCD' + radi + '_WeightCSVHFStats1down, Bottoms_ABCD' + radi + '_WeightCSVLFStats1up, Bottoms_ABCD' + radi + '_WeightCSVLFStats1down, Bottoms_ABCD' + radi + '_WeightCSVHFStats2up, Bottoms_ABCD' + radi + '_WeightCSVHFStats2down, Bottoms_ABCD' + radi + '_WeightCSVLFStats2up, Bottoms_ABCD' + radi + '_WeightCSVLFStats2down, Bottoms_ABCD' + radi + '_WeightCSVCErr1up, Bottoms_ABCD' + radi + '_WeightCSVCErr1down, Bottoms_ABCD' + radi + '_WeightCSVCErr2up, Bottoms_ABCD' + radi + '_WeightCSVCErr2down, Topsubjets_ABCD' + radi + '_WeightCSVnominal, Topsubjets_ABCD' + radi + '_WeightCSVLFup, Topsubjets_ABCD' + radi + '_WeightCSVLFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFup, Topsubjets_ABCD' + radi + '_WeightCSVHFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVCErr1up, Topsubjets_ABCD' + radi + '_WeightCSVCErr1down, Topsubjets_ABCD' + radi + '_WeightCSVCErr2up, Topsubjets_ABCD' + radi + '_WeightCSVCErr2down  ))[7]',
                        '' + ABCDversion + '_WeightCSVLFStats1Down:=(CSV_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ',Bottoms_ABCD' + radi + '_WeightCSVnominal, Bottoms_ABCD' + radi + '_WeightCSVLFup, Bottoms_ABCD' + radi + '_WeightCSVLFdown, Bottoms_ABCD' + radi + '_WeightCSVHFup, Bottoms_ABCD' + radi + '_WeightCSVHFdown, Bottoms_ABCD' + radi + '_WeightCSVHFStats1up, Bottoms_ABCD' + radi + '_WeightCSVHFStats1down, Bottoms_ABCD' + radi + '_WeightCSVLFStats1up, Bottoms_ABCD' + radi + '_WeightCSVLFStats1down, Bottoms_ABCD' + radi + '_WeightCSVHFStats2up, Bottoms_ABCD' + radi + '_WeightCSVHFStats2down, Bottoms_ABCD' + radi + '_WeightCSVLFStats2up, Bottoms_ABCD' + radi + '_WeightCSVLFStats2down, Bottoms_ABCD' + radi + '_WeightCSVCErr1up, Bottoms_ABCD' + radi + '_WeightCSVCErr1down, Bottoms_ABCD' + radi + '_WeightCSVCErr2up, Bottoms_ABCD' + radi + '_WeightCSVCErr2down, Topsubjets_ABCD' + radi + '_WeightCSVnominal, Topsubjets_ABCD' + radi + '_WeightCSVLFup, Topsubjets_ABCD' + radi + '_WeightCSVLFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFup, Topsubjets_ABCD' + radi + '_WeightCSVHFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVCErr1up, Topsubjets_ABCD' + radi + '_WeightCSVCErr1down, Topsubjets_ABCD' + radi + '_WeightCSVCErr2up, Topsubjets_ABCD' + radi + '_WeightCSVCErr2down  ))[8]',
                        '' + ABCDversion + '_WeightCSVHFStats2Up:=(CSV_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ',Bottoms_ABCD' + radi + '_WeightCSVnominal, Bottoms_ABCD' + radi + '_WeightCSVLFup, Bottoms_ABCD' + radi + '_WeightCSVLFdown, Bottoms_ABCD' + radi + '_WeightCSVHFup, Bottoms_ABCD' + radi + '_WeightCSVHFdown, Bottoms_ABCD' + radi + '_WeightCSVHFStats1up, Bottoms_ABCD' + radi + '_WeightCSVHFStats1down, Bottoms_ABCD' + radi + '_WeightCSVLFStats1up, Bottoms_ABCD' + radi + '_WeightCSVLFStats1down, Bottoms_ABCD' + radi + '_WeightCSVHFStats2up, Bottoms_ABCD' + radi + '_WeightCSVHFStats2down, Bottoms_ABCD' + radi + '_WeightCSVLFStats2up, Bottoms_ABCD' + radi + '_WeightCSVLFStats2down, Bottoms_ABCD' + radi + '_WeightCSVCErr1up, Bottoms_ABCD' + radi + '_WeightCSVCErr1down, Bottoms_ABCD' + radi + '_WeightCSVCErr2up, Bottoms_ABCD' + radi + '_WeightCSVCErr2down, Topsubjets_ABCD' + radi + '_WeightCSVnominal, Topsubjets_ABCD' + radi + '_WeightCSVLFup, Topsubjets_ABCD' + radi + '_WeightCSVLFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFup, Topsubjets_ABCD' + radi + '_WeightCSVHFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVCErr1up, Topsubjets_ABCD' + radi + '_WeightCSVCErr1down, Topsubjets_ABCD' + radi + '_WeightCSVCErr2up, Topsubjets_ABCD' + radi + '_WeightCSVCErr2down  ))[9]',
                        '' + ABCDversion + '_WeightCSVHFStats2Down:=(CSV_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ',Bottoms_ABCD' + radi + '_WeightCSVnominal, Bottoms_ABCD' + radi + '_WeightCSVLFup, Bottoms_ABCD' + radi + '_WeightCSVLFdown, Bottoms_ABCD' + radi + '_WeightCSVHFup, Bottoms_ABCD' + radi + '_WeightCSVHFdown, Bottoms_ABCD' + radi + '_WeightCSVHFStats1up, Bottoms_ABCD' + radi + '_WeightCSVHFStats1down, Bottoms_ABCD' + radi + '_WeightCSVLFStats1up, Bottoms_ABCD' + radi + '_WeightCSVLFStats1down, Bottoms_ABCD' + radi + '_WeightCSVHFStats2up, Bottoms_ABCD' + radi + '_WeightCSVHFStats2down, Bottoms_ABCD' + radi + '_WeightCSVLFStats2up, Bottoms_ABCD' + radi + '_WeightCSVLFStats2down, Bottoms_ABCD' + radi + '_WeightCSVCErr1up, Bottoms_ABCD' + radi + '_WeightCSVCErr1down, Bottoms_ABCD' + radi + '_WeightCSVCErr2up, Bottoms_ABCD' + radi + '_WeightCSVCErr2down, Topsubjets_ABCD' + radi + '_WeightCSVnominal, Topsubjets_ABCD' + radi + '_WeightCSVLFup, Topsubjets_ABCD' + radi + '_WeightCSVLFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFup, Topsubjets_ABCD' + radi + '_WeightCSVHFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVCErr1up, Topsubjets_ABCD' + radi + '_WeightCSVCErr1down, Topsubjets_ABCD' + radi + '_WeightCSVCErr2up, Topsubjets_ABCD' + radi + '_WeightCSVCErr2down  ))[10]',
                        '' + ABCDversion + '_WeightCSVLFStats2Up:=(CSV_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ',Bottoms_ABCD' + radi + '_WeightCSVnominal, Bottoms_ABCD' + radi + '_WeightCSVLFup, Bottoms_ABCD' + radi + '_WeightCSVLFdown, Bottoms_ABCD' + radi + '_WeightCSVHFup, Bottoms_ABCD' + radi + '_WeightCSVHFdown, Bottoms_ABCD' + radi + '_WeightCSVHFStats1up, Bottoms_ABCD' + radi + '_WeightCSVHFStats1down, Bottoms_ABCD' + radi + '_WeightCSVLFStats1up, Bottoms_ABCD' + radi + '_WeightCSVLFStats1down, Bottoms_ABCD' + radi + '_WeightCSVHFStats2up, Bottoms_ABCD' + radi + '_WeightCSVHFStats2down, Bottoms_ABCD' + radi + '_WeightCSVLFStats2up, Bottoms_ABCD' + radi + '_WeightCSVLFStats2down, Bottoms_ABCD' + radi + '_WeightCSVCErr1up, Bottoms_ABCD' + radi + '_WeightCSVCErr1down, Bottoms_ABCD' + radi + '_WeightCSVCErr2up, Bottoms_ABCD' + radi + '_WeightCSVCErr2down, Topsubjets_ABCD' + radi + '_WeightCSVnominal, Topsubjets_ABCD' + radi + '_WeightCSVLFup, Topsubjets_ABCD' + radi + '_WeightCSVLFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFup, Topsubjets_ABCD' + radi + '_WeightCSVHFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVCErr1up, Topsubjets_ABCD' + radi + '_WeightCSVCErr1down, Topsubjets_ABCD' + radi + '_WeightCSVCErr2up, Topsubjets_ABCD' + radi + '_WeightCSVCErr2down  ))[11]',
                        '' + ABCDversion + '_WeightCSVLFStats2Down:=(CSV_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ',Bottoms_ABCD' + radi + '_WeightCSVnominal, Bottoms_ABCD' + radi + '_WeightCSVLFup, Bottoms_ABCD' + radi + '_WeightCSVLFdown, Bottoms_ABCD' + radi + '_WeightCSVHFup, Bottoms_ABCD' + radi + '_WeightCSVHFdown, Bottoms_ABCD' + radi + '_WeightCSVHFStats1up, Bottoms_ABCD' + radi + '_WeightCSVHFStats1down, Bottoms_ABCD' + radi + '_WeightCSVLFStats1up, Bottoms_ABCD' + radi + '_WeightCSVLFStats1down, Bottoms_ABCD' + radi + '_WeightCSVHFStats2up, Bottoms_ABCD' + radi + '_WeightCSVHFStats2down, Bottoms_ABCD' + radi + '_WeightCSVLFStats2up, Bottoms_ABCD' + radi + '_WeightCSVLFStats2down, Bottoms_ABCD' + radi + '_WeightCSVCErr1up, Bottoms_ABCD' + radi + '_WeightCSVCErr1down, Bottoms_ABCD' + radi + '_WeightCSVCErr2up, Bottoms_ABCD' + radi + '_WeightCSVCErr2down, Topsubjets_ABCD' + radi + '_WeightCSVnominal, Topsubjets_ABCD' + radi + '_WeightCSVLFup, Topsubjets_ABCD' + radi + '_WeightCSVLFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFup, Topsubjets_ABCD' + radi + '_WeightCSVHFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVCErr1up, Topsubjets_ABCD' + radi + '_WeightCSVCErr1down, Topsubjets_ABCD' + radi + '_WeightCSVCErr2up, Topsubjets_ABCD' + radi + '_WeightCSVCErr2down  ))[12]',
                        '' + ABCDversion + '_WeightCSVCErr1Up:=(CSV_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ',Bottoms_ABCD' + radi + '_WeightCSVnominal, Bottoms_ABCD' + radi + '_WeightCSVLFup, Bottoms_ABCD' + radi + '_WeightCSVLFdown, Bottoms_ABCD' + radi + '_WeightCSVHFup, Bottoms_ABCD' + radi + '_WeightCSVHFdown, Bottoms_ABCD' + radi + '_WeightCSVHFStats1up, Bottoms_ABCD' + radi + '_WeightCSVHFStats1down, Bottoms_ABCD' + radi + '_WeightCSVLFStats1up, Bottoms_ABCD' + radi + '_WeightCSVLFStats1down, Bottoms_ABCD' + radi + '_WeightCSVHFStats2up, Bottoms_ABCD' + radi + '_WeightCSVHFStats2down, Bottoms_ABCD' + radi + '_WeightCSVLFStats2up, Bottoms_ABCD' + radi + '_WeightCSVLFStats2down, Bottoms_ABCD' + radi + '_WeightCSVCErr1up, Bottoms_ABCD' + radi + '_WeightCSVCErr1down, Bottoms_ABCD' + radi + '_WeightCSVCErr2up, Bottoms_ABCD' + radi + '_WeightCSVCErr2down, Topsubjets_ABCD' + radi + '_WeightCSVnominal, Topsubjets_ABCD' + radi + '_WeightCSVLFup, Topsubjets_ABCD' + radi + '_WeightCSVLFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFup, Topsubjets_ABCD' + radi + '_WeightCSVHFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVCErr1up, Topsubjets_ABCD' + radi + '_WeightCSVCErr1down, Topsubjets_ABCD' + radi + '_WeightCSVCErr2up, Topsubjets_ABCD' + radi + '_WeightCSVCErr2down  ))[13]',
                        '' + ABCDversion + '_WeightCSVCErr1Down:=(CSV_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ',Bottoms_ABCD' + radi + '_WeightCSVnominal, Bottoms_ABCD' + radi + '_WeightCSVLFup, Bottoms_ABCD' + radi + '_WeightCSVLFdown, Bottoms_ABCD' + radi + '_WeightCSVHFup, Bottoms_ABCD' + radi + '_WeightCSVHFdown, Bottoms_ABCD' + radi + '_WeightCSVHFStats1up, Bottoms_ABCD' + radi + '_WeightCSVHFStats1down, Bottoms_ABCD' + radi + '_WeightCSVLFStats1up, Bottoms_ABCD' + radi + '_WeightCSVLFStats1down, Bottoms_ABCD' + radi + '_WeightCSVHFStats2up, Bottoms_ABCD' + radi + '_WeightCSVHFStats2down, Bottoms_ABCD' + radi + '_WeightCSVLFStats2up, Bottoms_ABCD' + radi + '_WeightCSVLFStats2down, Bottoms_ABCD' + radi + '_WeightCSVCErr1up, Bottoms_ABCD' + radi + '_WeightCSVCErr1down, Bottoms_ABCD' + radi + '_WeightCSVCErr2up, Bottoms_ABCD' + radi + '_WeightCSVCErr2down, Topsubjets_ABCD' + radi + '_WeightCSVnominal, Topsubjets_ABCD' + radi + '_WeightCSVLFup, Topsubjets_ABCD' + radi + '_WeightCSVLFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFup, Topsubjets_ABCD' + radi + '_WeightCSVHFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVCErr1up, Topsubjets_ABCD' + radi + '_WeightCSVCErr1down, Topsubjets_ABCD' + radi + '_WeightCSVCErr2up, Topsubjets_ABCD' + radi + '_WeightCSVCErr2down  ))[14]',
                        '' + ABCDversion + '_WeightCSVCErr2Up:=(CSV_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ',Bottoms_ABCD' + radi + '_WeightCSVnominal, Bottoms_ABCD' + radi + '_WeightCSVLFup, Bottoms_ABCD' + radi + '_WeightCSVLFdown, Bottoms_ABCD' + radi + '_WeightCSVHFup, Bottoms_ABCD' + radi + '_WeightCSVHFdown, Bottoms_ABCD' + radi + '_WeightCSVHFStats1up, Bottoms_ABCD' + radi + '_WeightCSVHFStats1down, Bottoms_ABCD' + radi + '_WeightCSVLFStats1up, Bottoms_ABCD' + radi + '_WeightCSVLFStats1down, Bottoms_ABCD' + radi + '_WeightCSVHFStats2up, Bottoms_ABCD' + radi + '_WeightCSVHFStats2down, Bottoms_ABCD' + radi + '_WeightCSVLFStats2up, Bottoms_ABCD' + radi + '_WeightCSVLFStats2down, Bottoms_ABCD' + radi + '_WeightCSVCErr1up, Bottoms_ABCD' + radi + '_WeightCSVCErr1down, Bottoms_ABCD' + radi + '_WeightCSVCErr2up, Bottoms_ABCD' + radi + '_WeightCSVCErr2down, Topsubjets_ABCD' + radi + '_WeightCSVnominal, Topsubjets_ABCD' + radi + '_WeightCSVLFup, Topsubjets_ABCD' + radi + '_WeightCSVLFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFup, Topsubjets_ABCD' + radi + '_WeightCSVHFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVCErr1up, Topsubjets_ABCD' + radi + '_WeightCSVCErr1down, Topsubjets_ABCD' + radi + '_WeightCSVCErr2up, Topsubjets_ABCD' + radi + '_WeightCSVCErr2down  ))[15]',
                        '' + ABCDversion + '_WeightCSVCErr2Down:=(CSV_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ',Bottoms_ABCD' + radi + '_WeightCSVnominal, Bottoms_ABCD' + radi + '_WeightCSVLFup, Bottoms_ABCD' + radi + '_WeightCSVLFdown, Bottoms_ABCD' + radi + '_WeightCSVHFup, Bottoms_ABCD' + radi + '_WeightCSVHFdown, Bottoms_ABCD' + radi + '_WeightCSVHFStats1up, Bottoms_ABCD' + radi + '_WeightCSVHFStats1down, Bottoms_ABCD' + radi + '_WeightCSVLFStats1up, Bottoms_ABCD' + radi + '_WeightCSVLFStats1down, Bottoms_ABCD' + radi + '_WeightCSVHFStats2up, Bottoms_ABCD' + radi + '_WeightCSVHFStats2down, Bottoms_ABCD' + radi + '_WeightCSVLFStats2up, Bottoms_ABCD' + radi + '_WeightCSVLFStats2down, Bottoms_ABCD' + radi + '_WeightCSVCErr1up, Bottoms_ABCD' + radi + '_WeightCSVCErr1down, Bottoms_ABCD' + radi + '_WeightCSVCErr2up, Bottoms_ABCD' + radi + '_WeightCSVCErr2down, Topsubjets_ABCD' + radi + '_WeightCSVnominal, Topsubjets_ABCD' + radi + '_WeightCSVLFup, Topsubjets_ABCD' + radi + '_WeightCSVLFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFup, Topsubjets_ABCD' + radi + '_WeightCSVHFdown, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats1down, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVHFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2up, Topsubjets_ABCD' + radi + '_WeightCSVLFStats2down, Topsubjets_ABCD' + radi + '_WeightCSVCErr1up, Topsubjets_ABCD' + radi + '_WeightCSVCErr1down, Topsubjets_ABCD' + radi + '_WeightCSVCErr2up, Topsubjets_ABCD' + radi + '_WeightCSVCErr2down  ))[16]',
                        
                        #'ABCD1_Wtagweightnominal:=(Wtag_weights_ABCD' + radi + '1(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + '))[0]',
                        #'ABCD1_WtagweightUp:=(Wtag_weights_ABCD' + radi + '1(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + '))[1]',
                        #'ABCD1_WtagweightDown:=(Wtag_weights_ABCD' + radi + '1(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + '))[2]',
                        #'ABCD1_toptagweightnominal:=(toptag_weights_ABCD' + radi + '1(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + '))[0]',
                        #'ABCD1_toptagweightUp:=(toptag_weights_ABCD' + radi + '1(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + '))[1]',
                        #'ABCD1_toptagweightDown:=(toptag_weights_ABCD' + radi + '1(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + '))[2]',
 
                        #'ABCD2_Wtagweightnominal:=(Wtag_weights_ABCD' + radi + '2(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + '))[0]',
                        #'ABCD2_WtagweightUp:=(Wtag_weights_ABCD' + radi + '2(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + '))[1]',
                        #'ABCD2_WtagweightDown:=(Wtag_weights_ABCD' + radi + '2(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + '))[2]',
                        #'ABCD2_toptagweightnominal:=(toptag_weights_ABCD' + radi + '2(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + '))[0]',
                        #'ABCD2_toptagweightUp:=(toptag_weights_ABCD' + radi + '2(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + '))[1]',
                        #'ABCD2_toptagweightDown:=(toptag_weights_ABCD' + radi + '2(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + '))[2]',
                        
                        ABCDversion + '_Wtag_tag_t21_weightnominal:=(Wtag_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ', Ws_ABCD' + radi + '_real, Ws_ABCD' + radi + '_matcheddecays))[0]',
                        ABCDversion + '_Wtag_tag_t21_weightUp:=(Wtag_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ', Ws_ABCD' + radi + '_real, Ws_ABCD' + radi + '_matcheddecays))[1]',
                        ABCDversion + '_Wtag_tag_t21_weightDown:=(Wtag_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ', Ws_ABCD' + radi + '_real, Ws_ABCD' + radi + '_matcheddecays))[2]',
                        
                        #ABCDversion + '_Wtag_tag_t21anti_weightnominal:=(Wtag_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ', Ws_ABCD' + radi + '_real, Ws_ABCD' + radi + '_matcheddecays))[3]',
                        #ABCDversion + '_Wtag_tag_t21anti_weightUp:=(Wtag_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ', Ws_ABCD' + radi + '_real, Ws_ABCD' + radi + '_matcheddecays))[4]',
                        #ABCDversion + '_Wtag_tag_t21anti_weightDown:=(Wtag_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ', Ws_ABCD' + radi + '_real, Ws_ABCD' + radi + '_matcheddecays))[5]',
                                                
                        #ABCDversion + '_Wtag_mistag_t21_weightnominal:=(Wtag_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ', Ws_ABCD' + radi + '_real, Ws_ABCD' + radi + '_matcheddecays))[6]',
                        #ABCDversion + '_Wtag_mistag_t21_weightUp:=(Wtag_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ', Ws_ABCD' + radi + '_real, Ws_ABCD' + radi + '_matcheddecays))[7]',
                        #ABCDversion + '_Wtag_mistag_t21_weightDown:=(Wtag_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ', Ws_ABCD' + radi + '_real, Ws_ABCD' + radi + '_matcheddecays))[8]',
                                                
                        #ABCDversion + '_Wtag_mistag_t21anti_weightnominal:=(Wtag_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ', Ws_ABCD' + radi + '_real, Ws_ABCD' + radi + '_matcheddecays))[9]',
                        #ABCDversion + '_Wtag_mistag_t21anti_weightUp:=(Wtag_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ', Ws_ABCD' + radi + '_real, Ws_ABCD' + radi + '_matcheddecays))[10]',
                        #ABCDversion + '_Wtag_mistag_t21anti_weightDown:=(Wtag_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ', Ws_ABCD' + radi + '_real, Ws_ABCD' + radi + '_matcheddecays))[11]',
                        
                        
                        ABCDversion + '_toptagweightnominal:=(toptag_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ', Tops_ABCD' + radi + '_real, Tops_ABCD' + radi + '_matcheddecays))[0]',
                        ABCDversion + '_toptagweightUp:=(toptag_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ', Tops_ABCD' + radi + '_real, Tops_ABCD' + radi + '_matcheddecays))[1]',
                        ABCDversion + '_toptagweightDown:=(toptag_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ', Tops_ABCD' + radi + '_real, Tops_ABCD' + radi + '_matcheddecays))[2]',
                        ABCDversion + '_topmisstagweightnominal:=(toptag_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ', Tops_ABCD' + radi + '_real, Tops_ABCD' + radi + '_matcheddecays))[3]',
                        ABCDversion + '_topmisstagweightUp:=(toptag_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ', Tops_ABCD' + radi + '_real, Tops_ABCD' + radi + '_matcheddecays))[4]',
                        ABCDversion + '_topmisstagweightDown:=(toptag_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ', Tops_ABCD' + radi + '_real, Tops_ABCD' + radi + '_matcheddecays))[5]',
  
 
 
 
                        'MCSF_RenFac_envelopeUp:=(RenFacEnv(Weight_scale_variation_muR2p0_muF2p0, Weight_scale_variation_muR0p5_muF0p5, Weight_scale_variation_muR1p0_muF2p0 , Weight_scale_variation_muR1p0_muF0p5, Weight_scale_variation_muR2p0_muF1p0, Weight_scale_variation_muR0p5_muF1p0))[0]',
                        'MCSF_RenFac_envelopeDown:=(RenFacEnv(Weight_scale_variation_muR2p0_muF2p0, Weight_scale_variation_muR0p5_muF0p5, Weight_scale_variation_muR1p0_muF2p0 , Weight_scale_variation_muR1p0_muF0p5, Weight_scale_variation_muR2p0_muF1p0, Weight_scale_variation_muR0p5_muF1p0))[1]',
                                               #'N_Jets', 'Jet_Pt','Jet_Eta','Jet_CSV','Jet_Flav','Jet_M','Jet_Phi','Jet_E',
                        'PDF_RMSMean:=PDF_RMS('+ stringforPDFs1 +')[0]',
                        'PDF_RMSUp:=PDF_RMS('+ stringforPDFs1 +')[1]',
                        'PDF_RMSDown:=PDF_RMS('+ stringforPDFs1 +')[2]',
                        
                        #'MCSF_Weight_ABCD' + radi + '1:=ABCD1_toptagweightnominal*ABCD1_Wtagweightnominal*ABCD1_WeightCSVnominal*Weight_pu69p2*PDF_RMSMean',
                        #'MCSF_Weight_ABCD2:=ABCD2_toptagweightnominal*ABCD2_Wtagweightnominal*ABCD2_WeightCSVnominal*Weight_pu69p2*PDF_RMSMean',
                        'MCSF_Weight_' + ABCDversion + ':=' + ABCDversion + '_toptagweightnominal*' + ABCDversion + '_topmisstagweightnominal*' + ABCDversion + '_WeightCSVnominal*Weight_pu69p2*PDF_RMSMean*' + ABCDversion + '_Wtag_tag_t21_weightnominal*' + ABCDversion + '_Wtag_tag_t21anti_weightnominal*' + ABCDversion + '_Wtag_mistag_t21_weightnominal*' + ABCDversion + '_Wtag_mistag_t21anti_weightnominal' ,
                        
                        
                        'triggered:=triggerresult(Triggered_HLT_PFHT800_vX, Triggered_HLT_PFHT900_vX, Triggered_HLT_PFJet450_vX, Prescale_HLT_PFHT800_vX, Prescale_HLT_PFHT900_vX, Prescale_HLT_PFJet450_vX)',

]

