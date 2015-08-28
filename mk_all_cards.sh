cd /nfs/dust/cms/user/hmildner/CMSSW_7_4_4_patch4/src 
cmsenv
cd -
for i in '' _6j2t _4j3t _5j3t _6j3t _4j4t _5j4t _6j4t
do
    mk_datacard_ttbb -d BDT -o datacard${i}.txt  new_bdts${i}.root
done
