import sys

if sys.argv[1]==[]:
    print ("usage: match.py filename")
    exit(0)

f=open(sys.argv[1])
k=open('12.lst','r')
count=[i for i in range(2) ]

for i in f.readlines():
    ser1=int(i.split('@')[0])
    file2=k.readline()
    ser2=int(file2.split()[0])
#    print("%s,%s"%(ser1,ser2))
    while ser1 > ser2 :
        file2=k.readline()
        ser2=int(file2.split()[0])
    if ser1==ser2:
        x=int(file2.split()[5].split("=")[1].split(",")[0])
        y=int(file2.split()[5].split("=")[1].split(",")[1])
        dis=((x-300)**2+(y-300)**2)**0.5
        print(dis)


print count
norm=max(count)
for j in count:
    ll=int(((j+0.1)/norm)*20)
    s="%s\t%s"%('='*ll,j)
    print s
