#include "../interface/SFCorrectionHelper.h"

SFCorrectionHelper::SFCorrectionHelper(): nameTemplate_("") {}

SFCorrectionHelper::SFCorrectionHelper(
    const TString& sfFile, 
    const TString& nameTemplate, 
    const std::vector<TString>& sfHistograms, 
    std::map<TString, TString>& sfCorrections, 
    std::map<TString, int>& sfDims):
    nameTemplate_("") 
{
    init(sfFile, nameTemplate, sfHistograms, sfCorrections, sfDims);
}

void SFCorrectionHelper::init(
    const TString& sfFile, 
    const TString& nameTemplate,
    const std::vector<TString>& sfHistograms, 
    std::map<TString, TString>& sfCorrections,
    std::map<TString, int>& sfDims) 
{
    std::cout << "initializing helper function for applying SF corrections" << std::endl;

    // save values
    nameTemplate_ = nameTemplate;
    sfCorrections_ = sfCorrections;
    sfDims_ = sfDims;

    // store number of histograms
    nHists = sfHistograms.size();

    // open rootfile
    TFile *f_sfCorrections = new TFile(sfFile);

    // fill histograms in map
    // loop over histograms
    for( const auto& histName: sfHistograms ) 
    {
        // subloop over correction types
        for( const auto& corrType: sfCorrections_ ) 
        {
            // if correction type matches the histName add histogram
            if( histName.Index(corrType.second) != -1 )
            {
                // figure out correct dimension
                if(sfDims_[corrType.first]==1) 
                {
                    m_TH1[histName] = readTH1(f_sfCorrections, histName);
                    m_histRanges[histName] = getHistRanges(*m_TH1[histName]);
                    std::cout << "added histogram "<<histName<<" to TH1 list"<<std::endl;
                }
                if(sfDims_[corrType.first]==2) 
                {
                    m_TH2[histName] = readTH2(f_sfCorrections, histName);
                    std::cout << "added histogram "<<histName<<" to TH2 list"<<std::endl;
                    m_histRanges[histName] = getHistRanges(*m_TH2[histName]);
                }
                if(sfDims_[corrType.first]==3) 
                {
                    m_TH3[histName] = readTH3(f_sfCorrections, histName);
                    std::cout << "added histogram "<<histName<<" to TH3 list"<<std::endl;
                    m_histRanges[histName] = getHistRanges(*m_TH3[histName]);
                }
                for(auto it = m_histRanges[histName].cbegin(); it != m_histRanges[histName].cend(); ++it) 
                {
                        std::cout << "    "<<it->first<< " = "<< it->second<< std::endl;
                }
            }
        }
    }
    // close root file
    f_sfCorrections->Close();
    delete f_sfCorrections;
}

// histogram reader for TH1
TH1* SFCorrectionHelper::readTH1(TFile* file, const TString& name) const 
{
    TH1* h = NULL;
    file->GetObject(name, h);
    h->SetDirectory(0);
    return h;
}

// histogram reader for TH2
TH2* SFCorrectionHelper::readTH2(TFile* file, const TString& name) const 
{
    TH2* h = NULL;
    file->GetObject(name, h);
    h->SetDirectory(0);
    return h;
}

// histogram reader for TH3
TH3* SFCorrectionHelper::readTH3(TFile* file, const TString& name) const 
{
    TH3* h = NULL;
    file->GetObject(name, h);
    h->SetDirectory(0);
    return h;
}


std::map<TString, double> SFCorrectionHelper::getHistRanges(TH1 &sfHist)
{
    std::map<TString, double> histRanges;
    double nbinsX = sfHist.GetXaxis()->GetNbins();
    histRanges["xmin"] = sfHist.GetXaxis()->GetBinLowEdge(1);
    histRanges["xmax"] = sfHist.GetXaxis()->GetBinLowEdge(nbinsX+1);
    histRanges["xlo"] = sfHist.GetXaxis()->GetBinCenter(1);
    histRanges["xhi"] = sfHist.GetXaxis()->GetBinCenter(nbinsX);
    return histRanges;
}

std::map<TString, double> SFCorrectionHelper::getHistRanges(TH2 &sfHist)
{
    std::map<TString, double> histRanges;
    int nbinsX = sfHist.GetXaxis()->GetNbins();
    int nbinsY = sfHist.GetYaxis()->GetNbins();
    histRanges["xmin"] = sfHist.GetXaxis()->GetBinLowEdge(1);
    histRanges["xmax"] = sfHist.GetXaxis()->GetBinLowEdge(nbinsX+1);
    histRanges["xlo"] = sfHist.GetXaxis()->GetBinCenter(1);
    histRanges["xhi"] = sfHist.GetXaxis()->GetBinCenter(nbinsX);

    histRanges["ymin"] = sfHist.GetYaxis()->GetBinLowEdge(1);
    histRanges["ymax"] = sfHist.GetYaxis()->GetBinLowEdge(nbinsY+1);
    histRanges["ylo"] = sfHist.GetYaxis()->GetBinCenter(1);
    histRanges["yhi"] = sfHist.GetYaxis()->GetBinCenter(nbinsY);
    return histRanges;
}

