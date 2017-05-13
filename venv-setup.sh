set -x
VENV="$(which virtualenv)"
if [ -z "$VENV" ]; then
   pip install virtualenv
fi
if [[ -d 'datatest' ]]; then
   rm -rf ./datatest
   echo 'xx';
fi
virtualenv datatest
source datatest/bin/activate && pip install -r requirements.txt
echo "Run 'source datatest/bin/activate' to begin"

python checkenv.py
