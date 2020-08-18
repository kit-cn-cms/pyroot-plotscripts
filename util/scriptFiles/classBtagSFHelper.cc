
// #ifndef BTagEntry_H
// #define BTagEntry_H

/**
 *
 * BTagEntry
 *
 * Represents one pt- or discriminator-dependent calibration function.
 *
 * measurement_type:    e.g. comb, ttbar, di-mu, boosted, ...
 * sys_type:            e.g. central, plus, minus, plus_JEC, plus_JER, ...
 *
 * Everything is converted into a function, as it is easiest to store it in a
 * txt or json file.
 *
 ************************************************************/

#include <string>
#include <TF1.h>
#include <TH1.h>
#include <TH3.h>


class BTagEntry
{
public:
  enum OperatingPoint {
    OP_LOOSE=0,
    OP_MEDIUM=1,
    OP_TIGHT=2,
    OP_RESHAPING=3,
  };
  enum JetFlavor {
    FLAV_B=0,
    FLAV_C=1,
    FLAV_UDSG=2,
  };
  struct Parameters {
    OperatingPoint operatingPoint;
    std::string measurementType;
    std::string sysType;
    JetFlavor jetFlavor;
    float etaMin;
    float etaMax;
    float ptMin;
    float ptMax;
    float discrMin;
    float discrMax;

    // default constructor
    Parameters(
      OperatingPoint op=OP_TIGHT,
      std::string measurement_type="comb",
      std::string sys_type="central",
      JetFlavor jf=FLAV_B,
      float eta_min=-99999.,
      float eta_max=99999.,
      float pt_min=0.,
      float pt_max=99999.,
      float discr_min=0.,
      float discr_max=99999.
    );

  };

  BTagEntry() {}
  BTagEntry(const std::string &csvLine);
  BTagEntry(const std::string &func, Parameters p);
  BTagEntry(const TF1* func, Parameters p);
  BTagEntry(const TH1* histo, Parameters p);
  ~BTagEntry() {}
  static std::string makeCSVHeader();
  std::string makeCSVLine() const;
  static std::string trimStr(std::string str);

  // public, no getters needed
  std::string formula;
  Parameters params;

};

// #endif  // BTagEntry_H


// #ifndef BTagCalibration_H
// #define BTagCalibration_H

/**
 * BTagCalibration
 *
 * The 'hierarchy' of stored information is this:
 * - by tagger (BTagCalibration)
 *   - by operating point or reshape bin
 *     - by jet parton flavor
 *       - by type of measurement
 *         - by systematic
 *           - by eta bin
 *             - as 1D-function dependent of pt or discriminant
 *
 ************************************************************/

#include <map>
#include <vector>
#include <string>
#include <istream>
#include <ostream>


class BTagCalibration
{
public:
  BTagCalibration() {}
  BTagCalibration(const std::string &tagger);
  BTagCalibration(const std::string &tagger, const std::string &filename);
  ~BTagCalibration() {}

  std::string tagger() const {return tagger_;}

  void addEntry(const BTagEntry &entry);
  const std::vector<BTagEntry>& getEntries(const BTagEntry::Parameters &par) const;

  void readCSV(std::istream &s);
  void readCSV(const std::string &s);
  void makeCSV(std::ostream &s) const;
  std::string makeCSV() const;

protected:
  static std::string token(const BTagEntry::Parameters &par);

  std::string tagger_;
  std::map<std::string, std::vector<BTagEntry> > data_;

};

// #endif  // BTagCalibration_H


// #ifndef BTagCalibrationReader_H
// #define BTagCalibrationReader_H

/**
 * BTagCalibrationReader
 *
 * Helper class to pull out a specific set of BTagEntry's out of a
 * BTagCalibration. TF1 functions are set up at initialization time.
 *
 ************************************************************/

#include <memory>
#include <string>



class BTagCalibrationReader
{
public:
  class BTagCalibrationReaderImpl;

  BTagCalibrationReader() {}
  BTagCalibrationReader(BTagEntry::OperatingPoint op,
                        const std::string & sysType="central",
                        const std::vector<std::string> & otherSysTypes={});

  void load(const BTagCalibration & c,
            BTagEntry::JetFlavor jf,
            const std::string & measurementType="comb");

  double eval(BTagEntry::JetFlavor jf,
              float eta,
              float pt,
              float discr=0.) const;

  double eval_auto_bounds(const std::string & sys,
                          BTagEntry::JetFlavor jf,
                          float eta,
                          float pt,
                          float discr=0.) const;

  std::pair<float, float> min_max_pt(BTagEntry::JetFlavor jf,
                                     float eta,
                                     float discr=0.) const;
protected:
  std::shared_ptr<BTagCalibrationReaderImpl> pimpl;
};

#include <iostream>
#include <exception>
#include <algorithm>
#include <sstream>


BTagEntry::Parameters::Parameters(
  OperatingPoint op,
  std::string measurement_type,
  std::string sys_type,
  JetFlavor jf,
  float eta_min,
  float eta_max,
  float pt_min,
  float pt_max,
  float discr_min,
  float discr_max
):
  operatingPoint(op),
  measurementType(measurement_type),
  sysType(sys_type),
  jetFlavor(jf),
  etaMin(eta_min),
  etaMax(eta_max),
  ptMin(pt_min),
  ptMax(pt_max),
  discrMin(discr_min),
  discrMax(discr_max)
{
  std::transform(measurementType.begin(), measurementType.end(),
                 measurementType.begin(), ::tolower);
  std::transform(sysType.begin(), sysType.end(),
                 sysType.begin(), ::tolower);
}

