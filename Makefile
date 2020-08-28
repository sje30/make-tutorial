# make-tut.pdf: make-tut.Rmd preamble.sty
# 	Rscript -e 'rmarkdown::render("$<", "pdf_document")'


make-tut.pdf: make-tut.Rnw
	Rscript -e 'knitr::knit2pdf("$<")'
