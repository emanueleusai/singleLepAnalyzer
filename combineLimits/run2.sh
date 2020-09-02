# python dataCard.py 2017
# python dataCard.py 2018
# source run.sh 2017
# source run.sh 2018
# combine -M MultiDimFit cmb/690/workspace.root  --expectSignal 0 --name mdf --cminDefaultMinimizerStrategy 0 --redefineSignalPOIs n4Jet --freezeParameters r --setParameters r=0 --algo=singles --cl=0.68 | grep n4Jet
# combine -M MultiDimFit cmb/690/workspace.root  --expectSignal 0 --name mdf --cminDefaultMinimizerStrategy 0 --redefineSignalPOIs n5Jet --freezeParameters r --setParameters r=0 --algo=singles --cl=0.68 | grep n5Jet
# combine -M MultiDimFit cmb/690/workspace.root  --expectSignal 0 --name mdf --cminDefaultMinimizerStrategy 0 --redefineSignalPOIs n6Jet --freezeParameters r --setParameters r=0 --algo=singles --cl=0.68 | grep n6Jet
# combine -M MultiDimFit cmb/690/workspace.root  --expectSignal 0 --name mdf --cminDefaultMinimizerStrategy 0 --redefineSignalPOIs n7Jet --freezeParameters r --setParameters r=0 --algo=singles --cl=0.68 | grep n7Jet
# combine -M MultiDimFit cmb/690/workspace.root  --expectSignal 0 --name mdf --cminDefaultMinimizerStrategy 0 --redefineSignalPOIs n8Jet --freezeParameters r --setParameters r=0 --algo=singles --cl=0.68 | grep n8Jet
# combine -M MultiDimFit cmb/690/workspace.root  --expectSignal 0 --name mdf --cminDefaultMinimizerStrategy 0 --redefineSignalPOIs n9pJet --freezeParameters r --setParameters r=0 --algo=singles --cl=0.68 | grep n9pJet

# combine -M GoodnessOfFit cmb/690/workspace.root  --expectSignal 0 --name gof --cminDefaultMinimizerStrategy 0 --algo=saturated --redefineSignalPOIs n4Jet --freezeParameters r --setParameters r=0 -v2 | grep "SimNLL created with"
# combine -M GoodnessOfFit cmb/690/workspace.root  --expectSignal 0 --name gof --cminDefaultMinimizerStrategy 0 --algo=saturated --redefineSignalPOIs n4Jet --freezeParameters r --setParameters r=0 | grep "Best fit test statistic"
# combine -M GoodnessOfFit cmb/690/workspace.root  --expectSignal 0 --name gof --cminDefaultMinimizerStrategy 0 --algo=saturated --redefineSignalPOIs n5Jet --freezeParameters r --setParameters r=0 | grep "Best fit test statistic"
# combine -M GoodnessOfFit cmb/690/workspace.root  --expectSignal 0 --name gof --cminDefaultMinimizerStrategy 0 --algo=saturated --redefineSignalPOIs n6Jet --freezeParameters r --setParameters r=0 | grep "Best fit test statistic"
# combine -M GoodnessOfFit cmb/690/workspace.root  --expectSignal 0 --name gof --cminDefaultMinimizerStrategy 0 --algo=saturated --redefineSignalPOIs n7Jet --freezeParameters r --setParameters r=0 | grep "Best fit test statistic"
# combine -M GoodnessOfFit cmb/690/workspace.root  --expectSignal 0 --name gof --cminDefaultMinimizerStrategy 0 --algo=saturated --redefineSignalPOIs n8Jet --freezeParameters r --setParameters r=0 | grep "Best fit test statistic"
# combine -M GoodnessOfFit cmb/690/workspace.root  --expectSignal 0 --name gof --cminDefaultMinimizerStrategy 0 --algo=saturated --redefineSignalPOIs n9pJet --freezeParameters r --setParameters r=0 | grep "Best fit test statistic"