BTagEntry::BTagEntry(const std::string &csvLine)
{
  // make tokens
  std::stringstream buff(csvLine);
  std::vector<std::string> vec;
  std::string token;
  while (std::getline(buff, token, ","[0])) {
    token = BTagEntry::trimStr(token);
    if (token.empty()) {
      continue;
    }
    vec.push_back(token);
  }
  if (vec.size() != 11) {
std::cerr << "ERROR in BTagCalibration: "
          << "Invalid csv line; num tokens != 11: "
          << csvLine;
throw std::exception();
  }

  // clean string values
  char chars[] = " \"\n";
  for (unsigned int i = 0; i < strlen(chars); ++i) {
    vec[1].erase(remove(vec[1].begin(),vec[1].end(),chars[i]),vec[1].end());
    vec[2].erase(remove(vec[2].begin(),vec[2].end(),chars[i]),vec[2].end());
    vec[10].erase(remove(vec[10].begin(),vec[10].end(),chars[i]),vec[10].end());
  }

  // make formula
  formula = vec[10];
  TF1 f1("", formula.c_str());  // compile formula to check validity
  if (f1.IsZombie()) {
std::cerr << "ERROR in BTagCalibration: "
          << "Invalid csv line; formula does not compile: "
          << csvLine;
throw std::exception();
  }

  // make parameters
  unsigned op = stoi(vec[0]);
  if (op > 3) {
std::cerr << "ERROR in BTagCalibration: "
          << "Invalid csv line; OperatingPoint > 3: "
          << csvLine;
throw std::exception();
  }
  unsigned jf = stoi(vec[3]);
  if (jf > 2) {
std::cerr << "ERROR in BTagCalibration: "
          << "Invalid csv line; JetFlavor > 2: "
          << csvLine;
throw std::exception();
  }
  params = BTagEntry::Parameters(
    BTagEntry::OperatingPoint(op),
    vec[1],
    vec[2],
    BTagEntry::JetFlavor(jf),
    stof(vec[4]),
    stof(vec[5]),
    stof(vec[6]),
    stof(vec[7]),
    stof(vec[8]),
    stof(vec[9])
  );
}

BTagEntry::BTagEntry(const std::string &func, BTagEntry::Parameters p):
  formula(func),
  params(p)
{
  TF1 f1("", formula.c_str());  // compile formula to check validity
  if (f1.IsZombie()) {
std::cerr << "ERROR in BTagCalibration: "
          << "Invalid func string; formula does not compile: "
          << func;
throw std::exception();
  }
}

BTagEntry::BTagEntry(const TF1* func, BTagEntry::Parameters p):
  formula(std::string(func->GetExpFormula("p").Data())),
  params(p)
{
  if (func->IsZombie()) {
std::cerr << "ERROR in BTagCalibration: "
          << "Invalid TF1 function; function is zombie: "
          << func->GetName();
throw std::exception();
  }
}

// Creates chained step functions like this:
// "<prevous_bin> : x<bin_high_bound ? bin_value : <next_bin>"
// e.g. "x<0 ? 1 : x<1 ? 2 : x<2 ? 3 : 4"
std::string th1ToFormulaLin(const TH1* hist) {
  int nbins = hist->GetNbinsX();
  TAxis const* axis = hist->GetXaxis();
  std::stringstream buff;
  buff << "x<" << axis->GetBinLowEdge(1) << " ? 0. : ";  // default value
  for (int i=1; i<nbins+1; ++i) {
    char tmp_buff[50];
    sprintf(tmp_buff,
            "x<%g ? %g : ",  // %g is the smaller one of %e or %f
            axis->GetBinUpEdge(i),
            hist->GetBinContent(i));
    buff << tmp_buff;
  }
  buff << 0.;  // default value
  return buff.str();
}

// Creates step functions making a binary search tree:
// "x<mid_bin_bound ? (<left side tree>) : (<right side tree>)"
// e.g. "x<2 ? (x<1 ? (x<0 ? 0:0.1) : (1)) : (x<4 ? (x<3 ? 2:3) : (0))"
std::string th1ToFormulaBinTree(const TH1* hist, int start=0, int end=-1) {
  if (end == -1) {                      // initialize
    start = 0.;
    end = hist->GetNbinsX()+1;
    TH1* h2 = (TH1*) hist->Clone();
    h2->SetBinContent(start, 0);  // kill underflow
    h2->SetBinContent(end, 0);    // kill overflow
    std::string res = th1ToFormulaBinTree(h2, start, end);
    delete h2;
    return res;
  }
  if (start == end) {                   // leave is reached
    char tmp_buff[20];
    sprintf(tmp_buff, "%g", hist->GetBinContent(start));
    return std::string(tmp_buff);
  }
  if (start == end - 1) {               // no parenthesis for neighbors
    char tmp_buff[70];
    sprintf(tmp_buff,
            "x<%g ? %g:%g",
            hist->GetXaxis()->GetBinUpEdge(start),
            hist->GetBinContent(start),
            hist->GetBinContent(end));
    return std::string(tmp_buff);
  }

  // top-down recursion
  std::stringstream buff;
  int mid = (end-start)/2 + start;
  char tmp_buff[25];
  sprintf(tmp_buff,
          "x<%g ? (",
          hist->GetXaxis()->GetBinUpEdge(mid));
  buff << tmp_buff
       << th1ToFormulaBinTree(hist, start, mid)
       << ") : ("
       << th1ToFormulaBinTree(hist, mid+1, end)
       << ")";
  return buff.str();
}

