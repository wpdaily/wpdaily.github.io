import os
import csv
import markdown  # pip install markdown

# Get the directory of this script
script_directory = os.path.dirname(os.path.realpath(__file__))

# Get the list of files in the directory
files = os.listdir(script_directory + '/../md/')

# Sort the files in descending order
files.sort(reverse=True)

# Check if script_directory + '/html/somename.html' dir exists
html_directory = script_directory + '/../md/html/'
if not os.path.exists(html_directory):
    os.makedirs(html_directory)

result_dict = {}

# Convert markdown files to HTML
for file_name in files:
    md_file_path = script_directory + '/../md/' + file_name

    # Skip if it's a directory
    if os.path.isdir(md_file_path):
        continue

    html_file_path = html_directory + file_name.replace('.md', '.html')

    with open(md_file_path, 'r') as md_file:
        temp_md = md_file.read()

    # Convert the input to HTML
    temp_html = markdown.markdown(temp_md)

    # Write the HTML output to a file
    with open(html_file_path, 'w') as html_file:
        html_file.write(temp_html)

    result_dict[file_name] = temp_html

# Create a CSV file export.csv
csv_file_path = script_directory + '/../md/html/dump.csv'
with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['title', 'body'])

    for file_name, html_content in result_dict.items():
        escaped_html = html_content.replace('"', '""')
        writer.writerow([file_name.replace(".md", ""), escaped_html])
