from django.shortcuts import render
import requests
from .models import Video
from datetime import datetime
from pyrfc3339 import generate, parse
from datetime import datetime
import pytz
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from background_task import background


# Create your views here.

@background(schedule=10)
def dataFetcher():
    print("fetching...")
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    timestamp-=10000
    dt_object = datetime.fromtimestamp(timestamp)
    publishedAfterDate=generate(dt_object.replace(tzinfo=pytz.utc))
    maxResults=100000
    q="cricket"
    apiKey="AIzaSyD1qMTlkWaB-GlsJMuhFVgQ27CeFK92oi0"
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
        page-=1
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

def getData(request):
    data = Video.objects.all().order_by('-publishedDate')
    result=[]
    page = request.GET.get('page', 1)

    paginator = Paginator(data, 10)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
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
    return render(request, "search/ui.html", {"result":result, "data":data})
