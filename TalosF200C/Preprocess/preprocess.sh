# 2021.12.30 JXD
# Preprocess talosF200C acquired movies
# import - motion - ctf - (cryolo/warp) - extract
#------------------------------input--------------------------------------------#
new_folder='TRF_20220120_sample3'
raw_folder='Supervisor_20220120_145529'
# /run/user/1000/gvfs/smb-share\:server\=winstorageserve\,share\=offloaddata/

apix=1.185
# 92k=1.516/1.52, 120k=1.185, 150k=0.936

totaldose=60
frame=84
motion_bin=1
group_frame=2
# Average together this many frames before calculating the beam-induced shifts

extract_size=384
# Size of the extracted area in micrographs (in pixels)
boxsize=192
# Rescaled box size to this values. 120 168 256
win_disk="d"
#-------------------------------------------------------------------------------#

mkdir /media/talos/Storage/${new_folder}
#[[ -e /media/talos/Storage/${new_folder}/Preprocess ]] || rsync -avP /media/talos/Storage/${new_folder} em@192.168.1.13:/mnt/${win_disk}/
cd /media/talos/Storage/${new_folder}

cp /home/talos/bin/preprocess/link.sh .
kill `ps -aux | grep "link.sh $raw_folder" | grep bash | awk {'print $2'}` 2> /dev/null
nohup bash link.sh ${raw_folder} > link.log &

mkdir Preprocess
mkdir Preprocess/job001
mkdir Preprocess/job002
mkdir Preprocess/job003
mkdir Preprocess/job004
mkdir Preprocess/job004/Micrographs
mkdir Preprocess/job005
mkdir Preprocess/warp
mkdir Preprocess/warp/average
touch apix${apix}_Dose${totaldose}_box${extract_size}to${boxsize}


while true; do

echo -e "\n\nimport"
date
relion_import  --do_movies  --optics_group_name "opticsGroup1" --angpix ${apix} --kV 200 --Cs 2.7 --Q0 0.15 --beamtilt_x 0 --beamtilt_y 0 --i "Micrographs/*.mrc" --odir Preprocess/job001/ --ofile movies.star --continue  --pipeline_control Preprocess/job001/ > Preprocess/import.out

grep Written Preprocess/import.out


echo -e "\n\nMotion"
date
mpirun -np 4 `which relion_run_motioncorr_mpi` --i Preprocess/job001/movies.star --o Preprocess/job002/ --first_frame_sum 1 --last_frame_sum -1 --use_own  --j 6 --bin_factor ${motion_bin}  --group_frames ${group_frame}  --bfactor 150 --dose_per_frame `echo "scale=6;$totaldose/$frame" | bc` --preexposure 0.5 --patch_x 5 --patch_y 5 --eer_grouping 32 --dose_weighting  --only_do_unfinished   --pipeline_control Preprocess/job002/ > Preprocess/motion.out

#rsync -avP Preprocess/job002/Micrographs/Foil*mrc em@192.168.1.13:/mnt/${win_disk}/${new_folder}/ > /dev/null &
cd Preprocess/warp
ln -s ../job002/Micrographs/*mrc . 2> /dev/null
echo "" > header
echo "data_" >> header
echo "">> header
echo "loop_">> header
echo "_rlnCoordinateX #1">> header
echo "_rlnCoordinateY #2">> header
[[ -e allparticles_BoxNet2Mask_20180918.star ]] && python3 ~/bin/split_star_by_mic.py allparticles_BoxNet2Mask_20180918.star
mv F*star ../job004/Micrographs/
cd average
ln -s ../../job002/Micrographs/*mrc . 2> /dev/null
cd ../../..


echo -e "\n\nCtf"
date
mpirun -np 5 `which relion_run_ctffind_mpi` --i Preprocess/job002/corrected_micrographs.star --o Preprocess/job003/ --Box 512 --ResMin 30 --ResMax 3 --dFMin 5000 --dFMax 50000 --FStep 500 --dAst 100 --ctffind_exe /home/talos/software/ctffind-4.1.14/ctffind --ctfWin -1 --is_ctffind4  --only_do_unfinished  --pipeline_control Preprocess/job003/ > Preprocess/ctf.out


echo -e "\n\nExtract"
date
suffix="_warppicking.star" # _warppicking.star
mpirun -np 6 `which relion_preprocess_mpi` --i Preprocess/job003/micrographs_ctf.star --coord_dir Preprocess/job004/ --coord_suffix ${suffix} --part_star Preprocess/job005/particles.star --part_dir Preprocess/job005/ --extract --extract_size ${extract_size} --scale ${boxsize} --norm --bg_radius `echo "${boxsize}*0.375" | bc` --white_dust -1 --black_dust -1 --invert_contrast  --only_do_unfinished   --pipeline_control Preprocess/job005/ > Preprocess/particle.out 2> Preprocess/particle.err

echo -n "Particles:  "
[[ -e Preprocess/job005/particles.star ]] && grep -c Foil Preprocess/job005/particles.star

done


kill `ps -aux | grep "$raw_folder" | head -n 1 | awk {'print $2'}`

