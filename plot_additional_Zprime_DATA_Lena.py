from plot_cuts_ZPrime_MC_Lena import *


#plotselection_W_MSD =  " (65 < Ws_ABCD"+radi+"_MSD  &&   Ws_ABCD"+radi+"_MSD < 105) "
#plotselection_W_MSD_i =  " (65 < Ws_ABCD"+radi+"_MSD[i] &&   Ws_ABCD"+radi+"_MSD[i] < 105) "
#plotselection_W_MSD_0 =  " (65 < Ws_ABCD"+radi+"_MSD[0] &&   Ws_ABCD"+radi+"_MSD[0] < 105) "


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
""",    
    
    
#"""
#std::vector<float> bbarportionweight(int const N){
    #std::vector<float> res;
    
    #if(N>0){
        #res.push_back(1.0);
        #res.push_back(1.5);
        #res.push_back(0.5);
        #res.push_back(0.0);
    #} else {
        #res.push_back(1.0);
        #res.push_back(1.0);
        #res.push_back(1.0);
        #res.push_back(1.0);
    #};
    #return res;
#}
  
    #""",
"""
int ABCD1_Category(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Ws_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt, float const* Tops_ABCD"""+radi+"""_Pt, float const* Bottoms_ABCD"""+radi+"""_Pt, int N_Zprime_ABCD"""+radi+""",  float Evt_HT_Jets, float N_Jets, float N_packedPatJetsAK8PFCHSSoftDrop, float N_PrimaryVertices){
    int res=0;
    for (int i=0; i<N_Zprime_ABCD"""+radi+"""; i++){
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
int ABCD2_Category(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Ws_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt, float const* Tops_ABCD"""+radi+"""_Pt, float const* Bottoms_ABCD"""+radi+"""_Pt, int N_Zprime_ABCD"""+radi+""",  float Evt_HT_Jets, float N_Jets, float N_packedPatJetsAK8PFCHSSoftDrop, float N_PrimaryVertices){
    int res=0;
    for (int i=0; i<N_Zprime_ABCD"""+radi+"""; i++){
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
int ABCD3_Category(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Ws_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt, float const* Tops_ABCD"""+radi+"""_Pt, float const* Bottoms_ABCD"""+radi+"""_Pt, int N_Zprime_ABCD"""+radi+""",  float Evt_HT_Jets, float N_Jets, float N_packedPatJetsAK8PFCHSSoftDrop, float N_PrimaryVertices){
    int res=0;
    for (int i=0; i<N_Zprime_ABCD"""+radi+"""; i++){
        if ("""+ plotselection_ABCD_general_beta3_i +"""){
            if("""+ plotselection_topsubjetCSVv2_i +"""){
                if("""+ plotselection_W_tau21_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_W_MSD_i + """){
                            res=1;
                            break;
                        }
                        if(""" + plotselection_W_MSD_anti_i + """){
                            res=2;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_W_MSD_i + """){
                            res=3;
                            break;
                        }
                        if(""" + plotselection_W_MSD_anti_i + """){
                            res=4;
                            break;
                        }
                    }                
                }
                if("""+ plotselection_W_tau21_anti_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_W_MSD_i + """){
                            res=5;
                            break;
                        }
                        if(""" + plotselection_W_MSD_anti_i + """){
                            res=6;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_W_MSD_i + """){
                            res=7;
                            break;
                        }
                        if(""" + plotselection_W_MSD_anti_i + """){
                            res=8;
                            break;
                        }
                    }                
                }
            } else {
                if("""+ plotselection_W_tau21_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_W_MSD_i + """){
                            res=9;
                            break;
                        }
                        if(""" + plotselection_W_MSD_anti_i + """){
                            res=10;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_W_MSD_i + """){
                            res=11;
                            break;
                        }
                        if(""" + plotselection_W_MSD_anti_i + """){
                            res=12;
                            break;
                        }
                    }                
                }
                if("""+ plotselection_W_tau21_anti_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_W_MSD_i + """){
                            res=13;
                            break;
                        }
                        if(""" + plotselection_W_MSD_anti_i + """){
                            res=14;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_W_MSD_i + """){
                            res=15;
                            break;
                        }
                        if(""" + plotselection_W_MSD_anti_i + """){
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
int ABCD4_Category(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Ws_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt, float const* Tops_ABCD"""+radi+"""_Pt, float const* Bottoms_ABCD"""+radi+"""_Pt, int N_Zprime_ABCD"""+radi+""",  float Evt_HT_Jets, float N_Jets, float N_packedPatJetsAK8PFCHSSoftDrop, float N_PrimaryVertices){
    int res=0;
    for (int i=0; i<N_Zprime_ABCD"""+radi+"""; i++){
        if ("""+ plotselection_ABCD_general_beta4_i +"""){
            if("""+ plotselection_topsubjetCSVv2_i +"""){
                if("""+ plotselection_W_tau21_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_TprimeMass_i + """){
                            res=1;
                            break;
                        }
                        if(""" + plotselection_TprimeMass_anti_i + """){
                            res=2;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_TprimeMass_i + """){
                            res=3;
                            break;
                        }
                        if(""" + plotselection_TprimeMass_anti_i + """){
                            res=4;
                            break;
                        }
                    }                
                }
                if("""+ plotselection_W_tau21_anti_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_TprimeMass_i + """){
                            res=5;
                            break;
                        }
                        if(""" + plotselection_TprimeMass_anti_i + """){
                            res=6;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_TprimeMass_i + """){
                            res=7;
                            break;
                        }
                        if(""" + plotselection_TprimeMass_anti_i + """){
                            res=8;
                            break;
                        }
                    }                
                }
            } else {
                if("""+ plotselection_W_tau21_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_TprimeMass_i + """){
                            res=9;
                            break;
                        }
                        if(""" + plotselection_TprimeMass_anti_i + """){
                            res=10;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_TprimeMass_i + """){
                            res=11;
                            break;
                        }
                        if(""" + plotselection_TprimeMass_anti_i + """){
                            res=12;
                            break;
                        }
                    }                
                }
                if("""+ plotselection_W_tau21_anti_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_TprimeMass_i + """){
                            res=13;
                            break;
                        }
                        if(""" + plotselection_TprimeMass_anti_i + """){
                            res=14;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_TprimeMass_i + """){
                            res=15;
                            break;
                        }
                        if(""" + plotselection_TprimeMass_anti_i + """){
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

"""
,
"""
int ABCD5_Category(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Ws_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt, float const* Tops_ABCD"""+radi+"""_Pt, float const* Bottoms_ABCD"""+radi+"""_Pt, int N_Zprime_ABCD"""+radi+""",  float Evt_HT_Jets, float N_Jets, float N_packedPatJetsAK8PFCHSSoftDrop, float N_PrimaryVertices){
    int res=0;
    for (int i=0; i<N_Zprime_ABCD"""+radi+"""; i++){
        if ("""+ plotselection_ABCD_general_beta5_i +"""){
            //if((!("""+ plotselection_W_tau21_i + """) && !("""+ plotselection_W_tau21_anti_i + """) || (!(""" + plotselection_W_MSD_i + """) && !(""" + plotselection_W_MSD_anti_i + """)))){
            //    break;
            //};
            if("""+ plotselection_topsubjetCSVv2_i +"""){
                if("""+ plotselection_W_MSD_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=1;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=2;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=3;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=4;
                            break;
                        }
                    }                
                }
                if("""+ plotselection_W_MSD_anti_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=5;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=6;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=7;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=8;
                            break;
                        }
                    }                
                }
            } else {
                if("""+ plotselection_W_MSD_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=9;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=10;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=11;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=12;
                            break;
                        }
                    }                
                }
                if("""+ plotselection_W_MSD_anti_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=13;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=14;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=15;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
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

"""
,
"""
int ABCD6_Category(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Ws_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt, float const* Tops_ABCD"""+radi+"""_Pt, float const* Bottoms_ABCD"""+radi+"""_Pt, int N_Zprime_ABCD"""+radi+""",  float Evt_HT_Jets, float N_Jets, float N_packedPatJetsAK8PFCHSSoftDrop, float N_PrimaryVertices){
    int res=0;
    for (int i=0; i<N_Zprime_ABCD"""+radi+"""; i++){
        if ("""+ plotselection_ABCD_general_beta6_i +"""){
            if("""+ plotselection_topsubjetCSVv2_i +"""){
                if("""+ plotselection_B_CSV_i +"""){
                    if("""+ plotselection_t_MSD_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=1;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=2;
                            break;
                        }
                    }
                    if("""+ plotselection_t_MSD_anti_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=3;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=4;
                            break;
                        }
                    }                
                }
                if("""+ plotselection_B_CSV_anti_i +"""){
                    if("""+ plotselection_t_MSD_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=5;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=6;
                            break;
                        }
                    }
                    if("""+ plotselection_t_MSD_anti_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=7;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=8;
                            break;
                        }
                    }                
                }
            } else {
                if("""+ plotselection_B_CSV_i +"""){
                    if("""+ plotselection_t_MSD_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=9;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=10;
                            break;
                        }
                    }
                    if("""+ plotselection_t_MSD_anti_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=11;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=12;
                            break;
                        }
                    }                
                }
                if("""+ plotselection_B_CSV_anti_i +"""){
                    if("""+ plotselection_t_MSD_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=13;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=14;
                            break;
                        }
                    }
                    if("""+ plotselection_t_MSD_anti_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=15;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
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

"""
,
"""
int ABCD7_Category(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Ws_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt, float const* Tops_ABCD"""+radi+"""_Pt, float const* Bottoms_ABCD"""+radi+"""_Pt, int N_Zprime_ABCD"""+radi+""",  float Evt_HT_Jets, float N_Jets, float N_packedPatJetsAK8PFCHSSoftDrop, float N_PrimaryVertices){
    int res=0;
    for (int i=0; i<N_Zprime_ABCD"""+radi+"""; i++){
        if ("""+ plotselection_ABCD_general_beta7_i +"""){
            if("""+ plotselection_topsubjetCSVv2_i +"""){
                if("""+ plotselection_B_CSV_i +"""){
                    if("""+ plotselection_t_MSD_i + """){
                        if(""" + plotselection_W_MSD_i + """){
                            res=1;
                            break;
                        }
                        if(""" + plotselection_W_MSD_anti_i + """){
                            res=2;
                            break;
                        }
                    }
                    if("""+ plotselection_t_MSD_anti_i + """){
                        if(""" + plotselection_W_MSD_i + """){
                            res=3;
                            break;
                        }
                        if(""" + plotselection_W_MSD_anti_i + """){
                            res=4;
                            break;
                        }
                    }                
                }
                if("""+ plotselection_B_CSV_anti_i +"""){
                    if("""+ plotselection_t_MSD_i + """){
                        if(""" + plotselection_W_MSD_i + """){
                            res=5;
                            break;
                        }
                        if(""" + plotselection_W_MSD_anti_i + """){
                            res=6;
                            break;
                        }
                    }
                    if("""+ plotselection_t_MSD_anti_i + """){
                        if(""" + plotselection_W_MSD_i + """){
                            res=7;
                            break;
                        }
                        if(""" + plotselection_W_MSD_anti_i + """){
                            res=8;
                            break;
                        }
                    }                
                }
            } else {
                if("""+ plotselection_B_CSV_i +"""){
                    if("""+ plotselection_t_MSD_i + """){
                        if(""" + plotselection_W_MSD_i + """){
                            res=9;
                            break;
                        }
                        if(""" + plotselection_W_MSD_anti_i + """){
                            res=10;
                            break;
                        }
                    }
                    if("""+ plotselection_t_MSD_anti_i + """){
                        if(""" + plotselection_W_MSD_i + """){
                            res=11;
                            break;
                        }
                        if(""" + plotselection_W_MSD_anti_i + """){
                            res=12;
                            break;
                        }
                    }                
                }
                if("""+ plotselection_B_CSV_anti_i +"""){
                    if("""+ plotselection_t_MSD_i + """){
                        if(""" + plotselection_W_MSD_i + """){
                            res=13;
                            break;
                        }
                        if(""" + plotselection_W_MSD_anti_i + """){
                            res=14;
                            break;
                        }
                    }
                    if("""+ plotselection_t_MSD_anti_i + """){
                        if(""" + plotselection_W_MSD_i + """){
                            res=15;
                            break;
                        }
                        if(""" + plotselection_W_MSD_anti_i + """){
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
int ABCD8_Category(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Ws_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt, float const* Tops_ABCD"""+radi+"""_Pt, float const* Bottoms_ABCD"""+radi+"""_Pt, int N_Zprime_ABCD"""+radi+""",  float Evt_HT_Jets, float N_Jets, float N_packedPatJetsAK8PFCHSSoftDrop, float N_PrimaryVertices){
    int res=0;
    for (int i=0; i<N_Zprime_ABCD"""+radi+"""; i++){
        if ("""+ plotselection_ABCD_general_beta8_i +"""){
            if("""+ plotselection_topsubjetCSVv2_i +"""){
                if("""+ plotselection_t_MSD_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=1;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=2;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=3;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=4;
                            break;
                        }
                    }                
                }
                if("""+ plotselection_t_MSD_anti_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=5;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=6;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=7;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=8;
                            break;
                        }
                    }                
                }
            } else {
                if("""+ plotselection_t_MSD_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=9;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=10;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=11;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=12;
                            break;
                        }
                    }                
                }
                if("""+ plotselection_t_MSD_anti_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=13;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=14;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=15;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
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
int ABCD9_Category(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Ws_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt, float const* Tops_ABCD"""+radi+"""_Pt, float const* Bottoms_ABCD"""+radi+"""_Pt, int N_Zprime_ABCD"""+radi+""",  float Evt_HT_Jets, float N_Jets, float N_packedPatJetsAK8PFCHSSoftDrop, float N_PrimaryVertices){
    int res=0;
    for (int i=0; i<N_Zprime_ABCD"""+radi+"""; i++){
        if ("""+ plotselection_ABCD_general_beta9_i +"""){
            if("""+ plotselection_topsubjetCSVv2_i +"""){
                if("""+ plotselection_tau32_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=1;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=2;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=3;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=4;
                            break;
                        }
                    }                
                }
                if("""+ plotselection_tau32_anti_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=5;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=6;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=7;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=8;
                            break;
                        }
                    }                
                }
            } else {
                if("""+ plotselection_tau32_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=9;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=10;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=11;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=12;
                            break;
                        }
                    }                
                }
                if("""+ plotselection_tau32_anti_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=13;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=14;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=15;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
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

"""
,
"""
int ABCD10_Category(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Ws_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt, float const* Tops_ABCD"""+radi+"""_Pt, float const* Bottoms_ABCD"""+radi+"""_Pt, int N_Zprime_ABCD"""+radi+""",  float Evt_HT_Jets, float N_Jets, float N_packedPatJetsAK8PFCHSSoftDrop, float N_PrimaryVertices){
    int res=0;
    for (int i=0; i<N_Zprime_ABCD"""+radi+"""; i++){
        if ("""+ plotselection_ABCD_general_beta10_i +"""){
            if("""+ plotselection_topsubjetCSVv2_i +"""){
                if("""+ plotselection_TprimeMass_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=1;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=2;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=3;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=4;
                            break;
                        }
                    }                
                }
                if("""+ plotselection_TprimeMass_anti_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=5;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=6;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=7;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=8;
                            break;
                        }
                    }                
                }
            } else {
                if("""+ plotselection_TprimeMass_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=9;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=10;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=11;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=12;
                            break;
                        }
                    }                
                }
                if("""+ plotselection_TprimeMass_anti_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=13;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=14;
                            break;
                        }
                    }
                    if("""+ plotselection_B_CSV_anti_i + """){
                        if(""" + plotselection_W_tau21_i + """){
                            res=15;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
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

"""
,
  
"""int triggerresult(int Evt_Run,int Triggered_HLT_PFHT650_vX,int Triggered_HLT_PFHT800_vX,int Triggered_HLT_PFHT900_vX,int Triggered_HLT_PFJet450_vX){
    int result=0;
    if(Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFJet450_vX==1){result=1;}; //run H has damaged PFHT900 GeV
    return result;
}
"""
    
    ]

