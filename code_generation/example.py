from scriptgenerator import *
import sys
sys.path.insert(0,'../')
from plotutils import *

sample=Sample('ttbar',2,'~/HEP/data/ttbar_miniaodv2.root','')

plots=[Plot(ROOT.TH1F("avg_dr_tagged_jets","avg_dr_tagged_jets",19,0.0,4.75),"BDT_v3_input_avg_dr_tagged_jets",""),
       Plot(ROOT.TH1F("sphericity","sphericity",18,0.0,0.9),"BDT_v3_input_sphericity",""),
       Plot(ROOT.TH1F("Jet_Pt","Jet_Pt",50,0,500),"Jet_Pt",""),
       Plot(ROOT.TH1F("test","test",50,0,500),"BoostedJet_Pt[0]*Jet_Pt/Jet_Eta+Jet_Phi[1]+Jet_Pt[2]",""),
       ]

createScript("testplot",plots,sample)
compileScript("testplot")
