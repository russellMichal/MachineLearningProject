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
    points,radiuses = readInGPSPoints(initData);

    #this site says that the 5th decimal of the lat = 1.1m
    #http://gizmodo.com/how-precise-is-one-degree-of-longitude-or-latitude-1631241162
    featureArray = computeBinaryFeatures(points, initData,radiuses);
     
    exporteToFile(featureArray);                      

main()