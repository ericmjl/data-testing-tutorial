import os


def getfiles(extension):
    return [f for f in os.listdir() if f.endswith(extension)]

def writefile(handle, string):
    with open(handle, 'w+') as f:
        f.write(string)


# Convert Jupyter notebooks to HTML
files = getfiles('.ipynb')
for f in files:
    os.system(f"jupyter nbconvert --to html {f}")

# Move notebooks to docs/
os.system('mv *.html docs/.')

os.chdir('docs')

# Make index page.
header = """
---
title: Data Testing Tutorial
---

This contains static HTML versions of the Jupyter notebooks that I have made for this tutorial.

Files:
"""
for f in files:
    html_name = f.replace(".ipynb", ".html")
    header += f'- [{html_name}]({html_name})\n'

writefile('index.md', header)
