#!/bin/bash

set -e

cd content/blog
cat index_head.x > index.xml

# Loop through all .md files and extract the date
for file in `ls *.md | sort -r`; do
    # Extract the title
    sed -i "s|@TITLE@|$title|" $file
    # Extract the date from the second line
    date=$(sed -n 's/^\*Published: \(.*\) - Last Updated: .*$/\1/p' "$file")

    url=$(basename "$file" .md).html

    # Append the information to the temporary file
    
    echo "<tr><td><a href=\"$url\">$title</a></td><td>$date</td></tr>" >> index.xml
    
done

echo "</table></content></section></sections></page>" >> index.xml