# combine -M GoodnessOfFit cmb/690/workspace.root  --expectSignal 0 --name gof --cminDefaultMinimizerStrategy 0 --algo=saturated --redefineSignalPOIs n4Jet --freezeParameters r,n5Jet,n6Jet,n7Jet,n8Jet,n9pJet --setParameters r=0 -v2 | grep "SimNLL created with"
# combine -M GoodnessOfFit cmb/690/workspace.root  --expectSignal 0 --name gof --cminDefaultMinimizerStrategy 0 --algo=saturated --redefineSignalPOIs n4Jet --freezeParameters r,n5Jet,n6Jet,n7Jet,n8Jet,n9pJet --setParameters r=0 | grep "Best fit test statistic"
# combine -M GoodnessOfFit cmb/690/workspace.root  --expectSignal 0 --name gof --cminDefaultMinimizerStrategy 0 --algo=saturated --redefineSignalPOIs n5Jet --freezeParameters r,n4Jet,n6Jet,n7Jet,n8Jet,n9pJet --setParameters r=0 | grep "Best fit test statistic"
# combine -M GoodnessOfFit cmb/690/workspace.root  --expectSignal 0 --name gof --cminDefaultMinimizerStrategy 0 --algo=saturated --redefineSignalPOIs n6Jet --freezeParameters r,n4Jet,n5Jet,n7Jet,n8Jet,n9pJet --setParameters r=0 | grep "Best fit test statistic"
# combine -M GoodnessOfFit cmb/690/workspace.root  --expectSignal 0 --name gof --cminDefaultMinimizerStrategy 0 --algo=saturated --redefineSignalPOIs n7Jet --freezeParameters r,n4Jet,n5Jet,n6Jet,n8Jet,n9pJet --setParameters r=0 | grep "Best fit test statistic"
# combine -M GoodnessOfFit cmb/690/workspace.root  --expectSignal 0 --name gof --cminDefaultMinimizerStrategy 0 --algo=saturated --redefineSignalPOIs n8Jet --freezeParameters r,n4Jet,n5Jet,n6Jet,n7Jet,n9pJet --setParameters r=0 | grep "Best fit test statistic"
# combine -M GoodnessOfFit cmb/690/workspace.root  --expectSignal 0 --name gof --cminDefaultMinimizerStrategy 0 --algo=saturated --redefineSignalPOIs n9pJet --freezeParameters r,n4Jet,n5Jet,n6Jet,n7Jet,n8Jet --setParameters r=0 | grep "Best fit test statistic"

combine -M GoodnessOfFit cmb/690/workspace.root  --expectSignal 0 --name gof --cminDefaultMinimizerStrategy 0 --algo=saturated --redefineSignalPOIs n4Jet --freezeParameters r --setParameters r=0 -v2 | grep "SimNLL created with"
combine -M GoodnessOfFit cmb/690/workspace.root  --expectSignal 0 --name gof --cminDefaultMinimizerStrategy 0 --algo=saturated --redefineSignalPOIs n4Jet --freezeParameters r --setParameters r=0 | grep "Best fit test statistic"
combine -M GoodnessOfFit cmb/690/workspace.root  --expectSignal 0 --name gof --cminDefaultMinimizerStrategy 0 --algo=saturated --redefineSignalPOIs n5Jet --freezeParameters r --setParameters r=0 | grep "Best fit test statistic"
combine -M GoodnessOfFit cmb/690/workspace.root  --expectSignal 0 --name gof --cminDefaultMinimizerStrategy 0 --algo=saturated --redefineSignalPOIs n6pJet --freezeParameters r --setParameters r=0 | grep "Best fit test statistic"

combine -M GoodnessOfFit cmb/690/workspace.root  --expectSignal 0 --name gof --cminDefaultMinimizerStrategy 0 --algo=saturated --redefineSignalPOIs n4Jet --freezeParameters r,n5Jet,n6pJet --setParameters r=0 -v2 | grep "SimNLL created with"
combine -M GoodnessOfFit cmb/690/workspace.root  --expectSignal 0 --name gof --cminDefaultMinimizerStrategy 0 --algo=saturated --redefineSignalPOIs n4Jet --freezeParameters r,n5Jet,n6pJet --setParameters r=0 | grep "Best fit test statistic"
combine -M GoodnessOfFit cmb/690/workspace.root  --expectSignal 0 --name gof --cminDefaultMinimizerStrategy 0 --algo=saturated --redefineSignalPOIs n5Jet --freezeParameters r,n4Jet,n6pJet --setParameters r=0 | grep "Best fit test statistic"
combine -M GoodnessOfFit cmb/690/workspace.root  --expectSignal 0 --name gof --cminDefaultMinimizerStrategy 0 --algo=saturated --redefineSignalPOIs n6Jet --freezeParameters r,n4Jet,n5Jet --setParameters r=0 | grep "Best fit test statistic"