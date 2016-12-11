import os


pages = [
    'index',
    'chapter1',
    'chapter2',
    'chapter3',
    'chapter4',
    'chapter5',
    'chapter6',
]


for page in pages:
    os.system("pandoc {0}.md -s -o {0}.html".format(page))
