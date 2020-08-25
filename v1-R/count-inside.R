#!/bin/env Rscript
args <- commandArgs(TRUE)

darts = args[1]
xy = read.table(darts, header=F)
x = xy[,1]
y = xy[,2]
r2 = 1 * 1  # radius of 1
inside = (x^2) + (y^2) < r2
write(inside, '', ncol=1)