BTagEntry::BTagEntry(const TH1* hist, BTagEntry::Parameters p):
  params(p)
{
  int nbins = hist->GetNbinsX();
  TAxis const* axis = hist->GetXaxis();

  // overwrite bounds with histo values
  if (params.operatingPoint == BTagEntry::OP_RESHAPING) {
    params.discrMin = axis->GetBinLowEdge(1);
    params.discrMax = axis->GetBinUpEdge(nbins);
  } else {
    params.ptMin = axis->GetBinLowEdge(1);
    params.ptMax = axis->GetBinUpEdge(nbins);
  }

  // balanced full binary tree height = ceil(log(2*n_leaves)/log(2))
  // breakes even around 10, but lower values are more propable in pt-spectrum
  if (nbins < 15) {
    formula = th1ToFormulaLin(hist);
  } else {
    formula = th1ToFormulaBinTree(hist);
  }

  // compile formula to check validity
  TF1 f1("", formula.c_str());
  if (f1.IsZombie()) {
std::cerr << "ERROR in BTagCalibration: "
          << "Invalid histogram; formula does not compile (>150 bins?): "
          << hist->GetName();
throw std::exception();
  }
}

std::string BTagEntry::makeCSVHeader()
{
  return "OperatingPoint, "
         "measurementType, "
         "sysType, "
         "jetFlavor, "
         "etaMin, "
         "etaMax, "
         "ptMin, "
         "ptMax, "
         "discrMin, "
         "discrMax, "
         "formula \n";
}

std::string BTagEntry::makeCSVLine() const
{
  std::stringstream buff;
  buff << params.operatingPoint
       << ", " << params.measurementType
       << ", " << params.sysType
       << ", " << params.jetFlavor
       << ", " << params.etaMin
       << ", " << params.etaMax
       << ", " << params.ptMin
       << ", " << params.ptMax
       << ", " << params.discrMin
       << ", " << params.discrMax
       << ", \"" << formula
       << "\" \n";
  return buff.str();
}

std::string BTagEntry::trimStr(std::string str) {
  size_t s = str.find_first_not_of(" \n\r\t");
  size_t e = str.find_last_not_of (" \n\r\t");

  if((std::string::npos == s) || (std::string::npos == e))
    return "";
  else
    return str.substr(s, e-s+1);
}


#include <fstream>
#include <sstream>



BTagCalibration::BTagCalibration(const std::string &taggr):
  tagger_(taggr)
{}

BTagCalibration::BTagCalibration(const std::string &taggr,
                                 const std::string &filename):
  tagger_(taggr)
{
  std::ifstream ifs(filename);
  if (!ifs.good()) {
std::cerr << "ERROR in BTagCalibration: "
          << "input file not available: "
          << filename;
throw std::exception();
  }
  readCSV(ifs);
  ifs.close();
}

void BTagCalibration::addEntry(const BTagEntry &entry)
{
  data_[token(entry.params)].push_back(entry);
}

const std::vector<BTagEntry>& BTagCalibration::getEntries(
  const BTagEntry::Parameters &par) const
{
  std::string tok = token(par);
  if (!data_.count(tok)) {
std::cerr << "ERROR in BTagCalibration: "
          << "(OperatingPoint, measurementType, sysType) not available: "
          << tok;
throw std::exception();
  }
  return data_.at(tok);
}

void BTagCalibration::readCSV(const std::string &s)
{
  std::stringstream buff(s);
  readCSV(buff);
}

void BTagCalibration::readCSV(std::istream &s)
{
  std::string line;

  // firstline might be the header
  getline(s,line);
  if (line.find("OperatingPoint") == std::string::npos) {
    addEntry(BTagEntry(line));
  }

  while (getline(s,line)) {
    line = BTagEntry::trimStr(line);
    if (line.empty()) {  // skip empty lines
      continue;
    }
    addEntry(BTagEntry(line));
  }
}

void BTagCalibration::makeCSV(std::ostream &s) const
{
  s << tagger_ << ";" << BTagEntry::makeCSVHeader();
  for (std::map<std::string, std::vector<BTagEntry> >::const_iterator i
           = data_.cbegin(); i != data_.cend(); ++i) {
    const std::vector<BTagEntry> &vec = i->second;
    for (std::vector<BTagEntry>::const_iterator j
             = vec.cbegin(); j != vec.cend(); ++j) {
      s << j->makeCSVLine();
    }
  }
}

std::string BTagCalibration::makeCSV() const
{
  std::stringstream buff;
  makeCSV(buff);
  return buff.str();
}

std::string BTagCalibration::token(const BTagEntry::Parameters &par)
{
  std::stringstream buff;
  buff << par.operatingPoint << ", "
       << par.measurementType << ", "
       << par.sysType;
  return buff.str();
}




class BTagCalibrationReader::BTagCalibrationReaderImpl
{
  friend class BTagCalibrationReader;

public:
  struct TmpEntry {
    float etaMin;
    float etaMax;
    float ptMin;
    float ptMax;
    float discrMin;
    float discrMax;
    TF1 func;
  };

private:
  BTagCalibrationReaderImpl(BTagEntry::OperatingPoint op,
                            const std::string & sysType,
                            const std::vector<std::string> & otherSysTypes={});

  void load(const BTagCalibration & c,
            BTagEntry::JetFlavor jf,
            std::string measurementType);

  double eval(BTagEntry::JetFlavor jf,
              float eta,
              float pt,
              float discr) const;

  double eval_auto_bounds(const std::string & sys,
                          BTagEntry::JetFlavor jf,
                          float eta,
                          float pt,
                          float discr) const;

  std::pair<float, float> min_max_pt(BTagEntry::JetFlavor jf,
                                     float eta,
                                     float discr) const;
 
  std::pair<float, float> min_max_eta(BTagEntry::JetFlavor jf,
                                     float discr) const;

  BTagEntry::OperatingPoint op_;
  std::string sysType_;
  std::vector<std::vector<TmpEntry> > tmpData_;  // first index: jetFlavor
  std::vector<bool> useAbsEta_;                  // first index: jetFlavor
  std::map<std::string, std::shared_ptr<BTagCalibrationReaderImpl>> otherSysTypeReaders_;
};


