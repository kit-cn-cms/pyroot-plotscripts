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
]