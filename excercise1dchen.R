#define concentration function c, 
#a being rand unif between 80 and 90
# b and c are constant

# library(ggplot2)
# 
# conc <- function(a, b, c, t){
#   a <- runif(1000,80,90)
#   b <-2
#   c <- 1
#   a/((t/b)+1)^c
# }
#   
# dist10 <- conc(t=10)
# dist100 <- conc(t=100)
# dist10_ci <-  quantile(ecdf(dist10), c(.025, .975))
# dist100_ci <-  quantile(ecdf(dist100), c(.025, .975))

# 
# cont_ci <- data.frame()
# for (i in t) {
#   cont_ci <- conc(t=i)
# }

conc <- function(a=85, b=2, c=1, t){
  if (a =="UD"){
    a <- runif(100000,80,90)}
  if (a == "ND"){
    a <- rnorm(100000,85,2.4)
  }
  else{ a <- 85}
  if (b == "UD") { 
    b<-runif(100000, 1, 2)
    }
  else { 
    b<-2 
    }
  if (c== "UD") {
    c <- runif(100000, 0.5,1.5)
  }
  else {
    c <- 1
  }
  a/((t/b)+1)^c
}

# df <- data.frame(t = seq(c(1:100))

conc_cUD <- conc(c="UD", t=10)
plot.ecdf(conc_cUD)


intervals <- function(t, a=85, b=2, c=1){
  dist <- conc(a, b, c, t)
  dist_ci <- quantile(ecdf(dist), c(0.25, .975))
}


allUD_ci <- intervals(a="UD", b="UD", c="UD", t=10)
tmp <- intervals(a="UD",t=10)
