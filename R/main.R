hypot <- function(z) {
  1/(1+exp(-z))
}

gCost <- function(t,X,y) {
  1/nrow(X)*(t(X)%*%(hypot(X%*%t)-y))
}

heart <- function(path){
  data <- as.matrix(read.table(path))
  
  index <- seq(1,nrow(data)*0.2)
  X_test <- cbind(1,scale(data[index,1:ncol(data)-1],center=F))
  y_test <- as.matrix(data[index,ncol(data)])
  X_train <- cbind(1,scale(data[-index,1:ncol(data)-1],center=F))
  y_train <- as.matrix(data[-index,ncol(data)])
    
  theta <- as.matrix(rep(0,ncol(data)))
  
  alpha <- 0.3
  tol <- 1e-6
  step <- 1
  while(T) {
    p_gradient <- gCost(theta,X_train,y_train)
    theta <- theta-alpha*p_gradient
    gradient <- gCost(theta,X_train,y_train)
    if(abs(norm(gradient,type="F")-norm(p_gradient,type="F"))<=tol) break
    step <- step+1
  }
  
  y_pred <- hypot(X_test%*%theta)
  result <- xor(as.vector(round(y_pred)),as.vector(y_test))
  corrects = length(result[result==F])
  wrongs = length(result[result==T])
  cat("steps: ",step,"\n")
  cat("corrects: ",corrects,"\n")
  cat("wrongs: ",wrongs,"\n")
  cat("accuracy: ",corrects/length(y_pred),"\n")
}

print <- function(testname, step, corrects, wrongs, y_pred) {
  cat("Running", testname, "Tests.\n")
  cat("steps: ",step,"\n")
  cat("corrects: ",corrects,"\n")
  cat("wrongs: ",wrongs,"\n")
  cat("accuracy: ",corrects/length(y_pred),"\n")
}

heart <- function(path){
  data <- as.matrix(read.table(path))
  
  index <- seq(1,nrow(data)*0.2)
  X_test <- cbind(1,scale(data[index,1:ncol(data)-1],center=F))
  y_test <- as.matrix(data[index,ncol(data)])
  X_train <- cbind(1,scale(data[-index,1:ncol(data)-1],center=F))
  y_train <- as.matrix(data[-index,ncol(data)])
  
  theta <- as.matrix(rep(0,ncol(data)))
  
  alpha <- 0.3
  tol <- 1e-6
  step <- 1
  while(T) {
    p_gradient <- gCost(theta,X_train,y_train)
    theta <- theta-alpha*p_gradient
    gradient <- gCost(theta,X_train,y_train)
    if(abs(norm(gradient,type="F")-norm(p_gradient,type="F"))<=tol) break
    step <- step+1
  }
  
  y_pred <- hypot(X_test%*%theta)
  result <- xor(as.vector(round(y_pred)),as.vector(y_test))
  corrects = length(result[result==F])
  wrongs = length(result[result==T])
  print("heart", step, corrects, wrongs, y_pred)
  
  theta
}

diabetes <- function(path){
  data <- as.matrix(read.table(path))
  
  index <- seq(1,nrow(data)*0.2)
  X_test <- cbind(1,scale(data[index,1:ncol(data)-1],center=F))
  y_test <- as.matrix(data[index,ncol(data)])
  X_train <- cbind(1,scale(data[-index,1:ncol(data)-1],center=F))
  y_train <- as.matrix(data[-index,ncol(data)])
  
  theta <- as.matrix(rep(0,ncol(data)))
  
  alpha <- 0.3
  tol <- 1e-6
  step <- 1
  while(T) {
    p_gradient <- gCost(theta,X_train,y_train)
    theta <- theta-alpha*p_gradient
    gradient <- gCost(theta,X_train,y_train)
    if(abs(norm(gradient,type="F")-norm(p_gradient,type="F"))<=tol) break
    step <- step+1
  }
  
  y_pred <- hypot(X_test%*%theta)
  result <- xor(as.vector(round(y_pred)),as.vector(y_test))
  corrects = length(result[result==F])
  wrongs = length(result[result==T])
  print("diabetes", step, corrects, wrongs, y_pred)
  
  theta
}

heart_model <- heart("/Users/jacksonisaac/Development/HDFC/python/heart_1L.txt")
diab_model <- diabetes("/Users/jacksonisaac/Development/HDFC/python/diab_1L.txt")