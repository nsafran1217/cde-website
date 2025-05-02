import os
import subprocess
from datetime import datetime

# Define the directories
input_dirs = ["projects", "computers", "blog"]
output_base_dir = "../"

# Ensure the output base directory exists
# os.makedirs(output_base_dir, exist_ok=True)

# Process each input directory
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

print("Processing index.xml")    
file = "index.xml"
input_dir = "."
input_file = "./index.xml"
output_dir = os.path.join(output_base_dir, input_dir, relative_path)
output_file = os.path.join(output_dir, file.replace(".xml", ".html"))
print(f"Processing {input_file} to {output_file}")
# Run xsltproc
#subprocess.run(["xsltproc", "article.xslt", input_file, "-o", output_file], check=True)
subprocess.run(['xsltproc', '-o', output_file, 'home.xslt', input_file], check=True)


# Walk through the output base directory to find and update .html files
for root, _, files in os.walk(output_base_dir):
    for file in files:
        if file.endswith(".html"):
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
            
            # Replace the placeholder with the git last modified date
            updated_content = content.replace("%%UPDATEDATE%%", git_date)
            
            # Write the updated content back to the file
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(updated_content)