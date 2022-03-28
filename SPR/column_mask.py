# 20220301 JXD
# create a column mask
# mask=1, empty=0
# need eman2

import EMAN2,math,sys

def main():
    if len(sys.argv) == 3:
        column_mask(int(sys.argv[1]),int(sys.argv[2]),0)
    elif len(sys.argv) == 4:
        column_mask(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
    else:
        print("python3 column_mask.py <boxsize> <R> (<r=inner ridus>)")
        exit(0)    

def column_mask(boxsize, R, r):
    mask=EMAN2.EMData(boxsize,boxsize,boxsize)
    for z in range(boxsize):
        for y in range(boxsize):
            for x in range(boxsize):
                if r <= math.hypot(x-boxsize/2,y-boxsize/2) <= R:
                    mask[x,y,z]=1
                else:
                    mask[x,y,z]=0
    mask.write_image("columnmask_R%s_r%s.mrc"%(R,r))


if __name__ == "__main__":
    main()