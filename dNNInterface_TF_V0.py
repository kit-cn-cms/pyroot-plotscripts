# this class describes the interface to the CommonClassifier to be used in the scriptgenerator
# There are several methods which you will need to update for your own classifier 
# Then use the interface by passing THIS file path to the plotparallel function


class theInterface:
  
  def __init__(self):
    # path to include in the search for header files. This is probably the src CMSSW directory where you installed the CommonClassifier
    self.includeString="-I/nfs/dust/cms/user/kelmorab/CMSSW_Moriond2017/cardsCMSSWTF/CMSSW_8_0_26_patch2/src/"
    # precompiled library path and libraries to be included
    self.libraryString="-L/nfs/dust/cms/user/kelmorab/CMSSW_Moriond2017/cardsCMSSWTF/CMSSW_8_0_26_patch2/lib/slc6_amd64_gcc530 -lDNNBase -lDNNTensorflow -lTTHCommonClassifier"
    # if the following is true, the g++ compiler will also link the python libraries. You probably need this if you use Tensorflow
    self.usesPythonLibraries=True

  # This is a list of variables which should be visible for the plotscript.
  # You also need to define them in the getVariableInitLines method
  def getExternalyCallableVariables(self):
    return ["aachen_Out_other",
	    "aachen_Out_ttbar2B",
	    "aachen_Out_ttbarB",
	    "aachen_Out_ttbarBB",
	    "aachen_Out_ttbarCC",
	    "aachen_Out_ttbarOther",
	    "aachen_Out_ttH",
	    "aachen_pred_class",]
    
  # Write here the code with the include statements
  # DNN header is relative to CMSSW BASE
  def getIncludeLines(self):
    retstr="""
#include "TVector.h" 
#include <iterator>
#include "Python.h"
#include "TMatrixDSym.h"
#include "TMatrixDSymEigen.h"
#include "TVectorD.h"
#include "TTH/CommonClassifier/interface/DNNTFClassifier_SL.h"
"""
    return retstr
  
  # Here you define any additional functions you will need
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
  
  # here you write the code which shgould be inserted before the main event loop
  def getBeforeLoopLines(self):
    rstr="""
  DNNTFClassifier_SL dnn("v0");
"""
    return rstr

  # initialize variables INSIDE event loop
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
  
  # Code that call the Classifier and fills the needed variables
  # This is also inside of the event loop
  def getEventLoopCodeLines(self):
    rstr="""

  // first construct the needed lorentzvectors
  std::vector<TLorentzVector> dnnInJets;
  std::vector<double> dnnInCSVs;
  TLorentzVector dnnInMET;
  TLorentzVector dnnInLepton;

  // DANGERZONE
  // WRONG It looks like the MET is not actually used in v4 of SL DNNs
  // Need to put in MET !!
  dnnInMET= makeVectorE(0.0,0.0,0.0,0.0);
  dnnInLepton = makeVectorE(primlepPt,primlepEta,primlepPhi,primlepE);
  int firstNJets=min(N_Jets,6);
  for(int ijet=0; ijet<firstNJets; ijet++){
    dnnInCSVs.push_back(jetCSVs[ijet]);
    dnnInJets.push_back(makeVectorE(jetPts[ijet],jetEtas[ijet],jetPhis[ijet],jetEnergies[ijet]));
    }
  
  DNNTFOutput aachenoutput;
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

  # Here is code calling a test function to see wether the calling works as it should
  def getTestCallLines(self):
    rstr="""
  std::vector<TLorentzVector> testdnnjets = {
        makeVectorM(82.193317445, -1.381465673, 0.875596046, 12.354169733),
        makeVectorM(61.222326911, -0.624968886, 1.280390978, 7.378321245),
        makeVectorM(49.268722080, -1.523553133, 2.887234688, 10.714914255),
        makeVectorM(45.137310817, -0.522410452, 2.953480721, 4.287899215)
    };
    std::vector<double> testdnnjetCSVs = {
         0.951796949, 0.167348146, 0.164827660, 0.804015398
    };

    TLorentzVector testdnnlepton = makeVectorM(126.932662964, 0.030971697, -0.758532584, 0.105700001);
    TLorentzVector testdnnmet = makeVectorM(49.720878601, 0., -2.168250561, 0.); // dummy

    // evaluate
    DNNTFOutput aachentestdnnoutput = dnn.evaluate(testdnnjets, testdnnjetCSVs, testdnnlepton, testdnnmet);
    std::vector<double> targetOutputsfordnntest = { 46., 46., 46., 46., 46., 46., 46.};
    std::cout<<"doing DNN unit test"<<std::endl;
    std::cout<<"No error printout means it worked"<<std::endl;
    for (size_t i = 0; i < targetOutputsfordnntest.size(); ++i)
    {
        assert(fabs(targetOutputsfordnntest[i] - aachentestdnnoutput.values[i]) < 0.000001 && "The DNN output for 6 jet events is incorrect");
    }
"""
    return rstr
  
  # call need desctructors here and other cleanup things
  # Will be run after event loop
  def getCleanUpLines(self):
    rstr="""
   """
    return rstr
  
  
  