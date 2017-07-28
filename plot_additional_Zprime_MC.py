from plot_cuts_ZPrime_MC import *

stringforPDFs="float Weight_nnpdf30_lo_as_0130_0"
stringforPDFs1="Weight_nnpdf30_lo_as_0130_0"
stringforPDFs2="""
PDFweights.push_back(Weight_nnpdf30_lo_as_0130_0);
"""

for i in range(1,100):

    stringforPDFs=stringforPDFs+(", float Weight_nnpdf30_lo_as_0130_"+str(i))
    stringforPDFs1=stringforPDFs1+(", Weight_nnpdf30_lo_as_0130_"+str(i))
    stringforPDFs2=stringforPDFs2+("PDFweights.push_back(Weight_nnpdf30_lo_as_0130_"+str(i)+");")

#print stringforPDFs

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
""" ,
"""
int ABCD_Category(float const* Zprimes_ABCD_M, float const* Tprimes_ABCD_M, float const* Tops_ABCD_maxsubjetCSVv2, float const* Ws_ABCD_MSD, float const* Tops_ABCD_MSD, float const* Tops_ABCD_t32, float const* Bottoms_ABCD_CSV, float const* Ws_ABCD_t21,int N_Zprime_ABCD){
    int res=0;
    for (int i=0; i<N_Zprime_ABCD; i++){
        if ("""+ plotselection_ABCD_general_beta_i +"""){
            if("""+ plotselection_topsubjetCSVv2_i +"""){
                if("""+ plotselection_W_tau21_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_tau32_i + """){
                            res=1;
                            break;
                        }
                        if(""" + plotselection_tau32_anti_i + """){
                            res=2;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_tau32_i + """){
                            res=3;
                            break;
                        }
                        if(""" + plotselection_tau32_anti_i + """){
                            res=4;
                            break;
                        }
                    }                
                }
                if("""+ plotselection_W_tau21_anti_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_tau32_i + """){
                            res=5;
                            break;
                        }
                        if(""" + plotselection_tau32_anti_i + """){
                            res=6;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_tau32_i + """){
                            res=7;
                            break;
                        }
                        if(""" + plotselection_tau32_anti_i + """){
                            res=8;
                            break;
                        }
                    }                
                }
            } else {
                if("""+ plotselection_W_tau21_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_tau32_i + """){
                            res=9;
                            break;
                        }
                        if(""" + plotselection_tau32_anti_i + """){
                            res=10;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_tau32_i + """){
                            res=11;
                            break;
                        }
                        if(""" + plotselection_tau32_anti_i + """){
                            res=12;
                            break;
                        }
                    }                
                }
                if("""+ plotselection_W_tau21_anti_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_tau32_i + """){
                            res=13;
                            break;
                        }
                        if(""" + plotselection_tau32_anti_i + """){
                            res=14;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_tau32_i + """){
                            res=15;
                            break;
                        }
                        if(""" + plotselection_tau32_anti_i + """){
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
int ABCD2_Category(float const* Zprimes_ABCD_M, float const* Tprimes_ABCD_M, float const* Tops_ABCD_maxsubjetCSVv2, float const* Ws_ABCD_MSD, float const* Tops_ABCD_MSD, float const* Tops_ABCD_t32, float const* Bottoms_ABCD_CSV, float const* Ws_ABCD_t21,int N_Zprime_ABCD){
    int res=0;
    for (int i=0; i<N_Zprime_ABCD; i++){
        if ("""+ plotselection_ABCD_general_beta2_i +"""){
            if("""+ plotselection_topsubjetCSVv2_i +"""){
                if("""+ plotselection_W_tau21_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_t_MSD_i + """){
                            res=1;
                            break;
                        }
                        if(""" + plotselection_t_MSD_anti_i + """){
                            res=2;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_t_MSD_i + """){
                            res=3;
                            break;
                        }
                        if(""" + plotselection_t_MSD_anti_i + """){
                            res=4;
                            break;
                        }
                    }                
                }
                if("""+ plotselection_W_tau21_anti_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_t_MSD_i + """){
                            res=5;
                            break;
                        }
                        if(""" + plotselection_t_MSD_anti_i + """){
                            res=6;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_t_MSD_i + """){
                            res=7;
                            break;
                        }
                        if(""" + plotselection_t_MSD_anti_i + """){
                            res=8;
                            break;
                        }
                    }                
                }
            } else {
                if("""+ plotselection_W_tau21_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_t_MSD_i + """){
                            res=9;
                            break;
                        }
                        if(""" + plotselection_t_MSD_anti_i + """){
                            res=10;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_t_MSD_i + """){
                            res=11;
                            break;
                        }
                        if(""" + plotselection_t_MSD_anti_i + """){
                            res=12;
                            break;
                        }
                    }                
                }
                if("""+ plotselection_W_tau21_anti_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_t_MSD_i + """){
                            res=13;
                            break;
                        }
                        if(""" + plotselection_t_MSD_anti_i + """){
                            res=14;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_t_MSD_i + """){
                            res=15;
                            break;
                        }
                        if(""" + plotselection_t_MSD_anti_i + """){
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
std::vector<float> CSV_weights_ABCD1(float const* Zprimes_ABCD_M, float const* Tprimes_ABCD_M, float const* Tops_ABCD_maxsubjetCSVv2, float const* Ws_ABCD_MSD, float const* Tops_ABCD_MSD, float const* Tops_ABCD_t32, float const* Bottoms_ABCD_CSV, float const* Ws_ABCD_t21,int N_Zprime_ABCD, float const* Bottoms_ABCD_WeightCSVnominal, float const* Bottoms_ABCD_WeightCSVLFup, float const* Bottoms_ABCD_WeightCSVLFdown, float const* Bottoms_ABCD_WeightCSVHFup, float const* Bottoms_ABCD_WeightCSVHFdown, float const* Bottoms_ABCD_WeightCSVHFStats1up, float const* Bottoms_ABCD_WeightCSVHFStats1down, float const* Bottoms_ABCD_WeightCSVLFStats1up, float const* Bottoms_ABCD_WeightCSVLFStats1down, float const* Bottoms_ABCD_WeightCSVHFStats2up, float const* Bottoms_ABCD_WeightCSVHFStats2down, float const* Bottoms_ABCD_WeightCSVLFStats2up, float const* Bottoms_ABCD_WeightCSVLFStats2down, float const* Bottoms_ABCD_WeightCSVCErr1up, float const* Bottoms_ABCD_WeightCSVCErr1down, float const* Bottoms_ABCD_WeightCSVCErr2up, float const* Bottoms_ABCD_WeightCSVCErr2down){
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

    for (int i=0; i<N_Zprime_ABCD; i++){
        if ("""+ plotselection_ABCD_general_beta_i +"""){         
            CSVnominal *= Bottoms_ABCD_WeightCSVnominal[i];
            CSVLFup *= Bottoms_ABCD_WeightCSVLFup[i];
            CSVLFdown *= Bottoms_ABCD_WeightCSVLFdown[i];
            CSVHFup *= Bottoms_ABCD_WeightCSVHFup[i];
            CSVHFdown *= Bottoms_ABCD_WeightCSVHFdown[i];
            CSVHFStats1up *= Bottoms_ABCD_WeightCSVHFStats1up[i];
            CSVHFStats1down *= Bottoms_ABCD_WeightCSVHFStats1down[i];
            CSVLFStats1up *= Bottoms_ABCD_WeightCSVLFStats1up[i];
            CSVLFStats1down *= Bottoms_ABCD_WeightCSVLFStats1down[i];
            CSVHFStats2up *= Bottoms_ABCD_WeightCSVHFStats2up[i];
            CSVHFStats2down *= Bottoms_ABCD_WeightCSVHFStats2down[i];
            CSVLFStats2up *= Bottoms_ABCD_WeightCSVLFStats2up[i];
            CSVLFStats2down *= Bottoms_ABCD_WeightCSVLFStats2down[i];
            CSVCErr1down *= Bottoms_ABCD_WeightCSVCErr1up[i];
            CSVCErr1down *= Bottoms_ABCD_WeightCSVCErr1down[i];
            CSVCErr2up *= Bottoms_ABCD_WeightCSVCErr2up[i];
            CSVCErr2down *= Bottoms_ABCD_WeightCSVCErr2down[i];
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
std::vector<float> CSV_weights_ABCD2(float const* Zprimes_ABCD_M, float const* Tprimes_ABCD_M, float const* Tops_ABCD_maxsubjetCSVv2, float const* Ws_ABCD_MSD, float const* Tops_ABCD_MSD, float const* Tops_ABCD_t32, float const* Bottoms_ABCD_CSV, float const* Ws_ABCD_t21,int N_Zprime_ABCD, float const* Bottoms_ABCD_WeightCSVnominal, float const* Bottoms_ABCD_WeightCSVLFup, float const* Bottoms_ABCD_WeightCSVLFdown, float const* Bottoms_ABCD_WeightCSVHFup, float const* Bottoms_ABCD_WeightCSVHFdown, float const* Bottoms_ABCD_WeightCSVHFStats1up, float const* Bottoms_ABCD_WeightCSVHFStats1down, float const* Bottoms_ABCD_WeightCSVLFStats1up, float const* Bottoms_ABCD_WeightCSVLFStats1down, float const* Bottoms_ABCD_WeightCSVHFStats2up, float const* Bottoms_ABCD_WeightCSVHFStats2down, float const* Bottoms_ABCD_WeightCSVLFStats2up, float const* Bottoms_ABCD_WeightCSVLFStats2down, float const* Bottoms_ABCD_WeightCSVCErr1up, float const* Bottoms_ABCD_WeightCSVCErr1down, float const* Bottoms_ABCD_WeightCSVCErr2up, float const* Bottoms_ABCD_WeightCSVCErr2down){
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

    for (int i=0; i<N_Zprime_ABCD; i++){
        if ("""+ plotselection_ABCD_general_beta2_i +"""){         
            CSVnominal *= Bottoms_ABCD_WeightCSVnominal[i];
            CSVLFup *= Bottoms_ABCD_WeightCSVLFup[i];
            CSVLFdown *= Bottoms_ABCD_WeightCSVLFdown[i];
            CSVHFup *= Bottoms_ABCD_WeightCSVHFup[i];
            CSVHFdown *= Bottoms_ABCD_WeightCSVHFdown[i];
            CSVHFStats1up *= Bottoms_ABCD_WeightCSVHFStats1up[i];
            CSVHFStats1down *= Bottoms_ABCD_WeightCSVHFStats1down[i];
            CSVLFStats1up *= Bottoms_ABCD_WeightCSVLFStats1up[i];
            CSVLFStats1down *= Bottoms_ABCD_WeightCSVLFStats1down[i];
            CSVHFStats2up *= Bottoms_ABCD_WeightCSVHFStats2up[i];
            CSVHFStats2down *= Bottoms_ABCD_WeightCSVHFStats2down[i];
            CSVLFStats2up *= Bottoms_ABCD_WeightCSVLFStats2up[i];
            CSVLFStats2down *= Bottoms_ABCD_WeightCSVLFStats2down[i];
            CSVCErr1down *= Bottoms_ABCD_WeightCSVCErr1up[i];
            CSVCErr1down *= Bottoms_ABCD_WeightCSVCErr1down[i];
            CSVCErr2up *= Bottoms_ABCD_WeightCSVCErr2up[i];
            CSVCErr2down *= Bottoms_ABCD_WeightCSVCErr2down[i];
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
std::vector<float> toptag_weights_ABCD1(float const* Zprimes_ABCD_M, float const* Tprimes_ABCD_M, float const* Tops_ABCD_maxsubjetCSVv2, float const* Ws_ABCD_MSD, float const* Tops_ABCD_MSD, float const* Tops_ABCD_t32, float const* Bottoms_ABCD_CSV, float const* Ws_ABCD_t21,int N_Zprime_ABCD){
    std::vector<float> weights;
    
    float toptagnominal=1.0;
    float toptagup=1.0;
    float toptagdown=1.0;

    float SF_top_tau32_MSD_wtb=""" + MCSF_topwtb_t32_MSD + """;
    float SF_top_tau32_MSD_wtb_up=""" + MCSF_topwtb_t32_MSD_up + """;
    float SF_top_tau32_MSD_wtb_down=""" + MCSF_topwtb_t32_MSD_down + """;
    float SF_top_tau32_MSDanti_wtb=""" + MCSF_topwtb_t32_MSD_down + """;
    float SF_top_tau32_MSDanti_wtb_up=""" + MCSF_topwtb_t32_MSD_up + """;
    float SF_top_tau32_MSDanti_wtb_down=""" + MCSF_topwtb_t32_MSD_down + """;
    float SF_top_tau32anti_MSD_wtb=""" + MCSF_topwtb_t32_MSD + """;
    float SF_top_tau32anti_MSD_wtb_up=""" + MCSF_topwtb_t32_MSD_up + """;
    float SF_top_tau32anti_MSD_wtb_down=""" + MCSF_topwtb_t32_MSD_down + """;
    float SF_top_tau32anti_MSDanti_wtb=""" + MCSF_topwtb_t32_MSD + """;
    float SF_top_tau32anti_MSDanti_wtb_up=""" + MCSF_topwtb_t32_MSD_up + """;
    float SF_top_tau32anti_MSDanti_wtb_down=""" + MCSF_topwtb_t32_MSD_down + """;
    
    float SF_top_tau32_MSD_ntb=""" + MCSF_topntb_t32_MSD + """;
    float SF_top_tau32_MSD_ntb_up=""" + MCSF_topntb_t32_MSD_up + """;
    float SF_top_tau32_MSD_ntb_down=""" + MCSF_topntb_t32_MSD_down + """;
    float SF_top_tau32_MSDanti_ntb=""" + MCSF_topntb_t32_MSD + """;
    float SF_top_tau32_MSDanti_ntb_up=""" + MCSF_topntb_t32_MSD_up + """;
    float SF_top_tau32_MSDanti_ntb_down=""" + MCSF_topntb_t32_MSD_down + """;
    float SF_top_tau32anti_MSD_ntb=""" + MCSF_topntb_t32_MSD + """;
    float SF_top_tau32anti_MSD_ntb_up=""" + MCSF_topntb_t32_MSD_up + """;
    float SF_top_tau32anti_MSD_ntb_down=""" + MCSF_topntb_t32_MSD_down + """;
    float SF_top_tau32anti_MSDanti_ntb=""" + MCSF_topntb_t32_MSD + """;
    float SF_top_tau32anti_MSDanti_ntb_up=""" + MCSF_topntb_t32_MSD_up + """;
    float SF_top_tau32anti_MSDanti_ntb_down=""" + MCSF_topntb_t32_MSD_down + """;
    
    for (int i=0; i<N_Zprime_ABCD; i++){
        if ("""+ plotselection_ABCD_general_beta_i + """){
            if(""" + plotselection_topsubjetCSVv2_i + """){
                if(""" + plotselection_tau32_i + """ && """ + plotselection_t_MSD_i + """){
                    toptagnominal *= SF_top_tau32_MSD_wtb;
                    toptagup *= (SF_top_tau32_MSD_wtb + SF_top_tau32_MSD_wtb_up);
                    toptagdown *= (SF_top_tau32_MSD_wtb - SF_top_tau32_MSD_wtb_down);
                }
                if(""" + plotselection_tau32_anti_i + """ && """ + plotselection_t_MSD_i + """){
                    toptagnominal *= SF_top_tau32anti_MSD_wtb;
                    toptagup *= (SF_top_tau32anti_MSD_wtb + SF_top_tau32anti_MSD_wtb_up);
                    toptagdown *= (SF_top_tau32anti_MSD_wtb - SF_top_tau32anti_MSD_wtb_down);
                }
                if(""" + plotselection_tau32_i + """ && """ + plotselection_t_MSD_anti_i + """){
                    toptagnominal *= SF_top_tau32_MSDanti_wtb;
                    toptagup *= (SF_top_tau32_MSDanti_wtb + SF_top_tau32_MSDanti_wtb_up);
                    toptagdown *= (SF_top_tau32_MSDanti_wtb - SF_top_tau32_MSDanti_wtb_down);
                }
                if(""" + plotselection_tau32_anti_i + """ && """ + plotselection_t_MSD_anti_i + """){
                    toptagnominal *= SF_top_tau32anti_MSDanti_wtb;
                    toptagup *= (SF_top_tau32anti_MSDanti_wtb + SF_top_tau32anti_MSDanti_wtb_up);
                    toptagdown *= (SF_top_tau32anti_MSDanti_wtb - SF_top_tau32anti_MSDanti_wtb_down);
                }
            } else {
                if(""" + plotselection_tau32_i + """ && """ + plotselection_t_MSD_i + """){
                    toptagnominal *= SF_top_tau32_MSD_ntb;
                    toptagup *= (SF_top_tau32_MSD_ntb + SF_top_tau32_MSD_ntb_up);
                    toptagdown *= (SF_top_tau32_MSD_ntb - SF_top_tau32_MSD_ntb_down);
                }
                if(""" + plotselection_tau32_anti_i + """ && """ + plotselection_t_MSD_i + """){
                    toptagnominal *= SF_top_tau32anti_MSD_ntb;
                    toptagup *= (SF_top_tau32anti_MSD_ntb + SF_top_tau32anti_MSD_ntb_up);
                    toptagdown *= (SF_top_tau32anti_MSD_ntb - SF_top_tau32anti_MSD_ntb_down);
                }
                if(""" + plotselection_tau32_i + """ && """ + plotselection_t_MSD_anti_i + """){
                    toptagnominal *= SF_top_tau32_MSDanti_ntb;
                    toptagup *= (SF_top_tau32_MSDanti_ntb + SF_top_tau32_MSDanti_ntb_up);
                    toptagdown *= (SF_top_tau32_MSDanti_ntb - SF_top_tau32_MSDanti_ntb_down);
                }
                if(""" + plotselection_tau32_anti_i + """ && """ + plotselection_t_MSD_anti_i + """){
                    toptagnominal *= SF_top_tau32anti_MSDanti_ntb;
                    toptagup *= (SF_top_tau32anti_MSDanti_ntb + SF_top_tau32anti_MSDanti_ntb_up);
                    toptagdown *= (SF_top_tau32anti_MSDanti_ntb - SF_top_tau32anti_MSDanti_ntb_down);
                }
            }
            break;
        }
    }
    
    weights.push_back(toptagnominal);
    weights.push_back(toptagup);
    weights.push_back(toptagdown);
   
    
    return weights;
}

"""
,
"""
std::vector<float> toptag_weights_ABCD2(float const* Zprimes_ABCD_M, float const* Tprimes_ABCD_M, float const* Tops_ABCD_maxsubjetCSVv2, float const* Ws_ABCD_MSD, float const* Tops_ABCD_MSD, float const* Tops_ABCD_t32, float const* Bottoms_ABCD_CSV, float const* Ws_ABCD_t21,int N_Zprime_ABCD){
    std::vector<float> weights;
    
    float toptagnominal=1.0;
    float toptagup=1.0;
    float toptagdown=1.0;

    float SF_top_tau32_MSD_wtb=""" + MCSF_topwtb_t32_MSD + """;
    float SF_top_tau32_MSD_wtb_up=""" + MCSF_topwtb_t32_MSD_up + """;
    float SF_top_tau32_MSD_wtb_down=""" + MCSF_topwtb_t32_MSD_down + """;
    float SF_top_tau32_MSDanti_wtb=""" + MCSF_topwtb_t32_MSD_down + """;
    float SF_top_tau32_MSDanti_wtb_up=""" + MCSF_topwtb_t32_MSD_up + """;
    float SF_top_tau32_MSDanti_wtb_down=""" + MCSF_topwtb_t32_MSD_down + """;
    float SF_top_tau32anti_MSD_wtb=""" + MCSF_topwtb_t32_MSD + """;
    float SF_top_tau32anti_MSD_wtb_up=""" + MCSF_topwtb_t32_MSD_up + """;
    float SF_top_tau32anti_MSD_wtb_down=""" + MCSF_topwtb_t32_MSD_down + """;
    float SF_top_tau32anti_MSDanti_wtb=""" + MCSF_topwtb_t32_MSD + """;
    float SF_top_tau32anti_MSDanti_wtb_up=""" + MCSF_topwtb_t32_MSD_up + """;
    float SF_top_tau32anti_MSDanti_wtb_down=""" + MCSF_topwtb_t32_MSD_down + """;
    
    float SF_top_tau32_MSD_ntb=""" + MCSF_topntb_t32_MSD + """;
    float SF_top_tau32_MSD_ntb_up=""" + MCSF_topntb_t32_MSD_up + """;
    float SF_top_tau32_MSD_ntb_down=""" + MCSF_topntb_t32_MSD_down + """;
    float SF_top_tau32_MSDanti_ntb=""" + MCSF_topntb_t32_MSD + """;
    float SF_top_tau32_MSDanti_ntb_up=""" + MCSF_topntb_t32_MSD_up + """;
    float SF_top_tau32_MSDanti_ntb_down=""" + MCSF_topntb_t32_MSD_down + """;
    float SF_top_tau32anti_MSD_ntb=""" + MCSF_topntb_t32_MSD + """;
    float SF_top_tau32anti_MSD_ntb_up=""" + MCSF_topntb_t32_MSD_up + """;
    float SF_top_tau32anti_MSD_ntb_down=""" + MCSF_topntb_t32_MSD_down + """;
    float SF_top_tau32anti_MSDanti_ntb=""" + MCSF_topntb_t32_MSD + """;
    float SF_top_tau32anti_MSDanti_ntb_up=""" + MCSF_topntb_t32_MSD_up + """;
    float SF_top_tau32anti_MSDanti_ntb_down=""" + MCSF_topntb_t32_MSD_down + """;
    
    
    for (int i=0; i<N_Zprime_ABCD; i++){
        if ("""+ plotselection_ABCD_general_beta_i + """){
            if(""" + plotselection_topsubjetCSVv2_i + """){
                if(""" + plotselection_tau32_i + """ && """ + plotselection_t_MSD_i + """){
                    toptagnominal *= SF_top_tau32_MSD_wtb;
                    toptagup *= (SF_top_tau32_MSD_wtb + SF_top_tau32_MSD_wtb_up);
                    toptagdown *= (SF_top_tau32_MSD_wtb - SF_top_tau32_MSD_wtb_down);
                }
                if(""" + plotselection_tau32_anti_i + """ && """ + plotselection_t_MSD_i + """){
                    toptagnominal *= SF_top_tau32anti_MSD_wtb;
                    toptagup *= (SF_top_tau32anti_MSD_wtb + SF_top_tau32anti_MSD_wtb_up);
                    toptagdown *= (SF_top_tau32anti_MSD_wtb - SF_top_tau32anti_MSD_wtb_down);
                }
                if(""" + plotselection_tau32_i + """ && """ + plotselection_t_MSD_anti_i + """){
                    toptagnominal *= SF_top_tau32_MSDanti_wtb;
                    toptagup *= (SF_top_tau32_MSDanti_wtb + SF_top_tau32_MSDanti_wtb_up);
                    toptagdown *= (SF_top_tau32_MSDanti_wtb - SF_top_tau32_MSDanti_wtb_down);
                }
                if(""" + plotselection_tau32_anti_i + """ && """ + plotselection_t_MSD_anti_i + """){
                    toptagnominal *= SF_top_tau32anti_MSDanti_wtb;
                    toptagup *= (SF_top_tau32anti_MSDanti_wtb + SF_top_tau32anti_MSDanti_wtb_up);
                    toptagdown *= (SF_top_tau32anti_MSDanti_wtb - SF_top_tau32anti_MSDanti_wtb_down);
                }
            } else {
                if(""" + plotselection_tau32_i + """ && """ + plotselection_t_MSD_i + """){
                    toptagnominal *= SF_top_tau32_MSD_ntb;
                    toptagup *= (SF_top_tau32_MSD_ntb + SF_top_tau32_MSD_ntb_up);
                    toptagdown *= (SF_top_tau32_MSD_ntb - SF_top_tau32_MSD_ntb_down);
                }
                if(""" + plotselection_tau32_anti_i + """ && """ + plotselection_t_MSD_i + """){
                    toptagnominal *= SF_top_tau32anti_MSD_ntb;
                    toptagup *= (SF_top_tau32anti_MSD_ntb + SF_top_tau32anti_MSD_ntb_up);
                    toptagdown *= (SF_top_tau32anti_MSD_ntb - SF_top_tau32anti_MSD_ntb_down);
                }
                if(""" + plotselection_tau32_i + """ && """ + plotselection_t_MSD_anti_i + """){
                    toptagnominal *= SF_top_tau32_MSDanti_ntb;
                    toptagup *= (SF_top_tau32_MSDanti_ntb + SF_top_tau32_MSDanti_ntb_up);
                    toptagdown *= (SF_top_tau32_MSDanti_ntb - SF_top_tau32_MSDanti_ntb_down);
                }
                if(""" + plotselection_tau32_anti_i + """ && """ + plotselection_t_MSD_anti_i + """){
                    toptagnominal *= SF_top_tau32anti_MSDanti_ntb;
                    toptagup *= (SF_top_tau32anti_MSDanti_ntb + SF_top_tau32anti_MSDanti_ntb_up);
                    toptagdown *= (SF_top_tau32anti_MSDanti_ntb - SF_top_tau32anti_MSDanti_ntb_down);
                }
            }
            break;
        }
    }
    
    weights.push_back(toptagnominal);
    weights.push_back(toptagup);
    weights.push_back(toptagdown);
   
    
    return weights;
}

"""
,
"""
std::vector<float> Wtag_weights_ABCD1(float const* Zprimes_ABCD_M, float const* Tprimes_ABCD_M, float const* Tops_ABCD_maxsubjetCSVv2, float const* Ws_ABCD_MSD, float const* Tops_ABCD_MSD, float const* Tops_ABCD_t32, float const* Bottoms_ABCD_CSV, float const* Ws_ABCD_t21,int N_Zprime_ABCD){
    std::vector<float> weights;
    
    float Wtagnominal=1.0;
    float Wtagup=1.0;
    float Wtagdown=1.0;

    float SF_W_tau21_MSD=""" + MCSF_W_t21_MSD + """;
    float SF_W_tau21_MSD_up=""" + MCSF_W_t21_MSD_up + """;
    float SF_W_tau21_MSD_down=""" + MCSF_W_t21_MSD_down + """;
    float SF_W_tau21_MSDanti=""" + MCSF_W_t21_MSD + """;
    float SF_W_tau21_MSDanti_up=""" + MCSF_W_t21_MSD_up + """;
    float SF_W_tau21_MSDanti_down=""" + MCSF_W_t21_MSD_down + """;
    float SF_W_tau21anti_MSD=""" + MCSF_W_t21_MSD + """;
    float SF_W_tau21anti_MSD_up=""" + MCSF_W_t21_MSD_up + """;
    float SF_W_tau21anti_MSD_down=""" + MCSF_W_t21_MSD_down + """;
    float SF_W_tau21anti_MSDanti=""" + MCSF_W_t21_MSD + """;
    float SF_W_tau21anti_MSDanti_up=""" + MCSF_W_t21_MSD_up + """;
    float SF_W_tau21anti_MSDanti_down=""" + MCSF_W_t21_MSD_down + """;

    for (int i=0; i<N_Zprime_ABCD; i++){
        if ("""+ plotselection_ABCD_general_beta_i + """){
           
                if(""" + plotselection_W_tau21_i + """ && """ + plotselection_W_MSD_i + """){
                    Wtagnominal *= SF_W_tau21_MSD;
                    Wtagup *= (SF_W_tau21_MSD + SF_W_tau21_MSD_up);
                    Wtagdown *= (SF_W_tau21_MSD - SF_W_tau21_MSD_down);
                }
                if(""" + plotselection_W_tau21_anti_i + """ && """ + plotselection_W_MSD_i + """){
                    Wtagnominal *= SF_W_tau21anti_MSD;
                    Wtagup *= (SF_W_tau21anti_MSD + SF_W_tau21anti_MSD_up);
                    Wtagdown *= (SF_W_tau21anti_MSD - SF_W_tau21anti_MSD_down);
                }
                if(""" + plotselection_W_tau21_i + """ && """ + plotselection_W_MSD_anti_i + """){
                    Wtagnominal *= SF_W_tau21_MSDanti;
                    Wtagup *= (SF_W_tau21_MSDanti + SF_W_tau21_MSDanti_up);
                    Wtagdown *= (SF_W_tau21_MSDanti - SF_W_tau21_MSDanti_down);
                }
                if(""" + plotselection_W_tau21_anti_i + """ && """ + plotselection_W_MSD_anti_i + """){
                    Wtagnominal *= SF_W_tau21anti_MSDanti;
                    Wtagup *= (SF_W_tau21anti_MSDanti + SF_W_tau21anti_MSDanti_up);
                    Wtagdown *= (SF_W_tau21anti_MSDanti - SF_W_tau21anti_MSDanti_down);
                }        
                break;
        }
    }
    
    weights.push_back(Wtagnominal);
    weights.push_back(Wtagup);
    weights.push_back(Wtagdown);
   
    
    return weights;
}

"""
,
"""
std::vector<float> Wtag_weights_ABCD2(float const* Zprimes_ABCD_M, float const* Tprimes_ABCD_M, float const* Tops_ABCD_maxsubjetCSVv2, float const* Ws_ABCD_MSD, float const* Tops_ABCD_MSD, float const* Tops_ABCD_t32, float const* Bottoms_ABCD_CSV, float const* Ws_ABCD_t21,int N_Zprime_ABCD){
    std::vector<float> weights;
    
    float Wtagnominal=1.0;
    float Wtagup=1.0;
    float Wtagdown=1.0;

    float SF_W_tau21_MSD=""" + MCSF_W_t21_MSD + """;
    float SF_W_tau21_MSD_up=""" + MCSF_W_t21_MSD_up + """;
    float SF_W_tau21_MSD_down=""" + MCSF_W_t21_MSD_down + """;
    float SF_W_tau21_MSDanti=""" + MCSF_W_t21_MSD + """;
    float SF_W_tau21_MSDanti_up=""" + MCSF_W_t21_MSD_up + """;
    float SF_W_tau21_MSDanti_down=""" + MCSF_W_t21_MSD_down + """;
    float SF_W_tau21anti_MSD=""" + MCSF_W_t21_MSD + """;
    float SF_W_tau21anti_MSD_up=""" + MCSF_W_t21_MSD_up + """;
    float SF_W_tau21anti_MSD_down=""" + MCSF_W_t21_MSD_down + """;
    float SF_W_tau21anti_MSDanti=""" + MCSF_W_t21_MSD + """;
    float SF_W_tau21anti_MSDanti_up=""" + MCSF_W_t21_MSD_up + """;
    float SF_W_tau21anti_MSDanti_down=""" + MCSF_W_t21_MSD_down + """;

    for (int i=0; i<N_Zprime_ABCD; i++){
        if ("""+ plotselection_ABCD_general_beta2_i + """){
                if(""" + plotselection_W_tau21_i + """ && """ + plotselection_W_MSD_i + """){
                    Wtagnominal *= SF_W_tau21_MSD;
                    Wtagup *= (SF_W_tau21_MSD + SF_W_tau21_MSD_up);
                    Wtagup *= (SF_W_tau21_MSD - SF_W_tau21_MSD_down);
                }
                if(""" + plotselection_W_tau21_anti_i + """ && """ + plotselection_W_MSD_i + """){
                    Wtagnominal *= SF_W_tau21anti_MSD;
                    Wtagup *= (SF_W_tau21anti_MSD + SF_W_tau21anti_MSD_up);
                    Wtagup *= (SF_W_tau21anti_MSD - SF_W_tau21anti_MSD_down);
                }
                if(""" + plotselection_W_tau21_i + """ && """ + plotselection_W_MSD_anti_i + """){
                    Wtagnominal *= SF_W_tau21_MSDanti;
                    Wtagup *= (SF_W_tau21_MSDanti + SF_W_tau21_MSDanti_up);
                    Wtagup *= (SF_W_tau21_MSDanti - SF_W_tau21_MSDanti_down);
                }
                if(""" + plotselection_W_tau21_anti_i + """ && """ + plotselection_W_MSD_i + """){
                    Wtagnominal *= SF_W_tau21anti_MSDanti;
                    Wtagup *= (SF_W_tau21anti_MSDanti + SF_W_tau21anti_MSDanti_up);
                    Wtagup *= (SF_W_tau21anti_MSDanti - SF_W_tau21anti_MSDanti_down);
                }        
                break;
        }
    }
    
    weights.push_back(Wtagnominal);
    weights.push_back(Wtagup);
    weights.push_back(Wtagdown);
   
    
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
                        
                        'ABCD_CatID:=1.0 * ABCD_Category(Zprimes_ABCD_M,   Tprimes_ABCD_M,   Tops_ABCD_maxsubjetCSVv2,   Ws_ABCD_MSD,   Tops_ABCD_MSD,   Tops_ABCD_t32,   Bottoms_ABCD_CSV,   Ws_ABCD_t21, N_Zprime_ABCD)',
                        'ABCD2_CatID:=1.0* ABCD2_Category(Zprimes_ABCD_M,   Tprimes_ABCD_M,   Tops_ABCD_maxsubjetCSVv2,   Ws_ABCD_MSD,   Tops_ABCD_MSD,   Tops_ABCD_t32,   Bottoms_ABCD_CSV,   Ws_ABCD_t21, N_Zprime_ABCD)',
                        
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
                        
                        'ABCD2_CatA_withtopbtag:=1',
                        'ABCD2_CatB_withtopbtag:=2',
                        'ABCD2_CatC_withtopbtag:=3',
                        'ABCD2_CatD_withtopbtag:=4',
                        'ABCD2_CatE_withtopbtag:=5',
                        'ABCD2_CatF_withtopbtag:=6',
                        'ABCD2_CatG_withtopbtag:=7',
                        'ABCD2_CatH_withtopbtag:=8',
                        
                        'ABCD2_CatA_notopbtag:=9',
                        'ABCD2_CatB_notopbtag:=10',
                        'ABCD2_CatC_notopbtag:=11',
                        'ABCD2_CatD_notopbtag:=12',
                        'ABCD2_CatE_notopbtag:=13',
                        'ABCD2_CatF_notopbtag:=14',
                        'ABCD2_CatG_notopbtag:=15',
                        'ABCD2_CatH_notopbtag:=16',         
                        
                        
                        'ABCD1_WeightCSVnominal:=(CSV_weights_ABCD1(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[0]',
                        'ABCD1_WeightCSVLFup:=(CSV_weights_ABCD1(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[1]',
                        'ABCD1_WeightCSVLFdown:=(CSV_weights_ABCD1(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[2]',
                        'ABCD1_WeightCSVHFup:=(CSV_weights_ABCD1(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[3]',
                        'ABCD1_WeightCSVHFdown:=(CSV_weights_ABCD1(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[4]',
                        'ABCD1_WeightCSVHFStats1up:=(CSV_weights_ABCD1(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[5]',
                        'ABCD1_WeightCSVHFStats1down:=(CSV_weights_ABCD1(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[6]',
                        'ABCD1_WeightCSVLFStats1up:=(CSV_weights_ABCD1(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[7]',
                        'ABCD1_WeightCSVLFStats1down:=(CSV_weights_ABCD1(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[8]',
                        'ABCD1_WeightCSVHFStats2up:=(CSV_weights_ABCD1(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[9]',
                        'ABCD1_WeightCSVHFStats2down:=(CSV_weights_ABCD1(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[10]',
                        'ABCD1_WeightCSVLFStats2up:=(CSV_weights_ABCD1(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[11]',
                        'ABCD1_WeightCSVLFStats2down:=(CSV_weights_ABCD1(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[12]',
                        'ABCD1_WeightCSVCErr1up:=(CSV_weights_ABCD1(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[13]',
                        'ABCD1_WeightCSVCErr1down:=(CSV_weights_ABCD1(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[14]',
                        'ABCD1_WeightCSVCErr2up:=(CSV_weights_ABCD1(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[15]',
                        'ABCD1_WeightCSVCErr2down:=(CSV_weights_ABCD1(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[16]',

                        'ABCD2_WeightCSVnominal:=(CSV_weights_ABCD2(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[0]',
                        'ABCD2_WeightCSVLFup:=(CSV_weights_ABCD2(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[1]',
                        'ABCD2_WeightCSVLFdown:=(CSV_weights_ABCD2(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[2]',
                        'ABCD2_WeightCSVHFup:=(CSV_weights_ABCD2(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[3]',
                        'ABCD2_WeightCSVHFdown:=(CSV_weights_ABCD2(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[4]',
                        'ABCD2_WeightCSVHFStats1up:=(CSV_weights_ABCD2(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[5]',
                        'ABCD2_WeightCSVHFStats1down:=(CSV_weights_ABCD2(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[6]',
                        'ABCD2_WeightCSVLFStats1up:=(CSV_weights_ABCD2(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[7]',
                        'ABCD2_WeightCSVLFStats1down:=(CSV_weights_ABCD2(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[8]',
                        'ABCD2_WeightCSVHFStats2up:=(CSV_weights_ABCD2(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[9]',
                        'ABCD2_WeightCSVHFStats2down:=(CSV_weights_ABCD2(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[10]',
                        'ABCD2_WeightCSVLFStats2up:=(CSV_weights_ABCD2(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[11]',
                        'ABCD2_WeightCSVLFStats2down:=(CSV_weights_ABCD2(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[12]',
                        'ABCD2_WeightCSVCErr1up:=(CSV_weights_ABCD2(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[13]',
                        'ABCD2_WeightCSVCErr1down:=(CSV_weights_ABCD2(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[14]',
                        'ABCD2_WeightCSVCErr2up:=(CSV_weights_ABCD2(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[15]',
                        'ABCD2_WeightCSVCErr2down:=(CSV_weights_ABCD2(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD, Bottoms_ABCD_WeightCSVnominal,  Bottoms_ABCD_WeightCSVLFup, Bottoms_ABCD_WeightCSVLFdown, Bottoms_ABCD_WeightCSVHFup, Bottoms_ABCD_WeightCSVHFdown, Bottoms_ABCD_WeightCSVHFStats1up, Bottoms_ABCD_WeightCSVHFStats1down, Bottoms_ABCD_WeightCSVLFStats1up,  Bottoms_ABCD_WeightCSVLFStats1down, Bottoms_ABCD_WeightCSVHFStats2up, Bottoms_ABCD_WeightCSVHFStats2down, Bottoms_ABCD_WeightCSVLFStats2up, Bottoms_ABCD_WeightCSVLFStats2down, Bottoms_ABCD_WeightCSVCErr1up, Bottoms_ABCD_WeightCSVCErr1down, Bottoms_ABCD_WeightCSVCErr2up, Bottoms_ABCD_WeightCSVCErr2down))[16]',
                        
                        
                        'ABCD1_Wtagweightnominal:=(Wtag_weights_ABCD1(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD))[0]',
                        'ABCD1_Wtagweightup:=(Wtag_weights_ABCD1(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD))[1]',
                        'ABCD1_Wtagweightdown:=(Wtag_weights_ABCD1(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD))[2]',
                        'ABCD1_toptagweightnominal:=(toptag_weights_ABCD1(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD))[0]',
                        'ABCD1_toptagweightup:=(toptag_weights_ABCD1(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD))[1]',
                        'ABCD1_toptagweightdown:=(toptag_weights_ABCD1(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD))[2]',
 
                        'ABCD2_Wtagweightnominal:=(Wtag_weights_ABCD2(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD))[0]',
                        'ABCD2_Wtagweightup:=(Wtag_weights_ABCD2(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD))[1]',
                        'ABCD2_Wtagweightdown:=(Wtag_weights_ABCD2(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD))[2]',
                        'ABCD2_toptagweightnominal:=(toptag_weights_ABCD2(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD))[0]',
                        'ABCD2_toptagweightup:=(toptag_weights_ABCD2(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD))[1]',
                        'ABCD2_toptagweightdown:=(toptag_weights_ABCD2(Zprimes_ABCD_M, Tprimes_ABCD_M, Tops_ABCD_maxsubjetCSVv2, Ws_ABCD_MSD, Tops_ABCD_MSD, Tops_ABCD_t32, Bottoms_ABCD_CSV, Ws_ABCD_t21, N_Zprime_ABCD))[2]',
 
                        'MCSF_RenFac_envelopeUp:=(RenFacEnv(Weight_scale_variation_muR2p0_muF2p0, Weight_scale_variation_muR0p5_muF0p5, Weight_scale_variation_muR1p0_muF2p0 , Weight_scale_variation_muR1p0_muF0p5, Weight_scale_variation_muR2p0_muF1p0, Weight_scale_variation_muR0p5_muF1p0))[0]',
                        'MCSF_RenFac_envelopeDown:=(RenFacEnv(Weight_scale_variation_muR2p0_muF2p0, Weight_scale_variation_muR0p5_muF0p5, Weight_scale_variation_muR1p0_muF2p0 , Weight_scale_variation_muR1p0_muF0p5, Weight_scale_variation_muR2p0_muF1p0, Weight_scale_variation_muR0p5_muF1p0))[1]',
                                               #'N_Jets', 'Jet_Pt','Jet_Eta','Jet_CSV','Jet_Flav','Jet_M','Jet_Phi','Jet_E',
                        'PDF_RMSMean:=PDF_RMS('+ stringforPDFs1 +')[0]',
                        'PDF_RMSUp:=PDF_RMS('+ stringforPDFs1 +')[1]',
                        'PDF_RMSDown:=PDF_RMS('+ stringforPDFs1 +')[2]',
                        
                        'MCSF_Weight_ABCD1:=ABCD1_toptagweightnominal*ABCD1_Wtagweightnominal*ABCD1_WeightCSVnominal*PDF_RMSMean*Weight_pu69p2',
                        'MCSF_Weight_ABCD2:=ABCD2_toptagweightnominal*ABCD2_Wtagweightnominal*ABCD2_WeightCSVnominal*PDF_RMSMean*Weight_pu69p2',
                        

                        #'internalCSVweight:=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,internalSystName,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)',
                        #'internalCSVweight_CSVHFUp:=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,11,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight',
                        #'internalCSVweight_CSVHFDown:=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,12,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight',
                        #'internalCSVweight_CSVLFUp:=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,9,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight',
                        #'internalCSVweight_CSVLFDown:=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,10,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight',                        

]