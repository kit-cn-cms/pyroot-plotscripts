import csv 
import pandas


def ReadMEandPDFNormalizations(csv_file):
        mydict={}
        data = pandas.read_csv(csv_file)
        data["sample_name_modified"] = pandas.Series(
            (x.split("/")[1].replace("_","").replace("-","") for x in data.name.values), 
            index = data.index)
        for index in range(len(data.weight.values)):
            mydict[ (data.sample_name_modified[index],
                        data.weight[index]) ] = data.factor[index]
        
        return mydict

def AddMEandPDFNormalizationsMap(csv_file):
        mydict=ReadMEandPDFNormalizations(csv_file)
        code='std::map<TString,float> MEPDF_Norm_Map;\n'
        for key in mydict:
                code+='MEPDF_Norm_Map["'+key[0]+'_'+key[1]+'"]='+mydict[key]+';\n'
        return code

def GetMEPDFadditionalVariablesList(csv_file):
        mydict=ReadMEandPDFNormalizations(csv_file)
        seen = set()
        weight_vars_list=[]
        for key in mydict:
                if not key[1] in seen:
                        seen.add(key[1])
                        weight_vars_list.append(key[1])
        return weight_vars_list

def RelateMEPDFMapToNormFactor(csv_file):
        weight_list=GetMEPDFadditionalVariablesList(csv_file)
        code=''
        code+="""
    TString currentRelevantSampleNameForMEPDF=sampleDataBaseIdentifiers[currentfilename];
    TString translatedCurrentRelevantSampleNameForMEPDF=sampleTranslationMapCPP[currentRelevantSampleNameForMEPDF];
    //std::cout<<"MEPDF relation "<<currentfilename<<" "<<currentRelevantSampleNameForMEPDF<<" "<<translatedCurrentRelevantSampleNameForMEPDF<<std::endl;
  """
        code+='if(MEPDF_Norm_Map.find('+'translatedCurrentRelevantSampleNameForMEPDF'+'+"_'+weight_list[0]+'")!=MEPDF_Norm_Map.end()){;\n'
        for weight in weight_list:
                code+='internalNormFactor_'+weight+'='+'MEPDF_Norm_Map['+'translatedCurrentRelevantSampleNameForMEPDF'+'+"_'+weight+'"];\n'
        code+='}\n'
        code+='//else{std::cout<<"did not find pdf weights in map "<<translatedCurrentRelevantSampleNameForMEPDF<<std::endl;}\n'
        code+='//std::cout<<"first internal pdf weight "<<'+'translatedCurrentRelevantSampleNameForMEPDF'+'+"_'+weight_list[0]+'" <<" "<< internalNormFactor_'+weight_list[0]+'<<std::endl;\n'
        return code


def GetMEPDFVetoList(csv_file):
        weight_list=GetMEPDFadditionalVariablesList(csv_file)
        weight_veto_list=[]
        for weight in weight_list:
                weight_veto_list.append('internalNormFactor_'+weight)
        return weight_veto_list


def DeclareMEPDFNormFactors(csv_file):
        code=''
        weight_list=GetMEPDFadditionalVariablesList(csv_file)
        for weight in weight_list:
                code+='float internalNormFactor_'+weight+'=0.0;\n'
        return code
def ResetMEPDFNormFactors(csv_file):
        code=''
        weight_list=GetMEPDFadditionalVariablesList(csv_file)
        for weight in weight_list:
                code+='internalNormFactor_'+weight+'=0.0;\n'
        return code

def GetPDFadditionalVariablesList(csv_file):
        weight_list=GetMEPDFadditionalVariablesList(csv_file)
        pdf_weight_list=[]
        for weight in weight_list:
                if "pdf" in weight:
                        pdf_weight_list.append(weight)
        return pdf_weight_list

def PutPDFWeightsinVector(csv_file):
        pdf_weights=GetPDFadditionalVariablesList(csv_file)
        code='std::vector<double> pdf_weights;\n'
        code+='pdf_weights.push_back(1.);\n'
        for weight in pdf_weights:
                code+='pdf_weights.push_back(internalNormFactor_'+weight+'*'+weight+');\n'
        return code

def DefineLHAPDF():
    code='LHAPDF::PDFSet pdfSet("NNPDF30_nlo_as_0118");\n'
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

