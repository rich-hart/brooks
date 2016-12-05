from .models import Video
from rest_framework import serializers

# FIXME: Fix podcasts and videos with media (singluar medium). 
# choose from podcasts, videos, blog?.
class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = (
            'show',
            'title',
            'air_date', 
            'host',
        )


