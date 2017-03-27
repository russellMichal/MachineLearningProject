# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 22:45:52 2017

@author: rkm87
"""

#reads in the data from .csv files and returns a 2d array of the data
def readInGPSPoints():
    #return [[40.112030,-88.226770,0],[40.104610,-88.226150,0]]

    file = open("..\\no_anomalies.csv","r")
    lines = file.readlines()
    array = readToArray(lines, False)
    
    file = open("..\\anomalies.csv","r")
    lines = file.readlines()
    array = array + readToArray(lines, True) 
    
    #print(array[78270]) 
    return array

#takes the data file and returns a 2d array of the data
#data is the data file
#anomalies is a bool that sets the label to 0 or 1
#returns a 2d array of the data
def readToArray(data, anomalies):
    arr = []
    
    for i in range(1,len(data)):
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

    print(len(arr))
    return arr