# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from readInInitData import readInInitData
from readInGPSPoints import readInGPSPoints
from computeBinaryFeatures import computeBinaryFeatures
#this function reads a gpx file from https://waypointer.info/ and creats 
#a 2d array with the name of the landmark at [x][0] and the lat and log at 
#[x][1] [x][2] where x is a monument. there are x monuments totle
def main():
    initData = readInInitData();
    points = readInGPSPoints();#not made yet
    featureVector = computeBinaryFeatures(points, initData,0.00010);
    #exporteToFile();#not made yet dont know if we need this one
                            

main()