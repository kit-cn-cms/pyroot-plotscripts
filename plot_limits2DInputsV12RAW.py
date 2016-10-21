import sys
import os
sys.path.insert(0, 'limittools')

from scriptgeneratorMEMDBCSV import *
from plotutils import *
from limittools import renameHistos
from limittools import addPseudoData
from limittools import addRealData
from limittools import makeDatacards
from limittools import calcLimits
from limittools import replaceQ2scale
from plotconfigAnalysisV3csv import *

# output name
name='inputs2DV12RAW'

# define categories
boosted="(BoostedTopHiggs_TopHadCandidate_TopMVAOutput>=-0.485&&BoostedTopHiggs_HiggsCandidate_HiggsTag>=0.8925)"                        
categories_=[
              ("(N_Jets==4&&N_BTagsM==2)","ljets_j4_t2",""),
              ("(N_Jets==5&&N_BTagsM==2)","ljets_j5_t2",""),
              ("(N_Jets==4&&N_BTagsM==3)","ljets_j4_t3",""),
              ("(N_Jets==4&&N_BTagsM>=4)","ljets_j4_t4",""),
              ("(N_Jets==5&&N_BTagsM==3)","ljets_j5_t3",""),
              ("(N_Jets==5&&N_BTagsM>=4)","ljets_j5_tge4",""),             
              ("(N_Jets>=6&&N_BTagsM==2)","ljets_jge6_t2",""),
              ("(N_Jets>=6&&N_BTagsM==3)","ljets_jge6_t3",""),
              ("(N_Jets>=6&&N_BTagsM>=4)","ljets_jge6_tge4","")
]

categories=[]
#categories=categories_
bdtcuts=[-0.2,-0.2,0.2,0.26,0.17,0.26,0.1,0.12,0.13]
for cat,bdt in zip(categories_,bdtcuts):
  if cat[1] in ["ljets_jge6_tge4","ljets_j5_tge4","ljets_j4_t4","ljets_jge6_t3","ljets_j5_t3","ljets_j4_t3"]:
    categories.append(('('+cat[0]+')*(finalbdt_'+cat[1]+'>'+str(bdt)+')',cat[1]+'_high') )
    categories.append(('('+cat[0]+')*(finalbdt_'+cat[1]+'<='+str(bdt)+')',cat[1]+'_low') )
  #else:
    #categories.append(cat)

# add unsplit categories
for cat,bdt in zip(categories_,bdtcuts):
  categories.append(cat)

print categories

# define MEM discriminator variable
memexp='(memDBp>0.0)*(memDBp_sig/(memDBp_sig+0.15*memDBp_bkg))+(memDBp<0.0)*(0.01)'

# define BDT output variables
bdtweightpath="/nfs/dust/cms/user/kelmorab/80xBDTWeights/"
bdtset="V4"
additionalvariables=[
			'finalbdt_ljets_j4_t2:=Evt_HT_Jets',
			'finalbdt_ljets_j5_t2:=Evt_HT_Jets',
                      'finalbdt_ljets_j4_t3:='+bdtweightpath+'/weights_43_'+bdtset+'.xml',
                      'finalbdt_ljets_j4_t4:='+bdtweightpath+'/weights_44_'+bdtset+'.xml',
                      'finalbdt_ljets_j5_t3:='+bdtweightpath+'/weights_53_'+bdtset+'.xml',
                      'finalbdt_ljets_j5_tge4:='+bdtweightpath+'/weights_54_'+bdtset+'.xml',
                      'finalbdt_ljets_jge6_t2:='+bdtweightpath+'/weights_62_'+bdtset+'.xml',
                      'finalbdt_ljets_jge6_t3:='+bdtweightpath+'/weights_63_'+bdtset+'.xml',
                      'finalbdt_ljets_jge6_tge4:='+bdtweightpath+'/weights_64_'+bdtset+'.xml',
                      #'finalbdt_ljets_boosted:='+bdtweightpath+'/weights_Final_DB_boosted_76xmem.xml',
                      "Jet_Pt","Jet_Eta","Jet_CSV","Jet_Flav","N_Jets","Weight_CSV","Weight_CSVLFup","Weight_CSVLFdown","Weight_CSVHFup","Weight_CSVHFdown","Weight_CSVHFStats1up","Weight_CSVHFStats1down","Weight_CSVLFStats1up","Weight_CSVLFStats1down","Weight_CSVHFStats2up","Weight_CSVHFStats2down","Weight_CSVLFStats2up","Weight_CSVLFStats2down","Weight_CSVCErr1up","Weight_CSVCErr1down","Weight_CSVCErr2up","Weight_CSVCErr2down",
]

