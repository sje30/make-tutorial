# Tell Emacs this is a  -*- Makefile -*-_

.PHONY: all clean

REPEATS := $(shell seq 1 15)

TARGETS := $(patsubst %, pi-%.est, $(REPEATS))

all: $(TARGETS)

darts-%.xy: inputs.dat
	Rscript throw-darts.R inputs.dat > $@

inside-%.out: darts-%.xy
	Rscript count-inside.R $^ > $@


pi-%.est: inside-%.out
	Rscript estimate.R $^ > $@

distribution.pdf: $(TARGETS) plot-distribution.R
	Rscript plot-distribution.R $(TARGETS)

# https://blog.jgc.org/2015/04/the-one-line-you-should-add-to-every.html
print-%: ; @echo $*=$($*)


clean:
	rm -f $(TARGETS)
