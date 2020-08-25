#!/bin/env Rscript
args <- commandArgs(TRUE)

stopifnot(length(args)==1)
inputfile = args[1]
source(inputfile)

x = runif(n, -1, 1)
y = runif(n, -1, 1)

xy = cbind(x,y)

write(xy, ncolumns=2, file="")
