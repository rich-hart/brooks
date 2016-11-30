from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = (
           'about',
           'image',
        )

class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = (
           'username',
           'first_name',
           'last_name', 
           'email', 
#           'groups',
           'profile',
        )

