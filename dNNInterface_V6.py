
class theInterface:
  
  def __init__(self):
    self.includeString="-I/nfs/dust/cms/user/kelmorab/CMSSW_Moriond2017/cardsCMSSWv2/CMSSW_8_0_26_patch2/src/"
    #self.libraryString="-L/nfs/dust/cms/user/kelmorab/CMSSW_Moriond2017/cardsCMSSWTF/CMSSW_8_0_26_patch2/lib/slc6_amd64_gcc530 -lDNNBase -lDNNTensorflow -lTTHCommonClassifier"
    self.libraryString="-L/nfs/dust/cms/user/kelmorab/CMSSW_Moriond2017/cardsCMSSWv2/CMSSW_8_0_26_patch2/lib/slc6_amd64_gcc530 -lTTHCommonClassifier"
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
  
  def getAdditionalFunctionDefinitionLines(self):
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
  
  
  def getBeforeLoopLines(self):
    rstr="""
  DNNClassifierBase::pyInitialize();
  DNNClassifier_SL dnn("v6a");
"""
    return rstr

  def getVariableInitInsideEventLoopLines(self):
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
  std::vector<double> dnnInAdditionalFeatures;

  // DANGERZONE
  // It looks like the MET is not actually used in v6a of SL DNNs
  dnnInMET= makeVectorM(Evt_Pt_MET,0.0,Evt_Phi_MET,0.0);
  dnnInLepton = makeVectorE(primlepPt,primlepEta,primlepPhi,primlepE);
  int firstNJets=min(N_Jets,6);
  for(int ijet=0; ijet<firstNJets; ijet++){
    dnnInCSVs.push_back(jetCSVs[ijet]);
    dnnInJets.push_back(makeVectorE(jetPts[ijet],jetEtas[ijet],jetPhis[ijet],jetEnergies[ijet]));
    }
  double dnnInMem=fmod(max(0.0,memDBp),1.0);
  dnnInAdditionalFeatures.push_back(Evt_blr_ETH);
  dnnInAdditionalFeatures.push_back(Evt_blr_ETH_transformed);
  dnnInAdditionalFeatures.push_back(dnnInMem);
  
  DNNOutput aachenoutput;
  if(((N_Jets==4 or N_Jets==5) and N_BTagsM>=3) or (N_Jets>=6 and N_BTagsM>=2)){
  aachenoutput=dnn.evaluate(dnnInJets,dnnInCSVs,dnnInLepton,dnnInMET,dnnInAdditionalFeatures);
  
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
  }
  
"""

    return rstr

  def getTestCallLines(self):
    rstr="""
  std::vector<TLorentzVector> testdnnjets = {
        makeVectorE(561.853400685, -1.687604070, 1.248519063, 48.315901270),
        makeVectorE(317.050318074, -0.592420697, -1.641329408, 41.454653026),
        makeVectorE(130.993330071, -0.257405132, -2.218888283, 15.829634094),
        makeVectorE(90.088794331, -0.758062780, -1.199205875, 11.687776745),
        makeVectorE(57.793076163, 0.163249642, 2.988173246, 9.959981641),
        makeVectorE(45.080527604, -1.838460445, 1.761856556, 7.07615728)
    };
    std::vector<double> testdnnjetCSVs = {
        0.592329562, 0.156740859, 0.998748481, 0.944896400, 0.268956393, 0.109731160
    };

    TLorentzVector testdnnlepton = makeVectorM(45.567291260, -1.122234225, 2.685425282, 0.105700001);
    TLorentzVector testdnnmet = makeVectorM(70.089050293, 0.0, -2.230507374, 0.0); 
    std::vector<double> testdnnAddFeatures;
    testdnnAddFeatures.push_back(1.); // blr
    testdnnAddFeatures.push_back(1.); // blr_transformed
    testdnnAddFeatures.push_back(1.); // MEM
    
    // evaluate
    DNNOutput aachentestdnnoutput = dnn.evaluate(testdnnjets, testdnnjetCSVs, testdnnlepton, testdnnmet, testdnnAddFeatures);
    std::vector<double> targetOutputsfordnntest = { 0.51680371, 0.25959021, 0.07142095, 0.07112622, 0.05624627, 0.02481263, 0.0};
    std::cout<<"doing DNN unit test"<<std::endl;
    std::cout<<"No error printout means it worked"<<std::endl;
    for (size_t i = 0; i < targetOutputsfordnntest.size(); ++i)
    {
        //assert(fabs(targetOutputsfordnntest[i] - aachentestdnnoutput.values[i]) < 0.000001 && "The DNN output for 6 jet events is incorrect");
    }
"""
    return rstr
  
  def getCleanUpLines(self):
    rstr="""
     DNNClassifierBase::pyFinalize();
   """
    return rstr
  
  
  