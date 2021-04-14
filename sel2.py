import ROOT,os,sys

originbase='/mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2017_Oct2019_4t_03062021_step2/'
destbase='/mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2017_Oct2019_4t_03062021_step2p5/'

syst=sys.argv[1]+'/'
files=os.listdir(originbase+syst)

for f in files:
	print f
	ff=ROOT.TFile(originbase+syst+f)
	tree=ff.Get('ljmet')
	newfile = ROOT.TFile(destbase+syst+f, "recreate");
	newtree = tree.CopyTree("(NJetsCSV_MultiLepCalc >= 2)")
	newtree.Write()


# rooteventselector -s "(NJetsCSVwithSF_JetSubCalc >= 2)" /mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2017_Oct2019_4t_03092021_step2/nominal/SingleMuon_hadd.root:ljmet;99 /mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2017_Oct2019_4t_03092021_step2p5/nominal/SingleMuon_hadd.root