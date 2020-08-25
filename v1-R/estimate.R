args <- commandArgs(TRUE)
insidefile <- args[1]
inside <- scan(insidefile, what=logical(), quiet=TRUE)
n <- length(inside)
estimate <- 4*sum(inside)/n
cat(estimate,fill=TRUE)


