import optparse
import os,sys
import numpy as np
import math
import glob
import itertools
from EMAN2 import *

def Eman2Freali(az,alt,phi):
    t1=Transform({"type":"eman","az":az,"alt":alt,"phi":phi,"mirror":False})
    d = t1.get_params("eman")
#    print (d)
    psi = d["phi"]+90
    if psi > 360:
        psi -= 360
    theta = d["alt"]
    phi = d["az"] -90
    return psi,theta,phi

def Eman2Freali2(az,alt,phi):
    t1=Transform({"type":"eman","az":az,"alt":alt,"phi":phi,"mirror":False})
    d = t1.get_params("spider")
#    print (d)
    phi = d["phi"]
    theta = d["theta"]
    psi = d["psi"]
    return psi,theta,phi


def Freali2Eman(psi,theta,phi):
    t1=Transform({"type":"spider","psi":psi,"theta":theta,"phi":phi,"mirror":False})
    d = t1.get_params("eman")
#    print (d)
    az = d["az"]
    alt = d["alt"]
    phi = d["phi"]
    return az,alt,phi


f = open('good3k','r')
for i in f.readlines():
    cao = i.split(" ")
    num = int(cao[0])
    psiin = float(cao[1])
    thetain = float(cao[2])
    phiin = float(cao[3])
    x= float(cao[4])
    y= float(cao[5])
    huan = Freali2Eman(psiin,thetain,phiin)
    s="0\t../goodparticles/Good_%s.hdf\teuler=%s,%s,%s\tcenter=%s,%s"%(num-1,huan[0],huan[1],huan[2],192-x,192-y)
    print(s)
