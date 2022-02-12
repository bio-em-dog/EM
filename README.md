- [EM](#em)
  - [bin](#bin)
  - [ET](#et)
  - [FIB](#fib)
  - [JEM1400](#jem1400)
  - [SPR](#spr)
  - [TalosF200C](#talosf200c)
  - [Others](#others)
  - [Outdated](#outdated)
    - [Plot_each_class.sh](#plot_each_classsh)
    - [autolog.sh](#autologsh)
    - [autorelion.sh](#autorelionsh)
    - [awk_ClassNumber](#awk_classnumber)
    - [class_exchange.sh](#class_exchangesh)
    - [class_exchange_pot.sh](#class_exchange_potsh)
    - [refine helical](#refine-helical)
    - [remove_out_range.py](#remove_out_rangepy)
    - [runpar-4.py](#runpar-4py)
    - [DataTrans.py](#datatranspy)
    - [select_micrographs.py](#select_micrographspy)
    - [pot_change.sh](#pot_changesh)
    - [Split copy fft](#split-copy-fft)


# EM
## bin
## ET
## FIB
## JEM1400
## SPR
## TalosF200C
## Others
## Outdated








### Plot_each_class.sh

2017-12

画Class2D的结果

- x轴，循环轮数
- y轴，颗粒数
- 每条线代表一个class的“盒子”


### autolog.sh

2017.11

- [x] 加入常见信息grep


### autorelion.sh

2017-11

- 在eman过后，自动建立relion的一套文件夹


### awk_ClassNumber

2017-12

- 用awk的方法来统计ClassNumber


### class_exchange.sh

2017-12  
每一个iter的总变化颗粒数

- [ ] 加入自动画图

### class_exchange_pot.sh

2017-12  
每一个class在每一轮的出入数


### refine helical



### remove_out_range.py
2017-06


### runpar-4.py


### DataTrans.py

自动转移文件

### select_micrographs.py
2017-06
不熟练的时候的脚本;一个starfile，一个list是所有好的micrographs名称，只保留在list列micrographs面的颗粒。


### pot_change.sh

2017-12

/run/media/em/data3t-1/trf2/trf2-20171121-5p1/relion/Class2D/job004
- [x] 哪个class盒子的颗粒出入多 见class_exchange两个脚本

### Split copy fft

GUI的制作 PAGE  按钮-变量
打包发布 Pyinstaller
