import ROOT
import json

# local imports
import plotClasses
import PDFutils
ROOT.gROOT.SetBatch(True)

# -- generating the head of the script ------------------------------------------------------------
def getHead(basepath, dataBases, addCodeInterfaces=[]):
  
  includes = ['"TChain.h"', '"TBranch.h"', '"TLorentzVector.h"', '"TFile.h"',
                '"TH1F.h"', '"TH2F.h"', '<iostream>', '<string>', '<sstream>',
                '<vector>', '<algorithm>', '"TMVA/Reader.h"', '<algorithm>',
                '<map>', '"TStopwatch.h"', '<TString.h>', '<TH2D.h>',
                '"LHAPDF/LHAPDF.h"', '"TGraphAsymmErrors.h"', '"TStopwatch.h"',
                '<tuple>']
  retstr = ""
  for include in includes:
    retstr += "#include "+include+"\n"
  
  for addCodeInt in addCodeInterfaces:
    retstr += addCodeInt.getIncludeLines()
  
  if dataBases != []:
    retstr+="""
#include "/nfs/dust/cms/user/kelmorab/DataBaseCodeForScriptGenerator/MEMDataBaseSpring17/MEMDataBase/MEMDataBase/interface/MEMDataBase.h"
"""

  retstr+="""
using namespace std;
"""

  for addCodeInt in addCodeInterfaces:
    retstr += addCodeInt.getAdditionalFunctionDefinitionLines()
  
  with open(basepath+"/util/scriptFiles/runFile-head1.cc", "r") as head1:
    retstr += head1.read()

  with open('/nfs/dust/cms/user/kelmorab/DataBaseCodeForScriptGenerator/MEMDataBaseSpring17/MEMDataBase/MEMDataBase/test/sampleNameMap.json',"r") as jfile:
    jstring = jfile.read()
  sampleTranslationMap = json.loads(jstring)
  for transSample in sampleTranslationMap:
    retstr+="\tsampleTranslationMapCPP[TString(\""+transSample+"\")]=TString(\""+sampleTranslationMap[transSample]+"\");\n"
  
  with open(basepath+"/util/scriptFiles/runFile-head2.cc", "r") as head2:
    retstr += head2.read()
  return retstr
# -------------------------------------------------------------------------------------------------




# -- initializing data bases ----------------------------------------------------------------------
def InitDataBase(thisDataBase=[]):
  thisDataBaseName=thisDataBase[0]
  thisDataBasePath=thisDataBase[1]
 
  rstr= """
  // book the database
  
  """
  
  rstr+="  std::vector<MEMDataBase*> "+thisDataBaseName+"DB; \n"
  rstr+="  for(unsigned int isn=0; isn<databaseRelevantFilenames.size();isn++){ \n"
  rstr+="  "+thisDataBaseName+"DB.push_back(new MEMDataBase(\""+thisDataBasePath+"\",vec_memStrings));"+"\n"
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
  rstr+="  DataBaseMEMResult* "+thisDataBaseName+"DummyResultPointer= new DataBaseMEMResult(vec_memStrings);\n"
  rstr+="  int "+thisDataBaseName+"FoundResult = 1;\n"
  
  return rstr

# -------------------------------------------------------------------------------------------------




# -- initializing histograms ----------------------------------------------------------------------
def initHistos(catnames, systnames, plots):
    rstr = ""
    for cat in catnames:
        for plot in plots:
            if isinstance(plot, plotClasses.TwoDimPlot):
                title = plot.histo.GetTitle()+";"+plot.histo.GetXaxis().GetTitle()+";"+plot.histo.GetYaxis().GetTitle()
                name = plot.histo.GetName()
                maxX = plot.histo.GetXaxis().GetXmax()
                minX = plot.histo.GetXaxis().GetXmin()
                nbinsX = plot.histo.GetNbinsX()
                maxY = plot.histo.GetYaxis().GetXmax()
                minY = plot.histo.GetYaxis().GetXmin()
                nbinsY = plot.histo.GetNbinsY()
                for sname in systnames:
                    rstr += initTwoDimHisto(cat+name+sname, nbinsX, minX, maxX, nbinsY, minY, maxY, title)
            else:
                title = plot.histo.GetTitle()
                name = plot.histo.GetName()
                maxX = plot.histo.GetXaxis().GetXmax()
                minX = plot.histo.GetXaxis().GetXmin()
                nbins = plot.histo.GetNbinsX()
                for sname in systnames:
                    rstr += initOneDimHisto(cat+name+sname, nbins, minX, maxX, title)
    return rstr

