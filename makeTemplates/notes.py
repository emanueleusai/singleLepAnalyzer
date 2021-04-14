python makeTemplates/doCondorTemplates.py R17 BDT 40vars_6j /mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2018_Oct2019_4t_05182020_step3_wenyu/BDT_SepRank6j73vars2017year40top_40vars_mDepth2_4j_year2018/


python doCondorTemplates.py R17 BDT StdBin_4p /mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2017_Oct2019_4t_08122020_step2/
python doCondorTemplates.py R18 BDT StdBin_4p /mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2018_Oct2019_4t_08122020_step2/

python doCondorTemplates.py R17 BDT StdBin_456p /mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2017_Oct2019_4t_08122020_step2/
python doCondorTemplates.py R18 BDT StdBin_456p /mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2018_Oct2019_4t_08122020_step2/

python doCondorTemplates.py R17 BDT StdBin_234pB /mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2017_Oct2019_4t_08122020_step2/
python doCondorTemplates.py R18 BDT StdBin_234pB /mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2018_Oct2019_4t_08122020_step2/



python doCondorTemplates.py R17 BDT FineBin10_4p /mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2017_Oct2019_4t_08122020_step2/
python doCondorTemplates.py R18 BDT FineBin10_4p /mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2018_Oct2019_4t_08122020_step2/

python doCondorTemplates.py R17 BDT FineBin10_456p /mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2017_Oct2019_4t_08122020_step2/
python doCondorTemplates.py R18 BDT FineBin10_456p /mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2018_Oct2019_4t_08122020_step2/

python doCondorTemplates.py R17 BDT FineBin10_234pB /mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2017_Oct2019_4t_08122020_step2/
python doCondorTemplates.py R18 BDT FineBin10_234pB /mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2018_Oct2019_4t_08122020_step2/



python doCondorTemplates.py R17 BDT New_StdBin_4p /mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2017_Oct2019_4t_10072020_step2/
python doCondorTemplates.py R17 BDT New_StdBin_456p /mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2017_Oct2019_4t_10072020_step2/
python doCondorTemplates.py R17 BDT New_StdBin_234pB /mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2017_Oct2019_4t_10072020_step2/

python doCondorTemplates.py R17 BDT New_FineBin10_4p /mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2017_Oct2019_4t_10072020_step2/
python doCondorTemplates.py R17 BDT New_FineBin10_456p /mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2017_Oct2019_4t_10072020_step2/
python doCondorTemplates.py R17 BDT New_FineBin10_234pB /mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2017_Oct2019_4t_10072020_step2/


old step2 
4p 
--Normal bin 17
--Normal bin 18
--Fine bin 17
--Fine bin 18

4,5,6p 
--Normal bin 17
--Normal bin 18
--Fine bin 17
--Fine bin 18

234p btag 
--Normal bin 17
--Normal bin 18
--Fine bin 17
--Fine bin 18

New step2
4p 
Normal bin 17
..Normal bin 18
Fine bin 17
..Fine bin 18

4,5,6p 
Normal bin 17
..Normal bin 18
Fine bin 17
..Fine bin 18

234p btag 
Normal bin 17
..Normal bin 18
Fine bin 17
..Fine bin 18

step2 2017 /mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2017_Oct2019_4t_10072020_step2/


MC statonly
MC allsys

Data Normal
Data poiss

-------------------

chi2 statonly
chi2 allsys

KS X MC.(data)
KS X data.(MC)

KS MC.(data) statonly
KS MC.(data) allsys

KS X MC.(data) statonly
KS X MC.(data) allsys

h1->SetBinErrorOption(TH1::kPoisson);

(KS  fine
KS coarse)

(chi2 rebin Normal
 chi2 rebin without empty data bin) 




