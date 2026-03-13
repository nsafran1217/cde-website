#!/bin/bash

set -e

cd content


# Loop through all .md files and extract the date
for file in `find . -name *.md`; do
    # Extract the title
    title=$(grep -m 1 '^# ' "$file" | sed 's/^# //')


    # Identify theme based on parent directory
    parentdir=$(basename $(dirname "$file"))
    case $parentdir in 
        sgi)
            theme=$parentdir
            termtitle="winterm"
            ;;
        hp)
            theme=$parentdir
            termtitle="hpterm"
            ;;
        dec)
            theme=$parentdir
            termtitle="DECterm"
            ;;
        ibm)
            theme=$parentdir
            termtitle="dtterm"
            ;;
        sun)
            theme=$parentdir
            termtitle="Terminal"
            ;;
        *)
            theme="default"
            termtitle="Terminal"
            ;;
    esac

    #$file replace .md with .xml
    xmlfile="${file%.md}.xml"

    
    # Generate the XML file
    cat header.x > $xmlfile
    markdown "$file" >> $xmlfile
    cat footer.x >> $xmlfile


    #replace theme
    sed -i "s/@THEME@/$theme/" $xmlfile

    # Replace @TITLE@ in the XML file with the extracted title
    sed -i "s/@TITLE@/$title/" $xmlfile

    # Replace each remaining <h2> with a window-break section + <h2>
    sed -i 's|<h2[^>]*>\(.*\)</h2>|</content></section>\n<section><window-title>@TERMTITLE@ - \1</window-title>\n<content>\n<h2>\1</h2>|' $xmlfile

    # replace termtitle
    sed -i "s/@TERMTITLE@/$termtitle/" $xmlfile
    
done