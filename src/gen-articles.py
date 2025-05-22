import os
import subprocess
import re
from xml.etree import ElementTree as ET

# Define the directories
input_dirs = ["projects", "computers", "blog"]
output_base_dir = "../../OUTPUT/"

# Ensure the output base directory exists
# os.makedirs(output_base_dir, exist_ok=True)
#############################################

#############################################
# Process each input directory
# Generate HTML files for articles
for input_dir in input_dirs:
    for root, _, files in os.walk(input_dir):
        # Calculate the relative path and corresponding output directory
        relative_path = os.path.relpath(root, input_dir)
        output_dir = os.path.join(output_base_dir, input_dir, relative_path)
        os.makedirs(output_dir, exist_ok=True)

        # Process each XML file
        for file in files:
            if file.endswith(".xml"):
                input_file = os.path.join(root, file)
                output_file = os.path.join(output_dir, file.replace(".xml", ".html"))
                print(f"Processing {input_file} to {output_file}")
                # Run xsltproc
                subprocess.run(['xsltproc', '-o', output_file, '../templates/article.xslt', input_file], check=True)

