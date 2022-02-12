from numpy import *
from math import *

pos=[[150,150,33],
  [119,249,98],                                              
  [235,212,98],
  [47,151,98],
  [235,88,98],
  [119,53,98],
  [183,251,202],
  [65,212,202],
  [256,151,202],
  [65,88,202],
  [184,51,202],
  [150,150,267]]

'''
R=mat([
  [cos(psi)*cos(theta)*cos(phi)-sin(psi)*sin(theta), cos(psi)*cos(theta)*sin(phi)+sin(psi)*cos(theta), cos(psi)*sin(theta)*-1],
  [sin(psi)*cos(theta)*cos(phi)*-1-cos(psi)*sin(theta), sin(psi)*cos(theta)*sin(phi)*-1+cos(psi)*cos(theta), sin(psi)*sin(theta)],
  [sin(theta)*cos(phi), sin(theta)*sin(phi), cos(theta)]
  ])
'''
ang=open('angle','r')

for i in ang.readlines():
  x=float(i.split(" ")[0])
  y=float(i.split(" ")[1])
  name=i.split(" ")[2]
  phi=radians(float(i.split(" ")[3]))
  theta=radians(float(i.split(" ")[4]))
  psi=radians(float(i.split(" ")[5].split("\n")[0]))
  #print (x,y,name,phi,theta,psi)
  R=mat([
  [cos(psi)*cos(theta)*cos(phi)-sin(psi)*sin(theta), cos(psi)*cos(theta)*sin(phi)+sin(psi)*cos(theta), cos(psi)*sin(theta)*-1],
  [sin(psi)*cos(theta)*cos(phi)*-1-cos(psi)*sin(theta), sin(psi)*cos(theta)*sin(phi)*-1+cos(psi)*cos(theta), sin(psi)*sin(theta)],
  [sin(theta)*cos(phi), sin(theta)*sin(phi), cos(theta)]
  ])
  for k in range(12):
    newpos=((mat(pos[k])-150)*R.T).tolist()[0]
    #print((mat(pos[1])-150)*2)
    #print(newpos[0]+150,newpos[1]+150)
    s="%s %s 1 1\n"%(x+newpos[0]*2,y+newpos[1]*2)
    tmp=open(name,'a')
    tmp.write(s)
