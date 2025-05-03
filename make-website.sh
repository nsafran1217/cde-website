#!/bin/bash

set -e
mkdir -p OUTPUT
cd xslt
python gen-articles.py
python gen-index.py
cd ..
python gen-sitemap.py

echo "Copying to ./OUTPUT/"

cp -a blog OUTPUT/
cp -a css OUTPUT/
cp -a img OUTPUT/
cp -a computers OUTPUT/
cp -a projects OUTPUT/
cp index.html OUTPUT/
cp robots.txt OUTPUT/
cp sitemap.xml OUTPUT/
cp CNAME OUTPUT/

echo "DONE"