import ROOT
import json
import os

# local imports
import plotClasses
ROOT.gROOT.SetBatch(True)

# -- generating the head of the script ------------------------------------------------------------
def getHead(basepath, dataBases, memDB_path, addCodeInterfaces=[], useNormHeader = None):
  
  includes = ['"TChain.h"', '"TBranch.h"', '"TLorentzVector.h"', '"TFile.h"',
                '"TH1F.h"', '"TH2F.h"', '<iostream>', '<string>', '<sstream>',
                '<vector>', '<algorithm>', '"TMVA/Reader.h"', '<algorithm>',
                '<map>', '"TStopwatch.h"', '<TString.h>', '<TH2D.h>',
                '"LHAPDF/LHAPDF.h"', '"TGraphAsymmErrors.h"', '"TStopwatch.h"',
                '<tuple>']
  if useNormHeader:
    includes.append('"{}"'.format(useNormHeader))
  retstr = ""

  for include in includes:
    retstr += "#include "+include+"\n"
  
  # build paths for additional external c++ files
  # note: '*' (splat operator) returns all elements of list returned by "split"
  scriptdirpath = os.path.join(basepath,*("/util/scriptFiles".split("/")))
  include_template = os.path.join(*("src/{}.cc".split("/")))


  for addCodeInt in addCodeInterfaces:
    retstr += addCodeInt.getIncludeLines( pathToScriptDir = scriptdirpath,
                                          toinclude = include_template.format("tensorflow_utils")
                                        )
  
  if dataBases != []:
    retstr+='#include "'+str(memDB_path)+'/interface/MEMDataBase.h"\n'

  includedClasses = [
    "EventFilter",
    "LeptonSFHelper",
    "Systematics",
    "CSVHelper",
    #"QCDHelper",
    #"TTbarSystHelper",
    ]
  
  counter = 0
  for cls in includedClasses:
    includepath = include_template.format(cls)
    path = os.path.join(scriptdirpath,includepath)
    print "checking path to include: " + path
    if os.path.exists(path):
      if counter == 0:
        retstr += "// following files can be found in {}\n".format(scriptdirpath)
      retstr += '#include "{}"\n'.format(includepath)
      counter += 1
    else:
      print "WARNING: could not find file '{}', will not include it!".format(path)

  retstr+="""
using namespace std;
"""
  # exported into class "tensorflow_utils"
  # for addCodeInt in addCodeInterfaces:
  #   retstr += addCodeInt.getAdditionalFunctionDefinitionLines()
  
  
  plotHeadPath = os.path.join(scriptdirpath, "plotHead.cc")
  if not os.path.exists(plotHeadPath):
    exit("ERROR: Could not find file '{}'!".format(plotHeadPath))
  with open(plotHeadPath, "r") as head:
    retstr += head.read()

  return retstr
# -------------------------------------------------------------------------------------------------




# -- initializing data bases ----------------------------------------------------------------------
def InitDataBase(thisDataBase=[]):
  thisDataBaseName=thisDataBase[0]
  thisDataBasePath=thisDataBase[1]
 
  rstr= """
  // book the database
  std::vector<MEMDataBase*> {DBname}DB;

  for(unsigned int isn=0; isn<databaseRelevantFilenames.size();isn++){{
    {DBname}DB.push_back(new MEMDataBase("{DBpath}",vec_memStrings));
    {DBname}DB.back()->AddSample(databaseRelevantFilenames.at(isn),databaseRelevantFilenames.at(isn)+"_index.txt");
    {DBname}DB.back()->PrintStructure();
    std::cout<<"loaded database for "<<databaseRelevantFilenames.at(isn)<<std::endl;
  }}
  double {DBname}p=-99.9;
  double {DBname}p_sig=-99.9;
  double {DBname}p_bkg=-99.9;
  double {DBname}p_err_sig=-99.9;
  double {DBname}p_err_bkg=-99.9;
  double {DBname}n_perm_sig=-99.9;
  double {DBname}n_perm_bkg=-99.9;
  auto {DBname}DummyResultPointer = std::unique_ptr<DataBaseMEMResult>(new DataBaseMEMResult(vec_memStrings));
  int {DBname}FoundResult = 1;
  """.format(DBname = thisDataBaseName, DBpath = thisDataBasePath)
  return rstr

