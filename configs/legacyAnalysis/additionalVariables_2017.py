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
        #################
    "weight_NJet_SF_ttH_Nominal:=(((N_Jets==2)*0.98199671425)+((N_Jets==3)*0.974045700947)+((N_Jets==4)*0.962153308707)+((N_Jets==5)*0.943598923874)+((N_Jets==6)*0.916342209431)+((N_Jets==7)*0.877404039005)+((N_Jets==8)*0.834956000689)+((N_Jets>=9)*0.788034684785))",
    "weight_NJet_SF_Others_Nominal:=(((N_Jets==2)*1.00078815879)+((N_Jets==3)*0.963399476434)+((N_Jets==4)*0.937858573467)+((N_Jets==5)*0.914595650625)+((N_Jets==6)*0.874801900329)+((N_Jets==7)*0.804129410178)+((N_Jets==8)*0.78470038424)+((N_Jets>=9)*0.856314720361))",
    "weight_NJet_SF_ttbarOther_Nominal:=(((N_Jets==2)*1.00501756364)+((N_Jets==3)*0.998363912269)+((N_Jets==4)*0.976690694031)+((N_Jets==5)*0.938947565694)+((N_Jets==6)*0.892058294638)+((N_Jets==7)*0.847881546131)+((N_Jets==8)*0.777155081028)+((N_Jets>=9)*0.738569354438))",
    "weight_NJet_SF_ttbarPlus2B_Nominal:=(((N_Jets==2)*1.02170439015)+((N_Jets==3)*1.01464514909)+((N_Jets==4)*1.00098739781)+((N_Jets==5)*0.965661572712)+((N_Jets==6)*0.937375456227)+((N_Jets==7)*0.874797716334)+((N_Jets==8)*0.824271725465)+((N_Jets>=9)*0.795410260742))",
    "weight_NJet_SF_ttbarPlusB_Nominal:=(((N_Jets==2)*0.987703116668)+((N_Jets==3)*0.977685199223)+((N_Jets==4)*0.952529999253)+((N_Jets==5)*0.928315817939)+((N_Jets==6)*0.889864770735)+((N_Jets==7)*0.817826836846)+((N_Jets==8)*0.7820492571)+((N_Jets>=9)*0.736669529493))",
    "weight_NJet_SF_ttbarPlusBBbar_Nominal:=(((N_Jets==2)*0.985223694581)+((N_Jets==3)*0.970848590829)+((N_Jets==4)*0.970736601292)+((N_Jets==5)*0.949336091116)+((N_Jets==6)*0.919947900412)+((N_Jets==7)*0.860646433349)+((N_Jets==8)*0.798682934239)+((N_Jets>=9)*0.77703191534))",
    "weight_NJet_SF_ttbarPlusCCbar_Nominal:=(((N_Jets==2)*1.00118698018)+((N_Jets==3)*0.99629354846)+((N_Jets==4)*0.980127610255)+((N_Jets==5)*0.95094309998)+((N_Jets==6)*0.913657026072)+((N_Jets==7)*0.866645563088)+((N_Jets==8)*0.824793960131)+((N_Jets>=9)*0.768935385994))",


    "weight_NJet_SF_ttH_BSTAT1_UP:=(((N_Jets==2)*0.982420221613)+((N_Jets==3)*0.974636159259)+((N_Jets==4)*0.962796905557)+((N_Jets==5)*0.94426361933)+((N_Jets==6)*0.916835124681)+((N_Jets==7)*0.877734543723)+((N_Jets==8)*0.834798808309)+((N_Jets>=9)*0.787086346152))",
    "weight_NJet_SF_Others_BSTAT1_UP:=(((N_Jets==2)*1.00083140541)+((N_Jets==3)*0.963403490682)+((N_Jets==4)*0.937736718174)+((N_Jets==5)*0.914468745853)+((N_Jets==6)*0.873861428124)+((N_Jets==7)*0.803806498052)+((N_Jets==8)*0.784692217689)+((N_Jets>=9)*0.861816454007))",
    "weight_NJet_SF_ttbarOther_BSTAT1_UP:=(((N_Jets==2)*1.00557163675)+((N_Jets==3)*0.998900643707)+((N_Jets==4)*0.977190500433)+((N_Jets==5)*0.939351193617)+((N_Jets==6)*0.89226648653)+((N_Jets==7)*0.847981999217)+((N_Jets==8)*0.777721215898)+((N_Jets>=9)*0.738385194732))",
    "weight_NJet_SF_ttbarPlus2B_BSTAT1_UP:=(((N_Jets==2)*1.02415944643)+((N_Jets==3)*1.01777803364)+((N_Jets==4)*1.00416056608)+((N_Jets==5)*0.967997077098)+((N_Jets==6)*0.940133121475)+((N_Jets==7)*0.879029019504)+((N_Jets==8)*0.827929403058)+((N_Jets>=9)*0.797983122328))",
    "weight_NJet_SF_ttbarPlusB_BSTAT1_UP:=(((N_Jets==2)*0.987115866898)+((N_Jets==3)*0.976674630972)+((N_Jets==4)*0.950798449347)+((N_Jets==5)*0.926932671319)+((N_Jets==6)*0.888290006732)+((N_Jets==7)*0.81547421295)+((N_Jets==8)*0.779131937485)+((N_Jets>=9)*0.734836624646))",
    "weight_NJet_SF_ttbarPlusBBbar_BSTAT1_UP:=(((N_Jets==2)*0.984385366188)+((N_Jets==3)*0.969713164273)+((N_Jets==4)*0.969703770393)+((N_Jets==5)*0.948021882176)+((N_Jets==6)*0.918329826392)+((N_Jets==7)*0.858927727805)+((N_Jets==8)*0.794315615496)+((N_Jets>=9)*0.772983030552))",
    "weight_NJet_SF_ttbarPlusCCbar_BSTAT1_UP:=(((N_Jets==2)*1.0015808659)+((N_Jets==3)*0.996824141704)+((N_Jets==4)*0.980612829217)+((N_Jets==5)*0.951102031721)+((N_Jets==6)*0.913935444076)+((N_Jets==7)*0.866691799051)+((N_Jets==8)*0.82439398201)+((N_Jets>=9)*0.769732131491))",


    "weight_NJet_SF_ttH_BSTAT1_DOWN:=(((N_Jets==2)*0.981575385803)+((N_Jets==3)*0.973455733875)+((N_Jets==4)*0.96151346383)+((N_Jets==5)*0.942934741134)+((N_Jets==6)*0.915851176989)+((N_Jets==7)*0.877072251057)+((N_Jets==8)*0.835121906967)+((N_Jets>=9)*0.788971993378))",
    "weight_NJet_SF_Others_BSTAT1_DOWN:=(((N_Jets==2)*1.00074452657)+((N_Jets==3)*0.963395866874)+((N_Jets==4)*0.937975729762)+((N_Jets==5)*0.914714295266)+((N_Jets==6)*0.875742706619)+((N_Jets==7)*0.80444822684)+((N_Jets==8)*0.784736624112)+((N_Jets>=9)*0.851023990714))",
    "weight_NJet_SF_ttbarOther_BSTAT1_DOWN:=(((N_Jets==2)*1.00446627727)+((N_Jets==3)*0.997829325908)+((N_Jets==4)*0.976193822948)+((N_Jets==5)*0.938546269488)+((N_Jets==6)*0.891849529912)+((N_Jets==7)*0.847772807212)+((N_Jets==8)*0.776608925581)+((N_Jets>=9)*0.73873783737))",
    "weight_NJet_SF_ttbarPlus2B_BSTAT1_DOWN:=(((N_Jets==2)*1.01927274857)+((N_Jets==3)*1.01154426606)+((N_Jets==4)*0.997849412392)+((N_Jets==5)*0.963335816617)+((N_Jets==6)*0.934664723038)+((N_Jets==7)*0.870635358897)+((N_Jets==8)*0.820571881703)+((N_Jets>=9)*0.792869860341))",
    "weight_NJet_SF_ttbarPlusB_BSTAT1_DOWN:=(((N_Jets==2)*0.988286323364)+((N_Jets==3)*0.978698218062)+((N_Jets==4)*0.95425015866)+((N_Jets==5)*0.929700740149)+((N_Jets==6)*0.891446831063)+((N_Jets==7)*0.820138766607)+((N_Jets==8)*0.784994180655)+((N_Jets>=9)*0.73853246295))",
    "weight_NJet_SF_ttbarPlusBBbar_BSTAT1_DOWN:=(((N_Jets==2)*0.98606292733)+((N_Jets==3)*0.971964431628)+((N_Jets==4)*0.971756468867)+((N_Jets==5)*0.950627831269)+((N_Jets==6)*0.921559908092)+((N_Jets==7)*0.862349261455)+((N_Jets==8)*0.802978565462)+((N_Jets>=9)*0.781210417883))",
    "weight_NJet_SF_ttbarPlusCCbar_BSTAT1_DOWN:=(((N_Jets==2)*1.0007951874)+((N_Jets==3)*0.995765376588)+((N_Jets==4)*0.979645961593)+((N_Jets==5)*0.950785747101)+((N_Jets==6)*0.913378939928)+((N_Jets==7)*0.86659118534)+((N_Jets==8)*0.825174695959)+((N_Jets>=9)*0.768168744116))",


    "weight_NJet_SF_ttH_BSTAT2_UP:=(((N_Jets==2)*0.982198868343)+((N_Jets==3)*0.974329864608)+((N_Jets==4)*0.962359679484)+((N_Jets==5)*0.943962548753)+((N_Jets==6)*0.916567018319)+((N_Jets==7)*0.877673881185)+((N_Jets==8)*0.835075470709)+((N_Jets>=9)*0.788313717028))",
    "weight_NJet_SF_Others_BSTAT2_UP:=(((N_Jets==2)*1.00085497591)+((N_Jets==3)*0.9634464167)+((N_Jets==4)*0.937930348019)+((N_Jets==5)*0.914670454431)+((N_Jets==6)*0.874487991155)+((N_Jets==7)*0.803958420847)+((N_Jets==8)*0.785091035367)+((N_Jets>=9)*0.857221101484))",
    "weight_NJet_SF_ttbarOther_BSTAT2_UP:=(((N_Jets==2)*1.00506164402)+((N_Jets==3)*0.998427085162)+((N_Jets==4)*0.976768885084)+((N_Jets==5)*0.939043457227)+((N_Jets==6)*0.892217335808)+((N_Jets==7)*0.847917891626)+((N_Jets==8)*0.777905170481)+((N_Jets>=9)*0.738447878578))",
    "weight_NJet_SF_ttbarPlus2B_BSTAT2_UP:=(((N_Jets==2)*1.02185750936)+((N_Jets==3)*1.01469661553)+((N_Jets==4)*1.00150028629)+((N_Jets==5)*0.966216444278)+((N_Jets==6)*0.937317923517)+((N_Jets==7)*0.875784699688)+((N_Jets==8)*0.825292514511)+((N_Jets>=9)*0.797499151071))",
    "weight_NJet_SF_ttbarPlusB_BSTAT2_UP:=(((N_Jets==2)*0.987471744071)+((N_Jets==3)*0.977253354656)+((N_Jets==4)*0.951967458202)+((N_Jets==5)*0.927810670869)+((N_Jets==6)*0.889610278009)+((N_Jets==7)*0.818603720018)+((N_Jets==8)*0.783453524801)+((N_Jets>=9)*0.736300129824))",
    "weight_NJet_SF_ttbarPlusBBbar_BSTAT2_UP:=(((N_Jets==2)*0.98522574458)+((N_Jets==3)*0.970377127623)+((N_Jets==4)*0.970954490816)+((N_Jets==5)*0.948999080524)+((N_Jets==6)*0.918665609816)+((N_Jets==7)*0.861011684511)+((N_Jets==8)*0.798152057386)+((N_Jets>=9)*0.777041443994))",
    "weight_NJet_SF_ttbarPlusCCbar_BSTAT2_UP:=(((N_Jets==2)*1.00127088345)+((N_Jets==3)*0.996442429798)+((N_Jets==4)*0.98020380846)+((N_Jets==5)*0.951171041936)+((N_Jets==6)*0.913670626469)+((N_Jets==7)*0.866908747942)+((N_Jets==8)*0.824778046516)+((N_Jets>=9)*0.770654201431))",


    "weight_NJet_SF_ttH_BSTAT2_DOWN:=(((N_Jets==2)*0.981792591738)+((N_Jets==3)*0.973759078767)+((N_Jets==4)*0.961943921713)+((N_Jets==5)*0.943233199668)+((N_Jets==6)*0.916114226072)+((N_Jets==7)*0.877131856386)+((N_Jets==8)*0.834828905293)+((N_Jets>=9)*0.787755868441))",
    "weight_NJet_SF_Others_BSTAT2_DOWN:=(((N_Jets==2)*1.00072076718)+((N_Jets==3)*0.963352214078)+((N_Jets==4)*0.937789364176)+((N_Jets==5)*0.914526335089)+((N_Jets==6)*0.875118320949)+((N_Jets==7)*0.80430357742)+((N_Jets==8)*0.784297895612)+((N_Jets>=9)*0.855465397623))",
    "weight_NJet_SF_ttbarOther_BSTAT2_DOWN:=(((N_Jets==2)*1.0049732436)+((N_Jets==3)*0.998300486422)+((N_Jets==4)*0.976611487203)+((N_Jets==5)*0.938850199767)+((N_Jets==6)*0.891897195429)+((N_Jets==7)*0.847844868617)+((N_Jets==8)*0.776398271175)+((N_Jets>=9)*0.738691059161))",
    "weight_NJet_SF_ttbarPlus2B_BSTAT2_DOWN:=(((N_Jets==2)*1.02155379706)+((N_Jets==3)*1.0145901607)+((N_Jets==4)*1.00046293367)+((N_Jets==5)*0.965099408975)+((N_Jets==6)*0.937439194159)+((N_Jets==7)*0.873828101847)+((N_Jets==8)*0.823183686537)+((N_Jets>=9)*0.793171900925))",
    "weight_NJet_SF_ttbarPlusB_BSTAT2_DOWN:=(((N_Jets==2)*0.987938382609)+((N_Jets==3)*0.978121658722)+((N_Jets==4)*0.953094797613)+((N_Jets==5)*0.928823339667)+((N_Jets==6)*0.890120532074)+((N_Jets==7)*0.817045574751)+((N_Jets==8)*0.780590635713)+((N_Jets>=9)*0.737017071536))",
    "weight_NJet_SF_ttbarPlusBBbar_BSTAT2_DOWN:=(((N_Jets==2)*0.985217752989)+((N_Jets==3)*0.971325862508)+((N_Jets==4)*0.970520186716)+((N_Jets==5)*0.949682858854)+((N_Jets==6)*0.921245963544)+((N_Jets==7)*0.860283596084)+((N_Jets==8)*0.799227301484)+((N_Jets>=9)*0.777030268234))",
    "weight_NJet_SF_ttbarPlusCCbar_BSTAT2_DOWN:=(((N_Jets==2)*1.00110215618)+((N_Jets==3)*0.996143969923)+((N_Jets==4)*0.98005082237)+((N_Jets==5)*0.950713264125)+((N_Jets==6)*0.913648160387)+((N_Jets==7)*0.866385809061)+((N_Jets==8)*0.824818644982)+((N_Jets>=9)*0.767194103731))",


    "weight_NJet_SF_ttH_LSTAT1_UP:=(((N_Jets==2)*0.982106872025)+((N_Jets==3)*0.974126073492)+((N_Jets==4)*0.962244845017)+((N_Jets==5)*0.943617564204)+((N_Jets==6)*0.916270694472)+((N_Jets==7)*0.877102410149)+((N_Jets==8)*0.83373843475)+((N_Jets>=9)*0.786628221666))",
    "weight_NJet_SF_Others_LSTAT1_UP:=(((N_Jets==2)*1.00109209569)+((N_Jets==3)*0.963520516571)+((N_Jets==4)*0.938056191099)+((N_Jets==5)*0.912968110233)+((N_Jets==6)*0.873322302895)+((N_Jets==7)*0.802210585901)+((N_Jets==8)*0.783317574317)+((N_Jets>=9)*0.855522781102))",
    "weight_NJet_SF_ttbarOther_LSTAT1_UP:=(((N_Jets==2)*1.00511535636)+((N_Jets==3)*0.998617948105)+((N_Jets==4)*0.976886481634)+((N_Jets==5)*0.938802940199)+((N_Jets==6)*0.891591131365)+((N_Jets==7)*0.846647621283)+((N_Jets==8)*0.775358144787)+((N_Jets>=9)*0.737790071918))",
    "weight_NJet_SF_ttbarPlus2B_LSTAT1_UP:=(((N_Jets==2)*1.02176892781)+((N_Jets==3)*1.01467539333)+((N_Jets==4)*1.00091292196)+((N_Jets==5)*0.965449465347)+((N_Jets==6)*0.937505962719)+((N_Jets==7)*0.873608049317)+((N_Jets==8)*0.825513993723)+((N_Jets>=9)*0.796408272139))",
    "weight_NJet_SF_ttbarPlusB_LSTAT1_UP:=(((N_Jets==2)*0.987719284088)+((N_Jets==3)*0.977769577689)+((N_Jets==4)*0.95251769834)+((N_Jets==5)*0.928341316624)+((N_Jets==6)*0.889425962306)+((N_Jets==7)*0.816713974208)+((N_Jets==8)*0.782334011724)+((N_Jets>=9)*0.733908369672))",
    "weight_NJet_SF_ttbarPlusBBbar_LSTAT1_UP:=(((N_Jets==2)*0.985193206893)+((N_Jets==3)*0.970833537033)+((N_Jets==4)*0.970908612085)+((N_Jets==5)*0.94920864895)+((N_Jets==6)*0.920200983749)+((N_Jets==7)*0.859018105962)+((N_Jets==8)*0.799041077575)+((N_Jets>=9)*0.774964331586))",
    "weight_NJet_SF_ttbarPlusCCbar_LSTAT1_UP:=(((N_Jets==2)*1.00123981086)+((N_Jets==3)*0.996346750203)+((N_Jets==4)*0.980156069731)+((N_Jets==5)*0.950865083021)+((N_Jets==6)*0.91323531868)+((N_Jets==7)*0.865537091579)+((N_Jets==8)*0.823015758955)+((N_Jets>=9)*0.769271127211))",


    "weight_NJet_SF_ttH_LSTAT1_DOWN:=(((N_Jets==2)*0.981878012201)+((N_Jets==3)*0.973948684632)+((N_Jets==4)*0.962051076027)+((N_Jets==5)*0.943575713773)+((N_Jets==6)*0.916417333473)+((N_Jets==7)*0.877724691013)+((N_Jets==8)*0.836239181534)+((N_Jets>=9)*0.789617190569))",
    "weight_NJet_SF_Others_LSTAT1_DOWN:=(((N_Jets==2)*1.00047245405)+((N_Jets==3)*0.963301712179)+((N_Jets==4)*0.937677145665)+((N_Jets==5)*0.916233794347)+((N_Jets==6)*0.876484569527)+((N_Jets==7)*0.80609174025)+((N_Jets==8)*0.78629702292)+((N_Jets>=9)*0.857242773903))",
    "weight_NJet_SF_ttbarOther_LSTAT1_DOWN:=(((N_Jets==2)*1.00491737769)+((N_Jets==3)*0.998103097527)+((N_Jets==4)*0.976497367365)+((N_Jets==5)*0.939113898904)+((N_Jets==6)*0.892532809878)+((N_Jets==7)*0.849169306035)+((N_Jets==8)*0.778996344584)+((N_Jets>=9)*0.739529638467))",
    "weight_NJet_SF_ttbarPlus2B_LSTAT1_DOWN:=(((N_Jets==2)*1.02164831877)+((N_Jets==3)*1.01459954357)+((N_Jets==4)*1.00108910605)+((N_Jets==5)*0.96589584771)+((N_Jets==6)*0.937158266036)+((N_Jets==7)*0.876094723373)+((N_Jets==8)*0.823106569525)+((N_Jets>=9)*0.794698387573))",
    "weight_NJet_SF_ttbarPlusB_LSTAT1_DOWN:=(((N_Jets==2)*0.987679067174)+((N_Jets==3)*0.977591993768)+((N_Jets==4)*0.952562440147)+((N_Jets==5)*0.928305031643)+((N_Jets==6)*0.890339178283)+((N_Jets==7)*0.818947253469)+((N_Jets==8)*0.781936644186)+((N_Jets>=9)*0.73998249646))",
    "weight_NJet_SF_ttbarPlusBBbar_LSTAT1_DOWN:=(((N_Jets==2)*0.985241959703)+((N_Jets==3)*0.97087665505)+((N_Jets==4)*0.970544362167)+((N_Jets==5)*0.949480482312)+((N_Jets==6)*0.919731808777)+((N_Jets==7)*0.862231566232)+((N_Jets==8)*0.798180677514)+((N_Jets>=9)*0.779003706026))",
    "weight_NJet_SF_ttbarPlusCCbar_LSTAT1_DOWN:=(((N_Jets==2)*1.00113057357)+((N_Jets==3)*0.996239206703)+((N_Jets==4)*0.980090986377)+((N_Jets==5)*0.95102059136)+((N_Jets==6)*0.914112467586)+((N_Jets==7)*0.867783373477)+((N_Jets==8)*0.82675302256)+((N_Jets>=9)*0.768803319382))",


    "weight_NJet_SF_ttH_LSTAT2_UP:=(((N_Jets==2)*0.982630460128)+((N_Jets==3)*0.974787681134)+((N_Jets==4)*0.962973321183)+((N_Jets==5)*0.944446793989)+((N_Jets==6)*0.917164632208)+((N_Jets==7)*0.878232023654)+((N_Jets==8)*0.835198494406)+((N_Jets>=9)*0.788308529383))",
    "weight_NJet_SF_Others_LSTAT2_UP:=(((N_Jets==2)*1.00097360258)+((N_Jets==3)*0.963465783859)+((N_Jets==4)*0.937782613773)+((N_Jets==5)*0.914512541854)+((N_Jets==6)*0.87413364524)+((N_Jets==7)*0.80347795229)+((N_Jets==8)*0.784552304528)+((N_Jets>=9)*0.856326548919))",
    "weight_NJet_SF_ttbarOther_LSTAT2_UP:=(((N_Jets==2)*1.00511567483)+((N_Jets==3)*0.998565662105)+((N_Jets==4)*0.976910377925)+((N_Jets==5)*0.939097630076)+((N_Jets==6)*0.892119967077)+((N_Jets==7)*0.847590317841)+((N_Jets==8)*0.777594029962)+((N_Jets>=9)*0.740465241477))",
    "weight_NJet_SF_ttbarPlus2B_LSTAT2_UP:=(((N_Jets==2)*1.02181780741)+((N_Jets==3)*1.01478861305)+((N_Jets==4)*1.00134274263)+((N_Jets==5)*0.965618584752)+((N_Jets==6)*0.9381814112)+((N_Jets==7)*0.874069443689)+((N_Jets==8)*0.827124156728)+((N_Jets>=9)*0.797514203384))",
    "weight_NJet_SF_ttbarPlusB_LSTAT2_UP:=(((N_Jets==2)*0.987815778054)+((N_Jets==3)*0.97783890678)+((N_Jets==4)*0.952571718072)+((N_Jets==5)*0.928627880128)+((N_Jets==6)*0.88958202446)+((N_Jets==7)*0.818037125104)+((N_Jets==8)*0.783355119617)+((N_Jets>=9)*0.735100707388))",
    "weight_NJet_SF_ttbarPlusBBbar_LSTAT2_UP:=(((N_Jets==2)*0.985392433435)+((N_Jets==3)*0.970949879422)+((N_Jets==4)*0.971028149491)+((N_Jets==5)*0.949426113167)+((N_Jets==6)*0.920513827675)+((N_Jets==7)*0.860457579598)+((N_Jets==8)*0.798946596393)+((N_Jets>=9)*0.776889757916))",
    "weight_NJet_SF_ttbarPlusCCbar_LSTAT2_UP:=(((N_Jets==2)*1.00125055513)+((N_Jets==3)*0.996364335301)+((N_Jets==4)*0.980204953933)+((N_Jets==5)*0.951036974941)+((N_Jets==6)*0.913763398319)+((N_Jets==7)*0.866233319797)+((N_Jets==8)*0.823793584849)+((N_Jets>=9)*0.769820863518))",


    "weight_NJet_SF_ttH_LSTAT2_DOWN:=(((N_Jets==2)*0.981338200518)+((N_Jets==3)*0.97327432971)+((N_Jets==4)*0.961302451531)+((N_Jets==5)*0.942720450961)+((N_Jets==6)*0.915494998592)+((N_Jets==7)*0.876542452126)+((N_Jets==8)*0.834718381361)+((N_Jets>=9)*0.78778675877))",
    "weight_NJet_SF_Others_LSTAT2_DOWN:=(((N_Jets==2)*1.0005969271)+((N_Jets==3)*0.963348871073)+((N_Jets==4)*0.937948993886)+((N_Jets==5)*0.914635694732)+((N_Jets==6)*0.875526143736)+((N_Jets==7)*0.804832885272)+((N_Jets==8)*0.784863867349)+((N_Jets>=9)*0.856339163047))",
    "weight_NJet_SF_ttbarOther_LSTAT2_DOWN:=(((N_Jets==2)*1.00491704723)+((N_Jets==3)*0.998159873506)+((N_Jets==4)*0.976469779997)+((N_Jets==5)*0.938797981381)+((N_Jets==6)*0.892002624215)+((N_Jets==7)*0.848182900737)+((N_Jets==8)*0.776694243916)+((N_Jets>=9)*0.736530406098))",
    "weight_NJet_SF_ttbarPlus2B_LSTAT2_DOWN:=(((N_Jets==2)*1.02158959958)+((N_Jets==3)*1.01450104736)+((N_Jets==4)*1.00063465958)+((N_Jets==5)*0.965708133229)+((N_Jets==6)*0.936549959032)+((N_Jets==7)*0.875574164058)+((N_Jets==8)*0.821404041298)+((N_Jets>=9)*0.793451097588))",
    "weight_NJet_SF_ttbarPlusB_LSTAT2_DOWN:=(((N_Jets==2)*0.987584487764)+((N_Jets==3)*0.977525978785)+((N_Jets==4)*0.952488250045)+((N_Jets==5)*0.928000031517)+((N_Jets==6)*0.890150637139)+((N_Jets==7)*0.817638345822)+((N_Jets==8)*0.780661462985)+((N_Jets>=9)*0.738286422233))",
    "weight_NJet_SF_ttbarPlusBBbar_LSTAT2_DOWN:=(((N_Jets==2)*0.985040391137)+((N_Jets==3)*0.970743627791)+((N_Jets==4)*0.970429089688)+((N_Jets==5)*0.949237249724)+((N_Jets==6)*0.919391074011)+((N_Jets==7)*0.860858960053)+((N_Jets==8)*0.798474632747)+((N_Jets>=9)*0.777131252847))",
    "weight_NJet_SF_ttbarPlusCCbar_LSTAT2_DOWN:=(((N_Jets==2)*1.00112142226)+((N_Jets==3)*0.996223089756)+((N_Jets==4)*0.980053451601)+((N_Jets==5)*0.950853412373)+((N_Jets==6)*0.913548163527)+((N_Jets==7)*0.867074346474)+((N_Jets==8)*0.825848015053)+((N_Jets>=9)*0.768010058986))",


    "weight_NJet_SF_ttH_BPURITY_UP:=(((N_Jets==2)*0.986818204466)+((N_Jets==3)*0.980112616418)+((N_Jets==4)*0.969384821101)+((N_Jets==5)*0.951530257304)+((N_Jets==6)*0.925879279905)+((N_Jets==7)*0.889879392487)+((N_Jets==8)*0.848056940611)+((N_Jets>=9)*0.80375503964))",
    "weight_NJet_SF_Others_BPURITY_UP:=(((N_Jets==2)*1.00116747734)+((N_Jets==3)*0.965064420738)+((N_Jets==4)*0.93792424074)+((N_Jets==5)*0.923656499839)+((N_Jets==6)*0.884167122735)+((N_Jets==7)*0.811211487759)+((N_Jets==8)*0.792942600571)+((N_Jets>=9)*0.864731580007))",
    "weight_NJet_SF_ttbarOther_BPURITY_UP:=(((N_Jets==2)*1.00535351565)+((N_Jets==3)*0.998915328859)+((N_Jets==4)*0.978068347165)+((N_Jets==5)*0.941938499833)+((N_Jets==6)*0.897342135943)+((N_Jets==7)*0.854091754705)+((N_Jets==8)*0.792386648312)+((N_Jets>=9)*0.766057171073))",
    "weight_NJet_SF_ttbarPlus2B_BPURITY_UP:=(((N_Jets==2)*1.0221489508)+((N_Jets==3)*1.01582436821)+((N_Jets==4)*1.0043384506)+((N_Jets==5)*0.968352273427)+((N_Jets==6)*0.94385103648)+((N_Jets==7)*0.88441635359)+((N_Jets==8)*0.859564993538)+((N_Jets>=9)*0.83304457361))",
    "weight_NJet_SF_ttbarPlusB_BPURITY_UP:=(((N_Jets==2)*0.988624547249)+((N_Jets==3)*0.978654115673)+((N_Jets==4)*0.953277840266)+((N_Jets==5)*0.932113550885)+((N_Jets==6)*0.893286146484)+((N_Jets==7)*0.830814771535)+((N_Jets==8)*0.801731579485)+((N_Jets>=9)*0.741066844933))",
    "weight_NJet_SF_ttbarPlusBBbar_BPURITY_UP:=(((N_Jets==2)*0.986074487923)+((N_Jets==3)*0.972160763081)+((N_Jets==4)*0.972635508254)+((N_Jets==5)*0.95178778972)+((N_Jets==6)*0.926393021433)+((N_Jets==7)*0.868796333956)+((N_Jets==8)*0.808740178499)+((N_Jets>=9)*0.775858589777))",
    "weight_NJet_SF_ttbarPlusCCbar_BPURITY_UP:=(((N_Jets==2)*1.00156246439)+((N_Jets==3)*0.996765781684)+((N_Jets==4)*0.981095003845)+((N_Jets==5)*0.952851301117)+((N_Jets==6)*0.918007809107)+((N_Jets==7)*0.870976012576)+((N_Jets==8)*0.827491101917)+((N_Jets>=9)*0.786906220049))",


    "weight_NJet_SF_ttH_BPURITY_DOWN:=(((N_Jets==2)*0.977195343878)+((N_Jets==3)*0.967951843114)+((N_Jets==4)*0.954949344623)+((N_Jets==5)*0.935579878126)+((N_Jets==6)*0.906909349072)+((N_Jets==7)*0.864880890375)+((N_Jets==8)*0.822306531723)+((N_Jets>=9)*0.773859610424))",
    "weight_NJet_SF_Others_BPURITY_DOWN:=(((N_Jets==2)*1.0004337375)+((N_Jets==3)*0.96196045596)+((N_Jets==4)*0.937865914298)+((N_Jets==5)*0.906518642745)+((N_Jets==6)*0.869676216947)+((N_Jets==7)*0.796267910794)+((N_Jets==8)*0.775723663293)+((N_Jets>=9)*0.853357697387))",
    "weight_NJet_SF_ttbarOther_BPURITY_DOWN:=(((N_Jets==2)*1.00467352387)+((N_Jets==3)*0.997798148258)+((N_Jets==4)*0.975265648571)+((N_Jets==5)*0.93586812451)+((N_Jets==6)*0.886401167952)+((N_Jets==7)*0.841333959625)+((N_Jets==8)*0.76126900883)+((N_Jets>=9)*0.706521146387))",
    "weight_NJet_SF_ttbarPlus2B_BPURITY_DOWN:=(((N_Jets==2)*1.02125339366)+((N_Jets==3)*1.01359011299)+((N_Jets==4)*0.997441398643)+((N_Jets==5)*0.962594455705)+((N_Jets==6)*0.930907099402)+((N_Jets==7)*0.866766817063)+((N_Jets==8)*0.793902462391)+((N_Jets>=9)*0.76602141934))",
    "weight_NJet_SF_ttbarPlusB_BPURITY_DOWN:=(((N_Jets==2)*0.986861868395)+((N_Jets==3)*0.976726753698)+((N_Jets==4)*0.951791901956)+((N_Jets==5)*0.924252829699)+((N_Jets==6)*0.886361435911)+((N_Jets==7)*0.806583951749)+((N_Jets==8)*0.762675895367)+((N_Jets>=9)*0.73324691958))",
    "weight_NJet_SF_ttbarPlusBBbar_BPURITY_DOWN:=(((N_Jets==2)*0.98435934512)+((N_Jets==3)*0.969515899338)+((N_Jets==4)*0.968706952251)+((N_Jets==5)*0.946921808932)+((N_Jets==6)*0.913906851372)+((N_Jets==7)*0.852932938535)+((N_Jets==8)*0.790190305037)+((N_Jets>=9)*0.779219702636))",
    "weight_NJet_SF_ttbarPlusCCbar_BPURITY_DOWN:=(((N_Jets==2)*1.00082071992)+((N_Jets==3)*0.99580116613)+((N_Jets==4)*0.979146714624)+((N_Jets==5)*0.948854468189)+((N_Jets==6)*0.909240641828)+((N_Jets==7)*0.861973706843)+((N_Jets==8)*0.822830410787)+((N_Jets>=9)*0.751401784634))",


    "weight_NJet_SF_ttH_LPURITY_UP:=(((N_Jets==2)*0.979615354215)+((N_Jets==3)*0.970043358283)+((N_Jets==4)*0.957906679642)+((N_Jets==5)*0.938528818848)+((N_Jets==6)*0.913694050133)+((N_Jets==7)*0.875367836892)+((N_Jets==8)*0.834190583515)+((N_Jets>=9)*0.790104950293))",
    "weight_NJet_SF_Others_LPURITY_UP:=(((N_Jets==2)*1.00029396541)+((N_Jets==3)*0.962809794304)+((N_Jets==4)*0.938860621655)+((N_Jets==5)*0.915933195032)+((N_Jets==6)*0.885393725886)+((N_Jets==7)*0.806437772646)+((N_Jets==8)*0.782269458618)+((N_Jets>=9)*0.840208506683))",
    "weight_NJet_SF_ttbarOther_LPURITY_UP:=(((N_Jets==2)*1.00129168684)+((N_Jets==3)*0.99473469651)+((N_Jets==4)*0.973407550841)+((N_Jets==5)*0.936299828232)+((N_Jets==6)*0.88998137863)+((N_Jets==7)*0.846948939191)+((N_Jets==8)*0.772456047157)+((N_Jets>=9)*0.744174413799))",
    "weight_NJet_SF_ttbarPlus2B_LPURITY_UP:=(((N_Jets==2)*1.00989900196)+((N_Jets==3)*1.00085923169)+((N_Jets==4)*0.984190491518)+((N_Jets==5)*0.951560800584)+((N_Jets==6)*0.927339815895)+((N_Jets==7)*0.854623526243)+((N_Jets==8)*0.806331577267)+((N_Jets>=9)*0.791723817022))",
    "weight_NJet_SF_ttbarPlusB_LPURITY_UP:=(((N_Jets==2)*0.992469871004)+((N_Jets==3)*0.98599076041)+((N_Jets==4)*0.965226478757)+((N_Jets==5)*0.940523292134)+((N_Jets==6)*0.903683182436)+((N_Jets==7)*0.830635365233)+((N_Jets==8)*0.798524068271)+((N_Jets>=9)*0.737452652148))",
    "weight_NJet_SF_ttbarPlusBBbar_LPURITY_UP:=(((N_Jets==2)*0.990926385504)+((N_Jets==3)*0.978472135803)+((N_Jets==4)*0.975028374795)+((N_Jets==5)*0.958493976333)+((N_Jets==6)*0.936469775456)+((N_Jets==7)*0.86693293544)+((N_Jets==8)*0.821988060344)+((N_Jets>=9)*0.796815603309))",
    "weight_NJet_SF_ttbarPlusCCbar_LPURITY_UP:=(((N_Jets==2)*0.998406796013)+((N_Jets==3)*0.992591741083)+((N_Jets==4)*0.976933095882)+((N_Jets==5)*0.948771069114)+((N_Jets==6)*0.912784726569)+((N_Jets==7)*0.865527573579)+((N_Jets==8)*0.822871076594)+((N_Jets>=9)*0.769963325036))",


    "weight_NJet_SF_ttH_LPURITY_DOWN:=(((N_Jets==2)*0.984380688431)+((N_Jets==3)*0.978081430377)+((N_Jets==4)*0.966398636615)+((N_Jets==5)*0.94884145642)+((N_Jets==6)*0.918916435824)+((N_Jets==7)*0.879317537801)+((N_Jets==8)*0.83565138018)+((N_Jets>=9)*0.785245320943))",
    "weight_NJet_SF_Others_LPURITY_DOWN:=(((N_Jets==2)*1.00128032964)+((N_Jets==3)*0.96397859851)+((N_Jets==4)*0.936775941429)+((N_Jets==5)*0.91330799728)+((N_Jets==6)*0.864074360968)+((N_Jets==7)*0.801379163611)+((N_Jets==8)*0.788218640501)+((N_Jets>=9)*0.877381831517))",
    "weight_NJet_SF_ttbarOther_LPURITY_DOWN:=(((N_Jets==2)*1.00881208631)+((N_Jets==3)*1.00204938025)+((N_Jets==4)*0.980045401678)+((N_Jets==5)*0.941614057002)+((N_Jets==6)*0.894119953669)+((N_Jets==7)*0.848293089059)+((N_Jets==8)*0.78209199207)+((N_Jets>=9)*0.731611289067))",
    "weight_NJet_SF_ttbarPlus2B_LPURITY_DOWN:=(((N_Jets==2)*1.03357467572)+((N_Jets==3)*1.02873815818)+((N_Jets==4)*1.01857221349)+((N_Jets==5)*0.979905119045)+((N_Jets==6)*0.948824416002)+((N_Jets==7)*0.897018069923)+((N_Jets==8)*0.842789968425)+((N_Jets>=9)*0.799444843295))",
    "weight_NJet_SF_ttbarPlusB_LPURITY_DOWN:=(((N_Jets==2)*0.982806285574)+((N_Jets==3)*0.969474113745)+((N_Jets==4)*0.939905329691)+((N_Jets==5)*0.916031344131)+((N_Jets==6)*0.876385552629)+((N_Jets==7)*0.804034354752)+((N_Jets==8)*0.768499360712)+((N_Jets>=9)*0.738308245072))",
    "weight_NJet_SF_ttbarPlusBBbar_LPURITY_DOWN:=(((N_Jets==2)*0.979831918052)+((N_Jets==3)*0.962718346384)+((N_Jets==4)*0.965838648674)+((N_Jets==5)*0.940138802066)+((N_Jets==6)*0.904644503144)+((N_Jets==7)*0.853475485711)+((N_Jets==8)*0.774672127368)+((N_Jets>=9)*0.753441264648))",
    "weight_NJet_SF_ttbarPlusCCbar_LPURITY_DOWN:=(((N_Jets==2)*1.00406630292)+((N_Jets==3)*1.00005964127)+((N_Jets==4)*0.983350069274)+((N_Jets==5)*0.953279275808)+((N_Jets==6)*0.914656685302)+((N_Jets==7)*0.867490549976)+((N_Jets==8)*0.826575658117)+((N_Jets>=9)*0.768422885724))",


    "weight_NJet_SF_ttH_CERR1_UP:=(((N_Jets==2)*0.98273599712)+((N_Jets==3)*0.975761899858)+((N_Jets==4)*0.963855473296)+((N_Jets==5)*0.946375258458)+((N_Jets==6)*0.919715755459)+((N_Jets==7)*0.88196104248)+((N_Jets==8)*0.839478244774)+((N_Jets>=9)*0.793916705213))",
    "weight_NJet_SF_Others_CERR1_UP:=(((N_Jets==2)*1.00182501653)+((N_Jets==3)*0.963583334877)+((N_Jets==4)*0.942269075828)+((N_Jets==5)*0.90852217747)+((N_Jets==6)*0.876900820374)+((N_Jets==7)*0.80247977519)+((N_Jets==8)*0.782502253309)+((N_Jets>=9)*0.846431090695))",
    "weight_NJet_SF_ttbarOther_CERR1_UP:=(((N_Jets==2)*1.00495471848)+((N_Jets==3)*0.998286919239)+((N_Jets==4)*0.976538247839)+((N_Jets==5)*0.938814053627)+((N_Jets==6)*0.891734564376)+((N_Jets==7)*0.8472524911)+((N_Jets==8)*0.777377421799)+((N_Jets>=9)*0.735723880533))",
    "weight_NJet_SF_ttbarPlus2B_CERR1_UP:=(((N_Jets==2)*1.02204142885)+((N_Jets==3)*1.01472755244)+((N_Jets==4)*0.999580852162)+((N_Jets==5)*0.966672941507)+((N_Jets==6)*0.94413011452)+((N_Jets==7)*0.870097829253)+((N_Jets==8)*0.841233190623)+((N_Jets>=9)*0.80827312849))",
    "weight_NJet_SF_ttbarPlusB_CERR1_UP:=(((N_Jets==2)*0.987495375638)+((N_Jets==3)*0.977161162236)+((N_Jets==4)*0.951938308644)+((N_Jets==5)*0.928480733148)+((N_Jets==6)*0.891248098459)+((N_Jets==7)*0.819019201958)+((N_Jets==8)*0.772979613184)+((N_Jets>=9)*0.737654866459))",
    "weight_NJet_SF_ttbarPlusBBbar_CERR1_UP:=(((N_Jets==2)*0.984614905258)+((N_Jets==3)*0.970686316266)+((N_Jets==4)*0.971156043002)+((N_Jets==5)*0.951406560805)+((N_Jets==6)*0.921929786916)+((N_Jets==7)*0.865552632479)+((N_Jets==8)*0.800329979235)+((N_Jets>=9)*0.788933041429))",
    "weight_NJet_SF_ttbarPlusCCbar_CERR1_UP:=(((N_Jets==2)*1.002839402)+((N_Jets==3)*1.00036238784)+((N_Jets==4)*0.984856616915)+((N_Jets==5)*0.95689345766)+((N_Jets==6)*0.923346708897)+((N_Jets==7)*0.870278779561)+((N_Jets==8)*0.833995896323)+((N_Jets>=9)*0.77866336816))",


    "weight_NJet_SF_ttH_CERR1_DOWN:=(((N_Jets==2)*0.980650624713)+((N_Jets==3)*0.971012065219)+((N_Jets==4)*0.959034785051)+((N_Jets==5)*0.938707018602)+((N_Jets==6)*0.910222662498)+((N_Jets==7)*0.869605905164)+((N_Jets==8)*0.826968966481)+((N_Jets>=9)*0.777586484629))",
    "weight_NJet_SF_Others_CERR1_DOWN:=(((N_Jets==2)*0.998611677476)+((N_Jets==3)*0.963739844415)+((N_Jets==4)*0.928943631714)+((N_Jets==5)*0.924353608247)+((N_Jets==6)*0.870260708261)+((N_Jets==7)*0.807454106333)+((N_Jets==8)*0.789934886224)+((N_Jets>=9)*0.873740531917))",
    "weight_NJet_SF_ttbarOther_CERR1_DOWN:=(((N_Jets==2)*1.00512791068)+((N_Jets==3)*0.998490596519)+((N_Jets==4)*0.976946605906)+((N_Jets==5)*0.939185758455)+((N_Jets==6)*0.892620213877)+((N_Jets==7)*0.849052925959)+((N_Jets==8)*0.77672845791)+((N_Jets>=9)*0.74413586144))",
    "weight_NJet_SF_ttbarPlus2B_CERR1_DOWN:=(((N_Jets==2)*1.02115637553)+((N_Jets==3)*1.01453141193)+((N_Jets==4)*1.0034993753)+((N_Jets==5)*0.96395490335)+((N_Jets==6)*0.925341806993)+((N_Jets==7)*0.884506590763)+((N_Jets==8)*0.799498225407)+((N_Jets>=9)*0.78121315634))",
    "weight_NJet_SF_ttbarPlusB_CERR1_DOWN:=(((N_Jets==2)*0.988084849539)+((N_Jets==3)*0.978609174855)+((N_Jets==4)*0.953605972991)+((N_Jets==5)*0.92794823298)+((N_Jets==6)*0.887567079499)+((N_Jets==7)*0.815486754816)+((N_Jets==8)*0.798310664909)+((N_Jets>=9)*0.735435255951))",
    "weight_NJet_SF_ttbarPlusBBbar_CERR1_DOWN:=(((N_Jets==2)*0.986345110829)+((N_Jets==3)*0.971156426621)+((N_Jets==4)*0.970005918304)+((N_Jets==5)*0.945564182948)+((N_Jets==6)*0.916331846236)+((N_Jets==7)*0.851885496051)+((N_Jets==8)*0.7973569696)+((N_Jets>=9)*0.753874056026))",
    "weight_NJet_SF_ttbarPlusCCbar_CERR1_DOWN:=(((N_Jets==2)*0.998338669565)+((N_Jets==3)*0.989151780178)+((N_Jets==4)*0.971701535476)+((N_Jets==5)*0.940652503932)+((N_Jets==6)*0.896562310652)+((N_Jets==7)*0.858986164361)+((N_Jets==8)*0.80965004657)+((N_Jets>=9)*0.75814378643))",


    "weight_NJet_SF_ttH_CERR2_UP:=(((N_Jets==2)*0.98265355935)+((N_Jets==3)*0.975560520751)+((N_Jets==4)*0.963655336315)+((N_Jets==5)*0.945834273299)+((N_Jets==6)*0.919368899432)+((N_Jets==7)*0.881447167001)+((N_Jets==8)*0.838836196606)+((N_Jets>=9)*0.793087461324))",
    "weight_NJet_SF_Others_CERR2_UP:=(((N_Jets==2)*1.00163810047)+((N_Jets==3)*0.963266851381)+((N_Jets==4)*0.942173266017)+((N_Jets==5)*0.909232112821)+((N_Jets==6)*0.877281732869)+((N_Jets==7)*0.802769618034)+((N_Jets==8)*0.78306246235)+((N_Jets>=9)*0.846830311982))",
    "weight_NJet_SF_ttbarOther_CERR2_UP:=(((N_Jets==2)*1.00494342178)+((N_Jets==3)*0.998264249022)+((N_Jets==4)*0.976526580775)+((N_Jets==5)*0.938801944942)+((N_Jets==6)*0.891733618087)+((N_Jets==7)*0.847369024679)+((N_Jets==8)*0.777409084404)+((N_Jets>=9)*0.736063550831))",
    "weight_NJet_SF_ttbarPlus2B_CERR2_UP:=(((N_Jets==2)*1.02187098597)+((N_Jets==3)*1.01454290697)+((N_Jets==4)*0.999581890743)+((N_Jets==5)*0.966183342796)+((N_Jets==6)*0.941579178631)+((N_Jets==7)*0.87098660164)+((N_Jets==8)*0.833901743988)+((N_Jets>=9)*0.81103403481))",
    "weight_NJet_SF_ttbarPlusB_CERR2_UP:=(((N_Jets==2)*0.987489711554)+((N_Jets==3)*0.977114369734)+((N_Jets==4)*0.951839127538)+((N_Jets==5)*0.928126987328)+((N_Jets==6)*0.890895389878)+((N_Jets==7)*0.819530997978)+((N_Jets==8)*0.77437588346)+((N_Jets>=9)*0.738536732939))",
    "weight_NJet_SF_ttbarPlusBBbar_CERR2_UP:=(((N_Jets==2)*0.984741968978)+((N_Jets==3)*0.970632688893)+((N_Jets==4)*0.971095124947)+((N_Jets==5)*0.950970206759)+((N_Jets==6)*0.92172488595)+((N_Jets==7)*0.864619493382)+((N_Jets==8)*0.80077764922)+((N_Jets>=9)*0.785361100964))",
    "weight_NJet_SF_ttbarPlusCCbar_CERR2_UP:=(((N_Jets==2)*1.00196997019)+((N_Jets==3)*0.998666542729)+((N_Jets==4)*0.982980181337)+((N_Jets==5)*0.954630585728)+((N_Jets==6)*0.920336002828)+((N_Jets==7)*0.868912427558)+((N_Jets==8)*0.830325823958)+((N_Jets>=9)*0.773227791341))",


    "weight_NJet_SF_ttH_CERR2_DOWN:=(((N_Jets==2)*0.981040917613)+((N_Jets==3)*0.97190692466)+((N_Jets==4)*0.959970740453)+((N_Jets==5)*0.940453553875)+((N_Jets==6)*0.911965311472)+((N_Jets==7)*0.871768172173)+((N_Jets==8)*0.829464816799)+((N_Jets>=9)*0.780845615045))",
    "weight_NJet_SF_Others_CERR2_DOWN:=(((N_Jets==2)*0.999398474625)+((N_Jets==3)*0.963837467788)+((N_Jets==4)*0.931282062469)+((N_Jets==5)*0.921721241047)+((N_Jets==6)*0.870963752662)+((N_Jets==7)*0.806165818525)+((N_Jets==8)*0.787637015728)+((N_Jets>=9)*0.870204090419))",
    "weight_NJet_SF_ttbarOther_CERR2_DOWN:=(((N_Jets==2)*1.00512306569)+((N_Jets==3)*0.998502377452)+((N_Jets==4)*0.976917385732)+((N_Jets==5)*0.939158910123)+((N_Jets==6)*0.892512173246)+((N_Jets==7)*0.848640850463)+((N_Jets==8)*0.776784317061)+((N_Jets>=9)*0.742360821713))",
    "weight_NJet_SF_ttbarPlus2B_CERR2_DOWN:=(((N_Jets==2)*1.02147802333)+((N_Jets==3)*1.01481811004)+((N_Jets==4)*1.00299230007)+((N_Jets==5)*0.964952802079)+((N_Jets==6)*0.931291241892)+((N_Jets==7)*0.880989133907)+((N_Jets==8)*0.813168185599)+((N_Jets>=9)*0.778774781925))",
    "weight_NJet_SF_ttbarPlusB_CERR2_DOWN:=(((N_Jets==2)*0.988016316235)+((N_Jets==3)*0.978499156309)+((N_Jets==4)*0.953529562177)+((N_Jets==5)*0.928555050032)+((N_Jets==6)*0.88840506655)+((N_Jets==7)*0.815414439508)+((N_Jets==8)*0.79296998225)+((N_Jets>=9)*0.734400067893))",
    "weight_NJet_SF_ttbarPlusBBbar_CERR2_DOWN:=(((N_Jets==2)*0.985933006958)+((N_Jets==3)*0.971170955414)+((N_Jets==4)*0.970222465156)+((N_Jets==5)*0.94699568562)+((N_Jets==6)*0.917386440453)+((N_Jets==7)*0.855056047055)+((N_Jets==8)*0.796626157413)+((N_Jets>=9)*0.764554274993))",
    "weight_NJet_SF_ttbarPlusCCbar_CERR2_DOWN:=(((N_Jets==2)*1.00011551662)+((N_Jets==3)*0.992941025465)+((N_Jets==4)*0.976007214522)+((N_Jets==5)*0.945761841178)+((N_Jets==6)*0.904247104296)+((N_Jets==7)*0.862928659645)+((N_Jets==8)*0.817161523393)+((N_Jets>=9)*0.765856681135))",



    "weight_NJet_SF_ttbb_Nominal:=((weight_NJet_SF_ttbarPlusB_Nominal*(GenEvt_I_TTPlusBB==1))+(weight_NJet_SF_ttbarPlusBBbar_Nominal*(GenEvt_I_TTPlusBB==3))+(weight_NJet_SF_ttbarPlus2B_Nominal*(GenEvt_I_TTPlusBB==2)))",
    "weight_NJet_SF_ttcc_Nominal:=(weight_NJet_SF_ttbarPlusCCbar_Nominal*(GenEvt_I_TTPlusCC==1))",
    "weight_NJet_SF_ttlf_Nominal:=(weight_NJet_SF_ttbarOther_Nominal*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0))",
    

    "weight_NJet_SF_ttbb_BSTAT1_UP:=((weight_NJet_SF_ttbarPlusB_BSTAT1_UP*(GenEvt_I_TTPlusBB==1))+(weight_NJet_SF_ttbarPlusBBbar_BSTAT1_UP*(GenEvt_I_TTPlusBB==3))+(weight_NJet_SF_ttbarPlus2B_BSTAT1_UP*(GenEvt_I_TTPlusBB==2)))",
    "weight_NJet_SF_ttcc_BSTAT1_UP:=(weight_NJet_SF_ttbarPlusCCbar_BSTAT1_UP*(GenEvt_I_TTPlusCC==1))",
    "weight_NJet_SF_ttlf_BSTAT1_UP:=(weight_NJet_SF_ttbarOther_BSTAT1_UP*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0))",
    

    "weight_NJet_SF_ttbb_BSTAT1_DOWN:=((weight_NJet_SF_ttbarPlusB_BSTAT1_DOWN*(GenEvt_I_TTPlusBB==1))+(weight_NJet_SF_ttbarPlusBBbar_BSTAT1_DOWN*(GenEvt_I_TTPlusBB==3))+(weight_NJet_SF_ttbarPlus2B_BSTAT1_DOWN*(GenEvt_I_TTPlusBB==2)))",
    "weight_NJet_SF_ttcc_BSTAT1_DOWN:=(weight_NJet_SF_ttbarPlusCCbar_BSTAT1_DOWN*(GenEvt_I_TTPlusCC==1))",
    "weight_NJet_SF_ttlf_BSTAT1_DOWN:=(weight_NJet_SF_ttbarOther_BSTAT1_DOWN*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0))",
    

    "weight_NJet_SF_ttbb_BSTAT2_UP:=((weight_NJet_SF_ttbarPlusB_BSTAT2_UP*(GenEvt_I_TTPlusBB==1))+(weight_NJet_SF_ttbarPlusBBbar_BSTAT2_UP*(GenEvt_I_TTPlusBB==3))+(weight_NJet_SF_ttbarPlus2B_BSTAT2_UP*(GenEvt_I_TTPlusBB==2)))",
    "weight_NJet_SF_ttcc_BSTAT2_UP:=(weight_NJet_SF_ttbarPlusCCbar_BSTAT2_UP*(GenEvt_I_TTPlusCC==1))",
    "weight_NJet_SF_ttlf_BSTAT2_UP:=(weight_NJet_SF_ttbarOther_BSTAT2_UP*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0))",
    

    "weight_NJet_SF_ttbb_BSTAT2_DOWN:=((weight_NJet_SF_ttbarPlusB_BSTAT2_DOWN*(GenEvt_I_TTPlusBB==1))+(weight_NJet_SF_ttbarPlusBBbar_BSTAT2_DOWN*(GenEvt_I_TTPlusBB==3))+(weight_NJet_SF_ttbarPlus2B_BSTAT2_DOWN*(GenEvt_I_TTPlusBB==2)))",
    "weight_NJet_SF_ttcc_BSTAT2_DOWN:=(weight_NJet_SF_ttbarPlusCCbar_BSTAT2_DOWN*(GenEvt_I_TTPlusCC==1))",
    "weight_NJet_SF_ttlf_BSTAT2_DOWN:=(weight_NJet_SF_ttbarOther_BSTAT2_DOWN*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0))",
    

    "weight_NJet_SF_ttbb_LSTAT1_UP:=((weight_NJet_SF_ttbarPlusB_LSTAT1_UP*(GenEvt_I_TTPlusBB==1))+(weight_NJet_SF_ttbarPlusBBbar_LSTAT1_UP*(GenEvt_I_TTPlusBB==3))+(weight_NJet_SF_ttbarPlus2B_LSTAT1_UP*(GenEvt_I_TTPlusBB==2)))",
    "weight_NJet_SF_ttcc_LSTAT1_UP:=(weight_NJet_SF_ttbarPlusCCbar_LSTAT1_UP*(GenEvt_I_TTPlusCC==1))",
    "weight_NJet_SF_ttlf_LSTAT1_UP:=(weight_NJet_SF_ttbarOther_LSTAT1_UP*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0))",
    

    "weight_NJet_SF_ttbb_LSTAT1_DOWN:=((weight_NJet_SF_ttbarPlusB_LSTAT1_DOWN*(GenEvt_I_TTPlusBB==1))+(weight_NJet_SF_ttbarPlusBBbar_LSTAT1_DOWN*(GenEvt_I_TTPlusBB==3))+(weight_NJet_SF_ttbarPlus2B_LSTAT1_DOWN*(GenEvt_I_TTPlusBB==2)))",
    "weight_NJet_SF_ttcc_LSTAT1_DOWN:=(weight_NJet_SF_ttbarPlusCCbar_LSTAT1_DOWN*(GenEvt_I_TTPlusCC==1))",
    "weight_NJet_SF_ttlf_LSTAT1_DOWN:=(weight_NJet_SF_ttbarOther_LSTAT1_DOWN*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0))",
    

    "weight_NJet_SF_ttbb_LSTAT2_UP:=((weight_NJet_SF_ttbarPlusB_LSTAT2_UP*(GenEvt_I_TTPlusBB==1))+(weight_NJet_SF_ttbarPlusBBbar_LSTAT2_UP*(GenEvt_I_TTPlusBB==3))+(weight_NJet_SF_ttbarPlus2B_LSTAT2_UP*(GenEvt_I_TTPlusBB==2)))",
    "weight_NJet_SF_ttcc_LSTAT2_UP:=(weight_NJet_SF_ttbarPlusCCbar_LSTAT2_UP*(GenEvt_I_TTPlusCC==1))",
    "weight_NJet_SF_ttlf_LSTAT2_UP:=(weight_NJet_SF_ttbarOther_LSTAT2_UP*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0))",
    

    "weight_NJet_SF_ttbb_LSTAT2_DOWN:=((weight_NJet_SF_ttbarPlusB_LSTAT2_DOWN*(GenEvt_I_TTPlusBB==1))+(weight_NJet_SF_ttbarPlusBBbar_LSTAT2_DOWN*(GenEvt_I_TTPlusBB==3))+(weight_NJet_SF_ttbarPlus2B_LSTAT2_DOWN*(GenEvt_I_TTPlusBB==2)))",
    "weight_NJet_SF_ttcc_LSTAT2_DOWN:=(weight_NJet_SF_ttbarPlusCCbar_LSTAT2_DOWN*(GenEvt_I_TTPlusCC==1))",
    "weight_NJet_SF_ttlf_LSTAT2_DOWN:=(weight_NJet_SF_ttbarOther_LSTAT2_DOWN*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0))",
    

    "weight_NJet_SF_ttbb_BPURITY_UP:=((weight_NJet_SF_ttbarPlusB_BPURITY_UP*(GenEvt_I_TTPlusBB==1))+(weight_NJet_SF_ttbarPlusBBbar_BPURITY_UP*(GenEvt_I_TTPlusBB==3))+(weight_NJet_SF_ttbarPlus2B_BPURITY_UP*(GenEvt_I_TTPlusBB==2)))",
    "weight_NJet_SF_ttcc_BPURITY_UP:=(weight_NJet_SF_ttbarPlusCCbar_BPURITY_UP*(GenEvt_I_TTPlusCC==1))",
    "weight_NJet_SF_ttlf_BPURITY_UP:=(weight_NJet_SF_ttbarOther_BPURITY_UP*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0))",
    

    "weight_NJet_SF_ttbb_BPURITY_DOWN:=((weight_NJet_SF_ttbarPlusB_BPURITY_DOWN*(GenEvt_I_TTPlusBB==1))+(weight_NJet_SF_ttbarPlusBBbar_BPURITY_DOWN*(GenEvt_I_TTPlusBB==3))+(weight_NJet_SF_ttbarPlus2B_BPURITY_DOWN*(GenEvt_I_TTPlusBB==2)))",
    "weight_NJet_SF_ttcc_BPURITY_DOWN:=(weight_NJet_SF_ttbarPlusCCbar_BPURITY_DOWN*(GenEvt_I_TTPlusCC==1))",
    "weight_NJet_SF_ttlf_BPURITY_DOWN:=(weight_NJet_SF_ttbarOther_BPURITY_DOWN*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0))",
    

    "weight_NJet_SF_ttbb_LPURITY_UP:=((weight_NJet_SF_ttbarPlusB_LPURITY_UP*(GenEvt_I_TTPlusBB==1))+(weight_NJet_SF_ttbarPlusBBbar_LPURITY_UP*(GenEvt_I_TTPlusBB==3))+(weight_NJet_SF_ttbarPlus2B_LPURITY_UP*(GenEvt_I_TTPlusBB==2)))",
    "weight_NJet_SF_ttcc_LPURITY_UP:=(weight_NJet_SF_ttbarPlusCCbar_LPURITY_UP*(GenEvt_I_TTPlusCC==1))",
    "weight_NJet_SF_ttlf_LPURITY_UP:=(weight_NJet_SF_ttbarOther_LPURITY_UP*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0))",
    

    "weight_NJet_SF_ttbb_LPURITY_DOWN:=((weight_NJet_SF_ttbarPlusB_LPURITY_DOWN*(GenEvt_I_TTPlusBB==1))+(weight_NJet_SF_ttbarPlusBBbar_LPURITY_DOWN*(GenEvt_I_TTPlusBB==3))+(weight_NJet_SF_ttbarPlus2B_LPURITY_DOWN*(GenEvt_I_TTPlusBB==2)))",
    "weight_NJet_SF_ttcc_LPURITY_DOWN:=(weight_NJet_SF_ttbarPlusCCbar_LPURITY_DOWN*(GenEvt_I_TTPlusCC==1))",
    "weight_NJet_SF_ttlf_LPURITY_DOWN:=(weight_NJet_SF_ttbarOther_LPURITY_DOWN*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0))",
    

    "weight_NJet_SF_ttbb_CERR1_UP:=((weight_NJet_SF_ttbarPlusB_CERR1_UP*(GenEvt_I_TTPlusBB==1))+(weight_NJet_SF_ttbarPlusBBbar_CERR1_UP*(GenEvt_I_TTPlusBB==3))+(weight_NJet_SF_ttbarPlus2B_CERR1_UP*(GenEvt_I_TTPlusBB==2)))",
    "weight_NJet_SF_ttcc_CERR1_UP:=(weight_NJet_SF_ttbarPlusCCbar_CERR1_UP*(GenEvt_I_TTPlusCC==1))",
    "weight_NJet_SF_ttlf_CERR1_UP:=(weight_NJet_SF_ttbarOther_CERR1_UP*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0))",
    

    "weight_NJet_SF_ttbb_CERR1_DOWN:=((weight_NJet_SF_ttbarPlusB_CERR1_DOWN*(GenEvt_I_TTPlusBB==1))+(weight_NJet_SF_ttbarPlusBBbar_CERR1_DOWN*(GenEvt_I_TTPlusBB==3))+(weight_NJet_SF_ttbarPlus2B_CERR1_DOWN*(GenEvt_I_TTPlusBB==2)))",
    "weight_NJet_SF_ttcc_CERR1_DOWN:=(weight_NJet_SF_ttbarPlusCCbar_CERR1_DOWN*(GenEvt_I_TTPlusCC==1))",
    "weight_NJet_SF_ttlf_CERR1_DOWN:=(weight_NJet_SF_ttbarOther_CERR1_DOWN*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0))",
    

    "weight_NJet_SF_ttbb_CERR2_UP:=((weight_NJet_SF_ttbarPlusB_CERR2_UP*(GenEvt_I_TTPlusBB==1))+(weight_NJet_SF_ttbarPlusBBbar_CERR2_UP*(GenEvt_I_TTPlusBB==3))+(weight_NJet_SF_ttbarPlus2B_CERR2_UP*(GenEvt_I_TTPlusBB==2)))",
    "weight_NJet_SF_ttcc_CERR2_UP:=(weight_NJet_SF_ttbarPlusCCbar_CERR2_UP*(GenEvt_I_TTPlusCC==1))",
    "weight_NJet_SF_ttlf_CERR2_UP:=(weight_NJet_SF_ttbarOther_CERR2_UP*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0))",
    

    "weight_NJet_SF_ttbb_CERR2_DOWN:=((weight_NJet_SF_ttbarPlusB_CERR2_DOWN*(GenEvt_I_TTPlusBB==1))+(weight_NJet_SF_ttbarPlusBBbar_CERR2_DOWN*(GenEvt_I_TTPlusBB==3))+(weight_NJet_SF_ttbarPlus2B_CERR2_DOWN*(GenEvt_I_TTPlusBB==2)))",
    "weight_NJet_SF_ttcc_CERR2_DOWN:=(weight_NJet_SF_ttbarPlusCCbar_CERR2_DOWN*(GenEvt_I_TTPlusCC==1))",
    "weight_NJet_SF_ttlf_CERR2_DOWN:=(weight_NJet_SF_ttbarOther_CERR2_DOWN*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0))",


