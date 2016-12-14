import os

# Write an automatic index.
index = '\
# Data Testing Tutorial\n\
\n\
This is the book version of the data testing tutorial that I am creating.\n\
\n\
## Table of Contents\n\
\n\
1. [Chapter 1 - Why Data Testing](./chapter1)\n\
1. [Chapter 2 - Introduction to Testing & Writing Tests for\
    Functions](./chapter2)\n\
1. [Chapter 3 - Checking File Integrity](./chapter3)\n\
1. [Chapter 4 - Checking Data Assumptions](./chapter4)\n\
1. [Chapter 5 - Code coverage](./chapter5)\n\
1. [Chapter 6 - Property-based testing](./chapter6)\n\
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

for f in files:
    os.system('pandoc {0}.md -s -H book.css -o {0}.html'.format(f))


os.system('git add .')
os.system('git commit')
os.system('git push')