# -------------------------------------------------------------------------------------------------




# -- initializing histograms ----------------------------------------------------------------------
def initHistos(catnames, systnames, plots, nom_histname_template, syst_histname_template, edge_precision=4):
    rstr = """
double variable = -999;
double variable1 = -999;
double variable2 = -999;
std::vector<std::string> systematics = {{
{}
}};

""".format(",\n".join(['\t"{}"'.format(x) for x in systnames]))
# std::vector<std::string> categs = {\n"
# for cat in catnames:
#     rstr += "    \""+cat+"\",\n"
# rstr = rstr[:-2]+"\n};\n"
    rstr += """std::map<std::string, Plot1DInfoStruct> plotinfo1D;
std::map<std::string, Plot2DInfoStruct> plotinfo2D;
std::map<std::string, std::unique_ptr<TH1>> histos1D;
std::map<std::string, std::unique_ptr<TH2>> histos2D;
"""
    for plot in plots:
        if plot.dim == 2:
            title  = plot.histo.GetTitle()+";"+plot.histo.GetXaxis().GetTitle()+";"+plot.histo.GetYaxis().GetTitle()
            name   = plot.histo.GetName()
            nbinsX = plot.histo.GetNbinsX()
            bin_edges_x = []
            for i in range(1, nbinsX+2):
              bin_edges_x.append(str(round(plot.histo.GetXaxis().GetBinLowEdge(i),edge_precision)))
            nbinsY = plot.histo.GetNbinsY()
            bin_edges_y = []
            for i in range(1, nbinsY+2):
              bin_edges_y.append(str(round(plot.histo.GetYaxis().GetBinLowEdge(i),edge_precision)))
            rstr  += """plotinfo2D["{0}"] = {{"{0}","{1}",{2},{{ {3} }}, {4}, {{ {5} }} }};\n""".format(name, title, 
                                                                                                        nbinsX, ",".join(bin_edges_x), 
                                                                                                        nbinsY, ",".join(bin_edges_y)
                                                                                                        )
        else:
            title  = plot.histo.GetTitle()
            name   = plot.histo.GetName()
            nbins  = plot.histo.GetNbinsX()
            bin_edges = []
            for i in range(1, nbins+2):
              bin_edges.append(str(round(plot.histo.GetBinLowEdge(i),edge_precision)))
            rstr  += """plotinfo1D["{0}"] = {{"{0}","{1}",{2},{{ {3} }} }};\n""".format(name, title, nbins, ",".join(bin_edges))

    rstr += """
TString histname;
for(const auto& obj: plotinfo1D){{
  for(const auto& syst: systematics){{
    const auto& PlotInfo1D = obj.second;
    if(syst == "") histname = "{nom_hist_temp}";
    else histname = "{syst_hist_temp}";
    histname.ReplaceAll("$PROCESS", processname);
    histname.ReplaceAll("$CHANNEL", obj.first);
    histname.ReplaceAll("$SYSTEMATIC", syst);
    histos1D[obj.first+syst] = std::unique_ptr<TH1>(new TH1F((histname.Data()+suffix).c_str(), (PlotInfo1D.title).c_str(), PlotInfo1D.nbins, PlotInfo1D.edges.data()));
    histos1D[obj.first+syst]->SetDirectory(0);
    if (skipWeightSysts) break;
  }}
}}

for(const auto& obj: plotinfo2D){{
  for(const auto& syst: systematics){{
    const auto& PlotInfo2D = obj.second;
    if(syst == "") histname = "{nom_hist_temp}";
    else histname = "{syst_hist_temp}";
    histname.ReplaceAll("$PROCESS", processname);
    histname.ReplaceAll("$CHANNEL", obj.first);
    histname.ReplaceAll("$SYSTEMATIC", syst);
    histos2D[obj.first+syst] = std::unique_ptr<TH2>(new TH2F((histname.Data()+suffix).c_str(), (PlotInfo2D.title).c_str(), 
                                                                PlotInfo2D.nbinsx, PlotInfo2D.edges_x.data(), 
                                                                PlotInfo2D.nbinsy, PlotInfo2D.edges_y.data()));
    histos2D[obj.first+syst]->SetDirectory(0);
    if (skipWeightSysts) break;
  }}
}}""".format( nom_hist_temp   = nom_histname_template,
              syst_hist_temp  = syst_histname_template)
    
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
  with open(basepath + "/util/scriptFiles/eventLoopHead.cc", "r") as head:
    return head.read()
