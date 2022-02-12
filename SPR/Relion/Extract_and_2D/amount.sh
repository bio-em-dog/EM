rm -r list_auto2d
mkdir list_auto2d

for i in {1..100}
    do for j in {1..100}
        do cat 2D_ana/ex$i.star/run_it025_data.star | cut -b 200-300 | grep "  $j  "| wc -l 
    done > list_auto2d/list_$i
done
