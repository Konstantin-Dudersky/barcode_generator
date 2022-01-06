echo
echo "-----> Upgrading system:"
sudo apt -y update
sudo apt -y upgrade

echo
echo "-----> Install software:"
sudo apt -y install ghostscript

echo
echo "-----> Install poetry:"
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
# shellcheck disable=SC1090
source ~/.poetry/env
poetry config virtualenvs.in-project true

chmod +x ../start.sh