class CSVHelper {
   public:
    // nHFptBins specifies how many of these pt bins are used:
    // (jetPt >= 19.99 && jetPt < 30), (jetPt >= 30 && jetPt < 40), (jetPt >= 40 && jetPt < 60),
    // (jetPt >= 60 && jetPt < 100), (jetPt >= 100 && jetPt < 160), (jetPt >= 160 && jetPt < 10000).
    // If nHFptBins < 6, the last on is inclusive (eg jetPt >=100 && jetPt < 10000 for nHFptBins=5).
    // The SFs from data have 5 bins, the pseudo data scale factors 6 bins.

    // standard constructor
    CSVHelper();
    // another constructor
    CSVHelper(const std::string& hf, const std::string& lf, const int& nHFptBins = 5, const int& nLFptBins = 4, const int& nLFetaBins = 3,
              const std::vector< Systematics::Type >& jecsysts = std::vector< Systematics::Type >(1, Systematics::NA));
    // destructor
    ~CSVHelper();

    enum class CSVwp { Tight, Medium, Loose, None };

    // function to set up the needed stuff
    void init(const std::string& hf, const std::string& lf, const int& nHFptBins, const int& nLFptBins, const int& nLFetaBins,
              const std::vector< Systematics::Type >& jecsysts);
    // function to get the csv weight
    double getCSVWeight(const std::vector< double >& jetPts, const std::vector< double >& jetEtas, const std::vector< double >& jetCSVs,
                        const std::vector< int >& jetFlavors, const Systematics::Type syst, double& csvWgtHF, double& csvWgtLF, double& csvWgtCF) const;
    std::map< std::string, double > getCSVWeightsDiff(const std::vector< double >& jetPts, const std::vector< double >& jetEtas,
                                                      const std::vector< double >& jetCSVs, const std::vector< int >& jetFlavors,
                                                      const Systematics::Type syst) const;

    // If there is no SF for a jet because it is out of acceptance
    // of SF, an SF of 1 is used for this jet. Intended when running
    // on MC with a more inclusive selection.
    // USE WITH CARE!
    void allowJetsOutOfBinning(const bool allow) { allowJetsOutOfBinning_ = allow; }

   private:
    bool isInit_;
    int  nHFptBins_;   // number of pt bins in hf(including c flavour) histograms
    int  nLFptBins_;   // number of pt bins in lf histograms
    int  nLFetaBins_;  // number of eta bins in lf histograms
    bool allowJetsOutOfBinning_;

    std::vector< std::vector< TH1* > > h_csv_wgt_hf;                 // vector to store pointers to the needed hf histograms
    std::vector< std::vector< TH1* > > c_csv_wgt_hf;                 // vector to store pointers to the needed c flavour histograms
    std::vector< std::vector< std::vector< TH1* > > > h_csv_wgt_lf;  // vector to store pointers to the needed lf histograms
    // vector for the csv systematics
    std::vector< Systematics::Type > csvsysts = {
        Systematics::CSVLFup,       Systematics::CSVLFdown,       Systematics::CSVHFup,       Systematics::CSVHFdown,
        Systematics::CSVHFStats1up, Systematics::CSVHFStats1down, Systematics::CSVLFStats1up, Systematics::CSVLFStats1down,
        Systematics::CSVHFStats2up, Systematics::CSVHFStats2down, Systematics::CSVLFStats2up, Systematics::CSVLFStats2down,
        Systematics::CSVCErr1up,    Systematics::CSVCErr1down,    Systematics::CSVCErr2up,    Systematics::CSVCErr2down};
    // vector for all desired systematics -> csv+jec systematics
    std::vector< Systematics::Type > systs;
    // function to get the histograms from the provided root files
    void fillCSVHistos(TFile* fileHF, TFile* fileLF, const std::vector< Systematics::Type >& systs);
    // function which reads the desired histogram from the provided root file
    TH1* readHistogram(TFile* file, const TString& name) const;
};

CSVHelper::CSVHelper() : isInit_(false), nHFptBins_(0), nLFptBins_(0), nLFetaBins_(0), allowJetsOutOfBinning_(false) {}

