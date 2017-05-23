import sys
import os
import subprocess
import time
import datetime
import stat
import re
import ROOT
import xml.etree.ElementTree as ET
import variablebox
import plotutils
import glob
import json
import filecmp

ROOT.gROOT.SetBatch(True)

def getHead(dataBases,doAachenDNN):
  
  retstr="""
#include "TChain.h"
#include "TBranch.h"
#include "TLorentzVector.h"
#include "TFile.h"
#include "TH1F.h"
#include "TH2F.h"
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include "TMVA/Reader.h"
#include <algorithm>
#include <map>
#include "TStopwatch.h"
"""
  if doAachenDNN:
    retstr+="""
#include "TVector.h" 
#include <iterator>
#include "Python.h"
#include "TMatrixDSym.h"
#include "TMatrixDSymEigen.h"
#include "TVectorD.h"
"""

  if dataBases!=[]:
    retstr+="""
#include "/nfs/dust/cms/user/kelmorab/DataBaseCodeForScriptGenerator/MEMDataBase/MEMDataBase/interface/MEMDataBase.h"
"""

  retstr+="""

using namespace std;
"""

  if doAachenDNN:
    retstr+="""
// hacked DNN Classifier of RWTH from commit 
// https://gitlab.cern.ch/ttH/CommonClassifier/commit/91f1d2f81291ce6ee3a168e3778c0b9c806e7f2b

//first the common BDTVariable class

typedef std::map<std::string, std::string> mparams;
typedef std::vector< TLorentzVector > vecTLorentzVector;
typedef std::vector<std::vector<double> > vvdouble;
typedef std::vector<std::vector<std::string> > vvstring;
typedef std::vector<std::vector<int> > vvint;
typedef std::vector<std::string> vstring;
typedef std::vector<double> vdouble;
typedef std::vector<int> vint;

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

class CommonBDTvars{

	// === Functions === //
	public: 
		// Constructor(s) and destructor
		CommonBDTvars();
		virtual ~CommonBDTvars();
		


	//Algorithms 
   
		void getSp(TLorentzVector lepton, TLorentzVector met, vecTLorentzVector jets, double &aplanarity, double &sphericity);
		void getFox(vecTLorentzVector jets, double &h0, double &h1, double &h2, double &h3, double &h4);
		double getBestHiggsMass(TLorentzVector lepton, TLorentzVector met, vecTLorentzVector jets, vdouble btag, double &minChi, double &dRbb, TLorentzVector &bjet1, TLorentzVector &bjet2, vecTLorentzVector loose_jets, vdouble loose_btag);
   
    
	
	
		void convert_jets_to_TLVs(vvdouble jets, vecTLorentzVector &vect_of_jet_TLVs);
		void vect_of_tagged_TLVs(vvdouble jets, vdouble jetCSV, vecTLorentzVector &vect_of_btag_TLVs);
		double get_jet_jet_etamax (vvdouble jets);
		double get_jet_tag_etamax (vvdouble jets, vdouble jetCSV);
		double get_tag_tag_etamax (vvdouble jets, vdouble jetCSV);
		
		
		
		
		double study_tops_bb_syst (double MET, double METphi, TLorentzVector &metv, TLorentzVector lepton, vvdouble jets, vdouble csv, double &minChi, double &chi2lepW, double &chi2leptop, double &chi2hadW, double &chi2hadtop, double &mass_lepW, double &mass_leptop, double &mass_hadW, double &mass_hadtop, double &dRbb, double &testquant1, double &testquant2, double &testquant3, double &testquant4, double &testquant5, double &testquant6, double &testquant7, TLorentzVector &b1, TLorentzVector &b2);
		double getBestHiggsMass2(TLorentzVector lepton, TLorentzVector &met, vecTLorentzVector jets, vdouble btag, double &minChi, double &dRbb, TLorentzVector &bjet1, TLorentzVector &bjet2, double &chi2lepW, double &chi2leptop, double &chi2hadW, double &chi2hadtop, double &mass_lepW, double &mass_leptop, double &mass_hadW, double &mass_hadtop, TLorentzVector &toplep, TLorentzVector &tophad);
		double get_median_bb_mass(vvdouble jets, vdouble jetCSV);
		double pt_E_ratio_jets(vvdouble jets);
		
		double JetDelta_EtaAvgEta(vvdouble jet_vect_TLV, vdouble jet_CSV, std::string JetorTag, std::string JetorTag_Avg );

	
	private:

		// Parameter management
	private:
  
		// Old functions
	public:

	protected:
	
	double CSVLwp, CSVMwp, CSVTwp;

	private:


	// === Variables === //
	public:

	protected:

	private:

}; // End of class prototype

CommonBDTvars::CommonBDTvars(){


  // twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideBTagging#Preliminary_working_or_operating
  // Preliminary working (or operating) points for CSVv2+IVF
  CSVLwp = 0.5426; // 10.1716% DUSG mistag efficiency
  CSVMwp = 0.8484; // 1.0623% DUSG mistag efficiency
  CSVTwp = 0.9535; // 0.1144% DUSG mistag efficiency


}


CommonBDTvars::~CommonBDTvars(){

}


/*

Get These Variables

double	sphericity;
double	aplanarity;
*/


void CommonBDTvars::getSp(TLorentzVector lepton, TLorentzVector met, vecTLorentzVector jets, double &aplanarity, double &sphericity) {
	//
	// Aplanarity and sphericity
	//

	int nJets = int(jets.size());

	double mxx = lepton.Px()*lepton.Px() + met.Px()*met.Px();
	double myy = lepton.Py()*lepton.Py() + met.Py()*met.Py();
	double mzz = lepton.Pz()*lepton.Pz() + met.Pz()*met.Pz();
	double mxy = lepton.Px()*lepton.Py() + met.Px()*met.Py();
	double mxz = lepton.Px()*lepton.Pz() + met.Px()*met.Pz();
	double myz = lepton.Py()*lepton.Pz() + met.Py()*met.Pz();

	for (int i=0; i<nJets; i++) {
		mxx += jets[i].Px()*jets[i].Px();
		myy += jets[i].Py()*jets[i].Py();
		mzz += jets[i].Pz()*jets[i].Pz();
		mxy += jets[i].Px()*jets[i].Py();
		mxz += jets[i].Px()*jets[i].Pz();
		myz += jets[i].Py()*jets[i].Pz();		
	}
	double sum = mxx + myy + mzz;
	mxx /= sum;
	myy /= sum;
	mzz /= sum;
	mxy /= sum;
	mxz /= sum;
	myz /= sum;

	TMatrix tensor(3,3);
	tensor(0,0) = mxx;
	tensor(1,1) = myy;
	tensor(2,2) = mzz;
	tensor(0,1) = mxy;
	tensor(1,0) = mxy;
	tensor(0,2) = mxz;
	tensor(2,0) = mxz;
	tensor(1,2) = myz;
	tensor(2,1) = myz;
	TVector eigenval(3);
	tensor.EigenVectors(eigenval);

	sphericity = 3.0*(eigenval(1)+eigenval(2))/2.0;
	aplanarity = 3.0*eigenval(2)/2.0;

	return;
}

/*

Get These Variables

double	h0;
double	h1;
double	h2;
double	h3;
*/

void CommonBDTvars::getFox(vecTLorentzVector jets, double &h0, double &h1, double &h2, double &h3, double &h4) {
	

	int visObjects = int(jets.size());

	double eVis = 0.0;
	for (int i=0; i<visObjects; i++) {
		eVis += jets[i].E();
	}

	h0 = 0.0;
	h1 = 0.0;
	h2 = 0.0;
	h3 = 0.0;
	h4 = 0.0;
	for (int i=0; i<visObjects-1; i++) {
		for (int j=i+1; j<visObjects; j++) {
			double costh = cos(jets[i].Angle(jets[j].Vect()));
			double p0 = 1.0;
			double p1 = costh;
			double p2 = 0.5*(3.0*costh*costh - 1.0);
			double p3 = 0.5*(5.0*costh*costh*costh - 3.0*costh);
			double p4 = 0.125*(35.0*costh*costh*costh*costh - 30.0*costh*costh + 3.0);
			double pipj = jets[i].P()*jets[j].P();
			h0 += (pipj/(eVis*eVis))*p0;
			h1 += (pipj/(eVis*eVis))*p1;
			h2 += (pipj/(eVis*eVis))*p2;
			h3 += (pipj/(eVis*eVis))*p3;
			h4 += (pipj/(eVis*eVis))*p4;
		}
	}

	return;
}



/*

Get These Variables

double	best_higgs_mass;	
double	dRbb;
*/

double CommonBDTvars::getBestHiggsMass(TLorentzVector lepton, TLorentzVector met, vecTLorentzVector jets, vdouble btag, double &minChi, double &dRbb, TLorentzVector &bjet1, TLorentzVector &bjet2, vecTLorentzVector loose_jets, vdouble loose_btag)
{

  if( jets.size()<6 && loose_jets.size()>0 ){
    jets.push_back( loose_jets[0] );
    btag.push_back( loose_btag[0] );
  }

  int nJets = int(jets.size());

  double chi_top_lep=10000;
  double chi_top_had=10000;
  //double chi_W_lep=10000; //isn't really used
  double chi_W_had=10000;

  minChi = 1000000;
  dRbb = 1000000;
  const double btagCut = CSVMwp;
  double W_mass = 80.0;
  double top_mass = 172.5;
  //double H_mass=120.0;

  // updated 8/22/2012 from J. Timcheck
  //sigma's from >=6j >=4t, muon, no imaginary neutrino pz ttH
  double sigma_hadW   = 12.77;
  double sigma_hadTop = 18.9;
  double sigma_lepTop = 32.91;

  // //sigma's from >=6j >=4t, muon, no imaginary neutrino pz ttH
  // double sigma_hadW   = 12.59;
  // double sigma_hadTop = 19.9;
  // double sigma_lepTop = 39.05;

  //sigma's from >=6j >=4t, muon, no imaginary neutrino pz ttJets
  /*double sigma_hadW		= 12.72,
    sigma_hadTop	= 18.12,
    sigma_lepTop	= 38.72;
  */

  double metPz[2];
  double chi=999999;

  //stuff to find:
  double higgs_mass_high_energy=0;

  int nBtags = 0;
  for(int i=0;i<nJets;i++){
    if(btag[i]>btagCut) nBtags++;
  }

  int nUntags = nJets-nBtags;

  double lowest_btag = 99.;
  double second_lowest_btag = 999.;
  int ind_lowest_btag = 999;
  int ind_second_lowest_btag = 999;

  if( nJets>=6 && nBtags>=4 ){
    if( nUntags<2 ){
      for(int i=0;i<nJets;i++){
	if( btag[i]<lowest_btag ){
	  second_lowest_btag = lowest_btag;
	  ind_second_lowest_btag = ind_lowest_btag;

	  lowest_btag = btag[i];
	  ind_lowest_btag = i;
	}
	else if( btag[i]<second_lowest_btag ){
	  second_lowest_btag = btag[i];
	  ind_second_lowest_btag = i;
	}
      }
    }
  }


  //Handle 6j3t.
  int ind_promoted_btag = 999;

  if( nJets>=6 && nBtags==3 ){
    for(int i=0;i<nJets;i++){
      int rank = 0;
      for(int j=0;j<nJets;j++){
	if( btag[j] > btag[i] ){
	  rank++;
	}
      }
      if( rank == 3 ) ind_promoted_btag = i;
    }
  }

  // First get the neutrino z
  double energyLep = lepton.E();
  double a = (W_mass*W_mass/(2.0*energyLep)) + (lepton.Px()*met.Px() + lepton.Py()*met.Py())/energyLep;
  double radical = (2.0*lepton.Pz()*a/energyLep)*(2.0*lepton.Pz()*a/energyLep);
  radical = radical - 4.0*(1.0 - (lepton.Pz()/energyLep)*(lepton.Pz()/energyLep))*(met.Px()*met.Px() + met.Py()*met.Py()- a*a);
  if (radical < 0.0) radical = 0.0;
  metPz[0] = (lepton.Pz()*a/energyLep) + 0.5*sqrt(radical);
  metPz[0] = metPz[0] / (1.0 - (lepton.Pz()/energyLep)*(lepton.Pz()/energyLep));
  metPz[1] = (lepton.Pz()*a/energyLep) - 0.5*sqrt(radical);
  metPz[1] = metPz[1] / (1.0 - (lepton.Pz()/energyLep)*(lepton.Pz()/energyLep));


  // Loop over all jets, both Pz, calcaulte chi-square
  TLorentzVector metNew;
  for( int ipznu=0; ipznu<2; ipznu++ ){
    metNew.SetXYZM(met.Px(),met.Py(),metPz[ipznu],0.0); //neutrino has mass 0
    //with b-tag info
    if( (nJets>=6 && nBtags>=4) || (nJets>=6 && nBtags==3) ){
      vecTLorentzVector not_b_tagged,b_tagged;
      //fill not_b_tagged and b_tagged
      for( int i=0;i<nJets;i++ ){
	if( (btag[i]>btagCut && i!=ind_second_lowest_btag && i!=ind_lowest_btag) || (i==ind_promoted_btag) ) b_tagged.push_back(jets[i]);
	else not_b_tagged.push_back(jets[i]);
      }
      //first make possible t_lep's with b-tagged jets (includes making W_lep)
      for( int i=0; i<int(b_tagged.size()); i++ ){
	TLorentzVector W_lep=metNew+lepton; //used for histogram drawing only
	TLorentzVector top_lep=metNew+lepton+b_tagged.at(i);
	chi_top_lep=pow((top_lep.M()-top_mass)/sigma_lepTop,2);
	//next make possible W_had's with not b-tagged jets
	for( int j=0; j<int(not_b_tagged.size()); j++ ){
	  for( int k=0; k<int(not_b_tagged.size()); k++ ){
	    if( j!=k ){
	      TLorentzVector W_had=not_b_tagged.at(j)+not_b_tagged.at(k);
	      chi_W_had=pow((W_had.M()-W_mass)/sigma_hadW,2);
	      //now make possible top_had's (using the W_had + some b-tagged jet)
	      for( int l=0; l<int(b_tagged.size()); l++ ){
		if( l!=i ){
		  TLorentzVector top_had=W_had+b_tagged.at(l);
		  chi_top_had=pow((top_had.M()-top_mass)/sigma_hadTop,2);
		  chi=chi_top_lep+chi_W_had+chi_top_had;
		  //accept the lowest chi
		  if( chi<minChi ){
		    minChi=chi;
		    //pick the other two b's that have the highest et (energy in transverse plane) as higgs mass constituents
		    TLorentzVector H2;
		    int numH2Constituents=0;
		    TLorentzVector bBest[2];
		    for( int m=0; m<int(b_tagged.size()); m++ ){
		      if( m!=i && m!=l && numH2Constituents<2 ){
			bBest[numH2Constituents] = b_tagged.at(m);
			numH2Constituents++;
			H2+=b_tagged.at(m);
		      }
		    }
		    dRbb = bBest[0].DeltaR( bBest[1] );
		    higgs_mass_high_energy=H2.M();
		    bjet1 = bBest[0];
		    bjet2 = bBest[1];
		  }
		}
	      }
	    }
	  }
	}
      }
    }
  }
  return higgs_mass_high_energy;
}




// Some of this may seem redundant ( why not just feed TLVs into these functions instead of turning TLVs into vvdoubles and then converting vvdoubles to TLVs)
// This is because we dont save the jets as TLVs when we loop over them in TreeMaker. 
// They are saved as vvjets and most of these functions were used in treeReader where it was reading in vvjets from TreeMaker Trees




void CommonBDTvars::convert_jets_to_TLVs(vvdouble jets, vecTLorentzVector &vect_of_jet_TLVs)
{
	TLorentzVector jet;	
	int nJets = jets.size();
	
	for(int i=0;i<nJets;i++)
	{
		jet.SetPxPyPzE(jets[i][0],jets[i][1],jets[i][2],jets[i][3]);
		vect_of_jet_TLVs.push_back(jet);
	}
}

void CommonBDTvars::vect_of_tagged_TLVs(vvdouble jets, vdouble jetCSV, vecTLorentzVector &vect_of_btag_TLVs)
{
	TLorentzVector tagged_jet;
	
	int nJets = jets.size();
	double btagCut = CSVMwp;
	
	for(int i=0;i<nJets;i++)
	{
		if (jetCSV[i]>btagCut)
		{
		
			tagged_jet.SetPxPyPzE(jets[i][0],jets[i][1],jets[i][2],jets[i][3]);
			vect_of_btag_TLVs.push_back(tagged_jet);
		}
	}
}




double CommonBDTvars::get_jet_jet_etamax (vvdouble jets)
{
	vecTLorentzVector thejets;
	convert_jets_to_TLVs(jets, thejets);
	
	int count=0;
	double avgval=0.;
	
	for (int i=0; i<int(thejets.size()); i++){
	
				avgval += abs(thejets[i].Eta());
				count++;
	}
	
	avgval /= count;
	
	double deta = 0.;
	double etamax=-1.;
	
	for (int k=0; k<int(thejets.size()); k++)
	{
		deta = abs(abs(thejets[k].Eta())-avgval);
		
		if(deta>etamax)etamax = deta;
		
	}

	return etamax;
}


double CommonBDTvars::get_jet_tag_etamax (vvdouble jets, vdouble jetCSV)
{


	vecTLorentzVector thejets;
	convert_jets_to_TLVs(jets, thejets);
	
	int count=0;
	double avgval=0.;
	
	for (int i=0; i<int(thejets.size()); i++)
	{
				
				avgval += abs(thejets[i].Eta());
				count++;
				
	}
	
	avgval /= count;
	
	double deta = 0.;
	double etamax=0.;
	
	
	vecTLorentzVector thetags;
	vect_of_tagged_TLVs(jets, jetCSV, thetags);
	
	
	for (int k=0; k<int(thetags.size()); k++)
	{
		 deta = abs(abs(thetags[k].Eta())-avgval);
		
		if(deta>etamax)etamax=deta;
		
		
		
	}

	return etamax;
}


double CommonBDTvars::get_tag_tag_etamax (vvdouble jets, vdouble jetCSV)
{

//std::cout<<"tag_tag_etamax: ";

	vecTLorentzVector thetags;
	vect_of_tagged_TLVs(jets, jetCSV, thetags);
		
	int count=0;
	double avgval=0.;
	
	for (int i=0; i<int(thetags.size()); i++)
	{
	  
				
				avgval += abs(thetags[i].Eta());
				count++;
				
				
				//std::cout<<abs(thetags[i].Eta())<<" "<<avgval<<" | ";
		
	}
	
	avgval /= count;
	
	
	//cout<<avgval<<" ||| ";
	
	double deta = 0.;
	double etamax=0.;
	
	
	for (int k=0; k<int(thetags.size()); k++)
	{
		deta = abs(abs(thetags[k].Eta())-avgval);
		
		if(deta>etamax)etamax=deta;
		
		//std::cout<<deta<<" "<<etamax<<" | ";
		
	}
	
	
	//std::cout<<" ||| "<<etamax<<"               "<<count<<endl;

	return etamax;
	
	
}


double CommonBDTvars::study_tops_bb_syst (double MET, double METphi, TLorentzVector &metv, TLorentzVector lepton, vvdouble jets, vdouble csv, double &minChi, double &chi2lepW, double &chi2leptop, double &chi2hadW, double &chi2hadtop, double &mass_lepW, double &mass_leptop, double &mass_hadW, double &mass_hadtop, double &dRbb, double &testquant1, double &testquant2, double &testquant3, double &testquant4, double &testquant5, double &testquant6, double &testquant7, TLorentzVector &b1, TLorentzVector &b2)
{
	// cout<< "in study_tops_bb_syst" << endl;
	
	double pi = 3.14;
	
	metv.SetPtEtaPhiE(MET,0.,METphi,MET);
	
	// cout<< metv.Pt() << endl;
	
	//TLorentzVector lepton;
	
	
	//lepton.SetPxPyPzE(lep[0],lep[1],lep[2],lep[3]);
	
	// cout<< lepton.Pt() << endl;
	
	vecTLorentzVector jet_TLVs;	
	
	
	convert_jets_to_TLVs(jets, jet_TLVs);
	
	
	// cout<< jet_TLVs[0].Pt() << endl;
		
	//double minChi;
	//double dRbb;
	TLorentzVector bjet1;
	TLorentzVector bjet2;
	TLorentzVector leptop;
	TLorentzVector hadtop;
	
	// cout<< "before bhm" << endl;
	
	double bhm = getBestHiggsMass2(lepton, metv, jet_TLVs, csv, minChi, dRbb, bjet1, bjet2, chi2lepW, chi2leptop, chi2hadW, chi2hadtop, mass_lepW, mass_leptop, mass_hadW, mass_hadtop, leptop, hadtop); // Jon T. version 2

	
	b1 = bjet1;
	b2 = bjet2;
	
	TLorentzVector bsyst = bjet1+bjet2;
	TLorentzVector topsyst = leptop+hadtop;
	
	double dphihad = bsyst.DeltaPhi(hadtop);
	double dphilep = bsyst.DeltaPhi(leptop);
	
	
	testquant1 = bsyst.Eta() - leptop.Eta();	
	
	// cout<< testquant1 << endl;
	
	testquant2 = bsyst.Eta() - hadtop.Eta();
	
	// cout<< testquant2 << endl;
	
	testquant3 = fabs((dphilep - pi)*(dphilep + pi)) + pow(dphihad,2);
	testquant3 = sqrt(testquant3 / (2.0*pow(pi,2)));		
	
	// cout<< testquant3 << endl;
	
	testquant4 = bsyst.Eta();
	
	// cout<< testquant4 << endl;
	
	testquant5 = (hadtop.Eta() + leptop.Eta())/2;
	
	// cout<< testquant5 << endl;
		
	testquant6 = sqrt(abs((bsyst.Eta() - leptop.Eta())*(bsyst.Eta() - hadtop.Eta())));
	
	// cout<< testquant6 << endl;
	
	testquant7 = bsyst.Angle(topsyst.Vect());
	
	// cout<< testquant7 << endl;
	
	return bhm;
}


double CommonBDTvars::getBestHiggsMass2(TLorentzVector lepton, TLorentzVector &met, vecTLorentzVector jets, vdouble btag, double &minChi, double &dRbb, TLorentzVector &bjet1, TLorentzVector &bjet2, double &chi2lepW, double &chi2leptop, double &chi2hadW, double &chi2hadtop, double &mass_lepW, double &mass_leptop, double &mass_hadW, double &mass_hadtop, TLorentzVector &toplep, TLorentzVector &tophad)
{

  int nJets = int(jets.size());
  double pfmet_px=met.Px(), pfmet_py=met.Py();
  double chi_top_lep=10000;
  double chi_top_had=10000;
  //double chi_W_lep=10000; //isn't really used
  double chi_W_had=10000;

  minChi = 1000000;
  dRbb = 1000000;
  double btagCut = CSVMwp;
  double W_mass = 80.0;
  double top_mass = 172.5;
  //double H_mass=120.0;

  // updated 8/22/2012 from J. Timcheck
  //sigma's from >=6j >=4t, muon, no imaginary neutrino pz ttH
  double sigma_hadW   = 12.77;
  double sigma_hadTop = 18.9;
  //double sigma_lepTop = 32.91;
  double sigma_lepTop = 18.9;

  // //sigma's from >=6j >=4t, muon, no imaginary neutrino pz ttH
  // double sigma_hadW   = 12.59;
  // double sigma_hadTop = 19.9;
  // double sigma_lepTop = 39.05;

  //sigma's from >=6j >=4t, muon, no imaginary neutrino pz ttJets
  /*double sigma_hadW		= 12.72,
    sigma_hadTop	= 18.12,
    sigma_lepTop	= 38.72;
  */
  
  /// more initializitions
  
  bjet1.SetPxPyPzE(1.,1.,1.,2.);
  bjet2.SetPxPyPzE(1.,1.,1.,2.);
//  chi2lepW = 0.;
//  chi2leptop = 0.;
//  chi2hadtop = 0.;
  mass_lepW = 0.;
  mass_leptop = 0.;
  mass_hadW = 0.;
  mass_hadtop = 0.;
  toplep.SetPxPyPzE(1.,1.,1.,2.);
  tophad.SetPxPyPzE(1.,1.,1.,2.);
  
  
  double metPz[2];
  double chi=999999;

  //stuff to find:
  double higgs_mass_high_energy=0;

  int nBtags = 0;
  for(int i=0;i<nJets;i++){
    if(btag[i]>btagCut) nBtags++;
  }

  int nUntags = nJets-nBtags;

  double lowest_btag = 99.;
  double second_lowest_btag = 999.;
  int ind_lowest_btag = 999;
  int ind_second_lowest_btag = 999;

  vdouble btag_sorted = btag;
  //int ind_fourth_highest = 999;

  if( nJets>=6 && nBtags>=4 ){
    
    if( nUntags<2 ){
      for(int i=0;i<nJets;i++){
	if( btag[i]<lowest_btag ){
	  second_lowest_btag = lowest_btag;
	  ind_second_lowest_btag = ind_lowest_btag;

	  lowest_btag = btag[i];
	  ind_lowest_btag = i;
	}
	else if( btag[i]<second_lowest_btag ){
	  second_lowest_btag = btag[i];
	  ind_second_lowest_btag = i;
	}
      }
    }
    /*
    if( nBtags==3 )
    {
	sort(btag_sorted.begin(),btag_sorted.end());
	double fourth_highest_csv = btag_sorted[nJets-4];
	
	for (int f=0; f<nJets; f++)
	{
		if (btag[f]==fourth_highest_csv) ind_fourth_highest = f;
	}

    }
    */
  }

    //Handle 6j3t.
  int ind_promoted_btag = 999;

  if( nJets>=6 && nBtags==3 ){
    for(int i=0;i<nJets;i++){
      int rank = 0;
      for(int j=0;j<nJets;j++){
	if( btag[j] > btag[i] ){
	  rank++;
	}
      }
      if( rank == 3 ) ind_promoted_btag = i;
    }
  }


  // First get the neutrino z
  double energyLep = lepton.E();
  double a = (W_mass*W_mass/(2.0*energyLep)) + (lepton.Px()*met.Px() + lepton.Py()*met.Py())/energyLep;
  double radical = (2.0*lepton.Pz()*a/energyLep)*(2.0*lepton.Pz()*a/energyLep);
  radical = radical - 4.0*(1.0 - (lepton.Pz()/energyLep)*(lepton.Pz()/energyLep))*(met.Px()*met.Px() + met.Py()*met.Py()- a*a);
  
  bool imaginary = false;

if (radical < 0.0)
{
	imaginary=true;
}
if(imaginary)
{
	radical=-1.0;
	double value=.001;
	while(true)
	{
		met.SetPxPyPzE(pfmet_px,pfmet_py,0.0,sqrt(pow(pfmet_px,2)+pow(pfmet_py,2))); //neutrino mass 0, pt = sqrt(px^2+py^2)
//			energyLep = lepton.E();
		a = (W_mass*W_mass/(2.0*energyLep)) + (lepton.Px()*met.Px() + lepton.Py()*met.Py())/energyLep;
		radical = (2.0*lepton.Pz()*a/energyLep)*(2.0*lepton.Pz()*a/energyLep);
		radical = radical - 4.0*(1.0 - (lepton.Pz()/energyLep)*(lepton.Pz()/energyLep))*(met.Px()*met.Px() + met.Py()*met.Py()- a*a);
		if(radical>=0)
			break;
		pfmet_px-=pfmet_px*value;
		pfmet_py-=pfmet_py*value;
	}
}


  metPz[0] = (lepton.Pz()*a/energyLep) + 0.5*sqrt(radical);
  metPz[0] = metPz[0] / (1.0 - (lepton.Pz()/energyLep)*(lepton.Pz()/energyLep));
  metPz[1] = (lepton.Pz()*a/energyLep) - 0.5*sqrt(radical);
  metPz[1] = metPz[1] / (1.0 - (lepton.Pz()/energyLep)*(lepton.Pz()/energyLep));



  // Loop over all jets, both Pz, calcaulte chi-square
  TLorentzVector metNew;
  for( int ipznu=0; ipznu<2; ipznu++ ){
    metNew.SetXYZM(met.Px(),met.Py(),metPz[ipznu],0.0); //neutrino has mass 0
    //with b-tag info
    if(( nJets>=6 && nBtags>=4 )||( nJets>=6 && nBtags==3 )){
      vecTLorentzVector not_b_tagged,b_tagged;
      //fill not_b_tagged and b_tagged
      for( int i=0;i<nJets;i++ ){
      
        //if (nBtags>=4)
	//{
		if( (btag[i]>btagCut && i!=ind_second_lowest_btag && i!=ind_lowest_btag) || (i==ind_promoted_btag) ) b_tagged.push_back(jets[i]);
		else not_b_tagged.push_back(jets[i]);
	//}
	/*
	if (nBtags==3)
	{
      		if( btag[i]>btagCut || i==ind_fourth_highest) b_tagged.push_back(jets[i]);
		else not_b_tagged.push_back(jets[i]);
      	}
 	*/
      
      }
      //first make possible t_lep's with b-tagged jets (includes making W_lep)
      for( int i=0; i<int(b_tagged.size()); i++ ){
	TLorentzVector W_lep=metNew+lepton; //used for histogram drawing only
	TLorentzVector top_lep=metNew+lepton+b_tagged.at(i);
	chi_top_lep=pow((top_lep.M()-top_mass)/sigma_lepTop,2);
	//next make possible W_had's with not b-tagged jets
	for( int j=0; j<int(not_b_tagged.size()); j++ ){
	  for( int k=0; k<int(not_b_tagged.size()); k++ ){
	    if( j!=k ){
	      TLorentzVector W_had=not_b_tagged.at(j)+not_b_tagged.at(k);
	      chi_W_had=pow((W_had.M()-W_mass)/sigma_hadW,2);
	      //now make possible top_had's (using the W_had + some b-tagged jet)
	      for( int l=0; l<int(b_tagged.size()); l++ ){
		if( l!=i ){
		  TLorentzVector top_had=W_had+b_tagged.at(l);
		  chi_top_had=pow((top_had.M()-top_mass)/sigma_hadTop,2);
		  chi=chi_top_lep+chi_W_had+chi_top_had;
		  //accept the lowest chi
		  if( chi<minChi ){
		    minChi=chi;
		    //pick the other two b's that have the highest et (energy in transverse plane) as higgs mass constituents
		    TLorentzVector H2;
		    int numH2Constituents=0;
		    
		    TLorentzVector bBest[2];
		    
		    for( int m=0; m<int(b_tagged.size()); m++ ){
		      if( m!=i && m!=l && numH2Constituents<2 ){
			bBest[numH2Constituents] = b_tagged.at(m);
			numH2Constituents++;
			H2+=b_tagged.at(m);
		      }
		    }
		    dRbb = bBest[0].DeltaR( bBest[1] );
		    higgs_mass_high_energy=H2.M();
		    bjet1 = bBest[0];
		    bjet2 = bBest[1];
		    
		    mass_lepW = W_mass;
		    mass_leptop = top_lep.M();
		    mass_hadW = W_had.M();
		    mass_hadtop = top_had.M();
		    toplep = top_lep;
		    tophad = top_had;
		  }
		}
	      }
	    }
	  }
	}
      }
    }
  }
  
chi2lepW = 0.;
chi2leptop = chi_top_lep;
chi2hadtop = chi_top_had;
chi2hadW = chi_W_had;



  
  return higgs_mass_high_energy;

}


double CommonBDTvars::get_median_bb_mass(vvdouble jets, vdouble jetCSV)
{
	
	
	
	// all btags
	vecTLorentzVector all_btags;
	TLorentzVector bb;

	vect_of_tagged_TLVs(jets, jetCSV, all_btags);

	int bbcount = 0;
	vector<double> median_vect;
	double median_mass = 0.;
	

	for (int asdf=0; asdf<int(all_btags.size()-1); asdf++)
	{
	  for (int j=asdf+1; j<int(all_btags.size()); j++)
		{	

			bb = all_btags[asdf]+all_btags[j];

			median_vect.push_back(bb.M());

			bbcount++;

		}
	}



	double vectpos = (double)median_vect.size();
	
	if(vectpos!=0){

	 	vectpos = floor(vectpos/2)-1; // all these are even -> gets lower one

	 	sort(median_vect.begin(),median_vect.end());

		median_mass = median_vect[vectpos+1]; // gets upper one
	
	}
	
	
	

	return median_mass;

}



double CommonBDTvars::pt_E_ratio_jets(vvdouble jets)
{
	double ratio = 0.;
	double ptsum = 0.;
	double Esum = 0.;
	
	vecTLorentzVector jetvect;
	convert_jets_to_TLVs(jets,jetvect);
	
	for (int i=0; i<int(jetvect.size()); i++)
	{
		ptsum += jetvect[i].Pt();
		Esum += jetvect[i].E();
	}
	
	ratio = ptsum / Esum;
	
	return ratio;
}


double CommonBDTvars::JetDelta_EtaAvgEta(vvdouble jet_vect_TLV, vdouble jet_CSV, std::string JetorTag, std::string JetorTag_Avg )
{

//if(JetorTag == "Tag" && JetorTag_Avg =="Tag")std::cout<<"JetDelta_TagTag: ";
	double sumJetEta = 0;
	double sumTagEta = 0;
	double cntJetEta = 0;
	double cntTagEta = 0;
	
	
	for( int iJet=0; iJet<int(jet_vect_TLV.size()); iJet++ ){
	  TLorentzVector myJet;
	  myJet.SetPxPyPzE( jet_vect_TLV[iJet][0], jet_vect_TLV[iJet][1], jet_vect_TLV[iJet][2], jet_vect_TLV[iJet][3] );
	  double myCSV = jet_CSV[iJet];
	  sumJetEta += abs(myJet.Eta());
	  cntJetEta += 1.;
	  
	  
	  
	  

	  if( myCSV>CSVMwp ){
	    sumTagEta += abs(myJet.Eta());
	    cntTagEta += 1.;
	   // if(JetorTag == "Tag" && JetorTag_Avg == "Tag")std::cout<<abs(myJet.Eta())<<" "<<sumTagEta<<" | ";
	  }
  	}
	
	double aveJetEta = ( cntJetEta>0 ) ? sumJetEta/cntJetEta : -999;
	double aveTagEta = ( cntTagEta>0 ) ? sumTagEta/cntTagEta : -999;

	double maxDEta_jet_aveJetEta = -1;
	double maxDEta_tag_aveJetEta = -1;
	double maxDEta_tag_aveTagEta = -1;
	double maxDEta_jet_aveTagEta = -1;
	
	//if(JetorTag == "Tag" && JetorTag_Avg == "Tag")std::cout<<aveTagEta<<" || ";

	for( int iJet=0; iJet<int(jet_vect_TLV.size()); iJet++ ){
	  TLorentzVector myJet;
	  myJet.SetPxPyPzE( jet_vect_TLV[iJet][0], jet_vect_TLV[iJet][1], jet_vect_TLV[iJet][2], jet_vect_TLV[iJet][3] );

	  double myCSV = jet_CSV[iJet];
	  double myJetEta = abs(myJet.Eta());

	  maxDEta_jet_aveJetEta = std::max( maxDEta_jet_aveJetEta, fabs(myJetEta - aveJetEta) );
	  maxDEta_jet_aveTagEta = std::max( maxDEta_jet_aveTagEta, fabs(myJetEta - aveTagEta) );
	  if( myCSV>CSVMwp ){
	    maxDEta_tag_aveJetEta = std::max( maxDEta_tag_aveJetEta, fabs(myJetEta - aveJetEta) );
	    maxDEta_tag_aveTagEta = std::max( maxDEta_tag_aveTagEta, fabs(myJetEta - aveTagEta) );
	   // if(JetorTag == "Tag" && JetorTag_Avg == "Tag")std::cout<<fabs(myJetEta - aveTagEta)<<" "<<maxDEta_tag_aveTagEta<<" | ";
	  }
	}
	
	double returnVal = -1;
	
	if(JetorTag == "Jet" && JetorTag_Avg == "Jet")returnVal = maxDEta_jet_aveJetEta;
	if(JetorTag == "Tag" && JetorTag_Avg == "Jet")returnVal = maxDEta_tag_aveJetEta;
	if(JetorTag == "Tag" && JetorTag_Avg == "Tag")returnVal = maxDEta_tag_aveTagEta;
	if(JetorTag == "Jet" && JetorTag_Avg == "Tag")returnVal = maxDEta_jet_aveTagEta;
	
	//if(JetorTag == "Tag" && JetorTag_Avg == "Tag")std::cout<<" ||| "<<returnVal<<"            "<<cntTagEta<<endl;
	
	return returnVal;
	
	
}


class DNNOutput
{
public:
    std::vector<double> values;

    DNNOutput(double ttH, double ttbb, double ttb, double tt2b, double ttcc, double ttlf,
        double other)
    {
        values.push_back(ttH);
        values.push_back(ttbb);
        values.push_back(ttb);
        values.push_back(tt2b);
        values.push_back(ttcc);
        values.push_back(ttlf);
        values.push_back(other);
    }

    DNNOutput()
        : DNNOutput(0., 0., 0., 0., 0., 0., 0.)
    {
        reset();
    }

    ~DNNOutput()
    {
    }

    void reset();

    inline double ttH() const
    {
        return values[0];
    }

    inline double ttbb() const
    {
        return values[1];
    }

    inline double ttb() const
    {
        return values[2];
    }

    inline double tt2b() const
    {
        return values[3];
    }

    inline double ttcc() const
    {
        return values[4];
    }

    inline double ttlf() const
    {
        return values[5];
    }

    inline double other() const
    {
        return values[6];
    }

    inline size_t mostProbableClass() const
    {
        return distance(values.begin(), max_element(values.begin(), values.end()));
    }
};

class DNNVariables
{
public:
    double getHt(const std::vector<const TLorentzVector*>& lvecs) const;

    void getMinMaxDR(const std::vector<const TLorentzVector*>& lvecs, double& minDR,
        double& maxDR) const;

    void getMinMaxDR(const std::vector<const TLorentzVector*>& lvecs, const TLorentzVector* lvec,
        double& minDR, double& maxDR) const;

    double getCentrality(const std::vector<const TLorentzVector*>& lvecs) const;

    void getSphericalEigenValues(const std::vector<const TLorentzVector*>& lvecs, double& ev1,
        double& ev2, double& ev3) const;
};

class DNNClassifierBase
{
public:
    double csvCut;

    DNNClassifierBase(std::string version);

    virtual ~DNNClassifierBase();

    static void pyInitialize();
    static void pyFinalize();
    static void pyExcept(PyObject* pyObj, const std::string& msg);

protected:
    string version_;
    string inputName_;
    string outputName_;
    string dropoutName_;
    PyObject* pyContext_;
    PyObject* pyEval_;
    DNNVariables dnnVars_;
};

class DNNClassifier_SL : public DNNClassifierBase
{
public:
    DNNClassifier_SL(std::string version = "v4");

    ~DNNClassifier_SL();

    void evaluate(const std::vector<TLorentzVector>& jets, const std::vector<double>& jetCSVs,
        const TLorentzVector& lepton, const TLorentzVector& met, DNNOutput& dnnOutput);

    DNNOutput evaluate(const std::vector<TLorentzVector>& jets, const std::vector<double>& jetCSVs,
        const TLorentzVector& lepton, const TLorentzVector& met);

    void fillFeatures_(PyObject* pyEvalArgs, const std::vector<TLorentzVector>& jets,
        const std::vector<double>& jetCSVs, const TLorentzVector& lepton,
        const TLorentzVector& met);

private:
    size_t nFeatures4_;
    size_t nFeatures5_;
    size_t nFeatures6_;
    PyObject* pyEvalArgs4_;
    PyObject* pyEvalArgs5_;
    PyObject* pyEvalArgs6_;
    CommonBDTvars bdtVars_;
};



//DANGERZONE
// HERE you need to add escapes to get the correct print out
// python evaluation script
// python evaluation script
static string evalScript = \"\\
import sys, numpy as np\\n\\
td, inputs, outputs, dropouts = None, [], [], []\\n\\
def setup(python_path, model_files, input_name, output_name, dropout_name):\\n\\
    global td, inputs, outputs, dropouts\\n\\
    sys.path.insert(0, python_path)\\n\\
    import tfdeploy as td\\n\\
    for model_file in model_files:\\n\\
        model = td.Model(model_file)\\n\\
        inputs.append(model.get(input_name))\\n\\
        outputs.append(model.get(output_name))\\n\\
        dropouts.append(model.get(dropout_name))\\n\\
def eval(m, *values):\\n\\
    return list(outputs[m].eval({inputs[m]: [np.array(values).astype(np.float32)], dropouts[m]: 1.})[0])\\n\\
\";


/*
 * DNN Classifier.
 * Please note that this classifier actually outputs 7 discriminator values simultaneously.They can
 * be interpreted as a classification probability as they sum up to 1. Classes (order is important):
 * ttH, ttbb, ttb, tt2b, ttcc, ttlf, other
 */

void DNNOutput::reset()
{
    for (size_t i = 0; i < 7; i++)
    {
        values[i] = -2.;
    }
}

DNNClassifierBase::DNNClassifierBase(std::string version)
    : csvCut(0.8484)
    , version_(version)
    , inputName_("inp")
    , outputName_("outp")
    , dropoutName_("keep_prob")
    , pyContext_(0)
    , pyEval_(0)
{
}

DNNClassifierBase::~DNNClassifierBase()
{
    // cleanup python objects
    if (pyEval_) Py_DECREF(pyEval_);
    if (pyContext_) Py_DECREF(pyContext_);
}

void DNNClassifierBase::pyInitialize()
{
    PyEval_InitThreads();
    Py_Initialize();
}

void DNNClassifierBase::pyFinalize()
{
    Py_Finalize();
}

void DNNClassifierBase::pyExcept(PyObject* pyObj, const std::string& msg)
{
    if (pyObj == NULL)
    {
        if (PyErr_Occurred() != NULL)
        {
            PyErr_PrintEx(0);
        }
        throw runtime_error("a python error occured: " + msg);
    }
}

DNNClassifier_SL::DNNClassifier_SL(std::string version)
    : DNNClassifierBase(version)
    , nFeatures4_(0)
    , nFeatures5_(0)
    , nFeatures6_(0)
    , pyEvalArgs4_(0)
    , pyEvalArgs5_(0)
    , pyEvalArgs6_(0)
{
    // set feature numbers based in the version
    if (version_ == "v2")
    {
        nFeatures4_ = 39;
        nFeatures5_ = 44;
        nFeatures6_ = 49;
    }
    else if (version_ == "v3")
    {
        nFeatures4_ = 30;
        nFeatures5_ = 34;
        nFeatures6_ = 38;
    }
    else if (version_ == "v4")
    {
        nFeatures4_ = 30;
        nFeatures5_ = 34;
        nFeatures6_ = 38;
    }
    else
    {
        throw std::runtime_error("unknown version: " + version_);
    }

    // determine some local paths
    std::string cmsswBase = std::string(getenv("CMSSW_BASE"));
    std::string tfdeployBase = cmsswBase + "/python/TTH/CommonClassifier";
    std::string modelsBase = cmsswBase + "/src/TTH/CommonClassifier/data/dnnmodels_SL_" + version_;
    std::string modelFile4 = modelsBase + "/model_4j.pkl";
    std::string modelFile5 = modelsBase + "/model_5j.pkl";
    std::string modelFile6 = modelsBase + "/model_6j.pkl";

    // initialize the python main object, load the script
    PyObject* pyMainModule = PyImport_AddModule("__main__");

    PyObject* pyMainDict = PyModule_GetDict(pyMainModule);
    pyContext_ = PyDict_Copy(pyMainDict);

    PyRun_String(evalScript.c_str(), Py_file_input, pyContext_, pyContext_);

    // load the tfdeploy models
    PyObject* pySetup = PyDict_GetItemString(pyContext_, "setup");
    PyObject* pyModelFiles = PyTuple_New(3);
    PyTuple_SetItem(pyModelFiles, 0, PyString_FromString(modelFile4.c_str()));
    PyTuple_SetItem(pyModelFiles, 1, PyString_FromString(modelFile5.c_str()));
    PyTuple_SetItem(pyModelFiles, 2, PyString_FromString(modelFile6.c_str()));
    PyObject* pyArgs = PyTuple_New(5);
    PyTuple_SetItem(pyArgs, 0, PyString_FromString(tfdeployBase.c_str()));
    PyTuple_SetItem(pyArgs, 1, pyModelFiles);
    PyTuple_SetItem(pyArgs, 2, PyString_FromString(inputName_.c_str()));
    PyTuple_SetItem(pyArgs, 3, PyString_FromString(outputName_.c_str()));
    PyTuple_SetItem(pyArgs, 4, PyString_FromString(dropoutName_.c_str()));

    PyObject* pyResult = PyObject_CallObject(pySetup, pyArgs);
    pyExcept(pyResult, "could not load tfdeploy models");

    // store the evaluation function and prepare args
    // the "+ 1" is due to the model number being the first argument in the eval function
    pyEval_ = PyDict_GetItemString(pyContext_, "eval");
    pyEvalArgs4_ = PyTuple_New(nFeatures4_ + 1);
    pyEvalArgs5_ = PyTuple_New(nFeatures5_ + 1);
    pyEvalArgs6_ = PyTuple_New(nFeatures6_ + 1);
}

DNNClassifier_SL::~DNNClassifier_SL()
{
    // cleanup python objects
    if (pyEvalArgs4_) Py_DECREF(pyEvalArgs4_);
    if (pyEvalArgs5_) Py_DECREF(pyEvalArgs5_);
    if (pyEvalArgs6_) Py_DECREF(pyEvalArgs6_);
}

void DNNClassifier_SL::evaluate(const std::vector<TLorentzVector>& jets,
    const std::vector<double>& jetCSVs, const TLorentzVector& lepton, const TLorentzVector& met,
    DNNOutput& dnnOutput)
{
    dnnOutput.reset();

    size_t nJets = jets.size();
    size_t modelNum;
    PyObject* pyEvalArgs = NULL;
    if (nJets < 4)
    {
        // no DNN classifier existing for < 4 jets
        return;
    }
    else if (nJets == 4)
    {
        pyEvalArgs = pyEvalArgs4_;
        modelNum = 0;
    }
    else if (nJets == 5)
    {
        pyEvalArgs = pyEvalArgs5_;
        modelNum = 1;
    }
    else
    {
        pyEvalArgs = pyEvalArgs6_;
        modelNum = 2;
    }

    // modelNum is at pos 0
    PyTuple_SetItem(pyEvalArgs, 0, PyInt_FromSize_t(modelNum));

    // fill features into the py tuple
    fillFeatures_(pyEvalArgs, jets, jetCSVs, lepton, met);

    // evaluate
    PyObject* pyList = PyObject_CallObject(pyEval_, pyEvalArgs);
    pyExcept(pyList, "could not evaluate models");

    // fill the dnnOutput
    dnnOutput.values.resize(7);
    // v2 has the "other" category, v3 and v4 don't
    bool hasOther = version_ == "v2";
    for (size_t i = 0; i < (hasOther ? 7 : 6); i++)
    {
        dnnOutput.values[i] = PyFloat_AsDouble(PyList_GetItem(pyList, i));
    }
    if (!hasOther)
    {
        dnnOutput.values[6] = 0.0;
    }

    Py_DECREF(pyList);
}

DNNOutput DNNClassifier_SL::evaluate(const std::vector<TLorentzVector>& jets,
    const std::vector<double>& jetCSVs, const TLorentzVector& lepton, const TLorentzVector& met)
{
    DNNOutput dnnOutput;
    evaluate(jets, jetCSVs, lepton, met, dnnOutput);
    return dnnOutput;
}

void DNNClassifier_SL::fillFeatures_(PyObject* pyEvalArgs, const std::vector<TLorentzVector>& jets,
    const std::vector<double>& jetCSVs, const TLorentzVector& lepton, const TLorentzVector& met)
{
    size_t idx = 1;

    // low-level jet features: pt, eta, phi, mass, csv
    for (size_t i = 0; i < min(jets.size(), (size_t)6); i++)
    {
        PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(jets[i].Pt()));
        PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(jets[i].Eta()));
        PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(jets[i].Phi()));
        if (version_ == "v2")
        {
            PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(jets[i].Mag()));
        }
        PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(jetCSVs[i]));
    }

    // low-level lepton features: pt, eta, phi, mass
    PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(lepton.Pt()));
    PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(lepton.Eta()));
    PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(lepton.Phi()));
    if (version_ == "v2")
    {
        PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(lepton.Mag()));

        // low-level met features: pt, phi
        PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(met.Pt()));
        PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(met.Phi()));
    }

    // split jets into b jets and light jets
    // store pointers to avoid performance drawbacks due to vector copying
    std::vector<const TLorentzVector*> allJets;
    std::vector<const TLorentzVector*> bJets;
    std::vector<double> bCSVs;
    std::vector<const TLorentzVector*> lJets;
    std::vector<double> lCSVs;
    for (size_t i = 0; i < jets.size(); i++)
    {
        allJets.push_back(&jets[i]);
        if (jetCSVs[i] >= csvCut)
        {
            bJets.push_back(&jets[i]);
            bCSVs.push_back(jetCSVs[i]);
        }
        else
        {
            lJets.push_back(&jets[i]);
            lCSVs.push_back(jetCSVs[i]);
        }
    }

    // Ht
    PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(dnnVars_.getHt(allJets)));

    // min and max dR between jets
    double minDRJets, maxDRJets;
    dnnVars_.getMinMaxDR(allJets, minDRJets, maxDRJets);
    PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(minDRJets));
    PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(maxDRJets));

    // min and max dR between light jets
    if (version_ == "v2")
    {
        double minDRLJets, maxDRLJets;
        dnnVars_.getMinMaxDR(lJets, minDRLJets, maxDRLJets);
        PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(minDRLJets));
        PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(maxDRLJets));
    }

    // min and max dR between b jets
    double minDRBJets, maxDRBJets;
    dnnVars_.getMinMaxDR(bJets, minDRBJets, maxDRBJets);
    PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(minDRBJets));
    PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(maxDRBJets));

    // min and max dR between b jets and the lepton
    double minDRBJetsLep, maxDRBJetsLep;
    dnnVars_.getMinMaxDR(bJets, &lepton, minDRBJetsLep, maxDRBJetsLep);
    if (version_ == "v2" || version_ == "v3")
    {
        PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(minDRBJetsLep));
        PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(maxDRBJetsLep));
    }

    // jet centrality
    PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(dnnVars_.getCentrality(allJets)));

    // jet aplanarity, sphericity and transverse sphericity
    double ev1, ev2, ev3;
    dnnVars_.getSphericalEigenValues(allJets, ev1, ev2, ev3);
    PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(3. / 2. * ev3));
    PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(3. / 2. * (ev2 + ev3)));
    double tSphericity = ev2 == 0 ? 0 : (2. * ev2 / (ev1 + ev2));
    PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(tSphericity));

    if (version_ == "v4")
    {
        PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(minDRBJetsLep));
        PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(maxDRBJetsLep));
    }

    // Fox-Wolfram moments
    // disabled for the moment, see https://gitlab.cern.ch/ttH/CommonClassifier/issues/1
    // double fw1, fw2, fw3, fw4, fw5;
    // bdtVars_.getFox(jets, fw1, fw2, fw3, fw4, fw5);
    // PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(fw1));
    // PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(fw2));
    // PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(fw3));
    // PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(fw4));
    // PyTuple_SetItem(pyEvalArgs, idx++, PyFloat_FromDouble(fw5));
}


double DNNVariables::getHt(const std::vector<const TLorentzVector*>& lvecs) const
{
    double ht = 0;
    for (size_t i = 0; i < lvecs.size(); i++)
    {
        ht += lvecs[i]->Pt();
    }
    return ht;
}

void DNNVariables::getMinMaxDR(
    const std::vector<const TLorentzVector*>& lvecs, double& minDR, double& maxDR) const
{
    maxDR = lvecs.size() == 0 ? -1 : 0.;
    minDR = lvecs.size() == 0 ? -1 : 100.;
    if (lvecs.size() >= 2)
    {
        for (size_t i = 0; i < lvecs.size() - 1; i++)
        {
            for (size_t j = i + 1; j < lvecs.size(); j++)
            {
                double dR = lvecs[i]->DeltaR(*lvecs[j]);
                if (dR > maxDR)
                {
                    maxDR = dR;
                }
                if (dR < minDR)
                {
                    minDR = dR;
                }
            }
        }
    }
}

void DNNVariables::getMinMaxDR(const std::vector<const TLorentzVector*>& lvecs,
    const TLorentzVector* lvec, double& minDR, double& maxDR) const
{
    maxDR = lvecs.size() == 0 ? -1 : 0.;
    minDR = lvecs.size() == 0 ? -1 : 100.;
    for (size_t i = 0; i < lvecs.size(); i++)
    {
        double dR = lvecs[i]->DeltaR(*lvec);
        if (dR > maxDR)
        {
            maxDR = dR;
        }
        if (dR < minDR)
        {
            minDR = dR;
        }
    }
}

double DNNVariables::getCentrality(const std::vector<const TLorentzVector*>& lvecs) const
{
    double sumPt = 0.;
    double sumP = 0.;
    for (size_t i = 0; i < lvecs.size(); i++)
    {
        sumPt += lvecs[i]->Pt();
        sumP += lvecs[i]->P();
    }
    return sumPt / sumP;
}

void DNNVariables::getSphericalEigenValues(
    const std::vector<const TLorentzVector*>& lvecs, double& ev1, double& ev2, double& ev3) const
{
    TMatrixDSym momentumMatrix(3);
    double p2Sum = 0.;

    for (size_t i = 0; i < lvecs.size(); i++)
    {
        double px = lvecs[i]->Px();
        double py = lvecs[i]->Py();
        double pz = lvecs[i]->Pz();

        // fill the matrix
        momentumMatrix(0, 0) += px * px;
        momentumMatrix(0, 1) += px * py;
        momentumMatrix(0, 2) += px * pz;
        momentumMatrix(1, 0) += py * px;
        momentumMatrix(1, 1) += py * py;
        momentumMatrix(1, 2) += py * pz;
        momentumMatrix(2, 0) += pz * px;
        momentumMatrix(2, 1) += pz * py;
        momentumMatrix(2, 2) += pz * pz;

        // add 3 momentum squared to sum
        p2Sum += px * px + py * py + pz * pz;
    }

    // normalize each element by p2Sum
    if (p2Sum != 0.)
    {
        for (size_t i = 0; i < 3; i++)
        {
            for (size_t j = 0; j < 3; j++)
            {
                momentumMatrix(i, j) = momentumMatrix(i, j) / p2Sum;
            }
        }
    }

    // calculatate eigen values via eigen vectors
    TMatrixDSymEigen eig(momentumMatrix);
    TVectorD ev = eig.GetEigenValues();

    // some checks due to limited precision of TVectorD
    ev1 = fabs(ev[0]) < 0.00000000000001 ? 0 : ev[0];
    ev2 = fabs(ev[1]) < 0.00000000000001 ? 0 : ev[1];
    ev3 = fabs(ev[2]) < 0.00000000000001 ? 0 : ev[2];
}

"""
  

  retstr+="""
  
//hacked Lepton SF Helper from MiniAODHelper


class LeptonSFHelper {

 public:
  LeptonSFHelper( );
  ~LeptonSFHelper( );

  float GetElectronSF(  float electronPt , float electronEta , int syst , std::string type  );
  float GetMuonSF(  float muonPt , float muonEta , int syst , std::string type  );
  
 private:

  void SetElectronHistos( );
  void SetMuonHistos( );

  TH2F *h_ele_ID_abseta_pt_ratio;
  TH2F *h_ele_TRIGGER_abseta_pt_ratio;
  TH2F *h_ele_ISO_abseta_pt_ratio;
  TH2F *h_ele_GFS_abseta_pt_ratio;

    TH2F *h_mu_ID_abseta_pt_ratioBtoF;
  TH1D *h_mu_HIP_eta_ratioBtoF;
  TH2F *h_mu_TRIGGER_abseta_ptBtoF;
  TH2F *h_mu_ISO_abseta_pt_ratioBtoF;

    TH2F *h_mu_ID_abseta_pt_ratioGtoH;
  TH1D *h_mu_HIP_eta_ratioGtoH;
  TH2F *h_mu_TRIGGER_abseta_ptGtoH;
  TH2F *h_mu_ISO_abseta_pt_ratioGtoH;

  float electronMaxPt;
  float electronMaxPtHigh;
  float electronMaxPtHigher;
  float muonMaxPt;
  float muonMaxPtHigh;
  float ljets_mu_BtoF_lumi;
  float ljets_mu_GtoH_lumi;
  

};

LeptonSFHelper::LeptonSFHelper( ){

  //std::cout << "Initializing Lepton scale factors" << std::endl;

  SetElectronHistos( );
  SetMuonHistos( );
  
 electronMaxPt = 150.0;
  electronMaxPtHigh= 201.0;
  electronMaxPtHigher=499.0;
  muonMaxPt = 119.0;
  muonMaxPtHigh = 499.0;
  
  ljets_mu_BtoF_lumi=19691.782;
  ljets_mu_GtoH_lumi=16226.452;


}

LeptonSFHelper::~LeptonSFHelper( ){

}

float LeptonSFHelper::GetElectronSF(  float electronPt , float electronEta , int syst , std::string type  ) {
  if ( electronPt == 0.0 ){ return 1.0; }

  int thisBin=0;

  float searchEta=electronEta;
  float searchPt=TMath::Min( electronPt , electronMaxPt ); // if e_pt < 150 use the corresponding bin
  if(searchPt==electronMaxPt) {searchPt=electronMaxPtHigher;}; // if e_pt >= 150 go to last bin by setting searchpt to 499
  if (type=="Trigger"){
    searchPt=TMath::Min( electronPt , electronMaxPtHigh ); // if pt > 200 use overflow bin by setting searchpt to 201
  }

  float nomval = 0;
  float error = 0;
  float upval = 0;
  float downval= 0;


  if ( type == "ID" ){

    thisBin = h_ele_ID_abseta_pt_ratio->FindBin( searchEta , searchPt );
    nomval=h_ele_ID_abseta_pt_ratio->GetBinContent( thisBin );
    error=h_ele_ID_abseta_pt_ratio->GetBinError( thisBin );

    upval=nomval+error;
    downval=nomval-error;

  }
  else if ( type == "Trigger" ){

    thisBin = h_ele_TRIGGER_abseta_pt_ratio->FindBin( searchPt, searchEta );
    nomval=h_ele_TRIGGER_abseta_pt_ratio->GetBinContent( thisBin );
    error=h_ele_TRIGGER_abseta_pt_ratio->GetBinError( thisBin );
    upval=nomval+error;
    downval=nomval-error;

  }
  else if ( type == "Iso" ){

    thisBin = h_ele_ISO_abseta_pt_ratio->FindBin( searchEta , searchPt );
    nomval=h_ele_ISO_abseta_pt_ratio->GetBinContent( thisBin );
    error=h_ele_ISO_abseta_pt_ratio->GetBinError( thisBin );
    upval=nomval+error;  //DANGERZONE need to add pT depnednet 1% uncertainty
    downval=nomval-error;
    if(electronPt<20 || electronPt>80) {
        upval=upval*( 1.0+sqrt(0.01*0.01) );
        downval=downval*( 1.0-sqrt(0.01*0.01) );
    }

  }
  else if ( type == "GFS" ){

    thisBin = h_ele_GFS_abseta_pt_ratio->FindBin( searchEta , searchPt );
    nomval=h_ele_GFS_abseta_pt_ratio->GetBinContent( thisBin );
    error=h_ele_GFS_abseta_pt_ratio->GetBinError( thisBin );
    upval=nomval+error; //DANGERZONE need to add pT depnednet 1% uncertainty
    downval=nomval-error;
    if(electronPt<20 || electronPt>80) {
        upval=upval*( 1.0+sqrt(0.01*0.01) );
        downval=downval*( 1.0-sqrt(0.01*0.01) );
    }

  }
  else {

    std::cout << "Unknown Type. Supported Types are: ID, Trigger, Iso" << std::endl;
    nomval = -1;
    upval = -1;
    downval= -1;

  }

  if ( syst==-1 ){ return downval; }
  else if ( syst==1 ){ return upval; }
  else { return nomval; }

}

float LeptonSFHelper::GetMuonSF(  float muonPt , float muonEta , int syst , std::string type  ){
if ( muonPt == 0.0 ){ return 1.0; }

  int thisBin=0;

  float searchEta=fabs( muonEta ); 
  float searchPt=TMath::Min( muonPt , muonMaxPt ); // if muonpt > 119 use last bin
  if (type=="Trigger"){
    searchPt=TMath::Min( muonPt , muonMaxPtHigh );// if muonpt > 499 use last bin
  }
  float nomval = 0;
  float error = 0;
  float upval = 0;
  float downval= 0;
  float nomvalBtoF = 0;
  float errorBtoF = 0;
  float upvalBtoF = 0;
  float downvalBtoF= 0;
  float nomvalGtoH = 0;
  float errorGtoH = 0;
  float upvalGtoH = 0;
  float downvalGtoH= 0;
  

  if ( type == "ID" ){

    thisBin = h_mu_ID_abseta_pt_ratioBtoF->FindBin(  searchPt, searchEta  );
    nomvalBtoF=h_mu_ID_abseta_pt_ratioBtoF->GetBinContent( thisBin );
    errorBtoF=h_mu_ID_abseta_pt_ratioBtoF->GetBinError( thisBin );
    upvalBtoF=( nomvalBtoF+errorBtoF );
    downvalBtoF=( nomvalBtoF-errorBtoF );
    upvalBtoF=upvalBtoF*( 1.0+sqrt(0.01*0.01+0.005*0.005) );
    downvalBtoF=downvalBtoF*( 1.0-sqrt(0.01*0.01+0.005*0.005) );
    
    thisBin = h_mu_ID_abseta_pt_ratioGtoH->FindBin(  searchPt, searchEta  );
    nomvalGtoH=h_mu_ID_abseta_pt_ratioGtoH->GetBinContent( thisBin );
    errorGtoH=h_mu_ID_abseta_pt_ratioGtoH->GetBinError( thisBin );
    upvalGtoH=( nomvalGtoH+errorGtoH );
    downvalGtoH=( nomvalGtoH-errorGtoH );
    upvalGtoH=upvalGtoH*( 1.0+sqrt(0.01*0.01+0.005*0.005) );
    downvalGtoH=downvalGtoH*( 1.0-sqrt(0.01*0.01+0.005*0.005) );

    nomval=(ljets_mu_BtoF_lumi*nomvalBtoF + ljets_mu_GtoH_lumi * nomvalGtoH)/(ljets_mu_BtoF_lumi+ljets_mu_GtoH_lumi);
    upval=(ljets_mu_BtoF_lumi*upvalBtoF + ljets_mu_GtoH_lumi * upvalGtoH)/(ljets_mu_BtoF_lumi+ljets_mu_GtoH_lumi);
    downval=(ljets_mu_BtoF_lumi*downvalBtoF + ljets_mu_GtoH_lumi * downvalGtoH)/(ljets_mu_BtoF_lumi+ljets_mu_GtoH_lumi);

  }
  else if ( type == "Trigger" ){

    thisBin = h_mu_TRIGGER_abseta_ptBtoF->FindBin(  searchPt, searchEta  );
    nomvalBtoF=h_mu_TRIGGER_abseta_ptBtoF->GetBinContent( thisBin );
    errorBtoF=h_mu_TRIGGER_abseta_ptBtoF->GetBinError( thisBin );
    upvalBtoF=( nomvalBtoF+errorBtoF );
    downvalBtoF=( nomvalBtoF-errorBtoF );
    
    thisBin = h_mu_TRIGGER_abseta_ptGtoH->FindBin(  searchPt, searchEta  );
    nomvalGtoH=h_mu_TRIGGER_abseta_ptGtoH->GetBinContent( thisBin );
    errorGtoH=h_mu_TRIGGER_abseta_ptGtoH->GetBinError( thisBin );
    upvalGtoH=( nomvalGtoH+errorGtoH );
    downvalGtoH=( nomvalGtoH-errorGtoH );

    nomval=(ljets_mu_BtoF_lumi*nomvalBtoF + ljets_mu_GtoH_lumi * nomvalGtoH)/(ljets_mu_BtoF_lumi+ljets_mu_GtoH_lumi);
    upval=(ljets_mu_BtoF_lumi*upvalBtoF + ljets_mu_GtoH_lumi * upvalGtoH)/(ljets_mu_BtoF_lumi+ljets_mu_GtoH_lumi);
    downval=(ljets_mu_BtoF_lumi*downvalBtoF + ljets_mu_GtoH_lumi * downvalGtoH)/(ljets_mu_BtoF_lumi+ljets_mu_GtoH_lumi);
    
  }
  else if ( type == "Iso" ){
    
    
    thisBin = h_mu_ISO_abseta_pt_ratioBtoF->FindBin(  searchPt, searchEta  );
    nomvalBtoF=h_mu_ISO_abseta_pt_ratioBtoF->GetBinContent( thisBin );
    errorBtoF=h_mu_ISO_abseta_pt_ratioBtoF->GetBinError( thisBin );
    upvalBtoF=( nomvalBtoF+errorBtoF );
    downvalBtoF=( nomvalBtoF-errorBtoF );
    upvalBtoF=upvalBtoF*(1.0+0.005  );
    downvalBtoF=downvalBtoF*(1.0-0.005 );
    
    thisBin = h_mu_ISO_abseta_pt_ratioGtoH->FindBin(  searchPt, searchEta  );
    nomvalGtoH=h_mu_ISO_abseta_pt_ratioGtoH->GetBinContent( thisBin );
    errorGtoH=h_mu_ISO_abseta_pt_ratioGtoH->GetBinError( thisBin );
    upvalGtoH=( nomvalGtoH+errorGtoH );
    downvalGtoH=( nomvalGtoH-errorGtoH );
    upvalGtoH=upvalGtoH*(1.0+0.005  );
    downvalGtoH=downvalGtoH*( 1.0-0.005 );

    nomval=(ljets_mu_BtoF_lumi*nomvalBtoF + ljets_mu_GtoH_lumi * nomvalGtoH)/(ljets_mu_BtoF_lumi+ljets_mu_GtoH_lumi);
    upval=(ljets_mu_BtoF_lumi*upvalBtoF + ljets_mu_GtoH_lumi * upvalGtoH)/(ljets_mu_BtoF_lumi+ljets_mu_GtoH_lumi);
    downval=(ljets_mu_BtoF_lumi*downvalBtoF + ljets_mu_GtoH_lumi * downvalGtoH)/(ljets_mu_BtoF_lumi+ljets_mu_GtoH_lumi);

  }

  else if ( type == "HIP" ){

    thisBin = h_mu_HIP_eta_ratioBtoF->FindBin( searchEta );
    nomvalBtoF=h_mu_HIP_eta_ratioBtoF->GetBinContent( thisBin );
    errorBtoF=h_mu_HIP_eta_ratioBtoF->GetBinError( thisBin );
    upvalBtoF=( nomvalBtoF+errorBtoF );
    downvalBtoF=( nomvalBtoF-errorBtoF );
    
    thisBin = h_mu_HIP_eta_ratioGtoH->FindBin( searchEta );
    nomvalGtoH=h_mu_HIP_eta_ratioGtoH->GetBinContent( thisBin );
    errorGtoH=h_mu_HIP_eta_ratioGtoH->GetBinError( thisBin );
    upvalGtoH=( nomvalGtoH+errorGtoH );
    downvalGtoH=( nomvalGtoH-errorGtoH );
    
    nomval=(ljets_mu_BtoF_lumi*nomvalBtoF + ljets_mu_GtoH_lumi * nomvalGtoH)/(ljets_mu_BtoF_lumi+ljets_mu_GtoH_lumi);
    upval=(ljets_mu_BtoF_lumi*upvalBtoF + ljets_mu_GtoH_lumi * upvalGtoH)/(ljets_mu_BtoF_lumi+ljets_mu_GtoH_lumi);
    downval=(ljets_mu_BtoF_lumi*downvalBtoF + ljets_mu_GtoH_lumi * downvalGtoH)/(ljets_mu_BtoF_lumi+ljets_mu_GtoH_lumi);
   
//     upval=upval*( 1.0+0.005 );
//     downval=downval*( 1.0-0.005 );


  }
  else {

    std::cout << "Unknown Type. Supported Types are: ID, Trigger, Iso" << std::endl;
    nomval = -1;
    upval = -1;
    downval= -1;

  }


  if ( syst==-1 ){ return downval; }
  else if ( syst==1 ){ return upval; }
  else { return nomval; }


}

void LeptonSFHelper::SetElectronHistos( ){

   std::string IDinputFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/leptonsSF220517/ele_ID_SF.root";
  std::string TRIGGERinputFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/leptonsSF220517/ele_TriggerSF_Run2016All_v1.root";
  std::string ISOinputFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/leptonsSF220517/ele_Reco_EGM2D.root"; // DANGERZONE: no iso SF yet??
  std::string GFSinputFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/leptonsSF220517/ele_Reco_EGM2D.root";

  TFile *f_IDSF = new TFile(std::string(IDinputFile).c_str(),"READ");
  TFile *f_TRIGGERSF = new TFile(std::string(TRIGGERinputFile).c_str(),"READ");
  TFile *f_ISOSF = new TFile(std::string(ISOinputFile).c_str(),"READ");
  TFile *f_GFSSF = new TFile(std::string(GFSinputFile).c_str(),"READ");

  h_ele_ID_abseta_pt_ratio = (TH2F*)f_IDSF->Get("EGamma_SF2D");
  h_ele_TRIGGER_abseta_pt_ratio = (TH2F*)f_TRIGGERSF->Get("Ele27_WPTight_Gsf");
  h_ele_ISO_abseta_pt_ratio = (TH2F*)f_ISOSF->Get("EGamma_SF2D");
  h_ele_GFS_abseta_pt_ratio = (TH2F*)f_GFSSF->Get("EGamma_SF2D");

}

void LeptonSFHelper::SetMuonHistos( ){

  std::string IDinputFileBtoF = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/leptonsSF220517/mu_ID_EfficienciesAndSF_BCDEF.root";
  std::string IDinputFileGtoH = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/leptonsSF220517/mu_ID_EfficienciesAndSF_GH.root";

  std::string TRIGGERinputFileBtoF =  "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/leptonsSF220517/mu_TRIGGER_BtoF.root";
  std::string TRIGGERinputFileGtoH =  "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/leptonsSF220517/mu_TRIGGER_GtoH.root";

  std::string ISOinputFileBtoF =  "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/leptonsSF220517/mu_ISO_EfficienciesAndSF_BCDEF.root";
  std::string ISOinputFileGtoH =  "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/leptonsSF220517/mu_ISO_EfficienciesAndSF_GH.root";
  
  std::string HIPinputFileBtoF =  "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/leptonsSF220517/HIP_BCDEF_histos.root";
  std::string HIPinputFileGtoH =  "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/leptonsSF220517/HIP_GH_histos.root";


  TFile *f_IDSFBtoF = new TFile(std::string(IDinputFileBtoF).c_str(),"READ");
  TFile *f_IDSFGtoH = new TFile(std::string(IDinputFileGtoH).c_str(),"READ");
  
  TFile *f_HIPSFBtoF = new TFile(std::string(HIPinputFileBtoF).c_str(),"READ");
  TFile *f_HIPSFGtoH = new TFile(std::string(HIPinputFileGtoH).c_str(),"READ");

  
  TFile *f_TRIGGERSFBtoF = new TFile(std::string(TRIGGERinputFileBtoF).c_str(),"READ");
  TFile *f_TRIGGERSFGtoH = new TFile(std::string(TRIGGERinputFileGtoH).c_str(),"READ");

  TFile *f_ISOSFBtoF = new TFile(std::string(ISOinputFileBtoF).c_str(),"READ");
  TFile *f_ISOSFGtoH = new TFile(std::string(ISOinputFileGtoH).c_str(),"READ");

  h_mu_ID_abseta_pt_ratioBtoF = (TH2F*)f_IDSFBtoF->Get("MC_NUM_TightID_DEN_genTracks_PAR_pt_eta/pt_abseta_ratio");
  h_mu_ID_abseta_pt_ratioGtoH = (TH2F*)f_IDSFGtoH->Get("MC_NUM_TightID_DEN_genTracks_PAR_pt_eta/pt_abseta_ratio");

  h_mu_HIP_eta_ratioBtoF = (TH1D*)f_HIPSFBtoF->Get("ratio_eff_aeta_dr030e030_corr");
  h_mu_HIP_eta_ratioGtoH = (TH1D*)f_HIPSFGtoH->Get("ratio_eff_aeta_dr030e030_corr");

  h_mu_TRIGGER_abseta_ptBtoF= (TH2F*)f_TRIGGERSFBtoF->Get("IsoMu24_OR_IsoTkMu24_PtEtaBins/pt_abseta_ratio");
  h_mu_TRIGGER_abseta_ptGtoH= (TH2F*)f_TRIGGERSFGtoH->Get("IsoMu24_OR_IsoTkMu24_PtEtaBins/pt_abseta_ratio");

  h_mu_ISO_abseta_pt_ratioBtoF = (TH2F*)f_ISOSFBtoF->Get("TightISO_TightID_pt_eta/pt_abseta_ratio");
  h_mu_ISO_abseta_pt_ratioGtoH = (TH2F*)f_ISOSFGtoH->Get("TightISO_TightID_pt_eta/pt_abseta_ratio");

}

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


void plot(){
  TH1F::SetDefaultSumw2();

  std::string csvHFfile="/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/csv_rwt_fit_hf_v2_final_2017_3_29test.root";
  std::string csvLFfile="/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/csv_rwt_fit_lf_v2_final_2017_3_29test.root";
  
  CSVHelper* internalCSVHelper= new CSVHelper(csvHFfile,csvLFfile, 5);
  LeptonSFHelper* internalLeptonSFHelper= new LeptonSFHelper();

  // open files
  TChain* chain = new TChain("MVATree");
  char* filenames = getenv ("FILENAMES");
  char* outfilename = getenv ("OUTFILENAME");
  string processname = string(getenv ("PROCESSNAME"));
  string suffix = string(getenv ("SUFFIX"));
  int maxevents = atoi(getenv ("MAXEVENTS"));
  int skipevents = atoi(getenv ("SKIPEVENTS"));

std::cout<<"processname" <<processname<<std::endl;
    std::cout<<"suffix" <<suffix<<std::endl;

  std::vector<TString> databaseRelevantFilenames;

  int eventsAnalyzed=0;
  float sumOfWeights=0;

  int DoWeights=1;

  //initialize Trigger Helper

  if(processname=="SingleEl" || processname=="SingleMu"){DoWeights=0; std::cout<<"is data, dont use nominal weihgts"<<std::endl;}


  // read in samples to add to chain and get relevant names for the database
  std::map<TString, TString> sampleDataBaseIdentifiers;
  std::map<TString, std::map<TString, long>> sampleDataBaseFoundEvents;
  std::map<TString, std::map<TString, long>> sampleDataBaseLostEvents;
    
  int internalSystName=0;
  
  string buf;
  stringstream ss(filenames); 
  while (ss >> buf){
    chain->Add(buf.c_str());
    if (buf.find("JESDOWN")!=string::npos){internalSystName=8;}
    if (buf.find("JESUP")!=string::npos){internalSystName=7;}
    if (buf.find("JERDOWN")!=string::npos){internalSystName=0;}
    if (buf.find("JERUP")!=string::npos){internalSystName=0;}
    std::cout<<"internal sys for CSV "<<internalSystName<<std::endl;
    TString thisfilename = buf.c_str();
    TString originalfilename=buf.c_str();
    std::cout<<"file "<<buf.c_str()<<" "<<thisfilename<<std::endl; // karim debug 
    // cut of directories
    thisfilename.Replace(0,thisfilename.Last('/')+1,"");
    //cut if trailing tree and root
    thisfilename.Replace(thisfilename.Last('_'),thisfilename.Length(),"");
    //remove number
    int lastUnderscore=thisfilename.Last('_');
    thisfilename.Replace(thisfilename.Last('_'),1,"");
    thisfilename.Replace(thisfilename.Last('_'),lastUnderscore-thisfilename.Last('_'),"");
    //remove remaining underscores
    while(thisfilename.Last('_')>=0){ thisfilename.Replace(thisfilename.Last('_'),1,"");}
    std::cout<<" relevant database name "<<thisfilename<<std::endl;
    sampleDataBaseIdentifiers[originalfilename]=thisfilename;
    //check if already in vectr
    if(! (std::find(databaseRelevantFilenames.begin(),databaseRelevantFilenames.end(),thisfilename)!=databaseRelevantFilenames.end()  )){
      databaseRelevantFilenames.push_back(thisfilename.Copy());
      //sampleDataBaseFoundEvents["jt42"][thisfilename]=0;
      //sampleDataBaseLostEvents["jt42"][thisfilename]=0;
      //sampleDataBaseFoundEvents["jt52"][thisfilename]=0;
      //sampleDataBaseLostEvents["jt52"][thisfilename]=0;
      //sampleDataBaseFoundEvents["jt62"][thisfilename]=0;
      //sampleDataBaseLostEvents["jt62"][thisfilename]=0;
      sampleDataBaseFoundEvents["jt43"][thisfilename]=0;
      sampleDataBaseLostEvents["jt43"][thisfilename]=0;
      sampleDataBaseFoundEvents["jt53"][thisfilename]=0;
      sampleDataBaseLostEvents["jt53"][thisfilename]=0;
      sampleDataBaseFoundEvents["jt63"][thisfilename]=0;
      sampleDataBaseLostEvents["jt63"][thisfilename]=0;
      sampleDataBaseFoundEvents["jt44"][thisfilename]=0;
      sampleDataBaseLostEvents["jt44"][thisfilename]=0;
      sampleDataBaseFoundEvents["jt54"][thisfilename]=0;
      sampleDataBaseLostEvents["jt54"][thisfilename]=0;
      sampleDataBaseFoundEvents["jt64"][thisfilename]=0;
      sampleDataBaseLostEvents["jt64"][thisfilename]=0;
    }
  }
  std::cout<<"relevant db samplenames"<<std::endl;
  for(unsigned int isn=0; isn<databaseRelevantFilenames.size();isn++){
    std::cout<<databaseRelevantFilenames.at(isn)<<std::endl;
    }
    
  chain->SetBranchStatus("*",0);

  TFile* outfile=new TFile(outfilename,"RECREATE");

  TStopwatch* totalWatch= new TStopwatch();
  TStopwatch* databaseWatch= new TStopwatch();
  double memTime=0;
  
  
  int nEventsVetoed=0;
  int Evt_ID;
  int Evt_Run;
  int Evt_Lumi;
  
  chain->SetBranchStatus("Evt_ID",1);
  chain->SetBranchStatus("Evt_Run",1);
  chain->SetBranchStatus("Evt_Lumi",1);
  
  chain->SetBranchAddress("Evt_ID",&Evt_ID);
  chain->SetBranchAddress("Evt_Run",&Evt_Run);
  chain->SetBranchAddress("Evt_Lumi",&Evt_Lumi);

  


  // initialize variables from tree
"""
  return retstr

