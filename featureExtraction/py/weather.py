# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 10:01:47 2017

@author: rkm87
"""
import requests
#weather under ground key:
#f083252c5baea2f5

#lat =40.109880
#long =-88.228320
#dateTime = "2/6/2017  2:37:00 PM"
#setWeatherFeature(lat, long, dateTime)
dates = []
def computeDayWeather(lat, long):
    data={}
    print(len(dates))
    for i in range(0,len(dates)):
        
        dateList = dates[i].split("/")        
        YYYY = dateList[2]
        MM = dateList[0].zfill(2)
        DD = dateList[1].zfill(2)
    
        print(YYYY+MM+DD)
        r = requests.get("http://api.wunderground.com/api/f083252c5baea2f5/history_"+YYYY+MM+DD+"/q/IL/Urbana.json") 
        data.update({dates[i]:r.json()})
        r.close()
    
        #to save api calls for now the state and city are hard coded to IL and Urbana
        #r = requests.get("http://api.wunderground.com/api/f083252c5baea2f5/geolookup/q/"+str(lat)+","+str(long)+".json")
        #data = r.json()
        #r.close()
        
        #print( data['location']['state'])
        #print( data['location']['city'])
        
        
        #r = requests.get("http://api.wunderground.com/api/f083252c5baea2f5/history_"+YYYY+MM+DD+"/q/"+data['location']["state"]+"/"+data['location']["city"]+"/.json")
    print(data.keys())
    return data

def setWeatherFeature( dateTime, data ):
    YYYY,MM,DD,hour,minute = formateInput(dateTime)
    

    
    #print(len(data[MM+"/"+DD+"/"+YYYY]['history']['observations']))
    #print(data.keys())

    for i in range(0,len(data[MM+"/"+DD+"/"+YYYY]['history']['observations'])):

        #note: the minute range might need to be changed
        minIntoDay = int(data[MM+"/"+DD+"/"+YYYY]['history']['observations'][i]['date']['hour'])*60+int(data[MM+"/"+DD+"/"+YYYY]['history']['observations'][i]['date']['min'])
        
        if( minIntoDay>=int(minute)+int(hour)*60-30 and
            minIntoDay<=int(minute)+int(hour)*60+30):
            
            #print(i)
            #print(data['history']['observations'][i]['fog'])
            #print(data['history']['observations'][i]['rain'])
            #print(data['history']['observations'][i]['snow'])
            #print(data['history']['observations'][i]['hail'])
            
            #note: I think this is all the precipation, might need to change
            if(#data[MM+"/"+DD+"/"+YYYY]['history']['observations'][i]['fog']=="2" or
               #data[MM+"/"+DD+"/"+YYYY]['history']['observations'][i]['rain']=="1" or
               #data[MM+"/"+DD+"/"+YYYY]['history']['observations'][i]['snow']=="1" or
               #data[MM+"/"+DD+"/"+YYYY]['history']['observations'][i]['hail']=="1"
               data[MM+"/"+DD+"/"+YYYY]['history']['observations'][i]['precipi']!="-9999.00" and
               data[MM+"/"+DD+"/"+YYYY]['history']['observations'][i]['precipi']!="0.00"    ):
                return 1
            
            else:
                return 0 
            
    #should not happen
    x=int(int(minute)+int(hour)*60)
    print(x)
    print(dateTime)
    for i in range(0,len(data[MM+"/"+DD+"/"+YYYY]['history']['observations'])):
        minIntoDay = int(data[MM+"/"+DD+"/"+YYYY]['history']['observations'][i]['date']['hour'])*60+int(data[MM+"/"+DD+"/"+YYYY]['history']['observations'][i]['date']['min'])
        print(str(i)+" "+data[MM+"/"+DD+"/"+YYYY]['history']['observations'][i]['date']['pretty'])
        print(minIntoDay)
            
    #print("FAIL")
    
    #for i in range(0,len(data[MM+"/"+DD+"/"+YYYY]['history']['observations'])):
        #print(str(i)+" "+data[MM+"/"+DD+"/"+YYYY]['history']['observations'][i]['date']['pretty'])

def formateInput(dateTime):
    dateTimeList = dateTime.split()
    date = dateTimeList[0]
    time = dateTimeList[1]
    
    #print(dateTime)
    #print(date)
    #print(time)
    
    dateList = date.split("/")        
    YYYY = dateList[2]
    MM = dateList[0].zfill(2)
    DD = dateList[1].zfill(2)
    
    #print(YYYY)
    #print(MM)
    #print(DD)
    
    timeList = time.split(":")
    hour = timeList[0].zfill(2)
    minute = timeList[1]
    #amOrPm = dateTimeList[2]
    
    #if(amOrPm == "PM"):
        #hour = int(hour)+12
        #hour = str(hour)
    #print(hour)
    #print(minute)
    #print(amOrPm)
    
    return YYYY,MM,DD,hour,minute

def addDate(dateTime):
    dateTimeList = dateTime.split()
    
    dateL = dateTimeList[0]    
    dateList = dateL.split("/")

    date = dateList[0].zfill(2)+"/"+dateList[1].zfill(2)+"/"+dateList[2]
    
    global dates
    addDateToList = True
    for i in range(0,len(dates)):
        if(date in dates[i]):
            addDateToList = False
        
    if(addDateToList):
        print("adding date")
        print(date)
        dates.append(date)