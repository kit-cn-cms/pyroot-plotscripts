import csv 
import pandas

def ReadMEandPDFNormalizations(csv_file):
        mydict = {}
        data = pandas.read_csv(csv_file)
        data["sample_name_modified"] = pandas.Series(
            (x.split("/")[1].replace("_", "").replace("-", "") for x in data.name.values), 
            index = data.index)
        for index in range(len(data.weight.values)):
            mydict[ (data.sample_name_modified[index],
                        data.weight[index]) ] = data.factor[index]
        
        return mydict

def GetMEPDFadditionalVariablesList(csv_file):
        mydict = ReadMEandPDFNormalizations(csv_file)
        seen = set()
        weight_vars_list = []
        for key in mydict:
            if not key[1] in seen:
                seen.add(key[1])
                weight_vars_list.append(key[1])
        return weight_vars_list

def GetPDFadditionalVariablesList(csv_file):
        weight_list = GetMEPDFadditionalVariablesList(csv_file)
        pdf_weight_list = []
        for weight in weight_list:
            if "pdf" in weight:
                pdf_weight_list.append(weight)
        return pdf_weight_list

