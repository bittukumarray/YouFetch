from django.urls import path
from .views import getVideos
from . import views
app_name = 'search'
urlpatterns = [
    path('', views.index, name='index'),
    path('get-videos/<int:page>',getVideos.as_view(), name="getVideo"),
    path('get-data/<int:page>', views.getData, name="getdata")
]
