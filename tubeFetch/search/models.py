from django.db import models

# Create your models here.
class Video(models.Model):
    videoId = models.CharField(max_length=255, primary_key=True, unique=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=10000)
    publishedDate = models.CharField(max_length=100)
    thumb_default_url = models.URLField()
    thumb_medium_url = models.URLField()
    thumb_high_url = models.URLField()

    def __str__(self):
        return self.title