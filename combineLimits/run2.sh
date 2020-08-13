# python dataCard.py 2017
# python dataCard.py 2018
# source run.sh 2017
# source run.sh 2018
combine -M MultiDimFit cmb/690/workspace.root  --expectSignal 0 --name mdf --cminDefaultMinimizerStrategy 0 --redefineSignalPOIs n4Jet --freezeParameters r --setParameters r=0 --algo=singles --cl=0.68 | grep n4Jet
combine -M MultiDimFit cmb/690/workspace.root  --expectSignal 0 --name mdf --cminDefaultMinimizerStrategy 0 --redefineSignalPOIs n5Jet --freezeParameters r --setParameters r=0 --algo=singles --cl=0.68 | grep n5Jet
combine -M MultiDimFit cmb/690/workspace.root  --expectSignal 0 --name mdf --cminDefaultMinimizerStrategy 0 --redefineSignalPOIs n6Jet --freezeParameters r --setParameters r=0 --algo=singles --cl=0.68 | grep n6Jet
combine -M MultiDimFit cmb/690/workspace.root  --expectSignal 0 --name mdf --cminDefaultMinimizerStrategy 0 --redefineSignalPOIs n7Jet --freezeParameters r --setParameters r=0 --algo=singles --cl=0.68 | grep n7Jet
combine -M MultiDimFit cmb/690/workspace.root  --expectSignal 0 --name mdf --cminDefaultMinimizerStrategy 0 --redefineSignalPOIs n8Jet --freezeParameters r --setParameters r=0 --algo=singles --cl=0.68 | grep n8Jet
combine -M MultiDimFit cmb/690/workspace.root  --expectSignal 0 --name mdf --cminDefaultMinimizerStrategy 0 --redefineSignalPOIs n9pJet --freezeParameters r --setParameters r=0 --algo=singles --cl=0.68 | grep n9pJet