import sys

f = open(sys.argv[1],'r')

# [776, 964, 92, "tm", 16.222087860107422, 0],

for i in f.readlines():
    x = int(i.split(',')[0].split('[')[1])
    y = int(i.split(',')[1])
    z = int(i.split(',')[2])
    print("[%s, %s, %s,%s"%(x*1.5,y*1.5,z*1.5,",".join(i.split(',')[3:]))),
