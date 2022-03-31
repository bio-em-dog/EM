# based on distorted image (independent variable) to origin image (dependent variable) formula

from PIL import Image
import itertools
import math

image = Image.open('banna.jpg').convert('L')
out_x = image.size[0]+100
out_y = image.size[1]+100
out = Image.new('L', (out_x, out_y))
#super_res_list = [[0 for i in range(out_x)] for j in range(out_y)]


def blackWhite(img):
    blackXY = []

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            #print(img.getpixel((x, y)))
            if img.getpixel((x, y)) < 128:
                img.putpixel((x, y), 0)
                blackXY.append((x, y))
            else:
                img.putpixel((x, y), 255)
    return blackXY

'''
def writevalue(img,ax,ay,x,y,weight1,weight2):
    if super_res_list[int(ay)][int(ax)] == -1:
        super_res_list[int(ay)][int(ax)] = img.getpixel((x, y)) * weight1 * weight2
    else:
        super_res_list[int(ay)][int(ax)] = \
            0.5 * (super_res_list[int(ay)][int(ax)] +
                   img.getpixel((x, y)) * weight1 * weight2)
# super res style
'''

def corr(img):
    size_x = img.size[0]
    size_y = img.size[1]
    for x in range(size_x):
        for y in range(size_y):
            cx = x - (0.5 * size_x + 0.5 + 13)
            cy = y - (0.5 * size_y + 0.5 - 32)
            r = (cx**2 + cy**2)**0.5
            ang = math.atan(cy / cx)
            print("cx:%scy:%s\tr:%sang:%s"%(cx,cy,r,ang))
#            nx = cx * (1 + k1 * r + k2 * r**2)
#            ny = cy * (1 + k1 * r + k2 * r**2)
            nr = -2.4e-8*r**3 - 1.8e-5*r**2 + 1.0061*r
            dang = 8.3e-13*r**3 + 2.9e-8*r**2 - 4.7e-07*r
            ncy = math.sin(ang+dang)*nr
            ncx = math.cos(ang+dang)*nr
            if cx < 0:
                ncx = -ncx
                ncy = -ncy
            nx = ncx + 0.5 * out_x + 0.5
            ny = ncy + 0.5 * out_y + 0.5
            print("nx:%s,ny:%s" % (nx,ny))
            out.putpixel((int(round(nx)), int(round(ny))), img.getpixel((x, y)))

'''
            weight_x = nx - math.floor(nx)
            weight_y = ny - math.floor(ny)
            writevalue(img, math.floor(nx), math.floor(ny), x, y, (1-weight_x), (1-weight_y))
            writevalue(img, math.ceil(nx), math.ceil(ny), x, y, weight_x, weight_y)
            writevalue(img, math.ceil(nx), math.floor(ny), x, y, (1 - weight_x), weight_y)
            writevalue(img, math.floor(nx), math.ceil(ny), x, y, weight_x, (1 - weight_y))
#sim super resolution
'''




#blackWrite(image)
corr(image)
'''
for yy in range(out_y):
    for xx in range(out_x):
        out.putpixel((xx,yy),int(round(super_res_list[yy][xx])))
'''

#image.save("test_gray.jpg")
out.save("sd.jpg")

