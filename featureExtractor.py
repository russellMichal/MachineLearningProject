# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from readInInitData import readInInitData
from readInGPSPoints import readInGPSPoints
from computeBinaryFeatures import computeBinaryFeatures

def main():
    initData = readInInitData();
    points = readInGPSPoints();#not made yet
    featureVector = computeBinaryFeatures(points, initData,0.00010);
    #exporteToFile();#not made yet dont know if we need this one
                            

main()