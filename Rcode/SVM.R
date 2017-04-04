# Load the data from the csv file
#Set working directory
setwd("/Users/taomo/Documents/workspace/MLProject/MachineLearningProject/Rcode")

#read data file
data = read.table('data.txt')

#convert data to numerical
dataNum <- matrix(data = NA, nrow = dim(data)[1], ncol = dim(data)[2])
for (i in 1:dim(data)[2]) {
       dataNum[,i] <- c(as.numeric(data[[i]]))-1}


#using package e1071
library(e1071)

# Create a linear regression model
model <- svm(V9 ~ ., data = dataNum)

summary(model)

