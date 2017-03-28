# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 22:52:36 2017

@author: rkm87
"""

from weather import setWeatherFeature
from weather import addDate
from weather import computeDayWeather
#this site will convert lat to a distance in feet/miles
#http://www.somebits.com/weblog/tech/latitude-longitude-distance-approximations.html

#the startingPoints is going to data read from micheals database, it will be in the format
#lat, log, label
#dataList is the list of features we have read in from readInInitData
#bound is how far away a feature place can be and still get counted as close
def computeBinaryFeatures(startingPoints, dataList,bound):
    retvec = []
    print(len(startingPoints))
    for i in range(0,len(startingPoints)):
        retvec.append([])
        
        for place in dataList:

            #print(place)
            #print(startingPoints[i][0])
            #print(startingPoints[i][1])
                
            if(float(startingPoints[i][0])>float(place[1])-bound and 
               float(startingPoints[i][0])<float(place[1])+bound and
               float(startingPoints[i][1])>float(place[2])-bound and 
               float(startingPoints[i][1])<float(place[2])+bound):
                retvec[i].append(1)
            else:
                retvec[i].append(0)
    
            addDate(startingPoints[i][2])
            
    print("running api calls on all dates")
    d = computeDayWeather(startingPoints[i][0],startingPoints[i][1])
    for i in range(0,len(startingPoints)): 
        
        
        retvec[i].append(setWeatherFeature(startingPoints[i][2],d))
        retvec[i].append(startingPoints[i][len(startingPoints[i])-1])

    return retvec