def initOneDimHisto(name,nbins,xmin=0,xmax=0,title_=''):
  if title_=='':
    title = name
  else:
    title = title_

  return '  TH1F* h_'+name+'=new TH1F((processname+"_'+name+'"+suffix).c_str(),"'+title+'",'+str(nbins)+','+str(xmin)+','+str(xmax)+');\n'

def initTwoDimHisto(name,nbinsX=10,xminX=0,xmaxX=0,nbinsY=10,xminY=0,xmaxY=0,title_=''):
  if title_=='':
    title=name
  else:
    title=title_

  return '  TH2F* h_'+name+'=new TH2F((processname+"_'+name+'"+suffix).c_str(),"'+title+'",'+str(nbinsX)+','+str(xminX)+','+str(xmaxX)+','+str(nbinsY)+','+str(xminY)+','+str(xmaxY)+');\n'
# -------------------------------------------------------------------------------------------------




# -- defining LHAPDF ------------------------------------------------------------------------------
def DefineLHAPDF():
    code='LHAPDF::PDFSet pdfSet("NNPDF30_nlo_as_0118");\n'
    return code
# -------------------------------------------------------------------------------------------------



# -- starting loop over events --------------------------------------------------------------------
def startLoop(basepath):
  with open(basepath + "/util/scriptFiles/eventLoop-head.cc", "r") as head:
    return head.read()
# -------------------------------------------------------------------------------------------------





# -- handle MEPDF csv file ------------------------------------------------------------------------
class initMEPDF:
    def __init__(self, csv_file):
        self.weight_list = PDFutils.GetMEPDFadditionalVariablesList(csv_file)
        self.pdf_weights = PDFutils.GetPDFadditionalVariablesList(csv_file)

    def writeCode():
        code = ""
        code += self.ResetMEPDFNormFactors()
        code += self.RelateMEPDFMapToNormFactor()
        code += self.PutPDFWeightsinVector()
        code += self.UseLHAPDF()
        return code

    def ResetMEPDFNormFactors(self):
        code=''
        for weight in self.weight_list:
            code+='internalNormFactor_'+weight+'=0.0;\n'
        return code

    def RelateMEPDFMapToNormFactor(self):
        code=''
        code+="""
        TString currentRelevantSampleNameForMEPDF=sampleDataBaseIdentifiers[currentfilename];
        TString translatedCurrentRelevantSampleNameForMEPDF=sampleTranslationMapCPP[currentRelevantSampleNameForMEPDF];
        //std::cout<<"MEPDF relation "<<currentfilename<<" "<<currentRelevantSampleNameForMEPDF<<" "<<translatedCurrentRelevantSampleNameForMEPDF<<std::endl;
        """
        code+='if(MEPDF_Norm_Map.find('+'translatedCurrentRelevantSampleNameForMEPDF'+'+"_'+self.weight_list[0]+'")!=MEPDF_Norm_Map.end()){;\n'
        for weight in self.weight_list:
            code+='internalNormFactor_'+weight+'='+'MEPDF_Norm_Map['+'translatedCurrentRelevantSampleNameForMEPDF'+'+"_'+weight+'"];\n'
        code+='}\n'
        code+='//else{std::cout<<"did not find pdf weights in map "<<translatedCurrentRelevantSampleNameForMEPDF<<std::endl;}\n'
        code+='//std::cout<<"first internal pdf weight "<<'+'translatedCurrentRelevantSampleNameForMEPDF'+'+"_'+self.weight_list[0]+'" <<" "<< internalNormFactor_'+self.weight_list[0]+'<<std::endl;\n'
        return code

    def PutPDFWeightsinVector(self):
        code='std::vector<double> pdf_weights;\n'
        code+='pdf_weights.push_back(1.);\n'
        for weight in self.pdf_weights:
            code+='pdf_weights.push_back(internalNormFactor_'+weight+'*'+weight+');\n'
        return code

    def UseLHAPDF():
        code=''
        #code+='LHAPDF::PDFSet pdfSet("NNPDF30_nlo_as_0118");\n'
        code+='const LHAPDF::PDFUncertainty pdfUnc = pdfSet.uncertainty(pdf_weights, 68.);\n'
        code+='internalPDFweightUp   = pdfUnc.central + pdfUnc.errplus;\n'
        code+='internalPDFweightDown = pdfUnc.central - pdfUnc.errminus;\n'
        code+='internalPDFweight = pdfUnc.central;\n'
        code+='//std::cout<<"result pdf weights: central, down, up "<<pdfUnc.central<<" "<<internalPDFweightDown<< " "<<internalPDFweightUp<<std::endl;\n'
        return code