for ABCDversion,generalselection_i in zip(['ABCD1','ABCD2','ABCD3','ABCD4','ABCD5','ABCD6','ABCD7','ABCD8','ABCD9','ABCD10'],[plotselection_ABCD_general_beta_i,plotselection_ABCD_general_beta2_i,plotselection_ABCD_general_beta3_i,plotselection_ABCD_general_beta4_i,plotselection_ABCD_general_beta5_i,plotselection_ABCD_general_beta6_i,plotselection_ABCD_general_beta7_i,plotselection_ABCD_general_beta8_i,plotselection_ABCD_general_beta9_i,plotselection_ABCD_general_beta10_i]):
#for ABCDversion,generalselection_i in zip(['ABCD1'],[plotselection_ABCD_general_beta_i,plotselection_ABCD_general_beta2_i,plotselection_ABCD_general_beta3_i,plotselection_ABCD_general_beta4_i,plotselection_ABCD_general_beta5_i,plotselection_ABCD_general_beta6_i,plotselection_ABCD_general_beta7_i]):
    additionalfunctions=additionalfunctions+[


"""
float CSV_weights_""" + ABCDversion + """(float const* Zprimes_ABCD""" + radi + """_M, float const* Tprimes_ABCD""" + radi + """_M, float const* Tops_ABCD""" + radi + """_maxsubjetCSVv2, float const* Ws_ABCD""" + radi + """_MSD, float const* Ws_ABCD""" + radi + """_corrL2L3, float const* Tops_ABCD""" + radi + """_MSD, float const* Tops_ABCD""" + radi + """_corrL2L3, float const* Tops_ABCD""" + radi + """_t32, float const* Bottoms_ABCD""" + radi + """_CSV, float const* Ws_ABCD""" + radi + """_t21, float const* Ws_ABCD""" + radi + """_Pt, float const* Tops_ABCD""" + radi + """_Pt,  float const* Bottoms_ABCD""" + radi + """_Pt, float Evt_HT_Jets, float N_Jets, float N_packedPatJetsAK8PFCHSSoftDrop, int N_Zprime_ABCD""" + radi + """, float const* Bottoms_ABCD""" + radi + """_WeightCSVnominal, float const* Topsubjets_ABCD""" + radi + """_WeightCSVnominal, float N_PrimaryVertices){
    std::vector<float> weights;
    
    float CSVnominal=1.0;


    float tpt=0.0;
    float Wpt=0.0;
    float bpt=0.0;

    for (int i=0; i<N_Zprime_ABCD""" + radi + """; i++){
        if ("""+ generalselection_i +""" && Bottoms_ABCD""" + radi + """_WeightCSVnominal[i]>(-0.5)){         
            CSVnominal *= Bottoms_ABCD""" + radi + """_WeightCSVnominal[i];

            
            CSVnominal *= Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i];

                        
            break;
        }
    };
  
    
    return CSVnominal;
}

"""
,

"""
std::vector<float> toptag_weights_""" + ABCDversion + """(float const* Zprimes_ABCD""" + radi + """_M, float const* Tprimes_ABCD""" + radi + """_M, float const* Tops_ABCD""" + radi + """_maxsubjetCSVv2, float const* Ws_ABCD""" + radi + """_MSD, float const* Ws_ABCD""" + radi + """_corrL2L3, float const* Tops_ABCD""" + radi + """_MSD, float const* Tops_ABCD""" + radi + """_corrL2L3, float const* Tops_ABCD""" + radi + """_t32, float const* Bottoms_ABCD""" + radi + """_CSV, float const* Ws_ABCD""" + radi + """_t21, float const* Ws_ABCD""" + radi + """_Pt, float const* Tops_ABCD""" + radi + """_Pt,  float const* Bottoms_ABCD""" + radi + """_Pt, float Evt_HT_Jets, float N_Jets, float N_packedPatJetsAK8PFCHSSoftDrop, int N_Zprime_ABCD""" + radi + """, float const* Tops_ABCD""" + radi + """_real, float const* Tops_ABCD""" + radi + """_matcheddecays, float N_PrimaryVertices){
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
    
    
    for (int i=0; i<N_Zprime_ABCD""" + radi + """; i++){
        if (""" + generalselection_i + """ && Tops_ABCD""" + radi + """_real[i]==1){
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

"""
std::vector<float> Wtag_weights_""" + ABCDversion + """(float const* Zprimes_ABCD""" + radi + """_M, float const* Tprimes_ABCD""" + radi + """_M, float const* Tops_ABCD""" + radi + """_maxsubjetCSVv2, float const* Ws_ABCD""" + radi + """_MSD, float const* Ws_ABCD""" + radi + """_corrL2L3, float const* Tops_ABCD""" + radi + """_MSD, float const* Tops_ABCD""" + radi + """_corrL2L3, float const* Tops_ABCD""" + radi + """_t32, float const* Bottoms_ABCD""" + radi + """_CSV, float const* Ws_ABCD""" + radi + """_t21, float const* Ws_ABCD""" + radi + """_Pt, float const* Tops_ABCD""" + radi + """_Pt,  float const* Bottoms_ABCD""" + radi + """_Pt, float Evt_HT_Jets, float N_Jets, float N_packedPatJetsAK8PFCHSSoftDrop, int N_Zprime_ABCD""" + radi + """, float const* Ws_ABCD""" + radi + """_real, float const* Ws_ABCD""" + radi + """_matcheddecays, float N_PrimaryVertices){
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

    for (int i=0; i<N_Zprime_ABCD""" + radi + """; i++){
        //if ("""+ generalselection_i + """ && Ws_ABCD""" + radi + """_real[i]==1 && Ws_ABCD""" + radi + """_matcheddecays[i]>1){
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
        //}
    }
    
    weights.push_back(Wtagnominal);
    weights.push_back(Wtagup);
    weights.push_back(Wtagdown);
   
    
    return weights;
}

"""
  
]




additionalobjectsfromaddtionalrootfile=[
"""
  TFile* SFfile = new TFile("/nfs/dust/cms/user/skudella/pyroot-plotscripts/Zprime_SBSSSFs_Graphs.root","READONLY");
"""
]


additionalvariables=[
			#'bportionup:=(bbarportionweight(N_AK4_bottom_tag_candidates))[1]',
			#'bportiondown:=(bbarportionweight(N_AK4_bottom_tag_candidates))[2]',
			#'bportionno:=(bbarportionweight(N_AK4_bottom_tag_candidates))[3]',
			#'bportionnorm:=(bbarportionweight(N_AK4_bottom_tag_candidates))[0]',
			#"N_AK4_bottom_tag_candidates",
			#'IsnoSignalnotopbtag:=IsnoSignal_notopbtag(Zprimes_ABCD"+radi+"_M, Tprimes_ABCD"+radi+"_M, Tops_ABCD"+radi+"_maxsubjetCSVv2, Ws_ABCD"+radi+"_MSD, Tops_ABCD"+radi+"_MSD, Tops_ABCD"+radi+"_t32, Bottoms_ABCD"+radi+"_CSV, Ws_ABCD"+radi+"_t21, N_Zprime_ABCD"""+radi+""")',
			#'IsnoSignalwithtopbtag:=IsnoSignal_withtopbtag(Zprimes_ABCD"+radi+"_M, Tprimes_ABCD"+radi+"_M, Tops_ABCD"+radi+"_maxsubjetCSVv2, Ws_ABCD"+radi+"_MSD, Tops_ABCD"+radi+"_MSD, Tops_ABCD"+radi+"_t32, Bottoms_ABCD"+radi+"_CSV, Ws_ABCD"+radi+"_t21, N_Zprime_ABCD"""+radi+""")',
                        #'IsnoSignalinclusive:=IsnoSignal_inclusive(Zprimes_ABCD"+radi+"_M, Tprimes_ABCD"+radi+"_M, Ws_ABCD"+radi+"_MSD, Tops_ABCD"+radi+"_MSD, Tops_ABCD"+radi+"_t32, Bottoms_ABCD"+radi+"_CSV, Ws_ABCD"+radi+"_t21, N_Zprime_ABCD"""+radi+""")',
                        "N_Zprime_ABCD"+radi,"Zprimes_ABCD"+radi+"_M","Tprimes_ABCD"+radi+"_M","Tops_ABCD"+radi+"_maxsubjetCSVv2","Ws_ABCD"+radi+"_MSD","Tops_ABCD"+radi+"_MSD","Tops_ABCD"+radi+"_t32","Bottoms_ABCD"+radi+"_CSV","Ws_ABCD"+radi+"_t21",
                        
                        'ABCD1_CatID:=1.0 * ABCD1_Category(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3,   Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop, N_PrimaryVertices)',
                        'ABCD2_CatID:=1.0* ABCD2_Category(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3,   Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop, N_PrimaryVertices)',
                        'ABCD3_CatID:=1.0* ABCD3_Category(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3,   Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop, N_PrimaryVertices)',
                        'ABCD4_CatID:=1.0* ABCD4_Category(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3,   Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop, N_PrimaryVertices)',
                        'ABCD5_CatID:=1.0* ABCD5_Category(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3,   Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop, N_PrimaryVertices)',
                        'ABCD6_CatID:=1.0* ABCD6_Category(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3,   Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop, N_PrimaryVertices)',
                        'ABCD7_CatID:=1.0* ABCD6_Category(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3,   Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop, N_PrimaryVertices)',
                        'ABCD8_CatID:=1.0* ABCD8_Category(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3,   Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop, N_PrimaryVertices)',
                        'ABCD9_CatID:=1.0* ABCD9_Category(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3,   Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop, N_PrimaryVertices)',
                        'ABCD10_CatID:=1.0* ABCD10_Category(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3,   Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop, N_PrimaryVertices)',

                        'ABCD1_CatA_withtopbtag:=1',
                        'ABCD1_CatB_withtopbtag:=2',
                        'ABCD1_CatC_withtopbtag:=3',
                        'ABCD1_CatD_withtopbtag:=4',
                        'ABCD1_CatE_withtopbtag:=5',
                        'ABCD1_CatF_withtopbtag:=6',
                        'ABCD1_CatG_withtopbtag:=7',
                        'ABCD1_CatH_withtopbtag:=8',
                        
                        'ABCD1_CatA_notopbtag:=9',
                        'ABCD1_CatB_notopbtag:=10',
                        'ABCD1_CatC_notopbtag:=11',
                        'ABCD1_CatD_notopbtag:=12',
                        'ABCD1_CatE_notopbtag:=13',
                        'ABCD1_CatF_notopbtag:=14',
                        'ABCD1_CatG_notopbtag:=15',
                        'ABCD1_CatH_notopbtag:=16',
                        
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
                        
                        'ABCD3_CatA_withtopbtag:=1',
                        'ABCD3_CatB_withtopbtag:=2',
                        'ABCD3_CatC_withtopbtag:=3',
                        'ABCD3_CatD_withtopbtag:=4',
                        'ABCD3_CatE_withtopbtag:=5',
                        'ABCD3_CatF_withtopbtag:=6',
                        'ABCD3_CatG_withtopbtag:=7',
                        'ABCD3_CatH_withtopbtag:=8',
                        
                        'ABCD3_CatA_notopbtag:=9',
                        'ABCD3_CatB_notopbtag:=10',
                        'ABCD3_CatC_notopbtag:=11',
                        'ABCD3_CatD_notopbtag:=12',
                        'ABCD3_CatE_notopbtag:=13',
                        'ABCD3_CatF_notopbtag:=14',
                        'ABCD3_CatG_notopbtag:=15',
                        'ABCD3_CatH_notopbtag:=16',  
                        
                        
                        'ABCD4_CatA_withtopbtag:=1',
                        'ABCD4_CatB_withtopbtag:=2',
                        'ABCD4_CatC_withtopbtag:=3',
                        'ABCD4_CatD_withtopbtag:=4',
                        'ABCD4_CatE_withtopbtag:=5',
                        'ABCD4_CatF_withtopbtag:=6',
                        'ABCD4_CatG_withtopbtag:=7',
                        'ABCD4_CatH_withtopbtag:=8',
                        
                        'ABCD4_CatA_notopbtag:=9',
                        'ABCD4_CatB_notopbtag:=10',
                        'ABCD4_CatC_notopbtag:=11',
                        'ABCD4_CatD_notopbtag:=12',
                        'ABCD4_CatE_notopbtag:=13',
                        'ABCD4_CatF_notopbtag:=14',
                        'ABCD4_CatG_notopbtag:=15',
                        'ABCD4_CatH_notopbtag:=16',  
                        
                        'ABCD5_CatA_withtopbtag:=1',
                        'ABCD5_CatB_withtopbtag:=2',
                        'ABCD5_CatC_withtopbtag:=3',
                        'ABCD5_CatD_withtopbtag:=4',
                        'ABCD5_CatE_withtopbtag:=5',
                        'ABCD5_CatF_withtopbtag:=6',
                        'ABCD5_CatG_withtopbtag:=7',
                        'ABCD5_CatH_withtopbtag:=8',
                        
                        'ABCD5_CatA_notopbtag:=9',
                        'ABCD5_CatB_notopbtag:=10',
                        'ABCD5_CatC_notopbtag:=11',
                        'ABCD5_CatD_notopbtag:=12',
                        'ABCD5_CatE_notopbtag:=13',
                        'ABCD5_CatF_notopbtag:=14',
                        'ABCD5_CatG_notopbtag:=15',
                        'ABCD5_CatH_notopbtag:=16',  
                        
                        'ABCD6_CatA_withtopbtag:=1',
                        'ABCD6_CatB_withtopbtag:=2',
                        'ABCD6_CatC_withtopbtag:=3',
                        'ABCD6_CatD_withtopbtag:=4',
                        'ABCD6_CatE_withtopbtag:=5',
                        'ABCD6_CatF_withtopbtag:=6',
                        'ABCD6_CatG_withtopbtag:=7',
                        'ABCD6_CatH_withtopbtag:=8',
                        
                        'ABCD6_CatA_notopbtag:=9',
                        'ABCD6_CatB_notopbtag:=10',
                        'ABCD6_CatC_notopbtag:=11',
                        'ABCD6_CatD_notopbtag:=12',
                        'ABCD6_CatE_notopbtag:=13',
                        'ABCD6_CatF_notopbtag:=14',
                        'ABCD6_CatG_notopbtag:=15',
                        'ABCD6_CatH_notopbtag:=16',                         
                        
                        'ABCD7_CatA_withtopbtag:=1',
                        'ABCD7_CatB_withtopbtag:=2',
                        'ABCD7_CatC_withtopbtag:=3',
                        'ABCD7_CatD_withtopbtag:=4',
                        'ABCD7_CatE_withtopbtag:=5',
                        'ABCD7_CatF_withtopbtag:=6',
                        'ABCD7_CatG_withtopbtag:=7',
                        'ABCD7_CatH_withtopbtag:=8',
                        
                        'ABCD7_CatA_notopbtag:=9',
                        'ABCD7_CatB_notopbtag:=10',
                        'ABCD7_CatC_notopbtag:=11',
                        'ABCD7_CatD_notopbtag:=12',
                        'ABCD7_CatE_notopbtag:=13',
                        'ABCD7_CatF_notopbtag:=14',
                        'ABCD7_CatG_notopbtag:=15',
                        'ABCD7_CatH_notopbtag:=16', 
                        
                        'ABCD8_CatA_withtopbtag:=1',
                        'ABCD8_CatB_withtopbtag:=2',
                        'ABCD8_CatC_withtopbtag:=3',
                        'ABCD8_CatD_withtopbtag:=4',
                        'ABCD8_CatE_withtopbtag:=5',
                        'ABCD8_CatF_withtopbtag:=6',
                        'ABCD8_CatG_withtopbtag:=7',
                        'ABCD8_CatH_withtopbtag:=8',
                        
                        'ABCD8_CatA_notopbtag:=9',
                        'ABCD8_CatB_notopbtag:=10',
                        'ABCD8_CatC_notopbtag:=11',
                        'ABCD8_CatD_notopbtag:=12',
                        'ABCD8_CatE_notopbtag:=13',
                        'ABCD8_CatF_notopbtag:=14',
                        'ABCD8_CatG_notopbtag:=15',
                        'ABCD8_CatH_notopbtag:=16',  
                        
                        'ABCD9_CatA_withtopbtag:=1',
                        'ABCD9_CatB_withtopbtag:=2',
                        'ABCD9_CatC_withtopbtag:=3',
                        'ABCD9_CatD_withtopbtag:=4',
                        'ABCD9_CatE_withtopbtag:=5',
                        'ABCD9_CatF_withtopbtag:=6',
                        'ABCD9_CatG_withtopbtag:=7',
                        'ABCD9_CatH_withtopbtag:=8',
                        
                        'ABCD9_CatA_notopbtag:=9',
                        'ABCD9_CatB_notopbtag:=10',
                        'ABCD9_CatC_notopbtag:=11',
                        'ABCD9_CatD_notopbtag:=12',
                        'ABCD9_CatE_notopbtag:=13',
                        'ABCD9_CatF_notopbtag:=14',
                        'ABCD9_CatG_notopbtag:=15',
                        'ABCD9_CatH_notopbtag:=16',  
                        
                        'ABCD10_CatA_withtopbtag:=1',
                        'ABCD10_CatB_withtopbtag:=2',
                        'ABCD10_CatC_withtopbtag:=3',
                        'ABCD10_CatD_withtopbtag:=4',
                        'ABCD10_CatE_withtopbtag:=5',
                        'ABCD10_CatF_withtopbtag:=6',
                        'ABCD10_CatG_withtopbtag:=7',
                        'ABCD10_CatH_withtopbtag:=8',
                        
                        'ABCD10_CatA_notopbtag:=9',
                        'ABCD10_CatB_notopbtag:=10',
                        'ABCD10_CatC_notopbtag:=11',
                        'ABCD10_CatD_notopbtag:=12',
                        'ABCD10_CatE_notopbtag:=13',
                        'ABCD10_CatF_notopbtag:=14',
                        'ABCD10_CatG_notopbtag:=15',
                        'ABCD10_CatH_notopbtag:=16',  
                        'triggered:=triggerresult(Evt_Run, Triggered_HLT_PFHT650_vX, Triggered_HLT_PFHT800_vX, Triggered_HLT_PFHT900_vX, Triggered_HLT_PFJet450_vX)',
                               
]

for ABCDversion in ['ABCD1','ABCD2','ABCD3','ABCD4','ABCD5','ABCD6','ABCD7','ABCD8','ABCD9','ABCD10']:
#for ABCDversion in ['ABCD1']:
    additionalvariables=additionalvariables+[

                        '' + ABCDversion + '_WeightCSVnominal:=(CSV_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt, Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop, N_Zprime_ABCD' + radi + ',Bottoms_ABCD' + radi + '_WeightCSVnominal,Topsubjets_ABCD' + radi + '_WeightCSVnominal, N_PrimaryVertices))',

                        ABCDversion + '_Wtagweightnominal:=(Wtag_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt, Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop, N_Zprime_ABCD' + radi + ', Tops_ABCD' + radi + '_real, Tops_ABCD' + radi + '_matcheddecays, N_PrimaryVertices))[0]',
                        ABCDversion + '_toptagweightnominal:=(toptag_weights_' + ABCDversion + '(Zprimes_ABCD' + radi + '_M, Tprimes_ABCD' + radi + '_M, Tops_ABCD' + radi + '_maxsubjetCSVv2, Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3, Tops_ABCD' + radi + '_t32, Bottoms_ABCD' + radi + '_CSV, Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt, Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop, N_Zprime_ABCD' + radi + ', Tops_ABCD' + radi + '_real, Tops_ABCD' + radi + '_matcheddecays, N_PrimaryVertices))[0]',

                        'PDF_RMSMean:=PDF_RMS('+ stringforPDFs1 +')[0]',

                        'MCSF_Weight_' + ABCDversion + ':=' + ABCDversion + '_toptagweightnominal*' + ABCDversion + '_Wtagweightnominal*' + ABCDversion + '_WeightCSVnominal*Weight_pu69p2*PDF_RMSMean*triggered',
                        #'MCSF_Weight_' + ABCDversion + ':=' + ABCDversion + '_toptagweightnominal*' + ABCDversion + '_Wtagweightnominal*' + ABCDversion + '_WeightCSVnominal*Weight_pu69p2',
                        #'MCSF_Weight_' + ABCDversion + ':=' + ABCDversion + '_toptagweightnominal*' + ABCDversion + '_Wtagweightnominal*' + ABCDversion + '_WeightCSVnominal',
                        #'MCSF_Weight_' + ABCDversion + ':=' + ABCDversion + '_toptagweightnominal',


]