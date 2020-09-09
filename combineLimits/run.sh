cd limits_R$1_40vars_4j_4to9p_ttHFupLFdown
# cd limits_R$1_40vars_4j_ttHFupLFdown

# rm cmb/690/workspace.root
# combineTool.py -M T2W -i cmb/* -o workspace.root --parallel 4

# combine -M FitDiagnostics cmb/690/workspace.root -t -1 --expectSignal 0 --name AsimovBonly --cminDefaultMinimizerStrategy 0
# combine -M FitDiagnostics cmb/690/workspace.root -t -1 --expectSignal 1 --name AsimovSB --cminDefaultMinimizerStrategy 0
# combine -M FitDiagnostics cmb/690/workspace.root --expectSignal 0 --name Data --cminDefaultMinimizerStrategy 0
python ../diffNuisances.py --abs --all -g PlotAsimovBonly.root fitDiagnosticsAsimovBonly.root --sortBy correlation
python ../diffNuisances.py --abs --all -g PlotAsimovSB.root fitDiagnosticsAsimovSB.root --sortBy correlation
python ../diffNuisances.py --abs --all -g PlotData.root fitDiagnosticsData.root --sortBy correlation

cd ../

# cd limits_R$1_40vars_4j_4to9p_ttHFupLFdown

# python ../diffNuisances.py --abs --all -g PlotData.root fitDiagnosticsData.root --sortBy correlation

# cd ../