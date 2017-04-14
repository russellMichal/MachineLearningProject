rm(list=ls(all=TRUE))

#using package e1071
library(e1071)

#read data file
data = read.table('data.txt')

model <- naiveBayes(V10 ~ .,   data=data)

pred <- predict(model, data[,-1])
table(pred, data$V10)

#Cross Validation
require(caret)
flds <- createFolds(data$V10, k = 10, list = TRUE, returnTrain = FALSE)

for (i in 1:10){
  testData <- data[flds[[i]], ]
  trainData <- data[-flds[[i]],]
  fit <- naiveBayes(V10 ~ .,   data=trainData)
  pre <- predict(fit,testData)
  print(confusionMatrix(pre,testData$V10))
}

