#观察每一轮中有多少变化
[ -e exchange.txt ]&& rm exchange.txt
column=`grep "rlnClass" run_it000_data.star | cut -d '#' -f 2`
awk -v a=$column {'print $a'} < run_it001_data.star > tmp.aaa.1
for ((i=2;i<=25;i++));do
  file=`ls run_*it*${i}_data.star | tail -n 1`
  awk -v a=$column {'print $a'} < $file > tmp.aaa.$i

  paste tmp.aaa.$(($i - 1)) tmp.aaa.$i | awk {'print $2-$1'} | grep -cv '^0$' >> exchange.txt

done

echo "total:`grep -c "Micrographs" run_it000_data.star `" >> exchange.txt

rm tmp.aaa.*