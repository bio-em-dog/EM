#usage: 
#for i in `ls *.box`; do python remove_out_range.py $i ;done
#out put in folder ''inrange_box
from sys import argv
import os

script,boxfile = argv
if os.path.exists('./inrange_box'):
    'do nothing'
else:
    os.makedirs('./inrange_box')

infile = open (boxfile,'r')
outfile = open ('./inrange_box'+'/'+boxfile.split('/')[-1],'w')

ori_box = 0
out_box = 0

for i in open(boxfile):
    ori_box+=1
    line=infile.readline()
    xy = line.split('\t')
    if int(xy[1])< (3838-256) and int(xy[1])>0 and int(xy[0]) > 0 and int(xy[0]) < (3710-256):
        outfile.write("%s\t%s\t256\t256\n" % (xy[0],xy[1]))
        out_box+=1

print "%r/%r boxs selected from %s out put to ./inrange_box" % (out_box,ori_box,boxfile)