269 121 321 
rise 42.44106
twist 18.47096

# 线性代数
https://www.zhihu.com/question/19869518/answer/1873733565

# 

# coord
# rotatecd 



# Orientations

## Translation
shift observations into the reference projection
将颗粒移动到投影

右手坐标系xyz (x右, y向后, z向上)
> https://baike.baidu.com/item/%E5%8F%B3%E6%89%8B%E7%B3%BB/9751780

先Translation

### center

左上方第一个像素=(0, 0)
`((int)xdim/2, (int)(ydim/2))`


## rotation
rotate the reference into observations (i.e. particle image)
转动实体到颗粒

-180 < `Rot` < 180
0 < `Tilt` < 180
-180 < `Psi` < 0

右手旋转 right hand rotation

> https://www.researchgate.net/figure/Right-handed-rotation-with-the-thumb-of-the-right-hand-pointing-along-the-rotation-axis_fig18_257891177
> Angles are commonly defined according to the right-hand rule. Namely, they have positive values when they represent a rotation that appears `clockwise` when looking in the positive direction of the axis, and negative values when the rotation appears counter-clockwise.

Rot around Z
Tilt around Y
Psi around new Z

# particle coordinate

左上为0
pixel

# Euler angle
不能直接加和
通过旋转矩阵rotation matrix加和
