import sys
import os
filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = "/".join(filedir.split("/")[:-1])

sys.path.append(pyrootdir)
import util.tools.plotClasses as plotClasses
import ROOT



memexp = '(memDBp>0.0)*(memDBp)+(memDBp<=0.0)*(0.01)+(memDBp==1.0)*(0.01)'
def evtYieldCategories():
    return []

def add_JTBDT(data):
    cats = [
        ("(N_Jets==4&&N_BTagsM==2)","ljets_j4_t2",""),
        ("(N_Jets==5&&N_BTagsM==2)","ljets_j5_t2",""),
        ("(N_Jets==4&&N_BTagsM==3)","ljets_j4_t3",""),
        ("(N_Jets==4&&N_BTagsM>=4)","ljets_j4_t4",""),
        ("(N_Jets==5&&N_BTagsM==3)","ljets_j5_t3",""),
        ("(N_Jets==5&&N_BTagsM>=4)","ljets_j5_tge4",""),
        ("(N_Jets>=6&&N_BTagsM==2)","ljets_jge6_t2",""),
        ("(N_Jets>=6&&N_BTagsM==3)","ljets_jge6_t3",""),
        ("(N_Jets>=6&&N_BTagsM>=4)","ljets_jge6_tge4",""),
        ]

    discrs = [
        'finalbdt_ljets_j4_t2',
        'finalbdt_ljets_j5_t2',
        'finalbdt_ljets_j4_t3', 
        'finalbdt_ljets_j4_t4', 
        'finalbdt_ljets_j5_t3', 
        'finalbdt_ljets_j5_tge4', 
        'finalbdt_ljets_jge6_t2', 
        'finalbdt_ljets_jge6_t3', 
        'finalbdt_ljets_jge6_tge4'
        ]

    bins = [ 20, 20, 20, 12, 25, 16, 25, 25, 16]

    minX = [ 200, 200, -0.8, -0.8, -0.8, -0.9, -0.6, -0.8, -0.8]
    maxX = [ 800, 800, 0.75, 0.7, 0.7, 0.8, 0.7, 0.75, 0.76]

    data.categories += cats
    data.discrs += discrs
    data.nhistobins += bins
    data.minxvals += minX
    data.maxxvals += maxX
    


def add_JT2D(data):
    unsplitcats = [
        ("(N_Jets==4&&N_BTagsM>=4)","ljets_j4_t4",""),
        ("(N_Jets==5&&N_BTagsM>=4)","ljets_j5_tge4",""),
        ("(N_Jets>=6&&N_BTagsM==3)","ljets_jge6_t3",""),
        ("(N_Jets>=6&&N_BTagsM>=4)","ljets_jge6_tge4",""),
        ]

    #bdtcuts = [-0.2, -0.2, 0.2, 0.22, 0.17, 0.22, 0.05, 0.17, 0.17]
    bdtcuts=[0.22, 0.22, 0.17, 0.17]

    cats = []
    for cat, cut in zip(unsplitcats, bdtcuts):
        cats.append( ('('+cat[0]+')*(finalbdt_'+cat[1]+'>'+str(cut)+')',cat[1]+'_high') ) 
        cats.append( ('('+cat[0]+')*(finalbdt_'+cat[1]+'<='+str(cut)+')',cat[1]+'_low') )

    discrs = [
        memexp,    
        memexp,    
        memexp,    
        memexp,    
        memexp,    
        memexp,    
        memexp,    
        memexp
        ]

    bins = [10, 12, 8, 10, 25, 25, 12, 15]

    minX = [0.05, 0.05, 0.1, 0.1, 0, 0, 0.05, 0]
    maxX = [1.0, 0.9, 1.0, 0.95, 1.0, 1.0, 1.0, 1.0]

    data.categories += cats
    data.discrs += discrs
    data.nhistobins += bins
    data.minxvals += minX
    data.maxxvals += maxX



