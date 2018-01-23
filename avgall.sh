for i in {000..125};do
  for j in `ls trf2_${i}?_sum.mrc`;do
    echo $j
    proc2d $j total$i.hdf
  done
  proc2d total$i.hdf avg${i}_tmp1.mrc average
  rm total$i.hdf
  echo -e "\n>>>>>>$i*done\n"
done

for i in {00..12};do
  for j in `ls avg${i}?_tmp1.mrc`;do
    echo $j
    proc2d $j total$i.hdf
  done
  proc2d total$i.hdf avg${i}_tmp2.mrc average
  rm total$i.hdf
  rm avg$i?_tmp1.mrc
  echo -e "\n>>>>>>$i**done\n"
done

for i in `ls avg??_tmp2.mrc`;do
  proc2d $i total.hdf
done
proc2d total.hdf avgall.mrc
  rm total.hdf
  rm avg??_tmp2.mrc