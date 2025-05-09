import os
import subprocess
from datetime import datetime
import re
from xml.etree import ElementTree as ET

# Define the directories

output_base_dir = "../OUTPUT/"

##################################################
# New functionality: Generate blogspotlight.xml

print("Getting all blog entries")
# List to store blog entries with their published dates
blog_entries = []

# If a blog is not being processed, check the first <p> has text and not just an HTML tag
# Scan the blog folder for XML files
blog_dir = "./blog"
for root_dir, _, files in os.walk(blog_dir):  # Renamed 'root' to 'root_dir'
    print(f"Total blog entries found: {len(files)}")
    for file in files:
        print(f"Processing {file}")
        if file.endswith(".xml") and file != "index.xml" and file != "about.xml":  # Skip index.xml
            file_path = os.path.join(root_dir, file)
            try:
                # Parse the XML file
                tree = ET.parse(file_path)
                xml_root = tree.getroot()  # Renamed 'root' to 'xml_root'

                # Find all <span> elements and check their text for "Published:"
                published_date = None
                for span in xml_root.findall(".//span"):
                    if span.text and "Published:" in span.text:
                        # Extract the date from the "Published: DD-MMM-YYYY" format
                        match = re.search(r"Published: (\d{2}-[A-Za-z]{3}-\d{4})", span.text)
                        if match:
                            date_str = match.group(1)
                            published_date = datetime.strptime(date_str, "%d-%b-%Y")
                            break
                blogtitle = xml_root.find(".//title").text.replace("nsafran.com - ", "")
                if published_date:
                    # Extract the first <p> tag content inside <content>
                    content_element = xml_root.find(".//content")
                    if content_element is not None:
                        first_p = content_element.find(".//p")
                        if first_p is not None and first_p.text:
                            # Include text content and strip HTML tags
                            content_snippet = ''.join(ET.tostring(first_p, encoding='unicode', method='text')).strip()[:300]

                            # Add to the list of blog entries
                            blog_entries.append((published_date, file_path, content_snippet, blogtitle))
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

print("Generating blog/index.xml")
####################### 
# write blog/index.html, all blog entries
# get the blogs
print(f"Total blog entries found: {len(blog_entries)}")
blog_entries = sorted(blog_entries, key=lambda x: x[0], reverse=True)

#open the file and write out the full xml file, loop through all blog entires and insert into the xml
with open("blog/index.xml", "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<page theme="default">\n<title>nsafran.com - All Blog Entires</title>\n')
    f.write('<sections><section><window-title>Terminal - All Blog Entries</window-title>\n<content>\n')
    f.write('    <h2>All Blog Entries by Date</h2>\n')
    for date, file_path, snippet, blogtitle in blog_entries:
        print("Processing blog entry:", file_path)
        filename = os.path.splitext(os.path.basename(file_path))[0]
        f.write(f'    <hr></hr>\n<p><a href="/blog/{filename}.html"><span style="font-weight: bold;">{blogtitle}</span> - {date.strftime("%d-%b-%Y")}</a><br></br>\n')
        f.write(f'    {snippet}...</p>\n')
    f.write('    <hr></hr>\n')
    f.write('</content></section></sections></page>')


print("blog/index.xml generated successfully.")
print("Generating blogspotlight.xml")
# Sort the blog entries by date (most recent first) and take the top 5
blog_entries = sorted(blog_entries, key=lambda x: x[0], reverse=True)[:5]
##########
# Write the blogspotlight.xml file
#open the file and write out the full xml file, loop through all blog entires and insert the 5 into the xml
spotlight_path = "blogspotlight.xml"
with open(spotlight_path, "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<blogspotlight>\n    <content>\n')
    f.write('    <h2>Recent Blog Articles</h2>\n')
    for date, file_path, snippet, blogtitle in blog_entries:
        filename = os.path.splitext(os.path.basename(file_path))[0]
        
        f.write(f'        <hr></hr>\n<p><a href="/blog/{filename}.html"><span style="font-weight: bold;">{blogtitle}</span> - {date.strftime("%d-%b-%Y")}</a><br></br>\n')
        f.write(f'        {snippet}...</p>\n')
    f.write('    <hr></hr>\n')
    f.write('    <a href="/blog/index.html"><h3>All blog articles</h3></a>\n')
    f.write('    </content>\n</blogspotlight>\n')

print("blogspotlight.xml generated successfully.")
############################################


############################################
# Generate index.html
print("Processing index.xml")    
file = "index.xml"
input_dir = "."
input_file = "./index.xml"
output_dir = os.path.join(output_base_dir, input_dir)
output_file = os.path.join(output_dir, file.replace(".xml", ".html"))
print(f"Processing {input_file} to {output_file}")
# Run xsltproc
#subprocess.run(["xsltproc", "article.xslt", input_file, "-o", output_file], check=True)
subprocess.run(['xsltproc', '-o', output_file, 'home.xslt', input_file], check=True)
#############################################