BTagCalibrationReader::BTagCalibrationReaderImpl::BTagCalibrationReaderImpl(
                                             BTagEntry::OperatingPoint op,
                                             const std::string & sysType,
                                             const std::vector<std::string> & otherSysTypes):
  op_(op),
  sysType_(sysType),
  tmpData_(3),
  useAbsEta_(3, true)
{
  for (const std::string & ost : otherSysTypes) {
    if (otherSysTypeReaders_.count(ost)) {
std::cerr << "ERROR in BTagCalibration: "
            << "Every otherSysType should only be given once. Duplicate: "
            << ost;
throw std::exception();
    }
    otherSysTypeReaders_[ost] = std::auto_ptr<BTagCalibrationReaderImpl>(
        new BTagCalibrationReaderImpl(op, ost)
    );
  }
}

void BTagCalibrationReader::BTagCalibrationReaderImpl::load(
                                             const BTagCalibration & c,
                                             BTagEntry::JetFlavor jf,
                                             std::string measurementType)
{
  if (tmpData_[jf].size()) {
std::cerr << "ERROR in BTagCalibration: "
          << "Data for this jet-flavor is already loaded: "
          << jf;
throw std::exception();
  }

  BTagEntry::Parameters params(op_, measurementType, sysType_);
  const std::vector<BTagEntry> &entries = c.getEntries(params);

  for (const auto &be : entries) {
    if (be.params.jetFlavor != jf) {
      continue;
    }

    TmpEntry te;
    te.etaMin = be.params.etaMin;
    te.etaMax = be.params.etaMax;
    te.ptMin = be.params.ptMin;
    te.ptMax = be.params.ptMax;
    te.discrMin = be.params.discrMin;
    te.discrMax = be.params.discrMax;

    if (op_ == BTagEntry::OP_RESHAPING) {
      te.func = TF1("", be.formula.c_str(),
                    be.params.discrMin, be.params.discrMax);
    } else {
      te.func = TF1("", be.formula.c_str(),
                    be.params.ptMin, be.params.ptMax);
    }

    tmpData_[be.params.jetFlavor].push_back(te);
    if (te.etaMin < 0) {
      useAbsEta_[be.params.jetFlavor] = false;
    }
  }

  for (auto & p : otherSysTypeReaders_) {
    p.second->load(c, jf, measurementType);
  }
}

double BTagCalibrationReader::BTagCalibrationReaderImpl::eval(
                                             BTagEntry::JetFlavor jf,
                                             float eta,
                                             float pt,
                                             float discr) const
{
  bool use_discr = (op_ == BTagEntry::OP_RESHAPING);
  if (useAbsEta_[jf] && eta < 0) {
    eta = -eta;
  }

  // search linearly through eta, pt and discr ranges and eval
  // future: find some clever data structure based on intervals
  const auto &entries = tmpData_.at(jf);
  for (unsigned i=0; i<entries.size(); ++i) {
    const auto &e = entries.at(i);
    if (
      e.etaMin <= eta && eta <= e.etaMax                   // find eta
      && e.ptMin < pt && pt <= e.ptMax                    // check pt
    ){
      if (use_discr) {                                    // discr. reshaping?
        if (e.discrMin <= discr && discr < e.discrMax) {  // check discr
          return e.func.Eval(discr);
        }
      } else {
        return e.func.Eval(pt);
      }
    }
  }

  return 0.;  // default value
}

double BTagCalibrationReader::BTagCalibrationReaderImpl::eval_auto_bounds(
                                             const std::string & sys,
                                             BTagEntry::JetFlavor jf,
                                             float eta,
                                             float pt,
                                             float discr) const
{
  auto sf_bounds_eta = min_max_eta(jf, discr);
  bool eta_is_out_of_bounds = false;

  if (sf_bounds_eta.first < 0) sf_bounds_eta.first = -sf_bounds_eta.second;   
  if (eta <= sf_bounds_eta.first || eta > sf_bounds_eta.second ) {
    eta_is_out_of_bounds = true;
  }
   
  if (eta_is_out_of_bounds) {
    return 1.;
  }


   auto sf_bounds = min_max_pt(jf, eta, discr);
   float pt_for_eval = pt;
   bool is_out_of_bounds = false;

   if (pt <= sf_bounds.first) {
    pt_for_eval = sf_bounds.first + .0001;
    is_out_of_bounds = true;
  } else if (pt > sf_bounds.second) {
    pt_for_eval = sf_bounds.second - .0001;
    is_out_of_bounds = true;
  }

  // get central SF (and maybe return)
  double sf = eval(jf, eta, pt_for_eval, discr);
  if (sys == sysType_) {
    return sf;
  }

  // get sys SF (and maybe return)
  if (!otherSysTypeReaders_.count(sys)) {
std::cerr << "ERROR in BTagCalibration: "
        << "sysType not available (maybe not loaded?): "
        << sys;
throw std::exception();
  }
  double sf_err = otherSysTypeReaders_.at(sys)->eval(jf, eta, pt_for_eval, discr);
  if (!is_out_of_bounds) {
    return sf_err;
  }

  // double uncertainty on out-of-bounds and return
  sf_err = sf + 2*(sf_err - sf);
  return sf_err;
}

std::pair<float, float> BTagCalibrationReader::BTagCalibrationReaderImpl::min_max_pt(
                                               BTagEntry::JetFlavor jf,
                                               float eta,
                                               float discr) const
{
  bool use_discr = (op_ == BTagEntry::OP_RESHAPING);
  if (useAbsEta_[jf] && eta < 0) {
    eta = -eta;
  }

  const auto &entries = tmpData_.at(jf);
  float min_pt = -1., max_pt = -1.;
  for (const auto & e: entries) {
    if (
      e.etaMin <= eta && eta <=e.etaMax                   // find eta
    ){
      if (min_pt < 0.) {                                  // init
        min_pt = e.ptMin;
        max_pt = e.ptMax;
        continue;
      }

      if (use_discr) {                                    // discr. reshaping?
        if (e.discrMin <= discr && discr < e.discrMax) {  // check discr
          min_pt = min_pt < e.ptMin ? min_pt : e.ptMin;
          max_pt = max_pt > e.ptMax ? max_pt : e.ptMax;
        }
      } else {
        min_pt = min_pt < e.ptMin ? min_pt : e.ptMin;
        max_pt = max_pt > e.ptMax ? max_pt : e.ptMax;
      }
    }
  }

  return std::make_pair(min_pt, max_pt);
}

