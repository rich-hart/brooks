from .models import Show
from rest_framework import serializers


class ShowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Show
        fields = (
            'name',
            'home',
            'logo', 
        )
