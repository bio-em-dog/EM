#!/usr/bin/env bash

IFS='
'
mkdir star
for i in {1..100}
    do cat run_it025_data.star | head -n 21 > star/ex$i.star
    for LINE in `cat run_it025_data.star`; 
        do echo $LINE | cut -b 220-280 | grep " $i " && echo $LINE >> star/ex$i.star
    done
done

#while read LINE; do echo $LINE;done < run_it025_data.star
