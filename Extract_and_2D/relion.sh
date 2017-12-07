rm -r 2D_ana
mkdir 2D_ana
for i in `ls star/ex*.star | cut -d '/' -f 2`;do mkdir 2D_ana/$i
mpirun -np 3 `which relion_refine_mpi` --o 2D_ana/$i/run --i star/$i --dont_combine_weights_via_disc --pool 3 --iter 25 --tau2_fudge 2 --particle_diameter -1 --K 100 --flatten_solvent  --zero_mask  --oversampling 1 --psi_step 12 --offset_range 5 --offset_step 2 --norm --scale  --j 1 --gpu "" --dont_check_norm > 2D_ana/$i/log
done

