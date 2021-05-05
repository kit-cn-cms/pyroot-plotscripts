#include "../interface/Systematics.h"
// Systematics enum from MiniAODHelper. Needed for the CSV helper (date 26.06.2017)


std::map<Systematics::Type,std::string> Systematics::typeStringMap_ = std::map<Systematics::Type,std::string>();
std::map<std::string,Systematics::Type> Systematics::stringTypeMap_ = std::map<std::string,Systematics::Type>();
std::map<Systematics::Type,std::string> Systematics::typeLabelMap_  = std::map<Systematics::Type,std::string>();


void Systematics::init() {
  add( JESup,JESdown,"JES","Uncertainty");
  add( JERup,JERdown,"JER","JER");
  // JEY groups
  add( JERpt0eta0up,JERpt0eta0down,"JERpt0eta0","JERpt0eta0");
  add( JERpt0eta1up,JERpt0eta1down,"JERpt0eta1","JERpt0eta1");
  add( JERpt1eta0up,JERpt1eta0down,"JERpt1eta0","JERpt1eta0");
  add( JERpt1eta1up,JERpt1eta1down,"JERpt1eta1","JERpt1eta1");
  add( JEReta2up,JEReta2down,"JEReta2","JEReta2");

  add(JESAbsoluteup,             JESAbsolutedown,            "JESAbsolute",              "Absolute"          );
  add(JESAbsoluteyearup,         JESAbsoluteyeardown,        "JESAbsoluteyear",          "Absoluteyear"       );
  // add(JESFlavorQCDup,            JESFlavorQCDdown,           "JESFlavorQCD",             "FlavorQCD"           );
  add(JESBBEC1up,                JESBBEC1down,               "JESBBEC1",                 "BBEC1"               );
  add(JESBBEC1yearup,            JESBBEC1yeardown,           "JESBBEC1year",             "BBEC1year"          );
  add(JESEC2up,                  JESEC2down,                 "JESEC2",                   "EC2"                 );
  add(JESEC2yearup,              JESEC2yeardown,             "JESEC2year",               "EC2year"            );
  add(JESHFup,                   JESHFdown,                  "JESHF",                    "HF"                  );
  add(JESHFyearup,               JESHFyeardown,              "JESHFyear",                "HFyear"             );
  // add(JESRelativeBalup,          JESRelativeBaldown,         "JESRelativeBal",           "RelativeBal"         );
  add(JESRelativeSampleyearup,   JESRelativeSampleyeardown,  "JESRelativeSampleyear",    "RelativeSampleyear" );

  // all sources
  add( JESAbsoluteStatup,        JESAbsoluteStatdown,        "JESAbsoluteStat",          "AbsoluteStat"        );             
  add( JESAbsoluteScaleup,       JESAbsoluteScaledown,       "JESAbsoluteScale",         "AbsoluteScale"       );             
  add( JESAbsoluteFlavMapup,     JESAbsoluteFlavMapdown,     "JESAbsoluteFlavMap",       "AbsoluteFlavMap"     );                             
  add( JESAbsoluteMPFBiasup,     JESAbsoluteMPFBiasdown,     "JESAbsoluteMPFBias",       "AbsoluteMPFBias"     );                             
  add( JESFragmentationup,       JESFragmentationdown,       "JESFragmentation",         "Fragmentation"       );             
  add( JESSinglePionECALup,      JESSinglePionECALdown,      "JESSinglePionECAL",        "SinglePionECAL"      );                             
  add( JESSinglePionHCALup,      JESSinglePionHCALdown,      "JESSinglePionHCAL",        "SinglePionHCAL"      );                             
  add( JESFlavorQCDup,           JESFlavorQCDdown,           "JESFlavorQCD",             "FlavorQCD"           );                        
  add( JESTimePtEtaup,           JESTimePtEtadown,           "JESTimePtEta",             "TimePtEta"           ); 
  // HEM
  add( JESHEMup,                 JESHEMdown,                 "JESHEMIssue",              "HEMIssue"            );

  add( JESRelativeSampleup,      JESRelativeSampledown,      "JESRelativeSample",        "RelativeSample"      );                       
  add( JESRelativeJEREC1up,      JESRelativeJEREC1down,      "JESRelativeJEREC1",        "RelativeJEREC1"      );                             
  add( JESRelativeJEREC2up,      JESRelativeJEREC2down,      "JESRelativeJEREC2",        "RelativeJEREC2"      );                             
  add( JESRelativeJERHFup,       JESRelativeJERHFdown,       "JESRelativeJERHF",         "RelativeJERHF"       );             
  add( JESRelativePtBBup,        JESRelativePtBBdown,        "JESRelativePtBB",          "RelativePtBB"        );             
  add( JESRelativePtEC1up,       JESRelativePtEC1down,       "JESRelativePtEC1",         "RelativePtEC1"       );             
  add( JESRelativePtEC2up,       JESRelativePtEC2down,       "JESRelativePtEC2",         "RelativePtEC2"       );             
  add( JESRelativePtHFup,        JESRelativePtHFdown,        "JESRelativePtHF",          "RelativePtHF"        );             
  add( JESRelativeBalup,         JESRelativeBaldown,         "JESRelativeBal",           "RelativeBal"         );                        
  add( JESRelativeFSRup,         JESRelativeFSRdown,         "JESRelativeFSR",           "RelativeFSR"         );                        
  add( JESRelativeStatFSRup,     JESRelativeStatFSRdown,     "JESRelativeStatFSR",       "RelativeStatFSR"     );                             
  add( JESRelativeStatECup,      JESRelativeStatECdown,      "JESRelativeStatEC",        "RelativeStatEC"      );                             
  add( JESRelativeStatHFup,      JESRelativeStatHFdown,      "JESRelativeStatHF",        "RelativeStatHF"      );                             
  add( JESPileUpDataMCup,        JESPileUpDataMCdown,        "JESPileUpDataMC",          "PileUpDataMC"        );             
  add( JESPileUpPtRefup,         JESPileUpPtRefdown,         "JESPileUpPtRef",           "PileUpPtRef"         );                        
  add( JESPileUpPtBBup,          JESPileUpPtBBdown,          "JESPileUpPtBB",            "PileUpPtBB"          );                        
  add( JESPileUpPtEC1up,         JESPileUpPtEC1down,         "JESPileUpPtEC1",           "PileUpPtEC1"         );                        
  add( JESPileUpPtEC2up,         JESPileUpPtEC2down,         "JESPileUpPtEC2",           "PileUpPtEC2"         );                        
  add( JESPileUpPtHFup,          JESPileUpPtHFdown,          "JESPileUpPtHF",            "PileUpPtHF"          );                        
  add( JESPileUpMuZeroup,        JESPileUpMuZerodown,        "JESPileUpMuZero",          "PileUpMuZero"        );             
  add( JESPileUpEnvelopeup,      JESPileUpEnvelopedown,      "JESPileUpEnvelope",        "PileUpEnvelope"      );                             
  add( JESSubTotalPileUpup,      JESSubTotalPileUpdown,      "JESSubTotalPileUp",        "SubTotalPileUp"      );                             
  add( JESSubTotalRelativeup,    JESSubTotalRelativedown,    "JESSubTotalRelative",      "SubTotalRelative"    );                             
  add( JESSubTotalPtup,          JESSubTotalPtdown,          "JESSubTotalPt",            "SubTotalPt"          );                        
  add( JESSubTotalScaleup,       JESSubTotalScaledown,       "JESSubTotalScale",         "SubTotalScale"       );             
  add( JESSubTotalAbsoluteup,    JESSubTotalAbsolutedown,    "JESSubTotalAbsolute",      "SubTotalAbsolute"    );                             
  add( JESSubTotalMCup,          JESSubTotalMCdown,          "JESSubTotalMC",            "SubTotalMC"          );                        
  add( JESTotalup,               JESTotaldown,               "JESTotal",                 "Total"               );
                 
  add( JESTotalNoFlavorup,       JESTotalNoFlavordown,       "JESTotalNoFlavor",         "TotalNoFlavor"       );             
  add( JESTotalNoTimeup,         JESTotalNoTimedown,         "JESTotalNoTime",           "TotalNoTime"         );                        
  add( JESTotalNoFlavorNoTimeup, JESTotalNoFlavorNoTimedown, "JESTotalNoFlavorNoTime",   "TotalNoFlavorNoTime" );                    
  add( JESFlavorZJetup,          JESFlavorZJetdown,          "JESFlavorZJet",            "FlavorZJet"          );                        
  add( JESFlavorPhotonJetup,     JESFlavorPhotonJetdown,     "JESFlavorPhotonJet",       "FlavorPhotonJet"     );                             
  add( JESFlavorPureGluonup,     JESFlavorPureGluondown,     "JESFlavorPureGluon",       "FlavorPureGluon"     );                             
  add( JESFlavorPureQuarkup,     JESFlavorPureQuarkdown,     "JESFlavorPureQuark",       "FlavorPureQuark"     );                             
  add( JESFlavorPureCharmup,     JESFlavorPureCharmdown,     "JESFlavorPureCharm",       "FlavorPureCharm"     );                             
  add( JESFlavorPureBottomup,    JESFlavorPureBottomdown,    "JESFlavorPureBottom",      "FlavorPureBottom"    );                             
  add( JESTimeRunBCDup,          JESTimeRunBCDdown,          "JESTimeRunBCD",            "TimeRunBCD"          );                  
  add( JESTimeRunEFup,           JESTimeRunEFdown,           "JESTimeRunEF",             "TimeRunEF"           );                        
  add( JESTimeRunGup,            JESTimeRunGdown,            "JESTimeRunG",              "TimeRunG"            );                                 
  add( JESTimeRunHup,            JESTimeRunHdown,            "JESTimeRunH",              "TimeRunH"            );

  add( CSVLFup,                  CSVLFdown,                  "CSVLF",                    "LF"                  );
  add( CSVHFup,                  CSVHFdown,                  "CSVHF",                    "HF"                  );
  add( CSVLFStats1up,            CSVLFStats1down,            "CSVLFStats1",              "LFStats1"            );
  add( CSVHFStats1up,            CSVHFStats1down,            "CSVHFStats1",              "HFStats1"            );
  add( CSVLFStats2up,            CSVLFStats2down,            "CSVLFStats2",              "LFStats2"            );
  add( CSVHFStats2up,            CSVHFStats2down,            "CSVHFStats2",              "HFStats2"            );
  add( CSVCErr1up,               CSVCErr1down,               "CSVcErr1",                 "CErr1"               );
  add( CSVCErr2up,               CSVCErr2down,               "CSVcErr2",                 "CErr2"               );
}