# set discriminator histograms configuration
nhistobins= [ 	10, 10,     5,5,         10,10,    5,5,         10,10,   5,5 ]+[  20,20, 	10,   10,    10,    10,   20,   10,   10 ]
minxvals=   [ 0, 0,  	    0,0,         0,0       ,0,0 ,       0,0,0,0,]+[ 200, 200, -0.7,  -0.75, -0.8,   -0.8, -0.8, -0.8,   -0.7]
maxxvals=   [  0.9, 0.9,  0.8,0.8,   0.95,0.95,    0.9,0.9 ,   0.9,   0.9,0.9,   0.9]+[800,800,    0.8,  0.75,   0.8,    0.7,  0.7,  0.75,    0.65]


#nhistobins= [  200]*9
#minxvals=   [ 200, 200, -1,-1,-1,-1,-1,-1,-1]
#maxxvals=   [700,700, 1.0,1.0,1.0,1.0,1.0,1.0,1.0]

#nhistobins= [   50 ]*7
#minxvals=   [-1.0]*7
#maxxvals=   [1.0]*7

discrs =    [memexp, memexp, memexp, memexp,memexp, memexp,memexp, memexp,  memexp, memexp,memexp, memexp]+ ['finalbdt_ljets_j4_t2','finalbdt_ljets_j5_t2','finalbdt_ljets_j4_t3', 'finalbdt_ljets_j4_t4', 'finalbdt_ljets_j5_t3', 'finalbdt_ljets_j5_tge4', 'finalbdt_ljets_jge6_t2', 'finalbdt_ljets_jge6_t3', 'finalbdt_ljets_jge6_tge4']
discrname='finaldiscr'
assert(len(nhistobins)==len(maxxvals))
assert(len(nhistobins)==len(minxvals))
assert(len(nhistobins)==len(categories))
assert(len(nhistobins)==len(discrs))

# get input for plotting function
bins= [c[0] for c in categories]
binlabels= [c[1] for c in categories]
samples=samplesLimits
allsystnames=weightsystnames+othersystnames

# adapt weights for exlusive samples
systsamples=[]
for sample in samples:
  for sysname,sysfilename in zip(othersystnames,othersystfilenames):
    thisnewsel=sample.selection
    systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),thisnewsel,sample.nick+sysname))
  
allsamples=samples+systsamples
samplesdata=samples_data_controlplots

# define plots
bdts=[]
print len(discrs),len(bins),len(binlabels),len(nhistobins),len(minxvals),len(maxxvals),
print len(zip(discrs,bins,binlabels,nhistobins,minxvals,maxxvals))
for discr,b,bl,nb,minx,maxx in zip(discrs,bins,binlabels,nhistobins,minxvals,maxxvals):
  bdts.append(Plot(ROOT.TH1F("finaldiscr_"+bl,"final discriminator ("+bl+")",nb,minx,maxx),discr,b))

categoriesJT=[
              ("(N_Jets>=6&&N_BTagsM==2)","6j2t",""),
              ("(N_Jets==4&&N_BTagsM==3)","4j3t",""),
              ("(N_Jets==5&&N_BTagsM==3)","5j3t",""),
              ("(N_Jets>=6&&N_BTagsM==3)","6j3t",""),
              ("(N_Jets==4&&N_BTagsM>=4)","4j4t",""),
              ("(N_Jets==5&&N_BTagsM>=4)","5j4t",""),
              ("(N_Jets>=6&&N_BTagsM>=4)","6j4t","")
]

plotlabel="1 lepton, 4 jets, 3 b-tags"
plotselection=categoriesJT[1][0]
plotprefix="inputVar_s43_"
plots43=[
    Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_HT","HT",20,0,1000),"BDT_common5_input_HT",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_sphericity","sphericity",20,0,1),"BDT_common5_input_sphericity",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_third_highest_btag","third highest btag",22,0.79,1),"BDT_common5_input_third_highest_btag",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_h1","H_{1}",30,-0.2,0.4),"BDT_common5_input_h1",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_dr_between_lep_and_closest_jet","#Delta R (lepton,jet)",35,0,3.5),"BDT_common5_input_dr_between_lep_and_closest_jet",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"s43_blr","B-tagging likelihood ratio",30,-3,8),"Evt_blr_ETH_transformed",'(N_Jets==4&&N_BTagsM==3)',plotlabel),
    Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_dev_from_avg_disc_btags","dev from avg b-tag (tags)",25,0,0.008),"BDT_common5_input_dev_from_avg_disc_btags",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_fourth_jet_pt","jet 4 p_{T}",32,0,160),"BDT_common5_input_fourth_jet_pt",plotselection,plotlabel),
]

