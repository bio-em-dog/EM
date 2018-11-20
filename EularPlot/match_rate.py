#!/usr/bin/env python3

import sys
import os
import linecache
import commands

#i shorter
#j longer

def smart_int(data):
    if len(str(data))!=0:
	return int(data)
    else:
	sys.exit(0)

def count_line(filename):
    z=1
    for i in open(filename,'r').readlines():
	z+=1
    return z

if count_line(sys.argv[1]) <= count_line(sys.argv[2]):
    shorter=sys.argv[1]
    longer=sys.argv[2]
elif count_line(sys.argv[1]) > count_line(sys.argv[2]):
    shorter=sys.argv[2]
    longer=sys.argv[1]


j=1
match=[]
for i in open(longer,'r').readlines():
    linej=smart_int(linecache.getline(shorter, j).strip().split(' ')[0])
    linei=smart_int(i.strip().split(' ')[0])

    while linei > linej:
    	j+=1
        linej=smart_int(linecache.getline(shorter, j).strip().split(' ')[0].strip())

    if linei == linej:
        #print ("%s\t%s"%(linei, linej))
        match.append('rrr')
	j+=1

print (match)
print (len(match))