def InitDataBase(thisDataBase=[]):
  thisDataBaseName=thisDataBase[0]
  thisDataBasePath=thisDataBase[1]
 
  rstr= """
  // book the database
  
  """
  
  rstr+="  std::vector<MEMDataBase*> "+thisDataBaseName+"DB; \n"
  rstr+="  for(unsigned int isn=0; isn<databaseRelevantFilenames.size();isn++){ \n"
  rstr+="  "+thisDataBaseName+"DB.push_back(new MEMDataBase(\""+thisDataBasePath+"\"));"+"\n"
  rstr+="  "+thisDataBaseName+"DB.back()->AddSample(databaseRelevantFilenames.at(isn),databaseRelevantFilenames.at(isn)+\"_index.txt\");\n"
  rstr+="  "+thisDataBaseName+"DB.back()->PrintStructure();\n"
  rstr+="  std::cout<<\"loaded database for \"<<databaseRelevantFilenames.at(isn)<<std::endl;\n"
  rstr+="  }\n"
  rstr+="  double "+thisDataBaseName+"p=-99.9;\n"
  rstr+="  double "+thisDataBaseName+"p_sig=-99.9;\n"
  rstr+="  double "+thisDataBaseName+"p_bkg=-99.9;\n"
  rstr+="  double "+thisDataBaseName+"p_err_sig=-99.9;\n"
  rstr+="  double "+thisDataBaseName+"p_err_bkg=-99.9;\n"
  rstr+="  double "+thisDataBaseName+"n_perm_sig=-99.9;\n"
  rstr+="  double "+thisDataBaseName+"n_perm_bkg=-99.9;\n"
  rstr+="  DataBaseMEMResult* "+thisDataBaseName+"DummyResultPointer= new DataBaseMEMResult();\n"
  rstr+="  int "+thisDataBaseName+"FoundResult = 1;\n"
  
  return rstr

