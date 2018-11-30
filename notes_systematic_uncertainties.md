# Scale Uncertainties

Recommendation: 
```
QCDscale_<X> for uncertainties on inclusive cross-sections, where <X> is ggH, qqH, VH (for WH, ZH), ttH, V (for W,Z), VV (for WW/WZ/ZZ), ggVV (for ggWW, ggZZ), ttbar (for ttbar, single top)
```
- ggH -> not relevant
- qqH -> not relevant
- VH -> not relevant
- ttH -> correct in our setup
- V -> correct
- VV -> correct
- ggVV -> not relevant
- **ttbar -> FIXME: currently, ttbar and single top are treated separately! Change?**

# PDF Uncertainties

Recommendation: 
```
PDF uncertainties: pdf_gg for gluon induced, pdf_qqbar for quark-induced (including qq processes like qqH), pdf_qg.
Signal PDF uncertainties: For the signal processes, the PDF uncertainties should contain the work Higgs in them as follows, pdf_Higgs_qqbar, pdf_Higgs_gg, pdf_Higgs_qg and for the ttH process, pdf_Higgs_ttH
```
- checks all out

# CMS Common Uncertainties

## Luminosity

Recommendation: 
```
luminosity should be called lumi_7TeV, lumi_8TeV or lumi_13TeV
```
- **current naming scheme includes year at the end -> drop**

## Efficiencies

Recommendation: 
```
efficiencies should be called CMS_eff_<x> where x = e, m, t, g, j, b for electrons, muons, hadronic taus, photons, jets and b-tagging (note that if you have a b-veto the kappa for CMS_eff_b associated to a process with real b jets should be < 1).
If you are using some significantly different objects or methods to determine the efficiencies from the rest of the CMS analyses, you may want to use a different name.
Include trigger efficiencies inside this term as well.
```
- **currently, trigger efficiencies are decorrelated from other efficiencies -> change?**
- **not using jet efficiencies?**
- unclear from TWiki how to name split uncertainties for SL and DL (probably didn't change?)

## Energy Scale

Recommendation:
```
energy scale should be called CMS_scale_<x> where x = e, m, t, g, j, met(, b) for electrons, muons, hadronic taus, photons, jets, missing energy (and b-jets if you have something specific for those).
The convention is that a positive value of the nuisance parameter corresponds to shift of the energy scale upwards.
```
- only using energy scale uncertainties for jets
- currently, the different sources for JES are split (probably ok though)

## Energy Resolution

Recommendation:
```
energy resolution should be called CMS_res_<x> where x = e, m, t, g, j, met(, b) for electrons, muons, hadronic taus, photons, jets, missing energy (and b-jets if you have something specific for those).
The convention is that a positive value of the nuisance parameter corresponds to a degradation of the energy resolution, while a negative value corresponds to an improvement. 
```
- only using energy resoltuion uncertainties for jets
- naming checks out

## Btag

Recommendation:
```
if you are using the iterativeFit method with the CSVv2 algorithm, each source should be called CMS_btag_<x> where x corresponds to the name of the source in the B-Pog .csv file (x = jes, lf, hf, lfstats1, lfstats2, hfstats1, hfstats2, cferr1, cferr2). 
```
- **not using jes source?**
- rest checks out

## Side Note

 If your analysis strongly constraints any of these uncertainties, please report this: the assumption that keeping things correlated is conservative does not apply in that case, and so it should be discussed if the constraint is legitimate also outside the boundaries of your analysis.

For each of these uncertainties (e.g. electron efficiency), you should evaluate and report the effect as follows:

    1. Compute κUP: shift that parameter up by 1 σ compute the expected yields, and divide them by the nominal yields.
    2. Compute κDOWN: shift that parameter down by 1 σ compute the expected yields, and divide them by the nominal yields.
    3. If the effect is approximately symmetric, then κUP * κDOWN is close to 1. Then you should put just κUP in the datacard (or can take geometric average of the two: κ = sqrt( κUP / κDOWN )).
    4. If instead the effect is significantly asymmetric, put in the datacard the two κ's separated by a slash: κDOWN/κUP 

# Analysis Specific Uncertainties

Recommendation:
```
Uncertainties specific for your particular analysis should have a double-prefix: CMS_<analysis id>_ where the analysis ids are the ones that go into the datacard names.
``` 
- PS uncertainties (UE, ISR, FSR, HDAMP) follow this convention
- **bgnorm uncertainties should probably also follow this (e.g. `bgnorm_ttbarPlusBBbar` -> `CMS_ttHbb_bgnorm_ttbarPlusBBbar`)**