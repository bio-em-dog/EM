echo "cd 'C:\Users\jia\Sync\demo_lp0.1\threshold_0.1'" > gnuplot_tmp
echo "set term pdf" >> gnuplot_tmp
echo "set output \"aaaa.pdf\"" >> gnuplot_tmp
echo "set xrange [0:1950]" >> gnuplot_tmp
echo "set yrange [0:1950]" >> gnuplot_tmp
echo "set size ratio -1" >> gnuplot_tmp

for i in `ls F*.data | cut -b -28`;do
  title=`echo $i | sed 's/_/\\_/g'`
  echo "set key right outside vertical center title \"${i}\" " >> gnuplot_tmp
  echo "DeepPicker=\"${i}_cnnPick.data\"" >> gnuplot_tmp
  echo "RelionAutoPcik=\"../../auto/${i}_autopick.data\"" >> gnuplot_tmp
  echo "plot DeepPicker pointsize 0.4, RelionAutoPcik pointsize 0.4">> gnuplot_tmp
done

echo "set output" >> gnuplot_tmp
