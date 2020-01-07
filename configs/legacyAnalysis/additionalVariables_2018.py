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
    "weight_NJet_SF_ttH_Nominal:=(((N_Jets==2)*0.988309581757)+((N_Jets==3)*0.986540359853)+((N_Jets==4)*0.98360406277)+((N_Jets==5)*0.973676528405)+((N_Jets==6)*0.961788960927)+((N_Jets==7)*0.936593321903)+((N_Jets==8)*0.932391402684)+((N_Jets>=9)*0.852955462593))",
    "weight_NJet_SF_Others_Nominal:=(((N_Jets==2)*1.01867411742)+((N_Jets==3)*1.00957297213)+((N_Jets==4)*0.980528837392)+((N_Jets==5)*0.958160887939)+((N_Jets==6)*0.961187304813)+((N_Jets==7)*0.793167148673)+((N_Jets==8)*0.931187544001)+((N_Jets>=9)*0.626016213144))",
    "weight_NJet_SF_ttbarOther_Nominal:=(((N_Jets==2)*1.01004894628)+((N_Jets==3)*1.01810161589)+((N_Jets==4)*1.01386105709)+((N_Jets==5)*0.996573860992)+((N_Jets==6)*0.967816926298)+((N_Jets==7)*0.942772861624)+((N_Jets==8)*0.914060021758)+((N_Jets>=9)*0.939194200612))",
    "weight_NJet_SF_ttbarPlus2B_Nominal:=(((N_Jets==2)*1.02018533958)+((N_Jets==3)*1.01779685786)+((N_Jets==4)*1.00987345129)+((N_Jets==5)*1.00425030473)+((N_Jets==6)*0.994386027634)+((N_Jets==7)*0.963120255683)+((N_Jets==8)*0.970070241347)+((N_Jets>=9)*1.02234148622))",
    "weight_NJet_SF_ttbarPlusB_Nominal:=(((N_Jets==2)*0.991064874474)+((N_Jets==3)*0.9895858216)+((N_Jets==4)*0.984175944207)+((N_Jets==5)*0.965260405432)+((N_Jets==6)*0.933131727265)+((N_Jets==7)*0.923009990283)+((N_Jets==8)*0.855995350025)+((N_Jets>=9)*0.849372161097))",
    "weight_NJet_SF_ttbarPlusBBbar_Nominal:=(((N_Jets==2)*0.998293748366)+((N_Jets==3)*0.987628567101)+((N_Jets==4)*0.984501084389)+((N_Jets==5)*0.98077463045)+((N_Jets==6)*0.949139120293)+((N_Jets==7)*0.910364663192)+((N_Jets==8)*0.93158964452)+((N_Jets>=9)*0.948865586747))",
    "weight_NJet_SF_ttbarPlusCCbar_Nominal:=(((N_Jets==2)*1.00518597259)+((N_Jets==3)*1.00708806494)+((N_Jets==4)*1.00790459899)+((N_Jets==5)*0.993024010763)+((N_Jets==6)*0.973912278049)+((N_Jets==7)*0.942641604953)+((N_Jets==8)*0.952984849492)+((N_Jets>=9)*0.86061414658))",


    "weight_NJet_SF_ttH_BSTAT1_UP:=(((N_Jets==2)*0.988787947429)+((N_Jets==3)*0.987330194282)+((N_Jets==4)*0.984467665675)+((N_Jets==5)*0.974363456325)+((N_Jets==6)*0.962381007335)+((N_Jets==7)*0.936688849136)+((N_Jets==8)*0.933175418456)+((N_Jets>=9)*0.853492102573))",
    "weight_NJet_SF_Others_BSTAT1_UP:=(((N_Jets==2)*1.01865042744)+((N_Jets==3)*1.00959446784)+((N_Jets==4)*0.980547794199)+((N_Jets==5)*0.957794734881)+((N_Jets==6)*0.961472324719)+((N_Jets==7)*0.793809427585)+((N_Jets==8)*0.92919453844)+((N_Jets>=9)*0.626547378448))",
    "weight_NJet_SF_ttbarOther_BSTAT1_UP:=(((N_Jets==2)*1.01059631804)+((N_Jets==3)*1.01868054119)+((N_Jets==4)*1.01440433078)+((N_Jets==5)*0.997142829683)+((N_Jets==6)*0.968198492859)+((N_Jets==7)*0.943429774961)+((N_Jets==8)*0.914013837452)+((N_Jets>=9)*0.938374907471))",
    "weight_NJet_SF_ttbarPlus2B_BSTAT1_UP:=(((N_Jets==2)*1.02237822029)+((N_Jets==3)*1.02074790036)+((N_Jets==4)*1.01233445902)+((N_Jets==5)*1.00662259032)+((N_Jets==6)*0.99741625031)+((N_Jets==7)*0.967498063724)+((N_Jets==8)*0.973566113458)+((N_Jets>=9)*1.02510636757))",
    "weight_NJet_SF_ttbarPlusB_BSTAT1_UP:=(((N_Jets==2)*0.990504752307)+((N_Jets==3)*0.988727459654)+((N_Jets==4)*0.983011229625)+((N_Jets==5)*0.964347090923)+((N_Jets==6)*0.930956083016)+((N_Jets==7)*0.922414146334)+((N_Jets==8)*0.855367528586)+((N_Jets>=9)*0.855800042709))",
    "weight_NJet_SF_ttbarPlusBBbar_BSTAT1_UP:=(((N_Jets==2)*0.998158748517)+((N_Jets==3)*0.986893190171)+((N_Jets==4)*0.983755155839)+((N_Jets==5)*0.980014711432)+((N_Jets==6)*0.947840819167)+((N_Jets==7)*0.90833377137)+((N_Jets==8)*0.928386387445)+((N_Jets>=9)*0.953426110933))",
    "weight_NJet_SF_ttbarPlusCCbar_BSTAT1_UP:=(((N_Jets==2)*1.00562662978)+((N_Jets==3)*1.00754628507)+((N_Jets==4)*1.00858119286)+((N_Jets==5)*0.993497436325)+((N_Jets==6)*0.974453043744)+((N_Jets==7)*0.943050077811)+((N_Jets==8)*0.952539547601)+((N_Jets>=9)*0.859804143109))",


    "weight_NJet_SF_ttH_BSTAT1_DOWN:=(((N_Jets==2)*0.987832194314)+((N_Jets==3)*0.985753485266)+((N_Jets==4)*0.982745264458)+((N_Jets==5)*0.972991285957)+((N_Jets==6)*0.961195040782)+((N_Jets==7)*0.936501111109)+((N_Jets==8)*0.931617097042)+((N_Jets>=9)*0.852424011219))",
    "weight_NJet_SF_Others_BSTAT1_DOWN:=(((N_Jets==2)*1.01869821534)+((N_Jets==3)*1.00955146426)+((N_Jets==4)*0.980511171969)+((N_Jets==5)*0.958519942985)+((N_Jets==6)*0.960910716483)+((N_Jets==7)*0.792518431064)+((N_Jets==8)*0.933177741307)+((N_Jets>=9)*0.625469657415))",
    "weight_NJet_SF_ttbarOther_BSTAT1_DOWN:=(((N_Jets==2)*1.00950365273)+((N_Jets==3)*1.0175242618)+((N_Jets==4)*1.01331946746)+((N_Jets==5)*0.996007188108)+((N_Jets==6)*0.967437495857)+((N_Jets==7)*0.942114411315)+((N_Jets==8)*0.914086880432)+((N_Jets>=9)*0.939947462051))",
    "weight_NJet_SF_ttbarPlus2B_BSTAT1_DOWN:=(((N_Jets==2)*1.01801895766)+((N_Jets==3)*1.01486719302)+((N_Jets==4)*1.00742242564)+((N_Jets==5)*1.00190122397)+((N_Jets==6)*0.991389560048)+((N_Jets==7)*0.958818024145)+((N_Jets==8)*0.966625013396)+((N_Jets>=9)*1.01947713909))",
    "weight_NJet_SF_ttbarPlusB_BSTAT1_DOWN:=(((N_Jets==2)*0.991624261011)+((N_Jets==3)*0.990445963586)+((N_Jets==4)*0.985342768615)+((N_Jets==5)*0.966184886279)+((N_Jets==6)*0.935303431152)+((N_Jets==7)*0.92363958798)+((N_Jets==8)*0.856721114402)+((N_Jets>=9)*0.843032377604))",
    "weight_NJet_SF_ttbarPlusBBbar_BSTAT1_DOWN:=(((N_Jets==2)*0.998427305007)+((N_Jets==3)*0.988367199096)+((N_Jets==4)*0.985241751105)+((N_Jets==5)*0.981537972694)+((N_Jets==6)*0.95045291391)+((N_Jets==7)*0.912313621039)+((N_Jets==8)*0.934647635634)+((N_Jets>=9)*0.944381852787))",
    "weight_NJet_SF_ttbarPlusCCbar_BSTAT1_DOWN:=(((N_Jets==2)*1.00474655778)+((N_Jets==3)*1.00663027593)+((N_Jets==4)*1.00722922082)+((N_Jets==5)*0.992551336799)+((N_Jets==6)*0.97336706957)+((N_Jets==7)*0.942224290268)+((N_Jets==8)*0.95340009261)+((N_Jets>=9)*0.86141669889))",


    "weight_NJet_SF_ttH_BSTAT2_UP:=(((N_Jets==2)*0.98847286396)+((N_Jets==3)*0.986784818431)+((N_Jets==4)*0.983790643746)+((N_Jets==5)*0.973902653806)+((N_Jets==6)*0.961745634094)+((N_Jets==7)*0.936843905322)+((N_Jets==8)*0.932731848407)+((N_Jets>=9)*0.852843459655))",
    "weight_NJet_SF_Others_BSTAT2_UP:=(((N_Jets==2)*1.018638927)+((N_Jets==3)*1.00954385956)+((N_Jets==4)*0.980588541843)+((N_Jets==5)*0.958202196584)+((N_Jets==6)*0.961907515573)+((N_Jets==7)*0.792675273487)+((N_Jets==8)*0.932635368423)+((N_Jets>=9)*0.627117163398))",
    "weight_NJet_SF_ttbarOther_BSTAT2_UP:=(((N_Jets==2)*1.01006076459)+((N_Jets==3)*1.01812288907)+((N_Jets==4)*1.01390623241)+((N_Jets==5)*0.996714650776)+((N_Jets==6)*0.967811188431)+((N_Jets==7)*0.942731700532)+((N_Jets==8)*0.914078031623)+((N_Jets>=9)*0.938861266215))",
    "weight_NJet_SF_ttbarPlus2B_BSTAT2_UP:=(((N_Jets==2)*1.02025537001)+((N_Jets==3)*1.01805314244)+((N_Jets==4)*1.01007192557)+((N_Jets==5)*1.00442232837)+((N_Jets==6)*0.994806046683)+((N_Jets==7)*0.964008630914)+((N_Jets==8)*0.971393363532)+((N_Jets>=9)*1.02464972736))",
    "weight_NJet_SF_ttbarPlusB_BSTAT2_UP:=(((N_Jets==2)*0.990814228469)+((N_Jets==3)*0.989139578034)+((N_Jets==4)*0.983682863998)+((N_Jets==5)*0.964836949815)+((N_Jets==6)*0.932595843992)+((N_Jets==7)*0.921931939139)+((N_Jets==8)*0.855353457375)+((N_Jets>=9)*0.853080620292))",
    "weight_NJet_SF_ttbarPlusBBbar_BSTAT2_UP:=(((N_Jets==2)*0.997999292722)+((N_Jets==3)*0.987379933166)+((N_Jets==4)*0.984305549637)+((N_Jets==5)*0.980467845558)+((N_Jets==6)*0.948635913661)+((N_Jets==7)*0.909815119951)+((N_Jets==8)*0.930658416632)+((N_Jets>=9)*0.950851172913))",
    "weight_NJet_SF_ttbarPlusCCbar_BSTAT2_UP:=(((N_Jets==2)*1.00523365194)+((N_Jets==3)*1.00713901732)+((N_Jets==4)*1.008001119)+((N_Jets==5)*0.993038728361)+((N_Jets==6)*0.973965937488)+((N_Jets==7)*0.942706039296)+((N_Jets==8)*0.952708897841)+((N_Jets>=9)*0.859788674239))",


    "weight_NJet_SF_ttH_BSTAT2_DOWN:=(((N_Jets==2)*0.988142836538)+((N_Jets==3)*0.986292746869)+((N_Jets==4)*0.983417117679)+((N_Jets==5)*0.973449257159)+((N_Jets==6)*0.96183132623)+((N_Jets==7)*0.936339057285)+((N_Jets==8)*0.932044784846)+((N_Jets>=9)*0.853065409585))",
    "weight_NJet_SF_Others_BSTAT2_DOWN:=(((N_Jets==2)*1.01870982699)+((N_Jets==3)*1.0096020294)+((N_Jets==4)*0.980470964121)+((N_Jets==5)*0.958122340895)+((N_Jets==6)*0.960461883188)+((N_Jets==7)*0.793671305667)+((N_Jets==8)*0.929731878628)+((N_Jets>=9)*0.624941570185))",
    "weight_NJet_SF_ttbarOther_BSTAT2_DOWN:=(((N_Jets==2)*1.01003689351)+((N_Jets==3)*1.0180798824)+((N_Jets==4)*1.01381457814)+((N_Jets==5)*0.996432031238)+((N_Jets==6)*0.967822404612)+((N_Jets==7)*0.94282041953)+((N_Jets==8)*0.914040408441)+((N_Jets>=9)*0.939559846554))",
    "weight_NJet_SF_ttbarPlus2B_BSTAT2_DOWN:=(((N_Jets==2)*1.02011658698)+((N_Jets==3)*1.01753180566)+((N_Jets==4)*1.00966515057)+((N_Jets==5)*1.00407961)+((N_Jets==6)*0.99394055642)+((N_Jets==7)*0.962215581922)+((N_Jets==8)*0.968700780083)+((N_Jets>=9)*1.02000639943))",
    "weight_NJet_SF_ttbarPlusB_BSTAT2_DOWN:=(((N_Jets==2)*0.991318792773)+((N_Jets==3)*0.990033561595)+((N_Jets==4)*0.984674172473)+((N_Jets==5)*0.965690027651)+((N_Jets==6)*0.933670051379)+((N_Jets==7)*0.924102881942)+((N_Jets==8)*0.856675154581)+((N_Jets>=9)*0.845762234316))",
    "weight_NJet_SF_ttbarPlusBBbar_BSTAT2_DOWN:=(((N_Jets==2)*0.998594116846)+((N_Jets==3)*0.987869273205)+((N_Jets==4)*0.984695098002)+((N_Jets==5)*0.981092575417)+((N_Jets==6)*0.949647294038)+((N_Jets==7)*0.91094480407)+((N_Jets==8)*0.932460877801)+((N_Jets>=9)*0.946786726503))",
    "weight_NJet_SF_ttbarPlusCCbar_BSTAT2_DOWN:=(((N_Jets==2)*1.00513829049)+((N_Jets==3)*1.00703555138)+((N_Jets==4)*1.00780665327)+((N_Jets==5)*0.993009184049)+((N_Jets==6)*0.973856117649)+((N_Jets==7)*0.942576569585)+((N_Jets==8)*0.953253997048)+((N_Jets>=9)*0.86145306348))",


    "weight_NJet_SF_ttH_LSTAT1_UP:=(((N_Jets==2)*0.988476678067)+((N_Jets==3)*0.986833590818)+((N_Jets==4)*0.983975842697)+((N_Jets==5)*0.974033594597)+((N_Jets==6)*0.962130810407)+((N_Jets==7)*0.936632280464)+((N_Jets==8)*0.932427487779)+((N_Jets>=9)*0.852888401964))",
    "weight_NJet_SF_Others_LSTAT1_UP:=(((N_Jets==2)*1.01924702966)+((N_Jets==3)*1.01007370653)+((N_Jets==4)*0.981218134293)+((N_Jets==5)*0.957698297939)+((N_Jets==6)*0.960658257838)+((N_Jets==7)*0.788525529555)+((N_Jets==8)*0.929954629206)+((N_Jets>=9)*0.629290828713))",
    "weight_NJet_SF_ttbarOther_LSTAT1_UP:=(((N_Jets==2)*1.01017730017)+((N_Jets==3)*1.01848193525)+((N_Jets==4)*1.01428453543)+((N_Jets==5)*0.996893311211)+((N_Jets==6)*0.967863472952)+((N_Jets==7)*0.942496619366)+((N_Jets==8)*0.913451158216)+((N_Jets>=9)*0.938653387236))",
    "weight_NJet_SF_ttbarPlus2B_LSTAT1_UP:=(((N_Jets==2)*1.0202864581)+((N_Jets==3)*1.01794938766)+((N_Jets==4)*1.01014766396)+((N_Jets==5)*1.00442017972)+((N_Jets==6)*0.994426939525)+((N_Jets==7)*0.963317636005)+((N_Jets==8)*0.967682418901)+((N_Jets>=9)*1.02129264078))",
    "weight_NJet_SF_ttbarPlusB_LSTAT1_UP:=(((N_Jets==2)*0.991129354697)+((N_Jets==3)*0.989766829169)+((N_Jets==4)*0.984341706923)+((N_Jets==5)*0.965307655689)+((N_Jets==6)*0.933313656707)+((N_Jets==7)*0.922765804815)+((N_Jets==8)*0.854022025047)+((N_Jets>=9)*0.846024121109))",
    "weight_NJet_SF_ttbarPlusBBbar_LSTAT1_UP:=(((N_Jets==2)*0.998368297149)+((N_Jets==3)*0.987667647297)+((N_Jets==4)*0.984643472876)+((N_Jets==5)*0.980804734911)+((N_Jets==6)*0.948715637051)+((N_Jets==7)*0.908917702271)+((N_Jets==8)*0.93117658241)+((N_Jets>=9)*0.950968304167))",
    "weight_NJet_SF_ttbarPlusCCbar_LSTAT1_UP:=(((N_Jets==2)*1.0052509745)+((N_Jets==3)*1.00723000825)+((N_Jets==4)*1.00818453544)+((N_Jets==5)*0.993314130393)+((N_Jets==6)*0.973967878534)+((N_Jets==7)*0.942276662919)+((N_Jets==8)*0.952689578758)+((N_Jets>=9)*0.859418608815))",


    "weight_NJet_SF_ttH_LSTAT1_DOWN:=(((N_Jets==2)*0.988163630252)+((N_Jets==3)*0.986279481371)+((N_Jets==4)*0.983262332873)+((N_Jets==5)*0.973357783957)+((N_Jets==6)*0.961493887701)+((N_Jets==7)*0.936618721929)+((N_Jets==8)*0.932439090268)+((N_Jets>=9)*0.853231106019))",
    "weight_NJet_SF_Others_LSTAT1_DOWN:=(((N_Jets==2)*1.01808707027)+((N_Jets==3)*1.00904259049)+((N_Jets==4)*0.9798032243)+((N_Jets==5)*0.958736186771)+((N_Jets==6)*0.961725935416)+((N_Jets==7)*0.797975601862)+((N_Jets==8)*0.932549976944)+((N_Jets>=9)*0.622567019376))",
    "weight_NJet_SF_ttbarOther_LSTAT1_DOWN:=(((N_Jets==2)*1.00991649912)+((N_Jets==3)*1.01770591414)+((N_Jets==4)*1.01342004954)+((N_Jets==5)*0.996242199937)+((N_Jets==6)*0.967782402613)+((N_Jets==7)*0.943098449948)+((N_Jets==8)*0.914736734726)+((N_Jets>=9)*0.939850106392))",
    "weight_NJet_SF_ttbarPlus2B_LSTAT1_DOWN:=(((N_Jets==2)*1.02007812259)+((N_Jets==3)*1.01764540492)+((N_Jets==4)*1.0095971299)+((N_Jets==5)*1.00410414681)+((N_Jets==6)*0.994350572594)+((N_Jets==7)*0.96301768665)+((N_Jets==8)*0.972661658932)+((N_Jets>=9)*1.02310579686))",
    "weight_NJet_SF_ttbarPlusB_LSTAT1_DOWN:=(((N_Jets==2)*0.991005795687)+((N_Jets==3)*0.989397238858)+((N_Jets==4)*0.984005469707)+((N_Jets==5)*0.965244082668)+((N_Jets==6)*0.933006248007)+((N_Jets==7)*0.923257576528)+((N_Jets==8)*0.858117012795)+((N_Jets>=9)*0.852635515408))",
    "weight_NJet_SF_ttbarPlusBBbar_LSTAT1_DOWN:=(((N_Jets==2)*0.998217171482)+((N_Jets==3)*0.987593296218)+((N_Jets==4)*0.984362174878)+((N_Jets==5)*0.980748619524)+((N_Jets==6)*0.949582983093)+((N_Jets==7)*0.911879190294)+((N_Jets==8)*0.932071730123)+((N_Jets>=9)*0.946502430933))",
    "weight_NJet_SF_ttbarPlusCCbar_LSTAT1_DOWN:=(((N_Jets==2)*1.00511862683)+((N_Jets==3)*1.00694405538)+((N_Jets==4)*1.00761145454)+((N_Jets==5)*0.992731817564)+((N_Jets==6)*0.973877479038)+((N_Jets==7)*0.94310006253)+((N_Jets==8)*0.953362233995)+((N_Jets>=9)*0.861880631298))",


    "weight_NJet_SF_ttH_LSTAT2_UP:=(((N_Jets==2)*0.988880757862)+((N_Jets==3)*0.987318818116)+((N_Jets==4)*0.984514143846)+((N_Jets==5)*0.974539817045)+((N_Jets==6)*0.962574707448)+((N_Jets==7)*0.937436921973)+((N_Jets==8)*0.933154814327)+((N_Jets>=9)*0.854553065093))",
    "weight_NJet_SF_Others_LSTAT2_UP:=(((N_Jets==2)*1.01909400661)+((N_Jets==3)*1.00973828143)+((N_Jets==4)*0.981022966627)+((N_Jets==5)*0.958201937582)+((N_Jets==6)*0.960031411497)+((N_Jets==7)*0.789303010136)+((N_Jets==8)*0.929237809316)+((N_Jets>=9)*0.631409571489))",
    "weight_NJet_SF_ttbarOther_LSTAT2_UP:=(((N_Jets==2)*1.01013781247)+((N_Jets==3)*1.01828261849)+((N_Jets==4)*1.01400992561)+((N_Jets==5)*0.996654853767)+((N_Jets==6)*0.967768808813)+((N_Jets==7)*0.942898783839)+((N_Jets==8)*0.91363271039)+((N_Jets>=9)*0.939045650436))",
    "weight_NJet_SF_ttbarPlus2B_LSTAT2_UP:=(((N_Jets==2)*1.02020088663)+((N_Jets==3)*1.01798438309)+((N_Jets==4)*1.01006149967)+((N_Jets==5)*1.00419298575)+((N_Jets==6)*0.994294617245)+((N_Jets==7)*0.96349176862)+((N_Jets==8)*0.969859605027)+((N_Jets>=9)*1.01823596025))",
    "weight_NJet_SF_ttbarPlusB_LSTAT2_UP:=(((N_Jets==2)*0.991188468793)+((N_Jets==3)*0.989708633099)+((N_Jets==4)*0.984241635944)+((N_Jets==5)*0.965512652541)+((N_Jets==6)*0.933518413877)+((N_Jets==7)*0.922969459337)+((N_Jets==8)*0.854321061695)+((N_Jets>=9)*0.847327535495))",
    "weight_NJet_SF_ttbarPlusBBbar_LSTAT2_UP:=(((N_Jets==2)*0.998489538721)+((N_Jets==3)*0.987715963814)+((N_Jets==4)*0.984630637656)+((N_Jets==5)*0.980855212245)+((N_Jets==6)*0.94874346399)+((N_Jets==7)*0.909366573654)+((N_Jets==8)*0.931469222762)+((N_Jets>=9)*0.947209993481))",
    "weight_NJet_SF_ttbarPlusCCbar_LSTAT2_UP:=(((N_Jets==2)*1.00524743218)+((N_Jets==3)*1.00715874708)+((N_Jets==4)*1.00800867814)+((N_Jets==5)*0.993298756768)+((N_Jets==6)*0.973987667903)+((N_Jets==7)*0.942511317237)+((N_Jets==8)*0.952449424037)+((N_Jets>=9)*0.860210806202))",


    "weight_NJet_SF_ttH_LSTAT2_DOWN:=(((N_Jets==2)*0.987733383913)+((N_Jets==3)*0.985757448936)+((N_Jets==4)*0.982687830966)+((N_Jets==5)*0.97281387306)+((N_Jets==6)*0.961011765403)+((N_Jets==7)*0.935767923005)+((N_Jets==8)*0.931661286946)+((N_Jets>=9)*0.851411134198))",
    "weight_NJet_SF_Others_LSTAT2_DOWN:=(((N_Jets==2)*1.01823621183)+((N_Jets==3)*1.00939013273)+((N_Jets==4)*0.980018688364)+((N_Jets==5)*0.9581457565)+((N_Jets==6)*0.9623879444)+((N_Jets==7)*0.797232169671)+((N_Jets==8)*0.933318569267)+((N_Jets>=9)*0.620470837796))",
    "weight_NJet_SF_ttbarOther_LSTAT2_DOWN:=(((N_Jets==2)*1.00995777875)+((N_Jets==3)*1.01791538098)+((N_Jets==4)*1.0137084878)+((N_Jets==5)*0.996496258667)+((N_Jets==6)*0.967878316656)+((N_Jets==7)*0.942653970173)+((N_Jets==8)*0.914532085258)+((N_Jets>=9)*0.939397895525))",
    "weight_NJet_SF_ttbarPlus2B_LSTAT2_DOWN:=(((N_Jets==2)*1.02016854843)+((N_Jets==3)*1.01760883988)+((N_Jets==4)*1.00968165136)+((N_Jets==5)*1.00433095367)+((N_Jets==6)*0.994496213997)+((N_Jets==7)*0.962800592925)+((N_Jets==8)*0.970307909487)+((N_Jets>=9)*1.02652335406))",
    "weight_NJet_SF_ttbarPlusB_LSTAT2_DOWN:=(((N_Jets==2)*0.990941964025)+((N_Jets==3)*0.98945799747)+((N_Jets==4)*0.984109816202)+((N_Jets==5)*0.965015109224)+((N_Jets==6)*0.932757937223)+((N_Jets==7)*0.923051266782)+((N_Jets==8)*0.857734006321)+((N_Jets>=9)*0.851480080114))",
    "weight_NJet_SF_ttbarPlusBBbar_LSTAT2_DOWN:=(((N_Jets==2)*0.99809363674)+((N_Jets==3)*0.987539961679)+((N_Jets==4)*0.984370687873)+((N_Jets==5)*0.980700960416)+((N_Jets==6)*0.949563532228)+((N_Jets==7)*0.911377802706)+((N_Jets==8)*0.931754874964)+((N_Jets>=9)*0.950490373146))",
    "weight_NJet_SF_ttbarPlusCCbar_LSTAT2_DOWN:=(((N_Jets==2)*1.00512298632)+((N_Jets==3)*1.00701634821)+((N_Jets==4)*1.00779828538)+((N_Jets==5)*0.992746755065)+((N_Jets==6)*0.973858980785)+((N_Jets==7)*0.942810478648)+((N_Jets==8)*0.95358570545)+((N_Jets>=9)*0.861068431876))",


    "weight_NJet_SF_ttH_BPURITY_UP:=(((N_Jets==2)*0.9919324052)+((N_Jets==3)*0.991551352057)+((N_Jets==4)*0.98937198004)+((N_Jets==5)*0.97974508915)+((N_Jets==6)*0.96847799184)+((N_Jets==7)*0.945198677121)+((N_Jets==8)*0.941622668211)+((N_Jets>=9)*0.867691051613))",
    "weight_NJet_SF_Others_BPURITY_UP:=(((N_Jets==2)*1.0189032578)+((N_Jets==3)*1.00887994891)+((N_Jets==4)*0.985035852547)+((N_Jets==5)*0.958208809144)+((N_Jets==6)*0.959787480145)+((N_Jets==7)*0.794959748724)+((N_Jets==8)*0.931010126355)+((N_Jets>=9)*0.638819155111))",
    "weight_NJet_SF_ttbarOther_BPURITY_UP:=(((N_Jets==2)*1.01010440223)+((N_Jets==3)*1.0176259066)+((N_Jets==4)*1.01319683101)+((N_Jets==5)*0.996496849427)+((N_Jets==6)*0.969170790814)+((N_Jets==7)*0.947856709989)+((N_Jets==8)*0.917054176424)+((N_Jets>=9)*0.939549583872))",
    "weight_NJet_SF_ttbarPlus2B_BPURITY_UP:=(((N_Jets==2)*1.02048753253)+((N_Jets==3)*1.01902866198)+((N_Jets==4)*1.01172084063)+((N_Jets==5)*1.00581770461)+((N_Jets==6)*0.996550505246)+((N_Jets==7)*0.96816222597)+((N_Jets==8)*0.972640866772)+((N_Jets>=9)*0.999142715459))",
    "weight_NJet_SF_ttbarPlusB_BPURITY_UP:=(((N_Jets==2)*0.991626749085)+((N_Jets==3)*0.989839389209)+((N_Jets==4)*0.984083993596)+((N_Jets==5)*0.967397605136)+((N_Jets==6)*0.93644145067)+((N_Jets==7)*0.926436887449)+((N_Jets==8)*0.855421953499)+((N_Jets>=9)*0.842114026445))",
    "weight_NJet_SF_ttbarPlusBBbar_BPURITY_UP:=(((N_Jets==2)*0.998948788568)+((N_Jets==3)*0.988463848836)+((N_Jets==4)*0.985229147894)+((N_Jets==5)*0.981475832163)+((N_Jets==6)*0.949767404021)+((N_Jets==7)*0.909554695859)+((N_Jets==8)*0.935867037188)+((N_Jets>=9)*0.938629144671))",
    "weight_NJet_SF_ttbarPlusCCbar_BPURITY_UP:=(((N_Jets==2)*1.00538739024)+((N_Jets==3)*1.00702292282)+((N_Jets==4)*1.00781417938)+((N_Jets==5)*0.994226663502)+((N_Jets==6)*0.975663527585)+((N_Jets==7)*0.945749989646)+((N_Jets==8)*0.952200870645)+((N_Jets>=9)*0.865526261211))",


    "weight_NJet_SF_ttH_BPURITY_DOWN:=(((N_Jets==2)*0.984567273306)+((N_Jets==3)*0.981315774509)+((N_Jets==4)*0.977556198976)+((N_Jets==5)*0.967288027855)+((N_Jets==6)*0.954847665285)+((N_Jets==7)*0.927473314893)+((N_Jets==8)*0.922744696957)+((N_Jets>=9)*0.837683307129))",
    "weight_NJet_SF_Others_BPURITY_DOWN:=(((N_Jets==2)*1.01836312292)+((N_Jets==3)*1.0101153464)+((N_Jets==4)*0.975598350554)+((N_Jets==5)*0.957985803581)+((N_Jets==6)*0.962673830555)+((N_Jets==7)*0.79104090201)+((N_Jets==8)*0.931363248124)+((N_Jets>=9)*0.613449861217))",
    "weight_NJet_SF_ttbarOther_BPURITY_DOWN:=(((N_Jets==2)*1.00998584974)+((N_Jets==3)*1.01855910263)+((N_Jets==4)*1.01447624633)+((N_Jets==5)*0.996536131244)+((N_Jets==6)*0.966424466603)+((N_Jets==7)*0.937259542357)+((N_Jets==8)*0.910833509582)+((N_Jets>=9)*0.939315533051))",
    "weight_NJet_SF_ttbarPlus2B_BPURITY_DOWN:=(((N_Jets==2)*1.01986908654)+((N_Jets==3)*1.01648914324)+((N_Jets==4)*1.00792487689)+((N_Jets==5)*1.00279862688)+((N_Jets==6)*0.992434650526)+((N_Jets==7)*0.958189459735)+((N_Jets==8)*0.968404250741)+((N_Jets>=9)*1.04608818293))",
    "weight_NJet_SF_ttbarPlusB_BPURITY_DOWN:=(((N_Jets==2)*0.990472519503)+((N_Jets==3)*0.989312939306)+((N_Jets==4)*0.984263034814)+((N_Jets==5)*0.962960132994)+((N_Jets==6)*0.929714340955)+((N_Jets==7)*0.919646106055)+((N_Jets==8)*0.855973338012)+((N_Jets>=9)*0.857231149527))",
    "weight_NJet_SF_ttbarPlusBBbar_BPURITY_DOWN:=(((N_Jets==2)*0.997595996997)+((N_Jets==3)*0.986805706853)+((N_Jets==4)*0.983773491374)+((N_Jets==5)*0.979978620753)+((N_Jets==6)*0.948325362008)+((N_Jets==7)*0.911209742156)+((N_Jets==8)*0.927878213663)+((N_Jets>=9)*0.959498664915))",
    "weight_NJet_SF_ttbarPlusCCbar_BPURITY_DOWN:=(((N_Jets==2)*1.00497027076)+((N_Jets==3)*1.00714261152)+((N_Jets==4)*1.00795921208)+((N_Jets==5)*0.991660857208)+((N_Jets==6)*0.972106978766)+((N_Jets==7)*0.939210577164)+((N_Jets==8)*0.954354101639)+((N_Jets>=9)*0.856091017571))",


    "weight_NJet_SF_ttH_LPURITY_UP:=(((N_Jets==2)*0.985530117459)+((N_Jets==3)*0.981258986593)+((N_Jets==4)*0.978058429783)+((N_Jets==5)*0.968678381123)+((N_Jets==6)*0.959025629669)+((N_Jets==7)*0.934651979801)+((N_Jets==8)*0.928603740635)+((N_Jets>=9)*0.852507153909))",
    "weight_NJet_SF_Others_LPURITY_UP:=(((N_Jets==2)*1.01876924533)+((N_Jets==3)*1.01009923862)+((N_Jets==4)*0.980283151292)+((N_Jets==5)*0.958178810558)+((N_Jets==6)*0.958768756373)+((N_Jets==7)*0.793000230645)+((N_Jets==8)*0.934959345932)+((N_Jets>=9)*0.629471932325))",
    "weight_NJet_SF_ttbarOther_LPURITY_UP:=(((N_Jets==2)*1.00641897462)+((N_Jets==3)*1.01432391876)+((N_Jets==4)*1.01018345546)+((N_Jets==5)*0.992577008774)+((N_Jets==6)*0.96544238363)+((N_Jets==7)*0.937378050128)+((N_Jets==8)*0.910929154167)+((N_Jets>=9)*0.934421723878))",
    "weight_NJet_SF_ttbarPlus2B_LPURITY_UP:=(((N_Jets==2)*1.00813846429)+((N_Jets==3)*1.00253498848)+((N_Jets==4)*0.997842538051)+((N_Jets==5)*0.991373550651)+((N_Jets==6)*0.981804212872)+((N_Jets==7)*0.936589895049)+((N_Jets==8)*0.942273771575)+((N_Jets>=9)*0.992369863725))",
    "weight_NJet_SF_ttbarPlusB_LPURITY_UP:=(((N_Jets==2)*0.995864805887)+((N_Jets==3)*0.998363491953)+((N_Jets==4)*0.995274235966)+((N_Jets==5)*0.973505895348)+((N_Jets==6)*0.950116889019)+((N_Jets==7)*0.936526154909)+((N_Jets==8)*0.854820850242)+((N_Jets>=9)*0.829069228103))",
    "weight_NJet_SF_ttbarPlusBBbar_LPURITY_UP:=(((N_Jets==2)*0.998703054619)+((N_Jets==3)*0.991101472657)+((N_Jets==4)*0.989751191595)+((N_Jets==5)*0.985589303604)+((N_Jets==6)*0.957750964465)+((N_Jets==7)*0.923174453769)+((N_Jets==8)*0.956669286791)+((N_Jets>=9)*0.934018527652))",
    "weight_NJet_SF_ttbarPlusCCbar_LPURITY_UP:=(((N_Jets==2)*1.00237574256)+((N_Jets==3)*1.00380892225)+((N_Jets==4)*1.00370995713)+((N_Jets==5)*0.990091151608)+((N_Jets==6)*0.96967577697)+((N_Jets==7)*0.940175877028)+((N_Jets==8)*0.954638388232)+((N_Jets>=9)*0.868915345673))",


    "weight_NJet_SF_ttH_LPURITY_DOWN:=(((N_Jets==2)*0.991103418844)+((N_Jets==3)*0.991909141848)+((N_Jets==4)*0.989311918278)+((N_Jets==5)*0.978727340872)+((N_Jets==6)*0.964487939554)+((N_Jets==7)*0.938468936183)+((N_Jets==8)*0.936867616215)+((N_Jets>=9)*0.853364576691))",
    "weight_NJet_SF_Others_LPURITY_DOWN:=(((N_Jets==2)*1.01860810425)+((N_Jets==3)*1.00906587164)+((N_Jets==4)*0.980876926847)+((N_Jets==5)*0.95828182482)+((N_Jets==6)*0.963569411799)+((N_Jets==7)*0.793154312666)+((N_Jets==8)*0.926626532626)+((N_Jets>=9)*0.62319210397))",
    "weight_NJet_SF_ttbarOther_LPURITY_DOWN:=(((N_Jets==2)*1.01375586646)+((N_Jets==3)*1.02193807656)+((N_Jets==4)*1.01761155337)+((N_Jets==5)*1.00069135796)+((N_Jets==6)*0.970324823991)+((N_Jets==7)*0.948359858533)+((N_Jets==8)*0.917427456502)+((N_Jets>=9)*0.944368188132))",
    "weight_NJet_SF_ttbarPlus2B_LPURITY_DOWN:=(((N_Jets==2)*1.03257703196)+((N_Jets==3)*1.03319433385)+((N_Jets==4)*1.02198791194)+((N_Jets==5)*1.01790564505)+((N_Jets==6)*1.00617626884)+((N_Jets==7)*0.991414555463)+((N_Jets==8)*0.998824799957)+((N_Jets>=9)*1.04895554713))",
    "weight_NJet_SF_ttbarPlusB_LPURITY_DOWN:=(((N_Jets==2)*0.986329795925)+((N_Jets==3)*0.981078086252)+((N_Jets==4)*0.97358637205)+((N_Jets==5)*0.957448356179)+((N_Jets==6)*0.916403988561)+((N_Jets==7)*0.910675865404)+((N_Jets==8)*0.858047567578)+((N_Jets>=9)*0.872752402826))",
    "weight_NJet_SF_ttbarPlusBBbar_LPURITY_DOWN:=(((N_Jets==2)*0.997532069762)+((N_Jets==3)*0.984150606968)+((N_Jets==4)*0.979090592524)+((N_Jets==5)*0.976600829978)+((N_Jets==6)*0.942201290401)+((N_Jets==7)*0.896012261164)+((N_Jets==8)*0.897118588356)+((N_Jets>=9)*0.966556476388))",
    "weight_NJet_SF_ttbarPlusCCbar_LPURITY_DOWN:=(((N_Jets==2)*1.00805436972)+((N_Jets==3)*1.0103908617)+((N_Jets==4)*1.01208443428)+((N_Jets==5)*0.996055592764)+((N_Jets==6)*0.978290565853)+((N_Jets==7)*0.945111805911)+((N_Jets==8)*0.950560409504)+((N_Jets>=9)*0.853052454764))",


    "weight_NJet_SF_ttH_CERR1_UP:=(((N_Jets==2)*0.988845104878)+((N_Jets==3)*0.987700858166)+((N_Jets==4)*0.984264712543)+((N_Jets==5)*0.97494278833)+((N_Jets==6)*0.964102755526)+((N_Jets==7)*0.939641080504)+((N_Jets==8)*0.9344778982)+((N_Jets>=9)*0.856606576483))",
    "weight_NJet_SF_Others_CERR1_UP:=(((N_Jets==2)*1.01903460776)+((N_Jets==3)*1.01019596582)+((N_Jets==4)*0.981146179399)+((N_Jets==5)*0.951204215035)+((N_Jets==6)*0.966096028774)+((N_Jets==7)*0.784333270509)+((N_Jets==8)*0.929337677647)+((N_Jets>=9)*0.572773176332))",
    "weight_NJet_SF_ttbarOther_CERR1_UP:=(((N_Jets==2)*1.00996232469)+((N_Jets==3)*1.01797746408)+((N_Jets==4)*1.01372126872)+((N_Jets==5)*0.996406228442)+((N_Jets==6)*0.967326699141)+((N_Jets==7)*0.942780059505)+((N_Jets==8)*0.915307456725)+((N_Jets>=9)*0.939769122738))",
    "weight_NJet_SF_ttbarPlus2B_CERR1_UP:=(((N_Jets==2)*1.01972501722)+((N_Jets==3)*1.01771462618)+((N_Jets==4)*1.01122018894)+((N_Jets==5)*1.00352771303)+((N_Jets==6)*0.997236957368)+((N_Jets==7)*0.968692260587)+((N_Jets==8)*0.972646864482)+((N_Jets>=9)*1.01738077995))",
    "weight_NJet_SF_ttbarPlusB_CERR1_UP:=(((N_Jets==2)*0.990958217977)+((N_Jets==3)*0.989277878498)+((N_Jets==4)*0.984181600974)+((N_Jets==5)*0.964583509603)+((N_Jets==6)*0.932053666202)+((N_Jets==7)*0.91945325416)+((N_Jets==8)*0.855912581281)+((N_Jets>=9)*0.827814229532))",
    "weight_NJet_SF_ttbarPlusBBbar_CERR1_UP:=(((N_Jets==2)*0.9984707424)+((N_Jets==3)*0.987136742581)+((N_Jets==4)*0.984380962252)+((N_Jets==5)*0.980487799297)+((N_Jets==6)*0.949083969679)+((N_Jets==7)*0.909030767766)+((N_Jets==8)*0.938931465873)+((N_Jets>=9)*0.934135321126))",
    "weight_NJet_SF_ttbarPlusCCbar_CERR1_UP:=(((N_Jets==2)*1.0049663971)+((N_Jets==3)*1.00762231785)+((N_Jets==4)*1.00996740235)+((N_Jets==5)*0.995520193786)+((N_Jets==6)*0.975139426325)+((N_Jets==7)*0.94503568295)+((N_Jets==8)*0.959597077917)+((N_Jets>=9)*0.862381553868))",


    "weight_NJet_SF_ttH_CERR1_DOWN:=(((N_Jets==2)*0.987366691971)+((N_Jets==3)*0.984569056224)+((N_Jets==4)*0.98247725486)+((N_Jets==5)*0.971409260253)+((N_Jets==6)*0.957805106868)+((N_Jets==7)*0.931417052078)+((N_Jets==8)*0.928427473258)+((N_Jets>=9)*0.846602542774))",
    "weight_NJet_SF_Others_CERR1_DOWN:=(((N_Jets==2)*1.01785273398)+((N_Jets==3)*1.00817595212)+((N_Jets==4)*0.979320585997)+((N_Jets==5)*0.969947288594)+((N_Jets==6)*0.94917190961)+((N_Jets==7)*0.807063900448)+((N_Jets==8)*0.935132294615)+((N_Jets>=9)*0.727662989554))",
    "weight_NJet_SF_ttbarOther_CERR1_DOWN:=(((N_Jets==2)*1.01019677929)+((N_Jets==3)*1.01831421132)+((N_Jets==4)*1.01409815368)+((N_Jets==5)*0.996864837565)+((N_Jets==6)*0.968658062377)+((N_Jets==7)*0.942827474222)+((N_Jets==8)*0.912092300996)+((N_Jets>=9)*0.938781903399))",
    "weight_NJet_SF_ttbarPlus2B_CERR1_DOWN:=(((N_Jets==2)*1.0210495629)+((N_Jets==3)*1.01792378211)+((N_Jets==4)*1.0076522013)+((N_Jets==5)*1.00571835366)+((N_Jets==6)*0.989506213865)+((N_Jets==7)*0.951914095195)+((N_Jets==8)*0.963350460487)+((N_Jets>=9)*1.03466446282))",
    "weight_NJet_SF_ttbarPlusB_CERR1_DOWN:=(((N_Jets==2)*0.991262364638)+((N_Jets==3)*0.990058229514)+((N_Jets==4)*0.984146193146)+((N_Jets==5)*0.966362328639)+((N_Jets==6)*0.935241168972)+((N_Jets==7)*0.930130408534)+((N_Jets==8)*0.853765364529)+((N_Jets>=9)*0.887245152542))",
    "weight_NJet_SF_ttbarPlusBBbar_CERR1_DOWN:=(((N_Jets==2)*0.99792760262)+((N_Jets==3)*0.988563486838)+((N_Jets==4)*0.984532125185)+((N_Jets==5)*0.981514896741)+((N_Jets==6)*0.94943140013)+((N_Jets==7)*0.911950360163)+((N_Jets==8)*0.923057706965)+((N_Jets>=9)*0.970808432636))",
    "weight_NJet_SF_ttbarPlusCCbar_CERR1_DOWN:=(((N_Jets==2)*1.00569082333)+((N_Jets==3)*1.00632808463)+((N_Jets==4)*1.00436899554)+((N_Jets==5)*0.988354565304)+((N_Jets==6)*0.97186993632)+((N_Jets==7)*0.937589051069)+((N_Jets==8)*0.939432390446)+((N_Jets>=9)*0.855311297046))",


    "weight_NJet_SF_ttH_CERR2_UP:=(((N_Jets==2)*0.988747439877)+((N_Jets==3)*0.987483541631)+((N_Jets==4)*0.984160501144)+((N_Jets==5)*0.974865827824)+((N_Jets==6)*0.963793636597)+((N_Jets==7)*0.939191673959)+((N_Jets==8)*0.933747407587)+((N_Jets>=9)*0.856446703155))",
    "weight_NJet_SF_Others_CERR2_UP:=(((N_Jets==2)*1.0188309754)+((N_Jets==3)*1.01020607249)+((N_Jets==4)*0.980992148051)+((N_Jets==5)*0.952076149098)+((N_Jets==6)*0.965083859098)+((N_Jets==7)*0.787082103839)+((N_Jets==8)*0.931819180356)+((N_Jets>=9)*0.577557969248))",
    "weight_NJet_SF_ttbarOther_CERR2_UP:=(((N_Jets==2)*1.00995793616)+((N_Jets==3)*1.01797015947)+((N_Jets==4)*1.01370288182)+((N_Jets==5)*0.996372358304)+((N_Jets==6)*0.967401279375)+((N_Jets==7)*0.942716986649)+((N_Jets==8)*0.914625177977)+((N_Jets>=9)*0.939691097117))",
    "weight_NJet_SF_ttbarPlus2B_CERR2_UP:=(((N_Jets==2)*1.01962561362)+((N_Jets==3)*1.01739730198)+((N_Jets==4)*1.0108917509)+((N_Jets==5)*1.00311725759)+((N_Jets==6)*0.996370914839)+((N_Jets==7)*0.966444272908)+((N_Jets==8)*0.971652085406)+((N_Jets>=9)*1.01223005463))",
    "weight_NJet_SF_ttbarPlusB_CERR2_UP:=(((N_Jets==2)*0.990944516756)+((N_Jets==3)*0.989202985914)+((N_Jets==4)*0.983986212921)+((N_Jets==5)*0.964422733957)+((N_Jets==6)*0.931363121392)+((N_Jets==7)*0.920407965452)+((N_Jets==8)*0.854104844048)+((N_Jets>=9)*0.831641146416))",
    "weight_NJet_SF_ttbarPlusBBbar_CERR2_UP:=(((N_Jets==2)*0.998401019741)+((N_Jets==3)*0.987147537306)+((N_Jets==4)*0.984410016007)+((N_Jets==5)*0.980277326612)+((N_Jets==6)*0.948591432356)+((N_Jets==7)*0.909162939729)+((N_Jets==8)*0.940131557041)+((N_Jets>=9)*0.93806107337))",
    "weight_NJet_SF_ttbarPlusCCbar_CERR2_UP:=(((N_Jets==2)*1.00451530961)+((N_Jets==3)*1.00669420773)+((N_Jets==4)*1.00873684958)+((N_Jets==5)*0.994238077013)+((N_Jets==6)*0.974108970356)+((N_Jets==7)*0.943622340041)+((N_Jets==8)*0.957122090051)+((N_Jets>=9)*0.863413919132))",


    "weight_NJet_SF_ttH_CERR2_DOWN:=(((N_Jets==2)*0.987684452962)+((N_Jets==3)*0.985218859451)+((N_Jets==4)*0.98283249604)+((N_Jets==5)*0.971972650179)+((N_Jets==6)*0.958955662815)+((N_Jets==7)*0.932977831313)+((N_Jets==8)*0.93019548254)+((N_Jets>=9)*0.847962623816))",
    "weight_NJet_SF_Others_CERR2_DOWN:=(((N_Jets==2)*1.01834584252)+((N_Jets==3)*1.0084493776)+((N_Jets==4)*0.979833512307)+((N_Jets==5)*0.966585364653)+((N_Jets==6)*0.953577231372)+((N_Jets==7)*0.801149094751)+((N_Jets==8)*0.930774460168)+((N_Jets>=9)*0.700920200023))",
    "weight_NJet_SF_ttbarOther_CERR2_DOWN:=(((N_Jets==2)*1.01017827589)+((N_Jets==3)*1.01828896755)+((N_Jets==4)*1.01408705805)+((N_Jets==5)*0.996860324116)+((N_Jets==6)*0.968405846043)+((N_Jets==7)*0.942887843706)+((N_Jets==8)*0.913358941624)+((N_Jets>=9)*0.938763380878))",
    "weight_NJet_SF_ttbarPlus2B_CERR2_DOWN:=(((N_Jets==2)*1.02102146613)+((N_Jets==3)*1.01838017088)+((N_Jets==4)*1.00848670097)+((N_Jets==5)*1.00596681212)+((N_Jets==6)*0.991486557517)+((N_Jets==7)*0.957666960839)+((N_Jets==8)*0.966271161321)+((N_Jets>=9)*1.03795413974))",
    "weight_NJet_SF_ttbarPlusB_CERR2_DOWN:=(((N_Jets==2)*0.991242202342)+((N_Jets==3)*0.990108653173)+((N_Jets==4)*0.984427051711)+((N_Jets==5)*0.966403392992)+((N_Jets==6)*0.935729109375)+((N_Jets==7)*0.927285234205)+((N_Jets==8)*0.857729813344)+((N_Jets>=9)*0.874724574968))",
    "weight_NJet_SF_ttbarPlusBBbar_CERR2_DOWN:=(((N_Jets==2)*0.998103706596)+((N_Jets==3)*0.988353198695)+((N_Jets==4)*0.984551138552)+((N_Jets==5)*0.981620837372)+((N_Jets==6)*0.950013590188)+((N_Jets==7)*0.911712876114)+((N_Jets==8)*0.922177477746)+((N_Jets>=9)*0.962239904483))",
    "weight_NJet_SF_ttbarPlusCCbar_CERR2_DOWN:=(((N_Jets==2)*1.00618789158)+((N_Jets==3)*1.00770258089)+((N_Jets==4)*1.00673785909)+((N_Jets==5)*0.991067280983)+((N_Jets==6)*0.973570901588)+((N_Jets==7)*0.940429787995)+((N_Jets==8)*0.945752689959)+((N_Jets>=9)*0.854784804974))",



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
    
    
    #combine NJet SF with logic for systematics
