#!/bin/sh
./throw-darts inputs.dat > darts.txt
./count-inside darts.txt > inside.out
./estimate inside.out > pi.est
./draw-figure darts.txt inside.out pi.est output.pdf