def add_JT2DOPT(data):
    unsplitcats = [
        ("(N_Jets==4&&N_BTagsM>=4)","ljets_j4_t4",""),
        ("(N_Jets==5&&N_BTagsM>=4)","ljets_j5_tge4",""),
        ("(N_Jets>=6&&N_BTagsM==3)","ljets_jge6_t3",""),
        ("(N_Jets>=6&&N_BTagsM>=4)","ljets_jge6_tge4",""),
        ]

    bdtcuts=[-0.2, -0.2, 0.2, 0.22, 0.17, 0.22, 0.05, 0.17, 0.17]
    
    cats = []
    for cat, cut in zip(unsplitcats, bdtcuts):
        if cat[1] in ["ljets_jge6_tge4", "ljets_j5_tge4", "ljets_j4_t4", "ljets_jge6_t3"]:
            cats.append( ('('+cat[0]+')*(alternativebdt_'+cat[1]+'>'+str(cut)+')',cat[1]+'_ttbbOpt_high') )
            cats.append( ('('+cat[0]+')*(alternativebdt_'+cat[1]+'<='+str(bdt)+')',cat[1]+'_ttbbOpt_low') )

    discrs = [
        memexp,
        memexp,
        memexp,
        memexp,
        memexp,
        memexp,
        memexp,
        memexp
        ]

    bins = [10, 12, 8, 10, 25, 25, 12, 15]

    minX = [0.05, 0.05, 0.1, 0.1, 0, 0, 0.05, 0]
    maxX = [0.95, 0.9, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

    data.categories += cats
    data.discrs += discrs
    data.nhistobins += bins
    data.minxvals += minX
    data.maxxvals += maxX



def add_JTBDTOPT(data):
    cats = [
        ("(N_Jets==4&&N_BTagsM>=4)","ljets_j4_t4_ttbbOpt",""),
        ("(N_Jets==5&&N_BTagsM>=4)","ljets_j5_tge4_ttbbOpt",""),
        ("(N_Jets>=6&&N_BTagsM==3)","ljets_jge6_t3_ttbbOpt",""),
        ("(N_Jets>=6&&N_BTagsM>=4)","ljets_jge6_tge4_ttbbOpt",""),
        ]

    discrs = [
        'alternativebdt_ljets_j4_t4',  
        'alternativebdt_ljets_j5_tge4',  
        'alternativebdt_ljets_jge6_t3', 
        'alternativebdt_ljets_jge6_tge4'
        ]

    bins = [12, 16, 25, 16]

    minX = [-0.8, -0.65, -0.65, -0.7]
    maxX = [0.6, 0.65, 0.65, 0.8]

    data.categories += cats
    data.discrs += discrs
    data.nhistobins += bins
    data.minxvals += minX
    data.maxxvals += maxX



def add_JTMEM(data):
    cats = [
        ("(N_Jets==4&&N_BTagsM==3)","ljets_j4_t3_BLR",""),
        ("(N_Jets==4&&N_BTagsM>=4)","ljets_j4_t4_MEMONLY",""),
        ("(N_Jets==5&&N_BTagsM==3)","ljets_j5_t3_BLR",""),
        ("(N_Jets==5&&N_BTagsM>=4)","ljets_j5_tge4_MEMONLY",""),
        ("(N_Jets>=6&&N_BTagsM==2)","ljets_jge6_t2_BLR",""),
        ("(N_Jets>=6&&N_BTagsM==3)","ljets_jge6_t3_MEMONLY",""),
        ("(N_Jets>=6&&N_BTagsM>=4)","ljets_jge6_tge4_MEMONLY",""),
        ("(N_Jets>=6&&N_BTagsM==3)","ljets_jge6_t3_BLR",""),
        ]

    discrs = [
        'Evt_blr_ETH_transformed',   
        memexp,    
        'Evt_blr_ETH_transformed',    
        memexp,   
        'Evt_blr_ETH_transformed',   
        memexp,   
        memexp, 
        'Evt_blr_ETH_transformed'
        ]

    bins = [20, 12, 20, 18, 25, 25, 16, 25]

    minX = [-1, 0.05, 0.0, 0.1, -3, 0, 0.1, 0.5]
    maxX = [6, 0.9, 6.5, 1.0, 4, 1.0, 0.9, 7.0]

    data.categories += cats
    data.discrs += discrs
    data.nhistobins += bins
    data.minxvals += minX
    data.maxxvals += maxX



def add_MultiDNN(data):
    cats = [
        ("(N_Jets==4&&N_BTagsM>=3&&aachen_pred_class==0)","ljets_j4_tge3_ttHnode",""),
        ("(N_Jets==5&&N_BTagsM>=3&&aachen_pred_class==0)","ljets_j5_tge3_ttHnode",""),
        ("(N_Jets>=6&&N_BTagsM>=3&&aachen_pred_class==0)","ljets_jge6_tge3_ttHnode",""),

        ("(N_Jets==4&&N_BTagsM>=3&&aachen_pred_class==1)","ljets_j4_tge3_ttbbnode",""),
        ("(N_Jets==5&&N_BTagsM>=3&&aachen_pred_class==1)","ljets_j5_tge3_ttbbnode",""),
        ("(N_Jets>=6&&N_BTagsM>=3&&aachen_pred_class==1)","ljets_jge6_tge3_ttbbnode",""),

        ("(N_Jets==4&&N_BTagsM>=3&&aachen_pred_class==2)","ljets_j4_tge3_ttbnode",""),
        ("(N_Jets==5&&N_BTagsM>=3&&aachen_pred_class==2)","ljets_j5_tge3_ttbnode",""),
        ("(N_Jets>=6&&N_BTagsM>=3&&aachen_pred_class==2)","ljets_jge6_tge3_ttbnode",""),

        ("(N_Jets==4&&N_BTagsM>=3&&aachen_pred_class==3)","ljets_j4_tge3_tt2bnode",""),
        ("(N_Jets==5&&N_BTagsM>=3&&aachen_pred_class==3)","ljets_j5_tge3_tt2bnode",""),
        ("(N_Jets>=6&&N_BTagsM>=3&&aachen_pred_class==3)","ljets_jge6_tge3_tt2bnode",""),

        ("(N_Jets==4&&N_BTagsM>=3&&aachen_pred_class==4)","ljets_j4_tge3_ttccnode",""),
        ("(N_Jets==5&&N_BTagsM>=3&&aachen_pred_class==4)","ljets_j5_tge3_ttccnode",""),
        ("(N_Jets>=6&&N_BTagsM>=3&&aachen_pred_class==4)","ljets_jge6_tge3_ttccnode",""),

        ("(N_Jets==4&&N_BTagsM>=3&&aachen_pred_class==5)","ljets_j4_tge3_ttlfnode",""),
        ("(N_Jets==5&&N_BTagsM>=3&&aachen_pred_class==5)","ljets_j5_tge3_ttlfnode",""),
        ("(N_Jets>=6&&N_BTagsM>=3&&aachen_pred_class==5)","ljets_jge6_tge3_ttlfnode",""),

        ("(N_Jets>=6&&N_BTagsM>=2&&aachen_pred_class==0)","ljets_jge6_tge2_ttHnode",""),
        ("(N_Jets>=6&&N_BTagsM>=2&&aachen_pred_class==1)","ljets_jge6_tge2_ttbbnode",""),
        ("(N_Jets>=6&&N_BTagsM>=2&&aachen_pred_class==2)","ljets_jge6_tge2_ttbnode",""),
        ("(N_Jets>=6&&N_BTagsM>=2&&aachen_pred_class==3)","ljets_jge6_tge2_tt2bnode",""),
        ("(N_Jets>=6&&N_BTagsM>=2&&aachen_pred_class==4)","ljets_jge6_tge2_ttccnode",""),
        ("(N_Jets>=6&&N_BTagsM>=2&&aachen_pred_class==5)","ljets_jge6_tge2_ttlfnode",""),
        ]

    discrs = [
        'aachen_Out_ttH',
        'aachen_Out_ttH',
        'aachen_Out_ttH',
        'aachen_Out_ttbarBB',
        'aachen_Out_ttbarBB',
        'aachen_Out_ttbarBB',
        'aachen_Out_ttbarB',
        'aachen_Out_ttbarB',
        'aachen_Out_ttbarB',
        'aachen_Out_ttbar2B',
        'aachen_Out_ttbar2B',
        'aachen_Out_ttbar2B',
        'aachen_Out_ttbarCC',
        'aachen_Out_ttbarCC',
        'aachen_Out_ttbarCC',
        'aachen_Out_ttbarOther',
        'aachen_Out_ttbarOther',
        'aachen_Out_ttbarOther',
        ]
    discrs += [
        'aachen_Out_ttH',
        'aachen_Out_ttbarBB',
        'aachen_Out_ttbarB',
        'aachen_Out_ttbar2B',
        'aachen_Out_ttbarCC',
        'aachen_Out_ttbarOther'
        ]

    bins = [7, 10, 12, 7, 7, 12, 7, 7, 7, 8, 7, 7, 7, 7, 7, 7, 7, 4,]
    bins += [12, 12, 7, 7, 7, 7]

    minX = [0.2, 0.16, 0.17, 0.16, 0.16, 0.18, 0.2, 0.2, 0.18, 0.2, 0.16, 0.16, 0.17, 0.17, 0.21, 0.17, 0.17, 0.19,]
    minX += [0.17, 0.18, 0.18, 0.16, 0.21, 0.19]

    maxX = [0.6,  0.6, 0.7, 0.6, 0.6, 0.7, 0.4, 0.4, 0.35, 0.55, 0.5, 0.55, 0.35, 0.35, 0.3, 0.5, 0.4, 0.3,]
    maxX += [0.7, 0.7, 0.35, 0.55, 0.3, 0.3]

    data.categories += cats
    data.discrs += discrs
    data.nhistobins += bins
    data.minxvals += minX
    data.maxxvals += maxX



def add_JTcontrol(data):
    cats = [
        ("(N_Jets==4&&N_BTagsM==3)","ljets_j4_t3_hardestJetPt",""),
        ]

    discrs = [
        'hardestJetPt'
        ]

    bins = [10]

    minX = [30]
    maxX = [280]

    data.categories += cats
    data.discrs += discrs
    data.nhistobins += bins
    data.minxvals += minX
    data.maxxvals += maxX





def assertLengths(data):
    assert( len(data.nhistobins) == len(data.maxxvals) )
    assert( len(data.nhistobins) == len(data.minxvals) )
    assert( len(data.nhistobins) == len(data.categories) )
    assert( len(data.nhistobins) == len(data.discrs) )

def genPlotInput(data):
    data.plotPreselections = [c[0] for c in data.categories]
    data.binlabels = [c[1] for c in data.categories]


def getDiscriminatorPlots(data, discrname):
    add_JTBDT(data)
    add_JT2D(data)
    #add_JT2DOPT(data)
    #add_JTBDTOPT(data)
    add_JTMEM(data)
    add_MultiDNN(data)
    add_JTcontrol(data)

    assertLengths(data)
    genPlotInput(data)

    discriminatorPlots = []
    for discr, b, blabel, nb, minX, maxX in zip(data.discrs, data.plotPreselections, data.binlabels, data.nhistobins, data.minxvals, data.maxxvals):
        discriminatorPlots.append(
            plotClasses.Plot(
                ROOT.TH1F(discrname+"_"+blabel, "final discriminator ("+blabel+")", nb, minX, maxX),
                discr, b, blabel))

    return discriminatorPlots





