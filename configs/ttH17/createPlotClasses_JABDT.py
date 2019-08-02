import subprocess



Recolabels_THW = list(set([
    "Reco_tHW_btop_idx",
    "Reco_tHW_whaddau_idx1",
    "Reco_tHW_whaddau_idx2",
    "Reco_tHW_hdau_idx1",
    "Reco_tHW_hdau_idx2",
    "Reco_tHW_leptonictop",
    "Reco_tHW_top_m",
    "Reco_tHW_top_pt",
    "Reco_tHW_top_phi",
    "Reco_tHW_top_eta",
    "Reco_tHW_top_h_dr",
    "Reco_tHW_btop_m",
    "Reco_tHW_btop_pt",
    "Reco_tHW_btop_phi",
    "Reco_tHW_btop_eta",
    "Reco_tHW_btop_lepw_dr",
    "Reco_tHW_whad_m",
    "Reco_tHW_whad_pt",
    "Reco_tHW_whad_phi",
    "Reco_tHW_whad_eta",
    "Reco_tHW_whad_dr",
    "Reco_tHW_whaddau_m1",
    "Reco_tHW_whaddau_pt1",
    "Reco_tHW_whaddau_phi1",
    "Reco_tHW_whaddau_eta1",
    "Reco_tHW_whaddau_m2",
    "Reco_tHW_whaddau_pt2",
    "Reco_tHW_whaddau_phi2",
    "Reco_tHW_whaddau_eta2",
    "Reco_tHW_h_m",
    "Reco_tHW_h_pt",
    "Reco_tHW_h_phi",
    "Reco_tHW_h_eta",
    "Reco_tHW_h_dr",
    "Reco_tHW_hdau_m1",
    "Reco_tHW_hdau_pt1",
    "Reco_tHW_hdau_phi1",
    "Reco_tHW_hdau_eta1",
    "Reco_tHW_hdau_m2",
    "Reco_tHW_hdau_pt2",
    "Reco_tHW_hdau_phi2",
    "Reco_tHW_hdau_eta2",
    "Reco_tHW_top_m",
    "Reco_tHW_top_pt",
    "Reco_tHW_top_phi",
    "Reco_tHW_top_eta",
    "Reco_tHW_top_h_dr",
    "Reco_tHW_wtop_m",
    "Reco_tHW_wtop_pt",
    "Reco_tHW_wtop_phi",
    "Reco_tHW_wtop_eta",
    "Reco_tHW_wtop_h_dr",
    "Reco_tHW_wb_m",
    "Reco_tHW_wb_pt",
    "Reco_tHW_wb_phi",
    "Reco_tHW_wb_eta",
    "Reco_tHW_wb_h_dr",
    "Reco_JABDT_tHW_Jet_CSV_btop",
    "Reco_JABDT_tHW_Jet_CSV_hdau1",
    "Reco_JABDT_tHW_Jet_CSV_hdau2",
    "Reco_JABDT_tHW_log_top_m",
    "Reco_JABDT_tHW_log_top_pt",
    "Reco_JABDT_tHW_log_h_m",
    "Reco_JABDT_tHW_log_h_pt",
    "Reco_JABDT_tHW_log_wb_m",
    "Reco_JABDT_tHW_log_wb_pt",
    "Reco_JABDT_tHW_log_whad_m",
    "Reco_JABDT_tHW_log_whad_pt",
    "Reco_JABDT_tHW_wlep_pt__M__whad_pt",
    "Reco_JABDT_tHW_abs_wlep_eta__M__whad_eta",
    "Reco_JABDT_tHW_abs_top_eta__M__wb_eta",
    "Reco_JABDT_tHW_abs_btop_eta",
    "Reco_JABDT_tHW_abs_top_eta__M__higg_eta",
    "Reco_JABDT_tHW_abs_wb_eta",
    "Reco_JABDT_tHW_abs_top_eta",
    "Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",
    "Reco_JABDT_tHW_costheta_btop_lep",
]))

