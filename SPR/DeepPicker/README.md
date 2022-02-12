用deeppicker软件生成了不同threshold下的Autopick结果(star file)，
使用一些脚本分析一下
* 画出deeppicker结果和relion的示例结果画出一张图

先使用 rm_first5.sh 把生成的 star file 的前5行头去掉，方便gnuplot用

然后用 generate\_gnuplot\_script.sh 生成gnuplot脚本

### generate\_gnuplot\_script.sh

因为在win上用，第一行先cd

set term pdf  
set output  
set xrange[:]  
set size ratio -1  gnuplot绘图时xy轴成1:1比例  
set key right outside vertical center title "${tit}" 设置图例key的位置、排列方式、标题  
在title里面`_`会导致后面的字符被小写，要写成`\\_`

### 脚本里对文本查找替换

sed进行替换  
和vi里面一样`sed 's/<查找内容>/<替换内容>/g'`