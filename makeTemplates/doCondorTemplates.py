#!/usr/bin/python

import os,sys,datetime,itertools
parent = os.path.dirname(os.getcwd())
sys.path.append(parent)
from utils import *

thisDir = os.getcwd()
outputDir = thisDir+'/'

year=sys.argv[1]
region='SR' #PS,SR,TTCR,WJCR
categorize=1 #1==categorize into t/W/b/j, 0==only split into flavor

cTime=datetime.datetime.now()
date='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
time='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)
if region=='TTCR': pfix='ttbar'
elif region=='WJCR': pfix='wjets'
else: pfix='templates'
if not categorize: pfix='kinematics_'+region
pfix+='_'+year+'_'+sys.argv[3]#+date#+'_'+time

iPlotList = [#distribution name as defined in "doHists.py"
# sys.argv[2],
#'HT',
# 'HTb',
# 'maxJJJpt',
# 'ST',
# 'minMlb',
# 
# 'lepPt',
# 'lepEta',
# 'deltaRjet1',
# 'deltaRjet2',
# 'deltaRjet3',
# 'JetEta',
# 'JetPt',
# 'Jet1Pt',
# 'Jet2Pt',
# 'Jet3Pt',
# 'Jet4Pt',
# 'Jet5Pt',
# 'Jet6Pt',
# 'MET',
# 'NJets',
# 'NDCSVBJets',
# 'NBJets',
# 'NBJetsNoSF',
# 'NDCSVBJetsNoSF',
# 'mindeltaR',
# 'PtRel',
# 'MTlmet',
# 'minMlj',
# 'lepIso',
# 'Bjet1Pt',
# 'METphi',
# 'lepPhi',
# 'JetPhi',
# 'NresolvedTops1p',
# 'NresolvedTops2p',
# 'NresolvedTops5p',
# 'NresolvedTops10p',
# 'HOTtPt',
# 'HOTtEta',
# 'HOTtPhi',
# 'HOTtMass',
# 'HOTtDisc',
# 'HOTtDRmax',
# 'HOTtDThetaMax',
# 'HOTtDThetaMin',
# 'topMass',
# 'topPt',

# 'NWJets',
# 'NTJets',
# 'NJetsAK8',
# 'JetPtAK8',
# 'JetEtaAK8',
# 'JetPhiAK8',
# 'deltaRAK8',
# 'Tau21',
# 'Tau21Nm1',
# 'Tau32',
# 'Tau32Nm1',
# 'SoftDropMass', 
# 'SoftDropMassNm1W',
# 'SoftDropMassNm1t',
# 'Tau1',
# 'Tau2',
# 'Tau3',
# 'NBJets',
# 'NBJetsNoSF',
# 'NDCSVBJetsNoSF',
# 'Wjet1Pt',
# 'Tjet1Pt',

# 'HT_vs_HTb',
# 'HT_vs_maxJJJpt',
# 'HTb_vs_maxJJJpt',
'BDT',
#BDTvars
# 'AK4HT',
# 'AK4HTpMETpLepPt',
# 'minMleppBjet',
# 'leptonPt_MultiLepCalc',
# 'corr_met_MultiLepCalc',
# 'NJets_JetSubCalc',
# 'NJetsCSVwithSF_MultiLepCalc',
# 'NJetsTtagged',
# 'MT_lepMet',
# 'BDTtrijet2',
# 'thirdcsvb_bb',
# 'fourthcsvb_bb',
# 'fifthJetPt',
# 'BDTtrijet3',
# 'sixthJetPt',
# 'BDTtrijet1',
# 'MT2bb',
# 'mass_maxJJJpt',
# 'hemiout',
# 'Aplanarity',
# 'centrality',
# 'HT_bjets',
# 'FW_momentum_1',
# 'mass_lepBJet0',
# 'mass_lepBJet_mindr',
# 'deltaR_lepBJet_maxpt',
# 'Sphericity',
# 'deltaR_lepbJetInMinMlb',
# 'minDR_lepBJet',
# 'mass_maxBBmass',
# 'deltaR_minBB',
# 'aveBBdr',
# 'ratio_HTdHT4leadjets',
# 'aveCSVpt',
# 'mass_lepJets0',
# 'mass_minBBdr',
# 'mass_minLLdr',
# 'theJetLeadPt',
# 'FW_momentum_5',
# 'deltaR_lepJetInMinMljet',
# 'secondJetPt',
# 'BJetLeadPt',
# 'csvJet4',
# 'lepDR_minBBdr',
# 'deltaEta_maxBB',
# 'FW_momentum_0',
# 'FW_momentum_2',
# 'FW_momentum_3',
# 'FW_momentum_4',
# 'FW_momentum_6',
# 'mass_lepJets1',
# 'mass_lepJets2',
# 'PtFifthJet',
# 'deltaPhi_lepJetInMinMljet',
# 'deltaPhi_lepbJetInMinMlb',
# 'M_allJet_W',
# 'csvJet3',
# 'HT_2m',
# 'BDTtrijet4',
# 'NresolvedTops1pFake',
# 'NJetsWtagged',
# 'HOTGoodTrijet1_mass',
# 'HOTGoodTrijet1_dijetmass',
# 'HOTGoodTrijet1_pTratio',
# 'HOTGoodTrijet1_dRtridijet',
# 'HOTGoodTrijet1_dRtrijetJetnotdijet',
# 'HOTGoodTrijet1_csvJetnotdijet',
# 'HOTGoodTrijet2_mass',
# 'HOTGoodTrijet2_dijetmass',
# 'HOTGoodTrijet2_pTratio',
# 'HOTGoodTrijet2_dRtridijet',
# 'HOTGoodTrijet2_dRtrijetJetnotdijet',
# 'HOTGoodTrijet2_csvJetnotdijet',

#'thirdcsvb_bb_BTagBHad',
#'thirdcsvb_bb_BTagNBHad',
#'thirdcsvb_bb_NBTagBHad',
#'thirdcsvb_bb_NBTagNBHad',


]

