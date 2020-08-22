.PHONY: clean all

all: darts.pdf

darts.xy: inputs.dat
	python throw-darts.py inputs.dat > darts.xy

inside.out: darts.xy
	python count-inside.py darts.xy > inside.out

pi.est: inside.out
	python estimate.py inside.out > pi.est



darts.pdf: darts.xy inside.out pi.est
	python draw-figure.py darts.xy inside.out pi.est darts.pdf


clean:
	rm -f darts.xy inside.out pi.est darts.pdf