def readOutDataBase(thisDataBase=[]):
  thisDataBaseName=thisDataBase[0]
  thisDataBasePath=thisDataBase[1]
  skipNonExistingEvent=thisDataBase[2]
  
  rstr= """
  // read the database
    //std::cout<<std::endl<<"run lumi event "<<Evt_Run<<" "<<Evt_Lumi<<" "<<Evt_ID<<std::endl;
  """
  
  rstr+="  "+thisDataBaseName+"p="+thisDataBaseName+"DummyResultPointer->p;\n"
  rstr+="  "+thisDataBaseName+"p_sig="+thisDataBaseName+"DummyResultPointer->p_sig;\n"
  rstr+="  "+thisDataBaseName+"p_bkg="+thisDataBaseName+"DummyResultPointer->p_bkg;\n"
  rstr+="  "+thisDataBaseName+"p_err_sig="+thisDataBaseName+"DummyResultPointer->p_err_sig;\n"
  rstr+="  "+thisDataBaseName+"p_err_bkg="+thisDataBaseName+"DummyResultPointer->p_err_bkg;\n"
  rstr+="  "+thisDataBaseName+"n_perm_sig="+thisDataBaseName+"DummyResultPointer->n_perm_sig;\n"
  rstr+="  "+thisDataBaseName+"n_perm_bkg="+thisDataBaseName+"DummyResultPointer->n_perm_bkg;\n"
  
  rstr+="""
    //get name of current file so that the correct db can be read
    // already done in this version due to trigger stuff
    //TString currentfilename="";
    //currentfilename = chain->GetCurrentFile()->GetName();    
    //std::cout<<"current fileanme for this event "<<currentfilename<<std::endl; // karim debug 
    // cut of directories
    //currentfilename.Replace(0,currentfilename.Last('/')+1,"");
    //cut if trailing tree and root
    //currentfilename.Replace(currentfilename.Last('_'),currentfilename.Length(),"");
    //remove number
    //int lastUnderscore=currentfilename.Last('_');
    //currentfilename.Replace(currentfilename.Last('_'),1,"");
    //currentfilename.Replace(currentfilename.Last('_'),lastUnderscore-currentfilename.Last('_'),"");
    //remove remaining underscores
    //while(currentfilename.Last('_')>=0){ currentfilename.Replace(currentfilename.Last('_'),1,"");}
    TString currentRelevantSampleName=sampleDataBaseIdentifiers[currentfilename];
    //std::cout<<" relevant database name "<<currentRelevantSampleName<<std::endl;
  """
  
  rstr+=" // loop over subsamples of this database\n"
  rstr+="    int nfoundresults=0;\n"
  
  rstr+="  if(N_BTagsM>=3){ \n"
  rstr+="  databaseWatch->Start(); \n"
  
  rstr+="  for(unsigned int isn=0; isn<"+thisDataBaseName+"DB.size();isn++){ \n"
  rstr+="    if(databaseRelevantFilenames.at(isn)==currentRelevantSampleName){;\n"
  rstr+="         DataBaseMEMResult "+thisDataBaseName+"Result = "+thisDataBaseName+"DB.at(isn)->GetMEMResult(databaseRelevantFilenames.at(isn),Evt_Run,Evt_Lumi,Evt_ID);\n"

  #rstr+="        std::cout<<\" p p_sig p_bkg p_err_sig p_err_bkg n_perm_sig n_perm_bkg \"<<"+thisDataBaseName+"p<<\" \"<<"+thisDataBaseName+"p_sig<<\"   \"<<"+thisDataBaseName+"p_bkg<<\" \"<<"+thisDataBaseName+"p_err_sig<<\" \"<<"+thisDataBaseName+"p_err_bkg<<\" \"<<"+thisDataBaseName+"n_perm_sig<<\" \"<<"+thisDataBaseName+"n_perm_bkg<<\" \"<<std::endl;\n"
  
  rstr+="        // check if the event was found using the default values. If any event was found the return values should be different and the resuilt will be replaced\n"
  #rstr+="        if(("+thisDataBaseName+"Result.p != "+thisDataBaseName+"DummyResultPointer->p) or ("+thisDataBaseName+"Result.p_sig != "+thisDataBaseName+"DummyResultPointer->p_sig) or ("+thisDataBaseName+"Result.p_bkg != "+thisDataBaseName+"DummyResultPointer->p_bkg) or ("+thisDataBaseName+"Result.p_err_sig != "+thisDataBaseName+"DummyResultPointer->p_err_sig) or ("+thisDataBaseName+"Result.p_err_bkg != "+thisDataBaseName+"DummyResultPointer->p_err_bkg) or ("+thisDataBaseName+"Result.n_perm_sig != "+thisDataBaseName+"DummyResultPointer->n_perm_sig) or ("+thisDataBaseName+"Result.n_perm_bkg != "+thisDataBaseName+"DummyResultPointer->n_perm_bkg)){\n"
  rstr+="        if(("+thisDataBaseName+"Result.p != -99)){\n"
  rstr+="        nfoundresults+=1;"

  rstr+="      "+thisDataBaseName+"p="+thisDataBaseName+"Result.p;\n"
  rstr+="      "+thisDataBaseName+"p_sig="+thisDataBaseName+"Result.p_sig;\n"
  rstr+="      "+thisDataBaseName+"p_bkg="+thisDataBaseName+"Result.p_bkg;\n"
  rstr+="      "+thisDataBaseName+"p_err_sig="+thisDataBaseName+"Result.p_err_sig;\n"
  rstr+="      "+thisDataBaseName+"p_err_bkg="+thisDataBaseName+"Result.p_err_bkg;\n"
  rstr+="      "+thisDataBaseName+"n_perm_sig="+thisDataBaseName+"Result.n_perm_sig;\n"
  rstr+="      "+thisDataBaseName+"n_perm_bkg="+thisDataBaseName+"Result.n_perm_bkg;\n"
  #rstr+="      std::cout<<\"found database entry \"<<std::endl;\n"
  rstr+="    }\n"
  rstr+="    }\n"
  rstr+="  }// end db loop \n"
  rstr+="    if(nfoundresults!=1){\n"
  rstr+="    //std::cout<<\"WARNING found not exaclty one result \"<<nfoundresults<<\" \"<<currentRelevantSampleName<<\" \"<<Evt_ID<<\" \"<<N_Jets<<\" \"<<N_BTagsM<<std::endl;\n"
  rstr+="    if(N_BTagsM>=3){\n"
  rstr+="      std::cout<<\"VETO this event\"<<\" \"<<currentRelevantSampleName<<\" \"<<Evt_ID<<\" \"<<N_Jets<<\" \"<<N_BTagsM<<std::endl;\n"
  rstr+="      std::cout<<\"RedoThisEvent\"<<\" \"<<currentRelevantSampleName<<\" \"<<currentfilename<<\" \"<<Evt_Run<<\" \"<<Evt_Lumi<<\" \"<<Evt_ID<<std::endl;\n"
  rstr+="      "+thisDataBaseName+"FoundResult=0;\n"
  rstr+="      nEventsVetoed+=1;\n"
  rstr+="""
	       if(N_Jets==4 && N_BTagsM==3){sampleDataBaseLostEvents["jt43"][currentRelevantSampleName]+=1;}
	       else if(N_Jets==4 && N_BTagsM>=4){sampleDataBaseLostEvents["jt44"][currentRelevantSampleName]+=1;}  
	       else if(N_Jets==5 && N_BTagsM==3){sampleDataBaseLostEvents["jt53"][currentRelevantSampleName]+=1;}  
	       else if(N_Jets==5 && N_BTagsM>=4){sampleDataBaseLostEvents["jt54"][currentRelevantSampleName]+=1;}  
	       else if(N_Jets>=6 && N_BTagsM==3){sampleDataBaseLostEvents["jt63"][currentRelevantSampleName]+=1;}  
	       else if(N_Jets>=6 && N_BTagsM>=4){sampleDataBaseLostEvents["jt64"][currentRelevantSampleName]+=1;}  
	"""
  rstr+="    }\n"
  rstr+="  }\n"
  rstr+="  else{\n"
  rstr+="      "+thisDataBaseName+"FoundResult=1;\n"
  rstr+="""
	       if(N_Jets==4 && N_BTagsM==3){sampleDataBaseFoundEvents["jt43"][currentRelevantSampleName]+=1;}
	       else if(N_Jets==4 && N_BTagsM>=4){sampleDataBaseFoundEvents["jt44"][currentRelevantSampleName]+=1;}  
	       else if(N_Jets==5 && N_BTagsM==3){sampleDataBaseFoundEvents["jt53"][currentRelevantSampleName]+=1;}  
	       else if(N_Jets==5 && N_BTagsM>=4){sampleDataBaseFoundEvents["jt54"][currentRelevantSampleName]+=1;}  
	       else if(N_Jets>=6 && N_BTagsM==3){sampleDataBaseFoundEvents["jt63"][currentRelevantSampleName]+=1;}  
	       else if(N_Jets>=6 && N_BTagsM>=4){sampleDataBaseFoundEvents["jt64"][currentRelevantSampleName]+=1;}  
      """  
  #rstr+="  std::cout<<\"FOUNDEVENT\"<<\" \"<<currentRelevantSampleName<<\" \"<<Evt_ID<<\" \"<<N_Jets<<\" \"<<N_BTagsM<<std::endl;\n"
  rstr+=" }\n"
  rstr+="  databaseWatch->Stop(); memTime+=databaseWatch->RealTime();\n"
  if skipNonExistingEvent:
    rstr+="  if("+thisDataBaseName+"FoundResult==0 and N_BTagsM>=3){ std::cout<<\"skipping\"<<std::endl; continue; }\n"
  rstr+="  }\n"
  #if skipNonExistingEvent:
    #rstr+="  if("+thisDataBaseName+"FoundResult==0 and N_BTagsM>=3){ std::cout<<\"skipping\"<<std::endl; continue; }\n"
  
  #rstr+="  std::cout<<\"FINAL p p_sig p_bkg p_err_sig p_err_bkg n_perm_sig n_perm_bkg \"<<"+thisDataBaseName+"p<<\" \"<<"+thisDataBaseName+"p_sig<<\" \"<<"+thisDataBaseName+"p_bkg<<\" \"<<"+thisDataBaseName+"p_err_sig<<\" \"<<"+thisDataBaseName+"p_err_bkg<<\" \"<<"+thisDataBaseName+"n_perm_sig<<\" \"<<"+thisDataBaseName+"n_perm_bkg<<\" \"<<std::endl;\n"
  
  return rstr
  
  
  # Todo write this function that loops over the vector and books the databases and creates the variables ->CHECK
  # write a function that creates the event lumi and run variales and sets the branches  ->CHECK
  # write a function that reads every database. In case of the vector check every one for the -2 return values ->CHECK
  # need to change those return values for blr from -2 to -100 or something -> CHECK?
  # need to set those variables to initalized ones -> CHECK
  # add those functions in the appropriate places ->CHECK
  # need to update the linked database code to the most current one. Also maybe create extra branch or handle the headers differently -> CHECK

