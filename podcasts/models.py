from django.db import models
from shows.models import Show

class Podcast(models.Model):
    show = models.ForeignKey(
        Show, 
        on_delete=models.CASCADE,
    )
    episode = models.IntegerField()
    title = models.CharField(max_length=255)
    air_date = models.DateField()
    description = models.TextField()
    host = models.URLField()





