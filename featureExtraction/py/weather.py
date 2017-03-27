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

def setWeatherFeature(lat, long, dateTime):
    YYYY,MM,DD,hour,minute = formateInput(dateTime)
    
    #to save api calls for now the state and city are hard coded to IL and Urbana
    #r = requests.get("http://api.wunderground.com/api/f083252c5baea2f5/geolookup/q/"+str(lat)+","+str(long)+".json")
    #data = r.json()
    #r.close()
    
    #print( data['location']['state'])
    #print( data['location']['city'])
    
    
    #r = requests.get("http://api.wunderground.com/api/f083252c5baea2f5/history_"+YYYY+MM+DD+"/q/"+data['location']["state"]+"/"+data['location']["city"]+"/.json")
    r = requests.get("http://api.wunderground.com/api/f083252c5baea2f5/history_"+YYYY+MM+DD+"/q/IL/Urbana.json") 
    data = r.json()
    r.close()
    
    print(len(data['history']['observations']))
    
    for i in range(0,len(data['history']['observations'])):
        
        #note: the minute range might need to be changed
        if(data['history']['observations'][i]['date']['hour']==hour and
           int(data['history']['observations'][i]['date']['min'])>int(minute)-30 and
           int(data['history']['observations'][i]['date']['min'])<int(minute)+30):
            
            #print(i)
            #print(data['history']['observations'][i]['fog'])
            #print(data['history']['observations'][i]['rain'])
            #print(data['history']['observations'][i]['snow'])
            #print(data['history']['observations'][i]['hail'])
            
            #note: I think this is all the precipation, might need to change
            if(data['history']['observations'][i]['fog']=="1" or
               data['history']['observations'][i]['rain']=="1" or
               data['history']['observations'][i]['snow']=="1" or
               data['history']['observations'][i]['hail']=="1"):
                return 1
            else:
                return 0
    
    #for i in range(0,len(data['history']['observations'])):
    #    print(str(i)+" "+data['history']['observations'][i]['date']['pretty'])

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
    hour = timeList[0]
    minute = timeList[1]
    amOrPm = dateTimeList[2]
    
    if(amOrPm == "PM"):
        hour = int(hour)+12
        hour = str(hour)
    #print(hour)
    #print(minute)
    #print(amOrPm)
    
    return YYYY,MM,DD,hour,minute