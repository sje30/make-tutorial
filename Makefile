make-tut.pdf: make-tut.Rmd preamble.sty
	Rscript -e 'rmarkdown::render("$<", "pdf_document")'
