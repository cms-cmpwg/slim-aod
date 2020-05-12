# Instructions for running:

These scripts are used for checking what event content in AOD is needed for a workflow. It takes a config file and an input file and generates condor jobs (on lxplus) to check whether the config will crash if a collection is dropped on input. Here is an example that uses CMSSW_10_6_12.

# Step 1

python submitJobs.py -t myTest -s step5_PAT.py -i /eos/cms/store/mc/RunIISummer19UL18RECO/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/AODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/70000/01131E1D-6292-B746-BA60-5D490F310A14.root

The input file also needs to be specified inside the config file (-s option). The scripts are configured for a file on the CERN eos but can be modified by the user.

# Step 2

After the jobs complete, run the analyzeResults.py script:

python analyzeResults.py -t myTest -i /eos/cms/store/mc/RunIISummer19UL18RECO/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/AODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/70000/01131E1D-6292-B746-BA60-5D490F310A14.root

This will check for fatal exepctions in the log files, and print a set of inputCommands. 

# Step 3

The user should take the inputCommands from Step 2 and add them to the slimAOD.py script (also modifying the input file) and run it. Then check when using that as the input to the original script, that there are no new warnings or errors.