Recolabels_THQ = list(set([
    "Reco_tHq_top_m",
    "Reco_tHq_top_pt",
    "Reco_tHq_top_phi",
    "Reco_tHq_top_eta",
    "Reco_tHq_top_h_dr",
    "Reco_tHq_btop_m",
    "Reco_tHq_btop_pt",
    "Reco_tHq_btop_phi",
    "Reco_tHq_btop_eta",
    "Reco_tHq_btop_idx",
    "Reco_tHq_btop_lep_dr",
    "Reco_tHq_btop_w_dr",
    "Reco_tHq_ljet_m",
    "Reco_tHq_ljet_pt",
    "Reco_tHq_ljet_phi",
    "Reco_tHq_ljet_eta",
    "Reco_tHq_ljet_idx",
    "Reco_tHq_h_m",
    "Reco_tHq_h_pt",
    "Reco_tHq_h_phi",
    "Reco_tHq_h_eta",
    "Reco_tHq_h_dr",
    "Reco_tHq_hdau_m1",
    "Reco_tHq_hdau_pt1",
    "Reco_tHq_hdau_phi1",
    "Reco_tHq_hdau_eta1",
    "Reco_tHq_hdau_idx1",
    "Reco_tHq_hdau_m2",
    "Reco_tHq_hdau_pt2",
    "Reco_tHq_hdau_phi2",
    "Reco_tHq_hdau_eta2",
    "Reco_tHq_hdau_idx2",
    "Reco_tHq_costhetastar",
    "Reco_JABDT_tHq_log_top_m",
    "Reco_JABDT_tHq_log_top_pt",
    "Reco_JABDT_tHq_log_h_m",
    "Reco_JABDT_tHq_log_h_pt",
    "Reco_JABDT_tHq_log_ljet_pt",
    "Reco_JABDT_tHq_abs_top_eta",
    "Reco_JABDT_tHq_abs_btop_eta",
    "Reco_JABDT_tHq_abs_h_eta",
    "Reco_JABDT_tHq_abs_ljet_eta",
    "Reco_JABDT_tHq_abs_ljet_eta__M__btop_eta",
    "Reco_JABDT_tHq_abs_top_eta__M__higg_eta",
    "Reco_JABDT_tHq_Jet_CSV_hdau1",
    "Reco_JABDT_tHq_Jet_CSV_hdau2",
    "Reco_JABDT_tHq_Jet_CSV_btop",
    "Reco_JABDT_tHq_Jet_CSV_ljet",
    "Reco_JABDT_tHq_costheta_btop_lep",
    "Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt",
    "Reco_JABDT_tHq_ljet_e__M__btop_e",
    "Reco_JABDT_tHq_top_pt__P__h_pt__P__ljet_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",
]))

Recolabels_ttbar = list(set([
    "Reco_ttbar_btoplep_m",
    "Reco_ttbar_btoplep_pt",
    "Reco_ttbar_btoplep_phi",
    "Reco_ttbar_btoplep_eta",
    "Reco_ttbar_btoplep_idx",
    "Reco_ttbar_whad_m",
    "Reco_ttbar_whad_pt",
    "Reco_ttbar_whad_phi",
    "Reco_ttbar_whad_eta",
    "Reco_ttbar_whad_dr",
    "Reco_ttbar_whaddau_m1",
    "Reco_ttbar_whaddau_m2",
    "Reco_ttbar_whaddau_pt1",
    "Reco_ttbar_whaddau_pt2",
    "Reco_ttbar_whaddau_phi1",
    "Reco_ttbar_whaddau_phi2",
    "Reco_ttbar_whaddau_eta1",
    "Reco_ttbar_whaddau_eta2",
    "Reco_ttbar_whaddau_idx1",
    "Reco_ttbar_whaddau_idx2",
    "Reco_ttbar_btophad_m",
    "Reco_ttbar_btophad_pt",
    "Reco_ttbar_btophad_phi",
    "Reco_ttbar_btophad_eta",
    "Reco_ttbar_btophad_idx",
    "Reco_ttbar_tophad_m",
    "Reco_ttbar_tophad_pt",
    "Reco_ttbar_tophad_phi",
    "Reco_ttbar_tophad_eta",
    "Reco_ttbar_tophad_dr",
    "Reco_ttbar_toplep_m",
    "Reco_ttbar_toplep_pt",
    "Reco_ttbar_toplep_phi",
    "Reco_ttbar_toplep_eta",
    "Reco_LeptonicW_Eta",
    "Reco_LeptonicW_M",
    "Reco_LeptonicW_Phi",
    "Reco_LeptonicW_Pt",
    "Reco_JABDT_ttbar_log_whad_m",
    "Reco_JABDT_ttbar_Jet_CSV_btoplep",
    "Reco_JABDT_ttbar_Jet_CSV_btophad",
    "Reco_JABDT_ttbar_Jet_CSV_whaddau1",
    "Reco_JABDT_ttbar_Jet_CSV_whaddau2",
    "Reco_JABDT_ttbar_log_tophad_m__M__whad_m",
    "Reco_JABDT_ttbar_log_tophad_pt",
    "Reco_JABDT_ttbar_log_toplep_m",
    "Reco_JABDT_ttbar_log_toplep_pt",
    "Reco_JABDT_ttbar_tophad_pt__P__toplep_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",
    "Reco_JABDT_ttbar_costheta_toplep_tophad",
]))

