import os
from datetime import datetime
import re
import subprocess


output_base_dir = "../../OUTPUT/"
# Define the directories
blog_dir = "./blog"
spotlight_path = "../templates/blogspotlight.xml"

print("Getting all blog entries from markdown files")
# List to store blog entries with their published dates
blog_entries = []

# Scan the blog folder for markdown files
for root_dir, _, files in os.walk(blog_dir):
    for file in files:
        if file.endswith(".md"):  # Process only markdown files
            file_path = os.path.join(root_dir, file)
            print(f"Processing file: {file}")
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()

                # Extract the title (first line) and date (second line)
                title = lines[0].strip("# ").strip()
                date_line = lines[1].strip()
                match = re.search(r"Published: (\d{2}-[A-Za-z]{3}-\d{4})", date_line)
                if match:
                    date_str = match.group(1)
                    published_date = datetime.strptime(date_str, "%d-%b-%Y")

                    # Extract the first paragraph (content after the date)
                    content = ""
                    for line in lines[2:]:
                        if line.strip():  # Skip empty lines
                            content = line.strip()
                            break

                    # Add the entry to the list
                    blog_entries.append((published_date, file_path, content, title))
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

# Sort the blog entries by date (most recent first) and take the top 5
blog_entries = sorted(blog_entries, key=lambda x: x[0], reverse=True)[:5]

print("Generating blogspotlight.xml")
# Write the blogspotlight.xml file
with open(spotlight_path, "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<blogspotlight>\n    <content>\n')
    f.write('    <h2>Recent Blog Articles</h2>\n')
    for date, file_path, snippet, title in blog_entries:
        filename = os.path.splitext(os.path.basename(file_path))[0]
        f.write(f'        <hr></hr>\n<p><a href="/blog/{filename}.html"><span style="font-weight: bold;">{title}</span> - {date.strftime("%d-%b-%Y")}</a><br></br>\n')
        f.write(f'        {snippet}...</p>\n')
    f.write('    <hr></hr>\n')
    f.write('    <a href="/blog/index.html"><h3>All blog articles</h3></a>\n')
    f.write('    </content>\n</blogspotlight>\n')

print("blogspotlight.xml generated successfully.")

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
subprocess.run(['xsltproc', '-o', output_file, '../templates/home.xslt', input_file], check=True)
#############################################
