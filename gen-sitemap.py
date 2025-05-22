import os
from datetime import datetime

# Define the base URL of your website
BASE_URL = "https://nsafran.com"

# Define the folder to exclude
EXCLUDE_FOLDER = "xslt"

# Define the output file
OUTPUT_FILE = "./sitemap.xml"

def generate_sitemap():
    # List to store sitemap entries
    sitemap_entries = []

    # Walk through the root folder and subfolders
    for root, _, files in os.walk("./"):
        # Skip the excluded folder
        if EXCLUDE_FOLDER in root:
            continue

        for file in files:
            # Include only .html files
            if file.endswith(".html"):
                # Get the relative path of the file
                relative_path = os.path.relpath(os.path.join(root, file), ".")
                # Convert Windows backslashes to forward slashes for URLs
                url_path = relative_path.replace("\\", "/")
                # Get the last modified time of the file
                last_modified = datetime.fromtimestamp(os.path.getmtime(os.path.join(root, file))).strftime("%Y-%m-%d")
                # Add the entry to the sitemap
                sitemap_entries.append(f"  <url>\n    <loc>{BASE_URL}/{url_path}</loc>\n    <lastmod>{last_modified}</lastmod>\n  </url>")

    # Write the sitemap to the output file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        f.write("\n".join(sitemap_entries))
        f.write('\n</urlset>')

    print(f"Sitemap generated: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_sitemap()