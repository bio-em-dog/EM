#运行文件夹内有一以下文件：cls文件夹，box文件夹，remove_out_range.py，right_inrange.py（非必须）

for i in `ls ./box/*.box`
    do python remove_out_range.py $i 
done | cut -d '/' -f 1 > remove.log && echo 'out range box removed'

#iminfo start.hed all > allparticle

#查找start.img里面用了那些图片里面的particle
for i in `ls ./inrange_box/*.box | cut -d '/' -f 3 | cut -d '.' -f 1`
    do cat allparticle | grep $i && echo $i >> tmp1
    cat allparticle | grep $i | wc -l >> tmp4
done > tmp3 && echo 'used micrograph found'
paste tmp4 remove.log > tmp5
python right_inrange.py

#把用到的box文件合成一个列表，然后粘贴到allparticle后面
for i in `cat tmp1`
    do cat ./inrange_box/$i* >> tmp2
done
paste allparticle tmp2 > all && echo 'creat all'
rm tmp1 #用了的box文件列表
rm tmp2 #用了的box文件首尾相连
rm tmp3 #防止刷屏
rm tmp4 #用了box数量列表
rm tmp5 #判断用了的和box文件里的数量是否一样
rm remove.log

#遍历每个cls文件，按照cls文件中的颗粒编号从all中找到坐标
for i in `ls cls/cls*.lst`
    do for j in `cat $i | cut -f 1`
        do cat all | grep "^${j}\." || echo $i 
    done > ${i}.tmp
    cat ${i}.tmp | cut -f 1,5,6,7,8 | grep -v 'cls' > ${i}.xy
    rm ${i}.tmp
done && echo 'done'

