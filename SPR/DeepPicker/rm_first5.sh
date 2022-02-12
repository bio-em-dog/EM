for i in `ls *.star | cut -d '.' -f 1`;do
row=`cat $i.star | wc -l`
tail -n $(($row-5)) $i.star > $i.data
done