# -------------------------------------------------------------------------------------------------





# -- encoding sampleSelections --------------------------------------------------------------------
def encodeSampleSelection(samples, varManager):
    text = ''
    for sample in samples:
        arraySelection = varManager.checkArrayLengths(sample.selection)
        if arraySelection == '':  arraySelection = '1'
        sampleSelection = sample.selection
        if sampleSelection == '': sampleSelection = '1'
        text+= '    if(processname=="'+sample.nick+'" && (!('+arraySelection+') || ('+sampleSelection+')==0) ) continue;\n'
        text+= '    else if(processname=="'+sample.nick+'") sampleweight='+sampleSelection+';\n'
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
    //TString translatedCurrentRelevantSampleName=sampleTranslationMapCPP[currentRelevantSampleName];
    //if(processname=="QCD" or processname=="QCD_CMS_ttH_QCDScaleFactorUp" or processname=="QCD_CMS_ttH_QCDScaleFactorDown"){
    //  translatedCurrentRelevantSampleName+="QCD";
    //  }
    //std::cout<<currentfilename<<" "<<currentRelevantSampleName<<" "<<translatedCurrentRelevantSampleName<<std::endl;
  """
  
  rstr+=" // loop over subsamples of this database\n"
  rstr+="    int nfoundresults=0;\n"
  
  # at the moment we want the MEM for everything
  #rstr+="  if((N_BTagsM>=3 && N_Jets>=6) || (N_BTagsM>=4 && (N_Jets==4 || N_Jets==5))){ \n"
  rstr+="  if((N_BTagsM>=3 && N_Jets>=4)){ \n"
  rstr+="  databaseWatch->Start(); \n"
  
  rstr+="  for(unsigned int isn=0; isn<"+thisDataBaseName+"DB.size();isn++){ \n"
  rstr+="    if(databaseRelevantFilenames.at(isn)==currentRelevantSampleName){;\n"
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
    def __init__(self, varManager, systnames, systweights):
        self.systnames = systnames
        self.systweights = systweights
        self.varManager = varManager

    def startCat(self, catWeight):
        script ='\n    // starting category\n'

        arraySelection = self.varManager.checkArrayLengths(catWeight)
        print("arraySelection:" +str(arraySelection))

        if catWeight == '':         catWeight='1'
        if arraySelection == '':    arraySelection ='1'

        script +='    if( ( ('+arraySelection+')*('+catWeight+') )!=0 )\n    {\n'
        script +='      float categoryweight='+catWeight+';\n'
        return script

    def endCat(self):
        return '    }\n    // end of category\n\n'

    def initPlot(self, plot, tree, catname):
        # get dimension of plot
        try: dim = plot.dim
        except:
            print("seems like plot is not an instance of Plot or TwoDimPlot...")
            sys.exit()

        script = ""
        plotName = plot.histo.GetName()
        if dim == 1: variables = [plot.variable]
        if dim == 2: variables = [plot.variable1, plot.variable2]
        sel = plot.selection
        if sel == "": sel = "1"

        # prepare loop over array variables
        variablesNoIndex = []
        for var in variables:
            variablesNoIndex += self.varManager.getVariablesNoIndex(var)
        variablesNoIndex += self.varManager.getVariablesNoIndex(sel)
        variablesNoIndex = list(set(variablesNoIndex))

        # get size of array
        loopSize = None
        for var in variablesNoIndex:
            if not var in self.varManager.variables: continue

            if self.varManager.variables[var].isArray:
                assert loopSize == None or loopSize == self.varManager.variables[var].indexVariable
                loopSize = self.varManager.variables[var].indexVariable

        # set histogram name
        histName = catname + plotName
        
        script += "\n"
        if not loopSize == None:
            # write histo for array
            var_i = [self.varManager.getArrayEntries(var, "i") for var in variables]
            sel_i = self.varManager.getArrayEntries(sel, "i")

            script += varLoop("i", loopSize)
            script += "{\n"
            
            arraySelection = self.varManager.checkArrayLengths(",".join(variables + [sel]))
            weight = "("+arraySelection+")*("+sel_i+")*Weight_XS*categoryweight*sampleweight"

            script += fillHistoSyst(histName, var_i, weight, self.systnames, self.systweights)
            script += "            }\n"
        else:
            # only handle one dimensional plots that are not BDT variables, are not in tree and have '_' in name
            if dim == 1 and not ".xml" in variables[0] and not hasattr(tree, variables[0]) and "_" in variables[0]:
                
                varOld = variables[0]
                varHead, varTail = varOld.rsplit("_", 1)
                if hasattr(tree, varHead) and varTail.isdigit():
                    # construct array like variable varHead[index]
                    variables[0] = varHead + "[" + str(int(varTail) - 1) + "]"
                    print("found vector variable "+str(varOld)+". Converted to: "+str(variables[0]))

            arraySelection = self.varManager.checkArrayLengths(",".join(variables + [sel]))
            weight = '('+arraySelection+')*('+sel+')*Weight_XS*categoryweight*sampleweight'
            script += fillHistoSyst(histName, variables, weight, self.systnames, self.systweights)
        if self.varManager.verbose > 20: print("\n\ninit plot code for "+str(plotName)+":\n"+str(script))
        return script
        



def varLoop(i,n):
    return '      for(int '+str(i)+'=0; '+str(i)+'<'+str(n)+'; '+str(i)+'++)'

def fillHistoSyst(histName, varNames, weight, systNames, systWeights):
    text = '      float weight_'+histName+'='+weight+';\n'
    # Write all individual systnames and systweights in nested vector 
    # to use together with function allowing variadic vector size 
    # -> speed-up of compilation and less code lines
    if len(varNames) == 1:
        # 1D Histograms
        text += '       std::vector<structHelpFillHisto> helpWeightVec_' + histName + ' = {\n'
        # Do Nominal Plot for sure
        text += "           {histos1D[\""+histName+"\"].get()"+", (weight_"+histName+")},\n"
        text += "       };\n"

        text += "       if (!skipWeightSysts) { // append plots for weight systs if neccessary \n"
        for systName, systWeight in zip(systNames[1:], systWeights[1:]):
            text += "             helpWeightVec_" + histName + ".push_back({histos1D[\""+histName+systName+"\"].get()"+", ("+systWeight+")*(weight_"+histName+")});\n"
        text += "       };\n"
            
        text += "       variable = "+varNames[0]+";\n"

        text += "       helperFillHisto(helpWeightVec_"+histName+", variable);\n"
        text += "       variable = -999;\n"
    if len(varNames) == 2:
        # 2D Histograms
        text += '       std::vector<structHelpFillTwoDimHisto> helpWeightVec_' + histName + ' = {\n'
        # Do Nominal Plot for sure
        text += "           {histos2D[\""+histName+"\"].get()"+", (weight_"+histName+")},\n"
        text += "       };\n"

        text += "       if (!skipWeightSysts) { // append plots for weight systs if neccessary \n"
        for systName, systWeight in zip(systNames[1:], systWeights[1:]):
            text += "             helpWeightVec_" + histName + ".push_back({histos2D[\""+histName+systName+"\"].get()"+", ("+systWeight+")*(weight_"+histName+")});\n"
        text += "       };\n"
            
        text += "       helperFillTwoDimHisto(helpWeightVec_"+histName+", variable1, variable2);\n"
        text += "       variable1 = -999;\n"
        text += "       variable2 = -999;\n"
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
  for(auto& histo1D: histos1D){ outfile->WriteTObject(histo1D.second.get()); }
  for(auto& histo2D: histos2D){ outfile->WriteTObject(histo2D.second.get()); }
  //outfile->Write();

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




