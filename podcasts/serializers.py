from .models import Podcast, Show
from rest_framework import serializers


class PodcastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Podcast
        fields = (
            'url',
            'show',
            'episode', 
            'title',
            'air_date', 
#            'description',
            'host',
        )


