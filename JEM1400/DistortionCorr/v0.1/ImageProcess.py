#!/usr/bin/env python
from PIL import Image
import itertools

image = Image.open("vv006.tif")\
    #.convert('L')


def blackWrite(img):
    blackXY = []

    for x in range(img.size[0]):
        for y in range(img.size[1]):
#            print img.getpixel((x, y))
            if img.getpixel((x, y)) < 75:
                img.putpixel((x, y), 0)
            else:
                img.putpixel((x, y), 255)
    return blackXY


blackWrite(image)

image.save("vvv.jpg")