import os

from bs4 import BeautifulSoup
from jinja2 import Template
from xlsx2html import xlsx2html

# Get the directory of this script
script_directory = os.path.dirname(os.path.realpath(__file__))

# Define the source and destination directories
src_directory = script_directory + '/../excel/'
dst_directory = script_directory + '/../excel/html/'

# Get all the files in the source directory
files = os.listdir(src_directory)

# Prepare a list for storing file names
html_files = []

# Get HTML template header
with open(script_directory + '/../excel/html/template/single_h.html', 'r') as f:
    header = f.read()

# Get HTML template footer
with open(script_directory + '/../excel/html/template/single_f.html', 'r') as f:
    footer = f.read()

for file in files:
    # Check if the file is an Excel file
    if file.endswith('.xlsx') or file.endswith('.xls'):
        # Define source and destination paths for the file
        src_path = os.path.join(src_directory, file)
        html_filename = file.replace('.xlsx', '.html').replace('.xls', '.html')
        dst_path = os.path.join(dst_directory, html_filename)

        # Convert the source file to HTML and save it to the destination path
        xlsx2html(src_path, dst_path)

        # Load the created HTML file using BeautifulSoup
        with open(dst_path, 'r') as f:
            soup = BeautifulSoup(f, 'html.parser')

        # Remove all attributes from all elements
        for tag in soup.findAll(True):
            tag.attrs = {}

        # Set page title to filename
        soup.title.string = html_filename.replace('.html', '')

        # Add char set and viewport meta tags
        soup.head.append(BeautifulSoup('<meta charset="UTF-8">', 'html.parser'))
        soup.head.append(
            BeautifulSoup('<meta name="viewport" content="width=device-width, initial-scale=1.0">', 'html.parser'))

        # Add css
        soup.head.append(BeautifulSoup('<link rel="stylesheet" href="css/style.css">', 'html.parser'))

        # Save the cleaned HTML back to the file
        with open(dst_path, 'w') as f:
            f.write(str(soup))

        # Append HTML file name to the list
        html_files.append(html_filename)

# Sort the HTML files in descending order
html_files.sort(reverse=True)

# Prepare data for rendering
data = [{'filename': f.split('.')[0], 'link': f} for f in html_files]

index_template = header + \
                 '''
                     <h1>白纸行动日报 White Paper Daily</h1>
                     <ul class="meta">
                     </ul>
                     <ul>
                     {% for item in data %}
                         <li><a href="{{ item.link }}">{{ item.filename }}</a></li>
                     {% endfor %}
                     </ul>
                 ''' \
                 + footer

# Prepare the HTML template
template = Template(index_template)

# Render the template with the data
rendered_html = template.render(data=data)

# Write the rendered HTML to the index.html file
with open(script_directory + '/../excel/html/index.html', 'w') as f:
    f.write(rendered_html)
