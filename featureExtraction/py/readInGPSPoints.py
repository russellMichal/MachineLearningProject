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
    temp,maxDist = readFile("..\\files\\initial_data\\radiationPoints\\cpmi.csv",places,placeName="nuclear lab")
    array = temp
    if(maxDist!=None):
        radius.update(maxDist)
   
#    #add the data to the array
#    temp,maxDist = readFile("..\\files\\initial_data\\radiationPoints\\talbot_lab.csv",places, placeName="talbot")
#    array += temp
#    if(maxDist!=None):
#        radius.update(maxDist)
        
#    #add the data to the array
#    temp,maxDist = readFile("..\\files\\initial_data\\radiationPoints\\belltower.csv",places, placeName="bell tower")
#    array += temp
#    if(maxDist!=None):
#        radius.update(maxDist)
    
    #add the data to the array
    temp,maxDist = readFile("..\\files\\initial_data\\radiationPoints\\alma.csv",places, placeName="alma")
    array += temp
    if(maxDist!=None):
        radius.update(maxDist) 
    
    #add the data to the array
    temp,maxDist = readFile("..\\files\\initial_data\\noRadiationPoints\\wesley_church.csv",places, placeName="wesley church")
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
    temp,maxDist = readFile("..\\files\\initial_data\\noRadiationPoints\\morrow_plots.csv",places,hasAnomalies=False, placeName="morrow_plots", avgDistance = avgDist)
    array += temp
    if(maxDist!=None):
        radius.update(maxDist)
        
    #add the data to the array
    temp,maxDist = readFile("..\\files\\initial_data\\noRadiationPoints\\monument_on_engr_quad.csv",places,hasAnomalies=False, placeName="monument_on_engr_quad",avgDistance = avgDist)
    array += temp
    if(maxDist!=None):
        radius.update(maxDist)
        
    #add the data to the array
    temp,maxDist = readFile("..\\files\\initial_data\\noRadiationPoints\\cemetery.csv",places, hasAnomalies=False,placeName="cemetery",avgDistance = avgDist)
    array += temp
    if(maxDist!=None):
        radius.update(maxDist)
        
#    #add the data to the array
#    temp,maxDist = readFile("..\\files\\initial_data\\noRadiationPoints\\arc.csv",places, hasAnomalies=False,placeName="ARC",avgDistance = avgDist)
#    array += temp
#    if(maxDist!=None):
#        radius.update(maxDist)
        
    #add the data to the array
    temp,maxDist = readFile("..\\files\\initial_data\\noRadiationPoints\\Townsend Hall.csv",places, hasAnomalies=False,placeName="Townsend Hall",avgDistance = avgDist)
    array += temp
    if(maxDist!=None):
        radius.update(maxDist)
        
    #add the data to the array
    temp,maxDist = readFile("..\\files\\initial_data\\noRadiationPoints\\grainger.csv",places, hasAnomalies=False,placeName="Grainger",avgDistance = avgDist)
    array += temp
    if(maxDist!=None):
        radius.update(maxDist)
        
#    #add positive points that are not near monuments but are positive because of weather
#    #add the data to the array
#    temp,maxDist = readFile("..\\files\\initial_data\\WeatherPoints\\01_18_2017.csv",places, hasAnomalies=True, avgDistance = avgDist)
#    array += temp
#    if(maxDist!=None):
#        radius.update(maxDist) 
     
    #add the data to the array
    temp,maxDist = readFile("..\\files\\initial_data\\WeatherPoints\\01_25_2017.csv",places, hasAnomalies=True, avgDistance = avgDist)
    array += temp
    if(maxDist!=None):
        radius.update(maxDist) 

    #add the data to the array
    temp,maxDist = readFile("..\\files\\initial_data\\WeatherPoints\\01_28_2017.csv",places, hasAnomalies=True, avgDistance = avgDist)
    array += temp
    if(maxDist!=None):
        radius.update(maxDist) 
        
    #add the data to the array
    temp,maxDist = readFile("..\\files\\initial_data\\WeatherPoints\\01_31_2017.csv",places, hasAnomalies=True, avgDistance = avgDist)
    array += temp
    if(maxDist!=None):
        radius.update(maxDist) 
        
    #add the data to the array
    temp,maxDist = readFile("..\\files\\initial_data\\WeatherPoints\\02_01_2017.csv",places, hasAnomalies=True, avgDistance = avgDist)
    array += temp
    if(maxDist!=None):
        radius.update(maxDist) 
        
    #add the data to the array
    temp,maxDist = readFile("..\\files\\initial_data\\WeatherPoints\\02_13_2017.csv",places, hasAnomalies=True, avgDistance = avgDist)
    array += temp
    if(maxDist!=None):
        radius.update(maxDist) 
        
    #add the data to the array
    temp,maxDist = readFile("..\\files\\initial_data\\WeatherPoints\\03_05_2017.csv",places, hasAnomalies=True, avgDistance = avgDist)
    array += temp
    if(maxDist!=None):
        radius.update(maxDist) 
        
    #add the data to the array
    temp,maxDist = readFile("..\\files\\initial_data\\WeatherPoints\\03_09_2017.csv",places, hasAnomalies=True, avgDistance = avgDist)
    array += temp
    if(maxDist!=None):
        radius.update(maxDist) 
        
    #add the data to the array
    temp,maxDist = readFile("..\\files\\initial_data\\WeatherPoints\\03_13_2017.csv",places, hasAnomalies=True, avgDistance = avgDist)
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











#this function should probably be in its own file but it uses a lot of the methods in this file to read the .csv file so it is here for now
#this function reads the file that holds the avg gc pre day if the gc for the day is >40 we say there is weather on this day
#>40 may change it was just a guess by micheal
def getAvgGcPerDay():
    avgGcPerDay = {};
    days,maxDist = readFile("..\\files\\initial_data\\avg_daily_gc.csv",['filler1','filler2'], hasAnomalies=False, avgDistance = 0.0)
    for day in days:
        gc = day[1]
        date = day[2]
        avgGcPerDay.update({date:float(gc)});
                          
    if(float(gc)>40):
        print (avgGcPerDay)
    
    return avgGcPerDay
                    
        
        