for i in _4j3t _4j4t _5j3t  _5j4t  _6j2t  _6j3t _6j4t ''
do
    combine -M Asymptotic -m 125 --minosAlgo stepping datacard${i}.txt --run="blind"
done
