set -ex
wget https://github.com/ericmjl/conda-envs/raw/master/data_test.yml -O environment.yml
conda env update -f environment.yml
