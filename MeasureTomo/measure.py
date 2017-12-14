#!usr/bin/env python

from EMAN2 import *
import os, sys, math


img=EMData(sys.argv[1])

#outfile = open ('./inrange_box'+'/'+boxfile.split('/')[-1],'w')

zmax=img["nz"]
ymax=img["ny"]
xmax=img["nx"]

#slice pos 25
z1=zmax/2-sys.argv[2]
z2=zmax/2+sys.argv[2]

#line pos 28
x1=xmax/2-sys.argv[2]
x2=xmax/2+sys.argv[2]

for y in range(1,ymax):
##    delt=abs(img[x,y,z]-img[x,(y-1),z])
    total=img[x1,y,z1]+img[x1,y,z2]+img[x2,y,z1]+img[x2,y,z2]
##   outfile.write(('%r\t%r') % (img[x,y,z],delt))
##    print (('%r\t%r') % (img[x,y,z],delt))
    print (total)

#for y in range(1,ymax-1):
#    previous=img[x1,y-1,z1]+img[x1,y-1,z2]+img[x2,y-1,z1]+img[x2,y-1,z2]
#    now=img[x1,y,z1]+img[x1,y,z2]+img[x2,y,z1]+img[x2,y,z2]
#    nextone=img[x1,y+1,z1]+img[x1,y+1,z2]+img[x2,y+1,z1]+img[x2,y+1,z2]
#    print ((previous+now+nextone)/3)