def initDNNs():
  rstr="""
  DNNClassifierBase::pyInitialize();
  DNNClassifier_SL dnn("v4");
"""
  return rstr




def initHisto(name,nbins,xmin=0,xmax=0,title_=''):
  if title_=='':
    title=name
  else:
    title=title_
  return '  TH1F* h_'+name+'=new TH1F("'+name+'","'+title+'",'+str(nbins)+','+str(xmin)+','+str(xmax)+');\n'


def initHistoWithProcessNameAndSuffix(name,nbins,xmin=0,xmax=0,title_=''):
  if title_=='':
    title=name
  else:
    title=title_

  return '  TH1F* h_'+name+'=new TH1F((processname+"_'+name+'"+suffix).c_str(),"'+title+'",'+str(nbins)+','+str(xmin)+','+str(xmax)+');\n'


def initTwoDimHistoWithProcessNameAndSuffix(name,nbinsX=10,xminX=0,xmaxX=0,nbinsY=10,xminY=0,xmaxY=0,title_=''):
  if title_=='':
    title=name
  else:
    title=title_

  return '  TH2F* h_'+name+'=new TH2F((processname+"_'+name+'"+suffix).c_str(),"'+title+'",'+str(nbinsX)+','+str(xminX)+','+str(xmaxX)+','+str(nbinsY)+','+str(xminY)+','+str(xmaxY)+');\n'


