import ROOT

def deriveSFs(analysis, configData, nom_histname_template, syst_histname_template):
    # infile
    infile = ROOT.TFile(analysis.ppRootPath)

    # outfiles
    outfile_path = analysis.workdir+"/SFratios.root"
    outfile = ROOT.TFile(outfile_path, "RECREATE")


    # loop over variables
    for plot in configData.getDiscriminatorPlots():
        channel = plot.name
        # loop over samples
        for sample in configData.samples:
            process = sample.nick

            # get the nominal histogram for that combination
            nom = infile.Get(
                nom_histname_template.replace("$PROCESS", process).replace("$CHANNEL", channel)
                )

            # loop over systematics
            for syst in ["nom"]+configData.allSystNames:
                if "NOMINAL" in syst: continue

                print("calculating SFs for {}, {}, {}".format(channel, process, syst))
                systName = syst
                if syst == "nom": systName = "btag_NOMINAL"

                systHist = infile.Get(
                    syst_histname_template.replace("$PROCESS", process).replace("$CHANNEL", channel).replace("$SYSTEMATIC", systName)
                    )
                ratioHist = nom.Clone()
                ratioHist.Divide(systHist)

                if syst == "nom":
                    nomHist = ratioHist.Clone()
                else:
                    ratioHist.Divide(nomHist)

                outName = "SF_$CHANNEL__$PROCESS__$SYSTEMATIC".replace("$PROCESS", process).replace("$CHANNEL", channel).replace("$SYSTEMATIC", systName)

                #hardcoded shit
                if syst == "nom": outName = outName.replace(systName, "btag_NOMINAL")

                # save ratio hist
                outfile.cd()
                print("writing histogram {}".format(outName))
                ratioHist.Write(outName)

    print("finished creating scale factor file")
    outfile.Close()

