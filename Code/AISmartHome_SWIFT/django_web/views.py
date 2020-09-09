# -*- coding: utf-8 -*-
import json
import sys
import base64
import time
import requests
from django.shortcuts import render
from django.http import JsonResponse
import hashlib

URL = "http://api.xfyun.cn/v1/service/v1/iat"
APPID = "5c613028"
API_KEY = "a0108de414b143cd27290312b288103e"


def getHeader(aue, engineType):
    curTime = str(int(time.time()))
    param = "{\"aue\":\"" + aue + "\"" + ",\"engine_type\":\"" + engineType + "\"}"
    paramBase64 = str(base64.b64encode(param.encode('utf-8')), 'utf-8')
    m2 = hashlib.md5()
    m2.update((API_KEY + curTime + paramBase64).encode('utf-8'))
    checkSum = m2.hexdigest()
    header = {
        'X-CurTime': curTime,
        'X-Param': paramBase64,
        'X-Appid': APPID,
        'X-CheckSum': checkSum,
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    }
    return header


def getBody(filepath):
    binfile = open(filepath, 'rb')
    data = {'audio': base64.b64encode(binfile.read())}
    return data


aue = "raw"
engineType = "sms8k"
audioFilePath = r"../AISmartHome_SWIFT/django_web/pcm/test.wav"

# HomePage
def index(request):
    return render(request, 'index.html')

def getdata(request):
    device='515484674'       #设备ID
    apikey='ZZxwkh=B3YJ8BWFEQY2aCyHMcV4='          #APIKey

    url='http://api.heclouds.com/devices/%s/datastreams' % device

    print(url)

    headers={
        "api-key":apikey,
        }

    r=requests.get(url,headers=headers)
    res = json.loads(r.content)

    context  = {}
    context['data'] = res['data']
    print(r.content)

    return render(request, 'get.html', context)

def lighton(request):

    url = "http://api.heclouds.com/mqtt?topic=TurnipRobot"

    querystring = {"device_id":"515484674"}

    payload = "on"

    headers = {
        'api-key': "ZZxwkh=B3YJ8BWFEQY2aCyHMcV4=",
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    print(response.text)

    return render(request, 'index.html')

def lightoff(request):
    
    url = "http://api.heclouds.com/mqtt?topic=TurnipRobot"

    querystring = {"device_id":"515484674"}

    payload = "off"

    headers = {
        'api-key': "ZZxwkh=B3YJ8BWFEQY2aCyHMcV4=",
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    print(response.text)
    
    return render(request, 'index.html')

def upload(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    audioData = request.FILES.get('audioData')
    with open('../AISmartHome_SWIFT/django_web/pcm/test.wav', 'wb') as file:
        file.write(audioData.read())
        file.close()
    result = ""
    try:
        r = requests.post(URL, headers=getHeader(aue, engineType), data=getBody(audioFilePath))
        result = r.content.decode('utf-8')
    except Exception as e:
        return JsonResponse({'status':'Failed,Please try again'})  

    print(result)

    json_obj={}
    message=""
    print(result)
    try:
        json_obj=json.loads(result)
        message = json_obj['data']
    except Exception as e:
        print(e)

    print(json_obj)
    
    if("开" in message or "开灯" in message):
        lighton(request)
        return JsonResponse({'status':'lighton'})
    elif("关" in message or "关灯" in message):
        lightoff(request)
        return JsonResponse({'status':'lightoff'})
    elif("数据" in message or "获取信息" in message):
        getdata(request)
        return JsonResponse({'status':'getdata'})
    else:
        print(message)
        return JsonResponse({'status':'Failed'})

    return JsonResponse({'foo':'bar'})