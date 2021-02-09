
names = ["Weight_pdf_variation_{}".format(x) 
            for x in range(306000, 306101)]
names_alphaS = ["Weight_pdf_variation_{}".format(x) 
            for x in range(306101, 306103)]

names_mcrelic = ["Weight_pdf_variation_{}".format(x)
            for x in range(320900, 321001)]
config = {
    "CMS_ttHbb_PDF" : {
        "to_replace" : "PDF_RELIC",
        "construction" : "Hessian",
        "expand_with" : names,
        "merge_with" : ["CMS_ttHbb_PDF_alphaS"]
    },
    "CMS_ttHbb_PDF_alphaS" : {
        "to_replace" : "PDF_RELIC",
        "construction" : "Hessian",
        "expand_with" : names_alphaS
    },
    "CMS_ttHbb_PDF_tHq" : {
        "to_replace" : "PDF_RELIC",
        "construction" : "Hessian",
        "expand_with" : names,
        "merge_with" : ["CMS_ttHbb_PDF_alphaS_tHq"]
    },
    "CMS_ttHbb_PDF_alphaS_tHq" : {
        "to_replace" : "PDF_RELIC",
        "construction" : "Hessian",
        "expand_with" : names_alphaS
    },
    "CMS_ttHbb_PDF_tHW" : {
        "to_replace" : "PDF_RELIC",
        "construction" : "Hessian",
        "expand_with" : names,
        "merge_with" : ["CMS_ttHbb_PDF_alphaS_tHW"]
    },
    "CMS_ttHbb_PDF_alphaS_tHW" : {
        "to_replace" : "PDF_RELIC",
        "construction" : "Hessian",
        "expand_with" : names_alphaS
    },
    "CMS_ttHbb_PDF_ttbbNLO" : {
        "to_replace" : "PDF_RELIC",
        "construction" : "MCrelic",
        "expand_with" : names_mcrelic,
    },
}