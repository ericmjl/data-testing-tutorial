set -ex
conda env create -f environment.yml
source activate datatest
python checkenv.py
