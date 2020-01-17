def getAddVars():
    addVars = [
        "Jet_Pt",
        "Muon_Pt",
        "Electron_Pt",
        "Jet_Eta",
        "Muon_Eta",
        "Electron_Eta",
        "Muon_Pt_BeForeRC",
        "Electron_Pt_BeforeRun2Calibration",
        "Electron_Eta_Supercluster",
        "Jet_CSV",
        "Jet_Flav",
        "N_Jets",
        "Jet_E",
        "Jet_Phi",
        "Jet_M",
        "Evt_Pt_PrimaryLepton:=LooseLepton_Pt[0]",
        "Evt_E_PrimaryLepton:=LooseLepton_E[0]",
        "Evt_M_PrimaryLepton:=LooseLepton_M[0]",
        "Evt_Phi_PrimaryLepton:=LooseLepton_Phi[0]",
        "Evt_Eta_PrimaryLepton:=LooseLepton_Eta[0]",
        "Evt_MET_Pt",
        "Weight_CSV",
        "Weight_CSVLFup",
        "Weight_CSVLFdown",
        "Weight_CSVHFup",
        "Weight_CSVHFdown",
        "Weight_CSVHFStats1up",
        "Weight_CSVHFStats1down",
        "Weight_CSVLFStats1down",
        "Weight_CSVHFStats2up",
        "Weight_CSVHFStats2down",
        "Weight_CSVLFStats2up",
        "Weight_CSVLFStats2down",
        "Weight_CSVCErr1down",
        "Weight_CSVCErr2up",
        "Weight_CSVCErr2down",
        # "Evt_blr_ETH",
        # "Evt_blr_ETH_transformed",
        #################
        # NJet weights ##
        #################a

        "selection_hbb:=((abs(GenHiggs_DecProd1_PDGID)==5 && abs(GenHiggs_DecProd2_PDGID)==5))",
        "selection_nonhbb:=((abs(GenHiggs_DecProd1_PDGID)!=5 && abs(GenHiggs_DecProd2_PDGID)!=5))",
        "selection_ttsl:=(N_GenTopLep==1)",
        "selection_ttdl:=(N_GenTopLep==2)",
        "selection_ttfh:=(N_GenTopLep==0)",

        "selection_ttbb:=(GenEvt_I_TTPlusBB==3&&GenEvt_I_TTPlusCC==0)",
        "selection_ttb:=(GenEvt_I_TTPlusBB==1&&GenEvt_I_TTPlusCC==0)",
        "selection_tt2b:=(GenEvt_I_TTPlusBB==2&&GenEvt_I_TTPlusCC==0)",
        "selection_ttcc:=(GenEvt_I_TTPlusBB==1&&GenEvt_I_TTPlusCC==1)",
        "selection_ttlf:=(GenEvt_I_TTPlusBB==0&&GenEvt_I_TTPlusCC==0)",




        "weight_SF_N_Jets__ttH_bb__btag_LPURITYUp:=(((N_Jets==4)*0.97704654932)+((N_Jets==5)*0.974404811859)+((N_Jets==6)*0.971823453903)+((N_Jets==7)*0.968964576721)+((N_Jets==8)*0.968566417694)+((N_Jets>=9)*0.969218075275))",
        "weight_SF_N_Jets__ttH_bb__btag_LPURITYDown:=(((N_Jets==4)*1.02426421642)+((N_Jets==5)*1.02713978291)+((N_Jets==6)*1.02994823456)+((N_Jets==7)*1.03301882744)+((N_Jets==8)*1.03326332569)+((N_Jets>=9)*1.03224790096))",
        "weight_SF_N_Jets__ttH_bb__btag_BPURITYUp:=(((N_Jets==4)*1.00322639942)+((N_Jets==5)*1.00243258476)+((N_Jets==6)*1.00166034698)+((N_Jets==7)*1.00032806396)+((N_Jets==8)*0.999964058399)+((N_Jets>=9)*0.998906612396))",
        "weight_SF_N_Jets__ttH_bb__btag_BPURITYDown:=(((N_Jets==4)*0.997583150864)+((N_Jets==5)*0.998395144939)+((N_Jets==6)*0.999182522297)+((N_Jets==7)*1.00059020519)+((N_Jets==8)*1.00069236755)+((N_Jets>=9)*1.00142419338))",
        "weight_SF_N_Jets__ttH_bb__btag_BSTAT1Up:=(((N_Jets==4)*1.00448966026)+((N_Jets==5)*1.00493991375)+((N_Jets==6)*1.00541687012)+((N_Jets==7)*1.0059441328)+((N_Jets==8)*1.00608229637)+((N_Jets>=9)*1.00572168827))",
        "weight_SF_N_Jets__ttH_bb__btag_BSTAT1Down:=(((N_Jets==4)*0.996165812016)+((N_Jets==5)*0.995708167553)+((N_Jets==6)*0.995288610458)+((N_Jets==7)*0.994715690613)+((N_Jets==8)*0.994407534599)+((N_Jets>=9)*0.99451482296))",
        "weight_SF_N_Jets__ttH_bb__btag_LSTAT1Up:=(((N_Jets==4)*0.998648166656)+((N_Jets==5)*0.998672246933)+((N_Jets==6)*0.998661458492)+((N_Jets==7)*0.998542487621)+((N_Jets==8)*0.998662531376)+((N_Jets>=9)*0.998511731625))",
        "weight_SF_N_Jets__ttH_bb__btag_LSTAT1Down:=(((N_Jets==4)*1.001937747)+((N_Jets==5)*1.00188755989)+((N_Jets==6)*1.00195598602)+((N_Jets==7)*1.00203335285)+((N_Jets==8)*1.00173699856)+((N_Jets>=9)*1.00164818764))",
        "weight_SF_N_Jets__ttH_bb__btag_BSTAT2Up:=(((N_Jets==4)*1.00106143951)+((N_Jets==5)*1.00100421906)+((N_Jets==6)*1.00091278553)+((N_Jets==7)*1.00092446804)+((N_Jets==8)*1.00067424774)+((N_Jets>=9)*1.00079905987))",
        "weight_SF_N_Jets__ttH_bb__btag_BSTAT2Down:=(((N_Jets==4)*0.99953430891)+((N_Jets==5)*0.999561548233)+((N_Jets==6)*0.999716520309)+((N_Jets==7)*0.999664604664)+((N_Jets==8)*0.999747574329)+((N_Jets>=9)*0.99936902523))",
        "weight_SF_N_Jets__ttH_bb__btag_LSTAT2Up:=(((N_Jets==4)*0.999268352985)+((N_Jets==5)*0.999164819717)+((N_Jets==6)*0.999050736427)+((N_Jets==7)*0.998733699322)+((N_Jets==8)*0.998766422272)+((N_Jets>=9)*0.998422384262))",
        "weight_SF_N_Jets__ttH_bb__btag_LSTAT2Down:=(((N_Jets==4)*1.00132966042)+((N_Jets==5)*1.00140619278)+((N_Jets==6)*1.00157940388)+((N_Jets==7)*1.00185167789)+((N_Jets==8)*1.0016450882)+((N_Jets>=9)*1.00175869465))",
        "weight_SF_N_Jets__ttH_bb__btag_CERR1Up:=(((N_Jets==4)*1.00239014626)+((N_Jets==5)*1.00256240368)+((N_Jets==6)*1.0027692318)+((N_Jets==7)*1.00402128696)+((N_Jets==8)*1.0054217577)+((N_Jets>=9)*1.00741255283))",
        "weight_SF_N_Jets__ttH_bb__btag_CERR1Down:=(((N_Jets==4)*0.995995104313)+((N_Jets==5)*0.99593091011)+((N_Jets==6)*0.995648741722)+((N_Jets==7)*0.993190169334)+((N_Jets==8)*0.99077129364)+((N_Jets>=9)*0.986788988113))",
        "weight_SF_N_Jets__ttH_bb__btag_CERR2Up:=(((N_Jets==4)*1.00201332569)+((N_Jets==5)*1.00231838226)+((N_Jets==6)*1.00256145)+((N_Jets==7)*1.00374472141)+((N_Jets==8)*1.00486588478)+((N_Jets>=9)*1.0057374239))",
        "weight_SF_N_Jets__ttH_bb__btag_CERR2Down:=(((N_Jets==4)*0.997330725193)+((N_Jets==5)*0.997073113918)+((N_Jets==6)*0.996824622154)+((N_Jets==7)*0.99498462677)+((N_Jets==8)*0.993439018726)+((N_Jets>=9)*0.991924464703))",
        "weight_SF_N_Jets__ttH_bb__btag_NOMINAL:=(((N_Jets==4)*0.958406329155)+((N_Jets==5)*0.946640312672)+((N_Jets==6)*0.928485929966)+((N_Jets==7)*0.913526296616)+((N_Jets==8)*0.886205792427)+((N_Jets>=9)*0.82247453928))",

        "weight_SF_N_Jets__ttH_nonbb__btag_LPURITYUp:=(((N_Jets==4)*0.989624023438)+((N_Jets==5)*0.988555550575)+((N_Jets==6)*0.988110482693)+((N_Jets==7)*0.987289369106)+((N_Jets==8)*0.985683083534)+((N_Jets>=9)*0.98507642746))",
        "weight_SF_N_Jets__ttH_nonbb__btag_LPURITYDown:=(((N_Jets==4)*1.01072525978)+((N_Jets==5)*1.0121254921)+((N_Jets==6)*1.01263189316)+((N_Jets==7)*1.01297605038)+((N_Jets==8)*1.01457071304)+((N_Jets>=9)*1.01542270184))",
        "weight_SF_N_Jets__ttH_nonbb__btag_BPURITYUp:=(((N_Jets==4)*1.0073735714)+((N_Jets==5)*1.00718891621)+((N_Jets==6)*1.00710070133)+((N_Jets==7)*1.0052396059)+((N_Jets==8)*1.00490379333)+((N_Jets>=9)*1.0030618906))",
        "weight_SF_N_Jets__ttH_nonbb__btag_BPURITYDown:=(((N_Jets==4)*0.993204474449)+((N_Jets==5)*0.993579864502)+((N_Jets==6)*0.993803799152)+((N_Jets==7)*0.99527990818)+((N_Jets==8)*0.995334625244)+((N_Jets>=9)*0.997490823269))",
        "weight_SF_N_Jets__ttH_nonbb__btag_BSTAT1Up:=(((N_Jets==4)*1.00189709663)+((N_Jets==5)*1.00235295296)+((N_Jets==6)*1.00239825249)+((N_Jets==7)*1.00227093697)+((N_Jets==8)*1.00254642963)+((N_Jets>=9)*1.00268447399))",
        "weight_SF_N_Jets__ttH_nonbb__btag_BSTAT1Down:=(((N_Jets==4)*0.998318850994)+((N_Jets==5)*0.998098492622)+((N_Jets==6)*0.998007118702)+((N_Jets==7)*0.997717797756)+((N_Jets==8)*0.997316718102)+((N_Jets>=9)*0.997423291206))",
        "weight_SF_N_Jets__ttH_nonbb__btag_LSTAT1Up:=(((N_Jets==4)*0.999947965145)+((N_Jets==5)*1.00025367737)+((N_Jets==6)*1.00034582615)+((N_Jets==7)*1.00024950504)+((N_Jets==8)*1.00021350384)+((N_Jets>=9)*1.00014328957))",
        "weight_SF_N_Jets__ttH_nonbb__btag_LSTAT1Down:=(((N_Jets==4)*1.00025391579)+((N_Jets==5)*1.00017499924)+((N_Jets==6)*1.00002527237)+((N_Jets==7)*0.99968034029)+((N_Jets==8)*0.999593734741)+((N_Jets>=9)*0.999891996384))",
        "weight_SF_N_Jets__ttH_nonbb__btag_BSTAT2Up:=(((N_Jets==4)*1.00068330765)+((N_Jets==5)*1.00072598457)+((N_Jets==6)*1.00070059299)+((N_Jets==7)*1.00046551228)+((N_Jets==8)*1.00035405159)+((N_Jets>=9)*1.0007392168))",
        "weight_SF_N_Jets__ttH_nonbb__btag_BSTAT2Down:=(((N_Jets==4)*0.999570310116)+((N_Jets==5)*0.999769866467)+((N_Jets==6)*0.999735355377)+((N_Jets==7)*0.999528944492)+((N_Jets==8)*0.999486088753)+((N_Jets>=9)*0.999338328838))",
        "weight_SF_N_Jets__ttH_nonbb__btag_LSTAT2Up:=(((N_Jets==4)*1.00079834461)+((N_Jets==5)*1.00098323822)+((N_Jets==6)*1.00099205971)+((N_Jets==7)*1.00063228607)+((N_Jets==8)*1.00048279762)+((N_Jets>=9)*1.00020313263))",
        "weight_SF_N_Jets__ttH_nonbb__btag_LSTAT2Down:=(((N_Jets==4)*0.999395370483)+((N_Jets==5)*0.999442219734)+((N_Jets==6)*0.999371111393)+((N_Jets==7)*0.999305725098)+((N_Jets==8)*0.999317228794)+((N_Jets>=9)*0.999855279922))",
        "weight_SF_N_Jets__ttH_nonbb__btag_CERR1Up:=(((N_Jets==4)*1.00488007069)+((N_Jets==5)*1.00657355785)+((N_Jets==6)*1.00628149509)+((N_Jets==7)*1.00745534897)+((N_Jets==8)*1.0111758709)+((N_Jets>=9)*1.01100695133))",
        "weight_SF_N_Jets__ttH_nonbb__btag_CERR1Down:=(((N_Jets==4)*0.991528213024)+((N_Jets==5)*0.988684535027)+((N_Jets==6)*0.989199578762)+((N_Jets==7)*0.986681222916)+((N_Jets==8)*0.980229914188)+((N_Jets>=9)*0.981528997421))",
        "weight_SF_N_Jets__ttH_nonbb__btag_CERR2Up:=(((N_Jets==4)*1.00442051888)+((N_Jets==5)*1.00601041317)+((N_Jets==6)*1.00592243671)+((N_Jets==7)*1.00699841976)+((N_Jets==8)*1.01038396358)+((N_Jets>=9)*1.01001775265))",
        "weight_SF_N_Jets__ttH_nonbb__btag_CERR2Down:=(((N_Jets==4)*0.993878543377)+((N_Jets==5)*0.991850376129)+((N_Jets==6)*0.991990029812)+((N_Jets==7)*0.990059196949)+((N_Jets==8)*0.98534655571)+((N_Jets>=9)*0.986341834068))",
        "weight_SF_N_Jets__ttH_nonbb__btag_NOMINAL:=(((N_Jets==4)*0.907583355904)+((N_Jets==5)*0.887570559978)+((N_Jets==6)*0.863608837128)+((N_Jets==7)*0.838708817959)+((N_Jets==8)*0.810989439487)+((N_Jets>=9)*0.761805832386))",

        "weight_SF_N_Jets__ttbb_4FS_SL__btag_LPURITYUp:=(((N_Jets==4)*0.997833371162)+((N_Jets==5)*0.9932320714)+((N_Jets==6)*0.987049102783)+((N_Jets==7)*0.98428940773)+((N_Jets==8)*0.984614014626)+((N_Jets>=9)*0.984805762768))",
        "weight_SF_N_Jets__ttbb_4FS_SL__btag_LPURITYDown:=(((N_Jets==4)*1.0022881031)+((N_Jets==5)*1.00667917728)+((N_Jets==6)*1.01337254047)+((N_Jets==7)*1.01582682133)+((N_Jets==8)*1.01616966724)+((N_Jets>=9)*1.01426386833))",
        "weight_SF_N_Jets__ttbb_4FS_SL__btag_BPURITYUp:=(((N_Jets==4)*1.00251722336)+((N_Jets==5)*1.00224971771)+((N_Jets==6)*1.00247967243)+((N_Jets==7)*1.00564849377)+((N_Jets==8)*1.00400280952)+((N_Jets>=9)*1.00711739063))",
        "weight_SF_N_Jets__ttbb_4FS_SL__btag_BPURITYDown:=(((N_Jets==4)*0.997745275497)+((N_Jets==5)*0.997823655605)+((N_Jets==6)*0.997611999512)+((N_Jets==7)*0.994773626328)+((N_Jets==8)*0.996126413345)+((N_Jets>=9)*0.994120299816))",
        "weight_SF_N_Jets__ttbb_4FS_SL__btag_BSTAT1Up:=(((N_Jets==4)*1.00077664852)+((N_Jets==5)*1.00161683559)+((N_Jets==6)*1.00236999989)+((N_Jets==7)*1.00295996666)+((N_Jets==8)*1.00294911861)+((N_Jets>=9)*1.00301301479))",
        "weight_SF_N_Jets__ttbb_4FS_SL__btag_BSTAT1Down:=(((N_Jets==4)*0.999271869659)+((N_Jets==5)*0.998400866985)+((N_Jets==6)*0.997702658176)+((N_Jets==7)*0.997080862522)+((N_Jets==8)*0.997089982033)+((N_Jets>=9)*0.996983170509))",
        "weight_SF_N_Jets__ttbb_4FS_SL__btag_LSTAT1Up:=(((N_Jets==4)*1.000451684)+((N_Jets==5)*1.00015366077)+((N_Jets==6)*0.999746859074)+((N_Jets==7)*0.999468326569)+((N_Jets==8)*0.999548375607)+((N_Jets>=9)*0.999243974686))",
        "weight_SF_N_Jets__ttbb_4FS_SL__btag_LSTAT1Down:=(((N_Jets==4)*0.999539315701)+((N_Jets==5)*0.999829590321)+((N_Jets==6)*1.00025117397)+((N_Jets==7)*1.00048613548)+((N_Jets==8)*1.00040853024)+((N_Jets>=9)*1.00071310997))",
        "weight_SF_N_Jets__ttbb_4FS_SL__btag_BSTAT2Up:=(((N_Jets==4)*0.999933362007)+((N_Jets==5)*0.999954223633)+((N_Jets==6)*1.00016582012)+((N_Jets==7)*1.0005428791)+((N_Jets==8)*1.00051665306)+((N_Jets>=9)*1.00031459332))",
        "weight_SF_N_Jets__ttbb_4FS_SL__btag_BSTAT2Down:=(((N_Jets==4)*1.00011348724)+((N_Jets==5)*1.00006246567)+((N_Jets==6)*0.999874174595)+((N_Jets==7)*0.99948734045)+((N_Jets==8)*0.99947398901)+((N_Jets>=9)*0.99966442585))",
        "weight_SF_N_Jets__ttbb_4FS_SL__btag_LSTAT2Up:=(((N_Jets==4)*1.00063705444)+((N_Jets==5)*1.00041472912)+((N_Jets==6)*1.00012803078)+((N_Jets==7)*1.00011765957)+((N_Jets==8)*1.0000834465)+((N_Jets>=9)*0.999728560448))",
        "weight_SF_N_Jets__ttbb_4FS_SL__btag_LSTAT2Down:=(((N_Jets==4)*0.99938595295)+((N_Jets==5)*0.999570548534)+((N_Jets==6)*0.999880313873)+((N_Jets==7)*0.999871253967)+((N_Jets==8)*0.999907016754)+((N_Jets>=9)*1.00022900105))",
        "weight_SF_N_Jets__ttbb_4FS_SL__btag_CERR1Up:=(((N_Jets==4)*1.0009636879)+((N_Jets==5)*1.00088775158)+((N_Jets==6)*1.00266683102)+((N_Jets==7)*1.00068259239)+((N_Jets==8)*1.00344336033)+((N_Jets>=9)*1.00783312321))",
        "weight_SF_N_Jets__ttbb_4FS_SL__btag_CERR1Down:=(((N_Jets==4)*0.998155653477)+((N_Jets==5)*0.998128771782)+((N_Jets==6)*0.994954288006)+((N_Jets==7)*0.998856127262)+((N_Jets==8)*0.992983818054)+((N_Jets>=9)*0.986805021763))",
        "weight_SF_N_Jets__ttbb_4FS_SL__btag_CERR2Up:=(((N_Jets==4)*1.00091457367)+((N_Jets==5)*1.00087964535)+((N_Jets==6)*1.00241136551)+((N_Jets==7)*1.00070226192)+((N_Jets==8)*1.00320577621)+((N_Jets>=9)*1.00664460659))",
        "weight_SF_N_Jets__ttbb_4FS_SL__btag_CERR2Down:=(((N_Jets==4)*0.998669803143)+((N_Jets==5)*0.998602926731)+((N_Jets==6)*0.996476650238)+((N_Jets==7)*0.999083936214)+((N_Jets==8)*0.994816064835)+((N_Jets>=9)*0.990965366364))",
        "weight_SF_N_Jets__ttbb_4FS_SL__btag_NOMINAL:=(((N_Jets==4)*0.918195545673)+((N_Jets==5)*0.90467607975)+((N_Jets==6)*0.883087515831)+((N_Jets==7)*0.835724651814)+((N_Jets==8)*0.811563551426)+((N_Jets>=9)*0.737140059471))",

        "weight_SF_N_Jets__ttbb_4FS_DL__btag_LPURITYUp:=(((N_Jets==4)*0.985685348511)+((N_Jets==5)*0.980274558067)+((N_Jets==6)*0.978751122952)+((N_Jets==7)*0.983207941055)+((N_Jets==8)*0.979501724243)+((N_Jets>=9)*0.98046118021))",
        "weight_SF_N_Jets__ttbb_4FS_DL__btag_LPURITYDown:=(((N_Jets==4)*1.01467049122)+((N_Jets==5)*1.02006220818)+((N_Jets==6)*1.02198636532)+((N_Jets==7)*1.01652169228)+((N_Jets==8)*1.02184677124)+((N_Jets>=9)*1.02084362507))",
        "weight_SF_N_Jets__ttbb_4FS_DL__btag_BPURITYUp:=(((N_Jets==4)*1.00845050812)+((N_Jets==5)*1.0130802393)+((N_Jets==6)*1.01661622524)+((N_Jets==7)*1.02081942558)+((N_Jets==8)*1.01794242859)+((N_Jets>=9)*1.01909327507))",
        "weight_SF_N_Jets__ttbb_4FS_DL__btag_BPURITYDown:=(((N_Jets==4)*0.991666913033)+((N_Jets==5)*0.987626791)+((N_Jets==6)*0.984231114388)+((N_Jets==7)*0.980049848557)+((N_Jets==8)*0.981469869614)+((N_Jets>=9)*0.981796741486))",
        "weight_SF_N_Jets__ttbb_4FS_DL__btag_BSTAT1Up:=(((N_Jets==4)*1.00262224674)+((N_Jets==5)*1.00363886356)+((N_Jets==6)*1.00391542912)+((N_Jets==7)*1.00351750851)+((N_Jets==8)*1.00403809547)+((N_Jets>=9)*1.00489234924))",
        "weight_SF_N_Jets__ttbb_4FS_DL__btag_BSTAT1Down:=(((N_Jets==4)*0.997265219688)+((N_Jets==5)*0.996360123158)+((N_Jets==6)*0.996133327484)+((N_Jets==7)*0.996484458447)+((N_Jets==8)*0.996041893959)+((N_Jets>=9)*0.995158970356))",
        "weight_SF_N_Jets__ttbb_4FS_DL__btag_LSTAT1Up:=(((N_Jets==4)*0.998824775219)+((N_Jets==5)*0.99862742424)+((N_Jets==6)*0.998594343662)+((N_Jets==7)*0.998844623566)+((N_Jets==8)*0.999309539795)+((N_Jets>=9)*0.998681426048))",
        "weight_SF_N_Jets__ttbb_4FS_DL__btag_LSTAT1Down:=(((N_Jets==4)*1.0010048151)+((N_Jets==5)*1.00129020214)+((N_Jets==6)*1.00135791302)+((N_Jets==7)*1.0010664463)+((N_Jets==8)*1.00068593025)+((N_Jets>=9)*1.00138187408))",
        "weight_SF_N_Jets__ttbb_4FS_DL__btag_BSTAT2Up:=(((N_Jets==4)*0.999907672405)+((N_Jets==5)*1.0004761219)+((N_Jets==6)*1.00051486492)+((N_Jets==7)*1.00078105927)+((N_Jets==8)*1.00099730492)+((N_Jets>=9)*1.00010633469))",
        "weight_SF_N_Jets__ttbb_4FS_DL__btag_BSTAT2Down:=(((N_Jets==4)*0.999966979027)+((N_Jets==5)*0.999493002892)+((N_Jets==6)*0.999480843544)+((N_Jets==7)*0.999233841896)+((N_Jets==8)*0.999029815197)+((N_Jets>=9)*0.999939858913))",
        "weight_SF_N_Jets__ttbb_4FS_DL__btag_LSTAT2Up:=(((N_Jets==4)*1.00010097027)+((N_Jets==5)*1.00029754639)+((N_Jets==6)*1.00081455708)+((N_Jets==7)*1.00173413754)+((N_Jets==8)*1.00154268742)+((N_Jets>=9)*1.00082659721))",
        "weight_SF_N_Jets__ttbb_4FS_DL__btag_LSTAT2Down:=(((N_Jets==4)*0.999725818634)+((N_Jets==5)*0.999603271484)+((N_Jets==6)*0.999105155468)+((N_Jets==7)*0.998139202595)+((N_Jets==8)*0.998365044594)+((N_Jets>=9)*0.999109685421))",
        "weight_SF_N_Jets__ttbb_4FS_DL__btag_CERR1Up:=(((N_Jets==4)*0.999938249588)+((N_Jets==5)*1.00047504902)+((N_Jets==6)*1.0010778904)+((N_Jets==7)*1.00185918808)+((N_Jets==8)*0.996399700642)+((N_Jets>=9)*1.00451219082))",
        "weight_SF_N_Jets__ttbb_4FS_DL__btag_CERR1Down:=(((N_Jets==4)*1.00005626678)+((N_Jets==5)*0.999222040176)+((N_Jets==6)*0.997929155827)+((N_Jets==7)*0.996508538723)+((N_Jets==8)*1.00609505177)+((N_Jets>=9)*0.992502450943))",
        "weight_SF_N_Jets__ttbb_4FS_DL__btag_CERR2Up:=(((N_Jets==4)*0.999825060368)+((N_Jets==5)*1.0000975132)+((N_Jets==6)*1.00061476231)+((N_Jets==7)*1.0011318922)+((N_Jets==8)*0.995798826218)+((N_Jets>=9)*1.00461816788))",
        "weight_SF_N_Jets__ttbb_4FS_DL__btag_CERR2Down:=(((N_Jets==4)*1.00022065639)+((N_Jets==5)*0.999895632267)+((N_Jets==6)*0.99909722805)+((N_Jets==7)*0.99818199873)+((N_Jets==8)*1.00583660603)+((N_Jets>=9)*0.993637859821))",
        "weight_SF_N_Jets__ttbb_4FS_DL__btag_NOMINAL:=(((N_Jets==4)*0.901804864407)+((N_Jets==5)*0.870256185532)+((N_Jets==6)*0.829614698887)+((N_Jets==7)*0.782587647438)+((N_Jets==8)*0.755793809891)+((N_Jets>=9)*0.684283196926))",

        "weight_SF_N_Jets__ttbb_4FS_FH__btag_LPURITYUp:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttbb_4FS_FH__btag_LPURITYDown:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttbb_4FS_FH__btag_BPURITYUp:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttbb_4FS_FH__btag_BPURITYDown:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttbb_4FS_FH__btag_BSTAT1Up:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttbb_4FS_FH__btag_BSTAT1Down:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttbb_4FS_FH__btag_LSTAT1Up:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttbb_4FS_FH__btag_LSTAT1Down:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttbb_4FS_FH__btag_BSTAT2Up:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttbb_4FS_FH__btag_BSTAT2Down:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttbb_4FS_FH__btag_LSTAT2Up:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttbb_4FS_FH__btag_LSTAT2Down:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttbb_4FS_FH__btag_CERR1Up:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttbb_4FS_FH__btag_CERR1Down:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttbb_4FS_FH__btag_CERR2Up:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttbb_4FS_FH__btag_CERR2Down:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttbb_4FS_FH__btag_NOMINAL:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",

        "weight_SF_N_Jets__ttb_4FS_SL__btag_LPURITYUp:=(((N_Jets==4)*0.994208216667)+((N_Jets==5)*0.992181479931)+((N_Jets==6)*0.990660190582)+((N_Jets==7)*0.98934930563)+((N_Jets==8)*0.986049890518)+((N_Jets>=9)*0.983838260174))",
        "weight_SF_N_Jets__ttb_4FS_SL__btag_LPURITYDown:=(((N_Jets==4)*1.00555288792)+((N_Jets==5)*1.00771570206)+((N_Jets==6)*1.00971615314)+((N_Jets==7)*1.01082932949)+((N_Jets==8)*1.01450264454)+((N_Jets>=9)*1.01555466652))",
        "weight_SF_N_Jets__ttb_4FS_SL__btag_BPURITYUp:=(((N_Jets==4)*1.00113487244)+((N_Jets==5)*1.00268673897)+((N_Jets==6)*1.00389492512)+((N_Jets==7)*1.00528180599)+((N_Jets==8)*1.00622236729)+((N_Jets>=9)*1.00711596012))",
        "weight_SF_N_Jets__ttb_4FS_SL__btag_BPURITYDown:=(((N_Jets==4)*0.998638391495)+((N_Jets==5)*0.997286558151)+((N_Jets==6)*0.996237695217)+((N_Jets==7)*0.995312988758)+((N_Jets==8)*0.994598329067)+((N_Jets>=9)*0.994252502918))",
        "weight_SF_N_Jets__ttb_4FS_SL__btag_BSTAT1Up:=(((N_Jets==4)*1.00111222267)+((N_Jets==5)*1.0014090538)+((N_Jets==6)*1.00176024437)+((N_Jets==7)*1.00249409676)+((N_Jets==8)*1.00274348259)+((N_Jets>=9)*1.00274753571))",
        "weight_SF_N_Jets__ttb_4FS_SL__btag_BSTAT1Down:=(((N_Jets==4)*0.998591423035)+((N_Jets==5)*0.998335182667)+((N_Jets==6)*0.998181462288)+((N_Jets==7)*0.997563898563)+((N_Jets==8)*0.997313737869)+((N_Jets>=9)*0.997290730476))",
        "weight_SF_N_Jets__ttb_4FS_SL__btag_LSTAT1Up:=(((N_Jets==4)*1.00016403198)+((N_Jets==5)*1.00018143654)+((N_Jets==6)*1.00019693375)+((N_Jets==7)*1.00032627583)+((N_Jets==8)*0.999962747097)+((N_Jets>=9)*0.999581038952))",
        "weight_SF_N_Jets__ttb_4FS_SL__btag_LSTAT1Down:=(((N_Jets==4)*0.999495625496)+((N_Jets==5)*0.999511301517)+((N_Jets==6)*0.999680399895)+((N_Jets==7)*0.999666035175)+((N_Jets==8)*1.00000035763)+((N_Jets>=9)*1.00036144257))",
        "weight_SF_N_Jets__ttb_4FS_SL__btag_BSTAT2Up:=(((N_Jets==4)*0.999864041805)+((N_Jets==5)*0.999832630157)+((N_Jets==6)*0.999933362007)+((N_Jets==7)*0.999915957451)+((N_Jets==8)*1.00049030781)+((N_Jets>=9)*1.00112426281))",
        "weight_SF_N_Jets__ttb_4FS_SL__btag_BSTAT2Down:=(((N_Jets==4)*0.999829649925)+((N_Jets==5)*0.99990350008)+((N_Jets==6)*0.999983489513)+((N_Jets==7)*1.00012516975)+((N_Jets==8)*0.999520659447)+((N_Jets>=9)*0.998878479004))",
        "weight_SF_N_Jets__ttb_4FS_SL__btag_LSTAT2Up:=(((N_Jets==4)*1.00025391579)+((N_Jets==5)*1.00040960312)+((N_Jets==6)*1.00055396557)+((N_Jets==7)*1.00069022179)+((N_Jets==8)*1.00062096119)+((N_Jets>=9)*1.00050449371))",
        "weight_SF_N_Jets__ttb_4FS_SL__btag_LSTAT2Down:=(((N_Jets==4)*0.999407708645)+((N_Jets==5)*0.999286651611)+((N_Jets==6)*0.999321639538)+((N_Jets==7)*0.99929869175)+((N_Jets==8)*0.999332249165)+((N_Jets>=9)*0.999419391155))",
        "weight_SF_N_Jets__ttb_4FS_SL__btag_CERR1Up:=(((N_Jets==4)*1.00096225739)+((N_Jets==5)*1.00061523914)+((N_Jets==6)*1.00245273113)+((N_Jets==7)*1.0022970438)+((N_Jets==8)*1.00104010105)+((N_Jets>=9)*0.998466968536))",
        "weight_SF_N_Jets__ttb_4FS_SL__btag_CERR1Down:=(((N_Jets==4)*0.998145461082)+((N_Jets==5)*0.998799622059)+((N_Jets==6)*0.995605349541)+((N_Jets==7)*0.996558427811)+((N_Jets==8)*0.997692286968)+((N_Jets>=9)*1.00414705276))",
        "weight_SF_N_Jets__ttb_4FS_SL__btag_CERR2Up:=(((N_Jets==4)*1.00095415115)+((N_Jets==5)*1.00070691109)+((N_Jets==6)*1.00206816196)+((N_Jets==7)*1.0022803545)+((N_Jets==8)*1.00149989128)+((N_Jets>=9)*0.999802529812))",
        "weight_SF_N_Jets__ttb_4FS_SL__btag_CERR2Down:=(((N_Jets==4)*0.998504936695)+((N_Jets==5)*0.998907983303)+((N_Jets==6)*0.997041225433)+((N_Jets==7)*0.997076928616)+((N_Jets==8)*0.997497498989)+((N_Jets>=9)*1.00106179714))",
        "weight_SF_N_Jets__ttb_4FS_SL__btag_NOMINAL:=(((N_Jets==4)*0.932512640953)+((N_Jets==5)*0.90585321188)+((N_Jets==6)*0.865367591381)+((N_Jets==7)*0.835592210293)+((N_Jets==8)*0.798147678375)+((N_Jets>=9)*0.756896615028))",

        "weight_SF_N_Jets__ttb_4FS_DL__btag_LPURITYUp:=(((N_Jets==4)*0.986935257912)+((N_Jets==5)*0.989085376263)+((N_Jets==6)*0.987565636635)+((N_Jets==7)*0.983159065247)+((N_Jets==8)*0.979617476463)+((N_Jets>=9)*0.990543603897))",
        "weight_SF_N_Jets__ttb_4FS_DL__btag_LPURITYDown:=(((N_Jets==4)*1.01305401325)+((N_Jets==5)*1.01097881794)+((N_Jets==6)*1.01262581348)+((N_Jets==7)*1.01725625992)+((N_Jets==8)*1.02125811577)+((N_Jets>=9)*1.01132762432))",
        "weight_SF_N_Jets__ttb_4FS_DL__btag_BPURITYUp:=(((N_Jets==4)*1.01255917549)+((N_Jets==5)*1.01606488228)+((N_Jets==6)*1.01714122295)+((N_Jets==7)*1.021302104)+((N_Jets==8)*1.02524113655)+((N_Jets>=9)*1.02618288994))",
        "weight_SF_N_Jets__ttb_4FS_DL__btag_BPURITYDown:=(((N_Jets==4)*0.987549304962)+((N_Jets==5)*0.984393894672)+((N_Jets==6)*0.983992874622)+((N_Jets==7)*0.979260861874)+((N_Jets==8)*0.976788580418)+((N_Jets>=9)*0.97460693121))",
        "weight_SF_N_Jets__ttb_4FS_DL__btag_BSTAT1Up:=(((N_Jets==4)*1.00227570534)+((N_Jets==5)*1.00216853619)+((N_Jets==6)*1.00267076492)+((N_Jets==7)*1.00339245796)+((N_Jets==8)*1.00358915329)+((N_Jets>=9)*1.00134444237))",
        "weight_SF_N_Jets__ttb_4FS_DL__btag_BSTAT1Down:=(((N_Jets==4)*0.997483551502)+((N_Jets==5)*0.997689366341)+((N_Jets==6)*0.997358977795)+((N_Jets==7)*0.99662989378)+((N_Jets==8)*0.996437370777)+((N_Jets>=9)*0.998722612858))",
        "weight_SF_N_Jets__ttb_4FS_DL__btag_LSTAT1Up:=(((N_Jets==4)*0.999077737331)+((N_Jets==5)*0.99944549799)+((N_Jets==6)*0.999513864517)+((N_Jets==7)*0.999052762985)+((N_Jets==8)*0.998368144035)+((N_Jets>=9)*0.999615311623))",
        "weight_SF_N_Jets__ttb_4FS_DL__btag_LSTAT1Down:=(((N_Jets==4)*1.00059974194)+((N_Jets==5)*1.00033402443)+((N_Jets==6)*1.00044977665)+((N_Jets==7)*1.00089657307)+((N_Jets==8)*1.00162065029)+((N_Jets>=9)*1.00050532818))",
        "weight_SF_N_Jets__ttb_4FS_DL__btag_BSTAT2Up:=(((N_Jets==4)*1.00012767315)+((N_Jets==5)*1.00011312962)+((N_Jets==6)*1.00053477287)+((N_Jets==7)*1.00018513203)+((N_Jets==8)*1.00162744522)+((N_Jets>=9)*1.00322413445))",
        "weight_SF_N_Jets__ttb_4FS_DL__btag_BSTAT2Down:=(((N_Jets==4)*0.999611794949)+((N_Jets==5)*0.999733746052)+((N_Jets==6)*0.999466836452)+((N_Jets==7)*0.999819219112)+((N_Jets==8)*0.998378157616)+((N_Jets>=9)*0.996820628643))",
        "weight_SF_N_Jets__ttb_4FS_DL__btag_LSTAT2Up:=(((N_Jets==4)*1.00079274178)+((N_Jets==5)*1.00150287151)+((N_Jets==6)*1.0016065836)+((N_Jets==7)*1.00184512138)+((N_Jets==8)*1.0012704134)+((N_Jets>=9)*1.00237190723))",
        "weight_SF_N_Jets__ttb_4FS_DL__btag_LSTAT2Down:=(((N_Jets==4)*0.9988707304)+((N_Jets==5)*0.998229682446)+((N_Jets==6)*0.998278439045)+((N_Jets==7)*0.99803674221)+((N_Jets==8)*0.998592793941)+((N_Jets>=9)*0.997611820698))",
        "weight_SF_N_Jets__ttb_4FS_DL__btag_CERR1Up:=(((N_Jets==4)*0.9995855093)+((N_Jets==5)*1.00030744076)+((N_Jets==6)*0.998485147953)+((N_Jets==7)*1.00060689449)+((N_Jets==8)*0.997618198395)+((N_Jets>=9)*1.00545108318))",
        "weight_SF_N_Jets__ttb_4FS_DL__btag_CERR1Down:=(((N_Jets==4)*1.00071084499)+((N_Jets==5)*0.999504983425)+((N_Jets==6)*1.00271594524)+((N_Jets==7)*0.998274207115)+((N_Jets==8)*1.0040333271)+((N_Jets>=9)*0.990733504295))",
        "weight_SF_N_Jets__ttb_4FS_DL__btag_CERR2Up:=(((N_Jets==4)*0.999424517155)+((N_Jets==5)*1.00004816055)+((N_Jets==6)*0.998456537724)+((N_Jets==7)*0.999529898167)+((N_Jets==8)*0.99779343605)+((N_Jets>=9)*1.00489473343))",
        "weight_SF_N_Jets__ttb_4FS_DL__btag_CERR2Down:=(((N_Jets==4)*1.00079393387)+((N_Jets==5)*0.999933540821)+((N_Jets==6)*1.00222396851)+((N_Jets==7)*1.00030064583)+((N_Jets==8)*1.00304567814)+((N_Jets>=9)*0.993405163288))",
        "weight_SF_N_Jets__ttb_4FS_DL__btag_NOMINAL:=(((N_Jets==4)*0.8818385005)+((N_Jets==5)*0.836226522923)+((N_Jets==6)*0.799994945526)+((N_Jets==7)*0.764801740646)+((N_Jets==8)*0.725424170494)+((N_Jets>=9)*0.59903472662))",

        "weight_SF_N_Jets__ttb_4FS_FH__btag_LPURITYUp:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttb_4FS_FH__btag_LPURITYDown:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttb_4FS_FH__btag_BPURITYUp:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttb_4FS_FH__btag_BPURITYDown:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttb_4FS_FH__btag_BSTAT1Up:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttb_4FS_FH__btag_BSTAT1Down:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttb_4FS_FH__btag_LSTAT1Up:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttb_4FS_FH__btag_LSTAT1Down:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttb_4FS_FH__btag_BSTAT2Up:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttb_4FS_FH__btag_BSTAT2Down:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttb_4FS_FH__btag_LSTAT2Up:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttb_4FS_FH__btag_LSTAT2Down:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttb_4FS_FH__btag_CERR1Up:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttb_4FS_FH__btag_CERR1Down:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttb_4FS_FH__btag_CERR2Up:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttb_4FS_FH__btag_CERR2Down:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__ttb_4FS_FH__btag_NOMINAL:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",

        "weight_SF_N_Jets__tt2b_4FS_SL__btag_LPURITYUp:=(((N_Jets==4)*0.972256422043)+((N_Jets==5)*0.9691157341)+((N_Jets==6)*0.966566562653)+((N_Jets==7)*0.967159330845)+((N_Jets==8)*0.96573138237)+((N_Jets>=9)*0.968816459179))",
        "weight_SF_N_Jets__tt2b_4FS_SL__btag_LPURITYDown:=(((N_Jets==4)*1.02902388573)+((N_Jets==5)*1.03240847588)+((N_Jets==6)*1.03485929966)+((N_Jets==7)*1.03431344032)+((N_Jets==8)*1.03645312786)+((N_Jets>=9)*1.03227984905))",
        "weight_SF_N_Jets__tt2b_4FS_SL__btag_BPURITYUp:=(((N_Jets==4)*1.00237882137)+((N_Jets==5)*1.00487589836)+((N_Jets==6)*1.00684511662)+((N_Jets==7)*1.00624918938)+((N_Jets==8)*1.00974798203)+((N_Jets>=9)*1.00984275341))",
        "weight_SF_N_Jets__tt2b_4FS_SL__btag_BPURITYDown:=(((N_Jets==4)*0.997956991196)+((N_Jets==5)*0.995373249054)+((N_Jets==6)*0.993665933609)+((N_Jets==7)*0.993727743626)+((N_Jets==8)*0.990837693214)+((N_Jets>=9)*0.991404592991))",
        "weight_SF_N_Jets__tt2b_4FS_SL__btag_BSTAT1Up:=(((N_Jets==4)*1.0053384304)+((N_Jets==5)*1.00646162033)+((N_Jets==6)*1.00677454472)+((N_Jets==7)*1.00658607483)+((N_Jets==8)*1.00748670101)+((N_Jets>=9)*1.00582015514))",
        "weight_SF_N_Jets__tt2b_4FS_SL__btag_BSTAT1Down:=(((N_Jets==4)*0.994778931141)+((N_Jets==5)*0.99367249012)+((N_Jets==6)*0.993348836899)+((N_Jets==7)*0.993526041508)+((N_Jets==8)*0.992630362511)+((N_Jets>=9)*0.994274914265))",
        "weight_SF_N_Jets__tt2b_4FS_SL__btag_LSTAT1Up:=(((N_Jets==4)*0.998095929623)+((N_Jets==5)*0.998122751713)+((N_Jets==6)*0.998133420944)+((N_Jets==7)*0.998087227345)+((N_Jets==8)*0.997907459736)+((N_Jets>=9)*0.998431146145))",
        "weight_SF_N_Jets__tt2b_4FS_SL__btag_LSTAT1Down:=(((N_Jets==4)*1.00192213058)+((N_Jets==5)*1.00188004971)+((N_Jets==6)*1.00184202194)+((N_Jets==7)*1.00188696384)+((N_Jets==8)*1.00186812878)+((N_Jets>=9)*1.0015963316))",
        "weight_SF_N_Jets__tt2b_4FS_SL__btag_BSTAT2Up:=(((N_Jets==4)*1.00050139427)+((N_Jets==5)*1.00027894974)+((N_Jets==6)*1.00074732304)+((N_Jets==7)*1.00071239471)+((N_Jets==8)*0.999785125256)+((N_Jets>=9)*1.00193274021))",
        "weight_SF_N_Jets__tt2b_4FS_SL__btag_BSTAT2Down:=(((N_Jets==4)*0.999546408653)+((N_Jets==5)*0.999765396118)+((N_Jets==6)*0.999278485775)+((N_Jets==7)*0.999297916889)+((N_Jets==8)*1.00022315979)+((N_Jets>=9)*0.998062074184))",
        "weight_SF_N_Jets__tt2b_4FS_SL__btag_LSTAT2Up:=(((N_Jets==4)*0.998737871647)+((N_Jets==5)*0.998967885971)+((N_Jets==6)*0.999048352242)+((N_Jets==7)*0.999244689941)+((N_Jets==8)*0.999442994595)+((N_Jets>=9)*0.998894810677))",
        "weight_SF_N_Jets__tt2b_4FS_SL__btag_LSTAT2Down:=(((N_Jets==4)*1.00128698349)+((N_Jets==5)*1.00103533268)+((N_Jets==6)*1.00094139576)+((N_Jets==7)*1.00070357323)+((N_Jets==8)*1.00046014786)+((N_Jets>=9)*1.00110387802))",
        "weight_SF_N_Jets__tt2b_4FS_SL__btag_CERR1Up:=(((N_Jets==4)*0.999420583248)+((N_Jets==5)*1.00280785561)+((N_Jets==6)*1.00323164463)+((N_Jets==7)*0.999042630196)+((N_Jets==8)*1.00414657593)+((N_Jets>=9)*0.998651742935))",
        "weight_SF_N_Jets__tt2b_4FS_SL__btag_CERR1Down:=(((N_Jets==4)*1.00111675262)+((N_Jets==5)*0.994913339615)+((N_Jets==6)*0.994284152985)+((N_Jets==7)*1.00161135197)+((N_Jets==8)*0.992070794106)+((N_Jets>=9)*1.00376331806))",
        "weight_SF_N_Jets__tt2b_4FS_SL__btag_CERR2Up:=(((N_Jets==4)*0.999704778194)+((N_Jets==5)*1.00229930878)+((N_Jets==6)*1.00272369385)+((N_Jets==7)*0.999426722527)+((N_Jets==8)*1.00269329548)+((N_Jets>=9)*1.00041592121))",
        "weight_SF_N_Jets__tt2b_4FS_SL__btag_CERR2Down:=(((N_Jets==4)*1.00046932697)+((N_Jets==5)*0.996721625328)+((N_Jets==6)*0.996159136295)+((N_Jets==7)*1.00079226494)+((N_Jets==8)*0.996167361736)+((N_Jets>=9)*1.00052416325))",
        "weight_SF_N_Jets__tt2b_4FS_SL__btag_NOMINAL:=(((N_Jets==4)*0.981753528118)+((N_Jets==5)*0.9555529356)+((N_Jets==6)*0.92030197382)+((N_Jets==7)*0.880551278591)+((N_Jets==8)*0.841189920902)+((N_Jets>=9)*0.745058357716))",

        "weight_SF_N_Jets__tt2b_4FS_DL__btag_LPURITYUp:=(((N_Jets==4)*0.96769797802)+((N_Jets==5)*0.966965556145)+((N_Jets==6)*0.967757880688)+((N_Jets==7)*0.962900519371)+((N_Jets==8)*0.964097976685)+((N_Jets>=9)*0.964197874069))",
        "weight_SF_N_Jets__tt2b_4FS_DL__btag_LPURITYDown:=(((N_Jets==4)*1.03367567062)+((N_Jets==5)*1.03425991535)+((N_Jets==6)*1.03409099579)+((N_Jets==7)*1.03967118263)+((N_Jets==8)*1.03728187084)+((N_Jets>=9)*1.03667318821))",
        "weight_SF_N_Jets__tt2b_4FS_DL__btag_BPURITYUp:=(((N_Jets==4)*1.0133780241)+((N_Jets==5)*1.01748907566)+((N_Jets==6)*1.01990962029)+((N_Jets==7)*1.01867687702)+((N_Jets==8)*1.01247227192)+((N_Jets>=9)*1.01846444607))",
        "weight_SF_N_Jets__tt2b_4FS_DL__btag_BPURITYDown:=(((N_Jets==4)*0.986899554729)+((N_Jets==5)*0.983103632927)+((N_Jets==6)*0.980523884296)+((N_Jets==7)*0.982315182686)+((N_Jets==8)*0.98819309473)+((N_Jets>=9)*0.978537678719))",
        "weight_SF_N_Jets__tt2b_4FS_DL__btag_BSTAT1Up:=(((N_Jets==4)*1.00657451153)+((N_Jets==5)*1.00662946701)+((N_Jets==6)*1.00689530373)+((N_Jets==7)*1.00732338428)+((N_Jets==8)*1.00808525085)+((N_Jets>=9)*1.00790095329))",
        "weight_SF_N_Jets__tt2b_4FS_DL__btag_BSTAT1Down:=(((N_Jets==4)*0.993438124657)+((N_Jets==5)*0.993457019329)+((N_Jets==6)*0.993227422237)+((N_Jets==7)*0.992801606655)+((N_Jets==8)*0.992050230503)+((N_Jets>=9)*0.992192924023))",
        "weight_SF_N_Jets__tt2b_4FS_DL__btag_LSTAT1Up:=(((N_Jets==4)*0.997209012508)+((N_Jets==5)*0.997671484947)+((N_Jets==6)*0.997713804245)+((N_Jets==7)*0.99692428112)+((N_Jets==8)*0.997914373875)+((N_Jets>=9)*0.995849370956))",
        "weight_SF_N_Jets__tt2b_4FS_DL__btag_LSTAT1Down:=(((N_Jets==4)*1.0026652813)+((N_Jets==5)*1.00225615501)+((N_Jets==6)*1.00214350224)+((N_Jets==7)*1.00310790539)+((N_Jets==8)*1.00194656849)+((N_Jets>=9)*1.00408089161))",
        "weight_SF_N_Jets__tt2b_4FS_DL__btag_BSTAT2Up:=(((N_Jets==4)*1.00037038326)+((N_Jets==5)*1.00013113022)+((N_Jets==6)*1.00063228607)+((N_Jets==7)*1.00126457214)+((N_Jets==8)*1.00020551682)+((N_Jets>=9)*1.00362944603))",
        "weight_SF_N_Jets__tt2b_4FS_DL__btag_BSTAT2Down:=(((N_Jets==4)*0.999550700188)+((N_Jets==5)*0.99986743927)+((N_Jets==6)*0.99936580658)+((N_Jets==7)*0.998743593693)+((N_Jets==8)*0.999805510044)+((N_Jets>=9)*0.996378958225))",
        "weight_SF_N_Jets__tt2b_4FS_DL__btag_LSTAT2Up:=(((N_Jets==4)*0.999317467213)+((N_Jets==5)*1.00000333786)+((N_Jets==6)*1.00045585632)+((N_Jets==7)*0.999403595924)+((N_Jets==8)*0.999934077263)+((N_Jets>=9)*0.99816185236))",
        "weight_SF_N_Jets__tt2b_4FS_DL__btag_LSTAT2Down:=(((N_Jets==4)*1.00052666664)+((N_Jets==5)*0.999906003475)+((N_Jets==6)*0.999444901943)+((N_Jets==7)*1.00051951408)+((N_Jets==8)*1.00000703335)+((N_Jets>=9)*1.00173425674))",
        "weight_SF_N_Jets__tt2b_4FS_DL__btag_CERR1Up:=(((N_Jets==4)*1.00037372112)+((N_Jets==5)*1.00156843662)+((N_Jets==6)*1.00014197826)+((N_Jets==7)*1.00551974773)+((N_Jets==8)*1.00521278381)+((N_Jets>=9)*1.00969040394))",
        "weight_SF_N_Jets__tt2b_4FS_DL__btag_CERR1Down:=(((N_Jets==4)*0.999281108379)+((N_Jets==5)*0.997059226036)+((N_Jets==6)*0.999551177025)+((N_Jets==7)*0.991515219212)+((N_Jets==8)*0.99128651619)+((N_Jets>=9)*0.985206127167))",
        "weight_SF_N_Jets__tt2b_4FS_DL__btag_CERR2Up:=(((N_Jets==4)*1.0001373291)+((N_Jets==5)*1.0008431673)+((N_Jets==6)*1.00006091595)+((N_Jets==7)*1.00347137451)+((N_Jets==8)*1.00387346745)+((N_Jets>=9)*1.00649559498))",
        "weight_SF_N_Jets__tt2b_4FS_DL__btag_CERR2Down:=(((N_Jets==4)*0.999773025513)+((N_Jets==5)*0.99879693985)+((N_Jets==6)*0.999811530113)+((N_Jets==7)*0.995723068714)+((N_Jets==8)*0.994626045227)+((N_Jets>=9)*0.992153227329))",
        "weight_SF_N_Jets__tt2b_4FS_DL__btag_NOMINAL:=(((N_Jets==4)*0.928451597691)+((N_Jets==5)*0.881482005119)+((N_Jets==6)*0.837522685528)+((N_Jets==7)*0.804429888725)+((N_Jets==8)*0.77636474371)+((N_Jets>=9)*0.677708268166))",

        "weight_SF_N_Jets__tt2b_4FS_FH__btag_LPURITYUp:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__tt2b_4FS_FH__btag_LPURITYDown:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__tt2b_4FS_FH__btag_BPURITYUp:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__tt2b_4FS_FH__btag_BPURITYDown:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__tt2b_4FS_FH__btag_BSTAT1Up:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__tt2b_4FS_FH__btag_BSTAT1Down:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__tt2b_4FS_FH__btag_LSTAT1Up:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__tt2b_4FS_FH__btag_LSTAT1Down:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__tt2b_4FS_FH__btag_BSTAT2Up:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__tt2b_4FS_FH__btag_BSTAT2Down:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__tt2b_4FS_FH__btag_LSTAT2Up:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__tt2b_4FS_FH__btag_LSTAT2Down:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__tt2b_4FS_FH__btag_CERR1Up:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__tt2b_4FS_FH__btag_CERR1Down:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__tt2b_4FS_FH__btag_CERR2Up:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__tt2b_4FS_FH__btag_CERR2Down:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",
        "weight_SF_N_Jets__tt2b_4FS_FH__btag_NOMINAL:=(((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",

        "weight_SF_N_Jets__ttlf_SL__btag_LPURITYUp:=(((N_Jets==4)*0.984688282013)+((N_Jets==5)*0.984327912331)+((N_Jets==6)*0.983844339848)+((N_Jets==7)*0.983874976635)+((N_Jets==8)*0.987037479877)+((N_Jets>=9)*0.981444656849))",
        "weight_SF_N_Jets__ttlf_SL__btag_LPURITYDown:=(((N_Jets==4)*1.01656651497)+((N_Jets==5)*1.01625239849)+((N_Jets==6)*1.01677596569)+((N_Jets==7)*1.01636815071)+((N_Jets==8)*1.01311337948)+((N_Jets>=9)*1.01955413818))",
        "weight_SF_N_Jets__ttlf_SL__btag_BPURITYUp:=(((N_Jets==4)*1.00192594528)+((N_Jets==5)*1.00344479084)+((N_Jets==6)*1.00479388237)+((N_Jets==7)*1.00418424606)+((N_Jets==8)*1.00782060623)+((N_Jets>=9)*1.00952327251))",
        "weight_SF_N_Jets__ttlf_SL__btag_BPURITYDown:=(((N_Jets==4)*0.999137401581)+((N_Jets==5)*0.997102975845)+((N_Jets==6)*0.995772957802)+((N_Jets==7)*0.996294558048)+((N_Jets==8)*0.992411673069)+((N_Jets>=9)*0.992485046387))",
        "weight_SF_N_Jets__ttlf_SL__btag_BSTAT1Up:=(((N_Jets==4)*1.00329184532)+((N_Jets==5)*1.00290238857)+((N_Jets==6)*1.00305449963)+((N_Jets==7)*1.00257444382)+((N_Jets==8)*1.00225520134)+((N_Jets>=9)*1.00383031368))",
        "weight_SF_N_Jets__ttlf_SL__btag_BSTAT1Down:=(((N_Jets==4)*0.99756103754)+((N_Jets==5)*0.99729269743)+((N_Jets==6)*0.997107028961)+((N_Jets==7)*0.997391343117)+((N_Jets==8)*0.997763872147)+((N_Jets>=9)*0.996213793755))",
        "weight_SF_N_Jets__ttlf_SL__btag_LSTAT1Up:=(((N_Jets==4)*1.0002310276)+((N_Jets==5)*1.00015509129)+((N_Jets==6)*1.00043654442)+((N_Jets==7)*1.00037813187)+((N_Jets==8)*1.00141370296)+((N_Jets>=9)*0.999487221241))",
        "weight_SF_N_Jets__ttlf_SL__btag_LSTAT1Down:=(((N_Jets==4)*1.00057649612)+((N_Jets==5)*0.999951303005)+((N_Jets==6)*0.999617993832)+((N_Jets==7)*0.999478161335)+((N_Jets==8)*0.998517632484)+((N_Jets>=9)*1.00045049191))",
        "weight_SF_N_Jets__ttlf_SL__btag_BSTAT2Up:=(((N_Jets==4)*1.00060093403)+((N_Jets==5)*1.00027430058)+((N_Jets==6)*1.00015461445)+((N_Jets==7)*1.000395298)+((N_Jets==8)*1.00056231022)+((N_Jets>=9)*1.00044465065))",
        "weight_SF_N_Jets__ttlf_SL__btag_BSTAT2Down:=(((N_Jets==4)*1.0003374815)+((N_Jets==5)*0.999912321568)+((N_Jets==6)*0.999984562397)+((N_Jets==7)*0.999550640583)+((N_Jets==8)*0.999448657036)+((N_Jets>=9)*0.999561071396))",
        "weight_SF_N_Jets__ttlf_SL__btag_LSTAT2Up:=(((N_Jets==4)*1.00042212009)+((N_Jets==5)*1.00054121017)+((N_Jets==6)*1.00079846382)+((N_Jets==7)*1.00070500374)+((N_Jets==8)*1.00149059296)+((N_Jets>=9)*0.999963998795))",
        "weight_SF_N_Jets__ttlf_SL__btag_LSTAT2Down:=(((N_Jets==4)*1.00041127205)+((N_Jets==5)*0.999582350254)+((N_Jets==6)*0.999281466007)+((N_Jets==7)*0.999179959297)+((N_Jets==8)*0.998456060886)+((N_Jets>=9)*1.00005197525))",
        "weight_SF_N_Jets__ttlf_SL__btag_CERR1Up:=(((N_Jets==4)*1.00247120857)+((N_Jets==5)*1.00220227242)+((N_Jets==6)*1.00213682652)+((N_Jets==7)*1.00055789948)+((N_Jets==8)*1.00432324409)+((N_Jets>=9)*1.00693368912))",
        "weight_SF_N_Jets__ttlf_SL__btag_CERR1Down:=(((N_Jets==4)*0.996102571487)+((N_Jets==5)*0.996078848839)+((N_Jets==6)*0.996348619461)+((N_Jets==7)*0.998970031738)+((N_Jets==8)*0.992663025856)+((N_Jets>=9)*0.988737761974))",
        "weight_SF_N_Jets__ttlf_SL__btag_CERR2Up:=(((N_Jets==4)*1.00242459774)+((N_Jets==5)*1.00216519833)+((N_Jets==6)*1.00217688084)+((N_Jets==7)*1.0009303093)+((N_Jets==8)*1.00414717197)+((N_Jets>=9)*1.00586819649))",
        "weight_SF_N_Jets__ttlf_SL__btag_CERR2Down:=(((N_Jets==4)*0.996884524822)+((N_Jets==5)*0.996939361095)+((N_Jets==6)*0.997002661228)+((N_Jets==7)*0.998657107353)+((N_Jets==8)*0.994341135025)+((N_Jets>=9)*0.992203831673))",
        "weight_SF_N_Jets__ttlf_SL__btag_NOMINAL:=(((N_Jets==4)*0.968565821648)+((N_Jets==5)*0.929920971394)+((N_Jets==6)*0.889562189579)+((N_Jets==7)*0.848294913769)+((N_Jets==8)*0.777036607265)+((N_Jets>=9)*0.74977940321))",

        "weight_SF_N_Jets__ttlf_DL__btag_LPURITYUp:=(((N_Jets==4)*0.983667135239)+((N_Jets==5)*0.983938455582)+((N_Jets==6)*0.984955012798)+((N_Jets==7)*0.981209278107)+((N_Jets==8)*0.987900078297)+((N_Jets>=9)*1.00487816334))",
        "weight_SF_N_Jets__ttlf_DL__btag_LPURITYDown:=(((N_Jets==4)*1.01630425453)+((N_Jets==5)*1.01657772064)+((N_Jets==6)*1.01510763168)+((N_Jets==7)*1.01932704449)+((N_Jets==8)*1.01160013676)+((N_Jets>=9)*0.997249305248))",
        "weight_SF_N_Jets__ttlf_DL__btag_BPURITYUp:=(((N_Jets==4)*1.01500880718)+((N_Jets==5)*1.01783955097)+((N_Jets==6)*1.02175021172)+((N_Jets==7)*1.02422940731)+((N_Jets==8)*1.01723945141)+((N_Jets>=9)*1.01635622978))",
        "weight_SF_N_Jets__ttlf_DL__btag_BPURITYDown:=(((N_Jets==4)*0.985127687454)+((N_Jets==5)*0.983084619045)+((N_Jets==6)*0.979555785656)+((N_Jets==7)*0.976972103119)+((N_Jets==8)*0.981283962727)+((N_Jets>=9)*0.981919705868))",
        "weight_SF_N_Jets__ttlf_DL__btag_BSTAT1Up:=(((N_Jets==4)*1.00273287296)+((N_Jets==5)*1.00280356407)+((N_Jets==6)*1.00252211094)+((N_Jets==7)*1.00356757641)+((N_Jets==8)*1.00201022625)+((N_Jets>=9)*1.00221693516))",
        "weight_SF_N_Jets__ttlf_DL__btag_BSTAT1Down:=(((N_Jets==4)*0.996897339821)+((N_Jets==5)*0.997294008732)+((N_Jets==6)*0.997469782829)+((N_Jets==7)*0.996472775936)+((N_Jets==8)*0.997992217541)+((N_Jets>=9)*0.997788608074))",
        "weight_SF_N_Jets__ttlf_DL__btag_LSTAT1Up:=(((N_Jets==4)*0.999172389507)+((N_Jets==5)*0.999584436417)+((N_Jets==6)*1.00002777576)+((N_Jets==7)*1.00010752678)+((N_Jets==8)*1.00072515011)+((N_Jets>=9)*1.00158691406))",
        "weight_SF_N_Jets__ttlf_DL__btag_LSTAT1Down:=(((N_Jets==4)*1.00034976006)+((N_Jets==5)*1.00040960312)+((N_Jets==6)*0.999800503254)+((N_Jets==7)*0.999749362469)+((N_Jets==8)*0.999120414257)+((N_Jets>=9)*0.998245298862))",
        "weight_SF_N_Jets__ttlf_DL__btag_BSTAT2Up:=(((N_Jets==4)*1.0001064539)+((N_Jets==5)*1.00047457218)+((N_Jets==6)*1.00059533119)+((N_Jets==7)*1.00055062771)+((N_Jets==8)*1.00080227852)+((N_Jets>=9)*0.998807549477))",
        "weight_SF_N_Jets__ttlf_DL__btag_BSTAT2Down:=(((N_Jets==4)*0.999508917332)+((N_Jets==5)*0.999591767788)+((N_Jets==6)*0.999372720718)+((N_Jets==7)*0.999455869198)+((N_Jets==8)*0.999189555645)+((N_Jets>=9)*1.0011909008))",
        "weight_SF_N_Jets__ttlf_DL__btag_LSTAT2Up:=(((N_Jets==4)*1.00118756294)+((N_Jets==5)*1.00178170204)+((N_Jets==6)*1.00233089924)+((N_Jets==7)*1.00251829624)+((N_Jets==8)*1.00291478634)+((N_Jets>=9)*1.00432777405))",
        "weight_SF_N_Jets__ttlf_DL__btag_LSTAT2Down:=(((N_Jets==4)*0.998303413391)+((N_Jets==5)*0.998173594475)+((N_Jets==6)*0.997505664825)+((N_Jets==7)*0.997323930264)+((N_Jets==8)*0.996905088425)+((N_Jets>=9)*0.995516121387))",
        "weight_SF_N_Jets__ttlf_DL__btag_CERR1Up:=(((N_Jets==4)*0.999935567379)+((N_Jets==5)*0.999681770802)+((N_Jets==6)*1.00016057491)+((N_Jets==7)*1.00021076202)+((N_Jets==8)*0.998745620251)+((N_Jets>=9)*0.996893405914))",
        "weight_SF_N_Jets__ttlf_DL__btag_CERR1Down:=(((N_Jets==4)*1.00010240078)+((N_Jets==5)*1.00057601929)+((N_Jets==6)*0.999686956406)+((N_Jets==7)*0.999649584293)+((N_Jets==8)*1.00249183178)+((N_Jets>=9)*1.00566279888))",
        "weight_SF_N_Jets__ttlf_DL__btag_CERR2Up:=(((N_Jets==4)*0.99988079071)+((N_Jets==5)*0.999688446522)+((N_Jets==6)*1.00002014637)+((N_Jets==7)*1.0001553297)+((N_Jets==8)*0.998990356922)+((N_Jets>=9)*0.997285306454))",
        "weight_SF_N_Jets__ttlf_DL__btag_CERR2Down:=(((N_Jets==4)*1.00016117096)+((N_Jets==5)*1.0004503727)+((N_Jets==6)*0.999966621399)+((N_Jets==7)*0.999792873859)+((N_Jets==8)*1.00157546997)+((N_Jets>=9)*1.00394082069))",
        "weight_SF_N_Jets__ttlf_DL__btag_NOMINAL:=(((N_Jets==4)*0.889103531837)+((N_Jets==5)*0.842189252377)+((N_Jets==6)*0.787316143513)+((N_Jets==7)*0.756484866142)+((N_Jets==8)*0.728161334991)+((N_Jets>=9)*0.639573991299))",

        "weight_SF_N_Jets__ttlf_FH__btag_LPURITYUp:=(((N_Jets==4)*0.988051891327)+((N_Jets==5)*0.984952151775)+((N_Jets==6)*0.983146607876)+((N_Jets==7)*0.983211636543)+((N_Jets==8)*0.98353099823)+((N_Jets>=9)*0.985647857189))",
        "weight_SF_N_Jets__ttlf_FH__btag_LPURITYDown:=(((N_Jets==4)*1.01227605343)+((N_Jets==5)*1.01554143429)+((N_Jets==6)*1.01746273041)+((N_Jets==7)*1.01741802692)+((N_Jets==8)*1.01702427864)+((N_Jets>=9)*1.01482725143))",
        "weight_SF_N_Jets__ttlf_FH__btag_BPURITYUp:=(((N_Jets==4)*0.994938850403)+((N_Jets==5)*0.993215024471)+((N_Jets==6)*0.992277801037)+((N_Jets==7)*0.99126470089)+((N_Jets==8)*0.9896941185)+((N_Jets>=9)*0.990622878075))",
        "weight_SF_N_Jets__ttlf_FH__btag_BPURITYDown:=(((N_Jets==4)*1.00522243977)+((N_Jets==5)*1.0070258379)+((N_Jets==6)*1.00800454617)+((N_Jets==7)*1.00934517384)+((N_Jets==8)*1.01090276241)+((N_Jets>=9)*1.00930643082))",
        "weight_SF_N_Jets__ttlf_FH__btag_BSTAT1Up:=(((N_Jets==4)*1.00212752819)+((N_Jets==5)*1.00263750553)+((N_Jets==6)*1.00306856632)+((N_Jets==7)*1.00313699245)+((N_Jets==8)*1.00268125534)+((N_Jets>=9)*1.00225651264))",
        "weight_SF_N_Jets__ttlf_FH__btag_BSTAT1Down:=(((N_Jets==4)*0.99795794487)+((N_Jets==5)*0.997453570366)+((N_Jets==6)*0.997054338455)+((N_Jets==7)*0.996976137161)+((N_Jets==8)*0.997370123863)+((N_Jets>=9)*0.997751176357))",
        "weight_SF_N_Jets__ttlf_FH__btag_LSTAT1Up:=(((N_Jets==4)*1.00042974949)+((N_Jets==5)*1.00060653687)+((N_Jets==6)*1.00073349476)+((N_Jets==7)*1.00092482567)+((N_Jets==8)*1.00084161758)+((N_Jets>=9)*1.00148391724))",
        "weight_SF_N_Jets__ttlf_FH__btag_LSTAT1Down:=(((N_Jets==4)*0.9995906353)+((N_Jets==5)*0.999402761459)+((N_Jets==6)*0.999294936657)+((N_Jets==7)*0.999111711979)+((N_Jets==8)*0.999138057232)+((N_Jets>=9)*0.998467504978))",
        "weight_SF_N_Jets__ttlf_FH__btag_BSTAT2Up:=(((N_Jets==4)*1.00011539459)+((N_Jets==5)*1.00017595291)+((N_Jets==6)*1.0001168251)+((N_Jets==7)*1.00009679794)+((N_Jets==8)*1.00009119511)+((N_Jets>=9)*1.00062477589))",
        "weight_SF_N_Jets__ttlf_FH__btag_BSTAT2Down:=(((N_Jets==4)*0.999934494495)+((N_Jets==5)*0.999886572361)+((N_Jets==6)*0.999987304211)+((N_Jets==7)*0.999992489815)+((N_Jets==8)*0.999947845936)+((N_Jets>=9)*0.999355852604))",
        "weight_SF_N_Jets__ttlf_FH__btag_LSTAT2Up:=(((N_Jets==4)*0.999692618847)+((N_Jets==5)*0.999578475952)+((N_Jets==6)*0.999554395676)+((N_Jets==7)*0.999493300915)+((N_Jets==8)*0.999276995659)+((N_Jets>=9)*0.999782264233))",
        "weight_SF_N_Jets__ttlf_FH__btag_LSTAT2Down:=(((N_Jets==4)*1.00037145615)+((N_Jets==5)*1.00048816204)+((N_Jets==6)*1.00053548813)+((N_Jets==7)*1.00059962273)+((N_Jets==8)*1.00076556206)+((N_Jets>=9)*1.00021541119))",
        "weight_SF_N_Jets__ttlf_FH__btag_CERR1Up:=(((N_Jets==4)*1.00332570076)+((N_Jets==5)*1.0039024353)+((N_Jets==6)*1.00548124313)+((N_Jets==7)*1.0059646368)+((N_Jets==8)*1.00708627701)+((N_Jets>=9)*1.01117444038))",
        "weight_SF_N_Jets__ttlf_FH__btag_CERR1Down:=(((N_Jets==4)*0.994110107422)+((N_Jets==5)*0.993019402027)+((N_Jets==6)*0.990364015102)+((N_Jets==7)*0.989921927452)+((N_Jets==8)*0.987320065498)+((N_Jets>=9)*0.981809854507))",
        "weight_SF_N_Jets__ttlf_FH__btag_CERR2Up:=(((N_Jets==4)*1.00339865685)+((N_Jets==5)*1.00399637222)+((N_Jets==6)*1.00539159775)+((N_Jets==7)*1.00592291355)+((N_Jets==8)*1.0069937706)+((N_Jets>=9)*1.01046907902))",
        "weight_SF_N_Jets__ttlf_FH__btag_CERR2Down:=(((N_Jets==4)*0.995153188705)+((N_Jets==5)*0.994266986847)+((N_Jets==6)*0.992465794086)+((N_Jets==7)*0.991971373558)+((N_Jets==8)*0.990158498287)+((N_Jets>=9)*0.986086010933))",
        "weight_SF_N_Jets__ttlf_FH__btag_NOMINAL:=(((N_Jets==4)*0.998388886452)+((N_Jets==5)*0.995514571667)+((N_Jets==6)*0.972341954708)+((N_Jets==7)*0.935100138187)+((N_Jets==8)*0.889777183533)+((N_Jets>=9)*0.83453142643))",

        "weight_SF_N_Jets__ttcc_SL__btag_LPURITYUp:=(((N_Jets==4)*0.985290527344)+((N_Jets==5)*0.984489321709)+((N_Jets==6)*0.985207855701)+((N_Jets==7)*0.985609650612)+((N_Jets==8)*0.983703911304)+((N_Jets>=9)*0.990553379059))",
        "weight_SF_N_Jets__ttcc_SL__btag_LPURITYDown:=(((N_Jets==4)*1.01481771469)+((N_Jets==5)*1.01593804359)+((N_Jets==6)*1.01521980762)+((N_Jets==7)*1.01442468166)+((N_Jets==8)*1.01693475246)+((N_Jets>=9)*1.0089097023))",
        "weight_SF_N_Jets__ttcc_SL__btag_BPURITYUp:=(((N_Jets==4)*1.00051152706)+((N_Jets==5)*1.00089871883)+((N_Jets==6)*1.00369560719)+((N_Jets==7)*1.00733029842)+((N_Jets==8)*1.01003098488)+((N_Jets>=9)*1.00801634789))",
        "weight_SF_N_Jets__ttcc_SL__btag_BPURITYDown:=(((N_Jets==4)*0.999563932419)+((N_Jets==5)*0.99922311306)+((N_Jets==6)*0.996873736382)+((N_Jets==7)*0.993711173534)+((N_Jets==8)*0.989016473293)+((N_Jets>=9)*0.992370188236))",
        "weight_SF_N_Jets__ttcc_SL__btag_BSTAT1Up:=(((N_Jets==4)*1.00252199173)+((N_Jets==5)*1.00258982182)+((N_Jets==6)*1.00261163712)+((N_Jets==7)*1.00250923634)+((N_Jets==8)*1.00241196156)+((N_Jets>=9)*1.00187242031))",
        "weight_SF_N_Jets__ttcc_SL__btag_BSTAT1Down:=(((N_Jets==4)*0.997418582439)+((N_Jets==5)*0.997365057468)+((N_Jets==6)*0.997385859489)+((N_Jets==7)*0.997523069382)+((N_Jets==8)*0.997595906258)+((N_Jets>=9)*0.998127162457))",
        "weight_SF_N_Jets__ttcc_SL__btag_LSTAT1Up:=(((N_Jets==4)*0.999482929707)+((N_Jets==5)*0.999535143375)+((N_Jets==6)*1.0000244379)+((N_Jets==7)*1.00029957294)+((N_Jets==8)*0.999038338661)+((N_Jets>=9)*1.00152313709))",
        "weight_SF_N_Jets__ttcc_SL__btag_LSTAT1Down:=(((N_Jets==4)*1.00041604042)+((N_Jets==5)*1.00035941601)+((N_Jets==6)*0.999884784222)+((N_Jets==7)*0.999624431133)+((N_Jets==8)*1.00096297264)+((N_Jets>=9)*0.998437106609))",
        "weight_SF_N_Jets__ttcc_SL__btag_BSTAT2Up:=(((N_Jets==4)*1.00028479099)+((N_Jets==5)*1.00038468838)+((N_Jets==6)*1.00037312508)+((N_Jets==7)*1.0003900528)+((N_Jets==8)*1.00066661835)+((N_Jets>=9)*1.00013840199))",
        "weight_SF_N_Jets__ttcc_SL__btag_BSTAT2Down:=(((N_Jets==4)*0.99963337183)+((N_Jets==5)*0.999545097351)+((N_Jets==6)*0.999599933624)+((N_Jets==7)*0.999622404575)+((N_Jets==8)*0.99933886528)+((N_Jets>=9)*0.999861299992))",
        "weight_SF_N_Jets__ttcc_SL__btag_LSTAT2Up:=(((N_Jets==4)*0.999580025673)+((N_Jets==5)*0.999686062336)+((N_Jets==6)*1.00027751923)+((N_Jets==7)*1.00101423264)+((N_Jets==8)*1.0007430315)+((N_Jets>=9)*1.00121378899))",
        "weight_SF_N_Jets__ttcc_SL__btag_LSTAT2Down:=(((N_Jets==4)*1.0003246069)+((N_Jets==5)*1.00022614002)+((N_Jets==6)*0.999665617943)+((N_Jets==7)*0.998909950256)+((N_Jets==8)*0.999160587788)+((N_Jets>=9)*0.998748242855))",
        "weight_SF_N_Jets__ttcc_SL__btag_CERR1Up:=(((N_Jets==4)*0.995244503021)+((N_Jets==5)*1.00090503693)+((N_Jets==6)*1.00278413296)+((N_Jets==7)*1.01010274887)+((N_Jets==8)*1.03559553623)+((N_Jets>=9)*1.0121537447))",
        "weight_SF_N_Jets__ttcc_SL__btag_CERR1Down:=(((N_Jets==4)*1.00817978382)+((N_Jets==5)*0.998087346554)+((N_Jets==6)*0.995640695095)+((N_Jets==7)*0.983329534531)+((N_Jets==8)*0.940536618233)+((N_Jets>=9)*0.966482162476))",
        "weight_SF_N_Jets__ttcc_SL__btag_CERR2Up:=(((N_Jets==4)*0.994798123837)+((N_Jets==5)*0.999783635139)+((N_Jets==6)*1.00185072422)+((N_Jets==7)*1.00701904297)+((N_Jets==8)*1.02778339386)+((N_Jets>=9)*1.00790536404))",
        "weight_SF_N_Jets__ttcc_SL__btag_CERR2Down:=(((N_Jets==4)*1.00725209713)+((N_Jets==5)*1.00015580654)+((N_Jets==6)*0.997685134411)+((N_Jets==7)*0.990759313107)+((N_Jets==8)*0.961113452911)+((N_Jets>=9)*0.982986450195))",
        "weight_SF_N_Jets__ttcc_SL__btag_NOMINAL:=(((N_Jets==4)*0.971940457821)+((N_Jets==5)*0.947355091572)+((N_Jets==6)*0.909967720509)+((N_Jets==7)*0.858635127544)+((N_Jets==8)*0.796678900719)+((N_Jets>=9)*0.762499213219))",

        "weight_SF_N_Jets__ttcc_DL__btag_LPURITYUp:=(((N_Jets==4)*0.983060419559)+((N_Jets==5)*0.98479861021)+((N_Jets==6)*0.985175430775)+((N_Jets==7)*0.984267532825)+((N_Jets==8)*0.981015205383)+((N_Jets>=9)*0.979294002056))",
        "weight_SF_N_Jets__ttcc_DL__btag_LPURITYDown:=(((N_Jets==4)*1.01736068726)+((N_Jets==5)*1.01560723782)+((N_Jets==6)*1.01481509209)+((N_Jets==7)*1.01611697674)+((N_Jets==8)*1.02048230171)+((N_Jets>=9)*1.02149009705))",
        "weight_SF_N_Jets__ttcc_DL__btag_BPURITYUp:=(((N_Jets==4)*1.00998401642)+((N_Jets==5)*1.01575243473)+((N_Jets==6)*1.01599311829)+((N_Jets==7)*1.02079212666)+((N_Jets==8)*1.02562570572)+((N_Jets>=9)*1.06143558025))",
        "weight_SF_N_Jets__ttcc_DL__btag_BPURITYDown:=(((N_Jets==4)*0.990217447281)+((N_Jets==5)*0.984700024128)+((N_Jets==6)*0.984234988689)+((N_Jets==7)*0.980790793896)+((N_Jets==8)*0.976577222347)+((N_Jets>=9)*0.954575657845))",
        "weight_SF_N_Jets__ttcc_DL__btag_BSTAT1Up:=(((N_Jets==4)*1.00301456451)+((N_Jets==5)*1.00255548954)+((N_Jets==6)*1.00294172764)+((N_Jets==7)*1.00306689739)+((N_Jets==8)*1.00344097614)+((N_Jets>=9)*1.00341105461))",
        "weight_SF_N_Jets__ttcc_DL__btag_BSTAT1Down:=(((N_Jets==4)*0.996957182884)+((N_Jets==5)*0.997476041317)+((N_Jets==6)*0.997083306313)+((N_Jets==7)*0.996923625469)+((N_Jets==8)*0.996603906155)+((N_Jets>=9)*0.996611714363))",
        "weight_SF_N_Jets__ttcc_DL__btag_LSTAT1Up:=(((N_Jets==4)*0.998849570751)+((N_Jets==5)*0.999252855778)+((N_Jets==6)*0.999446690083)+((N_Jets==7)*0.999190270901)+((N_Jets==8)*0.998338758945)+((N_Jets>=9)*0.997942626476))",
        "weight_SF_N_Jets__ttcc_DL__btag_LSTAT1Down:=(((N_Jets==4)*1.00106215477)+((N_Jets==5)*1.00065302849)+((N_Jets==6)*1.00055813789)+((N_Jets==7)*1.00078094006)+((N_Jets==8)*1.00138556957)+((N_Jets>=9)*1.00195300579))",
        "weight_SF_N_Jets__ttcc_DL__btag_BSTAT2Up:=(((N_Jets==4)*1.00047791004)+((N_Jets==5)*1.00060021877)+((N_Jets==6)*1.00048673153)+((N_Jets==7)*1.00084936619)+((N_Jets==8)*1.00098335743)+((N_Jets>=9)*1.00195360184))",
        "weight_SF_N_Jets__ttcc_DL__btag_BSTAT2Down:=(((N_Jets==4)*0.99946975708)+((N_Jets==5)*0.999412596226)+((N_Jets==6)*0.999512851238)+((N_Jets==7)*0.99913674593)+((N_Jets==8)*0.998990178108)+((N_Jets>=9)*0.998047947884))",
        "weight_SF_N_Jets__ttcc_DL__btag_LSTAT2Up:=(((N_Jets==4)*1.00029337406)+((N_Jets==5)*1.00117015839)+((N_Jets==6)*1.00166225433)+((N_Jets==7)*1.00172388554)+((N_Jets==8)*1.00081837177)+((N_Jets>=9)*1.00305950642))",
        "weight_SF_N_Jets__ttcc_DL__btag_LSTAT2Down:=(((N_Jets==4)*0.999588906765)+((N_Jets==5)*0.998731255531)+((N_Jets==6)*0.998256325722)+((N_Jets==7)*0.99816429615)+((N_Jets==8)*0.999065458775)+((N_Jets>=9)*0.996667206287))",
        "weight_SF_N_Jets__ttcc_DL__btag_CERR1Up:=(((N_Jets==4)*1.00207591057)+((N_Jets==5)*1.00782084465)+((N_Jets==6)*1.01277410984)+((N_Jets==7)*1.00699901581)+((N_Jets==8)*1.01214766502)+((N_Jets>=9)*1.05382692814))",
        "weight_SF_N_Jets__ttcc_DL__btag_CERR1Down:=(((N_Jets==4)*0.996021389961)+((N_Jets==5)*0.9872392416)+((N_Jets==6)*0.978136360645)+((N_Jets==7)*0.988334000111)+((N_Jets==8)*0.976546406746)+((N_Jets>=9)*0.922919273376))",
        "weight_SF_N_Jets__ttcc_DL__btag_CERR2Up:=(((N_Jets==4)*1.00050830841)+((N_Jets==5)*1.00473248959)+((N_Jets==6)*1.01015675068)+((N_Jets==7)*1.00359773636)+((N_Jets==8)*1.00929176807)+((N_Jets>=9)*1.04493355751))",
        "weight_SF_N_Jets__ttcc_DL__btag_CERR2Down:=(((N_Jets==4)*0.999056100845)+((N_Jets==5)*0.993781268597)+((N_Jets==6)*0.985786437988)+((N_Jets==7)*0.99535626173)+((N_Jets==8)*0.986618876457)+((N_Jets>=9)*0.945965707302))",
        "weight_SF_N_Jets__ttcc_DL__btag_NOMINAL:=(((N_Jets==4)*0.922974050045)+((N_Jets==5)*0.872450113297)+((N_Jets==6)*0.831920564175)+((N_Jets==7)*0.803282439709)+((N_Jets==8)*0.745712816715)+((N_Jets>=9)*0.661658942699))",

        "weight_SF_N_Jets__ttcc_FH__btag_LPURITYUp:=(((N_Jets==4)*0.98920494318)+((N_Jets==5)*0.98742544651)+((N_Jets==6)*0.984015643597)+((N_Jets==7)*0.983183443546)+((N_Jets==8)*0.985076129436)+((N_Jets>=9)*0.982397675514))",
        "weight_SF_N_Jets__ttcc_FH__btag_LPURITYDown:=(((N_Jets==4)*1.01107883453)+((N_Jets==5)*1.01295185089)+((N_Jets==6)*1.0166311264)+((N_Jets==7)*1.0172598362)+((N_Jets==8)*1.01490998268)+((N_Jets>=9)*1.01828825474))",
        "weight_SF_N_Jets__ttcc_FH__btag_BPURITYUp:=(((N_Jets==4)*0.996570289135)+((N_Jets==5)*0.99574637413)+((N_Jets==6)*0.9940341115)+((N_Jets==7)*0.994334340096)+((N_Jets==8)*0.995412945747)+((N_Jets>=9)*0.991472125053))",
        "weight_SF_N_Jets__ttcc_FH__btag_BPURITYDown:=(((N_Jets==4)*1.00356841087)+((N_Jets==5)*1.00453305244)+((N_Jets==6)*1.00620687008)+((N_Jets==7)*1.00610136986)+((N_Jets==8)*1.00461792946)+((N_Jets>=9)*1.00859618187))",
        "weight_SF_N_Jets__ttcc_FH__btag_BSTAT1Up:=(((N_Jets==4)*1.00189244747)+((N_Jets==5)*1.00239610672)+((N_Jets==6)*1.00291740894)+((N_Jets==7)*1.00311982632)+((N_Jets==8)*1.00266695023)+((N_Jets>=9)*1.00305902958))",
        "weight_SF_N_Jets__ttcc_FH__btag_BSTAT1Down:=(((N_Jets==4)*0.99816429615)+((N_Jets==5)*0.997681736946)+((N_Jets==6)*0.997151553631)+((N_Jets==7)*0.996918618679)+((N_Jets==8)*0.997351646423)+((N_Jets>=9)*0.99695712328))",
        "weight_SF_N_Jets__ttcc_FH__btag_LSTAT1Up:=(((N_Jets==4)*1.00018775463)+((N_Jets==5)*1.00029313564)+((N_Jets==6)*1.00005829334)+((N_Jets==7)*1.0002733469)+((N_Jets==8)*1.00056254864)+((N_Jets>=9)*0.999760329723))",
        "weight_SF_N_Jets__ttcc_FH__btag_LSTAT1Down:=(((N_Jets==4)*0.999824941158)+((N_Jets==5)*0.999719083309)+((N_Jets==6)*0.999938070774)+((N_Jets==7)*0.999688506126)+((N_Jets==8)*0.999377191067)+((N_Jets>=9)*1.00022661686))",
        "weight_SF_N_Jets__ttcc_FH__btag_BSTAT2Up:=(((N_Jets==4)*1.00024139881)+((N_Jets==5)*1.00018656254)+((N_Jets==6)*1.00008261204)+((N_Jets==7)*1.00008773804)+((N_Jets==8)*1.00059568882)+((N_Jets>=9)*1.00042200089))",
        "weight_SF_N_Jets__ttcc_FH__btag_BSTAT2Down:=(((N_Jets==4)*0.999805212021)+((N_Jets==5)*0.999865472317)+((N_Jets==6)*0.999963760376)+((N_Jets==7)*0.999925911427)+((N_Jets==8)*0.999388039112)+((N_Jets>=9)*0.999570667744))",
        "weight_SF_N_Jets__ttcc_FH__btag_LSTAT2Up:=(((N_Jets==4)*0.99969959259)+((N_Jets==5)*0.999669492245)+((N_Jets==6)*0.999304294586)+((N_Jets==7)*0.999398350716)+((N_Jets==8)*0.999791443348)+((N_Jets>=9)*0.998814642429))",
        "weight_SF_N_Jets__ttcc_FH__btag_LSTAT2Down:=(((N_Jets==4)*1.00033950806)+((N_Jets==5)*1.00037848949)+((N_Jets==6)*1.00074660778)+((N_Jets==7)*1.00059938431)+((N_Jets==8)*1.00019586086)+((N_Jets>=9)*1.00122010708))",
        "weight_SF_N_Jets__ttcc_FH__btag_CERR1Up:=(((N_Jets==4)*0.989148736)+((N_Jets==5)*0.989208877087)+((N_Jets==6)*0.996788322926)+((N_Jets==7)*0.998180091381)+((N_Jets==8)*1.00027894974)+((N_Jets>=9)*0.996642649174))",
        "weight_SF_N_Jets__ttcc_FH__btag_CERR1Down:=(((N_Jets==4)*1.01939582825)+((N_Jets==5)*1.01954102516)+((N_Jets==6)*1.00625252724)+((N_Jets==7)*1.00338423252)+((N_Jets==8)*1.00209891796)+((N_Jets>=9)*1.00712680817))",
        "weight_SF_N_Jets__ttcc_FH__btag_CERR2Up:=(((N_Jets==4)*0.98969745636)+((N_Jets==5)*0.990081965923)+((N_Jets==6)*0.99596452713)+((N_Jets==7)*0.997798323631)+((N_Jets==8)*0.999787688255)+((N_Jets>=9)*0.997242331505))",
        "weight_SF_N_Jets__ttcc_FH__btag_CERR2Down:=(((N_Jets==4)*1.01478517056)+((N_Jets==5)*1.01443731785)+((N_Jets==6)*1.00598239899)+((N_Jets==7)*1.00324547291)+((N_Jets==8)*1.00183784962)+((N_Jets>=9)*1.00468981266))",
        "weight_SF_N_Jets__ttcc_FH__btag_NOMINAL:=(((N_Jets==4)*0.989679336548)+((N_Jets==5)*0.983271300793)+((N_Jets==6)*0.968236744404)+((N_Jets==7)*0.946002781391)+((N_Jets==8)*0.887506663799)+((N_Jets>=9)*0.833955407143))",






        "sf_N_Jets__ttH__btag_LPURITYUp:=((selection_hbb*weight_SF_N_Jets__ttH_bb__btag_LPURITYUp)+(selection_nonhbb*weight_SF_N_Jets__ttH_nonbb__btag_LPURITYUp))",
        "sf_N_Jets__ttbb__btag_LPURITYUp:=((selection_ttdl*selection_ttb*weight_SF_N_Jets__ttb_4FS_DL__btag_LPURITYUp)+(selection_ttdl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_DL__btag_LPURITYUp)+(selection_ttdl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_DL__btag_LPURITYUp)+(selection_ttsl*selection_ttb*weight_SF_N_Jets__ttb_4FS_SL__btag_LPURITYUp)+(selection_ttsl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_SL__btag_LPURITYUp)+(selection_ttsl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_SL__btag_LPURITYUp)+(selection_ttfh*selection_ttb*weight_SF_N_Jets__ttb_4FS_FH__btag_LPURITYUp)+(selection_ttfh*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_FH__btag_LPURITYUp)+(selection_ttfh*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_FH__btag_LPURITYUp))",
        "sf_N_Jets__ttcc__btag_LPURITYUp:=((selection_ttdl*selection_ttcc*weight_SF_N_Jets__ttcc_DL__btag_LPURITYUp)+(selection_ttsl*selection_ttcc*weight_SF_N_Jets__ttcc_SL__btag_LPURITYUp)+(selection_ttfh*selection_ttcc*weight_SF_N_Jets__ttcc_FH__btag_LPURITYUp))",
        "sf_N_Jets__ttlf__btag_LPURITYUp:=((selection_ttdl*selection_ttlf*weight_SF_N_Jets__ttlf_DL__btag_LPURITYUp)+(selection_ttsl*selection_ttlf*weight_SF_N_Jets__ttlf_SL__btag_LPURITYUp)+(selection_ttfh*selection_ttlf*weight_SF_N_Jets__ttlf_FH__btag_LPURITYUp))",

        "sf_N_Jets__btag_LPURITYUp:=((isTTbarSample==1)*(sf_N_Jets__ttlf__btag_LPURITYUp+sf_N_Jets__ttcc__btag_LPURITYUp+sf_N_Jets__ttbb__btag_LPURITYUp)+(isTthSample==1)*(sf_N_Jets__ttH__btag_LPURITYUp)+(isTTbarSample==0&&isTthSample==0)*(1.))",





        "sf_N_Jets__ttH__btag_LPURITYDown:=((selection_hbb*weight_SF_N_Jets__ttH_bb__btag_LPURITYDown)+(selection_nonhbb*weight_SF_N_Jets__ttH_nonbb__btag_LPURITYDown))",
        "sf_N_Jets__ttbb__btag_LPURITYDown:=((selection_ttdl*selection_ttb*weight_SF_N_Jets__ttb_4FS_DL__btag_LPURITYDown)+(selection_ttdl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_DL__btag_LPURITYDown)+(selection_ttdl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_DL__btag_LPURITYDown)+(selection_ttsl*selection_ttb*weight_SF_N_Jets__ttb_4FS_SL__btag_LPURITYDown)+(selection_ttsl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_SL__btag_LPURITYDown)+(selection_ttsl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_SL__btag_LPURITYDown)+(selection_ttfh*selection_ttb*weight_SF_N_Jets__ttb_4FS_FH__btag_LPURITYDown)+(selection_ttfh*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_FH__btag_LPURITYDown)+(selection_ttfh*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_FH__btag_LPURITYDown))",
        "sf_N_Jets__ttcc__btag_LPURITYDown:=((selection_ttdl*selection_ttcc*weight_SF_N_Jets__ttcc_DL__btag_LPURITYDown)+(selection_ttsl*selection_ttcc*weight_SF_N_Jets__ttcc_SL__btag_LPURITYDown)+(selection_ttfh*selection_ttcc*weight_SF_N_Jets__ttcc_FH__btag_LPURITYDown))",
        "sf_N_Jets__ttlf__btag_LPURITYDown:=((selection_ttdl*selection_ttlf*weight_SF_N_Jets__ttlf_DL__btag_LPURITYDown)+(selection_ttsl*selection_ttlf*weight_SF_N_Jets__ttlf_SL__btag_LPURITYDown)+(selection_ttfh*selection_ttlf*weight_SF_N_Jets__ttlf_FH__btag_LPURITYDown))",

        "sf_N_Jets__btag_LPURITYDown:=((isTTbarSample==1)*(sf_N_Jets__ttlf__btag_LPURITYDown+sf_N_Jets__ttcc__btag_LPURITYDown+sf_N_Jets__ttbb__btag_LPURITYDown)+(isTthSample==1)*(sf_N_Jets__ttH__btag_LPURITYDown)+(isTTbarSample==0&&isTthSample==0)*(1.))",





        "sf_N_Jets__ttH__btag_BPURITYUp:=((selection_hbb*weight_SF_N_Jets__ttH_bb__btag_BPURITYUp)+(selection_nonhbb*weight_SF_N_Jets__ttH_nonbb__btag_BPURITYUp))",
        "sf_N_Jets__ttbb__btag_BPURITYUp:=((selection_ttdl*selection_ttb*weight_SF_N_Jets__ttb_4FS_DL__btag_BPURITYUp)+(selection_ttdl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_DL__btag_BPURITYUp)+(selection_ttdl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_DL__btag_BPURITYUp)+(selection_ttsl*selection_ttb*weight_SF_N_Jets__ttb_4FS_SL__btag_BPURITYUp)+(selection_ttsl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_SL__btag_BPURITYUp)+(selection_ttsl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_SL__btag_BPURITYUp)+(selection_ttfh*selection_ttb*weight_SF_N_Jets__ttb_4FS_FH__btag_BPURITYUp)+(selection_ttfh*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_FH__btag_BPURITYUp)+(selection_ttfh*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_FH__btag_BPURITYUp))",
        "sf_N_Jets__ttcc__btag_BPURITYUp:=((selection_ttdl*selection_ttcc*weight_SF_N_Jets__ttcc_DL__btag_BPURITYUp)+(selection_ttsl*selection_ttcc*weight_SF_N_Jets__ttcc_SL__btag_BPURITYUp)+(selection_ttfh*selection_ttcc*weight_SF_N_Jets__ttcc_FH__btag_BPURITYUp))",
        "sf_N_Jets__ttlf__btag_BPURITYUp:=((selection_ttdl*selection_ttlf*weight_SF_N_Jets__ttlf_DL__btag_BPURITYUp)+(selection_ttsl*selection_ttlf*weight_SF_N_Jets__ttlf_SL__btag_BPURITYUp)+(selection_ttfh*selection_ttlf*weight_SF_N_Jets__ttlf_FH__btag_BPURITYUp))",

        "sf_N_Jets__btag_BPURITYUp:=((isTTbarSample==1)*(sf_N_Jets__ttlf__btag_BPURITYUp+sf_N_Jets__ttcc__btag_BPURITYUp+sf_N_Jets__ttbb__btag_BPURITYUp)+(isTthSample==1)*(sf_N_Jets__ttH__btag_BPURITYUp)+(isTTbarSample==0&&isTthSample==0)*(1.))",





        "sf_N_Jets__ttH__btag_BPURITYDown:=((selection_hbb*weight_SF_N_Jets__ttH_bb__btag_BPURITYDown)+(selection_nonhbb*weight_SF_N_Jets__ttH_nonbb__btag_BPURITYDown))",
        "sf_N_Jets__ttbb__btag_BPURITYDown:=((selection_ttdl*selection_ttb*weight_SF_N_Jets__ttb_4FS_DL__btag_BPURITYDown)+(selection_ttdl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_DL__btag_BPURITYDown)+(selection_ttdl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_DL__btag_BPURITYDown)+(selection_ttsl*selection_ttb*weight_SF_N_Jets__ttb_4FS_SL__btag_BPURITYDown)+(selection_ttsl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_SL__btag_BPURITYDown)+(selection_ttsl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_SL__btag_BPURITYDown)+(selection_ttfh*selection_ttb*weight_SF_N_Jets__ttb_4FS_FH__btag_BPURITYDown)+(selection_ttfh*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_FH__btag_BPURITYDown)+(selection_ttfh*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_FH__btag_BPURITYDown))",
        "sf_N_Jets__ttcc__btag_BPURITYDown:=((selection_ttdl*selection_ttcc*weight_SF_N_Jets__ttcc_DL__btag_BPURITYDown)+(selection_ttsl*selection_ttcc*weight_SF_N_Jets__ttcc_SL__btag_BPURITYDown)+(selection_ttfh*selection_ttcc*weight_SF_N_Jets__ttcc_FH__btag_BPURITYDown))",
        "sf_N_Jets__ttlf__btag_BPURITYDown:=((selection_ttdl*selection_ttlf*weight_SF_N_Jets__ttlf_DL__btag_BPURITYDown)+(selection_ttsl*selection_ttlf*weight_SF_N_Jets__ttlf_SL__btag_BPURITYDown)+(selection_ttfh*selection_ttlf*weight_SF_N_Jets__ttlf_FH__btag_BPURITYDown))",

        "sf_N_Jets__btag_BPURITYDown:=((isTTbarSample==1)*(sf_N_Jets__ttlf__btag_BPURITYDown+sf_N_Jets__ttcc__btag_BPURITYDown+sf_N_Jets__ttbb__btag_BPURITYDown)+(isTthSample==1)*(sf_N_Jets__ttH__btag_BPURITYDown)+(isTTbarSample==0&&isTthSample==0)*(1.))",





        "sf_N_Jets__ttH__btag_BSTAT1Up:=((selection_hbb*weight_SF_N_Jets__ttH_bb__btag_BSTAT1Up)+(selection_nonhbb*weight_SF_N_Jets__ttH_nonbb__btag_BSTAT1Up))",
        "sf_N_Jets__ttbb__btag_BSTAT1Up:=((selection_ttdl*selection_ttb*weight_SF_N_Jets__ttb_4FS_DL__btag_BSTAT1Up)+(selection_ttdl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_DL__btag_BSTAT1Up)+(selection_ttdl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_DL__btag_BSTAT1Up)+(selection_ttsl*selection_ttb*weight_SF_N_Jets__ttb_4FS_SL__btag_BSTAT1Up)+(selection_ttsl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_SL__btag_BSTAT1Up)+(selection_ttsl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_SL__btag_BSTAT1Up)+(selection_ttfh*selection_ttb*weight_SF_N_Jets__ttb_4FS_FH__btag_BSTAT1Up)+(selection_ttfh*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_FH__btag_BSTAT1Up)+(selection_ttfh*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_FH__btag_BSTAT1Up))",
        "sf_N_Jets__ttcc__btag_BSTAT1Up:=((selection_ttdl*selection_ttcc*weight_SF_N_Jets__ttcc_DL__btag_BSTAT1Up)+(selection_ttsl*selection_ttcc*weight_SF_N_Jets__ttcc_SL__btag_BSTAT1Up)+(selection_ttfh*selection_ttcc*weight_SF_N_Jets__ttcc_FH__btag_BSTAT1Up))",
        "sf_N_Jets__ttlf__btag_BSTAT1Up:=((selection_ttdl*selection_ttlf*weight_SF_N_Jets__ttlf_DL__btag_BSTAT1Up)+(selection_ttsl*selection_ttlf*weight_SF_N_Jets__ttlf_SL__btag_BSTAT1Up)+(selection_ttfh*selection_ttlf*weight_SF_N_Jets__ttlf_FH__btag_BSTAT1Up))",

        "sf_N_Jets__btag_BSTAT1Up:=((isTTbarSample==1)*(sf_N_Jets__ttlf__btag_BSTAT1Up+sf_N_Jets__ttcc__btag_BSTAT1Up+sf_N_Jets__ttbb__btag_BSTAT1Up)+(isTthSample==1)*(sf_N_Jets__ttH__btag_BSTAT1Up)+(isTTbarSample==0&&isTthSample==0)*(1.))",





        "sf_N_Jets__ttH__btag_BSTAT1Down:=((selection_hbb*weight_SF_N_Jets__ttH_bb__btag_BSTAT1Down)+(selection_nonhbb*weight_SF_N_Jets__ttH_nonbb__btag_BSTAT1Down))",
        "sf_N_Jets__ttbb__btag_BSTAT1Down:=((selection_ttdl*selection_ttb*weight_SF_N_Jets__ttb_4FS_DL__btag_BSTAT1Down)+(selection_ttdl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_DL__btag_BSTAT1Down)+(selection_ttdl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_DL__btag_BSTAT1Down)+(selection_ttsl*selection_ttb*weight_SF_N_Jets__ttb_4FS_SL__btag_BSTAT1Down)+(selection_ttsl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_SL__btag_BSTAT1Down)+(selection_ttsl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_SL__btag_BSTAT1Down)+(selection_ttfh*selection_ttb*weight_SF_N_Jets__ttb_4FS_FH__btag_BSTAT1Down)+(selection_ttfh*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_FH__btag_BSTAT1Down)+(selection_ttfh*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_FH__btag_BSTAT1Down))",
        "sf_N_Jets__ttcc__btag_BSTAT1Down:=((selection_ttdl*selection_ttcc*weight_SF_N_Jets__ttcc_DL__btag_BSTAT1Down)+(selection_ttsl*selection_ttcc*weight_SF_N_Jets__ttcc_SL__btag_BSTAT1Down)+(selection_ttfh*selection_ttcc*weight_SF_N_Jets__ttcc_FH__btag_BSTAT1Down))",
        "sf_N_Jets__ttlf__btag_BSTAT1Down:=((selection_ttdl*selection_ttlf*weight_SF_N_Jets__ttlf_DL__btag_BSTAT1Down)+(selection_ttsl*selection_ttlf*weight_SF_N_Jets__ttlf_SL__btag_BSTAT1Down)+(selection_ttfh*selection_ttlf*weight_SF_N_Jets__ttlf_FH__btag_BSTAT1Down))",

        "sf_N_Jets__btag_BSTAT1Down:=((isTTbarSample==1)*(sf_N_Jets__ttlf__btag_BSTAT1Down+sf_N_Jets__ttcc__btag_BSTAT1Down+sf_N_Jets__ttbb__btag_BSTAT1Down)+(isTthSample==1)*(sf_N_Jets__ttH__btag_BSTAT1Down)+(isTTbarSample==0&&isTthSample==0)*(1.))",





        "sf_N_Jets__ttH__btag_LSTAT1Up:=((selection_hbb*weight_SF_N_Jets__ttH_bb__btag_LSTAT1Up)+(selection_nonhbb*weight_SF_N_Jets__ttH_nonbb__btag_LSTAT1Up))",
        "sf_N_Jets__ttbb__btag_LSTAT1Up:=((selection_ttdl*selection_ttb*weight_SF_N_Jets__ttb_4FS_DL__btag_LSTAT1Up)+(selection_ttdl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_DL__btag_LSTAT1Up)+(selection_ttdl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_DL__btag_LSTAT1Up)+(selection_ttsl*selection_ttb*weight_SF_N_Jets__ttb_4FS_SL__btag_LSTAT1Up)+(selection_ttsl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_SL__btag_LSTAT1Up)+(selection_ttsl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_SL__btag_LSTAT1Up)+(selection_ttfh*selection_ttb*weight_SF_N_Jets__ttb_4FS_FH__btag_LSTAT1Up)+(selection_ttfh*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_FH__btag_LSTAT1Up)+(selection_ttfh*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_FH__btag_LSTAT1Up))",
        "sf_N_Jets__ttcc__btag_LSTAT1Up:=((selection_ttdl*selection_ttcc*weight_SF_N_Jets__ttcc_DL__btag_LSTAT1Up)+(selection_ttsl*selection_ttcc*weight_SF_N_Jets__ttcc_SL__btag_LSTAT1Up)+(selection_ttfh*selection_ttcc*weight_SF_N_Jets__ttcc_FH__btag_LSTAT1Up))",
        "sf_N_Jets__ttlf__btag_LSTAT1Up:=((selection_ttdl*selection_ttlf*weight_SF_N_Jets__ttlf_DL__btag_LSTAT1Up)+(selection_ttsl*selection_ttlf*weight_SF_N_Jets__ttlf_SL__btag_LSTAT1Up)+(selection_ttfh*selection_ttlf*weight_SF_N_Jets__ttlf_FH__btag_LSTAT1Up))",

        "sf_N_Jets__btag_LSTAT1Up:=((isTTbarSample==1)*(sf_N_Jets__ttlf__btag_LSTAT1Up+sf_N_Jets__ttcc__btag_LSTAT1Up+sf_N_Jets__ttbb__btag_LSTAT1Up)+(isTthSample==1)*(sf_N_Jets__ttH__btag_LSTAT1Up)+(isTTbarSample==0&&isTthSample==0)*(1.))",





        "sf_N_Jets__ttH__btag_LSTAT1Down:=((selection_hbb*weight_SF_N_Jets__ttH_bb__btag_LSTAT1Down)+(selection_nonhbb*weight_SF_N_Jets__ttH_nonbb__btag_LSTAT1Down))",
        "sf_N_Jets__ttbb__btag_LSTAT1Down:=((selection_ttdl*selection_ttb*weight_SF_N_Jets__ttb_4FS_DL__btag_LSTAT1Down)+(selection_ttdl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_DL__btag_LSTAT1Down)+(selection_ttdl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_DL__btag_LSTAT1Down)+(selection_ttsl*selection_ttb*weight_SF_N_Jets__ttb_4FS_SL__btag_LSTAT1Down)+(selection_ttsl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_SL__btag_LSTAT1Down)+(selection_ttsl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_SL__btag_LSTAT1Down)+(selection_ttfh*selection_ttb*weight_SF_N_Jets__ttb_4FS_FH__btag_LSTAT1Down)+(selection_ttfh*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_FH__btag_LSTAT1Down)+(selection_ttfh*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_FH__btag_LSTAT1Down))",
        "sf_N_Jets__ttcc__btag_LSTAT1Down:=((selection_ttdl*selection_ttcc*weight_SF_N_Jets__ttcc_DL__btag_LSTAT1Down)+(selection_ttsl*selection_ttcc*weight_SF_N_Jets__ttcc_SL__btag_LSTAT1Down)+(selection_ttfh*selection_ttcc*weight_SF_N_Jets__ttcc_FH__btag_LSTAT1Down))",
        "sf_N_Jets__ttlf__btag_LSTAT1Down:=((selection_ttdl*selection_ttlf*weight_SF_N_Jets__ttlf_DL__btag_LSTAT1Down)+(selection_ttsl*selection_ttlf*weight_SF_N_Jets__ttlf_SL__btag_LSTAT1Down)+(selection_ttfh*selection_ttlf*weight_SF_N_Jets__ttlf_FH__btag_LSTAT1Down))",

        "sf_N_Jets__btag_LSTAT1Down:=((isTTbarSample==1)*(sf_N_Jets__ttlf__btag_LSTAT1Down+sf_N_Jets__ttcc__btag_LSTAT1Down+sf_N_Jets__ttbb__btag_LSTAT1Down)+(isTthSample==1)*(sf_N_Jets__ttH__btag_LSTAT1Down)+(isTTbarSample==0&&isTthSample==0)*(1.))",





        "sf_N_Jets__ttH__btag_BSTAT2Up:=((selection_hbb*weight_SF_N_Jets__ttH_bb__btag_BSTAT2Up)+(selection_nonhbb*weight_SF_N_Jets__ttH_nonbb__btag_BSTAT2Up))",
        "sf_N_Jets__ttbb__btag_BSTAT2Up:=((selection_ttdl*selection_ttb*weight_SF_N_Jets__ttb_4FS_DL__btag_BSTAT2Up)+(selection_ttdl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_DL__btag_BSTAT2Up)+(selection_ttdl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_DL__btag_BSTAT2Up)+(selection_ttsl*selection_ttb*weight_SF_N_Jets__ttb_4FS_SL__btag_BSTAT2Up)+(selection_ttsl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_SL__btag_BSTAT2Up)+(selection_ttsl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_SL__btag_BSTAT2Up)+(selection_ttfh*selection_ttb*weight_SF_N_Jets__ttb_4FS_FH__btag_BSTAT2Up)+(selection_ttfh*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_FH__btag_BSTAT2Up)+(selection_ttfh*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_FH__btag_BSTAT2Up))",
        "sf_N_Jets__ttcc__btag_BSTAT2Up:=((selection_ttdl*selection_ttcc*weight_SF_N_Jets__ttcc_DL__btag_BSTAT2Up)+(selection_ttsl*selection_ttcc*weight_SF_N_Jets__ttcc_SL__btag_BSTAT2Up)+(selection_ttfh*selection_ttcc*weight_SF_N_Jets__ttcc_FH__btag_BSTAT2Up))",
        "sf_N_Jets__ttlf__btag_BSTAT2Up:=((selection_ttdl*selection_ttlf*weight_SF_N_Jets__ttlf_DL__btag_BSTAT2Up)+(selection_ttsl*selection_ttlf*weight_SF_N_Jets__ttlf_SL__btag_BSTAT2Up)+(selection_ttfh*selection_ttlf*weight_SF_N_Jets__ttlf_FH__btag_BSTAT2Up))",

        "sf_N_Jets__btag_BSTAT2Up:=((isTTbarSample==1)*(sf_N_Jets__ttlf__btag_BSTAT2Up+sf_N_Jets__ttcc__btag_BSTAT2Up+sf_N_Jets__ttbb__btag_BSTAT2Up)+(isTthSample==1)*(sf_N_Jets__ttH__btag_BSTAT2Up)+(isTTbarSample==0&&isTthSample==0)*(1.))",





        "sf_N_Jets__ttH__btag_BSTAT2Down:=((selection_hbb*weight_SF_N_Jets__ttH_bb__btag_BSTAT2Down)+(selection_nonhbb*weight_SF_N_Jets__ttH_nonbb__btag_BSTAT2Down))",
        "sf_N_Jets__ttbb__btag_BSTAT2Down:=((selection_ttdl*selection_ttb*weight_SF_N_Jets__ttb_4FS_DL__btag_BSTAT2Down)+(selection_ttdl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_DL__btag_BSTAT2Down)+(selection_ttdl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_DL__btag_BSTAT2Down)+(selection_ttsl*selection_ttb*weight_SF_N_Jets__ttb_4FS_SL__btag_BSTAT2Down)+(selection_ttsl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_SL__btag_BSTAT2Down)+(selection_ttsl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_SL__btag_BSTAT2Down)+(selection_ttfh*selection_ttb*weight_SF_N_Jets__ttb_4FS_FH__btag_BSTAT2Down)+(selection_ttfh*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_FH__btag_BSTAT2Down)+(selection_ttfh*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_FH__btag_BSTAT2Down))",
        "sf_N_Jets__ttcc__btag_BSTAT2Down:=((selection_ttdl*selection_ttcc*weight_SF_N_Jets__ttcc_DL__btag_BSTAT2Down)+(selection_ttsl*selection_ttcc*weight_SF_N_Jets__ttcc_SL__btag_BSTAT2Down)+(selection_ttfh*selection_ttcc*weight_SF_N_Jets__ttcc_FH__btag_BSTAT2Down))",
        "sf_N_Jets__ttlf__btag_BSTAT2Down:=((selection_ttdl*selection_ttlf*weight_SF_N_Jets__ttlf_DL__btag_BSTAT2Down)+(selection_ttsl*selection_ttlf*weight_SF_N_Jets__ttlf_SL__btag_BSTAT2Down)+(selection_ttfh*selection_ttlf*weight_SF_N_Jets__ttlf_FH__btag_BSTAT2Down))",

        "sf_N_Jets__btag_BSTAT2Down:=((isTTbarSample==1)*(sf_N_Jets__ttlf__btag_BSTAT2Down+sf_N_Jets__ttcc__btag_BSTAT2Down+sf_N_Jets__ttbb__btag_BSTAT2Down)+(isTthSample==1)*(sf_N_Jets__ttH__btag_BSTAT2Down)+(isTTbarSample==0&&isTthSample==0)*(1.))",





        "sf_N_Jets__ttH__btag_LSTAT2Up:=((selection_hbb*weight_SF_N_Jets__ttH_bb__btag_LSTAT2Up)+(selection_nonhbb*weight_SF_N_Jets__ttH_nonbb__btag_LSTAT2Up))",
        "sf_N_Jets__ttbb__btag_LSTAT2Up:=((selection_ttdl*selection_ttb*weight_SF_N_Jets__ttb_4FS_DL__btag_LSTAT2Up)+(selection_ttdl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_DL__btag_LSTAT2Up)+(selection_ttdl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_DL__btag_LSTAT2Up)+(selection_ttsl*selection_ttb*weight_SF_N_Jets__ttb_4FS_SL__btag_LSTAT2Up)+(selection_ttsl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_SL__btag_LSTAT2Up)+(selection_ttsl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_SL__btag_LSTAT2Up)+(selection_ttfh*selection_ttb*weight_SF_N_Jets__ttb_4FS_FH__btag_LSTAT2Up)+(selection_ttfh*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_FH__btag_LSTAT2Up)+(selection_ttfh*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_FH__btag_LSTAT2Up))",
        "sf_N_Jets__ttcc__btag_LSTAT2Up:=((selection_ttdl*selection_ttcc*weight_SF_N_Jets__ttcc_DL__btag_LSTAT2Up)+(selection_ttsl*selection_ttcc*weight_SF_N_Jets__ttcc_SL__btag_LSTAT2Up)+(selection_ttfh*selection_ttcc*weight_SF_N_Jets__ttcc_FH__btag_LSTAT2Up))",
        "sf_N_Jets__ttlf__btag_LSTAT2Up:=((selection_ttdl*selection_ttlf*weight_SF_N_Jets__ttlf_DL__btag_LSTAT2Up)+(selection_ttsl*selection_ttlf*weight_SF_N_Jets__ttlf_SL__btag_LSTAT2Up)+(selection_ttfh*selection_ttlf*weight_SF_N_Jets__ttlf_FH__btag_LSTAT2Up))",

        "sf_N_Jets__btag_LSTAT2Up:=((isTTbarSample==1)*(sf_N_Jets__ttlf__btag_LSTAT2Up+sf_N_Jets__ttcc__btag_LSTAT2Up+sf_N_Jets__ttbb__btag_LSTAT2Up)+(isTthSample==1)*(sf_N_Jets__ttH__btag_LSTAT2Up)+(isTTbarSample==0&&isTthSample==0)*(1.))",





        "sf_N_Jets__ttH__btag_LSTAT2Down:=((selection_hbb*weight_SF_N_Jets__ttH_bb__btag_LSTAT2Down)+(selection_nonhbb*weight_SF_N_Jets__ttH_nonbb__btag_LSTAT2Down))",
        "sf_N_Jets__ttbb__btag_LSTAT2Down:=((selection_ttdl*selection_ttb*weight_SF_N_Jets__ttb_4FS_DL__btag_LSTAT2Down)+(selection_ttdl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_DL__btag_LSTAT2Down)+(selection_ttdl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_DL__btag_LSTAT2Down)+(selection_ttsl*selection_ttb*weight_SF_N_Jets__ttb_4FS_SL__btag_LSTAT2Down)+(selection_ttsl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_SL__btag_LSTAT2Down)+(selection_ttsl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_SL__btag_LSTAT2Down)+(selection_ttfh*selection_ttb*weight_SF_N_Jets__ttb_4FS_FH__btag_LSTAT2Down)+(selection_ttfh*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_FH__btag_LSTAT2Down)+(selection_ttfh*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_FH__btag_LSTAT2Down))",
        "sf_N_Jets__ttcc__btag_LSTAT2Down:=((selection_ttdl*selection_ttcc*weight_SF_N_Jets__ttcc_DL__btag_LSTAT2Down)+(selection_ttsl*selection_ttcc*weight_SF_N_Jets__ttcc_SL__btag_LSTAT2Down)+(selection_ttfh*selection_ttcc*weight_SF_N_Jets__ttcc_FH__btag_LSTAT2Down))",
        "sf_N_Jets__ttlf__btag_LSTAT2Down:=((selection_ttdl*selection_ttlf*weight_SF_N_Jets__ttlf_DL__btag_LSTAT2Down)+(selection_ttsl*selection_ttlf*weight_SF_N_Jets__ttlf_SL__btag_LSTAT2Down)+(selection_ttfh*selection_ttlf*weight_SF_N_Jets__ttlf_FH__btag_LSTAT2Down))",

        "sf_N_Jets__btag_LSTAT2Down:=((isTTbarSample==1)*(sf_N_Jets__ttlf__btag_LSTAT2Down+sf_N_Jets__ttcc__btag_LSTAT2Down+sf_N_Jets__ttbb__btag_LSTAT2Down)+(isTthSample==1)*(sf_N_Jets__ttH__btag_LSTAT2Down)+(isTTbarSample==0&&isTthSample==0)*(1.))",





        "sf_N_Jets__ttH__btag_CERR1Up:=((selection_hbb*weight_SF_N_Jets__ttH_bb__btag_CERR1Up)+(selection_nonhbb*weight_SF_N_Jets__ttH_nonbb__btag_CERR1Up))",
        "sf_N_Jets__ttbb__btag_CERR1Up:=((selection_ttdl*selection_ttb*weight_SF_N_Jets__ttb_4FS_DL__btag_CERR1Up)+(selection_ttdl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_DL__btag_CERR1Up)+(selection_ttdl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_DL__btag_CERR1Up)+(selection_ttsl*selection_ttb*weight_SF_N_Jets__ttb_4FS_SL__btag_CERR1Up)+(selection_ttsl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_SL__btag_CERR1Up)+(selection_ttsl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_SL__btag_CERR1Up)+(selection_ttfh*selection_ttb*weight_SF_N_Jets__ttb_4FS_FH__btag_CERR1Up)+(selection_ttfh*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_FH__btag_CERR1Up)+(selection_ttfh*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_FH__btag_CERR1Up))",
        "sf_N_Jets__ttcc__btag_CERR1Up:=((selection_ttdl*selection_ttcc*weight_SF_N_Jets__ttcc_DL__btag_CERR1Up)+(selection_ttsl*selection_ttcc*weight_SF_N_Jets__ttcc_SL__btag_CERR1Up)+(selection_ttfh*selection_ttcc*weight_SF_N_Jets__ttcc_FH__btag_CERR1Up))",
        "sf_N_Jets__ttlf__btag_CERR1Up:=((selection_ttdl*selection_ttlf*weight_SF_N_Jets__ttlf_DL__btag_CERR1Up)+(selection_ttsl*selection_ttlf*weight_SF_N_Jets__ttlf_SL__btag_CERR1Up)+(selection_ttfh*selection_ttlf*weight_SF_N_Jets__ttlf_FH__btag_CERR1Up))",

        "sf_N_Jets__btag_CERR1Up:=((isTTbarSample==1)*(sf_N_Jets__ttlf__btag_CERR1Up+sf_N_Jets__ttcc__btag_CERR1Up+sf_N_Jets__ttbb__btag_CERR1Up)+(isTthSample==1)*(sf_N_Jets__ttH__btag_CERR1Up)+(isTTbarSample==0&&isTthSample==0)*(1.))",





        "sf_N_Jets__ttH__btag_CERR1Down:=((selection_hbb*weight_SF_N_Jets__ttH_bb__btag_CERR1Down)+(selection_nonhbb*weight_SF_N_Jets__ttH_nonbb__btag_CERR1Down))",
        "sf_N_Jets__ttbb__btag_CERR1Down:=((selection_ttdl*selection_ttb*weight_SF_N_Jets__ttb_4FS_DL__btag_CERR1Down)+(selection_ttdl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_DL__btag_CERR1Down)+(selection_ttdl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_DL__btag_CERR1Down)+(selection_ttsl*selection_ttb*weight_SF_N_Jets__ttb_4FS_SL__btag_CERR1Down)+(selection_ttsl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_SL__btag_CERR1Down)+(selection_ttsl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_SL__btag_CERR1Down)+(selection_ttfh*selection_ttb*weight_SF_N_Jets__ttb_4FS_FH__btag_CERR1Down)+(selection_ttfh*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_FH__btag_CERR1Down)+(selection_ttfh*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_FH__btag_CERR1Down))",
        "sf_N_Jets__ttcc__btag_CERR1Down:=((selection_ttdl*selection_ttcc*weight_SF_N_Jets__ttcc_DL__btag_CERR1Down)+(selection_ttsl*selection_ttcc*weight_SF_N_Jets__ttcc_SL__btag_CERR1Down)+(selection_ttfh*selection_ttcc*weight_SF_N_Jets__ttcc_FH__btag_CERR1Down))",
        "sf_N_Jets__ttlf__btag_CERR1Down:=((selection_ttdl*selection_ttlf*weight_SF_N_Jets__ttlf_DL__btag_CERR1Down)+(selection_ttsl*selection_ttlf*weight_SF_N_Jets__ttlf_SL__btag_CERR1Down)+(selection_ttfh*selection_ttlf*weight_SF_N_Jets__ttlf_FH__btag_CERR1Down))",

        "sf_N_Jets__btag_CERR1Down:=((isTTbarSample==1)*(sf_N_Jets__ttlf__btag_CERR1Down+sf_N_Jets__ttcc__btag_CERR1Down+sf_N_Jets__ttbb__btag_CERR1Down)+(isTthSample==1)*(sf_N_Jets__ttH__btag_CERR1Down)+(isTTbarSample==0&&isTthSample==0)*(1.))",





        "sf_N_Jets__ttH__btag_CERR2Up:=((selection_hbb*weight_SF_N_Jets__ttH_bb__btag_CERR2Up)+(selection_nonhbb*weight_SF_N_Jets__ttH_nonbb__btag_CERR2Up))",
        "sf_N_Jets__ttbb__btag_CERR2Up:=((selection_ttdl*selection_ttb*weight_SF_N_Jets__ttb_4FS_DL__btag_CERR2Up)+(selection_ttdl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_DL__btag_CERR2Up)+(selection_ttdl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_DL__btag_CERR2Up)+(selection_ttsl*selection_ttb*weight_SF_N_Jets__ttb_4FS_SL__btag_CERR2Up)+(selection_ttsl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_SL__btag_CERR2Up)+(selection_ttsl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_SL__btag_CERR2Up)+(selection_ttfh*selection_ttb*weight_SF_N_Jets__ttb_4FS_FH__btag_CERR2Up)+(selection_ttfh*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_FH__btag_CERR2Up)+(selection_ttfh*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_FH__btag_CERR2Up))",
        "sf_N_Jets__ttcc__btag_CERR2Up:=((selection_ttdl*selection_ttcc*weight_SF_N_Jets__ttcc_DL__btag_CERR2Up)+(selection_ttsl*selection_ttcc*weight_SF_N_Jets__ttcc_SL__btag_CERR2Up)+(selection_ttfh*selection_ttcc*weight_SF_N_Jets__ttcc_FH__btag_CERR2Up))",
        "sf_N_Jets__ttlf__btag_CERR2Up:=((selection_ttdl*selection_ttlf*weight_SF_N_Jets__ttlf_DL__btag_CERR2Up)+(selection_ttsl*selection_ttlf*weight_SF_N_Jets__ttlf_SL__btag_CERR2Up)+(selection_ttfh*selection_ttlf*weight_SF_N_Jets__ttlf_FH__btag_CERR2Up))",

        "sf_N_Jets__btag_CERR2Up:=((isTTbarSample==1)*(sf_N_Jets__ttlf__btag_CERR2Up+sf_N_Jets__ttcc__btag_CERR2Up+sf_N_Jets__ttbb__btag_CERR2Up)+(isTthSample==1)*(sf_N_Jets__ttH__btag_CERR2Up)+(isTTbarSample==0&&isTthSample==0)*(1.))",





        "sf_N_Jets__ttH__btag_CERR2Down:=((selection_hbb*weight_SF_N_Jets__ttH_bb__btag_CERR2Down)+(selection_nonhbb*weight_SF_N_Jets__ttH_nonbb__btag_CERR2Down))",
        "sf_N_Jets__ttbb__btag_CERR2Down:=((selection_ttdl*selection_ttb*weight_SF_N_Jets__ttb_4FS_DL__btag_CERR2Down)+(selection_ttdl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_DL__btag_CERR2Down)+(selection_ttdl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_DL__btag_CERR2Down)+(selection_ttsl*selection_ttb*weight_SF_N_Jets__ttb_4FS_SL__btag_CERR2Down)+(selection_ttsl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_SL__btag_CERR2Down)+(selection_ttsl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_SL__btag_CERR2Down)+(selection_ttfh*selection_ttb*weight_SF_N_Jets__ttb_4FS_FH__btag_CERR2Down)+(selection_ttfh*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_FH__btag_CERR2Down)+(selection_ttfh*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_FH__btag_CERR2Down))",
        "sf_N_Jets__ttcc__btag_CERR2Down:=((selection_ttdl*selection_ttcc*weight_SF_N_Jets__ttcc_DL__btag_CERR2Down)+(selection_ttsl*selection_ttcc*weight_SF_N_Jets__ttcc_SL__btag_CERR2Down)+(selection_ttfh*selection_ttcc*weight_SF_N_Jets__ttcc_FH__btag_CERR2Down))",
        "sf_N_Jets__ttlf__btag_CERR2Down:=((selection_ttdl*selection_ttlf*weight_SF_N_Jets__ttlf_DL__btag_CERR2Down)+(selection_ttsl*selection_ttlf*weight_SF_N_Jets__ttlf_SL__btag_CERR2Down)+(selection_ttfh*selection_ttlf*weight_SF_N_Jets__ttlf_FH__btag_CERR2Down))",

        "sf_N_Jets__btag_CERR2Down:=((isTTbarSample==1)*(sf_N_Jets__ttlf__btag_CERR2Down+sf_N_Jets__ttcc__btag_CERR2Down+sf_N_Jets__ttbb__btag_CERR2Down)+(isTthSample==1)*(sf_N_Jets__ttH__btag_CERR2Down)+(isTTbarSample==0&&isTthSample==0)*(1.))",





        "sf_N_Jets__ttH__btag_NOMINAL:=((selection_hbb*weight_SF_N_Jets__ttH_bb__btag_NOMINAL)+(selection_nonhbb*weight_SF_N_Jets__ttH_nonbb__btag_NOMINAL))",
        "sf_N_Jets__ttbb__btag_NOMINAL:=((selection_ttdl*selection_ttb*weight_SF_N_Jets__ttb_4FS_DL__btag_NOMINAL)+(selection_ttdl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_DL__btag_NOMINAL)+(selection_ttdl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_DL__btag_NOMINAL)+(selection_ttsl*selection_ttb*weight_SF_N_Jets__ttb_4FS_SL__btag_NOMINAL)+(selection_ttsl*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_SL__btag_NOMINAL)+(selection_ttsl*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_SL__btag_NOMINAL)+(selection_ttfh*selection_ttb*weight_SF_N_Jets__ttb_4FS_FH__btag_NOMINAL)+(selection_ttfh*selection_tt2b*weight_SF_N_Jets__tt2b_4FS_FH__btag_NOMINAL)+(selection_ttfh*selection_ttbb*weight_SF_N_Jets__ttbb_4FS_FH__btag_NOMINAL))",
        "sf_N_Jets__ttcc__btag_NOMINAL:=((selection_ttdl*selection_ttcc*weight_SF_N_Jets__ttcc_DL__btag_NOMINAL)+(selection_ttsl*selection_ttcc*weight_SF_N_Jets__ttcc_SL__btag_NOMINAL)+(selection_ttfh*selection_ttcc*weight_SF_N_Jets__ttcc_FH__btag_NOMINAL))",
        "sf_N_Jets__ttlf__btag_NOMINAL:=((selection_ttdl*selection_ttlf*weight_SF_N_Jets__ttlf_DL__btag_NOMINAL)+(selection_ttsl*selection_ttlf*weight_SF_N_Jets__ttlf_SL__btag_NOMINAL)+(selection_ttfh*selection_ttlf*weight_SF_N_Jets__ttlf_FH__btag_NOMINAL))",

        "sf_N_Jets__btag_NOMINAL:=((isTTbarSample==1)*(sf_N_Jets__ttlf__btag_NOMINAL+sf_N_Jets__ttcc__btag_NOMINAL+sf_N_Jets__ttbb__btag_NOMINAL)+(isTthSample==1)*(sf_N_Jets__ttH__btag_NOMINAL)+(isTTbarSample==0&&isTthSample==0)*(1.))",



    ]

    return addVars
