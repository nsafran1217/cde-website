import os
import subprocess
from datetime import datetime
import re
from xml.etree import ElementTree as ET

# Define the directories
input_dirs = ["projects", "computers", "blog"]
output_base_dir = "../"

##################################################
# New functionality: Generate blogspotlight.xml
print("Generating blogspotlight.xml")

# List to store blog entries with their published dates
blog_entries = []

# Scan the blog folder for XML files
blog_dir = "blog"
for root_dir, _, files in os.walk(blog_dir):  # Renamed 'root' to 'root_dir'
    for file in files:
        if file.endswith(".xml"):
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

                if published_date:
                    # Extract the first 300 characters of <content>, ignoring <h2> and <span>
                    content_element = xml_root.find(".//content")
                    if content_element is not None:
                        content = ET.tostring(content_element, encoding="unicode", method="text")
                        content = re.sub(r"<(h2|span)[^>]*>.*?</\1>", "", content, flags=re.DOTALL)  # Remove <h2> and <span>
                        content = re.sub(r"<[^>]+>", "", content)  # Strip all HTML tags
                        content_snippet = content[:300].strip()

                        # Add to the list of blog entries
                        blog_entries.append((published_date, file_path, content_snippet))
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

# Sort the blog entries by date (most recent first) and take the top 5
blog_entries = sorted(blog_entries, key=lambda x: x[0], reverse=True)[:5]
##########
# Write the blogspotlight.xml file
spotlight_path = "blogspotlight.xml"
with open(spotlight_path, "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<blogspotlight>\n    <content>\n')
    f.write('    <h2>Recent Blog Articles</h2>\n')
    for date, file_path, snippet in blog_entries:
        title = os.path.splitext(os.path.basename(file_path))[0].replace("nsafran.com - ", "")
        f.write(f'        <p><span style="font-style: bold;">{title}</span> - Published: {date.strftime("%d-%b-%Y")}</p>')
        f.write(f'        <p>{snippet}...</p>\n')
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
