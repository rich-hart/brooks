from django.db import models
from django.contrib.auth.models import User
from os.path import join
from django.conf import settings

class Profile(models.Model):
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
#        unique=True,
    )
    about = models.TextField(max_length=1024)
    image = models.FileField(upload_to=settings.MEDIA_ROOT)
#    picture

