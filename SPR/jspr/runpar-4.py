#!/usr/bin/env python
import os,sys,time,subprocess
from subprocess import Popen
file=open(sys.argv[2].split('=')[1],'r')
a=file.readlines()
file.close()
if len(a) <= 80:
        os.system('runpar-eman proc=32 '+sys.argv[2])
if len(a) > 80:
        part1=open('runpar-list1','w')
        part2=open('runpar-list2','w')
        part3=open('runpar-list3','w')
        part4=open('runpar-list4','w')
        n=int(len(a)/80)
        yu=len(a)-80*n
        for j in range(0,n):
                for i in range(0+80*j,32+80*j):
                        print >>part1,a[i].split('\n')[0]
                for i in range(32+80*j,48+80*j):
                        print >>part2,a[i].split('\n')[0]
                for i in range(48+80*j,64+80*j):
                        print >>part3,a[i].split('\n')[0]
                for i in range(64+80*j,80+80*j):
                        print >>part4,a[i].split('\n')[0]
        if yu <> 0 :
                for i in range(80*n,len(a)):
                        print >>part1,a[i].split('\n')[0]
        part1.close()
        part2.close()
        part3.close()
        part4.close()
        run1=subprocess.Popen(["runpar-eman","proc=32","file=runpar-list1"])
        run2=subprocess.Popen(["ssh","em","'/home/em/tmp1.sh'"])
        run3=subprocess.Popen(["ssh","em2","'/home/em/tmp1.sh'"])
        run4=subprocess.Popen(["ssh","em4","'/home/em/tmp1.sh'"])
        run1.wait()
        run2.wait()
        run3.wait()
        run4.wait()
os.system('rm runpar-list*')
exit()
