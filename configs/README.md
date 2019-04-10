# Configs
## Plot config
 create/adjust a plotconfig file named `pltcfg_STR.py`, that includes all samples that shall be used in the pyroot-plotscript. Two lists of Samples 
- `samplesDataControlPlots` (data samples)
- `samples` (simulated samples)
add Sample using, with `SAMPLENAMEINCSVCONFIG` being the process name in the used systematics csv file `STR_systematics.csv`
```python
plotClasses.Sample(SAMPLENAMEONPLOTS,COLOR,
    PATH/TO/SAMPLE,
    SELECTION,
    SAMPLENAMEINCSVCONFIG,
    samDict=sampleDict, readTrees=doReadTrees)
```
for example for ttH_hbb
```python
plotClasses.Sample('t#bar{t}H, H to b#bar{b}',ROOT.kBlue+1,
    'path/to/ttHTobb*/*nominal*.root',
    '1.0*41.53*2.0*(Evt_Odd==0)*(Evt_Pt_MET>20.)',
    'ttH_hbb',
    samDict=sampleDict, readTrees=doReadTrees)
```

## Systematic config
create/adjust a systematics csv file `STR_systematics.csv`, **care to use semicolon as seperator!**

add entries regarding the columns:
- **Uncertainty** name of the uncertainty as it is used later for the datacards, uncertainties starting with `#` are skipped
- **Type** type of the uncertainty for the datacards (for example `lnN` or `shape`)
- **Construction** construction type of the uncertainty, 
	- type `lnN` use `rate`
	- type `shape` with calculated weights use `weight`
	- type `shape` with samples use `variation`
- **Up** if construction is `weight`, add the weight expression for the up shape, if the construction is `variation` add the `SAMPLENAME` that gets replaced with the nominal path or absolute `PATH/TO/SAMPLE` for the up shape
- **Down** if construction is `weight`, add the weight expression for the down shape, if the construction is `variation` add the `SAMPLENAME` that gets replaced with the nominal path or absolute `PATH/TO/SAMPLE` for the down shape
- **Plot** use `1` when uncertainty shall be plotted (only for plotting step!)
- **PROCESSES** all processes used in `samples` in `pltcfg_STR.py` need to be defined in the csv file `STR_systematics.csv` (processes in `STR_systematics.csv` that are not defined in `samples` in `pltcfg_STR.py` are skipped) for example `ttH_hbb;ttH_hcc;ttH_hww;ttH_hzz;ttH_htt;ttH_hgg;ttH_hgluglu;ttH_hzg;ttbarOther;ttbarPlusB;ttbarPlus2B;ttbarPlusBBbar;ttbarPlusCCbar`
	- to activate `rate` uncertainties add values for specific processes to be used for the datacards later
	- use `1` to activate `shape` uncertaities for specific processes 
