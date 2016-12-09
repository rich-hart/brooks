from django.db import models
from django.contrib.auth.models import User
from os.path import join
from django.conf import settings

class Profile(models.Model):
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    profession = models.CharField(max_length=255)
    about = models.TextField(max_length=1024)
    image = models.FileField(upload_to=settings.MEDIA_ROOT)
    facebook = models.URLField(null=True)
    instagram = models.URLField(null=True)
    snapchat = models.URLField(null=True)
    pinterest = models.URLField(null=True)
    twitter = models.URLField(null=True)
    linkedin = models.URLField(null=True)
    

class Testimonial(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        unique=False,
    )
    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_related",
    )
    quote = models.TextField(max_length=1024)

