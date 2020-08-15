.PHONY: clean all

all: darts.pdf

darts.xy: inputs.dat
	./throw-darts inputs.dat > darts.xy

inside.out: darts.xy
	./count-inside darts.xy > inside.out

pi.est: inside.out
	./estimate inside.out > pi.est



darts.pdf: darts.xy inside.out pi.est
	./draw-figure darts.xy inside.out pi.est darts.pdf


clean:
	rm -f darts.xy inside.out pi.est darts.pdf



## This depends on https://github.com/lindenb/makefile2graph

graph.pdf: Makefile
	make -Bnd | makefile2graph | dot -Tpdf > graph.pdf

