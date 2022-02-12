将一个relion class2d里的每一个class都拿出来，然后做一次Class2d，根据分辨率，判断好的Class2D
### 目前：
- 全取全class
- 只能看final res

### 实际上还有改进空间：
- 原来的一个class颗粒数少于多少，直接就不做class了
- 分类多出了多少？/空分类有几个？


mpirun -np 3 `which relion_refine_mpi` --o 2D_ana/$i/run --i star/$i --dont_combine_weights_via_disc --pool 3 --iter 25 --tau2_fudge 2 --particle_diameter -1 --K 100 --flatten_solvent  --zero_mask  --oversampling 1 --psi_step 12 --offset_range 5 --offset_step 2 --norm --scale  --j 1 --gpu "" --dont_check_norm > 2D_ana/$i/log

运行relion脚本