# -------------------------------------------------------------------------------------------------



# -- encoding samples -----------------------------------------------------------------------------
def encodeSampleSelection(samples, variables):
  text = ''
  for sample in samples:
    arrayselection = variables.checkArrayLengths(sample.selection)
    if arrayselection == '':
      arrayselection = '1'
    sselection = sample.selection
    if sselection == '':
      sselection = '1'
    text+= '    if(processname=="'+sample.nick+'" && (!('+arrayselection+') || ('+sselection+')==0) ) continue;\n'
    text+= '    else if(processname=="'+sample.nick+'") sampleweight='+sselection+';\n'
  return text
# -------------------------------------------------------------------------------------------------




# -- reading data base ----------------------------------------------------------------------------
def readOutDataBase(thisDataBase=[]):
  thisDataBaseName=thisDataBase[0]
  thisDataBasePath=thisDataBase[1]
  skipNonExistingEvent=thisDataBase[2]
  
  rstr= """
  // read the database
    //std::cout<<std::endl<<"run lumi event "<<Evt_Run<<" "<<Evt_Lumi<<" "<<Evt_ID<<std::endl;
  """
  
  rstr+="  "+thisDataBaseName+"p="+thisDataBaseName+"DummyResultPointer->p_vec[0];\n"
  rstr+="  "+thisDataBaseName+"p_sig="+thisDataBaseName+"DummyResultPointer->p_sig;\n"
  rstr+="  "+thisDataBaseName+"p_bkg="+thisDataBaseName+"DummyResultPointer->p_bkg;\n"
  rstr+="  "+thisDataBaseName+"p_err_sig="+thisDataBaseName+"DummyResultPointer->p_err_sig;\n"
  rstr+="  "+thisDataBaseName+"p_err_bkg="+thisDataBaseName+"DummyResultPointer->p_err_bkg;\n"
  rstr+="  "+thisDataBaseName+"n_perm_sig="+thisDataBaseName+"DummyResultPointer->n_perm_sig;\n"
  rstr+="  "+thisDataBaseName+"n_perm_bkg="+thisDataBaseName+"DummyResultPointer->n_perm_bkg;\n"
  
  rstr+="""
    TString currentRelevantSampleName=sampleDataBaseIdentifiers[currentfilename];
    TString translatedCurrentRelevantSampleName=sampleTranslationMapCPP[currentRelevantSampleName];
    if(processname=="QCD" or processname=="QCD_CMS_ttH_QCDScaleFactorUp" or processname=="QCD_CMS_ttH_QCDScaleFactorDown"){
      translatedCurrentRelevantSampleName+="QCD";
      }
    //std::cout<<currentfilename<<" "<<currentRelevantSampleName<<" "<<translatedCurrentRelevantSampleName<<std::endl;
  """
  
  rstr+=" // loop over subsamples of this database\n"
  rstr+="    int nfoundresults=0;\n"
  
  rstr+="  if((N_BTagsM>=3 && N_Jets>=6) || (N_BTagsM>=4 && (N_Jets==4 || N_Jets==5))){ \n"
  rstr+="  databaseWatch->Start(); \n"
  
  rstr+="  for(unsigned int isn=0; isn<"+thisDataBaseName+"DB.size();isn++){ \n"
  rstr+="    if(databaseRelevantFilenames.at(isn)==translatedCurrentRelevantSampleName){;\n"
  rstr+="         DataBaseMEMResult "+thisDataBaseName+"Result = "+thisDataBaseName+"DB.at(isn)->GetMEMResult(databaseRelevantFilenames.at(isn),Evt_Run,Evt_Lumi,Evt_ID);\n"

  #rstr+="        std::cout<<\" p p_sig p_bkg p_err_sig p_err_bkg n_perm_sig n_perm_bkg \"<<"+thisDataBaseName+"p<<\" \"<<"+thisDataBaseName+"p_sig<<\"   \"<<"+thisDataBaseName+"p_bkg<<\" \"<<"+thisDataBaseName+"p_err_sig<<\" \"<<"+thisDataBaseName+"p_err_bkg<<\" \"<<"+thisDataBaseName+"n_perm_sig<<\" \"<<"+thisDataBaseName+"n_perm_bkg<<\" \"<<std::endl;\n"
  
  rstr+="        // check if the event was found using the default values. If any event was found the return values should be different and the resuilt will be replaced\n"
  #rstr+="        if(("+thisDataBaseName+"Result.p != "+thisDataBaseName+"DummyResultPointer->p) or ("+thisDataBaseName+"Result.p_sig != "+thisDataBaseName+"DummyResultPointer->p_sig) or ("+thisDataBaseName+"Result.p_bkg != "+thisDataBaseName+"DummyResultPointer->p_bkg) or ("+thisDataBaseName+"Result.p_err_sig != "+thisDataBaseName+"DummyResultPointer->p_err_sig) or ("+thisDataBaseName+"Result.p_err_bkg != "+thisDataBaseName+"DummyResultPointer->p_err_bkg) or ("+thisDataBaseName+"Result.n_perm_sig != "+thisDataBaseName+"DummyResultPointer->n_perm_sig) or ("+thisDataBaseName+"Result.n_perm_bkg != "+thisDataBaseName+"DummyResultPointer->n_perm_bkg)){\n"
  rstr+="        if(("+thisDataBaseName+"Result.p_vec[0] != -99)){\n"
  rstr+="        nfoundresults+=1;"

  rstr+="      "+thisDataBaseName+"p="+thisDataBaseName+"Result.p_vec[0];\n"
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
  rstr+="    std::cout<<\"WARNING found not exaclty one result \"<<nfoundresults<<\" \"<<currentRelevantSampleName<<\" \"<<Evt_ID<<\" \"<<N_Jets<<\" \"<<N_BTagsM<<std::endl;\n"
  rstr+="    if(N_BTagsM>=3){\n"
  rstr+="      std::cout<<\"VETO this event\"<<\" \"<<currentRelevantSampleName<<\" \"<<Evt_ID<<\" \"<<N_Jets<<\" \"<<N_BTagsM<<std::endl;\n"
  rstr+="      //std::cout<<\"RedoThisEvent\"<<\" \"<<currentRelevantSampleName<<\" \"<<currentfilename<<\" \"<<Evt_Run<<\" \"<<Evt_Lumi<<\" \"<<Evt_ID<<std::endl;\n"
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
  rstr+="  //std::cout<<\"FOUNDEVENT\"<<\" \"<<currentRelevantSampleName<<\" \"<<Evt_ID<<\" \"<<N_Jets<<\" \"<<N_BTagsM<<std::endl;\n"
  rstr+=" }\n"
  rstr+="  databaseWatch->Stop(); memTime+=databaseWatch->RealTime();\n"
  if skipNonExistingEvent:
    rstr+="  if("+thisDataBaseName+"FoundResult==0 and N_BTagsM>=3){ std::cout<<\"skipping\"<<std::endl; continue; }\n"
  rstr+="  }\n"
  
  rstr+="  //std::cout<<\"FINAL p p_sig p_bkg p_err_sig p_err_bkg n_perm_sig n_perm_bkg \"<<"+thisDataBaseName+"p<<\" \"<<"+thisDataBaseName+"p_sig<<\" \"<<"+thisDataBaseName+"p_bkg<<\" \"<<"+thisDataBaseName+"p_err_sig<<\" \"<<"+thisDataBaseName+"p_err_bkg<<\" \"<<"+thisDataBaseName+"n_perm_sig<<\" \"<<"+thisDataBaseName+"n_perm_bkg<<\" \"<<std::endl;\n"
  return rstr
