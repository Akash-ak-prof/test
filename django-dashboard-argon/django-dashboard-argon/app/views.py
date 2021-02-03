# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
import json
import sys

@login_required(login_url="/login/")
def form(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'profile.html' )
    return HttpResponse(html_template.render(context, request))
#
# def index(request):
#     context = {}
#
#     Vname = request.POST.get('Vesselnm', None)
#     context['Vname'] = Vname
#
#     MsiId = request.POST.get('MsiId', None)
#     context['MsiId'] = MsiId
#
#     return render(request, 'index.html', context)


def index(request):
    context = {}

    Vname = request.POST.get('Vesselnm', None)
    context['Vname'] = Vname

    MsiId = request.POST.get('MsiId', None)
    context['MsiId'] = MsiId

    Status = request.POST.get('Status', None)
    context['Status'] = Status

    SOG = request.POST.get('SOG', None)
    context['SOG'] = SOG

    vesselType = request.POST.get('VesselType', None)
    context['vesselType'] = vesselType


    Lat1 = request.POST.get('Lat1', None)
    context['Lat1'] = Lat1

    Long1 = request.POST.get('Long1', None)
    context['Long1'] = Long1

    Lat2 = request.POST.get('Lat2', None)
    context['Lat2'] = Lat2

    Long2 = request.POST.get('Long2', None)
    context['Long2'] = Long2

    Lat3 = request.POST.get('Lat3', None)
    context['Lat3'] = Lat3

    Long3 = request.POST.get('Long3', None)
    context['Long3'] = Long3

    Lat4 = request.POST.get('Lat4', None)
    context['Lat4'] = Lat4

    Long4 = request.POST.get('Long4', None)
    context['Long4'] = Long4

    Lat5 = request.POST.get('Lat5', None)
    context['Lat5'] = Lat5

    Long5 = request.POST.get('Long5', None)
    context['Long5'] = Long5


    date1 = request.POST.get('Tdate1', None)
    context['date1'] = date1

    time1 = request.POST.get('Ttime1', None)
    context['time1'] = time1

    date2 = request.POST.get('Tdate2', None)
    context['date2'] = date2

    time2 = request.POST.get('Ttime2', None)
    context['time2'] = time2

    date3 = request.POST.get('Tdate3', None)
    context['date3'] = date3

    time3 = request.POST.get('Ttime3', None)
    context['time3'] = time3

    date4 = request.POST.get('Tdate4', None)
    context['date4'] = date4

    time4 = request.POST.get('Ttime4', None)
    context['time4'] = time4

    date5 = request.POST.get('Tdate5', None)
    context['date5'] = date5

    time5 = request.POST.get('Ttime5', None)
    context['time5'] = time5


    Distance1 = request.POST.get('Distance1', None)
    context['Distance1'] = Distance1

    Speed1 = request.POST.get('Speed1', None)
    context['Speed1'] = Speed1

    Distance2 = request.POST.get('Distance2', None)
    context['Distance2'] = Distance2

    Speed2 = request.POST.get('Speed2', None)
    context['Speed2'] = Speed2

    Distance3 = request.POST.get('Distance3', None)
    context['Distance3'] = Distance3

    Speed3 = request.POST.get('Speed3', None)
    context['Speed3'] = Speed3

    Distance4 = request.POST.get('Distance4', None)
    context['Distance4'] = Distance4

    Speed4 = request.POST.get('Speed4', None)
    context['Speed4'] = Speed4

    Distance5 = request.POST.get('Distance5', None)
    context['Distance5'] = Distance5

    Speed5 = request.POST.get('Speed5', None)
    context['Speed5'] = Speed5


    Draft1 = request.POST.get('Draft1', None)
    context['Draft1'] = Draft1

    Draft2 = request.POST.get('Draft2', None)
    context['Draft2'] = Draft2

    Draft3 = request.POST.get('Draft3', None)
    context['Draft3'] = Draft3

    Draft4 = request.POST.get('Draft4', None)
    context['Draft4'] = Draft4

    Draft5 = request.POST.get('Draft5', None)
    context['Draft5'] = Draft5

    q1=date1.split('-')
    dat1=q1[2]+'-'+q1[1]+'-'+q1[0]
    q2=date2.split('-')
    dat2=q2[2]+'-'+q2[1]+'-'+q2[0]
    q3=date3.split('-')
    dat3=q3[2]+'-'+q3[1]+'-'+q3[0]
    q4=date4.split('-')
    dat4=q4[2]+'-'+q4[1]+'-'+q4[0]
    q5=date5.split('-')
    dat5=q5[2]+'-'+q5[1]+'-'+q5[0]


    distport = [int(Distance1),int(Distance2),int(Distance3),int(Distance4),int(Distance5)]
    maxspeed = [18,18,18,18,18]
    dwt = [int(Draft1),int(Draft2),int(Draft3),int(Draft4),int(Draft5)]


    ################################################################################################

    id=[int(MsiId),int(MsiId),int(MsiId),int(MsiId),int(MsiId)]
    time=[dat1+" "+time1, dat2+" "+time2, dat3+" "+time3, dat4+" "+time4, dat5+" "+time5]
    vtype=[int(vesselType),int(vesselType),int(vesselType),int(vesselType),int(vesselType)]
    lon=[float(Long1),float(Long2), float(Long3), float(Long4),float(Long5)]
    lat = [float(Lat1),float(Lat2),float(Lat3),float(Lat4),float(Lat5)]


    import datetime
    import pandas as pd
    def tlap(n):
      a= time[n-1]
      b=time[n]
      t1=a.split()
      t2=b.split()

      td1=t1[0].split('-')
      td2=t2[0].split('-')
      tt1=t1[1].split(':')
      tt2=t2[1].split(':')

      a1=[]
      a2=[]

      ti1= datetime.datetime(int(td1[2]),int(td1[1]),int(td1[0]),int(tt1[0]),int(tt1[1]),0)
      ti2= datetime.datetime(int(td2[2]),int(td2[1]),int(td2[0]),int(tt2[0]),int(tt2[1]),0)

      c = ti2-ti1
    
      minutes = c.total_seconds() / 60

      return minutes

    n=5

    new_data = []
    count=0
    rate=0
    for i in range(1,5):
      #if(id[i]==id[i-1]):
        count=count+1
        t=tlap(i)
        #tdiffout[i-1]=t/60
        x=abs(lon[i]-lon[i-1])
        #lndiff.append(x)
        y=abs(lat[i]-lat[i-1])
        #ltdiff.append()
        #z=(speed[i-1]+speed[i])/2
        rate=1
        date=time[i].split()[0]
        tim= int (time[i].split()[1].split(':')[0])
        #print(t)
        if (dwt[i]==dwt[i-1]):
          dwtdif=0
        else:
          dwtdif=1

        if (t!=0):

          #dic={}
          #dic[id[i]]=rate

          new_list = []
          new_list.append(id[i])
          #new_list.append(date)
          #new_list.append(tim)
          new_list.append(t)
          new_list.append(vtype[i])
          new_list.append(x)
          new_list.append(y)
          #new_list.append(z)
          new_list.append(rate)
          new_list.append(1)
          #new_list.append(lon[i-1])
          #new_list.append(lon[i])
          #new_list.append(lat[i-1])
          #new_list.append(lat[i])
          new_list.append((maxspeed[i]*18)/5)
          new_list.append(dwtdif)
          new_list.append(distport[i-1])
          new_list.append(distport[i])

          new_data.append(new_list)
      #else:
       # count=0

    testdata = pd.DataFrame(new_data,columns=['ID','timediff','type','lon','lat','rate','SD','spmax','dwtdiff','d1','d2'])

    td=testdata['timediff']
    lndiff=testdata['lon']
    ltdiff=testdata['lat']
    spmax=testdata['spmax']
    dwtdiff=testdata['dwtdiff']
    d1=testdata['d1']
    d2=testdata['d2']

    #dwtdiff

    for i in range(0,len(new_data)):
      a=[]
      for j in range(0,4):
        a.append(new_data[j][1])

      b=max(a)
      a.remove(b)
      total=sum(a)
      mean = total / len(a) 
      variance = sum([((x - mean) ** 2) for x in a]) / len(a) 
      res = variance ** 0.5
      new_data[i][5]=mean
      new_data[i][6]=res

    inactivity=[]
    for i in range (0,4):
      if (new_data[i][1]<60):
        inactivity.append(0)

      else:  
        if (new_data[i][1]>new_data[i][5]+new_data[i][6]):
          if (new_data[i][1]>1440):
            inactivity.append(2)
          else:
            inactivity.append(1)

        else:
          inactivity.append(0)

    import numpy as np
    import pandas as pd

    import tensorflow as tf

    from tensorflow import feature_column
    import keras
    from tensorflow.keras import layers
    from sklearn.model_selection import train_test_split
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense

    from keras.models import load_model
    new_model = keras.models.load_model('DL_model.h5')
    print(new_model.summary())

    tout=[time[1],time[2],time[3],time[4]]
    #tdiffout=[0,0,0,0]
    dp=[]
    sus=[]
    typsus=[]
    conf=[]
    for i in range (0,4):
      if (inactivity[i]==0):
        dp.append(0)
        sus.append(0)
        typsus.append(0)
        conf.append(101)


      if (inactivity[i]==2):
        dp.append(1)
        sus.append(1)
        typsus.append(1)
        conf.append(101)
        #print('1')

      if (inactivity[i]==1):
        #print('here')
        dp.append(1)
        a=[td[i]/60,lndiff[i],ltdiff[i],spmax[i],dwtdiff[i],d1[i],d2[i]]
        new_output=new_model.predict([a])
        label=np.argmax(new_output,axis=1)
        su=label[0]

        #print(su)

        if (su==0):
          if (dwtdiff[i]==0):
            susi=0
            typsusi=0
            confi=101
          else:
            su=1
        if (su==1):
          susi=1
          typsusi=1
          if (dwtdiff[i]>0):
            confi=0.9
          else:
            confi=101



        if (su==2):
          susi=1
          typsusi=2
          confi=1-path/dis


        sus.append(susi)
        typsus.append(typsusi) 
        conf.append(confi)
      #print(conf)
      #print(conf)

    print ('timestamp,timediff, dark, sus, type of sus,conf')
    for i in range (0,4):
      print(tout[i],td[i],dp[i],sus[i],typsus[i],conf[i])

    
    context['sus1']=  sus[0];
    context['sus2'] = sus[1];
    context['sus3'] = sus[2];
    context['sus4'] = sus[3];

    context['time1']=  tout[0];
    context['time2'] = tout[1];
    context['time3'] = tout[2];
    context['time4'] = tout[3];

    context['dark1']=  dp[0];
    context['dark2'] = dp[1];
    context['dark3'] = dp[2];
    context['dark4'] = dp[3];

    context['typsus1'] = typsus[0];
    context['typsus2'] = typsus[1];
    context['typsus3'] = typsus[2];
    context['typsus4'] = typsus[3];

    context['conf1'] = conf[0];
    context['conf2'] = conf[1];
    context['conf3'] = conf[2];
    context['conf4'] = conf[3];

    context['td1'] = td[0];
    context['td2'] = td[1];
    context['td3'] = td[2];
    context['td4'] = td[3];

    #################################################################################################

    #print("LOgggg---------------------",List_Lat[0])

    dictionary = {
        "VesselName": Vname,
        "MMsiId": MsiId,
        "VesselType":vesselType,
        "Status": Status,
        "SOG": SOG,

        "Lat1": Lat1,
        "Long1": Long1,
        "Lat2": Lat2,
        "Long2": Long2,
        "Lat3": Lat3,
        "Long3": Long3,
        "Lat4": Lat4,
        "Long4": Long4,
        "Lat5": Lat5,
        "Long5": Long5,

        "Date1":date1,
        "Time1":time1,
        "Date2": date2,
        "Time2": time2,
        "Date3": date3,
        "Time3": time3,
        "Date4": date4,
        "Time4": time4,
        "Date5": date5,
        "Time5": time5,

        "Distance1":Distance1,
        "Speed1":Speed1,
        "Distance2": Distance2,
        "Speed2": Speed2,
        "Distance3": Distance3,
        "Speed3": Speed3,
        "Distance4": Distance4,
        "Speed4": Speed4,
        "Distance5": Distance5,
        "Speed5": Speed5,

        "Draft1": Draft1,
        "Draft2": Draft2,
        "Draft3": Draft3,
        "Draft4": Draft4,
        "Draft5": Draft5
    }
    print("hello", flush=True)
    with open("sample.json", "w") as outfile:
        json.dump(dictionary, outfile)

    return render(request, 'index.html', context)

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))


