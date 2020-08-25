args <- commandArgs(TRUE)

darts_file = args[1]
inside_file = args[2]
estimate_file = args[3]
output_file = args[4]

xy <- read.table(darts_file, header=F)
inside <- scan(inside_file, what=logical(), quiet=TRUE)
estimate <- scan(estimate_file, quiet=TRUE)

pdf(file=output_file)
plot(xy, asp=1, pch=20, bty='n',
     xaxt="n", yaxt="n", xlab="", ylab="",
     col=ifelse(inside, "blue", "red"))
symbols(x=0, y=0, circles=1, inches=FALSE, add=TRUE)
symbols(x=0, y=0, squares=2, inches=FALSE, add=TRUE)
title(main=sprintf("Estimate of pi: %s", estimate))
invisible(dev.off())





