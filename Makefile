# make-tut.pdf: make-tut.Rmd preamble.sty
# 	Rscript -e 'rmarkdown::render("$<", "pdf_document")'


make-tut.pdf: make-tut.Rnw v1-R/darts.pdf
	Rscript -e 'knitr::knit2pdf("$<")'


v1-R/darts.pdf:
	cd v1-R; make -fMakefile1 darts.pdf

