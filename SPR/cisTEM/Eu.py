#!/usr/bin/env python3

import sys
import os
import linecache
import commands

filename=sys.argv[1:5]
print ("file input: "),
print (filename)
#should in order of class1 2 3 4

class1=open(filename[0][:-1]+"class1", 'w')
class2=open(filename[1][:-1]+"class2", 'w')
class3=open(filename[2][:-1]+"class3", 'w')
class4=open(filename[3][:-1]+"class4", 'w')


def getocc(filename,line):
    return (linecache.getline(filename, line).strip().split(' ')[10])

def output(outfile,infile,line):
    outfile.write("%s"%(linecache.getline(infile, line)))


num_line=commands.getstatusoutput("cat %s | wc -l"%(sys.argv[1]))[1]
print ("total lines: "),
print (num_line)
for i in range(1,int(num_line)+1):
    occ = []

    for j in filename:
        occ.append(getocc(j, i))

    best_occ = occ.index(max(occ))
#    print (best_occ)
    if best_occ == 0:
        output(class1,filename[0], i)
    elif best_occ == 1:
        output(class2,filename[1], i)
    elif best_occ == 2:
        output(class3,filename[2], i)
    elif best_occ == 3:
        output(class4,filename[3], i)


