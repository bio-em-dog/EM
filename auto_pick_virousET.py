#!/usr/bin/env python3

import sys
import os
import commands
import math

filelist=["et_"+str(i)+".box" for i in range(40,81)]
print filelist

def distance(x1,x2,y1,y2):
    return (int(math.sqrt((x1-x2)**2+(y1-y2)**2)))

def getxy(filename):
    #num_line=commands.getstatusoutput("cat %s | wc -l" % (filename))[1]
#    num_line=0
    xy=[]
    z=filelist.index(filename)+1
    f=open(filename,'r')
    for i in f.readlines():
        line=i.strip().split('\t')
        xy.append([int(line[0]),int(line[1]),z])
#        num_line+=1
    return xy	

#ini position list
position=[]
for i in getxy(filelist[0]):
    position.append([i[0],i[1],i])


for k in filelist[1:]:
    for i in getxy(k):
        x1=i[0]
        y1=i[1]
        for j in range(len(position)):
            x2=position[j][0]
            y2=position[j][1]
#            print (distance(x1,x2,y1,y2))
            if distance(x1,x2,y1,y2) > 10 :
                position.append([x1,y1,i])
            elif distance(x1,x2,y1,y2) <=10 :
                position[j].append(i)
                position[j][0]=0.5*abs(x1-x2)
                position[j][1]=0.5*abs(y1-y2)

kkk=open('jieguo','w')
kkk.write(position)