std::pair<float, float> BTagCalibrationReader::BTagCalibrationReaderImpl::min_max_eta(
                                               BTagEntry::JetFlavor jf,
                                               float discr) const
{
  bool use_discr = (op_ == BTagEntry::OP_RESHAPING);

  const auto &entries = tmpData_.at(jf);
  float min_eta = 0., max_eta = 0.;
  for (const auto & e: entries) {

      if (use_discr) {                                    // discr. reshaping?
        if (e.discrMin <= discr && discr < e.discrMax) {  // check discr
          min_eta = min_eta < e.etaMin ? min_eta : e.etaMin;
          max_eta = max_eta > e.etaMax ? max_eta : e.etaMax;
        }
      } else {
        min_eta = min_eta < e.etaMin ? min_eta : e.etaMin;
        max_eta = max_eta > e.etaMax ? max_eta : e.etaMax;
      }
    }


  return std::make_pair(min_eta, max_eta);
}


BTagCalibrationReader::BTagCalibrationReader(BTagEntry::OperatingPoint op,
                                             const std::string & sysType,
                                             const std::vector<std::string> & otherSysTypes):
  pimpl(new BTagCalibrationReaderImpl(op, sysType, otherSysTypes)) {}

void BTagCalibrationReader::load(const BTagCalibration & c,
                                 BTagEntry::JetFlavor jf,
                                 const std::string & measurementType)
{
  pimpl->load(c, jf, measurementType);
}

double BTagCalibrationReader::eval(BTagEntry::JetFlavor jf,
                                   float eta,
                                   float pt,
                                   float discr) const
{
  return pimpl->eval(jf, eta, pt, discr);
}

double BTagCalibrationReader::eval_auto_bounds(const std::string & sys,
                                               BTagEntry::JetFlavor jf,
                                               float eta,
                                               float pt,
                                               float discr) const
{
  return pimpl->eval_auto_bounds(sys, jf, eta, pt, discr);
}

std::pair<float, float> BTagCalibrationReader::min_max_pt(BTagEntry::JetFlavor jf,
                                                          float eta,
                                                          float discr) const
{
  return pimpl->min_max_pt(jf, eta, discr);
}

// From here on usercode!!!

class BtagSFHelper {
   public:
    // standard constructor
    BtagSFHelper();
    // another constructor
    BtagSFHelper(const std::string& csvFile, const std::string& effFile, const std::string& type, const double& WP);
    void init(const std::string& csvFile, const std::string& effFile, const std::string& type, const double& WP);
    // double getCSVWeight(const std::vector< double >& jetPts, const std::vector< double >& jetEtas, const std::vector< double >& jetCSVs,  const std::vector< int >& jetFlavors,  const std::string& LFvariation, const std::string& HFvariation);
    // double getCSVWeight(const std::vector< double >& jetPts_tagged, const std::vector< double >& jetEtas_tagged, const std::vector< int >& jetFlavors_tagged,
    //                     const std::vector< double >& jetPts_untagged, const std::vector< double >& jetEtas_untagged, const std::vector< int >& jetFlavors_untagged,
    //                     const std::string& LFvariation, const std::string& HFvariation);
    // double getCSVWeight_MethodOneB_ge1t(const std::vector< double >& jetPts, const std::vector< double >& jetEtas, const std::vector< int >& jetFlavors,
                                      //  const std::string& LFvariation, const std::string& HFvariation, bool tag);
    // double getCSVWeight_MethodOneB_1t(const std::vector< double >& jetPts, const std::vector< double >& jetEtas, const std::vector< int >& jetFlavors,
    //                                    const std::string& LFvariation, const std::string& HFvariation, bool tag);
    std::pair<double, double> getCSVWeight_0B(const std::vector< double >& jetPts, const std::vector< double >& jetEtas, const std::vector< int >& jetFlavors,
                                       const std::string& LFvariation, const std::string& HFvariation);
    std::pair<double, double> getCSVWeight_1B(const std::vector< double >& jetPts, const std::vector< double >& jetEtas, const std::vector< int >& jetFlavors,
                                       const std::string& LFvariation, const std::string& HFvariation);
        
    
    double getEff(const double& jetPt, const double& jetEta, const int& jetFlavor);
    // destructor
    ~BtagSFHelper();
   private:
    bool isInit_;
    double wp;
    TH3* h_eff = NULL;
    BTagCalibration calib;
    BTagCalibrationReader reader;
};

BtagSFHelper::BtagSFHelper(const std::string& csvFile, const std::string& effFile, const std::string& type, const double& WP)
    // isInit_(false),
{
    init(csvFile, effFile, type, WP);
}

