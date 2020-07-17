#ifndef SFCORRHELPER
#define SFCORRHELPER

#include <string>
#include <vector>
#include <map>

#include "TFile.h"
#include "TH1.h"
#include "TH2.h"
#include "TH3.h"
#include "TString.h"

class SFCorrectionHelper
{
public:
    SFCorrectionHelper();
    SFCorrectionHelper(
        const TString& sfFile,
        const TString& nameTemplate,
        const std::vector<TString>& sfHistograms,
        std::map<TString, TString>& sfCorrections,
        std::map<TString, int>& sfDims);

    void init(
        const TString& sfFile,
        const TString& nameTemplate,
        const std::vector<TString>& sfHistograms,
        std::map<TString, TString>& sfCorrections,
        std::map<TString, int>& sfDims);

    TString GetProcID(TString procName, int ttbar, int ttH);

    double GetSF(TString procID, TString correction, TString name, double x) 
        {return GetSF(procID, correction, name, x, 0., 0.);}
    double GetSF(TString procID, TString correction, TString name, double x, double y) 
        {return GetSF(procID, correction, name, x, y, 0.);}
    double GetSF(TString procID, TString correction, TString name, double x, double y, double z);

private:
    // init in header
    TString nameTemplate_;
    size_t nHists;
    std::map<TString, TString> sfCorrections_;
    std::map<TString, int> sfDims_;

    std::map<TString, TH1*> m_TH1;
    std::map<TString, TH2*> m_TH2;
    std::map<TString, TH3*> m_TH3;

    std::map<TString, std::map<TString, double>> m_histRanges;

    TH1* readTH1(TFile* file, const TString& name) const; 
    TH2* readTH2(TFile* file, const TString& name) const; 
    TH3* readTH3(TFile* file, const TString& name) const; 

    std::map<TString, double> getHistRanges(TH1& sfHist);
    std::map<TString, double> getHistRanges(TH2& sfHist);
    std::map<TString, double> getHistRanges(TH3& sfHist);

    double restrictRange(double val, TString axis, TString sfHist);
};
#endif

