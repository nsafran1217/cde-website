#!/bin/bash

set -e
mkdir -p output
cd xslt
python gen-articles.py
python gen-index.py
cd ..
python gen-sitemap.py

echo "Copying to ./output/"

cp -a blog output/
cp -a css output/
cp -a img output/
cp -a computers output/
cp -a projects output/
cp -a index.html output/
cp -a robots.txt output/
cp -a sitemap.xml output/

echo "DONE"