# -------------------------------------------------------------------------------------------------




# -- initializing plots ---------------------------------------------------------------------------
class initPlots:
    def __init__(self, variables, systnames, systweights):
        self.systnames = systnames
        self.systweights = systweights
        self.variables = variables

    def startCat(self, catweight):
        script ='\n    // staring category\n'

        arrayselection = self.variables.checkArrayLengths(catweight)
        if catweight=='':
            catweight='1'
        if arrayselection=='':
            arrayselection ='1'
        script +='    if((('+arrayselection+')*('+catweight+'))!=0) {\n'
        script +='      float categoryweight='+catweight+';\n'
        return script

    def endCat(self):
        return '    }\n    // end of category\n\n'

    def initPlot(self, plot, tree, catname):
        # get dimension of plot
        try:
            dim = plot.dim
        except:
            print("seems like plot is not an instance of Plot or TwoDimPlot...")
            sys.exit()

        script = ""
        plotName = plot.histo.GetName()
        if dim == 1:
            vars = [plot.variable]
        if dim == 2:
            vars = [plot.variable1, plot.variable2]
        sel = plot.selection
        if sel == "":
            sel = "1"

        # prepare loop over array variables
        varsNoIndex = []
        for var in vars:
            varsNoIndex += self.variables.varsNoIndex(var)
        varsNoIndex += self.variables.varsNoIndex(sel)

        # get size of array
        loopSize = None
        for var in varsNoIndex:
            if not var in self.variables.variables:
                continue
            if self.variables.variables[var].arraylength != None:
                assert loopSize == None or loopSize == self.variables.variables[var].arraylength
                loopSize = self.variables.variables[var].arraylength

        histName = catname + plotName
        
        script += "\n"
        if loopSize != None:
            # write histo for array
            var_i = [self.variables.getArrayEntries(var, "i") for var in vars]
            sel_i = self.variables.getArrayEntries(sel, "i")

            script += varLoop("i", loopSize)
            script += "{\n"
            
            arraySelection = self.variables.checkArrayLengths(",".join(vars + [sel]))
            weight = "("+arraySelection+")*("+sel_i+")*Weight_XS*categoryweight*sampleweight"

            script += fillHistoSyst(histName, var_i, weight, self.systnames, self.systweights)
            script += "            }\n"
        else:
            # write histo for single

            # if the variable in 1Dplot doesnt have .xml in name, is not in tree and has "_" in name
            # split the variable name, because it is a vector subvariable
            if dim == 1 and not ".xml" in vars[0] and not hasattr(tree, vars[0]) and "_" in vars[0]:
                varOld = vars[0]
                varHead, varTail = varOld.rsplit("_", 1)
                if hasattr(tree, varHead) and varTail.isdigit():
                    vars[0] = varHead + "[" + str(int(varTail) - 1) + "]"
                    print "Found vector sub variable: ", varOld, " which was converted to: ",vars[0] 

            arraySelection = self.variables.checkArrayLengths(",".join(vars + [sel]))
            weight = '('+arraySelection+')*('+sel+')*Weight_XS*categoryweight*sampleweight'
            script += fillHistoSyst(histName, vars, weight, self.systnames, self.systweights)
        
        return script
        



