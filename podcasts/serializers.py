from .models import Podcast, Show
from rest_framework import serializers


class PodcastSerializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='podcast-highlight', format='html')
    class Meta:
        model = Podcast
        fields = (
            'url',
            'show',
            'title',
            'air_date', 
            'host',
            'highlight',
        )