def fillHistoSyst(name,varname,weight,systnames,systweights):
  text='      float weight_'+name+'='+weight+';\n'
  for sn,sw in zip(systnames,systweights):
    text+=fillHisto(name+sn,varname,'('+sw+')*(weight_'+name+')')
  return text


def fillTwoDimHistoSyst(name,varname1,varname2,weight,systnames,systweights):
  text='      float weight_'+name+'='+weight+';\n'
  for sn,sw in zip(systnames,systweights):
    text+=fillTwoDimHisto(name+sn,varname1,varname2,'('+sw+')*(weight_'+name+')')
  return text


def startLoop():
  return """
  // loop over all events
  long nentries = chain->GetEntries();
  cout << "total number of events: " << nentries << endl;

  for (long iEntry=skipevents;iEntry<nentries;iEntry++) {
    if(iEntry==maxevents) break;
    if(iEntry%10000==0) cout << "analyzing event " << iEntry << endl;

    chain->GetEntry(iEntry);

    TString currentfilename="";
    currentfilename = chain->GetCurrentFile()->GetName();   
    int hasTrigger=0;
    if(currentfilename.Index("withTrigger")!=-1){hasTrigger=1;}
    eventsAnalyzed++;
    sumOfWeights+=Weight;


  // DANGERZONE
  // Only Works for SL events at the moment
  // Lepton SFs 
     double muonPt=0.0;
     double muonEta=0.0;
     double electronEta=0.0;
     double electronPt=0.0;

    if(N_TightMuons==1){muonPt=Muon_Pt[0]; muonEta=Muon_Eta[0];}
    else{muonPt=0.0; muonEta=0.0;}
    if(N_TightElectrons==1){electronPt=Electron_Pt[0]; electronEta=Electron_Eta[0];}
    else{electronPt=0.0; electronEta=0.0;}
   
    float internalEleTriggerWeight=1.0;
    float internalEleTriggerWeightUp=1.0;
    float internalEleTriggerWeightDown=1.0;
    float internalEleIDWeight=1.0;
    float internalEleIDWeightUp=1.0;
    float internalEleIDWeightDown=1.0;
    float internalEleIsoWeight=1.0;
    float internalEleIsoWeightUp=1.0;
    float internalEleIsoWeightDown=1.0;
    float internalEleGFSWeight=1.0;
    float internalEleGFSWeightUp=1.0;
    float internalEleGFSWeightDown=1.0;
    
    float internalMuTriggerWeight=1.0;
    float internalMuTriggerWeightUp=1.0;
    float internalMuTriggerWeightDown=1.0;
    float internalMuIDWeight=1.0;
    float internalMuIDWeightUp=1.0;
    float internalMuIDWeightDown=1.0;
    float internalMuIsoWeight=1.0;
    float internalMuIsoWeightUp=1.0;
    float internalMuIsoWeightDown=1.0;
    float internalMuHIPWeight=1.0;
    float internalMuHIPWeightUp=1.0;
    float internalMuHIPWeightDown=1.0;
   
    if(N_TightMuons==1){
      internalMuTriggerWeight=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,0,"Trigger");
      internalMuTriggerWeightUp=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,1,"Trigger");
      internalMuTriggerWeightDown=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,-1,"Trigger");
      
      internalMuIDWeight=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,0,"ID");
      internalMuIDWeightUp=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,1,"ID");
      internalMuIDWeightDown=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,-1,"ID");
      
      internalMuIsoWeight=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,0,"Iso");
      internalMuIsoWeightUp=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,1,"Iso");
      internalMuIsoWeightDown=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,-1,"Iso");
      
      internalMuHIPWeight=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,0,"HIP");
      internalMuHIPWeightUp=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,1,"HIP");
      internalMuHIPWeightDown=internalLeptonSFHelper->GetMuonSF(muonPt,muonEta,-1,"HIP");
    }
   
    if(N_TightElectrons==1){
      internalEleTriggerWeight=internalLeptonSFHelper->GetElectronSF(muonPt,muonEta,0,"Trigger");
      internalEleTriggerWeightUp=internalLeptonSFHelper->GetElectronSF(muonPt,muonEta,1,"Trigger");
      internalEleTriggerWeightDown=internalLeptonSFHelper->GetElectronSF(muonPt,muonEta,-1,"Trigger");
      
      internalEleIDWeight=internalLeptonSFHelper->GetElectronSF(muonPt,muonEta,0,"ID");
      internalEleIDWeightUp=internalLeptonSFHelper->GetElectronSF(muonPt,muonEta,1,"ID");
      internalEleIDWeightDown=internalLeptonSFHelper->GetElectronSF(muonPt,muonEta,-1,"ID");
      
      internalEleIsoWeight=internalLeptonSFHelper->GetElectronSF(muonPt,muonEta,0,"Iso");
      internalEleIsoWeightUp=internalLeptonSFHelper->GetElectronSF(muonPt,muonEta,1,"Iso");
      internalEleIsoWeightDown=internalLeptonSFHelper->GetElectronSF(muonPt,muonEta,-1,"Iso");
      
      internalEleGFSWeight=internalLeptonSFHelper->GetElectronSF(muonPt,muonEta,0,"GFS");
      internalEleGFSWeightUp=internalLeptonSFHelper->GetElectronSF(muonPt,muonEta,1,"GFS");
      internalEleGFSWeightDown=internalLeptonSFHelper->GetElectronSF(muonPt,muonEta,-1,"GFS");
    }
   
   
  std::vector<double> jetPts;    
  std::vector<double> jetEtas;    
  std::vector<double> jetPhis; 
  std::vector<double> jetMasses;
  std::vector<double> jetEnergies; 
  std::vector<double> jetCSVs;    
  std::vector<int> jetFlavors;    
    
  for(int ijet =0; ijet<N_Jets; ijet++){
	jetPts.push_back(Jet_Pt[ijet]);
	jetEtas.push_back(Jet_Eta[ijet]);
	jetCSVs.push_back(Jet_CSV[ijet]);
	jetFlavors.push_back(Jet_Flav[ijet]);
	jetMasses.push_back(Jet_M[ijet]);
	jetPhis.push_back(Jet_Phi[ijet]);
	jetEnergies.push_back(Jet_E[ijet]);
  }
  
  double primlepPt;    
  double primlepEta;    
  double primlepPhi; 
  double primlepM;
  double primlepE; 
  
  primlepPt=Evt_Pt_PrimaryLepton;
  primlepE=Evt_E_PrimaryLepton;
  primlepPhi=Evt_Phi_PrimaryLepton;
  primlepEta=Evt_Eta_PrimaryLepton;
  primlepM=Evt_M_PrimaryLepton;
  
  float internalCSVweight=1.0;
  float internalCSVweight_CSVHFUp=1.0;
  float internalCSVweight_CSVHFDown=1.0;
  float internalCSVweight_CSVLFUp=1.0;
  float internalCSVweight_CSVLFDown=1.0;
  float internalCSVweight_CSVLFStats1Up=1.0;
  float internalCSVweight_CSVLFStats1Down=1.0;
  float internalCSVweight_CSVLFStats2Up=1.0;
  float internalCSVweight_CSVLFStats2Down=1.0;
  float internalCSVweight_CSVHFStats1Up=1.0;
  float internalCSVweight_CSVHFStats1Down=1.0;
  float internalCSVweight_CSVHFStats2Up=1.0;
  float internalCSVweight_CSVHFStats2Down=1.0;
  float internalCSVweight_CSVCErr1Up=1.0;
  float internalCSVweight_CSVCErr1Down=1.0;
  float internalCSVweight_CSVCErr2Up=1.0;
  float internalCSVweight_CSVCErr2Down=1.0;  
  
  double tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF;
  
  internalCSVweight=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,internalSystName,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF);
  internalCSVweight_CSVHFUp=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,11,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVHFDown=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,12,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVLFUp=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,9,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVLFDown=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,10,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  
  internalCSVweight_CSVLFStats1Up=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,17,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVLFStats1Down=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,18,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVLFStats2Up=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,19,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVLFStats2Down=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,20,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  
  internalCSVweight_CSVHFStats1Up=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,13,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVHFStats1Down=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,14,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVHFStats2Up=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,15,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVHFStats2Down=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,16,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  
  internalCSVweight_CSVCErr1Up=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,21,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVCErr1Down=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,22,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVCErr2Up=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,23,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  internalCSVweight_CSVCErr2Down=internalCSVHelper->getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,24,tmpcsvWgtHF, tmpcsvWgtLF, tmpcsvWgtCF)/internalCSVweight;
  
  /*
  if(internalCSVweight!=Weight_CSV){std::cout<<"internalCSVweight "<<internalCSVweight<<" "<<Weight_CSV<<std::endl;}
  if(internalCSVweight_CSVHFUp!=Weight_CSVHFup){std::cout<<"internalCSVweight_CSVHFUp "<<internalCSVweight_CSVHFUp<<" "<<Weight_CSVHFup<<std::endl;}
  if(internalCSVweight_CSVHFDown!=Weight_CSVHFdown){std::cout<<"internalCSVweight_CSVHFDown "<<internalCSVweight_CSVHFDown<<" "<<Weight_CSVHFdown<<std::endl;}
  if(internalCSVweight_CSVLFUp!=Weight_CSVLFup){std::cout<<"internalCSVweight_CSVLFUp "<<internalCSVweight_CSVLFUp<<" "<<Weight_CSVLFup<<std::endl;}
 if(internalCSVweight_CSVLFDown!=Weight_CSVLFdown){ std::cout<<"internalCSVweight_CSVLFDown "<<internalCSVweight_CSVLFDown<<" "<<Weight_CSVLFdown<<std::endl;}
  
 if(internalCSVweight_CSVLFStats1Up!=Weight_CSVLFStats1up){ std::cout<<"internalCSVweight_CSVLFStats1Up "<<internalCSVweight_CSVLFStats1Up<<" "<<Weight_CSVLFStats1up<<std::endl;}
 if(internalCSVweight_CSVLFStats1Down!=Weight_CSVLFStats1down){ std::cout<<"internalCSVweight_CSVLFStats1Down "<<internalCSVweight_CSVLFStats1Down<<" "<<Weight_CSVLFStats1down<<std::endl;}
 if(internalCSVweight_CSVLFStats2Up!=Weight_CSVLFStats2up){ std::cout<<"internalCSVweight_CSVLFStats2Up "<<internalCSVweight_CSVLFStats2Up<<" "<<Weight_CSVLFStats2up<<std::endl;}
 if(internalCSVweight_CSVLFStats2Down!=Weight_CSVLFStats2down){ std::cout<<"internalCSVweight_CSVLFStats2Down "<<internalCSVweight_CSVLFStats2Down<<" "<<Weight_CSVLFStats2down<<std::endl;}
  
 if(internalCSVweight_CSVHFStats1Up!=Weight_CSVHFStats1up){ std::cout<<"internalCSVweight_CSVHFStats1Up "<<internalCSVweight_CSVHFStats1Up<<" "<<Weight_CSVHFStats1up<<std::endl;}
 if(internalCSVweight_CSVHFStats1Down!=Weight_CSVHFStats1down){ std::cout<<"internalCSVweight_CSVHFStats1Down "<<internalCSVweight_CSVHFStats1Down<<" "<<Weight_CSVHFStats1down<<std::endl;}
 if(internalCSVweight_CSVHFStats2Up!=Weight_CSVHFStats2up){ std::cout<<"internalCSVweight_CSVHFStats2Up "<<internalCSVweight_CSVHFStats2Up<<" "<<Weight_CSVHFStats2up<<std::endl;}
 if(internalCSVweight_CSVHFStats2Down!=Weight_CSVHFStats2down){ std::cout<<"internalCSVweight_CSVHFStats2Down "<<internalCSVweight_CSVHFStats2Down<<" "<<Weight_CSVHFStats2down<<std::endl;}
  
 if(internalCSVweight_CSVCErr1Up!=Weight_CSVCErr1up){ std::cout<<"internalCSVweight_CSVCErr1Up "<<internalCSVweight_CSVCErr1Up<<" "<<Weight_CSVCErr1up<<std::endl;}
 if(internalCSVweight_CSVCErr1Down!=Weight_CSVCErr1down){ std::cout<<"internalCSVweight_CSVCErr1Down "<<internalCSVweight_CSVCErr1Down<<" "<<Weight_CSVCErr1down<<std::endl;}
 if(internalCSVweight_CSVCErr2Up!=Weight_CSVCErr2up){ std::cout<<"internalCSVweight_CSVCErr2Up "<<internalCSVweight_CSVCErr2Up<<" "<<Weight_CSVCErr2up<<std::endl;}
 if(internalCSVweight_CSVCErr2Down!=Weight_CSVCErr2down){ std::cout<<"internalCSVweight_CSVCErr2Down "<<internalCSVweight_CSVCErr2Down<<" "<<Weight_CSVCErr2down<<std::endl;}
 */
 
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

def EvaluateAachenDNNs():
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

def testAachenDNN():
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

def encodeSampleSelection(samples,variables):
  text=''
  for sample in samples:
    arrayselection=variables.checkArrayLengths(sample.selection)
    if arrayselection=='':
      arrayselection ='1'
    sselection=sample.selection
    if sselection=='':
      sselection='1'
    text+= '    if(processname=="'+sample.nick+'" && (!('+arrayselection+') || ('+sselection+')==0) ) continue;\n'
    text+= '    else if(processname=="'+sample.nick+'") sampleweight='+sselection+';\n'
  return text


def startCat(catweight,variables):
  text='\n    // staring category\n'

  arrayselection=variables.checkArrayLengths(catweight)
  if catweight=='':
    catweight='1'
  if arrayselection=='':
    arrayselection ='1'
  text+='    if((('+arrayselection+')*('+catweight+'))!=0) {\n'
  text+='      float categoryweight='+catweight+';\n'
  return text


def endCat():
  return '    }\n    // end of category\n\n'


def fillHisto(histo,var,weight):
  text= '        if(('+weight+')!=0)\n'
  text+='          h_'+histo+'->Fill(fmin(h_'+histo+'->GetXaxis()->GetXmax()-1e-6,fmax(h_'+histo+'->GetXaxis()->GetXmin()+1e-6,'+var+')),'+weight+');\n'
  return text


def fillTwoDimHisto(histo,var1,var2,weight):
  text= '        if(('+weight+')!=0)\n'
  text+='          h_'+histo+'->Fill(fmin(h_'+histo+'->GetXaxis()->GetXmax()-1e-6,fmax(h_'+histo+'->GetXaxis()->GetXmin()+1e-6,'+var1+')),fmin(h_'+histo+'->GetYaxis()->GetXmax()-1e-6,fmax(h_'+histo+'->GetYaxis()->GetXmin()+1e-6,'+var2+')),'+weight+');\n'
  return text


def endLoop():
  return """
  }\n // end of event loop
