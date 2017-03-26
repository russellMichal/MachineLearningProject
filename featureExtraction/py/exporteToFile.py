# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 22:45:52 2017

@author: rkm87
"""

#exportes the features to a file
#features is the list of features extracted by the program
#it is in the formate: (x1,x2,...,xn,y) where y is the label and the xs are the features
def exporteToFile(features):
    file = open("data.txt","w")
    for i in range(0,len(features)):
        file.write(str(features[i]))
        file.write("\n")
        
    file.close()