CSVHelper::CSVHelper(const std::string& hf, const std::string& lf, const int& nHFptBins, const int& nLFptBins, const int& nLFetaBins,
                     const std::vector< Systematics::Type >& jecsysts) :
    isInit_(false),
    nHFptBins_(0),
    nLFptBins_(0),
    nLFetaBins_(0),
    allowJetsOutOfBinning_(false)
{
    init(hf, lf, nHFptBins, nLFptBins, nLFetaBins, jecsysts);
}

CSVHelper::~CSVHelper()
{
    for (auto& i : h_csv_wgt_hf) {
        for (auto& j : i) {
            if (j) delete j;
        }
    }
    for (auto& i : c_csv_wgt_hf) {
        for (auto& j : i) {
            if (j) delete j;
        }
    }
    for (auto& i : h_csv_wgt_lf) {
        for (auto& j : i) {
            for (auto& k : j) {
                if (k) delete k;
            }
        }
    }
}

void CSVHelper::init(const std::string& hf, const std::string& lf, const int& nHFptBins, const int& nLFptBins, const int& nLFetaBins,
                     const std::vector< Systematics::Type >& jecsysts)
{
    std::cout << "Initializing b-tag scale factors"
              << "\n  HF : " << hf << " (" << nHFptBins << " pt bins)"
              << "\n  LF : " << lf << " (" << nLFptBins << " pt bins)"
              << "\n  LF : " << lf << " (" << nLFetaBins << " eta bins)" << std::endl;

    nHFptBins_  = nHFptBins;
    nLFptBins_  = nLFptBins;
    nLFetaBins_ = nLFetaBins;

    // combine the vector with the csv systematics and the jec systematics into one vector
    systs.reserve(csvsysts.size() + jecsysts.size());
    systs.insert(systs.end(), jecsysts.begin(), jecsysts.end());
    systs.insert(systs.end(), csvsysts.begin(), csvsysts.end());

    const std::string inputFileHF = hf.size() > 0 ? hf : "data/csv_rwt_hf_IT_FlatSF.root";
    const std::string inputFileLF = lf.size() > 0 ? lf : "data/csv_rwt_lf_IT_FlatSF.root";

    TFile* f_CSVwgt_HF = new TFile((inputFileHF).c_str());
    TFile* f_CSVwgt_LF = new TFile((inputFileLF).c_str());

    fillCSVHistos(f_CSVwgt_HF, f_CSVwgt_LF, systs);
    f_CSVwgt_HF->Close();
    f_CSVwgt_LF->Close();
    delete f_CSVwgt_HF;
    delete f_CSVwgt_LF;

    isInit_ = true;
}

