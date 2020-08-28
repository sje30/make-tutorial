## Plot the distribution of estimates for pi.

args <- commandArgs(TRUE)

## Read in all the estimates of pi

estimates <- c()

for (file in args) {
  this_estimate <- scan(file)
  estimates <- c(estimates, this_estimate)
}


pdf(file="distribution.pdf")
stripchart(estimates,vertical=TRUE,pch=19,
           ##bty='n',
           method='jitter', ylab='Estimates of pi')

abline(h=pi, col='green')
dev.off()
