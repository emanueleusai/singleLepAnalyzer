#!/usr/bin/python

import sys

def printlim(spec,year,variable):

	inputDir='limits_'+year+'_'+spec+'_'+variable

	sigFile = inputDir+'/sig.txt'
	sigData = open(sigFile,'r').read()
	siglines = sigData.split('\n')
	limFile = inputDir+'/asy.txt'
	limData = open(limFile,'r').read()
	limlines = limData.split('\n')
	theSig = ''
	theLim = ['']*5
	for line in siglines:
		if line.startswith('Significance:'): theSig = line.split()[-1]
	for line in limlines:
		if line.startswith('Expected  2.5%:'): theLim[0] =  "{:.2f}".format(float(line.split()[-1])*12)
		if line.startswith('Expected 16.0%:'): theLim[1] = "{:.2f}".format(float(line.split()[-1])*12)
		if line.startswith('Expected 50.0%:'): theLim[2] = "{:.2f}".format(float(line.split()[-1])*12)
		if line.startswith('Expected 84.0%:'): theLim[3] = "{:.2f}".format(float(line.split()[-1])*12)
		if line.startswith('Expected 97.5%:'): theLim[4] = "{:.2f}".format(float(line.split()[-1])*12)
	print year+' , '+variable+' , '+spec+' , '+theSig+' , '+theLim[0]+' , '+theLim[1]+' , '+theLim[2]+' , '+theLim[3]+' , '+theLim[4]

print 'Year , Var , Specifications , Significance , -2sigma, -1sigma, central, +1sigma, +2sigma'
printlim('08262020_66vars_4j' , 'R17' , 'BDT')
printlim('08262020_66vars_6j' , 'R17' , 'BDT')
printlim('08262020_73vars_4j' , 'R17' , 'BDT')
printlim('08262020_73vars_6j' , 'R17' , 'BDT')
printlim('08262020_66vars_4j' , 'R18' , 'BDT')
printlim('08262020_66vars_6j' , 'R18' , 'BDT')
printlim('08262020_73vars_4j' , 'R18' , 'BDT')
printlim('08262020_73vars_6j' , 'R18' , 'BDT')



