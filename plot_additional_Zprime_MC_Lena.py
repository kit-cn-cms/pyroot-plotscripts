from plot_cuts_ZPrime_MC_Lena import *

additionalfunctions=[
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
#"""
#bool IsnoSignal_notopbtag(float const* Zprimes_ABCD_M, float const* Tprimes_ABCD_M, float const* Tops_ABCD_maxsubjetCSVv2, float const* Ws_ABCD_MSD, float const* Tops_ABCD_MSD, float const* Tops_ABCD_t32, float const* Bottoms_ABCD_CSV, float const* Ws_ABCD_t21,int N_Zprime_ABCD"""+radi+"""){
    #bool res=true;
    #for (int i=0; i<N_Zprime_ABCD"""+radi+"""; i++){
        #if ("""+plotselection_topsubjetCSVv2_anti_i + " && " + plotselection_ABCD_general_beta_i + " && " + plotselection_tau32_i + " && " + plotselection_W_tau21_i + " && " + plotselection_B_CSV_i+"""){
            #res=false;
            #break;
        #}
    #}

    #return res;
#}

#""",
#"""
#bool IsnoSignal_withtopbtag(float const* Zprimes_ABCD_M, float const* Tprimes_ABCD_M, float const* Tops_ABCD_maxsubjetCSVv2, float const* Ws_ABCD_MSD, float const* Tops_ABCD_MSD, float const* Tops_ABCD_t32, float const* Bottoms_ABCD_CSV, float const* Ws_ABCD_t21,int N_Zprime_ABCD"""+radi+"""){
    #bool res=true;
    #for (int i=0; i<N_Zprime_ABCD"""+radi+"""; i++){
        #if ("""+plotselection_topsubjetCSVv2_i + " && " + plotselection_ABCD_general_beta_i + " && " + plotselection_tau32_i + " && " + plotselection_W_tau21_i + " && " + plotselection_B_CSV_i+"""){
            #res=false;
            #break;
        #}
    #}
    #return res;
#}

#""",
#"""
#bool IsnoSignal_inclusive(float const* Zprimes_ABCD_M, float const* Tprimes_ABCD_M, float const* Ws_ABCD_MSD, float const* Tops_ABCD_MSD, float const* Tops_ABCD_t32, float const* Bottoms_ABCD_CSV, float const* Ws_ABCD_t21,int N_Zprime_ABCD"""+radi+"""){
    #bool res=true;
    #for (int i=0; i<N_Zprime_ABCD"""+radi+"""; i++){
        #if ("""+ plotselection_ABCD_general_beta_i + " && " + plotselection_tau32_i + " && " + plotselection_W_tau21_i + " && " + plotselection_B_CSV_i+"""){
            #res=false;
            #break;
        #}
    #}
    #return res;
#}
#"""  ,

"""
int ABCD_Category(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt,int N_Zprime_ABCD"""+radi+""",  float Evt_HT){
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
int ABCD2_Category(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt,int N_Zprime_ABCD"""+radi+""",  float Evt_HT){
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
int ABCD3_Category(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt,int N_Zprime_ABCD"""+radi+""",  float Evt_HT){
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
int ABCD4_Category(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt,int N_Zprime_ABCD"""+radi+""",  float Evt_HT){
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
int ABCD5_Category(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt,int N_Zprime_ABCD"""+radi+""",  float Evt_HT){
    int res=0;
    for (int i=0; i<N_Zprime_ABCD"""+radi+"""; i++){
        if ("""+ plotselection_ABCD_general_beta5_i +"""){
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
int ABCD6_Category(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt,int N_Zprime_ABCD"""+radi+""",  float Evt_HT){
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
int ABCD7_Category(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt,int N_Zprime_ABCD"""+radi+""",  float Evt_HT){
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

"""
#"""
#std::vector<int> ABCD_Category_list(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt,int N_Zprime_ABCD"""+radi+"""){
    #std::vector<int> res;
    #res.assign(17,0);
    #int CatID=0;
    #bool CatIDfound=false;
    #for (int i=0; i<N_Zprime_ABCD"""+radi+"""; i++){
        #if ("""+ plotselection_ABCD_general_beta_i +"""){
            #if("""+ plotselection_topsubjetCSVv2_i +"""){
                #if("""+ plotselection_W_tau21_i +"""){
                    #if("""+ plotselection_B_CSV_i + """){
                        #if(""" + plotselection_tau32_i + """){
                            #res.at(1)=1;
                            #if(!CatIDfound){
                                #res.at(0)=1;
                                #CatIDfound=true;
                            #}
                        #}
                        #if(""" + plotselection_tau32_anti_i + """){
                            #res.at(2)=1;
                            #if(!CatIDfound){
                                #res.at(0)=2;
                                #CatIDfound=true;
                            #}
                        #}
                    #}
                    #if("""+ plotselection_B_CSV_anti_i + """){
                        #if(""" + plotselection_tau32_i + """){
                            #res.at(3)=1;
                            #if(!CatIDfound){
                                #res.at(0)=3;
                                #CatIDfound=true;
                            #}
                        #}
                        #if(""" + plotselection_tau32_anti_i + """){
                            #res.at(4)=1;
                            #if(!CatIDfound){
                                #res.at(0)=4;
                                #CatIDfound=true;
                            #}
                        #}
                    #}                
                #}
                #if("""+ plotselection_W_tau21_anti_i +"""){
                    #if("""+ plotselection_B_CSV_i + """){
                        #if(""" + plotselection_tau32_i + """){
                            #res.at(5)=1;
                            #if(!CatIDfound){
                                #res.at(0)=5;
                                #CatIDfound=true;
                            #}
                        #}
                        #if(""" + plotselection_tau32_anti_i + """){
                            #res.at(6)=1;
                            #if(!CatIDfound){
                                #res.at(0)=6;
                                #CatIDfound=true;
                            #}
                        #}
                    #}
                    #if("""+ plotselection_B_CSV_anti_i + """){
                        #if(""" + plotselection_tau32_i + """){
                            #res.at(7)=1;
                            #if(!CatIDfound){
                                #res.at(0)=7;
                                #CatIDfound=true;
                            #}
                        #}
                        #if(""" + plotselection_tau32_anti_i + """){
                            #res.at(8)=1;
                            #if(!CatIDfound){
                                #res.at(0)=8;
                                #CatIDfound=true;
                            #}
                        #}
                    #}                
                #}
            #} else {
                #if("""+ plotselection_W_tau21_i +"""){
                    #if("""+ plotselection_B_CSV_i + """){
                        #if(""" + plotselection_tau32_i + """){
                            #res.at(9)=1;
                            #if(!CatIDfound){
                                #res.at(0)=9;
                                #CatIDfound=true;
                            #}
                        #}
                        #if(""" + plotselection_tau32_anti_i + """){
                            #res.at(10)=1;
                            #if(!CatIDfound){
                                #res.at(0)=10;
                                #CatIDfound=true;
                            #}
                        #}
                    #}
                    #if("""+ plotselection_B_CSV_anti_i + """){
                        #if(""" + plotselection_tau32_i + """){
                            #res.at(11)=1;
                            #if(!CatIDfound){
                                #res.at(0)=11;
                                #CatIDfound=true;
                            #}
                        #}
                        #if(""" + plotselection_tau32_anti_i + """){
                            #res.at(12)=1;
                            #if(!CatIDfound){
                                #res.at(0)=12;
                                #CatIDfound=true;
                            #}
                        #}
                    #}                
                #}
                #if("""+ plotselection_W_tau21_anti_i +"""){
                    #if("""+ plotselection_B_CSV_i + """){
                        #if(""" + plotselection_tau32_i + """){
                            #res.at(13)=1;
                            #if(!CatIDfound){
                                #res.at(0)=13;
                                #CatIDfound=true;
                            #}
                        #}
                        #if(""" + plotselection_tau32_anti_i + """){
                            #res.at(14)=1;
                            #if(!CatIDfound){
                                #res.at(0)=14;
                                #CatIDfound=true;
                            #}
                        #}
                    #}
                    #if("""+ plotselection_B_CSV_anti_i + """){
                        #if(""" + plotselection_tau32_i + """){
                            #res.at(15)=1;
                            #if(!CatIDfound){
                                #res.at(0)=15;
                                #CatIDfound=true;
                            #}
                        #}
                        #if(""" + plotselection_tau32_anti_i + """){
                            #res.at(16)=1;
                            #if(!CatIDfound){
                                #res.at(0)=16;
                                #CatIDfound=true;
                            #}
                        #}
                    #}                
                #}
            #}
        #}
    #}
    #return res;
#}

#""",
#"""
#std::vector<int> ABCD2_Category_list(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt,int N_Zprime_ABCD"""+radi+"""){
    #std::vector<int> res;
    #res.assign(18,0);
    #int CatID=0;
    #bool CatIDfound=false;
    #for (int i=0; i<N_Zprime_ABCD"""+radi+"""; i++){
        #if ("""+ plotselection_ABCD_general_beta2_i +"""){
            #if("""+ plotselection_topsubjetCSVv2_i +"""){
                #if("""+ plotselection_W_tau21_i +"""){
                    #if("""+ plotselection_B_CSV_i + """){
                        #if(""" + plotselection_t_MSD_i + """){
                            #res.at(1)=1;
                            #if(!CatIDfound){
                                #res.at(0)=1;
                                #CatIDfound=true;
                            #}
                        #}
                        #if(""" + plotselection_t_MSD_anti_i + """){
                            #res.at(2)=1;
                            #if(!CatIDfound){
                                #res.at(0)=2;
                                #CatIDfound=true;
                            #}
                        #}
                    #}
                    #if("""+ plotselection_B_CSV_anti_i + """){
                        #if(""" + plotselection_t_MSD_i + """){
                            #res.at(3)=1;
                            #if(!CatIDfound){
                                #res.at(0)=3;
                                #CatIDfound=true;
                            #}
                        #}
                        #if(""" + plotselection_t_MSD_anti_i + """){
                            #res.at(4)=1;
                            #if(!CatIDfound){
                                #res.at(0)=4;
                                #CatIDfound=true;
                            #}
                        #}
                    #}                
                #}
                #if("""+ plotselection_W_tau21_anti_i +"""){
                    #if("""+ plotselection_B_CSV_i + """){
                        #if(""" + plotselection_t_MSD_i + """){
                            #res.at(5)=1;
                            #if(!CatIDfound){
                                #res.at(0)=5;
                                #CatIDfound=true;
                            #}
                        #}
                        #if(""" + plotselection_t_MSD_anti_i + """){
                            #res.at(6)=1;
                            #if(!CatIDfound){
                                #res.at(0)=6;
                                #CatIDfound=true;
                            #}
                        #}
                    #}
                    #if("""+ plotselection_B_CSV_anti_i + """){
                        #if(""" + plotselection_t_MSD_i + """){
                            #res.at(7)=1;
                            #if(!CatIDfound){
                                #res.at(0)=7;
                                #CatIDfound=true;
                            #}
                        #}
                        #if(""" + plotselection_t_MSD_anti_i + """){
                            #res.at(8)=1;
                            #if(!CatIDfound){
                                #res.at(0)=8;
                                #CatIDfound=true;
                            #}
                        #}
                    #}                
                #}
            #} else {
                #if("""+ plotselection_W_tau21_i +"""){
                    #if("""+ plotselection_B_CSV_i + """){
                        #if(""" + plotselection_t_MSD_i + """){
                            #res.at(9)=1;
                            #if(!CatIDfound){
                                #res.at(0)=9;
                                #CatIDfound=true;
                            #}
                        #}
                        #if(""" + plotselection_t_MSD_anti_i + """){
                            #res.at(10)=1;
                            #if(!CatIDfound){
                                #res.at(0)=10;
                                #CatIDfound=true;
                            #}
                        #}
                    #}
                    #if("""+ plotselection_B_CSV_anti_i + """){
                        #if(""" + plotselection_t_MSD_i + """){
                            #res.at(11)=1;
                            #if(!CatIDfound){
                                #res.at(0)=11;
                                #CatIDfound=true;
                            #}
                        #}
                        #if(""" + plotselection_t_MSD_anti_i + """){
                            #res.at(12)=1;
                            #if(!CatIDfound){
                                #res.at(0)=12;
                                #CatIDfound=true;
                            #}
                        #}
                    #}                
                #}
                #if("""+ plotselection_W_tau21_anti_i +"""){
                    #if("""+ plotselection_B_CSV_i + """){
                        #if(""" + plotselection_t_MSD_i + """){
                            #res.at(13)=1;
                            #if(!CatIDfound){
                                #res.at(0)=13;
                                #CatIDfound=true;
                            #}
                        #}
                        #if(""" + plotselection_t_MSD_anti_i + """){
                            #res.at(14)=1;
                            #if(!CatIDfound){
                                #res.at(0)=14;
                                #CatIDfound=true;
                            #}
                        #}
                    #}
                    #if("""+ plotselection_B_CSV_anti_i + """){
                        #if(""" + plotselection_t_MSD_i + """){
                            #res.at(15)=1;
                            #if(!CatIDfound){
                                #res.at(0)=15;
                                #CatIDfound=true;
                            #}
                        #}
                        #if(""" + plotselection_t_MSD_anti_i + """){
                            #res.at(16)=1;
                            #if(!CatIDfound){
                                #res.at(0)=16;
                                #CatIDfound=true;
                            #}
                        #}
                    #}                
                #}
            #}
        #}
    #}
    #float numberofBKGCat=0;
        #for(int i=2;i++;i<(res.size()-1)){
            #if(res.at(i)==1){
                #numberofBKGCat+=1;
            #}
        #}
    #if(numberofBKGCat==0.0 || res[1]==1){
        #res.at(17)=1.0;
    #} else {
        #res.at(17)=1.0/numberofBKGCat;
    #}
    #return res;
#}

#""",



  
  
  
  
]