# isEMlist  = ['E','M']
# nhottlist = ['0','1p']
# nttaglist = ['0p']
# nWtaglist = ['0p']
# nbtaglist = ['2','3','4p']
# njetslist = ['6','7','8','9','10p']

#4p
isEMlist1  = ['E','M']
nhottlist1 = ['0p']
nttaglist1 = ['0p']
nWtaglist1 = ['0p']
nbtaglist1 = ['2p']
njetslist1 = ['4p']

#456p
isEMlist2  = ['E','M']
nhottlist2 = ['0p']
nttaglist2 = ['0p']
nWtaglist2 = ['0p']
nbtaglist2 = ['2p']
njetslist2 = ['4','5','6p']

#btag
isEMlist3  = ['E','M']
nhottlist3 = ['0p']
nttaglist3 = ['0p']
nWtaglist3 = ['0p']
nbtaglist3 = ['2','3','4p']
njetslist3 = ['4p']

if not categorize: 	
	nhottlist = ['0p']
	nttaglist = ['0p']
	nWtaglist = ['0p']
	nbtaglist = ['2p']
	njetslist = ['4p']
catList1 = list(itertools.product(isEMlist1,nhottlist1,nttaglist1,nWtaglist1,nbtaglist1,njetslist1))
catList2 = list(itertools.product(isEMlist2,nhottlist2,nttaglist2,nWtaglist2,nbtaglist2,njetslist2))
catList3 = list(itertools.product(isEMlist3,nhottlist3,nttaglist3,nWtaglist3,nbtaglist3,njetslist3))
catList = catList1 + catList2 + catList3
# print catList
# sys.exit( 0 )

outDir = outputDir+pfix
if not os.path.exists(outDir): os.system('mkdir '+outDir)
if year=='R17': 
	os.system('cp ../weights17.py ../weights.py')
	os.system('cp ../samples17.py ../samples.py')
elif year=='R18': 
	os.system('cp ../weights18.py ../weights.py')
	os.system('cp ../samples18.py ../samples.py')
os.system('cp ../analyze.py ../weights.py ../samples.py ../utils.py doHists.py doCondorTemplates.py doCondorTemplates.sh '+outDir+'/')
os.chdir(outDir)

count=0
for iplot in iPlotList:
	for cat in catList:
		if skip(cat): continue #check the "skip" function in utils module to see if you want to remove specific categories there!!!
		catDir = cat[0]+'_nHOT'+cat[1]+'_nT'+cat[2]+'_nW'+cat[3]+'_nB'+cat[4]+'_nJ'+cat[5]
		print "iPlot: "+iplot+", cat: "+catDir
		if not os.path.exists(outDir+'/'+catDir): os.system('mkdir '+catDir)
		os.chdir(catDir)
	
		dict={'dir':outDir,'iPlot':iplot,'region':region,'isCategorized':categorize,'year':year,
			  'isEM':cat[0],'nhott':cat[1],'nttag':cat[2],'nWtag':cat[3],'nbtag':cat[4],'njets':cat[5],'step1dir':sys.argv[4],
			  'exeDir':thisDir}
	
		jdf=open('condor_'+iplot+'.job','w')
		jdf.write(
"""universe = vanilla
Executable = %(dir)s/doCondorTemplates.sh
Should_Transfer_Files = YES
WhenToTransferOutput = ON_EXIT
request_memory = 3072
Output = condor_%(iPlot)s.out
Error = condor_%(iPlot)s.err
Log = condor_%(iPlot)s.log
Notification = Error
Arguments = %(dir)s %(iPlot)s %(region)s %(isCategorized)s %(year)s %(isEM)s %(nhott)s %(nttag)s %(nWtag)s %(nbtag)s %(njets)s %(step1dir)s
Queue 1"""%dict)
		jdf.close()

		os.system('condor_submit condor_'+iplot+'.job')
		os.chdir('..')
		count+=1

print "Total jobs submitted:", count
                  
                                                  