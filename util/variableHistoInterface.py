class variableHistoInterface(object):


    def __init__(self, **kwargs):
        self.category = kwargs.get("category", "")
        self.varname = kwargs.get("variable_name", "")
        self.category_label = kwargs.get("category_label", "")
        self.nhistobins = kwargs.get("nhistobins", 1)
        self.histotitle = kwargs.get("histotitle", "")
        self.histoname = kwargs.get("histoname", "default_hist")
        self.selection = kwargs.get("selection", "(1.)")
        self.label = kwargs.get("label", "")

        self.minxval = kwargs.get("minxval", None)
        self.maxxval = kwargs.get("maxxval", None)
        self.bin_edges = kwargs.get("bin_edges", None)

    def __str__(self):
        dic = {}
        dic["category"]             = self.category
        dic["varname"]              = self.varname
        dic["catlabel"]             = self.category_label
        dic["nhistobins"]           = self.nhistobins
        dic["histotitle"]           = self.histotitle
        dic["histoname"]            = self.histoname
        dic["plotPreselections"]    = self.selection
        dic["label"]                = self.label
        
        dic["bin_edges"]            = self.bin_edges
        dic["minxval"]              = self.minxval
        dic["maxxval"]              = self.maxxval
        for k in dic:
            print("\t{}\t{}".format(k, dic[k]))

    def getDictionary(self):
        dic = {}
        dic["category"]             = self.category
        dic["varname"]              = self.varname
        dic["catlabel"]             = self.category_label
        dic["nhistobins"]           = self.nhistobins
        dic["histotitle"]           = self.histotitle
        dic["histoname"]            = self.histoname
        dic["plotPreselections"]    = self.selection
        dic["label"]                = self.label
        
        if not self.bin_edges is None:
            dic["bin_edges"]            = self.bin_edges
        elif not (self.minxval is None or self.maxxval is None):
            dic["minxval"]              = self.minxval
            dic["maxxval"]              = self.maxxval
        else:
            print("ERROR: could not load bin edges or min/max val!")
            for k in dic:
                print("\t{}\t{}".format(k, dic[k]))
            raise ValueError
        return dic
