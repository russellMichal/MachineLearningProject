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
    points = readInGPSPoints();
    
    #http://www.somebits.com/weblog/tech/latitude-longitude-distance-approximations.html
    #.0001 ~ 36 feet
    featureArray = computeBinaryFeatures(points, initData,0.00010);
     
    exporteToFile(featureArray);
                            

main()