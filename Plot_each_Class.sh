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

#生成gnuplot的命令
echo -e "set term pdf\nset output \"aaaa_$DATE.pdf\"\nunset key" > gnuplot_script_$DATE
echo -n "plot \"list_$DATE\" using 1 with lp ls 7" >> gnuplot_script_$DATE
for i in {2..25}
do
  echo -n ", \"list_$DATE\" u $i w lp ls 7" >> gnuplot_script_$DATE
done
echo -e "\nset output" >> gnuplot_script_$DATE

gnuplot gnuplot_script_$DATE