// fill the histograms (done once)
void CSVHelper::fillCSVHistos(TFile* fileHF, TFile* fileLF, const std::vector< Systematics::Type >& systs)
{
    const size_t nSys = systs.size();  // purity,stats1,stats2 with up/down + jec systs including nominal variation
    h_csv_wgt_hf      = std::vector< std::vector< TH1* > >(nSys, std::vector< TH1* >(nHFptBins_, NULL));
    c_csv_wgt_hf      = std::vector< std::vector< TH1* > >(nSys, std::vector< TH1* >(nHFptBins_, NULL));
    h_csv_wgt_lf =
        std::vector< std::vector< std::vector< TH1* > > >(nSys, std::vector< std::vector< TH1* > >(nLFptBins_, std::vector< TH1* >(nLFetaBins_, NULL)));
    TString syst_csv_suffix = "final";
    // loop over all the available systematics
    for (size_t iSys = 0; iSys < nSys; iSys++) {
        // some string cosmetics to search for the correct histogram in the root files
        TString systematic          = Systematics::toString(systs[iSys]);
        TString systematic_original = systematic;

        systematic.ReplaceAll("up", "Up");
        systematic.ReplaceAll("down", "Down");
        systematic.ReplaceAll("CSV", "");
        systematic.ReplaceAll("Stats", "stats");

        std::cout << "############################################### " << std::endl;
        std::cout << "adding histograms for systematic " << systematic << std::endl;
        std::cout << "############################################### " << std::endl;

        if (systematic != "") { systematic = "_" + systematic; }

        // loop over all pt bins of the different jet flavours
        // b flavor
        for (int iPt = 0; iPt < nHFptBins_; iPt++) {
            TString name = Form("csv_ratio_Pt%i_Eta0_%s", iPt, (syst_csv_suffix + systematic).Data());
            // only read the histogram if it exits in the root file
            if (fileHF->GetListOfKeys()->Contains(name)) {
                h_csv_wgt_hf.at(iSys).at(iPt) = readHistogram(fileHF, name);
                std::cout << "for " << systematic_original << " added " << h_csv_wgt_hf.at(iSys).at(iPt)->GetName() << " from HF file" << std::endl;
            }
            else {
                std::cout << "WARNING: didn't find Histogram " << name << " in HF File, using nominal instead" << std::endl;
                h_csv_wgt_hf.at(iSys).at(iPt) = readHistogram(fileHF, name.ReplaceAll(systematic, ""));
                std::cout << "for " << systematic_original << " added " << h_csv_wgt_hf.at(iSys).at(iPt)->GetName() << " from HF file" << std::endl;
            }
        }
        // c flavor
        for (int iPt = 0; iPt < nHFptBins_; iPt++) {
            TString name = Form("c_csv_ratio_Pt%i_Eta0_%s", iPt, (syst_csv_suffix + systematic).Data());
            if (fileHF->GetListOfKeys()->Contains(name)) {
                c_csv_wgt_hf.at(iSys).at(iPt) = readHistogram(fileHF, name);
                std::cout << "for " << systematic_original << " added " << c_csv_wgt_hf.at(iSys).at(iPt)->GetName() << " from CF(HF) file" << std::endl;
            }
            else {
                std::cout << "WARNING: didn't find Histogram " << name << " in CF(HF) File, using nominal instead" << std::endl;
                c_csv_wgt_hf.at(iSys).at(iPt) = readHistogram(fileHF, name.ReplaceAll(systematic, ""));
                std::cout << "for " << systematic_original << " added " << c_csv_wgt_hf.at(iSys).at(iPt)->GetName() << " from CF(HF) file" << std::endl;
            }
        }
        // light flavor
        for (int iPt = 0; iPt < nLFptBins_; iPt++) {
            for (int iEta = 0; iEta < nLFetaBins_; iEta++) {
                TString name = Form("csv_ratio_Pt%i_Eta%i_%s", iPt, iEta, (syst_csv_suffix + systematic).Data());
                if (fileLF->GetListOfKeys()->Contains(name)) {
                    h_csv_wgt_lf.at(iSys).at(iPt).at(iEta) = readHistogram(fileLF, name);
                    std::cout << "for " << systematic_original << " added " << h_csv_wgt_lf.at(iSys).at(iPt).at(iEta)->GetName() << " from LF file"
                              << std::endl;
                }
                else {
                    std::cout << "WARNING: didn't find Histogram " << name << " in LF File, using nominal instead" << std::endl;
                    h_csv_wgt_lf.at(iSys).at(iPt).at(iEta) = readHistogram(fileLF, name.ReplaceAll(systematic, ""));
                    std::cout << "for " << systematic_original << " added " << h_csv_wgt_lf.at(iSys).at(iPt).at(iEta)->GetName() << " from LF file"
                              << std::endl;
                }
            }
        }
    }
}

TH1* CSVHelper::readHistogram(TFile* file, const TString& name) const
{
    TH1* h = NULL;
    file->GetObject(name, h);
    if (h == NULL) {
        // throw cms::Exception("BadCSVWeightInit")
        std::cerr << "BadCSVWeightInit" << std::endl << "Could not find CSV SF histogram '" << name << "' in file '" << file->GetName() << "'";
    }
    h->SetDirectory(0);

    return h;
}

