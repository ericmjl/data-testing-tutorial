import os

files = [
    'index',
    'chapter1',
    'chapter2',
    'chapter3',
    'chapter4',
    'chapter5',
    'chapter6',
]

for f in files:
    os.system('pandoc {0}.md -s -H book.css -o {0}.html'.format(f))

os.system('git add .')
os.system('git commit -m "updated pages"')
os.system('git push')
