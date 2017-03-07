# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#this function reads a gpx file from https://waypointer.info/ and creats 
#a 2d array with the name of the landmark at [x][0] and the lat and log at 
#[x][1] [x][2] where x is a monument. there are x monuments totle
def main():
    monuments = readInMonumentData();
    points = readInGPSPoints();#not made yet
    computeBinaryFeatures();#not made yet
    exporteToFile();#not made yet dont know if we need this one
                            
 def readInMonumentData():
    f= open("points.gpx","r");
    fileLines = f.readlines();
    skipping = True;
    i=0;
    arr = [];
    arr.append([])
        
    for line in fileLines:
        if(line.strip() != "</metadata>" and skipping):
            continue;
            
        skipping=False;
        
        if(line.strip() == "</metadata>"):
            continue;    
            
        print(line.strip())
        arr.append([]);
        if("<wpt" in line.strip()):
            start = line.strip().find('"')+1;
            end = line.strip().find('"', start);

            arr[i].append(line.strip()[start:end]);

            start = line.strip().find('"', end+1)+1;
            end = line.strip().find('"', start);

            arr[i].append(line.strip()[start:end]);
        
        if("<desc" in line.strip()):   
            start = line.strip().find('>')+1;
            end = line.strip().find('<', start);

            arr[i].insert(0,line.strip()[start:end]);
        i+=1;
        
    return arr;
main()