"""


def varLoop(i,n):
  return '      for(uint '+str(i)+'=0; '+str(i)+'<'+str(n)+'; '+str(i)+'++)'


def getFoot(doAachenDNN):
  rstr= """
  outfile->Write();
  outfile->Close();
  std::ofstream f_nevents((string(outfilename)+".cutflow.txt").c_str());
  f_nevents << "0" << " : " << "all" << " : " << eventsAnalyzed << " : " << sumOfWeights <<endl;
  f_nevents.close();
  std::cout<<"events vetoed because if missing mem "<<nEventsVetoed<<std::endl;
  std::cout<<"all done"<<std::endl;
  totalWatch->Stop();
  std::cout<<"total time "<<totalWatch->RealTime()<<std::endl;
  std::cout<<"time for databse "<<memTime<<std::endl;
  
  std::cout<<"All found events"<<std::endl;
  for(auto const &ent1 : sampleDataBaseFoundEvents) {
  // ent1.first is the first key
    for(auto const &ent2 : ent1.second) {
      // ent2.first is the second key
      // ent2.second is the data
      std::cout<<"FOUNDEVENTSINCAT "<<ent1.first<<" "<<ent2.first<<" "<<ent2.second<<std::endl;
    }
  }
  std::cout<<"All lost events"<<std::endl;
  for(auto const &ent1 : sampleDataBaseLostEvents) {
  // ent1.first is the first key
    for(auto const &ent2 : ent1.second) {
      // ent2.first is the second key
      // ent2.second is the data
      std::cout<<"LOSTEVENTSINCAT "<<ent1.first<<" "<<ent2.first<<" "<<ent2.second<<std::endl;
    }
  }
