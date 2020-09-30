from django.shortcuts import render
import threading
import os
import requests
from .models import Video
from datetime import datetime
from pyrfc3339 import generate, parse
from datetime import datetime
import pytz
# Create your views here.


def index(request):
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    timestamp-=10000
    dt_object = datetime.fromtimestamp(timestamp)
    publishedAfterDate=generate(dt_object.replace(tzinfo=pytz.utc))
    maxResults=10
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

    # print(rqstDataJson)
    return render(request, "search/index.html",)
