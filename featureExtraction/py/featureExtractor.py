# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from readInInitData import readInInitData
from readInGPSPoints import readInGPSPoints
from computeBinaryFeatures import computeBinaryFeatures
from exporteToFile import exporteToFile

def main():
    initData = readInInitData();
    points = readInGPSPoints();#not made yet
    
    #http://www.somebits.com/weblog/tech/latitude-longitude-distance-approximations.html
    #.0001 ~ 36 feet
    featureVector = computeBinaryFeatures(points, initData,0.00010);
    
    for i in range(0,len(featureVector)):
        print(featureVector[i])
     
    exporteToFile(featureVector);
                            

main()