##########
# combined factors with logic for syst csv
##########
    "N_JetWeight_Nominal:= (((isTTbarSample==1)*weight_NJet_SF_ttbb_Nominal*weight_NJet_SF_ttcc_Nominal*weight_NJet_SF_ttlf_Nominal)*((isTthSample==1)*weight_NJet_SF_ttH_Nominal)*(isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_Nominal)",
    "N_JetWeight_BSTAT1_UP:= (((isTTbarSample==1)*weight_NJet_SF_ttbb_BSTAT1_UP*weight_NJet_SF_ttcc_BSTAT1_UP*weight_NJet_SF_ttlf_BSTAT1_UP)*((isTthSample==1)*weight_NJet_SF_ttH_BSTAT1_UP)*(isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_BSTAT1_UP)",
    "N_JetWeight_BSTAT1_DOWN:= (((isTTbarSample==1)*weight_NJet_SF_ttbb_BSTAT1_DOWN*weight_NJet_SF_ttcc_BSTAT1_DOWN*weight_NJet_SF_ttlf_BSTAT1_DOWN)*((isTthSample==1)*weight_NJet_SF_ttH_BSTAT1_DOWN)*(isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_BSTAT1_DOWN)",
    "N_JetWeight_BSTAT2_UP:= (((isTTbarSample==1)*weight_NJet_SF_ttbb_BSTAT2_UP*weight_NJet_SF_ttcc_BSTAT2_UP*weight_NJet_SF_ttlf_BSTAT2_UP)*((isTthSample==1)*weight_NJet_SF_ttH_BSTAT2_UP)*(isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_BSTAT2_UP)",
    "N_JetWeight_BSTAT2_DOWN:= (((isTTbarSample==1)*weight_NJet_SF_ttbb_BSTAT2_DOWN*weight_NJet_SF_ttcc_BSTAT2_DOWN*weight_NJet_SF_ttlf_BSTAT2_DOWN)*((isTthSample==1)*weight_NJet_SF_ttH_BSTAT2_DOWN)*(isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_BSTAT2_DOWN)",
    "N_JetWeight_LSTAT1_UP:= (((isTTbarSample==1)*weight_NJet_SF_ttbb_LSTAT1_UP*weight_NJet_SF_ttcc_LSTAT1_UP*weight_NJet_SF_ttlf_LSTAT1_UP)*((isTthSample==1)*weight_NJet_SF_ttH_LSTAT1_UP)*(isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_LSTAT1_UP)",
    "N_JetWeight_LSTAT1_DOWN:= (((isTTbarSample==1)*weight_NJet_SF_ttbb_LSTAT1_DOWN*weight_NJet_SF_ttcc_LSTAT1_DOWN*weight_NJet_SF_ttlf_LSTAT1_DOWN)*((isTthSample==1)*weight_NJet_SF_ttH_LSTAT1_DOWN)*(isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_LSTAT1_DOWN)",
    "N_JetWeight_LSTAT2_UP:= (((isTTbarSample==1)*weight_NJet_SF_ttbb_LSTAT2_UP*weight_NJet_SF_ttcc_LSTAT2_UP*weight_NJet_SF_ttlf_LSTAT2_UP)*((isTthSample==1)*weight_NJet_SF_ttH_LSTAT2_UP)*(isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_LSTAT2_UP)",
    "N_JetWeight_LSTAT2_DOWN:= (((isTTbarSample==1)*weight_NJet_SF_ttbb_LSTAT2_DOWN*weight_NJet_SF_ttcc_LSTAT2_DOWN*weight_NJet_SF_ttlf_LSTAT2_DOWN)*((isTthSample==1)*weight_NJet_SF_ttH_LSTAT2_DOWN)*(isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_LSTAT2_DOWN)",
    "N_JetWeight_BPURITY_UP:= (((isTTbarSample==1)*weight_NJet_SF_ttbb_BPURITY_UP*weight_NJet_SF_ttcc_BPURITY_UP*weight_NJet_SF_ttlf_BPURITY_UP)*((isTthSample==1)*weight_NJet_SF_ttH_BPURITY_UP)*(isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_BPURITY_UP)",
    "N_JetWeight_BPURITY_DOWN:= (((isTTbarSample==1)*weight_NJet_SF_ttbb_BPURITY_DOWN*weight_NJet_SF_ttcc_BPURITY_DOWN*weight_NJet_SF_ttlf_BPURITY_DOWN)*((isTthSample==1)*weight_NJet_SF_ttH_BPURITY_DOWN)*(isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_BPURITY_DOWN)",
    "N_JetWeight_LPURITY_UP:= (((isTTbarSample==1)*weight_NJet_SF_ttbb_LPURITY_UP*weight_NJet_SF_ttcc_LPURITY_UP*weight_NJet_SF_ttlf_LPURITY_UP)*((isTthSample==1)*weight_NJet_SF_ttH_LPURITY_UP)*(isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_LPURITY_UP)",
    "N_JetWeight_LPURITY_DOWN:= (((isTTbarSample==1)*weight_NJet_SF_ttbb_LPURITY_DOWN*weight_NJet_SF_ttcc_LPURITY_DOWN*weight_NJet_SF_ttlf_LPURITY_DOWN)*((isTthSample==1)*weight_NJet_SF_ttH_LPURITY_DOWN)*(isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_LPURITY_DOWN)",
    "N_JetWeight_CERR1_UP:= (((isTTbarSample==1)*weight_NJet_SF_ttbb_CERR1_UP*weight_NJet_SF_ttcc_CERR1_UP*weight_NJet_SF_ttlf_CERR1_UP)*((isTthSample==1)*weight_NJet_SF_ttH_CERR1_UP)*(isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_CERR1_UP)",
    "N_JetWeight_CERR1_DOWN:= (((isTTbarSample==1)*weight_NJet_SF_ttbb_CERR1_DOWN*weight_NJet_SF_ttcc_CERR1_DOWN*weight_NJet_SF_ttlf_CERR1_DOWN)*((isTthSample==1)*weight_NJet_SF_ttH_CERR1_DOWN)*(isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_CERR1_DOWN)",
    "N_JetWeight_CERR2_UP:= (((isTTbarSample==1)*weight_NJet_SF_ttbb_CERR2_UP*weight_NJet_SF_ttcc_CERR2_UP*weight_NJet_SF_ttlf_CERR2_UP)*((isTthSample==1)*weight_NJet_SF_ttH_CERR2_UP)*(isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_CERR2_UP)",
    "N_JetWeight_CERR2_DOWN:= (((isTTbarSample==1)*weight_NJet_SF_ttbb_CERR2_DOWN*weight_NJet_SF_ttcc_CERR2_DOWN*weight_NJet_SF_ttlf_CERR2_DOWN)*((isTthSample==1)*weight_NJet_SF_ttH_CERR2_DOWN)*(isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_CERR2_DOWN)",

    ]

    return addVars
