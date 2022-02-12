#name=relion
#for i in {001..100}
#do
#type=`ls $name/* | grep -B 1 job$i | head -n 1 | cut -d '/' -f 2 | cut -d ':' -f 1 `
#ls $name/* | grep -q job$i && echo $type$i
#done

#for j in {001..100}
#do
#  for i in Import CtfFind Extract Class2D Class3D Select Refine3D JoinStar AutoPick
#  do 
#    if [ -e "relion/$i/job$j" ]&&echo $i$j
#  done
#done

Relion_dir=relion

for j in {001..100}
do
  if [ -e "$Relion_dir/Import/job$j" ] ;then
    DIR=$Relion_dir/Import/job$j
    Micog=`grep -c 'Micrographs' $DIR/micrographs.star`
    echo -e "Import$j\t导入$Micog张照片"

  elif [ -e "$Relion_dir/Extract/job$j" ] ;then
    DIR="$Relion_dir/Extract/job$j"
    Particle=`grep 'Written' $DIR/run.out | cut -d ' ' -f 7`
    Boxsize=`grep 'Particle box size' $DIR/run.job | cut -d ' ' -f 6`
    Apix=`grep 'Pixel size' $DIR/run.job | cut -d ' ' -f 5`
    Rescale_size=`grep 'Re-scaled size' $DIR/run.job | cut -d ' ' -f 6`
    Apix2=`echo "$Boxsize / $Rescale_size * $Apix" | bc`
    echo -e "Extract$j\t导出$Particle个颗粒, boxsize=$Boxsize,apix=$Apix,boxsize缩小到$Rescale_size,apix=$Apix2 "

  elif [ -e "$Relion_dir/Class2D/job$j" ] ;then
    DIR="$Relion_dir/Class2D/job$j"
    Input_type=`grep 'Input images STAR file' $Relion_dir/Class2D/job$j/run.job | cut -d ' ' -f 6 | cut -d '/' -f 1 `
    Input_job=`grep 'Input images STAR file' $Relion_dir/Class2D/job$j/run.job | cut -d ' ' -f 6 | cut -d '/' -f 2 | cut -b 4- `
    Number_of_classes=`grep 'Number of classes' $Relion_dir/Class2D/job$j/run.job | cut -d ' ' -f 5 `
    Resolution=`grep 'Res' $DIR/run.out | tail -n 1 | cut -d ' ' -f 3`
    Limit=`grep 'Limit resolution E-step to' $Relion_dir/Class2D/job$j/run.job | cut -d ' ' -f 8 `
    Mask=`grep 'Mask diameter' $Relion_dir/Class2D/job$j/run.job | cut -d ' ' -f 5`
    echo -en "Class2D$j\t将$Input_type$Input_job分成$Number_of_classes类, 最终分辨率为$Resolution"
    [ $Mask != -1 ] && echo -n ",Mask=$Mask"
    [ $Limit != -1 ] && echo -n ",限制分辨率到${Limit}A"
    echo ""

  elif [ -e "$Relion_dir/Class3D/job$j" ] ; then
    DIR="$Relion_dir/Class3D/job$j"
    Input_type=`grep 'Input images STAR file' $DIR/run.job | cut -d ' ' -f 6 | cut -d '/' -f 1 `
    Input_job=`grep 'Input images STAR file' $DIR/run.job | cut -d ' ' -f 6 | cut -d '/' -f 2 | cut -b 4- `
    Number_of_classes=`grep 'Number of classes' $DIR/run.job | cut -d ' ' -f 5 `
    echo -e "Class3D$j\t$Input_type$Input_job,分为$Number_of_classes类"

  elif [ -e "$Relion_dir/Select/job$j" ] ; then
    DIR="$Relion_dir/Select/job$j"
    Input_type=`grep 'Select classes from model.star' $DIR/run.job | cut -d ' ' -f 6 | cut -d '/' -f 1 `
    Input_job=`grep 'Select classes from model.star' $DIR/run.job | cut -d ' ' -f 6 | cut -d '/' -f 2 | cut -b 4- `
    Outputimage=`grep 'selected images' $DIR/run.out | tail -n 1 | cut -d ' ' -f 4`
    Outputparticle=`grep 'selected particles' $DIR/run.out | tail -n 1 | cut -d ' ' -f 4`
    echo -e "Select$j\t从$Input_type$Input_job选出$Outputimage个分类的$Outputparticle个颗粒"

  elif [ -e "$Relion_dir/Refine3D/job$j" ] ; then
    DIR="$Relion_dir/Refine3D/job$j"
    Input_type=`grep 'Input images STAR file' $DIR/run.job | cut -d ' ' -f 6 | cut -d '/' -f 1 `
    Input_job=`grep 'Input images STAR file' $DIR/run.job | cut -d ' ' -f 6 | cut -d '/' -f 2 | cut -b 4- `
    Resolution=`grep 'Res' $DIR/run.out | tail -n 1 | cut -d ' ' -f 3 `
    echo -e "Refine3D$j\t$Input_type$Input_job,分辨率为$Resolution"

  elif [ -e "$Relion_dir/JoinStar/job$j" ] ; then
    ehco -e "JoinStar$j\t"

  elif [ -e "$Relion_dir/AutoPick/job$j" ] ; then
    ehco -e "AutoPick$j\t"

  elif [ -e "$Relion_dir/CtfFind/job$j" ] ;then
    echo -e "CtfFind$j\t"
  fi
done
