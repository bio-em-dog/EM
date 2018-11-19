#!/bin/env python
###	tomohunter.py MFS 02/2006


#N tomohunter.py
#F tomography hunter

import os
import sys
import string
import commands
import math
import EMAN
#import Numeric
from math import *
from sys import argv


def tomoccf(targetMRC,probeMRC,norm):
	ccf=targetMRC.calcCCF(probeMRC)
	ccf.toCorner()
	if norm==1:
		ccf.normalize()
	return (ccf)

def updateCCF(bestCCF,bestALT,bestAZ,bestPHI,altrot,azrot,phirot,currentCCF,box,scalar,searchx,searchy,searchz):
	box2=box/2
	bestValue=-1.e10
	xbest=-10
	ybest=-10
	zbest=-10
	currentValue=currentCCF.Max()
	currentLoc=currentCCF.MaxLoc()
	x=currentLoc[0]-box2
	y=currentLoc[1]-box2
	z=currentLoc[2]-box2
	if (abs(x)<=searchx and abs(y)<=searchy and abs(z)<=searchz):
		currentValue=currentValue/scalar
		if currentValue > bestValue:
			bestValue = currentValue
			xbest=x
			ybest=y
			zbest=z
			#print x,y,z, currentValue
	inlist=0
	while inlist < 10:
		if  bestValue > bestCCF.valueAt(inlist,1,1):
			swlist=9
			while swlist >inlist:
				#print swlist
				bestCCF.setValueAt(swlist,1,1,bestCCF.valueAt(swlist-1,1,1))
				bestALT.setValueAt(swlist,1,1,bestALT.valueAt(swlist-1,1,1))
				bestAZ.setValueAt(swlist,1,1,bestAZ.valueAt(swlist-1,1,1))
				bestPHI.setValueAt(swlist,1,1,bestPHI.valueAt(swlist-1,1,1))
				bestX.setValueAt(swlist,1,1,bestX.valueAt(swlist-1,1,1))
				bestY.setValueAt(swlist,1,1,bestY.valueAt(swlist-1,1,1))
				bestZ.setValueAt(swlist,1,1,bestZ.valueAt(swlist-1,1,1))
				swlist=swlist-1
			bestCCF.setValueAt(inlist,1,1,bestValue)
			bestALT.setValueAt(inlist,1,1,altrot*180/3.14159)
			bestAZ.setValueAt(inlist,1,1,azrot*180/3.14159)
			bestPHI.setValueAt(inlist,1,1,phirot*180/3.14159)
			bestX.setValueAt(inlist,1,1,xbest)
			bestY.setValueAt(inlist,1,1,ybest)
			bestZ.setValueAt(inlist,1,1,zbest)
			break
		inlist=inlist+1
	#print "one"
	bestCCF.update()
	#print "two"
	bestALT.update()
	bestAZ.update()
	bestPHI.update()
	return(bestCCF)
	
def ccfFFT(currentCCF, thresh, box):
	tempCCF = currentCCF.copy()
	tempCOMPLEX=tempCCF.doFFT()
	tempCOMPLEX.gimmeFFT() # supposed to give me "ownership". whatever...
	tempCOMPLEX.ri2ap()
	tempCOMPLEX.realFilter(2,thresh)
	mapSum=tempCOMPLEX.Mean()*box*box*box/2.
	#print mapSum
	return(mapSum)

def peakSearch(bestCCF,Max_location,width,box):
	xmin=Max_location[0]-width
	xmax=Max_location[0]+width
	ymin=Max_location[1]-width
	ymax=Max_location[1]+width
	zmin=Max_location[2]-width
	zmax=Max_location[2]+width
	for x in (range(xmin,xmax)):
		for y in (range(ymin,ymax)):
			for z in (range(zmin,zmax)):
				print x,y,z
				bestCCF.setValueAt(x,y,z,-10000)
	bestCCF.update()
	return(bestCCF)		

if (len(argv)<3) :
	print "Usage:\ntomohunter.py <target mrc file> <probe mrc file> \n"
	print "Options: da=<search step (default=30)>, thresh=<threshold (default=0), maxpeaks=<number of results returned in log file (default=20)>, width=<peak width (default=2)>"
	sys.exit()
	
target=argv[1]
probe=argv[2]
thresh=0
da=60
maxPeaks=10
width=2
norm=0
searchx=3
searchy=3
searchz=3
for a in argv[3:] :
        s=a.split('=')
	if (s[0]=='dal'):
		dal=float(s[1])
	elif (s[0]=='daz'):
		daz=float(s[1])
	elif (s[0]=='dap'):
		dap=float(s[1])
	elif (s[0]=='thresh'):
		thresh=float(s[1])
	elif (s[0]=='ral'):
		ral=float(s[1])
#	elif (s[0]=='raz'):
#		raz=float(s[1])
	elif (s[0]=='rap'):
		rap=float(s[1])
	elif (s[0]=='norm'):
		norm=int(s[1])
	elif (s[0]=='searchx'):
		searchx=int(s[1])
	elif (s[0]=='searchy'):
		searchy=int(s[1])
	elif (s[0]=='searchz'):
		searchz=int(s[1])
        else:
                print("Unknown argument "+a)
                exit(1)

print target, probe

targetMRC=EMAN.EMData()
targetMRC.readImage(argv[1],-1)
targetMean=targetMRC.Mean()
targetSigma=targetMRC.Sigma()
print "Target Information"
print "   mean:       %f"%(targetMean)
print "   sigma:      %f"%(targetSigma)

