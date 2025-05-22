#!/bin/bash


mkdir -p OUTPUT
cd OUTPUT
rm -rf blog
rm -rf computer
rm-rf projects
rm index.html
rm sitemap.xml
cd ..
set -e


cd src
./gen-blog.sh
cd content
python ../gen-articles.py
python ../gen-index.py
cd ../../OUTPUT
python ../gen-sitemap.py


echo "DONE"