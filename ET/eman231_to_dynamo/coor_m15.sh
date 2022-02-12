for i in {29..32};do
cat bak/p${i}_full_info.json.bak | sed 's/\[\[/\[\n\[/g' | grep tm > coor${i}
python coor_m15.py coor${i} > ncoor${i}
cat h ncoor${i} t > p${i}_full_info.json
rm coor${i} ncoor${i}
done