void BtagSFHelper::init(const std::string& csvFile, const std::string& effFile, const std::string& type, const double& WP)
{
    std::cout << "Initializing b-tag scale factors" << std::endl;
    wp = WP;
    std::cout << "Setting working point to " << wp << std::endl;
    BTagEntry::OperatingPoint wp_;
    std::string h_eff_name = "";
    if (type == "loose") {
      wp_ = BTagEntry::OP_LOOSE;
      h_eff_name = "loose_btagging_efficiency_leptonic";
    }
    else if (type == "medium") {
      wp_ = BTagEntry::OP_MEDIUM;
      h_eff_name = "medium_btagging_efficiency_leptonic";
    }
    else if (type == "medium_outside") {
      wp_ = BTagEntry::OP_MEDIUM;
      h_eff_name = "medium_btagging_efficiency_outside_hadronic";
    }
    else if (type == "loose_outside") {
      wp_ = BTagEntry::OP_LOOSE;
      h_eff_name = "loose_btagging_efficiency_outside_hadronic";
    }
    else{
      std::cout << "Please specifiy meaningful WP. Options are 'loose', 'medium', 'medium_outside', 'loose_outside' !!!" << std::endl;
    }

    // setup calibration + reader
    calib = BTagCalibration("csvv1", csvFile);
    reader = BTagCalibrationReader(wp_,  // operating point
                                "central",             // central sys type
                                {"up", "down"});      // other sys types
    reader.load(calib,                // calibration instance
                BTagEntry::FLAV_B,    // btag flavour
                "comb");               // measurement type
    reader.load(calib,                // calibration instance
                BTagEntry::FLAV_C,    // btag flavour
                "comb");               // measurement type
    reader.load(calib,                // calibration instance
                BTagEntry::FLAV_UDSG, // btag flavour
                "incl");               // measurement type
    TFile* f_eff = new TFile((effFile).c_str());
    f_eff->GetObject(h_eff_name.c_str(), h_eff);
    if (h_eff == NULL) {
        std::cerr << "BadCSVWeightInit" << std::endl << "Could not find CSV SF histogram '" << h_eff_name << "' in file '" << f_eff->GetName() << "'";
    }
    h_eff->SetDirectory(0);
        
    isInit_ = true;
}

// double BtagSFHelper::getCSVWeight(const std::vector< double >& jetPts, const std::vector< double >& jetEtas, const std::vector< double >& jetCSVs, const std::vector< int >& jetFlavors, const std::string& LFvariation, const std::string& HFvariation){
//   double p_mc = 1.;
//   double p_data = 1.;
//   double sf = 1.;
//   double eff = 1.;
//   for (int i=0; i<jetPts.size(); ++i){
//     if (abs(jetFlavors[i]) == 5) {
//       sf = reader.eval_auto_bounds( HFvariation, 
//                                     BTagEntry::FLAV_B, 
//                                     abs(jetEtas[i]), // absolute value of eta
//                                     jetPts[i]
//                                 ); 
//     } 
//     else if (abs(jetFlavors[i]) == 4) {
//       sf = reader.eval_auto_bounds( HFvariation, 
//                                 BTagEntry::FLAV_C, 
//                                 abs(jetEtas[i]), // absolute value of eta
//                                 jetPts[i]
//                             ); 
//     }
//     else {
//       sf = reader.eval_auto_bounds( LFvariation, 
//                                 BTagEntry::FLAV_UDSG, 
//                                 abs(jetEtas[i]), // absolute value of eta
//                                 jetPts[i]
//                             );       
//     }
//     eff = getEff(jetPts[i], jetEtas[i], jetFlavors[i]);
//     // std::cout << "-------------------------" << std::endl;
//     // std::cout << "pt, eta, flav" << std::endl;
//     // std::cout << jetPts[i] << ", " << jetEtas[i] << ", " << jetFlavors[i] << std::endl;
//     // std::cout << "sf, eff, p_mc, p_data" << std::endl;
//     // std::cout << sf << ", "<< eff << ", " << p_mc<< ", " << p_data << std::endl;
//     if (jetCSVs[i] > wp){
//       p_mc *= eff;
//       p_data *= eff*sf;
//     }
//     else {
//       p_mc *= 1-eff;
//       p_data *= 1-(eff*sf);
//     }
//   }
//   return p_data/p_mc;
// }

// double BtagSFHelper::getCSVWeight(const std::vector< double >& jetPts_tagged, const std::vector< double >& jetEtas_tagged, const std::vector< int >& jetFlavors_tagged,
//                                   const std::vector< double >& jetPts_untagged, const std::vector< double >& jetEtas_untagged, const std::vector< int >& jetFlavors_untagged,
//                                   const std::string& LFvariation, const std::string& HFvariation){
//   double p_mc = 1.;
//   double p_data = 1.;
//   double sf = 1.;
//   double eff = 1.;
//   // tagged Jets
//   for (int i=0; i<jetPts_tagged.size(); ++i){
//     // std::cout << "--------tagged----------" << std::endl;
//     // h_eff->Print();
//     if (abs(jetFlavors_tagged[i]) == 5) {
//       sf = reader.eval_auto_bounds( HFvariation, 
//                                     BTagEntry::FLAV_B, 
//                                     abs(jetEtas_tagged[i]), // absolute value of eta
//                                     jetPts_tagged[i]
//                                 ); 
//       // std::cout << "Flav 5: SF = " << sf << std::endl;
//     } 
//     else if (abs(jetFlavors_tagged[i]) == 4) {
//       sf = reader.eval_auto_bounds( HFvariation, 
//                                 BTagEntry::FLAV_C, 
//                                 abs(jetEtas_tagged[i]), // absolute value of eta
//                                 jetPts_tagged[i]
//                             ); 
//     }
//     else {
//       sf = reader.eval_auto_bounds( LFvariation, 
//                                 BTagEntry::FLAV_UDSG, 
//                                 abs(jetEtas_tagged[i]), // absolute value of eta
//                                 jetPts_tagged[i]
//                             );       
//     }
//     eff = getEff(jetPts_tagged[i], jetEtas_tagged[i], jetFlavors_tagged[i]);
//     p_mc *= eff;
//     p_data *= eff*sf;
//     // std::cout << "LFvariation, HFvariation" << std::endl;
//     // std::cout << LFvariation << ", " << HFvariation << std::endl;
//     // std::cout << "pt, eta, flav" << std::endl;
//     // std::cout << jetPts_tagged[i] << ", " << jetEtas_tagged[i] << ", " << jetFlavors_tagged[i] << std::endl;
//     // std::cout << "sf, eff, p_mc, p_data" << std::endl;
//     // std::cout << sf << ", "<< eff << ", " << p_mc<< ", " << p_data << std::endl;
//   }
//   // untagged jets
//   for (int i=0; i<jetPts_untagged.size(); ++i){
//     if (abs(jetFlavors_untagged[i]) == 5) {
//       sf = reader.eval_auto_bounds( HFvariation, 
//                                     BTagEntry::FLAV_B, 
//                                     abs(jetEtas_untagged[i]), // absolute value of eta
//                                     jetPts_untagged[i]
//                                 ); 
//     } 
//     else if (abs(jetFlavors_untagged[i]) == 4) {
//       sf = reader.eval_auto_bounds( HFvariation, 
//                                 BTagEntry::FLAV_C, 
//                                 abs(jetEtas_untagged[i]), // absolute value of eta
//                                 jetPts_untagged[i]
//                             ); 
//     }
//     else {
//       sf = reader.eval_auto_bounds( LFvariation, 
//                                 BTagEntry::FLAV_UDSG, 
//                                 abs(jetEtas_untagged[i]), // absolute value of eta
//                                 jetPts_untagged[i]
//                             );       
//     }
//     eff = getEff(jetPts_untagged[i], jetEtas_untagged[i], jetFlavors_untagged[i]);
//     p_mc *= 1-eff;
//     p_data *= 1-(eff*sf);
//     // std::cout << "-------untagged---------" << std::endl;
//     // std::cout << "pt, eta, flav" << std::endl;
//     // std::cout << jetPts_untagged[i] << ", " << jetEtas_untagged[i] << ", " << jetFlavors_untagged[i] << std::endl;
//     // std::cout << "sf, eff, p_mc, p_data" << std::endl;
//     // std::cout << sf << ", "<< eff << ", " << p_mc<< ", " << p_data << std::endl;
//   }
//   return p_data/p_mc;
// }