bool Systematics::isInit() {
  return typeStringMap_.size()>1;
}

void Systematics::add(Systematics::Type typeUp, Systematics::Type typeDn, const std::string& name, const std::string& label) {
  typeStringMap_[typeUp] = boost::to_upper_copy(name)+"UP";
  typeStringMap_[typeDn] = boost::to_upper_copy(name)+"DOWN";
  // std::cout << "adding syst '" << std::toupper(name)+"UP" << "'\n";
  stringTypeMap_[boost::to_upper_copy(name)+"UP"] = typeUp;
  stringTypeMap_[boost::to_upper_copy(name)+"DOWN"] = typeDn;
  typeLabelMap_[typeUp] = label;
  typeLabelMap_[typeDn] = label;
}

// added method to get a vector of all systematics
std::vector<Systematics::Type> Systematics::getTypeVector() {
  if( !isInit() ) init();
  std::vector<Systematics::Type> outvector;
  outvector.push_back(NA);
  for(auto it : typeStringMap_ ){
    std::cout<<it.first<<" "<<it.second<<std::endl;
    outvector.push_back(it.first);
    }
  return outvector;
}

Systematics::Type Systematics::get(const std::string& name) {
  if( name == "" ) return NA;

  if( !isInit() ) init();
  
  std::map<std::string,Systematics::Type>::const_iterator it = stringTypeMap_.find(name);
  if( it == stringTypeMap_.end() ) {
    std::cout << "ERROR: No uncertainty with name " << name << " will use nominal "<<std::endl;
    return Systematics::NA;
  } else {
    return it->second;
  }
}

std::string Systematics::toString(const Type type) {
  if( type == NA ) return "";

  if( !isInit() ) init();

  std::map<Systematics::Type,std::string>::const_iterator it = typeStringMap_.find(type);
  if( it == typeStringMap_.end() ) {
    std::cout << "ERROR: No uncertainty with name " << type << " will use nominal "<<std::endl;
    return "";
  } else {
    return it->second;
  }
}

bool Systematics::isJECUncertaintyUp(const Type type) {
  const std::string str = toString(type);
  return str.find("JES")==0 && str.find("up")==str.size()-2;
}

bool Systematics::isJECUncertaintyDown(const Type type) {
  const std::string str = toString(type);
  return str.find("JES")==0 && str.find("down") == str.size()-4;
}

bool Systematics::isJECUncertainty(const Type type) {
  return isJECUncertaintyUp(type) || isJECUncertaintyDown(type);
}

std::string Systematics::GetJECUncertaintyLabel(const Type type) {
  if( !isInit() ) init();
  std::map<Systematics::Type,std::string>::const_iterator it = typeLabelMap_.find(type);
  if( it == typeLabelMap_.end() ) {
    return "";
  } else {
    return it->second;
  }
}
