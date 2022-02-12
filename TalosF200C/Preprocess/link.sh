# 2021.12.30 JXD
# continually link Movies from StotageServer to working "Micrographs" dirctory
# bash link.sh Supervisor_20220120_145529

if [ $# -ne 1 ]; then
echo "USAGE: bash $0 <raw_movies_folder>"
exit 1;
fi

[[ -e Micrographs ]] || mkdir Micrographs
cd Micrographs

while true ;do
a=`ls *mrc 2> /dev/null | wc -l `
ln -s /run/user/1000/gvfs/smb-share\:server\=winstorageserve\,share\=offloaddata/$1/Images-Disc1/GridSquare_*/Data/*mrc . 2> /dev/null
b=`ls *mrc | wc -l`
echo "`echo "$b-$a" | bc` new movies"
sleep 60
done

cd ..
