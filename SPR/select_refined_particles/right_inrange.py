import os

line = 0
ls = os.popen('ls ./box/*.box').readlines()

print ('micrographs\tused_by_refine\tparticle_in_boxfie\tsame?')
for i in open('tmp5'):
    if i.split('\t')[0] == i.split('\t')[1][:-1]:
        print (ls[line][:-1]+'\t'+i[:-1]+'\tsame')
    elif i.split('\t')[0] == '0':
        print (ls[line][:-1]+'\t'+i[:-1]+'\tunuse')
    else:
        print (ls[line][:-1]+'\t'+i[:-1]+'\twrong!!!!!!')
    line += 1
