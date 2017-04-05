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
    temp,maxDist = readFile("..\\files\\initial_data\\belltower.csv",places, placeName="bell tower")
    array += temp
    if(maxDist!=None):
        radius.update(maxDist)
    
    #add the data to the array
    temp,maxDist = readFile("..\\files\\initial_data\\alma.csv",places, placeName="alma")
    array += temp
    if(maxDist!=None):
        radius.update(maxDist) 
    
    #add the data to the array
    temp,maxDist = readFile("..\\files\\initial_data\\wesley_church.csv",places, placeName="wesley church")
    array += temp
    if(maxDist!=None):
        radius.update(maxDist) 
    
    #after finding the distance form monuments that emit radiation find the avg and use that as the distance to monuments that do not emit radaition    
    #people dont go by these points... set distance to a large number for now.
    avgDist = 0.005#getAvgDist(radius)
        
    #add the data to the array
    temp,maxDist = readFile("..\\files\\initial_data\\no_anomalies.csv",places, hasAnomalies=False, avgDistance = avgDist)
    array += temp
    if(maxDist!=None):
        radius.update(maxDist) 
        
    #add the data to the array
    temp,maxDist = readFile("..\\files\\initial_data\\morrow_plots.csv",places,hasAnomalies=False, placeName="morrow_plots", avgDistance = avgDist)
    array += temp
    if(maxDist!=None):
        radius.update(maxDist)
        
    #add the data to the array
    temp,maxDist = readFile("..\\files\\initial_data\\monument_on_engr_quad.csv",places,hasAnomalies=False, placeName="monument_on_engr_quad",avgDistance = avgDist)
    array += temp
    if(maxDist!=None):
        radius.update(maxDist)
        
    #add the data to the array
    temp,maxDist = readFile("..\\files\\initial_data\\cemetery.csv",places, hasAnomalies=False,placeName="cemetery",avgDistance = avgDist)
    array += temp
    if(maxDist!=None):
        radius.update(maxDist)      
     
    print("radius"+str(radius))
    return array,radius

#reads the file
#@parm fileName: then path to the file to read
#@parm places: the places to compare the distance against
#@parm hasAnomalies: T/F value that dettermines the label
#@parm placeName: the name of the place that is close to the points
def readFile( fileName,places, hasAnomalies = True, placeName = "no place",avgDistance = 0):
    
    #add the data to the array
    file = open(fileName,"r")
    lines = file.readlines()
    fileArray = readToArray(lines, hasAnomalies) 

    #look to see if this place is a radiation spot
    #if it is then add the radius of the spot to the dict
    for place in places:
        if(place[0] == placeName and hasAnomalies):
            return fileArray, {place[0]:findMaxDistance(place, fileArray)}
        
        elif (not(hasAnomalies) and placeName!="no place"):
            return fileArray,{placeName:avgDistance}
        
    return fileArray,None
            
#takes the data file and returns a 2d array of the data
#data is the data file
#anomalies is a bool that sets the label to 0 or 1
#returns a 2d array of the data
def readToArray(data, anomalies):
    from weather import addDate
    
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

        #adds unique datas to a global list so we know how many api calls to make
        addDate(arr[i-1][2])
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
            #for debuging we should not get this big of a distance
            if(dist>1):
                print(dataMember)
                print(place)
                print(dist)
            maxdist = dist

    return maxdist
      
def getAvgDist(d):
    retval = 0
    
    for key, value in d.items():
        retval+=value
        
    retval/=len(d)
    return retval
#returns the distance between (x1, y1) and (x2,y2)
def distance(x1,y1,x2,y2):
    import math
    x = pow((float(x2)-float(x1)),2)
    y = pow((float(y2)-float(y1)),2)
    return math.sqrt(x+y)
        