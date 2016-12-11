import os

os.system("pandoc chapter1.md -s -o chapter1.html")
os.system("pandoc index.md -s -o index.html")