std::map<TString, double> SFCorrectionHelper::getHistRanges(TH3 &sfHist)
{
    std::map<TString, double> histRanges;
    int nbinsX = sfHist.GetXaxis()->GetNbins();
    int nbinsY = sfHist.GetYaxis()->GetNbins();
    int nbinsZ = sfHist.GetZaxis()->GetNbins();
    histRanges["xmin"] = sfHist.GetXaxis()->GetBinLowEdge(1);
    histRanges["xmax"] = sfHist.GetXaxis()->GetBinLowEdge(nbinsX+1);
    histRanges["xlo"] = sfHist.GetXaxis()->GetBinCenter(1);
    histRanges["xhi"] = sfHist.GetXaxis()->GetBinCenter(nbinsX);

    histRanges["ymin"] = sfHist.GetYaxis()->GetBinLowEdge(1);
    histRanges["ymax"] = sfHist.GetYaxis()->GetBinLowEdge(nbinsY+1);
    histRanges["ylo"] = sfHist.GetYaxis()->GetBinCenter(1);
    histRanges["yhi"] = sfHist.GetYaxis()->GetBinCenter(nbinsY);

    histRanges["zmin"] = sfHist.GetZaxis()->GetBinLowEdge(1);
    histRanges["zmax"] = sfHist.GetZaxis()->GetBinLowEdge(nbinsZ+1);
    histRanges["zlo"] = sfHist.GetZaxis()->GetBinCenter(1);
    histRanges["zhi"] = sfHist.GetZaxis()->GetBinCenter(nbinsZ);
    return histRanges;
}

// hardcoded function to figure out correct SF histogram name
// TODO: reduce shittyness
TString SFCorrectionHelper::GetProcID(TString procName, int ttbar, int ttH, int nTopLep) 
{
    TString procID = "";

    // ttH naming
    if( ttH == 1 ) 
    {
        procID+="ttH";
        //if (hdPDGID == -5 || hdPDGID == 5)
        //    procID+="_bb";
        //else 
        //    procID+="_nonbb";
        return procID;
    }

    // ttbar naming
    if( ttbar == 1) 
    {
        if(procName.Index("ttbb")!=-1)
            {
            // default name for 4FS sample is 'ttbb'
            procID+="ttbb";
            // default name for 5FS sample should be 'ttbb_5FS'
            if(procName.Index("ttbb_5FS")!=-1)
                procID+="_5FS";
            else if(procName.Index("ttbb_4FS")!=-1)
                procID+="_4FS";
            }
        else if(procName.Index("ttcc")!=-1) 
            procID+="ttcc";
        else if(procName.Index("ttlf")!=-1) 
            procID+="ttlf";
        else
            procID+=procName;


        //if(nTopLep==0) procID+="_FH";
        //if(nTopLep==1) procID+="_SL";
        //if(nTopLep==2) procID+="_DL";
        return procID;
    }
    
    if(procName.Index("ttZ")!=-1)
    {
        procID+="ttZ";
        return procID;
    }    
    return procID;
}

// restrict values to binrange of SF histogram
double SFCorrectionHelper::restrictRange(double val, TString axis, TString sfHist) 
{
    if (val > m_histRanges[sfHist][axis+"max"])
    {
        //std::cout << "value "<< val<< " exceeds bin range of axis "<< axis<< std::endl;
        //std::cout << "setting value to "<<m_histRanges[sfHist][axis+"hi"]<<std::endl;
        return m_histRanges[sfHist][axis+"hi"];
    }
    else if (val < m_histRanges[sfHist][axis+"min"])
    {
        //std::cout << "value "<< val<< " exceeds bin range of axis "<< axis<< std::endl;
        //std::cout << "setting value to "<<m_histRanges[sfHist][axis+"lo"]<<std::endl;
        return m_histRanges[sfHist][axis+"lo"];
    }
    else
        return val;

}

// extract SF 
double SFCorrectionHelper::GetSF(TString procID, TString correction, TString name, double x, double y, double z) 
{
    TString sfHist = nameTemplate_;
    sfHist.ReplaceAll("$PROCESS", procID);
    sfHist.ReplaceAll("$BINNING", sfCorrections_[correction]);
    sfHist.ReplaceAll("$NAME", name);

    int binIdx = -1;
    if(sfDims_[correction]==1) 
    {
        if (m_TH1.count(sfHist)==0) return 1.;
        TH1* h = m_TH1[sfHist];
        binIdx = h->FindBin(restrictRange(x,"x",sfHist));
        return h->GetBinContent(binIdx);
    }
    if(sfDims_[correction]==2) 
    {
        if (m_TH2.count(sfHist)==0) return 1.;
        TH2* h = m_TH2[sfHist];
        binIdx = h->FindBin(restrictRange(x,"x",sfHist),restrictRange(y,"y",sfHist));
        return h->GetBinContent(binIdx);
    }
    if(sfDims_[correction]==3) 
    {
        if (m_TH3.count(sfHist)==0) return 1.;
        TH3* h = m_TH3[sfHist];
        binIdx = h->FindBin(restrictRange(x,"x",sfHist),restrictRange(y,"y",sfHist),restrictRange(z,"z",sfHist));
        return h->GetBinContent(binIdx);
    }

    return 1.;
}
