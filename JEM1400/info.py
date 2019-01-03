#!-coding-utf8
input_path = 'C:\\Users\\Jia\\Documents\\tiff\\Image_01.tif'


def bytes2hex(bytes):
    num = len(bytes)
    hexstr = u""
    for i in range(num):
        t = u"%x" % bytes[i]
        if len(t) % 2:
            hexstr += u"0"
        hexstr += t
    return hexstr.upper()



binfile = open(input_path, 'rb')

bins = binfile.read(20)
binfile.close()
bins = bytes2hex(bins)
bins = bins.lower()
print(bins)