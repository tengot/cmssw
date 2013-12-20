import FWCore.ParameterSet.Config as cms

PdwgLeptonRecoSkim = cms.EDFilter('LeptonRecoSkim',
  HltLabel = cms.InputTag("TriggerResults","","HLT"),
  electronCollection      = cms.InputTag("gedGsfElectrons"),
  pfElectronCollection    = cms.InputTag("particleFlow"),
  muonCollection          = cms.InputTag("muons"),
  caloJetCollection       = cms.InputTag("ak5CaloJetsL2L3"),
  PFJetCollection         = cms.InputTag("ak5PFJetsL2L3"),
  ecalBarrelRecHitsCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
  ecalEndcapRecHitsCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
  UseElectronSelection    = cms.bool(False),
  UsePfElectronSelection  = cms.bool(False),
  UseMuonSelection        = cms.bool(False),
  UseHtSelection          = cms.bool(False),
  UsePFHtSelection          = cms.bool(False),
  UseJetSelection         = cms.bool(False),                              
  FilterName              = cms.string("None"),
  electronPtMin           = cms.double(0),
  electronN               = cms.int32(0),
  pfElectronPtMin         = cms.double(0),
  pfElectronN             = cms.int32(0),
  globalMuonPtMin         = cms.double(0),
  trackerMuonPtMin        = cms.double(0),
  muonN                   = cms.int32(0),
  HtMin                   = cms.double(0),
  PFHtMin                   = cms.double(0),
  HtJetThreshold          = cms.double(0),
  PFHtJetThreshold          = cms.double(0),
  jetN                    = cms.int32(0),
  jetPtMin                = cms.double(0)
)