// double BtagSFHelper::getCSVWeight_MethodOneB_ge1t(const std::vector< double >& jetPts, const std::vector< double >& jetEtas, const std::vector< int >& jetFlavors,
//                                        const std::string& LFvariation, const std::string& HFvariation, bool tag){
//   double eff = 1.;
//   double sf = 1.;
//   double w_zeroTags_num = 1.;
//   double w_zeroTags_den = 1.;
//   // all Jets
//   for (int i=0; i<jetPts.size(); ++i){
//     // h_eff->Print();
//     if (abs(jetFlavors[i]) == 5) {
//       sf = reader.eval_auto_bounds( HFvariation, BTagEntry::FLAV_B, abs(jetEtas[i]), jetPts[i]); 
//     } 
//     else if (abs(jetFlavors[i]) == 4) {
//       sf = reader.eval_auto_bounds( HFvariation, BTagEntry::FLAV_C, abs(jetEtas[i]), jetPts[i]); 
//     }
//     else {
//       sf = reader.eval_auto_bounds( LFvariation, BTagEntry::FLAV_UDSG, abs(jetEtas[i]), jetPts[i]); 
//     }
//     eff = getEff(jetPts[i], jetEtas[i], jetFlavors[i]);
//     w_zeroTags_num *= (1-sf*eff);
//     w_zeroTags_den *= (1-eff);
          
//     // std::cout << "LFvariation, HFvariation" << std::endl;
//     // std::cout << LFvariation << ", " << HFvariation << std::endl;
//     // std::cout << "pt, eta, flav" << std::endl;
//     // std::cout << jetPts[i] << ", " << jetEtas[i] << ", " << jetFlavors[i] << std::endl;
//     // std::cout << "sf, eff, w_zeroTags" << std::endl;
//     // std::cout << sf << ", "<< eff << ", " << w_zeroTags << std::endl;
//   }
//   if (tag == false) return w_zeroTags_num/w_zeroTags_den;
//   else if (tag == true){
//     if (1-w_zeroTags_den == 0.) return 0.;
//     else return (1-w_zeroTags_num)/(1-w_zeroTags_den);
  
//   }
// }

// double BtagSFHelper::getCSVWeight_MethodOneB_1t(const std::vector< double >& jetPts, const std::vector< double >& jetEtas, const std::vector< int >& jetFlavors,
//                                        const std::string& LFvariation, const std::string& HFvariation, bool tag){
//   double eff_i = 1.;
//   double eff_j = 1.;
//   double sf_i = 1.;
//   double sf_j = 1.;
//   double w_oneTag_num = 1.;
//   double w_oneTag_den = 1.;
//   double w_zeroTags_num = 1.;
//   double w_zeroTags_den = 1.;
//   // all Jets
//   for (int i=0; i<jetPts.size(); ++i){
//     w_zeroTags_num = 1.;
//     w_zeroTags_den = 1.;
//     eff_i = getEff(jetPts[i], jetEtas[i], jetFlavors[i]);
//     if (abs(jetFlavors[i]) == 5) {
//       sf_i = reader.eval_auto_bounds( HFvariation, BTagEntry::FLAV_B, abs(jetEtas[i]), jetPts[i] ); 
//     } 
//     else if (abs(jetFlavors[i]) == 4) {
//       sf_i = reader.eval_auto_bounds( HFvariation, BTagEntry::FLAV_C, abs(jetEtas[i]), jetPts[i] ); 
//     }
//     else {
//       sf_i = reader.eval_auto_bounds( LFvariation, BTagEntry::FLAV_UDSG, abs(jetEtas[i]), jetPts[i] ); 
//     }