def extract(request):
    context = {}
    # Opening JSON file
    with open('sample.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)

    Vname = json_object["VesselName"]
    context['Vname'] = Vname

    MsiId = json_object["MMsiId"]
    context['MsiId'] = MsiId

    Status = json_object["Status"]
    context['Status'] = Status

    SOG = json_object["SOG"]
    context['SOG'] = SOG

    vesselType = json_object["VesselType"]
    context['vesselType'] = vesselType

    Lat1 = json_object["Lat1"]
    context['Lat1'] = Lat1

    Long1 = json_object["Long1"]
    context['Long1'] = Long1

    Lat2 = json_object["Lat2"]
    context['Lat2'] = Lat2

    Long2 =  json_object["Long2"]
    context['Long2'] = Long2

    Lat3 = json_object["Lat3"]
    context['Lat3'] = Lat3

    Long3 =  json_object["Long3"]
    context['Long3'] = Long3

    Lat4 =json_object["Lat4"]
    context['Lat4'] = Lat4

    Long4 = json_object["Long4"]
    context['Long4'] = Long4

    Lat5 = json_object["Lat5"]
    context['Lat5'] = Lat5

    Long5 = json_object["Long5"]
    context['Long5'] = Long5

    date1 = json_object["Date1"]
    context['date1'] = date1

    time1 = json_object["Time1"]
    context['time1'] = time1

    date2 =json_object["Date2"]
    context['date2'] = date2

    time2 = json_object["Time2"]
    context['time2'] = time2

    date3 = json_object["Date3"]
    context['date3'] = date3

    time3 = json_object["Time3"]
    context['time3'] = time3

    date4 = json_object["Date4"]
    context['date4'] = date4

    time4 = json_object["Time4"]
    context['time4'] = time4

    date5 = json_object["Date5"]
    context['date5'] = date5

    time5 = json_object["Time5"]
    context['time5'] = time5

    Distance1 =  json_object["Distance1"]
    context['Distance1'] = Distance1

    Speed1 = json_object["Speed2"]
    context['Speed1'] = Speed1

    Distance2 = json_object["Distance2"]
    context['Distance2'] = Distance2

    Speed2 = json_object["Speed3"]
    context['Speed2'] = Speed2

    Distance3 = json_object["Distance3"]
    context['Distance3'] = Distance3

    Speed3 = json_object["Speed3"]
    context['Speed3'] = Speed3

    Distance4 = json_object["Distance4"]
    context['Distance4'] = Distance4

    Speed4 = json_object["Speed4"]
    context['Speed4'] = Speed4

    Distance5 = json_object["Distance5"]
    context['Distance5'] = Distance5

    Speed5 = json_object["Speed5"]
    context['Speed5'] = Speed5

    Draft1 = json_object["Draft1"]
    context['Draft1'] = Draft1

    Draft2 = json_object["Draft2"]
    context['Draft2'] = Draft2

    Draft3 = json_object["Draft3"]
    context['Draft3'] = Draft3

    Draft4 = json_object["Draft4"]
    context['Draft4'] = Draft4

    Draft5 = json_object["Draft5"]
    context['Draft5'] = Draft5

    print(json_object, flush=True)
    print("Distance",json_object["VesselName"], flush=True)
    return render(request,'index.html',context)
    # return render(request, 'index.html', context)
    #