"""
  if doAachenDNN:
   rstr+="""
     DNNClassifierBase::pyFinalize();
"""

  rstr+="""
  
  
}

int main(){
  plot();
}
"""
  return rstr

def compileProgram(scriptname,usesDataBases,doAachenDNN):
  p = subprocess.Popen(['root-config', '--cflags', '--libs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  out, err = p.communicate()
  if doAachenDNN:
    ppyc = subprocess.Popen(['python-config', '--cflags'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    outpyc, errpyc = ppyc.communicate()
    ppyl = subprocess.Popen(['python-config', '--ldflags'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    outpyl, errpyl = ppyl.communicate()
    print "communicated"
    # get library path for python
    print outpyc
    pythonincludepath=outpyc.split(" ")[0]
    pythonlibrarypath=pythonincludepath.replace("-I","-L").replace("include/python2.7","lib")
  
  memDBccfiles=[]
  dnnfiles=[]
  if doAachenDNN:
    dnnfiles=outpyc[:-1].replace("\n"," ").split(' ')+[pythonlibrarypath]+outpyl[:-1].replace("\n"," ").split(' ')
  if usesDataBases:
    memDBccfiles=glob.glob('/nfs/dust/cms/user/kelmorab/DataBaseCodeForScriptGenerator/MEMDataBase/MEMDataBase/src/*.cc') 
    #TODO update the dataBases code
  cmd= ['g++']+out[:-1].replace("\n"," ").split(' ')+dnnfiles+['-lTMVA']+memDBccfiles+[scriptname+'.cc','-o',scriptname]
  print cmd
  print ""
  print " ".join(cmd)
  print ""
  subprocess.call(cmd)


def createProgram(scriptname,plots,samples,catnames=[""],catselections=["1"],systnames=[""],allsystweights=["1"],additionalvariables=[],dataBases=[],doAachenDNN=False):

  # collect variables
  # list varibles that should not be written to the program automatically

  vetolist=['processname','DoWeights','TMath','electronPt','electronEta','muonPt','muonEta','muonTriggerHelper','electronTriggerHelper','hasTrigger','internalCSVweight','internalCSVweight_CSVHFUp','internalCSVweight_CSVHFDown','internalCSVweight_CSVLFUp','internalCSVweight_CSVLFDown','internalCSVweight_CSVLFStats1Up','internalCSVweight_CSVLFStats1Down','internalCSVweight_CSVLFStats2Up','internalCSVweight_CSVLFStats2Down','internalCSVweight_CSVHFStats1Up','internalCSVweight_CSVHFStats1Down','internalCSVweight_CSVHFStats2Up','internalCSVweight_CSVHFStats2Down','internalCSVweight_CSVCErr1Up','internalCSVweight_CSVCErr1Down','internalCSVweight_CSVCErr2Up','internalCSVweight_CSVCErr2Down',
	    "internalEleTriggerWeight","internalEleTriggerWeightUp","internalEleTriggerWeightDown",
	    "internalEleIDWeight","internalEleIDWeightUp","internalEleIDWeightDown",
	    "internalEleIsoWeight","internalEleIsoWeightUp","internalEleIsoWeightDown",
	    "internalEleGFSWeight","internalEleGFSWeightUp","internalEleGFSWeightDown",
	    "internalMuTriggerWeight","internalMuTriggerWeightUp","internalMuTriggerWeightDown",
	    "internalMuIDWeight","internalMuIDWeightUp","internalMuIDWeightDown",
	    "internalMuIsoWeight","internalMuIsoWeightUp","internalMuIsoWeightDown",
	    "internalMuHIPWeight","internalMuHIPWeightUp","internalMuHIPWeightDown",
	    "aachen_Out_other","aachen_Out_ttbar2B","aachen_Out_ttbarB","aachen_Out_ttbarBB","aachen_Out_ttbarCC","aachen_Out_ttbarOther","aachen_Out_ttH","aachen_pred_class",
]
  for db in dataBases:
    vetolist.append(db[0]+"p")
    vetolist.append(db[0]+"p_sig")
    vetolist.append(db[0]+"p_bkg")
    vetolist.append(db[0]+"p_err_sig")
    vetolist.append(db[0]+"p_err_bkg")
    vetolist.append(db[0]+"n_perm_sig")
    vetolist.append(db[0]+"n_perm_bkg")
    vetolist.append(db[0]+"FoundResult")
    
  print vetolist # karim debug

  # initialize variables object
  variables = variablebox.Variables(vetolist)
  #print variables
  
  # get tree for variable check
  tree = ROOT.TTree()
  for i in range(len(samples)):
    thistreeisgood=False
    for j in range(len(samples[i].files)):
      f=ROOT.TFile(samples[i].files[j])
      tree=f.Get('MVATree')
      if tree.GetEntries()>0:
        print 'using',samples[i].files[j],'to determine variable types'
        thistreeisgood=True
        break
    if thistreeisgood:
      break

  # get standard variables
  standardvars=['Weight','Weight_CSV','Weight_XS']
  variables.initVarsFromExprList(standardvars,tree)

  # get additional variables
  if len(additionalvariables)>0:
    #print additionalvariables
    variables.initVarsFromExprList(additionalvariables,tree)

  # get systematic weight variables
  variables.initVarsFromExprList(allsystweights,tree)

  systweights=[]
  for systweight in allsystweights:
    if ":=" in systweight:
	    systweights.append(systweight.split(":=")[0])
    else:
	    systweights.append(systweight)

  # get sample selection variables
  for sample in samples:
    variables.initVarsFromExpr(sample.selection,tree)

  # get category selection variables
  variables.initVarsFromExprList(catselections,tree)

  # get variables used in plots
  for plot in plots:
    if isinstance(plot,plotutils.Plot):
      variables.initVarsFromExpr(plot.variable,tree)
    if isinstance(plot,plotutils.TwoDimPlot):
      variables.initVarsFromExpr(plot.variable1,tree)
      variables.initVarsFromExpr(plot.variable2,tree)

    variables.initVarsFromExpr(plot.selection,tree)



  # write program
  # start writing program
  script=""
  script+=getHead(dataBases,doAachenDNN)
  
  for db in dataBases:
    script+=InitDataBase(db)
  if doAachenDNN:
    script+=initDNNs()
  # initialize all variables
  script+=variables.initVarsProgram()
  script+=variables.initBranchAddressesProgram()

  # initialize TMVA Readers
  script+=variables.setupTMVAReadersProgram()

  # initialize histograms in all categories and for all systematics
  for c in catnames:
    for plot in plots:
      if isinstance(plot,plotutils.TwoDimPlot):
        t=plot.histo.GetTitle()+";"+plot.histo.GetXaxis().GetTitle()+";"+plot.histo.GetYaxis().GetTitle()
        n=plot.histo.GetName()
        mxX=plot.histo.GetXaxis().GetXmax()
        mnX=plot.histo.GetXaxis().GetXmin()
        nbX=plot.histo.GetNbinsX()
        mxY=plot.histo.GetYaxis().GetXmax()
        mnY=plot.histo.GetYaxis().GetXmin()
        nbY=plot.histo.GetNbinsY()
        for s in systnames:
          script+=initTwoDimHistoWithProcessNameAndSuffix(c+n+s,nbX,mnX,mxX,nbY,mnY,mxY,t)
      else:
        t=plot.histo.GetTitle()
        n=plot.histo.GetName()
        mx=plot.histo.GetXaxis().GetXmax()
        mn=plot.histo.GetXaxis().GetXmin()
        nb=plot.histo.GetNbinsX()
        for s in systnames:
          script+=initHistoWithProcessNameAndSuffix(c+n+s,nb,mn,mx,t)

  # start event loop
  script+=startLoop()
  
  script+='    float sampleweight=1;\n'
  script+=encodeSampleSelection(samples,variables)
  for db in dataBases:
    script+=readOutDataBase(db)  
  script+="\n"
  
  if doAachenDNN:
    script+=EvaluateAachenDNNs()
    script+="\n"

  # calculate varibles and get TMVA outputs
  script+=variables.calculateVarsProgram()

  # start plotting
  for cn,cs in zip(catnames,catselections):

     # for every category
    script+=startCat(cs,variables)

    # plot everything
    # plot one dimensional plots
    for plot in plots:
      if isinstance(plot,plotutils.TwoDimPlot):
        continue

      n=plot.histo.GetName()
      ex=plot.variable
      pw=plot.selection
      if pw=='':
        pw='1'

      # prepare loop over array variables
      variablenames_without_index=variables.varsNoIndex(ex)
      variablenames_without_index+=variables.varsNoIndex(pw)

      # get size of array
      size_of_loop=None
      for v in variablenames_without_index:
        if not v in variables.variables:
          continue
        if variables.variables[v].arraylength != None:
          assert size_of_loop == None or size_of_loop == variables.variables[v].arraylength
          size_of_loop=variables.variables[v].arraylength

      histoname=cn+n
      script+="\n"
      if size_of_loop!=None:
        exi=variables.getArrayEntries(ex,"i")
        pwi=variables.getArrayEntries(pw,"i")
        script+=varLoop("i",size_of_loop)
        script+="{\n"
        arrayselection=variables.checkArrayLengths(','.join([ex,pw]))
        weight='('+arrayselection+')*('+pwi+')*Weight_XS*categoryweight*sampleweight'
        print histoname
        print exi
        print weight
        script+=fillHistoSyst(histoname,exi,weight,systnames,systweights)
        script+="      }\n"
      else:
        arrayselection=variables.checkArrayLengths(','.join([ex,pw]))
        weight='('+arrayselection+')*('+pw+')*Weight_XS*categoryweight*sampleweight'
        script+=fillHistoSyst(histoname,ex,weight,systnames,systweights)

    # plot two dimensional plots
    for plot in plots:
        if not isinstance(plot,plotutils.TwoDimPlot):
          continue

        n=plot.histo.GetName()
        exX=plot.variable1
        exY=plot.variable2
        pw=plot.selection
        if pw=='':
          pw='1'

        # prepare loop over array variables
        variablenames_without_index=varsNoIndex(exX)
        variablenames_without_index+=varsNoIndex(exY)
        variablenames_without_index+=varsNoIndex(pw)

        # get size of array
        size_of_loop=None
        for v in variablenames_without_index:
          if not v in variables.variables:
            continue
          if variables.variables[v].arraylength != None:
            assert size_of_loop == None or size_of_loop == variables.variables[v].arraylength
            size_of_loop=variables.variables[v].arraylength


        histoname=cn+n
        script+="\n"
        if size_of_loop!=None:
          exiX=variables.getArrayEntries(exX,"i")
          exiY=variables.getArrayEntries(ex,"i")
          pwi=variables.getArrayEntries(pw,"i")
          script+=varLoop("i",size_of_loop)
          script+="{\n"
          arrayselection=variables.checkArrayLengths(','.join([exX,exY,pw]))
          weight='('+arrayselection+')*('+pwi+')*Weight_XS*categoryweight*sampleweight'
          script+=fillTwoDimHistoSyst(histoname,exiX,exiY,weight,systnames,systweights)
          script+="      }\n"
        else:
          arrayselection=variables.checkArrayLengths(','.join([ex,pw]),variables)
          weight='('+arrayselection+')*('+pw+')*Weight_XS*categoryweight*sampleweight'
          script+=fillTwoDimHistoSyst(histoname,exX,exY,weight,systnames,systweights)

    # finish category
    script+=endCat()

  # finish loop
  script+=endLoop()
  
  if doAachenDNN:
    script+="\n"
    script+=testAachenDNN()
    script+="\n"
  
  # get program footer
  script+=getFoot(doAachenDNN)

  # write program text to file
  f=open(scriptname+'.cc','w')
  f.write(script)
  f.close()


def createScript(scriptname,programpath,processname,filenames,outfilename,maxevents,skipevents,cmsswpath,suffix):
  script="#!/bin/bash \n"
  if cmsswpath!='':
    script+="export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch \n"
    script+="source $VO_CMS_SW_DIR/cmsset_default.sh \n"
    script+="export SCRAM_ARCH="+os.environ['SCRAM_ARCH']+"\n"
    script+='cd '+cmsswpath+'/src\neval `scram runtime -sh`\n'
    script+='cd - \n'
  script+='export PROCESSNAME="'+processname+'"\n'
  script+='export FILENAMES="'+filenames+'"\n'
  script+='export OUTFILENAME="'+outfilename+'"\n'
  script+='export MAXEVENTS="'+str(maxevents)+'"\n'
  script+='export SKIPEVENTS="'+str(skipevents)+'"\n'
  script+='export SUFFIX="'+suffix+'"\n'
  script+=programpath+'\n'
  #DANGERZONE
  script+='python '+programpath+'_rename.py\n'
  f=open(scriptname,'w')
  f.write(script)
  f.close()
  st = os.stat(scriptname)
  os.chmod(scriptname, st.st_mode | stat.S_IEXEC)


def askYesNo(question):
  print question
  yes = set(['yes','y', 'ye', ''])
  no = set(['no','n'])
  choice = raw_input().lower()
  if choice in yes:
    return True
  elif choice in no:
    return False
  else:
    print "Please respond with 'yes' or 'no'"
    return askYesNo(question)


def submitToNAF(scripts):
  jobids=[]
  logdir = os.getcwd()+"/logs"
  if not os.path.exists(logdir):
    os.makedirs(logdir)
  for script in scripts:
    print 'submitting',script
    command=['qsub', '-cwd', '-S', '/bin/bash','-l', 'h=bird*', '-hard','-l', 'os=sld6', '-l' ,'h_vmem=2000M', '-l', 's_vmem=2000M' ,'-o', logdir, '-e', logdir, script]
    a = subprocess.Popen(command, stdout=subprocess.PIPE,stderr=subprocess.STDOUT,stdin=subprocess.PIPE)
    output = a.communicate()[0]
    jobidstring = output.split()
    for jid in jobidstring:
      if jid.isdigit():
        jobid=int(jid)
        print "this job's ID is", jobid
        jobids.append(jobid)
        break

  return jobids


def do_qstat(jobids):
  allfinished=False
  while not allfinished:
    time.sleep(10)
    a = subprocess.Popen(['qstat'], stdout=subprocess.PIPE,stderr=subprocess.STDOUT,stdin=subprocess.PIPE)
    qstat=a.communicate()[0]
    lines=qstat.split('\n')
    nrunning=0
    for line in lines:
      words=line.split()
      for jid in words:
        if jid.isdigit():
          jobid=int(jid)
          if jobid in jobids:
           nrunning+=1
          break

    if nrunning>0:
      print nrunning,'jobs running'
    else:
      allfinished=True


def get_scripts_outputs_and_nentries(samples,maxevents,scriptsfolder,plotspath,programpath,cmsswpath,treejsonfile=""):
  scripts=[]
  outputs=[]
  nentries=[]
  SaveTreeInforamtion={}
  LoadedTreeInformation={}
  if treejsonfile!="":
    print "Loading file with tree event information"
    jsonfile=open(treejsonfile,"r")
    jsonstring=list(jsonfile)[0]
    LoadedTreeInformation=json.loads(jsonstring)
  for s in samples:
    print 'creating scripts for',s.name,'from',s.path
    ntotal_events=0
    njob=0
    events_in_files=0
    files_to_submit=[]
    for fn in s.files:
      events_in_file=0
      if LoadedTreeInformation!={} and fn in LoadedTreeInformation:
	#print "using tree event information"
	events_in_file=LoadedTreeInformation[fn]
      else:
	#print "did not find this sample in the json file yet"
	#print "will add it"
        f=ROOT.TFile(fn)
        t=f.Get('MVATree')
        events_in_file=t.GetEntries()
      SaveTreeInforamtion[fn]=events_in_file
      # if the file is larger than maxevents it is analyzed in portions of nevents
      if events_in_file > maxevents:
        for ijob in range(events_in_file/maxevents+1):
          njob+=1
          skipevents=(ijob)*maxevents
          scriptname=scriptsfolder+'/'+s.nick+'_'+str(njob)+'.sh'
          processname=s.nick
          filenames=fn
          outfilename=plotspath+s.nick+'_'+str(njob)+'.root'
          createScript(scriptname,programpath,processname,filenames,outfilename,maxevents,skipevents,cmsswpath,'')
          scripts.append(scriptname)
          outputs.append(outfilename)
          nentries.append(events_in_file)
          ntotal_events+=events_in_file

      # else additional files are appended to list of files to be submitted
      else :
        files_to_submit+=[fn]
        events_in_files+=events_in_file
        if events_in_files>maxevents or fn==s.files[-1]:
          njob+=1
          skipevents=0
          scriptname=scriptsfolder+'/'+s.nick+'_'+str(njob)+'.sh'
          processname=s.nick
          filenames=' '.join(files_to_submit)
          outfilename=plotspath+s.nick+'_'+str(njob)+'.root'
          createScript(scriptname,programpath,processname,filenames,outfilename,events_in_files,skipevents,cmsswpath,'')
          scripts.append(scriptname)
          outputs.append(outfilename)
          nentries.append(events_in_files)
          ntotal_events+=events_in_files
          files_to_submit=[]
          events_in_files=0

    # submit remaining scripts (can happen if the last file was large)
    if len(files_to_submit)>0:
      njob+=1
      skipevents=0
      scriptname=scriptsfolder+'/'+s.nick+'_'+str(njob)+'.sh'
      processname=s.nick
      filenames=' '.join(files_to_submit)
      outfilename=plotspath+s.nick+'_'+str(njob)+'.root'
      createScript(scriptname,programpath,processname,filenames,outfilename,events_in_files,skipevents,cmsswpath,'')
      scripts.append(scriptname)
      outputs.append(outfilename)
      nentries.append(events_in_files)
      ntotal_events+=events_in_files
      files_to_submit=[]
      events_in_files=0

    print ntotal_events,'events found in',s.name
  
  # save tree information to json file
    treejson=json.dumps(SaveTreeInforamtion)
    jsonfile=open(scriptsfolder+'/'+"treejson.json","w")
    jsonfile.write(treejson)
    jsonfile.close()
    print "Saved information about events in trees to ", scriptsfolder+'/'+"treejson.json"
  return scripts,outputs,nentries


def check_jobs(scripts,outputs,nentries):
  failed_jobs=[]
  for script,o,n in zip(scripts,outputs,nentries):
    if not os.path.exists(o+'.cutflow.txt'):
      failed_jobs.append(script)
      continue
    f=open(o+'.cutflow.txt')
    processed_entries=-1
    for line in f:
      s=line.split(' : ')
      if len(s)>2 and 'all' in s[1]:
        processed_entries=int(s[2])
        break
    if n!=processed_entries:
      failed_jobs.append(script)
  return failed_jobs

# the dataBases should be defined as follows e.g. [[memDB,path],[blrDB,path]]
def plotParallel(name,maxevents,plots,samples,catnames=[""],catselections=["1"],systnames=[""],systweights=["1"],additionalvariables=[],dataBases=[],treeInformationJsonFile="",otherSystnames=[],doAachenDNN=False):
  cmsswpath=os.environ['CMSSW_BASE']
  if not "CMSSW" in cmsswpath:
    print "you need CMSSW for this to work. Exiting!"
    exit(0)
  cmsswversion=os.environ['CMSSW_VERSION']
  splitcmsswversion=cmsswversion.split("_")
  if doAachenDNN and not int(splitcmsswversion[1])>=8:
    print "You need at least CMSSW 8_0_26_patch2 for the DNNs from Aachen. Exiting!"
    exit(0)
  if doAachenDNN:
    commonclassifierexists=os.path.exists(cmsswpath+"/src/TTH/CommonClassifier")
    if not commonclassifierexists:
      print "You need the common classifier package with the dnns and tf installed. Exiting!"
      exit(0)
  workdir=os.getcwd()+'/workdir/'+name
  outputpath=workdir+'/output.root'

  usesDataBases=False
  if dataBases!=[]:
    usesDataBases=True

  # create workdir folder
  print 'creating workdir folder'
  if not os.path.exists('workdir'):
    os.makedirs('workdir')

  if not os.path.exists(workdir):
    os.makedirs(workdir)
  else:
    if askYesNo('plot existing histograms?'):
      return outputpath
    workdirold=workdir+datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    os.rename(workdir,workdirold)
    os.makedirs(workdir)
    cmd='cp -v '+workdirold+'/'+name+'.cc'+' '+workdir+'/'+name+'.cc'
    subprocess.call(cmd,shell=True)
    cmd='cp -v '+workdirold+'/'+name+''+' '+workdir+'/'+name+'Backup'
    subprocess.call(cmd,shell=True)

  if not os.path.exists(workdir):
    os.makedirs(workdir)

  cmsswpath=os.environ['CMSSW_BASE']
  programpath=workdir+'/'+name

  # create c++ program
  # check if the program already exists
  alreadyWritten=os.path.exists(programpath+'.cc')
  print os.path.exists(programpath+'.cc')
  if alreadyWritten:
    print "a c++ program was written previously. Will check if this needs to be updated"
    cmd='cp -v '+programpath+'.cc'+' '+programpath+'.ccBackup'
    subprocess.call(cmd,shell=True)
  print 'creating c++ program'
  createProgram(programpath,plots,samples,catnames,catselections,systnames,systweights,additionalvariables, dataBases,doAachenDNN)
  if not os.path.exists(programpath+'.cc'):
    print 'could not create c++ program'
    sys.exit()
  # check if the code changed
  codeWasChanged=True
  if alreadyWritten:
    print "comparing c++ code"
    print programpath+'.ccBackup' ," vs ", programpath+'.cc'
    codeWasChanged=not filecmp.cmp(programpath+'.ccBackup',programpath+'.cc')
  if codeWasChanged:
    print "c++ codes differ"
    print 'compiling c++ program'
    compileProgram(programpath, usesDataBases,doAachenDNN)
  else:
    print 'c++ program already existing !!!! Check if this is reasonable!!!'
    cmd = 'cp -v '+programpath+'Backup'+' '+programpath
    subprocess.call(cmd,shell=True)
  if not os.path.exists(programpath):
    print 'could not compile c++ program'
    sys.exit()
    
  #create script to rename histograms
  createRenameScript(programpath,systnames+otherSystnames)
  
  # create output folders
  print 'creating output folders'
  scriptsfolder=workdir+'/'+name+'_scripts'
  if not os.path.exists(scriptsfolder):
    os.makedirs(scriptsfolder)
  plotspath=workdir+'/'+name+'_plots/'
  if not os.path.exists(plotspath):
    os.makedirs(plotspath)
  if not os.path.exists(workdir):
    print 'could not create workdirs'
    sys.exit()

  # create run scripts
  print 'creating run scripts'
  scripts,outputs,nentries=get_scripts_outputs_and_nentries(samples,maxevents,scriptsfolder,plotspath,programpath,cmsswpath,treeInformationJsonFile)
  
  #DANGERZONE
  #exit(0)
  # submit run scripts
  print 'submitting scripts'
  jobids=submitToNAF(scripts)
  do_qstat(jobids)

  # check outputs
  print 'checking outputs'
  failed_jobs=check_jobs(scripts,outputs,nentries)
  retries=0
  while retries<=3 and len(failed_jobs)>0:
    retries+=1
    print 'the following jobs failed'
    for j in failed_jobs:
      print j
    print 'resubmitting'
    jobids=submitToNAF(failed_jobs)
    do_qstat(jobids)
    failed_jobs=check_jobs(scripts,outputs,nentries)
  if retries>=10:
    print 'could not submit jobs'
    sys.exit()

  # hadd outputs
  print 'hadd output'
  subprocess.call(['hadd', outputpath]+outputs)
  print 'done'
  return  outputpath


def createRenameScript(scriptname,systematics):
  header= """
