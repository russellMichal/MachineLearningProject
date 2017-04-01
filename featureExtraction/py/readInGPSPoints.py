# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 22:45:52 2017

@author: rkm87
"""

#reads in the data from .csv files and returns a 2d array of the data
def readInGPSPoints(places):
    #return [[40.112030,-88.226770,0],[40.104610,-88.226150,0]]
    radius = {}
    
    #add the data to the array
    temp,maxDist = readFile("..\\files\\initial_data\\cpmi.csv",places,placeName="nuclear lab")
    array = temp
    if(maxDist!=None):
        radius.update(maxDist)
   
    #add the data to the array
    temp,maxDist = readFile("..\\files\\initial_data\\talbot_lab.csv",places, placeName="talbot")
    array += temp
    if(maxDist!=None):
        radius.update(maxDist)
    
    #add the data to the array
    temp,maxDist = readFile("..\\files\\initial_data\\no_anomalies.csv",places, hasAnomalies=False)
    array += temp
    if(maxDist!=None):
        radius.update(maxDist) 
    
    #add the data to the array
    temp,maxDist = readFile("..\\files\\initial_data\\alma.csv",places, placeName="Alma Mater")
    array += temp
    if(maxDist!=None):
        radius.update(maxDist) 
    
    #add the data to the array
    temp,maxDist = readFile("..\\files\\initial_data\\wesley_church.csv",places, placeName="wesley church")
    array += temp
    if(maxDist!=None):
        radius.update(maxDist) 
     
    return array,radius

def readFile( fileName,places, hasAnomalies = True, placeName = "no place"):
    
    #add the data to the array
    file = open(fileName,"r")
    lines = file.readlines()
    fileArray = readToArray(lines, hasAnomalies) 
    print(hasAnomalies)
    print(placeName)
    #look to see if this place is a radiation spot
    #if it is then add the radius of the spot to the dict
    for place in places:
        if(place[0] == placeName):
            return fileArray, {place[0]:findMaxDistance(place, fileArray)}
        
    return fileArray,None
            
#takes the data file and returns a 2d array of the data
#data is the data file
#anomalies is a bool that sets the label to 0 or 1
#returns a 2d array of the data
def readToArray(data, anomalies):
    arr = []
    
    for i in range(1,len(data)):
        
        #break out if we get enough data
        if(i==561): break;
          
        arr.append([]); 
        end = data[i].find(',')
        end = data[i].find(',', end)+1;
                  
        for j in range(1,4):
            start = data[i].find(',', end)+1;
            end = data[i].find(',', start);
    
            arr[i-1].append(data[i][start:end]);

        if(anomalies):
            arr[i-1].append(1)
        else:
            arr[i-1].append(0)

    print("array length: "+str(len(arr)))
    return arr

#finds the max distance between the plac and all the data members
#@parm place: the place emitting radiation
#@parm data: the data to be compared to the place to find the furthest data member
def findMaxDistance( place, data ):
    maxdist = -1
    
    for dataMember in data:
        dist = distance(dataMember[0],dataMember[1],place[1],place[2])
        if(dist>maxdist):
            maxdist = dist

    return maxdist
        
#returns the distance between (x1, y1) and (x2,y2)
def distance(x1,y1,x2,y2):
    import math
    x = pow((float(x2)-float(x1)),2)
    y = pow((float(y2)-float(y1)),2)
    return math.sqrt(x+y)
        