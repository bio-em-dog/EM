#!/usr/bin/env python
import os,time
k=0
while k == 0:
        os.system('ls *.mrcs > filelist')
        os.system("ls /mnt/raidx/20180303-gyz/data/*.mrcs|cut -d'/' -f 6 > filelist1")
        lst1=open('filelist','r').readlines()
        lst2=open('filelist1','r').readlines()
        if len(lst2) > 2:
                for i in range(0,len(lst2)-1):
                        if lst2[i] not in lst1:
                                print('mv /mnt/raidx/20180303-gyz/data/'+lst2[i].split('\n')[0]+' .')
                                os.system('mv /mnt/raidx/20180303-gyz/data/'+lst2[i].split('\n')[0]+' .')
        time.sleep(5)
