#Set working directory
setwd("/Users/taomo/Documents/workspace/MLProject/MachineLearningProject/Rcode")

#read data file
data = read.table('data.txt')

# Random Forest prediction of Kyphosis data
library(randomForest)
fit <- randomForest(V9 ~ .,   data=data)
print(fit) # view results 
importance(fit) # importance of each predictor

#Cross Validation
require(caret)
flds <- createFolds(data$V9, k = 10, list = TRUE, returnTrain = FALSE)

for (i in 1:10){
  testData <- data[flds[[i]], ]
  trainData <- data[-flds[[i]],]
  fit <- randomForest(V9 ~ .,   data=trainData)
  pre <- predict(fit,testData)
  print(confusionMatrix(pre,testData$V9))
}


