#Set working directory
setwd("/Users/taomo/Documents/workspace/MLProject/MachineLearningProject/Rcode")

# Classification Tree with rpart
library(rpart)

#read data file
data = read.table('data.txt')

# grow tree 
fit <- rpart(V9 ~ .,method="class",data=data)

printcp(fit) # display the results 
plotcp(fit) # visualize cross-validation results 
summary(fit) # detailed summary of splits


# plot tree 
plot(fit, uniform=TRUE, 
     main="Classification Tree for Kyphosis")
text(fit, use.n=TRUE, all=TRUE, cex=.8)


#Cross Validation
require(caret)
flds <- createFolds(data$V9, k = 10, list = TRUE, returnTrain = FALSE)

for (i in 1:10){
  testData <- data[flds[[i]], ]
  trainData <- data[-flds[[i]],]
  fit <- rpart(V9 ~ .,   method="class", data=trainData)
  pre <- predict(fit,testData,type="class")
  print(confusionMatrix(pre,testData$V9))
}

