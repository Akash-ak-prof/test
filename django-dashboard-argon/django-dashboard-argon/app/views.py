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


    List_Lat = [Lat1,Lat2,Lat3,Lat4,Lat5]
    List_Long = [Long1,Long2,Long3,Long4,Long5]
    List_Date = [date1 ,date2,date3,date4,date5]
    List_Time = [time1,time2,time3,time4,time5]
    List_Distance = [Distance1,Distance2,Distance3,Distance4,Distance5]
    List_Speed = [Speed1,Speed2,Speed3,Speed4,Speed5]
    List_Draft = [Draft1,Draft2,Draft3,Draft4,Draft5]


    print("LOgggg---------------------",List_Lat[0])

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
