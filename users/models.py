from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
#        unique=True,
    )
    about = models.TextField(max_length=1024)
#    picture