Recolabels_ttH = list(set([
    "Reco_ttH_btoplep_m",
    "Reco_ttH_btoplep_pt",
    "Reco_ttH_btoplep_phi",
    "Reco_ttH_btoplep_eta",
    "Reco_ttH_btoplep_idx",
    "Reco_ttH_btoplep_w_dr",
    "Reco_ttH_whad_m",
    "Reco_ttH_whad_pt",
    "Reco_ttH_whad_phi",
    "Reco_ttH_whad_eta",
    "Reco_ttH_whad_dr",
    "Reco_ttH_whaddau_m1",
    "Reco_ttH_whaddau_pt1",
    "Reco_ttH_whaddau_phi1",
    "Reco_ttH_whaddau_eta1",
    "Reco_ttH_whaddau_idx1",
    "Reco_ttH_whaddau_m2",
    "Reco_ttH_whaddau_pt2",
    "Reco_ttH_whaddau_phi2",
    "Reco_ttH_whaddau_eta2",
    "Reco_ttH_whaddau_idx2",
    "Reco_ttH_btophad_m",
    "Reco_ttH_btophad_pt",
    "Reco_ttH_btophad_phi",
    "Reco_ttH_btophad_eta",
    "Reco_ttH_btophad_idx",
    "Reco_ttH_tophad_m",
    "Reco_ttH_tophad_pt",
    "Reco_ttH_tophad_phi",
    "Reco_ttH_tophad_eta",
    "Reco_ttH_tophad_dr",
    "Reco_ttH_toplep_m",
    "Reco_ttH_toplep_pt",
    "Reco_ttH_toplep_phi",
    "Reco_ttH_toplep_eta",
    "Reco_ttH_toplep_w_dr",
    "Reco_ttH_h_m",
    "Reco_ttH_h_pt",
    "Reco_ttH_h_phi",
    "Reco_ttH_h_eta",
    "Reco_ttH_h_dr",
    "Reco_ttH_hdau_m1",
    "Reco_ttH_hdau_pt1",
    "Reco_ttH_hdau_phi1",
    "Reco_ttH_hdau_eta1",
    "Reco_ttH_hdau_m2",
    "Reco_ttH_hdau_pt2",
    "Reco_ttH_hdau_phi2",
    "Reco_ttH_hdau_eta2",
    "Reco_ttH_hdau_idx1",
    "Reco_ttH_hdau_idx2",
    "Reco_JABDT_ttH_log_whad_m",
    "Reco_JABDT_ttH_Jet_CSV_btophad",
    "Reco_JABDT_ttH_Jet_CSV_btoplep",
    "Reco_JABDT_ttH_Jet_CSV_hdau1",
    "Reco_JABDT_ttH_Jet_CSV_hdau2",
    "Reco_JABDT_ttH_Jet_CSV_whaddau1",
    "Reco_JABDT_ttH_Jet_CSV_whaddau2",
    "Reco_JABDT_ttH_log_tophad_m__M__whad_m",
    "Reco_JABDT_ttH_log_tophad_pt",
    "Reco_JABDT_ttH_log_toplep_m",
    "Reco_JABDT_ttH_log_toplep_pt",
    "Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",
    "Reco_JABDT_ttH_log_h_pt",
    "Reco_JABDT_ttH_log_h_m",
]))


def constructPlotClasses(variablelist=Recolabels_ttH, prefix="ge4j_ge3t_", label="tHW"):
    plotClasses = []
    pltBase = "plotClasses.Plot(ROOT.TH1D("
    pltEnd = ",selection,label),"
    for var in variablelist:
        pltcl = pltBase + '"' + prefix + var + '",' + '"' + var
        if "_log_" in var:
            pltcl += '",50,-1.0,20),"'
        elif "_m" in var:
            pltcl += '",50,0,200),"'
        elif "_eta" in var:
            pltcl += '",50,-4.2,4.2),"'
        elif "abs" and "_eta" in var:
            pltcl += '",50,-1.0,4.2),"'
        elif "costheta" in var:
            pltcl += '",50,-1.0,2.2),"'


        elif "costheta" in var:
            pltcl += '",50,-1.0,2.2),"'
        elif "costheta" in var:
            pltcl += '",50,-1.0,2.2),"'
        elif "costheta" in var:
            pltcl += '",50,-1.0,2.2),"'

        elif "_phi" in var:
            pltcl += '",50,-3.2,3.2),"'
        elif "_dr" in var:
            pltcl += '",50,0,4),"'
        elif "CSV" in var:
            pltcl += '",50,0,1),"'
        else:
            pltcl += '",50,0,200),"'


        pltcl += var + '"' + pltEnd
        

        plotClasses.append(pltcl)
        # print pltcl
    with open("plots.txt","a+") as f:
        f.write("plots_"+label+"=[\n")
        for plt in plotClasses:
            f.write(plt+"\n")
        f.write("]\n")


subprocess.call("rm -f plots.txt", shell=True)
constructPlotClasses(variablelist=Recolabels_ttH, prefix="ge4j_ge3t_", label="ttH")
constructPlotClasses(variablelist=Recolabels_ttbar, prefix="ge4j_ge3t_", label="ttbar")
constructPlotClasses(variablelist=Recolabels_THW, prefix="ge4j_ge3t_", label="tHW")
constructPlotClasses(variablelist=Recolabels_THQ, prefix="ge4j_ge3t_", label="THQ")
