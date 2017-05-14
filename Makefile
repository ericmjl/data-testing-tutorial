NBS = $(wildcard *.ipynb)

html: $(NBS)
	jupyter nbconvert --to html $(NBS)
	mv *.html docs/.

	pandoc docs/index.md -o docs/index.html -css docs/book.css