def varLoop(i,n):
    return '      for(uint '+str(i)+'=0; '+str(i)+'<'+str(n)+'; '+str(i)+'++)'

def fillHistoSyst(histName, varNames, weight, systNames, systWeights):
    text = '      float weight_'+histName+'='+weight+';\n'
    # Write all individual systnames and systweights in nested vector 
    # to use together with function allowing variadic vector size 
    # -> speed-up of compilation and less code lines
    text += '     std::vector<structHelpFillHisto> helpWeightVec_' + histName + ' = {'

    # loop over systematics
    for systName, systWeight in zip(systNames, systWeights):
        text += '       { ' + 'h_'+ histName+systName + ', '
        if len(varNames) == 1:
            # this is a oneDimPlot
            text += 'double(' + varNames[0] + '), '
        elif len(varNames) == 2:
            # this is a twoDimplot
            text += varNames[0] + ', ' + varNames[1] + ', '
        else:
            print("this is not a valid configuration of varNames "+str(varNames))
            return None
        text+= '('+systWeight+')*(weight_'+histName+')' + '},'

    # finish vector     
    text+= '     };\n'

    # call helper fill histo function which is defined in the beginning of CC script
    if len(varNames) == 1:
        text+='     helperFillHisto(helpWeightVec_' + histName + ');\n'
    elif len(varNames) == 2:
        text+='     helperFillTwoDimHisto(helpWeightVec_' + name + ');\n'
    return text

