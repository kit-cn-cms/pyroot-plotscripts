# pyroot-plotscripts
:ambulance: ask for help if things are not working :boom:

## Refer to READMEs in the corresponding directories for specific information!
For readability there is a README for each step, if deeper adjustments have to be done:
- [configs](https://github.com/kit-cn-cms/pyroot-plotscripts/tree/ttHLegacyAnalysis/configs/README.md)
- [plottinscripts](https://github.com/kit-cn-cms/pyroot-plotscripts/tree/ttHLegacyAnalysis/plottingscripts/README.md)
- util WIP
- data: not used right now, change structure to have files local
- standaloneTools: files not correlated to the pyroot-plotscript but Karim insists on keeping them

## Package-requirements
- `CMSSW_9_4_9` or newer

## Workflow
### Configs
- create/adjust a plotconfig file named `pltcfg_STR.py`, that includes all samples that shall be used in the pyroot-plotscript and the nominal weight expression. Two lists of Samples 
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
	- create/adjust the nominal weight expression 
	```python
	nominalweight="STR"
	```
- create/adjust a systematics csv file `STR_systematics.csv`, add entries regarding the columns:
	- **Uncertainty** name of the uncertainty, add `#` to skip
	- **Type** type of the uncertainty 
	- **Construction** construction type of the uncertainty, `rate` for `lnN`, `variation` and `weight` for `shape`
	- **Up** add the weight expression or `SAMPLENAME` for the up shape
	- **Down** add the weight expression or `SAMPLENAME` for the down shape
	- **Plot** use `1` to plot uncertainty
	- **PROCESSES** contains at least all processes used in `pltcfg_STR.py`, add `1` to activate shape for specific process

### plottingscripts
create/adjust a plottingscript `plotLimits_STR.py`, define variables and analysis options in the first paragraph of the main function
### Usage
Navigate to the plottinscripts directory and run the plottingscript `plotLimits_STR.py`
```bash
python `plotLimits_STR.py`
```


