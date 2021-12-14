xyz 269 121 321 
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
Tilt around **new** Y
Psi around **new** Z

# particle coordinate

左上为0
pixel

# Euler angle
不能直接加和
通过旋转矩阵rotation matrix转换

https://www.p-chao.com/2018-04-14/%E6%AC%A7%E6%8B%89%E8%A7%92%EF%BC%88eular-angle%EF%BC%89%E8%AF%A6%E8%A7%A3/#i-2
https://zhuanlan.zhihu.com/p/195683958
https://zhuanlan.zhihu.com/p/85108850
https://zhuanlan.zhihu.com/p/183973440
https://blog.csdn.net/hzwwpgmwy/article/details/101547949

```python
import numpy as np
model_coor=np.array([[x-center],[y-center],[z-center]])  # column xyz
rot_coor=rz(psi).dot(ry(tilt)).dot(rz(rot)).dot(model_coor)   # 

def rz(angle):
    angle=np.deg2rad(angle)
    array=np.array([[np.cos(angle), np.sin(angle), 0], [-1*np.sin(angle), np.cos(angle), 0], [0,0,1]])
    return(array)

def ry(angle):
    angle=np.deg2rad(angle)
    array=np.array([[np.cos(angle),0,-1*np.sin(angle)], [0,1,0], [np.sin(angle), 0, np.cos(angle)]])
    return(array)
```
$$
rz=\begin{bmatrix}
cos&sin&0\\
-sin&cos&0\\
0&0&1\\
\end{bmatrix}
$$
旋转顺序$Z_{rot}Y_{tilt}Z_{psi}$，旋转矩阵：
$$
\begin{bmatrix} x\\ y\\ z\\ \end{bmatrix}
=Z(psi)Y(tilt)Z(rot)
\begin{bmatrix} x_r\\ y_r\\ z_r\\ \end{bmatrix}
=
\begin{bmatrix}
c3&s3&0\\
-s3&c3&0\\
0&0&1\\
\end{bmatrix}
\begin{bmatrix}
c2&0&-s2\\
0&1&0\\
s2&0&c2\\
\end{bmatrix}
\begin{bmatrix}
c1&s1&0\\
-s1&c1&0\\
0&0&1\\
\end{bmatrix}
\begin{bmatrix}
x_r\\
y_r\\
z_r\\
\end{bmatrix}
\\
=
\begin{bmatrix}
c3c2c1-s3s1&c3c2s1+s3c1&-c3s2\\
-s3c2c1-c3s1&-s3c2s1+c3c1&s3s2\\
s2c1&s2s1&c2\\
\end{bmatrix}
\begin{bmatrix}
x_r\\
y_r\\
z_r\\
\end{bmatrix}
$$

$(x_{r},y_{r},z_{r})$ 在reference model中的点