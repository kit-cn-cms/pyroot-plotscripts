from plot_cuts_ZPrime_MC import *


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
/*
// hacked in CSV helper
class CSVHelper
{
  public:
    // nHFptBins specifies how many of these pt bins are used:
    // (jetPt >= 19.99 && jetPt < 30), (jetPt >= 30 && jetPt < 40), (jetPt >= 40 && jetPt < 60), 
    // (jetPt >= 60 && jetPt < 100), (jetPt >= 100 && jetPt < 160), (jetPt >= 160 && jetPt < 10000).
    // If nHFptBins < 6, the last on is inclusive (eg jetPt >=100 && jetPt < 10000 for nHFptBins=5).
    // The SFs from data have 5 bins, the pseudo data scale factors 6 bins.
    CSVHelper();
  CSVHelper(const std::string& hf, const std::string& lf, const int nHFptBins=6);
  ~CSVHelper();
  void init(const std::string& hf, const std::string& lf, const int nHFptBins);
  double getCSVWeight(const std::vector<double>& jetPts,
		      const std::vector<double>& jetEtas,
		      const std::vector<double>& jetCSVs,
		      const std::vector<int>& jetFlavors,
		      const int iSys,
		      double &csvWgtHF,
		      double &csvWgtLF,
		      double &csvWgtCF) const;
  void allowJetsOutOfBinning(const bool allow) { allowJetsOutOfBinning_ = allow; }
  private:
    bool isInit_;
    int nHFptBins_;
    bool allowJetsOutOfBinning_;
    std::vector< std::vector<TH1*> > h_csv_wgt_hf;
    std::vector< std::vector<TH1*> > c_csv_wgt_hf;
    std::vector< std::vector< std::vector<TH1*> > > h_csv_wgt_lf;
    void fillCSVHistos(TFile *fileHF, TFile *fileLF);
    TH1* readHistogram(TFile* file, const TString& name) const;
};
CSVHelper::CSVHelper()
  : isInit_(false), nHFptBins_(0), allowJetsOutOfBinning_(false) {}
CSVHelper::CSVHelper(const std::string& hf, const std::string& lf, const int nHFptBins)
  : isInit_(false), nHFptBins_(0), allowJetsOutOfBinning_(false) {
  init(hf,lf,nHFptBins);
}
CSVHelper::~CSVHelper() {
  for(auto& i: h_csv_wgt_hf ) {
    for(auto& j: i) {
      if( j ) delete j;
    }
  }
  for(auto& i: c_csv_wgt_hf ) {
    for(auto& j: i) {
      if( j ) delete j;
    }
  }
  for(auto& i: h_csv_wgt_lf ) {
    for(auto& j: i) {
      for(auto& k: j) {
	if( k ) delete k;
      }
    }
  }
}
void CSVHelper::init(const std::string& hf, const std::string& lf, const int nHFptBins) {
  std::cout << "Initializing b-tag scale factors"<< "  HF : " << hf << " (" << nHFptBins << " pt bins)"<< "  LF : " << lf << std::endl;
  nHFptBins_ = nHFptBins;
  const std::string inputFileHF = hf.size() > 0 ? hf : "data/csv_rwt_hf_IT_FlatSF.root";
  const std::string inputFileLF = lf.size() > 0 ? lf : "data/csv_rwt_lf_IT_FlatSF.root";
  TFile *f_CSVwgt_HF = new TFile(inputFileHF.c_str());
  TFile *f_CSVwgt_LF = new TFile(inputFileLF.c_str());
  fillCSVHistos(f_CSVwgt_HF, f_CSVwgt_LF);
  f_CSVwgt_HF->Close();
  f_CSVwgt_LF->Close();
  delete f_CSVwgt_HF;
  delete f_CSVwgt_LF;
  isInit_ = true;
}
// fill the histograms (done once)
void
CSVHelper::fillCSVHistos(TFile *fileHF, TFile *fileLF)
{
  const size_t nSys = 9;
  const size_t nPt = 6;
  const size_t nEta = 3;
  h_csv_wgt_hf = std::vector< std::vector<TH1*> >(nSys,std::vector<TH1*>(nPt,NULL));
  c_csv_wgt_hf = std::vector< std::vector<TH1*> >(nSys,std::vector<TH1*>(nPt,NULL));
  h_csv_wgt_lf = std::vector< std::vector< std::vector<TH1*> > >(nSys,std::vector< std::vector<TH1*> >(nPt,std::vector<TH1*>(nEta,NULL)));
  // CSV reweighting /// only care about the nominal ones
  for (size_t iSys = 0; iSys < nSys; iSys++) {
    TString syst_csv_suffix_hf = "final";
    TString syst_csv_suffix_c = "final";
    TString syst_csv_suffix_lf = "final";
    switch (iSys) {
    case 0:
      // this is the nominal case
      break;
    case 1:
      // JESUp
      syst_csv_suffix_hf = "final_JESUp";
      syst_csv_suffix_lf = "final_JESUp";
      syst_csv_suffix_c = "final_cErr1Up";
      break;
    case 2:
      // JESDown
      syst_csv_suffix_hf = "final_JESDown";
      syst_csv_suffix_lf = "final_JESDown";
      syst_csv_suffix_c = "final_cErr1Down";
      break;
    case 3:
      // purity up
      syst_csv_suffix_hf = "final_LFUp";
      syst_csv_suffix_lf = "final_HFUp";
      syst_csv_suffix_c = "final_cErr2Up";
      break;
    case 4:
      // purity down
      syst_csv_suffix_hf = "final_LFDown";
      syst_csv_suffix_lf = "final_HFDown";
      syst_csv_suffix_c = "final_cErr2Down";
      break;
    case 5:
      // stats1 up
      syst_csv_suffix_hf = "final_Stats1Up";
      syst_csv_suffix_lf = "final_Stats1Up";
      break;
    case 6:
      // stats1 down
      syst_csv_suffix_hf = "final_Stats1Down";
      syst_csv_suffix_lf = "final_Stats1Down";
      break;
    case 7:
      // stats2 up
      syst_csv_suffix_hf = "final_Stats2Up";
      syst_csv_suffix_lf = "final_Stats2Up";
      break;
    case 8:
      // stats2 down
      syst_csv_suffix_hf = "final_Stats2Down";
      syst_csv_suffix_lf = "final_Stats2Down";
      break;
    }
    
    for (int iPt = 0; iPt < nHFptBins_; iPt++) {
      const TString name = Form("csv_ratio_Pt%i_Eta0_%s", iPt, syst_csv_suffix_hf.Data());
      h_csv_wgt_hf.at(iSys).at(iPt) = readHistogram(fileHF,name);
    }
    if (iSys < 5) {
      for (int iPt = 0; iPt < nHFptBins_; iPt++) {
	const TString name = Form("c_csv_ratio_Pt%i_Eta0_%s", iPt, syst_csv_suffix_c.Data());
	c_csv_wgt_hf.at(iSys).at(iPt) = readHistogram(fileHF,name);
      }
    }    
    for (int iPt = 0; iPt < 4; iPt++) {
      for (int iEta = 0; iEta < 3; iEta++) {
	const TString name = Form("csv_ratio_Pt%i_Eta%i_%s", iPt, iEta, syst_csv_suffix_lf.Data());
	h_csv_wgt_lf.at(iSys).at(iPt).at(iEta) = readHistogram(fileLF,name);
      }
    }
  }
}
TH1* CSVHelper::readHistogram(TFile* file, const TString& name) const {
  TH1* h = NULL;
  file->GetObject(name,h);
  if( h==NULL ) {
    std::cout<<"CSVHelper: DID not find histograms"<<std::endl;
  }
  h->SetDirectory(0);
  
  return h;
}
double
CSVHelper::getCSVWeight(const std::vector<double>& jetPts,
			const std::vector<double>& jetEtas,
			const std::vector<double>& jetCSVs,
			const std::vector<int>& jetFlavors,
			const int iSys,
			double &csvWgtHF,
			double &csvWgtLF,
			double &csvWgtCF) const
{
  if( !isInit_ ) {
    std::cout<<"CSVHelper: Not initualized"<<std::endl;
  }
  int iSysHF = 0;
  switch (iSys) {
  case 7:
    iSysHF = 1;
    break; // JESUp
  case 8:
    iSysHF = 2;
    break; // JESDown
  case 9:
    iSysHF = 3;
    break; // LFUp
  case 10:
    iSysHF = 4;
    break; // LFDown
  case 13:
    iSysHF = 5;
    break; // Stats1Up
  case 14:
    iSysHF = 6;
    break; // Stats1Down
  case 15:
    iSysHF = 7;
    break; // Stats2Up
  case 16:
    iSysHF = 8;
    break; // Stats2Down
  default:
    iSysHF = 0;
    break; // NoSys
  }
  
  int iSysC = 0;
  switch (iSys) {
  case 21:
    iSysC = 1;
    break;
  case 22:
    iSysC = 2;
    break;
  case 23:
    iSysC = 3;
    break;
  case 24:
    iSysC = 4;
    break;
  default:
    iSysC = 0;
    break;
  }
  
  int iSysLF = 0;
  switch (iSys) {
  case 7:
    iSysLF = 1;
    break; // JESUp
  case 8:
    iSysLF = 2;
    break; // JESDown
  case 11:
    iSysLF = 3;
    break; // HFUp
  case 12:
    iSysLF = 4;
    break; // HFDown
  case 17:
    iSysLF = 5;
    break; // Stats1Up
  case 18:
    iSysLF = 6;
    break; // Stats1Down
  case 19:
    iSysLF = 7;
    break; // Stats2Up
  case 20:
    iSysLF = 8;
    break; // Stats2Down
  default:
    iSysLF = 0;
    break; // NoSys
  }
  double csvWgthf = 1.;
  double csvWgtC = 1.;
  double csvWgtlf = 1.;
  
  for (size_t iJet = 0; iJet < jetPts.size(); iJet++) {
    const double csv = jetCSVs.at(iJet);
    const double jetPt = jetPts.at(iJet);
    const double jetAbsEta = fabs(jetEtas.at(iJet));
    const int flavor = jetFlavors.at(iJet);
    int iPt = -1;
    int iEta = -1;
    if(abs(flavor)>3) {
        if (jetPt >= 19.99 && jetPt < 30)
            iPt = 0;
        else if (jetPt >= 30 && jetPt < 50)
            iPt = 1;
        else if (jetPt >= 50 && jetPt < 70)
            iPt = 2;
        else if (jetPt >= 70 && jetPt < 100)
            iPt = 3;
        else if (jetPt >= 100 && jetPt < 160)
            iPt = 4;
        else if (jetPt >= 160)
            iPt = 5;
    }
    else {
        if (jetPt >= 19.99 && jetPt < 30)
            iPt = 0;
        else if (jetPt >= 30 && jetPt < 40)
            iPt = 1;
        else if (jetPt >= 40 && jetPt < 60)
            iPt = 2;
        else if (jetPt >= 60 && jetPt < 100)
            iPt = 3;
        else if (jetPt >= 100 && jetPt < 160)
            iPt = 4;
        else if (jetPt >= 160)
            iPt = 5;
    }
    
    if (jetAbsEta >= 0 && jetAbsEta < 0.8)
      iEta = 0;
    else if (jetAbsEta >= 0.8 && jetAbsEta < 1.6)
      iEta = 1;
    else if (jetAbsEta >= 1.6 && jetAbsEta < 2.41)
      iEta = 2;
    
    if (iPt < 0 || iEta < 0) {
      if( allowJetsOutOfBinning_ ) continue;
    }
    
    if (abs(flavor) == 5) {
      // RESET iPt to maximum pt bin (only 5 bins for new SFs)
      if(iPt>=nHFptBins_){
	iPt=nHFptBins_-1;
      }
      const int useCSVBin = (csv >= 0.) ? h_csv_wgt_hf.at(iSysHF).at(iPt)->FindBin(csv) : 1;
      const double iCSVWgtHF = h_csv_wgt_hf.at(iSysHF).at(iPt)->GetBinContent(useCSVBin);
      if (iCSVWgtHF != 0)
	csvWgthf *= iCSVWgtHF;
      
    } else if (abs(flavor) == 4) {
      // RESET iPt to maximum pt bin (only 5 bins for new SFs)
      if(iPt>=nHFptBins_){
	iPt=nHFptBins_-1;
      }
      const int useCSVBin = (csv >= 0.) ? c_csv_wgt_hf.at(iSysC).at(iPt)->FindBin(csv) : 1;
      const double iCSVWgtC = c_csv_wgt_hf.at(iSysC).at(iPt)->GetBinContent(useCSVBin);
      if (iCSVWgtC != 0)
	csvWgtC *= iCSVWgtC;
    } else {
      if (iPt >= 3)
	iPt = 3; /// [30-40], [40-60] and [60-10000] only 3 Pt bins for lf
      const int useCSVBin = (csv >= 0.) ? h_csv_wgt_lf.at(iSysLF).at(iPt).at(iEta)->FindBin(csv) : 1;
      const double iCSVWgtLF = h_csv_wgt_lf.at(iSysLF).at(iPt).at(iEta)->GetBinContent(useCSVBin);
      if (iCSVWgtLF != 0)
	csvWgtlf *= iCSVWgtLF;
    }
  }
  const double csvWgtTotal = csvWgthf * csvWgtC * csvWgtlf;
  csvWgtHF = csvWgthf;
  csvWgtLF = csvWgtlf;
  csvWgtCF = csvWgtC;
  return csvWgtTotal;
}
*/
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
                        
                        #'N_Jets', 'Jet_Pt','Jet_Eta','Jet_CSV','Jet_Flav','Jet_M','Jet_Phi','Jet_E',
                        
                        

                        #'internalCSVweight:=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,internalSystName,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)',
                        #'internalCSVweight_CSVHFUp:=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,11,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight',
                        #'internalCSVweight_CSVHFDown:=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,12,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight',
                        #'internalCSVweight_CSVLFUp:=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,9,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight',
                        #'internalCSVweight_CSVLFDown:=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,10,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight',                        

]