# cd limits_R$1_40vars_4j_ttHFupLFdown
cd limits_$2_08262020_$1

rm cmb/workspace.root
combineTool.py -M T2W -i cmb/* -o workspace.root --parallel 4

combine -M Significance cmb/workspace.root -t -1 --expectSignal=1 --cminDefaultMinimizerStrategy 0 &> sig.txt
combine -M AsymptoticLimits cmb/workspace.root --run=blind --cminDefaultMinimizerStrategy 0 &> asy.txt

cd ../