target_xsize=targetMRC.xSize()
target_ysize=targetMRC.ySize()
target_zsize=targetMRC.zSize()
if (target_xsize!=target_ysize!=target_zsize) or (target_xsize%2==1):
	print "The density map must be even and cubic. Terminating."
	sys.exit()
box=target_xsize

probeMRC=EMAN.EMData()
probeMRC.readImage(argv[2],-1)
probeMean=probeMRC.Mean()
probeSigma=probeMRC.Sigma()
print "Probe Information"
print "   mean:       %f"%(probeMean)
print "   sigma:      %f"%(probeSigma)


bestCCF=EMAN.EMData()
bestCCF.setSize(box,box,box)
bestCCF.zero()

bestAZ=EMAN.EMData()
bestAZ.setSize(box,box,box)
bestAZ.zero()

bestALT=EMAN.EMData()
bestALT.setSize(box,box,box)
bestALT.zero()

bestPHI=EMAN.EMData()
bestPHI.setSize(box,box,box)
bestPHI.zero()

bestX=EMAN.EMData()
bestX.setSize(box,box,box)
bestX.zero()

bestY=EMAN.EMData()
bestY.setSize(box,box,box)
bestY.zero()

bestZ=EMAN.EMData()
bestZ.setSize(box,box,box)
bestZ.zero()


altarray=[]
alt=0
while alt <= ral:
	altarray.append(alt*3.14159/180)
	alt=alt+dal

azarray=[]
az=-180
while az < 180:
	azarray.append(az*3.14159/180)
	az=az+daz

#phiarray=[]
#phi=-180
#while phi < 180:
#	phiarray.append(phi*3.14159/180)
#	phi=phi+da
# I had to change this because the phi range varies depending on the azimuth (it is nearly the negative of it, within
# a range, when alt is near zero, which it will be at this point)
rarad=rap*3.14159/180.
darad=dap*3.14159/180.
maxfrac=0.
for altrot in altarray:
	print "Trying rotation %f"%(altrot*180./3.14159)
	if (altrot==0.):
		azrot=0.
		phirot=-azrot-rarad
		minnum=10000000
		maxnum=0
		#print "Trying rotation %f %f"%(altrot, azrot)
		while phirot <= -azrot+rarad:
			dMRC=EMAN.EMData()
			dMRC = probeMRC.copy()
			dMRC.setRAlign(altrot,azrot,phirot)
			dMRC.setTAlign(0,0,0)
			dMRC.rotateAndTranslate()	
			#print "Trying rotation %f %f %f"%(altrot, azrot, phirot)
			currentCCF=tomoccf(targetMRC,dMRC,norm)
			scalar=ccfFFT(currentCCF,thresh,box)
			if scalar>maxnum:
				maxnum=int(scalar)
			if scalar<minnum:
				minnum=int(scalar)
			scalar=scalar/(box*box*box/2.)
			#scalar=1
			#scaledCCF=currentCCF/scalar
			#print "three"
			bestCCF=updateCCF(bestCCF,bestALT,bestAZ,bestPHI,altrot,azrot,phirot,currentCCF,box,scalar,searchx,searchy,searchz)
			phirot=phirot+darad
		#print minnum,maxnum, float(maxnum)/float(minnum)
	else:
		for azrot in azarray:
			phirot=-azrot-rarad
			#print "Trying rotation %f %f"%(altrot, azrot)
			while phirot <= -azrot+rarad:
				dMRC=EMAN.EMData()
				dMRC = probeMRC.copy()
				dMRC.setRAlign(altrot,azrot,phirot)
				dMRC.setTAlign(0,0,0)
				dMRC.rotateAndTranslate()	
				#print "Trying rotation %f %f %f"%(altrot, azrot, phirot)
				currentCCF=tomoccf(targetMRC,dMRC,norm)
				scalar=ccfFFT(currentCCF,thresh,box)
				if scalar>maxnum:
					maxnum=int(scalar)
				if scalar<minnum:
					minnum=int(scalar)
				scalar=scalar/(box*box*box/2.)
				#scalar=1
				#scaledCCF=currentCCF/scalar
				#print "three"
				bestCCF=updateCCF(bestCCF,bestALT,bestAZ,bestPHI,altrot,azrot,phirot,currentCCF,box,scalar,searchx,searchy,searchz)
				phirot=phirot+darad
			#print minnum,maxnum, float(maxnum)/float(minnum)
print minnum,maxnum, float(maxnum)/float(minnum)
#outCCF="rl-%s"%(argv[1])
#outalt="alt-%s"%(argv[1])
#outaz="az-%s"%(argv[1])
#outphi="phi-%s"%(argv[1])

#bestCCF.writeImage(outCCF)
#bestALT.writeImage(outalt)
#bestAZ.writeImage(outaz)
#bestPHI.writeImage(outphi)

out=open("log-s4-%s%s.txt"%(argv[1],argv[2]),"w")
peak=0
while peak < 10:
	#Max_location=bestCCF.MinLoc()
	ALT=str(bestALT.valueAt(peak,1,1))
	AZ=str(bestAZ.valueAt(peak,1,1))
	PHI=str(bestPHI.valueAt(peak,1,1))
	COEFF=str(bestCCF.valueAt(peak,1,1))
	LOC=str( ( (bestX.valueAt(peak,1,1)),(bestY.valueAt(peak,1,1)),(bestZ.valueAt(peak,1,1) ) ) )
	line="Peak %d rot=( %s, %s, %s ) trans= %s coeff= %s\n"%(peak,ALT,AZ,PHI,LOC,COEFF)
	out.write(line)
	#bestCCF=peakSearch(bestCCF,Max_location, width, box)
	peak=peak+1
out.close()

