# based on origin coordinate to distorted image

from PIL import Image
import itertools
import math

image = Image.open('banna03-bin2.jpg').convert('L')
in_x = image.size[0]
in_y = image.size[1]
out_x = image.size[0]+200
out_y = image.size[1]+200
out = Image.new('L', (out_x, out_y))


def corr(img):
    for x in range(out_x):
        for y in range(out_y):
            cx = x - (0.5 * out_x + 0.5 + 13)
            cy = y - (0.5 * out_y + 0.5 - 32)
            r = (cx**2 + cy**2)**0.5
            ang = math.atan(cy / cx)
            print("cx:%scy:%s\tr:%s\tang:%s"%(cx,cy,r,ang))
            nr = 4.21e-8*r**3 - 1.2e-6*r**2 + 0.9987*r
            dang = 8.3e-12*r**3 + 2.237e-8*r**2 - 1.121e-6*r
            ncy = math.sin(ang-dang)*nr
            ncx = math.cos(ang-dang)*nr
            if cx < 0:
                ncx = -ncx
                ncy = -ncy
            nx = ncx + (0.5 * in_x + 0.5 + 13)
            ny = ncy + (0.5 * in_y + 0.5 - 32)
            if math.ceil(nx) >= in_x or math.floor(nx) <= 0 or math.ceil(ny) >= in_y or math.floor(ny) <= 0:
                out.putpixel((x, y), 0)
            else:
                weight_x = nx - math.floor(nx)
                weight_y = ny - math.floor(ny)
                # floor--left-lower-(1-weight), ceil--right-upper-(weight)
                pixel_ll=img.getpixel((int(math.floor(nx)), int(math.floor(ny)))) * (1-weight_x) * (1-weight_y)
                pixel_ur=img.getpixel((int(math.ceil(nx)), int(math.ceil(ny)))) * weight_x * weight_y
                pixel_lr=img.getpixel((int(math.ceil(nx)), int(math.floor(ny)))) * weight_x * (1-weight_y)
                pixel_ul=img.getpixel((int(math.floor(nx)), int(math.ceil(ny)))) * (1-weight_x) * weight_y
                out.putpixel((x, y), int(round(pixel_ll + pixel_lr + pixel_ul + pixel_ur)))
                print("%s\t%s"%(weight_x,weight_y))
            #print("nx:%s,ny:%s" % (nx,ny))

#            super_res_list[int(math.floor(ny))][int(math.floor(nx))] += img.getpixel((x, y)) * (1-weight_x) * (1-weight_y)
#            super_res_list[int(math.ceil(ny))][int(math.ceil(nx))] += img.getpixel((x, y)) * weight_x * weight_y
#            super_res_list[int(math.floor(ny))][int(math.ceil(nx))] += img.getpixel((x, y)) * (1-weight_x) * weight_y
#            super_res_list[int(math.ceil(ny))][int(math.floor(nx))] += img.getpixel((x, y)) * weight_x * (1-weight_y)

#            out.putpixel((int(round(nx+0.5*out_x)),int(round(ny+0.5*out_y)),img.getpixel((x,y)))


corr(image)


#image.save("test2.jpg")
out.save("sd_sup2.jpg")