double CSVHelper::getCSVWeight(const std::vector< double >& jetPts, const std::vector< double >& jetEtas, const std::vector< double >& jetCSVs,
                               const std::vector< int >& jetFlavors, const Systematics::Type syst, double& csvWgtHF, double& csvWgtLF, double& csvWgtCF) const
{
    if (!isInit_) {
        // throw cms::Exception("BadCSVWeightAccess") << "CSVHelper not initialized";
        std::cerr << "BadCSVWeightAccess" << std::endl << "CSVHelper not initialized";
    }
    // search for the position of the desired systematic in the systs vector
    const int iSys = std::find(systs.begin(), systs.end(), syst) - systs.begin();

    // std::cout << "Systematic index " << iSys << std::endl;
    // initialize the weight for the different jet flavours with 1
    double csvWgthf = 1.;
    double csvWgtC  = 1.;
    double csvWgtlf = 1.;

    // loop over all jets in the event and calculate the final weight by multiplying the single jet scale factors
    for (size_t iJet = 0; iJet < jetPts.size(); iJet++) {
        const double csv       = jetCSVs.at(iJet);
        const double jetPt     = jetPts.at(iJet);
        const double jetAbsEta = fabs(jetEtas.at(iJet));
        const int    flavor    = jetFlavors.at(iJet);

        int iPt  = -1;
        int iEta = -1;
        // pt binning for heavy flavour jets
        if (abs(flavor) > 3) {
            if (jetPt >= 19.99 && jetPt <= 30)
                iPt = 0;
            else if (jetPt > 30 && jetPt <= 50)
                iPt = 1;
            else if (jetPt > 50 && jetPt <= 70)
                iPt = 2;
            else if (jetPt > 70 && jetPt <= 100)
                iPt = 3;
            else if (jetPt > 100)
                iPt = 4;
            else
                iPt = 5;
        }
        // pt binning for light flavour jets
        else {
            if (jetPt >= 19.99 && jetPt <= 30)
                iPt = 0;
            else if (jetPt > 30 && jetPt <= 40)
                iPt = 1;
            else if (jetPt > 40 && jetPt <= 60)
                iPt = 2;
            else if (jetPt > 60)
                iPt = 3;
            else
                iPt = 4;
        }
        // light flavour jets also have eta bins
        if (jetAbsEta >= 0 && jetAbsEta < 0.8)
            iEta = 0;
        else if (jetAbsEta >= 0.8 && jetAbsEta < 1.6)
            iEta = 1;
        else if (jetAbsEta >= 1.6 && jetAbsEta < 2.5)  // difference between 2016/2017, nut not neccesary since |eta|<2.4 anyway
            iEta = 2;

        if (iPt < 0 || iEta < 0) {
            if (allowJetsOutOfBinning_) continue;
            // throw cms::Exception("BadCSVWeightAccess") << "couldn't find Pt, Eta bins for this b-flavor jet, jetPt = " << jetPt << ", jetAbsEta = " <<
            // jetAbsEta;
            std::cerr << "BadCSVWeightAccess" << std::endl
                      << "couldn't find Pt, Eta bins for this b-flavor jet, jetPt = " << jetPt << ", jetAbsEta = " << jetAbsEta;
        }

        // std::cout << "program is in front of calculating the csv weights " << std::endl;
        // b flavour jet
        if (abs(flavor) == 5) {
            // std::cout << "b flavor jet " << std::endl;
            // RESET iPt to maximum pt bin (only 5 bins for new SFs)
            // -> updated above
            if (iPt >= nHFptBins_) {
                iPt = nHFptBins_ - 1;  // [20-30], [30-50], [50-70], [70,100] and [100-10000] only 5 Pt bins for hf
            }
            if (h_csv_wgt_hf.at(iSys).at(iPt)) {
                const int    useCSVBin = (csv >= 0.) ? h_csv_wgt_hf.at(iSys).at(iPt)->FindBin(csv) : 1;
                const double iCSVWgtHF = h_csv_wgt_hf.at(iSys).at(iPt)->GetBinContent(useCSVBin);
                if (iCSVWgtHF != 0) csvWgthf *= iCSVWgtHF;
            }
        }  // c flavour jet
        else if (abs(flavor) == 4) {
            // std::cout << "c flavor jet " << std::endl;
            // RESET iPt to maximum pt bin (only 5 bins for new SFs)
            // -> updated above

            if (iPt >= nHFptBins_) {
                iPt = nHFptBins_ - 1;  // [20-30], [30-50], [50-70], [70,100] and [100-10000] only 5 Pt bins for hf
            }
            if (c_csv_wgt_hf.at(iSys).at(iPt)) {
                const int    useCSVBin = (csv >= 0.) ? c_csv_wgt_hf.at(iSys).at(iPt)->FindBin(csv) : 1;
                const double iCSVWgtC  = c_csv_wgt_hf.at(iSys).at(iPt)->GetBinContent(useCSVBin);
                if (iCSVWgtC != 0) csvWgtC *= iCSVWgtC;
            }
        }  // light flavour jet
        else {
            // std::cout << "light flavor jet " << std::endl;
            // RESET iPt to maximum pt bin (only 5 bins for new SFs)
            // -> updated above
            if (iPt >= nLFptBins_) {
                iPt = nLFptBins_ - 1;  // [20-30], [30-40], [40-60] and [60-10000] only 4 Pt bins for lf
            }
            if (h_csv_wgt_lf.at(iSys).at(iPt).at(iEta)) {
                const int    useCSVBin = (csv >= 0.) ? h_csv_wgt_lf.at(iSys).at(iPt).at(iEta)->FindBin(csv) : 1;
                const double iCSVWgtLF = h_csv_wgt_lf.at(iSys).at(iPt).at(iEta)->GetBinContent(useCSVBin);
                if (iCSVWgtLF != 0) csvWgtlf *= iCSVWgtLF;
            }
        }
    }

    const double csvWgtTotal = csvWgthf * csvWgtC * csvWgtlf;

    csvWgtHF = csvWgthf;
    csvWgtLF = csvWgtlf;
    csvWgtCF = csvWgtC;

    return csvWgtTotal;
}

