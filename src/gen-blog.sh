#!/bin/bash

set -e

cd content/blog
cat index_head.x > index.xml

# Loop through all .md files and extract the date
for file in `ls *.md | sort -r`; do
    # Extract the title
    title=$(grep -m 1 '^# ' "$file" | sed 's/^# //')
    # Extract the date from the second line
    date=$(sed -n 's/^\*Published: \(.*\) - Last Updated: .*$/\1/p' "$file")

    # Strip off the "000-" prefix from the URL
    url=$(basename "$file" .md | sed 's/^[0-9]\{3\}-//').html
    url=$(basename "$file" .md).html
    
    # Generate the XML file
    cat header.x > "${url%.html}.xml"
    markdown "$file" >> "${url%.html}.xml"
    cat footer.x >> "${url%.html}.xml"

    # Replace @TITLE@ in the XML file with the extracted title
    sed -i "s/@TITLE@/$title/" "${url%.html}.xml"

    # Append the information to the temporary file
    
    echo "<tr><td><a href=\"$url\">$title</a></td><td>$date</td></tr>" >> index.xml
    
done

echo "</table></content></section></sections></page>" >> index.xml
