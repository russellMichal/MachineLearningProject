# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def main():
    f= open("points.gpx","r");
    fileLines = f.readlines();
    skipping = True;
    i=0;
    arr = []
    arr.append([])
        
    for line in fileLines:
        if(line.strip() != "</metadata>" and skipping):
            continue;
            
        skipping=False;
        
        if(line.strip() == "</metadata>"):
            continue;    
            
        print(line.strip())
        arr.append([])
        if("<wpt" in line.strip()):
            start = line.strip().find('"')+1;
            end = line.strip().find('"', start)

            arr[i].append(line.strip()[start:end]);

            start = line.strip().find('"', end+1)+1;
            end = line.strip().find('"', start)

            arr[i].append(line.strip()[start:end]);
        
        if("<desc" in line.strip()):   
            start = line.strip().find('>')+1;
            end = line.strip().find('<', start)

            arr[i].insert(0,line.strip()[start:end]);
        i+=1;
main()