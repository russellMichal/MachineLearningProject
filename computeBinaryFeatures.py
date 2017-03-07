# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 22:52:36 2017

@author: rkm87
"""

#the startingPoints is going to data read from micheals database, it will be in the format
#lat, log, label
#dataList is the list of features we have read in from readInInitData
#bound is how far away a feature place can be and still get counted as close
def computeBinaryFeatures(startingPoints, dataList,bound):
    retvec = []
        
    for place in dataList:
        if(startingPoints[0]>float(place[1])-bound and startingPoints[1]<float(place[2])+bound):
            retvec.append(1)
        else:
            retvec.append(0)

    retvec.append(startingPoints[len(startingPoints)-1])

    return retvec