# -------------------------------------------------------------------------------------------------





# -- finishing loop over events -------------------------------------------------------------------
def endLoop():
  return """
  }\n // end of event loop
  totalTime+=timerTotal->RealTime();
  std::cout<<"skipped a total of "<<evtFilter->GetNFiltered()<<std::endl;
"""
# -------------------------------------------------------------------------------------------------





# -- generating foot of the script ----------------------------------------------------------------
def getFoot(addCodeInterfaces):
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
  
  for addCodeInt in addCodeInterfaces:
    rstr+=addCodeInt.getCleanUpLines()


  rstr+="""
  
  std::cout<<"time getting event: "<<totalTimeGetEntry<<std::endl;
  std::cout<<"time calculating SFs: "<<totalTimeCalculateSFs<<std::endl;
  std::cout<<"time reading DBs: "<<totalTimeReadDataBase<<std::endl;
  std::cout<<"time Eval DNN: "<<totalTimeEvalDNN<<std::endl;
  std::cout<<"time Eval weights and BDTs: "<<totalTimeEvalWeightsAndBDT<<std::endl;
  std::cout<<"time for sampel weight: "<<totalTimeSampleWeight<<std::endl;
  std::cout<<"time filling histos: "<<totalTimeFillHistograms<<std::endl;
  std::cout<<"time mapping values: "<<totalTimeMapping<<std::endl;
  std::cout<<"time spent in event loop: "<<totalTime<<std::endl;

  
}

int main(){
  plot();
}
"""
  return rstr
# -------------------------------------------------------------------------------------------------





# -- functions dealing with MEPDFcsv file ---------------------------------------------------------
def AddMEandPDFNormalizationsMap(csv_file):
    mydict = PDFutils.ReadMEandPDFNormalizations(csv_file)
    code='std::map<TString,float> MEPDF_Norm_Map;\n'
    for key in mydict:
        code+='MEPDF_Norm_Map["'+key[0]+'_'+key[1]+'"]='+mydict[key]+';\n'
    return code


def GetMEPDFVetoList(csv_file):
    weightList = PDFutils.GetMEPDFadditionalVariablesList(csv_file)
    weightVetoList = []
    for weight in weightList:
        weightVetoList.append('internalNormFactor_'+weight)
    return weightVetoList

def DeclareMEPDFNormFactors(csv_file):
    code=''
    weight_list=PDFutils.GetMEPDFadditionalVariablesList(csv_file)
    for weight in weight_list:
        code+='float internalNormFactor_'+weight+'=0.0;\n'
    return code
# -------------------------------------------------------------------------------------------------
