mkdir relion

cd relion
mkdir Micrographs
mkdir .box
cd .box
mkdir Micrographs

cd ../../raw
echo 'ser to lp 10 hdf'
for i in `ls *.ser | cut -d '.' -f 1`
do e2proc2d.py $i.ser ../micrographs/$i.hdf --process=filter.lowpass.gauss:cutoff_freq=0.1
done

echo 'ser to mrc'
for i in `ls *.ser | cut -d '.' -f 1`
do e2proc2d.py $i.ser ../relion/Micrographs/$i.mrc
done

cd ../