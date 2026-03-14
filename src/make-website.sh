#!/bin/bash


mkdir -p OUTPUT
cd OUTPUT
rm -rf blog
rm -rf computer
rm -rf projects
rm index.html
rm sitemap.xml
cd ..
set -e


cd src
echo "GEN XML"
./gen-xml-from-md.sh
echo "GEN index for blogs"
./gen-blog-index.sh

cd content
echo "GEN articles from xml"
python ../gen-articles.py
echo "GEN home page"
python ../gen-index.py
cd ../../OUTPUT
python ../gen-sitemap.py


echo "DONE"