std::map< std::string, double > CSVHelper::getCSVWeightsDiff(const std::vector< double >& jetPts, const std::vector< double >& jetEtas,
                                                             const std::vector< double >& jetCSVs, const std::vector< int >& jetFlavors,
                                                             const Systematics::Type syst) const
{
    if (!isInit_) {
        // throw cms::Exception("BadCSVWeightAccess") << "CSVHelper not initialized";
        std::cerr << "BadCSVWeightAccess" << std::endl << "CSVHelper not initialized";
    }
    // search for the position of the desired systematic in the systs vector
    const int iSys = std::find(systs.begin(), systs.end(), syst) - systs.begin();

    // std::cout << "Systematic index " << iSys << std::endl;
    // initialize the weight for the different jet flavours with 1
    double                               csvWgthf = 1.;
    double                               csvWgtC  = 1.;
    double                               csvWgtlf = 1.;
    std::vector< double >                w_HF(nHFptBins_, 1);
    std::vector< std::vector< double > > w_LF(nLFptBins_, std::vector< double >(nLFetaBins_, 1));

    // loop over all jets in the event and calculate the final weight by multiplying the single jet scale factors
    for (size_t iJet = 0; iJet < jetPts.size(); iJet++) {
        const double csv       = jetCSVs.at(iJet);
        const double jetPt     = jetPts.at(iJet);
        const double jetAbsEta = fabs(jetEtas.at(iJet));
        const int    flavor    = jetFlavors.at(iJet);

        int iPt  = -1;
        int iEta = -1;
        // pt binning for heavy flavour jets
        if (abs(flavor) > 3) {
            if (jetPt >= 19.99 && jetPt <= 30)
                iPt = 0;
            else if (jetPt > 30 && jetPt <= 50)
                iPt = 1;
            else if (jetPt > 50 && jetPt <= 70)
                iPt = 2;
            else if (jetPt > 70 && jetPt <= 100)
                iPt = 3;
            else if (jetPt > 100)
                iPt = 4;
            else
                iPt = 5;
        }
        // pt binning for light flavour jets
        else {
            if (jetPt >= 19.99 && jetPt <= 30)
                iPt = 0;
            else if (jetPt > 30 && jetPt <= 40)
                iPt = 1;
            else if (jetPt > 40 && jetPt <= 60)
                iPt = 2;
            else if (jetPt > 60)
                iPt = 3;
            else
                iPt = 4;
        }
        // light flavour jets also have eta bins
        if (jetAbsEta >= 0 && jetAbsEta < 0.8)
            iEta = 0;
        else if (jetAbsEta >= 0.8 && jetAbsEta < 1.6)
            iEta = 1;
        else if (jetAbsEta >= 1.6 && jetAbsEta < 2.5)  // difference between 2016/2017, nut not neccesary since |eta|<2.4 anyway
            iEta = 2;

        if (iPt < 0 || iEta < 0) {
            if (allowJetsOutOfBinning_) continue;
            // throw cms::Exception("BadCSVWeightAccess") << "couldn't find Pt, Eta bins for this b-flavor jet, jetPt = " << jetPt << ", jetAbsEta = " <<
            // jetAbsEta;
            std::cerr << "BadCSVWeightAccess" << std::endl
                      << "couldn't find Pt, Eta bins for this b-flavor jet, jetPt = " << jetPt << ", jetAbsEta = " << jetAbsEta;
        }

        // std::cout << "program is in front of calculating the csv weights " << std::endl;
        // b flavour jet
        if (abs(flavor) == 5) {
            // std::cout << "b flavor jet " << std::endl;
            // RESET iPt to maximum pt bin (only 5 bins for new SFs)
            // -> updated above
            if (iPt >= nHFptBins_) {
                iPt = nHFptBins_ - 1;  // [20-30], [30-50], [50-70], [70,100] and [100-10000] only 5 Pt bins for hf
            }
            if (h_csv_wgt_hf.at(iSys).at(iPt)) {
                const int    useCSVBin = (csv >= 0.) ? h_csv_wgt_hf.at(iSys).at(iPt)->FindBin(csv) : 1;
                const double iCSVWgtHF = h_csv_wgt_hf.at(iSys).at(iPt)->GetBinContent(useCSVBin);
                w_HF.at(iPt) *= iCSVWgtHF;
                if (iCSVWgtHF != 0) csvWgthf *= iCSVWgtHF;
            }
        }  // c flavour jet
        else if (abs(flavor) == 4) {
            // std::cout << "c flavor jet " << std::endl;
            // RESET iPt to maximum pt bin (only 5 bins for new SFs)
            // -> updated above

            if (iPt >= nHFptBins_) {
                iPt = nHFptBins_ - 1;  // [20-30], [30-50], [50-70], [70,100] and [100-10000] only 5 Pt bins for hf
            }
            if (c_csv_wgt_hf.at(iSys).at(iPt)) {
                const int    useCSVBin = (csv >= 0.) ? c_csv_wgt_hf.at(iSys).at(iPt)->FindBin(csv) : 1;
                const double iCSVWgtC  = c_csv_wgt_hf.at(iSys).at(iPt)->GetBinContent(useCSVBin);
                w_HF.at(iPt) *= iCSVWgtC;
                if (iCSVWgtC != 0) csvWgtC *= iCSVWgtC;
            }
        }  // light flavour jet
        else {
            // std::cout << "light flavor jet " << std::endl;
            // RESET iPt to maximum pt bin (only 5 bins for new SFs)
            // -> updated above
            if (iPt >= nLFptBins_) {
                iPt = nLFptBins_ - 1;  // [20-30], [30-40], [40-60] and [60-10000] only 4 Pt bins for lf
            }
            if (h_csv_wgt_lf.at(iSys).at(iPt).at(iEta)) {
                const int    useCSVBin = (csv >= 0.) ? h_csv_wgt_lf.at(iSys).at(iPt).at(iEta)->FindBin(csv) : 1;
                const double iCSVWgtLF = h_csv_wgt_lf.at(iSys).at(iPt).at(iEta)->GetBinContent(useCSVBin);
                w_LF[iPt][iEta] *= iCSVWgtLF;
                if (iCSVWgtLF != 0) csvWgtlf *= iCSVWgtLF;
            }
        }
    }

    const double csvWgtTotal = csvWgthf * csvWgtC * csvWgtlf;

    std::map< std::string, double > weights;
    bool                            isUp     = false;
    TString                         basename = Systematics::toString(syst);
    if (basename.EndsWith("up")) { isUp = true; }
    basename.ReplaceAll("up", "");
    basename.ReplaceAll("down", "");

    for (int i = 0; i < nHFptBins_; i++) {
        TString name = "HF_" + basename + "_Pt" + std::to_string(i);
        if (isUp) { name += "up"; }
        else {
            name += "down";
        }
        weights[name.Data()] = w_HF.at(i);
    }

    for (int i = 0; i < nLFptBins_; i++) {
        for (int j = 0; j < nLFetaBins_; j++) {
            TString name = "LF_" + basename + "_Pt" + std::to_string(i) + "_Eta" + std::to_string(j);
            if (isUp) { name += "up"; }
            else {
                name += "down";
            }
            weights[name.Data()] = w_LF[i][j];
        }
    }
    return weights;
}