plotlabel="1 lepton, 4 jets, 4 b-tags"
plotselection=categoriesJT[4][0]
plotprefix="inputVar_s44_"
# weights_Final_44_MEMBDTv2.xml
plots44=[
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_btag_disc_btags","avg CSV tagged",6,0.8,1.05),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_aplanarity","aplanarity",9,0,0.3),"BDT_common5_input_aplanarity",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","dijet mass of closest tagged jets",10,0,200),"BDT_common5_input_closest_tagged_dijet_mass",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_all_sum_pt_with_met","#sum p_{T} (lepton,jet,met)",10,0,1000),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h3","H_{3}",15,-0.2,1.0),"BDT_common5_input_h3",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","(#sum jet p_{T})/(#sum jet E))",20,0.2,1.2),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotselection,plotlabel),
]

plotlabel="1 lepton, 5 jets, 3 b-tags"
plotselection=categoriesJT[2][0]
plotprefix="inputVar_s53_"
plots53=[
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_all_sum_pt_with_met","#sum p_{T} (lepton,jet,met)",30,0,1500),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"blr","B-tagging likelihood ratio",20,-2,10),"Evt_blr_ETH_transformed",'(N_Jets==5&&N_BTagsM==3)',plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",30,0.5,3.5),"BDT_common5_input_avg_dr_tagged_jets",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_sphericity","sphericity",25,0,1),"BDT_common5_input_sphericity",plotselection,plotlabel),
    #Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","dev from ave CSV (tags)",25,0,0.008),"BDT_common5_input_dev_from_avg_disc_btags",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_btag_disc_btags","avg CSV tagged",25,0.8,1.05),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","#Delta R (lepton,jet)",25,0,3.2),"BDT_common5_input_dr_between_lep_and_closest_jet",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_tag_tag","max #Delta #eta (tag,avg tag #eta)",25,0,1.5),"BDT_common5_input_maxeta_tag_tag",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_third_jet_pt","jet 3 p_{T}",20,0,250),"BDT_common5_input_third_jet_pt",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h2","H_{2}",20,0,0.15),"BDT_common5_input_h2",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","dijet mass of closest tagged jets",10,0,200),"BDT_common5_input_closest_tagged_dijet_mass",plotselection,plotlabel),
]

plotlabel="1 lepton, 5 jets, #geq4 b-tags"
plotselection=categoriesJT[5][0]
plotprefix="inputVar_s54_"
plots54=[
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_btag_disc_btags","avg CSV (tags)",7,.8,1.04),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"Evt_Deta_JetsAverage","avg #Delta #eta jets",10,0,2.5),"Evt_Deta_JetsAverage",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_M3","M3",20,0,1000),"BDT_common5_input_M3",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_all_sum_pt_with_met","#sum (lepton pt,jet pt,met)",12,0,1200),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",10,1,4),"BDT_common5_input_avg_dr_tagged_jets",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","closest tagged dijet mass",10,0,200),"BDT_common5_input_closest_tagged_dijet_mass",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","tagged dijet mass closest to 125",10,80,180),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_HT","HT",10,0,1000),"BDT_common5_input_HT",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_aplanarity","aplanarity",9,0,0.3),"BDT_common5_input_aplanarity",plotselection,plotlabel),
]

plotlabel="1 lepton, #geq6 jets, 3 b-tags"
plotselection=categoriesJT[3][0]
plotprefix="inputVar_s63_"
plots63=[
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","dev from ave CSV (tags)",25,0,0.008),"BDT_common5_input_dev_from_avg_disc_btags",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_all_sum_pt_with_met","#sum (lepton pt,jet pt,met)",25,0,2000),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_aplanarity","aplanarity",20,0,0.4),"BDT_common5_input_aplanarity",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"blr","B-tagging likelihood ratio",20,-2,8),"Evt_blr_ETH_transformed",'(N_Jets>=6&&N_BTagsM==3)',plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_min_dr_tagged_jets","min #Delta R (tag,tag)",17,0,3.4),"BDT_common5_input_min_dr_tagged_jets",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dEta_fn","#sqrt{#Delta #eta(t^{lep}, bb) #times #Delta #eta(t^{had}, bb)}",20,0,5),"BDT_common5_input_dEta_fn",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","(#sum jet p_{T})/(#sum jet E))",10,0.2,1.1),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotselection,plotlabel),
]

