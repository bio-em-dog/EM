import os


def count(path):
    c=0
    f=0
    for i in os.listdir(path):
        if i.split('.')[-1] == 'tif' or i.split('.')[-1] == 'tiff':
            c+=1
        if os.path.isdir(os.path.join(path,i)):
            f+=1
    return c,f

allimg=0

def lsall(path):
    global allimg
    global allsub
    layer=0
    allimg += count(path)[0]
    for i in os.listdir(path):
        abspath = os.path.join(path, i)
        if os.path.isdir(abspath):
            lsall(abspath)
            layer += 1
        elif os.path.isfile(abspath) and os.path.splitext(abspath)[1] == '.tif':
            ''
    return layer,allimg
path1 = 'C:\\Users\\Jia\\Documents\\tiff\\'

print(lsall(path1))
print (count(path1))

sss='1622'
print (os.path.abspath('C:\\Users\\Jia\\Documents\\tiff\\')+sss)


def checkall(path,out):
    for i in os.listdir(path):
        abspath = os.path.join(path, i)
        outpath = os.path.join(out, i)
        if os.path.exists(outpath):
            return 1
        if os.path.isdir(abspath):
            checkall(abspath,outpath)
    return 0

a=checkall('C:\\Users\\Jia\\Documents\\tiff','C:\\Users\\Jia\\Documents\\aaa')
print (a)