##########
# combined factors with logic for syst csv
##########
    "N_JetWeight_Nominal:= ((isTTbarSample==1)*(weight_NJet_SF_ttbb_Nominal+weight_NJet_SF_ttcc_Nominal+weight_NJet_SF_ttlf_Nominal)+((isTthSample==1)*weight_NJet_SF_ttH_Nominal)+((isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_Nominal))",
    "N_JetWeight_BSTAT1_UP:= ((isTTbarSample==1)*(weight_NJet_SF_ttbb_BSTAT1_UP+weight_NJet_SF_ttcc_BSTAT1_UP+weight_NJet_SF_ttlf_BSTAT1_UP)+((isTthSample==1)*weight_NJet_SF_ttH_BSTAT1_UP)+((isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_BSTAT1_UP))",
    "N_JetWeight_BSTAT1_DOWN:= ((isTTbarSample==1)*(weight_NJet_SF_ttbb_BSTAT1_DOWN+weight_NJet_SF_ttcc_BSTAT1_DOWN+weight_NJet_SF_ttlf_BSTAT1_DOWN)+((isTthSample==1)*weight_NJet_SF_ttH_BSTAT1_DOWN)+((isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_BSTAT1_DOWN))",
    "N_JetWeight_BSTAT2_UP:= ((isTTbarSample==1)*(weight_NJet_SF_ttbb_BSTAT2_UP+weight_NJet_SF_ttcc_BSTAT2_UP+weight_NJet_SF_ttlf_BSTAT2_UP)+((isTthSample==1)*weight_NJet_SF_ttH_BSTAT2_UP)+((isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_BSTAT2_UP))",
    "N_JetWeight_BSTAT2_DOWN:= ((isTTbarSample==1)*(weight_NJet_SF_ttbb_BSTAT2_DOWN+weight_NJet_SF_ttcc_BSTAT2_DOWN+weight_NJet_SF_ttlf_BSTAT2_DOWN)+((isTthSample==1)*weight_NJet_SF_ttH_BSTAT2_DOWN)+((isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_BSTAT2_DOWN))",
    "N_JetWeight_LSTAT1_UP:= ((isTTbarSample==1)*(weight_NJet_SF_ttbb_LSTAT1_UP+weight_NJet_SF_ttcc_LSTAT1_UP+weight_NJet_SF_ttlf_LSTAT1_UP)+((isTthSample==1)*weight_NJet_SF_ttH_LSTAT1_UP)+((isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_LSTAT1_UP))",
    "N_JetWeight_LSTAT1_DOWN:= ((isTTbarSample==1)*(weight_NJet_SF_ttbb_LSTAT1_DOWN+weight_NJet_SF_ttcc_LSTAT1_DOWN+weight_NJet_SF_ttlf_LSTAT1_DOWN)+((isTthSample==1)*weight_NJet_SF_ttH_LSTAT1_DOWN)+((isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_LSTAT1_DOWN))",
    "N_JetWeight_LSTAT2_UP:= ((isTTbarSample==1)*(weight_NJet_SF_ttbb_LSTAT2_UP+weight_NJet_SF_ttcc_LSTAT2_UP+weight_NJet_SF_ttlf_LSTAT2_UP)+((isTthSample==1)*weight_NJet_SF_ttH_LSTAT2_UP)+((isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_LSTAT2_UP))",
    "N_JetWeight_LSTAT2_DOWN:= ((isTTbarSample==1)*(weight_NJet_SF_ttbb_LSTAT2_DOWN+weight_NJet_SF_ttcc_LSTAT2_DOWN+weight_NJet_SF_ttlf_LSTAT2_DOWN)+((isTthSample==1)*weight_NJet_SF_ttH_LSTAT2_DOWN)+((isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_LSTAT2_DOWN))",
    "N_JetWeight_BPURITY_UP:= ((isTTbarSample==1)*(weight_NJet_SF_ttbb_BPURITY_UP+weight_NJet_SF_ttcc_BPURITY_UP+weight_NJet_SF_ttlf_BPURITY_UP)+((isTthSample==1)*weight_NJet_SF_ttH_BPURITY_UP)+((isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_BPURITY_UP))",
    "N_JetWeight_BPURITY_DOWN:= ((isTTbarSample==1)*(weight_NJet_SF_ttbb_BPURITY_DOWN+weight_NJet_SF_ttcc_BPURITY_DOWN+weight_NJet_SF_ttlf_BPURITY_DOWN)+((isTthSample==1)*weight_NJet_SF_ttH_BPURITY_DOWN)+((isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_BPURITY_DOWN))",
    "N_JetWeight_LPURITY_UP:= ((isTTbarSample==1)*(weight_NJet_SF_ttbb_LPURITY_UP+weight_NJet_SF_ttcc_LPURITY_UP+weight_NJet_SF_ttlf_LPURITY_UP)+((isTthSample==1)*weight_NJet_SF_ttH_LPURITY_UP)+((isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_LPURITY_UP))",
    "N_JetWeight_LPURITY_DOWN:= ((isTTbarSample==1)*(weight_NJet_SF_ttbb_LPURITY_DOWN+weight_NJet_SF_ttcc_LPURITY_DOWN+weight_NJet_SF_ttlf_LPURITY_DOWN)+((isTthSample==1)*weight_NJet_SF_ttH_LPURITY_DOWN)+((isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_LPURITY_DOWN))",
    "N_JetWeight_CERR1_UP:= ((isTTbarSample==1)*(weight_NJet_SF_ttbb_CERR1_UP+weight_NJet_SF_ttcc_CERR1_UP+weight_NJet_SF_ttlf_CERR1_UP)+((isTthSample==1)*weight_NJet_SF_ttH_CERR1_UP)+((isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_CERR1_UP))",
    "N_JetWeight_CERR1_DOWN:= ((isTTbarSample==1)*(weight_NJet_SF_ttbb_CERR1_DOWN+weight_NJet_SF_ttcc_CERR1_DOWN+weight_NJet_SF_ttlf_CERR1_DOWN)+((isTthSample==1)*weight_NJet_SF_ttH_CERR1_DOWN)+((isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_CERR1_DOWN))",
    "N_JetWeight_CERR2_UP:= ((isTTbarSample==1)*(weight_NJet_SF_ttbb_CERR2_UP+weight_NJet_SF_ttcc_CERR2_UP+weight_NJet_SF_ttlf_CERR2_UP)+((isTthSample==1)*weight_NJet_SF_ttH_CERR2_UP)+((isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_CERR2_UP))",
    "N_JetWeight_CERR2_DOWN:= ((isTTbarSample==1)*(weight_NJet_SF_ttbb_CERR2_DOWN+weight_NJet_SF_ttcc_CERR2_DOWN+weight_NJet_SF_ttlf_CERR2_DOWN)+((isTthSample==1)*weight_NJet_SF_ttH_CERR2_DOWN)+((isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_CERR2_DOWN))",

   ]

    return addVars
