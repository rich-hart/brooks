from django.db import models
from shows.models import Show

class Video(models.Model):
    show = models.ForeignKey(
        Show, 
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    air_date = models.DateField()
    host = models.URLField()

