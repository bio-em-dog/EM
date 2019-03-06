if [ -e ctfparm.txt ];then
echo "ctfparm.txt exist"
exit 0
fi

imagename=`grep _rlnMicrographName micrographs_ctf.star | cut -d "#" -f 2`
defU=`grep _rlnDefocusU micrographs_ctf.star | cut -d "#" -f 2`
defV=`grep _rlnDefocusV micrographs_ctf.star | cut -d "#" -f 2`

grep Micrographs micrographs_ctf.star | awk -v a=$imagename -v b=$defU -v c=$defV {'print $a"\t"($b+$c)/20000*-1'} | sed 's/Micrographs\///g' | sed 's/.mrc//g' > tmp12312321321321
IFS='
'
for i in `cat tmp12312321321321`;do
echo "$i,56.478,1.79402,0.096346,0.89701,13.0233,9.33555,3.8206,120,1.6,2.21,/home/em/mounttmp/20190223/strucfac.txt"
done > ctfparm.txt
rm tmp12312321321321

