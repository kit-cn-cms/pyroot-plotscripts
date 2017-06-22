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
"""
bool IsnoSignal_notopbtag(float const* Zprimes_ABCD_M, float const* Tprimes_ABCD_M, float const* Tops_ABCD_maxsubjetCSVv2, float const* Ws_ABCD_MSD, float const* Tops_ABCD_MSD, float const* Tops_ABCD_t32, float const* Bottoms_ABCD_CSV, float const* Ws_ABCD_t21,int N_Zprime_ABCD){
    bool res=true;
    for (int i=0; i<N_Zprime_ABCD; i++){
        if ("""+plotselection_topsubjetCSVv2_anti_i + " && " + plotselection_ABCD_general_beta_i + " && " + plotselection_tau32_i + " && " + plotselection_W_tau21_i + " && " + plotselection_B_CSV_i+"""){
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
        if ("""+plotselection_topsubjetCSVv2_i + " && " + plotselection_ABCD_general_beta_i + " && " + plotselection_tau32_i + " && " + plotselection_W_tau21_i + " && " + plotselection_B_CSV_i+"""){
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
        if ("""+ plotselection_ABCD_general_beta_i + " && " + plotselection_tau32_i + " && " + plotselection_W_tau21_i + " && " + plotselection_B_CSV_i+"""){
            res=false;
            break;
        }
    }
    return res;
}
"""  ,

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

"""

  
  
  
  
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
                        
                        ]