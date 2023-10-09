import os

# Get the directory of this script
script_directory = os.path.dirname(os.path.realpath(__file__))

# Get the list of files in the directory
files = os.listdir(script_directory + '/../md/')

# Sort the files in descending order
files.sort(reverse=True)

# Now we generate the list of hyperlinks

hyperlinks = []

for file in files:
    # We assume that the files are markdown files
    # If they have other file extensions, change .md to the correct extension
    if file.endswith('.md'):
        filename = file.split('.')[0]
        link = f"[{filename}](md/{file})"
        hyperlinks.append(link)

# Now we write the hyperlinks to the readme file

with open(script_directory + '/../readme.md', 'w') as f:
    f.write("# 白纸行动日报 White Paper Daily\n\n")
    for link in hyperlinks:
        f.write(f"{link}\n\n")
