#name=relion
#for i in {001..100}
#do
#type=`ls $name/* | grep -B 1 job$i | head -n 1 | cut -d '/' -f 2 | cut -d ':' -f 1 `
#ls $name/* | grep -q job$i && echo $type$i
#done

for j in {001..100}
do
  for i in Import CtfFind Extract Class2D Class3D Select Refine3D JoinStar 
  do 
    [ -e "relion/$i/job$j" ]&&echo $i$j
  done
done