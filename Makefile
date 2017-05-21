DOCSDIR := docs
DOCSIMGDIR := $(DOCSDIR)/images
NBS = $(wildcard *.ipynb)
# HTML := $(addprefix $(DOCSDIR)/, index.html)
HTML = $(patsubst %.ipynb, %.html, $(NBS))
HTMLDOCS = $(patsubst %.html, docs/%.html, $(HTML))

all: $(DOCSDIR) $(DOCSIMGDIR) $(HTML) $(HTMLDOCS) index readme


$(DOCSDIR):
	mkdir $(DOCSDIR)

%.html: %.ipynb
	# echo $< $@
	jupyter nbconvert --to html $<
	mv $@ docs/$@

# docs/%.html: %.html Makefile
	# mv $< $@

index: docs/index.md docs/book.css
	pandoc docs/index.md -o docs/index.html -c book.css

readme: README.md docs/book.css
	pandoc README.md -o docs/readme.html -c book.css
