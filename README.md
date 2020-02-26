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
- `export SCRAM_ARCH=slc7_amd64_gcc700`
- `CMSSW_10_6_10`

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

### Cross Evaluation Workflow

- first train separate DNNs with the `DRACO_MLfoy` Framework on the `Odd/Even` subsamples by appending the options `--even` or `--odd` to the execution of the train script (this of course requires a previous preprocessing of `Odd` and `Even` MC events)
- generate a new set of DNNs with the following structure:
```
NAME_OF_DNN_SET
----/DNNS_OF_FIRST_JT_REGION
--------/ODD
------------checkpointfiles
--------/EVEN
------------checkpointfiles
----/DNNS_OF_SECOND_JT_REGION
...
```
- generate a new `plt_config` with the `utils/tools/dNNInterfaces/MLfoyInterface.py` and specify the option `-x` to activate the cross evaluation setup.
Activating this option creates input-feature-plots and output-discriminator-plots for each jet-tag-region by combining the subfolders (`EVEN/ODD`). If the option is not specified when creating the new `plt_config`, separate plots are created for the subfolder checkpoint files.
- add the created config to the `plt_config` variable in your top-level-script.
- check your `config` file and remove the `(Evt_Odd==0)*2.0` selection if it still exists and replace it by `1.0` to select all events and remove the adjusted weight.
- add the variable `Evt_Odd` to your `variable_cfg` if it does not exist yet.
- add the option `crossEvaluation` to your `analysisOptions` dictionary in the top-level-script if it does not exist yet and set it to `True`.
If the option is set to `False` the `c++` code that is written will evaluate all DNNs separately, so you also need a `plt_config` that was not created with the `-x` option.
- set the path to your new DNNSet in the `dnnInterface` dictionary in the top-level-script.
- execute the top-level-script as usual.



### b tagging sf corrections
#### setup for deriving b tagging scale factor patches
- module `util/scaleFactorCreator.py` can be called in a top level script to create SF histograms
- SF are caluclated as ratios between nominal template and dummy systematic templates for each variable and process
- example configs are added in `configs/sfPatch/`
- example scripts are added in `plottingscripts/sfPatch/derive_X.py`

#### new SF histograms
- sf histograms are added to the `data/btagSFCorrection/` directory
- three different binnings are available for each year (which one to use is still to be decided)
- sf histograms are available for all ttbar, ttbb, ttH and ttZ processes

#### setup for applying b tagging scale factor patches
- C++ module `SFCorrectionHelper` has been included
- module is loaded per default into the created C script
- add the following excerpt to the top level script
```
    sfCorrection = {}
    sfCorrection["sfFile"] =  pyrootdir+"/data/btagSFCorrection/sf_2018_deepJet_fineBinning.root"
    # variables for the correction
    sfCorrection["corrections"] = {}
    sfCorrection["corrections"]["HT_vs_NJet"] = ["Evt_HT_jets", "N_Jets"]
    # in root file sf histograms exist with some naming scheme
    sfCorrection["nameTemplate"] = "$BINNING__$PROCESS__$NAME"
    # SF_ is always preprended by default, that should not be changed
    # $BINNING = "_vs_".join(corrections[X])
    # DANGER: order of variables is important
    # name of corrections to be applied (should match whats defined in syst.csv or samples.py)
    sfCorrection["names"] = ["btag_NOMINAL"]
```
- pass information to `plotParallel` via `pP.setSFCorrection(sfCorrection)`
- new SFs can for example be applied by using variables with naming scheme
```
sf__$BINNING__$NAME
```
e.g.
```
sf__HT_vs_NJet__btag_NOMINAL
```

### friend trees

friend trees can be used to get additional variables (i.e. branches) from other root ntuple files. 
Creation of such friend tree files is currently implemented in the `karim` framework for reconstruction information. 
The friend tree files need to have the same order of events as the original ntuple files. In the current implementation it is also required to have the same folder structure for the original ntuple files and the friend tree files:
```
BASEPATH/
----/SAMPLEA/
----/----/FILE1.root
----/----/FILE2.root
----/SAMPLEB/
----/----/FILE3.root
...
```
The current implementation of friend trees replaces the `BASEPATH` of the original ntuple files with a new path where the friend trees are supposed to be stored.
To activate the use add a dictionary to your sample config, e.g.
```
friendTrees = {
	"friendTreeName": "/new/base/path/to/friend/trees/",
	...
	}
```
and add `pP.SetUseFriendTrees(True)` to your top level script.


If the name of a branch you want to access is unique between the friend trees and the original tree, you can just use the variable name.
If the same variable exists in a friend tree and your original tree, the content of the original tree will be accessed when you call the plain variable name. 
To access any variable in a friend tree, you can use the variable name `friendTreeName.variableName`.

