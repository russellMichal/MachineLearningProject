rm(list=ls(all=TRUE))

library(RSNNS)

#Set working directory
setwd("/Users/taomo/Documents/workspace/MLProject/MachineLearningProject/Rcode")

#read data file
data = read.table('data.txt')

#convert data to numerical
dataNum <- matrix(data = NA, nrow = dim(data)[1], ncol = dim(data)[2])
for (i in 1:dim(data)[2]) {
  dataNum[,i] <- c(as.numeric(data[[i]]))-1}

dataValues <- dataNum[,1:9]
dataTargets <- decodeClassLabels(dataNum[,10])
#irisTargets <- decodeClassLabels(iris[,5], valTrue=0.9, valFalse=0.1)

dataSplit <- splitForTrainingAndTest(dataValues, dataTargets, ratio=0.15)

model <- mlp(dataSplit$inputsTrain, dataSplit$targetsTrain, size=5, learnFuncParams=c(0.1), 
             maxit=50, inputsTest=dataSplit$inputsTest, targetsTest=dataSplit$targetsTest)

summary(model)
model
weightMatrix(model)
extractNetInfo(model)

par(mfrow=c(2,2))
plotIterativeError(model)

predictions <- predict(model,dataSplit$inputsTest)

plotRegressionError(predictions[,2], dataSplit$targetsTest[,2])

confusionMatrix(dataSplit$targetsTrain,fitted.values(model))
confusionMatrix(dataSplit$targetsTest,predictions)

plotROC(fitted.values(model)[,2], dataSplit$targetsTrain[,2])
plotROC(predictions[,2], dataSplit$targetsTest[,2])

#confusion matrix with 402040-method
confusionMatrix(dataSplit$targetsTrain, encodeClassLabels(fitted.values(model),
                                                     method="402040", l=0.4, h=0.6))

