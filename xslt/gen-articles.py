import os
import subprocess
from datetime import datetime
import re
from xml.etree import ElementTree as ET

# Define the directories
input_dirs = ["projects", "computers", "blog"]
output_base_dir = "../"

# Ensure the output base directory exists
# os.makedirs(output_base_dir, exist_ok=True)
#############################################
# Walk through the current working directory to find and update .xml files
# Update the date in each xml file, taken from git log
for root, _, files in os.walk("."):
    for file in files:
        if file.endswith(".xml"):
            file_path = os.path.join(root, file)
            print(f"Updating {file_path}")
            
            # Get the last modified date of the file from git
            try:
                git_date = subprocess.check_output(
                    ["git", "log", "-1", "--format=%cd", "--date=format:%d-%b-%Y", file_path],
                    universal_newlines=True
                ).strip()
            except subprocess.CalledProcessError:
                print(f"Could not retrieve git date for {file_path}, skipping.")
                continue
            
            # Read the file content
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Replace the existing date in the format "Last Updated: DD-MMM-YYYY"
            updated_content = re.sub(
                r"Last Updated: \d{2}-[A-Za-z]{3}-\d{4}",
                f"Last Updated: {git_date}",
                content
            )
            
            # Write the updated content back to the file
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(updated_content)
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
                #subprocess.run(["xsltproc", "article.xslt", input_file, "-o", output_file], check=True)
                subprocess.run(['xsltproc', '-o', output_file, 'article.xslt', input_file], check=True)

