#!/bin/bash

set -e
mkdir -p OUTPUT
cd xslt
python gen-articles.py
python gen-index.py
cd ..
python gen-sitemap.py


echo "DONE"