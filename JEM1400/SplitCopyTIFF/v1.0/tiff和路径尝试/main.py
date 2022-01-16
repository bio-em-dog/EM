#1632 1092
#4904 3280


import os
os.environ["PATH"] += os.pathsep + "C:\\Program Files (x86)\\GnuWin32\\bin"
from libtiff import TIFF
from scipy import misc
from libtiff import TIFFfile


input_path = 'C:\\Users\\Jia\\Documents\\tiff\\'
output_path = 'C:\\Users\\Jia\\Documents\\'

def lsall(path):
    """ls all file in a folder and its sub-folder"""
    for i in os.listdir(path):
        abspath = os.path.join(path, i)
        print (abspath)
        if os.path.isdir(abspath):
            lsall(abspath)
        elif os.path.isfile(abspath):
            if os.path.splitext(abspath)[1] == '.tif':
                binTIF(abspath, os.path.join(output_path, i))

def binTIF(tiff_inpath,tiff_outpath):
    tiffin = TIFF.open(tiff_inpath, mode='r')
    tiffout = TIFF.open(tiff_outpath, mode='w')
    tiffout.write_image(tiffin)
    tiffout.close()


lsall(input_path)