# First Excercise: Risk and Uncertainty
# Patricia Pérez

# Function
concentration <- function(time)
{
  # Theta 2 and 3 are constant
  theta2 <- 2
  theta3 <- 1
  # Uniform distribution for theta 1
  a = 80 # Lim inferior
  b = 90 # Lim superior
  theta1 <- runif(1000, min = a, max = b)
  (theta1) / (((time / theta2)+1)^ theta3)
}

# Defining two time steps
# time.1 <- 10
# time.2 <- 100
times <- list(10,100)
for (x in times){
  # Concentration
  concentration(x)
  # Cumulative distribution function
  cfd <- ecdf(concentration(x))
  plot(cfd)
  # Confidence intervals calculation
  interval <- 0.05 * (max(concentration(x)) - min(concentration(x)))
  max_conf <- max(concentration(x)) - interval
  min_conf <- min(concentration(x)) + interval
  new_interval <- c(max_conf, min_conf)
  m <- matrix(c(new_interval, x), ncol = 3, nrow = 1)
  colnames(m) <- (c("max conf.", "min conf.", "time"))
  print(m)
  #legend(c(max_conf, min_conf, x), c("max conf.", "min conf.", "time"))
}
