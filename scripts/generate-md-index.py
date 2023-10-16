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
    f.write("# 白纸行动日报 White Paper Daily\n\n"
            "抗议行动的每日简要整理，关注即是力量。\n\n"
            "- Mastodon: [@whitepaperdaily@mstdn.social](https://mstdn.social/@whitepaperdaily)\n"
            "- 网站: [https://whitepaperdaily.wordpress.com](https://whitepaperdaily.wordpress.com/)\n"
            "- Git: [GitHub](https://github.com/wpdaily/white-paper-daily/)\n"
            "- 投稿: [CryptPad](https://cryptpad.fr/form/#/2/form/view/cte4PXjIT6AxP-9V+mpEd6708q57aGYip+tuK7tr+FE/)\n"
            "\n\n"
            "# 目录\n\n")
    for link in hyperlinks:
        f.write(f"{link}\n\n")
