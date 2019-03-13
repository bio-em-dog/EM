

if [[ $1 = "" || $2 = "" ]]; then
echo "usage: ClassNumber.sh <number of classes> <iter>"
exit 0
fi

classes=$1
if [[ $2 -lt 10 ]];then
iter=0$2
else
iter=$2
fi
column=`grep "_rlnClassNumber" run_it001_data.star | cut -d '#' -f 2`


for ((i=1;i<=classes;i++)) 
do echo -en "$i\t"
if [ -e run_it0${iter}_data.star ];then
cat run_it0${iter}_data.star | awk -v a=$column {'print $a'} | grep -c "^$i$"
elif [ -e run_ct??_it0${iter}_data.star ];then
cat run_ct??_it0${iter}_data.star | awk -v a=$column {'print $a'} | grep -c "^$i$"
fi
done

