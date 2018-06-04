# read write image
f(filename string, img zero-indexed list/int, header_only bool, Region Region(ox,oy,xsize,ysize), is_3D bool)
f_default(,all/0,False,Region(1,1,nx,ny),mrc/mrcs)

## image stack
no need initializes
`imagelist=EMData.read_images("stack.mrc",[2,3])`
count
`EMUtil.get_image_count("stack.mrc")`

## single image

# 1
initializes EMData object
```
singleimage=EMData()
singleimage.read_image("stack.mrc",2,True,,)
```

# 2
`singleimage=EMData("name.mrc",0,False,Region(1,1,50,50))`

# 3
```
singleimage=EMData()
name="name.mrc"
region=Region(1,1,50,50)
singleimage.read_image(name,0,False)
```

## write
f(filename string, img zero-indexed list/int,filetype , header_only bool, Region, Datatype) 

`var.write_image("newname.mrc",2)`
