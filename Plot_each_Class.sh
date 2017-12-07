#生成一个包含每个iter（行）每个classes颗粒数目的文件list_$DATE
#------------------------------------------------------
DATE=$(date +%Y%m%d%H%M%S)

Number_of_iteration=25
Number_of_Classes=100
#注意cut的位置！！！
#------------------------------------------------------

for j in {01..25}
do
  for ((i=1;i<=$Number_of_Classes;i++))
  do
    ClassNumber=`cat run*_it0${j}_data.star | cut -b 230-265 | grep "  $i  " | wc -l`
    echo -n "$ClassNumber " >> list_$DATE
  done
  echo "" >> list_$DATE
done

#将最后一轮的数据单独列出
for i in `tail -n 1 list_$DATE`
do
  echo $i
done > ClassNumber025

large1=`sort -r -n ClassNumber025 | head -n 1 | tail -n 1`
large1Pos=`grep -n $large1 ClassNumber025 | cut -d ':' -f 1`
large2=`sort -r -n ClassNumber025 | head -n 2 | tail -n 1`
large2Pos=`grep -n $large2 ClassNumber025 | cut -d ':' -f 1`
large3=`sort -r -n ClassNumber025 | head -n 3 | tail -n 1`
large3Pos=`grep -n $large3 ClassNumber025 | cut -d ':' -f 1`

#生成gnuplot的命令
echo -e "set term pdf\nset output \"aaaa_$DATE.pdf\"\nunset key" > gnuplot_script_$DATE
echo "set label 1 \"$large1\" at $Number_of_iteration,$large1 center" >> gnuplot_script_$DATE
echo "set label 2 \"$large2\" at $Number_of_iteration,$large2 center" >> gnuplot_script_$DATE
echo "set label 3 \"$large3\" at $Number_of_iteration,$large3 center" >> gnuplot_script_$DATE
echo -n "plot \"list_$DATE\" using 1 with lp ls 7" >> gnuplot_script_$DATE
for ((i=2;i<=$Number_of_Classes;i++))
do
  if [ $i -eq large1Pos ];then
    echo -n ", \"list_$DATE\" u $i w lp ls 3" >> gnuplot_script_$DATE
  elif [ $i -eq large2Pos ];then
    echo -n ", \"list_$DATE\" u $i w lp ls 4" >> gnuplot_script_$DATE
  elif [ $i -eq large3Pos ];then
    echo -n ", \"list_$DATE\" u $i w lp ls 5" >> gnuplot_script_$DATE
  else
    echo -n ", \"list_$DATE\" u $i w lp ls 7" >> gnuplot_script_$DATE
  fi
done
echo -e "\nset output" >> gnuplot_script_$DATE

gnuplot gnuplot_script_$DATE
