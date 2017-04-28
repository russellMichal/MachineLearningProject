# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 22:52:36 2017

@author: rkm87
"""

from weather import setWeatherFeature
from weather import computeDayWeather
from readInGPSPoints import distance
from readInGPSPoints import getAvgGcPerDay
import numpy as np
#this site says that the 5th decimal of the lat = 1.1m
#http://gizmodo.com/how-precise-is-one-degree-of-longitude-or-latitude-1631241162

#the startingPoints is going to data read from micheals database, it will be in the format
#lat, log, label
#dataList is the list of features we have read in from readInInitData
#bound is how far away a feature place can be and still get counted as close
def computeBinaryFeatures(startingPoints, dataList,bounds,placeProperties):
    retvec = []
    
    #print("running api calls on all dates")
    #d = computeDayWeather(startingPoints[i][0],startingPoints[i][1])
    
    #get the avg daily gc for the data based weather feature
    avgDailyGC = getAvgGcPerDay()
    #print(str(avgDailyGC))

    print("total array length: "+str(len(startingPoints)))
    for i in range(0,len(startingPoints)):
        #retvec.append([])
        properties=np.zeros(len(placeProperties),dtype = np.int8)
                
        for place in dataList:
            dist = distance(startingPoints[i][0],startingPoints[i][1],place[1],place[2])

            if(place[0] in bounds.keys() and dist<=bounds[place[0]]):
                for j in range(0,len(placeProperties)):
                    for placeProp in place[3].split(","):
                        if(placeProperties[j] == placeProp):
                            properties[j]=1
                

        retvec.append(properties.tolist().copy());

        #add weather feature based of date
        if(avgDailyGC[getDate(startingPoints[i][2])]>=40):
            retvec[i].append(1)
        else:
            retvec[i].append(0)
            
        #retvec[i].append(setWeatherFeature(startingPoints[i][2],d))
        retvec[i].append(startingPoints[i][len(startingPoints[i])-1])
        #addDate(startingPoints[i][2])
            
    #print("running api calls on all dates")
    #d = computeDayWeather(startingPoints[i][0],startingPoints[i][1])
    #for i in range(0,len(startingPoints)): 
        
        
        #retvec[i].append(setWeatherFeature(startingPoints[i][2],d))
        #retvec[i].append(startingPoints[i][len(startingPoints[i])-1])

    return retvec

#takes the full date/time and returns just the date part
def getDate(dateTime):
    dateTimeList = dateTime.split()
    date = dateTimeList[0]
    
    return date