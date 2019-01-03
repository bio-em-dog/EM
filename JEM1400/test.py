import os
import tifffile
from os import listdir
from os.path import isfile, join
import PIL.Image
import PIL.ExifTags


input_path = 'C:\\Users\\Jia\\Documents\\tiff\\Image_01.tif'
output_path = 'C:\\Users\\Jia\\Documents\\tiff\\a42.tif'

series1 = tifffile.imread(input_path, series=0)
print (series1.shape)
print (series1.dtype)

tifffile.imwrite(output_path, series1[:,:,1])
print (tifffile.imread(output_path))

from PIL import Image
im=Image.open(input_path)
print (im)
