#Set working directory
setwd("/Users/taomo/Documents/workspace/MLProject/MachineLearningProject/Rcode")

# Classification Tree with rpart
library(rpart)

#read data file
data = read.table('data.txt')

# grow tree 
fit <- rpart(V9 ~ .,
             method="class",data=data)

printcp(fit) # display the results 
plotcp(fit) # visualize cross-validation results 
summary(fit) # detailed summary of splits


# plot tree 
plot(fit, uniform=TRUE, 
     main="Classification Tree for Kyphosis")
text(fit, use.n=TRUE, all=TRUE, cex=.8)


