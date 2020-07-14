
names = ["Weight_pdf_variation_{}".format(x) 
            for x in range(306000, 306101)]
names_alphaS = ["Weight_pdf_variation_{}".format(x) 
            for x in range(306101, 306103)]

names_mcrelic = ["Weight_pdf_variation_{}".format(x)
            for x in range(320900, 321001)]
config = {
    "pdf" : {
        "to_replace" : "PDF_RELIC",
        "construction" : "Hessian",
        "expand_with" : names,
        "merge_with" : ["pdf_alphaS"]
    },
    "pdf_alphaS" : {
        "to_replace" : "PDF_RELIC",
        "construction" : "Hessian",
        "expand_with" : names_alphaS
    },
    "pdf_ttbbNLO" : {
        "to_replace" : "PDF_RELIC",
        "construction" : "MCrelic",
        "expand_with" : names_mcrelic,
    },
}
