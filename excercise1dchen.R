#define concentration function c, 
#a being rand unif between 80 and 90
# b and c are constant

library(ggplot2)

conc <- function(a, b, c, t){
  a <- runif(1000,80,90)
  b <-2
  c <- 1
  a/((t/b)+1)^c
}

#distribution at time t = 10
dist10 <- conc(t=10)
#conf int 
interval <- 0.05*(max(dist10) - min(dist10))
max10 <- max(dist10) - interval
min10 <- min(dist10) + interval

conf_int10 <- c(min10,max10)

#distribution at time t = 100
dist100 <- conc(t=100)
interval <- 0.05*(max(dist100) - min(dist100))
max100 <- max(dist100) - interval
min100 <- min(dist100) + interval
conf_int100 <- c(min100,max100)


