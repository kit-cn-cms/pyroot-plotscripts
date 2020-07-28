def construct_variations(weight_names, selection_dict, nom_weight, expression_template):
    variationdict = {}
    for keyword in weight_names:
        for current_process in selection_dict:
            key = "".join([keyword, current_process.upper()])
            weight_list = []
            final_weight = "" 
            for p in selection_dict:
                s = ""
                # print(weight_names[keyword])
                subdict = selection_dict[p]
                sel = subdict["selection"].format(weight = weight_names[keyword], 
                                                    nom_weight = nom_weight)
                phasespace_frac = subdict["phasespace_frac"].format(weight = weight_names[keyword], 
                                                                    nom_weight = nom_weight,
                                                                    current_process = current_process)
                weight_norm = expression_template.format(weight = weight_names[keyword], 
                                                        nom_weight = nom_weight)
                if p == current_process:
                    s = "*".join([sel, weight_norm])
                else:
                    s = "*".join([sel, phasespace_frac])
                # print("\t{} : {}".format(key, s))
                # s.format(weight = weight_names[keyword], nom_weight = nom_weight)
                weight_list.append(s)
            final_weight = " + ".join(weight_list)
            # final_weight.format(weight = weight_names[keyword], nom_weight = nom_weight)
            variationdict[key] = final_weight
    # print(variationdict)
    return variationdict

def main():
    weightReplacements = {}
    variations = "UP DOWN".split()
    # do ISR/FSR uncertainties. These are split for all three tt+X classes, so
    # calculating the corrections depends on the exact flavor of the additional
    # jets
    weight_names = {
        "".join([u.upper(),var.upper()]) : "GenWeight_{}_Def_{}".format(u.lower(), var.lower()) \
            for u in "ISR FSR".split() for var in variations
    }

    expression_template = """({weight}*internalNormFactors.at("{weight}"))"""
    nom_weight = "Weight_scale_variation_muR_1p0_muF_1p0"

    selection_dict = {
        "ttbb": {
            "selection": "((GenEvt_I_TTPlusBB==1)||(GenEvt_I_TTPlusBB==2)||(GenEvt_I_TTPlusBB==3))",
            "phasespace_frac" : """((1. - fractions_{current_process}.at("{weight}"))/(1 - fractions_{current_process}.at("{nom_weight}")))"""
            },
        "ttcc": {
            "selection": "(GenEvt_I_TTPlusCC==1)",
            "phasespace_frac" : """((1. - fractions_{current_process}.at("{weight}"))/(1 - fractions_{current_process}.at("{nom_weight}")))"""
            },
        "ttlf": {
            "selection": "(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)",
            "phasespace_frac" : """((1. - fractions_{current_process}.at("{weight}"))/(1 - fractions_{current_process}.at("{nom_weight}")))"""
            }
    }

    variationdict = construct_variations(weight_names = weight_names, 
                                            selection_dict = selection_dict, 
                                            nom_weight = nom_weight,
                                            expression_template = expression_template)
    weightReplacements.update(variationdict)

    # do muR/F uncertainties. These uncertainties are split according to the
    # heavy flavor contribution of the jets (b-jets vs non-b-jets)
    weight_names = {}
    muRF_templates = {
        "".join(["MUR", var.upper()]) : "Weight_scale_variation_muR_{}_muF_1p0".format(val) \
            for var, val in zip(variations, "2p0 0p5".split())
    }
    weight_names.update(muRF_templates)
    muRF_templates = {
        "".join(["MUF", var.upper()]) : "Weight_scale_variation_muR_1p0_muF_{}".format(val) \
            for var, val in zip(variations, "2p0 0p5".split())
    }
    weight_names.update(muRF_templates)


    selection_dict = {
        "ttbb": {
            "selection": "((GenEvt_I_TTPlusBB==1)||(GenEvt_I_TTPlusBB==2)||(GenEvt_I_TTPlusBB==3))",
            "phasespace_frac" : """(fractions_ttbb.at("{weight}")/fractions_ttbb.at("{nom_weight}"))"""
            },
        "ttnonbb": {
            "selection": "(GenEvt_I_TTPlusBB==0)",
            "phasespace_frac" : """((1. - fractions_ttbb.at("{weight}"))/(1 - fractions_ttbb.at("{nom_weight}")))"""
            },
    }
    variationdict = construct_variations(weight_names = weight_names, 
                                            selection_dict = selection_dict, 
                                            nom_weight = nom_weight,
                                            expression_template = expression_template)
    weightReplacements.update(variationdict)

    # do PDF uncertainty. Same as muR/F, but has to be handled separately because the
    # weight expression is different and there is only one variation
    weight_names = {}
    weight_names["PDF"] = """PDF_RELIC"""
    expression_template = """(fmax(0, {weight})*internalNormFactors.at("{weight}"))"""
    variationdict = construct_variations(weight_names = weight_names, 
                                            selection_dict = selection_dict, 
                                            nom_weight = nom_weight,
                                            expression_template = expression_template)
    weightReplacements.update(variationdict)
    return weightReplacements

if __name__ == "__main__":
    main()