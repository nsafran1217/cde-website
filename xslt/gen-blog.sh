#!/bin/bash

set -e

cd blog

for file in *.md; do
    cat header.x > "${file%.md}.xml"
    markdown "$file" >> "${file%.md}.xml"
    cat footer.x >> "${file%.md}.xml"
done