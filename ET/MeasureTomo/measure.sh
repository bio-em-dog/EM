#!bin/bash
#---------------------------------------#
input=ct-[0-9][0-9]-*-srt.mrc
#input file
output=4point.pdf
#out put pdf file name
shift=10
#shift distance against center
#--------------------------------------#

echo -e "set term pdf\nset output \"$output\"" > gnuplot_script
#\nset multiplot layout 2,4

task=1
#task counter

for i in `ls $input`;do
  xvalue=0

  proc3d $i due$i rot=-90,0,0
  proc3d due$i due$i sym=c12
  proc3d due$i due$i rot=90,0,0

  python measure.py due$i $shift > tmp.$i.tmp

  for j in `cat tmp.$i.tmp`;do
    echo "set label \"$xvalue\" at $xvalue,$j font \"Times-Roman,8\"" >> gnuplot_script
    xvalue=$(($xvalue+1))
  done

  echo "plot \"tmp.$i.tmp\" with lp ls 2" >> gnuplot_script

  for ((k=0;k<=`cat tmp.$i.tmp | wc -l`;k++));do
    echo "unset label \"$k\"" >> gnuplot_script
  done
  echo "$task/`ls $input|wc -l` done"
  task=$(($task+1))

  rm due$i
done
rm tmp.*.tmp

echo -e "set output" >> gnuplot_script

gnuplot gnuplot_script

