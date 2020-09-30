from django.shortcuts import render
import threading
import os
import requests
from .models import Video
from datetime import datetime
from pyrfc3339 import generate, parse
from datetime import datetime
import pytz
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from collections import OrderedDict
from django.http import HttpResponse, JsonResponse
from background_task import background
# Create your views here.

@background(schedule=10)
def dataFetcher():
    print("yes")
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    timestamp-=10000
    dt_object = datetime.fromtimestamp(timestamp)
    publishedAfterDate=generate(dt_object.replace(tzinfo=pytz.utc))
    maxResults=100000
    q="cricket"
    apiKey="AIzaSyB-8rBWOv1G61zFB79z0cmQ1qknLtjzkqw"
    url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&order=date&type=video'
    full_url=url+"&maxResults="+str(maxResults)+"&q="+str(q)+"&publishedAfter="+publishedAfterDate+"&key="+apiKey
    rqstData = requests.get(full_url)
    rqstDataJson=rqstData.json()
    for data in rqstDataJson["items"]:
        try:
            dataObj = Video.objects.create(videoId=data["id"]["videoId"], title=data["snippet"]["title"], description=data["snippet"]["description"],publishedDate=data["snippet"]["publishedAt"], thumb_default_url=data["snippet"]["thumbnails"]["default"]["url"], thumb_high_url=data["snippet"]["thumbnails"]["high"]["url"], thumb_medium_url=data["snippet"]["thumbnails"]["medium"]["url"])
            dataObj.save()
        except:
            pass


def index(request):
    return render(request, "search/index.html",)


class getVideos(APIView):
    def get(self, request, page):
        result=[]
        
        data = Video.objects.filter().order_by('-publishedDate')[25*page:25*page+25]
        for eachData in data:
            dictData={
                "title":eachData.title,
                "video_url":"https://www.youtube.com/embed/"+eachData.videoId,
                "description":eachData.description,
                "publishedDate":eachData.publishedDate,
                "thumb_default_url":eachData.thumb_default_url,
                "thumb_medium_url":eachData.thumb_medium_url,
                "thumb_high_url":eachData.thumb_high_url,
            }
            result.append(dictData)
        return Response({"data":result})

def getData(request, page):
    data = Video.objects.filter().order_by('-publishedDate')[25*page:25*page+25]
    result=[]
    for eachData in data:
        dictData={
            "title":eachData.title,
            "video_url":"https://www.youtube.com/embed/"+eachData.videoId,
            "description":eachData.description,
            "publishedDate":eachData.publishedDate,
            "thumb_default_url":eachData.thumb_default_url,
            "thumb_medium_url":eachData.thumb_medium_url,
            "thumb_high_url":eachData.thumb_high_url,
        }
        result.append(dictData)
    return render(request, "search/ui.html", {"data":result})
