import os,sys,datetime,itertools

thisDir = os.getcwd()
outputDir = thisDir+'/'

isTTbarCR = 1 # 1:TTBar, 0:Wjets

isEMlist =['E','M']
if isTTbarCR: 
	nttaglist = ['0','1p'] #if '0p', the cut will not be applied
	nWtaglist = ['0','1p']
	nbtaglist = ['1','2p']
else: 
	nttaglist = ['0','1p'] #if '0p', the cut will not be applied
	nWtaglist = ['0','1p']
	nbtaglist = ['0','1p']

cTime=datetime.datetime.now()
datestr='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
timestr='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)
if isTTbarCR: pfix='ttbar'
else: pfix='wjets'
pfix+='_x53x53'
pfix+='_'+datestr+'_'+timestr

outDir = outputDir+pfix
if not os.path.exists(outDir): os.system('mkdir '+outDir)
os.chdir(outDir)

for cat in list(itertools.product(isEMlist,nttaglist,nWtaglist,nbtaglist)):
	catDir = cat[0]+'_nT'+cat[1]+'_nW'+cat[2]+'_nB'+cat[3]
	print catDir
	if not os.path.exists(outDir+'/'+catDir): os.system('mkdir '+catDir)
	os.chdir(catDir)			
	
	dict={'dir':outputDir,'isTTbarCR':isTTbarCR,'isEM':cat[0],'nttag':cat[1],'nWtag':cat[2],'nbtag':cat[3]}
	
	jdf=open('condor.job','w')
	jdf.write(
"""universe = vanilla
Executable = %(dir)s/doCondorCRs.sh
Should_Transfer_Files = YES
WhenToTransferOutput = ON_EXIT
notify_user = joseph_van_der_list@brown.edu

arguments      = ""

Output = condor.out
Error = condor.err
Log = condor.log
Notification = Error
Arguments = %(dir)s %(isTTbarCR)s %(isEM)s %(nttag)s %(nWtag)s %(nbtag)s

Queue 1"""%dict)
	jdf.close()

	os.system('condor_submit condor.job')
	os.chdir('..')


                  