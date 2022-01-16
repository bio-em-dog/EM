V2.0：直接操作tiff文件，不借助第三方tiff库，保留完整的tag信息

LZW?

## EMSIS Tiff Sturcture

preview

## GUI

Gooey?
TKinter?
TKinter Designer https://www.codercto.com/a/106320.html

## Tiff有关的信息

https://blog.csdn.net/u010476739/article/details/98640034
https://www.cnblogs.com/gywei/p/3393816.html
https://blog.csdn.net/liygcheng/article/details/16833499


HexView用来看二进制文件，一个格子的位置表示1个Byte=8bit，因为一个Byte是8位置，0-256，16进制表示就是16*16



* IFH
  * 2, Byte 0-1, Byteorder, 字节顺序标志位。II表示小字节在前， 称为`little-endian`。MM表示大字节在前，`big-endian`。
  * 2, Byte 2-3, Version, 2A00，TIFF的标志位，固定的
  * 4, Byte 4-7, Offset to first IFD, 第一个IFD偏移量
* IFD
  * 2, Byte 0-1：Directory Entry Count, IFD中DE的数量
  * 12, DE
    * 2, tag标签编号 tag: https://www.loc.gov/preservation/digital/formats/content/tiff_tags.shtml
    * 2, type该属性数据的类型 
    * 4, length该种类型的数据的**个数**
    * 4, valueOffset,偏移量，但如果变量值占用的空间不多于4个字节（例如只有1个Integer类型的值），那么该值就直接存放在valueOffset中
  * 4, Offset to next IFD, 下一个IFD的偏移量

0001　　Byte
0002　　Ascii　　　文本类型，7位Ascii码加1位二进制0
0003　　Integer
0004　　Long
0005　　RATIONAL　 分数类型，由两个Long组成，第1个是分子，第2个是分母

## history
v1.0
Tkinter写的GUI
遍历目录


