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
bool anti_loose_btag_new(float const* Bottoms_ABCD""" +  radi + """_CSV,float const* Bottoms_ABCD""" +  radi + """_Pt, float const* Ws_ABCD""" + radi + """_Pt, float const* Tops_ABCD""" + radi + """_Pt, int N_Zprime_ABCD""" +  radi + """, float currentTopPt, float currentWPt){
    float anti_tag=true;
    for (int i=0; i<N_Zprime_ABCD""" +  radi + """; i++){
        if(abs(currentWPt-Ws_ABCD""" + radi + """_Pt[i])>0.1 || abs(currentTopPt-Tops_ABCD""" + radi + """_Pt[i])>0.1){
            continue;
        }
        if(Bottoms_ABCD""" +  radi + """_CSV[i]>0.46){
            //std::cout<<"bottomcsv"<<bottomCSVs[i]<<endl;
            anti_tag=false;
        }
    }
            //std::cout<<"anti_tag"<<anti_tag<<endl;
    return anti_tag;
}
""",



"""
int ABCD_Category(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Ws_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt, float const* Tops_ABCD"""+radi+"""_Pt, float const* Bottoms_ABCD"""+radi+"""_Pt, int N_Zprime_ABCD"""+radi+""",  float Evt_HT_Jets, float N_Jets, float N_packedPatJetsAK8PFCHSSoftDrop){
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
int ABCD2_Category(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Ws_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt, float const* Tops_ABCD"""+radi+"""_Pt, float const* Bottoms_ABCD"""+radi+"""_Pt, int N_Zprime_ABCD"""+radi+""",  float Evt_HT_Jets, float N_Jets, float N_packedPatJetsAK8PFCHSSoftDrop){
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
int ABCD3_Category(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Ws_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt, float const* Tops_ABCD"""+radi+"""_Pt, float const* Bottoms_ABCD"""+radi+"""_Pt, int N_Zprime_ABCD"""+radi+""",  float Evt_HT_Jets, float N_Jets, float N_packedPatJetsAK8PFCHSSoftDrop){
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
int ABCD4_Category(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Ws_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt, float const* Tops_ABCD"""+radi+"""_Pt, float const* Bottoms_ABCD"""+radi+"""_Pt, int N_Zprime_ABCD"""+radi+""",  float Evt_HT_Jets, float N_Jets, float N_packedPatJetsAK8PFCHSSoftDrop){
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
int ABCD5_Category(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Ws_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt, float const* Tops_ABCD"""+radi+"""_Pt, float const* Bottoms_ABCD"""+radi+"""_Pt, int N_Zprime_ABCD"""+radi+""",  float Evt_HT_Jets, float N_Jets, float N_packedPatJetsAK8PFCHSSoftDrop){
    int res=0;
    //float current_bottom_pt=0;
    for (int i=0; i<N_Zprime_ABCD"""+radi+"""; i++){
        //if (current_bottom_pt-)
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
                    else if("""+ plotselection_B_CSV_anti_i + """ || anti_loose_btag_new(Bottoms_ABCD""" +  radi + """_CSV, Bottoms_ABCD""" +  radi + """_Pt, Ws_ABCD""" + radi + """_Pt, Tops_ABCD""" + radi + """_Pt, N_Zprime_ABCD""" +  radi + """, Tops_ABCD"""+radi+"""_Pt[i], Ws_ABCD""" + radi + """_Pt[i])){
                        if(""" + plotselection_W_tau21_i + """){
                            res=3;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=4;
                            break;
                        }
                    }  
                    else{
                            break;
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
                    else if("""+ plotselection_B_CSV_anti_i + """ || anti_loose_btag_new(Bottoms_ABCD""" +  radi + """_CSV, Bottoms_ABCD""" +  radi + """_Pt, Ws_ABCD""" + radi + """_Pt, Tops_ABCD""" + radi + """_Pt, N_Zprime_ABCD""" +  radi + """, Tops_ABCD"""+radi+"""_Pt[i], Ws_ABCD""" + radi + """_Pt[i])){
                        if(""" + plotselection_W_tau21_i + """){
                            res=7;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=8;
                            break;
                        }
                    }  
                    else{
                            break;
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
                    else if("""+ plotselection_B_CSV_anti_i + """ || anti_loose_btag_new(Bottoms_ABCD""" +  radi + """_CSV, Bottoms_ABCD""" +  radi + """_Pt, Ws_ABCD""" + radi + """_Pt, Tops_ABCD""" + radi + """_Pt, N_Zprime_ABCD""" +  radi + """, Tops_ABCD"""+radi+"""_Pt[i], Ws_ABCD""" + radi + """_Pt[i])){
                        if(""" + plotselection_W_tau21_i + """){
                            res=11;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=12;
                            break;
                        }
                    }
                    else{
                            break;
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
                    else if("""+ plotselection_B_CSV_anti_i + """ || anti_loose_btag_new(Bottoms_ABCD""" +  radi + """_CSV, Bottoms_ABCD""" +  radi + """_Pt, Ws_ABCD""" + radi + """_Pt, Tops_ABCD""" + radi + """_Pt, N_Zprime_ABCD""" +  radi + """, Tops_ABCD"""+radi+"""_Pt[i], Ws_ABCD""" + radi + """_Pt[i])){
                        if(""" + plotselection_W_tau21_i + """){
                            res=15;
                            break;
                        }
                        if(""" + plotselection_W_tau21_anti_i + """){
                            res=16;
                            break;
                        }
                    }
                    else{
                            break;
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
int ABCD6_Category(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Ws_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt, float const* Tops_ABCD"""+radi+"""_Pt, float const* Bottoms_ABCD"""+radi+"""_Pt, int N_Zprime_ABCD"""+radi+""",  float Evt_HT_Jets, float N_Jets, float N_packedPatJetsAK8PFCHSSoftDrop){
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
int ABCD7_Category(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Ws_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt, float const* Tops_ABCD"""+radi+"""_Pt, float const* Bottoms_ABCD"""+radi+"""_Pt, int N_Zprime_ABCD"""+radi+""",  float Evt_HT_Jets, float N_Jets, float N_packedPatJetsAK8PFCHSSoftDrop){
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
,
"""
int ABCD8_Category(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Ws_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt, float const* Tops_ABCD"""+radi+"""_Pt, float const* Bottoms_ABCD"""+radi+"""_Pt, int N_Zprime_ABCD"""+radi+""",  float Evt_HT_Jets, float N_Jets, float N_packedPatJetsAK8PFCHSSoftDrop){
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

"""
,
"""
int ABCD9_Category(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Ws_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt, float const* Tops_ABCD"""+radi+"""_Pt, float const* Bottoms_ABCD"""+radi+"""_Pt, int N_Zprime_ABCD"""+radi+""",  float Evt_HT_Jets, float N_Jets, float N_packedPatJetsAK8PFCHSSoftDrop){
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
int ABCD10_Category(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Ws_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt, float const* Tops_ABCD"""+radi+"""_Pt, float const* Bottoms_ABCD"""+radi+"""_Pt, int N_Zprime_ABCD"""+radi+""",  float Evt_HT_Jets, float N_Jets, float N_packedPatJetsAK8PFCHSSoftDrop){
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
"""
float calc_sqrts(int const N_Jets, float const* Jet_Pt, float const* Jet_Phi, float const* Jet_Eta, float const* Jet_E){
    //std::vector<TLorentzVector> Jets;
    TLorentzVector sqrts;
    for(int i; i<N_Jets;i++){
        TLorentzVector Jet;
        Jet.SetPtEtaPhiE(Jet_Pt[i],Jet_Eta[i],Jet_Phi[i],Jet_E[i]);
        //Jets.push_back(Jet);
        sqrts=sqrts+Jet;
    };
    return sqrts.M();
}
"""

,
"""
std::vector <float> Zprime_minus_Evt_HT(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Ws_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt, float const* Tops_ABCD"""+radi+"""_Pt, float const* Bottoms_ABCD"""+radi+"""_Pt, int N_Zprime_ABCD"""+radi+""",  float Evt_HT_Jets, float N_Jets, float N_packedPatJetsAK8PFCHSSoftDrop){
    std::vector <float> res;
    res.push_back(-20000.0);
    res.push_back(-20000.0);
    
    for (int i=0; i<N_Zprime_ABCD"""+radi+"""; i++){
        if ("""+ plotselection_ABCD_general_beta10_i +"""){
            if("""+plotselection_W_tau21_i  +"""){
                if("""+ plotselection_TprimeMass_i +"""){
                    if("""+ plotselection_B_CSV_i + """){
                        if(""" + plotselection_topsubjetCSVv2_i + """){
                            res[0]=(Zprimes_ABCD"""+radi+"""_M[i]-Evt_HT_Jets)/Zprimes_ABCD"""+radi+"""_M[i];
                            break;
                        }else{
                            res[1]=(Zprimes_ABCD"""+radi+"""_M[i]-Evt_HT_Jets)/Zprimes_ABCD"""+radi+"""_M[i];
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
std::vector <float> Evt_HT_minus_Zprime(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Ws_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt, float const* Tops_ABCD"""+radi+"""_Pt, float const* Bottoms_ABCD"""+radi+"""_Pt, int N_Zprime_ABCD"""+radi+""",  float Evt_HT_Jets, float N_Jets, float N_packedPatJetsAK8PFCHSSoftDrop){
    std::vector <float> res;
    res.push_back(-20000.0);
    res.push_back(-20000.0);
    res.push_back(-20000.0);
    res.push_back(-20000.0);
    
    for (int i=0; i<N_Zprime_ABCD"""+radi+"""; i++){
        if ("""+ plotselection_ABCD_general_beta5_i +"""){
            if("""+plotselection_W_MSD_i  +"""){
                        if(""" + plotselection_topsubjetCSVv2_i + """){
                            res[0]=(Zprimes_ABCD"""+radi+"""_M[i]-Evt_HT_Jets)/Zprimes_ABCD"""+radi+"""_M[i];
                            res[2]=Bottoms_ABCD"""+radi+"""_CSV[i];
                            break;
                        }else{
                            res[1]=(Zprimes_ABCD"""+radi+"""_M[i]-Evt_HT_Jets)/Zprimes_ABCD"""+radi+"""_M[i];
                            res[3]=Bottoms_ABCD"""+radi+"""_CSV[i];
                            break;
                        }
                        
                        
            }
        }
    }
    return res;
}
"""
,
"""
std::vector<int> btagged_jet_number(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Ws_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt, float const* Tops_ABCD"""+radi+"""_Pt, float const* Bottoms_ABCD"""+radi+"""_Pt, int N_Zprime_ABCD"""+radi+""",  float Evt_HT_Jets, float N_Jets, float N_packedPatJetsAK8PFCHSSoftDrop){
std::vector<int> res;
 for (int i=0; i<10; i++){res.push_back(0);};
 int j=0;
 float bottompt=0;
    for (int i=0; i<N_Zprime_ABCD"""+radi+"""; i++){
        if ("""+ plotselection_ABCD_general_beta5_i +"""){
                if("""+ plotselection_W_MSD_i +"""){
                    if("""+ plotselection_W_tau21_i + """){
                        if(abs(bottompt-Bottoms_ABCD"""+radi+"""_Pt[i])>0.1){
                            bottompt=Bottoms_ABCD"""+radi+"""_Pt[i];

                            if (j<=10 && """ + plotselection_B_CSV_i + """){res[j]=j+1;}
                            j++;
                        }
                    }            
                }
            
        }
    }
 return res;
}
""",
"""
std::vector<int> bcand_jet_number(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Ws_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt, float const* Tops_ABCD"""+radi+"""_Pt, float const* Bottoms_ABCD"""+radi+"""_Pt, int N_Zprime_ABCD"""+radi+""",  float Evt_HT_Jets, float N_Jets, float N_packedPatJetsAK8PFCHSSoftDrop){
std::vector<int> res;
 for (int i=0; i<10; i++){res.push_back(0);};
 int j=1;
 float bottompt=0;
    for (int i=0; i<N_Zprime_ABCD"""+radi+"""; i++){
        if ("""+ plotselection_ABCD_general_beta5_i +"""){
                if("""+ plotselection_W_MSD_i +"""){
                    if("""+ plotselection_W_tau21_i + """){
                        if(abs(bottompt-Bottoms_ABCD"""+radi+"""_Pt[i])>0.1){
                            bottompt=Bottoms_ABCD"""+radi+"""_Pt[i];
                            j++;
                        }
                    }            
                }
            
        }
    }
 if (j<=10){res[j]=j;};

 return res;
}
"""
,
"""
std::vector<int> Wtagged_jet_number(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Ws_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt, float const* Tops_ABCD"""+radi+"""_Pt, float const* Bottoms_ABCD"""+radi+"""_Pt, int N_Zprime_ABCD"""+radi+""",  float Evt_HT_Jets, float N_Jets, float N_packedPatJetsAK8PFCHSSoftDrop){
std::vector<int> res;
 for (int i=0; i<10; i++){res.push_back(0);};
 int j=0;
 float Wpt=0;
    for (int i=0; i<N_Zprime_ABCD"""+radi+"""; i++){
        if ("""+ plotselection_ABCD_general_beta5_i +"""){
                //if("""+ plotselection_W_MSD_i +"""){
                    //if("""+ plotselection_W_MSD_i + """){
                        if(abs(Wpt-Ws_ABCD"""+radi+"""_Pt[i])>0.1){
                            Wpt=Ws_ABCD"""+radi+"""_Pt[i];

                            if (j<=10 && """ + plotselection_W_tau21_i + """&& """ + plotselection_W_MSD_i + """){res[j]=j+1;}
                            j++;
                        }
                    //}            
                //}
            
        }
    }
 return res;
}
""",
"""
std::vector<int> Wcand_jet_number(float const* Zprimes_ABCD"""+radi+"""_M, float const* Tprimes_ABCD"""+radi+"""_M, float const* Tops_ABCD"""+radi+"""_maxsubjetCSVv2, float const* Ws_ABCD"""+radi+"""_MSD, float const* Ws_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_MSD, float const* Tops_ABCD"""+radi+"""_corrL2L3, float const* Tops_ABCD"""+radi+"""_t32, float const* Bottoms_ABCD"""+radi+"""_CSV, float const* Ws_ABCD"""+radi+"""_t21, float const* Ws_ABCD"""+radi+"""_Pt, float const* Tops_ABCD"""+radi+"""_Pt, float const* Bottoms_ABCD"""+radi+"""_Pt, int N_Zprime_ABCD"""+radi+""",  float Evt_HT_Jets, float N_Jets, float N_packedPatJetsAK8PFCHSSoftDrop){
std::vector<int> res;
 for (int i=0; i<10; i++){res.push_back(0);};
 int j=1;
 float Wpt=0;
    for (int i=0; i<N_Zprime_ABCD"""+radi+"""; i++){
        if ("""+ plotselection_ABCD_general_beta5_i +"""){
                //if("""+ plotselection_W_MSD_i +"""){
                    //if("""+ plotselection_W_tau21_i + """){
                        if(abs(Wpt-Ws_ABCD"""+radi+"""_Pt[i])>0.1){
                            Wpt=Ws_ABCD"""+radi+"""_Pt[i];
                            j++;
                        }
                    //}            
                //}
            
        }
    }
 if (j<=10){res[j]=j;};
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
			#'IsnoSignalnotopbtag:=IsnoSignal_notopbtag(Zprimes_ABCD"+radi+"_M, Tprimes_ABCD"+radi+"_M, Tops_ABCD"+radi+"_maxsubjetCSVv2, Ws_ABCD"+radi+"_MSD, Tops_ABCD"+radi+"_MSD, Tops_ABCD"+radi+"_t32, Bottoms_ABCD"+radi+"_CSV, Ws_ABCD"+radi+"_t21, N_Zprime_ABCD"""+radi+""")',
			#'IsnoSignalwithtopbtag:=IsnoSignal_withtopbtag(Zprimes_ABCD"+radi+"_M, Tprimes_ABCD"+radi+"_M, Tops_ABCD"+radi+"_maxsubjetCSVv2, Ws_ABCD"+radi+"_MSD, Tops_ABCD"+radi+"_MSD, Tops_ABCD"+radi+"_t32, Bottoms_ABCD"+radi+"_CSV, Ws_ABCD"+radi+"_t21, N_Zprime_ABCD"""+radi+""")',
                        #'IsnoSignalinclusive:=IsnoSignal_inclusive(Zprimes_ABCD"+radi+"_M, Tprimes_ABCD"+radi+"_M, Ws_ABCD"+radi+"_MSD, Tops_ABCD"+radi+"_MSD, Tops_ABCD"+radi+"_t32, Bottoms_ABCD"+radi+"_CSV, Ws_ABCD"+radi+"_t21, N_Zprime_ABCD"""+radi+""")',
                        "N_Zprime_ABCD"+radi,"Zprimes_ABCD"+radi+"_M","Tprimes_ABCD"+radi+"_M","Tops_ABCD"+radi+"_maxsubjetCSVv2","Ws_ABCD"+radi+"_MSD","Tops_ABCD"+radi+"_MSD","Tops_ABCD"+radi+"_t32","Bottoms_ABCD"+radi+"_CSV","Ws_ABCD"+radi+"_t21",
                        
                        'ABCD_CatID:=1.0 * ABCD_Category(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_MSD, Tops_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop)',
                        'ABCD2_CatID:=1.0* ABCD2_Category(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_MSD, Tops_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop)',
                        'ABCD3_CatID:=1.0* ABCD3_Category(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_MSD, Tops_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop)',
                        'ABCD4_CatID:=1.0* ABCD4_Category(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_MSD, Tops_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop)',
                        'ABCD5_CatID:=1.0* ABCD5_Category(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_MSD, Tops_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop)',
                        'ABCD6_CatID:=1.0* ABCD6_Category(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_MSD, Tops_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop)',
                        'ABCD7_CatID:=1.0* ABCD7_Category(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_MSD, Tops_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop)',
                        'ABCD8_CatID:=1.0* ABCD8_Category(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_MSD, Tops_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop)',
                        'ABCD9_CatID:=1.0* ABCD9_Category(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_MSD, Tops_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop)',
                        'ABCD10_CatID:=1.0* ABCD10_Category(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_MSD, Tops_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop)',


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
                        'Evt_sqrts:=calc_sqrts(N_Jets,Jet_Pt,Jet_Phi,Jet_Eta, Jet_E)',
                        'ZprimeminusEvtHT_wtb:=Zprime_minus_Evt_HT(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_MSD, Tops_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop)[0]',
                        'ZprimeminusEvtHT_ntb:=Zprime_minus_Evt_HT(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_MSD, Tops_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop)[1]',
                        'ZprimeminusEvtHT_wtb_vs_CSV_evtht:=Evt_HT_minus_Zprime(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_MSD, Tops_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop)[0]',
                        'ZprimeminusEvtHT_ntb_vs_CSV_evtht:=Evt_HT_minus_Zprime(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_MSD, Tops_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop)[1]',
                        'ZprimeminusEvtHT_wtb_vs_CSV_csv:=Evt_HT_minus_Zprime(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_MSD, Tops_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop)[2]',
                        'ZprimeminusEvtHT_ntb_vs_CSV_csv:=Evt_HT_minus_Zprime(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_MSD, Tops_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop)[3]',                           
                           
                        #'ZprimeminusSqrtS_wtb:=Zprime_minus_sqrtS(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_MSD, Tops_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop,Evt_sqrts)[0]',
                        #'ZprimeminusSqrtS_ntb:=Zprime_minus_sqrtS(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_MSD, Tops_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+', Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop,Evt_sqrts)[1]',
                                                
                        
                        
                        #'ABCD_Eventreweight:=ABCD_Category_list(Zprimes_ABCD'+radi+'_M,   Tprimes_ABCD'+radi+'_M,   Tops_ABCD'+radi+'_maxsubjetCSVv2,   Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_MSD, Tops_ABCD'+radi+'_corrL2L3,   Tops_ABCD'+radi+'_t32,   Bottoms_ABCD'+radi+'_CSV,   Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, N_Zprime_ABCD"""+radi+""")[0]',
                        
]

for l in range(1,11):
    print "check if this goes from 1 to 10 ",l
    additionalvariables=additionalvariables+[
    'bottom_jet_tagged_numbers'+str(l)+':=btagged_jet_number(Zprimes_ABCD'+radi+'_M, Tprimes_ABCD'+radi+'_M, Tops_ABCD'+radi+'_maxsubjetCSVv2, Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3, Tops_ABCD'+radi+'_MSD, Tops_ABCD'+radi+'_corrL2L3, Tops_ABCD'+radi+'_t32, Bottoms_ABCD'+radi+'_CSV, Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+',  Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop)['+str(l-1)+']',
    'bottom_jet_cand_numbers'+str(l)+':=bcand_jet_number(Zprimes_ABCD'+radi+'_M, Tprimes_ABCD'+radi+'_M, Tops_ABCD'+radi+'_maxsubjetCSVv2, Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3, Tops_ABCD'+radi+'_MSD, Tops_ABCD'+radi+'_corrL2L3, Tops_ABCD'+radi+'_t32, Bottoms_ABCD'+radi+'_CSV, Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+',  Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop)['+str(l-1)+']',
    
    'W_jet_tagged_numbers'+str(l)+':=Wtagged_jet_number(Zprimes_ABCD'+radi+'_M, Tprimes_ABCD'+radi+'_M, Tops_ABCD'+radi+'_maxsubjetCSVv2, Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3, Tops_ABCD'+radi+'_MSD, Tops_ABCD'+radi+'_corrL2L3, Tops_ABCD'+radi+'_t32, Bottoms_ABCD'+radi+'_CSV, Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+',  Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop)['+str(l-1)+']',
    'W_jet_cand_numbers'+str(l)+':=Wcand_jet_number(Zprimes_ABCD'+radi+'_M, Tprimes_ABCD'+radi+'_M, Tops_ABCD'+radi+'_maxsubjetCSVv2, Ws_ABCD'+radi+'_MSD, Ws_ABCD'+radi+'_corrL2L3, Tops_ABCD'+radi+'_MSD, Tops_ABCD'+radi+'_corrL2L3, Tops_ABCD'+radi+'_t32, Bottoms_ABCD'+radi+'_CSV, Ws_ABCD'+radi+'_t21, Ws_ABCD'+radi+'_Pt, Tops_ABCD'+radi+'_Pt, Bottoms_ABCD'+radi+'_Pt, N_Zprime_ABCD'+radi+',  Evt_HT_Jets, N_Jets, N_packedPatJetsAK8PFCHSSoftDrop)['+str(l-1)+']',
    
]