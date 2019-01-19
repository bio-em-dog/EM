from PIL import Image
import itertools

image = Image.open('banna.jpg').convert('L')
out = Image.new('L',(image.size[0], image.size[1]))

def blackWrite(img):
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


def corr(img, k1, k2, p1, p2):
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            cx = x - (0.5*img.size[0])
            cy = y - (0.5*img.size[1])
            r = cx**2 + cy**2
            print("r%scx%sx%s"%(r,cx,x))
#            nx = cx * (1 + k1 * r + k2 * r**2) + (2*p1*cy + p2*(r+2*cx**2))
            nx = cx * (1 + k1 * r + k2 * r**2)
#            nx = cx + (2*p1*cy + p2*(r+2*cx**2))
            #print("nx%s"%(nx))
#            ny = cy * (1 + k1 * r + k2 * r**2) + (2*p1*cx + p2*(r+2*cy**2))
            ny = cy * (1 + k1 * r + k2 * r**2)
#            ny = cy + (2*p1*cx + p2*(r+2*cy**2))
            out.putpixel((int(nx+(0.5*img.size[0])),int(ny+(0.5*img.size[1]))),img.getpixel((x,y)))

#blackWrite(image)
corr(image,-8e-8,-8e-15,1,1)

#image.save("test2.jpg")
out.save("test8.jpg")

