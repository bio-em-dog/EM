#rotate volume to 60 symm positon

from numpy import *
from math import *

anglist=open('anglist','r').readlines()
file2=open('micrographlst','r').readlines()
x1=['']*len(anglist)
y1=['']*len(anglist)
z1=['']*len(anglist)
for i in range(0,len(anglist)):
    x1[i]=float(anglist[i].split(' ')[0])
    y1[i]=float(anglist[i].split(' ')[1])
    z1[i]=float(anglist[i].split(' ')[2].split('\n')[0])

for i in range(0,len(file2)):
    file2i=file2[i].split('\t')
    particle=file2i[0]
    name=file2i[1].split('.')[0]
    al=float(file2i[2].split(',')[0].split('=')[1])*3.14159265/180
    phi=float(file2i[2].split(',')[1])*3.14159265/180
    az=float(file2i[2].split(',')[2])*3.14159265/180
    trans1=float(file2i[3].split(',')[0].split('=')[1])
    trans2=float(file2i[3].split(',')[1].split('\n')[0])
    euler_phi=mat([[cos (phi),sin (phi), 0], [-sin (phi),cos (phi),0],[0,0,1]])
    euler_al=mat([[1,0,0],[0, cos (al), sin (al)],[0, -sin (al), cos (al)]])
#    euler_al=mat([[cos (al),0,-sin (al)],[0,1,0],[sin (al), 0, cos (al)]])
    euler_az=mat([[cos (az),sin (az), 0],[-sin (az),cos (az),0],[0,0,1]])

    print 'proc2d '+name+'.hdf '+name+'-'+particle+'.mrc first='+particle+' last='+particle
    for j in range(0,len(anglist)):
	spike=mat([[x1[j]],
	           [y1[j]],
	           [z1[j]]])
	out=array(euler_az*euler_al*euler_phi*spike)
#	out=array(euler_phi*euler_al*euler_az*spike)
	x=int(float(out[0])+trans1)
	y=int(float(out[1])+trans2)
	z=int(float(out[2])+256.5)
	
	if float(out[0])**2+float(out[1])**2 > 25600:
	    print 'clip resize -ox 80 -oy 80 -oz 1 -cz 1 -cx '+str(x)+' -cy '+str(y)+' '+name+'-'+particle+'.mrc '+name+'-'+particle+'-pt'+str(j)+'.mrc'
	    print 'proc2d '+name+'-'+particle+'-pt'+str(j)+'.mrc '+name+'.img edgnorm'
    print 'rm '+name+'-*.mrc'