additionalobjectsfromaddtionalrootfile=[
"""
  TFile* SFfile = new TFile("/nfs/dust/cms/user/skudella/pyroot-plotscripts/Zprime_SBSSSFs_Graphs.root","READONLY");
"""
]


additionalvariables=[
			'bportionup:=(bbarportionweight(N_AK4_bottom_tag_candidates))[1]',
			'bportiondown:=(bbarportionweight(N_AK4_bottom_tag_candidates))[2]',
			'bportionno:=(bbarportionweight(N_AK4_bottom_tag_candidates))[3]',
			'bportionnorm:=(bbarportionweight(N_AK4_bottom_tag_candidates))[0]',
			"N_AK4_bottom_tag_candidates",
			#'IsnoSignalnotopbtag:=IsnoSignal_notopbtag(Zprimes_ABCD"+radi+"_M, Tprimes_ABCD"+radi+"_M, Tops_ABCD"+radi+"_maxsubjetCSVv2, Ws_ABCD"+radi+"_MSD, Tops_ABCD"+radi+"_MSD, Tops_ABCD"+radi+"_t32, Bottoms_ABCD"+radi+"_CSV, Ws_ABCD"+radi+"_t21, N_Zprime_ABCD"""+radi+""")',
			#'IsnoSignalwithtopbtag:=IsnoSignal_withtopbtag(Zprimes_ABCD"+radi+"_M, Tprimes_ABCD"+radi+"_M, Tops_ABCD"+radi+"_maxsubjetCSVv2, Ws_ABCD"+radi+"_MSD, Tops_ABCD"+radi+"_MSD, Tops_ABCD"+radi+"_t32, Bottoms_ABCD"+radi+"_CSV, Ws_ABCD"+radi+"_t21, N_Zprime_ABCD"""+radi+""")',
                        #'IsnoSignalinclusive:=IsnoSignal_inclusive(Zprimes_ABCD"+radi+"_M, Tprimes_ABCD"+radi+"_M, Ws_ABCD"+radi+"_MSD, Tops_ABCD"+radi+"_MSD, Tops_ABCD"+radi+"_t32, Bottoms_ABCD"+radi+"_CSV, Ws_ABCD"+radi+"_t21, N_Zprime_ABCD"""+radi+""")',
                        "N_Zprime_ABCD"+radi,"Zprimes_ABCD"+radi+"_M","Tprimes_ABCD"+radi+"_M","Tops_ABCD"+radi+"_maxsubjetCSVv2","Ws_ABCD"+radi+"_MSD","Tops_ABCD"+radi+"_MSD","Tops_ABCD"+radi+"_t32","Bottoms_ABCD"+radi+"_CSV","Ws_ABCD"+radi+"_t21",
                        
                        'ABCD_CatID:=1.0 * ABCD_Category(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD,   Tops_ABCD'+radi+'_MSD,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT)',
                        'ABCD2_CatID:=1.0* ABCD2_Category(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD,   Tops_ABCD'+radi+'_MSD,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT)',
                        'ABCD3_CatID:=1.0* ABCD3_Category(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD,   Tops_ABCD'+radi+'_MSD,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT)',
                        'ABCD4_CatID:=1.0* ABCD4_Category(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD,   Tops_ABCD'+radi+'_MSD,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT)',
                        'ABCD5_CatID:=1.0* ABCD5_Category(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD,   Tops_ABCD'+radi+'_MSD,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT)',
                        'ABCD6_CatID:=1.0* ABCD6_Category(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD,   Tops_ABCD'+radi+'_MSD,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT)',
                        'ABCD7_CatID:=1.0* ABCD6_Category(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD,   Tops_ABCD'+radi+'_MSD,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT)',
                        
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
                        
                        #'ABCD_Eventreweight:=ABCD_Category_list(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD,   Tops_ABCD'+radi+'_MSD,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, N_Zprime_ABCD"""+radi+""")[17]',
                        
]