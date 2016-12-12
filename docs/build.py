import os

# Write an automatic index.
index = '\
# Data Testing Tutorial\n\
\n\
## Table of Contents\n\
'

files = [
    'index',
    'chapter1',
    'chapter2',
    'chapter3',
    'chapter4',
    'chapter5',
    'chapter6',
]

with open('index.md', 'w+') as f:
    f.write(index)
    for fname in files:
        if fname != 'index':
            f.write('[{0}](./{0})\n'.format(fname))


for f in files:
    os.system('pandoc {0}.md -s -H book.css -o {0}.html'.format(f))


os.system('git add .')
os.system('git commit -m "updated pages"')
os.system('git push')