//     for (int j=0; (j<jetPts.size()) && (i!=j); ++j){
//       if (abs(jetFlavors[i]) == 5) {
//         sf_j = reader.eval_auto_bounds( HFvariation, BTagEntry::FLAV_B, abs(jetEtas[j]), jetPts[j]); 
//       } 
//       else if (abs(jetFlavors[i]) == 4) {
//         sf_j = reader.eval_auto_bounds( HFvariation, BTagEntry::FLAV_C, abs(jetEtas[j]), jetPts[j]); 
//       }
//       else {
//         sf_j = reader.eval_auto_bounds( LFvariation, BTagEntry::FLAV_UDSG, abs(jetEtas[j]), jetPts[j]); 
//       }
//       eff_j = getEff(jetPts[j], jetEtas[j], jetFlavors[j]);
//       w_zeroTags_num *= (1-sf_j*eff_j);
//       w_zeroTags_den *= (1-eff_j);
//     }
//     w_oneTag_num += eff_i*w_zeroTags_num;
//     w_oneTag_den += sf_i*eff_i*w_zeroTags_den;
//   }
//   // if tag == True: ???
//   return w_oneTag_num/w_oneTag_den;
  
// }


double BtagSFHelper::getEff(const double& jetPt, const double& jetEta, const int& jetFlavor){
  return h_eff->GetBinContent(h_eff->FindBin(jetPt,abs(jetEta),jetFlavor));
}

// btag weights according to modified Version of 1B from https://twiki.cern.ch/twiki/bin/view/CMS/BTagSFMethods
std::pair<double, double> BtagSFHelper::getCSVWeight_0B(const std::vector< double >& jetPts, const std::vector< double >& jetEtas, const std::vector< int >& jetFlavors,
                                       const std::string& LFvariation, const std::string& HFvariation){
  double eff = 1.;
  double sf = 1.;
  double w_zeroTags_num = 1.;
  double w_zeroTags_den = 1.;
  // all Jets
  for (int i=0; i<jetPts.size(); ++i){
    // h_eff->Print();
    if (abs(jetFlavors[i]) == 5) {
      sf = reader.eval_auto_bounds( HFvariation, BTagEntry::FLAV_B, abs(jetEtas[i]), jetPts[i]); 
    } 
    else if (abs(jetFlavors[i]) == 4) {
      sf = reader.eval_auto_bounds( HFvariation, BTagEntry::FLAV_C, abs(jetEtas[i]), jetPts[i]); 
    }
    else {
      sf = reader.eval_auto_bounds( LFvariation, BTagEntry::FLAV_UDSG, abs(jetEtas[i]), jetPts[i]); 
    }
    eff = getEff(jetPts[i], jetEtas[i], jetFlavors[i]);
    w_zeroTags_num *= (1-sf*eff);
    w_zeroTags_den *= (1-eff);
          
    // std::cout << "LFvariation, HFvariation" << std::endl;
    // std::cout << LFvariation << ", " << HFvariation << std::endl;
    // std::cout << "pt, eta, flav" << std::endl;
    // std::cout << jetPts[i] << ", " << jetEtas[i] << ", " << jetFlavors[i] << std::endl;
    // std::cout << "sf, eff, w_zeroTags" << std::endl;
    // std::cout << sf << ", "<< eff << ", " << w_zeroTags << std::endl;
  }
  return std::make_pair(w_zeroTags_num, w_zeroTags_den);
}

std::pair<double, double> BtagSFHelper::getCSVWeight_1B(const std::vector< double >& jetPts, const std::vector< double >& jetEtas, const std::vector< int >& jetFlavors,
                                       const std::string& LFvariation, const std::string& HFvariation){
  double eff_i = 1.;
  double eff_j = 1.;
  double sf_i = 1.;
  double sf_j = 1.;
  double w_oneTag_num = 0.;
  double w_oneTag_den = 0.;
  double w_zeroTags_num = 1.;
  double w_zeroTags_den = 1.;
  // all Jets
  for (int i=0; i<jetPts.size(); ++i){
    w_zeroTags_num = 1.;
    w_zeroTags_den = 1.;
    eff_i = getEff(jetPts[i], jetEtas[i], jetFlavors[i]);
    if (abs(jetFlavors[i]) == 5) {
      sf_i = reader.eval_auto_bounds( HFvariation, BTagEntry::FLAV_B, abs(jetEtas[i]), jetPts[i] ); 
    } 
    else if (abs(jetFlavors[i]) == 4) {
      sf_i = reader.eval_auto_bounds( HFvariation, BTagEntry::FLAV_C, abs(jetEtas[i]), jetPts[i] ); 
    }
    else {
      sf_i = reader.eval_auto_bounds( LFvariation, BTagEntry::FLAV_UDSG, abs(jetEtas[i]), jetPts[i] ); 
    }

    for (int j=0; j<jetPts.size(); ++j){
      if (i == j) continue;
      if (abs(jetFlavors[j]) == 5) {
        sf_j = reader.eval_auto_bounds( HFvariation, BTagEntry::FLAV_B, abs(jetEtas[j]), jetPts[j]); 
      } 
      else if (abs(jetFlavors[j]) == 4) {
        sf_j = reader.eval_auto_bounds( HFvariation, BTagEntry::FLAV_C, abs(jetEtas[j]), jetPts[j]); 
      }
      else {
        sf_j = reader.eval_auto_bounds( LFvariation, BTagEntry::FLAV_UDSG, abs(jetEtas[j]), jetPts[j]); 
      }
      eff_j = getEff(jetPts[j], jetEtas[j], jetFlavors[j]);
      w_zeroTags_num *= (1-sf_j*eff_j);
      w_zeroTags_den *= (1-eff_j);
    }
    w_oneTag_num += sf_i*eff_i*w_zeroTags_num;
    w_oneTag_den += eff_i*w_zeroTags_den;
  }
  return std::make_pair(w_oneTag_num, w_oneTag_den);
  
}

