#Set working directory
setwd("/Users/taomo/Documents/workspace/MLProject/MachineLearningProject/Rcode")

#read data file
data = read.table('data.txt')

# Random Forest prediction of Kyphosis data
library(randomForest)
fit <- randomForest(V9 ~ .,   data=data)
print(fit) # view results 
importance(fit) # importance of each predictor
