# import ROOT in batch mode
import sys
oldargv = sys.argv[:]
sys.argv = [ '-b-' ]
import ROOT
ROOT.gROOT.SetBatch(True)
sys.argv = oldargv

# load FWLite C++ libraries
ROOT.gSystem.Load("libFWCoreFWLite.so")
ROOT.gSystem.Load("libDataFormatsFWLite.so")
ROOT.AutoLibraryLoader.enable()

# load FWlite python libraries
from DataFormats.FWLite import Handle, Events

muons, muonLabel = Handle("std::vector<pat::Muon>"), "slimmedMuons"
electrons, electronLabel = Handle("std::vector<pat::Electron>"), "slimmedElectrons"
photons, photonLabel = Handle("std::vector<pat::Photon>"), "slimmedPhotons"
taus, tauLabel = Handle("std::vector<pat::Tau>"), "slimmedTaus"
jets, jetLabel = Handle("std::vector<pat::Jet>"), "slimmedJets"
fatjets, fatjetLabel = Handle("std::vector<pat::Jet>"), "slimmedJetsAK8"
mets, metLabel = Handle("std::vector<pat::MET>"), "slimmedMETs"
vertices, vertexLabel = Handle("std::vector<reco::Vertex>"), "offlineSlimmedPrimaryVertices"
verticesScore = Handle("edm::ValueMap<float>")

# open file (you can use 'edmFileUtil -d /store/whatever.root' to get the physical file name)
events = Events('file:/pnfs/desy.de/cms/tier2/store/user/hmildner/ttHTobb_M125_13TeV_powheg_pythia8/Boostedv2MiniAOD/151017_154254/0000/BoostedTTH_MiniAOD_1.root')

