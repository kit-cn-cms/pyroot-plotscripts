# plottingscripts
create/adjust a plottingscript `plotLimits_STR.py`

## Options
- name of the analysis (i.e. workdir name)
`name = 'STR'`
- path to workdir subfolder where all information should be saved
`workdir = pyrootdir + "/workdir/" + name`
- name of the root file 
`rootPathForAnalysis = workdir+'/output_limitInput.root'`
- signal process
`signalProcess = "ttH"`
- Name of final discriminator, should not contain underscore
`discrName = 'finaldiscr'`
- define MEM discriminator variable
`memexp = 'EXPRESSION'`
- define the configs used for the analysis
```python
config          = "pltcfg_STR"
variable_cfg    = "STR_addVariables"
plot_cfg        = "STR_discrPlots"
syst_cfg        = "STR_systematics"
```
- file for rate factors
`rateFactorsFile = "/path/to/file"`
- analysisOptions 
    1. general options
	    - "plotBlinded":         
	    - "testrun":               
	    - "stopAfterCompile":       
    2. options to activate parts of the script
	    - "haddFromWildcard":    
	    - "makeDataCards":       
	    - "addData":                
	    - "drawParallel":         
    3. options for drawParallel/singleExecute sub programs
	    - "makeSimplePlots":      
	    - "makeMCControlPlots":   
	    - "makeEventYields":      
    4. the `skipX` options try to skip the submission of files to the batch system before skipping the output is crosschecked if the output is not complete, the skipped part is done anyways
	    - "skipPlotParallel":     
	    - "skipHaddParallel":     
	    - "skipHaddFromWildcard": 
	    - "skipRenaming":         
	    - "skipDatacards":        
- paths to files
```python
plotJson = "/path/to/json"
plotDataBases = [["memDB","/path/to/mems/",True]] 
memDataBase = "path/to/memCodehandling/"
dnnInterface = {"interfacePath":    pyrootdir+"/util/dNNInterfaces/dNNInterface_Keras_cool.py",
                "checkpointFiles":  "/path/to/CheckpointFiles/"}
```
- path to datacardMaker directory 
`datacardmaker = "/path/to/datacardMaker"`


# prefit/postfit plotting

examplary commands (need a lotta options, sorry)
```
python ../util/PlotScript.py --plotconfig /some/plotconfig/in/workdir/plotconfig.py --channelname "ch1" --rootfile /some/fitdiagnositcs/file/fitDiagnostics.root --directory /path/to/plotscript --workdir ../workdir/testPath --data "data_obs" --ratio "#frac{Data}{Background}" --combineflag "shapes_prefit" --selectionlabel "#scale[0.8]{#splitline{4 jets (pre fit)}{t#bar{t}+H node}}" --combineDatacard /path/to/combined/datacard/combined_datacard.txt

python ../util/PlotScript.py --plotconfig /some/plotconfig/in/workdir/plotconfig.py --channelname "ch1" --rootfile /some/fitdiagnositcs/file/fitDiagnostics.root --directory /path/to/plotscript --workdir ../workdir/testPath --data "data_obs" --ratio "#frac{Data}{S+B}" --combineflag "shapes_fit_s" --selectionlabel "#scale[0.8]{#splitline{4 jets (post fit)}{t#bar{t}+H node}}" --combineDatacard /path/to/combined/datacard/combined_datacard.txt
```
