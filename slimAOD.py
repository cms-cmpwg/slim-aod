import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")


process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.MessageLogger.cerr.FwkReport.reportEvery = 10

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

process.source = cms.Source("PoolSource", 
    fileNames = cms.untracked.vstring('file:file:/eos/cms/store/mc/RunIISummer19UL18RECO/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/AODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/70000/01131E1D-6292-B746-BA60-5D490F310A14.root'),
    inputCommands=cms.untracked.vstring(
'drop *',
'keep LHEEventProduct_externalLHEProducer__GEN',
'keep int_addPileupInfo_bunchSpacing_DIGI2RAW',
'keep int_mixData_bunchSpacing_DIGI2RAW',
'keep PileupSummaryInfos_mixData__DIGI2RAW',
'keep ints_genParticles__DIGI2RAW',
'keep recoGenJets_ak4GenJetsNoNu__DIGI2RAW',
'keep recoGenParticles_genParticles__DIGI2RAW',
'keep edmTriggerResults_TriggerResults__HLT',
'keep ClusterSummary_clusterSummaryProducer__RECO',
'keep HcalNoiseSummary_hcalnoise__RECO',
'keep double_fixedGridRhoAll__RECO',
'keep double_fixedGridRhoFastjetAll__RECO',
'keep double_fixedGridRhoFastjetAllTmp__RECO',
'keep double_fixedGridRhoFastjetCentralNeutral__RECO',
'keep recoDeDxHitInfosedmAssociation_dedxHitInfo__RECO',
'keep recoTracksToOnerecoTracksAssociation_tevMuons_dyt_RECO',
'keep recoTracksToOnerecoTracksAssociation_tevMuons_firstHit_RECO',
'keep recoTracksToOnerecoTracksAssociation_tevMuons_picky_RECO',
'keep recoPFTausedmRefProdrecoPFTauTransverseImpactParametersrecoPFTauTransverseImpactParameterrecoPFTauTransverseImpactParametersTorecoPFTauTransverseImpactParameteredmrefhelperFindUsingAdvanceedmRefsAssociationVector_hpsPFTauTransverseImpactParameters__RECO',
'keep recoJetedmRefToBaseProdrecoTracksrecoTrackrecoTracksTorecoTrackedmrefhelperFindUsingAdvanceedmRefVectorsAssociationVector_ak4JetTracksAssociatorAtVertexPF__RECO',
'keep recoJetedmRefToBaseProdTofloatsAssociationVector_pfCombinedCvsBJetTags__RECO',
'keep recoJetedmRefToBaseProdTofloatsAssociationVector_pfCombinedCvsLJetTags__RECO',
'keep recoJetedmRefToBaseProdTofloatsAssociationVector_pfCombinedInclusiveSecondaryVertexV2BJetTags__RECO',
'keep recoJetedmRefToBaseProdTofloatsAssociationVector_pfCombinedMVAV2BJetTags__RECO',
'keep recoJetedmRefToBaseProdTofloatsAssociationVector_pfCombinedSecondaryVertexV2BJetTags__RECO',
'keep recoJetedmRefToBaseProdTofloatsAssociationVector_pfJetBProbabilityBJetTags__RECO',
'keep recoJetedmRefToBaseProdTofloatsAssociationVector_pfJetProbabilityBJetTags__RECO',
'keep recoJetedmRefToBaseProdTofloatsAssociationVector_pfSimpleInclusiveSecondaryVertexHighEffBJetTags__RECO',
'keep recoJetedmRefToBaseProdTofloatsAssociationVector_pfSimpleSecondaryVertexHighEffBJetTags__RECO',
'keep recoJetedmRefToBaseProdTofloatsAssociationVector_pfTrackCountingHighEffBJetTags__RECO',
'keep recoJetedmRefToBaseProdTofloatsAssociationVector_softPFElectronBJetTags__RECO',
'keep recoJetedmRefToBaseProdTofloatsAssociationVector_softPFMuonBJetTags__RECO',
'keep recoJetedmRefToBaseProdTofloatsAssociationVector_pfDeepCSVJetTags_probb_RECO',
'keep recoJetedmRefToBaseProdTofloatsAssociationVector_pfDeepCSVJetTags_probbb_RECO',
'keep recoJetedmRefToBaseProdTofloatsAssociationVector_pfDeepCSVJetTags_probc_RECO',
'keep recoJetedmRefToBaseProdTofloatsAssociationVector_pfDeepCSVJetTags_probudsg_RECO',
'keep CTPPSDiamondDigiedmDetSetVector_ctppsDiamondRawToDigi_TimingDiamond_RECO',
'keep CTPPSDiamondLocalTrackedmDetSetVector_ctppsDiamondLocalTracks__RECO',
'keep CTPPSDiamondRecHitedmDetSetVector_ctppsDiamondRecHits__RECO',
'keep CTPPSPixelClusteredmDetSetVector_ctppsPixelClusters__RECO',
'keep CTPPSPixelDigiedmDetSetVector_ctppsPixelDigis__RECO',
'keep CTPPSPixelLocalTrackedmDetSetVector_ctppsPixelLocalTracks__RECO',
'keep CTPPSPixelRecHitedmDetSetVector_ctppsPixelRecHits__RECO',
'keep TotemRPClusteredmDetSetVector_totemRPClusterProducer__RECO',
'keep TotemRPDigiedmDetSetVector_totemRPRawToDigi_TrackingStrip_RECO',
'keep TotemRPLocalTrackedmDetSetVector_totemRPLocalTrackFitter__RECO',
'keep TotemRPRecHitedmDetSetVector_totemRPRecHitProducer__RECO',
'keep TotemRPUVPatternedmDetSetVector_totemRPUVPatternFinder__RECO',
'keep CSCDetIdCSCSegmentsOwnedRangeMap_cscSegments__RECO',
'keep DTChamberIdDTRecSegment4DsOwnedRangeMap_dt4DCosmicSegments__RECO',
'keep DTChamberIdDTRecSegment4DsOwnedRangeMap_dt4DSegments__RECO',
'keep GEMDetIdGEMRecHitsOwnedRangeMap_gemRecHits__RECO',
'keep RPCDetIdRPCRecHitsOwnedRangeMap_rpcRecHits__RECO',
'keep EcalRecHitsSorted_reducedEcalRecHitsEB__RECO',
'keep EcalRecHitsSorted_reducedEcalRecHitsEE__RECO',
'keep EcalRecHitsSorted_reducedEcalRecHitsES__RECO',
'keep HBHERecHitsSorted_reducedHcalRecHits_hbhereco_RECO',
'keep booledmValueMap_chargedHadronPFTrackIsolation__RECO',
'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_muCorrData_RECO',
'keep recoPFCandidatesrecoPFCandidaterecoPFCandidatesrecoPFCandidateedmrefhelperFindUsingAdvanceedmRefsedmValueMap_particleBasedIsolation_gedGsfElectrons_RECO',
'keep recoPFCandidatesrecoPFCandidaterecoPFCandidatesrecoPFCandidateedmrefhelperFindUsingAdvanceedmRefsedmValueMap_particleBasedIsolation_gedPhotons_RECO',
'keep recoBeamHaloSummary_BeamHaloSummary__RECO',
'keep recoBeamSpot_offlineBeamSpot__RECO',
'keep recoCSCHaloData_CSCHaloData__RECO',
'keep recoGlobalHaloData_GlobalHaloData__RECO',
'keep recoPFTauDiscriminator_hpsPFTauChargedIsoPtSum__RECO',
'keep recoPFTauDiscriminator_hpsPFTauChargedIsoPtSumdR03__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByDecayModeFinding__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByDecayModeFindingNewDMs__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLTraw__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLTraw__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLTraw__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3Hits__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBdR03oldDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBnewDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBoldDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWdR03oldDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWnewDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWoldDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByLooseMuonRejection3__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByMVA6LooseElectronRejection__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByMVA6MediumElectronRejection__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByMVA6TightElectronRejection__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByMVA6VLooseElectronRejection__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByMVA6VTightElectronRejection__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByMVA6rawElectronRejection__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3Hits__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBdR03oldDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBnewDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBoldDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWdR03oldDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWnewDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWoldDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3Hits__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBdR03oldDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBnewDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBoldDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWdR03oldDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWnewDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWoldDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByTightMuonRejection3__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBdR03oldDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBnewDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBoldDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWdR03oldDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWnewDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWoldDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBdR03oldDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBnewDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBoldDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWdR03oldDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWnewDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWoldDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByVVLooseIsolationMVArun2v1DBdR03oldDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByVVLooseIsolationMVArun2v1DBnewDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByVVLooseIsolationMVArun2v1DBoldDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBdR03oldDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBnewDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBoldDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWdR03oldDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWnewDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWoldDMwLT__RECO',
'keep recoPFTauDiscriminator_hpsPFTauFootprintCorrection__RECO',
'keep recoPFTauDiscriminator_hpsPFTauFootprintCorrectiondR03__RECO',
'keep recoPFTauDiscriminator_hpsPFTauNeutralIsoPtSum__RECO',
'keep recoPFTauDiscriminator_hpsPFTauNeutralIsoPtSumWeight__RECO',
'keep recoPFTauDiscriminator_hpsPFTauNeutralIsoPtSumWeightdR03__RECO',
'keep recoPFTauDiscriminator_hpsPFTauNeutralIsoPtSumdR03__RECO',
'keep recoPFTauDiscriminator_hpsPFTauPUcorrPtSum__RECO',
'keep recoPFTauDiscriminator_hpsPFTauPhotonPtSumOutsideSignalCone__RECO',
'keep recoPFTauDiscriminator_hpsPFTauPhotonPtSumOutsideSignalConedR03__RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw_category_RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw_category_RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw_category_RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLTraw_category_RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLTraw_category_RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLTraw_category_RECO',
'keep recoPFTauDiscriminator_hpsPFTauDiscriminationByMVA6rawElectronRejection_category_RECO',
'keep edmErrorSummaryEntrys_logErrorHarvester__RECO',
'keep recoPFCandidateedmFwdPtrs_particleFlowPtrs__RECO',
'keep recoPFCandidateedmFwdPtrs_particleFlowTmpPtrs__RECO',
'keep recoCaloClusters_particleFlowEGamma_EBEEClusters_RECO',
'keep recoCaloClusters_particleFlowEGamma_ESClusters_RECO',
'keep recoCaloClusters_hybridSuperClusters_hybridBarrelBasicClusters_RECO',
'keep recoCaloClusters_multi5x5SuperClusters_multi5x5EndcapBasicClusters_RECO',
'keep recoCaloClusters_particleFlowSuperClusterECAL_particleFlowBasicClusterECALBarrel_RECO',
'keep recoCaloClusters_particleFlowSuperClusterECAL_particleFlowBasicClusterECALEndcap_RECO',
'keep recoCaloClusters_particleFlowSuperClusterECAL_particleFlowBasicClusterECALPreshower_RECO',
'keep recoCaloClusters_particleFlowSuperClusterOOTECAL_particleFlowBasicClusterOOTECALBarrel_RECO',
'keep recoCaloClusters_particleFlowSuperClusterOOTECAL_particleFlowBasicClusterOOTECALEndcap_RECO',
'keep recoCaloClusters_particleFlowSuperClusterOOTECAL_particleFlowBasicClusterOOTECALPreshower_RECO',
'keep recoCaloClusters_hybridSuperClusters_uncleanOnlyHybridBarrelBasicClusters_RECO',
'keep recoCaloJets_ak4CaloJets__RECO',
'keep recoCaloMETs_caloMet__RECO',
'keep recoCaloMETs_caloMetM__RECO',
'keep recoConversions_allConversions__RECO',
'keep recoConversions_conversions__RECO',
'keep recoConversions_particleFlowEGamma__RECO',
'keep recoDeDxHitInfos_dedxHitInfo__RECO',
'keep recoGsfElectrons_gedGsfElectrons__RECO',
'keep recoGsfElectronCores_gedGsfElectronCores__RECO',
'keep recoGsfTracks_electronGsfTracks__RECO',
'keep recoMuons_muons__RECO',
'keep recoMuons_muonsFromCosmics__RECO',
'keep recoMuons_muonsFromCosmics1Leg__RECO',
'keep recoPFCandidates_particleFlow__RECO',
'keep recoPFJets_ak4PFJets__RECO',
'keep recoPFJets_ak4PFJetsCHS__RECO',
'keep recoPFJets_ak8PFJetsCHS__RECO',
'keep recoPFMETs_pfMet__RECO',
'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_RECO',
'keep recoPFTaus_hpsPFTauProducer__RECO',
'keep recoPFTauTransverseImpactParameters_hpsPFTauTransverseImpactParameters_PFTauTIP_RECO',
'keep recoPhotons_gedPhotons__RECO',
'keep recoPhotons_ootPhotons__RECO',
'keep recoPhotons_photons__RECO',
'keep recoPhotonCores_gedPhotonCore__RECO',
'keep recoPhotonCores_ootPhotonCore__RECO',
'keep recoPhotonCores_photonCore__RECO',
'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_RECO',
'keep recoSuperClusters_correctedHybridSuperClusters__RECO',
'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower__RECO',
'keep recoSuperClusters_particleFlowEGamma__RECO',
'keep recoSuperClusters_particleFlowSuperClusterECAL_particleFlowSuperClusterECALBarrel_RECO',
'keep recoSuperClusters_particleFlowSuperClusterECAL_particleFlowSuperClusterECALEndcapWithPreshower_RECO',
'keep recoSuperClusters_particleFlowSuperClusterOOTECAL_particleFlowSuperClusterOOTECALBarrel_RECO',
'keep recoSuperClusters_particleFlowSuperClusterOOTECAL_particleFlowSuperClusterOOTECALEndcapWithPreshower_RECO',
'keep recoTracks_ckfInOutTracksFromConversions__RECO',
'keep recoTracks_ckfOutInTracksFromConversions__RECO',
'keep recoTracks_conversionStepTracks__RECO',
'keep recoTracks_cosmicMuons__RECO',
'keep recoTracks_cosmicMuons1Leg__RECO',
'keep recoTracks_generalTracks__RECO',
'keep recoTracks_globalMuons__RECO',
'keep recoTracks_standAloneMuons__RECO',
'keep recoTracks_standAloneMuons_UpdatedAtVtx_RECO',
'keep recoTracks_tevMuons_dyt_RECO',
'keep recoTracks_tevMuons_firstHit_RECO',
'keep recoTracks_tevMuons_picky_RECO',
'keep recoTrackExtrapolations_trackExtrapolator__RECO',
'keep recoVertexs_inclusiveSecondaryVertices__RECO',
'keep recoVertexs_offlinePrimaryVertices__RECO',
'keep recoVertexs_offlinePrimaryVerticesWithBS__RECO',
'keep recoVertexCompositeCandidates_generalV0Candidates_Kshort_RECO',
'keep recoVertexCompositeCandidates_generalV0Candidates_Lambda_RECO',
'keep recoVertexCompositePtrCandidates_inclusiveCandidateSecondaryVertices__RECO',
'keep recoVertexCompositePtrCandidates_inclusiveCandidateSecondaryVerticesCvsL__RECO',
'keep triggerTriggerEvent_hltTriggerSummaryAOD__HLT',
    ),
 dropDescendantsOfDroppedBranches=cms.untracked.bool(False)
)


process.output = cms.OutputModule("PoolOutputModule",
       fileName = cms.untracked.string('slimAOD.root')
)


process.e1 = cms.EndPath(process.output)
