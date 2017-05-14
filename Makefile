NBS = $(wildcard *.ipynb)

all: nbhtml index readme

nbhtml: $(NBS)
	jupyter nbconvert --to html $(NBS)
	mv *.html docs/.

index: docs/index.md docs/book.css
	pandoc docs/index.md -o docs/index.html -c book.css

readme: README.md docs/book.css
	pandoc README.md -o docs/readme.html -c book.css
