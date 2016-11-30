from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
class Donation(models.Model):
    owner = models.Forieng(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
#        unique=True,
    )