for iev,event in enumerate(events):
    if iev >= 10: break 
    event.getByLabel(muonLabel, muons)
    event.getByLabel(electronLabel, electrons)
    event.getByLabel(photonLabel, photons)
    event.getByLabel(tauLabel, taus)
    event.getByLabel(jetLabel, jets)
    event.getByLabel(fatjetLabel, fatjets)
    event.getByLabel(metLabel, mets)
    event.getByLabel(vertexLabel, vertices)
    event.getByLabel(vertexLabel, verticesScore)
    print "\nEvent %d: run %6d, lumi %4d, event %12d" % (iev,event.eventAuxiliary().run(), event.eventAuxiliary().luminosityBlock(),event.eventAuxiliary().event())
    # Vertices 
    if len(vertices.product()) == 0 or vertices.product()[0].ndof() < 4:
        print "Event has no good primary vertex."
        continue
    else:
        PV = vertices.product()[0]
        print "PV at x,y,z = %+5.3f, %+5.3f, %+6.3f, ndof: %.1f, score: (pt2 of clustered objects) %.1f" % (PV.x(), PV.y(), PV.z(), PV.ndof(),verticesScore.product().get(0))

    # Muons
    for i,mu in enumerate(muons.product()): 
        if mu.pt() < 5 or not mu.isLooseMuon(): continue
        print "muon %2d: pt %4.1f, dz(PV) %+5.3f, POG loose id %d, tight id %d." % (
            i, mu.pt(), mu.muonBestTrack().dz(PV.position()), mu.isLooseMuon(), mu.isTightMuon(PV))

    # Electrons
    for i,el in enumerate(electrons.product()):
        if el.pt() < 5: continue
        print "elec %2d: pt %4.1f, supercluster eta %+5.3f, sigmaIetaIeta %.3f (%.3f with full5x5 shower shapes), lost hits %d, pass conv veto %d" % (
                    i, el.pt(), el.superCluster().eta(), el.sigmaIetaIeta(), el.full5x5_sigmaIetaIeta(),el.gsfTrack().hitPattern().numberOfLostHits(ROOT.reco.HitPattern.MISSING_INNER_HITS), el.passConversionVeto())

    # Photon
    for i,pho in enumerate(photons.product()):
        if pho.pt() < 20 or pho.chargedHadronIso()/pho.pt() > 0.3: continue
        print "phot %2d: pt %4.1f, supercluster eta %+5.3f, sigmaIetaIeta %.3f (%.3f with full5x5 shower shapes)" % (
                    i, pho.pt(), pho.superCluster().eta(), pho.sigmaIetaIeta(), pho.full5x5_sigmaIetaIeta())

    # Tau
    for i,tau in enumerate(taus.product()):
        if tau.pt() < 20: continue
        print "tau  %2d: pt %4.1f, dxy signif %.1f, ID(byMediumCombinedIsolationDeltaBetaCorr3Hits) %.1f, lead candidate pt %.1f, pdgId %d " % (
                    i, tau.pt(), tau.dxy_Sig(), tau.tauID("byMediumCombinedIsolationDeltaBetaCorr3Hits"), tau.leadCand().pt(), tau.leadCand().pdgId()) 


    # Jets (standard AK4)
    for i,j in enumerate(jets.product()):
        if j.pt() < 20: continue
        print "jet %3d: pt %5.1f (raw pt %5.1f, matched-calojet pt %5.1f), eta %+4.2f, btag run1(CSV) ) %.3f, run2(pfCSVIVFV2) %.3f, pileup mva disc %+.2f" % (
            i, j.pt(), j.pt()*j.jecFactor('Uncorrected'), j.userFloat("caloJetMap:pt"), j.eta(), max(0,j.bDiscriminator("combinedSecondaryVertexBJetTags")), max(0,j.bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")), j.userFloat("pileupJetId:fullDiscriminant"))
        if i == 0: # for the first jet, let's print the leading constituents
            constituents = [ j.daughter(i2) for i2 in xrange(j.numberOfDaughters()) ]
            constituents.sort(key = lambda c:c.pt(), reverse=True)
            for i2, cand in enumerate(constituents):
                if i2 > 4: 
                        print "         ....."
                        break
                print "         constituent %3d: pt %6.2f, dz(pv) %+.3f, pdgId %+3d" % (i2,cand.pt(),cand.dz(PV.position()),cand.pdgId()) 

    # Fat AK8 Jets
    for i,j in enumerate(fatjets.product()):
        print "jetAK8 %3d: pt %5.1f (raw pt %5.1f), eta %+4.2f, mass %5.1f ungroomed, %5.1f softdrop, %5.1f pruned, %5.1f trimmed, %5.1f filtered. CMS TopTagger %.1f" % (
            i, j.pt(), j.pt()*j.jecFactor('Uncorrected'), j.eta(), j.mass(), j.userFloat('ak8PFJetsCHSSoftDropMass'), j.userFloat('ak8PFJetsCHSPrunedMass'), j.userFloat('ak8PFJetsCHSTrimmedMass'), j.userFloat('ak8PFJetsCHSFilteredMass'), j.userFloat("cmsTopTagPFJetsCHSMassAK8"))


        # To get the constituents of the AK8 jets, you have to loop over all of the
        # daughters recursively. To save space, the first two constituents are actually
        # the Soft Drop SUBJETS, which will then point to their daughters.
        # The remaining constituents are those constituents removed by soft drop but
        # still in the AK8 jet.
        constituents = []
        for ida in xrange( j.numberOfDaughters() ) :
            cand = j.daughter(ida)
            if cand.numberOfDaughters() == 0 :
                constituents.append( cand )
            else :
                for jda in xrange( cand.numberOfDaughters() ) :
                    cand2 = cand.daughter(jda)
                    constituents.append( cand2 )
        constituents.sort(key = lambda c:c.pt(), reverse=True)
        for i2, cand in enumerate(constituents):
            if i2 > 4: 
                        print "         ....."
                        break
            print "         constituent %3d: pt %6.2f, pdgId %+3d, #dau %+3d" % (i2,cand.pt(),cand.pdgId(), cand.numberOfDaughters()) 
                    
        wSubjets = j.subjets('SoftDrop')        
        for iw,wsub in enumerate( wSubjets ) :
            print "   w subjet %3d: pt %5.1f (raw pt %5.1f), eta %+4.2f, mass %5.1f " % (
                iw, wsub.pt(), wsub.pt()*wsub.jecFactor('Uncorrected'), wsub.eta(), wsub.mass()
                )
        tSubjets = j.subjets('CMSTopTag')
        for it,tsub in enumerate( tSubjets ) :
            print "   t subjet %3d: pt %5.1f (raw pt %5.1f), eta %+4.2f, mass %5.1f " % (
                it, tsub.pt(), tsub.pt()*tsub.jecFactor('Uncorrected'), tsub.eta(), tsub.mass()
                )


