# usage: copy this script in folder with datacard and source rename_cards.sh

for i in *hdecay*txt; do cp $i ttH_hbb_13TeV_sl_${i#76xBDToptionD_datacard_ljets_}; done
for i in ttH_hbb_13TeV*txt; do mv $i ${i%_hdecay.txt}.txt; done
mkdir common
cp 76xBDToptionD_limitInput.root common/ttH_hbb_13TeV_sl.root 
sed -i 's-76xBDToptionD/76xBDToptionD_limitInput.root-common/ttH_hbb_13TeV_sl.root-g' ttH_hbb_13TeV*txt
mkdir finalcards
mv common finalcards/
mv ttH_hbb_13TeV*txt finalcards/
mv finalcards/76xBDToptionD_datacard_hdecay.txt finalcards/ttH_hbb_13TeV_sl.txt