import ROOT
import sys
import os
from subprocess import call
filename=os.getenv("OUTFILENAME")


"""
  
  body="""

def renameHistosParallel(infname,sysnames,prune=False):
  cmd="cp -v "+infname+" "+infname.replace(".root","_original.root")
  call(cmd,shell=True)
  print sysnames
  #infile=ROOT.TFile(infname,"READ")
  outfile=ROOT.TFile(infname,"UPDATE")

  keylist=outfile.GetListOfKeys()
  for key in keylist:
    thisname=key.GetName()
    thish=outfile.Get(thisname)
    newname=thisname
    do=True
    if do and "PSscaleUp" in thisname and "Q2scale" in thisname and thisname[-2:]=="Up":
      tmp=thisname
      tmp=tmp.replace('_CMS_ttH_PSscaleUp','')
      print 'stripped',tmp
      newname=tmp.replace('Q2scale','CombinedScale')

    if "PSscaleDown" in thisname and "Q2scale" in thisname and thisname[-4:]=="Down":
      tmp=thisname
      tmp=tmp.replace('_CMS_ttH_PSscaleDown','')
      newname=tmp.replace('Q2scale','CombinedScale')

    if "dummy" in thisname:
      continue
    nsysts=0
    for sys in sysnames:
      if sys in newname:
	newname=newname.replace(sys,"")
	newname+=sys
	nsysts+=1
	
    if "JES" in thisname or "JER" in thisname:
      if nsysts>2:
	print nsysts, " systs: removing ", thisname
	outfile.Delete(thisname)
	outfile.Delete(thisname+";1")
	continue
    	
    #filter histograms for systs not belonging to the samples 
    #for now until we have NNPDF syst for other samples
    if prune:
      if "CMS_ttH_NNPDF" in thisname:
	if thisname.split("_",1)[0]+"_" not in ["ttbarPlus2B_","ttbarPlusB_","ttbarPlusBBbar_","ttbarPlusCCbar_","ttbarOther_"]:
	  print "wrong syst: removing histogram", thisname
	  continue
      if "CMS_ttH_Q2scale_ttbarOther" in thisname and "ttbarOther"!=thisname.split("_",1)[0]:
	print "wrong syst: removing histogram", thisname
	continue
      if ("CMS_ttH_Q2scale_ttbarPlusBUp" in thisname or "CMS_ttH_Q2scale_ttbarPlusBDown" in thisname ) and "ttbarPlusB"!=thisname.split("_",1)[0] :
	print "wrong syst: removing histogram", thisname
	continue
      if "CMS_ttH_Q2scale_ttbarPlusBBbar" in thisname and "ttbarPlusBBbar"!=thisname.split("_",1)[0] :
	print "wrong syst: removing histogram", thisname
	continue
      if "CMS_ttH_Q2scale_ttbarPlusCCbar" in thisname and "ttbarPlusCCbar"!=thisname.split("_",1)[0] :
	print "wrong syst: removing histogram", thisname
	continue
      if "CMS_ttH_Q2scale_ttbarPlus2B" in thisname and "ttbarPlus2B"!=thisname.split("_",1)[0] :
	print "wrong syst: removing histogram", thisname
	continue
    
    #add ttbar type to systematics name for PS scale
    if "CMS_ttH_PSscaleUp" in newname or "CMS_ttH_PSscaleDown" in newname:
      
      ttbartype=""
      if "ttbarOther"==thisname.split("_",1)[0]:
	ttbartype="ttbarOther"
      elif "ttbarPlusB"==thisname.split("_",1)[0] :
	ttbartype="ttbarPlusB"
      elif "ttbarPlusBBbar"==thisname.split("_",1)[0] :
	ttbartype="ttbarPlusBBbar"
      elif "ttbarPlusCCbar"==thisname.split("_",1)[0] :
	ttbartype="ttbarPlusCCbar"
      elif "ttbarPlus2B"==thisname.split("_",1)[0] :
	ttbartype="ttbarPlus2B"
      else:
	print "wrong syst: removing histogram", thisname
	continue
      
      if "CMS_ttH_PSscaleUp" in newname:
	newname=newname.replace("CMS_ttH_PSscaleUp","CMS_ttH_PSscale_"+ttbartype+"Up")
      elif "CMS_ttH_PSscaleDown" in newname:
	newname=newname.replace("CMS_ttH_PSscaleDown","CMS_ttH_PSscale_"+ttbartype+"Down")
      else:
	print "wrong syst: removing histogram", thisname

    if newname!=thisname:
      print "changed ", thisname, " to ", newname  
      thish.SetName(newname)
      #outfile.cd()
      thish.Write()
      outfile.Delete(thisname+";1")
  
  outfile.Close()
  #infile.Close()    
  
renameHistosParallel(filename,systematics,False) 
  
  """
  
  script=header
  script+="systematics="+str(systematics)+"\n"
  script+=body
  
  scrfile=open(scriptname+"_rename.py","w")
  scrfile.write(script)
  scrfile.close()
    
    
    
    