plotlabel="1 lepton, #geq6 jets, #geq4 b-tags"
plotselection=categoriesJT[6][0]
plotprefix="inputVar_s64_"
plots64=[
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_best_higgs_mass","best higgs mass",30,0,600),"BDT_common5_input_best_higgs_mass",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","tagged dijet mass closest to 125",17,40,210),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fourth_highest_btag","fourth highest btag",22,.8,1),"BDT_common5_input_fourth_highest_btag",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fifth_highest_CSV","fifth highest CSV",22,-.1,1),"BDT_common5_input_fifth_highest_CSV",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_all_sum_pt_with_met","#sum (lepton pt,jet pt,met)",10,200,2000),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_invariant_mass_of_everything","mass(jets,lepton,MET)",10,400,1600),"BDT_common5_input_invariant_mass_of_everything",plotselection,plotlabel),
]

additPlots=plots64+plots63+plots54+plots53+plots44+plots43
bdts=bdts+additPlots
print bdts
# plot everthing
outputpath=plotParallel(name,500000,bdts,allsamples+samplesdata,[''],['1.'],weightsystnames,systweights,additionalvariables,[["memDB","/nfs/dust/cms/user/kelmorab/DataBases/MemDataBase_ICHEP_V5New",False]],"/nfs/dust/cms/user/kelmorab/plotscripts80X/higgsCoupling/pyroot-plotscripts/treejson.json")

if not os.path.exists(name):
  os.makedirs(name)

# rename output histos and save in one file
#renameHistos(outputpath,name+'/'+name+'_limitInput.root',allsystnames)

#replaceQ2scale( os.getcwd()+'/'+name+'/'+name+'_limitInput.root')


additbinlables=[]
for p in additPlots:
  additbinlables.append(p.name.replace("inputVar_",""))
  
print samples
# add real/pseudo data
#addPseudoData(name+'/'+name+'_limitInput.root',[s.nick for s in samples[9:]],binlabels,allsystnames,discrname)
addRealData(name+'/'+name+'_limitInput.root',[s.nick for s in samples_data_controlplots],binlabels,discrname)
addRealData(name+'/'+name+'_limitInput.root',[s.nick for s in samples_data_controlplots],additbinlables,"inputVar")

# make datacards
listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,bdts)
lolT=transposeLOL(listOfHistoLists)
writeLOLAndOneOnTop(transposeLOL(lolT[9:]),samples[9:],lolT[0],samples[0],20,name+'/'+name+'_controlplots')
#writeListOfHistoListsAN(transposeLOL([lolT[0]]+lolT[9:]),samples_,"",name+'/'+name+'_controlplots_no_stack',True,False,False,'histo',False,False,False)


#plotdiscriminants
labels=[plot.label for plot in bdts]
listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,bdts,1)
listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samplesdata,bdts,1)
if not os.path.exists(outputpath[:-4]+'_syst.root') or not askYesNo('reuse systematic histofile?'):
    renameHistos(outputpath,outputpath[:-4]+'_syst.root',allsystnames,False)
lll=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[9:],bdts,errorSystnames)
exit(0)
plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[9:]),samples[9:],lolT[0],samples[0],-1,name+'/'+name+'_Blinded',[[lll,3354,ROOT.kBlack,True]],False,labels,True,True)

#listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,bdts,1)
#listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samplesdata,bdts,1)
#lll=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[9:],bdts,errorSystnames)
#plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[9:]),samples[9:],lolT[0],samples[0],-1,name+'/'+name+'_Unblinded',[[lll,3354,ROOT.kBlack,True]],False,labels,True,False)


#exit(0)
makeDatacards(name+'/'+name+'_limitInput.root',name+'/'+name+'_datacard',binlabels,True,"finaldiscr")
makeDatacards(name+'/'+name+'_limitInput.root',name+'/'+name+'_datacard',additbinlables,True,"inputVar")

# calculate limits
#if askYesNo('Calculate limits?'):
  #limit=calcLimits(name+'/'+name+'_datacard',binlabels)
  #limit.dump()
