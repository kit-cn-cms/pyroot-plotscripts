
class theInterface:
  
  def __init__(self):
    self.includeString="-I/nfs/dust/cms/user/kelmorab/CMSSW_Moriond2017/cardsCMSSWTF/CMSSW_8_0_26_patch2/src/"
    self.libraryString="-L/nfs/dust/cms/user/kelmorab/CMSSW_Moriond2017/cardsCMSSWTF/CMSSW_8_0_26_patch2/lib/slc6_amd64_gcc530 -lDNNBase -lDNNTensorflow -lTTHCommonClassifier"
    self.usesPythonLibraries=True

  def getExternalyCallableVariables(self):
    return ["aachen_Out_other",
	    "aachen_Out_ttbar2B",
	    "aachen_Out_ttbarB",
	    "aachen_Out_ttbarBB",
	    "aachen_Out_ttbarCC",
	    "aachen_Out_ttbarOther",
	    "aachen_Out_ttH",
	    "aachen_pred_class",]
    
  def getIncludeLines(self):
    retstr="""
#include "TVector.h" 
#include <iterator>
#include "Python.h"
#include "TMatrixDSym.h"
#include "TMatrixDSymEigen.h"
#include "TVectorD.h"
#include "TTH/CommonClassifier/interface/DNNClassifier.h"
"""
    return retstr
  
  def getAdditionalFunctionLines(self):
    retstr="""

const TLorentzVector makeVectorE(double pt, double eta, double phi, double energy)
{
    TLorentzVector lv;
    lv.SetPtEtaPhiE(pt, eta, phi, energy);
    return lv;
}

const TLorentzVector makeVectorM(double pt, double eta, double phi, double mass)
{
    TLorentzVector lv;
    lv.SetPtEtaPhiM(pt, eta, phi, mass);
    return lv;
}


"""
    return retstr
  
  
  def getConstructorLines(self):
    rstr="""
  DNNClassifierBase::pyInitialize();
  DNNClassifier_SL dnn("v4");
"""
    return rstr

  def getVariableInitLines(self):
    rstr="""
    // variables for Aachen DNNs
 double aachen_Out_ttH=-2.0;
 double aachen_Out_ttbarOther=-2.0;
 double aachen_Out_ttbarCC=-2.0;
 double aachen_Out_ttbarBB=-2.0;
 double aachen_Out_ttbarB=-2.0;
 double aachen_Out_ttbar2B=-2.0;
 double aachen_Out_other=-2.0;
 
 
 int aachen_pred_class=-2;
 """
    return rstr
  
  
  def getEventLoopCodeLines(self):
    rstr="""

  // first construct the needed lorentzvectors
  std::vector<TLorentzVector> dnnInJets;
  std::vector<double> dnnInCSVs;
  TLorentzVector dnnInMET;
  TLorentzVector dnnInLepton;

  // DANGERZONE
  // It looks like the MET is not actually used in v4 of SL DNNs
  dnnInMET= makeVectorE(0.0,0.0,0.0,0.0);
  dnnInLepton = makeVectorE(primlepPt,primlepEta,primlepPhi,primlepE);
  int firstNJets=min(N_Jets,6);
  for(int ijet=0; ijet<firstNJets; ijet++){
    dnnInCSVs.push_back(jetCSVs[ijet]);
    dnnInJets.push_back(makeVectorE(jetPts[ijet],jetEtas[ijet],jetPhis[ijet],jetEnergies[ijet]));
    }
  
  DNNOutput aachenoutput;
  aachenoutput=dnn.evaluate(dnnInJets,dnnInCSVs,dnnInLepton,dnnInMET);
  
  aachen_Out_ttH=aachenoutput.ttH();
  aachen_Out_ttbarOther=aachenoutput.ttlf();
  aachen_Out_ttbarBB=aachenoutput.ttbb();
  aachen_Out_ttbarB=aachenoutput.ttb();
  aachen_Out_ttbar2B=aachenoutput.tt2b();
  aachen_Out_ttbarCC=aachenoutput.ttcc();
  aachen_Out_other=aachenoutput.other();
  
  aachen_pred_class=aachenoutput.mostProbableClass();
  // classes are 
  // 0 = ttH 
  // 1 = ttbb 
  // 2 = ttb 
  // 3 = tt2b 
  // 4 = ttcc 
  // 5 = ttlf
  // 6 = other
  
  bool printstuff=0;
  if(printstuff){
    cout<<"-----DNN-----"<<std::endl;
    cout<<"ttH node "<<aachen_Out_ttH<<std::endl;
    cout<<"ttbarOther node "<<aachen_Out_ttbarOther<<std::endl;
    cout<<"ttbarCC node "<<aachen_Out_ttbarCC<<std::endl;
    cout<<"ttbarBB node "<<aachen_Out_ttbarBB<<std::endl;
    cout<<"ttbarB node "<<aachen_Out_ttbarB<<std::endl;
    cout<<"ttbar2B node "<<aachen_Out_ttbar2B<<std::endl;
    cout<<"other node "<<aachen_Out_other<<std::endl;
    cout<<"predicted class "<<aachen_pred_class<<std::endl;
    }
  
"""

    return rstr

  def getTestCallLines(self):
    rstr="""
  std::vector<TLorentzVector> testdnnjets = {
        makeVectorM(104.253659103, -0.73279517889, -3.07644724846, 15.8214708715),
        makeVectorM(93.7207496495, -1.09075820446, -0.518474698067, 11.1629637015),
        makeVectorM(82.3087599786, -0.29058226943, 0.934316039085, 12.3491756063),
        makeVectorM(71.0101406197, -0.311807841063, -0.00518677430227, 17.680727362),
        makeVectorM(48.2224599416, -0.770735502243, 0.56352609396, 7.37671529065),
        makeVectorM(46.0958273368, -0.883650183678, 1.04447424412, 5.60050991848)
    };
    std::vector<double> testdnnjetCSVs = {
        0.597419083118, 0.759489059448, 0.635843455791, 0.603073060513, 0.999078631401, 0.988624215126
    };

    TLorentzVector testdnnlepton = makeVectorM(54.6405308843, -1.68255746365, -2.53192830086, 0.0313574418471);
    TLorentzVector testdnnmet = makeVectorM(0.0, 0.0, 0.0, 0.0); // dummy

    // evaluate
    DNNOutput aachentestdnnoutput = dnn.evaluate(testdnnjets, testdnnjetCSVs, testdnnlepton, testdnnmet);
    std::vector<double> targetOutputsfordnntest = { 0.51680371, 0.25959021, 0.07142095, 0.07112622, 0.05624627, 0.02481263, 0.0};
    std::cout<<"doing DNN unit test"<<std::endl;
    std::cout<<"No error printout means it worked"<<std::endl;
    for (size_t i = 0; i < targetOutputsfordnntest.size(); ++i)
    {
        assert(fabs(targetOutputsfordnntest[i] - aachentestdnnoutput.values[i]) < 0.000001 && "The DNN output for 6 jet events is incorrect");
    }
"""
    return rstr
  
  def getCleanUpLines(self):
    rstr="""
     DNNClassifierBase::pyFinalize();
   """
    return rstr
  
  
  