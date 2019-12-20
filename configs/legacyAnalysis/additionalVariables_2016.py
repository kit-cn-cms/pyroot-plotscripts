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
        
    "weight_NJet_SF_ttH_Nominal:=(((N_Jets==2)*0.996733156162)+((N_Jets==3)*0.999400353493)+((N_Jets==4)*1.00007493333)+((N_Jets==5)*0.994237532517)+((N_Jets==6)*0.986724008791)+((N_Jets==7)*0.977874968002)+((N_Jets==8)*0.96526018611)+((N_Jets>=9)*0.955727138536))",
    "weight_NJet_SF_Others_Nominal:=(((N_Jets==2)*0.999953634101)+((N_Jets==3)*0.993981223321)+((N_Jets==4)*0.988817294122)+((N_Jets==5)*0.963001266922)+((N_Jets==6)*0.99293022776)+((N_Jets==7)*0.975590063337)+((N_Jets==8)*0.904854152938)+((N_Jets>=9)*1.29043236404))",
    "weight_NJet_SF_ttbarOther_Nominal:=(((N_Jets==2)*1.00424008648)+((N_Jets==3)*1.00394348348)+((N_Jets==4)*0.997961375816)+((N_Jets==5)*0.98919873762)+((N_Jets==6)*0.976871480047)+((N_Jets==7)*0.970503835166)+((N_Jets==8)*0.948989522527)+((N_Jets>=9)*0.939063986115))",
    "weight_NJet_SF_ttbarPlus2B_Nominal:=(((N_Jets==2)*1.00856053983)+((N_Jets==3)*1.01282547411)+((N_Jets==4)*1.01484311935)+((N_Jets==5)*1.00696471955)+((N_Jets==6)*0.98257298128)+((N_Jets==7)*0.992178377055)+((N_Jets==8)*0.968314335569)+((N_Jets>=9)*0.954426193981))",
    "weight_NJet_SF_ttbarPlusB_Nominal:=(((N_Jets==2)*0.992040668603)+((N_Jets==3)*0.984202254393)+((N_Jets==4)*0.980054917706)+((N_Jets==5)*0.962518986338)+((N_Jets==6)*0.958285651524)+((N_Jets==7)*0.926443819865)+((N_Jets==8)*0.870350857786)+((N_Jets>=9)*0.899614411919))",
    "weight_NJet_SF_ttbarPlusBBbar_Nominal:=(((N_Jets==2)*0.989438605176)+((N_Jets==3)*0.985322548851)+((N_Jets==4)*0.978026196779)+((N_Jets==5)*0.97574156285)+((N_Jets==6)*0.972467332979)+((N_Jets==7)*0.957994492802)+((N_Jets==8)*0.938507316139)+((N_Jets>=9)*0.870143886797))",
    "weight_NJet_SF_ttbarPlusCCbar_Nominal:=(((N_Jets==2)*1.00353247426)+((N_Jets==3)*1.0032068925)+((N_Jets==4)*1.00061765214)+((N_Jets==5)*0.992696001507)+((N_Jets==6)*0.983084664739)+((N_Jets==7)*0.975430263126)+((N_Jets==8)*0.972317900344)+((N_Jets>=9)*0.958997234732))",


    "weight_NJet_SF_ttH_BSTAT1_UP:=(((N_Jets==2)*0.996976392384)+((N_Jets==3)*1.00010781728)+((N_Jets==4)*1.00123642057)+((N_Jets==5)*0.995131758688)+((N_Jets==6)*0.987694882764)+((N_Jets==7)*0.978873456232)+((N_Jets==8)*0.965747727714)+((N_Jets>=9)*0.95589085264))",
    "weight_NJet_SF_Others_BSTAT1_UP:=(((N_Jets==2)*0.999890222783)+((N_Jets==3)*0.994094158368)+((N_Jets==4)*0.988920904351)+((N_Jets==5)*0.962797537491)+((N_Jets==6)*0.993040200076)+((N_Jets==7)*0.976392516838)+((N_Jets==8)*0.906397128551)+((N_Jets>=9)*1.29239261888))",
    "weight_NJet_SF_ttbarOther_BSTAT1_UP:=(((N_Jets==2)*1.00476844892)+((N_Jets==3)*1.00464938041)+((N_Jets==4)*0.998679095536)+((N_Jets==5)*0.98987419315)+((N_Jets==6)*0.977480362058)+((N_Jets==7)*0.971584065708)+((N_Jets==8)*0.950241790463)+((N_Jets>=9)*0.940806910004))",
    "weight_NJet_SF_ttbarPlus2B_BSTAT1_UP:=(((N_Jets==2)*1.01003838817)+((N_Jets==3)*1.01530223783)+((N_Jets==4)*1.01795819012)+((N_Jets==5)*1.00988553819)+((N_Jets==6)*0.983492743449)+((N_Jets==7)*0.995342384693)+((N_Jets==8)*0.97082815144)+((N_Jets>=9)*0.961960947548))",
    "weight_NJet_SF_ttbarPlusB_BSTAT1_UP:=(((N_Jets==2)*0.991489996437)+((N_Jets==3)*0.982983427695)+((N_Jets==4)*0.978718371759)+((N_Jets==5)*0.960495895312)+((N_Jets==6)*0.957295772302)+((N_Jets==7)*0.92359992797)+((N_Jets==8)*0.860664974331)+((N_Jets>=9)*0.897302716625))",
    "weight_NJet_SF_ttbarPlusBBbar_BSTAT1_UP:=(((N_Jets==2)*0.988656027346)+((N_Jets==3)*0.984217675436)+((N_Jets==4)*0.976205686329)+((N_Jets==5)*0.97453976939)+((N_Jets==6)*0.972296097004)+((N_Jets==7)*0.954174889543)+((N_Jets==8)*0.933932405898)+((N_Jets>=9)*0.866417825591))",
    "weight_NJet_SF_ttbarPlusCCbar_BSTAT1_UP:=(((N_Jets==2)*1.00406368592)+((N_Jets==3)*1.00381605446)+((N_Jets==4)*1.00143656453)+((N_Jets==5)*0.993498232011)+((N_Jets==6)*0.983696092168)+((N_Jets==7)*0.976452087205)+((N_Jets==8)*0.974036134361)+((N_Jets>=9)*0.958455823391))",


    "weight_NJet_SF_ttH_BSTAT1_DOWN:=(((N_Jets==2)*0.9964945509)+((N_Jets==3)*0.998699467535)+((N_Jets==4)*0.998922487609)+((N_Jets==5)*0.993345317603)+((N_Jets==6)*0.985754700048)+((N_Jets==7)*0.976886384646)+((N_Jets==8)*0.964782325048)+((N_Jets>=9)*0.95554276972))",
    "weight_NJet_SF_Others_BSTAT1_DOWN:=(((N_Jets==2)*1.0000175906)+((N_Jets==3)*0.993864353148)+((N_Jets==4)*0.988712963176)+((N_Jets==5)*0.963217146071)+((N_Jets==6)*0.992811915806)+((N_Jets==7)*0.974773407559)+((N_Jets==8)*0.903310877146)+((N_Jets>=9)*1.28909147614))",
    "weight_NJet_SF_ttbarOther_BSTAT1_DOWN:=(((N_Jets==2)*1.00372072907)+((N_Jets==3)*1.00324685383)+((N_Jets==4)*0.997249401592)+((N_Jets==5)*0.988528430785)+((N_Jets==6)*0.97626663738)+((N_Jets==7)*0.969434011652)+((N_Jets==8)*0.947767825348)+((N_Jets>=9)*0.937358589788))",
    "weight_NJet_SF_ttbarPlus2B_BSTAT1_DOWN:=(((N_Jets==2)*1.00709353568)+((N_Jets==3)*1.01036729067)+((N_Jets==4)*1.01175780154)+((N_Jets==5)*1.00407720242)+((N_Jets==6)*0.981606738419)+((N_Jets==7)*0.988977142846)+((N_Jets==8)*0.965774396095)+((N_Jets>=9)*0.947367996794))",
    "weight_NJet_SF_ttbarPlusB_BSTAT1_DOWN:=(((N_Jets==2)*0.992602059587)+((N_Jets==3)*0.98543573739)+((N_Jets==4)*0.981402829942)+((N_Jets==5)*0.964556473214)+((N_Jets==6)*0.959246951036)+((N_Jets==7)*0.929214145151)+((N_Jets==8)*0.87989296801)+((N_Jets>=9)*0.901926922796))",
    "weight_NJet_SF_ttbarPlusBBbar_BSTAT1_DOWN:=(((N_Jets==2)*0.990206794683)+((N_Jets==3)*0.986420362546)+((N_Jets==4)*0.97981830152)+((N_Jets==5)*0.976953917921)+((N_Jets==6)*0.972660119278)+((N_Jets==7)*0.961685050975)+((N_Jets==8)*0.94304704175)+((N_Jets>=9)*0.873869055764))",
    "weight_NJet_SF_ttbarPlusCCbar_BSTAT1_DOWN:=(((N_Jets==2)*1.00300965672)+((N_Jets==3)*1.00260411158)+((N_Jets==4)*0.999806698452)+((N_Jets==5)*0.991899563759)+((N_Jets==6)*0.982480969614)+((N_Jets==7)*0.974405399893)+((N_Jets==8)*0.970586509265)+((N_Jets>=9)*0.959543745889))",


    "weight_NJet_SF_ttH_BSTAT2_UP:=(((N_Jets==2)*0.996987767503)+((N_Jets==3)*0.999608793473)+((N_Jets==4)*1.00034681437)+((N_Jets==5)*0.994528878004)+((N_Jets==6)*0.987051659967)+((N_Jets==7)*0.978209204384)+((N_Jets==8)*0.965545691626)+((N_Jets>=9)*0.955860494693))",
    "weight_NJet_SF_Others_BSTAT2_UP:=(((N_Jets==2)*0.999912867052)+((N_Jets==3)*0.994208139722)+((N_Jets==4)*0.989340580362)+((N_Jets==5)*0.962765765001)+((N_Jets==6)*0.992422389484)+((N_Jets==7)*0.976933304431)+((N_Jets==8)*0.905916180533)+((N_Jets>=9)*1.31135225919))",
    "weight_NJet_SF_ttbarOther_BSTAT2_UP:=(((N_Jets==2)*1.00428176285)+((N_Jets==3)*1.004013229)+((N_Jets==4)*0.998039025798)+((N_Jets==5)*0.989350818983)+((N_Jets==6)*0.977082537426)+((N_Jets==7)*0.970744472775)+((N_Jets==8)*0.949471954006)+((N_Jets>=9)*0.939160710373))",
    "weight_NJet_SF_ttbarPlus2B_BSTAT2_UP:=(((N_Jets==2)*1.0093254847)+((N_Jets==3)*1.01335606674)+((N_Jets==4)*1.01504529588)+((N_Jets==5)*1.00762324163)+((N_Jets==6)*0.983071083166)+((N_Jets==7)*0.9931916645)+((N_Jets==8)*0.967703756503)+((N_Jets>=9)*0.952303034528))",
    "weight_NJet_SF_ttbarPlusB_BSTAT2_UP:=(((N_Jets==2)*0.99173334836)+((N_Jets==3)*0.983793065074)+((N_Jets==4)*0.979545817888)+((N_Jets==5)*0.961794518483)+((N_Jets==6)*0.9581567952)+((N_Jets==7)*0.925587344465)+((N_Jets==8)*0.86742664171)+((N_Jets>=9)*0.89723788655))",
    "weight_NJet_SF_ttbarPlusBBbar_BSTAT2_UP:=(((N_Jets==2)*0.98872952558)+((N_Jets==3)*0.984915348881)+((N_Jets==4)*0.978053418369)+((N_Jets==5)*0.976228723021)+((N_Jets==6)*0.973118075137)+((N_Jets==7)*0.958816132763)+((N_Jets==8)*0.937599416413)+((N_Jets>=9)*0.869694300602))",
    "weight_NJet_SF_ttbarPlusCCbar_BSTAT2_UP:=(((N_Jets==2)*1.0036783251)+((N_Jets==3)*1.00335801116)+((N_Jets==4)*1.00085478174)+((N_Jets==5)*0.99288909992)+((N_Jets==6)*0.983340908726)+((N_Jets==7)*0.975018651327)+((N_Jets==8)*0.972521691328)+((N_Jets>=9)*0.959568274641))",


    "weight_NJet_SF_ttH_BSTAT2_DOWN:=(((N_Jets==2)*0.996487520416)+((N_Jets==3)*0.999200954546)+((N_Jets==4)*0.999812589227)+((N_Jets==5)*0.993957159507)+((N_Jets==6)*0.986401401606)+((N_Jets==7)*0.977544674046)+((N_Jets==8)*0.964978664462)+((N_Jets>=9)*0.955609637742))",
    "weight_NJet_SF_Others_BSTAT2_DOWN:=(((N_Jets==2)*0.999997752912)+((N_Jets==3)*0.993753152591)+((N_Jets==4)*0.988289727663)+((N_Jets==5)*0.963229200096)+((N_Jets==6)*0.993442604189)+((N_Jets==7)*0.974252271138)+((N_Jets==8)*0.903791903039)+((N_Jets>=9)*1.26988856305))",
    "weight_NJet_SF_ttbarOther_BSTAT2_DOWN:=(((N_Jets==2)*1.00421156478)+((N_Jets==3)*1.00388543608)+((N_Jets==4)*0.997893896368)+((N_Jets==5)*0.989055009406)+((N_Jets==6)*0.976666348684)+((N_Jets==7)*0.970270659788)+((N_Jets==8)*0.948515935015)+((N_Jets>=9)*0.938967354677))",
    "weight_NJet_SF_ttbarPlus2B_BSTAT2_DOWN:=(((N_Jets==2)*1.00779816924)+((N_Jets==3)*1.0122958851)+((N_Jets==4)*1.01464922579)+((N_Jets==5)*1.00630641621)+((N_Jets==6)*0.982088051788)+((N_Jets==7)*0.991113259132)+((N_Jets==8)*0.968907852458)+((N_Jets>=9)*0.956822965631))",
    "weight_NJet_SF_ttbarPlusB_BSTAT2_DOWN:=(((N_Jets==2)*0.992363263312)+((N_Jets==3)*0.984640075671)+((N_Jets==4)*0.980592136006)+((N_Jets==5)*0.963273877297)+((N_Jets==6)*0.958441425621)+((N_Jets==7)*0.927310511609)+((N_Jets==8)*0.873312491247)+((N_Jets>=9)*0.901943486453))",
    "weight_NJet_SF_ttbarPlusBBbar_BSTAT2_DOWN:=(((N_Jets==2)*0.990156298953)+((N_Jets==3)*0.985742258278)+((N_Jets==4)*0.978011364922)+((N_Jets==5)*0.975264144071)+((N_Jets==6)*0.971837912468)+((N_Jets==7)*0.95719454648)+((N_Jets==8)*0.939421960408)+((N_Jets>=9)*0.870599055481))",
    "weight_NJet_SF_ttbarPlusCCbar_BSTAT2_DOWN:=(((N_Jets==2)*1.00339588313)+((N_Jets==3)*1.0030659312)+((N_Jets==4)*1.00038898652)+((N_Jets==5)*0.992506671148)+((N_Jets==6)*0.982830732166)+((N_Jets==7)*0.975852527401)+((N_Jets==8)*0.972108477779)+((N_Jets>=9)*0.958443508503))",


    "weight_NJet_SF_ttH_LSTAT1_UP:=(((N_Jets==2)*0.996566651053)+((N_Jets==3)*0.999175652265)+((N_Jets==4)*0.999803821831)+((N_Jets==5)*0.993795164877)+((N_Jets==6)*0.985964103875)+((N_Jets==7)*0.976649314943)+((N_Jets==8)*0.963425001796)+((N_Jets>=9)*0.953697434792))",
    "weight_NJet_SF_Others_LSTAT1_UP:=(((N_Jets==2)*1.00018905552)+((N_Jets==3)*0.993919922872)+((N_Jets==4)*0.988422238145)+((N_Jets==5)*0.962075252889)+((N_Jets==6)*0.991927220107)+((N_Jets==7)*0.97219249542)+((N_Jets==8)*0.901609840676)+((N_Jets>=9)*1.36635509937))",
    "weight_NJet_SF_ttbarOther_LSTAT1_UP:=(((N_Jets==2)*1.00429946397)+((N_Jets==3)*1.00410296697)+((N_Jets==4)*0.997901916415)+((N_Jets==5)*0.98878163502)+((N_Jets==6)*0.975765186457)+((N_Jets==7)*0.968843445478)+((N_Jets==8)*0.945990207023)+((N_Jets>=9)*0.934801032113))",
    "weight_NJet_SF_ttbarPlus2B_LSTAT1_UP:=(((N_Jets==2)*1.00856914013)+((N_Jets==3)*1.01270865343)+((N_Jets==4)*1.01479831839)+((N_Jets==5)*1.00618626439)+((N_Jets==6)*0.982370273091)+((N_Jets==7)*0.989213532227)+((N_Jets==8)*0.966323949836)+((N_Jets>=9)*0.948969855699))",
    "weight_NJet_SF_ttbarPlusB_LSTAT1_UP:=(((N_Jets==2)*0.992016787651)+((N_Jets==3)*0.984155449329)+((N_Jets==4)*0.979903161743)+((N_Jets==5)*0.962023227751)+((N_Jets==6)*0.957095916795)+((N_Jets==7)*0.924648175804)+((N_Jets==8)*0.8681293924)+((N_Jets>=9)*0.898962603209))",
    "weight_NJet_SF_ttbarPlusBBbar_LSTAT1_UP:=(((N_Jets==2)*0.989392119633)+((N_Jets==3)*0.985319851979)+((N_Jets==4)*0.97789127034)+((N_Jets==5)*0.975566176985)+((N_Jets==6)*0.971841907505)+((N_Jets==7)*0.956362295051)+((N_Jets==8)*0.937630854794)+((N_Jets>=9)*0.867991873063))",
    "weight_NJet_SF_ttbarPlusCCbar_LSTAT1_UP:=(((N_Jets==2)*1.00354471606)+((N_Jets==3)*1.00322669146)+((N_Jets==4)*1.00055841873)+((N_Jets==5)*0.992238728135)+((N_Jets==6)*0.982370658251)+((N_Jets==7)*0.974016581434)+((N_Jets==8)*0.969960546372)+((N_Jets>=9)*0.957590110454))",


    "weight_NJet_SF_ttH_LSTAT1_DOWN:=(((N_Jets==2)*0.996939898924)+((N_Jets==3)*0.999675624182)+((N_Jets==4)*1.00044398083)+((N_Jets==5)*0.994818717938)+((N_Jets==6)*0.987679418825)+((N_Jets==7)*0.979353638736)+((N_Jets==8)*0.967442741676)+((N_Jets>=9)*0.958207774931))",
    "weight_NJet_SF_Others_LSTAT1_DOWN:=(((N_Jets==2)*0.999767938332)+((N_Jets==3)*0.994202931556)+((N_Jets==4)*0.989136199462)+((N_Jets==5)*0.96386686219)+((N_Jets==6)*0.993634681907)+((N_Jets==7)*0.98043212831)+((N_Jets==8)*0.908599705623)+((N_Jets>=9)*1.22297322948))",
    "weight_NJet_SF_ttbarOther_LSTAT1_DOWN:=(((N_Jets==2)*1.00419224288)+((N_Jets==3)*1.00382282236)+((N_Jets==4)*0.998090719389)+((N_Jets==5)*0.989747140529)+((N_Jets==6)*0.978143700535)+((N_Jets==7)*0.972371438501)+((N_Jets==8)*0.952215260337)+((N_Jets>=9)*0.94393321444))",
    "weight_NJet_SF_ttbarPlus2B_LSTAT1_DOWN:=(((N_Jets==2)*1.00855877963)+((N_Jets==3)*1.01295833899)+((N_Jets==4)*1.01494362111)+((N_Jets==5)*1.00781104091)+((N_Jets==6)*0.982898004667)+((N_Jets==7)*0.995396074735)+((N_Jets==8)*0.970325747229)+((N_Jets>=9)*0.960840579543))",
    "weight_NJet_SF_ttbarPlusB_LSTAT1_DOWN:=(((N_Jets==2)*0.992067112004)+((N_Jets==3)*0.984259210408)+((N_Jets==4)*0.980221786547)+((N_Jets==5)*0.9630258646)+((N_Jets==6)*0.959580228962)+((N_Jets==7)*0.928365267221)+((N_Jets==8)*0.87302083618)+((N_Jets>=9)*0.900775269664))",
    "weight_NJet_SF_ttbarPlusBBbar_LSTAT1_DOWN:=(((N_Jets==2)*0.989483068021)+((N_Jets==3)*0.985345818742)+((N_Jets==4)*0.978191327047)+((N_Jets==5)*0.97595442761)+((N_Jets==6)*0.973242230037)+((N_Jets==7)*0.959799507116)+((N_Jets==8)*0.939407034267)+((N_Jets>=9)*0.872955847343))",
    "weight_NJet_SF_ttbarPlusCCbar_LSTAT1_DOWN:=(((N_Jets==2)*1.00353158478)+((N_Jets==3)*1.00321169306)+((N_Jets==4)*1.00072295442)+((N_Jets==5)*0.993251294955)+((N_Jets==6)*0.98395696004)+((N_Jets==7)*0.977059598072)+((N_Jets==8)*0.974983552414)+((N_Jets>=9)*0.960774928717))",


    "weight_NJet_SF_ttH_LSTAT2_UP:=(((N_Jets==2)*0.996974897029)+((N_Jets==3)*0.999722746464)+((N_Jets==4)*1.00042660669)+((N_Jets==5)*0.994500214108)+((N_Jets==6)*0.986887480605)+((N_Jets==7)*0.977853296181)+((N_Jets==8)*0.964658890703)+((N_Jets>=9)*0.954511419188))",
    "weight_NJet_SF_Others_LSTAT2_UP:=(((N_Jets==2)*1.00014425111)+((N_Jets==3)*0.993812187756)+((N_Jets==4)*0.988620795211)+((N_Jets==5)*0.9629852765)+((N_Jets==6)*0.99063932819)+((N_Jets==7)*0.974070219792)+((N_Jets==8)*0.902989034294)+((N_Jets>=9)*1.30918234025))",
    "weight_NJet_SF_ttbarOther_LSTAT2_UP:=(((N_Jets==2)*1.00428128799)+((N_Jets==3)*1.00402856936)+((N_Jets==4)*0.997918849782)+((N_Jets==5)*0.989020278883)+((N_Jets==6)*0.976282077456)+((N_Jets==7)*0.96965772119)+((N_Jets==8)*0.947210533968)+((N_Jets>=9)*0.936940930015))",
    "weight_NJet_SF_ttbarPlus2B_LSTAT2_UP:=(((N_Jets==2)*1.00854622732)+((N_Jets==3)*1.01270511877)+((N_Jets==4)*1.01471137727)+((N_Jets==5)*1.0068348925)+((N_Jets==6)*0.98254318046)+((N_Jets==7)*0.991490883342)+((N_Jets==8)*0.968314015109)+((N_Jets>=9)*0.949311254187))",
    "weight_NJet_SF_ttbarPlusB_LSTAT2_UP:=(((N_Jets==2)*0.992074989041)+((N_Jets==3)*0.984221162697)+((N_Jets==4)*0.980039512683)+((N_Jets==5)*0.962335041026)+((N_Jets==6)*0.957577406337)+((N_Jets==7)*0.926195275887)+((N_Jets==8)*0.871351603772)+((N_Jets>=9)*0.897703099361))",
    "weight_NJet_SF_ttbarPlusBBbar_LSTAT2_UP:=(((N_Jets==2)*0.989391006495)+((N_Jets==3)*0.985328959694)+((N_Jets==4)*0.977927574524)+((N_Jets==5)*0.975610975029)+((N_Jets==6)*0.97206535291)+((N_Jets==7)*0.957572826081)+((N_Jets==8)*0.937541671893)+((N_Jets>=9)*0.869434832127))",
    "weight_NJet_SF_ttbarPlusCCbar_LSTAT2_UP:=(((N_Jets==2)*1.00355196883)+((N_Jets==3)*1.00325294972)+((N_Jets==4)*1.00060468708)+((N_Jets==5)*0.992445820469)+((N_Jets==6)*0.982684259315)+((N_Jets==7)*0.975006602055)+((N_Jets==8)*0.970099405933)+((N_Jets>=9)*0.959311539352))",


    "weight_NJet_SF_ttH_LSTAT2_DOWN:=(((N_Jets==2)*0.996529692752)+((N_Jets==3)*0.999133022244)+((N_Jets==4)*0.999824382652)+((N_Jets==5)*0.994122619639)+((N_Jets==6)*0.986764713698)+((N_Jets==7)*0.97816227109)+((N_Jets==8)*0.966199163884)+((N_Jets>=9)*0.957389333433))",
    "weight_NJet_SF_Others_LSTAT2_DOWN:=(((N_Jets==2)*0.999831685881)+((N_Jets==3)*0.994306222158)+((N_Jets==4)*0.989098459486)+((N_Jets==5)*0.963133862124)+((N_Jets==6)*0.995201775444)+((N_Jets==7)*0.978028180972)+((N_Jets==8)*0.907144994914)+((N_Jets>=9)*1.2733896594))",
    "weight_NJet_SF_ttbarOther_LSTAT2_DOWN:=(((N_Jets==2)*1.00421774075)+((N_Jets==3)*1.00392566048)+((N_Jets==4)*0.998124667488)+((N_Jets==5)*0.989568411256)+((N_Jets==6)*0.977707559146)+((N_Jets==7)*0.971645653779)+((N_Jets==8)*0.951046080316)+((N_Jets>=9)*0.94174287856))",
    "weight_NJet_SF_ttbarPlus2B_LSTAT2_DOWN:=(((N_Jets==2)*1.00858692888)+((N_Jets==3)*1.01297920252)+((N_Jets==4)*1.01506095384)+((N_Jets==5)*1.00722310854)+((N_Jets==6)*0.982774749823)+((N_Jets==7)*0.993090682369)+((N_Jets==8)*0.968480800975)+((N_Jets>=9)*0.960414177387))",
    "weight_NJet_SF_ttbarPlusB_LSTAT2_DOWN:=(((N_Jets==2)*0.99201758384)+((N_Jets==3)*0.984211040223)+((N_Jets==4)*0.980131609448)+((N_Jets==5)*0.962801719279)+((N_Jets==6)*0.95919702428)+((N_Jets==7)*0.926825018693)+((N_Jets==8)*0.869792994005)+((N_Jets>=9)*0.901867622338))",
    "weight_NJet_SF_ttbarPlusBBbar_LSTAT2_DOWN:=(((N_Jets==2)*0.989490847109)+((N_Jets==3)*0.985336733198)+((N_Jets==4)*0.978168713986)+((N_Jets==5)*0.975940733909)+((N_Jets==6)*0.973025419747)+((N_Jets==7)*0.958637869837)+((N_Jets==8)*0.939562307288)+((N_Jets>=9)*0.871190539372))",
    "weight_NJet_SF_ttbarPlusCCbar_LSTAT2_DOWN:=(((N_Jets==2)*1.00352924194)+((N_Jets==3)*1.00320068013)+((N_Jets==4)*1.00070679919)+((N_Jets==5)*0.993080637533)+((N_Jets==6)*0.983675837199)+((N_Jets==7)*0.9760825367)+((N_Jets==8)*0.97488488201)+((N_Jets>=9)*0.959128087531))",


    "weight_NJet_SF_ttH_BPURITY_UP:=(((N_Jets==2)*1.00056010037)+((N_Jets==3)*1.00462503924)+((N_Jets==4)*1.00678062531)+((N_Jets==5)*1.00211689549)+((N_Jets==6)*0.996856306726)+((N_Jets==7)*0.99051675893)+((N_Jets==8)*0.978647269962)+((N_Jets>=9)*0.968241591801))",
    "weight_NJet_SF_Others_BPURITY_UP:=(((N_Jets==2)*1.00062240155)+((N_Jets==3)*0.994678405921)+((N_Jets==4)*0.993289333695)+((N_Jets==5)*0.974290812393)+((N_Jets==6)*0.971702740924)+((N_Jets==7)*0.986653804639)+((N_Jets==8)*0.904877640215)+((N_Jets>=9)*1.06449782829))",
    "weight_NJet_SF_ttbarOther_BPURITY_UP:=(((N_Jets==2)*1.00446358709)+((N_Jets==3)*1.00441968619)+((N_Jets==4)*0.999353632763)+((N_Jets==5)*0.992632860081)+((N_Jets==6)*0.9823065893)+((N_Jets==7)*0.978097482878)+((N_Jets==8)*0.95911644462)+((N_Jets>=9)*0.959386971016))",
    "weight_NJet_SF_ttbarPlus2B_BPURITY_UP:=(((N_Jets==2)*1.00878190444)+((N_Jets==3)*1.01285578995)+((N_Jets==4)*1.01578317737)+((N_Jets==5)*1.01458443054)+((N_Jets==6)*0.988568389306)+((N_Jets==7)*1.00346739584)+((N_Jets==8)*0.988910563363)+((N_Jets>=9)*0.96210001693))",
    "weight_NJet_SF_ttbarPlusB_BPURITY_UP:=(((N_Jets==2)*0.992696742982)+((N_Jets==3)*0.985057817845)+((N_Jets==4)*0.981750986235)+((N_Jets==5)*0.965987091232)+((N_Jets==6)*0.960942678758)+((N_Jets==7)*0.940197128117)+((N_Jets==8)*0.896698515827)+((N_Jets>=9)*0.890222938727))",
    "weight_NJet_SF_ttbarPlusBBbar_BPURITY_UP:=(((N_Jets==2)*0.989836596635)+((N_Jets==3)*0.985627513201)+((N_Jets==4)*0.979391047532)+((N_Jets==5)*0.977610718285)+((N_Jets==6)*0.976300641759)+((N_Jets==7)*0.964233906614)+((N_Jets==8)*0.937772720988)+((N_Jets>=9)*0.897993955667))",
    "weight_NJet_SF_ttbarPlusCCbar_BPURITY_UP:=(((N_Jets==2)*1.00381558673)+((N_Jets==3)*1.00400085724)+((N_Jets==4)*1.00197975474)+((N_Jets==5)*0.995049506452)+((N_Jets==6)*0.987413179661)+((N_Jets==7)*0.983593937137)+((N_Jets==8)*0.972417772283)+((N_Jets>=9)*0.978646793292))",


    "weight_NJet_SF_ttH_BPURITY_DOWN:=(((N_Jets==2)*0.993159023346)+((N_Jets==3)*0.994522328082)+((N_Jets==4)*0.993898103525)+((N_Jets==5)*0.987165013509)+((N_Jets==6)*0.977474838388)+((N_Jets==7)*0.966106080567)+((N_Jets==8)*0.952985531924)+((N_Jets>=9)*0.94446450814))",
    "weight_NJet_SF_Others_BPURITY_DOWN:=(((N_Jets==2)*0.999630018392)+((N_Jets==3)*0.993916634593)+((N_Jets==4)*0.983683547189)+((N_Jets==5)*0.951777243198)+((N_Jets==6)*1.01410937789)+((N_Jets==7)*0.963731013393)+((N_Jets==8)*0.905374902589)+((N_Jets>=9)*1.66195489405))",
    "weight_NJet_SF_ttbarOther_BPURITY_DOWN:=(((N_Jets==2)*1.00410330837)+((N_Jets==3)*1.00372947492)+((N_Jets==4)*0.996954178339)+((N_Jets==5)*0.986326066649)+((N_Jets==6)*0.971975151693)+((N_Jets==7)*0.963022494154)+((N_Jets==8)*0.939972926801)+((N_Jets>=9)*0.922518285274))",
    "weight_NJet_SF_ttbarPlus2B_BPURITY_DOWN:=(((N_Jets==2)*1.00829359358)+((N_Jets==3)*1.01294917481)+((N_Jets==4)*1.01420781839)+((N_Jets==5)*0.999564697717)+((N_Jets==6)*0.975945407291)+((N_Jets==7)*0.981015290236)+((N_Jets==8)*0.948218433423)+((N_Jets>=9)*0.949298949148))",
    "weight_NJet_SF_ttbarPlusB_BPURITY_DOWN:=(((N_Jets==2)*0.99147132505)+((N_Jets==3)*0.98340648523)+((N_Jets==4)*0.978524990993)+((N_Jets==5)*0.959270438674)+((N_Jets==6)*0.956100208525)+((N_Jets==7)*0.913048330823)+((N_Jets==8)*0.846310619994)+((N_Jets>=9)*0.910694414176))",
    "weight_NJet_SF_ttbarPlusBBbar_BPURITY_DOWN:=(((N_Jets==2)*0.98909638464)+((N_Jets==3)*0.985079877973)+((N_Jets==4)*0.976840752559)+((N_Jets==5)*0.973916566249)+((N_Jets==6)*0.968806159697)+((N_Jets==7)*0.952102472388)+((N_Jets==8)*0.939112183742)+((N_Jets>=9)*0.84461288931))",
    "weight_NJet_SF_ttbarPlusCCbar_BPURITY_DOWN:=(((N_Jets==2)*1.00332189347)+((N_Jets==3)*1.00256387334)+((N_Jets==4)*0.999541336993)+((N_Jets==5)*0.990761571584)+((N_Jets==6)*0.979266048487)+((N_Jets==7)*0.968156148162)+((N_Jets==8)*0.972449464265)+((N_Jets>=9)*0.940627405164))",


    "weight_NJet_SF_ttH_LPURITY_UP:=(((N_Jets==2)*0.994834499649)+((N_Jets==3)*0.995460406812)+((N_Jets==4)*0.994124032148)+((N_Jets==5)*0.989209236042)+((N_Jets==6)*0.981878018342)+((N_Jets==7)*0.973041526484)+((N_Jets==8)*0.96241936753)+((N_Jets>=9)*0.952373603525))",
    "weight_NJet_SF_Others_LPURITY_UP:=(((N_Jets==2)*1.00031758952)+((N_Jets==3)*0.992822242315)+((N_Jets==4)*0.988072339876)+((N_Jets==5)*0.962920640366)+((N_Jets==6)*0.993216677985)+((N_Jets==7)*0.972568129109)+((N_Jets==8)*0.902290621576)+((N_Jets>=9)*1.26316346635))",
    "weight_NJet_SF_ttbarOther_LPURITY_UP:=(((N_Jets==2)*1.0013663315)+((N_Jets==3)*1.00029559043)+((N_Jets==4)*0.994292472342)+((N_Jets==5)*0.985421280389)+((N_Jets==6)*0.973861187375)+((N_Jets==7)*0.965991816621)+((N_Jets==8)*0.943983414872)+((N_Jets>=9)*0.934690083583))",
    "weight_NJet_SF_ttbarPlus2B_LPURITY_UP:=(((N_Jets==2)*1.00230057796)+((N_Jets==3)*1.00215133533)+((N_Jets==4)*1.00429332232)+((N_Jets==5)*0.991751124231)+((N_Jets==6)*0.976600255503)+((N_Jets==7)*0.977549272365)+((N_Jets==8)*0.958946950035)+((N_Jets>=9)*0.956482950411))",
    "weight_NJet_SF_ttbarPlusB_LPURITY_UP:=(((N_Jets==2)*0.995572923407)+((N_Jets==3)*0.990113802618)+((N_Jets==4)*0.986825297379)+((N_Jets==5)*0.972294471114)+((N_Jets==6)*0.965857345374)+((N_Jets==7)*0.94089134498)+((N_Jets==8)*0.921447748457)+((N_Jets>=9)*0.932801483708))",
    "weight_NJet_SF_ttbarPlusBBbar_LPURITY_UP:=(((N_Jets==2)*0.9945232629)+((N_Jets==3)*0.990421734704)+((N_Jets==4)*0.982059372711)+((N_Jets==5)*0.979492087351)+((N_Jets==6)*0.970429704799)+((N_Jets==7)*0.961703463993)+((N_Jets==8)*0.952438635762)+((N_Jets>=9)*0.899420874697))",
    "weight_NJet_SF_ttbarPlusCCbar_LPURITY_UP:=(((N_Jets==2)*1.00074925911)+((N_Jets==3)*0.99968415378)+((N_Jets==4)*0.996200345948)+((N_Jets==5)*0.988924804434)+((N_Jets==6)*0.979701273628)+((N_Jets==7)*0.973434714773)+((N_Jets==8)*0.961949602008)+((N_Jets>=9)*0.955138519363))",


    "weight_NJet_SF_ttH_LPURITY_DOWN:=(((N_Jets==2)*0.998222603396)+((N_Jets==3)*1.0027904392)+((N_Jets==4)*1.00546528821)+((N_Jets==5)*0.998637349357)+((N_Jets==6)*0.990990192511)+((N_Jets==7)*0.981991167432)+((N_Jets==8)*0.967928576871)+((N_Jets>=9)*0.958878277695))",
    "weight_NJet_SF_Others_LPURITY_DOWN:=(((N_Jets==2)*0.999489584624)+((N_Jets==3)*0.994971701335)+((N_Jets==4)*0.989436975061)+((N_Jets==5)*0.9630517932)+((N_Jets==6)*0.992497560067)+((N_Jets==7)*0.979300607259)+((N_Jets==8)*0.907322450486)+((N_Jets>=9)*1.31418126501))",
    "weight_NJet_SF_ttbarOther_LPURITY_DOWN:=(((N_Jets==2)*1.00658575622)+((N_Jets==3)*1.00709688248)+((N_Jets==4)*1.00116252852)+((N_Jets==5)*0.992525047512)+((N_Jets==6)*0.979455706816)+((N_Jets==7)*0.974488263321)+((N_Jets==8)*0.953733860726)+((N_Jets>=9)*0.943157454436))",
    "weight_NJet_SF_ttbarPlus2B_LPURITY_DOWN:=(((N_Jets==2)*1.01419960504)+((N_Jets==3)*1.02320700212)+((N_Jets==4)*1.02521884627)+((N_Jets==5)*1.0223220796)+((N_Jets==6)*0.987698470492)+((N_Jets==7)*1.00513304084)+((N_Jets==8)*0.976044879113)+((N_Jets>=9)*0.958227957794))",
    "weight_NJet_SF_ttbarPlusB_LPURITY_DOWN:=(((N_Jets==2)*0.98804645454)+((N_Jets==3)*0.977676675017)+((N_Jets==4)*0.972847809025)+((N_Jets==5)*0.952140805571)+((N_Jets==6)*0.950466338538)+((N_Jets==7)*0.909807874663)+((N_Jets==8)*0.819063033092)+((N_Jets>=9)*0.867238641515))",
    "weight_NJet_SF_ttbarPlusBBbar_LPURITY_DOWN:=(((N_Jets==2)*0.98337961714)+((N_Jets==3)*0.979236818936)+((N_Jets==4)*0.972253714887)+((N_Jets==5)*0.970998518276)+((N_Jets==6)*0.972900852644)+((N_Jets==7)*0.950908200808)+((N_Jets==8)*0.921570362244)+((N_Jets>=9)*0.84303046384))",
    "weight_NJet_SF_ttbarPlusCCbar_LPURITY_DOWN:=(((N_Jets==2)*1.00592965235)+((N_Jets==3)*1.00630618237)+((N_Jets==4)*1.00466519265)+((N_Jets==5)*0.995966251855)+((N_Jets==6)*0.985934603879)+((N_Jets==7)*0.977174166763)+((N_Jets==8)*0.982500394926)+((N_Jets>=9)*0.963415690635))",


    "weight_NJet_SF_ttH_CERR1_UP:=(((N_Jets==2)*0.996778360233)+((N_Jets==3)*1.00034875651)+((N_Jets==4)*1.00162529814)+((N_Jets==5)*0.996219700781)+((N_Jets==6)*0.989908280318)+((N_Jets==7)*0.982972375796)+((N_Jets==8)*0.970890911809)+((N_Jets>=9)*0.96020428549))",
    "weight_NJet_SF_Others_CERR1_UP:=(((N_Jets==2)*0.998748240932)+((N_Jets==3)*0.99065392891)+((N_Jets==4)*0.987150776282)+((N_Jets==5)*0.949135153174)+((N_Jets==6)*1.00020316352)+((N_Jets==7)*0.952170485306)+((N_Jets==8)*0.915853643533)+((N_Jets>=9)*1.53262195471))",
    "weight_NJet_SF_ttbarOther_CERR1_UP:=(((N_Jets==2)*1.00413534763)+((N_Jets==3)*1.00384624492)+((N_Jets==4)*0.997850206236)+((N_Jets==5)*0.989094925184)+((N_Jets==6)*0.976690891791)+((N_Jets==7)*0.970442938421)+((N_Jets==8)*0.948818300569)+((N_Jets>=9)*0.93795084103))",
    "weight_NJet_SF_ttbarPlus2B_CERR1_UP:=(((N_Jets==2)*1.00889557467)+((N_Jets==3)*1.01297714232)+((N_Jets==4)*1.01551212162)+((N_Jets==5)*1.00884675032)+((N_Jets==6)*0.985410133558)+((N_Jets==7)*0.99593321987)+((N_Jets==8)*0.963108416886)+((N_Jets>=9)*0.969528697432))",
    "weight_NJet_SF_ttbarPlusB_CERR1_UP:=(((N_Jets==2)*0.991926484785)+((N_Jets==3)*0.983518560016)+((N_Jets==4)*0.979628368595)+((N_Jets==5)*0.961210295316)+((N_Jets==6)*0.957355323108)+((N_Jets==7)*0.924247202885)+((N_Jets==8)*0.867806183648)+((N_Jets>=9)*0.888576082782))",
    "weight_NJet_SF_ttbarPlusBBbar_CERR1_UP:=(((N_Jets==2)*0.989751720551)+((N_Jets==3)*0.985134059963)+((N_Jets==4)*0.978330585613)+((N_Jets==5)*0.976621163786)+((N_Jets==6)*0.972491135194)+((N_Jets==7)*0.958178599194)+((N_Jets==8)*0.935712972316)+((N_Jets>=9)*0.86553529298))",
    "weight_NJet_SF_ttbarPlusCCbar_CERR1_UP:=(((N_Jets==2)*1.00302946156)+((N_Jets==3)*1.00301331075)+((N_Jets==4)*1.00196606718)+((N_Jets==5)*0.994441856883)+((N_Jets==6)*0.986421764184)+((N_Jets==7)*0.978928986086)+((N_Jets==8)*0.979321787917)+((N_Jets>=9)*0.960454109249))",


    "weight_NJet_SF_ttH_CERR1_DOWN:=(((N_Jets==2)*0.996641455146)+((N_Jets==3)*0.997846488347)+((N_Jets==4)*0.997586622363)+((N_Jets==5)*0.990946548195)+((N_Jets==6)*0.98155392358)+((N_Jets==7)*0.969542498063)+((N_Jets==8)*0.956147007406)+((N_Jets>=9)*0.949577724217))",
    "weight_NJet_SF_Others_CERR1_DOWN:=(((N_Jets==2)*1.00193019348)+((N_Jets==3)*0.999101285514)+((N_Jets==4)*0.991318246121)+((N_Jets==5)*0.986375812414)+((N_Jets==6)*0.985924339865)+((N_Jets==7)*1.0107153851)+((N_Jets==8)*0.888956926817)+((N_Jets>=9)*1.06755543521))",
    "weight_NJet_SF_ttbarOther_CERR1_DOWN:=(((N_Jets==2)*1.00440798822)+((N_Jets==3)*1.00409725331)+((N_Jets==4)*0.99813717406)+((N_Jets==5)*0.989349249952)+((N_Jets==6)*0.977147752049)+((N_Jets==7)*0.970594687518)+((N_Jets==8)*0.949240686157)+((N_Jets>=9)*0.940685065124))",
    "weight_NJet_SF_ttbarPlus2B_CERR1_DOWN:=(((N_Jets==2)*1.00798567648)+((N_Jets==3)*1.0125961148)+((N_Jets==4)*1.013654204)+((N_Jets==5)*1.00356344784)+((N_Jets==6)*0.977278217498)+((N_Jets==7)*0.986512652507)+((N_Jets==8)*0.977964148756)+((N_Jets>=9)*0.934457994246))",
    "weight_NJet_SF_ttbarPlusB_CERR1_DOWN:=(((N_Jets==2)*0.992258535506)+((N_Jets==3)*0.985318683404)+((N_Jets==4)*0.980651239597)+((N_Jets==5)*0.964499906858)+((N_Jets==6)*0.959626591375)+((N_Jets==7)*0.927833387881)+((N_Jets==8)*0.874369848523)+((N_Jets>=9)*0.917821153375))",
    "weight_NJet_SF_ttbarPlusBBbar_CERR1_DOWN:=(((N_Jets==2)*0.988922434816)+((N_Jets==3)*0.985593904178)+((N_Jets==4)*0.977418849907)+((N_Jets==5)*0.974144390725)+((N_Jets==6)*0.972434153393)+((N_Jets==7)*0.95840927248)+((N_Jets==8)*0.943175877569)+((N_Jets>=9)*0.878897580864))",
    "weight_NJet_SF_ttbarPlusCCbar_CERR1_DOWN:=(((N_Jets==2)*1.00441429048)+((N_Jets==3)*1.00347368904)+((N_Jets==4)*0.998289147633)+((N_Jets==5)*0.989775228091)+((N_Jets==6)*0.977400064368)+((N_Jets==7)*0.970523206019)+((N_Jets==8)*0.961644200354)+((N_Jets>=9)*0.959388505876))",


    "weight_NJet_SF_ttH_CERR2_UP:=(((N_Jets==2)*0.996856823707)+((N_Jets==3)*1.00034478878)+((N_Jets==4)*1.00161306838)+((N_Jets==5)*0.996222193907)+((N_Jets==6)*0.989696117313)+((N_Jets==7)*0.982602344808)+((N_Jets==8)*0.970513667117)+((N_Jets>=9)*0.959740331038))",
    "weight_NJet_SF_Others_CERR2_UP:=(((N_Jets==2)*0.998961271356)+((N_Jets==3)*0.991111067048)+((N_Jets==4)*0.987366030559)+((N_Jets==5)*0.951221944388)+((N_Jets==6)*0.998745296939)+((N_Jets==7)*0.955107228777)+((N_Jets==8)*0.915438320594)+((N_Jets>=9)*1.52407997227))",
    "weight_NJet_SF_ttbarOther_CERR2_UP:=(((N_Jets==2)*1.00414263215)+((N_Jets==3)*1.00384553733)+((N_Jets==4)*0.997853575916)+((N_Jets==5)*0.989079554329)+((N_Jets==6)*0.97663225383)+((N_Jets==7)*0.97040034249)+((N_Jets==8)*0.948514950673)+((N_Jets>=9)*0.93800578019))",
    "weight_NJet_SF_ttbarPlus2B_CERR2_UP:=(((N_Jets==2)*1.00883364918)+((N_Jets==3)*1.01287429154)+((N_Jets==4)*1.01525249136)+((N_Jets==5)*1.00850106111)+((N_Jets==6)*0.984866691719)+((N_Jets==7)*0.996022574168)+((N_Jets==8)*0.964224389028)+((N_Jets>=9)*0.973836472301))",
    "weight_NJet_SF_ttbarPlusB_CERR2_UP:=(((N_Jets==2)*0.991901900628)+((N_Jets==3)*0.983582167692)+((N_Jets==4)*0.979659129231)+((N_Jets==5)*0.961403938976)+((N_Jets==6)*0.957395493831)+((N_Jets==7)*0.924753064672)+((N_Jets==8)*0.867925969779)+((N_Jets>=9)*0.892000230591))",
    "weight_NJet_SF_ttbarPlusBBbar_CERR2_UP:=(((N_Jets==2)*0.989622153312)+((N_Jets==3)*0.985098916045)+((N_Jets==4)*0.978218349421)+((N_Jets==5)*0.976260262266)+((N_Jets==6)*0.972044590178)+((N_Jets==7)*0.958266317776)+((N_Jets==8)*0.93643080121)+((N_Jets>=9)*0.866867929202))",
    "weight_NJet_SF_ttbarPlusCCbar_CERR2_UP:=(((N_Jets==2)*1.00280557897)+((N_Jets==3)*1.00262525836)+((N_Jets==4)*1.00145151163)+((N_Jets==5)*0.993828937374)+((N_Jets==6)*0.985816711672)+((N_Jets==7)*0.978906444598)+((N_Jets==8)*0.978701738776)+((N_Jets>=9)*0.960055226888))",


    "weight_NJet_SF_ttH_CERR2_DOWN:=(((N_Jets==2)*0.996554465767)+((N_Jets==3)*0.998095527153)+((N_Jets==4)*0.997982021021)+((N_Jets==5)*0.99146709338)+((N_Jets==6)*0.982637996901)+((N_Jets==7)*0.971267268227)+((N_Jets==8)*0.958012983058)+((N_Jets>=9)*0.950791814739))",
    "weight_NJet_SF_Others_CERR2_DOWN:=(((N_Jets==2)*1.00130602902)+((N_Jets==3)*0.997845434018)+((N_Jets==4)*0.990636607498)+((N_Jets==5)*0.979293997404)+((N_Jets==6)*0.988109150693)+((N_Jets==7)*1.00171366754)+((N_Jets==8)*0.891596706191)+((N_Jets>=9)*1.09386912112))",
    "weight_NJet_SF_ttbarOther_CERR2_DOWN:=(((N_Jets==2)*1.00437395228)+((N_Jets==3)*1.00407723059)+((N_Jets==4)*0.998108630251)+((N_Jets==5)*0.989355543274)+((N_Jets==6)*0.977189718516)+((N_Jets==7)*0.970649624898)+((N_Jets==8)*0.949642486027)+((N_Jets>=9)*0.940410736295))",
    "weight_NJet_SF_ttbarPlus2B_CERR2_DOWN:=(((N_Jets==2)*1.00816616741)+((N_Jets==3)*1.01277629204)+((N_Jets==4)*1.01424530191)+((N_Jets==5)*1.00464024662)+((N_Jets==6)*0.979111087465)+((N_Jets==7)*0.987165592895)+((N_Jets==8)*0.974586652928)+((N_Jets>=9)*0.930647621517))",
    "weight_NJet_SF_ttbarPlusB_CERR2_DOWN:=(((N_Jets==2)*0.99225242331)+((N_Jets==3)*0.985063121513)+((N_Jets==4)*0.980545614534)+((N_Jets==5)*0.963992312143)+((N_Jets==6)*0.959486131048)+((N_Jets==7)*0.927539108601)+((N_Jets==8)*0.873670595443)+((N_Jets>=9)*0.910068594493))",
    "weight_NJet_SF_ttbarPlusBBbar_CERR2_DOWN:=(((N_Jets==2)*0.989177768678)+((N_Jets==3)*0.985615671112)+((N_Jets==4)*0.97770289591)+((N_Jets==5)*0.974943606884)+((N_Jets==6)*0.97308470197)+((N_Jets==7)*0.958026330619)+((N_Jets==8)*0.941214662878)+((N_Jets>=9)*0.875495508636))",
    "weight_NJet_SF_ttbarPlusCCbar_CERR2_DOWN:=(((N_Jets==2)*1.00457605116)+((N_Jets==3)*1.0039783825)+((N_Jets==4)*0.999375302456)+((N_Jets==5)*0.991058926085)+((N_Jets==6)*0.979184647811)+((N_Jets==7)*0.970893198317)+((N_Jets==8)*0.96378452472)+((N_Jets>=9)*0.959651387328))",



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
