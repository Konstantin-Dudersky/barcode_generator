#!/bin/bash

# setup file for barcode_generator - https://github.com/Konstantin-Dudersky/barcode_generator
# can be removed after installation

echo
echo "-----> Upgrading system:"
sudo apt -y update
sudo apt -y upgrade

echo
echo "-----> Install software:"
sudo apt -y install ghostscript curl

echo
echo "-----> Install poetry:"
sudo apt -y install python3-distutils
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
# shellcheck disable=SC1090
source ~/.poetry/env
poetry config virtualenvs.in-project true

echo
echo "-----> Download source code:"
wget https://github.com/Konstantin-Dudersky/barcode_generator/tarball/master
mkdir barcode_generator
tar -xf master --strip-components 1 -C barcode_generator
rm master

echo
echo "-----> Install packages:"
cd barcode_generator || exit
poetry install
cd ..

echo
echo "-----> Copy files:"
cd barcode_generator || exit
cp example.config.yaml config.yaml
cp example.input.csv input.csv
cd ..

echo
echo "-----> Make executable:"
chmod +x barcode_generator/start.sh

echo
echo "-----> Installation complete!"